# [2610.19133v1] TRACER: Trace-Regularized Training Against Indirect Prompt Injection

## Core value (1 sentence)
Channel-aware adversarial training against indirect prompt injection: sample presentation channels (follow-up, retrieved document, tool output, agent message) during training and combine an answer-anchored, evidence-gated composite reward with ATRC trace regularization to preserve clean reasoning when injected evidence is invalid.

## Problem
Prior work failed to address the assumption that robustness to indirect prompt injection transfers across presentation channels — in fact the same attack payload succeeds 18% of the time as a follow-up message but 53% when placed in retrieved context (RAG), and existing defenses are usually trained and evaluated within a single wrapper.

## Contribution
- Identifies and quantifies the "framing gap": identical adversarial content becomes substantially more successful when presented through a different untrusted-context channel.
- Introduces TRACER (Trace-Regularized Adversarial Channel Exposure with Reward-shaping): an adversarial training framework that samples presentation channels as part of the optimization, combines an answer-anchored, evidence-gated composite reward with ATRC (committed-span Adversarial Trace Recovery and Consistency) to preserve clean reasoning under invalid injected evidence.
- Cross-framing evaluation: transfer across wrappers is asymmetric, revealing a depth–breadth trade-off between native robustness and generalization.

## Method
Each training episode is a three-turn robustness game: (1) the model receives the clean task and produces a clean reasoning trace plus clean answer; (2) the same adversarial payload is rendered through a sampled channel; (3) the model produces a post-attack reasoning trace and answer. The channel is sampled as a random variable in the training objective (channel exposure). The post-attack reward is a composite of 5 terms: answer correctness (ans), process quality (proc), anchor retention (anc), evidence-gated corrigibility (corr), and length control (len), with weights 0.25, 0.25, 0.20, 0.20, 0.10 respectively. ATRC is a trace regularizer: when the clean answer is correct and the injected evidence is invalid (evidence gate active), ATRC aligns post-attack token distributions to the clean distribution via KL divergence and committed-span token recovery. The overall objective optimizes with GRPO plus KL regularization and ATRC regularization.

## KNOWLEDGE — Data & figures
- Same attack payload: ASR 18% (follow-up) vs 53% (retrieved context/RAG) across six intermediate snapshots trained only on follow-up-style attacks (+35 pp).
- Base model authority gradient: prompt injection ASR from 70% (casual follow-up) to 92–96% (agent, tool, RAG wrappers).
- TRACER on GSM8K with Qwen2.5-3B-Instruct: reduces RAG-framed ASR from 65.5% to 6.1% while maintaining 78–82% clean accuracy.
- RAG specialist: 6.1% ASR on RAG but 25.7% (tool) and 26.5% (agent) — RAG training learns depth in-channel, weak transfer.
- Tool-output training: higher native ASR (15.0%) but nearly flat across all four framings (15.0–20.2%) — learns breadth.
- Multi-framing (RAG+tool) 3B: best average ASR 13.9%, improves native RAG (5.2% vs 6.1%).
- 7B scaling: one epoch RAG training reaches 9.4% average ASR across four framings; final 7B model 10.8% average ASR.
- Objective ablation: answer-only 21.3% ASR, composite reward 13.8%, full TRACER 6.1%.
- Held-out paraphrase: TRACER 10.0% ASR vs base 62.7%.
- Channel-aware escalation: TRACER 18.1%, defense-aware 23.8%, baselines 68.8–70.0%.
- Mixed evidence: clean/evidence accuracy 81–83%, injection-induced flip rate from 46.3–58.1% (base) to 13.8–17.5% (TRACER).
- Training: 3 epochs, LR 2×10⁻⁶, batch size 1, gradient accumulation 8, group size 4, KL coefficient 0.10, ATRC weight 0.10, 4-bit QLoRA, vLLM rollouts.
- Reward weights: ans 0.25, proc 0.25, anc 0.20, corr 0.20, len 0.10.
- Channels: {followup, rag, tool, agent}.
- Code: https://github.com/Mishrakshitij/TRACER.git

## INSIGHT — Mechanism & why
[Same payload succeeds 53% at RAG vs 18% at follow-up] BECAUSE [users treat retrieved context as having higher authority (authority gradient) — the surface form carries implicit authority even though contents may be untrusted]. This means [robustness in one wrapper is not robustness to the underlying attack; single-channel evaluation misses cross-channel risk].
[RAG specialist strong in RAG but weak on tool/agent] BECAUSE [the model learns channel-specific skepticism rather than channel-invariant robustness]. This means [multi-channel training yields more transferable robustness, especially at 3B scale].
[TRACER keeps 78–82% clean accuracy while cutting ASR to 6.1%] BECAUSE [the corrigibility term is evidence-gated: rewards preserving a correct answer under invalid evidence, but not refusing genuinely valid evidence]. This means [defense is not blanket rejection of external context, but distinguishing valid from invalid evidence].

## IDEA — What to apply
Apply TRACER to an enterprise RAG system: step 1 is to collect indirect prompt injection samples across channels (follow-up message, retrieved document, tool output, agent message), then train adversarially with randomly sampled channels and an evidence-gated reward.
Use cross-channel evaluation instead of evaluating in a single wrapper: step 1 is to test an injection-hardened model with the same payload wrapped as retrieved document, tool output, and agent message.

## WISDOM — General principle
Principle: Robustness to indirect prompt injection must be trained and evaluated against the channels through which untrusted context actually reaches the model; DO NOT assume robustness in one channel transfers to another. Defense should combine channel-aware robust training with runtime safeguards (retrieval filtering, tool-output parsing, monitoring, sandboxing).

## Assumptions & Limitations
- Conditions for validity: indirect prompt injection setting, model receives untrusted context through multiple channels, clean trace available as anchor.
- Limitations acknowledged by the paper: attacks are primarily template-based, not covering arbitrary optimization-based or multi-turn adversaries; full TRACER training evaluated only on Qwen2.5 at 3B and 7B scale; TRACER is a training-time defense, complementary to not a replacement for inference-time safeguards.
- Limitations the paper does NOT mention: operational cost of per-channel sampling at scale; impact on inference latency when combining multiple channels; stability across repeated retraining as the tool catalog changes.

## Metadata
- Year: 2026
- Authors: Kshitij Mishra, Salem Lahlou, Nils Lukas (Mohamed bin Zayed University of Artificial Intelligence)
- arXiv category: cs.LG
- PDF link: https://arxiv.org/pdf/2610.19133v1
- arXiv ID: 2610.19133v1
- Label: [applied]
- Skill: tracer-trace-regularized-training | Test: [SKILL VALID]
