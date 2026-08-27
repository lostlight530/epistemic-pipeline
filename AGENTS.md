# Agent Guide — Epistemic Pipeline

This guide defines how coding/research agents should modify the repository without overstating its scientific authority.

## Canonical authority

Current capability/semantic authority is:

1. implementation in `core/`, `states/`, `graphs/`, `validators/`;
2. `RESEARCH_CONTRACT.md`;
3. `CLAIM_AUDIT_CONTRACT.md`;
4. `ARCHITECTURE.md`;
5. `MANIFEST.yaml`;
6. `README.md` and examples.

If documentation disagrees with code, correct the documentation or the implementation explicitly; do not invent a capability to reconcile them.

## Stable internal identifiers

Project-owned profile names are unversioned. Do **not** add decorative `@1/@2`, `/v1`, `mock-fixture@1`, or similar pseudo-version suffixes.

Use stable identifiers such as:

```text
epistemic-pipeline/engine
epistemic-pipeline/runtime-policy
epistemic-pipeline/trace
epistemic-pipeline/checkpoint
epistemic-pipeline/prov
epistemic-pipeline/confidence-heuristic
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
```

External standard versions are different: preserve real versions when an external standard actually defines them.

## System identity

```text
graphs/*.yaml
  -> DependencyGraph
  -> StateMachineEngine
  -> LLMHarness / injected LLMProvider
  -> RuntimePolicyEvaluator
  -> bounded heuristic score network
  -> RunTracer + checkpoint

core/run_bundle.py
  -> PROV-aligned lineage
  -> claim verification sidecar
  -> evidence envelope
```

Executable graphs currently include linear, parallel and diamond forms. Experimental topologies remain experimental until integrated.

## No hallucinated provider identity

`LLMProvider.describe()` may contain only metadata actually known by the provider integration.

- unknown vendor/model/version -> `null` or omitted;
- do not infer a model from prompt style, class name, environment variable name or marketing copy;
- `MockProvider` remains a local synthetic fixture with `model: null`, `version: null` and `external_model_call: false`.

## Runtime vocabulary

Use active terms:

```text
runtime policy
bounded heuristic score
numerical convergence
project trace
checkpoint identity
PROV-aligned lineage
claim verification
process disclosure
Evidence Envelope
```

Historical compatibility names such as `Gatekeeper`, `quality_gates`, `check_quality_gates` and `use_gatekeeper` may remain in code where needed, but should not drive the conceptual architecture.

## Claim verification rule

`core/claim_audit.py` records audit dimensions, not scientific verdicts.

Allowed descriptive states:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

Do not add universal `verified=true`, `accepted`, `rejected`, `proven`, or equivalent scientific verdicts unless a future implementation has a separately specified and evidenced review authority.

## Score rule

Never describe:

- `[0,1]` as probability by default;
- convergence as certainty;
- score change as Bayesian update;
- unfitted temperature scaling as calibrated probability.

## Provenance and trace rule

`core/provenance.py` is PROV-aligned project JSON, not a PROV-O RDF serializer. `core/run_tracer.py` is project JSONL tracing, not an OpenTelemetry exporter.

Do not upgrade alignment language into standards-conformance claims.

## Runtime policy rule

Machine behavior comes from `check` + explicit parameters. Human-readable `rule` text is documentation only. Unknown checks fail explicitly.

## Evidence stack separation

Keep these distinct:

```text
trace -> chronology
checkpoint -> recovery state
provenance -> lineage
claim audit -> claim-level observations/conflicts/scores
evidence envelope -> compact cross-tool index
```

Do not merge all of them into one “proof” object.

## Cross-repository handoff

Preferred upstream:

```text
auto-doc-engine/artifact-record
```

Preferred downstream:

```text
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

These are references, not runtime imports or inherited truth claims.

## Experimental modules

Files such as `anti_entropy.py`, `convergence.py`, `infinite_regression.py`, `neuro_symbolic.py`, `perception.py`, and `thread_collapse.py` remain experimental unless deliberately integrated and documented.

Do not infer capability from metaphorical filenames.

## R3 discipline

Metadata, checkpoint, provenance, provider disclosure or a claim audit never counts as independent reproduction. R3 requires an actual separate rerun plus a declared comparison criterion.

## Governance boundary

Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge-gate language as part of ordinary repository architecture unless the user explicitly asks.

Local checks/tests are optional maintenance aids and must not be presented as scientific validation.

## Documentation synchronization

Whenever a core contract changes, synchronize:

```text
README.md
ARCHITECTURE.md
RESEARCH_CONTRACT.md
CLAIM_AUDIT_CONTRACT.md
MANIFEST.yaml
CUSTOMIZATION_GUIDE.md
examples/README.md
FRONTIER_ALIGNMENT.md
```

Prefer honest `implemented / experimental / proposed / not integrated` states over aspirational wording.
