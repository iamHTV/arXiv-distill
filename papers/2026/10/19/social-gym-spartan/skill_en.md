# Skill: SPARTAN Playbook Loop (Self-Play and Reflect-Transfer)
Source: 2608.09128v1
Type: workflow

## When to use this skill
- You need to improve an AI agent on a social/asymmetric task (negotiation, customer service, auction, group collaboration) without fine-tuning or weight updates.
- The structurally weaker role (minority, information-poor, passive side) underperforms the strong role on the same task.
- Do NOT use: small open-weights models (≤32B) on discussion-heavy workflows (paper result is near-null); tasks with no objectively measurable outcome.

## Inputs required
- A model agent (use a strong model as teacher if you want distillation to a weaker model).
- A set of self-play scenarios with objective outcomes (win/loss per role).
- N ≥ 30 games per condition → binomial 95% CI ≈ ±18pp; more if you need precision.
- The ability to prepend text to the system prompt.
- Full trajectory logs for every game, labeled by role (main/alt).

## Steps
1. **Play:** let model M play N self-play games; log full trajectories + outcomes per role. Identify the structurally weaker role (usually the minority / information-poor side).
2. **Reflect:** prompt M (first person) to write a game-agnostic playbook from {trajectories, outcomes}. The playbook must cover 6 dimensions: deception, detection, persuasion, information management, coalition dynamics, timing. Do not reference game-specific numbers or events. Notation: R1 = Reflect(M, τ1:N).
3. **Transfer:** prepend the playbook to the system prompt for subsequent games. Measure per-role win rate vs baseline.
4. **Iterate (optional):** Rn = Reflect(M, τ under playbook Rn−1). Measure each round — the bulk of gain arrives at R1, peaks are usually R1–R3; stop when alt-side win rate stops rising (extra rounds only redistribute).
5. **Verify transfer:** test the playbook on (a) a held-out scenario and (b) a weaker student model. Inject the playbook into the student and measure BOTH roles — expect gains only on the weaker side (+13–24pp with GPT-5-mini teacher, n=30).

## Expected output
- A playbook (a few hundred tokens) that can be prepended to a system prompt.
- Alt-side (weak side) win rate rises (GPT-5-mini: average 24%→43% at R3 peak across 3 hidden-role games); the main side may drop (76%→59% worst at R2) — this trade-off is expected, not a bug.
- With a sufficiently capable model: cross-game transfer (median +7pp alt-side, max +27pp) and strong-to-weak distillation (+13–24pp) both work.

## Example application
- A solopreneur uses an agent to negotiate prices with suppliers: run 30 self-play games (agent vs agent, buyer/seller roles), reflect on the buyer role (structurally weaker) into a playbook (keep the real budget hidden, detect anchoring, manage information, time the final offer), prepend it to the real negotiation agent's system prompt. Measure the rate of better deals vs baseline.

## Gotchas
- A single reflection round (R1) already captures the bulk of the gain; iterating to R4 can crash the main side (76→59%) without helping the alt side.
- Playbooks inherit the teacher's bad habits — Qwen3-32B codified its own parroting into the playbook without eliminating it.
- The paper has no placebo control → part of the effect may be prompt perturbation; when verifying yourself, always A/B against a placebo text of equal length.
- Multigame playbooks do NOT stack: merging multiple sources is no better than the single most related source.
- Models ≤32B cannot learn from discussion-heavy trajectories — effective only when the action collapses to a single discrete token (e.g. a yes/no vote).
- Always measure win rate per role: an overall average hides the "lift the weaker side" pattern.
