# [2610.35031] PatentAgentBench: Benchmarking LLM Agents with Professional Patent Task Suites

## Core Value (1 sentence)

Before deploying agents for patent practice, evaluate the model–agent harness pair on PatentAgentBench (510 instances, 8 task suites) — the strongest pair (Claude Opus 5 + Hermes) averages only 52.8/100, showing current agents still fall far short in retrieving relevant evidence and producing substantively sound patent documents.

## Problem

Patent practice lies at the intersection of technical, legal, and linguistic work, making it challenging yet crucial to technological innovation. Recent advances in LLMs and agentic systems have demonstrated the potential to complete realistic business workflows and even patent work. This raises a question: can current AI systems perform patent work reliably? Existing benchmarks cover a limited range of patent tasks and simplify evidence acquisition by providing reference materials or candidate documents. There is no comprehensive way to evaluate whether AI agents can perform professional patent work reliably.

## Contribution

1. Introduces PatentAgentBench, a benchmark comprising 510 instances across eight task suites: novelty search, freedom-to-operate (FTO) search, design FTO, invalidity search, claim charting, patent drafting, office-action response, and patent translation.
2. The benchmark is curated from real patent records and professional materials, combining task-specific metrics with expert-reviewed annotations and rubrics.
3. Retrieval tasks (novelty search, FTO, etc.) require agents to search and compare patent collections without a supplied candidate pool. Drafting and OAR tasks assess agent work quality given technical disclosure and office action notice.
4. Evaluates seven LLMs across four agent harnesses on PatentAgentBench, finding that current systems still struggle to identify novelty, assess risk, and understand practitioner intent throughout patent workflows. The strongest model–harness pair averages 52.8, leaving substantial room for improvement.

## Method

PatentAgentBench follows a four-stage curation pipeline combining automated processing with expert review. First, each task's input, expected deliverable, task evidence, and evaluation criteria are defined based on professional patent practice. Second, experts establish inclusion/exclusion criteria to guide rule-based and LLM-assisted screening of patent records, official proceedings, and professional work materials. The expert team comprises 31 professionals: 5 senior patent examiners, 15 senior patent agents, 3 dual-qualified lawyers, and 8 senior IPR specialists. Experts review candidate cases for relevance, completeness, and suitability. Third, selected materials are parsed and normalized, task inputs reconstructed, and reference evidence or scoring criteria derived from source records. Automated pre-annotation supports this process, while experts correct labels and review rubrics. Each instance is annotated by one expert and reviewed by a second. Finally, each case is packaged with its input, evidence conditions, output requirements, and evaluation anchors. Reference evidence is traceable to its source and task inputs do not expose answers.

PatentAgentBench covers eight task suites spanning evidence discovery, feature-level comparison, and document preparation. Novelty search, patent FTO, design FTO, and invalidity search require agents to retrieve relevant evidence. Claim charting requires mapping technical features to supplied evidence. Patent drafting, office action response, and translation require producing professional documents. Metrics: novelty search uses Hit@100; FTO/design FTO/invalidity search use recall; claim charting uses F1; drafting and OAR use weighted rubric-based scores; translation uses category-specific metrics.

## KNOWLEDGE — Data & Concepts

- PatentAgentBench: 510 instances, 8 task suites, 7 LLMs × 4 agent harnesses (Codex, Claude Code, OpenClaw, Hermes).
- Models: GPT-5.6-Sol, Qwen3.8-Max, Kimi K3, DeepSeek-V4-Pro, MiniMax-M3, GLM-5.3, Claude Opus 5.
- Strongest model–harness pair: Claude Opus 5 + Hermes, average score 52.8/100.
- Claude Opus 5 + Claude Code: 50.3 average.
- Design FTO: recall under 4 on every evaluated configuration — the largest gap.
- Invalidity search: switching Opus from Claude Code to Hermes raises recall from 28.7% to 55.0% (+26.3 points).
- GPT-5.6-Sol with OpenClaw: 50.0; with Claude Code: 49.3.
- GLM-5.3 beats GPT-5.6-Sol under Codex (48.1 vs 43.8), but ordering reverses under OpenClaw (GPT 50.0 vs GLM 29.5).
- 31 expert professionals curated data: 5 senior patent examiners, 15 senior patent agents, 3 dual-qualified lawyers, 8 senior IPR specialists.
- Task suites: Novelty Search (80 instances, Hit@100), Patent FTO (60, Recall), Design FTO (80, Recall), Invalidity Search (80, Recall), Claim Charting (40, F1), Patent Drafting (80, rubric), Office Action Response (60, 57 rubric criteria), Patent Translation (80, category-specific metrics).

