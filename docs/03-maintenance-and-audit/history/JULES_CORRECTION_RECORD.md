# Jules Correction Record — epistemic-pipeline

**Status:** active correction / authority record  
**Calibrated:** 2026-09-06  
**Scope:** historical Jules-created pull-request narratives and their relationship to current repository truth

## Purpose

This record does not declare historical Jules work invalid and does not rewrite old pull requests.

It corrects one governance ambiguity: early automated-agent PR descriptions contain implementation, test, completeness, comparison, and quality claims. Those are useful point-in-time delivery metadata, but they are not durable current evidence by themselves.

```text
agent task / PR narrative != current repository truth
claimed test pass != current runtime verification
historical completion claim != permanent capability guarantee
proposal wording != normative evidence contract
```

## Historical Jules PRs in scope

- PR #1 — `feat: Dynamic Engine, Gatekeeper, LLM Harness, and Bilingual Docs`
- PR #2 — `feat: optimize role constraints by enforcing rigid JSON output schemas`
- PR #3 — `全面完善规则对齐与核心逻辑的边界保护`

Each was created automatically by Jules for a user-started Jules task. Their PR bodies remain historical task/delivery narratives.

Descriptions such as successful multi-round tests, complete rule alignment, framework comparisons, confidence-network correctness, or other completion language are time-scoped assertions unless the current revision independently re-establishes them.

## Current authority order

```text
current main implementation
> MANIFEST.yaml and current machine-readable configuration
> latest dated repair / current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active evidence / scientific-integrity contracts
> MAINTENANCE_CADENCE.md and maintenance/cadence.yaml
> Architecture / README
> historical consolidation snapshots
> historical PR / task narratives, including Jules
```

Subject-specific contracts remain authoritative for their named surface.

## Correction rules

### J-C01 — PR body is not merged state

An unmerged agent PR is a proposal. After merge, the repository fact is the actual resulting tree on `main`, not every statement in the PR body.

### J-C02 — Execution claims expire unless reverified

Historical test counts, test-success claims, engine-run claims, convergence statements, performance/completeness statements, or similar execution assertions must be reverified against the current revision before use as current evidence.

### J-C03 — Agent framing is not scientific semantics

Historical phrases such as `confidence`, `memory rules`, comparisons to other agent frameworks, or broad claims of alignment do not define current scientific semantics. Current contracts preserve the repository's explicit boundaries, including heuristic score != probability and structured/audited != scientifically verified.

### J-C04 — Correct forward; do not rewrite history

If current implementation or contracts supersede an old agent narrative, preserve the historical PR and record the correction in current documentation or a dated repair/maintenance record.

```text
superseded != fabricated
requires re-verification != false
historical != current
```

## Current epistemic-pipeline calibration

The current repository has materially evolved beyond the early Jules PR descriptions. Current authority includes trace/checkpoint/provenance separation, runtime policy, claim verification, claim identity/origin ambiguity, claim transfer, Evidence Envelope, assertion-basis/audit coverage, maintenance cadence, document authority, and post-stage repair semantics.

Therefore early Jules PRs are development history, not a substitute for current implementation/contracts and not a scientific-verification record.

## External calibration

Google's Jules guidance states that generated code should still be carefully reviewed before use even when agent-side review mechanisms are present. Later Jules evaluation work likewise focuses on measuring useful agent insight rather than treating confident output as correctness.

Primary references checked 2026-09-06:

- Google Developers Blog — `Meet Jules’ sharpest critic and most valuable ally` (2025-08-12)
- Google Developers Blog — `Measuring What Matters with Jules` (2026-06-22)

These references calibrate governance only. They do not prove any historical repository change wrong.

## Durable boundary

```text
agent assistance != repository authority
review mechanism != infallibility
PR metadata != runtime proof
structured output != scientific verification
current main != historical PR prose
correction record != deletion of history
```
