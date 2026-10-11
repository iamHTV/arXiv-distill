# Skill: CARE — Human-AI Escalation With Risk Control
Source: 2610.09043
Type: framework

## When to use this skill
- You have a cheap AI model making safety-relevant binary decisions and an expensive human expert who must review.
- You want to reduce human review volume while keeping risk below a given tolerance ε.
- The AI model updates over time and your safety gate must track each update.

Do NOT use when:
- The task is multi-class or regression — the paper only instantiates binary classification.
- The oracle (label source) is unreliable — the skill assumes the expert is always correct.

## Inputs needed
- A black-box AI model outputting probability p_A and confidence c_A (may be overconfident; does NOT need to be calibrated).
- An i.i.d. stream of unlabeled data.
- A human oracle: an expert who provides correct labels when queried (each query is costly).
- Risk tolerance ε (e.g., 5%) and a loss function (zero-one loss or Brier score).
- A preparation fraction of 10–40% for the offline phase.

## Steps
1. Set an offline-online schedule: offline checkpoints refit the rectifier and rebuild calibration; run online between checkpoints.
2. Residual Gauss: place a GP (Gaussian process) on the human-AI residual at the score scale; linear mean captures systematic bias, kernel combines k_phi (residual correlation) with k_A (AI uncertainty). Fit prior parameters by MLE/EM at checkpoints; online, use assumed-density filtering after each label.
3. Confident Jack: calibrate the escalation threshold via weighted cross-conformal — weights account for adaptively-selected labels — to control marginal risk at EVERY time step, even under arbitrary model updates.
4. Exacting Gates: accept the rectified AI decision only when rectified confidence c_t > lambda_t; otherwise escalate to the human.
5. Active Max: select the most informative queries (high epistemic uncertainty) to ask the human, prioritizing feedback that improves future decisions.
6. Monitor: empirical risk vs ε and human query rate; if risk exceeds ε, lower the threshold; if query rate is high, check whether the GP kernel captures the misalignment structure.

## Expected output
- A human-AI decision system with empirical risk ≤ ε in every region and 25–81% fewer human queries vs selective-escalation (SE) baselines.
- The rectified model becomes increasingly aligned: 15.5–70.5% relative error reduction (HateBench).

## Example application
Content moderation: AI screens posts, an expert handles hard cases. Run CARE with ε=5% → auto-approve ~78% of posts (only 21.7% escalation) instead of 57.1% with pure SE, while risk stays under 5%. Each expert label both corrects bias and recalibrates the gate.

## Gotchas
- Do not split labels into separate piles for training and calibration (PPI+SE) — it costs 26–48% more queries; CARE reuses the same labels.
- Do not use the AI's raw confidence directly if overconfident: SE/PPI query rate rises +28.0pp/+11.8pp when switching to direct confidence; CARE also rectifies the confidence.
- If initial uncertainty > ε and residuals are treated as independent → query-all degradation; model local correlation with a GP kernel.
- Every guarantee requires a correct-oracle assumption; a weak expert skews the whole pipeline.
