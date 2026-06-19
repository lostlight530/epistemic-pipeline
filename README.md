# epistemic-pipeline

> 认知流水线 — 状态机驱动的动态科研分析系统 | State-machine driven dynamic research analysis

## 核心差异 / Key Differences（vs `paper-pipeline`）

| 维度 / Dimension | paper-pipeline | epistemic-pipeline |
|------|----------------|-------------------|
| 执行单元 / Execution Unit | 固定 6 个 Agent（A0-A5）/ Fixed 6 agents | 动态状态机（5 states × N roles）/ Dynamic state machine |
| 通信方式 / Communication | 文件系统通信 / File system | 状态变迁 + 消息传递 / State transitions + message passing |
| 角色分配 / Role Assignment | 固化 / Hardcoded | 动态（根据任务类型自动选择）/ Dynamic, task-type auto-select |
| 依赖管理 / Dependency | 固化表 / Hardcoded table | 图依赖引擎（DAG，运行时计算）/ DAG engine, runtime computed |
| 可信度 / Confidence | 三级标记 🟢🟡🔴 / 3-tier labels | 置信度传播网络（0-1 连续值）/ Continuous propagation network |
| 质量验证 / QA | 10 项模板合规 / Template compliance | 认知验证（一致性/冲突/覆盖度）/ Epistemic validation |
| 哲学框架 / Philosophy | 五仓库矩阵（硬编码）/ Hardcoded matrix | 无默认框架，用户自定义 / User-defined, no defaults |
| 定时任务 / Scheduling | 10 个每日任务 / 10 daily cron | 事件驱动 + 可选 cron / Event-driven + optional cron |

## 核心概念 / Core Concepts

```
状态机 / State Machine     → 认知过程的阶段定义 / Cognitive stage definitions
角色模板 / Role Template   → 动态分配给状态的执行者能力包 / Dynamic executor capability packs
依赖图 / Dependency Graph  → 任务间的有向无环关系 / DAG relationships between tasks
置信度网络 / Confidence Net → 跨任务信息可信度传播 / Cross-task confidence propagation
认知框架 / Epistemic Frame → 用户自定义的价值判断体系 / User-defined evaluation framework
```

## 快速开始 / Quick Start

```bash
# 定义一个分析流水线 / Define an analysis pipeline
# graphs/literature-review.yaml
# 执行 / Execute
python core/engine.py run graphs/literature-review.yaml --inputs papers/
```

## 设计理念 / Design Philosophy

1. **状态机优先 / State Machine First**：认知过程是状态流转，不是固定角色流水线 / Cognition is state flow, not fixed role pipeline
2. **角色动态化 / Dynamic Roles**：同一状态可由不同角色执行，按任务匹配 / Same state, different roles, task-matched
3. **置信度传播 / Confidence Propagation**：连续值在网络中传播收敛，非离散标记 / Continuous values propagate in network
4. **图依赖 / Graph Dependency**：任务依赖是运行时计算 DAG，非硬编码 / Runtime-computed DAG, not hardcoded
5. **框架可插拔 / Pluggable Frame**：认知框架由用户定义，不硬编码 / User-defined epistemic frames

## 目录结构 / Directory Structure

```
epistemic-pipeline/
├── README.md
├── MANIFEST.yaml
├── core/                  ← 引擎核心 / Engine core
│   ├── engine.py          ← 状态机执行引擎 / State machine executor
│   ├── dependency_graph.py ← DAG 计算 / DAG computation
│   └── confidence_net.py   ← 置信度传播网络 / Confidence propagation
├── states/                ← 状态定义 / State definitions (5 core)
│   ├── discover.yaml        ← 发现：收集、扫描、检索 / Discover: collect, scan, search
│   ├── analyze.yaml         ← 分析：拆解、理解、结构化 / Analyze: decompose, understand, structure
│   ├── verify.yaml          ← 验证：交叉检查、一致性、冲突 / Verify: cross-check, consistency
│   ├── synthesize.yaml      ← 综合：聚合、洞察、报告 / Synthesize: aggregate, insight, report
│   └── archive.yaml         ← 归档：沉淀、元数据、溯源 / Archive: preserve, metadata, provenance
├── roles/                 ← 动态角色模板 / Dynamic role templates
│   ├── explorer.md        ← 探索者：发现阶段能力包 / Explorer: discovery capabilities
│   ├── analyst.md         ← 分析师：分析阶段能力包 / Analyst: analysis capabilities
│   ├── verifier.md        ← 验证者：验证阶段能力包 / Verifier: verification capabilities
│   ├── synthesizer.md     ← 综合者：综合阶段能力包 / Synthesizer: synthesis capabilities
│   └── auditor.md         ← 审计者：归档阶段能力包 / Auditor: archive capabilities
├── graphs/                ← 依赖图模板 / Dependency graph templates
│   ├── linear.yaml        ← 线性：串行执行 / Linear: serial execution
│   ├── parallel.yaml      ← 并行：分组并行 + 聚合 / Parallel: grouped + aggregation
│   ├── diamond.yaml       ← 菱形：分散 → 并行 → 聚合 / Diamond: scatter → parallel → gather
│   └── adaptive.yaml      ← 自适应：按输入规模动态选择 / Adaptive: scale-based auto-select
├── validators/            ← 验证规则 / Validation rules
│   ├── confidence.schema.yaml  ← 置信度网络 Schema
│   └── epistemic.rules.yaml    ← 认知规则 / Epistemic rules
└── tests/                 ← 测试 / Tests
    └── test_all.py
```

## 协议 / License

MIT
