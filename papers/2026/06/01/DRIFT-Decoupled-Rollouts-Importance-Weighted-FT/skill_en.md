# Skill: DRIFT — Multi-Turn Optimization with Importance-Weighted SFT
Source: 2605.31455v1
Type: workflow

## When to use this skill
- When training multi-turn AI agents with correction feedback
- When needing RL-level performance with SFT-level efficiency
- When repeated online rollouts are too expensive

## When NOT to use
- Open-ended dialogue without clear correctness signal
- Stochastic or preference-based feedback
- Long-horizon planning (>10 turns)

## Required inputs
- Base LLM to fine-tune
- Reference policy — trained model
- Correction trajectories from reference policy
- Verifier function for correctness signal
- Training dataset

## Steps

### Step 1 — Generate Offline Trajectories
1. Freeze reference policy
2. Sample multi-turn correction trajectories from reference
3. Each trajectory: try → fail → fix → ... → succeed/fail
4. Record: actions, feedback, returns per trajectory
5. One-time generation — no repeated rollouts needed

### Step 2 — Compute Importance Weights
1. Derive return-based importance weights from KL-regularized objective
2. Higher weight = trajectory has better correction behavior
3. Exponential weighting: successful corrections get higher weight
4. Normalize weights for stable training

### Step 3 — Weighted SFT Training
1. Standard SFT loop but with importance-weighted loss
2. Trajectories with higher weight contribute more to gradient
3. Model learns to mimic successful correction patterns
4. Avoids distribution shift by using offline data

### Step 4 — Evaluate Multi-Turn Performance
1. Test multi@k metric: cumulative accuracy with k turns
2. Compare: DRIFT vs single-turn SFT vs multi-turn RL
3. Check: correction rate per turn — DRIFT expected higher in early turns
4. Verify: training efficiency comparable to SFT

## Expected output
- Multi-turn performance matching RL baselines
- Training efficiency comparable to SFT
- Higher correction rates in early turns
- Improved performance beyond training domain

## Example application
**Scenario**: Train AI coding assistant with multi-turn corrections. Limited budget — can't afford online RL.

**Application**:
1. Reference policy: existing code model
2. Generate trajectories: model tries code → fails test → fixes → passes
3. Weight: trajectories with successful fixes get higher weight
4. DRIFT training: weighted SFT on correction trajectories
5. Result: model learns to correct errors efficiently, matches RL performance

## Gotchas
1. **Verifier availability**: DRIFT needs clear correctness signal. Without verifier, importance weights are meaningless
2. **Short-horizon only**: Intended for 2-5 turn corrections. Long conversations need different approach
3. **Offline coverage limitation**: Can only upweight behaviors in collected trajectories. May miss novel strategies
4. **Reference policy quality**: Trajectory quality limited by reference policy. Better reference → better DRIFT
5. **Much faster than RL**: Training efficiency comparable to SFT — main advantage over online RL
6. **Multi-turn > single-turn**: Single-turn only improves turn 1. Multi-turn training essential for correction behavior
