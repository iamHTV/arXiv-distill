# Skill: Build Profile-Conditioned User Simulators for Sales Agents (ProfileSim Recipe)
Source: 2610.32435
Type: framework (data-synthesis + training recipe)

## When to use this skill
- You need domain-specific dialogue data to train intent recognition or evaluate a sales agent, but lack enough real data (privacy, cost, expert labor).
- You want to stress-test a chatbot/call bot before deployment with diverse simulated users (fake users with personas).
- You need a cold start (fast bootstrap) for a new agent without interaction history.

## Prerequisites (must have)
- Your own real call/chat logs from the domain (≥10K sessions) to extract profiles and reverse-engineer intents.
- You need user voice style (spoken telephony), not written text.

## When NOT to use
- You have no real logs at all → profiles/intents would all be invented → simulator learns fiction.
- The domain changes continuously and the intent taxonomy can't be rebuilt.
- You need emotion dynamics (feelings shifting across turns) — this skill uses static profiles only.

## Inputs required
- Real dialogue corpus (voice/telephony or chat) from your domain, already desensitized (anonymized).
- Structured product information (attributes of the product/service sold).
- SOP (standard operating procedure) with stages + allowed transitions.
- Knowledge base for RAG: product docs, FAQ, policy.
- GPU: 2×A100-class for SFT (~14 h), 8×H200-class for GRPO (~20 h).

## Steps
1. **Clean + extract user profiles**: desensitize, correct transcription errors, filter quality; annotate 10,000 dialogue–profile pairs with a strong LLM (paper uses GPT-5); profiles = objective features (gender, age range, occupation, income status, language style) + subjective features (Big Five five dimensions). LoRA fine-tune a Qwen3.5-9B profile extractor for 3 epochs; manually validate 1,000 pairs (target ≥95% valid).
2. **Reverse-engineer business profiles**: map each utterance → intent label (73 fine-grained intents in the paper), grouped into 9 intent groups; rewrite each intent as a natural-language business profile prompt (e.g. "Next, you may ask about the loan application process..."). Estimate a 9×9 transition matrix from consecutive (intent group t, t+1) pairs in logs; add stay probability pstay = 0.1; sample a group by the matrix, then uniformly sample a profile within the group.
3. **SFT the user simulator**: quintuples (product; history; user profile; business profile; target utterance); LoRA on a ~9B-class backbone, 3 epochs, lr 2e-4, max 1,024 output tokens; objectives: colloquial generation + profile-conditioned generation.
4. **SOP + RAG agent (environment)**: SOP = directed graph of stages; each turn retrieve 3 kinds of info (recognized intent, candidate next stages, stage templates) → filter by current SOP state; optional CoT prompting; output JSON {next_stage, response}; freeze the agent while training the simulator.
5. **GRPO with hierarchical rewards**: G=8 dialogue rollouts per context; user simulator = trainable policy, agent = fixed environment; full-dialogue rollouts (the profile reward needs cumulative responses); dialogue-level reward = cosine similarity(target profile, profile implied by cumulative responses) in [0,1]; utterance-level = 0.30·coherence + 0.15·nonrepetition (cosine vs previous user utterance > 0.8 → reward 0) + 0.25·naturalness + 0.30·business-consistency (judge scores 1–5, normalized (s−1)/4 for coherence/naturalness; nonrep/business are binary); turn reward = 0.5·dialogue + 0.5·utterance; advantage A_i,t = (r_i,t − μG)/(σG+ε) with μ,σ computed from dialogue mean rewards → turn-level credit assignment.
6. **Closed-loop dataset generation**: the agent opens with an opening template; the simulator responds conditioned on profiles; the business profile evolves via the transition mechanism; terminate on max turns or explicit user end intent. Paper: 3,000 sessions, ~20,000 pairs, avg 7 turns, 58% scenario-specific intents.
7. **Evaluate**: (a) PPL on a real held-out test set (distribution alignment); (b) colloquial naturalness judge score (target ~4.9/5); (c) utterance length (target ≈11 chars for telephony); (d) profile adherence cosine (target ≥92%); (e) agent score on long-tail intents (bottom 20% frequency) — lower = better stress testing (target < baseline LLMs 4.18–4.45); (f) human spot-checks on 500 samples per metric, Cohen's κ ≥ 0.72.
8. **Downstream use**: train an intent recognition model on the synthetic corpus; evaluate agent robustness; cold-start a new agent deployment.

## Expected output
- A 9B-class user simulator achieving colloquial 4.97/5, 11.14-char utterances, 92.55% profile adherence, agent stress score 3.49 (lowest among generators); PPL 17.49 ≈ Full SFT 17.52 (GRPO does not degrade distribution alignment); a 3,000-session dataset for intent-recognition training + agent evaluation.

## Example application
- A solopreneur selling online courses takes 5,000 anonymized consultation calls → personas (Big Five + income) + intent taxonomy (price, schedule, refunds, curriculum) + transition matrix; SFT+GRPO on Qwen3.5-9B; agent SOP graph (greet → needs discovery → course pitch → objection handling → close). Generate 3,000 fake calls → discover the agent answers the rare "refund policy" intent worst → train the intent classifier and patch scripts before launch.

## Gotchas
- **User profile dominant**: user-profile conditioning cut PPL by 36.24 vs 15.44 for business profile — don't skip personas assuming "business context is enough".
- **Full-dialogue rollouts are mandatory**: the profile-consistency reward is computed from cumulative responses → you cannot evaluate utterances independently; don't shorten rollouts.
- **Freeze the agent during GRPO**: it is the fixed environment; training both simultaneously makes rewards unstable.
- **Compliance ≠ realism**: GPT-5 reaches 62% business compliance but 44.54-char verbose utterances — high compliance can just mean explicit intent verbalization; judge realism by colloquial score, length, and agent stress, not compliance alone.
- **PPL is insensitive**: PPL measures token likelihood, not long-range coherence/persona consistency → GRPO's behavioral gains don't show in PPL (17.52→17.49 is tiny); don't conclude GRPO is useless from a flat PPL.
- **Static profiles**: the simulator doesn't model attitude/emotion shifts within a call → scenarios needing empathy dynamics must be extended separately.
- **pstay = 0.1 is hard-coded**: tune per domain (topic-switch-heavy domains may need it lower).
- **Transcript noise**: real voice logs need a serious transcription-error correction step — profile quality depends on transcript quality (95.4% valid only after cleaning).
