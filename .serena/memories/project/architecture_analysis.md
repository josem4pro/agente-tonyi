# agente-tonyi — Architecture Analysis Summary

## Date: 2026-02-24
## Analysis: 3-layer (repo-mapper + Serena semantic + Aider tree-sitter)

## Architecture
- ReAct agent loop: think → tool_call → observation × N → answer
- Entry point: `inference/run_multi_react.py` (ThreadPoolExecutor, argparse)
- Core class: `MultiTurnReactAgent(FnCallAgent)` in `inference/react_agent.py`
- Tool dispatch: TOOL_MAP dict comprehension from TOOL_CLASS list
- 4 active tools: search, visit, google_scholar, parse_file
- 2 registered but unused: video_analysis, VideoAgent
- 1 disabled: PythonInterpreter (SandboxFusion dependency)

## Key Design Decisions
1. AGENT_MODE (concise, 50 rounds, 1500 tokens) >> REPORT_MODE (verbose, 30 rounds, 16384 tokens)
2. Triple budget guard: tokens + time + call count
3. Sticky port routing for vLLM (prevent context thrashing)
4. SearXNG self-hosted replaces paid Serper API
5. Selenium singleton with thread-safe lock for page reading

## Dependency Clusters
- Cluster 1 (Agent Core): run_multi_react → react_agent → prompt + gpu_preflight
- Cluster 2 (Web Tools): tool_search/tool_scholar → searxng_adapter; tool_visit → selenium_adapter
- Cluster 3 (File Tools): tool_file → file_parser → idp; video_agent → video_analysis; utils shared

## Technical Debt
- 3 TODOs in file_tools (audio, PDF headers, font analysis)
- 2 bare excepts in react_agent.py (lines 136, 213)
- No test suite, no linter, no CI/CD
- PythonInterpreter disabled (SandboxFusion unavailable)

## Stats
- 4,643 LOC total, 23 files, 191 dependencies (30 critical)
- GPU: RTX 3090 24GB, vLLM AWQ or llama.cpp GGUF
- Model: Tongyi-DeepResearch-30B-A3B (MoE, 3B active / 30B total)
