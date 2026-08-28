# Six-Day Consolidation — Epistemic Pipeline

**Date:** 2026-08-29  
**Status:** research-engineering consolidation note

## Day-6 change

Days 1–5 established explicit claim/evidence/conflict structure, runtime policy, bounded heuristic-score semantics, trace/checkpoint/PROV lineage, claim verification, assertion basis and dimensional audit coverage.

Day 6 adds a portable **claim transfer** layer:

```text
claim-verification
        ↓ select claim IDs
claim-transfer
        ↓
downstream figure/report/archive workflow
```

The transfer preserves evidence relations, conflicts, observations, heuristic-score semantics and explicit non-inheritance constraints.

## Why this layer exists

A claim ID by itself is too weak for long-horizon research. Copying only the ID can silently drop:

```text
which evidence was attached
which conflicts were visible
which structural observations existed
which score semantics applied
whether the source audit had any scientific authority
```

`core/claim_transfer.py` makes those conditions travel with the claim reference.

## Explicit transfer constraints

```text
scientific_validity_inherited: false
evidence_sufficiency_inherited: false
peer_review_inherited: false
conflicts_must_remain_visible: true
heuristic_scores_must_retain_non_probability_semantics: true
```

## Coverage without a fake score

The transfer reports counts for selected claims, evidence bindings, conflicts, structural observations and final heuristic scores.

```text
aggregate_score: null
```

This is handoff observability, not a scientific quality metric.

## Global research calibration

Day 6 was rechecked against:

- Praxist (arXiv:2608.25955), which emphasizes reusable solution/evidence lineage across research generations;
- ReproAgent (arXiv:2608.24291), which maintains persistent requirements/reference-evidence contracts across long agent trajectories;
- From Fluent to Verifiable (arXiv:2602.13855), which treats claim-level auditability and contradiction transparency as first-class requirements;
- provenance-grounded autonomous science work already used by this repository.

These works motivate persistence and explicit inheritance boundaries. They do not certify this implementation.

## Six-day architecture position

```text
claim/evidence structure
+ audit observations
+ assertion basis
+ dimensional coverage
+ portable claim transfer
        ↓
evidence-aware downstream handoff
```

## Boundaries

```text
transfer != scientific acceptance
inheritance != validation
conflict preservation != conflict resolution
claim coverage != provenance soundness
heuristic score != probability
provenance != truth
```

No GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge gates are part of this consolidation. Test execution is not used as completion evidence.
