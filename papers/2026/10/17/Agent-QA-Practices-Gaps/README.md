# 2609.17698 — A Large-Scale Empirical Study of Quality Assurance Practices and Gaps in AI Agents

## Problem
- Agent QA (đảm bảo chất lượng) chưa được study hệ thống trong thực tế: prior work đánh giá capability/benchmark hoặc từng attack riêng lẻ, KHÔNG đo lường how often real repos expose tools, policies, tests, configuration paths tương ứng. Unknown: developer áp dụng QA practice nào, safeguard/test tích hợp thế nào qua các execution path, repo có evidence end-to-end assurance cho model-mediated action không.

## Contribution
- Study 157 open-source LLM-agent projects (≥100 GitHub stars, snapshot May 2026; 5,852 raw hits 2026-05-21 trước lọc) với 4-layer coding rubric (execution surfaces, safeguards, testing artifacts, risk scenarios) — góc nhìn repository-level về QA engineering thực tế.
- Corpus: SWE automation 26.8% (42), personal/multichannel assistants 19.7% (31), coding assistants 19.1% (30), research/information 13.4% (21), browser/computer-use 12.1% (19), domain-specific 8.9% (14).
- Phát hiện gap lượng hóa: testing agent-specific thưa (prompt-injection tests chỉ 5.1%), controls không đồng nhất qua equivalent routes, risk chains ít thành end-to-end QA checks.

## Method
- Coding rubric 4 layers: execution surfaces (UI, CLI, API, browser, filesystem, shell, plugin, subagent), safeguards (approval, policy, sandboxing, redaction, domain scoping), testing artifacts (tests, evals, repro scripts, security tests, failure-oriented checks), risk scenarios (chain templates: untrusted context → sensitive action/state; KHÔNG phải confirmed vulnerabilities).
- Annotation: mỗi label phải trỏ tới repository-visible artifact; capability label (shell/browser/MCP/plugin access) tách khỏi QA label (approval/permission/sandbox/redaction/tests); QA label ghi presence of reviewable mechanism, KHÔNG phải runtime effectiveness. Open coding → annotation cards → refined labels.
- 2 RQ: RQ1 (4 layers practices) + RQ2 (undercovered problems: thiếu direct practice hoặc chỉ local control cho 1 route).

## Key Findings
- Execution-surface challenges (trên 157 repos): outbound network/API effects 156 (99.4%), credential leakage 155 (98.7%), workspace escape 153 (97.5%), inconsistent control across overlapping paths 152 (96.8%), host process modification 148 (94.3%), extension-driven authority 127 (80.9%), unreviewed runtime code 123 (78.3%), browser session exposure 119 (75.8%). Controls: approval 91.7–93.7%, sandboxing 69.6–69.9%, permission/policy 65.4–76.4%, secret mgmt/redaction 63.9–69.3%, MCP/plugin registration 72.9–81.9%, browser/domain scoping 73.1%.
- Safeguard challenges: privileged command 148 (94.3%), file/workspace 153 (97.5%), secrets 155 (98.7%), plugin/MCP 144 (91.7%), browser session 119 (75.8%).
- Testing: conventional tests/specs 137 (87.3%); security/safety tests 95 (60.5%); evaluation/benchmark/red-team-like 78 (49.7%); prompt-injection/adversarial/jailbreak/red-team tests 8 (5.1%).
- Risk chains (projects có chain): secret-to-tool 149 (94.9%), extension-to-authority 137 (87.3%), workspace-to-persistent-state 128 (81.5%), model-to-process 131 (83.4%), mode-switch-to-privilege 123 (78.3%), runtime-code 99 (63.1%), session-to-action 60 (38.2%), untrusted-context-to-action 45 (28.7%).
- RQ2 gaps (share lacking direct practice): testing — prompt-injection/adversarial tests 97.8%, red-team-like paths 52.4%, security/safety tests 39.7%; safeguards — secret mgmt 36.1%, sandboxing 30.1%, MCP/plugin registration 27.1%, browser/domain scoping 26.9%; execution surfaces — secret mgmt 36.1%, permission 34.6%, sandboxing 30.1–30.4%; risk chains — secret mgmt 35.6%, sandboxing 29.7–30.5%, MCP/plugin 26.3%.
- Pattern: weakest coverage ở COMMON routes (credentials, network/API, file access, shell, dynamic code), không phải obscure surfaces. Chain-interruption practices (authorize transition, contain execution, stop secret propagation) + systematic risk-avoidance (scope paths/tools/modes, reviewable extension authority, scope browser sessions).
- Examples repos: google-gemini/gemini-cli, OpenHands/OpenHands, openai/codex, aaif-goose/goose, browser-use/browser-use, CherryHQ/cherry-studio, 1Panel-dev/MaxKB, Alibaba-NLP/DeepResearch, cordum-io/cordum, Yeachan-Heo/oh-my-claudecode, NousResearch/hermes-agent.

## Actionable Insights
- Định nghĩa control theo protected action/asset, KHÔNG theo interface: cùng secret/file/shell/plugin/browser/network boundary áp dụng cho mọi route (CLI, API, MCP, browser, headless, batch) — vì 96.8% projects có inconsistent control across overlapping paths.
- Thêm failure-oriented test/replay case cho mỗi high-authority route: test phải FAIL khi bỏ approval/sandbox/policy/redaction/domain-scope/extension check — vì 97.8% repos thiếu prompt-injection/adversarial tests và 52.4% thiếu red-team-like paths.
- Audit theo 8 risk-chain templates (secret-to-tool, workspace-to-persistent-state, extension-to-authority, mode-switch-to-privilege, runtime-code, model-to-process, session-to-action, untrusted-context-to-action): mỗi chain đặt tên trigger, protected asset, required control, regression check.

## Assumptions & Limitations
- Counts là repository-visible QA practices, KHÔNG phải runtime effectiveness — repo có thể document safeguard mà không test nó, hoặc expose risky surface mà không có confirmed vulnerability.
- Inductive coding: không tính inter-rater agreement (taxonomy evolved during analysis); mitigated bằng continuous label refinement + consensus.
- May 2026 snapshot, overrepresents coding/browser agents; không phải census (closed-source, enterprise, prototype agents có thể khác); GitHub stars ≠ security maturity; repos có thể thay đổi sau collection.
- Automated search + LLM-assisted summarization có thể tạo false positives/negatives (mitigated bằng manual verification + fixed coding schema).

## Metadata
- 2026 (2026-09-15), Wuyang Dai, Moses Openja (Polytechnique Montréal), Jiho Shin, Hung Viet Pham, Song Wang (York University), cs.SE, https://arxiv.org/pdf/2609.17698, data: anonymous.4open.science/r/Data-Quality-Assurance-Practices-and-Gaps-in-AI-Agents-85F2/
