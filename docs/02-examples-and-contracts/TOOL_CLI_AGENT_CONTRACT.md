# Native Tool / CLI / Agent Contract — 2026-10-19

本仓 Tool CLI 是对已有 canonical core 模块的显式封装，不是第二套算法、独立运行时、MCP Server 或 LLM 自动 Agent

## Invocation contract

Tool discovery: python3 tool_cli.py list

Single call: python3 tool_cli.py call TOOL --input request.json --output output/tool-receipt.json

Plan runner: python3 tool_cli.py agent --input examples/tool_plan.json --output output/agent-plan.json

--input 默认为 stdin (-)，--output 为可选的显式原子文件写入。未指定 --output 时只向 stdout 打印 JSON；本接口不会主动远程请求、运行 shell 或调用 LLM

### Envelope

单工具输出 profile = REPOSITORY/tool-execution，包含 repository、tool、status、input_sha256、assertion_basis、output 或 error。input_sha256 是排序键、紧凑序列化后的参数 SHA-256，属于输入身份，不证明内容正确

Agent 输出 profile = REPOSITORY/agent-plan，包含 plan_sha256、status、completed_steps、requested_steps、steps 和 execution_mode。Plan 输入为带 steps 数组的 JSON 对象，元素包含唯一 id、tool、arguments，允许 1–32 步，失败时停止并保留已经执行的步骤，后续步骤保持未执行而非虚报完成

Tools 白名单定义在 tool_cli.py 中，未知工具、错误类型、缺失必需参数、重复 step ID 均为显式错误。exit 0 代表调用正常结束，不代表输出业务 status 或 scientific validity 通过。工具结果中的 valid、evaluation_status、audit_state 由原生模块单独解释

## Tool map

graph.inspect — required nodes list; delegates to core.dependency_graph.DependencyGraph and returns validity, cycles, deterministic topological order/groups/critical path when valid. A returned valid:false is a successful structural inspection, not a runtime failure

claim.transfer — required claim_audit_path, optional claim_ids/purpose; delegates to core.claim_transfer.build_claim_transfer, preserving ambiguity/conflicts without a scientific truth claim

## Human / Agent / UI boundary

Human 或外部 Agent -> JSON parameters / plan -> local allowlisted Tool CLI -> canonical core -> tool/agent receipt -> sci-render-kit offline Evidence Console

- 这不是 MCP transport。不能只因使用 inputSchema / JSON 或工具清单，就宣称支持某个 MCP revision。需要正式 MCP 时应另行使用经核验的 SDK
- 这是确定性声明式 Agent 计划执行，不会执行模型生成的任意代码，不具备自主推理、持久调度或用户权限认证
- 本地进程能访问传入的文件路径，不具备 OS 级沙箱和网络隔离保证，不能直接执行不可信计划
- GUI 位于 sci-render-kit/ui/tri_repo_console.html，本地浏览器手动选择 JSON，不向服务器上传，也不验证 GitHub / CI 实时状态
- 科学有效性、独立复现和 publisher acceptance 不会从工具成功或绿色 UI 徽标中推导出来
- 测试入口：python3 -m unittest tests.test_tool_cli -v；仓库 make test 仍属人工可选检查，而非合并门禁

## Demo

Run from repository root:

    python3 tool_cli.py list
    echo '{"nodes":[{"id":"A","dependencies":[]},{"id":"B","dependencies":["A"]}]}' | python3 tool_cli.py call graph.inspect
    python3 tool_cli.py agent --input examples/tool_plan.json --output output/agent-plan.json

## Evidential constraints

operation result != scientific truth

claim transfer != acceptance

figure preflight != generated figure

UI rendering != current repository state

Draft PR != merged or CI validated
