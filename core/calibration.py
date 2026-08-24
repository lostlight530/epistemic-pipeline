#!/usr/bin/env python3
"""Optional monotone transform for bounded confidence-like scores.

The historical API calls this temperature scaling because it applies the usual
logit-domain temperature transform. In this repository, mock confidence values
are heuristic scores rather than calibrated probabilities. Applying this
function does not make them calibrated probabilities; fitting a temperature to
labelled prediction outcomes would be a separate empirical process.
"""

from __future__ import annotations

import math
from typing import Dict

_EPS = 1e-7


def _clamp01(value: float) -> float:
    return min(max(float(value), 0.0), 1.0)


def temperature_scale(confidence: float, temperature: float) -> float:
    """Apply a stable monotone logit-temperature transform to one score."""
    if temperature <= 0:
        raise ValueError(f"temperature must be > 0, got {temperature}")
    bounded = min(max(float(confidence), _EPS), 1.0 - _EPS)
    logit = math.log(bounded / (1.0 - bounded))
    z = logit / float(temperature)
    if z >= 0:
        scaled = 1.0 / (1.0 + math.exp(-z))
    else:
        exp_z = math.exp(z)
        scaled = exp_z / (1.0 + exp_z)
    return _clamp01(scaled)


def calibrate_confidence_map(confidences: Dict[str, float], temperature: float) -> Dict[str, float]:
    """Transform a claim-score mapping while preserving order for fixed ``T``."""
    return {claim_id: temperature_scale(value, temperature) for claim_id, value in confidences.items()}
