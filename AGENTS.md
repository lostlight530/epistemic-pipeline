# Agent Guide — epistemic-pipeline

This is the operational contract for agents changing the repository. `README.md`, `ARCHITECTURE.md`, and `MANIFEST.yaml` define the public capability boundary.

## 1. System map

```text
graphs/*.yaml
  -> core/engine.py
     -> role templates
     -> core/llm_harness.py
     -> core/gatekeeper.py
     -> core/confidence_net.py @ synthesize
     -> core/resilience.py
     -> checkpoints/
     -> core/run_tracer.py -> traces/

core/run_bundle.py
  -> StateMachineEngine
  -> core/provenance.py
  -> provenance/<run_id>.prov.json
```

Executable graphs: `linear`, `parallel`, `diamond`. `adaptive` remains Experimental.

## 2. Setup and full contract

```bash
python -m pip install pyyaml numpy
make test
```

`make test` runs `tests/test_all.py` plus `tests/test_provenance.py`. GitHub Actions runs the same contract under Python 3.12.

## 3. Entry points

Low-level execution:

```bash
python3 core/engine.py validate graphs/linear.yaml
python3 core/engine.py run graphs/linear.yaml
```

Audited execution:

```bash
python3 core/run_bundle.py graphs/linear.yaml
python3 core/run_bundle.py graphs/parallel.yaml --trace-dir traces --checkpoint-dir checkpoints --provenance-dir provenance
```

Use the audited entry point when a research run must leave trace/checkpoint/provenance evidence together.

## 4. Hard rules

1. **State machine first.** New execution behavior must map to the canonical state model or explicitly introduce a versioned state extension.
2. **Gatekeeper is not optional documentation.** New state outputs must provide the keys consumed by their quality gates; unknown prefixes must not silently fail open.
3. **Provider contract stays vendor-neutral.** Real model integrations implement `LLMProvider`; do not hard-code vendor SDK calls into `StateMachineEngine`.
4. **Mock honesty.** Deterministic mock outputs are test fixtures, not evidence of real model performance.
5. **Confidence honesty.** Mock confidence is heuristic. Do not call it calibrated probability without labelled calibration evidence.
6. **Retry taxonomy.** Permanent errors fail fast; only transient classes are retried.
7. **Timeout honesty.** Thread timeout fails the caller but cannot kill the underlying worker thread.
8. **Same-graph resume.** Checkpoint reuse across a different graph remains fail-closed.
9. **Trace scope.** OTel GenAI field names are naming alignment only; project JSONL is not an OTel exporter.
10. **Provenance scope.** `epistemic-pipeline/prov@1` uses W3C PROV core semantics but is not PROV-O RDF. Preserve that wording.
11. **No payload duplication by default.** Provenance stores hashes and structural metadata. Adding full payload capture requires an explicit privacy/security design.
12. **Stable provenance profile.** Breaking entity/relation semantics requires a new profile version.
13. **Experimental stays Experimental.** `adaptive` and the experimental modules are not promoted because they import successfully.

## 5. Where to change what

| Goal | Files | Required checks |
|---|---|---|
| new executable graph | `graphs/`, `core/engine.py` if semantics change | DAG validation + run test + docs |
| new state/gate | `states/`, `validators/`, `core/gatekeeper.py` | provider output contract + failure test |
| provider integration | `core/llm_harness.py` or external adapter | contract tests, no engine vendor coupling |
| retry/timeout | `core/resilience.py`, node YAML | transient/permanent tests |
| checkpoint semantics | `core/engine.py` | resume and cross-graph fail-closed tests |
| trace field | `core/run_tracer.py` | hash-chain test + OTel scope review |
| provenance entity/relation | `core/provenance.py` | privacy + lineage tests + profile-version review |
| audited CLI | `core/run_bundle.py` | success/failure bundle tests |
| public capability | README/ARCHITECTURE/MANIFEST | update together |

## 6. Provenance invariants

For every completed node represented in a run bundle:

- an output `prov:Entity` is identified by canonical SHA-256,
- a node `prov:Activity` records state/stage/status,
- the output `wasGeneratedBy` the node activity,
- the activity `wasAssociatedWith` the software agent,
- dependency outputs are `used` and current output `wasDerivedFrom` them when available.

The full node payload must not appear in the provenance JSON under the default profile.

## 7. Before completion

- `make test` is the intended repository gate,
- docs and MANIFEST reflect actual wiring,
- no real-LLM claim was inferred from mock execution,
- no PROV/OTel compatibility claim exceeds the implemented profile,
- new runtime artifacts are gitignored,
- any new dependency is justified and documented.
