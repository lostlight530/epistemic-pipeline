# Research Template / 科研记录模板

Status: prospective research-record template
Scope: new research records only; durable open-research method is owned by `OPEN_RESEARCH.md`
Historical records are not rewritten by this template

## Repository positioning boundary / 仓库定位边界

Canonical repository positioning:
> Evidence-aware state-machine research workflow software for explicit state transitions, runtime policies, bounded heuristic propagation, provenance, claim audit, checkpointing, and portable evidence handoff

Primary research domains:
research workflows; state machines; evidence provenance; knowledge representation; agent systems

Explicit non-goals / disallowed interpretations:
truth oracle; calibrated probability system; autonomous scientist; generic ETL pipeline; scientific-verdict engine

This repository defines its own research identity through current repository contracts, implementation, methodology, and maintained metadata

```text
External Classification != Repository Identity
Inferred Topic != Canonical Research Domain
Keyword Match != Project Purpose
Indexing Ontology != Repository Architecture
Scholarly Graph Representation != Repository Self-Definition
```

External systems such as Zenodo, DataCite, OpenAlex, OpenAIRE, search engines, citation indexes, or automated classifiers are downstream representations
They may be recorded as observations but never silently redefine this repository

### External classification check

- Channel / platform:
- Observed classification:
- Observation time:
- Compared against canonical positioning:
- Check status: RUN / NOT_RUN
- Alignment (only when RUN): ALIGNED / PARTIALLY_ALIGNED / MISCLASSIFIED / CLASSIFIER_NOISE
- Required repository change: NONE unless the repository's own canonical positioning is actually wrong
- Downstream correction candidate:

A downstream misclassification is evidence about the classifier or metadata projection, not evidence that the repository should change research identity

## Research identity / 研究身份

- Research record ID:
- Record type: Daily / Weekly-derived / Monthly-derived / Special / Experiment / Other
- Logical date or period:
- Actual execution date:
- Execution window:
- Record provenance:
- Base revision:
- Observed branch/ref snapshot:
- Research object identity:
- Evidence/source identity:
- Runtime/environment identity:
- Current-state cutoff:
- Prior related record:

Use `UNKNOWN`, `NOT_APPLICABLE`, `NOT_EXECUTED`, or `NOT_OBSERVED` instead of inference from neighboring fields

## Research question / 研究问题

State one question that can be contradicted by evidence

## Falsifiable hypothesis or judgment under test / 可证伪假设

- Proposed explanation:
- Support condition:
- Falsifier:

## Evidence or source basis / 证据基础

For each material source or input record identity, authority, time, supported proposition, limitation, and independence where relevant

Repository publication, DOI presence, index inclusion, or classifier labels do not create scientific validity by themselves

## Identity boundary / 身份边界

List identities that must not collapse in this study, such as object, source, dataset, configuration, run, Git ref, store, target, evaluator, timestamp, or version

## Controls / 控制条件

- Held constant:
- Changed:
- Baseline:
- Known confounders:

## Trial or bounded evidence procedure / 实验或有界证据过程

Describe exactly what was executed or inspected

If no execution occurred, say so explicitly

## Raw observations / 原始观测

Record direct observations only

```text
raw observation != interpretation
source existence != source truth
checker present != checker executed
checker pass != scientific truth
```

## Counterexample / 反例检查

Attempt at least one condition that would break the preferred interpretation
If not executable, record why

## Interpretation / 解释

Separate verified facts, evidence-based inference, and unknowns

## Provisional conclusion / 暂时结论

Allowed states include
- OBSERVATION
- CANDIDATE
- FINDING where repository-specific thresholds are satisfied
- NO_CONCLUSION
- UNKNOWN
- PARTIAL
- DEGRADED
- REFUTED
- INVALIDATED

Do not manufacture a positive conclusion for cadence completeness

## Research increment / 研究增量

Record only what this study actually added
- new evidence
- new counterexample
- narrower boundary
- reusable case
- corrected interpretation
- invalidated claim
- new uncertainty
- NONE

Research activity itself does not imply implementation, validation, reproduction, adoption, or impact

## Retest condition / 复验条件

State what must change, what must remain fixed, and what stronger evidence would alter the conclusion

## Repository-specific research surfaces
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

## Permanent separation rules

```text
research record != capability claim
repository self-definition != external ontology assignment
current truth != historical truth
publication != validation
usage != adoption
citation != reproduction
metadata consistency != scientific correctness
```

This template complements repository-native METHOD, METHODOLOGY, SOP, evidence contracts, and executable checks
When a repository-specific contract is stricter, the stricter repository-specific rule wins
