# Epistemic Pipeline

> 面向科研工程的状态机执行、claim/evidence/conflict 结构、运行时约束、恢复、溯源与 claim-level audit 层  
> Evidence-aware state-machine execution with claim-level verification records for research workflows

[Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Claim Audit Contract](CLAIM_AUDIT_CONTRACT.md) · [Four-Day Consolidation](FOUR_DAY_CONSOLIDATION.md) · [Frontier Alignment](FRONTIER_ALIGNMENT.md) · [Customization](CUSTOMIZATION_GUIDE.md) · [Examples](examples/README.md)

---

## 简体中文

### 当前定位

Epistemic Pipeline 不是“多个 Agent 排队聊天”的框架，也不是 scientific truth oracle

它把科研分析过程拆成可检查的执行与证据结构：

```text
discover -> analyze -> verify -> synthesize -> archive
```

核心问题不是“用了几个 Agent”，而是：

- 输入、状态和依赖是否明确
- provider 输出是否满足机器可读 runtime policy
- claim / evidence / conflict 是否保持分离
- claim 到底绑定了哪些 source / evidence
- verify 阶段记录了哪些 consistency / conflict observations
- 初始和最终 `[0,1]` heuristic score 到底是什么语义
- run 是否能 trace / checkpoint / resume
- provenance、claim audit 和 cross-tool evidence handoff 是否保持不同职责
- provider / human-review context 是否被显式声明

### Day-4 规范主链

```text
upstream artifact / evidence refs
        ↓
Graph + State Definition
        ↓
Role Binding + LLMProvider contract
        ↓
RuntimePolicyEvaluator @1
        ↓
claim / evidence / conflict structures
        ↓
initial heuristic scores @ verify
        ↓
final heuristic scores @ synthesize
        ↓
Trace @2 + Checkpoint @2
        ↓
PROV-aligned lineage @2
        ↓
Claim Verification @1
        ↓
Evidence Envelope @2
```

### 已接入能力

- **DAG 执行**：`linear` / `parallel` / `diamond` 可执行；`adaptive` 仍是实验性规格
- **图身份**：`graph_id` + canonical graph SHA-256；checkpoint resume 不仅相信同名 ID
- **Provider 解耦**：`LLMProvider.complete(system, user, schema) -> dict`
- **Provider disclosure**：`LLMProvider.describe()` 暴露有界 provider/model/process 元数据；默认 `MockProvider` 明确是 synthetic fixture
- **运行时策略**：state YAML 使用 machine-readable `runtime_policies`; 人类 `rule` 文本不参与执行
- **启发式 score network**：同步 bounded weighted propagation，不是 Bayesian posterior
- **弹性执行**：transient/permanent 分类、指数退避+jitter、caller-side timeout
- **checkpoint**：`epistemic-pipeline/checkpoint@2`，原子写入并绑定 graph digest
- **trace**：`epistemic-pipeline/trace@2` 项目 JSONL；借用适用的 OTel GenAI 命名，但不是 exporter/span 实现
- **provenance**：`epistemic-pipeline/prov@2`，W3C PROV-aligned project JSON，不是 PROV-O RDF
- **claim index**：`epistemic-pipeline/claim-index@1`，只索引 claim ID/source/evidence refs，不复制完整 claim prose
- **claim verification**：`epistemic-pipeline/claim-verification@1`，把 claim 的 evidence、consistency、conflict、score evolution 和 process context 分开记录
- **evidence envelope**：`epistemic-pipeline/evidence-envelope@2`，汇总 graph/trace/checkpoint/provenance/claim-audit 与 upstream refs 成跨工具 handoff index

## 为什么新增 Claim Verification

`verify` state 以前已经输出：

```text
internal_consistency_report
cross_source_matrix
conflict_registry
confidence_seed
coverage
```

但这些只存在于运行输出里，并没有形成独立、可携带的 claim-level audit artifact

2026-08-27 新增：

```text
epistemic-pipeline/claim-verification@1
```

它故意**不输出**：

```text
verified: true
```

因为“核验”不是一个 boolean 科学真值标签

每条 claim 可以分别记录：

```text
claim_id
source_refs[]
evidence_refs[]
evidence_relations[]
internal_consistency observation
cross_source observation
conflicts[]
heuristic_scores.initial
heuristic_scores.final
audit_state
provider / human-review context
```

### audit_state 的真实含义

当前 descriptive states：

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

它们只说明**运行时留下了什么审计结构**

它们不表示：

```text
accepted by science
rejected by science
true
false
peer reviewed
statistically valid
causally valid
```

### Initial / Final heuristic score

