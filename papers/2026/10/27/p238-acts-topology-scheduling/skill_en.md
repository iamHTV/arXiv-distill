# Skill: ACTS — Role-Aware Communication Topology Scheduling for Agent Teams
Source: 2610.25851
Type: framework (multi-agent communication scheduling)

## When to use this skill
- You have a team of 3+ LLM agents (writer/editor/reviewer/researcher...) currently using full-mesh debate or a fixed broadcast chain → high token cost, accuracy not matching the spend.
- You want to design "who talks to whom and when" by role + evolving state instead of all-to-all chat every round.
- You measure cost-per-task of agent teams and need to optimize accuracy-per-token, not raw accuracy.

## When NOT to use
- Tasks where a single agent already suffices (IG ≈ 0 — null information gain): the team is pointless and only burns tokens (HLE evidence: ACTS ≈ single agent).
- Workflows without a measurable task reward (subjective creative work, no ground truth) — the scheduler needs a labeled reward to train/validate.
- Teams of only 2 agents or very large teams (>10) — the paper validates N=3 only; larger N needs re-testing.

## Inputs required
- N agents, each with a clear role ρ_i (job description: critic, researcher, writer...).
- Task class + measurable reward (accuracy / pass rate) to evaluate; a 30–50 task sample to measure IG (single-vs-team Δaccuracy).
- A frozen backbone LLM; token budget cap B per workflow; production API access.
- (Path A — RL) MARL infrastructure: replay buffer, GNN/GRU modules, target network — engineering effort required.

## Steps
1. **Measure IG first (gate)**: run single-agent vs full-team on a sample; if ΔACC < 2/n (n = sample size) → task is IG≈0 → USE A SINGLE AGENT and stop. Large ΔACC → the team is justified, continue.
2. **Define the six communication modes**: off (agent disabled, skip its LLM call), solo (work alone), broadcast (send to all), attn-broadcast (send to a high-relevance subset), receive (accept from all), attn-receive (pull a high-relevance subset). Each agent each round selects a mode + partners.
3. **Build role embeddings + relevance scores**: embed each role (e.g., via the backbone LLM on the role description); each round compute directed relevance α_ij between agent i→j from hidden state + role embedding (directional: α_ij ≠ α_ji). Threshold ᾱ = mean over eligible candidates → attn-* modes retain edges with α > ᾱ. Agents that chose off/solo leave the eligible set (Eq. 1).
4. **Path A (full ACTS, needs MARL)**: train the scheduler under CTDE — local Q network per agent (GRU state + GNN aggregation along the topology + relational attention), a centralized topological mixer Q_tot = b_t + Σ_h w_h·Σ_i λ_{i,h}·Q_i with weights from the global state + in/out neighborhoods; objective w_task·R_task − w_tok·min(Σtokens/B, 1); replay buffer + greedy TD targets; backbone frozen.
5. **Path B (heuristic zero-RL — for solopreneurs)**: skip training; use a rule instantiation: (a) partner selection = attention threshold on α_ij computed from a role-affinity matrix (complementary role pairs like critic↔writer, researcher↔writer get high affinity; same-role pairs low); (b) mode policy by IG regime: high-IG tasks allow broadcast/attn-broadcast; low-IG → attn-receive pull-based + off/solo allowed; (c) token penalty = hard cap B, abort the round when exceeded; (d) early termination when a majority of agents are off/solo for 2 consecutive rounds.
6. **Topology-based credit assignment**: when evaluating agents (manual or automated), weight contribution by directed in/out neighborhood — agent i's credit ∝ Σ edges (i,j) that used i's message, NOT participation counts. (Evidence: the topology mixer is the strongest component — removing it costs 3.18 pp accuracy and +24% tokens.)
7. **Early termination + monitoring**: track per-round tokens + action distribution; off share > ~20% → the team is correctly restricting communication; high broadcast share on low-IG tasks → misconfiguration, re-run with attn-receive pull instead.
8. **Evaluate the Pareto front**: plot accuracy vs tokens for single / static / adaptive / scheduled teams; keep the team only if it sits on the Pareto frontier (static-level accuracy at ≤ static tokens). Report token-per-solved-task and accuracy-per-token, not raw accuracy.

## Expected output
- A per-round communication schedule (edges + modes), token usage within budget B, accuracy ≥ static baseline on high-IG tasks, near-single-agent cost on low-IG tasks; a Pareto accuracy-vs-token table confirming the team is worth it.

## Example application
- A solopreneur content pipeline with 3 agents (Researcher / Writer / Editor) on the task "write a blog comparing 5 products" (high-IG: multi-entity evidence): Researcher broadcasts findings to Writer; the Editor attn-receives only the relevant sections from Writer + Researcher (does not receive everything); round 2: Researcher off (done), Writer solo polish, Editor attn-receives. ~12k tokens vs ~21k for a 3-round full-mesh (−43%), accuracy preserved (Editor still receives sufficient evidence). On the task "reformat one paragraph" (low-IG): skip the team → single Writer, saving ~100% of team tokens.

## Gotchas
- **The IG gate is mandatory**: deploying a team on an IG≈0 task is waste (ACTS itself retreats to single-agent-level performance on HLE) — always measure single-vs-team ΔACC BEFORE building the scheduler.
- **Directional scores**: α_ij ≠ α_ji — "Writer→Editor" differs from "Editor→Writer"; don't use symmetric cosine similarity for partner selection.
- **Fixed partners are the worst variant**: ablation (b) fixed partner routing = 72.50% accuracy, 8.10k tokens vs ACTS 75.01% / 5.97k — never hardcode a role-pair graph; in Path B role affinity is only an initialization heuristic, recompute per state each round.
- **Token penalty clamp**: the objective clamp B (min(Σ/B, 1)) means the penalty saturates — set B realistically (your real budget), otherwise the scheduler "cooperates" by over-squeezing → quality drops.
- **Training cost is excluded**: the 5.97k tokens are INFERENCE only; Path A training (MARL + replay LLM calls) costs as much as many rounds — worth it only when the team runs thousands of tasks (amortize).
- **Aggregation node**: the paper uses a separate final answer-aggregation node (not one of the 3 agents) — your team needs a final aggregator; don't let agents conclude separately.
- **N=3 only**: results are not validated for N>3; all-to-all Θ(N²) scaling remains a risk — cap N or use sparse coupling when scaling.
- **Path B heuristic is not validated by the paper** — it is a rule instantiation of the ACTS pattern; measure your own Pareto before trusting it (Path A is the paper's actual result).
