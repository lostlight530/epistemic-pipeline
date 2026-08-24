"""Experimental normalized-distribution metric window.

[EXPERIMENTAL] Not integrated into the main execution engine.

The historical ``AntiEntropyLens`` name is retained for compatibility. The
implementation computes normalized Shannon entropy over a caller-provided set
of non-negative numeric metrics, optionally subtracts a per-component baseline,
and emits threshold callbacks. It does **not** measure system disorder in a
physical sense, predict cascading failure, or infer causal system stability.
"""

from __future__ import annotations

import math
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Callable, Deque, Dict, List, Optional


@dataclass
class EntropyReading:
    timestamp: float
    entropy_score: float
    component: str
    indicators: Dict[str, float] = field(default_factory=dict)


class AntiEntropyLens:
    """Bounded window of normalized Shannon-entropy indicator summaries."""

    def __init__(
        self,
        warning_threshold: float = 0.6,
        critical_threshold: float = 0.8,
        window_size: int = 100,
    ):
        if not 0 <= warning_threshold <= 1 or not 0 <= critical_threshold <= 1:
            raise ValueError("thresholds must be within [0,1]")
        if warning_threshold > critical_threshold:
            raise ValueError("warning_threshold must be <= critical_threshold")
        if window_size < 1:
            raise ValueError("window_size must be >= 1")
        self.warning_threshold = float(warning_threshold)
        self.critical_threshold = float(critical_threshold)
        self.window_size = int(window_size)
        self._readings: Deque[EntropyReading] = deque(maxlen=window_size)
        self._baselines: Dict[str, float] = {}
        self._alert_callbacks: List[Callable[[str, EntropyReading], Any]] = []

    def set_baseline(self, component: str, baseline_entropy: float) -> None:
        value = float(baseline_entropy)
        if not 0 <= value <= 1:
            raise ValueError("baseline_entropy must be within [0,1]")
        self._baselines[component] = value

    def register_alert_callback(self, callback: Callable[[str, EntropyReading], Any]) -> None:
        if not callable(callback):
            raise TypeError("callback must be callable")
        self._alert_callbacks.append(callback)

    def observe(self, component: str, metrics: Dict[str, float]) -> EntropyReading:
        if not isinstance(metrics, dict):
            raise TypeError("metrics must be a mapping")
        normalized_metrics: Dict[str, float] = {}
        for key, raw in metrics.items():
            value = float(raw)
            if value < 0:
                raise ValueError("entropy inputs must be non-negative")
            normalized_metrics[str(key)] = value
        entropy = self._compute_entropy(normalized_metrics)
        baseline = self._baselines.get(component, 0.0)
        score = min(max(entropy - baseline, 0.0), 1.0)
        reading = EntropyReading(time.time(), score, component, normalized_metrics)
        self._readings.append(reading)
        if score >= self.critical_threshold:
            self._trigger_alerts("CRITICAL", reading)
        elif score >= self.warning_threshold:
            self._trigger_alerts("WARNING", reading)
        return reading

    @staticmethod
    def _compute_entropy(metrics: Dict[str, float]) -> float:
        values = list(metrics.values())
        total = sum(values)
        if not values or total <= 0:
            return 0.0
        probabilities = [value / total for value in values if value > 0]
        entropy = -sum(probability * math.log2(probability) for probability in probabilities)
        maximum = math.log2(len(values)) if len(values) > 1 else 1.0
        return entropy / maximum if maximum > 0 else 0.0

    def _trigger_alerts(self, level: str, reading: EntropyReading) -> None:
        for callback in self._alert_callbacks:
            try:
                callback(level, reading)
            except Exception:
                # An observation callback must not alter the metric result.
                continue

    def stability_trend(self) -> str:
        """Return a descriptive first-half vs second-half score trend label."""
        if len(self._readings) < 3:
            return "INSUFFICIENT_DATA"
        readings = list(self._readings)
        midpoint = len(readings) // 2
        first = sum(item.entropy_score for item in readings[:midpoint]) / midpoint
        second = sum(item.entropy_score for item in readings[midpoint:]) / (len(readings) - midpoint)
        delta = second - first
        if delta > 0.1:
            return "INCREASING_SCORE"
        if delta < -0.1:
            return "DECREASING_SCORE"
        return "STABLE_SCORE"

    def get_readings(self, component: Optional[str] = None) -> List[EntropyReading]:
        if component is None:
            return list(self._readings)
        return [item for item in self._readings if item.component == component]

    def stats(self) -> Dict[str, Any]:
        return {
            "readings": len(self._readings),
            "components": sorted({item.component for item in self._readings}),
            "warning_threshold": self.warning_threshold,
            "critical_threshold": self.critical_threshold,
            "semantics": "normalized Shannon-entropy indicator only",
            "experimental": True,
        }