claim audit 同时保存：

```text
initial score @ verify
final score @ synthesize
```

两者都是：

> bounded/runtime heuristic score observation

不是：

- calibrated probability
- posterior probability
- truth score
- confidence interval
- certainty

score 变高也不表示“真值概率变高”

## 推荐运行入口

低层执行：

```bash
python3 core/engine.py validate graphs/linear.yaml
python3 core/engine.py run graphs/linear.yaml
```

完整 evidence-bearing run：

```bash
python3 core/run_bundle.py graphs/linear.yaml
```

典型产物：

```text
traces/<run_id>.jsonl
checkpoints/<run_id>/checkpoint.json
provenance/<run_id>.prov.json
claim-audits/<run_id>.claim-audit.json
evidence/<run_id>.evidence.json
```

职责严格分开：

| 产物 | 回答的问题 |
|---|---|
| trace | 运行过程中发生了什么 |
| checkpoint | 哪些成功节点可在同一 graph digest 下复用 |
| provenance | Entity / Activity / Agent 之间如何形成 lineage |
| claim audit | 每个 claim 绑定了什么 evidence、记录了什么检查/冲突/score 观察 |
| evidence envelope | 这次 run 的跨工具引用、profiles、upstream refs 与科学边界是什么 |

## 从 Auto Doc 接入上游 Artifact

`run_bundle.py` 支持 repeatable：

```bash
python3 core/run_bundle.py graphs/linear.yaml \
  --upstream-artifact-ref ../auto-doc-engine/output/report.artifact.json \
  --upstream-evidence-ref ../auto-doc-engine/output/ro-crate-metadata.json
```

也可以传 URI/opaque reference

解析边界：

```text
存在的本地文件 -> hash
URI -> opaque，不联网解引用
其他 unresolved string -> 保留 unresolved/opaque
```

`upstream artifact/evidence ref` 只建立 handoff/context

它不会自动继承上游的：

- scientific validity
- source credibility
- peer review
- authorship

## Runtime Policy，不是真理门禁

示例：

```yaml
runtime_policies:
  - id: evidence_linked
    check: claim_evidence_ratio
    claims_field: claims_registry
    evidence_field: evidence_chains
    min_ratio: 0.8
```

Python 只执行 `check` 与参数，不解析中文规则 prose

policy pass 只表示：

> 声明的 machine predicate 在当前 structured output 上成立

它不表示：

```text
结论为真
来源可靠
同行评审完成
统计设计正确
scientific validity established
```

历史 `Gatekeeper` / `quality_gates` / `check_quality_gates()` / `use_gatekeeper` 仅兼容旧调用；当前术语是 **runtime policy / constraint evaluation**

## Score 与 convergence 边界

`synthesize` 的 `[0,1]` 数值是：

> **bounded weighted heuristic score**

`converged=True` 只表示数值迭代达到设定 delta 阈值

```text
heuristic score != probability
numerical convergence != epistemic certainty
```

`core/calibration.py` 提供 temperature-scaling **transform**；没有 labelled fit + independent evaluation 就不声称概率校准

## Trace 与 OpenTelemetry 边界

项目 trace：

```text
epistemic-pipeline/trace@2
```

当前原则：

- 可以借用适用的 `gen_ai.operation.name`
- 使用自己的 `epistemic.run.id` / `epistemic.node.id` / `epistemic.stage`
- local run ID 不等于 provider conversation/session ID
- JSONL start/end records 不是 OTel SDK Span Event objects
- hash chain 只建立现有 records 的内部顺序/哈希一致性，不是外部锚定 immutable ledger

GenAI semantic conventions 仍持续演化，所以仓库坚持 **selected naming alignment, not conformance claim**

## PROV 与 Evidence Envelope

`epistemic-pipeline/prov@2`：

- W3C PROV-aligned project JSON
- 不是 PROV-O RDF serializer
- 默认记录 hash + 结构元数据
- 不复制完整研究 payload

`epistemic-pipeline/evidence-envelope@2`：

- 不是 PROV 的替代品
- 不是外部标准
- 是跨工具 handoff/index
- 可引用 `claim-verification@1`
- 可引用 upstream artifact/evidence

Evidence Envelope 保持小，是为了不把它变成第二个 research database

## 2026-08-27 全球前沿借鉴

### Provenance grounds trust in autonomous science

Nature Computational Science 2026-08-20 强调 complete, re-openable provenance 作为纠错基础设施

借鉴：运行记录必须能重新打开和追溯

不借鉴成：provenance = truth

### Artifact-centered Claim-aware Observability

