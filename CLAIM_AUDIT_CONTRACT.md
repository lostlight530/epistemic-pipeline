# Claim Audit Contract — Epistemic Pipeline

**Calibration:** 2026-08-31  
**Implemented profile:** `epistemic-pipeline/claim-verification`  
**Scope:** claim identity, evidence bindings, structural observations, conflicts, heuristic scores, assertion basis, dimensional audit coverage, and process context

## Why a separate claim audit exists

Run telemetry answers when operations happened. Provenance answers lineage questions. Neither alone answers which claim had which evidence refs, observations, conflicts, scores, and audit coverage

`core/claim_audit.py` therefore writes a separate `<run_id>.claim-audit.json` sidecar

## It is not a truth graph

There is no universal `verified` boolean

```text
structurally checked != scientifically correct
evidence linked != evidence sufficient
no conflict recorded != independent corroboration
```

## Claim record fields

A normalized claim audit can contain

```text
claim_id
origin_state_id
claim_record_sha256
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

Full claim prose is not duplicated by default

## Audit states

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

These are descriptive process states, not `accepted`, `rejected`, `validated`, `confirmed`, `proven`, or other scientific-review verdicts

## Assertion / observation basis

Audit fields record how they entered the sidecar

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

## Structural observations

`internal_consistency_report` and `cross_source_matrix` are retained as provider/runtime observations. The audit layer does not independently rerun experiments or validate all sources

## Conflict records

Claim-linked conflict records retain relation/severity/other-ref plus a structure hash and `observation_basis: structured-verify-output`

A conflict hash identifies recorded conflict structure; it does not adjudicate which side is correct

## Heuristic scores

When available

```text
initial -> verify-stage observation
final   -> synthesize-stage observation
```

Both carry `observation_basis: structured-state-output` and remain heuristic values

```text
score != calibrated probability
score change != probability update
final score != truth score
```

## Dimensional audit coverage

The sidecar summarizes indexed-claim coverage for

```text
source refs
evidence refs
internal-consistency observations
cross-source observations
conflicts
initial heuristic scores
final heuristic scores
```

Each dimension can have a count and ratio over `claims_indexed`

Example

```text
evidence_refs_ratio = 0.80
```

means 80% of indexed claims carry at least one evidence reference in structured run output

It does not mean 80% correctness, evidence sufficiency, provenance soundness, or truth probability

```json
{"aggregate_score": null}
```

Coverage dimensions are not combined into an unsupported research-quality score

## Process context

Provider metadata carries explicit assertion basis. Unknown model/version stays `null`. MockProvider declares `synthetic-fixture-runtime`; no fake release version is invented

Human-review state is caller-declared when supplied

The current process path records

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

Claim Transfer preserves selected audit context and explicit non-inheritance constraints

Evidence Envelope remains compact and does not duplicate full claim audit content

```text
claim transfer != acceptance
evidence envelope != proof object
```

## Upstream/downstream role

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
        ↓
epistemic-pipeline/claim-verification
        ↓ optional claim-transfer / envelope reference
sci-render-kit research_context / figure evidence
```

References do not inherit truth

## Privacy and payload minimization

The audit stores IDs, hashes, and references rather than full claim/source prose by default. This limits payload duplication but is not a confidentiality guarantee

## Research calibration

Current research signals support separating audit dimensions from verdicts

- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- end-to-end scientific-agent consistency gaps
- claim-level auditability separating provenance coverage, provenance soundness, contradiction transparency, and audit effort
- long-horizon process evaluation showing terminal scores alone can hide where progress/regression occurs

This repository implements measurable coverage and explicit observation provenance. It does not claim provenance soundness or domain scientific-review authority

## Maintenance / document status

This is a current authoritative specialized contract under `DOCUMENT_STATUS.md`

Weekly/monthly maintenance may reconcile terminology, profile names, and evidence-stack references, but it must not rewrite historical claim-audit records or convert descriptive audit states into truth labels

The August evidence-infrastructure stage closed on 2026-08-31

```text
stage close != scientific validation
calendar-month close != reproduction
```

## Forbidden interpretations

```text
indexed_only -> false
structurally_checked -> true
no conflict -> corroborated
coverage ratio -> probability
coverage -> provenance soundness
human_review=reviewed -> peer reviewed
provider declared -> provider authenticated
claim_record_sha256 -> semantic truth
maintenance clean -> claim true
```
