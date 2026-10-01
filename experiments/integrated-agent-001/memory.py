"""Minimal persistent memory for the integrated experiment."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class MemoryStore:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.records: list[dict[str, Any]] = []
        self.load()

    def load(self) -> None:
        if self.path.exists():
            self.records = json.loads(self.path.read_text(encoding="utf-8"))
        else:
            self.records = []

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self.records, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def add(self, record: dict[str, Any]) -> None:
        required = {"id", "topic", "content", "source", "status"}
        missing = required - record.keys()
        if missing:
            raise ValueError(f"missing fields: {sorted(missing)}")
        self.records.append(dict(record))
        self.save()

    def search(self, query: str, limit: int = 5) -> list[dict[str, Any]]:
        terms = {term.lower() for term in query.split() if term.strip()}
        scored: list[tuple[int, dict[str, Any]]] = []
        for record in self.records:
            haystack = (
                f"{record.get('topic', '')} {record.get('content', '')}"
            ).lower()
            score = sum(term in haystack for term in terms)
            if score:
                scored.append((score, record))
        scored.sort(key=lambda item: item[0], reverse=True)
        return [record for _, record in scored[:limit]]
