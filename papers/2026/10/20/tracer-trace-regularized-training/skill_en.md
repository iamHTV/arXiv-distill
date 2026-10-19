# Skill: tracer-trace-regularized-training
Source: 2610.19133v1
Type: framework

## When to use this skill
- An LLM/RAG/agent system receives untrusted content through multiple channels (retrieved document, tool output, agent message, follow-up message).
- Want to reduce indirect prompt injection attack success rate (ASR) without degrading clean-task accuracy.
- A task dataset with gold answers and template-based indirect injection samples are available.

## When NOT to use this skill
- Evaluation in a single channel only (ignores cross-channel risk).
- Adversary is optimization-based or multi-turn, not covered by template-based attacks.

## Required inputs
- A base language model (e.g., Qwen2.5-3B-Instruct).
- A task dataset with inputs and gold answers.
- Adversarial payloads and presentation channels: follow-up, rag, tool, agent.
- GRPO (or equivalent), 4-bit QLoRA, vLLM for rollouts.
- A verifier to extract anchor propositions from clean reasoning traces.

## Steps
1. Collect task samples (xi, yi) and adversarial payloads (ai).
2. Each training episode (three-turn game): model produces clean reasoning trace (τ0) and clean answer (ŷ0) from the clean task.
3. Sample a channel (ci) from distribution pS(c) (e.g., follow-up/rag/tool/agent), render payload through it as ρci(ai).
4. Model produces post-attack reasoning trace (τci) and post-attack answer (ŷci) from clean prefix + rendered content.
5. Compute the composite post-attack reward: answer correctness (ans, weight 0.25), process quality (proc, 0.25), anchor retention (anc, 0.20), evidence-gated corrigibility (corr, 0.20), length control (len, 0.10).
6. When the evidence gate is active (clean answer correct and injected evidence invalid), apply ATRC: align post-attack token distribution to clean distribution via KL divergence and committed-span token recovery on committed positions.
7. Update the model with GRPO plus KL regularization and ATRC regularization.
8. Evaluate cross-channel: same payload, change wrapper (follow-up → rag → tool → agent), measure ASR and clean accuracy per channel.

## Expected output
- Model substantially reduces indirect injection ASR (e.g., from 65.5% to 6.1% at RAG) while keeping clean accuracy high (78–82%), and transfers robustness better than single-channel training.

## Example application
- Enterprise internal RAG system: collect injection samples across retrieved document, tool output, agent message channels; train Qwen2.5-3B with TRACER for 3 epochs; evaluate on 4 channels; average ASR drops to ~13.9% (multi-framing RAG+tool).

## Gotchas
- Do not evaluate in a single wrapper only — channel-specific robustness does not transfer across channels.
- Do not use answer-only reward — it reaches 21.3% ASR vs 6.1% for full TRACER; composite reward keeps clean reasoning.
- Do not force the model to keep the clean trace when injected evidence is valid — the corrigibility term must be evidence-gated to avoid blanket refusal.
- Do not treat TRACER as a complete security boundary — combine with runtime safeguards (retrieval filtering, tool-output parsing, monitoring, sandboxing).

## Self-check
- Can someone who has not read the original paper follow these 8 steps? [YES] — each step is a concrete action.
- Which step is most vague? Step 6 (ATRC on committed spans) needs implementation-specific details on aligning logits by response-relative position.
- Is the Input section sufficient? [YES] — base model, task dataset, payloads, channels, GRPO/QLoRA/vLLM, anchor verifier are all covered.

## Dry run (hypothetical scenario)
- Scenario: A small business's internal RAG chatbot; attacker can inject into retrieved documents.
- Run the skill: (1) Collect 2,000 GSM8K task samples and injection payloads; (2) train Qwen2.5-3B for 3 epochs, randomly sampling channels (follow-up/rag/tool/agent); (3) compute composite reward after each attack; (4) apply ATRC when the gate is active; (5) update via GRPO; (6) evaluate ASR on 4 channels; (7) if RAG ASR drops from 65.5% to under 10% and clean accuracy stays 78–82%, deploy.

## Verdict: [SKILL VALID]
