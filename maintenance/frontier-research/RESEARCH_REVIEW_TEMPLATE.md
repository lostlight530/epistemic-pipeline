# Frontier Research Review — TEMPLATE

> Instantiate as `RESEARCH_REVIEW.md` before declaring a Stage complete. This is a research-quality review, not a CI status log.

## 0. Review identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Stage / artifact reviewed:** `<scope>`
- **Review date:** `<date>`
- **Reviewer(s):** `<observed identity / UNKNOWN>`
- **Independence:** `<INDEPENDENT_REVIEW | PARTIALLY_INDEPENDENT | SAME_PRODUCER_REVIEW | INDEPENDENCE_NOT_ESTABLISHED>`
- **Review scope:** `<method / search / source identity / charting / analysis / synthesis / repository boundary / full>`
- **Specification version:** `2026-09-19-first-batch`

## 1. Review question

> Is the research product supported by its declared method and evidence, with temporal and repository boundaries preserved?

## 2. Protocol-to-execution review

- Are research questions aligned with executed methods?
- Were material deviations recorded?
- Does claimed coverage match actual search/source coverage?
- Were stopping/completion criteria applied honestly?

## 3. Search and source review

- Are important source classes missing relative to the declared question?
- Are exact searches/navigation methods recorded where relevant?
- Are mutable sources version/date bounded?
- Are source authority and limitations correctly stated?
- Were same-origin reports incorrectly counted as independent corroboration?

## 4. Research-object identity review

- Are projects/releases/standards/events correctly disambiguated?
- Are multiple reports grouped to the same object where appropriate?
- Are version transitions or renames causing false duplication?
- Are source/object identity conflicts preserved when unresolved?

## 5. Evidence extraction / charting review

- Are extracted variables relevant to the question?
- Are unsupported fields left unknown rather than inferred?
- Were material charting-method changes recorded?
- Is appraisal methodology explicit if appraisal claims are made?

## 6. Analysis review

- Does analysis go beyond source inventory into justified research interpretation?
- Are alternative explanations and counterevidence addressed?
- Are negative findings bounded to what was actually searched/observed?
- Are causal/lineage claims stronger than the evidence allows?

## 7. Synthesis review

- Does the synthesis preserve material Part-level conflicts?
- Is source-family dependence visible?
- Are non-comparable Parts/Stages identified?
- Does the conclusion stay within the evidence boundary?
- Are important limitations adjacent to the conclusions they qualify?

## 8. Temporal-integrity review

- Are event date, publication date, reconstruction date, and repository date distinguished?
- Has current knowledge been projected backward?
- Has later success been used to imply earlier success?
- Have historical corrections been handled forward rather than silently rewritten?

## 9. Repository-boundary review

Review against: **claims, evidence, state transitions, provenance, uncertainty, verification, conflicts, transfer, evidence envelopes, and research-execution traceability.**

Hard boundaries:

- `claim indexed != claim true`
- `evidence linked != evidence sufficient`
- `heuristic score != probability`
- `runtime-policy pass != truth`
- `claim verification != scientific adjudication`
- `claim transfer != acceptance`
- `provider identity != output validity`
- `provenance != truth`

Check that external research has not been converted into an unsupported repository capability/defect claim.

## 10. Contributor / instrument provenance review

- Are responsible contributions separated from tools/models?
- Is reviewer independence represented accurately?
- Are unobserved model/provider identities left unknown?

## 11. Findings

| Finding ID | Class | Severity | Evidence | Required research action |
|---|---|---|---|---|
| `R1` | `<METHOD_DEFECT / EVIDENCE_GAP / SOURCE_IDENTITY_CONFLICT / TEMPORAL_CONFLATION / SYNTHESIS_OVERREACH / BOUNDARY_OVERREACH / CLARIFICATION / other>` | `<MATERIAL / NON_MATERIAL>` | `<refs>` | `<action>` |

## 12. Unresolved review questions

- `<question>`

## 13. Review disposition

Use one:

- `RESEARCH_READY_FOR_STAGE_CLOSE`
- `REVISION_REQUIRED_BEFORE_STAGE_CLOSE`
- `PARTIAL_REVIEW_ONLY`
- `REVIEW_BLOCKED_BY_MISSING_EVIDENCE`

Explain the disposition in prose. Do not treat the label alone as validation.

## 14. Independent-validation boundary

State explicitly what was **not** independently reproduced, rerun, or scientifically validated during this review.
