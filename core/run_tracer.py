#!/usr/bin/env python3
"""
运行轨迹记录器 (RunTracer)
每个节点的开始/结束写入项目自有 JSONL 结构化审计记录，字段命名参考
OpenTelemetry GenAI semantic conventions（Development 级；GenAI 约定现已迁移到
独立 semantic-conventions-genai 仓库），仅对齐适用字段名，不依赖 OTel SDK。

这些 JSONL 记录不是 OpenTelemetry Span Event API 事件，也不声明完整 OTel span
兼容性；2026 年 OTel 已建议新事件转向与 span 关联的 Logs API。这里保留项目内部
start/end 事件模型，并通过 prev_hash 哈希链提供防篡改审计能力。

纯标准库实现（json + hashlib + time + threading），线程安全。
"""

import json
import hashlib
import threading
import time
from pathlib import Path
from typing import Optional

# OTel GenAI 字段来源：
# https://github.com/open-telemetry/semantic-conventions-genai/tree/main/docs/gen-ai
# 主 OpenTelemetry semantic-conventions 的旧 GenAI registry 已标记 moved/deprecated。
# 当前约定仍为 Development 级；这里只复用适用字段命名，不引入 OTel SDK。
OP_INVOKE_AGENT = "invoke_agent"


class RunTracer:
    """
    结构化运行轨迹记录器。

    每次 run 对应一个 JSONL 文件：traces/<run_id>.jsonl
    每行记录包含：
      - gen_ai.operation.name: 固定为 "invoke_agent"
      - gen_ai.agent.name:     节点 state_id
      - gen_ai.agent.stage:    节点阶段 (discover/analyze/...)
      - gen_ai.conversation.id:  run_id（关联同一次运行的所有记录）
      - event:                 "start" | "end"
      - duration_ms:           仅 end 事件，节点耗时（毫秒）
      - error.type:            仅失败 end 事件，异常/错误分类名
      - prev_hash / hash:      SHA-256 哈希链，任何篡改都会断链
    """

    def __init__(self, run_id: str, output_dir: str = 'traces'):
        self.run_id = run_id
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.path = self.output_dir / f"{run_id}.jsonl"
        self._lock = threading.Lock()
        self._starts = {}       # state_id -> start monotonic timestamp
        self._prev_hash = self._load_chain_head()

    def _load_chain_head(self) -> str:
        """续跑（resume）时从已有轨迹文件恢复链头，保证哈希链跨 run 延续。"""
        if not self.path.exists():
            return "GENESIS"
        last_hash = "GENESIS"
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        last_hash = json.loads(line).get('hash', last_hash)
                    except json.JSONDecodeError:
                        break  # 文件尾部损坏：拒绝在断链后续写
        return last_hash

    @staticmethod
    def _digest(record: dict) -> str:
        canonical = json.dumps(record, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(canonical.encode('utf-8')).hexdigest()

    def _append(self, record: dict):
        with self._lock:
            record['prev_hash'] = self._prev_hash
            record['hash'] = self._digest(record)
            with open(self.path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(record, ensure_ascii=False) + '\n')
            self._prev_hash = record['hash']

    def start_node(self, state_id: str, stage: str):
        with self._lock:
            self._starts[state_id] = time.monotonic()
        self._append({
            "timestamp": time.time(),
            "gen_ai.operation.name": OP_INVOKE_AGENT,
            "gen_ai.agent.name": state_id,
            "gen_ai.agent.stage": stage,
            "gen_ai.conversation.id": self.run_id,
            "event": "start",
        })

    def end_node(self, state_id: str, stage: str, status: str,
                 error_type: Optional[str] = None):
        with self._lock:
            started = self._starts.pop(state_id, None)
        duration_ms = round((time.monotonic() - started) * 1000, 3) if started else None
        record = {
            "timestamp": time.time(),
            "gen_ai.operation.name": OP_INVOKE_AGENT,
            "gen_ai.agent.name": state_id,
            "gen_ai.agent.stage": stage,
            "gen_ai.conversation.id": self.run_id,
            "event": "end",
            "status": status,
            "duration_ms": duration_ms,
        }
        if error_type:
            record["error.type"] = error_type
        self._append(record)

    @staticmethod
    def verify_chain(path: str) -> bool:
        """校验轨迹文件哈希链完整性；任何记录被篡改/删除/重排都会返回 False。"""
        prev = "GENESIS"
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                stored_hash = record.pop('hash', None)
                if record.get('prev_hash') != prev:
                    return False
                if RunTracer._digest(record) != stored_hash:
                    return False
                prev = stored_hash
        return True
