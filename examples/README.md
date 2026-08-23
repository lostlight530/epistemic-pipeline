# Epistemic Pipeline Examples

## Validate an executable graph

```bash
python3 core/engine.py validate graphs/linear.yaml
```

`linear`, `parallel`, and `diamond` are executable. `adaptive` remains an experimental routing specification and is rejected by the current engine.

## Run the low-level engine

```bash
python3 core/engine.py run graphs/linear.yaml
python3 core/engine.py run graphs/parallel.yaml
```

The repository default uses deterministic mock provider output. A successful local run is not evidence of a live external LLM.

## Resume from a checkpoint

```bash
python3 core/engine.py run graphs/linear.yaml --resume-from <run_id>
```

Only successful states from the same graph are reusable.

## Run with a provenance bundle

```bash
python3 core/run_bundle.py graphs/linear.yaml
```

The audited wrapper composes:

```text
engine result
+ traces/<run_id>.jsonl
+ checkpoints/<run_id>/checkpoint.json (when present)
+ provenance/<run_id>.prov.json
```

The provenance sidecar uses canonical hashes and W3C PROV-aligned Entity / Activity / Agent relationships. It does not copy full node payloads by default.

## Verify repository contracts

```bash
make test
```

The contract covers the existing execution/gating/reliability suite plus provenance and audited-run behavior. GitHub Actions runs the same command on pull requests and main-branch pushes.
