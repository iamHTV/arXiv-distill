# Skill: Agent QA Four-Layer Audit
Source: 2609.17698
Type: evaluation-method / audit-workflow

## When to use this skill
- Building or reviewing a production agent (coding agent, browser agent, MCP integration) — you need to verify actual QA coverage
- The agent has multiple execution routes (CLI, API, MCP, browser, headless, batch) — risk of inconsistent control
- Before shipping: you need an inventory of execution surfaces + safeguards + tests + risk chains

Do NOT use: a pure LLM API wrapper with no tool use / shell / file access (no model-mediated action surface); you need runtime effectiveness measurement (this skill audits repository-visible practices, not penetration testing).

## Input required
- The agent repository (source code, config, manifests, tests, docs, CI workflows, deployment artifacts)
- A list of model-mediated action surfaces: tool calling, shell/process execution, file editing, browser automation, MCP/plugin integration, workflow execution, persistent agent state
- The four-layer rubric: execution surfaces / safeguards / testing artifacts / risk scenarios
- The eight risk-chain templates: secret-to-tool, workspace-to-persistent-state, extension-to-authority, mode-switch-to-privilege, runtime-code, model-to-process, session-to-action, untrusted-context-to-action

## Steps
1. Inventory execution surfaces: list every interface the agent can invoke or act through (UI, CLI, API, browser, filesystem, shell, plugin, subagent). For each surface, record action routes (e.g., gemini-cli: CLI, shell, filesystem, browser, web, MCP).
2. Code safeguards: for each route, check approval/authorization, sandboxing/isolation, permission/policy, secret management/redaction, MCP/plugin registration, browser/domain scoping. Rule: controls must be bound BY protected action/asset, not by interface — the same boundary for every equivalent route.
3. Audit testing artifacts: count conventional tests, security/safety tests, evaluation/red-team-like paths, prompt-injection/adversarial tests. Rule: every high-authority route needs a failure-oriented test that FAILS when the approval/sandbox/policy/redaction/domain-scope/extension check is removed.
4. Trace the eight risk chains: for each chain, name trigger → protected asset → required control → regression check. Example secret-to-tool: a stored key/OAuth token/MCP env var enters a model-mediated tool path → does it flow into logs/subprocesses/provider calls/tool outputs?
5. Compute gap shares: the % of projects/routes lacking the direct practice for each layer. Focus on COMMON routes first (credentials, network/API, file access, shell, dynamic code) — the weakest coverage lives there, not on obscure surfaces.
6. Remediate: (a) define controls by protected action; (b) add a failure-oriented test/replay case per high-authority route; (c) convert each risk chain into a bounded-action requirement + check.

## Expected output
- An inventory table: surfaces × routes × safeguards × tests × risk chains, with gap % per layer; a prioritized remediation list: common-route gaps first, risk-chain operationalization second.

## Example application
- Auditing a coding agent with CLI + API + MCP: the inventory shows shell execution via 3 routes but sandboxing attached only to the CLI route → inconsistent control (the 96.8% pattern); testing has conventional tests but zero prompt-injection tests (5.1% baseline); the secret-to-tool chain: MCP env var reachable from tool output, no redaction (36.1% gap). Remediate: sandbox policy for all 3 routes, add a "sandbox removed → command fails" test, add log redaction for MCP env.

## Gotchas
- Capability ≠ QA: shell/browser/MCP access is a capability; approval/permission/sandbox/redaction/tests are the QA mechanisms — code the two separately; don't confuse "has the tool" with "controls the tool".
- Repository-visible ≠ runtime effective: a sandbox config in the repo doesn't mean the sandbox prevents failures in deployment — the audit records presence, not effectiveness.
- Don't just inventory surfaces: each action route needs an attached boundary (redaction, permission policy, sandboxing) — a surface inventory alone is insufficient (paper RQ2).
- Broad controls are not enough: generic approval/authentication doesn't protect a specific action — bind the right safeguard to the specific sensitive action (secret handling ≠ file containment ≠ MCP extension ≠ browser session).
- Mode-switch trap: an action checked on the interactive path may be reachable via automatic mode, setup hook, API route, headless path, or an alternate tool — check every mode.
- Extension authority: newly added plugins/MCP/skills inherit local subprocess/network/file/env authority — they must be subject to the same review boundary as built-in code.
- Don't compute inter-rater agreement if the taxonomy is developed inductively — use a fixed coding schema and consensus for ambiguous cases.
