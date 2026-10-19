# Epistemic runtime Tool / CLI / Agent console

> Current implementation surface · 2026-10-19 · `epistemic-pipeline/tool-adapter`

## Where this sits

```text
caller / human / independent agent
    ├─ import agent_tools.tool_definitions() → JSON Schema declarations
    ├─ import agent_tools.execute_tool_call(name, arguments)
    └─ tool_cli.py (JSON / styled terminal / offline HTML)
                    ↓
          explicit allowlist dispatch
                    ↓
             existing core modules
                    ↓
        typed result + explicit error/domain finding
```

This is an **opt-in, local, synchronous** tool adapter. The caller orchestrates model decisions, approvals and persistence. No background agent, scheduler, online gateway, MCP server, remote model SDK, external provider authentication, unrestricted shell or automatic repository edits are introduced.

## Registered tools

`graph_inspect` loads a declared local YAML graph and reports structural validity, deterministic ordering, parallel groups, and critical path without executing LLMs. `claim_transfer` delegates to `core.claim_transfer.build_claim_transfer` and preserves existing claim evidence/ambiguity constraints without acceptance or verification.

Tool names, required arguments and JSON Schema are inspected with `list` and `describe`. The registry rejects unknown tool names, unexpected argument keys, wrong value types and malformed JSON before calling implementation. Runtime paths are caller-supplied and are *not* sandboxed; execute only with appropriate filesystem permissions and inspect untrusted inputs independently.

## CLI: immediate practical use

From this repository root with its existing Python dependencies installed:

```bash
python3 tool_cli.py list --format text
python3 tool_cli.py describe graph_inspect
python3 tool_cli.py invoke graph_inspect --args '{"graph":"graphs/diamond.yaml"}' --format text
python3 tool_cli.py invoke claim_transfer --args '{"claim_audit":"evidence/example.claim-audit.json","claim_ids":["claim-1"],"purpose":"downstream figure selection"}'
```

**JSON-first automation** (single JSON object on stdout, no ANSI escape sequences):

```bash
python3 tool_cli.py list
python3 tool_cli.py invoke graph_inspect --args-file request.json > result.json
cat request.json | python3 tool_cli.py invoke graph_inspect --args-file - > result.json
```

To generate a **standalone offline UI report**:

```bash
python3 tool_cli.py invoke graph_inspect --args '{"graph":"graphs/diamond.yaml"}' --format html --output output/tool-inspection.html
```

Open the resulting HTML file locally. It is a static report; it does not fetch content, execute JavaScript, host a server or provide live agent control.

## Programmatic Agent binding (no vendor SDK needed)

```python
import json
from agent_tools import tool_definitions, execute_tool_call

definitions = tool_definitions()  # agent/model-side function declarations
assert len(definitions) == 2

# The caller chooses an allowlisted function and supplies validated arguments.
name = "graph_inspect"
arguments = { "graph": "graphs/diamond.yaml" }
result = execute_tool_call(name, arguments)
assert result["tool"] == name
print(json.dumps(result, ensure_ascii=False))
```

Stringified JSON arguments are also supported for provider-neutral function-call transport, but there is no built-in provider loop, approval policy, retry orchestration or MCP protocol conformance.

## Stable result contract

```json
{
  "profile": "epistemic-pipeline/tool-adapter",
  "tool": "an-allowlisted-tool",
  "status": "ok",
  "result": {},
  "error": null,
  "scientific_validity_claim": false,
  "remote_provider_called": false
}
```

The execution status reports whether **tool invocation succeeded**, not whether domain findings passed. For CLI automation, exit 0 means invocation and domain checks passed; exit 1 means an invocation or domain check failed; exit 2 means writing the requested output report failed. Error responses include `error.code` such as `UNKNOWN_TOOL`, `INVALID_ARGUMENT` or `EXECUTION_FAILED`. Failures are valid evidence and must not be rewritten into successes.

`graph_inspect` does not run state transitions, providers, traces, checkpoints or scientific verification. `valid:false` is a domain-failure signal and CLI exit status 1. Omitting `claim_ids` means all indexed source claims are selected; never imply selection is acceptance.

## UI style and accessibility scope

The console shares a single visual language across all three repositories:

| Surface | Design | Reliability boundary |
|---|---|---|
| `--format json` | stable key structure, machine-readable, no decorative output | truth comes only from `status` and domain findings |
| `--format text` | compact cyan console frame, explicit EXECUTED / CHECK FAILED headings | ANSI only for interactive TTY, removable with `--no-color` or `NO_COLOR` |
| `--format html` | navy/teal editorial style, responsive cards, system typography, auto light/dark mode, readable monospace blocks | local static HTML with escaped user data and **no scripts** |

Color is never the only status indicator. A result can be `EXECUTED` while its research/diagnostic meaning stays bounded; a human should still review the original evidence and source.

## Test and operational verification

```bash
python3 -m unittest tests.test_tool_cli -v
python3 tool_cli.py list
python3 tool_cli.py list --format html --output output/tool-catalog.html
```

These are executable instructions, **not a claim that any runner, GitHub Actions, security review or independent reproduction passed**. The adapter is optional and deliberately does not alter the canonical scientific/runtime paths.

For the three-repository chain, produce upstream artifact/claim/figure sidecars with each repository's native runtime first; then use these explicit read/transfer tools for portable handoffs. There are no hidden direct cross-repository imports, shared secrets, or automatic promotion of source evidence into scientific truth.
