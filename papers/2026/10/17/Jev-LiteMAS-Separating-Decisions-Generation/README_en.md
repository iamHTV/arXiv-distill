# [2610.21411v1] Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows

## Problem
- Multi-agent LLM systems rely on generative models for expert execution, workflow planning, and artifact review. Yet many coordination operations require only bounded decisions, such as selecting the next expert or judging artifact quality. Prior work does not address replacing these operations with low-cost decision models.

## Contribution
- Jev-LiteMAS — a multi-agent framework that bridges both gaps by combining a lightweight decision model (Jev) with generative execution and feedback.
- Jev selects experts dynamically from the task and prior expert outputs, using accumulated context to ground subsequent execution without a pre-generated trajectory.
- Jev screens intermediate artifacts against task criteria: passing artifacts proceed directly, whereas flagged ones undergo LLM re-review for acceptance or corrective feedback.
- Across four benchmarks and two backbones, Jev-LiteMAS reduces generative-LLM tokens by 12.7–54.6% over LAS, maintaining accuracy within 1.34 percentage points and lowering latency in seven of eight settings.

## Method (core summary)
- Jev-LiteMAS framework with three components: Jev (lightweight decision model), generative execution, and feedback.
- Jev selects experts dynamically from task and prior outputs; Jev screens intermediate artifacts: passing artifacts proceed directly, flagged ones undergo LLM re-review.
- Grounds routing in substantive expert outputs to prevent accuracy loss.
- Evaluated on four benchmarks and two backbones (DeepSeek-V4-Flash, GPT-5).
- Jev screening detects 91.33–95.33% of corrupted cases.
- Cascaded configuration consumes 14.6–21.7% fewer generative-LLM tokens than LLM judgment.

## Key Findings
- 4 authors from Shanghai Jiao Tong University, arXiv category: cs.AI.
- Across four benchmarks and two backbones, Jev-LiteMAS reduces generative-LLM tokens by 12.7–54.6% vs LAS.
- Accuracy changes within 1.34 percentage points.
- Reduces latency in seven of eight settings.
- Grounding routing in substantive expert outputs prevents up to 18.0 points in accuracy loss.

## Actionable Insights
1. Separate decision-making from generation in multi-agent workflows: use a lightweight decision model for coordination decisions, only call LLM review when artifact needs fixing. Application: replace LLM for every orchestration decision with a lightweight decision model (Jev), only call LLM review when artifact needs correction, reducing tokens by 12.7–54.6%.
2. Ground routing in substantive expert outputs to prevent up to 18 points of accuracy loss. Application: when the agent writes an artifact, check the artifact before deciding the next step, don't rely on abstract reasoning.

## Assumptions & Limitations
- Feedback-driven routing operates over a predefined pool of expert roles and legal actions.
- Framework does not dynamically create new expert roles.
- Evaluated on 4 benchmarks and 2 backbones.

## Metadata
- Year: 2026, authors: Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li (Shanghai Jiao Tong University), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2610.21411v1
