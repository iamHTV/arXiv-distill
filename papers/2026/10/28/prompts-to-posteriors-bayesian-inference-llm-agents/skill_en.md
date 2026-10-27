# Skill: Bayesian Belief-Update Audit for LLM Agents
Source: 2610.29331 (From Prompts to Posteriors)
Type: evaluation-method

## When to use this skill
- Before trusting an LLM agent to accumulate evidence over multiple turns: forecasting, diagnosis, operations monitoring, scientific discovery.
- When you plan to replace a strict harness (a rigid external framework à la BED-LLM that fixes the probabilistic model outside the model) with the LLM's own updates.
- Do NOT use: single-shot classification with no evidence accumulation; truly open hypothesis spaces where no likelihood model can be specified (then no oracle can be built).

## Inputs needed
- A finite hypothesis space Θ (or a manageable dynamic subset Θ_k), an externally fixed prior p0.
- A likelihood model p(y|θ,ξ) — start with a simple closed-form version; prepare a Monte Carlo estimator for the hard variant if needed.
- An experiment space Ξ and a horizon T (number of update steps, e.g. 6–20).
- The same LLM in 3 configurations: no reasoning, reasoning mode, reasoning + code-execution tool.

## Steps
1. Elicit ALL probability judgments within a SINGLE dialogue — never ask scattered questions across sessions and stitch results (cross-conversation Dutch-bookable >50% of scenarios vs 0–10% within-dialogue).
2. Self-check the three Kolmogorov axioms on ≥10 scenario sets: normalization (N — probabilities sum to 1), monotonicity (M — nested events have monotone probabilities), extensionality (E — consistent judgments under equivalent phrasings). Any violation → outputs are unusable as a distribution; stop the audit.
3. Run the sequential loop for T steps: choose experiment ξ_k → observe outcome y_k → update posterior p^LLM_k. In parallel compute the oracle trajectory p^ora-pas via Bayes' rule (Eq. 1) with the same prior and the same outcomes.
4. Compute posterior fidelity: forward KL(p^ora-pas ∥ p^LLM) per step (clip p^LLM below at 1e-6, then renormalize). Use forward KL — NOT reverse KL — to penalize early discarding of still-valid hypotheses.
5. Compute the downstream gap: posterior-mass gap = p^ora-act(θ*) − p^LLM(θ*) (mass on the true hypothesis hidden by the environment). This is the end-to-end measure, less influenced by environment hardness than absolute accuracy.
6. Escalate interventions in 3 rungs, re-measuring steps 4–5 at each: (a) base; (b) enable reasoning mode; (c) add a code-execution sandbox. Decision: reasoning+tools with KL ≈ 0 and gap ≈ 0 → drop the strict harness, but keep an explicit belief state persisted to a database for cross-conversation coherence and human inspection; still high → keep the harness.
7. Audit the code output at rung (c): reasoning models recognize intractable likelihoods but will hallucinate simulation output without a real tool — verify the code contains a numerically stable estimator, don't just read the model's reported numbers.

## Expected output
- A table of per-step KL divergence + posterior-mass gap for the 3 intervention rungs; a verdict: "posterior updates trustworthy" (reasoning+tools pass) or "harness required" (fail); a list of axiom violations if any.

## Example application
- Customer-churn monitoring agent: build a synthetic world of 8 customer segments with latent attributes and 6 measurements; run the 6-step audit → base: large KL + gap −30%; reasoning: small KL; reasoning+sandbox: gap ≈ 0 → production: the churn agent stores a posterior table over the 8 segments in a database, updates weekly with a code sandbox computing posteriors, and operators read the belief state directly.

## Gotchas
- Do NOT stitch probability judgments from separate conversations — >50% of scenarios become Dutch-bookable.
- Non-reasoning models collapse to ~0% on open 20Q-style tasks — don't conclude "model is bad" without reasoning enabled.
- Reasoning-only on intractable likelihoods: the model reports MC numbers but actually fabricates them — require real code execution.
- 20Q-style setups: the oracle uses the LLM's own declared likelihoods → the audit measures internal consistency, not correctness against the world.
- Fixed compute budget when comparing base vs reasoning: base gets exactly the tokens needed to output probabilities, no free compute — without this control the comparison is biased.
