# [2605.31518v1] Activation Outliers and Feature Death in Sparse Autoencoders

## Problem
Sparse Autoencoders (SAEs) decompose neural network activations into interpretable features, but many learned features never activate — called feature death. Death rates vary dramatically between models: near-zero on GPT-2, over 70% on AlphaFold3 with identical configurations. Prior work does not explain why and when feature death occurs, and whether mean-centering is necessary.

## Contribution
1. **Identifies root cause**: Dimension-level activation outliers cause feature death by shifting pre-activations at initialization. Features anti-aligned with the mean receive permanently negative pre-activations and never fire.
2. **Metric γ predicts death**: Formalizes outlier severity as γ = ||μ||/||σ|| — predicts initial death rates with Spearman ρ = 0.89 (dead-by-TopK), 0.82 (dead-by-ReLU) across 454 model-layer combinations.
3. **Mean-centering eliminates death**: Initializing SAE bias with geometric median eliminates outlier-induced death across all tested models.

## Method (core summary)
Geometric analysis: pre-activation z_i = w_i · x + b. If activations have mean μ ≠ 0, shift term w_i · μ shifts pre-activation. Features anti-aligned with μ receive large negative shift → never activate. Formalizes severity γ = ||μ||/||σ||. Dead-by-ReLU: feature dies when shift too negative, no input pushes pre-activation > 0. Dead-by-TopK: feature dies when cannot rank in top-k. Fix: initialize bias = geometric median of activations → shift term cancels, all features centered around zero. Geometric median more robust than arithmetic mean with 50% breakdown point.

## Key Findings
- γ predicts death rates: Spearman ρ = 0.89 (dead-by-TopK), 0.82 (dead-by-ReLU) across 454 model-layer combinations spanning language, vision, protein, genomic models
- Mean-centering achieves near-zero death on synthetic data (γ=40): from 75-90% dead → 0%
- ESM3 layer 24 (γ≈8): baseline 75% dead → mean-centering near zero
- Mean-centered SAEs match 4× larger baseline on concept recovery and are more monosemantic
- Geometric median vs arithmetic mean: on 4 models with outlier tokens, AM centering WORSE (91.7% dead on DINOv3-B), GM centering 0% dead
- Dead features revive during training but prohibitively slow at high γ: γ≥30 plateau 75-90% dead even after 2M steps

## Actionable Insights
1. **Always mean-center when training SAEs**: Initialize encoder bias with geometric median of activations — zero runtime cost, eliminates feature death. Example: when training SAE for production model, compute geometric median on 500-token calibration set, set bias = GM. Simple but eliminates 70%+ dead features.

2. **Use γ to diagnose before training**: Compute γ = ||μ||/||σ|| on activation distribution. If γ > 10 → expect high death rate, mean-centering mandatory. If γ < 5 → centering optional. Example: before deploying SAE interpretability pipeline, check γ per layer — layers with high γ, prioritize centering.

3. **Geometric median more robust than arithmetic mean**: When outlier tokens exist (attention sinks, register tokens), arithmetic mean gets inflated → centering反而 worse. Use geometric median (50% breakdown point). Example: vision transformers often have register tokens with extreme norms — use GM, not AM.

## Assumptions & Limitations
**Conditions for method to work:**
- Feature death must be caused by activation outliers (not other training instability)
- SAE must have bias terms to learn offset
- Need calibration set (500 tokens) to compute geometric median

**Limitations the paper acknowledges:**
- Analysis focused on initialization-time death; training dynamics more complex
- Low-rank activation layers need additional PCA whitening, not just mean-centering
- Geometric median computation adds small overhead (Weiszfeld's algorithm)

**Limitations the paper does NOT mention:**
- Not tested on very large models (>70B) — unclear if γ still predicts at large scale
- No discussion of interaction between mean-centering and other SAE techniques (residual stream, cross-layer)
- Geometric median may converge slowly on very high-dimensional activations
- No address of feature death from other causes (e.g., dead gradients, learning rate issues)

## Metadata
- Year: 2026
- Authors: Elana Simon, Etowah Adams, James Zou
- Category: cs.LG
- PDF: https://arxiv.org/pdf/2605.31518v1
- Citation count: [EXTRACTION FAILED]
