# Customization Guide

## 1. Choose the layer you are changing

Epistemic Pipeline deliberately separates graph topology, epistemic state, provider execution, quality gates, resilience, traces, and provenance. Extend the smallest layer that matches the problem.

## 2. Add or modify an executable graph

Executable graphs contain `nodes` with `id`, `stage`, and `dependencies`. Validate before running:

```bash
python3 core/engine.py validate graphs/linear.yaml
```

`adaptive.yaml` is currently an experimental routing specification, not an executable DAG.

## 3. Add a state or quality gate

A state extension must keep three contracts aligned:

1. state YAML fields and role bindings,
2. `LLMProvider` / `MockProvider` structured output keys,
3. Gatekeeper enforcement logic.

A new state prefix that the Gatekeeper does not understand must not silently pass.

## 4. Add a real model provider

Implement:

```text
LLMProvider.complete(system, user, schema) -> dict
```

and inject the provider into the harness/engine. Do not replace the deterministic mock in repository tests with live network calls.

## 5. Configure resilience

Nodes may declare retry and timeout parameters supported by `core/resilience.py`. Retry only transient failures. Remember that a thread timeout returns control to the caller but does not terminate the underlying worker thread.

## 6. Use checkpoints

```bash
python3 core/engine.py run graphs/linear.yaml --resume-from <run_id>
```

Resume reuses successful nodes from the same graph. Cross-graph reuse is intentionally rejected.

## 7. Produce an audited research run

```bash
python3 core/run_bundle.py graphs/linear.yaml
```

The wrapper preserves the existing trace/checkpoint behavior and adds `provenance/<run_id>.prov.json`.

Customize output locations without changing the profile semantics:

```bash
python3 core/run_bundle.py graphs/parallel.yaml \
  --trace-dir traces \
  --checkpoint-dir checkpoints \
  --provenance-dir provenance
```

## 8. Extend provenance

`core/provenance.py` currently represents graph, node-output, trace, and checkpoint entities using W3C PROV-aligned semantics. When adding a new entity or relation:

- use a stable logical identifier,
- keep canonical SHA-256 for content identity,
- do not embed full payloads by default,
- add lineage tests,
- bump `epistemic-pipeline/prov@1` if existing semantics break,
- never claim PROV-O RDF conformance unless an actual conforming serializer is implemented.

## 9. Verify

```bash
make test
```

Keep README, ARCHITECTURE, AGENTS, MANIFEST, CONTRIBUTING, and examples aligned with the resulting capability boundary.
