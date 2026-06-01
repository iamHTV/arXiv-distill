# Skill: SAE Mean-Centering Fix for Feature Death
Source: 2605.31518v1
Type: workflow

## When to use this skill
- When training Sparse Autoencoders (SAEs) and encountering feature death
- When wanting to improve SAE interpretability without increasing model size
- When deploying SAEs on production models and needing to maximize feature utilization

## When NOT to use
- Model activations already pre-processed with normalization
- SAE does not have bias terms
- Activation distribution is already zero-mean naturally

## Required inputs
- Pre-trained model to interpret
- SAE architecture with bias terms
- Calibration set: 500 tokens from model activations
- Compute: sufficient to run SAE training

## Steps

### Step 1 — Compute γ
1. Forward pass 500 calibration tokens through model
2. Extract activations at target layer
3. Compute mean μ = E[activations] and std σ = std(activations)
4. Calculate γ = ||μ|| / ||σ||
5. If γ > 10 → mean-centering MANDATORY. If γ < 5 → optional

### Step 2 — Compute Geometric Median
1. Use Weiszfeld's algorithm on 500 calibration tokens
2. Iterative: start with arithmetic mean, iterate: μ_GM = Σ(x_i / ||x_i - μ||) / Σ(1 / ||x_i - μ||)
3. Converge when ||μ_new - μ_old|| < ε
4. Output: geometric median μ_GM
5. Do NOT use arithmetic mean if outlier tokens exist (attention sinks, register tokens)

### Step 3 — Initialize SAE Bias
1. Set encoder bias b_enc = μ_GM
2. Mathematically equivalent to runtime centering but zero overhead
3. Pre-activation: z_i = w_i · (x - μ_GM) + b_enc → shift term cancels
4. All features centered around zero, vary only by input content

### Step 4 — Verify
1. Train SAE with centered initialization
2. Check death rate: should be < 5% (vs baseline 70%+ if γ high)
3. Compare feature quality: monosemanticity, concept recovery
4. If death rate still high → check if activations are low-rank → need additional PCA whitening

### Step 5 — PCA Whitening for Low-Rank Layers (if needed)
1. Compute effective rank of activation covariance
2. If effective rank < 2% of hidden dimension → mean-centering alone insufficient
3. Apply PCA whitening before training SAE
4. Alternative: Active Subspace Initialization

## Expected output
- Death rate drops from 70%+ → < 5%
- Feature quality improves: mean-centered SAE matches 4× larger baseline
- More monosemantic features
- Better concept recovery

## Example application
**Scenario**: Train SAE on production LLM to interpret internal representations. Layer 24 has γ ≈ 8, baseline 75% dead features.

**Application**:
1. Compute γ = 8 → mandatory centering
2. Extract 500 calibration tokens, compute geometric median μ_GM
3. Initialize SAE bias = μ_GM
4. Train SAE → death rate ~0% (vs 75% baseline)
5. Interpret features: recover biological concepts (ESM3 example) or language patterns (LLM example)
6. Deploy: same SAE size but 4× effective capacity

## Gotchas
1. **Arithmetic mean can be WORSE**: On models with outlier tokens (DINOv3, ModernBERT), AM centering → 91.7% dead. ALWAYS use geometric median
2. **γ threshold**: γ > 10 = mandatory, γ < 5 = optional, between 5-10 = recommended
3. **Low-rank activations**: If effective rank < 2% of hidden dim, mean-centering alone insufficient → add PCA whitening
4. **Runtime overhead**: Bias initialization = zero runtime cost. Geometric median computation only needed once on calibration set
5. **Cross-layer methods**: Mean-centering stabilizes effective capacity → helps transcoders and cross-layer feature dictionaries
6. **Training revival**: Dead features can revive during training but prohibitively slow at high γ → better to fix at init
