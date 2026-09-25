# F2 — Terminal-Bench Environment, Test and Execution Identity

## Evidence
Terminal-Bench launched on 2025-05-19 as an evaluation framework and benchmark for complex terminal tasks. At launch, Terminal-Bench-Core contained 80 hand-crafted, human-verified tasks. Each task has a dedicated Docker environment, a human-verified solution and test cases for checking the agent solution.

Source: https://www.tbench.ai/news/announcement

## Analysis
The benchmark makes execution context part of the evidence object:

```text
task specification
+ Docker environment
+ agent/model/scaffold
+ action trajectory
+ tests
-> task-resolution result
```

A test pass is stronger than a prose claim that the task was solved, but it remains bounded by test coverage and environment identity.

```text
tests_pass
!= universal_correctness
dedicated_container
!= production_environment
```

## Outcome
`SUPPORTED_OBSERVATION`
