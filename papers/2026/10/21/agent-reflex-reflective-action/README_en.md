# 2610.17953 Agent-Reflex: Teaching Language Agents to Act Reflectively

## Problem
- LLMs have become long-horizon interactive agents, but real deployments face noisy MCP tool feedback and user corrections at arbitrary turns — existing methods provide limited supervision for reflection learning and failure recovery. Current environments assume clean feedback; GPT-5.2 and Claude-4.5-Sonnet degrade markedly under user/tool noise.

## Contribution
- Agent-Reflex: a general training framework for incentivizing proactive reflection, in three stages.
- Stage 1 — RSD (Environment Reflection Skill Discovery): injects grounded tool-feedback perturbations into environment scaling, samples a capability-diverse LLM pool, mines matched success–failure pairs, and summarizes reusable reflection meta-skills.
- Stage 2 — ReSFT (Reflective Supervised Fine-Tuning): converts each skill into supervision for self-reflection, skill recovery, and user-centric correction.
- Stage 3 — ORPO (On-Policy Reflective Policy Optimization): agentic reinforcement learning under noisy interactions plus reflection-guided on-policy distillation.

## Method
- Data: 8 tool-error families mined from 24,510 real error returns.
- Backbone: Qwen3-8B; evaluation in standard MCP format with each benchmark's official metric.
- ORPO combines RL under noise with distillation from reflection meta-skills — skills summarized from real failures transfer better than experience estimated from rollouts.

## Key Findings
- Five long-horizon tool-use benchmarks (BFCL-v4, ACEBench, 200 stratified ToolSandbox tasks, τ²-Bench, VitaBench): overall 58.6 — highest among strong baselines.
- VitaBench: 17.5% vs Reflexion-8B 6.8%. ACEBench: 78.0% vs NoisyAgent-8B 52.0%; turn-level 73.3% while baselines keep 85.0% step-level accuracy — gains come from multi-turn interaction.
- τ²-Bench: 62.1% vs EnvScaler-8B 54.6%.
- AgentNoiseBench (noisy interaction): overall 29.1% vs NoisyAgent-8B 25.9% — highest among 8B methods. Clean foundation models: GPT-5.2 81.0/61.0, Claude-4.5-Sonnet 73.0/57.0, Gemini-2.5-Pro 60.0/37.0, Qwen3-8B 26.2/14.1 (τ²/Vita).
- ORPO holds a stable advantage over GRPO, DAPO, REINFORCE++, SEED, and noisy Agent RL over 100 RL steps on BFCL-v4, τ²-Bench, and real interaction noise.
- Fine-grained noise table: partially extracted (pdfminer mangled) — only prose-verified numbers used.

## Actionable Insights
1. Teach recovery behavior, don't just give advice at inference. Example: instead of prompting "re-check when a tool errors", fine-tune on real success–failure pairs — the agent self-corrects without critique text.
2. Summarize meta-skills from real failures and reuse them across tasks. Example: log 8 tool-error families (timeout, schema mismatch, permission denied...) → write 8 recovery skills → train the agent to use them.
3. RL under noise beats RL on clean data. Example: when training a customer-support agent, inject tool/user noise from the start — more robust than training clean and deploying into noise.

## Assumptions & Limitations
- Needs mined success–failure pairs from environment scaling — depends on grounded perturbation quality.
- ORPO requires on-policy distillation — more compute than plain SFT.
- Benchmarked on tool-use domains; generalization to other domains unproven.
- ACEBench gains are mostly multi-turn — single-turn gains are small.

## Metadata
- 2026; authors: Guanting Dong, Xinyu Yang, Jiajie Jin, Yuyang Hu, Xiaoshuai Song, Yifei Chen, Xiaoxi Li, Jiejun Tan, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou (Gaoling School of AI, Renmin University of China), Tat-Seng Chua (NUS); code: https://github.com/RUC-NLPIR/Agent-Reflex; models & data: HuggingFace collection dongguanting/agent-reflex; category: cs.CL; PDF: https://arxiv.org/pdf/2610.17953; citation count: [NO DATA — published 2026-10-13]
