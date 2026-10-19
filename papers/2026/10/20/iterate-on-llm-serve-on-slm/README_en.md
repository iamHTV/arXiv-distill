# [2610.14576v1] Iterate on an LLM, Serve on an SLM

## Core value (1 sentence)
Develop agent behavior in prompt space on a frontier model, then distill the converged behavior into a small and cheap SLM using real production data — not synthetic data.

## Problem
Prior work failed to extract correct behavior from small language models (SLMs) for narrow, repetitive agent tasks, because every behavior change required retraining the model from scratch — taking days or weeks — while engineers defaulted to larger models just because they "work out of the box."

## Contribution
- A two-phase method: (1) develop behavior in prompt space on a frontier model with immediate feedback from live traffic, (2) distill the converged behavior into an SLM via supervised fine-tuning (SFT) on recorded production behavior — not synthetic imitations.
- Use the teacher's self-agreement on its own recorded prompts as a noise floor to decide whether the SLM is good enough for production.
- A real-world case study on a yes/no caregiver-shift classification task at a home-care agency, with blinded evaluation by a professional scheduler.

## Method
Two-phase pipeline. Phase 1: the agent runs on GPT-5.4-nano; every prompt change is tested immediately against live traffic, and every trace (execution trace) is recorded. Phase 2: once behavior converges, the system replays each recorded batch byte-exactly using the same prompt builder and serializer as the live evaluator, producing the identical chat context that would be served to a deployed model, then pairs it with the recorded tool call as the target. Contract filtering drops samples whose reasoning lacks a hard-conflict justification; deduplication keeps the most recent decisions; train/validation split is by source batch. Finally, LoRA-tune Qwen3-4B and Qwen3-8B on this corpus. The gate for deployment: the SLM must beat the teacher's self-agreement (72.7%) and pass blinded human evaluation.

## KNOWLEDGE — Data & concepts
- Teacher GPT-5.4-nano self-agrees only 72.7% (95% CI 0.65–0.79) when re-run on its own recorded prompts — the noise floor.
- Tuned Qwen3-8B achieves 0.913 agreement (95% CI 0.89–0.93) on 880 validation cases, more consistent with production traces than the teacher itself.
- Tuned Qwen3-4B: 0.863 agreement but 12% malformed output rate — not production-usable.
- Base Qwen3-8B zero-shot: 0.774 agreement*, 23% malformed outputs, 14.9s p50 latency.
- Professional scheduler sided with the student 48 times vs. 29 for the teacher on 77 disagreements (62%–38%, p=0.040).
- Training corpus: 549 production batches, 11,621 train + 1,604 validation examples, 17 organizations.
- Cost: teacher ~$1.9–7.7 per 1,000 decisions (depending on prompt-cache state); SLM ~$0.19–0.38 per 1,000.
- Latency: teacher 7.1s p50 / 13.1s p95; tuned 8B SLM 2.9s p50 / 4.3s p95 (~2.5× faster).
- Training: LoRA, ~1,023 optimizer steps, ~1B training tokens, 65,536 max context. Final eval loss: 0.534 (4B), 0.254 (8B).

## INSIGHT — Mechanism & why
[SLM achieves higher agreement than teacher] BECAUSE [the teacher is non-deterministic, only agreeing with itself 72.7% of the time, so it acts as a noisy annotator rather than ground truth]. This means [the SLM can be trained to be more consistent than the teacher that defined it].
[Base zero-shot SLM fails on 23% of cases due to malformed output] BECAUSE [the SLM is not tuned for the specific task contract/format]. This means [zero-shot SLM is not a viable alternative; fine-tuning is required].
[Developing behavior in prompt space takes minutes-seconds vs. days-weeks of retraining] BECAUSE [prompt changes get immediate feedback from live traffic without retraining model weights]. This means [the agent behavior design loop should happen at the prompt level, not the weight level].

## IDEA — What to apply
Apply the two-phase pipeline to lead classification for outbound sales calls: step 1 is to use a frontier model to design the prompt for deciding high-quality leads, collect production traces from real calls, then distill into a small SLM to run thousands of calls per day at low cost.
Apply contract filtering when building SLM training data from production traces: step 1 is to define hard-conflict justification in the reasoning trace, then drop samples lacking it before SFT.

## WISDOM — General principle
Principle: Develop agent behavior at the prompt level (cheap, fast), then compile it into an SLM using real production data (not synthetic data) once behavior has converged. Apply when the task is narrow, repetitive, and runs thousands of times per day. DO NOT apply when behavior changes continuously or the task requires broad open-ended reasoning.

## Assumptions & Limitations
- Conditions for validity: the task is a narrow yes/no classification, production traces are recorded, behavior has converged (not changing continuously).
- Limitations acknowledged by the paper: the distilled model is not yet serving production traffic; all numbers are offline replay; ground truth labels come from a single professional scheduler; statistics do not model correlation between cases from the same organization/batch; covers only one subtask, one domain, one teacher.
- Limitations the paper does NOT mention: storage cost of thousands of production trace batches; time to collect enough traces for behavior to converge; impact of prompt-cache dynamics and traffic mix in online A/B testing.

## Metadata
- Year: 2026
- Authors: Keegan Wang (Carnegie Mellon University)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.14576v1
- arXiv ID: 2610.14576v1
- Label: [applied]
- Skill: iterate-on-llm-serve-on-slm | Test: [SKILL VALID]
