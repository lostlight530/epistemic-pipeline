# Agent Guide for Customization

Welcome, Agent/Bot! If you are assigned to extend, modify, or customize the `epistemic-pipeline` repository on behalf of a user, please read this guide.

## 1. Core Philosophy

- **State Machine Driven**: Research workflow is modeled as a state machine with 5 canonical states (discover, analyze, verify, synthesize, archive). Flow control is deterministic, not probabilistic.
- **DAG Parallelism**: Dependencies between nodes are expressed as a Directed Acyclic Graph. The engine computes parallel groups via topological sort and executes them concurrently via ThreadPool.
- **Schema as Contract**: Inputs and outputs are validated against YAML schemas. Missing inputs are intercepted by the Gatekeeper with `MISSING_GATE_INPUT`.

## 2. System Architecture

The pipeline is orchestrated by `core/engine.py` (StateMachineEngine).

1. Load a graph definition from `graphs/*.yaml`.
2. `DependencyGraph` validates the DAG (cycle detection, unreachable node detection) and computes parallel execution groups.
3. `StateMachineEngine` executes nodes layer by layer via `ThreadPoolExecutor`; each node runs through `LLMHarness.execute()` with the state's `role_bindings` (mock by default). Node-level `retry{max_attempts, base_delay, factor}` and `timeout_seconds` are honored: transient errors retry with exponential backoff + jitter, permanent errors fail fast (`core/resilience.py`).
4. `Gatekeeper.check_quality_gates()` validates outputs against state-specific rules after each node; failures abort the pipeline. If a node in a parallel group fails, completed sibling results are preserved in the failure payload (`result['results']`).
5. At `synthesize` nodes, `KnowledgeExtractor` bridges upstream claims/conflicts into `ConfidenceNetwork`, which propagates belief scores via supports/contradicts/derives/related edges until convergence; the resulting `delta` feeds the `confidence_converged` quality gate. An optional `calibration_temperature` applies temperature scaling to the converged values, with disclosure of `calibration` metadata and `uncalibrated` originals (`core/calibration.py`).
6. Every run emits a structured trace to `traces/<run_id>.jsonl` (OTel GenAI-aligned field names, SHA-256 hash chain, `core/run_tracer.py`) and per-layer checkpoints to `checkpoints/<run_id>/checkpoint.json`; `run(resume_from=run_id)` reuses successful nodes and re-runs only failures and downstream.

**Key Boundaries:**
- `core/llm_harness.py` runs in `mock=True` mode by default via `MockProvider`. Real LLM calls raise `NotImplementedError` unless a custom `LLMProvider` is injected (`complete(system, user, schema) -> dict`); `MockProvider.STAGE_CONTRACTS` defines the 5-stage output contract that any real provider must satisfy (contract tests in `tests/test_all.py`).
- Mock-stage confidence values are heuristics, not calibrated probabilities; `core/calibration.py` only provides a monotonic order-preserving transform hook.
- Thread-based timeouts cannot kill the underlying thread: the caller fails fast on `timeout_seconds`, the background thread finishes naturally.
- `core/knowledge_extractor.py` is a 33-line static bridge, not a live extraction engine.
- Experimental modules (`anti_entropy`, `convergence`, `infinite_regression`, `neuro_symbolic`, `perception`, `thread_collapse`) are not wired into the main engine.

## 3. How to Customize / Extend

### A. Add a New State

1. Create `states/your_state.yaml` defining inputs, outputs, and transitions.
2. Register the state in `MANIFEST.yaml` under `states`.
3. Add Gatekeeper rules in `validators/epistemic.rules.yaml` with the state ID prefix.
4. If the state requires a new role, create `roles/your_role.md` with JSON Schema for structured output.

### B. Wire a Real LLM

1. Implement the `LLMProvider` protocol from `core/llm_harness.py`: `complete(system, user, schema) -> dict` wrapping your real API (e.g., Kimi, 百炼).
2. Inject it: `StateMachineEngine(graph, harness=LLMHarness(provider=YourProvider()))` — no engine changes needed.
3. Reuse the provider contract tests (`test_mock_provider_contract` pattern): your provider must return the keys declared in `MockProvider.STAGE_CONTRACTS` so the Gatekeeper and downstream states keep working.
4. Preserve the JSON Schema contract from `roles/*.md` so downstream states receive structured input.
5. See `CUSTOMIZATION_GUIDE.md` for detailed integration steps.

### C. Add a New Graph Topology

1. Create `graphs/your_graph.yaml` following the structure in `graphs/linear.yaml`.
2. Define nodes with `id`, `stage`, and `dependencies` fields (`stage` must match a file in `states/*.yaml`; `dependencies` lists upstream node ids). Optional per-node resilience fields: `retry: {max_attempts, base_delay, factor}` and `timeout_seconds`.
3. Test with: `python3 core/engine.py run graphs/your_graph.yaml`

## 4. Constraints & Conventions

- **Never bypass DAG validation**: The engine rejects cyclic and unreachable graphs by design. Do not suppress these checks.
- **Always validate outputs**: Any new state must have corresponding Gatekeeper rules. Missing rules should cause failure, not silent passage.
- **Mock mode is the default**: Do not assume real LLM availability. All new features must be testable with `mock=True`.
- **Thread safety**: Nodes in the same parallel group execute concurrently. Shared state must be thread-safe.
- Always run the test suite: `python3 tests/test_all.py` before finalizing any change.
