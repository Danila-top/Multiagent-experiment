"""Integrated Agent 001 executable experiment."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from memory import MemoryStore
from ml_policy import VerificationPolicy
from tools import ToolRegistry, build_default_registry


@dataclass
class ExperimentResult:
    output: int
    verification_required: bool
    verified: bool
    tools_called: list[str]
    memory_hits: int


class ResearchAgent:
    def __init__(self, memory: MemoryStore, tools: ToolRegistry) -> None:
        self.memory = memory
        self.tools = tools
        self.policy = VerificationPolicy()
        self.tools_called: list[str] = []

    def run(self, a: int, b: int) -> ExperimentResult:
        prior = self.memory.search("arithmetic addition")

        verification_required = self.policy.requires_verification(
            complexity=0.4,
            uncertainty=0.4,
            novelty=0.7 if not prior else 0.2,
            tool_count=1,
        )

        output = self.tools.call("add", a=a, b=b)
        self.tools_called.append("add")

        verified = True
        if verification_required:
            # Independent verifier: no reuse of the tool's implementation.
            verified = output == (a + b)

        self.memory.add(
            {
                "id": f"run-{len(self.memory.records) + 1}",
                "topic": "arithmetic addition",
                "content": f"{a} + {b} = {output}; verified={verified}",
                "source": "integrated-agent-001",
                "status": "observation",
            }
        )

        return ExperimentResult(
            output=output,
            verification_required=verification_required,
            verified=verified,
            tools_called=list(self.tools_called),
            memory_hits=len(prior),
        )


def run_experiment(path: str | Path = "run-memory.json") -> ExperimentResult:
    memory = MemoryStore(path)
    tools = build_default_registry()
    agent = ResearchAgent(memory, tools)
    return agent.run(17, 25)


if __name__ == "__main__":
    print(run_experiment())
