# Contributing — Epistemic Pipeline

Changes should strengthen explicit research-execution semantics, evidence traceability, portable constraints, or honest maintenance boundaries rather than merely increase module count

## Before changing the repository

Read

```text
README.md
ARCHITECTURE.md
RESEARCH_CONTRACT.md
DOCUMENT_STATUS.md
MAINTENANCE_CADENCE.md
MANIFEST.yaml
AGENTS.md
```

Use `DOCUMENT_STATUS.md` to distinguish current authority from historical consolidation snapshots

## Contribution principles

1. Change the smallest layer that owns the requirement
2. Keep graph/state/provider/policy/score/trace/provenance/claim-audit/claim-transfer/envelope concerns separate
3. Fail explicitly for unsupported machine checks, wrong sidecar profiles, missing requested claims, and ambiguous recovery identity
4. Keep provider/model/version metadata unknown when unknown; preserve assertion basis for metadata that is known
5. Never infer scientific truth from structural success
6. Preserve conflicts and non-probability score semantics during transfer
7. Keep experimental modules experimental until deliberately integrated
8. Update authoritative documentation when public semantics change
9. Do not rewrite historical Day-N snapshots merely because current terminology changed

## Stable internal identifiers

Do not introduce decorative project versions such as `@1`, `@2`, `/v1`, or fake fixture/model versions

Preserve actual external standard/runtime versions when those are real

## Claim/evidence changes

When changing claim/evidence structures

- retain claim IDs separately from prose
- never manufacture missing evidence refs
- keep conflict records distinct from adjudication
- do not turn claim audit into `verified=true`
- preserve assertion/observation basis for new audit fields
- keep coverage dimensional; do not create an aggregate research-quality score
- update Claim Audit, Assertion Basis, Manifest, examples, and relevant current docs

## Claim-transfer changes

When changing transfer behavior

- require the expected source profile
- fail explicitly for missing requested claim IDs
- preserve source/evidence refs, structural observations, conflicts, heuristic-score semantics, and audit state
- never remove conflict context to make a downstream handoff look cleaner
- never upgrade heuristic scores to probability
- never imply acceptance, peer review, or evidence sufficiency through transfer
- synchronize `CLAIM_TRANSFER_CONTRACT.md`, Manifest, examples, and downstream profile references

## Assertion-basis rule

A new audit field should answer both

```text
What value is recorded
How did this repository obtain that value
```

If the basis is only a provider report or caller declaration, say so. Do not upgrade it to vendor authentication, external verification, or scientific truth

## Coverage rule

```text
coverage != provenance soundness
coverage != scientific validity
coverage ratio != probability
```

The current repository has no validated weighting regime for a composite audit-quality score, so `aggregate_score` remains `null`

## Score changes

Any new score semantics must state whether values are heuristic, empirically calibrated, probabilistic, or something else

`[0,1]` alone is not evidence of probability semantics

## Provider integrations

Real providers belong behind `LLMProvider`

Their `describe()` metadata must reflect what the integration actually knows and include truthful assertion basis

Do not guess model versions or infer AI authorship/use from prose

## Trace/provenance changes

OpenTelemetry naming alignment must not be described as an OTel exporter unless implemented

PROV-aligned JSON must not be described as PROV-O RDF unless a real serializer exists

## Daily / weekly / monthly maintenance

Maintenance rules are defined in `MAINTENANCE_CADENCE.md` and `maintenance/cadence.yaml`

Current document/historical roles are defined in `DOCUMENT_STATUS.md`

```text
daily -> bounded demonstrated runtime/claim/evidence drift
weekly -> full current evidence/document reconciliation
monthly -> calendar-month or explicit phase-close baseline
```

Current closed stage

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

Maintenance reports are structural evidence only

```text
maintenance clean != scientific validity
calendar close != reproduction
history inventory != deprecation decision
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

References do not inherit truth or scientific validity

## Governance boundary

Local/manual checks may be used when useful

Do not add GitHub Actions, CI, CodeQL, dependency bots, branch protection, or merge-gate architecture as ordinary maintenance unless explicitly requested

Test execution is not scientific-validation evidence and is not a default completion gate for this repository-maintenance workflow
