# 02 — Examples and Contracts

This class answers: **how are claims, evidence, audit state, transfer, and customization represented without silently strengthening scientific meaning?**

## Machine and capability surfaces

- root `MANIFEST.yaml` — machine-readable capability map.
- `validators/` — implemented structural/rule validation surfaces.
- `examples/` — supported representation examples.

Machine readability and validator success do not turn a claim into truth or an evidence link into sufficient support.

## Active contracts

### [`RESEARCH_CONTRACT.md`](./RESEARCH_CONTRACT.md)

Repository-wide evidence/execution semantics: claim state, source/evidence boundaries, runtime-policy interpretation, reproduction levels, and cross-repository non-inheritance.

### [`CLAIM_AUDIT_CONTRACT.md`](./CLAIM_AUDIT_CONTRACT.md)

Defines how a claim is structurally audited against declared evidence, observations, conflicts, and review state.

An audit can report coverage or a structural finding without establishing truth, peer review, or evidence sufficiency.

### [`CLAIM_TRANSFER_CONTRACT.md`](./CLAIM_TRANSFER_CONTRACT.md)

Defines bounded transfer of claim/evidence state between repository profiles.

```text
claim transfer != claim acceptance
reference carried forward != truth inherited
conflict preserved != contradiction resolved
```

Transfer must preserve source/evidence references, conflicts, score semantics, audit state, and unknown/missing status rather than cleaning them away.

### [`ASSERTION_BASIS_AND_AUDIT_COVERAGE.md`](./ASSERTION_BASIS_AND_AUDIT_COVERAGE.md)

Separates a field's value from how it was asserted/observed and separates audit coverage from correctness, quality, probability, or provenance soundness.

```text
assertion basis != correctness
coverage != quality
coverage ratio != probability
```

### [`CUSTOMIZATION_GUIDE.md`](./CUSTOMIZATION_GUIDE.md)

Shows how to adapt supported profiles/rules while retaining the repository's semantic boundaries. Customization is not permission to relabel heuristic scores as probabilities or imported references as trusted evidence.

## Cross-repository role

In the three-repository research-infrastructure chain:

```text
auto-doc-engine artifact/provenance objects
        ↓
epistemic-pipeline claim/evidence interpretation and transfer
        ↓
sci-render-kit scientific communication
```

An upstream artifact identity is not automatically a verified claim. A downstream figure or communication object does not retroactively make the claim accepted or scientifically valid.

## Operator and contributor surfaces

- root `AGENTS.md` — repository-owned operational guidance.
- root `CONTRIBUTING.md` — public contribution guidance.
- `examples/` and `CUSTOMIZATION_GUIDE.md` — supported use/configuration examples.

These surfaces must remain consistent with the implementation and active contracts but do not outrank them.

## Scholarly metadata

- root `CITATION.cff`
- root `codemeta.json`
- root `RELEASE_POLICY.md`
- root `LICENSE`

The repository DOI identifies an archived software publication. It does not verify claims, establish evidence sufficiency, calibrate heuristic scores into probabilities, authenticate providers, or self-award R3 independent reproduction.

## Reading path

For a new claim/evidence integration:

1. identify the owning implementation/validator and `MANIFEST.yaml` capability;
2. read `RESEARCH_CONTRACT.md` for repository-wide semantics;
3. read the specialized audit/transfer/assertion contract;
4. use `CUSTOMIZATION_GUIDE.md` and examples only within those boundaries;
5. retain revision-matched execution evidence when reporting that validation or transfer actually ran.

Architecture and implementation explanation live under [`../01-source-and-explanation/`](../01-source-and-explanation/). Maintenance/audit material in class 03 is operational/historical context, not claim truth.
