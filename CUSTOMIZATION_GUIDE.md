# Customization Guide for Agents and Bots

Welcome, AI Agent or Bot developer!

If you have cloned the **Epistemic Pipeline**, you are looking at a highly advanced, State-Machine Driven Dynamic Epistemic Engine. This pipeline is fundamentally different from static, sequential Agent frameworks. It uses **concurrent DAG topology for execution**, **Dynamic Role Binding**, and a **Bayesian Confidence Network**.

As learned in our `.memory_log` and peer analyses (like LangGraph/MetaGPT), enforcing rigid JSON schemas in the prompt is paramount.

---

## 1. How to Connect a Real LLM and Enforce JSON Schemas
Currently, `core/llm_harness.py` uses simulated outputs (`mock=True`). To plug in a real LLM:

*   **File to edit:** `core/llm_harness.py`
*   **Crucial Step:** The framework's `Gatekeeper` will aggressively reject unstructured text. Because of this, **NEVER** delete the `### Output Structure` (JSON/YAML Schemas) from the agent documentation in `roles/*.md`.
*   **Action:** When calling an LLM (e.g. OpenAI), pass `response_format: { "type": "json_object" }` and map the output precisely to the schemas defined in the role files.

## 2. How to Modify the Pipeline Logic (State Machine & Concurrent DAG)
The execution order is NOT hardcoded. It uses `concurrent.futures.ThreadPoolExecutor` to run independent tasks in parallel.

*   **Files to edit:** `graphs/*.yaml` (e.g., `graphs/parallel.yaml`)
*   **Action:** Add, remove, or reorder nodes in the `nodes` array. The `DependencyGraph` will calculate parallel execution groups. Any group with multiple independent states will automatically execute concurrently!

## 3. How to Create or Modify Roles (The Brains)
The system uses "Roles" as capability constraint packs.

*   **Files to edit:** `roles/*.md`
*   **Structure Requirement:** Every role file MUST clearly define four things:
    1.  `Capability Domains`
    2.  `Core Constraints`
    3.  **`Output Structure`** (The JSON schema is mandatory here to prevent hallucinations).

## 4. How to Define Your Own Value System
*   **File to edit:** `validators/epistemic.rules.yaml`
*   Define the global rules for your specific domain here. The Gatekeeper intercepts bad outputs globally.

## 🛠️ Quick Checklist for Your First Custom Run
1. [ ] Define custom roles with **strict JSON Schemas** in `roles/*.md`.
2. [ ] Connect DAG dependencies to leverage thread concurrency in `graphs/my_custom_graph.yaml`.
3. [ ] Implement real LLM API calls returning JSON in `core/llm_harness.py`.
4. [ ] Run: `python3 core/engine.py run graphs/my_custom_graph.yaml`.
