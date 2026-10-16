# Skill: TRACER — Trajectory-Aware Tool Retrieval (trie retrieval for agents)
Source: 2610.21267
Type: framework / retrieval-front-end

## When to use this skill
- An agent has a large tool registry (>50 tools) — exposing all of them costs tokens and impairs selection
- You have a history of successful trajectories (logged)
- Multi-step tool-call workflows with a logical order (prefix predicts next call)

Do NOT use: a small registry (<20 tools); no trajectory history (cold start → every step is vector fallback, −38 points); tool usage concentrated in generic utility tools (KB_search, grep) — use TRACER+G instead of plain TRACER.

## Input required
- A dataset D of graded trajectories (successful runs only; collapse each task to one canonical decision point)
- Registry tool descriptions
- A frozen embedder (e.g., text-embedding-3-small)
- An executor model (the LLM makes the final choice — TRACER is only a front-end)

## Steps
1. Trie construction: insert every prefix of every trajectory as a node; children C(Si) = tools observed immediately after Si. Each edge stores: (a) empirical prior P_trie(t|Si) = normalized transition frequency (log + smoothing ε), (b) edge memory m(Si→t) = mean-pooled embedding of the training contexts in which the transition was taken. The trie is turn-local (resets at turn boundaries); the edge memory embeds the FULL conversation (cross-turn).
2. Contextual prior: embed the step context (previous turns + step reasonings, DROP tool-call signatures) → R(t) = cos(embedding, m(Si→t)); ReLU-normalize into a distribution (uniform if all similarities ≤0); L(t) = log(R̂(t)).
3. Learned blend: s(t) = (1/T)[(1−w)L(t) + wP(t)]; w, T from a learned map over a 5-dim state feature vector (logistic head for w, floored softplus for T); fit with Adam + ℓ2 minimizing NLL of the gold next call, with inner-fold isolation (trie/edge memory built WITHOUT the trajectory's own data).
4. Confidence gate: unseen state (C(Si)=∅) or flat distribution (κ<τ=0.20) → global vector search over the full registry, replacing trie candidates.
5. Present top k (k=5 for ~128-tool registries; sweep {3,5,10,20,30} per domain) — the model chooses at the end.
6. (Optional) TRACER+G: if generic utility tools take a large share of calls → union the |G|=3 tools with the highest prefix entropy H(S|t) into every candidate set.

## Expected output
- Teacher-forcing: +4.7 points over full-registry (GPT-5.4, Mixed Tau2 Large, 61.9 vs 57.2), CIC −80% (2.8k vs 14.2k tokens per step); beats full-registry in 21 of 24 model-environment pairs (avg +6–10 points).
- Free-running: parity task success (58.3% vs 58.2%) with 23% of the tools, −61% per-step input tokens; +13.7–15.2 points for a weaker model (GPT-5.4-mini).
- Specificity trap 36.4%→16.4%; procedural ordering (unlock before write) enforced automatically.

## Example application
- A 128-tool e-commerce agent (order management, shipping, returns): prefix "find_user → get_order_details" → trie node children = {split_order_shipment, add_gift_message, request_return_pickup, schedule_installation...} instead of 128 tools; edge memory separates "order #W4821 invoice + separate addresses" (→ split_order_shipment) from "espresso machine installation" (→ schedule_installation). GPT-5.4 selects correctly 61.9% of the time with 2.8k tokens vs 57.2% with 14.2k tokens.

## Gotchas
- Cold start: without trajectory history every step is vector fallback — accuracy −38 points on average. Log successful runs before using.
- Free-running errors compound: a single early miss → unseen prefix → fallback; out-of-trie rate ~3× teacher-forcing. Mitigation (paper's future work): present the full registry on out-of-trie steps alone (+38 points, retain 84% of the reduction).
- Prefix-independent lookups (no prefix predicts them) are the weakest point — TRACER trails the full registry on those steps even under teacher-forcing.
- Generic-utility registries: plain TRACER underperforms (Tau3 Banking) — use +G; but +G hurts diverse registries (adds distractors). Detection: if a few tools take >50% of calls → enable +G.
- w is not constant: the contextual prior dominates on diverse tries (w≈0.02) but the empirical prior matters more early in the conversation — use the learned blend, don't hand-tune a constant (TRACER-fixed loses 0.6–8.0 points).
- Edge memory beats description matching: dropping edge memory (description-only) costs 21 points. Don't shortcut with tool-description similarity caching.
- Premise: every tool is available at every step — permission-gated registries violate this assumption.
- Trie key depth: full current-turn prefix; last-2 performs nearly identically (within SD) but 9.6% vs 12.4% out-of-trie — test both per deployment.
- Inner-fold isolation is mandatory when fitting the blend: using the trajectory's own data in the trie gives optimistic scores and breaks generalization.
