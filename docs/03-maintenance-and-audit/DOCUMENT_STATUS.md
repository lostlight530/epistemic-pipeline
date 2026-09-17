# Document Status — epistemic-pipeline

**Status:** active document-governance router  
**Calibrated:** 2026-09-17  
**Stage:** August 2026 evidence-infrastructure phase closed on 2026-08-31

This file routes repository materials by current role and authority. It is a classifier/router, not an independent source of runtime, claim, provider, evidence-sufficiency, or scientific truth.

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
docs/01-source-and-explanation/ARCHITECTURE.md
```

Implementation determines actual runtime behavior. README/Architecture explain current behavior and must follow implemented and contracted boundaries.

`core/maintenance_cadence.py` is executable source in this class. Scanner source presence is not scanner execution.

## Class 02 — examples and contracts

Current capability/usage constraints include:

```text
MANIFEST.yaml
validators/
docs/02-examples-and-contracts/RESEARCH_CONTRACT.md
docs/02-examples-and-contracts/CLAIM_AUDIT_CONTRACT.md
docs/02-examples-and-contracts/CLAIM_TRANSFER_CONTRACT.md
docs/02-examples-and-contracts/ASSERTION_BASIS_AND_AUDIT_COVERAGE.md
docs/02-examples-and-contracts/CUSTOMIZATION_GUIDE.md
examples/
AGENTS.md
CONTRIBUTING.md
CITATION.cff
LICENSE
```

`MANIFEST.yaml` and validators are machine-readable capability/rule surfaces. Specialized evidence contracts define their named semantics. Structural state, validator success, and imported references do not become scientific truth merely by being indexed or machine-readable.

## Class 03 — maintenance and audit

Current maintenance/governance surfaces:

```text
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/README.md
docs/03-maintenance-and-audit/independent-gpt/README.md
maintenance/cadence.yaml
.github/pull_request_template.md
.github/ISSUE_TEMPLATE/governance.md
```

The Independent GPT file is a public cold-start recovery/delivery router inside Class 03. It does not create a fourth class and does not outrank implementation, validators, or active subject-specific evidence contracts.

Dated maintenance evidence includes:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
maintenance/POST_STAGE_REPAIR_2026_09_01.md
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md
maintenance/DAILY_WEEKLY_MONTH_TO_DATE_RECONCILIATION_2026_09_13.md
```

Closed-stage/historical evidence includes the `history/` stage, frontier, FOUR/FIVE/SIX_DAY, Jules-correction, and superseded design materials. These remain point-in-time evidence.

## Two authority questions must not be collapsed

### Claim / evidence / runtime semantics

```text
current implementation
> current validator / machine-readable rule / configuration for the subject
> active subject-specific contract
> executable/operational evidence for supported use
> current explanatory documentation
> maintenance evidence
> historical records
```

### Maintenance-control recovery

```text
current merged main implementation
> MANIFEST.yaml / validators / machine-readable configuration
> latest relevant dated repair or current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

A newer maintenance observation does not outrank implementation for claim truth or evidence sufficiency.

## Maintenance task ownership

A maintenance attempt should retain, when applicable:

```text
repository
+ owning surface/task
+ logical period/evidence window
+ producer/maintainer
+ exact base revision
+ run identity when available
```

Before a write, inspect current open PRs/live branches for overlapping ownership. Same owning surface and period with another live owner means `COORDINATE`, not a parallel repair.

No confirmed defect means `NO_CHANGE_REQUIRED`; do not create activity-only branch/PR churn. **Write never probes.**

## Epistemic hard boundaries

```text
claim indexed != claim true
evidence linked != evidence sufficient
structured verification != scientific verification
heuristic score != probability
runtime-policy pass != truth
claim transfer != acceptance
identity ambiguity != contradiction
provider-adapter-reported != vendor authentication
assertion basis != correctness
coverage != quality
coverage ratio != probability
```

`validators/` may define machine rules but cannot silently promote a structural result into probability, source authority, external corroboration, peer review, or scientific truth.

## Dated evidence interpretation

The 2026-08-31 cadence demonstration is historical/reference evidence, not an automatically preserved clean scanner or research-workflow run.

The 2026-09-01 repair records post-stage hardening without reopening August. The 2026-09-06 reconciliation records authority/cadence correction. The frontier refresh is source-bounded calibration, not scientific verification.

The 2026-09-13 reconciliation remains valid point-in-time evidence that the pass found `NO_CHANGE_REQUIRED` for implementation/evidence-contract semantics, refreshed maintenance observation through 2026-09-13, kept September month-to-date, and did not fabricate absent scanner/research runs. It does not mechanically advance `MANIFEST.yaml` or external-research calibration.

```text
maintenance freshness != evidence-contract calibration
structured state != scientific verdict
latest observation != highest semantic authority
NO_CHANGE_REQUIRED != skipped inspection
```

## Execution evidence boundary

```text
implementation presence != execution evidence
scanner source != scanner execution
checker definition != checker execution
contract inspection != checker PASS
historical PASS != current PASS
```

Unrun checks are `NOT_EXECUTED`. Unobserved scheduler/workflow execution is `EXECUTION_NOT_OBSERVED` when material.

## Historical preservation

Do not rewrite historical bodies merely because current terminology, paths, or behavior changed. Correct forward through a current file, correction, reconciliation, or later time-point record.

```text
historical snapshot != current contract
historical != invalid
later success != earlier success
correction != history rewrite
agent completion claim != current verification
path relocation != semantic change
```

## Stage status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
September 2026: month-to-date until natural month close
```

Post-stage maintenance does not reopen August.

## Delivery boundary

For a confirmed maintenance repair, verify the aggregate branch diff, refresh current-main/live-overlap state, open one bounded **Draft PR**, and stop for maintainer review. Do not auto-merge, force-push, or write maintenance repairs directly to `main`.

```text
Draft PR != validation success
maintenance clean != evidence sufficiency
calendar close != scientific validation
historical agent narrative != current repository truth
classification != deletion authority
```
