# Customization Guide

## 1. Choose the smallest layer

Epistemic Pipeline separates graph topology, state definition, provider execution, provider disclosure, runtime policy, bounded score propagation, resilience, trace, checkpoint identity, provenance, claim-aware audit and cross-tool evidence handoff.

Extend the smallest layer that actually owns the requirement.

## 2. Add or modify an executable graph

Executable graphs contain `nodes` with `id`, `stage` and `dependencies`.

```bash
python3 core/engine.py validate graphs/linear.yaml
```

Validation checks duplicate IDs, unknown dependencies, cycles and reachability. `adaptive.yaml` remains an Experimental specification, not an executable DAG.

Checkpoint resume is bound to both graph ID and canonical graph SHA-256. A changed graph with the same ID is a different executable definition.

## 3. Add or modify a state

Keep these contracts aligned:

1. state outputs and role bindings;
2. `LLMProvider` / `MockProvider` structured output keys;
3. `runtime_policies` machine-readable checks;
4. downstream score/evidence expectations.

Example:

```yaml
runtime_policies:
  - id: claims_exist
    check: non_empty
    field: claims_registry
```

Do not encode executable behavior only in prose.

## 4. Add a runtime policy predicate

Implement the predicate in `RuntimePolicyEvaluator._evaluate_rule()` and reference it through a stable `check` name.

Unknown checks fail explicitly. A predicate should establish a narrow structural/numeric property; it must not claim semantic truth that the code cannot evaluate.

Historical `quality_gates` input is accepted only for compatibility.

## 5. Add a real model provider

Implement:

```text
LLMProvider.complete(system, user, schema) -> dict
```

and inject it into the harness/engine. Keep provider/session/model identifiers explicit. Do not reinterpret project-local `run_id` as provider conversation identity.

For process disclosure, optionally override:

```text
LLMProvider.describe() -> dict
```

Recommended declared fields include:

```text
provider_class
provider
model
version
mode
external_model_call
metadata_semantics
```

Unknown vendor/model/version values should remain `None`/unknown. Do not derive a model name from filenames, environment assumptions, prompt content or marketing defaults.

A provider label is process metadata, not evidence that the model is correct or that a particular output is authentic.

## 6. Configure resilience

Nodes may declare retry/timeout parameters supported by `core/resilience.py`.

- Retry only failures classified as transient.
- A caller-side thread timeout cannot kill an already running Python worker.
- External side effects therefore require their own idempotency/cancellation design.

## 7. Use checkpoints

```bash
python3 core/engine.py run graphs/linear.yaml --resume-from <run_id>
```

Current `checkpoint@2` requires matching:

```text
graph_id
graph_sha256
```

Legacy checkpoints without digest identity are rejected as ambiguous.

## 8. Produce an evidence-bearing run

```bash
python3 core/run_bundle.py graphs/linear.yaml
```

Optionally declare the human-review state of the run/handoff:

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

Default: `not_declared`.

The wrapper can produce:

```text
traces/<run_id>.jsonl
checkpoints/<run_id>/checkpoint.json
provenance/<run_id>.prov.json
evidence/<run_id>.evidence.json
```

Custom directories:

```bash
python3 core/run_bundle.py graphs/parallel.yaml \
  --trace-dir traces \
  --checkpoint-dir checkpoints \
  --provenance-dir provenance \
  --evidence-dir evidence \
  --human-review partial
```

## 9. Extend provenance

`core/provenance.py` uses `epistemic-pipeline/prov@2`.

When changing entity/relation semantics:

- use stable logical identifiers;
- preserve canonical/file SHA-256 distinctions;
- avoid full payload duplication by default;
- bump the profile when existing meaning breaks;
- never claim PROV-O RDF conformance without an actual serializer.

## 10. Extend claim-aware audit

`core/run_bundle.py` derives `epistemic-pipeline/claim-index@1` from structured `claims_registry` and `evidence_chains` outputs.

Current index fields are intentionally narrow:

```text
claim_id
state_id
claim_record_sha256
source_refs[]
evidence_refs[]
relations[]
```

Full claim prose is not embedded in the Evidence Envelope.

If extending the index:

- add only fields that answer a concrete audit/handoff question;
- preserve the distinction between identity/reference and scientific truth;
- do not compute “truth scores” from the presence/number of evidence refs;
- do not infer entailment from relation labels;
- update `CLAIM_AUDIT_CONTRACT.md`, README, Architecture and Manifest together.

## 11. Extend process disclosure

Provider disclosure comes from `LLMProvider.describe()`. Human-review disclosure is caller supplied.

Do not add optimistic defaults:

```text
missing provider ≠ no AI used
missing human_review ≠ reviewed
model name ≠ capability proof
human review ≠ peer review
```

If a new disclosure field would adjudicate authorship, source credibility, journal policy compliance or scientific validity, it belongs outside this bounded project profile unless a separate explicit system is designed.

## 12. Extend the Evidence Envelope

`core/evidence_envelope.py` implements `epistemic-pipeline/evidence-envelope@2`, separate from PROV lineage.

Current major sections include:

```text
graph
artifacts
profiles
integrity
claim_observability
process_disclosure
confidence_semantics
reproducibility
scientific_validity_claim
payloads_embedded
```

New fields should answer a concrete interoperability question and preserve explicit boundaries.

A downstream RO-Crate mapping may consume this envelope, but this repository does not currently emit an RO-Crate itself.

## 13. Work with heuristic scores

Historical `confidence_*` field names may remain for compatibility. Treat them as bounded heuristic scores unless an external calibration contract says otherwise.

Do not add a calibration claim merely because a monotonic transform exists.

## 14. Experimental modules

Experimental modules are safe places to explore bounded mechanisms, but their filenames are not capability claims. Do not wire an Experimental module into `StateMachineEngine` merely because it was corrected or documented.

## 15. Local maintenance

```bash
python -m pip install pyyaml
make test
```

Keep README, ARCHITECTURE, RESEARCH_CONTRACT, CLAIM_AUDIT_CONTRACT, AGENTS, MANIFEST, CONTRIBUTING and examples synchronized with public behavior.
