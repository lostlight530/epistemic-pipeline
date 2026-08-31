# Claim Audit Contract — Epistemic Pipeline

**Calibration:** 2026-09-01  
**Implemented profile:** `epistemic-pipeline/claim-verification`  
**Scope:** claim identity, evidence bindings, structural observations, conflicts, heuristic scores, assertion basis, identity/origin ambiguity, dimensional audit coverage, and process context

## Why a separate claim audit exists

Run telemetry answers when operations happened. Provenance answers lineage questions. Neither alone answers which claim had which evidence refs, observations, conflicts, scores, identity ambiguity, and audit coverage.

`core/claim_audit.py` therefore writes a separate `<run_id>.claim-audit.json` sidecar.

## It is not a truth graph

There is no universal `verified` boolean.

```text
structurally checked != scientifically correct
evidence linked != evidence sufficient
no conflict recorded != independent corroboration
identity ambiguity != scientific contradiction
```

## Claim record fields

A normalized claim audit can contain:

```text
claim_id
origin_state_id
origin_state_ids[]
claim_origin_ambiguous
claim_record_sha256
claim_record_sha256s[]
claim_identity_ambiguous
source_refs[]
evidence_refs[]
evidence_relations[]
observations.internal_consistency
observations.cross_source
conflicts[]
heuristic_scores.initial
heuristic_scores.final
audit_state
observation_basis
```

Full claim prose is not duplicated by default.

## Claim identity / origin ambiguity

Before the 2026-09-01 repair, repeated `claim_id` values were merged while the first observed `origin_state_id` and `claim_record_sha256` remained in the singular fields. That could hide an important provenance ambiguity.

The current rule is explicit:

- every structured occurrence contributes its `state_id` to `origin_state_ids[]`;
- every structured claim record contributes its canonical SHA-256 to `claim_record_sha256s[]`;
- if exactly one origin exists, `origin_state_id` remains populated; otherwise it becomes `null` and `claim_origin_ambiguous: true`;
- if exactly one record hash exists, `claim_record_sha256` remains populated; otherwise it becomes `null` and `claim_identity_ambiguous: true`.

This is intentionally additive and conservative.

```text
same claim_id + multiple origins != automatically wrong claim
same claim_id + multiple record hashes != automatically scientific conflict
ambiguity recorded != ambiguity adjudicated
```

The audit state vocabulary is not changed by identity ambiguity. Scientific conflict remains a separate structured observation surface.

## Audit states

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

These are descriptive process states, not `accepted`, `rejected`, `validated`, `confirmed`, `proven`, or other scientific-review verdicts.

## Assertion / observation basis

| Surface | Basis |
|---|---|
| claim identity / source refs | `structured-analyze-output` |
| evidence refs / relations | `structured-analyze-output` |
| internal/cross-source observations | `structured-verify-output` |
| conflicts | `structured-verify-output` |
| heuristic scores | `structured-state-output` |
| provider metadata | provider-adapter / fixture runtime |
| human review | caller-declared when supplied |

```text
assertion basis != correctness
structured-verify-output != external scientific verification
provider-adapter-reported != vendor authentication
```

## Structural observations and conflicts

`internal_consistency_report` and `cross_source_matrix` are retained as provider/runtime observations. Conflict records retain relation/severity/other-ref plus structure hash.

A conflict hash identifies recorded structure; it does not adjudicate which side is correct.

## Heuristic scores

When available:

```text
initial -> verify-stage observation
final   -> synthesize-stage observation
```

```text
score != calibrated probability
score change != probability update
final score != truth score
```

## Dimensional audit coverage

Coverage now includes the previous dimensions plus:

```text
claims_with_origin_ambiguity
claims_with_identity_ambiguity
origin_ambiguity_ratio
identity_ambiguity_ratio
```

These ratios mean only that multiple structured origins or identities were observed for a claim ID.

```json
{"aggregate_score": null}
```

Coverage dimensions are not combined into an unsupported research-quality score.

## Process context

Unknown model/version stays `null`. MockProvider remains a synthetic fixture; no fake release version is invented. Human review is caller-declared when supplied.

```json
{"automatic_ai_detection_used": false}
```

```text
provider metadata != AI-text detection
human review != peer review
```

## Relationship to Claim Transfer and Evidence Envelope

```text
claim-verification
        ├─ selected bounded copy -> claim-transfer
        └─ reference/hash       -> evidence-envelope
```

Claim Transfer must preserve claim identity/origin ambiguity rather than collapsing it downstream.

Evidence Envelope remains compact and does not duplicate full claim audit content.

## Privacy and payload minimization

The audit stores IDs, hashes, and references rather than full claim/source prose by default. This limits payload duplication but is not a confidentiality guarantee.

## Research calibration

Current research signals continue to support process-level inspection rather than terminal-score-only evaluation. The 2026-09-01 repair is especially aligned with the narrow lesson that a final run state can hide intermediate structural ambiguity.

This repository implements explicit audit dimensions. It does not claim provenance soundness, citation correctness, domain scientific-review authority, or external verification.

## Maintenance / document status

This is a current authoritative specialized contract under `DOCUMENT_STATUS.md`.

The August evidence-infrastructure stage closed on 2026-08-31. This 2026-09-01 repair hardens the closed-stage implementation; it does not rewrite or reopen the stage.

## Forbidden interpretations

```text
indexed_only -> false
structurally_checked -> true
no conflict -> corroborated
identity ambiguity -> contradiction
coverage ratio -> probability
coverage -> provenance soundness
human_review=reviewed -> peer reviewed
provider declared -> provider authenticated
claim_record_sha256 -> semantic truth
maintenance clean -> claim true
```
