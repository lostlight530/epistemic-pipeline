# Epistemic Pipeline Scientific Closure Design — Historical Record

Date: 2026-08-05  
Status: **SUPERSEDED on 2026-08-24**  
Original base: `main@516f496fe29907034e83326b11ec84fa87231c4f`

> This document is preserved as design history. It is **not** the current implementation plan or repository-governance instruction. Current authority is `README.md`, `ARCHITECTURE.md`, `RESEARCH_CONTRACT.md`, `MANIFEST.yaml`, and `AGENTS.md`.

## Why it was superseded

The 2026-08-05 design mixed useful research-runtime concerns with a GitHub-platform governance direction that is no longer part of this repository's maintenance architecture. In particular, its planned GitHub verification, CodeQL, dependency-maintenance workflows, cloud-check acceptance and merge-check language must not be treated as open work items.

The current repository direction is **research-runtime-first**:

```text
graph identity
  -> state/provider contract
  -> runtime policy
  -> bounded heuristic scores
  -> trace + checkpoint
  -> PROV-aligned lineage
  -> Evidence Envelope
```

GitHub Actions, CI, CodeQL and merge-gate assumptions are outside normal research maintenance unless repository governance is explicitly redesigned in a separate task.

## Historical objective

The original objective was to make state-machine and confidence execution more deterministic, fail-closed, inspectable and reproducible while preserving module paths and graph/role/state/validator assets.

That objective remains useful in narrower form, but several historical assumptions have since changed.

## What survived into the current architecture

Useful ideas retained or refined:

- explicit DAG validation and fail-closed behavior;
- bounded retry and timeout semantics;
- atomic checkpoint writes;
- structured trace evidence;
- explicit confidence/score bounds;
- provider isolation;
- no `eval`, `exec`, shell-based runtime or implicit network provider behavior;
- clear distinction between integrated and Experimental modules.

## What changed materially

### Runtime policy

Historical “quality gate” architecture has been replaced by machine-readable `runtime_policies` evaluated through `RuntimePolicyEvaluator`. Prose is not parsed to invent execution behavior.

Historical `Gatekeeper` names remain compatibility aliases only.

### Confidence

The active model is a bounded weighted heuristic score network, not a Bayesian/probability model. Numerical convergence is an algorithmic stopping property only.

### Graph/checkpoint identity

Current `checkpoint@2` binds resume to both human graph ID and canonical graph SHA-256. Same-name changed graphs are not considered equivalent.

### Observability

`trace@2` keeps project-local run/node/stage identity distinct from provider conversation/session identity and only reuses selected OpenTelemetry GenAI Development naming where appropriate.

### Provenance and handoff

The current evidence architecture separates:

```text
epistemic-pipeline/prov@2
  W3C PROV-aligned lineage

epistemic-pipeline/evidence-envelope@1
  cross-tool artifact handoff
```

Neither layer claims scientific truth or independent reproduction.

### Experimental modules

Experimental filenames are treated as historical/metaphorical compatibility surfaces. Current docs describe the actual local algorithm instead of inferring advanced capabilities from names such as `neuro_symbolic`, `anti_entropy` or `infinite_regression`.

## Current acceptance philosophy

The repository no longer defines acceptance through cloud checks.

Engineering evidence should instead answer concrete questions such as:

```text
Is the graph structurally valid?
Does checkpoint identity match the graph definition?
Did the declared runtime predicate evaluate successfully?
What score semantics were used?
What artifacts and hashes identify this run?
What PROV relationships were recorded?
What can and cannot be reproduced from the retained evidence?
```

Optional local checks may help inspect those properties, but successful checks do not establish source truth, probability calibration, external service behavior, peer review or independent reproduction.

## Historical non-goals retained

The repository still does not claim:

- a built-in live LLM provider;
- an autonomous general-purpose agent framework;
- an integrated adaptive routing runtime;
- a hidden memory service;
- scientific truth from pipeline completion.

## Current references

See:

- `README.md`
- `ARCHITECTURE.md`
- `RESEARCH_CONTRACT.md`
- `MANIFEST.yaml`
- `AGENTS.md`
- `CUSTOMIZATION_GUIDE.md`
