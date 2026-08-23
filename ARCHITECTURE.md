# 架构设计与科研边界 / Architecture Design & Research Boundaries

> 当前架构校准日期 / Calibration date: 2026-08-23

`epistemic-pipeline` 是一个**状态机驱动、DAG 编排、有界质量门、可恢复运行轨迹**的科研分析参考系统。它组织研究过程与证据流，但不把结构化输出、数值收敛或模型回答自动提升为科学真理。

`epistemic-pipeline` is a **state-machine-driven, DAG-orchestrated research-analysis reference system with bounded quality gates and recoverable run traces**. It structures research execution and evidence flow; it does not automatically promote structured output, numerical convergence, or model responses into scientific truth.

---

## 1. 规范数据流 / Canonical data flow

```text
validated graph + declared inputs
            |
            v
role binding + provider execution
            |
            v
state-specific executable quality gates
            |
            v
evidence extraction + bounded confidence propagation
            |
            v
trace + checkpoint + terminal result
```

这条链描述当前主引擎的组合关系。`graphs/adaptive.yaml` 仍属于实验性资产，不能因为文件存在就被表述为已经接入规范执行链。

This flow describes the current main-chain composition. `graphs/adaptive.yaml` remains experimental; file presence alone does not make it part of the canonical execution chain.

## 2. Control Plane / 控制平面

核心组件：`core/engine.py`、`core/dependency_graph.py`、`core/gatekeeper.py`、`core/resilience.py`。

### 2.1 DAG 与并行

执行图通过显式依赖形成 DAG。满足依赖的同层节点可以并行执行；并行组中某个节点失败时，已经完成的兄弟节点结果可保留在失败上下文中。

并行执行只说明调度关系，不说明并行节点之间不存在语义依赖，也不保证外部副作用自动幂等。

### 2.2 Gatekeeper 的真实语义

旧文档曾把 Gatekeeper 描述成“执行 `epistemic.rules.yaml` 中的通用规则”。这超过了当前实现。

`core/gatekeeper.py` 的实际边界是：

1. 初始化时会加载 `validators/epistemic.rules.yaml`；
2. `check_quality_gates()` 的可执行检查仍通过 `state_id.startswith(...)` 的状态前缀分支，以及已识别的 gate ID / rule 文本进行显式分派；
3. 当前不存在一个可以把任意 YAML 规则自动解释为可执行策略的通用规则解释器。

因此，新状态前缀必须增加对应代码分支与契约测试。仅把规则写进 YAML 不能被描述为“已强制执行”。

The rules file is loaded, but executable enforcement is currently implemented through explicit state-prefix branches and recognized gates. There is no generic YAML policy interpreter. A newly declared rule is not enforced merely because it exists in configuration.

### 2.3 弹性执行与恢复边界

节点可以声明有限重试与超时。永久错误应 fail-fast；被分类为 transient 的错误可在预算内重试。

检查点允许复用已成功节点并重跑失败及其下游；跨图 resume 会 fail-closed。恢复能力不等于外部工具调用、网络请求或未来真实 provider 的副作用天然幂等，这仍需要调用方或具体适配器证明。

## 3. Execution Plane / 执行平面

核心组件：`core/llm_harness.py`、`roles/*.md`、`states/*.yaml`。

`LLMProvider.complete(system, user, schema) -> dict` 提供 provider 抽象；当前默认 `MockProvider` 用于确定性契约路径，真实 LLM provider 仍不是仓库的内建生产能力。

JSON Schema 和结构化输出契约可以降低**格式漂移**并拒绝不符合结构的输出，但不能“彻底解决幻觉”。结构正确与语义正确是两件不同的事。

Structured schemas constrain shape; they do not establish factual correctness, source validity, or reasoning quality.

## 4. Evidence & Confidence Plane / 证据与置信度平面

核心组件：`core/knowledge_extractor.py`、`core/confidence_net.py`、`core/calibration.py`、`validators/*`。

### 4.1 当前置信度传播不是 Bayesian posterior

`core/confidence_net.py` 实现的是一个**受限加权迭代启发式**，受简化 belief-propagation 思路启发。它把关系类型转换后的邻居值按权重组合，再与节点初始值混合，并将结果限制在 `[0, 1]`。

概念上可写为：

