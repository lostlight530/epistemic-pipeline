# Frontier Research Stage K / 2026-Q3 — research brief
- Repository: `lostlight530/epistemic-pipeline`; source window 2026-07-01–2026-09-30; `RETROSPECTIVE`.
- Protocol recorded 2026-10-19 **after targeted source discovery**, not preregistered during the historical months.
- Specification: `2026-09-19-first-batch`; design `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`; status `COMPLETE`.
## Rationale and research question
**Theme:** Programmatic toolset, protocol and replay safety. **Question:** How does programmatic toolset, protocol and replay safety change the evidence needed to assess claim/evidence, tool authority, action trajectory, interruptions, environment state, evaluator and replay limits without inferring local implementation?
## Eligibility and source method
On 2026-10-19, inspect the selected publishers' GitHub `GET /repos/{owner}/{repo}/releases?per_page=100&page=1` and exact `/releases/tags/{tag}` records. Select dated release/version objects inside the quarter relevant to the repository lens; one release is one object, even with many reported features. Exclude outside-window dates and undated speculation. Mark prereleases precisely, not as GA. The sample is neither exhaustive external research nor independent reproduction.
## Research Parts / unit of analysis
- K-O1 — What changes when a generated program mediates tool calls?; publisher [openai/openai-agents-python v0.19.0](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0) dated 2026-07-27
- K-O2 — What protocol identity can be claimed without implementation evidence?; publisher [modelcontextprotocol/modelcontextprotocol 2026-07-28](https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28) dated 2026-07-28
- K-O3 — How can an auditable trace be faithful without retaining prohibited output?; publisher [openai/openai-agents-python v0.22.0](https://github.com/openai/openai-agents-python/releases/tag/v0.22.0) dated 2026-08-19
- K-O4 — Which exact action payload did an approval authorize?; publisher [openai/openai-agents-python v0.22.3](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3) dated 2026-09-17
## Charting and review plan
Version/date, object/source identity, publisher-stated behavior, analytic interpretation, alternative reading, source-family independence and missing local verification. A producer review can close a source-bounded documentary Stage if its limitations are explicit; independent scholarly review is not claimed.
Hard boundary: `claim indexed != truth; approval != execution; tool schema != authorization; score != probability; transfer != acceptance`.
