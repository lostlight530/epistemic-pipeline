#!/usr/bin/env python3
"""
弹性执行策略 (Resilience)
- 错误分类：transient（可重试，如超时/连接错误） vs permanent（不可重试，如未实现/参数错误）
- 指数退避 + jitter 的重试策略（对齐 2025+ Agent 框架主流做法）
- 每节点超时：基于 future.result(timeout=) 实现

纯标准库（concurrent.futures + random + time），无第三方依赖。
"""

import concurrent.futures
import random
import time
from dataclasses import dataclass
from typing import Callable, Any

# transient：临时性故障，重试可能恢复
TRANSIENT_TYPES = (TimeoutError, ConnectionError, OSError)
# permanent：确定性故障，重试无意义（fail-fast）
PERMANENT_TYPES = (NotImplementedError, ValueError, KeyError, TypeError)


def classify_error(exc: BaseException) -> str:
    """将异常分类为 'transient' 或 'permanent'。未知异常按 transient 处理（保守重试）。"""
    if isinstance(exc, PERMANENT_TYPES):
        return 'permanent'
    if isinstance(exc, TRANSIENT_TYPES):
        return 'transient'
    return 'transient'


@dataclass
class RetryPolicy:
    """指数退避 + jitter 重试策略"""
    max_attempts: int = 1      # 总尝试次数（含首次），1 = 不重试
    base_delay: float = 0.1    # 首次重试前的基础等待秒数
    factor: float = 2.0        # 退避倍率
    max_delay: float = 30.0    # 单次等待上限

    @classmethod
    def from_node_spec(cls, spec: dict) -> 'RetryPolicy':
        """从 YAML 节点的 retry 字段构建；缺省/缺字段 = 不重试"""
        spec = spec or {}
        return cls(
            max_attempts=max(1, int(spec.get('max_attempts', 1))),
            base_delay=float(spec.get('base_delay', 0.1)),
            factor=float(spec.get('factor', 2.0)),
            max_delay=float(spec.get('max_delay', 30.0)),
        )

    def delay_for(self, attempt: int) -> float:
        """第 attempt 次失败后的等待时长（attempt 从 1 开始），全量 jitter"""
        base = min(self.base_delay * (self.factor ** (attempt - 1)), self.max_delay)
        return random.uniform(0, base)


class NodeTimeoutError(TimeoutError):
    """节点执行超过 timeout_seconds 时抛出（归类为 transient）"""


def run_with_timeout(fn: Callable[[], Any], timeout_seconds: float) -> Any:
    """
    在独立线程中执行 fn 并以 future.result(timeout=) 限时。
    已知边界：Python 线程无法被强制杀死，超时后后台线程仍会运行至结束，
    但调用方会立即收到 NodeTimeoutError，不会阻塞流水线。
    """
    if timeout_seconds is None:
        return fn()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = executor.submit(fn)
    try:
        return future.result(timeout=timeout_seconds)
    except concurrent.futures.TimeoutError:
        future.cancel()
        raise NodeTimeoutError(f"节点执行超过 {timeout_seconds}s 时限")
    finally:
        executor.shutdown(wait=False)


def run_with_retry(fn: Callable[[], Any], policy: RetryPolicy,
                   on_retry: Callable[[int, BaseException, float], None] = None) -> Any:
    """
    按策略执行 fn：transient 错误指数退避重试，permanent 错误立即抛出。
    on_retry(attempt, exc, delay) 用于日志/轨迹记录。
    """
    for attempt in range(1, policy.max_attempts + 1):
        try:
            return fn()
        except Exception as exc:
            if classify_error(exc) == 'permanent' or attempt >= policy.max_attempts:
                raise
            delay = policy.delay_for(attempt)
            if on_retry:
                on_retry(attempt, exc, delay)
            time.sleep(delay)
