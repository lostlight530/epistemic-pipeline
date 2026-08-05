# Epistemic Pipeline Scientific Closure Design

Date: 2026-08-05
Status: approved design baseline
Base: `main@516f496fe29907034e83326b11ec84fa87231c4f`

## Objective

Make the state-machine and confidence pipeline deterministic, fail-closed, inspectable, and reproducible while preserving current module paths and graph, role, state, and validator assets. The root README is outside scope.

## Verified starting point

The repository contains the core pipeline, V2 state machine, confidence DAG, neuro-symbolic bridge, YAML graphs, roles, states, validators, and tests. It has no GitHub workflow or cloud test evidence. A tracked root `.memory_log` contains one-time agent notes rather than scientific runtime evidence. V2 conditional routing evaluates serialized expressions dynamically, retry accounting can repeat without consuming its budget, and checkpoint storage lacks a versioned integrity boundary.

## Architecture decision

Callable predicates remain the preferred in-process routing interface. Serialized conditions use a deliberately small, parsed expression language with an allowlist of names, literals, Boolean operators, and comparisons; arbitrary Python execution is impossible. Execution state, checkpoints, and events have versioned schemas and explicit provenance. Confidence values are finite numbers in `[0, 1]`; invalid, cyclic, or incomplete evidence graphs fail before propagation.

The data flow is:

`validated graph + initial evidence -> deterministic routing -> state executor -> confidence update -> checkpoint/event stream -> terminal result`

State transitions and evidence transformations are recorded as structured events. Human approval pauses produce resumable checkpoints and never masquerade as completion.

## Planned change set

- Remove the tracked `.memory_log`; define an ignored `runtime/` boundary for checkpoints, logs, and local state.
- Replace dynamic expression execution with a safe condition parser and explicit typed failures.
- Consume retry budgets correctly and distinguish retryable failures from terminal failures.
- Version checkpoints, validate identifiers and payloads, use atomic writes, and reject corrupt or path-escaping checkpoint references.
- Enforce graph, confidence, convergence, and evidence-chain invariants before execution.
- Add deterministic clock and identifier injection points for reproducible tests without changing default callers.
- Add repository-contract tests for every graph, role, state, validator, and manifest declaration.
- Add negative and property-oriented tests for cycles, NaN/infinite confidence, contradictory evidence, invalid conditions, corrupt checkpoints, retry exhaustion, and resume equivalence.
- Add a compatibility document for the existing customization-guide filename without modifying the root README.
- Add reproducibility, evidence, AI-use, security, contribution, and repo-specific GitHub governance files.
- Add least-privilege GitHub verification, CodeQL, and dependency-maintenance workflows pinned to immutable action commits.

## Security and failure model

No `eval`, `exec`, shell execution, implicit network access, or unbounded retry is permitted. User-provided paths are resolved within an explicit runtime root. LLM adapters remain opt-in and must return source/model metadata; the symbolic path remains usable without a model or credential. Logs must exclude secrets and unneeded prompt content.

## Verification and acceptance

Cloud checks run on Python 3.12 and 3.14. All existing tests plus new routing, checkpoint, confidence, failure, and repository-contract tests must pass. `compileall` and YAML/schema validation must pass. The same graph, inputs, clock, and identifier source must yield the same terminal state, trace order, confidence values, and checkpoint digest. Pause/resume must be observationally equivalent to uninterrupted execution.

## Non-goals

No root README edit, frontend, autonomous agent framework, built-in model provider, hidden memory service, Jules workflow, or breaking rename of current graph and module paths.

## Rollout and rollback

Implementation is isolated on `codex/scientific-closure-20260805` and delivered through one repository-specific pull request. Merge occurs only after cloud checks pass. Rollback is a single merge-commit revert; the removed one-time log remains recoverable from Git history, and checkpoint readers retain the documented prior-format compatibility path.
