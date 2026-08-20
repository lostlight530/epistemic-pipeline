# Contributing to epistemic-pipeline

## Getting Started

1. Clone the repository.
2. Create an isolated environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install pyyaml numpy
   ```
3. Run tests to verify baseline:
   ```bash
   make test
   ```

## Development Principles

- **State machine first**: All workflow logic flows through the 5 canonical states. Do not bypass the state machine with ad-hoc execution paths.
- **DAG validation is sacred**: Never suppress cycle detection or unreachable node detection.
- **Mock mode is the default**: All new features must be testable with `mock=True` in `LLMHarness`. Do not assume real LLM availability.
- **Schema as contract**: New states must have corresponding Gatekeeper rules. Gate enforcement in `core/gatekeeper.py` branches on the `state_id` prefix — a state with a new prefix needs a matching branch there, otherwise its gates silently pass.
- **Dependencies are fixed**: `pyyaml` + `numpy` only. Everything else must be standard library. Do not add packages.
- **Fail-closed**: Invalid graphs, missing gate inputs, and unimplemented LLM paths must fail loudly, never fall back to silent passage.
- **Thread safety**: Nodes in the same parallel group execute concurrently. Shared state must be thread-safe.

## Pull Request Checklist

- [ ] All tests pass (`make test`)
- [ ] New states have corresponding `states/*.yaml` and Gatekeeper rules
- [ ] New graphs pass DAG validation (no cycles, no unreachable nodes)
- [ ] New modules are marked as `[EXPERIMENTAL]` if not wired into the main engine
- [ ] Documentation updated if behavior changes

## License

By contributing, you agree that your contributions are licensed under the MIT License.
