"""Deterministic ML routing policy for verification.

The classifier is deliberately tiny. It demonstrates where an ML component
can sit in an agent architecture without pretending that the model is the
agent itself.
"""

from __future__ import annotations

from sklearn.linear_model import LogisticRegression


class VerificationPolicy:
    def __init__(self) -> None:
        # Features: complexity, uncertainty, novelty, number_of_tools.
        x_train = [
            [0.0, 0.0, 0.0, 0.0],
            [0.2, 0.1, 0.0, 1.0],
            [0.3, 0.2, 0.2, 1.0],
            [0.5, 0.4, 0.4, 1.0],
            [0.7, 0.5, 0.5, 1.0],
            [0.8, 0.8, 0.7, 2.0],
            [0.9, 0.9, 0.9, 3.0],
            [0.4, 0.7, 0.8, 2.0],
        ]
        y_train = [0, 0, 0, 1, 1, 1, 1, 1]

        self.model = LogisticRegression(
            random_state=42,
            solver="liblinear",
        )
        self.model.fit(x_train, y_train)

    def requires_verification(
        self,
        *,
        complexity: float,
        uncertainty: float,
        novelty: float,
        tool_count: int,
    ) -> bool:
        features = [[complexity, uncertainty, novelty, tool_count]]
        return bool(self.model.predict(features)[0])
