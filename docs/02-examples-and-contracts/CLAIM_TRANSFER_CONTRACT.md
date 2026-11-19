> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `CONTRACT`
> - **Role:** Current bounded claim-transfer contract with explicit non-inheritance constraints
> - **Authority:** Current repository-native authority for the epistemic semantics explicitly owned by this file; current implementation and machine contracts remain the executable-behavior boundary
> - **Current meaning:** Read this subject inside the `claim identity → evidence/observation → audit → bounded transfer → evidence envelope` chain. The repository records structure, provenance and descriptive audit state rather than universal scientific verdicts
> - **Evidence / implementation boundary:** Indexed does not mean true; evidence linked does not mean sufficient; structured verification does not mean scientific verification; conflict absence does not mean corroboration; heuristic score does not mean calibrated probability; transfer does not mean acceptance; provider metadata does not mean vendor certification
> - **Cross-document relation:** Architecture integrates runtime/evidence planes; specialized contracts own claim-audit and transfer semantics; current code/machine contracts bound implementation; `DOCUMENT_STATUS.md` separates current contracts from historical snapshots
> - **Update trigger:** Update when owned claim/evidence semantics or implemented mechanics materially change, or when a confirmed cross-document/current-authority conflict appears
> - **Preservation rule:** Existing technical content and dated calibration remain intact. Closed-stage statements remain stage evidence and are not promoted into current runtime or scientific-validation claims

# Claim Transfer Contract — Epistemic Pipeline

## 中文技术对应 / Chinese subject counterpart

**具体责任 / Owning subject:** 跨仓传递必须使用精确源 profile 并保留原始命题身份、冲突与 unknown，不可隐式消歧或晋级

**English owner:** Claim Transfer Contract — Epistemic Pipeline

**可重复检查 / Reproducibility:** 应先固定 Graph/profile、state、checkpoint 及上下游 sidecar 的精确版本和 bytes，再按原文命令判断返回结果，不能把测试定义、Provider 说明或高分视为已经独立复现 / Freeze actual source and sidecar identity, execution inputs, real receipts and unknown outcomes, a declared audit cannot certify truth

| English chapter / 原章节 | 中文对应定位 / Chinese meaning |
| --- | --- |
| Purpose | 目标 |
| Stable profile | 该合同的实际规则、证据和失败范围 |
| Source-profile and selection semantics | 源 Profile 与选择语义 |
| Claim identity ambiguity preservation | 该合同的实际规则、证据和失败范围 |
| Transfer constraints | 传递约束 |
| Assertion basis | 该合同的实际规则、证据和失败范围 |
| Transfer coverage | 该合同的实际规则、证据和失败范围 |
| CLI | 该合同的实际规则、证据和失败范围 |
| Relationship to other evidence objects | 该合同的实际规则、证据和失败范围 |
| Downstream role | 该合同的实际规则、证据和失败范围 |
| Research calibration | 该合同的实际规则、证据和失败范围 |
| Maintenance / document status | 该合同的实际规则、证据和失败范围 |
| Hard boundaries | 该合同的实际规则、证据和失败范围 |
| Transfer-preservation contract: ambiguity survives selection | 该合同的实际规则、证据和失败范围 |

**保存不确定性 / Preserve unknowns:** 原始冲突、缺失来源、非概率 score 与失败注入观察保持各自身份，本节不新增科学或外部效果验证 / Historical and local evidence states are not silently promoted


**Status:** implemented project-owned handoff contract  
**Calibrated:** 2026-09-01  
**Implementation:** `core/claim_transfer.py`

## Purpose

`epistemic-pipeline/claim-transfer` packages selected records from an existing `epistemic-pipeline/claim-verification` sidecar for downstream research/communication workflows.

The transfer keeps context that is easy to lose when a claim ID is copied by itself:

```text
source refs
evidence refs / relations
structural observations
conflicts
claim origin / identity ambiguity
initial/final heuristic-score observations
audit state
transfer constraints
```

Full claim prose remains excluded by default.

## Stable profile

```text
epistemic-pipeline/claim-transfer
```

Project-owned identifiers remain unversioned.

## Source-profile and selection semantics

The source JSON must carry `epistemic-pipeline/claim-verification`. Wrong-profile JSON fails explicitly rather than being guessed into a claim audit.

A caller may select one or more claim IDs. A requested ID not present in the source claim audit fails explicitly rather than being silently manufactured.

Selecting a claim means only that the claim record is intentionally being handed to a downstream context. It does not mean accepted, verified, corroborated, publishable, or true.

## Claim identity ambiguity preservation

The transfer now preserves:

```text
origin_state_id
origin_state_ids[]
claim_origin_ambiguous
claim_record_sha256
claim_record_sha256s[]
claim_identity_ambiguous
```

If the source audit observed multiple origins or multiple structured claim hashes for one `claim_id`, that ambiguity must survive transfer unchanged.

