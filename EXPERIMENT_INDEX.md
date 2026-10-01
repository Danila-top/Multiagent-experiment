# Experiment index

## MA-001 — single-agent vs two-agent verification

**Goal:** compare a single agent performing a task with a two-agent workflow in which one agent performs the task and another independently checks the result.

**Variables**
- number of agents
- amount of shared context
- verification enabled/disabled

**Primary measurements**
- task success
- error count
- correction count
- total tool operations
- elapsed wall-clock time

---

## INT-001 — integrated agent stack

**Location:** `experiments/integrated-agent-001/`

This experiment is the first concrete integration of the ecosystem's four technical layers:

- **Agent:** task loop and orchestration;
- **Memory:** persistent JSON-backed context;
- **Tools:** explicit tool registry and calls;
- **ML:** deterministic verification-routing classifier.

### Run

The reference task is `17 + 25`.

Expected observable chain:

`memory retrieval -> ML policy -> tool call -> independent verification -> memory write`

### Success criteria

- output is `42`;
- the `add` tool is called explicitly;
- the ML policy requests verification for the first run;
- the independent verifier accepts the result;
- one observation is persisted;
- automated tests pass.

The experiment is intentionally small so failures can be attributed to a specific layer before increasing system complexity.
