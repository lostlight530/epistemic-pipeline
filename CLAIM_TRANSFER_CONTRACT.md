# Claim Transfer Contract — Epistemic Pipeline

**Status:** implemented project-owned handoff contract  
**Calibrated:** 2026-08-29  
**Implementation:** `core/claim_transfer.py`

## Purpose

`epistemic-pipeline/claim-transfer` packages selected records from an existing `epistemic-pipeline/claim-verification` sidecar for downstream research/communication workflows.

The transfer keeps the context that is easy to lose when a claim ID is copied by itself:

```text
source refs
evidence refs / relations
structural observations
conflicts
initial/final heuristic-score observations
audit state
transfer constraints
```

Full claim prose remains excluded by default.

## Stable profile

```text
epistemic-pipeline/claim-transfer
```

## Selection semantics

A caller may select one or more claim IDs. A requested ID that is not present in the source claim audit fails explicitly rather than being silently manufactured.

Selecting a claim means only:

> this claim record is intentionally being handed to a downstream context.

It does not mean accepted, verified, corroborated, publishable or true.

## Transfer constraints

Every transferred claim carries:

```text
scientific_validity_inherited: false
evidence_sufficiency_inherited: false
peer_review_inherited: false
conflicts_must_remain_visible: true
heuristic_scores_must_retain_non_probability_semantics: true
```

These constraints prevent downstream systems from weakening the epistemic boundary during handoff.

## Assertion basis

The source sidecar is locally byte-identified. Claim fields are copied from that sidecar; optional purpose is caller-declared.

```text
claim_records: copied-from-local-claim-verification-sidecar
purpose: caller-declared | not_declared
basis_inferred: false
```

No model is asked to reinterpret the records.

## Transfer coverage

The sidecar records selected-claim count and counts for evidence refs, conflicts, structural observations and final heuristic scores.

```text
aggregate_score: null
```

Coverage is not provenance soundness, evidence sufficiency, scientific validity or probability.

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

`claim-transfer` does not replace Trace, Checkpoint, PROV lineage or Evidence Envelope. It is a portable subset contract for claim-level handoff.

## Global calibration

- **Praxist** (arXiv:2608.25955, 26 Aug 2026) highlights typed evidence/solution lineages that preserve validated mechanisms, unresolved claims and constraints across generations.
- **ReproAgent** (arXiv:2608.24291, 25 Aug 2026) demonstrates the value of persistent contracts that survive planning, generation and repair.
- **From Fluent to Verifiable** (arXiv:2602.13855) frames claim-level provenance, contradiction transparency and auditability as first-class concerns.

The implementation borrows the persistence/visibility principle only. It does not claim the source audit has established provenance soundness or scientific review authority.

## Hard boundaries

```text
Transfer != Acceptance
Claim ID != Truth
Evidence ref != Evidence sufficiency
Conflict visibility != Conflict adjudication
Audit state != Scientific verdict
Heuristic score != Probability
Inheritance != Validation
```
