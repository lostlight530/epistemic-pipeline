#!/usr/bin/env python3
"""
置信度校准钩子 (Calibration)
Temperature scaling：单参数 logit 域缩放。
    calibrated = sigmoid(logit(c) / T)
  T = 1  恒等；T > 1 向 0.5 收缩（降温，更保守）；T < 1 向 0/1 锐化（升温）。

诚实边界：mock 阶段的置信度是启发值而非概率，本校准钩子仅提供
单调、保序、保 [0,1] 边界的数值变换接口；真实校准（用标注数据拟合 T）
需要真实模型输出与标签，当前阶段不做、也不宣称做了。
"""

import numpy as np

_EPS = 1e-7


def temperature_scale(confidence: float, temperature: float) -> float:
    """对单个置信度值做 temperature scaling，结果保持在 [0,1]"""
    if temperature <= 0:
        raise ValueError(f"temperature 必须为正数，got {temperature}")
    c = float(np.clip(confidence, _EPS, 1.0 - _EPS))
    logit = np.log(c / (1.0 - c))
    scaled = 1.0 / (1.0 + np.exp(-logit / temperature))
    return float(np.clip(scaled, 0.0, 1.0))


def calibrate_confidence_map(confidences: dict, temperature: float) -> dict:
    """对 {claim_id: confidence} 映射整体做 temperature scaling（保序单调变换）"""
    return {cid: temperature_scale(v, temperature) for cid, v in confidences.items()}
