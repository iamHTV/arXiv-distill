# Skill: Tool-Augmented Generation — Fetch Features On Demand While Generating
Source: 2610.26831 (AGR)
Type: framework

## When to use this skill
- Retrieval/recommendation systems that generate IDs, where quality depends on external features (user history, freshness) that are too costly to stuff into the input.
- An agent must decide per step whether to fetch data and what to fetch.
- Do NOT use when features are few, fixed, and cost is a non-issue — static injection is simpler.

## Inputs required
- Item corpus with learned hierarchical Semantic IDs (SIDs, via residual quantization).
- A tool set: each tool = function f(query, user, context) returning a discrete value (categorical features, behavioral sequence summary, query/user features).
- Quality logs to compute information gain per fetch.

## Steps
1. Extend the vocabulary: V = S ∪ T ∪ O — add tool tokens and observation tokens; each tool token triggers a function call whose result becomes an observation token.
2. Build training trajectories along the SID hierarchy, marking a fetch whenever a feature has applicability and positive information gain (e.g., reduces ΔPPL).
3. Pretrain the model on SID generation (no tools) to convergence.
4. Tool-augmented fine-tuning: the model learns when to emit a tool token, which feature, and how the observation shapes the next tokens.
5. Inference: decode beam by beam; the model emits a tool token when needed → call the tool → continue decoding with the observation token.

## Expected output
- A model that generates SIDs with on-demand feature fetches: higher Recall/MRR than static baselines, far lower serving cost than stuffing all features (AGR: −42.9% serving, −81.8% training time vs direct encoding).

## Example
- Short-video recommendation: the model generates item SIDs; when the prefix signals a new (cold) user, it emits a tool token fetching "freshness + trending" features instead of sending a 400-token full history → Recall@50 comparable (0.3237 vs 0.3241) at 4.76 vs 8.33 GPUs/1K requests.

## Gotchas
- Rules-based trajectory supervision caps performance — consider agentic RL with sparse rewards.
- Building trajectories on golden SID prefixes creates exposure bias — the model never learns to recover from a wrong prefix.
- Check the serving budget: tool calls cost ~2× the no-feature baseline — must fit the latency budget (AGR: 35ms).
