# Skill: End-to-End Ad Generation with Reinforcement Learning
Source: 2602.11780
Type: framework

## When to use this skill
- When generating ad text automatically that directly optimizes business metrics like CTR, CTCVR
- When current system uses two separate stages (generate → align) and you want to unify into end-to-end
- When needing to balance quality, diversity, and compliance in advertising

## When NOT to use
- No online feedback data from production system
- Low budget — RL training is more expensive than supervised fine-tuning
- Need real-time generation with strict latency constraints

## Required inputs
- Base LLM with basic fine-tuning
- Online feedback logs: CTR, CTCVR data from production
- Compliance rules: content policies list
- Training data: sample ad texts with metadata
- Evaluation metrics: quality, diversity, compliance, CTCVR

## Steps

### Step 1 — Define Reward Functions
1. **Quality reward**: Structural quality — length reward (check appropriate length), format reward (check format). Semantic quality — correctness, relevance (to product), risk-control (content safety)
2. **Diversity reward**: Reward ads different from historical ads — anti-text-fatigue
3. **CTCVR reward**: Conversion-oriented metrics directly from online feedback

### Step 2 — Design Credit Assignment Strategy
1. Sentence level: structural quality + CTCVR reward — reward for entire output
2. Token level: diversity + semantic quality constraints — reward for specific parts of output
3. Purpose: address reward sparsity and delayed feedback

### Step 3 — RL Training with GRPO
1. Algorithm: GRPO (Group Relative Policy Optimization)
2. Composite reward: r = w1·quality + w2·diversity + w3·CTCVR
3. Train model end-to-end: generation and alignment unified in single model
4. Monitor: compliance rate, diversity score, CTCVR convergence

### Step 4 — Online Deployment
1. A/B test: RELATE vs production baseline
2. Track metrics: CTCVR, compliance rate, diversity score, user engagement
3. Iterate: update reward weights based on online performance

## Expected output
- High-quality, diverse, compliant ad text
- Improved CTCVR over production baseline
- Reduced text fatigue via diversity reward
- Simpler end-to-end system vs two-stage approach

## Example application
**Scenario**: E-commerce platform wants AI to create product ads for Facebook/Google. Currently uses two stages: (1) LLM generates ad text, (2) ranker selects highest CTR ad. Problem: good ad text but low conversion, or repetitive causing fatigue.

**Application**:
1. Quality reward: check if ad mentions correct product features, correct Facebook/Google format
2. Diversity reward: reward ads different from last 100 ads for same product
3. CTCVR reward: direct reward from conversion data (after 7 days)
4. Credit assignment: quality check per sentence, CTCVR for entire ad
5. Train RELATE end-to-end → ads that are good, diverse, and convert

## Gotchas
1. **Cold start**: Needs sufficient historical data — if new launch, use SFT first then RL
2. **Reward model quality**: If reward model is wrong → policy is wrong → poor quality ads
3. **Latency**: End-to-end RL may have slower inference vs rule-based generation
4. **Compliance risk**: Model may learn to "cheat" reward — need robust risk-control reward
5. **Platform-specific**: Reward functions need customization per platform (Facebook vs Google vs TikTok)
6. **Data freshness**: CTCVR data needs frequent updates — stale data → suboptimal policy
