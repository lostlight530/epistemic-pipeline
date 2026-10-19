# K1 — 2026-07 bounded technical evidence study

## 0. Study identity
- Repository: `lostlight530/epistemic-pipeline`; stage: K/2026-Q3; Part: `K1`
- Study design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`
- Performed retrospectively: 2026-10-19; source cutoff: 2026-10-19
- Coverage: `SOURCE_BOUNDED`; status: `COMPLETE` as a release-source interpretation
- Instrument: GitHub repository releases and exact-tag fetch via connected GitHub access; no runtime executor.

## 1. Research question
How does this month's versioned external release evidence change the identity and interpretation of claim/evidence discrimination, uncertainty, policy authority, tool trajectories, execution state, evaluator versions and transfer boundaries, while keeping an authoritative upstream release **separate from** local implementation, empirical validation and scientific truth?

## 2. Object and source eligibility
Include only official releases with a verifiable tag URL and GitHub publication timestamp within 2026-07. Treat separate release tags as distinct version objects, even from one originating family; treat the release note and associated tag as one **same-origin** evidence family. Exclude undated claims, speculative announcements, 2025 historical objects and unverified downstream adoption. Ambiguous event/publication dates remain distinct rather than normalized.

## 3. Executed discovery and selection
On 2026-10-19 examined the upstream GitHub Releases listings for the selected projects and fetched exact tag details at `https://api.github.com/repos/{owner}/{repo}/releases/tags/{tag}` for the chosen records. Stopping rule: select relevant dated object(s) that clarify a repository-lens identity or verification distinction, not all releases. Scope is intentional and not a systematic literature search.

### Object O1 / Source S1: openai/openai-agents-python v0.19.0
- **Selected release date (GitHub published):** 2026-07-27
- **Primary upstream source:** https://github.com/openai/openai-agents-python/releases/tag/v0.19.0
- **Direct upstream observation:** Programmatic Tool Calling with caller restrictions and Runner/approval integration.
- **Analysis:** The model can coordinate eligible tools programmatically, enlarging the causal chain between policy, generated code, tool calls and results; allowed_callers scope is not a substitute for inspecting actions. This is a version-bounded distinction between *what the provider describes as shipped* and *what an independent execution would need to establish*. The exact object tag and publication time matter when comparing a prior release or reconstructing which capability could have existed in this window.
- **Counter-reading / uncertainty:** Vendor release is not an independent security review or local runtime trace. A release note may be technically accurate about code shipped and still be incomplete about integration conditions, environment dependence and downstream side effects.

### Object O2 / Source S2: modelcontextprotocol/modelcontextprotocol 2026-07-28
- **Selected release date (GitHub published):** 2026-07-28
- **Primary upstream source:** https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28
- **Direct upstream observation:** stable 2026-07-28 MCP specification revision.
- **Analysis:** Protocol revision identity is a separate clock from SDK release identity and any tool-server implementation; compatibility claims require all three versions. This is a version-bounded distinction between *what the provider describes as shipped* and *what an independent execution would need to establish*. The exact object tag and publication time matter when comparing a prior release or reconstructing which capability could have existed in this window.
- **Counter-reading / uncertainty:** The release notice alone does not establish adoption/conformance by a specific SDK or server. A release note may be technically accurate about code shipped and still be incomplete about integration conditions, environment dependence and downstream side effects.

## 4. Cross-object interpretation, alternative hypotheses and negative space
The 2 selected objects belong to 2 identifiable upstream project family/families. They illustrate separate kinds of versioned state; co-occurrence within a calendar month is **not causal evidence** or proof of a shared adoption trend.
No independently executed installation, benchmark, plot, tool-call replay, accessibility review or external reproducer was observed in this Part. No evidence was obtained that epistemic-pipeline actually enables any described feature. `NOT_VERIFIED_HERE` is not `DOES_NOT_EXIST`.

## 5. Research-to-repository relation
- Lens: claim/evidence discrimination, uncertainty, policy authority, tool trajectories, execution state, evaluator versions and transfer boundaries
- Hard limits: claim indexed != claim true; score != probability; runtime-policy pass != truth; verification != scientific adjudication; provenance != truth
- Provisional conclusion: `SUPPORTED_RELEASE_OBSERVATION + BOUNDED_INTERPRETATION`.
- Current implementation defect: `UNKNOWN`; current contract drift: `UNKNOWN`; runtime change justified here: `NO`.
- Companion [month record](MONTH_2026_07_RECONSTRUCTION.md), [source register](SOURCE_OBJECT_REGISTER.md), [quarter synthesis](STAGE_SYNTHESIS.md).

## 6. Contributions and review
OpenAI ChatGPT assistant assembled source selection and analysis through connected GitHub retrieval on 2026-10-19; responsible human reviewer/owner identity and independent validation were not observed. Same-producer methodological review is recorded at quarter level, not represented as independent peer review.
