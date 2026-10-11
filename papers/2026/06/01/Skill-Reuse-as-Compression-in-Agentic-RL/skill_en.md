# Skill: Skill Reuse as Compression for Agentic RL (ReuseRL)
Source: 2605.31509v1
Type: framework

## When to use this skill
- When training LLM agents with RL and want to improve generalization
- When agents learn task-specific shortcuts instead of reusable skills
- When you have many successful trajectories to extract common patterns from

## When NOT to use
- Tasks with no reusable substructure — each task completely different
- Not enough successful trajectories to build dictionary (at least 50+)
- Agent too small (< 1B parameters) or domain too large (alphabet > 100 atomic skills)

## Required inputs
- RL training environment with definable actions
- Rule-based skill mapping φ: action verbs → atomic skills
- Base RL algorithm (GRPO recommended)
- Successful trajectory buffer
- Hyperparameters: phrase length cap L=4, BPE merge threshold

## Steps

### Step 1 — Define Atomic Skill Alphabet
1. List all possible actions in the environment
2. Group actions into atomic skills Σ — each skill is 1 symbol
3. Example ALFWorld: {go_to, pick_up, put, toggle, open, look, inventory}
4. Mapping must be: small enough to capture reusable structure, large enough to distinguish behaviors

### Step 2 — Extract Skill Sequences
1. Run agent, collect successful trajectories (τ where R(τ)=1)
2. Apply φ mapping: τ → skill sequence s = φ(τ) ∈ Σ*
3. Store in global success buffer G (FIFO structure)
4. Combine current successful batch B+ with G into cluster T

### Step 3 — BPE Dictionary Extraction
1. Start with singleton phrases — each atomic skill = 1 phrase
2. Rank candidate pairs by frequency in T
3. Accept merge if: ΔBDL = L_BDL(T, C ∪ {p_a∘p_b}) - L_BDL(T, C) < 0
4. Cap phrase length at L=4
5. Terminate when no merge decreases MDL objective
6. Output: shared skill dictionary C

### Step 4 — Compute Segmentation Cost
1. For each successful skill sequence s: seg(s, C) = number of phrases needed to cover s using C
2. Segmentation cost = seg(s, C) / T (divide by trajectory length)
3. Lower = better (more reuse); Higher = worse (more idiosyncratic behavior)

### Step 5 — Augment GRPO Reward
1. Standard GRPO reward: r_outcome (binary)
2. Augmented: r = r_outcome - λ · seg_cost
3. λ = segmentation cost coefficient — tune on validation
4. EM-style: alternate between E-step (extract dictionary) and M-step (RL update)

## Expected output
- Agent learns reusable skill patterns instead of task-specific shortcuts
- Improved OOD generalization
- Reduced repeat actions and invalid actions
- Improvement: +5-13% on agentic benchmarks

## Example application
**Scenario**: Train AI agent to automatically handle IT support tickets. Agent needs: diagnose issue → search knowledge base → apply fix → verify → close ticket.

**Application**:
1. Atomic skills: {diagnose, search_kb, apply_fix, verify, escalate, ask_user}
2. Collect successful ticket resolutions, extract skill sequences
3. BPE merge: [diagnose, search_kb] → "investigate"; [apply_fix, verify] → "resolve"
4. Segmentation cost: agent uses "investigate → resolve → close" = 3 phrases = low cost = high reward
5. Agent learns generalizable workflow instead of memorizing specific ticket patterns

## Gotchas
1. **Rule-based φ limitation**: Manual mapping → needs redesign for each new domain. Trade-off: manual effort vs learned extraction (not yet explored)
2. **Greedy BPE approximation**: No guarantee of optimal dictionary. Gap grows with alphabet size — if |Σ| > 100, consider alternative heuristics
3. **Assumption 2**: Successful trajectories must share reusable structure. If domain is completely unstructured → segmentation cost degenerates to round-length penalty
4. **λ tuning**: Too high → agent over-compresses, loses fine-grained skills. Too low → doesn't enforce reuse
5. **Buffer size**: Global success buffer too small → unstable BPE. Too large → outdated patterns dominate. FIFO with appropriate capacity
6. **Compute overhead**: BPE merging per training step costs compute — cache dictionary if possible
