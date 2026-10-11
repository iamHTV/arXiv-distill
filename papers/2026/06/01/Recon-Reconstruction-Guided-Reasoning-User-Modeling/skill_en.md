# Skill: Recon — Evaluate Reasoning Quality via Action Reconstruction
Source: 2605.26969v1
Type: evaluation-method

## When to use this skill
- When evaluating quality of reasoning traces in user modeling
- When needing to distinguish post-hoc rationalization from real reasoning
- When training reasoning synthesis models for AI agents

## When NOT to use
- No context-action pairs available to evaluate
- Task is verifiable domain like math, coding — better metrics exist
- Reconstruction model too weak — cannot predict actions

## Required inputs
- Corpus of context-action pairs from target user
- Reasoning synthesis model (M_r) — generates candidate reasoning
- Reconstruction model (M_a) — predicts action from context + reasoning
- Evaluation metric: action alignment (compare predicted vs ground-truth)

## Steps

### Step 1 — Sample Candidate Reasoning
1. For each context-action pair (c, a*) in test set
2. Sample N=4 candidate reasoning traces from M_r
3. Conditioning: context + action → reasoning (post-hoc rationalization)
4. Output: N candidate reasoning traces r̂_1, ..., r̂_N

### Step 2 — Reconstruct Actions
1. For each candidate reasoning r̂_i:
   - Input: context c + reasoning r̂_i
   - M_a predicts action: â_i = M_a(c, r̂_i)
2. Measure alignment between â_i and ground-truth a*
3. Dimensions: style, intent, values
4. Output: reconstruction score per candidate

### Step 3 — Select Best Reasoning
1. Recon-Select: choose candidate with highest reconstruction score
2. Rationale: reasoning with predictive power = reasoning with causal power
3. Output: selected reasoning trace for each context-action pair

### Step 4 — Train with Recon Reward (if needed)
1. Recon-GRPO: use reconstruction score as reward signal
2. Train reasoning synthesis model M_r with GRPO
3. Reward = alignment between predicted action and ground-truth
4. Output: trained reasoning model with better quality reasoning

### Step 5 — Validate
1. Compare selected reasoning vs baseline (Backward Synthesis)
2. Win rate: what % of cases is selected reasoning better?
3. Human validation: 100 random pairs, check LM judge agreement
4. Target: >50% win rate = improvement

## Expected output
- Selected reasoning traces with higher predictive power
- Win rate: 54-70% over baseline
- Trained reasoning model (if using Recon-GRPO)
- Quality metric: reconstruction fidelity

## Example application
**Scenario**: Train AI agent to mimic customer behavior for market research. Agent needs to predict customer decisions from past interactions.

**Application**:
1. Corpus: customer context (browsing history, preferences) + action (purchase decision)
2. Generate N=4 reasoning traces: "Customer bought because X", "Customer preferred Y", etc.
3. Reconstruct: given context + reasoning → predict purchase decision
4. Select: which reasoning trace predicts best = best reasoning
5. Result: selected reasoning has predictive power, not just rationalization
6. Train: use Recon-GRPO to improve reasoning model → 70% win rate

## Gotchas
1. **Post-hoc rationalization is tempting but wrong**: Conditioning on both context + action → reasoning guaranteed to justify action but no causal power. ALWAYS test via reconstruction
2. **N=4 candidates sufficient**: 4 candidates per pair is sufficient for selection. More = more compute but diminishing returns
3. **Reconstruction model quality matters**: If M_a is weak → noisy reconstruction scores → poor selection. Ensure M_a is capable
4. **Transfers across models**: Good reasoning from Recon transfers to other models — useful for multi-model systems
5. **Compute cost**: Recon-Select needs 2N+1 LM calls per pair. Amortize over corpus lifetime
6. **Still conditioned on action**: Recon still uses ground-truth action to generate reasoning. Future: reasoning from context only
