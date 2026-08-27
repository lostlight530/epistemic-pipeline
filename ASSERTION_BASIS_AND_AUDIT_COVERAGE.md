# Assertion Basis & Claim Audit Coverage — epistemic-pipeline

**Calibration:** 2026-08-28  
**Status:** implemented companion contract for `epistemic-pipeline/claim-verification` and `epistemic-pipeline/evidence-envelope`

## 1. Purpose

A claim audit is only useful if an auditor can distinguish:

```text
what was recorded
where it came from
what was actually checked
what remains unknown
```

The repository therefore separates **assertion/observation basis** from **claim content**, and **audit coverage** from **scientific correctness**.

## 2. Assertion and observation bases

Current claim-verification bases include:

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

These labels answer *how the field entered the audit record*. They do not make the value correct.

```text
provider-adapter-reported != vendor-certified identity
structured-verify-output != external scientific verification
caller-declared review != peer review
```

## 3. Claim audit coverage

`claim-verification` emits dimensional coverage counts for indexed claims:

- claims with source refs;
- claims with evidence refs;
- claims with internal-consistency observations;
- claims with cross-source observations;
- claims with conflict records;
- claims with initial heuristic scores;
- claims with final heuristic scores.

Each dimension can also report a ratio using `claims_indexed` as denominator.

Example interpretation:

```text
evidence_refs_ratio = 0.80
```

means:

> 80% of indexed claims carry at least one evidence reference in the structured run output.

It does **not** mean:

- 80% of claims are correct;
- 80% of evidence is sufficient;
- provenance soundness is 0.80;
- citation accuracy is 80%;
- calibrated probability of truth is 0.80.

## 4. No aggregate audit score

The record deliberately emits:

```json
{
  "aggregate_score": null
}
```

Source presence, evidence linkage, contradiction visibility, consistency observations and heuristic scores are different dimensions. A scalar combination would require an explicit validated weighting/evaluation regime that this repository does not have.

## 5. Evidence Envelope coverage

The Evidence Envelope remains an index. It does not duplicate the full claim-verification record.

It may summarize reference-resolution coverage for:

```text
upstream artifact refs
upstream evidence refs
```

A local-file ratio means only that the referenced path resolved locally and could be hashed at envelope-generation time.

```text
local resolution != source credibility
local resolution != evidence validity
opaque URI != invalid evidence
```

## 6. No automatic AI detection

Process disclosure uses provider-adapter metadata and caller declarations. The repository does not inspect text and infer AI authorship/use.

```text
provider metadata != AI-text detection
AI-text detection != authorship decision
human review != peer review
```

Unknown provider/model/version metadata remains unknown.

## 7. Relation to current research-agent work

External work provides useful design pressure without defining this repository:

- claim-level auditability work highlights provenance coverage, soundness, contradiction transparency and audit effort;
- artifact-centered claim-aware observability argues that claims, artifacts and verification records should be first-class audit objects;
- trajectory-to-evidence work distinguishes completed execution from qualified evidence;
- Brain Researcher limits claims to what evidence supports and uses explicit scientific-review outcomes;
- EarthVerse shows that local task success can coexist with weak end-to-end evidence/scale/unit/calculation consistency;
- autonomous-science provenance work emphasizes complete, re-openable records.

This repository borrows **coverage as a measurable structural dimension**. It does not claim provenance soundness because soundness requires stronger external verification than the current runtime implements.

## 8. Hard boundaries

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
```
