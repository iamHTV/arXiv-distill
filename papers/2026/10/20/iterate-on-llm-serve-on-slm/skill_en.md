# Skill: iterate-on-llm-serve-on-slm
Source: 2610.14576v1
Type: workflow

## When to use this skill
- You have a narrow, repetitive agent task (e.g., yes/no classification, caregiver-shift matching) that must run thousands of times per day.
- The desired behavior is still changing and needs fast iteration (multiple times per day) before converging.
- You have a frontier model already running the task and can log every production trace (execution trace).

## When NOT to use this skill
- Behavior changes every hour and has not yet converged.
- The task requires broad open-ended reasoning, not a narrow decision.

## Required inputs
- A frontier model deployed to run the task during the development phase.
- A system that logs every production trace (prompt + tool call executed).
- A prompt builder and serializer matching the live evaluator for byte-exact replay.
- An SLM candidate (e.g., Qwen3-8B) and a LoRA-tuning (low-rank adaptation) tool.
- A domain expert for blinded evaluation when the SLM and teacher disagree.

## Steps
1. Run the agent on the frontier model in production, collect every trace and live traffic feedback; change prompts quickly until behavior stabilizes (phase 1).
2. Once behavior has converged, replay each recorded batch byte-exactly using the same prompt builder and serializer as the live evaluator, producing the identical chat context as at serving time.
3. Pair each replayed context with the recorded tool call as the training target.
4. Apply contract filtering: drop training samples whose reasoning lacks a hard-conflict justification; deduplicate, keeping the most recent decisions; split train/validation by source batch.
5. LoRA-tune the SLM on the filtered training corpus (e.g., Qwen3-8B, ~1,023 optimizer steps, ~1B tokens, 65,536 max context).
6. Evaluate the SLM on the validation set: compute agreement with recorded decisions, compared to the teacher's noise floor (self-agreement on its own recorded prompts).
7. If the SLM beats the noise floor and passes blinded expert evaluation, deploy the SLM to serve production (phase 2).

## Expected output
- A fine-tuned SLM that performs the narrow task with higher agreement than the teacher, at significantly lower cost and latency, and judged more accurate by the expert.

## Example application
- Home-care agency: the agent makes a yes/no decision for each caregiver-shift pair, up to 1,000 decisions per outreach. After behavior stabilizes on GPT-5.4-nano, distill 11,621 production decisions into Qwen3-8B via LoRA → 0.913 agreement, 2.9s p50 latency, ~$0.28 per 1,000 decisions.

## Gotchas
- Do not distill too early before behavior stabilizes — the SLM will learn changing behavior and require retraining.
- Do not use synthetic data as the target — use real production traces to capture real edge cases.
- Base zero-shot SLM can produce malformed output (wrongly formatted results) in up to 23% of cases — not production-usable without fine-tuning.
- The teacher's noise floor is only 72.7% — do not expect the SLM to reach 100% agreement with the teacher; the goal is to exceed the teacher's natural self-consistency.
- All numbers above are offline replay; an online A/B test is needed before claiming real-world cost and accuracy.

## Self-check
- Can someone who has not read the original paper follow these 7 steps? [YES] — each step is a concrete action, no paper context needed.
- Which step is most vague? Step 2 (byte-exact replay) requires understanding your own system's prompt builder/serializer.
- Is the Input section sufficient? [YES] — frontier model, trace storage, replay tool, SLM, LoRA, expert evaluator are all covered.

## Dry run (hypothetical scenario)
- Scenario: A solopreneur wants to classify customer messages into "reply immediately" vs "can wait" across 5,000 messages per day.
- Run the skill: (1) Use GPT-5.4-nano to classify, log traces from 2 weeks of real operation; (2) adjust prompts based on customer feedback as soon as errors are spotted; (3) after 2 weeks behavior stabilizes, replay 10,000 recorded traces; (4) filter out samples without clear justification; (5) LoRA-tune Qwen3-8B on the remaining 8,000 samples; (6) evaluate on 2,000 validation samples against teacher self-agreement; (7) if SLM beats the teacher and the expert prefers the SLM on disagreements, deploy the SLM to replace GPT-5.4-nano, cutting cost to ~1/10.

## Verdict: [SKILL VALID]
