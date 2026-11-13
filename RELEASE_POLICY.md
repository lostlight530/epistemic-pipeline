# Release and Archival Policy

This repository treats `main` as the current repository state and release tags as immutable point-in-time snapshots.

## Policy

- Create a release or tag only from a reviewed and merged `main` revision.
- A release records a historical snapshot; it does not override later repository state, governance, contracts, or evidence.
- Release identifiers may be repository-specific. Do not invent a semantic version where the repository has not established one.
- Add `version`, `date-released`, DOI, SWHID, or other archival identifiers to citation metadata only after those identifiers actually exist.
- Do not rewrite historical tags or releases to reflect later corrections; publish a new release or correction record instead.
- Archive externally only after the release snapshot and its metadata have been validated.

For current repository truth, follow the repository's native implementation, evidence, governance, and recovery surfaces rather than citation or archival metadata.

## Initial archived software publication — 2026-09-16

The repository has a public Zenodo software publication dated **2026-09-16**.

- DOI: `10.5281/zenodo.22791463`
- DOI resolver: `https://doi.org/10.5281/zenodo.22791463`
- Code repository: `https://github.com/lostlight530/epistemic-pipeline`

This DOI is an archival publication identifier, not a moving identifier for every later `main` revision. Later repository changes must not be represented as part of the archived publication unless a new archival release explicitly includes them.

A future archived release should preserve this record as point-in-time publication history and use its own confirmed release metadata. DOI presence, citation metadata, or archival availability does not by itself establish claim truth, evidence sufficiency, runtime execution, scientific validity, or reproduction.

## Verified archived version lineage (2026-10-10)

The September 16 publication described above is the **initial archival snapshot**; it is not the only release now registered under this software concept. The citation/CodeMeta DOI `10.5281/zenodo.22791463` is the **concept DOI**, not the DOI for the latest specific release.

