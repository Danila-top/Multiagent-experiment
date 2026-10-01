# Integrated Agent 001 — Agent + Memory + Tools + ML

This experiment combines four capabilities in one reproducible local system:

1. **Agent loop** — plans and executes a task.
2. **Persistent memory** — stores and retrieves prior observations.
3. **Tools** — exposes explicit, inspectable tool calls.
4. **ML policy** — predicts whether independent verification should be required.

## Experiment

Task: compute a simple arithmetic result using a registered tool.

The agent:

1. reads relevant memory;
2. estimates task characteristics;
3. asks the ML policy whether verification is required;
4. calls the arithmetic tool;
5. passes the result to an independent verifier;
6. records the outcome in memory.

## Important boundary

The ML model is not an intelligence test. It is a small deterministic routing component whose job is only to choose a verification policy from numeric task features.

## Success criteria

- all four components participate;
- the tool call is observable;
- the result is independently verified;
- the run is written to persistent memory;
- the full test suite passes.
