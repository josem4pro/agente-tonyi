#!/bin/bash
# llama.cpp server launch script for RTX 3090 (24GB VRAM)
# Tongyi-DeepResearch-30B-A3B GGUF Q4_K_M @ 131K context
# Expert offloading: 12 MoE layers to CPU, rest on GPU
#
# VRAM budget (~n-cpu-moe 8):
#   Model Q4_K_M:        18.63 GB
#   Offload 8 MoE:       -2.71 GB
#   KV cache 131K q8/q4: +4.88 GB
#   CUDA + FA + batch:   +1.80 GB
#   TOTAL:               ~22.6 GB (margin ~2.0 GB)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$SCRIPT_DIR/../.env"

if [ -f "$ENV_FILE" ]; then
    echo "Loading environment variables from .env..."
    set -a
    source "$ENV_FILE"
    set +a
fi

LLAMA_SERVER="${LLAMA_SERVER:-$HOME/llama.cpp/build/bin/llama-server}"
MODEL="${GGUF_MODEL_PATH:-$HOME/models/Alibaba-NLP_Tongyi-DeepResearch-30B-A3B-Q4_K_M.gguf}"
PORT="${VLLM_PORT:-6001}"
N_CPU_MOE="${N_CPU_MOE:-8}"

# Validate prerequisites
if [ ! -f "$LLAMA_SERVER" ]; then
    echo "ERROR: llama-server not found at $LLAMA_SERVER"
    echo "Build it: cd ~/llama.cpp && cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=86 && cmake --build build --config Release -j\$(nproc)"
    exit 1
fi

if [ ! -f "$MODEL" ]; then
    echo "ERROR: GGUF model not found at $MODEL"
    echo "Download: python3 -c \"from huggingface_hub import hf_hub_download; hf_hub_download('bartowski/Alibaba-NLP_Tongyi-DeepResearch-30B-A3B-GGUF', 'Alibaba-NLP_Tongyi-DeepResearch-30B-A3B-Q4_K_M.gguf', local_dir='$HOME/models')\""
    exit 1
fi

# Check GPU is free
GPU_USED=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null | head -1)
if [ -n "$GPU_USED" ] && [ "$GPU_USED" -gt 1000 ]; then
    echo "WARNING: GPU has ${GPU_USED} MiB in use. Kill vLLM first: pkill -f vllm"
    echo "Current GPU processes:"
    nvidia-smi --query-compute-apps=pid,name,used_memory --format=csv,noheader 2>/dev/null
    exit 1
fi

echo "Starting llama-server..."
echo "  Model: $MODEL"
echo "  Port: $PORT"
echo "  Context: 131072 tokens"
echo "  MoE layers offloaded to CPU: $N_CPU_MOE"
echo "  KV cache: K=q8_0, V=q4_0"
echo "  Flash attention: ON"

taskset -c 0-11 "$LLAMA_SERVER" \
    -m "$MODEL" \
    -c 131072 \
    --rope-scaling none \
    -ngl 48 \
    --n-cpu-moe "$N_CPU_MOE" \
    --cache-type-k q8_0 \
    --cache-type-v q4_0 \
    -fa on \
    -b 4096 \
    --ubatch-size 2048 \
    -t 6 \
    -tb 12 \
    --cpu-range 0-11 \
    --cpu-range-batch 0-11 \
    --cpu-strict 1 \
    --cpu-strict-batch 1 \
    --jinja \
    --chat-template chatml \
    --reasoning-format none \
    --mlock \
    --metrics \
    --perf \
    --host 0.0.0.0 \
    --port "$PORT"
