"""
Thought Thread Collapse - Multi-Threaded Reasoning Compression
[EXPERIMENTAL] Not yet integrated into the main execution engine.

When multiple parallel reasoning threads explore different hypotheses,
this module collapses them into a single coherent conclusion by finding
the thread with highest confidence and absorbing insights from others.

Real-world: Parallel hypothesis tracking and result aggregation.
"""

import time
import hashlib
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum


class ThreadStatus(Enum):
    ACTIVE = "active"
    COLLAPSED = "collapsed"
    ABSORBED = "absorbed"


@dataclass
class ThoughtThread:
    """A single reasoning thread exploring a hypothesis."""

    thread_id: str
    hypothesis: str
    confidence: float = 0.0
    evidence: List[str] = field(default_factory=list)
    status: ThreadStatus = ThreadStatus.ACTIVE
    created_at: float = field(default_factory=time.time)
    insights: List[str] = field(default_factory=list)
    parent_thread: Optional[str] = None


class ThreadCollapseEngine:
    """Collapses parallel reasoning threads into a unified conclusion."""

    def __init__(self, min_confidence_gap: float = 0.15, max_threads: int = 10):
        self.min_confidence_gap = min_confidence_gap
        self.max_threads = max_threads
        self._threads: Dict[str, ThoughtThread] = {}

    def spawn_thread(self, hypothesis: str, parent: str = None) -> str:
        """Spawn a new reasoning thread."""
        if len(self._threads) >= self.max_threads:
            self._collapse_weakest()

        thread_id = hashlib.sha256(f"{hypothesis}{time.time()}".encode()).hexdigest()[
            :12
        ]

        thread = ThoughtThread(
            thread_id=thread_id, hypothesis=hypothesis, parent_thread=parent
        )
        self._threads[thread_id] = thread
        return thread_id

    def add_evidence(self, thread_id: str, evidence: str, weight: float = 0.1) -> None:
        """Add evidence to a thread and update confidence."""
        if thread_id not in self._threads:
            return

        thread = self._threads[thread_id]
        thread.evidence.append(evidence)
        thread.confidence = min(1.0, thread.confidence + weight)

    def add_insight(self, thread_id: str, insight: str) -> None:
        """Add an insight to a thread."""
        if thread_id in self._threads:
            self._threads[thread_id].insights.append(insight)

    def collapse(self) -> Optional[ThoughtThread]:
        """Collapse all threads into the highest-confidence conclusion."""
        active_threads = [
            t for t in self._threads.values() if t.status == ThreadStatus.ACTIVE
        ]

        if not active_threads:
            return None

        active_threads.sort(key=lambda t: t.confidence, reverse=True)
        winner = active_threads[0]

        for thread in active_threads[1:]:
            if winner.confidence - thread.confidence >= self.min_confidence_gap:
                thread.status = ThreadStatus.ABSORBED
                winner.insights.extend(
                    f"[from {thread.thread_id}] {ins}" for ins in thread.insights
                )
            else:
                thread.status = ThreadStatus.COLLAPSED

        winner.status = ThreadStatus.COLLAPSED
        return winner

    def _collapse_weakest(self) -> None:
        """Collapse the weakest thread to make room."""
        active = [t for t in self._threads.values() if t.status == ThreadStatus.ACTIVE]
        if active:
            weakest = min(active, key=lambda t: t.confidence)
            weakest.status = ThreadStatus.ABSORBED

    def get_thread(self, thread_id: str) -> Optional[ThoughtThread]:
        """Get a thread by ID."""
        return self._threads.get(thread_id)

    def active_threads(self) -> List[ThoughtThread]:
        """Get all active threads."""
        return [t for t in self._threads.values() if t.status == ThreadStatus.ACTIVE]

    def summary(self) -> Dict[str, Any]:
        """Get a summary of all threads."""
        return {
            "total_threads": len(self._threads),
            "active": len(
                [t for t in self._threads.values() if t.status == ThreadStatus.ACTIVE]
            ),
            "collapsed": len(
                [
                    t
                    for t in self._threads.values()
                    if t.status == ThreadStatus.COLLAPSED
                ]
            ),
            "absorbed": len(
                [t for t in self._threads.values() if t.status == ThreadStatus.ABSORBED]
            ),
            "top_hypothesis": self._top_hypothesis(),
        }

    def _top_hypothesis(self) -> Optional[str]:
        """Get the highest confidence hypothesis."""
        active = [t for t in self._threads.values() if t.status == ThreadStatus.ACTIVE]
        if active:
            return max(active, key=lambda t: t.confidence).hypothesis
        return None
