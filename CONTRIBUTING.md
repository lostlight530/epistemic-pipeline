# Contributing

Changes should strengthen explicit research-execution semantics rather than only increase module count.

## Setup

```bash
python -m pip install pyyaml
```

`make test` remains an optional local maintenance command. It is not repository architecture, GitHub merge policy, or scientific validation.

## Contribution rules

- Keep executable graph semantics explicit: duplicate IDs, missing dependencies, cycles and unreachable nodes must remain observable.
- Checkpoint identity is content-sensitive: preserve `graph_id + graph_sha256` binding.
- Current state definitions use `runtime_policies`; machine-readable `check` fields define executable behavior.
- Do not parse human rule prose to invent execution semantics.
- Historical `Gatekeeper` names are compatibility surfaces only; new code should use `RuntimePolicyEvaluator` language.
- Provider integrations implement `LLMProvider`; do not put vendor SDK calls into `StateMachineEngine`.
- Deterministic mock outputs are fixtures, not evidence of real-model quality.
- Preserve bounded heuristic score semantics; do not relabel `[0,1]` as probability without calibration evidence.
- Numerical convergence does not establish truth, consensus or robustness.
- Preserve transient/permanent retry distinction and caller-side thread-timeout limitations.
- Keep local run IDs separate from provider conversation/session identifiers.
- `epistemic-pipeline/prov@2` is W3C PROV-aligned project JSON, not PROV-O RDF.
- `evidence-envelope@1` is a project handoff contract, not an external certification format.
- Provenance/evidence defaults to hashes and structural metadata; full payload capture needs an explicit privacy design.
- Experimental modules and `adaptive.yaml` remain Experimental until deliberately integrated into the canonical engine.
- Update README, ARCHITECTURE, RESEARCH_CONTRACT, AGENTS, MANIFEST and examples when a public capability boundary changes.

## Research integrity

A successful local run or policy evaluation may establish a narrow engineering property. It does not prove:

```text
source truth
scientific validity
probability calibration
external service availability
peer review
independent reproduction
```

## Repository governance

Ordinary research-maintenance contributions must not introduce GitHub Actions, CodeQL, dependency-update bots or merge-gate assumptions unless repository governance is explicitly being redesigned as a separate task.
