# epistemic-pipeline 示例 / Example

本目录包含 epistemic-pipeline 的认知流水线使用示例。

## 运行环境 / Prerequisites

```bash
pip install pyyaml numpy
```

CLI 接受 `action`（`run` / `validate`）、`graph`，以及可选的 `--resume-from <run_id>`（断点续跑）、`--checkpoint-dir`、`--trace-dir`；不支持 `--inputs`、`--workers`、`--threshold` 等选项；外部数据接入需要为 `core/llm_harness.py` 注入真实 `LLMProvider`（见 `CUSTOMIZATION_GUIDE.md`）。每次运行会产出 `traces/<run_id>.jsonl` 结构化轨迹与 `checkpoints/<run_id>/checkpoint.json` 检查点（均为 gitignored 运行产物）。

## 示例：文献综述流水线 / Literature Review Pipeline

```bash
# 1. 线性依赖图：5 个状态串行执行
python3 core/engine.py run graphs/linear.yaml

# 2. 并行依赖图：3 个 analyze 组经 ThreadPoolExecutor 并发执行
python3 core/engine.py run graphs/parallel.yaml

# 3. 菱形流水线：分散 → 并行验证 → 聚合
python3 core/engine.py run graphs/diamond.yaml

# 4. 仅校验图合法性（DAG 循环/不可达检测），不执行
python3 core/engine.py validate graphs/diamond.yaml
```

> **实验性 / Experimental**：`graphs/adaptive.yaml` 是"根据输入规模自动选择执行策略"的**路由规则规格**，不包含可执行的 `nodes` 定义，尚未接入主引擎。直接 `run` 会被引擎明确拒绝（fail-closed）。

## 流水线阶段 / Pipeline Stages

```
discover → analyze → verify → synthesize → archive
  收集      分析       验证       综合        归档
```

## 图模板选择 / Graph Template Guide

| 场景 | 图模板 | 说明 | 状态 |
|------|--------|------|------|
| 简单文献分析 | linear | 串行执行，适合 < 10 篇论文 | ✅ 可执行 |
| 批量对比分析 | parallel | 分组并行，适合 10-50 篇 | ✅ 可执行 |
| 深度综合研究 | diamond | 分散→并行→聚合，适合 > 50 篇 | ✅ 可执行 |
| 不确定性输入 | adaptive | 运行时根据规模自动选择 | ⚠️ 实验性，未接入执行链 |
