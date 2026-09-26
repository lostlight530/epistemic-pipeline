# Frontier Research Stage Brief — Stage G / 2025-Q3

## Identity
- Repository: `lostlight530/epistemic-pipeline`
- Specification: `2026-09-19-first-batch`
- Stage: `G / 2025-Q3`
- Window: `2025-07-01 through 2025-09-30`
- Record type: `RETROSPECTIVE`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- Coverage: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-26`
- Status: `COMPLETE`

## Rationale
Stage F moved the evidence story from task specification into execution trajectories: replication steps, concrete environments/tests, actor identity, and shared-state transitions. Stage G follows the next quarter as the trajectory itself becomes more demanding and more adversarial.

The quarter is reconstructed through three complementary research objects:
- agent red-teaming where policy violations emerge through realistic deployment trajectories;
- multi-tool MCP tasks evaluated against ground-truth execution plans;
- very long partially observable tasks where memory, planning, and tool management must survive tens to hundreds of actions.

## Research questions
1. What does large-scale agent red-teaming add when unsafe behavior is measured as trajectory-level policy violation rather than a single bad answer?
2. What changes when tool-use evaluation compares an agent against an expected execution plan rather than only final/API outputs?
3. What evidence becomes necessary when tasks are long-horizon and partially observable enough that memory and intermediate state dominate outcome interpretation?

## Hard boundaries
```text
benchmark attack success != universal exploitability
policy violation in benchmark != production incident
execution-plan match != scientific truth
benchmark success != general competence
long trace != correct trace
partial observability benchmark != production world model
paper result != independent reproduction
```
