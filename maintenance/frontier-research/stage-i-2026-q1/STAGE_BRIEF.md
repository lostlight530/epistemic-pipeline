# Frontier Research Stage I / 2026-Q1 — research brief
- Repository: `lostlight530/epistemic-pipeline`; source window 2026-01-01–2026-03-31; `RETROSPECTIVE`.
- Protocol recorded 2026-10-19 **after targeted source discovery**, not preregistered during the historical months.
- Specification: `2026-09-19-first-batch`; design `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`; status `COMPLETE`.
## Rationale and research question
**Theme:** Handoff history and approval state. **Question:** How does handoff history and approval state change the evidence needed to assess claim/evidence, tool authority, action trajectory, interruptions, environment state, evaluator and replay limits without inferring local implementation?
## Eligibility and source method
On 2026-10-19, inspect the selected publishers' GitHub `GET /repos/{owner}/{repo}/releases?per_page=100&page=1` and exact `/releases/tags/{tag}` records. Select dated release/version objects inside the quarter relevant to the repository lens; one release is one object, even with many reported features. Exclude outside-window dates and undated speculation. Mark prereleases precisely, not as GA. The sample is neither exhaustive external research nor independent reproduction.
## Research Parts / unit of analysis
- I-O1 — What history is available after a handoff?; publisher [openai/openai-agents-python v0.7.0](https://github.com/openai/openai-agents-python/releases/tag/v0.7.0) dated 2026-01-23
- I-O2 — What distinguishes intended tool calls from authorized and executed ones?; publisher [openai/openai-agents-python v0.8.0](https://github.com/openai/openai-agents-python/releases/tag/v0.8.0) dated 2026-02-05
- I-O3 — Why might denied-action reason text matter to epistemic reconstruction?; publisher [openai/openai-agents-python v0.12.1](https://github.com/openai/openai-agents-python/releases/tag/v0.12.1) dated 2026-03-13
## Charting and review plan
Version/date, object/source identity, publisher-stated behavior, analytic interpretation, alternative reading, source-family independence and missing local verification. A producer review can close a source-bounded documentary Stage if its limitations are explicit; independent scholarly review is not claimed.
Hard boundary: `claim indexed != truth; approval != execution; tool schema != authorization; score != probability; transfer != acceptance`.