```text
new_value = clip((initial + weighted_neighbor_influence) / (1 + total_weight), 0, 1)
```

这不是 Bayesian network 后验推断器，也没有因为取值在 `[0,1]` 就自动成为概率。

### 4.2 “收敛”的严格含义

当前收敛只表示：在给定图、初值、关系、阈值与最大迭代次数下，数值更新的最大变化进入配置阈值。

它不表示：

- 多个研究来源达成事实共识；
- 结论已经被证实；
- 系统可靠性被证明；
- 置信度已经经过统计校准。

可选 temperature scaling 也只是校准机制。只有在明确的校准数据集、目标定义、拟合过程、指标和留出评估存在时，才能作实际 calibration claim。

## 5. Observability Plane / 可观测性平面

核心组件：`core/run_tracer.py`。

每个节点的结构化运行记录用于追踪操作、错误、耗时和 run 关联；SHA-256 链用于检测记录内容被修改、删除或重排的情况。

### 5.1 Hash chain 的边界

哈希链是 **tamper-evident**，不是：

- 数字签名；
- 外部可信时间戳；
- append-only 存储证明；
- 不可删除的审计账本。

### 5.2 OpenTelemetry GenAI 对齐边界

截至 2026-08-23，OpenTelemetry 的 GenAI semantic conventions 已迁移到独立的 `open-telemetry/semantic-conventions-genai` 仓库继续维护。

本仓只声明**字段命名层面的参考对齐**，不声明已经接入 OpenTelemetry SDK、exporter 或完整 semantic-convention compliance。

特别地，本仓的 `run_id` 是本地运行/关联标识。未来若 provider 提供真正的 conversation/session ID，应与本地 run identity 分开建模，不能因为字段名相似就把本地 run 自动解释为 provider conversation。

## 6. Research Contract / 科研契约

根目录新增 [RESEARCH_CONTRACT.md](RESEARCH_CONTRACT.md)，用于统一以下边界：

```text
structured output != truthful output
numeric convergence != epistemic certainty
heuristic confidence != calibrated probability
passed gate != scientific validation
trace/checkpoint != immutable provenance
```

它同时定义与 `auto-doc-engine`、`sci-render-kit` 之间的**数据 handoff 契约**。这是接口思想，不是当前三个仓已经互相调用的声明。

## 7. Research-object interoperability / Research Object 互操作

RO-Crate 1.3 于 2026-06-22 发布为 Recommendation。对本仓来说，它是一个适合未来映射研究输入、运行、输出与上下文元数据的**proposed interoperability target**。

当前 JSONL trace、checkpoint 或任何 report 都不是 RO-Crate。只有在增加符合规范的 exporter/validator 与可执行测试后，才能把该状态升级为 implemented。

## 8. 可复现性分级 / Reproducibility levels

本仓采用本地项目术语：

- `R0 Traceable` — 有 run/evidence 引用；
- `R1 Replay-addressable` — 图、输入、配置、代码版本和确定性假设足以定位 replay；
- `R2 Environment-bounded` — 额外记录 provider、运行时、依赖版本和随机设置；
- `R3 Reproduced` — 已实际执行独立重跑并按声明判据比较。

这些不是外部标准。checkpoint 存在或 MockProvider 可确定运行，都不能单独证明 `R3`。

## 9. 架构 doctrine / Architecture doctrine

1. **可执行谓词高于规则文案。** YAML 声明与实际代码分支必须分开记录。
2. **结构约束不是语义真值。** Schema 能限制形状，不能验证事实。
3. **数值范围不是概率语义。** `[0,1]` 启发值必须显式标注其含义。
4. **恢复性不等于副作用幂等。** 外部系统必须单独定义幂等与重放边界。
5. **观测字段不等于标准合规。** 使用相似字段名时必须标明 alignment scope。
6. **实验资产不能靠文档升级为 integrated。** 进入主链需要代码接线与测试证据。
7. **跨仓协议优先保持松耦合。** 先统一 artifact/evidence/provenance 语义，再决定是否需要真正运行时集成。

## 10. 主要参考 / Primary references

检索日期 / Retrieved: 2026-08-23

- [OpenTelemetry GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai)
- [RO-Crate 1.3 Specification](https://www.researchobject.org/ro-crate/1.3/)
- [FAIR Principle R1.2](https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/)