arXiv:2608.18312 强调仅记录 model call 不够，需要 artifact / claim / evidence / verification relations

这与当前五层拆分高度相邻：

```text
trace
provenance
claim index
claim verification
evidence envelope
```

### EarthVerse

arXiv:2608.23525 暴露一个关键问题：agent 可以局部步骤做得不错，但仍无法维持 evidence / scale / unit / calculation / interpretation 的端到端一致链

借鉴：不要从 final answer 反推中间过程正确；每个 transition 都要保留 identity/semantics

### Brain Researcher

arXiv:2608.19902 强调 analytic output 只有在替代方案被权衡、claim scope 被限制到 evidence 支持范围后，才成为 defensible claim，并引入 accepted / qualified / revised / blocked / rejected / deferred 等 scientific-review outcomes

借鉴：**claim qualification 是一等研究操作**

不直接照搬 review labels：本仓没有独立 scientific reviewer，因此当前 `audit_state` 只描述 runtime audit structure

### From Trajectories to Evidence

arXiv:2608.05235 的核心提醒：

> completed trajectory is not automatically evidence

它强调 artifact verification、execution validity/attribution 与 post-execution claim qualification

这直接支持本仓把：

```text
run success
runtime policy
claim audit
provenance
scientific validity
```

保持成不同语义层

详见 [FOUR_DAY_CONSOLIDATION.md](FOUR_DAY_CONSOLIDATION.md)

## Experimental 区

仍未接入 canonical engine：

- `anti_entropy.py`：normalized Shannon-entropy metric window
- `convergence.py`：momentum-style bounded heuristic updater
- `infinite_regression.py`：bounded recursive termination controller
- `neuro_symbolic.py`：caller-supplied predicate dispatcher
- `perception.py`：signal intake prototypes；HTTP/WebSocket 当前不执行真实网络 I/O
- `thread_collapse.py`：bounded hypothesis-score aggregator

**修正 Experimental 实现 != 升级为主链能力**

## 本地维护

```bash
python -m pip install pyyaml
make test
```

只是可选本地维护工具，不属于 GitHub 平台门禁，也不构成科学正确性证明

2026-08-27 四日总整合不以测试执行作为完成证据

## 科研完整性硬边界

```text
Structured output != truthful output
Runtime policy pass != scientific validity
Evidence bound != evidence sufficient
Consistency observed != truth
Conflict absent != correctness
Heuristic score != probability
Numerical convergence != certainty
Audit state != scientific acceptance
Provider identity != output validity
Human review != peer review
Provenance != truth
Checkpoint resume != independent reproduction
```

---

## English

### Positioning

Epistemic Pipeline is an **evidence-aware research execution and claim-audit layer**, not a generic multi-agent chat framework or scientific truth oracle.

Current Day-4 chain:

```text
upstream artifact/evidence refs
  -> Graph + State Definition
  -> LLMProvider / Role contract
  -> Runtime Policy Evaluation
  -> claim / evidence / conflict structures
  -> initial heuristic scores
  -> final heuristic scores
  -> Trace + Digest-bound Checkpoint
  -> PROV-aligned Lineage
  -> Claim Verification @1
  -> Evidence Envelope @2
```

### Claim Verification

`epistemic-pipeline/claim-verification@1` preserves claim-specific dimensions separately:

- claim identity;
- source/evidence refs;
- evidence relations;
- internal/cross-source observations;
- conflict records;
- initial/final heuristic scores;
- descriptive audit state;
- provider/human-review context.

It intentionally does **not** emit a scientific `verified=true` label.

### Evidence-bearing run

```bash
python3 core/run_bundle.py graphs/linear.yaml \
  --upstream-artifact-ref path/to/report.artifact.json \
  --human-review reviewed
```

Outputs can include:

```text
trace
checkpoint
provenance
claim audit
evidence envelope
```

Each artifact answers a different audit question.

### Hard boundaries

```text
Evidence binding != evidence sufficiency
Structural checking != scientific verification
Heuristic score != calibrated probability
Numerical convergence != certainty
Audit state != claim acceptance
Provider identity != output validity
Human review != peer review
Provenance != truth
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
- [Claim Audit Contract](CLAIM_AUDIT_CONTRACT.md)
- [Four-Day Consolidation](FOUR_DAY_CONSOLIDATION.md)
- [Frontier Alignment](FRONTIER_ALIGNMENT.md)
- [Customization Guide](CUSTOMIZATION_GUIDE.md)
- [Examples](examples/README.md)
- [Agent Guide](AGENTS.md)
- [Manifest](MANIFEST.yaml)

## License

MIT License
