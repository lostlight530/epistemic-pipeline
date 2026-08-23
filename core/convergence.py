"""Experimental momentum-based bounded score tracker.

[EXPERIMENTAL] Not integrated into the main execution engine.

The historical ``ConvergenceAccelerator`` / ``BeliefState`` names are retained
for compatibility. The implementation applies a simple momentum update to a
caller-provided scalar stream and stops when consecutive score changes fall
below a threshold. It is not evidence aggregation, Bayesian updating, belief
revision logic, or proof that a hypothesis has become true.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class BeliefState:
    hypothesis: str
    confidence: float
    momentum: float = 0.0
    evidence_count: int = 0
    history: List[float] = field(default_factory=list)


class ConvergenceAccelerator:
    """Momentum update helper over bounded caller-supplied scores."""

    def __init__(
        self,
        momentum_factor: float = 0.9,
        learning_rate: float = 0.01,
        convergence_threshold: float = 0.001,
        max_iterations: int = 1000,
    ):
        if not 0 <= momentum_factor < 1:
            raise ValueError("momentum_factor must be in [0,1)")
        if learning_rate <= 0:
            raise ValueError("learning_rate must be > 0")
        if convergence_threshold <= 0:
            raise ValueError("convergence_threshold must be > 0")
        if max_iterations < 1:
            raise ValueError("max_iterations must be >= 1")
        self.momentum_factor = float(momentum_factor)
        self.learning_rate = float(learning_rate)
        self.convergence_threshold = float(convergence_threshold)
        self.max_iterations = int(max_iterations)
        self._beliefs: Dict[str, BeliefState] = {}

    def register_hypothesis(self, hypothesis: str, initial_confidence: float = 0.5) -> None:
        if not hypothesis:
            raise ValueError("hypothesis must be non-empty")
        value = float(initial_confidence)
        if not 0 <= value <= 1:
            raise ValueError("initial score must be within [0,1]")
        self._beliefs[hypothesis] = BeliefState(
            hypothesis=hypothesis,
            confidence=value,
            history=[value],
        )

    def update_belief(self, hypothesis: str, evidence_weight: float) -> None:
        """Apply one scalar momentum update; ``evidence_weight`` is caller semantics."""
        if hypothesis not in self._beliefs:
            self.register_hypothesis(hypothesis)
        belief = self._beliefs[hypothesis]
        gradient = float(evidence_weight) * self.learning_rate
        belief.momentum = self.momentum_factor * belief.momentum + gradient
        belief.confidence = min(max(belief.confidence + belief.momentum, 0.0), 1.0)
        belief.evidence_count += 1
        belief.history.append(belief.confidence)

    def check_convergence(self, hypothesis: str) -> bool:
        """Return whether the last scalar update was smaller than the threshold."""
        belief = self._beliefs.get(hypothesis)
        if belief is None or len(belief.history) < 2:
            return False
        return abs(belief.history[-1] - belief.history[-2]) < self.convergence_threshold

    def run_until_convergence(
        self, hypothesis: str, evidence_stream: List[float]
    ) -> Tuple[bool, int]:
        if hypothesis not in self._beliefs:
            self.register_hypothesis(hypothesis)
        for index, weight in enumerate(evidence_stream[: self.max_iterations], 1):
            self.update_belief(hypothesis, weight)
            if index >= 3 and self.check_convergence(hypothesis):
                return True, index
        iterations = min(len(evidence_stream), self.max_iterations)
        return self.check_convergence(hypothesis), iterations

    def get_belief(self, hypothesis: str) -> Optional[BeliefState]:
        return self._beliefs.get(hypothesis)

    def all_beliefs(self) -> Dict[str, BeliefState]:
        return dict(self._beliefs)

    def confidence_ranking(self) -> List[Tuple[str, float]]:
        """Sort current project scores; ranking is not a truth ranking."""
        return sorted(
            ((key, state.confidence) for key, state in self._beliefs.items()),
            key=lambda item: (-item[1], item[0]),
        )

    def semantics(self) -> dict:
        return {
            "experimental": True,
            "score_semantics": "caller-defined bounded scalar, not calibrated probability",
            "convergence_semantics": "small consecutive numerical update only",
        }
