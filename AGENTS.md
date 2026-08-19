# Agent Guide — Quick Start

Operational manual for agents assigned to run, extend, or customize `epistemic-pipeline`. Read this file first; it tells you how to run the pipeline, where things live, how to add nodes/states, and what you must not do.

## 0. Setup & First Run

Dependencies: **only `pyyaml` and `numpy`** (plus the Python 3 standard library). Nothing else may be added.

```bash
pip install pyyaml numpy

python3 tests/test_all.py          # full suite, must stay 36/36 (or: make test)
python3 core/engine.py run graphs/linear.yaml        # end-to-end run, mock LLM
python3 core/engine.py validate graphs/parallel.yaml # DAG validation only
python3 core/engine.py run graphs/linear.yaml --resume-from <run_id>  # resume from checkpoint
```

CLI flags (`core/engine.py`): `run|validate <graph> [--resume-from RUN_ID] [--checkpoint-dir DIR] [--trace-dir DIR]`. Defaults: `checkpoints/`, `traces/`. Both are run artifacts and are gitignored.

Engine constructor switches not exposed on the CLI: `mock_llm` (default `True`), `use_gatekeeper` (default `True`), `use_confidence_net` (default `True`), `harness=` (inject a custom `LLMProvider`), `trace_dir=None` / `checkpoint_dir=None` (disable tracing / checkpoints), `calibration_temperature=` (apply temperature scaling at synthesize).

## 1. Directory Tour

| Path | Contents |
|---|---|
| `core/engine.py` | `StateMachineEngine` — the only entry point into the execution chain |
| `core/dependency_graph.py` | DAG validation (cycle / unreachable detection), parallel grouping |
| `core/gatekeeper.py` | Quality-gate enforcement on node outputs |
| `core/llm_harness.py` | `LLMProvider` protocol + `MockProvider` (default) + prompt assembly |
| `core/confidence_net.py` | Confidence network; runs at `synthesize` nodes |
| `core/knowledge_extractor.py` | Static bridge: upstream claims/conflicts → network input format |
| `core/run_tracer.py` | Structured JSONL trace per run, SHA-256 hash chain |
| `core/resilience.py` | Retry policy (exponential backoff + jitter), per-node timeout, error classification |
| `core/calibration.py` | Temperature-scaling hook on converged confidence values |
| `core/{anti_entropy,convergence,infinite_regression,neuro_symbolic,perception,thread_collapse}.py` | **Experimental. NOT wired into the engine.** Do not call them from the main chain. |
| `graphs/*.yaml` | Executable DAGs: `linear`, `parallel`, `diamond`. `adaptive.yaml` is experimental (no `nodes`) and the engine rejects it by design. |
| `states/*.yaml` | The 5 canonical state definitions: `discover`, `analyze`, `verify`, `synthesize`, `archive` |
| `roles/*.md` | Role capability packs (system prompts) with mandatory JSON output schemas |
| `validators/` | `epistemic.rules.yaml` (global rules), `confidence.schema.yaml` |
| `tests/test_all.py` | Single-file suite, 36 tests, run from repo root |
| `traces/`, `checkpoints/` | Generated run artifacts (gitignored) |

## 2. What a Run Actually Does

1. Load `graphs/*.yaml`; graphs without `nodes` are rejected (fail-closed).
2. `DependencyGraph.validate()` — cyclic or unreachable graphs are rejected.
3. Nodes execute layer by layer via `ThreadPoolExecutor`; each node goes through `LLMHarness.execute()` with the state's `role_bindings` (mock by default). Per-node `retry` and `timeout_seconds` are honored: transient errors (timeout/connection/OS) retry with backoff, permanent errors (`NotImplementedError`/`ValueError`/`KeyError`/`TypeError`) fail fast.
4. `Gatekeeper.check_quality_gates()` validates each node's outputs against the state's `quality_gates`; failure aborts the pipeline. If a parallel-group node fails, completed sibling results are preserved in `result['results']`.
5. At `synthesize` nodes, upstream claims/conflicts are bridged into `ConfidenceNetwork`, which iterates to convergence; `delta` feeds the `confidence_converged` quality gate. With `calibration_temperature` set, the report also carries `calibration` metadata and the `uncalibrated` originals.
6. Every run writes `traces/<run_id>.jsonl` (start/end per node, hash-chained) and `checkpoints/<run_id>/checkpoint.json` after each layer. `run(resume_from=run_id)` reuses successful nodes and re-runs only failed/pending ones; resuming across a different graph id is rejected.

