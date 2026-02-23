# agente-tonyi

Motor de decision agentica basado en Tongyi-DeepResearch-30B-A3B.

Le das una pregunta. Investiga la web. Te da una respuesta directa.

## Quick Start

```bash
# 1. Setup
python3 -m venv venv
./venv/bin/pip install -r requirements.txt

# 2. Copy and configure environment
cp .env.example .env
# Edit .env: set LLM_LOCAL_PATH, SUMMARY_MODEL_NAME

# 3. Start inference server (pick one)
bash inference/run_single_gpu.sh    # vLLM (fast, needs AWQ model)
bash inference/run_llamacpp.sh      # llama.cpp (slower, uses GGUF)

# 4. Start SearXNG (required for web search)
docker start searxng

# 5. Run
cd inference && set -a && source ../.env && set +a
PYTHONUNBUFFERED=1 ../venv/bin/python3 run_multi_react.py \
  --dataset eval_data/test_agent_001.jsonl \
  --output ../output \
  --max_workers 1 --roll_out_count 1
```

## How it works

ReAct loop: the model thinks, calls a tool (search/visit/scholar), reads the result, thinks again.
Repeats for up to 50 rounds until it has a confident answer.

```
Question → [think → tool_call → observation] × N → <answer>
```

## Requirements

- NVIDIA GPU with 24GB+ VRAM (tested on RTX 3090)
- Docker (for SearXNG)
- Chrome (for Selenium page reader)
- Python 3.10+

## Structure

```
inference/
  react_agent.py       # ReAct agent loop
  run_multi_react.py   # Entry point
  prompt.py            # System prompts (agent + report mode)
  gpu_preflight.py     # GPU validation
  tool_search.py       # SearXNG web search
  tool_visit.py        # Page reader (Selenium + LLM extraction)
  tool_scholar.py      # Google Scholar via SearXNG
  tool_file.py         # File parser (PDF, DOCX, etc.)
  searxng_adapter.py   # SearXNG API adapter
  selenium_adapter.py  # Headless browser adapter
  run_llamacpp.sh      # llama.cpp launcher
  run_single_gpu.sh    # vLLM launcher
  file_tools/          # File parsing utilities
  eval_data/           # Test datasets
```

## Origin

Distilled from [Tonyi-DeepResearch-Trinidad](https://github.com/josem4pro/Tonyi-DeepResearch-Trinidad)
after 18+ lab sessions. See [GENESIS.md](GENESIS.md) for the full story.
