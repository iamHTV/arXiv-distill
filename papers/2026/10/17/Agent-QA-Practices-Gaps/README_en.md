# 2609.17698 — A Large-Scale Empirical Study of Quality Assurance Practices and Gaps in AI Agents

## Problem
- Agent QA (quality assurance) has not been systematically studied in practice: prior work evaluates capabilities/benchmarks or individual attacks, but does NOT measure how often real repositories expose the corresponding tools, policies, tests, and configuration paths. Unknown: which QA practices developers adopt, how safeguards and testing integrate across execution paths, and whether repos provide evidence of end-to-end assurance for model-mediated actions.

## Contribution
- A study of 157 open-source LLM-agent projects (≥100 GitHub stars, May 2026 snapshot; 5,852 raw hits on 2026-05-21 before filtering) with a four-layer coding rubric (execution surfaces, safeguards, testing artifacts, risk scenarios) — a repository-level view of real QA engineering.
- Corpus: SWE automation 26.8% (42), personal/multichannel assistants 19.7% (31), coding assistants 19.1% (30), research/information 13.4% (21), browser/computer-use 12.1% (19), domain-specific 8.9% (14).
- Quantified gaps: agent-specific testing is rare (prompt-injection tests only 5.1%), controls are inconsistently applied across equivalent routes, and risk chains are seldom translated into end-to-end QA checks.

## Method
- Four-layer coding rubric: execution surfaces (UI, CLI, API, browser, filesystem, shell, plugin, subagent), safeguards (approval, policy, sandboxing, redaction, domain scoping), testing artifacts (tests, evals, repro scripts, security tests, failure-oriented checks), risk scenarios (chain templates: untrusted context → sensitive action/state; NOT confirmed vulnerabilities).
- Annotation: every label must point to a repository-visible artifact; capability labels (shell/browser/MCP/plugin access) are separated from QA labels (approval/permission/sandbox/redaction/tests); QA labels record the presence of reviewable mechanisms, NOT runtime effectiveness. Open coding → annotation cards → refined labels.
- Two RQs: RQ1 (practices across the four layers) + RQ2 (undercovered problems: missing direct practice, or only a local control for one route).

## Key Findings
- Execution-surface challenges (of 157 repos): outbound network/API effects 156 (99.4%), credential leakage 155 (98.7%), workspace escape 153 (97.5%), inconsistent control across overlapping paths 152 (96.8%), host process modification 148 (94.3%), extension-driven authority 127 (80.9%), unreviewed runtime code 123 (78.3%), browser session exposure 119 (75.8%). Controls: approval 91.7–93.7%, sandboxing 69.6–69.9%, permission/policy 65.4–76.4%, secret management/redaction 63.9–69.3%, MCP/plugin registration 72.9–81.9%, browser/domain scoping 73.1%.
- Safeguard challenges: privileged command 148 (94.3%), file/workspace 153 (97.5%), secrets 155 (98.7%), plugin/MCP 144 (91.7%), browser session 119 (75.8%).
- Testing: conventional tests/specs 137 (87.3%); security/safety tests 95 (60.5%); evaluation/benchmark/red-team-like 78 (49.7%); prompt-injection/adversarial/jailbreak/red-team tests 8 (5.1%).
- Risk chains (projects showing the chain): secret-to-tool 149 (94.9%), extension-to-authority 137 (87.3%), workspace-to-persistent-state 128 (81.5%), model-to-process 131 (83.4%), mode-switch-to-privilege 123 (78.3%), runtime-code 99 (63.1%), session-to-action 60 (38.2%), untrusted-context-to-action 45 (28.7%).
- RQ2 gaps (share of affected projects lacking the direct practice): testing — prompt-injection/adversarial tests 97.8%, red-team-like paths 52.4%, security/safety tests 39.7%; safeguards — secret management 36.1%, sandboxing 30.1%, MCP/plugin registration 27.1%, browser/domain scoping 26.9%; execution surfaces — secret management 36.1%, permission 34.6%, sandboxing 30.1–30.4%; risk chains — secret management 35.6%, sandboxing 29.7–30.5%, MCP/plugin registration 26.3%.
- Pattern: the weakest coverage is on COMMON routes (credentials, network/API, file access, shell, dynamic code), not obscure surfaces. Chain-interruption practices (authorize the transition, contain execution, stop secret propagation) plus systematic risk-avoidance (scope paths/tools/modes, make extension authority reviewable, scope browser sessions).
- Example repos: google-gemini/gemini-cli, OpenHands/OpenHands, openai/codex, aaif-goose/goose, browser-use/browser-use, CherryHQ/cherry-studio, 1Panel-dev/MaxKB, Alibaba-NLP/DeepResearch, cordum-io/cordum, Yeachan-Heo/oh-my-claudecode, NousResearch/hermes-agent.

## Actionable Insights
- Define controls by protected action/asset, NOT by interface: the same secret/file/shell/plugin/browser/network boundary applies to every route (CLI, API, MCP, browser, headless, batch) — because 96.8% of projects have inconsistent control across overlapping paths.
- Add a failure-oriented test or replay case for every high-authority route: the test must FAIL when the approval/sandbox/policy/redaction/domain-scope/extension check is removed — because 97.8% of repos lack prompt-injection/adversarial tests and 52.4% lack red-team-like paths.
- Audit with the eight risk-chain templates (secret-to-tool, workspace-to-persistent-state, extension-to-authority, mode-switch-to-privilege, runtime-code, model-to-process, session-to-action, untrusted-context-to-action): each chain names the trigger, protected asset, required control, and regression check.

## Assumptions & Limitations
- Counts are repository-visible QA practices, NOT runtime effectiveness — a repo may document a safeguard without testing it, or expose a risky surface without a confirmed vulnerability.
- Inductive coding: no inter-rater agreement computed (taxonomy evolved during analysis); mitigated by continuous label refinement and consensus.
- May 2026 snapshot; overrepresents coding/browser agents; not a census (closed-source, enterprise, and prototype agents may differ); GitHub stars are not a security-maturity measure; repositories may have changed after collection.
- Automated search and LLM-assisted summarization may introduce false positives/negatives (mitigated by manual verification and a fixed coding schema).

## Metadata
- 2026 (2026-09-15), Wuyang Dai, Moses Openja (Polytechnique Montréal), Jiho Shin, Hung Viet Pham, Song Wang (York University), cs.SE, https://arxiv.org/pdf/2609.17698, data: anonymous.4open.science/r/Data-Quality-Assurance-Practices-and-Gaps-in-AI-Agents-85F2/
