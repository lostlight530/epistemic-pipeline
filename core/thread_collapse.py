"""Hypothesis Thread Aggregator
[EXPERIMENTAL] Not integrated into the main execution engine.

Historical compatibility name: ``ThreadCollapseEngine``.

The module tracks parallel hypotheses, opaque caller-supplied evidence weights
and notes, then selects the highest bounded heuristic score. It does not perform
multi-agent reasoning, probabilistic inference, or scientific adjudication.
"""

from __future__ import annotations

import hashlib
import itertools
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class ThreadStatus(Enum):
    ACTIVE = "active"
    SELECTED = "selected"
    DEFERRED = "deferred"
    ABSORBED = "absorbed"
    # Historical compatibility value.
    COLLAPSED = "collapsed"


@dataclass
class ThoughtThread:
    thread_id: str
    hypothesis: str
    confidence: float = 0.0  # compatibility field: bounded heuristic score
    evidence: List[str] = field(default_factory=list)
    status: ThreadStatus = ThreadStatus.ACTIVE
    insights: List[str] = field(default_factory=list)
    parent_thread: Optional[str] = None
    score_semantics: str = "bounded_heuristic_score_not_probability"


class ThreadCollapseEngine:
    """Compatibility facade for bounded hypothesis-score aggregation."""

    def __init__(self, min_confidence_gap: float = 0.15, max_threads: int = 10):
        if not 0.0 <= min_confidence_gap <= 1.0:
            raise ValueError("min_confidence_gap must be within [0, 1]")
        if max_threads < 1:
            raise ValueError("max_threads must be >= 1")
        self.min_confidence_gap = min_confidence_gap
        self.max_threads = max_threads
        self._threads: Dict[str, ThoughtThread] = {}
        self._counter = itertools.count()

    def spawn_thread(self, hypothesis: str, parent: Optional[str] = None) -> str:
        if not hypothesis.strip():
            raise ValueError("hypothesis must be non-empty")
        if parent is not None and parent not in self._threads:
            raise ValueError(f"unknown parent thread: {parent}")
        if len(self.active_threads()) >= self.max_threads:
            self._defer_weakest()

        ordinal = next(self._counter)
        seed = f"{ordinal}\x1f{parent or ''}\x1f{hypothesis}".encode("utf-8")
        thread_id = hashlib.sha256(seed).hexdigest()[:12]
        self._threads[thread_id] = ThoughtThread(
            thread_id=thread_id,
            hypothesis=hypothesis,
            parent_thread=parent,
        )
        return thread_id

    def add_evidence(self, thread_id: str, evidence: str, weight: float = 0.1) -> None:
        """Add an evidence note and adjust the local heuristic score."""
        thread = self._require_thread(thread_id)
        if not evidence.strip():
            raise ValueError("evidence must be non-empty")
        weight = float(weight)
        if not -1.0 <= weight <= 1.0:
            raise ValueError("evidence weight must be within [-1, 1]")
        thread.evidence.append(evidence)
        thread.confidence = max(0.0, min(1.0, thread.confidence + weight))

    def add_insight(self, thread_id: str, insight: str) -> None:
        thread = self._require_thread(thread_id)
        if insight.strip():
            thread.insights.append(insight)

    def collapse(self) -> Optional[ThoughtThread]:
        """Select the active thread with the highest heuristic score."""
        active = sorted(
            self.active_threads(),
            key=lambda thread: (-thread.confidence, thread.thread_id),
        )
        if not active:
            return None

        winner = active[0]
        winner.status = ThreadStatus.SELECTED
        for thread in active[1:]:
            gap = winner.confidence - thread.confidence
            if gap >= self.min_confidence_gap:
                thread.status = ThreadStatus.ABSORBED
                winner.insights.extend(
                    f"[from {thread.thread_id}] {insight}" for insight in thread.insights
                )
            else:
                thread.status = ThreadStatus.DEFERRED
        return winner

    def _defer_weakest(self) -> None:
        active = self.active_threads()
        if active:
            weakest = min(active, key=lambda thread: (thread.confidence, thread.thread_id))
            weakest.status = ThreadStatus.DEFERRED

    def _require_thread(self, thread_id: str) -> ThoughtThread:
        try:
            return self._threads[thread_id]
        except KeyError as exc:
            raise KeyError(f"unknown thread_id: {thread_id}") from exc

    def get_thread(self, thread_id: str) -> Optional[ThoughtThread]:
        return self._threads.get(thread_id)

    def active_threads(self) -> List[ThoughtThread]:
        return [thread for thread in self._threads.values() if thread.status == ThreadStatus.ACTIVE]

    def summary(self) -> Dict[str, Any]:
        by_status = {
            status.value: sum(1 for thread in self._threads.values() if thread.status == status)
            for status in ThreadStatus
        }
        top = max(self._threads.values(), key=lambda t: t.confidence, default=None)
        return {
            "total_threads": len(self._threads),
            "by_status": by_status,
            "top_hypothesis": top.hypothesis if top else None,
            "top_score": top.confidence if top else None,
            "score_semantics": "bounded_heuristic_score_not_probability",
            "selection_semantics": "ranking_not_truth_adjudication",
        }
