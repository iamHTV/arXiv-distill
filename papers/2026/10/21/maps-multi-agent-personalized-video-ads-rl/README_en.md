# [2610.25748v1] MAPS: A Multi-Agent Personalized Script-Driven Video Advertising System Enhanced by Reinforcement Learning

## Core Value (1 sentence)
MAPS (Multi-Agent Personalized Script-driven video advertising system enhanced by Reinforcement Learning) — a 4-agent system (Profile, Scripter, Director, Reflector) that generates personalized video ads on demand, improving CTR +2.87%, CVR +2.74%, ARPU +9.85% over generative baseline in live A/B testing at Kuaishou.

## Problem
Prior work on personalized video advertising uses retrieval-based paradigm (pre-produced creative pool, then retrieve), limiting personalization granularity and causing performance disparities across user groups; user feedback can only inform subsequent production cycles, with no mechanism for real-time optimization of currently deployed creatives.

## Contribution
1. Propose MAPS, a 4-agent collaborative system (Profile, Scripter, Director, Reflector) transforming personalized video advertising from static retrieval over discrete creative inventory into dynamic generative optimization in continuous creative space.
2. Build RL framework (based on GRPO) with multi-dimensional reward function for Scripter Agent, steering scripts to align with user content preferences and target product information simultaneously.
3. Closed-loop creative evolution mechanism via post-deployment online user feedback: Reflector Agent attributes interaction signals to profile-level and script-level causes, routes minimal revisions back to Profile and Scripter Agents.
4. Offline experiments on PCG-Bench and PCI-Bench benchmarks, plus online A/B testing in Kuaishou advertising system, showing significant CTR/CVR/ARPU improvements.

## Method
MAPS comprises 4 collaborative agents: (1) Profile Agent (Qwen3-VL-32B-Instruct) builds structured user profiles from historical interaction data and real-time contextual signals, across 4 dimensions (topical interests, preferred presentation styles, implicit needs, decision-making tendencies), continuously refined as new observations accumulate; (2) Scripter Agent (Qwen3-VL-8B-Instruct) generates personalized advertisement video scripts conditioned on user profile and product attributes, trained in two stages: SFT (LoRA rank 32, AdamW LR 1.0e-5, batch 4, max seq 8192, 20 epochs) then RL (GRPO, KL coeff 0.04, AdamW LR 1.0e-6, batch 4, 5000 steps) on 8 NVIDIA H100 GPUs; (3) Director Agent (Kling-Omni) converts structured scripts into deliverable video creatives with product visual assets as grounding constraints; (4) Reflector Agent (Qwen3-VL-32B-Instruct) attributes online user interaction signals (play duration, likes, comments, purchases) to profile-level and script-level causes, routes minimal revision directives back for iterative refinement. Combined reward function: Rtotal = 0.3·Rstruct + 0.4·Rpers + 0.3·Rprod, where Rstruct checks format compliance/script completeness/scene-character consistency/physical rationality, Rpers uses LLM-as-a-Judge for presentation style + content preference alignment (0–10 scale), Rprod uses LLM-as-a-Judge for product identity/brand elements/selling points factual consistency (0–10 scale). Qwen3-VL-32B-Instruct serves as judge. GRPO samples K candidate scripts per input, computes normalized advantage within group, updates policy with KL-divergence penalty.

