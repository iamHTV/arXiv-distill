# Skill: LLM Shepherding Cost Optimization
Source: 2601.22132
Type: framework

## When to use this skill

- When needing to reduce LLM inference costs in production while maintaining high accuracy — especially when an SLM is capable but not accurate enough standalone
- When deployment has both LLM (API or self-hosted) and SLM (edge device, local server) — want to leverage both without paying full LLM cost per query
- When tasks are reasoning or code generation — a "hint" (prefix-style guidance) from the LLM is sufficient to guide the SLM

- Do NOT use when: only 1 model available (no LLM + SLM combo); tasks are open-ended generation (creative writing, summarization) where the "beginning" of the response doesn't contain key info; SLM too weak to utilize hints

## Input needed

- LLM access (API or self-hosted) with ability to set max_new_tokens
- SLM (local or edge) capable of following hints
- Training dataset with ground-truth answers to train hint predictor (at least 1K+ queries)
- Quality threshold τ — accuracy level to achieve
- Cost model: per-token pricing for LLM input/output

## Steps

1. **Oracle Analysis** — Run LLM and SLM on eval dataset. For each query, determine: (a) Can SLM solve it? (b) If hint needed, what's the minimum hint size n*? Label n* by evaluating SLM accuracy at 10% increments (0%, 10%, ..., 90%) of full LLM response. Select smallest n* achieving quality threshold τ.

2. **Analyze Hint Distribution** — Plot distribution of n* values. Typically: 80% of queries have n*=0 (SLM can solve), 20% span 10-90% (heavy-tailed). Determine class imbalance ratio to configure weighted sampling.

3. **Train Two-Stage Predictor** — (a) Stage 1: Binary classifier — hint needed? Input: query features (embeddings), Output: probability hint > 0. Use weighted sampling for class imbalance. (b) Stage 2: Huber regression — predict log(1+n*) for positive cases. Joint loss: λ·BCE + (1-λ)·Huber.

4. **Choose Deployment Mode** — (a) Proactive Shepherding: router predicts hint size BEFORE SLM runs → lower latency but needs accurate prediction; (b) Reactive Shepherding: SLM runs first, SLM response features used to predict hint → higher accuracy but adds one SLM inference.

5. **Deploy with Threshold** — At test time: predictor outputs hint probability p and hint size n. If p < threshold → no hint, SLM alone. If p ≥ threshold → request n-token hint from LLM, concatenate with query, SLM generates final response. Tune threshold to match target accuracy-cost tradeoff.

6. **Evaluate ACE** — Compute Accuracy-per-Cost Efficiency: ACE = (A_π - A_s) / (C_π - C_s) × (C_l - C_s) / (A_l - A_s). Compare ACE with routing and cascading baselines. Target: ACE > 1.5 on math, > 2.0 on code tasks.

## Expected output

- 42-94% cost reduction vs. LLM-only inference
- ACE 1.25-2.78 depending on task difficulty
- Cross-domain generalization: train on 1 domain, apply to another
- Negligible latency overhead (<10ms/query for hint predictor)

## Example application

Scenario: E-commerce company runs a customer support chatbot. Currently: each query calls GPT-4 ($0.03/query). Solution: (1) Deploy Llama-3.2-3B as local SLM; (2) Train hint predictor on 5K historical queries with labeled answers; (3) 80% of queries: SLM handles alone (free); (4) 20% complex queries: request 20-token hint from GPT-4 (~$0.002), SLM generates full response; (5) Total cost drops from $0.03 to ~$0.006/query (80% savings). Accuracy drop: <2%.

## Gotchas

- Large class imbalance: 80% no-hint → weighted sampling mandatory, otherwise classifier always predicts "no hint"
- Non-monotonic quality: adding hint tokens is NOT always better. Too many hints can confuse SLM. Tune max hint size carefully.
- Training label quality: if SLM accuracy is noisy (sampling variability), n* labels will be unreliable. Recommend 5-7 independent trials per query + majority voting.
- Cross-domain transfer works well for structured tasks (math, code) but not tested for open-ended tasks. Do NOT assume transfer works for text generation.
- Output token cost dominant: hint-based savings mainly from output tokens. If LLM pricing is input-heavy, savings are smaller.
