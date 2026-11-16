# 02 — Examples and Contracts

## 中文技术对应 / Chinese subject counterpart

**具体责任 / Owning subject:** 合同目录明确 Claim、审计、移交和不同级别的核验权威，不以 profile 存在代替本地测试

**English owner:** 02 — Examples and Contracts

**可重复检查 / Reproducibility:** 应先固定 Graph/profile、state、checkpoint 及上下游 sidecar 的精确版本和 bytes，再按原文命令判断返回结果，不能把测试定义、Provider 说明或高分视为已经独立复现 / Freeze actual source and sidecar identity, execution inputs, real receipts and unknown outcomes, a declared audit cannot certify truth

| English chapter / 原章节 | 中文对应定位 / Chinese meaning |
| --- | --- |
| Machine and capability surfaces | 该合同的实际规则、证据和失败范围 |
| Active contracts | 该合同的实际规则、证据和失败范围 |
| Cross-repository role | 该合同的实际规则、证据和失败范围 |
| Operator and contributor surfaces | 该合同的实际规则、证据和失败范围 |
| Scholarly metadata | 该合同的实际规则、证据和失败范围 |
| Reading path | 该合同的实际规则、证据和失败范围 |

**保存不确定性 / Preserve unknowns:** 原始冲突、缺失来源、非概率 score 与失败注入观察保持各自身份，本节不新增科学或外部效果验证 / Historical and local evidence states are not silently promoted


This class answers: **how are claims, evidence, audit state, transfer, and customization represented without silently strengthening scientific meaning?**

## Machine and capability surfaces

- root `MANIFEST.yaml` — machine-readable capability map.
- `validators/` — implemented structural/rule validation surfaces.
- `examples/` — supported representation examples.

Machine readability and validator success do not turn a claim into truth or an evidence link into sufficient support.

## Active contracts

### [`RESEARCH_CONTRACT.md`](./RESEARCH_CONTRACT.md)

Repository-wide evidence/execution semantics: claim state, source/evidence boundaries, runtime-policy interpretation, reproduction levels, and cross-repository non-inheritance.

### [`CLAIM_AUDIT_CONTRACT.md`](./CLAIM_AUDIT_CONTRACT.md)

Defines how a claim is structurally audited against declared evidence, observations, conflicts, and review state.

An audit can report coverage or a structural finding without establishing truth, peer review, or evidence sufficiency.

### [`CLAIM_TRANSFER_CONTRACT.md`](./CLAIM_TRANSFER_CONTRACT.md)

Defines bounded transfer of claim/evidence state between repository profiles.

```text
claim transfer != claim acceptance
reference carried forward != truth inherited
conflict preserved != contradiction resolved
```

Transfer must preserve source/evidence references, conflicts, score semantics, audit state, and unknown/missing status rather than cleaning them away.

### [`ASSERTION_BASIS_AND_AUDIT_COVERAGE.md`](./ASSERTION_BASIS_AND_AUDIT_COVERAGE.md)

Separates a field's value from how it was asserted/observed and separates audit coverage from correctness, quality, probability, or provenance soundness.

```text
assertion basis != correctness
coverage != quality
coverage ratio != probability
```

### [`CUSTOMIZATION_GUIDE.md`](./CUSTOMIZATION_GUIDE.md)

Shows how to adapt supported profiles/rules while retaining the repository's semantic boundaries. Customization is not permission to relabel heuristic scores as probabilities or imported references as trusted evidence.

### [CLAIM_IDENTITY_NEGATIVE_CASES.md](./CLAIM_IDENTITY_NEGATIVE_CASES.md)

Source-grounded counterexamples for claim-ID ambiguity, audit-state precedence, source/evidence reference multiplicity, and ambiguity-preserving transfer

**This is a durable research-method casebook, not an executed test log or historical maintenance account**

## Cross-repository role

In the three-repository research-infrastructure chain:

```text
auto-doc-engine artifact/provenance objects
        ↓
epistemic-pipeline claim/evidence interpretation and transfer
        ↓
sci-render-kit scientific communication
```

An upstream artifact identity is not automatically a verified claim. A downstream figure or communication object does not retroactively make the claim accepted or scientifically valid.

## Operator and contributor surfaces

- root `AGENTS.md` — repository-owned operational guidance.
- root `CONTRIBUTING.md` — public contribution guidance.
- `examples/` and `CUSTOMIZATION_GUIDE.md` — supported use/configuration examples.

These surfaces must remain consistent with the implementation and active contracts but do not outrank them.


### [INTEROPERABILITY_VERIFICATION.md](./INTEROPERABILITY_VERIFICATION.md)

Current producer/consumer fixture scope, Python environment pins, CodeMeta 4 migration boundaries, and (where applicable) failure injection or offline renderer verification — evidence of a test is separate from its execution

## Scholarly metadata

- root `CITATION.cff`
- root `codemeta.json`
- root `RELEASE_POLICY.md`
- root `LICENSE`

The repository DOI identifies an archived software publication. It does not verify claims, establish evidence sufficiency, calibrate heuristic scores into probabilities, authenticate providers, or self-award R3 independent reproduction.

## Reading path

For a new claim/evidence integration:

1. identify the owning implementation/validator and `MANIFEST.yaml` capability;
2. read `RESEARCH_CONTRACT.md` for repository-wide semantics;
3. read the specialized audit/transfer/assertion contract;
4. use `CUSTOMIZATION_GUIDE.md` and examples only within those boundaries;
5. retain revision-matched execution evidence when reporting that validation or transfer actually ran.

Architecture and implementation explanation live under [`../01-source-and-explanation/`](../01-source-and-explanation/). Maintenance/audit material in class 03 is operational/historical context, not claim truth.
