# Contributing

Changes to Epistemic Pipeline should strengthen an explicit execution model rather than only increase module count.

## Setup

```bash
python -m pip install pyyaml numpy
```

`make test` is available as an optional local maintenance check. It is not a GitHub merge gate.

## Contribution rules

- Keep executable graph semantics acyclic and fail-closed.
- New state outputs must match both the provider contract and Gatekeeper inputs.
- Do not put vendor-specific LLM calls inside `StateMachineEngine`; implement the `LLMProvider` protocol.
- Preserve the transient/permanent retry distinction.
- Do not describe caller-side thread timeout as thread cancellation.
- Checkpoint resume stays same-graph unless a new identity/migration design is implemented.
- OTel GenAI names in `RunTracer` are naming alignment only; no SDK compatibility claim without an exporter.
- `epistemic-pipeline/prov@1` is a W3C PROV-aligned JSON profile, not PROV-O RDF.
- Provenance defaults to hashes and structural metadata. Full payload capture requires an explicit design review.
- Experimental modules and `adaptive.yaml` remain Experimental until wired into the canonical execution path.
- Update README, ARCHITECTURE, AGENTS, MANIFEST, and examples when a public capability boundary changes.

## Local checks

Execution/gating/retry/checkpoint behavior can be inspected with `tests/test_all.py`; provenance and audited-run behavior can be inspected with `tests/test_provenance.py` when useful. A successful local check is evidence for that checked boundary, not proof of a real external model or network service.
