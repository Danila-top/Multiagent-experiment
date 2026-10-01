import tempfile
from pathlib import Path

from experiment import run_experiment
from memory import MemoryStore
from ml_policy import VerificationPolicy
from tools import build_default_registry


def test_tool_registry() -> None:
    registry = build_default_registry()
    assert registry.list_tools() == ["add"]
    assert registry.call("add", a=17, b=25) == 42


def test_ml_policy_is_deterministic() -> None:
    first = VerificationPolicy().requires_verification(
        complexity=0.4,
        uncertainty=0.4,
        novelty=0.7,
        tool_count=1,
    )
    second = VerificationPolicy().requires_verification(
        complexity=0.4,
        uncertainty=0.4,
        novelty=0.7,
        tool_count=1,
    )
    assert first == second


def test_integrated_run_uses_memory_tools_and_verification() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        result = run_experiment(Path(tmp) / "memory.json")
        assert result.output == 42
        assert result.verification_required is True
        assert result.verified is True
        assert result.tools_called == ["add"]
        assert result.memory_hits == 0

        restored = MemoryStore(Path(tmp) / "memory.json")
        assert len(restored.records) == 1
        assert "42" in restored.records[0]["content"]
