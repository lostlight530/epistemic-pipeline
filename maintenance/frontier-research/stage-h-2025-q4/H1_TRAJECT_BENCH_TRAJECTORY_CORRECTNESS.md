# H1 — TRAJECT-Bench: Trajectory Correctness Beyond Final Accuracy

## Source identity
- arXiv:2510.04550v1
- v1 submitted: 2025-10-06
- Primary source: https://arxiv.org/abs/2510.04550

## Frontier observation
TRAJECT-Bench evaluates tool-use trajectories using diagnostics such as tool selection, argument correctness, and dependency/order satisfaction in addition to final task accuracy.

For epistemic-pipeline this sharpens the execution-evidence envelope:

```text
task
-> candidate tools
-> selected tool
-> arguments
-> dependency/order
-> intermediate trajectory
-> final output
```

A correct-looking final answer can coexist with a wrong or unsupported path.

## Boundary
- execution-plan/trajectory match != claim truth
- correct tool choice != correct external state
- final success != justified intermediate evidence
- benchmark construction != production execution

## Repository interpretation
This is evaluation calibration only. No TRAJECT-Bench task or model run was reproduced locally.
