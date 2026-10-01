"""Explicit, inspectable tools used by the integrated agent."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    handler: Callable[..., Any]


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def call(self, name: str, **kwargs: Any) -> Any:
        if name not in self._tools:
            raise KeyError(f"unknown tool: {name}")
        return self._tools[name].handler(**kwargs)

    def list_tools(self) -> list[str]:
        return sorted(self._tools)


def add(a: int, b: int) -> int:
    return a + b


def build_default_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(Tool("add", "Add two integers.", add))
    return registry
