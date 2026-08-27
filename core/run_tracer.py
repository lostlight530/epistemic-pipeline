#!/usr/bin/env python3
"""Project JSONL run tracing with scoped OpenTelemetry GenAI naming alignment.

The trace format is owned by epistemic-pipeline; it is not an OpenTelemetry
exporter, span implementation or Logs API implementation. Where useful, the
project reuses Development-grade GenAI semantic-convention names such as
``gen_ai.operation.name``. Project-local correlation uses ``epistemic.run.id``
rather than misrepresenting the run ID as a provider conversation/session ID.

Each record participates in a SHA-256 previous-record chain. ``verify_chain``
checks internal sequence/hash consistency for the bytes that are present. With
no externally anchored chain head or expected record count, this is not a
complete tamper-proof log and cannot by itself detect every tail truncation.
"""

from __future__ import annotations

import hashlib
import json
import threading
import time
from pathlib import Path
from typing import Dict, Optional

PROFILE = "epistemic-pipeline/trace"
OP_INVOKE_AGENT = "invoke_agent"


class RunTracer:
    """Thread-safe project tracer for node start/end records."""

    def __init__(self, run_id: str, output_dir: str = "traces"):
        if not run_id:
            raise ValueError("run_id must be non-empty")
        self.run_id = run_id
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.path = self.output_dir / f"{run_id}.jsonl"
        self._lock = threading.Lock()
        self._starts: Dict[str, float] = {}
        self._prev_hash = self._load_chain_head()

    def _load_chain_head(self) -> str:
        """Recover the last internally valid hash when resuming an existing trace."""
        if not self.path.exists():
            return "GENESIS"
        previous = "GENESIS"
        with self.path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"invalid trace JSON at line {line_number}") from exc
                stored_hash = record.get("hash")
                if not stored_hash:
                    raise ValueError(f"trace record missing hash at line {line_number}")
                check = dict(record)
                check.pop("hash", None)
                if check.get("prev_hash") != previous or self._digest(check) != stored_hash:
                    raise ValueError(f"trace hash-chain mismatch at line {line_number}")
                previous = stored_hash
        return previous

    @staticmethod
    def _digest(record: dict) -> str:
        canonical = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def _append(self, record: dict) -> None:
        with self._lock:
            record = dict(record)
            record["prev_hash"] = self._prev_hash
            record["hash"] = self._digest(record)
            with self.path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                handle.flush()
            self._prev_hash = record["hash"]

    def start_node(
        self,
        state_id: str,
        stage: str,
        operation_name: str = OP_INVOKE_AGENT,
    ) -> None:
        """Record a project node start using scoped GenAI operation naming."""
        with self._lock:
            self._starts[state_id] = time.monotonic()
        self._append(
            {
                "timestamp": time.time(),
                "profile": PROFILE,
                "gen_ai.operation.name": operation_name,
                "epistemic.run.id": self.run_id,
                "epistemic.node.id": state_id,
                "epistemic.stage": stage,
                "event": "start",
            }
        )

    def end_node(
        self,
        state_id: str,
        stage: str,
        status: str,
        error_type: Optional[str] = None,
        operation_name: str = OP_INVOKE_AGENT,
    ) -> None:
        """Record a project node end and elapsed monotonic duration."""
        with self._lock:
            started = self._starts.pop(state_id, None)
        duration_ms = round((time.monotonic() - started) * 1000, 3) if started is not None else None
        record = {
            "timestamp": time.time(),
            "profile": PROFILE,
            "gen_ai.operation.name": operation_name,
            "epistemic.run.id": self.run_id,
            "epistemic.node.id": state_id,
            "epistemic.stage": stage,
            "event": "end",
            "status": status,
            "duration_ms": duration_ms,
        }
        if error_type:
            record["error.type"] = error_type
        self._append(record)

    @staticmethod
    def verify_chain(path: str) -> bool:
        """Verify internal previous-hash linkage for all records currently present."""
        previous = "GENESIS"
        try:
            with Path(path).open("r", encoding="utf-8") as handle:
                for line in handle:
                    if not line.strip():
                        continue
                    record = json.loads(line)
                    stored_hash = record.pop("hash", None)
                    if not stored_hash or record.get("prev_hash") != previous:
                        return False
                    if RunTracer._digest(record) != stored_hash:
                        return False
                    previous = stored_hash
        except (OSError, json.JSONDecodeError):
            return False
        return True
