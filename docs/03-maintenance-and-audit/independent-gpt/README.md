# Independent GPT Governance — Epistemic Sentry

Status: current public recovery kernel
Scope: repository-local recovery, independent audit, reconciliation, bounded repair, and coordinated three-repository maintenance participation

This directory is the current public handoff point for a memoryless independent reviewer. It is a Class 03 maintenance/audit router, not a new claim, evidence, or scientific authority layer.

## Coordinated research-infrastructure context

This repository is maintained alongside:

```text
lostlight530/auto-doc-engine
lostlight530/epistemic-pipeline
lostlight530/sci-render-kit
```

One coordinated pass may inspect all three repositories, shared profile/contract names, handoff vocabulary, and maintenance timing. Coordination does not merge their authority or delivery state: recover, decide, branch, validate, report, and deliver each repository independently from its own latest merged `main`.

## Start from current main

At audit start record:

```text
current date / timezone
default branch
current merged main SHA
relevant open PRs
recent merged PRs / commits
checks actually executed
checks not executed
```

Read current repository truth before historical narrative. Use the repository’s subject-scoped recovery order from `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md`:

```text
current merged main implementation
> current machine-readable capability contract / schema / configuration for that subject
> active docs/02-examples-and-contracts/RESEARCH_CONTRACT.md and active specialized contract for that subject
> operational examples / configuration / test evidence for supported use
> README / docs/01-source-and-explanation/ARCHITECTURE.md / current explanatory documentation
> maintenance / audit / reconciliation evidence
> historical snapshots / superseded plans / PR-task narratives
```

This file does not override that order. A legacy generic order that puts the latest repair, `DOCUMENT_STATUS.md`, or `AGENTS.md` above active subject contracts is not canonical when it conflicts with this subject-scoped order.

## Repository map

