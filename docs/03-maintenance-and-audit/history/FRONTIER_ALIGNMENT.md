# Frontier Alignment — Epistemic Pipeline

**Repository:** `epistemic-pipeline`  
**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-31  
**Closed stage:** 2026-08-24 through 2026-08-31  
**Normative boundaries:** `RESEARCH_CONTRACT.md`, `CLAIM_AUDIT_CONTRACT.md`, `CLAIM_TRANSFER_CONTRACT.md`, `ASSERTION_BASIS_AND_AUDIT_COVERAGE.md`, `MAINTENANCE_CADENCE.md`, `DOCUMENT_STATUS.md`

## Current research question

The frontier increasingly asks not only whether an agent completed a workflow, but whether the resulting record can be reopened, audited, safely handed forward, and maintained across changing research phases

```text
Can artifacts be attributed to actions
Can claims be linked to evidence
Can conflicts and qualification remain visible
Can assertion basis be identified
Can audit coverage be measured without pretending it is truth
Can a claim move downstream without losing its constraints
Can long-horizon progress/regression be inspected beyond a final score
Can repository state be revalidated at the right horizon without rewriting history
```

Epistemic Pipeline addresses these at the research-execution and evidence-contract layer

## Current architecture response

```text
claim / evidence / conflict
      ↓
runtime policy + bounded heuristic scores
      ↓
trace / checkpoint / provenance
      ↓
claim-verification
  assertion basis + dimensional coverage
      ↓
claim-transfer
  explicit selection + non-inheritance constraints
      ↓
evidence-envelope
  compact cross-tool handoff

repository state
      ↓
daily / weekly / monthly maintenance
  current-document authority + stage/calendar status
```

```text
trace != provenance != claim audit != claim transfer != evidence envelope != maintenance report
```

## Claim transfer and non-inheritance

A downstream claim must retain its evidence refs, conflicts, structural observations, audit state, and heuristic-score semantics

Required constraints remain

```text
scientific_validity_inherited: false
evidence_sufficiency_inherited: false
peer_review_inherited: false
conflicts_must_remain_visible: true
heuristic_scores_must_retain_non_probability_semantics: true
```

```text
transfer != acceptance
inheritance != validation
conflict preservation != conflict adjudication
```

## Phase-aware maintenance and document authority

Long-horizon research work increasingly reports phase structure, persistent workspaces, recovery segments, and the need for re-validation when the research regime changes

A behavioural study of long-horizon autonomous architecture research reports phase transitions and motivates regime-aware re-validation rather than assuming one workflow remains optimal across a whole run

ScienceFlow organizes long-horizon research into persistent research segments to support continuity, recovery from dead ends, and evolving state

Beyond-final-score evaluation work further motivates process-level inspection because terminal metrics can hide where progress, regression, harness effects, or misleading experience reuse occurred

Persistent-runtime work such as Argus adds a neighboring design signal around durable project state and reviewed routes, without being equivalent to this evidence contract

Autonomous-science provenance work emphasizes that research records should remain re-openable, auditable, and correctable

Borrowed maintenance principle

```text
different drift horizons deserve different review scopes
and current authority must remain distinguishable from historical evidence
```

The repository distinguishes

```text
daily
  local runtime / claim / evidence / documentation drift

weekly
  full current evidence-stack and document reconciliation

monthly or explicit phase-close
  canonical baseline / history inventory / deprecation review
```

This is implemented in `MAINTENANCE_CADENCE.md`, `DOCUMENT_STATUS.md`, `maintenance/cadence.yaml`, `core/maintenance_cadence.py`, and `STAGE_2026_08_MAINTENANCE.md`

The scanner is local and read-only

It does not run the research workflow, call an LLM, verify citations, judge evidence sufficiency, delete history, or claim provenance soundness

Current closed stage

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

```text
maintenance clean != scientific validity
weekly consistency != evidence sufficiency
calendar-month close != reproduction
history inventory != deprecation decision
```

## External signals

Current calibration includes

- Nature Computational Science on re-openable provenance for autonomous science
- transparent AI use and human oversight in scientific publishing
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- EarthVerse-style end-to-end consistency gaps
- claim-level auditability separating provenance coverage from soundness
- Praxist solution/evidence lineages
- ReproAgent persistent implementation contracts
- long-horizon autonomous architecture research with phase-aware re-validation
- ScienceFlow segmented long-horizon research and recovery
- Beyond Final Scores-style process evaluation beyond terminal metrics
- persistent-runtime patterns for durable project state and reviewed routes

Borrowed principles are limited to explicit state, evidence, constraints, lineage, recovery, process inspection, and maintenance boundaries

Not claimed

```text
scientific truth oracle
provenance soundness
citation correctness
peer-review authority
calibrated truth probability
optimal maintenance frequency
```

These external systems and papers are architecture calibration only. They do not validate, certify, endorse, or prove novelty for this repository

## Cross-repository frontier position

```text
auto-doc-engine
  artifact identity / basis / coverage / lineage
        ↓
epistemic-pipeline
  claim-evidence execution / audit / transfer / provenance
        ↓
sci-render-kit
  claim-aware communication / figure evidence / communication transfer
```

Together the repositories explore evidence-aware research infrastructure with explicit inheritance, transfer, document-authority, and maintenance boundaries

## Document-history boundary

Current authority is mapped in `DOCUMENT_STATUS.md`

Historical Day-N consolidation files remain evidence of earlier repository states and are not current scientific/runtime contracts

```text
historical snapshot != current contract
later evidence model != permission to rewrite history
```

## Hard boundaries

```text
assertion basis != correctness
audit coverage != scientific validity
coverage ratio != probability
coverage != provenance soundness
evidence binding != evidence sufficiency
claim transfer != acceptance
inheritance != validation
maintenance clean != scientific validity
calendar-month close != reproduction
provider identity != output validity
human review != peer review
provenance != truth
```
