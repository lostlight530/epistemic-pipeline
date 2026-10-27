# epistemic-pipeline 仓库纪念｜2026-10-28｜CS：知识表示、证据推理与可追踪科研状态机
# Repository Commemoration · 2026-10-28 · Computer Science: Knowledge Representation, Evidence Reasoning, and Traceable Research State Machines

> **Identity / 记录身份：** Independent bilingual commemorative disciplinary study · 独立新增的中英双语学科研究纪念；static inspection of repository-native scripts and research documents / 基于原生脚本与研究文档的静态核查；not a historical rewrite, runtime execution report, or certification / 不改写历史、不声称执行或认证。
>
> **CS2023 alignment / 学科坐标：** AI (Knowledge Representation/Reasoning); SE; DM; AL. These are scholarly comparisons, not endorsements or exact implementation equivalences / 研究分类而非外部机构背书或实现等价。

## 1. 专业归属：这是 CS 的哪一类？ / Disciplinary Position

**中文** — 这里的 CS 定位是**知识表示与推理、工作流状态机、证据溯源与约束执行的交叉工程**。一个科研任务经过 discover / analyze / verify / synthesize / archive 不应只剩下“Agent 成功”的一句话；Claim 与 Evidence 必须有独立身份，冲突必须可见，运行决策和学术判断必须区别。它探索的是把科研过程作为可解释、可恢复的状态转换对象。

**English** — This repository is a **junction of knowledge representation, evidence-oriented reasoning, workflow state machines, and traceable execution**. A discover/analyze/verify/synthesize/archive workflow must not collapse into a single 'agent succeeded' flag. Claims, evidence, conflicts, policy predicates, and execution observations have separate identities and epistemic meanings.

## 2. 仓库自身如何体现？ / Repository-native Architecture and Evidence

**中文** — `core/dependency_graph.py` 检查 DAG 依赖与排序；`core/engine.py` 的 `StateMachineEngine` 安排节点、调用受配置的 provider/harness、跟踪运行策略、checkpoint 和恢复；`core/claim_audit.py` 保留 Claim 身份、来源、冲突、观察与维度覆盖；`core/provenance.py`、`run_tracer.py`、`evidence_envelope.py` 分别记录来源关联、哈希链追踪和跨工具交接对象；`core/claim_transfer.py` 保留 selected claims 的非继承边界。原生架构解释在 `docs/01-source-and-explanation/ARCHITECTURE.md`。

**English** — `core/dependency_graph.py` validates task dependencies; `core/engine.py` implements a `StateMachineEngine` with provider/harness interaction, runtime-policy checks, tracing, checkpoint, and bounded resume semantics. `core/claim_audit.py` separates claim identity, evidence references, conflicts, observations, and coverage. `core/provenance.py`, `run_tracer.py`, and `evidence_envelope.py` distinguish provenance linkage, local hash-chain traces, and portable handoff objects. `core/claim_transfer.py` keeps transfer from becoming automatic authority inheritance. Native architecture is described in `docs/01-source-and-explanation/ARCHITECTURE.md`.

## 3. 人话解释 / In Plain Language

**中文** — 想象一次科研答辩：每个论断都要指出证据，每个实验要说明是否真的跑过，发现矛盾时要把矛盾留下来。**这仓相当于把答辩过程放进一个可追踪的流程引擎**，但评委仍需要审查证据是否真的支持结论。

**English** — Imagine a **research defense turned into an inspectable workflow**. Each claim points to its evidence, each task has a state and run trace, and disagreements stay visible. The workflow can organize the defense; it cannot replace the scientific jury or make a weak source true.

## 4. 如何读懂而不夸大？ / Verification and Non-claim Boundaries

**中文** — Claim 被索引不等于正确；evidence linked 不等于足够；启发式 score 不是统计意义上的校准概率；hash 链在缺少外部锚点和预期记录数时不能排除所有截尾；DAG 执行成功不等于实验独立复现。W3C PROV 提供 lineage 对照，并不意味着所有对象天然符合完整标准。

**English** — Indexed claims are not necessarily true; bound evidence can be insufficient; heuristic confidence is not calibrated probability. A trace hash chain without an independent anchor or expected length cannot reveal every tail truncation. A completed DAG is not independent scientific reproduction. W3C PROV offers provenance vocabulary, not a blanket standards certification.

## 5. 十仓中的独特贡献 / Place in the Ten-repository Research System

**中文** — 它是十仓中的**科研论断与执行状态桥梁**：文档引擎定义产物，科研状态机组织 Claim/Evidence，图件工具表达研究内容。跨仓传递是结构与来源交接，不继承真值。

**English** — It is the **bridge between research claims and execution state**. Artifact engineering records documents, Epistemic Pipeline organizes claims and evidence, and Sci Render handles figure communication. Transporting context never automatically transports truth.

## 6. 纪念与升华 / Commemoration and Wider Meaning

**中文** — **复杂 Agent 系统越会生成结论，就越需要懂得把“说过”“查过”“算过”“证实过”拆成不同的事实。**

**English** — **The more readily agents generate conclusions, the more rigorously systems must distinguish what was said, retrieved, computed, and actually established.**

## 外部学科对照 / External Disciplinary Anchors

- [W3C PROV overview](https://www.w3.org/TR/prov-overview/)
- [CS2023: AI, Data Management, Software Engineering](https://csed.acm.org/knowledge-areas/)

> **Provenance / 证据说明：** GitHub repository-native artifacts were read at the 2026-10-28 review cutoff. External sources establish disciplinary context only; independent reproduction, external certification and newly executed tests are **NOT_CLAIMED**. / 原生文件按本次时间点核读；外部来源只用于学科对照；**不声称本轮重新执行测试、独立复现或第三方认证**。