1. `core/`, `graphs/`, `states/`, `roles/`, `tests/`, and current implementation determine actual runtime behavior.
2. Root `MANIFEST.yaml`, `validators/`, and other machine-readable configuration define capability/rule surfaces only for their named subjects.
3. `docs/02-examples-and-contracts/RESEARCH_CONTRACT.md` and the specialized contracts beside it govern their named claim, evidence, audit, and transfer semantics.
4. `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` routes document roles; `docs/README.md` defines the current three-class taxonomy.
5. `docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, and current maintenance records govern maintenance only within their declared scope.
6. `maintenance/POST_STAGE_REPAIR_2026_09_01.md` is the dated post-stage steady-state checkpoint, not a permanent semantic ceiling.
7. Closed-stage, consolidation, frontier, Jules-correction, and superseded design records under `docs/03-maintenance-and-audit/history/` are historical evidence, not automatic current claim authority.
8. Git history and revision-matched test / workflow evidence resolve disputed execution, timing, path, provider identity, and provenance claims.

## Repository-specific doctrine

Preserve these boundaries:

```text
claim identity ambiguity != scientific contradiction
MockProvider = deterministic fixture only
structured verification != external scientific verification
heuristic score != probability
claim transfer != acceptance
conflict preservation != conflict adjudication
assertion basis != correctness
coverage != quality
coverage ratio != probability
R1 != R3
```

Do not promote a deterministic fixture, provider-adapter report, structured claim state, or clean maintenance result into vendor authentication, external corroboration, peer review, evidence sufficiency, or scientific truth.

## Cadence and no-churn rule

The coordinated automation may run every day at 06:30 Asia/Shanghai. That schedule is an inspection opportunity, not a requirement to create commits, reports, or PRs.

```text
NO_CHANGE_REQUIRED = valid daily outcome
```

Perform daily recovery, inspection, validation, and evidence review as applicable. Create or update weekly/monthly artifacts only when the current maintenance contract, a natural calendar or phase boundary, accumulated evidence, demonstrated drift, or another explicit maintenance need justifies them. Do not force weekly synthesis before its natural/contract-defined point and do not force monthly synthesis before the natural month boundary or another explicit trigger.

The 2026-08-24 through 2026-08-31 research stage is closed historical evidence. The 2026-09-01 post-stage repair is the dated starting checkpoint for steady-state maintenance. Current merged `main` may supersede that checkpoint only through explicit current evidence or reconciliation.

## Evidence boundaries

Structured state is not a scientific verdict. Heuristic scores are not probabilities unless an active contract explicitly says so. Source presence is not independent corroboration. Maintenance freshness is not evidence-contract calibration. Execution evidence exists only when execution actually occurred and its result was preserved.

Independent governance may audit claim/evidence links, provenance, transfer, provider identity, validation scope, current documentation, and maintenance records, but it must not promote maintenance prose above current subject contracts.

Preserve at minimum:

```text
Provenance != Truth
Assertion basis != Correctness
Coverage != Quality
Coverage ratio != Probability
Evidence reference != Evidence sufficiency
Claim identity ambiguity != Scientific contradiction
Claim transfer != Acceptance
Human review != Peer review
R1 != R3
Maintenance clean != Scientific validation
```

## History discipline

Historical records remain point-in-time evidence. Later evidence may change current interpretation through a dated correction or reconciliation; it does not rewrite the earlier record. Preserve negative, failed, missing, blocked, insufficient-evidence, superseded, and unknown states. Do not fabricate absent scanner or research-workflow runs.

## Drift and repair decision

Do not invent work. If current recovery finds no real defect or drift, return `NO_CHANGE_REQUIRED` for this repository and do not create a PR.

When drift is confirmed:

1. identify the owning implementation/configuration/current-document surface;
2. identify every machine contract, router, or current explanation that must remain synchronized;
3. make the smallest truthful change;
4. preserve historical bodies and point-in-time evidence;
5. keep configured canonical/scan/governance/history paths repository-relative and inside the repository root;
6. preserve repository-relative report identity and configuration SHA-256 where the current contract requires it;
7. distinguish checks executed from checks not executed.

Use `HEALTHY`, `REPAIR`, `COORDINATE`, or `BLOCKED` when a compact governance state is useful.

## Delivery protocol

For any authorized change:

```text
refresh latest remote main
inspect relevant prior/open PR state
branch from latest merged main
make one coherent scoped change
run only actually available targeted checks
record commands/results accurately
compare main...branch
require behind_by = 0
create Draft PR
verify mergeability
STOP for maintainer review
```

Default independent-agent delivery does not write directly to `main` and does not auto-merge. A maintainer may explicitly authorize a different delivery action in a specific session; that authorization does not rewrite the default repository maintenance contract.

Do not modify GitHub Actions, CI, CodeQL, dependency bots, branch governance, or repository automation as routine maintenance unless explicitly authorized.

## Coordinated report contract

Report per repository:

```text
main revision examined
current defect or NO_CHANGE_REQUIRED
files changed, if any
checks executed
checks not executed
evidence boundary
Draft PR link, if created
unresolved gaps
cross-repository drift in shared profile / contract names
repository delivery state
```

Clearly separate verified facts, inferred conclusions, unresolved items, executed checks, unexecuted checks, and delivery state. A successful command, clean maintenance scan, or Draft PR does not become a stronger scientific-validity claim.

When this kernel is used by the research-maintenance GPT, the final user-facing report must be written in Chinese while repository names, file paths, SHAs, commands, state labels, profile names, and protocol terms remain canonical.

## Public boundary and handoff

This kernel is intentionally repository-bounded and does not require reconstruction of unavailable operator context or unrelated orchestration.

A durable audit should leave the next reviewer able to identify the base `main` SHA, scope/evidence window, authority used, checks run, checks not run, current findings, historical findings, corrections, unresolved items, and whether history and negative evidence were preserved.

Independent governance may recommend or prepare bounded changes. Final merge and doctrine authority remains with the maintainer.
