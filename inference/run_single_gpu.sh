#!/bin/bash
# Single-GPU vLLM launch script for RTX 3090 (24GB VRAM)
# Uses compressed-tensors 4-bit quantized model (auto-detected by vLLM)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$SCRIPT_DIR/../.env"

if [ -f "$ENV_FILE" ]; then
    echo "Loading environment variables from .env file..."
    set -a
    source "$ENV_FILE"
    set +a
fi

MODEL_PATH="${LLM_LOCAL_PATH:-$HOME/models/Tongyi-DeepResearch-30B-A3B-AWQ-4bit}"
PORT="${VLLM_PORT:-6001}"
MAX_MODEL_LEN="${MAX_MODEL_LEN:-65536}"
GPU_MEM_UTIL="${GPU_MEM_UTIL:-0.92}"
KV_CACHE_DTYPE="${KV_CACHE_DTYPE:-fp8}"

# CUDA toolkit for flashinfer FP8 kernel JIT compilation
export CUDA_HOME="${CUDA_HOME:-/usr/local/cuda-12.8}"
export PATH="$CUDA_HOME/bin:$PATH"

# GPU pre-flight check (skip vLLM check since we're about to start it)
echo "Running GPU pre-flight check..."
python "$SCRIPT_DIR/gpu_preflight.py" --no-vllm-check
if [ $? -ne 0 ]; then
    echo "Pre-flight check failed. Aborting vLLM launch."
    exit 1
fi

echo "Starting vLLM server..."
echo "  Model: $MODEL_PATH"
echo "  Port: $PORT"
echo "  Max model length: $MAX_MODEL_LEN"
echo "  GPU memory utilization: $GPU_MEM_UTIL"
echo "  KV cache dtype: $KV_CACHE_DTYPE"

python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --port "$PORT" \
    --gpu-memory-utilization "$GPU_MEM_UTIL" \
    --max-model-len "$MAX_MODEL_LEN" \
    --kv-cache-dtype "$KV_CACHE_DTYPE" \
    --enforce-eager \
    --tensor-parallel-size 1 \
    --trust-remote-code \
    --served-model-name "$MODEL_PATH"
