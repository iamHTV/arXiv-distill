# [2609.14896v1] Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning

## Core value (1 sentence)
MODA (MOde-conditioned Diversity Alignment) is an online post-training RL algorithm that jointly optimizes generation quality and diversity: mode conditioning via abstract tokens in a single shared policy, where each mode acts as a MARL agent competing to produce distinct outputs, plus prompt-adaptive quality gating to prevent reward hacking.

## Problem
Prior work failed to solve mode collapse — the progressive loss of output diversity from LLM alignment training — which narrows a model's expressivity at inference time, limiting applications requiring open-ended exploration and pluralistic perspectives such as scientific ideation and creative writing.

## Contribution
- Introduces MODA, an online post-training RL algorithm that jointly optimizes quality and diversity, inspired by the coordination perspective in multi-agent reinforcement learning (MARL).
- Trains a single shared LLM policy conditioned on abstract numbered mode tokens, where each mode acts as an agent competing to produce outputs distinct from the others, encouraging exploration of complementary regions of the high-quality output space without hand-crafted personas or architectural modifications.
- Prompt-adaptive quality gating: calibrates quality thresholds against a frozen reference policy and grants diversity rewards only to responses meeting them, preventing reward-hacking behaviors such as language switching and verbosity.
- Evaluation on a comprehensive benchmark spanning seven general capability tasks and four domain-specific diversity tasks in scientific ideation and creative writing.

## Method
MODA uses mode conditioning: role identifiers are prepended to the system prompt; a shared policy πθ(y | zi, x) is conditioned on role identifier zi, with all roles sharing parameters θ. During training, each role generates one response for K prompts within the batch, forming a response group Yx = {yi,k}. Each response receives a Quality-Gated Diversity Reward with four components: quality reward, prompt-adaptive quality gate, response-level diversity score, and explicit reward-hacking penalties. The shared policy is optimized with Group Relative Policy Optimization (GRPO) with KL regularization to the base policy. Quality gate: quality score si = Sϕ(x, yi) from a reference reward model; threshold τq(x) = smin + α(smax − µref), σq(x) = γ(µref − smin + ϵ); binary gate g(x, yi) = 1[si ≥ τq(x)]; quality reward rqual = µ tanh((si − τq(x))/σq(x)). Diversity score: normalized semantic distance to the nearest alternative within the response group, d(x, yi, Y) = minj≠i (1 − ei⊤ej/2). Penalties: rlen (excessive length), rlang (language mismatch), rfmt (formatting/role-label leakage). Two inference modes: standard mode (no role identifier → single response, recovers base behavior) and diverse mode (multiple role identifiers → candidate set of diverse responses).

## KNOWLEDGE — Data & figures
- Mode collapse: progressive loss of output diversity from alignment training, narrowing model expressivity at inference time.
- MODA improves SBERT diversity 265% on Infinite-Chat held-out prompts while increasing general capability performance 10.3% over Qwen3-8B baseline.
- vs strongest DivPO baseline: SBERT diversity from 0.274 to 0.482 (+75.9%), E-Vendi from 2.86 to 4.4 (+53.8%), avg general capability pass@1 +7.0%.
- Thinking-disabled mode: SBERT diversity +155.5%, E-Vendi +94.0% over Qwen3-8B initial policy; avg pass@1 +10.3pp over initial policy, +7.0pp over strongest DivPO on general capability benchmarks.
- 100 responses to "Name a shade of blue": MODA produces 40 distinct shades, 122% more than Qwen3-8B initial policy, 150% more than SSoT.
- Training: verl codebase, vLLM inference, FSDP training, Qwen3-8B-Instruct base, 6 role-response pairs per prompt as a response group, GRPO, 10K training prompts (4:1 Tulu3-SFT-Mixture : Infinite-Chat mixture).
- Seven general capability benchmarks: GSM8K, MMLU, GPQA, BoolQ, HellaSwag, TruthfulQA, IFEval.
- Four domain-specific diversity benchmarks: HypoBench, PreScience, NoveltyBench, held-out split of Infinite-Chat.
- Diversity metrics: SBERT (semantic-level), E-Vendi (entropy-level), Discriminator (entailment-level).
- Code: github.com/yuanjiayiy/mode-conditioned-diversity-alignment
- arXiv category: cs.CL

## INSIGHT — Mechanism & why
[Mode collapse occurs after alignment] BECAUSE [RL optimizing expected reward concentrates the policy on a small set of high-reward responses, suppressing equally valid alternatives and reducing policy entropy]. This means [post-training algorithms must be redesigned to preserve expressivity by construction, not just intervene at inference time].
[MODA conditions multiple roles in one shared policy] BECAUSE [each mode acts as a MARL agent competing to produce distinct outputs, incentivizing agents to specialize in different regions of the high-quality response space]. This means [a single model can serve both single-response mode (no role token) and diverse mode (with role tokens), supporting both factual single answers and creative multi-idea generation].
[Prompt-adaptive quality gate prevents reward hacking] BECAUSE [diversity reward is granted only to responses exceeding a prompt-adaptive quality threshold computed from a frozen reference policy; unusual/off-topic/malformed responses get no diversity credit]. This means [diversity reward must not be used alone; it must be gated by quality to ensure diverse responses remain useful].

## IDEA — What to apply
Apply MODA to fine-tune a content-idea generation model for a small business: step 1 is to add abstract role tokens to the system prompt, train RL with quality-gated diversity reward to generate multiple distinct content ideas from the same prompt.
Use dual inference mode: no role token for single factual answers, role tokens for multiple ideas on creative tasks.

## WISDOM — General principle
Principle: Preserving output diversity is not about adding a standalone diversity reward, but combining mode conditioning (role conditioning) with prompt-adaptive quality gating; a single model can serve both single and diverse modes.

## Assumptions & Limitations
- Conditions for validity: tasks requiring multiple distinct high-quality outputs; a frozen reference policy available for quality threshold computation; GPU resources for GRPO training.
- Limitations acknowledged by the paper: evaluation mainly on Qwen3-8B plus Llama-3.1-8B and GLM-4-9B; not all larger model architectures evaluated; thinking-enabled vs thinking-disabled settings may yield different results.
- Limitations the paper does NOT mention: operational cost of GRPO training with 6 role-response pairs per prompt at scale; stability across repeated retraining as data mix changes; latency impact of generating multiple mode candidates at inference.

## Metadata
- Year: 2026
- Authors: Jiayi Yuan, Hangoo Kang, James Jihao Liu, Yejin Choi, Vikram Iyer, Liwei Jiang, Natasha Jaques (University of Washington, Stanford University)
- arXiv category: cs.CL
- PDF link: https://arxiv.org/pdf/2609.14896v1
- arXiv ID: 2609.14896v1
- Label: [applied]
- Skill: forty-shades-of-blue-moda | Test: [SKILL VALID]
