"""Signal Intake Prototypes
[EXPERIMENTAL] Not integrated into the main execution engine.

Historical compatibility names are retained, but the current HTTP/WebSocket
anchors are *descriptors/simulations*: they do not perform network I/O. The
file anchor enumerates local files. Real transport implementations belong in
separate adapters with explicit dependencies, authentication and retry policy.
"""

from __future__ import annotations

import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class Signal:
    source: str
    timestamp: float
    payload: Any
    metadata: Dict[str, Any] = field(default_factory=dict)


class PerceptionAnchor(ABC):
    """Abstract signal-source interface."""

    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        if not name:
            raise ValueError("anchor name must be non-empty")
        self.name = name
        self.config = dict(config or {})
        self._healthy = False
        self._last_check = 0.0

    @abstractmethod
    async def perceive(self) -> List[Signal]:
        raise NotImplementedError

    @abstractmethod
    async def health_check(self) -> bool:
        raise NotImplementedError

    def is_healthy(self) -> bool:
        return self._healthy


class HTTPAnchor(PerceptionAnchor):
    """Compatibility prototype that emits an HTTP endpoint descriptor only."""

    async def perceive(self) -> List[Signal]:
        url = self.config.get("url")
        if not url:
            return []
        return [
            Signal(
                source=self.name,
                timestamp=time.time(),
                payload={"type": "http_descriptor", "endpoint": url},
                metadata={"simulated": True, "network_io_performed": False},
            )
        ]

    async def health_check(self) -> bool:
        self._last_check = time.time()
        self._healthy = bool(self.config.get("url"))
        return self._healthy


class WebSocketAnchor(PerceptionAnchor):
    """Compatibility prototype that emits a stream descriptor only."""

    async def perceive(self) -> List[Signal]:
        channel = self.config.get("channel")
        if not channel:
            return []
        return [
            Signal(
                source=self.name,
                timestamp=time.time(),
                payload={"type": "websocket_descriptor", "stream": channel},
                metadata={"simulated": True, "network_io_performed": False},
            )
        ]

    async def health_check(self) -> bool:
        self._last_check = time.time()
        self._healthy = bool(self.config.get("channel"))
        return self._healthy


class FileWatchAnchor(PerceptionAnchor):
    """Local recursive file snapshot adapter; it does not subscribe to OS events."""

    async def perceive(self) -> List[Signal]:
        watch_dir = Path(self.config.get("path", "."))
        if not watch_dir.is_dir():
            return []
        signals: List[Signal] = []
        for path in sorted(watch_dir.rglob("*")):
            if not path.is_file():
                continue
            stat = path.stat()
            signals.append(
                Signal(
                    source=self.name,
                    timestamp=stat.st_mtime,
                    payload={"path": str(path), "size": stat.st_size},
                    metadata={"mode": "snapshot_scan", "network_io_performed": False},
                )
            )
        return signals

    async def health_check(self) -> bool:
        self._last_check = time.time()
        watch_dir = Path(self.config.get("path", "."))
        self._healthy = watch_dir.is_dir()
        return self._healthy


class PerceptionArray:
    """Sequential collection facade for registered experimental anchors."""

    def __init__(self):
        self._anchors: Dict[str, PerceptionAnchor] = {}

    def register(self, anchor: PerceptionAnchor) -> None:
        if anchor.name in self._anchors:
            raise ValueError(f"duplicate anchor name: {anchor.name}")
        self._anchors[anchor.name] = anchor

    async def collect_all(self, refresh_health: bool = True) -> List[Signal]:
        all_signals: List[Signal] = []
        for anchor in self._anchors.values():
            healthy = await anchor.health_check() if refresh_health else anchor.is_healthy()
            if not healthy:
                continue
            try:
                all_signals.extend(await anchor.perceive())
            except Exception:
                anchor._healthy = False
        return all_signals

    async def health_report(self) -> Dict[str, bool]:
        return {name: await anchor.health_check() for name, anchor in self._anchors.items()}

    def semantics(self) -> dict:
        return {
            "status": "experimental",
            "http_anchor": "descriptor_only_no_network_io",
            "websocket_anchor": "descriptor_only_no_network_io",
            "file_anchor": "recursive_snapshot_scan_not_event_watch",
        }
