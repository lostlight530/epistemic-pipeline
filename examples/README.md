# Epistemic Pipeline Examples

## Validate an executable graph

```bash
python3 core/engine.py validate graphs/linear.yaml
```

`linear`, `parallel`, and `diamond` are executable. `adaptive` remains Experimental.

Validation covers graph structure; it does not evaluate research truth.

## Run the low-level engine

```bash
python3 core/engine.py run graphs/linear.yaml
python3 core/engine.py run graphs/parallel.yaml
```

The default provider is deterministic `MockProvider`. A successful local run is not evidence of a live external model.

The engine result includes graph identity such as:

```text
graph_id
graph_sha256
engine_profile
```

## Resume from a digest-bound checkpoint

```bash
python3 core/engine.py run graphs/linear.yaml --resume-from <run_id>
```

`checkpoint@2` reuses successful nodes only when both graph ID and canonical graph SHA-256 match. Same name with changed graph content is rejected.

## Runtime policies

Current state YAML uses machine-readable rules:

```yaml
runtime_policies:
  - id: report_complete
    check: mapping_required_keys
    field: synthesis_report
    required_keys:
      - summary
      - comparison
      - insights
      - recommendation
      - confidence_semantics
```

A policy pass means the declared predicate passed. It does not mean the report is scientifically correct.

## Produce a research evidence bundle

```bash
python3 core/run_bundle.py graphs/linear.yaml
```

The wrapper composes available artifacts:

```text
engine result
+ traces/<run_id>.jsonl
+ checkpoints/<run_id>/checkpoint.json
+ provenance/<run_id>.prov.json
+ evidence/<run_id>.evidence.json
```

### Provenance

`epistemic-pipeline/prov@2` records W3C PROV-aligned Entity / Activity / SoftwareAgent relationships in project JSON. It stores canonical hashes and structural metadata rather than duplicating full node payloads by default.

### Evidence Envelope

`epistemic-pipeline/evidence-envelope@1` references graph / trace / checkpoint / provenance files with SHA-256 identity and declares score/reproducibility/scientific-validity boundaries for downstream tools.

It is a project interchange object, not an external certification format.

## Score semantics

The score network produces bounded heuristic values in `[0,1]`.

```text
heuristic score ≠ probability
numerical convergence ≠ certainty
```

Temperature scaling in this repository is a transform unless a separate labelled-data fitting/evaluation process exists.

## Optional local maintenance

```bash
python -m pip install pyyaml
make test
```

The command is a local maintenance aid. No GitHub workflow is required by the repository architecture.
