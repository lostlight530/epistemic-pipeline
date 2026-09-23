# Frontier Research Stage Brief — Stage D / 2024-Q4

## Identity
- Repository: `lostlight530/epistemic-pipeline`
- Specification: `2026-09-19-first-batch`
- Stage: `D / 2024-Q4`
- Window: `2024-10-01 through 2024-12-31`
- Record type: `RETROSPECTIVE`
- Coverage intended: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-23`

## Rationale
Stage C established that evaluation evidence needs benchmark vintage, task/domain, evaluator identity, evaluator contract and configuration identity. Stage D asks how Q4 benchmarks further separate scope, freshness, difficulty, held-out data and automated judging.

## Research questions
1. How does a benchmark's task scope constrain what "factuality" or "reasoning" evidence means?
2. How do benchmark refreshes and expert-level difficulty affect comparability without becoming interchangeable notions of quality?
3. How should public/private splits and multi-judge evaluation enter the evidence envelope?

## Planned objects
- SimpleQA, published 2024-10-30.
- LiveBench 2024-11-25 refresh.
- FrontierMath, announced 2024-11-08, benchmark version identified in the announcement.
- FACTS Grounding, introduced 2024-12-17.

## Hard boundaries
```text
benchmark score != model truth
short-form factuality != long-form factuality
fresh questions != contamination-free certification
hard benchmark != universally better benchmark
benchmark family != benchmark vintage
judge output != ground truth
judge ensemble != independent scientific adjudication
public/private split != reproducibility
provider evaluation != independent reproduction
```
