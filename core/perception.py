"""
Action-at-a-Distance Perception Anchors — Distributed Signal Intake
[EXPERIMENTAL] Not yet integrated into the main execution engine.

Multi-source signal intake system enabling the pipeline to receive
inputs from remote sources in addition to local files.

Real-world: Distributed signal collection with health monitoring.
"""

import time
import json
import asyncio
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Callable
from pathlib import Path
from datetime import datetime


@dataclass
class Signal:
    """Normalized signal format regardless of source."""

    source: str
    timestamp: float
    payload: Any
    metadata: Dict[str, Any] = field(default_factory=dict)


class PerceptionAnchor(ABC):
    """Abstract base for all signal sources."""

    def __init__(self, name: str, config: Dict[str, Any] = None):
        self.name = name
        self.config = config or {}
        self._healthy = True
        self._last_check = 0.0

    @abstractmethod
    async def perceive(self) -> List[Signal]:
        """Collect signals from this source."""
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if this anchor is healthy."""
        pass

    def is_healthy(self) -> bool:
        """Return cached health status."""
        return self._healthy


class HTTPAnchor(PerceptionAnchor):
    """REST API polling with exponential backoff."""

    async def perceive(self) -> List[Signal]:
        # Simulated HTTP polling
        return [
            Signal(
                source=self.name,
                timestamp=time.time(),
                payload={"type": "http_poll", "endpoint": self.config.get("url")},
            )
        ]

    async def health_check(self) -> bool:
        self._healthy = True
        return True


class WebSocketAnchor(PerceptionAnchor):
    """Real-time stream intake."""

    async def perceive(self) -> List[Signal]:
        # Simulated WebSocket intake
        return [
            Signal(
                source=self.name,
                timestamp=time.time(),
                payload={"type": "websocket", "stream": self.config.get("channel")},
            )
        ]

    async def health_check(self) -> bool:
        self._healthy = True
        return True


class FileWatchAnchor(PerceptionAnchor):
    """Enhanced file system monitoring."""

    async def perceive(self) -> List[Signal]:
        watch_dir = Path(self.config.get("path", "."))
        signals = []
        for f in watch_dir.glob("**/*"):
            if f.is_file():
                signals.append(
                    Signal(
                        source=self.name,
                        timestamp=f.stat().st_mtime,
                        payload={"path": str(f), "size": f.stat().st_size},
                    )
                )
        return signals

    async def health_check(self) -> bool:
        watch_dir = Path(self.config.get("path", "."))
        self._healthy = watch_dir.exists()
        return self._healthy


class PerceptionArray:
    """Collection of all perception anchors."""

    def __init__(self):
        self._anchors: Dict[str, PerceptionAnchor] = {}

    def register(self, anchor: PerceptionAnchor) -> None:
        """Register a new perception anchor."""
        self._anchors[anchor.name] = anchor

    async def collect_all(self) -> List[Signal]:
        """Collect signals from all healthy anchors."""
        all_signals = []
        for name, anchor in self._anchors.items():
            if anchor.is_healthy():
                try:
                    signals = await anchor.perceive()
                    all_signals.extend(signals)
                except Exception as e:
                    print(f"Anchor {name} failed: {e}")
        return all_signals

    async def health_report(self) -> Dict[str, bool]:
        """Get health status of all anchors."""
        report = {}
        for name, anchor in self._anchors.items():
            report[name] = await anchor.health_check()
        return report
