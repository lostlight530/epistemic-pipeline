"""
Cognitive Convergence Accelerator - Iterative Belief Refinement

Accelerates convergence of multi-source evidence evaluation through
momentum-based belief updating and early stopping when confidence
stabilizes.

Real-world: Iterative algorithm convergence with momentum.
"""

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class BeliefState:
    """A belief state with confidence and momentum."""
    hypothesis: str
    confidence: float
    momentum: float = 0.0
    evidence_count: int = 0
    history: List[float] = field(default_factory=list)


class ConvergenceAccelerator:
    """Momentum-based belief convergence accelerator."""
    
    def __init__(
        self,
        momentum_factor: float = 0.9,
        learning_rate: float = 0.01,
        convergence_threshold: float = 0.001,
        max_iterations: int = 1000
    ):
        self.momentum_factor = momentum_factor
        self.learning_rate = learning_rate
        self.convergence_threshold = convergence_threshold
        self.max_iterations = max_iterations
        self._beliefs: Dict[str, BeliefState] = {}
    
    def register_hypothesis(self, hypothesis: str, initial_confidence: float = 0.5) -> None:
        """Register a new hypothesis for convergence tracking."""
        self._beliefs[hypothesis] = BeliefState(
            hypothesis=hypothesis,
            confidence=initial_confidence,
            momentum=0.0,
            evidence_count=0,
            history=[initial_confidence]
        )
    
    def update_belief(self, hypothesis: str, evidence_weight: float) -> None:
        """Update belief with new evidence using momentum."""
        if hypothesis not in self._beliefs:
            self.register_hypothesis(hypothesis)
        
        belief = self._beliefs[hypothesis]
        
        gradient = evidence_weight * self.learning_rate
        belief.momentum = self.momentum_factor * belief.momentum + gradient
        belief.confidence = max(0.0, min(1.0, belief.confidence + belief.momentum))
        belief.evidence_count += 1
        belief.history.append(belief.confidence)
    
    def check_convergence(self, hypothesis: str) -> bool:
        """Check if a hypothesis has converged."""
        if hypothesis not in self._beliefs:
            return False
        
        belief = self._beliefs[hypothesis]
        if len(belief.history) < 2:
            return False
        
        recent_delta = abs(belief.history[-1] - belief.history[-2])
        return recent_delta < self.convergence_threshold
    
    def run_until_convergence(self, hypothesis: str, evidence_stream: List[float]) -> Tuple[bool, int]:
        """Run updates until convergence or max iterations."""
        if hypothesis not in self._beliefs:
            self.register_hypothesis(hypothesis)
        
        for i, weight in enumerate(evidence_stream):
            self.update_belief(hypothesis, weight)
            
            if i >= 2 and self.check_convergence(hypothesis):
                return True, i + 1
            
            if i + 1 >= self.max_iterations:
                return False, i + 1
        
        return self.check_convergence(hypothesis), len(evidence_stream)
    
    def get_belief(self, hypothesis: str) -> Optional[BeliefState]:
        """Get current belief state for a hypothesis."""
        return self._beliefs.get(hypothesis)
    
    def all_beliefs(self) -> Dict[str, BeliefState]:
        """Get all belief states."""
        return dict(self._beliefs)
    
    def confidence_ranking(self) -> List[Tuple[str, float]]:
        """Rank hypotheses by confidence."""
        return sorted(
            [(h, b.confidence) for h, b in self._beliefs.items()],
            key=lambda x: x[1],
            reverse=True
        )
