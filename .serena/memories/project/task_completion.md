# What to Do When a Task is Completed

1. No automated linting/formatting/testing pipeline exists
2. Manual verification:
   - Ensure .env variables are documented if new ones are added
   - Test with `run_multi_react.py` using eval dataset
3. Check that any new tools are registered in TOOL_MAP (react_agent.py)
4. Verify GPU compatibility if modifying inference pipeline
