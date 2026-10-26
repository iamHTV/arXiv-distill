# [2610.32435] ProfileSim: Profile-Driven User Simulation via RL with Hierarchical Rewards for Task-Oriented Dialogues

## Problem
- Task-oriented dialogue (TOD) for high-value financial marketing outbound calls needs large volumes of domain-specific dialogue data, blocked by privacy regulations, annotation costs, and expert labor. Prior user-simulation work (UserLM, PersonaLLM, USP) targets general-domain written text and fails twice: (1) insufficient domain constraints — no modeling of business processes and compliance rules; (2) inadequate spoken-language modeling — written-trained outputs diverge from the disfluency and colloquial style of real voice interactions.

## Contribution
- Joint modeling of user profiles (demographics + Big Five personality traits: Extraversion, Agreeableness, Conscientiousness, Emotional Stability, Openness to Experience) and business profiles (intents reverse-engineered from real call logs) as explicit conditioning variables for fine-grained behavioral control.
- SFT on real voice dialogue data, then GRPO (Group Relative Policy Optimization) with hierarchical rewards at dialogue level (profile-consistency cosine) and utterance level (coherence / non-repetition / naturalness / business) with turn-level advantage for fine-grained credit assignment.
- Business profile transition mechanism: 73 fine-grained intents in 9 groups; empirical 9×9 intent-group transition matrix + stay probability pstay = 0.1.

## Method (core)
- Data pipeline: 242,438 raw call sessions → desensitization + transcription-error correction + quality filtering → 72,296 valid dialogues (432,457 utterances, avg 7 turns). 10,000 dialogue–profile pairs annotated with GPT-5; LoRA-tuned Qwen3.5-9B profile extractor; 1,000-pair manual validation → 95.4% valid.
- SFT: quintuples (product info, history, user profile, business profile, target utterance); 97,126 utterances; LoRA on 2×A100, 3 epochs, lr 2e-4, max 1,024 output tokens, ~14 h.
- GRPO: G=8 multi-turn dialogues per rollout context; user simulator is the trainable policy; the customer-service agent (DeepSeek-R1 backbone + SOP-constrained dialogue + RAG) is the fixed environment policy; 4,000 sampled profiles; 8×H200, 2 epochs, ~20 h. Turn reward r_t = 0.5·r_profile + 0.5·r_utterance, where r_utterance = 0.30·coherence + 0.15·nonrep (cosine vs previous user utterance > 0.8 → 0) + 0.25·naturalness + 0.30·business-consistency; judge = Gemini 3.1 Pro, scores 1–5 normalized (s−1)/4.
- Agent side: SOP as a directed graph of dialogue stages with allowed transitions; RAG retrieves intent recognition result, candidate next stages, and stage templates, filtered by the current SOP state; output is structured JSON (next stage, response).

## Key Findings
- Table 1 PPL (perplexity; lower = better alignment with real user distribution): SFT-only 58.48 → +Business Profile 43.04 (−15.44) → +User Profile 22.24 (−36.24) → Full SFT 17.52 → Full + GRPO 17.49. User-profile conditioning is the dominant factor (22.24 vs 43.04 business-only); the two profiles are complementary.
- Table 2 (3,000 sessions per generator, identical agent and protocol): Full Model colloquial naturalness 4.97 (SFT-only 4.46; GPT-5 4.21; DeepSeek-V3 3.22); mean user utterance length 11.14 chars (GPT-5 44.54; DeepSeek-V3 153.96); user profile adherence 92.55% (SFT 84.29%; general LLMs ≤ 84.05%); agent score on long-tail intents (bottom 20% frequency) 3.49 — lowest, i.e. strongest stress on the fixed agent (LLMs 4.18–4.45); business profile compliance 52.25% (GPT-5 higher at 62.01% but wordier).
- Generated dataset: 3,000 sessions, ~20,000 user–agent utterance pairs, 58% of user utterances map to scenario-specific intents; human spot-checks on 500 stratified samples per metric agree with the judge at Cohen's κ ≥ 0.72.
- Prior-work anchor: multi-turn RL reduces persona drift by over 55% (Abdulhai et al., 2025), motivating the GRPO design.

## Actionable Insights
- Persona modeling beats business context when simulating users: +User Profile cut PPL by 36.24 vs 15.44 for +Business Profile. Example: when building fake callers for a call center, assign demographics + Big Five traits ("male 40–55, unstable income, direct style, low Extraversion") rather than only "will ask about a loan".
- A closed-loop simulator–agent pair is a stress-test factory: profile-conditioned simulators generate long-tail-intent (bottom 20% frequency) interactions that score the fixed agent lowest — the most valuable corpus for robustness training. Example: before deploying a sales chatbot, generate 3,000 persona-diverse dialogues to find which rare intents the agent handles worst.
- Voice ≠ text: benchmark colloquial naturalness and utterance length separately; written-style models (GPT-5 at 44.54 chars) are poor fits for telephony. Example: for voice outbound AI, evaluate spoken-style brevity before choosing a model.
- Privacy-safe data pipeline: 242,438 raw → 72,296 usable after desensitization, with auto-extracted profiles 95.4% valid — a recipe to build from your own anonymized call logs without expert annotation of every call.

## Assumptions & Limitations
- Requires your own domain call logs (≥10K samples for profile annotation) plus GPU budget (SFT 2×A100 14 h; GRPO 8×H200 20 h).
- Paper-stated: user profiles are static — no dynamic attitude/emotion shift during a conversation; validated on a single domain (financial marketing outbound calls) with no cross-domain experiments; downstream intent-recognition accuracy gain is not actually measured (only agent stress score).
- [MY OWN] Business compliance metric is confounded — a high score can reflect explicit verbalization (GPT-5 62.01%) rather than realism; Gemini 3.1 Pro judging and GPT-5 annotation carry vendor bias risk; pstay = 0.1 is hard-coded, not tuned.

## Metadata
- 2026, Bairong Inc. (Juan Li, Fangshu Chang, Xinyi Jiang, Ling Huang, Yunzhang Chen), cs.CL, https://arxiv.org/abs/2610.32435, citation count: [NOT FOUND] (paper too recent)
