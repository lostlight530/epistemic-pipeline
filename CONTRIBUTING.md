# Contributing

Changes to Epistemic Pipeline are accepted when they strengthen an explicit execution contract rather than only increasing module count.

## Setup

```bash
python -m pip install pyyaml numpy
make test
```

GitHub Actions runs the same contract on pull requests and `main` pushes.

## Contribution rules

- Keep executable graph semantics acyclic and fail-closed.
- New state outputs must match both the provider contract and Gatekeeper inputs.
- Do not put vendor-specific LLM calls inside `StateMachineEngine`; implement the `LLMProvider` protocol.
- Preserve the transient/permanent retry distinction.
- Do not describe caller-side thread timeout as thread cancellation.
- Checkpoint resume stays same-graph unless a new identity/migration design is implemented and tested.
- OTel GenAI names in `RunTracer` are naming alignment only; no SDK compatibility claim without an exporter.
- `epistemic-pipeline/prov@1` is a W3C PROV-aligned JSON profile, not PROV-O RDF.
- Provenance defaults to hashes and structural metadata. Full payload capture requires an explicit design review.
- Experimental modules and `adaptive.yaml` remain Experimental until wired into the canonical execution path with tests.
- Update README, ARCHITECTURE, AGENTS, MANIFEST, and examples when a public capability boundary changes.

## Testing expectations

New behavior needs the nearest deterministic contract. Execution/gating/retry/checkpoint behavior belongs in `tests/test_all.py`; provenance and audited-run behavior belongs in `tests/test_provenance.py`.

A green test suite is evidence for the tested repository boundary, not proof of a real external model or network service.
