# 2605.03596 Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies

## Problem

Existing AI agent benchmarks evaluate on pre-specified or synthesized files with limited real-world dependencies. In practice, workers must navigate complex workspaces with dozens of different file types, cross-file dependencies, and multi-step tasks requiring holistic workspace understanding. No benchmark evaluates agents on realistic workspace learning — the ability to identify, reason over, exploit, and update explicit/implicit dependencies between heterogeneous files.

## Contribution

1. Introduce Workspace-Bench — the largest benchmark for AI agents on workspace learning, with 5 worker profiles, 74 file types, 20,476 files (up to 20GB), 388 tasks, 7,399 evaluation rubrics. Realistic digital workspaces instead of synthesized test files.
2. Curate tasks with explicit file dependency graphs — each task has a dependency graph enabling evaluation of cross-file retrieval, contextual reasoning, and adaptive decision-making.
3. Five-stage Workspace Learning framework — formalizes how agents navigate workspaces: Exploration → Task-Supporting File Utilization → Heterogeneous File Understanding → Lineage Tracing → Semantic Relations Understanding.

## Method (core summary)

Build realistic workspaces with 5 worker personas (Finance, Engineering, Marketing, HR, Legal), each persona having a workspace of ~4GB files spanning 74 file types (Excel, Word, PDF, code, images, emails, chat logs). 388 tasks curated by human annotators, each task with a dependency graph specifying file relationships. Evaluation: 7,399 rubrics — each rubric is a binary pass/fail criterion. Task counted correct only if ALL rubrics pass. Test 4 agent harnesses (OpenClaw, DeepAgent, Codex, Hermes) × 7 foundation models (GPT-5.4, Gemini-3.1-Pro, Grok-4.3, MiniMax-M2.7, Qwen-3.6-Plus, GLM-5.1, Kimi-2.5) = 28 configurations. Also provide Workspace-Bench-Lite (100 tasks, ~70% cost reduction).

## Key Findings

- Best agent (DeepAgent + GLM-5.1): ~60% rubrics pass rate on Workspace-Bench-Lite
- Human expert baseline: 80.7% — gap of ~20 points
- Average across all agents: 43.3% (only 45.1% mean pass rate)
- Performance degrades with difficulty: Easy 51.4% → Medium 46.0% → Hard 35.7%
- 3 primary capability bottlenecks: Heterogeneous File Understanding, Lineage Tracing, Semantic Relations Understanding
- 2 dimensions agents handle well: Workspace Exploration, Result-Providing File Utilization
- Harness framework choice significantly impacts performance (same backbone LLM)
- DeepAgent + GLM-5.1 highest, followed by Hermes + GLM-5.1, OpenClaw + GLM-5.1
- 15 agent configurations tested total
- Workspace-Bench-Lite preserves distribution while reducing eval cost ~70%

## Actionable Insights

1. Agent architectures need investment in cross-file dependency reasoning — current tool-use capabilities (file navigation, terminal commands) are good enough, but parsing cross-format content and reasoning over deep cross-file dependencies is the bottleneck. Example: enterprise agent needs to read Excel + Word + PDF simultaneously to answer questions about a quarterly report, but current agents fail at linking data across files.
2. When evaluating AI agents for workplace tasks, test on realistic workspaces with diverse file types — synthesized benchmarks inflate performance. Example: company evaluating a coding agent should test on real codebase with configs, docs, tests, CI files, not just coding challenges.
3. Task difficulty stratification is important — agents perform well on simple atomic operations but degrade sharply on tasks requiring dynamic file relationship reasoning. Example: agent can summarize 1 file well but fails when needing to trace version lineage across 5 related files.

## Assumptions & Limitations

- Assumption: rubric-based evaluation captures task completion accurately — may miss nuances in qualitative output
- Limitation: Benchmark currently only covers 5 worker personas, doesn't exhaust all workplace scenarios
- Limitation: 20GB workspace sizes — smaller companies may have much larger workspaces
- Limitation (observed): Paper focuses on English-language workspaces, not tested on multilingual environments. File dependency graphs constructed manually by annotators — may miss implicit dependencies humans naturally understand.

## Metadata

- Year: 2026
- Authors: Zirui Tang, Xuanhe Zhou, Yumou Liu, Linchun Li, Yukai Wu, Weizheng Wang, Hongzhang Huang, Wei Zhou, Jun Zhou, Jiachen Song
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.03596
- Citation count: N/A
- Classification: [applied]
- Skill: N/A — benchmark evaluation framework, no actionable workflow for practitioners
