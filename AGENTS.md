# Agent Guide — Epistemic Pipeline

This guide defines how coding/research agents should modify the repository without overstating its scientific authority.

## Canonical authority

Implementation in `core/`, `states/`, `graphs/`, `validators/` plus the active contracts (`RESEARCH_CONTRACT.md`, `CLAIM_AUDIT_CONTRACT.md`, `ASSERTION_BASIS_AND_AUDIT_COVERAGE.md`, `ARCHITECTURE.md`, `MANIFEST.yaml`) define current semantics.

If docs disagree with code, correct one explicitly; do not invent a capability to reconcile them.

## Stable internal identifiers

Project-owned profile names are unversioned. Do not add decorative `@1/@2`, `/v1`, fake fixture/model versions, or similar pseudo-version suffixes. Preserve real external standard/runtime versions when genuinely applicable.

## System identity

```text
graphs/*.yaml
  -> DependencyGraph
  -> StateMachineEngine
  -> LLMHarness / injected LLMProvider
  -> RuntimePolicyEvaluator
  -> bounded heuristic score network
  -> RunTracer + checkpoint
  -> PROV-aligned lineage
  -> claim-verification
       ├─ assertion / observation basis
       └─ dimensional audit coverage
  -> evidence-envelope
       └─ upstream-reference coverage
```

## No hallucinated provider identity

`LLMProvider.describe()` may contain only metadata actually known by the provider integration.

- unknown vendor/model/version -> `null` or omitted;
- never infer model identity from prompt style, class name, environment-variable name or marketing copy;
- MockProvider remains a synthetic fixture with `model: null`, `version: null`, `external_model_call: false`;
- provider descriptions must preserve assertion basis (`provider-adapter-reported`, `synthetic-fixture-runtime`, or `runtime-harness-state` as applicable);
- the canonical path records `automatic_ai_detection_used: false`; do not infer AI authorship/use from generated prose.

## Claim verification rules

`core/claim_audit.py` records audit dimensions, not scientific verdicts.

Allowed descriptive states:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

Do not add universal `verified=true`, accepted/rejected/proven verdicts without a separately designed and evidenced scientific-review authority.

## Assertion / observation basis rules

Current bases include:

```text
structured-analyze-output
structured-verify-output
structured-state-output
provider-adapter-reported
synthetic-fixture-runtime
runtime-harness-state
caller-declared
runtime-observed-local-filesystem
```

Never upgrade basis into correctness:

```text
structured-verify-output != scientific verification
provider-adapter-reported != vendor certification
caller-declared review != peer review
```

## Audit coverage rules

Coverage remains dimensional. Do not create a synthetic aggregate research-quality score.

```text
coverage != provenance soundness
coverage != scientific validity
coverage ratio != probability
coverage ratio != evidence sufficiency
```

`aggregate_score` remains `null` unless a future explicitly validated evaluation regime is designed and documented.

## Score rules

Never describe `[0,1]` as probability by default, convergence as certainty, score change as Bayesian update, or unfitted temperature scaling as calibrated probability.

## Provenance / trace rules

`core/provenance.py` is PROV-aligned project JSON, not PROV-O RDF conformance. `core/run_tracer.py` is project JSONL tracing, not an OpenTelemetry exporter or tamper-proof ledger.

## Runtime policy rule

Machine behavior comes from `check` + explicit parameters. Human-readable `rule` text is documentation only. Unknown checks fail explicitly.

## Evidence-stack separation

```text
trace -> chronology
checkpoint -> recovery state
provenance -> lineage
claim audit -> claim observations/basis/coverage
evidence envelope -> compact handoff + ref coverage
```

Do not merge them into one proof object.

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
  -> epistemic-pipeline/claim-verification
  -> epistemic-pipeline/evidence-envelope
  -> sci-render-kit/figure-claim-audit
  -> sci-render-kit/figure-evidence
```

References are not runtime imports or inherited truth claims.

## Experimental modules

`anti_entropy.py`, `convergence.py`, `infinite_regression.py`, `neuro_symbolic.py`, `perception.py`, and `thread_collapse.py` remain experimental unless deliberately integrated. Metaphorical names are not capability evidence.

## R3 discipline

Metadata, checkpoint, provenance, provider disclosure, audit coverage or a claim audit never counts as independent reproduction. R3 requires an actual separate rerun plus a declared comparison criterion.

## Governance boundary

Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge-gate architecture as ordinary repository architecture. Local checks/tests are optional maintenance aids, not scientific validation.

## Documentation synchronization

When a public contract changes, synchronize README, Architecture, Research Contract, Claim Audit Contract, Assertion Basis contract, Manifest, Customization, Examples and Frontier Alignment. Prefer honest `implemented / experimental / proposed / not integrated` states over aspirational wording.