| Archived release | Published/release date | Immutable version DOI |
| --- | --- | --- |
| `v2026.09-open-research-baseline` | 2026-09-16 | [`10.5281/zenodo.22791464`](https://doi.org/10.5281/zenodo.22791464) |
| `v2026.09-natural-month-close` | 2026-09-30 | [`10.5281/zenodo.23068494`](https://doi.org/10.5281/zenodo.23068494) |
| `v2026.10-open-research-production-framework` | 2026-10-04 | [`10.5281/zenodo.23137216`](https://doi.org/10.5281/zenodo.23137216) |

The October GitHub release [`v2026.10-open-research-production-framework`](https://github.com/lostlight530/epistemic-pipeline/releases/tag/v2026.10-open-research-production-framework) reports `published_at=2026-10-04T13:00:36Z`. These identifiers are confirmed public release/DOI records, **not a claim that present `main` was frozen in that snapshot**. The existing `CITATION.cff` September 16 date remains a recorded archival baseline; do not silently rewrite it into a present-day retrieval or publication date. This documentation note creates **no new software release, DOI, prospective observation, or evidence of external research adoption**. The [independent identity audit](https://github.com/lostlight530/research-software-identity-audit) observes ten fixed software objects and remains an external control repository, not an eleventh research sample.

## Archived checkpoint — 2026-10-14

The fourth archived version is [v2026.10-fourteen-day-evidence-checkpoint](https://github.com/lostlight530/epistemic-pipeline/releases/tag/v2026.10-fourteen-day-evidence-checkpoint).

- Version DOI: [10.5281/zenodo.23365517](https://doi.org/10.5281/zenodo.23365517)
- GitHub `published_at`: `2026-10-14T11:15:04Z`
- Tagged source commit: [`326095b7c962eed292e4f53af863297fd92360db`](https://github.com/lostlight530/epistemic-pipeline/tree/326095b7c962eed292e4f53af863297fd92360db)
- Software-family concept DOI: [10.5281/zenodo.22791463](https://doi.org/10.5281/zenodo.22791463)

Use the version DOI for this exact checkpoint and the concept DOI for the software family. `CITATION.cff` and CodeMeta retain the family identifier and recorded September 16 baseline date. Later changes to `main` belong to subsequent repository state; the checkpoint tag remains unchanged.

### 版本号、研究阶段与归档的不同责任 / Version, research-stage and archive ownership

**中文**：已发布的 tag、版本 DOI 和与该版本绑定的引用元数据属于特定历史发行对象，发布后不因 `main` 后续变化而追溯改号；此仓软件家族 concept DOI `10.5281/zenodo.22791463` 与任一版本 DOI 不可交换；需要精确重现时应固定所引用版本的 tag、源 commit、输入和运行收据；Daily／Weekly／Monthly 的科研阶段结果独立于软件归档，不因软件 Release 成功而自动完成

**English**: Published tags, version DOIs and citation metadata tied to those versions describe historical release objects; later `main` evolution must not silently renumber them. Software-family concept DOI `10.5281/zenodo.22791463` is not interchangeable with any version DOI. Reproduction requires the cited version's tag, source commit, inputs and actual run receipts. Daily/Weekly/Monthly research-stage conclusions are separate from software publication and cannot be settled by a successful release alone

### 版本固定、主线演进与引用口径 / Fixed versions, evolving main and citation

**中文**：`main` 随代码与研究证据演进，已发布的 Git tag 和对应 Zenodo version DOI 是固定的归档对象；软件家族 concept DOI `10.5281/zenodo.22791463` 不能代替具体归档版本的引用；若复现某个结论，需补充该版本的 Git SHA、依赖／执行环境、配置、输入、trace 和 checkpoint 以及比较结果；文档更新不表示已执行重放，也不应静默改写旧 release 元数据

**English**: `main` evolves; published Git tags and their Zenodo version DOIs remain fixed archives. Software-family concept DOI `10.5281/zenodo.22791463` cannot stand in for an exact release version. Reproduction requires the cited Git SHA, environment, configuration, inputs, trace/checkpoint and comparison outcome. Documentation updates neither replay old results nor rewrite historical release metadata

## Open-science reuse and research records

- Cite the software family through [CITATION.cff](CITATION.cff) or [CodeMeta](codemeta.json); cite the version DOI above when a result depends on this checkpoint.
- Use the linked tagged source commit for code inspection and retrieval, and record the revision, environment, procedure and observed result when performing a rerun.
- Follow [OPEN_RESEARCH.md](OPEN_RESEARCH.md) and the repository-native research contracts; use [RESEARCH_TEMPLATE.md](RESEARCH_TEMPLATE.md) for a new bounded research record where a more specific native template does not apply.
- Reuse repository-owned material under [LICENSE](LICENSE), preserve [authorship attribution](AUTHORS), and submit changes through [CONTRIBUTING.md](CONTRIBUTING.md).
- Keep later findings and corrections in new dated records so the archived checkpoint remains recoverable.


## Latest archived checkpoint — 2026-11-10

The latest archived repository snapshot is `v2026.11-ten-day-evidence-checkpoint`.

- GitHub Release: [v2026.11-ten-day-evidence-checkpoint](https://github.com/lostlight530/epistemic-pipeline/releases/tag/v2026.11-ten-day-evidence-checkpoint)
- GitHub release published: `2026-11-10T14:40:46Z`
- Tagged source commit: [`5df093c1c74902506bfcd9bd08ef7c12b40e39eb`](https://github.com/lostlight530/epistemic-pipeline/commit/5df093c1c74902506bfcd9bd08ef7c12b40e39eb)
- Zenodo exact-version record: [10.5281/zenodo.24112474](https://doi.org/10.5281/zenodo.24112474)
- Software-family concept DOI: [10.5281/zenodo.22791463](https://doi.org/10.5281/zenodo.22791463)

The Zenodo version record identifies the exact GitHub tag as its source reference. This is an immutable 2026-11-10 snapshot; subsequent changes on `main` are not part of this archive. The concept DOI remains the software-family identifier and is intentionally distinct from the version DOI.
