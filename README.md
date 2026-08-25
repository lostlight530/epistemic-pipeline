# Epistemic Pipeline

> 面向科研工程的状态机执行、证据关系、运行时约束、恢复与溯源层  
> Evidence-aware state-machine execution for research workflows

## 简体中文

### 当前定位

Epistemic Pipeline 不是“多个 Agent 排队聊天”的框架。它把科研分析过程拆成可检查的结构：

```text
discover -> analyze -> verify -> synthesize -> archive
```

核心问题不是“用了几个 Agent”，而是：

- 输入和依赖是否明确；
- provider 输出是否满足当前 state 的机器可读运行时约束；
- claim / evidence / conflict 是否保持分离；
- `[0,1]` 数值到底是什么语义；
- run 是否能被追踪、恢复和定位；
- claim 与 source/evidence 引用能否被下游发现；
- provider / human-review 过程信息是否被显式声明而不是猜测；
- provenance 与最终科研结论之间的边界是否清楚。

当前主链：

```text
Graph + State Definition
        ↓
Role Binding + LLMProvider contract
        ↓
RuntimePolicyEvaluator
        ↓
Bounded heuristic score network @ synthesize
        ↓
Trace + digest-bound checkpoint
        ↓
PROV-aligned lineage
        ↓
Claim index + process disclosure
        ↓
Evidence Envelope
```

### 已接入能力

- **DAG 执行**：`linear` / `parallel` / `diamond` 可执行；`adaptive` 仍是实验性规格
- **图身份**：执行图同时记录 `graph_id` 与 canonical SHA-256；checkpoint resume 不再只相信同名 ID
- **角色与 Provider 分离**：`LLMProvider.complete(system, user, schema) -> dict`；默认仍是 deterministic `MockProvider`
- **Provider disclosure**：`LLMProvider.describe() -> dict` 可声明 provider/model/version；基类不猜未知供应商字段
- **运行时策略**：state YAML 使用 `runtime_policies` + machine-readable `check`；人类 `rule` 文本不参与执行
- **启发式 score 网络**：同步迭代 bounded weighted score propagation；不是 Bayesian posterior
- **无 NumPy 核心依赖**：score propagation 与 temperature transform 使用 Python 标准库数学运算
- **弹性执行**：transient/permanent 分类、指数退避+jitter、caller-side timeout
- **checkpoint**：`epistemic-pipeline/checkpoint@2` 原子写入并绑定 graph SHA-256
- **trace**：`epistemic-pipeline/trace@2` 项目 JSONL；复用适用的 OpenTelemetry GenAI Development 命名，但不是 OTel exporter/span 实现
- **provenance**：`epistemic-pipeline/prov@2`，使用 W3C PROV Entity / Activity / Agent 与核心关系语义
- **claim index**：`epistemic-pipeline/claim-index@1` 只保留 claim identity + source/evidence refs，不复制 claim 正文
- **process disclosure**：`epistemic-pipeline/process-disclosure@1` 保存 provider 声明与 `human_review`
- **evidence envelope**：`epistemic-pipeline/evidence-envelope@2` 汇总 graph / trace / checkpoint / provenance、claim index、process disclosure 与 SHA-256，形成跨工具 handoff 对象

### 推荐运行入口

低层执行：

```bash
python3 core/engine.py validate graphs/linear.yaml
python3 core/engine.py run graphs/linear.yaml
```

需要研究运行证据包时：

```bash
python3 core/run_bundle.py graphs/linear.yaml
```

如果要显式记录本次 run 的人工审阅状态：

```bash
python3 core/run_bundle.py graphs/linear.yaml --human-review reviewed
```

`--human-review` 可选值：`reviewed` / `partial` / `not_reviewed` / `not_declared`。它不是 peer-review 状态，默认 `not_declared`。

它会按实际存在的产物形成：

```text
traces/<run_id>.jsonl
checkpoints/<run_id>/checkpoint.json
provenance/<run_id>.prov.json
evidence/<run_id>.evidence.json
```

这些文件的职责不同：

| 产物 | 回答的问题 |
|---|---|
| trace | 运行过程中发生了什么 |
| checkpoint | 哪些成功状态可以在同一图定义下复用 |
| provenance | 哪些 Entity / Activity / Agent 产生了哪些 lineage |
| evidence envelope | graph/artifact identity、claim↔evidence 索引、provider/review 声明与跨仓交接边界是什么 |

### Runtime policy，不是“真理门禁”

当前 state 使用：

```yaml
runtime_policies:
  - id: evidence_linked
    check: claim_evidence_ratio
    claims_field: claims_registry
    evidence_field: evidence_chains
    min_ratio: 0.8
```

Python 只执行 `check` 与参数，不解析中文规则句子。

一个 policy 通过只表示：

> 声明的机器 predicate 在当前结构化输出上成立

它**不表示**：

- 结论是真的；
- 来源可靠；
- peer review 已完成；
- scientific validity 已建立。

历史 `Gatekeeper` 类名、`check_quality_gates()` 与 `use_gatekeeper` 参数只为兼容旧调用保留；当前架构术语是 **runtime policy / constraint evaluation**。

### Score 与 convergence 的边界

`synthesize` 阶段的 `[0,1]` 数值是：

> **bounded weighted heuristic score**

不是：

- posterior probability；
- calibrated probability；
- truth score；
- 人类共识。

`converged=True` 只表示数值更新达到设定 delta 阈值。

`core/calibration.py` 提供 temperature-scaling **transform**。如果没有标注数据拟合 temperature 并做独立评估，就不能声称“完成概率校准”。

### OpenTelemetry 边界

