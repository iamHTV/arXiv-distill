# [2609.01736v1] Harness Engineering in LLM Tool Use via Agent-Native Reusable Tool Primitives

## Problem
LLMs augmented with external tools have demonstrated remarkable performance, but tool use still faces challenges: accuracy drops significantly when tool catalog scales (8K to 120K tokens), SFT-based models don't generalize to dynamic agentic tool scenarios, and API costs are high.

## Contribution
- Introduce Tool Primitives: a library of 25,519 reusable functions and ToolFace interface.
- Introduce HEART (Planner-Router-Verifier): a framework for planning, routing, and verifying tool use.
- HEART outperforms SFT-based models by 10% on average, surpasses GPT-5.4, Claude-4.6-Sonnet, Gemini-3.1-Pro by 6% on average while reducing API cost by up to 85%.
- On 50 real-world tasks: 84% task completion, 3.8× the average of three frontier commercial models (22%).

## Method (core summary)
Tool Primitives are a library of multi-arity functions (25,519 functions) designed for agents to call tools using natural language. ToolFace is the interface between agents and tool primitives. HEART framework has 3 components: Planner (planning), Router (routing tools), Verifier (verifying results). Agents use tool primitives to call tools; HEART manages the tool-calling flow; the verifier checks results before answering the user.

## Key Findings
- HEART outperforms SFT-based models by 10% on average, surpasses three commercial models by 6% on average while reducing token/API cost by up to 85%.
- On 50 real-world tasks: HEART achieves 84% task completion, 3.8× the average of three frontier commercial models (22%).
- ToolBench: Pass Rate 75.1%, Win Rate 75.7% (+1.7%/+1.9% over Claude-4.6-Sonnet; +7.8%/+12.6% over ToolLLaMA).
- ACEBench: Overall 86.9% (vs GPT-5.4 86.0%); Special 95.0% vs 94.0%; Agent 72.3% vs 69.5%.
- Web Search Overall 84.0%, Memory Overall 69.38% (surpassing Claude-Sonnet-4.6 by +3.0%/+1.10%).
- HEART achieves 0.0% ASR (attack success rate) under both prompt injection attack strategies.
- HEART (GPT-5.4 + Qwen3-8B) reduces cost by over 12× relative to HEART (GPT-5.4).

## Actionable Insights
- Use Planner-Router-Verifier framework (HEART) to manage tool use: plan, route tools, verify results before answering. Apply: solopreneur building tool-calling agents should split into these 3 stages, not let LLM decide everything.
- Use tool primitives (reusable tool functions) instead of letting LLM build tool calls from scratch. Apply: build a library of reusable functions for common tasks (search, calculation, data extraction) for agents to call.
- Reduce API cost up to 85% by combining large and small models (GPT-5.4 + Qwen3-8B) in HEART. Apply: use large model for planning, small model for simple tool calls.

## Assumptions & Limitations
- Requires a curated library of tool primitives (25,519 functions) and a tool-calling system; doesn't apply without tools.
- Paper admits: SFT-based models fail almost entirely on dynamic agentic tool scenarios; HEART needs evaluation on more models.
- Limitation paper doesn't mention: not evaluated on real deployment cost (beyond API), not tested on long multi-turn agents.

## Metadata
- Year: 2026
- Authors: Haibo Jin, Suijin Wang, Xucheng Yu, Haojing Luo, Haohan Wang (UIUC, Starc Institute)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2609.01736
