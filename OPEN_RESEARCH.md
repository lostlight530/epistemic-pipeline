# Open Research / 开放科研

Status: durable open-research production guide
Scope: repository-level research positioning, independent research-production method, scholarly-metadata boundaries, and semantic-drift governance

## Authority

This guide complements implementation, `MANIFEST.yaml`, architecture, runtime-policy, claim/evidence/transfer contracts, maintenance contracts, release policy, and historical evidence. It does not replace them.

```text
current repository truth
→ implementation / MANIFEST / claim-evidence contracts
→ OPEN_RESEARCH.md
→ RESEARCH_TEMPLATE.md
→ prospective research records
→ scholarly metadata / downstream indexes
```

A stricter repository-native contract wins.

## Canonical positioning

**Canonical Type:** Evidence-aware research-workflow and claim-provenance software

**One-line positioning:** Evidence-aware state-machine research workflow software for explicit state transitions, runtime policies, bounded heuristic propagation, provenance, claim audit, checkpointing, and portable evidence handoff

**Primary domains:** research workflows; state machines; evidence provenance; knowledge representation; agent systems

**Non-goals:** truth oracle; calibrated probability system; autonomous scientist; generic ETL pipeline; scientific-verdict engine

```text
External Classification != Repository Identity
Inferred Topic != Canonical Research Domain
Keyword Match != Project Purpose
Scholarly Graph Representation != Repository Self-Definition
```

## Independent research-production layer

Maintenance evidence, state-machine completion, and claim-audit output do not automatically constitute an independent research result. New research units should explicitly preserve question, falsifiability, evidence/source identity, graph/run/revision identity, executed procedure, raw observation, counterexample, bounded conclusion, research increment, and retest condition.

## Repository-specific method

Record when relevant
- claim under test and claim identity
- evidence set and source identity
- graph/state-machine identity
- state transition and runtime policy
- provider or fixture assertion basis
- trace and checkpoint identity
- provenance record
- claim-audit observation
- conflict and identity ambiguity
- claim-transfer or evidence-envelope boundary

`claim indexed != claim true`
`evidence linked != evidence sufficient`
`heuristic score != probability`
`claim transfer != acceptance`

A claim can be indexed, structurally checked, transferred, or scored without becoming scientifically true. Conflicts and identity ambiguity remain first-class evidence.

## Evidence and execution discipline

```text
claim indexed != claim true
evidence linked != evidence sufficient
structured verification != scientific verification
heuristic score != calibrated probability
claim transfer != acceptance
run completion != scientific validity
```

Unknown/unexecuted states stay explicit. Provider metadata and assertion basis remain source-bounded.

## Open-science file responsibilities

- `README.md` — public orientation.
- `OPEN_RESEARCH.md` — durable open-research method and positioning.
- `RESEARCH_TEMPLATE.md` — prospective bounded research-record template.
- `AUTHORS`, `LICENSE`, `CITATION.cff`, `codemeta.json` — authorship, reuse, citation/software metadata.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` — contribution/community/security governance.
- `RELEASE_POLICY.md` — release/archive semantics.
- `.github/ISSUE_TEMPLATE/**` and pull-request template — reviewable intake.

These support open research; they do not establish scientific validity.

## Scholarly metadata discipline

Preserve Canonical Type, One-line Positioning, Primary Domains, Non-goals, accurate structured subjects where supported, and 5–7 defining keywords before future metadata publication. Avoid classifier-facing marketing copy and keyword stuffing.

## Shadow classification

Candidate title + abstract/description may be checked against downstream topic/keyword inference.

```text
ALIGNED
PARTIALLY_ALIGNED
MISCLASSIFIED
CLASSIFIER_NOISE
```

Execution state is separately `RUN` or `NOT_RUN`. Repair owning metadata only for genuine upstream ambiguity; otherwise record classifier noise.

## Semantic drift audit

Compare canonical positioning with `CITATION.cff`, CodeMeta, archive/DOI metadata, OpenAIRE, and OpenAlex.

- **CANONICAL_DRIFT**
- **TRANSPORT_DRIFT**
- **DERIVATION_DRIFT**
- **VERSION_SKEW**

`DERIVATION_DRIFT != REPOSITORY_DEFECT`.

## History and correction

```text
CURRENT_STATE != TASK_TIME_STATE
LATER_SUCCESS != EARLIER_SUCCESS
PUBLICATION_IDENTITY != CURRENT_MAIN
RESEARCH_PRODUCTION != MAINTENANCE != PERIODIC_AUDIT
```

Preserve historical stage/maintenance records and correction chronology. Later availability does not rewrite earlier missing inputs or execution state.

## Contribution and review

Use `OPEN_RESEARCH.md` for research-method/positioning changes and `RESEARCH_TEMPLATE.md` for new research records. State claim identity, evidence set, run/graph/checkpoint identity, procedure actually executed, conflicts, unresolved ambiguity, and historical impact.

## Permanent boundary

```text
research record != capability claim
publication != validation
usage != adoption
citation != reproduction
metadata consistency != scientific correctness
external indexing != repository self-definition
```
