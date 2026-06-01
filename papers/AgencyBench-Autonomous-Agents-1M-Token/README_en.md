# [2601.11044] AgencyBench: Benchmarking Autonomous Agents in 1M-Token Real-World Contexts

## Problem
LLM-based autonomous agents have multifaceted capabilities contributing substantially to economic production. But existing benchmarks focus on single agentic capability — fail to capture long-horizon real-world scenarios. Reliance on human-in-the-loop feedback creates scalability bottleneck.

## Contribution
1. **AgencyBench**: Comprehensive benchmark from daily AI usage. 6 core agentic capabilities, 32 real-world scenarios, 138 tasks with specific queries, deliverables, rubrics.
2. **Long-horizon tasks**: Average 90 tool calls, 1M tokens, hours of execution time per task.
3. **Automated evaluation**: User simulation agent for iterative feedback + Docker sandbox for visual/functional rubric-based assessment.

## Method (core summary)
AgencyBench: derives from daily AI usage. 6 capabilities: tool use, planning, reasoning, memory, self-correction, multi-step execution. 32 scenarios, 138 tasks. Automated: user simulation agent provides feedback, Docker sandbox evaluates rubrics. Evaluates closed-source vs open-source models.

## Key Findings
- Closed-source models significantly outperform open-source: 48.4% vs 32.1%
- Significant disparities in resource efficiency, feedback-driven self-correction, tool-use preferences
- Proprietary models best in native ecosystems (Claude via Claude-Agent-SDK)
- Open-source models have distinct performance peaks for specific frameworks
- Average 90 tool calls, 1M tokens per task

## Actionable Insights
1. **Closed-source > open-source for agents**: 48.4% vs 32.1% gap. Invest in best closed-source models for agent tasks. Example: when deploying AI agent, choose Claude/GPT over open-source for better success rate.

2. **Native ecosystem advantage**: Proprietary models perform best in native SDKs. Example: when using Claude, use Claude-Agent-SDK. When using GPT, use OpenAI Agents SDK. Don't mix model + foreign framework.

3. **Long-horizon tasks need 1M tokens**: Real-world agent tasks average 90 tool calls, 1M tokens. Budget accordingly. Example: when planning agent deployment, budget for 1M tokens per complex task — not 10K.

## Assumptions & Limitations
**Conditions for benchmark to work:**
- 32 real-world scenarios representative
- User simulation agent accurate
- Docker sandbox reliable

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED]

**Limitations the paper does NOT mention:**
- 32 scenarios may not cover all use cases
- Cost of running 1M-token tasks
- Model versions change rapidly
- Framework-specific optimization bias

## Metadata
- Year: 2026
- Authors: Keyu Li, Junhao Shi, Yang Xiao, et al.
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2601.11044
- Citation count: [EXTRACTION FAILED]
