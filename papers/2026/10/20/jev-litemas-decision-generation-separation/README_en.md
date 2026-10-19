# [2610.21411v2] Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows

## Problem
- Prior work (MetaGPT, AgentNet, LAS) uses a generative LLM for EVERY operation in multi-agent workflows, including routing (selecting the next expert) and review (judging an intermediate artifact) — operations that only need a bounded decision (e.g., pick one expert ID or pass/escalate).
- Profiling three representative MAS frameworks (MetaGPT, AgentNet, LAS) on DeepSeek-V4-Flash: routing + review account for 31.7–43.5% of total generative-LLM tokens and 29.5–46.1% of latency. LAS alone: 40.4% (MATH) / 39.2% (MBPP+). Nobody addressed the two interface gaps when swapping these for a low-cost decision model: planning gap (no execution plan / handoff instructions) and review gap (no corrective feedback for repair).

## Contribution
- Capability-matched allocation principle: operations needing open-ended generation keep generative models; operations needing only a choice get a choice-based decision model (Jev).
- Jev-LiteMAS: (a) feedback-driven expert handoffs — Jev selects the next expert from the task + latest artifact + legal action set, with NO pre-generated trajectory; (b) Jev-gated LLM re-review — Jev screens artifacts against a rubric: pass → proceed without any LLM call, escalate → LLM reviewer returns verdict + corrective feedback, expert repairs and re-enters.
- Implemented on AutoGen with DeepSeek-V4-Flash and GPT-5 generative backbones, Jev as the decision model, Qwen3-1.7B-Instruct as the SLM baseline.

## Method (core)
- Shared state 𝑠𝑡 holds task, intermediate artifacts, feedback; per step: expert 𝑒𝑡 produces 𝑦𝑡 = 𝐺𝑒𝑡(𝑠𝑡−1), state update 𝑠𝑡 = 𝑈(𝑠𝑡−1, 𝑒𝑡, 𝑦𝑡).
- Routing: 𝑎𝑡 = 𝐽route(𝑠𝑡, 𝐴𝑡) ∈ 𝐴𝑡 (𝐴𝑡 = eligible experts ∪ {STOP}); the dispatched expert receives task + artifacts through the state.
- Review point: 𝑑𝑡 = 𝐽screen(𝑠𝑡) ∈ {pass, escalate}; on escalate: (𝑣𝑡, 𝑐𝑡) = 𝐺review(𝑠𝑡) (verdict + feedback); revision runs on state 𝑠𝑡 ⊕ (𝑣𝑡, 𝑐𝑡) and the new artifact is re-screened as a new artifact.

## Key Findings
- 4 benchmarks: MATH (math reasoning), MBPP+ (code generation), API-Bank (tool use), IDRBench I3 (interdisciplinary research-idea integration). 5 baselines: Single-Agent, MetaGPT, AFlow, AgentNet, LAS.
- vs LAS: generative-LLM tokens −17.5–54.6% (DeepSeek-V4-Flash) and −12.7–38.6% (GPT-5); accuracy differences −0.67 to +0.66 pp (DeepSeek), −1.34 to +0.67 pp (GPT-5); latency lower in 7 of 8 configurations, largest reductions IDRBench I3 DeepSeek −45.8% and API-Bank GPT-5 −50.2% (exception: GPT-5 MATH 30.04s vs 25.91s).
- DeepSeek: highest MBPP+ accuracy 85.33%; GPT-5 IDRBench I3 +0.67 pp vs LAS. MetaGPT higher on DeepSeek IDRBench I3 (82.67% vs 75.33%) but with substantially more tokens and API calls.
- Ablations: Jev Router vs LLM Router: +6.66/+0.67 accuracy points with −63.1%/−36.0% tokens; vs SLM Router (Qwen3-1.7B): +11.33/+4.94 points, −24.3%/−16.1% tokens; removing semantic feedback drops accuracy 75.33→57.33% (I3) and 66.29→57.30% (API-Bank) — grounding routing in substantive expert outputs prevents up to 18.0 points of accuracy loss.
- Robustness (error injected into one random expert's artifact, DeepSeek): Attack-MAS accuracy 46.67%/39.33%, attack success rate (ASR) 50.00%/48.67%; Jev-LiteMAS: 94.00%/84.67% accuracy, ASR 3.33%/4.00%; vs MAS-Shield +2.67/+6.00 points with −11.2%/−14.0% tokens; vs Jev-LLM Judge similar accuracy with −24.3%/−23.5% latency; Multi-agent Debate best accuracy/ASR among protected configs but the most resource-hungry.
- Screening gate: Jev true-positive rate (TPR) 95.33% (MATH) / 91.33% (MBPP+) vs LLM judge 96.67%/92.00% vs SLM judge only 61.33%/44.67%; SLM has lower clean-case false-positive rate (FPR 0.00%/0.67% vs Jev 4.00%/6.67%) but much weaker detection — fewer false alarms ≠ reliable detection; Jev cuts clean-case tokens −29.4%/−24.2% and latency −37.6%/−28.0%.
- Decision-layer overhead: Jev adds only 1.13–2.21s per evaluation unit, 2.92–6.85% of end-to-end latency and 1.56–2.14% of model cost; overall latency 30.04–75.57s, cost $0.00664–$0.01766 per evaluation unit (GPT-5 experts).

## Actionable Insights
- Measure the token/latency share of routing and review before optimizing a multi-agent pipeline: if coordination exceeds ~30% (as profiled: 31.7–43.5%), moving coordination to a decision model is the single biggest saving → example: in a content pipeline writer→editor→SEO, replace "LLM picks the next step" with a small routing/classifier model.
- Use gated review instead of reviewing everything: screen artifacts with a decision model against a rubric; only escalate suspicious artifacts to an LLM reviewer → example: gate blog drafts against an editorial rubric, send only failures to the LLM editor — cuts ~25–30% of review tokens.
- The router MUST see substantive expert outputs (real artifacts), not just metadata: content-blind routing costs up to 18 accuracy points → example: when building an orchestrator, pass a summary of the latest artifact into the router prompt, not just step names.

## Assumptions & Limitations
- Conditions: expert pool and legal actions must be predefined; artifact quality distribution must skew toward "passing" for the gate to save (if most artifacts need repair, savings shrink).
- Limitations acknowledged: (1) no dynamic creation/reconfiguration of experts or roles for unseen tasks; (2) savings depend on artifact-quality distribution — adaptive review policies are future work.
- Limitations NOT acknowledged: template artifacts in the paper (CCS Concepts placeholder "Do Not Use This Code"; running header "Trovato et al." mismatching the actual authors Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li — Shanghai Jiao Tong University) → presentation quality is sloppy, reproducibility needs scrutiny; Jev is a proprietary model (arXiv 2609.37647) with unclear open weights.

## Metadata
- Year: 2026 (submitted 15 Oct 2026, v2 16 Oct 2026), authors: Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li (Shanghai Jiao Tong University)
- arXiv category: cs.AI, PDF: https://arxiv.org/pdf/2610.21411v2, license: CC BY 4.0
- Citation count: [NO DATA — paper <1 week old, Semantic Scholar rate-limited]
