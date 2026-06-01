# [2605.26329v1] JobBench: Aligning Agent Work With Human Will

## Problem
Current benchmarks for occupational AI agents are scoped primarily by economic values, telling a replacement story. GDPVal — the current benchmark — is approaching saturation: GPT-5.4 achieves 83.0. But these benchmarks don't answer: which tasks do workers actually WANT to delegate to AI? Prior work doesn't align evaluation with human will.

## Contribution
1. **JobBench**: Benchmark aligns agentic evaluation with human will rather than just economic values. 130 agentic tasks across 35 occupations, each from Workbank-elicited delegation preference (survey of 1,500+ workers).
2. **Fact-anchored rubric chain**: 4,631 binary criteria, average 35.6 criteria per task. Awards credit only when EVERY step in the chain holds together.
3. **Heterogeneous workspaces**: Each task packaged with heterogeneous reference files — agents must locate, retrieve, reconcile source evidence before producing artifact.

## Method (core summary)
Based on Workbank survey (1,500+ workers rate work duties for delegation desire). Select duties experts WANT delegated and spend most preparation time on. Each task = workspace with reference files (CSVs, guidance documents, surveillance data, etc.) + fact-anchored rubric chain. Agent must reason through cluttered information streams, produce artifact, graded by chained binary criteria. 36 model-scaffold configurations evaluated.

## Key Findings
- Strongest: Claude Opus 4.7 under Claude Code = 45.9%
- GPT-5.5 under Codex = 42.7%
- GPT-5.4 under Codex = 38.9%
- Beyond Claude/GPT families: no model exceeds 19%
- Weakest: Grok-4.2-Fast = 4.38%
- GDPVal approaching saturation (GPT-5.4 = 83.0) but corresponding JobBench = 38.9
- GPT-5.4 under Codex takes 2.40× runtime of GDPVal, tool calls 1.3×

## Actionable Insights
1. **Measure AI readiness by delegation desire, not just economic value**: When evaluating AI for workplace automation, ask workers which tasks they WANT to delegate — not just which are most economically valuable. Example: reporter wants to delegate "cross-source fact checking" — economically valuable but workers also WANT to offload. Prioritize automation by worker satisfaction, not just cost savings.

2. **Heterogeneous workspaces > clean task packets**: Real professional work has cluttered, conflicting information. Benchmark AI on heterogeneous data, not just clean inputs. Example: when testing AI for financial analysis, have it reconcile conflicting reports from multiple sources — not just clean spreadsheets.

3. **Fact-anchored rubric chains for evaluation**: When evaluating AI outputs, use chained binary criteria — every step must hold together. Don't just check final output. Example: when evaluating AI-generated report, check: (1) sources located? (2) data reconciled? (3) analysis sound? (4) conclusion supported? — ALL must pass.

## Assumptions & Limitations
**Conditions for benchmark to work:**
- U.S.-centered, digital, document-heavy professional tasks
- 35 selected O*NET occupations — doesn't represent all occupations
- English-only, non-physical work

**Limitations the paper acknowledges:**
- Limited to U.S.-centered, digital, document-heavy tasks
- Does not represent all occupations, non-U.S. markets, non-English workplaces
- Physical work, real-time collaboration, long-term workflows not covered
- Not for deployment validation — benchmark only

**Limitations the paper does NOT mention:**
- 130 tasks may be too few for robust evaluation
- 35 occupations selection criteria opaque
- Rubric chain design has human bias
- Not tested with real workers — benchmark only
- Runtime comparison (2.40×) may be unfair — different task complexity
- No cost-effectiveness of agent deployment addressed

## Metadata
- Year: 2026
- Authors: Yuetai Li, Yichen Feng, Zhangchen Xu, et al.
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.26329v1
- Citation count: [EXTRACTION FAILED]
