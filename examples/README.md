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

Optionally declare the run/handoff's human-review state:

```bash
python3 core/run_bundle.py graphs/linear.yaml --human-review reviewed
```

Allowed values:

```text
reviewed
partial
not_reviewed
not_declared
```

The default is `not_declared`; missing review metadata is never inferred as reviewed.

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

### Claim-aware index

The run bundle scans structured `claims_registry` and `evidence_chains` outputs and builds:

```text
epistemic-pipeline/claim-index@1
```

Example logical shape:

```json
{
  "claim_id": "c1",
  "state_id": "analyze",
  "claim_record_sha256": "sha256:...",
  "source_refs": ["src_001"],
  "evidence_refs": ["src_001#seg_001"],
  "relations": ["declared_by_fixture"]
}
```

The Evidence Envelope does **not** embed claim prose. The index is for discoverability/audit/handoff, not truth adjudication.

```text
claim hash ≠ claim truth
source ref ≠ source credibility
evidence ref ≠ evidence sufficiency
```

### Provider disclosure

`LLMProvider.describe()` can expose bounded process metadata for an injected provider. The base class leaves provider/model/version unknown rather than guessing.

`MockProvider` explicitly declares itself as a local synthetic fixture with:

```text
external_model_call: false
```

Provider/model metadata is not evidence of scientific validity or output authenticity.

### Evidence Envelope

`epistemic-pipeline/evidence-envelope@2` references graph / trace / checkpoint / provenance files with SHA-256 identity and adds:

```text
claim_observability
process_disclosure
```

The envelope declares score/reproducibility/scientific-validity boundaries for downstream tools and keeps:

```text
payloads_embedded: false
claim_observability.payload_text_embedded: false
scientific_validity_claim: false
```

It is a project interchange object, not an external certification format.

A downstream figure recipe can reference this envelope and use its claim IDs, for example through `sci-render-kit/figure-claim-binding@1`, without requiring direct runtime coupling.

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

The command is a local maintenance aid. No GitHub workflow is required by the repository architecture, and this 2026-08-26 maintenance pass does not use test execution as its completion criterion.
