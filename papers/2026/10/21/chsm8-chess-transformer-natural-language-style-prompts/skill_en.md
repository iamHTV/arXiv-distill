# Skill: nlp-style-behavior-control-dpo

Source: 2610.25356v1
Type: framework / workflow

## When to use this skill
- When you need to control AI model behavior or style via natural language instructions, rather than only via rating or identity.
- When you want to improve style adherence without building a complex reward model.
- When you need to balance instruction following with maintaining base model strength.

## When NOT to use this skill
- When the task lacks a clear distinction between good and bad outputs.
- When you do not have paired data (same output, different conditions) for DPO training.
- When you do not have GPU resources to run fine-tuning or DPO.

## Required inputs
- Paired data: same output under two different conditions (matched vs mismatched description).
- A pre-trained SFT model (reference model).
- GPU resources for DPO (recommended at least 1 GPU for short runs, multiple GPUs for full pass).
- A validation set with metrics for style adherence and base strength.

## Steps to execute
1. Prepare paired data (label-swap pairs): take the same game/output, assign matched description as chosen sample and mismatched description as rejected sample.
2. Run SFT first: attach frozen text encoder via gated cross-attention, train on data with style descriptions.
3. Run DPO: use the same moves under mismatched description as rejected sample, with DPO loss combined with NLL anchor and KL term.
4. Pin no-text term: keep the no-prompt policy unchanged through cross-attention biases.
5. Tune hyperparameters: β, NLL weight, KL weight, learning rate for body and conditioning layers.
6. Evaluate on validation set: measure style adherence (e.g., trade rates, pawn moves, castling) and no-prompt strength (Elo or equivalent metric).
7. Run automated search loop: queue of configurations, each run for fixed time, scored, plan next round from results.

## Expected output
- A model with behavior controlled via natural language, high style adherence, and maintained base strength.
- Evaluation report: style adherence metrics, no-prompt strength, attack gap (strength loss under risky prompts).

## Example application
A company wants to build an LLM sales agent that can change its tone based on customer request (e.g., "be enthusiastic and fast", "be calm and professional"). They collect conversation pairs (same response, one described as enthusiastic, one as calm), run DPO to make the agent follow the requested style without needing a reward model.

## Gotchas
- DPO needs high-quality paired data: if NLL weight is too weak, the model finds a shortcut (making conditioning destructive) and Elo drops 50–145 points.
- Must pin the no-text term, otherwise the no-prompt policy changes through cross-attention biases.
- Full-pass DPO is not always better than short runs: style adherence saturates early, more data does not improve play.
- Screening with few games (100) can mislead (e.g., screened at −66 gap but measured −165 at 1,000 games).
- Style adherence is only reliable with validated metrics, not just hand-written metrics.