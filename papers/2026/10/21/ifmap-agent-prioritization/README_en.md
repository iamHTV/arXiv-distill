# 2610.24383 IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems

## Problem
- Improving every agent in an LLM multi-agent system is prohibitively costly — which agent should be prioritized for the greatest system-level gain with limited resources? Failure attribution shows who is responsible for failures, but responsibility does not reveal the system-level gains achievable by improving that agent.

## Contribution
- IF-MAP: an influence-function-inspired method for identifying agents with high potential for system-level improvement.
- Per agent: measures end-to-end loss changes under controlled semantic prompt perturbations, fits a regularized local response model in a low-dimensional prompt-embedding subspace, and uses the estimated response norm as a priority score.
- Black-box: no access to model parameters or gradients.

## Method
- Each agent: at most 10 formal perturbations (static, adaptive, structure-preserving) that keep the agent's role and output interface; structural checks reject unusable or duplicate prompts.
- Each probe changes only agent i's prompt and runs the full system, so the response includes changes propagated through agent interactions.
- Signed effect Δ = L0 − L(m) (positive = improvement). A fixed embedding model E gives displacement v = E(p(m)) − E(p), direction u = v/||v||, and y = (L(m) − L0)/||v|| (loss change per unit embedding distance).
- Priority = norm of the estimated local response in the subspace.

## Key Findings
- 6 AFlow-derived workflows: HumanEval, MBPP (code), NQ (factoid QA), HotpotQA (multi-hop QA), DROP (discrete reasoning), MATH. Execution model Qwen3-8B; prompt operations DeepSeek-V3.2.
- Prompt optimization on selected agents: macro-average gain +3.81 percentage points vs +1.85 for uniform selection.
- Model upgrades (5 targets: Qwen3-32B, Qwen3-235B-A22B Instruct-2507, Qwen3.7-Plus, DeepSeek-V3.2, GPT-5 nano): macro-average gains +7.62 to +16.42 pp vs +3.81 to +8.62 for uniform. Qwen3-32B/235B/3.7-Plus panel: IF-MAP +12.52 pp (Kendall τ 0.775) vs best baselines Who&When-AAO/A2P +10.32 and uniform +6.57.
- Token use: Qwen3-8B −74.2% and DeepSeek-V3.2 −35.2% vs optimizing every agent; target-model tokens −63.6–64.9% vs upgrading every agent.

## Actionable Insights
1. Measure "potential to improve", not just "who caused failures". Example: in a 4-agent pipeline (triage, research, draft, verify), probe each agent with 10 prompt variants and upgrade the one with the highest response norm — roughly 2× the system gain of picking at random.
2. Black-box probing works without model weights. Example: API-only agents qualify — just run the system with prompt perturbations and measure the end-to-end metric.
3. Concentrate upgrade budget: upgrade one selected agent instead of all. Example: swapping in GPT-5 nano for exactly one agent yields +7.62–16.42 pp macro while saving 63.6–64.9% of target-model tokens.

## Assumptions & Limitations
- Realized gains depend on the embedding model, local linearity, probe coverage, and the alignment between available interventions and the fitted loss-reducing direction.
- Probing overhead: up to 10 probes per agent × full-system runs — still cheaper than optimizing every agent, but not free.
- The response direction is continuous — translating it into discrete improvements is future work (direction-conditioned generation, iterative edit-and-measure).
- Six AFlow-derived workflows — results may differ on custom workflows.

## Metadata
- 2026; authors: Jie Mao, Pingchen Lu, Zikun Qu, Jiahang Sun, Xiangyi Wang, Zhiwei Shang, Zhongxiang Dai (The Chinese University of Hong Kong, Shenzhen), Zhiyong Wang (Harbin Institute of Technology), Guojun Xiong (Harvard University); code: https://github.com/s1412/IF-MAS; categories: cs.AI, cs.MA; PDF: https://arxiv.org/pdf/2610.24383; citation count: [NO DATA — published 2026-10-17]
