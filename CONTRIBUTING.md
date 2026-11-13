# Contributing — Epistemic Pipeline

## Open research contributions

For independent research-method or positioning changes, start with [`OPEN_RESEARCH.md`](./OPEN_RESEARCH.md). For new bounded research records, use [`RESEARCH_TEMPLATE.md`](./RESEARCH_TEMPLATE.md). Implementation, MANIFEST, runtime policy, claim/evidence/transfer contracts, maintenance, and historical evidence remain authoritative for their own surfaces.

Contributions should strengthen explicit research-execution semantics, evidence traceability, portable constraints, tests, documentation, or public metadata without turning structural success into scientific truth.

## Start from the owning surface

- implementation under `core/`, `graphs/`, `states/`, and `roles/` owns runtime behavior;
- `validators/` owns explicit machine predicates;
- `MANIFEST.yaml` owns the machine-readable capability map;
- `docs/02-examples-and-contracts/` owns claim/evidence/transfer semantics;
- `docs/01-source-and-explanation/` and README explain current behavior;
- `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` routes current documents and historical evidence;
- root metadata, `.github/`, security, citation, CodeMeta, and release files are repository infrastructure.

## Contribution principles

1. Change the smallest layer that owns the requirement.
2. Keep graph, state, provider, runtime policy, score, trace, provenance, claim audit, claim transfer, and evidence-envelope concerns separate.
3. Fail explicitly for unsupported checks, wrong profiles, missing requested claims, and ambiguous recovery identity.
4. Preserve unknown provider/model/version metadata rather than guessing.
5. Preserve conflicts and the non-probability semantics of heuristic scores.
6. Update machine contracts and public documentation only when their semantics actually change.
7. Keep historical point-in-time records recoverable.

### 长期阶段数据与归档引用 / Longitudinal stages and archived citations

**中文**：提交涉及状态机、claim verification／transfer、checkpoint 和阶段性研究记录时，分别写清源 commit、输入与环境、执行命令、结果、未测范围、异常和可复现的 evidence envelope；每日／每周／每月的文档与 GitHub Release 不属于同一状态对象，软件 concept DOI 不能代替特定 release version DOI 或运行回执

**English**: For state-machine, claim verification/transfer, checkpoint or periodic research changes, preserve source commit, input, environment, actual command/result, untested scope, failure and portable evidence envelope. Daily/weekly/monthly research records and GitHub releases are different objects; a software concept DOI cannot substitute for the cited version DOI or a run receipt

## Evidence boundaries

```text
claim indexed != claim true
evidence linked != evidence sufficient
structured verification != scientific verification
heuristic score != probability
runtime-policy pass != truth
claim transfer != acceptance
provider report != vendor authentication
assertion basis != correctness
coverage != quality
repository DOI != claim evidence
```

Any new claim/evidence field should make clear both the value and how the repository obtained it. Caller-declared or provider-reported basis does not become correctness, peer review, or external authentication.

## Claim-transfer changes

When transfer behavior changes:

- require the expected source profile;
- fail explicitly for missing requested claim IDs;
- preserve source/evidence refs, observations, conflicts, score semantics, and audit state;
- never remove conflict context merely to make a handoff cleaner;
- never upgrade a heuristic score to probability;
- never imply acceptance, peer review, or evidence sufficiency through transfer;
- synchronize the owning contract, Manifest, examples, and downstream profile references when semantics actually change.

### 中英阶段数据验收要求 / Bilingual stage-data acceptance

科研或发布说明变更须指出具体 source→claim→trace→checkpoint→result 路径、原始 Git 修订、是否真正运行、失败或不确定状态与比较口径；研究判断、验证器通过、代码合并、GitHub Release 和 DOI 归档不具有相互继承关系；未执行的检查只能记录为 NOT_EXECUTED

Research or publication changes must identify an inspectable source→claim→trace→checkpoint→result chain, exact revision, actual execution, failures/unknowns and comparison denominator. Scientific interpretation, validator PASS, merge, GitHub Release and DOI archive do not imply one another. Unrun checks remain NOT_EXECUTED

## Verification

Run tests, validators, schema checks, or targeted commands relevant to the changed surface and supported by the environment. Record exact commands and observed results in the pull request.

An unrun validator, scanner, provider route, or external service is not a pass. Structural validation is engineering evidence for the tested predicates, not scientific validation.

## Documentation and historical evidence

Use `DOCUMENT_STATUS.md` to distinguish current contracts from dated/historical records. Correct current interpretation forward; do not rewrite historical snapshots merely to make them match later knowledge.

## Publication and citation metadata

`CITATION.cff`, `codemeta.json`, and `RELEASE_POLICY.md` describe the public software publication. A DOI identifies an archived software object; it does not verify a claim, establish evidence sufficiency, calibrate a heuristic score, or reproduce an execution.

## Pull requests

Use the repository pull-request template and include:

- the problem and bounded change;
- affected implementation, validators, Manifest/contracts, examples, docs, or metadata;
- evidence/rationale and semantic impact;
- verification actually performed;
- checks or environments not exercised;
- compatibility and historical impact;
- security/privacy impact;
- a practical rollback.

## Security, privacy, license, and attribution

Follow `SECURITY.md` for sensitive reports. Do not publish credentials, private data, or exploit details requiring coordinated disclosure.

Contributions to repository-owned work are licensed under the repository license. Third-party material retains its original attribution and licensing, and Git/PR history remains the source of contribution attribution.
