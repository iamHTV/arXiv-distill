# [2610.03010v1] Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Workflows

## Problem
- Autonomous software engineering agents (SWE-agents) automate complex coding tasks but impose higher computational and environmental costs. Prior work does not systematically compare agentic LLM systems across multiple software engineering tasks.

## Contribution
- Systematic comparison of agentic LLM systems across five software engineering tasks: code generation, technical debt identification, code vulnerability detection, log parsing, and log analysis.
- Evaluates each configuration in terms of accuracy, inference latency, and energy consumption.
- Four main factors evaluated: agent configuration, hardware platform, prompt strategy, and LLM model.
- Six open-weight LLMs, two prompt strategies, three hardware platforms.
- Multi-agent designs consume on average 6.36× as much energy and run 6.07× as long as the non-agentic baseline, with worst-case slowdowns of up to 160×.
- Accuracy gains from additional agents are limited and task-specific: multi-agent improves average vulnerability-detection accuracy, but lightweight non-agentic and single-agent configurations still dominate the Pareto front, accounting for 59 of 66 Pareto-optimal configurations.
- Model and prompt choice act as task-specific levers whose effective direction varies between tasks rather than as global defaults.

## Method (core summary)
- Five software engineering tasks: code generation, technical debt identification, code vulnerability detection, log parsing, and log analysis.
- Four main factors evaluated: agent configuration, hardware platform, prompt strategy, and LLM model.
- Six open-weight LLMs, two prompt strategies, three hardware platforms.
- Evaluate each configuration in terms of accuracy, inference latency, and energy consumption.
- Multi-agent designs consume on average 6.36× as much energy and run 6.07× as long as the non-agentic baseline, with worst-case slowdowns of up to 160× per task-hardware pair.
- Accuracy gains from additional agents are limited and task-specific: multi-agent improves average vulnerability-detection accuracy, but lightweight non-agentic and single-agent configurations still dominate the Pareto front, accounting for 59 of 66 Pareto-optimal configurations.
- Model and prompt choice act as task-specific levers whose effective direction varies between tasks rather than as global defaults.

## Key Findings
- 8 authors from SINTEF, Singapore Management University, Ozyegin University, arXiv category: cs.SE.
- Multi-agent designs consume on average 6.36× as much energy and run 6.07× as long as the non-agentic baseline, with worst-case slowdowns of up to 160× per task-hardware pair.
- Accuracy gains from additional agents are limited and task-specific: multi-agent improves average vulnerability-detection accuracy, but lightweight non-agentic and single-agent configurations still dominate the Pareto front, accounting for 59 of 66 Pareto-optimal configurations.
- Model and prompt choice act as task-specific levers whose effective direction varies between tasks rather than as global defaults.

## Actionable Insights
1. Do not default to multi-agent — MA consumes 6.36× energy and 6.07× time vs non-agentic, only 1/66 configurations Pareto-optimal are MA; few-shot is stronger than adding agents. Application: do not default to multi-agent — lightweight configurations are often Pareto-optimal.
2. Model and prompt choice act as task-specific levers rather than global defaults. Application: select model and prompt per task rather than using one configuration for all tasks.

## Assumptions & Limitations
- Evaluated on code-repair benchmarks from GitHub issues; results may not transfer to agent benchmarks in other domains.
- Evaluated on 4 backbone models.
- No detailed information about training time and computational cost.

## Metadata
- Year: 2026, authors: Merve Astekin, Yan Naing Tun, Arda Goknil, Erik Johannes Husom, Lwin Khin Shar, Hasan Sözer, Ratnadira Widyasari, Hui Song (SINTEF, Singapore Management University, Ozyegin University), arXiv category: cs.SE, PDF link: https://arxiv.org/pdf/2610.03010v1
