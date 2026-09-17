# 03 — Maintenance and Audit

This class answers: **what maintenance/governance rule applied, what was inspected, what was concluded, who owned the maintenance surface, and what historical evidence must remain reviewable?**

It does **not** define runtime, claim truth, evidence sufficiency, provider identity, or scientific validity merely because a record is newer than an active contract.

## Current maintenance / governance surfaces

- [`DOCUMENT_STATUS.md`](DOCUMENT_STATUS.md) — current document-governance router
- [`MAINTENANCE_CADENCE.md`](MAINTENANCE_CADENCE.md) — active human-readable maintenance contract
- root `maintenance/cadence.yaml` — machine-readable maintenance/scanner configuration and control metadata
- [`independent-gpt/README.md`](independent-gpt/README.md) — public cold-start recovery/delivery kernel
- root `AGENTS.md` — operational agent guidance
- root `CONTRIBUTING.md` plus `.github/pull_request_template.md` and `.github/ISSUE_TEMPLATE/governance.md` — collaboration/delivery entry points

`core/maintenance_cadence.py` remains **Class 01 executable source**. Its source, configuration, or inspection does not prove the scanner ran.

## Coordinated research-infrastructure context

This repository participates in:

```text
lostlight530/auto-doc-engine
lostlight530/epistemic-pipeline
lostlight530/sci-render-kit
```

Coordination permits shared inspection windows and cross-repository vocabulary review. It does not create cross-repository authority.

## Maintenance-control recovery

```text
current merged main implementation
> MANIFEST.yaml / validators / current machine-readable configuration
> latest relevant dated repair or current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

For claim/evidence/runtime semantics, continue to use the most specific implementation, validator/machine rule, and active subject contract.

## Idempotent ownership

A maintenance attempt should retain, when applicable:

```text
repository + owning surface/task + logical period/evidence window
+ producer/maintainer + exact base revision + run identity when available
```

Before writing, inspect open PRs/live branches for overlapping ownership. Overlap means `COORDINATE`; no confirmed defect means `NO_CHANGE_REQUIRED` and no activity-only branch/PR. **Write never probes.**

## Dated maintenance / historical evidence

The August cadence demonstration, 2026-09-01 repair, 2026-09-06 reconciliation, frontier refresh, and 2026-09-13 month-to-date reconciliation remain point-in-time maintenance evidence. Closed-stage and FOUR/FIVE/SIX_DAY/Jules-correction/superseded-plan records under `history/` remain historical evidence.

A later record may report a newer observation or correction, but it does not silently override implementation, validators, machine contracts, or active evidence contracts.

## Epistemic boundaries

```text
claim indexed != claim true
evidence linked != evidence sufficient
heuristic score != probability
runtime-policy pass != truth
claim transfer != acceptance
identity ambiguity != scientific contradiction
structured output != scientific verification
provider report != vendor authentication
coverage != provenance soundness
```

## Validation and delivery boundary

```text
checker available != checker executed
checker executed != checker passed
checker passed != scientific validity
historical pass != current pass
contract inspection != runtime verification
Draft PR != merge approval or validation success
```

Record an unrun check as `NOT_EXECUTED`; use `EXECUTION_NOT_OBSERVED` when execution itself was not observed.

When a real repair exists, verify the aggregate branch diff, refresh current-main/overlap state, open one bounded **Draft PR**, and stop for maintainer review. Do not auto-merge or write maintenance repairs directly to `main`.

When current state conflicts with a dated record, preserve the dated record and correct forward in current governance or a later reconciliation record.
