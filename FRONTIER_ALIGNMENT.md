# Frontier Alignment — Epistemic Pipeline

**Repository:** `epistemic-pipeline`  
**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-30  
**Normative boundaries:** `RESEARCH_CONTRACT.md`, `CLAIM_AUDIT_CONTRACT.md`, `CLAIM_TRANSFER_CONTRACT.md`, `ASSERTION_BASIS_AND_AUDIT_COVERAGE.md`

## Current research question

The 2026 frontier increasingly asks not only whether an agent completed a workflow, but whether the resulting record can be reopened, audited, safely handed forward, and maintained across changing research phases

```text
Can artifacts be attributed to actions
Can claims be linked to evidence
Can conflicts and qualification remain visible
Can assertion basis be identified
Can audit coverage be measured without pretending it is truth
Can a claim move downstream without losing its constraints
Can the repository be revalidated at the right research horizon without rewriting history
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
```

```text
trace != provenance != claim audit != claim transfer != evidence envelope
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

## Day-7 phase-aware maintenance

Long-horizon research work increasingly reports phase structure, persistent workspaces, recovery segments, and the need for re-validation when the research regime changes

A behavioural study of long-horizon autonomous architecture research found clear phase transitions and argued for regime-aware re-validation rather than assuming one workflow remains optimal across the whole run

ScienceFlow similarly organizes long-horizon research into persistent research segments to support continuity, recovery from dead ends, and evolving state

Current autonomous-science provenance work emphasizes that research records should remain re-openable, auditable, and correctable

Borrowed maintenance principle

```text
different drift horizons deserve different review scopes
```

The repository now distinguishes

```text
daily
  local runtime / claim / evidence drift

weekly
  cross-day evidence-stack reconciliation

monthly or explicit phase-close
  canonical hash baseline / history inventory / deprecation review
```

This is implemented in `MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, `core/maintenance_cadence.py`, and `STAGE_2026_08_MAINTENANCE.md`

The scanner is local and read-only
It does not run the research workflow, call an LLM, verify citations, judge evidence sufficiency, delete history, or claim provenance soundness

On 2026-08-30 the August maintenance snapshot is month-to-date, not final calendar-month close

```text
maintenance clean != scientific validity
weekly consistency != evidence sufficiency
monthly baseline != reproduction
history inventory != deprecation decision
```

## External signals

Current calibration includes

- Nature Computational Science on re-openable provenance for autonomous science
- transparent AI use and human oversight in scientific publishing
- artifact-centered claim-aware observability
- From Trajectories to Evidence
- Brain Researcher evidence-bounded claims
- EarthVerse end-to-end consistency gaps
- claim-level auditability separating provenance coverage from soundness
- Praxist solution/evidence lineages
- ReproAgent persistent implementation contracts
- long-horizon autonomous architecture research with phase-aware re-validation
- ScienceFlow segmented long-horizon research and recovery

Borrowed principles are limited to explicit state, evidence, constraints, lineage, recovery, and maintenance boundaries

Not claimed

```text
scientific truth oracle
provenance soundness
citation correctness
peer-review authority
calibrated truth probability
optimal maintenance frequency
```

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

Together the repositories explore evidence-aware research infrastructure with explicit inheritance and maintenance boundaries

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
monthly baseline != reproduction
provider identity != output validity
human review != peer review
provenance != truth
```
