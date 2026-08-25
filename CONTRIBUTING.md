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
- External providers may override `LLMProvider.describe()` for bounded provider/model/version disclosure. Unknown metadata must remain unknown rather than guessed.
- Deterministic mock outputs are fixtures, not evidence of real-model quality. `MockProvider` must continue to declare `external_model_call: false`.
- Preserve bounded heuristic score semantics; do not relabel `[0,1]` as probability without calibration evidence.
- Numerical convergence does not establish truth, consensus or robustness.
- Preserve transient/permanent retry distinction and caller-side thread-timeout limitations.
- Keep local run IDs separate from provider conversation/session identifiers.
- `epistemic-pipeline/prov@2` is W3C PROV-aligned project JSON, not PROV-O RDF.
- `epistemic-pipeline/claim-index@1` is an audit/reference index, not a truth graph. Source/evidence references do not prove credibility or sufficiency.
- `epistemic-pipeline/process-disclosure@1` records provider and declared human-review context only; `reviewed` is not peer review.
- `epistemic-pipeline/evidence-envelope@2` is a project handoff contract, not an external certification format.
- Provenance/evidence defaults to hashes and structural metadata; full payload capture needs an explicit privacy design.
- Claim text remains outside the Evidence Envelope by default; do not silently duplicate provider payloads into audit metadata.
- Experimental modules and `adaptive.yaml` remain Experimental until deliberately integrated into the canonical engine.
- Update README, ARCHITECTURE, RESEARCH_CONTRACT, CLAIM_AUDIT_CONTRACT, AGENTS, MANIFEST and examples when a public capability boundary changes.

## Research integrity

A successful local run, claim index, provider disclosure, human-review declaration or policy evaluation may establish a narrow engineering property. It does not prove:

```text
source truth
claim truth
evidence sufficiency
scientific validity
probability calibration
provider/model validity
authorship
peer review
external service availability
independent reproduction
```

## Repository governance

Ordinary research-maintenance contributions must not introduce GitHub Actions, CodeQL, dependency-update bots or merge-gate assumptions unless repository governance is explicitly being redesigned as a separate task.
