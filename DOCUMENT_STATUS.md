# Document Status — epistemic-pipeline

**Status:** active document-governance router  
**Calibrated:** 2026-09-15  
**Stage:** August 2026 evidence-infrastructure phase closed on 2026-08-31

This file routes repository materials by current role and authority. It is a classifier/router, not an independent source of runtime, claim, or scientific truth.

See `docs/README.md` for the three-class taxonomy.

## Class 01 — source and explanation

Primary implementation and explanatory surfaces include:

```text
core/
graphs/
states/
roles/
tests/
Makefile
README.md
ARCHITECTURE.md
```

Implementation determines actual runtime behavior. README/Architecture explain current behavior and must follow implemented and contracted boundaries.

`core/maintenance_cadence.py` is executable source in this class. It is not itself a preserved scanner run, evidence-sufficiency verdict, or external governance audit.

## Class 02 — examples and contracts

Current capability/usage constraints include:

```text
MANIFEST.yaml
validators/
RESEARCH_CONTRACT.md
CLAIM_AUDIT_CONTRACT.md
CLAIM_TRANSFER_CONTRACT.md
ASSERTION_BASIS_AND_AUDIT_COVERAGE.md
examples/
CUSTOMIZATION_GUIDE.md
AGENTS.md
CONTRIBUTING.md
CITATION.cff
LICENSE
```

`MANIFEST.yaml` and validators are machine-readable capability/rule surfaces. The Research Contract and specialized evidence contracts define their named scientific/integrity semantics. Examples and customization/operator guidance demonstrate supported use but do not upgrade structural states into scientific truth.

## Class 03 — maintenance and audit

Current maintenance/governance surfaces:

```text
DOCUMENT_STATUS.md
MAINTENANCE_CADENCE.md
maintenance/cadence.yaml
JULES_CORRECTION_RECORD.md
```

Dated/stage/historical evidence:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
STAGE_2026_08_MAINTENANCE.md
POST_STAGE_REPAIR_2026_09_01.md
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md
maintenance/DAILY_WEEKLY_MONTH_TO_DATE_RECONCILIATION_2026_09_13.md
FRONTIER_ALIGNMENT.md
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
docs/03-maintenance-and-audit/history/superpowers/
```

The archived Superpowers material is superseded historical design evidence. Its relocation does not make it current authority.

## Recovery authority

Use **subject-scoped** authority in this order:

```text
current merged main implementation
> current machine-readable capability contract / schema / configuration for that subject
> active RESEARCH_CONTRACT.md and active specialized contract for that subject
> operational examples / configuration / test evidence for supported use
> README / Architecture / current explanatory documentation
> maintenance / audit / reconciliation evidence
> historical snapshots / superseded plans / PR-task narratives
```

Important consequences:

- a newer dated maintenance record does not outrank an active claim/evidence/scientific contract merely because its date is later;
- `validators/` may define machine rules but does not convert heuristic scores into probability or structural verification into scientific verification;
- `maintenance/cadence.yaml` is authoritative for its local maintenance/scanner configuration, not for claim truth, evidence sufficiency, provider identity, or transfer semantics;
- `DOCUMENT_STATUS.md` routes documents but does not override implementation or active subject contracts;
- `AGENTS.md` remains operational guidance and its hard rules remain active; if an older embedded recovery-order list conflicts with this 2026-09-15 router, this current router/taxonomy governs document recovery;
- execution evidence exists only when the execution actually occurred and its result was preserved.

## Dated evidence interpretation

The 2026-08-31 cadence demonstration is historical/reference evidence, not an automatically preserved clean scanner or research-workflow run.

The 2026-09-01 repair records post-stage hardening without reopening the August stage.

The 2026-09-06 reconciliation records authority/cadence correction. The 2026-09-01 through 2026-09-06 frontier refresh is source-bounded post-stage calibration for provider/model provenance, execution status, long-running agents, telemetry, source-authority conflict, and claim-transfer boundaries; it does not itself establish scientific verification.

The 2026-09-13 reconciliation remains valid point-in-time evidence that the pass found `NO_CHANGE_REQUIRED` for implementation/evidence-contract semantics, refreshed maintenance-layer observation through 2026-09-13, kept September month-to-date, and did not fabricate absent scanner or research-workflow runs. It does not mechanically advance `MANIFEST.yaml` or external-research calibration.

```text
maintenance freshness != evidence-contract calibration
structured state != scientific verdict
latest observation != highest semantic authority
NO_CHANGE_REQUIRED != skipped inspection
```

## Historical preservation

`FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, `SIX_DAY_CONSOLIDATION.md`, closed-stage records, superseded design files, and historical PR/task narratives remain point-in-time evidence.

Do not rewrite them merely because current terminology or behavior changed. Correct forward through a current file, correction, reconciliation, or later time-point record.

```text
historical snapshot != current contract
historical != invalid
later success != earlier success
correction != history rewrite
agent completion claim != current verification
```

## Stage status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
September 2026: month-to-date until natural month close
```

Post-stage repairs, reconciliations, taxonomy work, and frontier refreshes do not reopen the August stage.

## Hard boundaries

```text
document authority != claim truth
implementation presence != execution evidence
scanner source != scanner execution
maintenance clean != evidence sufficiency
heuristic score != probability
claim transfer != acceptance
frontier calibration != claim verification
reference demonstration != runtime proof
calendar close != scientific validation
historical agent narrative != current repository truth
path relocation != semantic change
classification != deletion authority
```
