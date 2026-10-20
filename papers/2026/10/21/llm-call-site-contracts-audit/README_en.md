# 2610.24545 When Code Becomes an LLM Call: An Empirical Study of Call-Site Contracts in Agentic Systems

## Problem
- Traditional software rests on specifications: pre-conditions, post-conditions, assertions. Agentic systems replace logic (choosing the next tool, judging whether an action is allowed, writing code to run) with LLM calls — behavior is not fixed, varies across runs, and can be steered by input — so the guarantee must come from a contract around each call site.

## Contribution
- First empirical study of call-site contracts: 496 LLM call sites in 40 popular open-source agentic systems (13.4 MLOC, four languages).
- A multi-agent pipeline validated by 17,428 human judgments traces every model output, derives an expected contract for each call site without reading its code, and compares it with the implemented contract.
- 10 recurring gap patterns explain 99% of gaps; 38 mechanisms trigger at runtime; a small code fix enforcing the expected constraint stops all 38.

## Method
- Stage I: call-site analysis → 917 typed outputs, 1,222 consumption relations. Stage II: contract reconstruction — 5,017 implemented constraints, 2,699 expected constraints. Stage III: exploitability and fix validation.
- Assurance levels: capability-bound > code-checked > prompt-only.

## Key Findings
- 48% of LLM outputs reach control flow or execution, 40% of them as free text; 73% of decision-relevant outputs never reach a person.
- 78% of constraints are enforced in code, but 67% of prompt-phase constraints are only requested from the model — including 268 syntactic constraints that code could decide.
- 82% of call sites have code checks before and after the call, yet 63% of expected constraints are unmet; only 5.3% of call sites satisfy their whole contract (median: one third).
- Gap rates: post-conditions 72% (highest), pre-conditions 62%, prompt constraints 47%; 29% of constraints are enforced more weakly than required.
- 10 patterns: unchecked call inputs (330), partial format check (249), unchecked content (253), underspecified prompt (242), faulty request assembly (168), fail-open handling (146), unvalidated action (138), path-dependent check (101), over-broad authority (90), prompt-only check (43).
- Fail-open handling accounts for 44% of conflicting verdicts — Gemini CLI returns ALLOW on 5 of 6 return paths.
- 17% of gaps are exploitable (290), 114 lie on the threat chain: CVSS 9 critical, 21 high. 38 of 60 mechanisms trigger in practice (JARVIS picked tools outside its candidate pool in all 5 runs); a small code fix stops all 38.

## Actionable Insights
1. Do not count "has a check" — measure "how much of the contract is satisfied". Example: audit an agent across the three phases (pre/prompt/post), list expected constraints, compute the satisfied fraction — target 100%, not "has guards".
2. Fail-open kills layered defenses. Example: every exception in a security gate must return DENY or ask-user, never a default ALLOW.
3. Unvalidated actions concentrate at decision-relevant sites (73%). Example: after every LLM call that selects a tool or action, code must verify action ∈ offered set before dispatch.

## Assumptions & Limitations
- 40 open-source systems — proprietary code may differ; four languages.
- Expected contracts are pipeline-derived then human-validated — still subjective.
- Stage III screening excludes 83% of gaps (never reach a consumer) → the exploitable fraction is an upper bound on real risk.
- Fix validation stops the 38 triggered exploits but does not prove it stops every attack.

## Metadata
- 2026; authors: Shihao Weng, Longtian Wang, Yang Feng, Mingfei Cheng, Jia Liu, Chao Shen (Nanjing University, Xi'an Jiaotong University), He Ye, Federica Sarro (UCL), Xiaofei Xie (SMU); categories: cs.SE, cs.AI, cs.CR; PDF: https://arxiv.org/pdf/2610.24545; citation count: [NO DATA — published 2026-10-17]
