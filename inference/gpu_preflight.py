"""GPU pre-flight check for DeepResearch inference pipeline.

Validates GPU state, kills parasitic VRAM consumers, checks service health,
and estimates maximum context length before launching inference.

Usage:
    python gpu_preflight.py                  # Full check
    python gpu_preflight.py --no-vllm-check  # Skip vLLM health (before vLLM start)
    python gpu_preflight.py --dry-run        # Report only, don't kill anything
"""

import argparse
import os
import signal
import subprocess
import sys
import time

import requests

PREFIX = "[PREFLIGHT]"

KNOWN_PARASITES = {
    "rustdesk": "signal",
    "ollama": "systemctl",
}

# VRAM estimation constants (MiB)
VRAM_MODEL_MIB = 17300
VRAM_OVERHEAD_MIB = 1024
VRAM_PER_1K_CONTEXT_MIB = 110


class PreflightError(Exception):
    pass


def log(msg):
    print(f"{PREFIX} {msg}")


def get_gpu_state():
    """Query GPU memory via nvidia-smi. Returns dict with total/used/free in MiB."""
    result = subprocess.run(
        [
            "nvidia-smi",
            "--query-gpu=memory.total,memory.used,memory.free",
            "--format=csv,noheader,nounits",
        ],
        capture_output=True,
        text=True,
        timeout=10,
    )
    if result.returncode != 0:
        raise PreflightError(f"nvidia-smi failed: {result.stderr.strip()}")

    line = result.stdout.strip().split("\n")[0]
    total, used, free = [int(x.strip()) for x in line.split(",")]
    return {"total": total, "used": used, "free": free}


def get_gpu_processes():
    """List processes using GPU VRAM. Returns list of dicts with pid/name/used_mib."""
    result = subprocess.run(
        [
            "nvidia-smi",
            "--query-compute-apps=pid,process_name,used_memory",
            "--format=csv,noheader,nounits",
        ],
        capture_output=True,
        text=True,
        timeout=10,
    )
    if result.returncode != 0:
        raise PreflightError(f"nvidia-smi process query failed: {result.stderr.strip()}")

    processes = []
    for line in result.stdout.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 3:
            try:
                processes.append({
                    "pid": int(parts[0]),
                    "name": parts[1],
                    "used_mib": int(parts[2]),
                })
            except ValueError:
                continue
    return processes


def kill_parasites(processes, dry_run=False):
    """Kill known parasitic processes. Returns list of killed process descriptions."""
    killed = []
    for proc in processes:
        proc_name = proc["name"].lower()
        for parasite, method in KNOWN_PARASITES.items():
            if parasite in proc_name:
                desc = f"{proc['name']} (PID {proc['pid']}, {proc['used_mib']} MiB)"
                if dry_run:
                    log(f"Would kill parasite: {desc}")
                    killed.append(desc)
                    continue

                if method == "signal":
                    try:
                        os.kill(proc["pid"], signal.SIGTERM)
                        time.sleep(1)
                        # Check if still alive
                        try:
                            os.kill(proc["pid"], 0)
                            os.kill(proc["pid"], signal.SIGKILL)
                            time.sleep(0.5)
                        except ProcessLookupError:
                            pass
                        log(f"Killed parasite: {desc}")
                        killed.append(desc)
                    except (ProcessLookupError, PermissionError) as e:
                        log(f"Failed to kill {desc}: {e}")

                elif method == "systemctl":
                    try:
                        subprocess.run(
                            ["systemctl", "stop", parasite],
                            capture_output=True,
                            timeout=10,
                        )
                        log(f"Stopped service: {desc}")
                        killed.append(desc)
                    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
                        log(f"Failed to stop {parasite}: {e}")
                break
    return killed


def estimate_max_context(free_vram_mib):
    """Estimate max context tokens from available VRAM after model load."""
    available_for_kv = free_vram_mib - VRAM_MODEL_MIB - VRAM_OVERHEAD_MIB
    if available_for_kv <= 0:
        return 0
    return int((available_for_kv / VRAM_PER_1K_CONTEXT_MIB) * 1000)


def check_vllm_health(port):
    """Check if vLLM is responding on the given port. Returns True if healthy."""
    try:
        resp = requests.get(f"http://127.0.0.1:{port}/v1/models", timeout=5)
        return resp.status_code == 200
    except (requests.ConnectionError, requests.Timeout):
        return False


def check_searxng_health():
    """Check SearXNG health. Attempts docker start if down. Returns True if healthy."""
    url = os.environ.get("SEARXNG_URL", "http://localhost:8080")
    try:
        resp = requests.get(f"{url}/healthz", timeout=5)
        if resp.status_code == 200:
            return True
    except (requests.ConnectionError, requests.Timeout):
        pass

    # Try to start the container
    log("SearXNG not responding, attempting docker start...")
    try:
        subprocess.run(
            ["docker", "start", "searxng"],
            capture_output=True,
            timeout=15,
        )
        time.sleep(3)
        resp = requests.get(f"{url}/healthz", timeout=5)
        return resp.status_code == 200
    except Exception:
        return False


