"""
Anti-Entropy Observation Lens - System Stability Monitor

A diagnostic lens that observes the pipeline's entropy levels and
detects when the system is drifting toward chaos. Provides early
warning before cascading failures occur.

Real-world: System health monitoring with entropy-based stability metrics.
"""

import time
import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from collections import deque


@dataclass
class EntropyReading:
    """A single entropy observation reading."""
    timestamp: float
    entropy_score: float
    component: str
    indicators: Dict[str, float] = field(default_factory=dict)


class AntiEntropyLens:
    """Observes system entropy and provides stability diagnostics."""
    
    def __init__(
        self,
        warning_threshold: float = 0.6,
        critical_threshold: float = 0.8,
        window_size: int = 100
    ):
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold
        self.window_size = window_size
        self._readings: deque = deque(maxlen=window_size)
        self._baselines: Dict[str, float] = {}
        self._alert_callbacks: List[Any] = []
    
    def set_baseline(self, component: str, baseline_entropy: float) -> None:
        """Set the baseline entropy for a component."""
        self._baselines[component] = baseline_entropy
    
    def register_alert_callback(self, callback) -> None:
        """Register a callback for entropy alerts."""
        self._alert_callbacks.append(callback)
    
    def observe(self, component: str, metrics: Dict[str, float]) -> EntropyReading:
        """Observe a component and compute its entropy score."""
        entropy = self._compute_entropy(metrics)
        baseline = self._baselines.get(component, 0.0)
        normalized = max(0.0, min(1.0, entropy - baseline))
        
        reading = EntropyReading(
            timestamp=time.time(),
            entropy_score=normalized,
            component=component,
            indicators=metrics
        )
        self._readings.append(reading)
        
        if normalized >= self.critical_threshold:
            self._trigger_alerts("CRITICAL", reading)
        elif normalized >= self.warning_threshold:
            self._trigger_alerts("WARNING", reading)
        
        return reading
    
    def _compute_entropy(self, metrics: Dict[str, float]) -> float:
        """Compute Shannon entropy from metric distribution."""
        values = list(metrics.values())
        if not values or sum(values) == 0:
            return 0.0
        
        total = sum(values)
        probabilities = [v / total for v in values]
        
        entropy = 0.0
        for p in probabilities:
            if p > 0:
                entropy -= p * math.log2(p)
        
        max_entropy = math.log2(len(values)) if len(values) > 1 else 1.0
        return entropy / max_entropy if max_entropy > 0 else 0.0
    
    def _trigger_alerts(self, level: str, reading: EntropyReading) -> None:
        """Trigger alert callbacks."""
        for callback in self._alert_callbacks:
            try:
                callback(level, reading)
            except Exception:
                pass
    
    def stability_trend(self) -> str:
        """Analyze the trend of entropy over time."""
        if len(self._readings) < 3:
            return "INSUFFICIENT_DATA"
        
        recent = list(self._readings)
        mid = len(recent) // 2
        first_half = sum(r.entropy_score for r in recent[:mid]) / mid
        second_half = sum(r.entropy_score for r in recent[mid:]) / (len(recent) - mid)
        
        delta = second_half - first_half
        
        if delta > 0.1:
            return "DESTABILIZING"
        elif delta < -0.1:
            return "STABILIZING"
        else:
            return "STABLE"
    
    def get_readings(self, component: str = None) -> List[EntropyReading]:
        """Retrieve readings, optionally filtered by component."""
        if component:
            return [r for r in self._readings if r.component == component]
        return list(self._readings)
    
    def health_report(self) -> Dict[str, Any]:
        """Generate a comprehensive health report."""
        readings = list(self._readings)
        if not readings:
            return {"status": "NO_DATA"}
        
        avg_entropy = sum(r.entropy_score for r in readings) / len(readings)
        max_entropy = max(r.entropy_score for r in readings)
        trend = self.stability_trend()
        
        status = "HEALTHY"
        if avg_entropy >= self.critical_threshold:
            status = "CRITICAL"
        elif avg_entropy >= self.warning_threshold:
            status = "WARNING"
        
        return {
            "status": status,
            "avg_entropy": avg_entropy,
            "max_entropy": max_entropy,
            "trend": trend,
            "components_monitored": len(set(r.component for r in readings)),
            "total_readings": len(readings)
        }
