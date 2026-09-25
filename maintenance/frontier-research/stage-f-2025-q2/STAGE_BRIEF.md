# Frontier Research Stage Brief — Stage F / 2025-Q2

## Identity
- Repository: `lostlight530/epistemic-pipeline`
- Specification: `2026-09-19-first-batch`
- Stage: `F / 2025-Q2`
- Window: `2025-04-01 through 2025-06-30`
- Record type: `RETROSPECTIVE`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- Coverage: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-25`
- Status: `COMPLETE`

## Rationale
Stage E expanded the evaluation object from difficult questions to economically situated tasks and underspecified problems. Stage F asks what changes when evaluation becomes long-horizon execution: reproducing research, operating in a terminal environment, and coordinating with a user who can also change shared state.

## Research questions
1. What does PaperBench add when the target is end-to-end research replication?
2. What does Terminal-Bench add when task identity includes a dedicated Docker environment, human solution and executable tests?
3. What does τ²-Bench add when both agent and user can act on a shared dynamic environment?

## Hard boundaries
```text
benchmark score != scientific reproduction
test pass != universal task competence
Docker environment != production environment
judge score != truth
dual-control success != general coordination competence
trajectory success != causal explanation
```