def run_preflight(planning_ports=None, target_context_len=30720, skip_vllm=False, dry_run=False):
    """Run all pre-flight checks. Raises PreflightError on failure.

    Args:
        planning_ports: List of vLLM ports to check (default: [6001])
        target_context_len: Required context length in tokens
        skip_vllm: Skip vLLM health check (for pre-launch)
        dry_run: Don't kill anything, just report

    Returns:
        dict with gpu_state, killed_parasites, estimated_context, services
    """
    if planning_ports is None:
        planning_ports = [6001]

    log("=" * 40)
    log("  GPU Pre-flight Check")
    log("=" * 40)

    # Check 1: GPU state
    state = get_gpu_state()
    log(f"GPU: {state['used']}/{state['total']} MiB used ({state['free']} MiB free)")

    # Check 2: Find and kill parasites
    processes = get_gpu_processes()
    killed = kill_parasites(processes, dry_run=dry_run)

    # Re-check GPU after cleanup
    if killed and not dry_run:
        time.sleep(2)
        state = get_gpu_state()
        log(f"GPU after cleanup: {state['used']}/{state['total']} MiB used ({state['free']} MiB free)")

    # Check 3: vLLM health (moved before VRAM check)
    services = {}
    vllm_already_running = False
    if not skip_vllm:
        for port in planning_ports:
            healthy = check_vllm_health(port)
            services[f"vllm:{port}"] = healthy
            status = "OK" if healthy else "FAILED"
            log(f"vLLM port {port}: {status}")
            if healthy:
                vllm_already_running = True
            else:
                raise PreflightError(f"vLLM not responding on port {port}")
    else:
        log("vLLM check: SKIPPED (pre-launch mode)")

    # Check 4: VRAM sufficient for target context
    # Skip if vLLM is already running — VRAM is allocated by vLLM for the model
    if vllm_already_running:
        log(f"VRAM check: SKIPPED (vLLM already running with model loaded)")
        estimated_ctx = target_context_len
    else:
        estimated_ctx = estimate_max_context(state["free"])
        if estimated_ctx >= target_context_len:
            log(f"VRAM OK: estimated max context ~{estimated_ctx} >= target {target_context_len}")
        else:
            raise PreflightError(
                f"Insufficient VRAM: estimated max context ~{estimated_ctx} < target {target_context_len}. "
                f"Free: {state['free']} MiB, need ~{VRAM_MODEL_MIB + VRAM_OVERHEAD_MIB + (target_context_len // 1000) * VRAM_PER_1K_CONTEXT_MIB} MiB"
            )

    # Check 5: SearXNG health
    searxng_ok = check_searxng_health()
    services["searxng"] = searxng_ok
    status = "OK" if searxng_ok else "FAILED"
    log(f"SearXNG: {status}")
    if not searxng_ok:
        raise PreflightError("SearXNG not responding (tried docker start)")

    log("=" * 40)
    log("  ALL CHECKS PASSED")
    log("=" * 40)

    return {
        "gpu_state": state,
        "killed_parasites": killed,
        "estimated_context": estimated_ctx,
        "services": services,
    }


def post_flight(start_time):
    """Report final GPU state and session duration."""
    try:
        elapsed = time.time() - start_time
        hours, remainder = divmod(int(elapsed), 3600)
        minutes, seconds = divmod(remainder, 60)

        state = get_gpu_state()
        log("=" * 40)
        log("  Post-flight Report")
        log("=" * 40)
        log(f"GPU: {state['used']}/{state['total']} MiB used ({state['free']} MiB free)")
        log(f"Session duration: {hours}h {minutes}m {seconds}s")
        log("=" * 40)
    except Exception as e:
        log(f"Post-flight report failed: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GPU pre-flight check for DeepResearch")
    parser.add_argument("--no-vllm-check", action="store_true", help="Skip vLLM health check")
    parser.add_argument("--dry-run", action="store_true", help="Report only, don't kill parasites")
    parser.add_argument("--target-context", type=int, default=None, help="Target context length (default: MAX_MODEL_LEN or 30720)")
    parser.add_argument("--port", type=int, default=None, help="vLLM port (default: from VLLM_PORTS env or 6001)")
    args = parser.parse_args()

    target = args.target_context or int(os.environ.get("MAX_MODEL_LEN", "30720"))
    ports = [args.port] if args.port else list(map(int, os.environ.get("VLLM_PORTS", "6001").split(",")))

    try:
        run_preflight(
            planning_ports=ports,
            target_context_len=target,
            skip_vllm=args.no_vllm_check,
            dry_run=args.dry_run,
        )
    except PreflightError as e:
        log(f"FAILED: {e}")
        sys.exit(1)
