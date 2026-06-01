# [2605.26969v1] Recon: Reconstruction-Guided Reasoning Synthesis for User Modeling

## Problem
User modeling uses language models to mimic individual behavior from context-action pairs. Recent approaches augment corpora with synthesized reasoning traces, but conditioning on both context and action constitutes post-hoc rationalization rather than reasoning — the trace is guaranteed to justify the action but may not encode underlying latent causal decision paths.

## Contribution
1. **Recon framework**: Uses action reconstruction to score reasoning traces by predictive power. Given context + candidate reasoning → reconstruction model predicts action → reconstruction fidelity determines reasoning quality.
2. **Recon-Select**: Selects reasoning traces without training — 54.7% win rate over Backward Synthesis baseline.
3. **Recon-GRPO**: Trains reasoning synthesis model with rewards from Recon — up to 70.0% win rate. Reasoning transfers across models.

## Method (core summary)
3-step pipeline: (1) Sample N=4 candidate reasoning traces from reasoning model M_r, conditioned on context-action pair; (2) Reconstruction model M_a predicts action from context + candidate reasoning; (3) Score reasoning by alignment between predicted action and ground-truth action. Recon-Select: choose reasoning trace with highest reconstruction score. Recon-GRPO: use reconstruction score as reward signal for GRPO training of reasoning synthesis model. Key insight: useful reasoning must naturally elicit the action from context, not just justify observed action.

## Key Findings
- Recon-Select (Qwen3-8B): 54.7% win rate over Backward Synthesis
- Recon-Select (GPT-5-mini): 53.5% win rate
- Recon-GRPO: up to 70.0% win rate over baselines
- E2E-GRPO (optimize action accuracy only): 38.4% win rate — worse than baseline
- Consistent improvements across 4 domains, 8 individuals
- Recon-synthesized reasoning transfers across models
- Human validation: 77% agreement with LM judge, Cohen's kappa 0.623

## Actionable Insights
1. **Post-hoc rationalization ≠ reasoning**: When generating reasoning traces for AI agents, do NOT just justify observed actions. Reasoning must have predictive power — must predict action from context. Example: when training AI to mimic customer behavior, reasoning "customer bought because they liked the color" is rationalization. Useful reasoning: "customer typically buys items matching their style preference, and color X matches → predict purchase."

2. **Reconstruction fidelity = reasoning quality metric**: Use reconstruction to evaluate reasoning quality. Given context + reasoning → predict action → if prediction correct → reasoning has quality. Example: when evaluating AI advisor's reasoning, test: given context + reasoning → can it predict user's decision? If not → reasoning has no causal power.

3. **Reasoning quality > action accuracy**: Optimizing for action accuracy alone (E2E-GRPO) produces WORSE reasoning (38.4% win rate). Must optimize for reasoning quality via reconstruction. Example: when training AI sales agent, don't just optimize conversion rate — optimize reasoning quality by testing: does reasoning predict customer behavior?

## Assumptions & Limitations
**Conditions for method to work:**
- Need corpus of context-action pairs from target user
- Reconstruction model must be capable enough to predict actions
- Reasoning traces must be conditioned on ground-truth action (limitation acknowledged)

**Limitations the paper acknowledges:**
- Only evaluates in user simulation setting — 8 individuals, 4 domains
- Recon-GRPO limited to single domain
- Additional computational cost: Recon-Select needs 2N+1 LM calls
- Still operates on rationalizations conditioned on ground-truth action

**Limitations the paper does NOT mention:**
- 8 individuals too few for generalization claims
- 4 domains specific — not tested on diverse user types
- LM judge bias — Gemini-3.1-Flash-Lite may have systematic preferences
- Not tested with very large models (>70B)
- Reconstruction model quality limits upper bound
- No privacy implications addressed for user behavior modeling

## Metadata
- Year: 2026
- Authors: Alan Zhu, Mihran Miroyan, Carolyn Wang, Andrew Zhou, Lisa Dunlap, Narges Norouzi, Joseph E. Gonzalez
- Category: cs.CL, cs.AI
- PDF: https://arxiv.org/pdf/2605.26969v1
- Citation count: [EXTRACTION FAILED]
