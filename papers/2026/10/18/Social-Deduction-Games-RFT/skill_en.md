# Skill: Social-Cognitive RFT — Training social agents with reading + influence rewards
Source: 2610.04261v1 (Social Deduction Games + RFT)
Type: workflow (training recipe)

## When to use this skill
- You need to train an LLM agent for multi-agent / human-interactive settings where success depends on social reasoning (reading other agents, influencing collective decisions): negotiation, customer support, meeting coordination, sales.
- Outcome-only RFT (reward = final win/loss) yields high-variance, non-monotonic training — the reward needs decomposition.
- Do NOT use when: the task is single-agent with no social component; the task has directly verifiable answers (code, math) — standard rewards suffice; no simulator can log intermediate social signals.

## Inputs required
- A game/arena simulator: hidden state (roles, private info), public transcript, structured actions (vote, proposal, approval), terminal outcome; a turn-based prompt-chaining protocol.
- Definitions of two reward components: a reading target (the latent state to infer: roles, teams, intentions — F1 for sets, exact-match for categorical) and an influence target (the intended effect on others' next actions: vote direction, approval, target concentration).
- Fixed opponent policies (at least initially) + a role distribution; budgets (training steps, group size G for GRPO).
- A backbone model + a reference model for the KL penalty.

## Steps
1. Build the arena: each episode records prompts, responses, parsed actions, private role info, public transcript, intermediate social outcomes, and the terminal outcome. Invalid actions → format failures (logged separately).
2. Define the reward decomposition: R(τ) = λ_read·R_read + λ_inf·R_inf + λ_aux·R_aux − λ_fmt·P_fmt − λ_leak·P_leak. R_read = the average score comparing the agent's emitted belief state against the hidden target at reading events; R_inf = the average score measuring others' subsequent actions against the intended social target; R_aux = intermediate game events (exile an adversary, protect a teammate); P_fmt penalizes invalid structured output; P_leak penalizes publicly revealing hidden information.
3. Reading before influence: run the reading regime first (reward emphasizing hidden-state inference) so the policy has a stable belief state — the influence reward is only effective when grounded in accurate beliefs (SI-only cut Qwen3-4B's win rate from 21% to 12%).
4. GRPO optimization: sample a group of G trajectories under the same condition; normalize the advantage within the group Â = (R(τ_g) − μ_R)/(σ_R + ε); clipped policy-gradient + β·KL(π_θ ‖ π_ref). No critic needed.
5. Same-side training (if the task is team-based): assign the same policy to every role on one side, each update conditioned on that role's private role and public history — one game yields multiple training samples without mixing objectives across sides.
6. Evaluate terminal win rate as a HELD-OUT DIAGNOSTIC (not the online reward): win rate must improve together with reading/influence scores — if win rises while reading/influence do not, suspect a formatting shortcut.
7. Cross-model check: play the learned policy against unseen opponents (≥9 opponents, 100 games each) — win rate + SR-F1 + SI-Follow + outcome metrics must be stable across families.
8. Human blinded evaluation (if possible): matched base-RFT pairs, ratings 1–5 on five dimensions (overall value, reading quality, influence & coordination, human-likeness, strategic correctness); evaluators must NOT high-score merely because a side won; sign-flip permutation tests.

## Expected output
- An improved policy: reading accuracy (hidden-state F1/accuracy), influence metrics (target hit rate, approval outcome), terminal win rate (held-out), human ratings (overall value +~1.09/5, strategic correctness +~1.17/5). Expected pattern: stronger gains at later evidence-rich states (Day-3 F1 +0.41 vs Day-1 +0.11).

## Example application
- A solopreneur sales-negotiation agent: reading reward = inferring the customer's budget/urgency from messages (F1 vs CRM labels); influence reward = the customer's next action (book a demo, share documents) moving in the intended direction; aux = meeting booked; format penalty = invalid JSON; leak penalty = revealing other customers' data. GRPO-train on simulated negotiations; evaluate on held-out negotiations + human ratings. Expected: better qualification + a higher booking rate, without needing to win every negotiation.

## Gotchas
- Do NOT use terminal win as the online reward — sparse/noisy: Werewolf/Mafia peaked at 0.88 then fell to 0.38; Avalon average reward only 0.25. Win rate is a diagnostic, not the objective.
- Influence WITHOUT reading is harmful — SI-only can halve the win rate. Always train reading first or jointly, never influence-only.
- The SI-only prompt scaffold can hurt models with weak beliefs (Qwen3-4B: 21%→12%) — run scaffold ablations (none/SR/SI/SR+SI) before RFT.
- Response length is NOT a proxy for skill: some models get more verbose when steering, while DeepSeek-7B improves with shorter responses — monitor length but don't optimize it.
- Role-fixed training (the Assassin) shows: when one role's payoff concentrates on a single inference problem, outcome-reward alignment is better — mixed-role training is necessary for a general policy, but role-specialized training is stronger for payoff-concentrated tasks.
- P_leak is mandatory: agents can learn to publicly reveal hidden information to "win" — penalize it explicitly.
- Fixed opponents → the policy may overfit opponent quirks; cross-model evaluation is mandatory before trusting transfer.
- The human evaluation is small (178 ratings) and descriptive — don't overclaim; human-likeness improves little (+0.36, n.s.) — strategic competence ≠ naturalness.
- A reward for agreement alone may train conformity — the reward must include "the effect advances an appropriate collective goal" (three components: represent accurately, produce the intended effect, the effect advances a normatively appropriate goal).
