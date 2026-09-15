# Assertion Basis & Claim Audit Coverage — epistemic-pipeline

**Calibration:** 2026-08-31  
**Status:** implemented companion contract for `epistemic-pipeline/claim-verification`, `epistemic-pipeline/claim-transfer`, and `epistemic-pipeline/evidence-envelope`

## 1. Purpose

A claim audit is only useful if an auditor can distinguish

```text
what was recorded
where it came from
what was actually checked
what remains unknown
```

The repository separates assertion/observation basis from claim content, and audit coverage from scientific correctness

## 2. Assertion and observation bases

Current bases include

| Surface | Basis |
|---|---|
| claim identity / source refs | `structured-analyze-output` |
| evidence refs / evidence relations | `structured-analyze-output` |
| internal-consistency observation | `structured-verify-output` |
| cross-source observation | `structured-verify-output` |
| conflict record | `structured-verify-output` |
| heuristic score | `structured-state-output` |
| provider metadata | `provider-adapter-reported` |
| human-review state | `caller-declared` when supplied |
| local artifact/reference identity | runtime-observed local bytes/filesystem |
| transferred claim record | `copied-from-local-claim-verification-sidecar` |

These labels answer how a field entered the audit/transfer record. They do not make the value correct

```text
provider-adapter-reported != vendor-certified identity
structured-verify-output != external scientific verification
caller-declared review != peer review
copied-from-sidecar != independently reverified
```

## 3. Claim audit coverage

`claim-verification` emits dimensional coverage counts for indexed claims

- claims with source refs
- claims with evidence refs
- claims with internal-consistency observations
- claims with cross-source observations
- claims with conflict records
- claims with initial heuristic scores
- claims with final heuristic scores

Each dimension can report a ratio using `claims_indexed` as denominator

Example

```text
evidence_refs_ratio = 0.80
```

means 80% of indexed claims carry at least one evidence reference in structured run output

It does not mean

- 80% of claims are correct
- 80% of evidence is sufficient
- provenance soundness is 0.80
- citation accuracy is 80%
- calibrated probability of truth is 0.80

## 4. Claim-transfer coverage

`claim-transfer` reports coverage over the selected portable subset

```text
selected_claim_count
claims_with_evidence_refs
claims_with_conflicts
claims_with_structural_observations
claims_with_final_heuristic_score
```

Structural-observation counts are based on explicit internal-consistency / cross-source observations rather than descriptive metadata fields

Transfer coverage does not establish that the selected claims are fit for downstream acceptance

## 5. No aggregate audit score

The records deliberately emit

```json
{
  "aggregate_score": null
}
```

Source presence, evidence linkage, contradiction visibility, consistency observations, heuristic scores, and transfer presence are different dimensions. A scalar combination would require an explicit validated weighting/evaluation regime that this repository does not have

## 6. Evidence Envelope coverage

The Evidence Envelope remains an index. It does not duplicate full claim-verification or claim-transfer records

It may summarize reference-resolution coverage for upstream artifact/evidence refs

A local-file ratio means only that a referenced path resolved locally and could be hashed at envelope-generation time

```text
local resolution != source credibility
local resolution != evidence validity
opaque URI != invalid evidence
```

## 7. No automatic AI detection

Process disclosure uses provider-adapter metadata and caller declarations. The repository does not inspect text and infer AI authorship/use

```text
provider metadata != AI-text detection
AI-text detection != authorship decision
human review != peer review
```

Unknown provider/model/version metadata remains unknown

## 8. Maintenance coverage is separate

`epistemic-pipeline/maintenance-report` may report canonical document/path presence, stable-profile drift, history inventory, hashes, and calendar/stage status

This is repository-maintenance evidence, not claim-level scientific evidence

```text
maintenance coverage != claim correctness
calendar-month close != reproduction
```

## 9. Relation to research-agent work

External work provides useful design pressure without defining this repository

- claim-level auditability highlights provenance coverage, soundness, contradiction transparency, and audit effort
- artifact-centered claim-aware observability argues claims, artifacts, and verification records should be first-class audit objects
- trajectory-to-evidence work distinguishes completed execution from qualified evidence
- evidence-bounded research agents constrain claims to what evidence can support
- end-to-end scientific-agent evaluation shows local task success can coexist with weak global evidence/scale/unit/calculation consistency
- long-horizon process evaluation shows final scores can hide where progress/regression occurs
- autonomous-science provenance emphasizes complete re-openable records

This repository borrows coverage as a measurable structural dimension. It does not claim provenance soundness because soundness requires stronger external verification than the current runtime implements

## 10. Document / stage status

This is a current authoritative specialized contract under `DOCUMENT_STATUS.md`

The August evidence-infrastructure stage closed on 2026-08-31. Stage closure changes maintenance status only and does not alter the semantics of assertion basis, coverage, or claim validity

## 11. Hard boundaries

```text
Assertion basis != correctness
Audit coverage != scientific validity
Evidence ref != evidence sufficiency
Conflict absent != independent corroboration
Structural check != truth
Heuristic score != calibrated probability
Convergence != certainty
Provider identity != output validity
Human review != peer review
Evidence Envelope != proof object
Claim transfer != acceptance
Maintenance clean != scientific validity
Calendar-month close != reproduction
```
