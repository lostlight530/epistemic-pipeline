# Contributing — Epistemic Pipeline

Changes should strengthen explicit research-execution semantics, evidence traceability, portable constraints, or honest maintenance boundaries rather than merely increase module count.

## Before changing the repository

Read:

```text
README.md
docs/01-source-and-explanation/ARCHITECTURE.md
docs/02-examples-and-contracts/RESEARCH_CONTRACT.md
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/independent-gpt/README.md
MANIFEST.yaml
AGENTS.md
```

For maintenance work, start from exact current merged `main`, inspect live PRs/branches for overlapping ownership, and identify the owning surface before writing.

Record, when applicable:

```text
repository + owning surface/task + logical period/evidence window
+ producer/maintainer + exact base revision + run identity when available
```

Overlap means `COORDINATE`. No confirmed defect means `NO_CHANGE_REQUIRED` and no activity-only branch/PR. **Write never probes.**

## Contribution principles

1. Change the smallest layer that owns the requirement.
2. Keep graph/state/provider/policy/score/trace/provenance/claim-audit/claim-transfer/envelope concerns separate.
3. Fail explicitly for unsupported checks, wrong profiles, missing requested claims, and ambiguous recovery identity.
4. Keep provider/model/version metadata unknown when unknown; preserve assertion basis when known.
5. Never infer scientific truth from structural success.
6. Preserve conflicts and non-probability score semantics during transfer.
7. Keep experimental modules experimental until deliberately integrated.
8. Update authoritative documentation when public semantics change.
9. Do not rewrite historical snapshots merely because terminology changes later.

## Core evidence boundaries

```text
claim indexed != claim true
evidence linked != evidence sufficient
structured verification != scientific verification
heuristic score != probability
runtime-policy pass != truth
claim transfer != acceptance
identity ambiguity != contradiction
provider report != vendor authentication
coverage != provenance soundness
```

Any new claim/evidence field must state both the value and how this repository obtained it. Caller-declared or provider-reported basis does not become correctness, peer review, or external authentication.

## Claim-transfer changes

When changing transfer behavior:

- require the expected source profile;
- fail explicitly for missing requested claim IDs;
- preserve source/evidence refs, structural observations, conflicts, heuristic-score semantics, and audit state;
- never remove conflict context to make a handoff look cleaner;
- never upgrade heuristic scores to probability;
- never imply acceptance, peer review, or evidence sufficiency through transfer;
- synchronize the transfer contract, Manifest, examples, and downstream profile references when semantics actually change.

## Maintenance workflow

Maintenance is defined by `DOCUMENT_STATUS.md`, `MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, `AGENTS.md`, and the Independent GPT recovery kernel.

```text
daily -> bounded demonstrated runtime/claim/evidence drift
weekly -> full current evidence/document reconciliation
monthly -> calendar-month or explicit phase-close baseline
```

Cadence is not an obligation to manufacture a change. Daily/Weekly work may coalesce into one real branch/PR when they own the same correction.

The maintenance scanner `.py` implementation is not rewritten merely to synchronize governance prose. Source/config inspection is not scanner execution.

Before delivery:

1. verify the aggregate diff against the exact base;
2. refresh current `main` and live overlap;
3. list checks actually executed and checks not run;
4. open one bounded **Draft PR**;
5. stop for maintainer review.

Use `NOT_EXECUTED` for an unrun checker/test and `EXECUTION_NOT_OBSERVED` when execution itself was not observed.

```text
maintenance clean != scientific validity
calendar close != reproduction
history inventory != deprecation decision
checker source != checker execution
Draft PR != validation success
```

## Cross-repository changes

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
        ↓
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

References do not inherit truth, acceptance, or scientific validity.

## Governance boundary

Local/manual checks may be used when useful. Test execution is engineering evidence for the tested surface, not scientific-validation evidence.

Do not add GitHub Actions, CI, CodeQL, dependency bots, branch protection, or merge-gate architecture as ordinary maintenance unless explicitly requested.

Do not publish private Jules prompts, repository memory, hidden reasoning, credentials, or unrelated operator context. Public governance may encode the effect of a rule without copying private control text.

Final review, doctrine, and merge authority remains with the maintainer.
