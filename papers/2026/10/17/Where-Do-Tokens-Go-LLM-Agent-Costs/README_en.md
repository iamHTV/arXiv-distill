# [2610.11602v1] Where Do the Tokens Go? Understanding and Reducing Costs in LLM Agents for Vulnerability Discovery

## Problem
- LLM agents can spend millions of tokens during vulnerability discovery without producing a working proof of concept (PoC). Prior work does not diagnose where that budget goes or why it fails to produce results — what consumes the budget, and why does the effort not yield a working PoC?

## Contribution
- Multi-axis open-coding study of 200 CyberGym traces, spanning four agents (Codex, OpenCode, Cybench, EnIGMA) under an unaided baseline and four existing efficiency methods.
- Three key findings: (1) agents vary substantially in success and cost, and higher spending does not consistently yield better outcomes; (2) code localization and understanding, together with vulnerability reasoning and trigger design, account for 60.4% of tokens and represent the two leading bottlenecks in failed runs; (3) only 24.4% of matched comparisons preserve success at lower total cost; unsuitable signals and auxiliary overhead limit the benefits of existing methods.
- AVRI (Agent-centric Vulnerability Reasoning Interface) built around a persistent Bidirectional Evidence Trace (BET). BET connects how the harness consumes input with the conditions required to make a selected operation unsafe, retaining source-supported correspondences alongside the agent's hypotheses and open questions. Reading, analysis, and persistence commands help agents build and reuse this evidence rather than repeatedly retrieve and reconstruct it.

## Method (core summary)
- Empirical study: 200 traces, four agents, five configurations per agent (baseline and four efficiency methods), ten tasks per configuration, each combination executed once.
- Four efficiency methods evaluated: AgentDiet (interaction history compression), Revelio (lightweight static analysis for vulnerability hypothesis generation and prioritization), PAgent (coverage feedback to guide PoC generation), CodeGraph (repository-level call and reference graph exposed through query interface).
- AVRI: agent-centric interface built around persistent BET — connects harness input consumption with conditions required to make a selected operation unsafe; reading, analysis, and persistence commands help agents build and reuse evidence rather than repeatedly retrieve and reconstruct.
- Evaluation: 20 CyberGym tasks, Codex and OpenCode, comparing AVRI with baseline and four efficiency methods; measuring success, recall, elapsed time, and cost.

## Key Findings
- 4 authors from Huazhong University of Science and Technology, arXiv category: cs.CR.
- Agents vary substantially in success and cost; higher spending does not consistently yield better outcomes.
- Code localization and understanding + vulnerability reasoning + trigger design account for 60.4% of tokens, two leading bottlenecks in failed runs.
- Only 24.4% of matched comparisons preserve success at lower total cost.
- Table 3: Codex — Baseline cost $132.65 → AVRI $108.75 (−18.0%), success 85% → 85%, recall 65% → 75%, time 50,968s → 33,313s.
- OpenCode — Baseline cost $4.38 → AVRI $3.34 (−23.7%), success 100% → 100%, recall 90% → 90%, time 25,324s → 24,017s.

## Actionable Insights
1. Code localization and understanding plus vulnerability reasoning and trigger design consume 60.4% of tokens and are the leading bottlenecks in failed runs. Application: focus optimization on these activities rather than blindly compressing interaction history.
2. Only 24.4% of matched comparisons preserve success at lower total cost — unsuitable signals and auxiliary overhead limit existing methods' benefits. Application: evaluate effectiveness together with cost, not just a single number.

## Assumptions & Limitations
- 20-task evaluation, one run per configuration — does not establish robustness to run-to-run variation.
- AVRI evaluation focuses on Codex and OpenCode (Cybench and EnIGMA had lower success rates).
- 7,200-second wall-clock timeout per run.
- Not stated: effectiveness on programming languages beyond C/C++ and other vulnerability types.

## Metadata
- Year: 2026, authors: Li Lu, Hongjie Chen, Yanjie Zhao, Haoyu Wang (Huazhong University of Science and Technology), arXiv category: cs.CR, PDF link: https://arxiv.org/pdf/2610.11602v1
