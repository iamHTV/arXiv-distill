# Skill: Attention-Handoff Tax — Measure the curve + handoff tax, choose single vs multi-agent
Source: 2610.06069v1 (Attention Tax, Handoff Tax)
Type: evaluation-method (architecture selection rule)

## When to use this skill
- Deciding whether to split a task into a multi-agent chain (decomposition) or run a single agent; or choosing the chunk size (steps per subagent); or choosing parallel sampling vs thinking longer at equal budget.
- The task is a chain of steps with accumulating context (ledgers, tool chains, document processing pipelines, multi-hop research).
- Do NOT use when: the task is a single call with no accumulating context; the task has directly verifiable answers (code, simple arithmetic); you cannot run a single agent as a baseline.

## Inputs required
- Task definition: step structure, tokens added per step k, task statement size c0.
- A fixed model + serving config (per-step budget b, temperature).
- A budget of ~100–200 instances and ~1,000 calls for measurement.
- (Optional) A summary schema for handoff notes.

## Steps
1. Measure the in-task curve: run the single agent (one growing conversation) on N instances at several context-load bins (e.g. 2k/8k/32k/64k tokens, padded with well-formed digit-free prose); record the per-step failure rate vs load. CAUTION: define failure first — arithmetic vs format definitions give different curves (the pilot: flat 5.5% vs steep 29.5% on the same 1,000 calls).
2. Measure the handoff tax per Definition 1: on a separate pool, run each chunk twice — (a) continued from history, (b) started from a summary note; add back the curve term Σ[g(c0+|H|+ki) − g(c0+s+ki)] → h = G_M − G_H + curve term. Repeat at 2–3 note lengths (the tax must be nonincreasing in s).
3. Fit the curve: linear regime (g = g0 + λc) or knee-shaped (hinge fit). If flat over the measured range → the single agent dominates (Corollary 1) — stop, do not decompose.
4. Compute the crossover depth (linear regime): L* = max{2, ⌊2(h+λs)/(λk)⌋+1}. Task depth < L* → single agent; > L* → decomposed.
5. Choose chunk size: m* ≈ √(2h/(λk)) (linear regime, with h including the writer overhead ∆o). Knee-shaped curve: agents own as many steps as fit under the knee; the square-root law only applies past the knee.
6. Choose summary length: an interior optimum at −h′(s*) = λ — do not use blind fixed-ratio compaction.
7. Parallel vs sequential (if the task allows N samples per step): measure the marginal failure ε_b and the pairwise correlation ρ between samples; compute F_max = ρε(1−ε)/(ρε(1−ε)+(½−ε)²); if F_max < ε∞(c) (the thinking floor) → parallel sampling wins for large N at equal budget.
8. Validate: run the prediction (exp(−G) per instance, product form) against observed success at 2–3 depths; predictions should miss by ≤ ~9 points (the single-agent side tends to land a few points above the prediction because failures cluster on hard instances).

## Expected output
- A concrete decision rule: single agent up to depth X, decomposed with chunk size m beyond it; predicted success rates for both systems at the depths you plan to deploy; the handoff tax in nats with a CI.

## Example application
- A solopreneur document-processing pipeline: the measured curve shows failure 3% (<8k tokens) → 60% (>32k); the measured handoff tax is 0.03 nats with 300-token notes; k = 400 tokens/step, λ = 8×10⁻⁶ per token, s = 300 → L* = max{2, ⌊2(0.03+0.0024)/0.0032⌋+1} = 21. Documents needing >21 processing steps → decompose with m ≈ √(2·0.03/0.0032) ≈ 4–5 steps per agent; shorter → one agent.

## Gotchas
- The failure definition is part of the curve — arithmetic failure can be flat while format failure (a missing ANSWER line) is steep: 47/51 format failures at 64k still had the right number. Repeat the instruction next to the question to flatten it.
- Fee steps (or any step whose grading depends on carried-in state) measure the state, not the step — exclude them from curve fitting, but still count their context growth.
- The product form overstates the single agent's loss when failures cluster on hard ledgers — the observed single agent often lands a few points above the prediction; don't be surprised.
- The handoff-tax bootstrap CI can include negative values (measured [−0.11, 0.16] nats) — per Assumption 4, project negatives to zero.
- Under a knee-shaped curve the chunk size is NOT the square root — agents own the steps under the knee first.
- The crossover prediction is tested on the winning side (depths > L*); the crossover depth itself needs more measurement if your task depth sits near L*.
- The vote floor depends on the whole mixing law, not just ρ — (ε_b, ρ) gives only a bound, not the exact floor; the common-shock floor ρε is one example.
- Temperature + a fixed budget affect the curve — keep the serving config identical between measurement and production.
- The handoff-note content is a design choice: balance + open holds + last-12-transactions in the paper; a different schema → a different tax.
- Million-step ambitions (L = 10⁶) require both the per-step vote failure and the handoff tax to be ~10⁻⁶ → pass the FULL STATE, not a summary (Corollary 4).
