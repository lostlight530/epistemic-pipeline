# Four-Day Consolidation — Epistemic Pipeline

**Window:** 2026-08-24 → 2026-08-27  
**Repository role:** evidence-aware research execution / claim-audit plane

## Consolidated result

Across the four-day refresh, the repository moved from a state-machine/research-agent skeleton toward a more explicit evidence-bearing runtime:

```text
graph
 -> provider contract
 -> runtime policy
 -> claim/evidence/conflict structures
 -> heuristic score propagation
 -> trace/checkpoint
 -> PROV-aligned lineage
 -> claim verification record
 -> Evidence Envelope
```

## Major engineering changes

- runtime policy is machine-readable and distinct from human prose;
- heuristic scores and numerical convergence have bounded non-probabilistic semantics;
- trace uses project-local correlation and an internal SHA-256 chain without claiming tamper-proof logging;
- checkpoint resume binds to graph identity;
- provenance uses W3C PROV concepts without claiming PROV-O RDF serialization;
- provider disclosure keeps unknown vendor/model/version fields unknown;
- claim index separates claim identity from payload prose;
- claim verification records evidence bindings, observations, conflicts, initial/final heuristic scores and review context without creating a truth verdict;
- Evidence Envelope references separate artifacts and optional upstream records rather than copying the whole run;
- upstream iterable refs are materialized once so programmatic generator callers retain correct final counts.

## Stable identifiers

Project-owned profiles now use stable semantic names rather than decorative `@1/@2` suffixes. Examples:

```text
epistemic-pipeline/engine
epistemic-pipeline/runtime-policy
epistemic-pipeline/trace
epistemic-pipeline/prov
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
```

Real external standard versions remain explicit where applicable.

## Scientific boundary consolidated

```text
run success != scientific validity
policy pass != truth
evidence binding != evidence sufficiency
claim verification record != scientific verdict
heuristic score != probability
convergence != certainty
provider identity != output validity
human review != peer review
provenance != truth
metadata != reproduction
```

## Global design calibration

The four-day architecture was rechecked against recent autonomous-science and scientific-agent work on provenance, transparent AI use, artifact-centered claim observability, evidence-constrained claim qualification, trajectory-to-evidence conversion and strict end-to-end evaluation.

Those works motivate architectural separation; they do not certify this repository.

## Cross-repository role

```text
auto-doc-engine/artifact-record
        ↓
epistemic-pipeline/claim-verification
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit claim-aware communication
```

The integration remains loose and reference-based.

## Maintenance decision

No GitHub Actions, CI, CodeQL, dependency bots or merge gates were added. No test suite is used as the completion gate for this consolidation; final maintenance validation is static contract/interface/diff inspection.
