# Skill: Agent QA Four-Layer Audit (kiểm toán QA agent)
Source: 2609.17698
Type: evaluation-method / audit-workflow

## Khi nào dùng skill này
- Build hoặc review agent production (coding agent, browser agent, MCP integration) — cần verify QA coverage thực tế
- Agent có nhiều execution routes (CLI, API, MCP, browser, headless, batch) — risk inconsistent control
- Trước khi ship: cần inventory execution surfaces + safeguards + tests + risk chains

Tình huống KHÔNG nên dùng: pure LLM API wrapper không có tool use / shell / file access (không có model-mediated action surface); cần đo runtime effectiveness (skill này audit repository-visible practices, không phải penetration test).

## Input cần có
- Repo agent (source code, config, manifests, tests, docs, CI workflows, deployment artifacts)
- Danh sách model-mediated action surfaces: tool calling, shell/process execution, file editing, browser automation, MCP/plugin integration, workflow execution, persistent agent state
- 4-layer rubric: execution surfaces / safeguards / testing artifacts / risk scenarios
- 8 risk-chain templates: secret-to-tool, workspace-to-persistent-state, extension-to-authority, mode-switch-to-privilege, runtime-code, model-to-process, session-to-action, untrusted-context-to-action

## Các bước thực hiện
1. Inventory execution surfaces: liệt kê mọi interface agent có thể invoke hoặc act (UI, CLI, API, browser, filesystem, shell, plugin, subagent). Với mỗi surface, ghi action routes (ví dụ gemini-cli: CLI, shell, filesystem, browser, web, MCP).
2. Code safeguards: với mỗi route, kiểm tra approval/authorization, sandboxing/isolation, permission/policy, secret management/redaction, MCP/plugin registration, browser/domain scoping. Rule: control phải gắn THEO protected action/asset, không theo interface — cùng boundary cho mọi route tương đương.
3. Audit testing artifacts: đếm conventional tests, security/safety tests, evaluation/red-team-like paths, prompt-injection/adversarial tests. Rule: mỗi high-authority route cần failure-oriented test FAIL khi bỏ approval/sandbox/policy/redaction/domain-scope/extension check.
4. Trace 8 risk chains: với mỗi chain, đặt tên trigger → protected asset → required control → regression check. Ví dụ secret-to-tool: stored key/OAuth token/MCP env var đi vào model-mediated tool path → có flow vào logs/subprocesses/provider calls/tool outputs không?
5. Tính gap shares: % projects/routes lacking direct practice cho mỗi layer. Tập trung COMMON routes trước (credentials, network/API, file access, shell, dynamic code) — weakest coverage nằm ở đây, không phải obscure surfaces.
6. Remediate: (a) define controls by protected action; (b) thêm failure-oriented test/replay case per high-authority route; (c) convert mỗi risk chain thành bounded-action requirement + check.

## Output mong đợi
- Bảng inventory: surfaces × routes × safeguards × tests × risk chains, với gap % mỗi layer; danh sách remediation theo thứ tự: common-route gaps trước, risk-chain operationalization sau.

## Ví dụ áp dụng
- Audit coding agent có CLI + API + MCP: inventory thấy shell execution qua 3 routes nhưng sandbox chỉ gắn route CLI → inconsistent control (96.8% pattern); testing có conventional tests nhưng 0 prompt-injection tests (5.1% baseline); secret-to-tool chain: MCP env var reachable từ tool output, no redaction (36.1% gap). Remediate: sandbox policy cho cả 3 routes, thêm test "sandbox removed → command fails", thêm log redaction cho MCP env.

## Gotchas
- Capability ≠ QA: shell/browser/MCP access là capability; approval/permission/sandbox/redaction/tests mới là QA mechanism — code riêng 2 loại, đừng nhầm "có tool" với "có kiểm soát tool".
- Repository-visible ≠ runtime effective: repo có sandbox config không nghĩa sandbox ngăn được failure trong deployment — audit ghi presence, không phải effectiveness.
- Đừng chỉ inventory surfaces: mỗi action route cần attached boundary (redaction, permission policy, sandboxing) — surface inventory alone là insufficient (paper RQ2).
- Broad controls không đủ: approval/authentication chung không bảo vệ specific action — bind right safeguard to specific sensitive action (secret handling ≠ file containment ≠ MCP extension ≠ browser session).
- Mode-switch trap: action checked ở interactive path có thể reachable qua automatic mode, setup hook, API route, headless path, alternate tool — kiểm tra mọi mode.
- Extension authority: plugin/MCP/skill mới thêm kế thừa local subprocess/network/file/env authority — phải subject to same review boundary as built-in code.
- Không tính inter-rater agreement nếu taxonomy tự phát triển — dùng fixed coding schema + consensus cho ambiguous cases.
