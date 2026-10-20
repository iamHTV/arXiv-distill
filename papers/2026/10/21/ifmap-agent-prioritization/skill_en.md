# Skill: Prioritizing Agents for Improvement via Influence Probing (IF-MAP)
Source: 2610.24383
Type: evaluation-method

## When to use this skill
- A multi-agent system where the budget for upgrades/optimization is limited and you need to know which agent to invest in.
- You need a ranking by potential for system-level improvement, not just a failure ranking.
- Do NOT use for single-agent systems, or when every agent can be upgraded without cost concerns.

## Inputs required
- A fixed workflow plus an end-to-end metric or loss, and a representative probing set.
- A fixed embedding model for prompts.
- The ability to run the full system repeatedly (once per probe).

## Steps
1. Per agent i: create ≤10 semantic prompt perturbations (static/adaptive/structure-preserving) that keep the role and output interface; drop duplicates or unusable ones.
2. Per probe: change only agent i's prompt, run the full system, record loss L(m); compute the signed effect Δ = L0 − L(m).
3. Embed prompts: displacement v = E(p(m)) − E(p); direction u = v/||v||; y = (L(m) − L0)/||v||.
4. Fit a regularized local response model in a low-dimensional prompt-embedding subspace.
5. Priority score = the estimated response norm → rank agents.
6. Spend the budget on the top agents: prompt optimization or model upgrade — never upgrade every agent.

## Expected output
- A per-agent priority ranking plus the estimated macro-average gain from improving the top agents, compared against uniform selection as a baseline.

## Example
- A 4-agent customer-support pipeline (triage, research, draft, verify): probe 10 variants per agent (40 runs), IF-MAP ranks "draft" highest → upgrade only that agent's model: +9 pp macro (random selection +4 pp), saving ~64% of target-model tokens.

## Gotchas
- Poor probe coverage gives wrong priorities — perturbations must be diverse (static + adaptive + structure-preserving).
- The local-linearity assumption — agents with strongly nonlinear responses will be misestimated.
- Gains depend on available interventions: if you cannot upgrade that agent's model, the priority is meaningless — check alignment with the loss-reducing direction.
