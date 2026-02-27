# Suggested Commands

## Setup
```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
cp .env.example .env
# Edit .env: set LLM_LOCAL_PATH, SUMMARY_MODEL_NAME
```

## Start Inference Server
```bash
# vLLM (fast, needs AWQ model)
bash inference/run_single_gpu.sh

# llama.cpp (slower, uses GGUF)
bash inference/run_llamacpp.sh
```

## Start SearXNG (required for web search)
```bash
docker start searxng
```

## Run Agent
```bash
cd inference && set -a && source ../.env && set +a
PYTHONUNBUFFERED=1 ../venv/bin/python3 run_multi_react.py \
  --dataset eval_data/test_agent_001.jsonl \
  --output ../output \
  --max_workers 1 --roll_out_count 1
```

## Testing
No formal test suite. Eval data in `inference/eval_data/test_agent_001.jsonl`.

## Linting/Formatting
No linting or formatting tools configured in the project.