## INSIGHT — Mechanism & Why

[Model and harness advantages do not transfer consistently across configurations and tasks] happens BECAUSE [GLM-5.3 beats GPT-5.6-Sol under Codex but the ordering reverses under OpenClaw; harness advantages are also task-specific]. This means [model and harness selection must be considered together, not in isolation].

[Current agents struggle to retrieve relevant evidence and produce substantively sound patent documents] happens BECAUSE [the strongest pair averages only 52.8/100, and Design FTO recall stays under 4 across all configurations]. This means [a gap remains between generating plausible documents and delivering reliable patent work].

[Design-related evidence discovery is a persistent gap] happens BECAUSE [high recall on textual FTO does not extend to visual design search; ability to extract visual features and search similar designs is not well supported by current LLMs and harnesses]. This means [visual patent search remains unsolved].

[Patent drafts follow expected structure but have weaknesses in claim organization, case understanding, and legal argumentation] happens BECAUSE [drafts exhibit strong formal organization but weak dependent-claim hierarchies; OAR shows weaknesses in case understanding, response strategy, and substantive argumentation]. This means [better control over substantive content is needed, not just format].

## IDEA — Actionable Applications

1. Use PatentAgentBench as an evaluation standard before deploying agents for patent work: evaluate the model–harness pair as a unit, not separately. For whom: IP/legal teams deploying patent agents. First step: run the benchmark across the 8 task suites with your chosen model and harness, compare average scores.

2. Apply expert-reviewed rubric evaluation to agent outputs in legal/IP domains: not just automatic scoring, but detailed rubrics on case understanding, response strategy, and amendment quality. For whom: evaluation teams for legal AI agents. First step: build rubrics for each type of legal document the agent produces (drafts, office action responses, claim charts).

3. Apply evidence retrieval verification before accepting agent output: agents often fail to retrieve relevant evidence, so cross-check cited references against source documents. For whom: legal decision-support agent systems. First step: add a source-verification step in the agent pipeline — require agents to cite sources and verify citations match source documents.

## WISDOM — General Principle

- Principle: Model and agent harness selection must be considered together, as their advantages vary across tasks — there is no single optimal model–harness pair for all legal tasks. Apply when building agent systems for high-specialization domains (law, medicine, finance). Do not apply when evaluating a standalone model without regard to its execution environment.

## Assumptions & Limitations

- Conditions that must hold: real patent record dataset available, patent experts available for rubric evaluation, agent harness environment available to run evaluation.
- Limitations acknowledged by the paper: PatentAgentBench covers 8 professional patent tasks. However, tasks are evaluated separately rather than as a complete patent lifecycle. The evaluation process focuses on the final output or delivery of agents rather than the agent working process. Future work plans to extend the benchmark to include more tasks and evaluate the complete patent lifecycle.
- Limitations the paper does NOT state: effectiveness on larger or newer models after publication date, benchmark operational cost at scale, and scalability to other legal domains beyond patent practice.

## Metadata

- Year: 2026
- Authors: Yijie Hu, Wei Li, Junjie Zhou, Zhiqi Jiang, Yi Jin, Licong Xu, Xinkai Sun, Kai Duan, Lisha Zhang (PatSnap Ltd. Co.)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.35031v1
- Citation count: [not found]