"""
Infinite Regression Loop - Recursive Depth Controller

Manages recursive reasoning that could theoretically go infinitely deep.
Like standing between two mirrors, each reflection contains the last -
but this module adds a termination condition so the loop converges.

Real-world: Recursive depth management with convergence detection.
"""

import time
import hashlib
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Callable, Set


@dataclass
class RegressionLevel:
    """A single level in the regression."""
    depth: int
    input_hash: str
    output: Any = None
    converged: bool = False
    timestamp: float = field(default_factory=time.time)


class InfiniteRegressionLoop:
    """Recursive depth controller with convergence detection."""
    
    def __init__(
        self,
        max_depth: int = 100,
        convergence_threshold: float = 0.001,
        hash_history_size: int = 50
    ):
        self.max_depth = max_depth
        self.convergence_threshold = convergence_threshold
        self.hash_history_size = hash_history_size
        self._levels: List[RegressionLevel] = []
        self._hash_history: List[str] = []
        self._cycle_cache: Set[str] = set()
    
    def run(
        self,
        initial_input: Any,
        regression_fn: Callable[[Any, int], Any],
        convergence_fn: Callable[[Any, Any], float] = None
    ) -> Optional[RegressionLevel]:
        """Run the regression loop until convergence or max depth."""
        current_input = initial_input
        
        for depth in range(self.max_depth):
            input_hash = self._hash_input(current_input)
            
            if input_hash in self._cycle_cache:
                level = RegressionLevel(
                    depth=depth,
                    input_hash=input_hash,
                    output=current_input,
                    converged=True
                )
                level.output = "CYCLE_DETECTED"
                self._levels.append(level)
                return level
            
            self._cycle_cache.add(input_hash)
            self._hash_history.append(input_hash)
            if len(self._hash_history) > self.hash_history_size:
                old = self._hash_history.pop(0)
                self._cycle_cache.discard(old)
            
            output = regression_fn(current_input, depth)
            
            level = RegressionLevel(
                depth=depth,
                input_hash=input_hash,
                output=output
            )
            self._levels.append(level)
            
            if convergence_fn:
                delta = convergence_fn(current_input, output)
                if delta < self.convergence_threshold:
                    level.converged = True
                    return level
            
            current_input = output
        
        return self._levels[-1] if self._levels else None
    
    def _hash_input(self, input_data: Any) -> str:
        """Compute a hash of the input for cycle detection."""
        try:
            input_str = str(input_data)
            return hashlib.sha256(input_str.encode()).hexdigest()[:16]
        except Exception:
            return hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
    
    def get_levels(self, depth_range: tuple = None) -> List[RegressionLevel]:
        """Get regression levels, optionally within a depth range."""
        if depth_range:
            start, end = depth_range
            return [l for l in self._levels if start <= l.depth <= end]
        return list(self._levels)
    
    def detect_cycle(self) -> Optional[tuple]:
        """Detect if a cycle exists in the hash history."""
        seen = {}
        for i, h in enumerate(self._hash_history):
            if h in seen:
                return (seen[h], i)
            seen[h] = i
        return None
    
    def convergence_rate(self) -> float:
        """Calculate what fraction of levels converged."""
        if not self._levels:
            return 0.0
        converged = sum(1 for l in self._levels if l.converged)
        return converged / len(self._levels)
    
    def stats(self) -> Dict[str, Any]:
        """Get regression statistics."""
        cycle = self.detect_cycle()
        return {
            "total_depth": len(self._levels),
            "max_depth": self.max_depth,
            "converged": any(l.converged for l in self._levels),
            "convergence_rate": self.convergence_rate(),
            "cycle_detected": cycle is not None,
            "cycle_range": cycle
        }
    
    def reset(self) -> None:
        """Reset the regression loop."""
        self._levels.clear()
        self._hash_history.clear()
        self._cycle_cache.clear()
