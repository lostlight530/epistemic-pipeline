"""Recursive Depth Controller
[EXPERIMENTAL] Not integrated into the main execution engine.

This module repeatedly applies a caller-supplied transformation while enforcing
bounded depth and optional caller-defined convergence. It can also detect a
repeated input fingerprint within a bounded history window.

Important boundaries:
- a repeated state is a *cycle termination*, not numerical convergence;
- convergence exists only when a caller supplies ``convergence_fn``;
- hashes identify the module's canonicalized input representation only;
- the module does not establish truth, reasoning quality, or fixed-point
  correctness for an external model.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set


@dataclass
class RegressionLevel:
    """One bounded iteration in a recursive transformation."""

    depth: int
    input_hash: str
    output: Any = None
    converged: bool = False
    cycle_detected: bool = False
    termination_reason: Optional[str] = None
    timestamp: float = field(default_factory=time.time)


class InfiniteRegressionLoop:
    """Compatibility name for a bounded recursive transformation controller."""

    def __init__(
        self,
        max_depth: int = 100,
        convergence_threshold: float = 0.001,
        hash_history_size: int = 50,
    ):
        if max_depth < 1:
            raise ValueError("max_depth must be >= 1")
        if convergence_threshold < 0:
            raise ValueError("convergence_threshold must be >= 0")
        if hash_history_size < 1:
            raise ValueError("hash_history_size must be >= 1")
        self.max_depth = max_depth
        self.convergence_threshold = convergence_threshold
        self.hash_history_size = hash_history_size
        self._levels: List[RegressionLevel] = []
        self._hash_history: List[str] = []
        self._cycle_cache: Set[str] = set()
        self._cycle_range: Optional[tuple[int, int]] = None

    def run(
        self,
        initial_input: Any,
        regression_fn: Callable[[Any, int], Any],
        convergence_fn: Optional[Callable[[Any, Any], float]] = None,
    ) -> Optional[RegressionLevel]:
        """Run until caller-defined convergence, cycle detection, or max depth."""
        self.reset()
        current_input = initial_input
        first_seen: Dict[str, int] = {}

        for depth in range(self.max_depth):
            input_hash = self._hash_input(current_input)

            if input_hash in self._cycle_cache:
                first_depth = first_seen.get(input_hash, depth)
                self._cycle_range = (first_depth, depth)
                level = RegressionLevel(
                    depth=depth,
                    input_hash=input_hash,
                    output=current_input,
                    converged=False,
                    cycle_detected=True,
                    termination_reason="cycle",
                )
                self._levels.append(level)
                return level

            first_seen[input_hash] = depth
            self._cycle_cache.add(input_hash)
            self._hash_history.append(input_hash)
            if len(self._hash_history) > self.hash_history_size:
                old = self._hash_history.pop(0)
                self._cycle_cache.discard(old)
                first_seen.pop(old, None)

            output = regression_fn(current_input, depth)
            level = RegressionLevel(depth=depth, input_hash=input_hash, output=output)
            self._levels.append(level)

            if convergence_fn is not None:
                delta = float(convergence_fn(current_input, output))
                if delta < 0:
                    raise ValueError("convergence_fn must return a non-negative delta")
                if delta < self.convergence_threshold:
                    level.converged = True
                    level.termination_reason = "converged"
                    return level

            current_input = output

        if self._levels:
            self._levels[-1].termination_reason = "max_depth"
        return self._levels[-1] if self._levels else None

    @staticmethod
    def _hash_input(input_data: Any) -> str:
        """Hash a stable JSON representation when possible, otherwise ``repr``."""
        try:
            encoded = json.dumps(
                input_data,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                default=repr,
            )
        except (TypeError, ValueError):
            encoded = repr(input_data)
        return hashlib.sha256(encoded.encode("utf-8")).hexdigest()[:16]

    def get_levels(self, depth_range: Optional[tuple] = None) -> List[RegressionLevel]:
        if depth_range:
            start, end = depth_range
            return [level for level in self._levels if start <= level.depth <= end]
        return list(self._levels)

    def detect_cycle(self) -> Optional[tuple[int, int]]:
        return self._cycle_range

    def convergence_rate(self) -> float:
        """Compatibility metric: fraction of recorded levels marked converged."""
        if not self._levels:
            return 0.0
        return sum(1 for level in self._levels if level.converged) / len(self._levels)

    def stats(self) -> Dict[str, Any]:
        last = self._levels[-1] if self._levels else None
        return {
            "total_depth": len(self._levels),
            "max_depth": self.max_depth,
            "converged": bool(last and last.converged),
            "cycle_detected": bool(last and last.cycle_detected),
            "termination_reason": last.termination_reason if last else None,
            "cycle_range": self._cycle_range,
            "semantics": "bounded_recursive_termination_not_reasoning_truth",
        }

    def reset(self) -> None:
        self._levels.clear()
        self._hash_history.clear()
        self._cycle_cache.clear()
        self._cycle_range = None