Every run returns `{"status", "results", "run_id", ...}`. On an exception-level fail-fast, `engine.last_run_id` still lets you resume the layers already checkpointed.

## 3. Common Tasks

### A. Add a Node to a Graph

Edit `graphs/*.yaml`. Node fields:

```yaml
- id: my_node                # unique within the graph
  stage: analyze             # MUST match a states/<stage>.yaml file
  dependencies: [discover]   # upstream node ids
  retry:                     # optional; omit = no retry
    max_attempts: 3          # total attempts incl. first
    base_delay: 0.1          # seconds before first retry
    factor: 2.0              # backoff multiplier
    max_delay: 30.0          # wait cap
  timeout_seconds: 10        # optional; omit = no limit
```

Then: `python3 core/engine.py validate graphs/<file>.yaml` before running.

### B. Add a New State

1. Create `states/your_state.yaml` with `id`, `activities`, `role_bindings`, `quality_gates` (follow `states/verify.yaml`).
2. Register it in `MANIFEST.yaml` under `states`.
3. **Extend `core/gatekeeper.py`**: gate enforcement branches on the `state_id` prefix (`discover`/`analyze`/...). A state with a new prefix gets **no** gate enforcement unless you add a matching branch — gates would silently pass. Do not treat a `quality_gates` entry alone as enforcement.
4. If it needs a new role, create `roles/your_role.md` with a strict `### Output Structure` JSON schema.
5. Add contract keys for the new stage to `MockProvider.STAGE_CONTRACTS` and its mock output in `core/llm_harness.py`, or mock-mode tests cannot cover it.
6. Run `python3 tests/test_all.py`.

### C. Wire a Real LLM

1. Implement the `LLMProvider` protocol from `core/llm_harness.py`: `complete(system, user, schema) -> dict`.
2. Inject it: `StateMachineEngine(graph, harness=LLMHarness(provider=YourProvider()))`. No engine changes needed. An injected provider always takes precedence over mock routing.
3. Your provider must return the keys declared in `MockProvider.STAGE_CONTRACTS` per stage, JSON-serializable — the Gatekeeper, checkpoints, and traces depend on this. Reuse the `test_mock_provider_contract` pattern for your provider.
4. Keep the JSON schemas in `roles/*.md`; downstream states and gates consume structured output only.
5. See `CUSTOMIZATION_GUIDE.md` for details.

### D. Add a New Graph Topology

1. Create `graphs/your_graph.yaml` following `graphs/linear.yaml` (top-level `id`, `nodes` list).
2. `python3 core/engine.py validate graphs/your_graph.yaml`, then `run`.

### E. Resume a Failed Run

```bash
python3 core/engine.py run graphs/linear.yaml --resume-from <run_id>
```

Fix the failure cause first (e.g. inject a working provider). Successful nodes are not re-run; only the failed node and its downstream re-execute. Checkpoints from a different graph are rejected.

## 4. Hard Boundaries — Do Not Cross

- **Fail-closed everywhere.** Invalid graphs, missing gate inputs, non-converged confidence, unimplemented LLM paths must fail loudly. Never add fallbacks that convert a failure into silent passage.
- **Never bypass DAG validation.** Cycle and unreachable-node checks stay on. Do not suppress them.
- **Never fake LLM capability.** `mock_llm=False` without an injected provider raises `NotImplementedError` by design. Do not catch-and-mock it.
- **Confidence values are heuristics, not calibrated probabilities** (mock stage). The calibration hook is a monotone order-preserving transform only; do not claim real calibration.
- **Honesty about mocks.** `MockProvider` outputs are fixed stubs. Document them as such; never present stub output as model reasoning.
- **Dependency policy: `pyyaml` + `numpy` only.** New modules must be pure stdlib otherwise. Do not add packages.
- **Thread safety.** Nodes in one parallel group run concurrently. Shared mutable state must be locked (see `RunTracer`).
- **Timeouts do not kill threads.** `timeout_seconds` makes the caller fail fast; the background thread runs to completion. Do not rely on it for resource reclamation.
- **Experimental modules stay out of the engine.** Mark new unwired modules `[EXPERIMENTAL]`.
- **Test discipline.** `python3 tests/test_all.py` from the repo root, 36/36, before finalizing any change. Behavior changes require new or updated tests in that file.
