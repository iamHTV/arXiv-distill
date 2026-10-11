# [2507.21504] Evaluation and Benchmarking of LLM Agents: A Survey

## Problem
LLM-based agents have opened new frontiers in AI applications, but evaluating these agents remains complex and underdeveloped. The landscape of agent evaluation is fragmented. Enterprise-specific challenges are often overlooked — role-based access, reliability guarantees, dynamic interactions, compliance.

## Contribution
1. **Two-dimensional taxonomy**: (1) Evaluation Objectives — WHAT to evaluate: behavior, capabilities, reliability, safety. (2) Evaluation Process — HOW to evaluate: interaction modes, data, metrics, tooling.
2. **Enterprise-specific challenges**: Role-based access, reliability guarantees, dynamic long-horizon interactions, compliance.
3. **Future directions**: Holistic frameworks, realistic settings, automated evaluation, cost-bounded protocols.

## Method (core summary)
Survey taxonomy: Evaluation Objectives (4 categories): Agent Behavior (task completion, output quality), Agent Capabilities (tool use, planning, reasoning, memory, multi-agent), Reliability (consistency, robustness), Safety & Alignment (fairness, compliance, security). Evaluation Process (4 categories): Interaction Mode (static vs interactive), Evaluation Data (synthetic vs real-world), Metrics Computation (quantitative vs qualitative), Evaluation Tooling (instrumentation, leaderboards).

## Key Findings
- [SURVEY] — no new experiments, taxonomy + synthesis
- 4 evaluation objectives: behavior, capabilities, reliability, safety
- 4 evaluation process dimensions: interaction, data, metrics, tooling
- Enterprise challenges: role-based access, reliability, compliance
- 4 future directions: holistic, realistic, automated, cost-bounded

## Actionable Insights
1. **Evaluate across multiple dimensions**: Don't just measure task success. Evaluate behavior, capabilities, reliability, safety simultaneously. Example: when deploying AI agent, evaluate: task completion (behavior), tool use quality (capabilities), consistency (reliability), bias/fairness (safety).

2. **Enterprise challenges matter**: Role-based access, compliance, data security — often overlooked but critical for deployment. Example: when deploying AI agent in enterprise, ensure: role-based data access, audit trails, compliance logging, error handling.

3. **Automated evaluation reduces cost**: LLM-as-a-judge, Agent-as-a-judge — reduce human effort. Example: when evaluating AI agent performance at scale, use LLM judge instead of human review for routine evaluations.

## Assumptions & Limitations
**Conditions for survey to work:**
- Comprehensive literature review
- Taxonomy must capture key dimensions

**Limitations the paper acknowledges:**
- Fragmented landscape — may miss some evaluation approaches
- Enterprise challenges underexplored in current research

**Limitations the paper does NOT mention:**
- Survey scope may miss emerging evaluation methods
- Taxonomy may not capture all nuances
- No empirical comparison of evaluation methods
- Enterprise challenges described but not solved

## Metadata
- Year: 2025
- Authors: Mahmoud Mohammadi, Yipeng Li, Jane Lo, Wendy Yip
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2507.21504
- Citation count: [EXTRACTION FAILED]
