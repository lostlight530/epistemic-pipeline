#!/usr/bin/env python3
"""Bounded retry/timeout helpers for node execution.

The module distinguishes explicitly known permanent failures from failures that
may be retried. Unknown exceptions are treated as permanent by default: blindly
retrying an unknown programming/domain error can multiply side effects and hide
bugs. Callers that need richer retry taxonomies should classify provider errors
before passing them here.

Thread timeouts are caller-side time bounds only. Python cannot forcibly kill
the running worker thread; timed-out work may continue in the background.
"""

from __future__ import annotations

import concurrent.futures
import random
import time
from dataclasses import dataclass
from typing import Any, Callable, Optional

TRANSIENT_TYPES = (TimeoutError, ConnectionError)
PERMANENT_TYPES = (NotImplementedError, ValueError, KeyError, TypeError, AssertionError)


def classify_error(exc: BaseException) -> str:
    """Classify known exceptions as ``transient`` or ``permanent``."""
    if isinstance(exc, PERMANENT_TYPES):
        return "permanent"
    if isinstance(exc, TRANSIENT_TYPES):
        return "transient"
    # OSError is broad; only retry subclasses callers intentionally surface as
    # connection/time-oriented errors rather than all filesystem/program errors.
    return "permanent"


@dataclass(frozen=True)
class RetryPolicy:
    """Exponential backoff with full jitter and explicit validation."""

    max_attempts: int = 1
    base_delay: float = 0.1
    factor: float = 2.0
    max_delay: float = 30.0

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be >= 1")
        if self.base_delay < 0 or self.max_delay < 0:
            raise ValueError("retry delays must be >= 0")
        if self.factor < 1:
            raise ValueError("factor must be >= 1")

    @classmethod
    def from_node_spec(cls, spec: Optional[dict]) -> "RetryPolicy":
        spec = spec or {}
        return cls(
            max_attempts=int(spec.get("max_attempts", 1)),
            base_delay=float(spec.get("base_delay", 0.1)),
            factor=float(spec.get("factor", 2.0)),
            max_delay=float(spec.get("max_delay", 30.0)),
        )

    def delay_for(self, attempt: int) -> float:
        """Return full-jitter delay after a 1-indexed failed attempt."""
        if attempt < 1:
            raise ValueError("attempt must be >= 1")
        ceiling = min(self.base_delay * (self.factor ** (attempt - 1)), self.max_delay)
        return random.uniform(0.0, ceiling)


class NodeTimeoutError(TimeoutError):
    """Caller-side node timeout; underlying worker thread may continue."""


def run_with_timeout(fn: Callable[[], Any], timeout_seconds: Optional[float]) -> Any:
    """Execute ``fn`` in one worker thread and bound caller wait time."""
    if timeout_seconds is None:
        return fn()
    timeout = float(timeout_seconds)
    if timeout <= 0:
        raise ValueError("timeout_seconds must be > 0")
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = executor.submit(fn)
    try:
        return future.result(timeout=timeout)
    except concurrent.futures.TimeoutError as exc:
        future.cancel()
        raise NodeTimeoutError(f"node execution exceeded {timeout}s caller timeout") from exc
    finally:
        executor.shutdown(wait=False, cancel_futures=True)


def run_with_retry(
    fn: Callable[[], Any],
    policy: RetryPolicy,
    on_retry: Optional[Callable[[int, BaseException, float], None]] = None,
) -> Any:
    """Run with bounded retry of explicitly transient exceptions only."""
    for attempt in range(1, policy.max_attempts + 1):
        try:
            return fn()
        except Exception as exc:
            if classify_error(exc) != "transient" or attempt >= policy.max_attempts:
                raise
            delay = policy.delay_for(attempt)
            if on_retry:
                on_retry(attempt, exc, delay)
            time.sleep(delay)
    raise RuntimeError("unreachable retry state")