2026-08-24 重新核对：OpenTelemetry GenAI agent/framework spans 仍为 **Development**，并定义 `create_agent`、`invoke_agent`、`invoke_workflow`、`plan`、`execute tool` 等操作。

本仓 `RunTracer`：

- 可复用适合的 `gen_ai.operation.name`；
- 使用项目自己的 `epistemic.run.id` / `epistemic.node.id` / `epistemic.stage`；
- **不再把本地 run_id 写成 provider conversation id**；
- JSONL start/end 是项目事件，不是 OTel Span Event API 对象。

### PROV、Claim Audit 与 Evidence Envelope

`epistemic-pipeline/prov@2` 是 **W3C PROV-aligned project JSON**，不是 PROV-O RDF serializer。

它默认只存：

- graph canonical/file SHA-256；
- node output canonical SHA-256 + keys/stage；
- trace/checkpoint 文件 SHA-256；
- `used` / `wasGeneratedBy` / `wasDerivedFrom` / `wasAssociatedWith` 等关系。

`evidence-envelope@2` 是项目自己的 handoff contract。相比 @1，它新增两个有边界的审计面：

1. **claim observability**：从 `claims_registry` / `evidence_chains` 提取 `claim_id`、claim record hash、source refs、evidence refs、relation，不复制 claim 正文；
2. **process disclosure**：记录 provider 的自声明 metadata 与显式 `human_review` 状态，不把 provider/model 名称或人工审阅升级成科学正确性证明。

详细字段见 [Claim-aware Audit Contract](CLAIM_AUDIT_CONTRACT.md)。

### Provider disclosure 的边界

外部 provider 可以重写：

```python
LLMProvider.describe() -> dict
```

基类只知道 Python provider class，不会猜 vendor/model/version。`MockProvider` 明确声明自己是本地 synthetic fixture，`external_model_call: false`。

```text
provider identity ≠ output authenticity proof
model name ≠ scientific validity
human review ≠ peer review
human review ≠ truth
```

### Experimental 区

这些文件仍然没有接入 canonical engine：

- `anti_entropy.py`：归一化 Shannon-entropy 指标窗口
- `convergence.py`：动量式 heuristic score updater
- `infinite_regression.py`：bounded recursive termination controller
- `neuro_symbolic.py`：caller-supplied local predicate dispatcher
- `perception.py`：signal intake prototypes；HTTP/WebSocket 当前不执行网络 I/O
- `thread_collapse.py`：hypothesis heuristic-score aggregator

**修正 Experimental 实现不等于把它升级为主链能力。**

### 本地维护工具

核心运行依赖只需要 PyYAML：

```bash
python -m pip install pyyaml
```

需要时可以手动：

```bash
make test
```

它只是本地检查工具，不属于 GitHub 平台门禁，也不构成科学正确性证明。

### 科研完整性

请把下面几句话当作仓库的硬边界：

```text
Structured output ≠ truthful output
Runtime policy pass ≠ scientific validity
Heuristic score ≠ probability
Numerical convergence ≠ certainty
Claim index ≠ truth graph
Provider/model identity ≠ output validity
Human review ≠ peer review
Provenance ≠ truth
Checkpoint resume ≠ independent reproduction
```

---

## English

### Positioning

Epistemic Pipeline is an **evidence-aware research execution layer**, not a generic “N agents chatting in sequence” framework.

```text
Graph + State Definition
  -> Role Binding + LLMProvider
  -> Runtime Policy Evaluation
  -> Bounded Heuristic Score Propagation
  -> Trace + Digest-bound Checkpoint
  -> PROV-aligned Lineage
  -> Claim Index + Process Disclosure
  -> Evidence Envelope
```

Implemented boundaries include executable linear/parallel/diamond DAGs, provider injection with a deterministic mock default, machine-readable runtime policies, graph-digest-bound resume, project JSONL traces, `prov@2` lineage, `claim-index@1`, `process-disclosure@1`, and `evidence-envelope@2` cross-tool handoff.

The claim index carries claim identity plus source/evidence references without copying claim prose. The process disclosure records provider-supplied metadata and an explicitly declared human-review state. Neither surface adjudicates truth, authorship, peer review, or scientific validity.

The score network is a synchronous bounded weighted heuristic. Its values are not calibrated probabilities; numerical convergence is not epistemic certainty.

The trace reuses selected Development-grade OpenTelemetry GenAI terminology where appropriate while keeping local run identity separate from provider conversation/session identity. The repository does not claim OTel SDK/exporter conformance.

The PROV profile is project JSON aligned with W3C PROV concepts and relations; it is not PROV-O RDF. The evidence envelope is a separate project-owned interoperability object.

### Entry points

```bash
python3 core/engine.py validate graphs/linear.yaml
python3 core/engine.py run graphs/linear.yaml
python3 core/run_bundle.py graphs/linear.yaml
python3 core/run_bundle.py graphs/linear.yaml --human-review reviewed
```

### Local maintenance

```bash
python -m pip install pyyaml
make test
```

Local checks are optional maintenance tools. They are neither GitHub merge policy nor scientific validation.

## Documentation

- [Architecture](ARCHITECTURE.md)
- [Research Contract](RESEARCH_CONTRACT.md)
- [Claim-aware Audit Contract](CLAIM_AUDIT_CONTRACT.md)
- [Frontier Alignment](FRONTIER_ALIGNMENT.md)
- [Customization Guide](CUSTOMIZATION_GUIDE.md)
- [Examples](examples/README.md)
- [Agent Guide](AGENTS.md)
- [Manifest](MANIFEST.yaml)

## License

MIT License
