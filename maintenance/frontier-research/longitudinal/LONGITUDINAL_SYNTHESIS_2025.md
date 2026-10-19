# Longitudinal Frontier Synthesis — Calendar Year 2025

## Identity and research boundary
- Repository: `lostlight530/epistemic-pipeline`
- Historical research period: 2025-01-01 through 2025-12-31
- Document synthesis date: 2026-10-19; **retrospective**, not contemporaneous publication
- Included Stages: E, F, G, H; method: `TARGETED_EVIDENCE_SYNTHESIS` + chronological process-tracing of prior Stage research
- Source coverage: `SOURCE_BOUNDED` to repository-native Stage and monthly files; Stage-local methods are `SEARCH_BOUNDED`
- State: `COMPLETE` as a bounded yearly interpretive artifact; independent reviewer: `INDEPENDENCE_NOT_ESTABLISHED`
- No benchmark run, evaluator replay, external reproduction, new independent source search or runtime-contract audit is claimed.

## Annual question
Across 2025, what evidence becomes necessary to interpret an agent or model result as **a bounded claim about a task performed in a specific environment**? Which aspects of authority, uncertainty, trajectory and evaluator identity can be compared across research objects, and which cannot?

## Month-level input ledger and stage ownership
The twelve original month reconstructions (each with its Stage evidence scope, not twelve independently reproduced experiments): [2025-01](../stage-e-2025-q1/MONTH_2025_01_RECONSTRUCTION.md) · [2025-02](../stage-e-2025-q1/MONTH_2025_02_RECONSTRUCTION.md) · [2025-03](../stage-e-2025-q1/MONTH_2025_03_RECONSTRUCTION.md) · [2025-04](../stage-f-2025-q2/MONTH_2025_04_RECONSTRUCTION.md) · [2025-05](../stage-f-2025-q2/MONTH_2025_05_RECONSTRUCTION.md) · [2025-06](../stage-f-2025-q2/MONTH_2025_06_RECONSTRUCTION.md) · [2025-07](../stage-g-2025-q3/MONTH_2025_07_RECONSTRUCTION.md) · [2025-08](../stage-g-2025-q3/MONTH_2025_08_RECONSTRUCTION.md) · [2025-09](../stage-g-2025-q3/MONTH_2025_09_RECONSTRUCTION.md) · [2025-10](../stage-h-2025-q4/MONTH_2025_10_RECONSTRUCTION.md) · [2025-11](../stage-h-2025-q4/MONTH_2025_11_RECONSTRUCTION.md) · [2025-12](../stage-h-2025-q4/MONTH_2025_12_RECONSTRUCTION.md).

| Quarter owner | Analytical class | Named native research objects | Research delta |
|---|---|---|---|
| [Stage E](../stage-e-2025-q1/STAGE_SYNTHESIS.md) | expert-question calibration; real paid software tasks; information acquisition | HLE (January), SWE-Lancer (February), QuestBench (March) | Task difficulty, real environment/evaluator authority and missing-information state cannot be collapsed into one score. |
| [Stage F](../stage-f-2025-q2/STAGE_SYNTHESIS.md) | execution trace and actor/environment ownership | PaperBench (April), Terminal-Bench (May), τ²-Bench (June) | Replication trajectory, terminal tests and a second actor's mutable world state enlarge the evidence envelope. |
| [Stage G](../stage-g-2025-q3/STAGE_SYNTHESIS.md) | adversarial and long-horizon trajectories | Agent Red Teaming (July), LiveMCP-101 (August), UltraHorizon (September) | Policy context, expected tool plans, memory, observations and action-state ordering become first-class. |
| [Stage H](../stage-h-2025-q4/STAGE_SYNTHESIS.md) | adaptive tool environment, costs and replanning | TRAJECT-Bench (October), CostBench (November), MCPAgentBench (December) | Trajectory correctness, mutable cost/blocking and toolset/distractor identity separate completion from efficiency. |

These are different tasks and research designs. HLE calibration, freelance software grading, information acquisition, paper replication, terminal execution, multi-actor state, tool planning, long-horizon memory, adversarial policy tests and dynamic tool pricing do **not** share a common sample frame or evaluator. Do not numerically pool their scores.

