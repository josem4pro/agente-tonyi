# Code Style & Conventions

## Language
- Python 3.10+, no type hints used consistently
- No docstrings convention enforced
- Script-style code in orchestrator (run_multi_react.py), class-based in agent (react_agent.py)

## Naming
- snake_case for functions, variables, files
- PascalCase for classes (e.g., MultiTurnReactAgent)
- UPPER_SNAKE_CASE for constants (e.g., SYSTEM_PROMPT, OBS_START, TOOL_MAP)

## Patterns
- Environment variables via python-dotenv (.env)
- OpenAI-compatible API client for LLM calls
- Tool dispatch via TOOL_MAP dictionary
- Concurrent execution with ThreadPoolExecutor
- argparse for CLI arguments
- JSONL for input datasets and output results

## File Organization
- All code in `inference/` directory (flat, no deep nesting)
- Sub-tools in `inference/file_tools/`
- Shell scripts for server launching
- Single .env for all configuration
