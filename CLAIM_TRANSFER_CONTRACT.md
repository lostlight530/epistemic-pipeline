# Claim Transfer Contract — Epistemic Pipeline

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
