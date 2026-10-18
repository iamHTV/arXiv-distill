# Skill: Receiver-Relative Protocol Selector (Gain − Tax Communication Control)
Source: 2610.03769v1
Type: evaluation-method / workflow

## When to use this skill
- A multi-agent workflow has a sender with broad context + an executor with a limited local view, and you need to choose the communication protocol (skip / compress / raw / escalate / refresh) at each step.
- You want to optimize the accuracy–cost frontier: avoid sending expensive messages when the receiver already has enough context, or send raw context when compression suffices.
- Do NOT use: single-agent setups (no sender/receiver asymmetry); tasks without measurable artifact/action targets (no hit_joint); without budget to run paired RO/SF/MA calibration (3 protocol runs per step).

## Inputs required
- Tasks with measurable acceptable artifact/action targets (G_t = {(Z^art, Z^act)}) — labels never exposed to the sender, receiver, or selector.
- A fixed receiver (model + prompt + parser + context window + tool interface), a sender (model), and a message budget B (tokens).
- Paired RO/SF/MA calibration records (receiver-only / raw-context / bounded-message) split by instance_id, keeping the receiver interface + action set fixed.
- Estimates: gain surrogate Â (clipped leading-token log-probability difference), action-level offset τ̂ (protocol burden + gain effects), local-sufficiency rate (from held-out RO records), cost weights η_c, η_r (tuned on a held-out split; paper uses η_c = 10⁻⁴ on raw token counts, η_r = 0 for the static one-step ablation).

## Steps
1. **Calibrate offline:** run paired RO/SF/MA on a calibration set (paper: instance-disjoint, 5–40% of records → accuracy 0.7368–0.7458). Extract the action-level offset τ̂ per protocol action and the local-sufficiency rate for the early-skip branch. Fix offsets, skip threshold, and cost weights BEFORE evaluation.
2. **At each step t,** read instance-level signals (local view X, burden proxy b, shared-state discrepancy D_t if any).
3. **Score the 5 actions:** skip (RO endpoint), compress(B) (bounded message under budget B — evaluated by the compression criterion ∆U = ∆τ_saved − I_omit − Λ_C), raw (full context — retained because Bayes-sufficient compression can still fail), escalate(C') (a stronger receiver on the compressed message — scored by the gain–tax comparison), refresh (shared-state resynchronization — scored by residual propagation Prop 7: D_{t+1} = k_t + λ_t[D_t − q_t]_+).
4. **J_t(α) = A* − τ − η_c·c(α) − η_r·r_t(α)** — receiver-relative utility minus immediate cost minus future residual risk; pick α* = argmax.
5. **Execute once** using the cached candidate (paper: the 5-action path refresh/skip/raw/compress/refresh caches real compress + refresh messages before 9 receiver probes, capped at 4 tokens).
6. **Early-skip gate:** if the local-sufficiency rate is high (receiver RO accuracy already ≥ crossover ~0.63), skip the message before calling the sender (ToolSandbox online: early-skip 1.000 accuracy, 919.4 tokens, 6.60 s/step vs always-send 0.8056, 3,085.4 tokens, 9.56 s).
7. **Monitor closure:** measure artifact accuracy h_a AND conditional action-conversion h_action separately — if h_a is high while h_action is low (closure-dominated, e.g. GLM-5 0.741/0.545, MiniMax-M2.5 0.613/0.053), the failure is in action closure, not message content → fix the receiver interface/format, not the sender.

## Expected output
- A per-step protocol decision with a better accuracy–cost profile than both always-skip and always-send: ContextBench static selector 0.7367 accuracy at 1,735 tokens/step (vs always-skip 0.6500/1,300 and always-send 0.7867/3,235.4) — recovering +8.67pp over always-skip with 46.4% fewer tokens than always-send.
- Knowledge of the regime (helpful/noisy/boundary) per receiver interface: the compression sign flips across benchmarks (ContextBench +0.14, ToolSandbox −0.24, BFCL −0.23, τ-bench 0.00).
- A sender-upgrade threshold b* (paper: 0.6289, CI [0.552, 0.706]) — knowing when a stronger sender helps vs hurts.

## Example application
- A solopreneur runs a pipeline: researcher agent (sender, broad context) → writer agent (executor, limited view). Calibrate on 10 articles: writer RO accuracy 0.7 (> crossover 0.63) → early-skip: the researcher sends no message, the writer works directly — saving ~2,000 tokens/step. For articles where writer RO is 0.4 (< threshold) → compress the researcher's findings into a 128-token brief in a template the writer knows → +8–20pp accuracy.

## Gotchas
- Bayes-sufficient ≠ receiver-usable: a message with correct content but the wrong surface form still fails (strict-recoding −13.5pp on τ-bench) — always format for the receiver's interface and test fixed-message replay before deploying.
- A stronger sender HURTS when receiver burden is low (ToolSandbox −26.4pp) — do not default to the strongest model as planner.
- The selector does not always win: on τ-bench, rewriting beat the selector 0.139 vs 0.083 at similar cost — keep raw/rewriting in the action set.
- Calibration costs 3× runs (RO/SF/MA) — only worth it for many-step workflows; for short pipelines, the early-skip gate by RO accuracy alone is simpler.
- Truncation: the gains are not a truncation artifact (capped +10.64pp, uncapped +32.89pp) — but keep both decision fields in capped messages.
- Action-closure errors (outputs choosing read when the action is edit — 40.8–94.0% wrong-action rates) need fixes in the receiver prompt/tool schema, NOT the message.
- η_r = 0 in the static ablation — for shared-state workflows (residual persists), you must charge future residual risk (η_r > 0) or errors multiply forward (Prop 7).
