# Evidence Chart — Stage B / 2024-Q2

## Identity

- Repository: lostlight530/epistemic-pipeline
- Coverage: SEARCH_BOUNDED
- Charted: 2026-09-22

## Variables

- model revision
- benchmark family/revision/vintage
- task/condition set
- input/context length
- prompt/judge/scoring method
- contamination-assessment method
- correction state
- source family
- execution date
- reproduction state

## Findings

| ID | Observation | Object | Source | Independence | Boundary |
|---|---|---|---|---|---|
| F1 | long-context performance can degrade far below nominal context claims under harder tasks | O1 | S1-S2 | one family | effective capability is condition-bounded |
| F2 | WMDP dataset/method state changed on 2024-04-23 | O2 | S3 | one family | correction does not erase prior state |
| F3 | contamination can be operationalized as benchmark-specific non-generalizing performance inflation | O3 | S4 | one family | detection != exact provenance |
| F4 | MMLU-Pro increases difficulty and reports lower prompt sensitivity in its experiments | O4 | S5-S6 | one family | harder != universally valid |
| F5 | LiveBench makes benchmark vintage/refresh part of evaluation design | O5 | S7-S8 | one family | live != permanently uncontaminated |
| F6 | LiveBench removed a task on 2024-06-24 after answer-parsing ambiguity | O5 | S7 | same family | objective/live benchmark still correctable |

## Cross-object analysis

Stage B shifts the evidence envelope from a mostly versioned container around a benchmark result to an object whose benchmark definition is itself temporal and revisable

A comparison-ready observation increasingly requires:

    model revision
    + benchmark family/revision/vintage
    + task and condition distribution
    + prompt/judge/scoring method
    + contamination assessment
    + execution date
    + source provenance

## Counterevidence

No evidence supports one universal benchmark-age threshold, one contamination detector, or one static notion of comparability

## Amendment

NONE
