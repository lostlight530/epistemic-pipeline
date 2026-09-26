# Frontier Research Annotations — Stage A-G 合并批注 (epistemic-pipeline)

**Reviewer:** 淇（Qi）· 2026-09-26 · Independence: 独立于交付链（SPEC §12 声明式） · 覆盖：Stage A-G 全部 + 纵向层 · Rewrite: NONE

## 0. 仓定位批注

epistemic 仓的 frontier-research 轴=**评估认识论**：评测证据包络（什么使一个评估结论可信）沿 2024Q1→2025Q3 演化。与 auto-doc（工件身份轴）的"evidence"语义分叉：前者证据=评测结论可信度条件，后者=工件可追溯条件——**两仓综合未互相声明此语义差**（纵向 correction 候选，同 auto-doc 批注 §3）。

## 1. 逐 Stage 批注

### Stage A / 2024-Q1（评估包络的奠基季）
- [厚度] 三仓 A 中最薄（61,862 vs auto-doc 98,949）——Parts 密度临界
- [事实核验] Q1 评估生态：LLM 评测的 contamination（基准污染）讨论在 Q1 升温；HELM 式多维评估框架沉淀期；幻觉量化（vectaraHallucination 等排行榜线）活跃——**"评估证据包络"命题的直接生态证据在 Q1 是污染焦虑**；Python 3.12 线/uv 发布为背景
- [决定] APPEND_RELATION：污染讨论锚（arXiv 线，UNKNOWN 具体 ID 待核）

### Stage B / 2024-Q2（修正方法学期）
- [事实核验] Q2 评估生态：benchmark contamination 修正方案集中出现（per-question 过滤/私有 heldout）；**Chatbot Arena 风格 human-preference 评估的方法学审视升温**；多模态评测（图像理解）进入主流排行榜
- [判定] B 的"基准刷新版本化"命题轴正确——污染→刷新是 Q2→Q3 的连续线
- [决定] NO_FOLLOW_UP + 语境锚 1

### Stage C / 2024-Q3（事实性与裁判分化）
- [事实核验] Q3：**LLM-as-judge 的位置偏差/自偏好研究集中期**；事实性评测（SimpleQA 类短事实事实性，2024 下半年）预热；agent 评测（WebArena 类）从 demo 走向可复现框架
- [决定] NO_FOLLOW_UP

### Stage D / 2024-Q4（协议与可靠性奠基）
- [事实核验] **Model Context Protocol 2024-11-25 发布**——工具调用协议单源首日，D 阶段对象域的锚事件（**本仓 D 文件必须收录——若缺失即漏事件，VERIFY_IN_PLACE**）；o1（2024-09-12）把"推理时计算"带进评测视野；agent 可靠性（重复执行方差）讨论升温
- [决定] APPEND_RELATION：MCP 锚 + o1 背景锚

### Stage E / 2025-Q1（终考与新范式）
- [事实核验] **HLE（Humanity's Last Exam）2025-01 发布（arXiv 2501.14249，约 2,500 题跨学科）**——评估天花板事件；**SWE-Lancer（OpenAI，2025-02-19，双源验证）**——真实自由职业工程任务定价评测；DeepSeek R1（01-20）把开放权重推理带入第一梯队——**评估对象从闭源 API 扩到开放权重**，评测基础设施（本地推理/成本）语义变化
- [判定] E 三事件全部为对象域内一等事件——**E 的 REGISTER（3 锚档）承载不了这个密度——correction 首要对象**
- [决定] APPEND_RELATION：三锚（arXiv 2501.14249/OpenAI 官方页/DeepSeek 官方页）

### Stage F / 2025-Q2（agent 评测三连）
- [事实核验] **PaperBench（2025-04 前后，8,316 rubric 项）**——AI 复现论文评测；**Terminal-Bench（2025-05，tbench.ai，Stanford/Laude）**——终端 agent 基准；**τ²-bench（Sierra，2025-06-11）**——用户模拟双控（tool-user 混合控制）评测；MCP 生态：OpenAI 2025-03 采纳后协议竞争线（Google A2A 2025-04）开启
- [判定] F 是本仓对象密度最高的季度（三 benchmark+协议竞争），文档厚度却全系列最薄——**密度剪刀差最尖锐样本**
- [决定] APPEND_RELATION：四锚

### Stage G / 2025-Q3（轨迹评估的成熟形态）
- [事实核验] G 三对象：大规模 agent red-teaming（轨迹级策略违规取代单次坏答案——安全评估的单位转换）；MCP 任务对照 ground-truth 执行计划（execution-plan match 取代 outcome match）；超视界部分可观测长轨迹（记忆/中间状态主导结果解释）——**G 的三对象是 2025Q3 评估方法论前沿的准确切片**
- [语境] GPT-5（08-07）与 Q3 评估线：能力代际推进使"轨迹质量"比"最终答案"更能区分模型——G 选题的生态时机准确
- [决定] NO_FOLLOW_UP + 语境锚

## 2. 治理件横切批注（七 Stage 合并）

- **BRIEF RQ 编号**：仅 A 显式——治理注记（同 auto-doc 系）
- **REVIEW 独立性**：七 Stage 全部未声明——GAP 汇总（本文件即外部 review 补位）
- **REGISTER 密度**：A→G 衰减同 auto-doc 系（E/F 最薄）——correction 优先级 E/F
- **厚度曲线**：A 最厚→F 最薄→G 回升，与 auto-doc 系同型——**同批同衰减=系统性生成特征而非单仓偶然**

## 3. 纵向层与跨仓三角

- 十二环节链在 epistemic 轴的对应物=**评估对象链：benchmark→contamination→refresh→factuality→judge→agent→trajectory→long-horizon**——纵向综合未显式给出 epistemic 侧的链（auto-doc 轴独占）——**correction 提案：纵向综合补 epistemic/sci-render 两轴的平行链**（三轴平行是三仓设计的本意，现只显式了一条）
- MCP 事件（2024-11-25）在三仓的归属：epistemic（对象域内一等）/auto-doc（背景）/sci-render（无涉）——三角核对完成

## 4. Search log
MCP 双源（2024-11-25/2025-03 OpenAI）/SWE-Lancer（2025-02-19）/PaperBench（8,316）/Terminal-Bench（tbench.ai）/τ²-bench（2025-06-11）/HLE（2501.14249）七组锚；污染讨论与 judge 研究的具体 arXiv ID 未验证——UNKNOWN。2026-09-26。
---
*Annotation ends. 历史文件零改动。*
