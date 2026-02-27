# agente-tonyi — Project Overview

## Purpose
Motor de decisión agéntica (agentic decision engine) based on Tongyi-DeepResearch-30B-A3B.
Takes a question, researches the web via a ReAct loop (think → tool_call → observation × N), and returns a direct answer.

## Tech Stack
- **Language**: Python 3.10+
- **LLM Inference**: vLLM or llama.cpp (local GPU inference, RTX 3090 24GB+)
- **Web Search**: SearXNG (self-hosted, Docker container)
- **Browser Automation**: Selenium (headless Chrome) for page reading
- **LLM Client**: OpenAI-compatible API (via vLLM server)
- **Dependencies**: torch, vllm, transformers, openai, selenium, pdfminer, pdfplumber, fastapi, pydantic, litellm, dashscope, qwen-agent
- **Environment**: .env file with python-dotenv

## Architecture Pattern
ReAct Agent Loop:
```
Question → [think → tool_call → observation] × N (up to 50 rounds) → <answer>
```

## Key Components
- `inference/react_agent.py` — Core ReAct agent (`MultiTurnReactAgent` class)
- `inference/run_multi_react.py` — Entry point / orchestrator (CLI with argparse)
- `inference/prompt.py` — System prompts (SYSTEM_PROMPT, AGENT_SYSTEM_PROMPT, EXTRACTOR_PROMPT)
- `inference/gpu_preflight.py` — GPU validation before inference
- `inference/tool_search.py` — Web search tool (SearXNG)
- `inference/tool_visit.py` — Page reader (Selenium + LLM extraction)
- `inference/tool_scholar.py` — Academic search (Google Scholar via SearXNG)
- `inference/tool_file.py` — File parser (PDF, DOCX, etc.)
- `inference/searxng_adapter.py` — SearXNG API adapter
- `inference/selenium_adapter.py` — Headless browser adapter
- `inference/file_tools/` — File parsing utilities (video_agent, idp, video_analysis, file_parser, utils)

## Distilled From
Tonyi-DeepResearch-Trinidad (18+ lab sessions)
