# [2610.03010v1] Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Workflows

## Problem
Agentic LLM systems are increasingly used in software engineering but impose higher computational and environmental costs than single-agent systems. Multi-agent coordination does not always bring proportional benefits.

## Contribution
- Comprehensive empirical study comparing agentic LLM configurations across 5 dev tasks, 6 models, 2 prompt strategies, 3 hardware platforms.
- Identify optimal configurations on the efficiency frontier between accuracy, energy, and latency.
- Investigate impact of agentic complexity on energy and latency.

## Method (core summary)
Experiments on 5 software development tasks (code generation, technical debt detection, vulnerability detection, log parsing, log analysis), 6 LLM models, 2 prompt strategies (zero-shot, few-shot), 3 hardware platforms. Compare 4 agentic configurations: NA (No Agent), SA (Single Agent), DA (Delegation Agent), MA (Multi Agent). Evaluate accuracy, energy (kWh), latency (seconds). Build Pareto front.

## Key Findings
- Multi-agent designs consume on average 6.36× as much energy and run 6.07× as long as non-agentic baseline, with worst-case slowdowns up to 160×.
- Of 66 Pareto-optimal configurations: 36 (55%) NA, 23 (35%) SA, 6 (9%) DA, only 1 (2%) MA.
- Few-shot prompting increases log parsing accuracy from 3.4% to 54.3%, reduces energy 24–41%.
- G3-4B highest Pass@1 for code generation (99.8%); GPT-OSS highest Macro F1 for technical debt detection (58.6%); Q3-4B best vulnerability detection (57.8%); Q2.5C-7B best log parsing (42.2%) and log analysis (8.5%).
- MA achieves highest F1-score (55.4%) for technical debt detection but NA has lowest energy and latency.

## Actionable Insights
- Don't default to multi-agent: lightweight configurations (single agent or no-agent) typically dominate the Pareto front, directly saving money and time. Apply: solopreneur building AI pipeline should start from single agent, add multi-agent only with clear evidence of benefit.
- Few-shot prompting is a more impactful lever than agentic configuration for many tasks: raises log parsing from 3.4% to 54.3% and reduces energy 24–41%. Apply: before adding complex agents, try few-shot prompt with concrete examples.

## Assumptions & Limitations
- Requires the 5 selected dev tasks and 6 chosen LLM models; results may differ on other tasks/models.
- Paper admits: hardware effects modest for lightweight workloads but larger for heavy workloads; lowest-energy model varies by task.
- Limitation paper doesn't mention: not evaluated on models larger than 70B, not tested on longer workflows.

## Metadata
- Year: 2026
- Authors: Merve Astekin, Yan Naing Tun, Arda Goknil, Erik Johannes Husom, Lwin Khin Shar, Hasan Sozer, Ratnadira Widyastari, Hui Song
- arXiv category: cs.AI, cs.SE
- PDF link: https://arxiv.org/pdf/2610.03010