## Turning points and temporal mechanism
1. **Q1: what is the task and what is missing?** A hard closed-ended exam question, a paid repository-centered task and a deliberately underspecified prompt demand different evidence. Question difficulty does not substitute for task-state and grading-authority identity; success after clarification does not prove correctness without the missing-information history.
2. **Q2: what happened between prompt and grade?** End-to-end research replication, executable terminal tests and environments affected by a second actor make intermediate operations and control boundaries inspectable. A terminal success flag cannot reconstruct who changed state or what a test actually assessed.
3. **Q3: under what policy and observation history?** Adversarial inputs, expected tool plans and partially observed long-horizon worlds make policy, tool selection, retained memory and observation freshness independent dimensions. A final answer can conceal an invalid trajectory.
4. **Q4: which tool environment was available at decision time?** TRAJECT-Bench separates plan/tool correctness from final accuracy; CostBench makes cost and tool availability dynamic; MCPAgentBench requires candidate/distractor toolset and efficiency/completion labels. Evaluation requires **time-indexed tool environment** and replanning identity, not merely a static tool manifest.

The direction across these selected objects is a research interpretation, not an independently observed historical law of agent evaluation.

## Stable dimensions, counterevidence and non-comparability
| Dimension | 2025 research treatment | Claim boundary |
|---|---|---|
| task / information state | difficulty, economic task, unknown input, clarification | benchmark design != real-world prevalence |
| actor / authority | model, user, tool, evaluator and policy roles | task-specific roles are not interchangeable |
| environment | repository, terminal, mutable multi-actor world, available toolset | described environment != executed local environment |
| trajectory | plan, arguments, ordering, actions, observations, memory, replanning | good endpoint != justified process |
| outcome | rubric, tests, completion, efficiency, calibration | score != truth/probability and judges differ |
| evidence maturity | selected public research artifacts and bounded claims | no independently rerun benchmark result here |

Competing reading: later selected benchmarks may encode more complex tasks because of **our object selection and benchmark framing**, not because all field evaluation practices improved monotonically. Neither independent accuracy statistics nor a representative benchmark landscape census is established. Reports from one benchmark origin are not treated as multiple independent validations.

## Cross-Stage synthesis
The 2025 epistemic evidence model becomes:

```text
claim / instruction / task identity
 -> provided versus missing information
 -> authority + policy + evaluator identity
 -> environment and allowed toolset snapshot
 -> plan / actions / arguments / order
 -> observed + remembered + externally mutated state
 -> replanning, cost and blocking state
 -> judge/test/completion/efficiency record
 -> bounded claim with uncertainty and transfer restriction
```

Every arrow is an evidence question. No arrow transfers correctness, calibrated probability or an evaluator's authority to the next surface. Stage E's task-state problem remains alive in H's adaptive toolset: a result cannot be decontextualized from information that was available when the agent chose an action. The annual contribution is **a traceability model for comparing evidence envelopes**, not a better score.

## Contradictions, negative space and correction
- The Stages do not establish one comparable cross-benchmark numerical performance trajectory. `NOT_COMPARABLE` is the correct label, not `IMPROVED`.
- No independent benchmark re-execution, task-by-task scoring audit, tool trace playback, exact-version reproduction or scientific adjudication was performed for this document.
- Temporal claims are inherited from dated Stage source registers and Parts; older Stage files are not revised. Future corrections must use append-only reconciliation.
- Previous [A→G longitudinal synthesis](LONGITUDINAL_SYNTHESIS_2024_TO_2025_Q3.md) remains intact with its earlier source cutoff.

## Current repository and export boundary
`claim indexed != claim true`; `evidence linked != evidence sufficient`; `heuristic score != probability`; `verification != scientific adjudication`; `transfer != acceptance`; `provenance != truth`.

This analysis does not independently establish current implementation drift and does not justify runtime/contract changes. Exported cross-L3 findings do not confer evidence authority upon another repository. Source-to-Stage cross-reading was performed; reviewer independence and current local runtime were not validated.

## Subsequent research
2026 must be researched as its own **dated monthly reconstructions + native quarterly Stage(s)** before any 2026 annual synthesis. SDK announcements and protocol revisions are candidate external sources, not evidence that a 2026 Stage was executed. Preserve the inherited `Stage I NOT_EVIDENCED` until the native research record is available.
