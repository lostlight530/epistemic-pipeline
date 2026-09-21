# Source and Research-Object Register — Stage A / 2024-Q1

## 0. Register identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Stage:** `A / 2024-Q1`
- **Specification:** `2026-09-19-first-batch`
- **Register date:** `2026-09-21`
- **Coverage:** `SEARCH_BOUNDED`

## 1. Identity rules

```text
benchmark != result
paper != benchmark implementation
dataset revision != same evidence state
toolkit version != benchmark concept
retrieved source != supported claim
provider report != independent reproduction
later correction != rewrite of earlier execution
```

## 2. Research-object register

| ID | Object | Type | Q1 state/date | Identity basis | Notes |
|---|---|---|---|---|---|
| O1 | TrustLLM | benchmark + toolkit | paper 2024-01-10; toolkit sequence Jan-Mar | paper + project repository | taxonomy, datasets, executable tooling |
| O2 | Sleeper Agents | experimental research study | 2024-01-10 | paper + Anthropic research page | proof-of-concept conditional behavior |
| O3 | RAGTruth | annotated RAG hallucination corpus | Jan release; Feb data update | paper + project repository | annotation ontology changes in-quarter |
| O4 | Gemini 1.5 | model/evaluation report object | Feb announcement; Mar technical report | Google official + arXiv technical report | provider-source family |
| O5 | Chatbot Arena | human-preference evaluation platform/paper | paper 2024-03-07 | arXiv + platform/project | pairwise preference and statistical aggregation |
| O6 | WMDP | hazardous-knowledge proxy benchmark + unlearning study | 2024-03-05; dataset correction 2024-03-08 | paper + project repo + website | later 2024-04-23 correction outside Stage |

## 3. Evidence-source register

| ID | Source | Family | Date/state | Authority | Limits |
|---|---|---|---|---|---|
| S1 | https://arxiv.org/abs/2401.05561 | TrustLLM authors | 2024-01-10 | paper method/results | not independent reproduction |
| S2 | https://github.com/HowieHwong/TrustLLM | TrustLLM project | Q1 update history | executable/tool/data state | same family as S1 |
| S3 | https://arxiv.org/abs/2401.05566 | Sleeper Agents authors | 2024-01-10 | experimental method/results | proof-of-concept scope |
| S4 | https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training | Anthropic | 2024-01-14 | producer summary | same family as S3 |
| S5 | https://arxiv.org/abs/2401.00396 | RAGTruth authors | first posted around Q1 boundary | paper/corpus method | not all repo revisions described |
| S6 | https://github.com/ParticleMedia/RAGTruth | RAGTruth project | Jan/Feb update history | dataset revision state | mutable repository |
| S7 | https://blog.google/innovation-and-ai/products/google-gemini-next-generation-model-february-2024/ | Google | 2024-02-15 | provider announcement/evaluation | provider-source family |
| S8 | https://arxiv.org/abs/2403.05530 | Google/DeepMind authors | 2024-03-08 | technical report | provider-authored |
| S9 | https://arxiv.org/abs/2403.04132 | Chatbot Arena authors | 2024-03-07 | platform method/results | preference evidence, not universal quality |
| S10 | https://arxiv.org/abs/2403.03218 | WMDP authors | 2024-03-05 | benchmark/method paper | proxy measure |
| S11 | https://www.wmdp.ai/ | WMDP team | Q1 | project summary | same family as S10 |
| S12 | https://github.com/centerforaisafety/wmdp | WMDP project | Mar + later correction history | dataset revision state | later state must not be backdated |

## 4. Source-to-object map

| Object | Sources | Relation | Directness | Independence |
|---|---|---|---|---|
| O1 | S1,S2 | defines/implements/updates | direct | same-family |
| O2 | S3,S4 | reports/summarizes | direct | same-family |
| O3 | S5,S6 | defines/releases/updates | direct | same-family |
| O4 | S7,S8 | announces/evaluates | direct | same provider family |
| O5 | S9 | defines/evaluates | direct | single primary family in this Stage |
| O6 | S10-S12 | defines/releases/corrects | direct | same-family |

## 5. Revision registry

| Object | Revision/event | Date | Effect |
|---|---|---|---|
| O1 | toolkit/data/leaderboard release | 2024-01-12 | executable evidence surface available |
| O1 | v0.2.0 | 2024-01-20 | tooling state change |
| O1 | v0.2.1 | 2024-01-29 | evaluation pipeline/provider support change |
| O1 | v0.2.4 | 2024-03-20 | bug fixes + Gemini Pro API support |
| O3 | data update + `implicit_true` | 2024-02 | annotation/evidence ontology refinement |
| O6 | WMDP-Cyber randomization correction | 2024-03-08 | Q1 dataset state transition |
| O6 | later dataset/method corrections | 2024-04-23 | post-Stage forward correction; qualifies future comparison |

## 6. Source-family / independence notes

No object has independent reproduction established by this Stage. Cross-object synthesis draws on distinct research teams/projects, but similar conclusions do not prove identical mechanisms.

## 7. Identity/conflict notes

- RAGTruth arXiv first-post timestamp is at the 2023/2024 boundary; the project repository explicitly records January corpus release, which is the event used for Stage inclusion.
- Gemini February announcement and March technical report are distinct evidence events about a related model family, not duplicate sources treated as independent.
- WMDP's April correction is outside the Stage and only used as a later reconciliation signal.

## 8. Limitations

No exhaustive benchmark inventory, no rerun of models, no dataset diff computation, no independent annotation audit, and no universal model-quality ranking.
