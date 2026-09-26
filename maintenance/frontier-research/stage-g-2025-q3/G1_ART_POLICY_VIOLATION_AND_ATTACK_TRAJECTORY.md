# G1 — Agent Red Teaming: Policy Violation as Trajectory Evidence

## Question
What changes when agent security is evaluated through realistic deployment trajectories and large-scale adversarial interaction rather than isolated prompt examples?

## Object
- Research object: *Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition*
- arXiv: `2507.20526`
- Event/publication window: 2025-07-28
- Source type: research paper describing the Agent Red Teaming (ART) benchmark/public competition
- Accessed: 2026-09-26

## Primary source
- https://arxiv.org/abs/2507.20526

## Reported evidence
The paper reports evaluation of 22 frontier agents across 44 realistic deployment scenarios and a large attack corpus, using policy-violation outcomes to study agent security. It reports that successful violations are not limited to one prompt pattern and discusses transferability across attacks/agents.

These are paper-reported benchmark results. This Stage did not reproduce the competition or attacks.

## Interpretation
The epistemic shift is from treating "unsafe output" as a terminal text property toward treating unsafe behavior as an **action trajectory under an adversarial input and policy boundary**.

```text
task / policy
-> adversarial input
-> model interpretation
-> tool/action trajectory
-> environment effect
-> policy evaluator
-> bounded violation outcome
```

For an evidence pipeline, this implies that a terminal outcome cannot explain:
- which attack input mattered;
- which intermediate action crossed the policy boundary;
- what environment/tool authority existed;
- which evaluator/rule classified the behavior;
- whether a superficially similar outcome arose through a different path.

## Boundary
Attack success within a competition/benchmark does not establish universal exploitability or a production incident. A paper-reported violation count does not become local execution evidence.

## Finding
`G1_FINDING`: by Q3 2025, agent security evidence increasingly treats the trajectory itself—policy, adversarial input, actions, effects, and evaluator state—as the object that must be preserved.