## KNOWLEDGE — Data & Concepts
- 4 agents: Profile (Qwen3-VL-32B-Instruct), Scripter (Qwen3-VL-8B-Instruct), Director (Kling-Omni), Reflector (Qwen3-VL-32B-Instruct)
- Scripter training: SFT LoRA rank 32, AdamW LR 1.0e-5, batch 4, max sequence length 8192, 20 epochs; RL GRPO KL coeff 0.04, AdamW LR 1.0e-6, batch 4, 5000 training steps; 8 NVIDIA H100 GPUs
- Reward function: Rtotal = 0.3·Rstruct + 0.4·Rpers + 0.3·Rprod; Rstruct: Format Compliance, Script Completeness, Scene & Character Consistency, Physical Rationality; Rpers: LLM-as-a-Judge on presentation style alignment (tone/lighting/texture/artistic) + content preference alignment (subject matter/scene semantics/information angle/motivational appeal); Rprod: LLM-as-a-Judge on product identity accuracy + brand/recognition elements + selling points factual consistency (0–10 scale)
- GRPO group sampling: K candidate scripts per input, normalized advantage Ak = (Rk − R̄)/(σR + ε), KL penalty to prevent large deviation from SFT initialization
- Offline evaluation (PCG-Bench, PCI-Bench): 50 users × 5 products = 250 user-product pairs, product library of 18 products; MAPS ranks first on all metrics on both benchmarks; Personalization 8.85, Product Alignment 9.78, Diversity 7.30; full MAPS improves personalization +1.25 points and product alignment +1.04 points vs variant without SFT and RL
- Online A/B testing (Kuaishou advertising system): vs DLRM → CTR +4.88%, CVR +4.01%, ARPU +12.89%; vs GRM → CTR +2.87%, CVR +2.74%, ARPU +9.85%

## INSIGHT — Mechanism & Why
[Shift from retrieval to on-demand creative generation] BECAUSE [static creative inventory cannot keep pace with rapidly evolving user preferences, while MAPS generates new creative per impression fitting each user and product]. This means [commercial value comes from generating native creative tailored per user, not just better matching].
[Multi-dimensional reward avoids trade-off between personalization and product alignment] BECAUSE [Rpers and Rprod have balanced weights (0.4 and 0.3), Scripter is guided to optimize both simultaneously rather than trading one off against the other]. This means [multi-agent collaboration enables global optimization across competing objectives].
[Reflector Agent enables closed-loop creative evolution] BECAUSE [online feedback is attributed to profile-level or script-level causes, minimal revisions are routed back instead of regenerating the entire creative]. This means [continuous adaptation without re-running the full pipeline from scratch].

## IDEA — Actionable Applications
1. Apply [4-agent multi-agent framework] to [building personalized video ad creative generation system]: first step is to deploy Profile Agent to extract user profiles from historical interaction data, then add Scripter Agent to generate scripts conditioned on profile and product.
2. Apply [GRPO with multi-dimensional reward function] to [guiding LLM content generation toward multiple objectives]: first step is to set up 3 reward components (structure, personalization, product alignment) with weights 0.3/0.4/0.3, use LLM-as-a-Judge for scoring.
3. Apply [Reflector Agent online feedback loop] to [deploying continuously adaptive creative system]: first step is to collect interaction signals (play duration, likes, comments, purchases) after each impression, attribute to profile/script causes, route minimal revisions back.

## WISDOM — General Principles
1. Principle: On-demand creative generation delivers greater commercial value than matching from a fixed inventory, because it opens a continuous creative space rather than being limited to static inventory. Apply when: building personalized advertising or content systems with large product inventory. Do not apply when: generation cost is too high relative to personalization benefits.
2. Principle: Multi-agent with closed-loop feedback (profile → script → creative → feedback → profile) outperforms single-agent systems because each agent specializes in one aspect and feedback loops continuously improve. Apply when: need system adapting to evolving user preferences over time. Do not apply when: task is simple and doesn't need deep personalization.

## Assumptions & Limitations
- Conditions that must hold: historical user interaction data available, product visual assets (images, logos) available, GPU resources (8 H100), video generation model (Kling-Omni) and MLLM (Qwen3-VL) available.
- Limitations acknowledged by paper: online experiments only in one specific scenario in Kuaishou advertising system; future work will explore finer-grained online feedback modeling and long-horizon creative evolution in larger-scale scenarios.
- Limitations paper does NOT mention: actual inference cost vs retrieval-based; time to generate creative per impression; scalability as users and products grow; no comparison with other multi-agent systems beyond DLRM and GRM baselines.

## Metadata
- Year: 2026
- Authors: Zhongyu Wang, Chen Zuo, Qingxuan Sun, Jiayang Qiao, Qiuhao Qian, Songyan Cui, Guocheng Chen (Beihang University, Kuaishou Technology)
- arXiv Category: cs.IR
- PDF Link: https://arxiv.org/pdf/2610.25748
- arXiv ID: 2610.25748v1
- Label: [applied]
- Citation count: [not found]