```text
ambiguity preserved != ambiguity resolved
multiple record hashes != scientific contradiction
multiple origins != duplicate claim proved erroneous
```

## Transfer constraints

Every transferred claim carries:

```text
scientific_validity_inherited: false
evidence_sufficiency_inherited: false
peer_review_inherited: false
conflicts_must_remain_visible: true
claim_origin_ambiguity_must_remain_visible: true
claim_identity_ambiguity_must_remain_visible: true
heuristic_scores_must_retain_non_probability_semantics: true
```

These constraints prevent downstream systems from weakening epistemic boundaries during handoff.

## Assertion basis

The source sidecar is locally byte-identified. Claim fields are copied from that sidecar; optional purpose is caller-declared.

```text
claim_records: copied-from-local-claim-verification-sidecar
claim_identity_ambiguity: copied-without-adjudication
purpose: caller-declared | not_declared
basis_inferred: false
```

No model is asked to reinterpret the records.

## Transfer coverage

The sidecar records selected-claim count and counts for evidence refs, conflicts, structural observations, final heuristic scores, origin ambiguity, and identity ambiguity.

It also reports descriptive ambiguity ratios where claims are selected.

```text
aggregate_score: null
```

Coverage is not provenance soundness, evidence sufficiency, scientific validity, contradiction probability, or correctness probability.

## CLI

```bash
python core/claim_transfer.py \
  claim-audits/run-42.claim-audit.json \
  --claim-id claim_1 \
  --claim-id claim_2 \
  --purpose scientific-figure-handoff \
  --output transfers/run-42.claim-transfer.json
```

Without `--claim-id`, all indexed records are transferred.

## Relationship to other evidence objects

```text
claim-verification
        ↓ selection / bounded copy
claim-transfer
        ↓ downstream reference
figure / report / archive workflow
```

`claim-transfer` does not replace Trace, Checkpoint, PROV lineage, or Evidence Envelope.

## Downstream role

```text
epistemic-pipeline/claim-transfer
  -> sci-render-kit/figure-claim-audit
  -> sci-render-kit/figure-evidence
  -> sci-render-kit/communication-transfer
```

A downstream communication artifact may preserve claim context, but it does not inherit scientific validity, evidence sufficiency, peer review, or calibrated probability.

## Research calibration

Current calibration includes claim-level auditability, long-horizon process continuity, and process-level evaluation showing that final results can hide intermediate structural defects.

The implementation borrows only the persistence/visibility principle. It does not claim the source audit has established provenance soundness or scientific-review authority.

## Maintenance / document status

This is a current authoritative specialized contract under `DOCUMENT_STATUS.md`.

The August evidence-infrastructure stage closed on 2026-08-31. The 2026-09-01 repair preserves ambiguity more faithfully without reopening that stage.

## Hard boundaries

```text
Transfer != Acceptance
Claim ID != Truth
Identity ambiguity != Scientific contradiction
Evidence ref != Evidence sufficiency
Conflict visibility != Conflict adjudication
Audit state != Scientific verdict
Heuristic score != Probability
Inheritance != Validation
Maintenance clean != Scientific validity
```

## Transfer-preservation contract: ambiguity survives selection

`core/claim_transfer.py::_select_claims` retains each selected record's `claim_id`, origin state and source record hashes, identity/origin ambiguity flags, source and evidence references, structural observations, conflicts, heuristic-score observations and audit state. It raises `ValueError` when an explicitly requested claim ID was not present rather than constructing a placeholder claim.

The resulting `claim-transfer` object carries the exact source audit path plus its local SHA-256 digest. `payload_text_embedded=False`: the original claim prose is not copied into the transfer. A downstream consumer must recover the source sidecar and original claim text before asserting what exact proposition was transferred.

**Negative case:** two different claim records share one `claim_id`, a transfer retains both hashes/ambiguity, and a downstream UI displays only the string ID. The UI has dropped identity evidence; its displayed sentence cannot inherit scientific truth. Likewise `evidence_reference_ratio` counts selected claims with at least one evidence reference, not evidence sufficiency, credibility, probability or correctness.

Never treat transfer `purpose` or a downstream destination declaration as independent review, acceptance or fact verification.

## Fail-closed source-shape validation — 2026-11-20

The implementation validates the *source claim-verification sidecar* before copying records or measuring transfer coverage. A correct source profile alone does not make malformed claim structures safe to transfer

- `claims` may be omitted, null or an array, where omitted/null/empty represents zero declared indexed claims
- Every supplied claim-array element must be an object with a nonempty string `claim_id`, not silently skipped
- If supplied and non-null, `observations` and `heuristic_scores` must be objects
- If supplied and non-null, `conflicts` must be an array of objects, so declared conflict data cannot silently disappear
- Malformed shapes raise `ValueError` before output generation; the direct CLI returns a nonzero exit code with a concise error, without generating a misleading zero-claim or conflict-free transfer

This is shape preservation, **not** a claim-truth, score-calibration, evidence-sufficiency, provenance-soundness or peer-review validator
