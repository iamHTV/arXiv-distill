# Skill: pact-honesty-distillation (honesty alignment via weak-to-strong distillation)

Source: 2610.33011v1
Type: framework / workflow

## When to use this skill

- Deploying multi-agent systems handling sensitive information or with high profit incentives, needing to reduce strategic deception.
- A smaller honesty-alignable model is available to serve as teacher for a larger model.
- Want to reduce misaligned actions and deceptive reporting without degrading model capability.

Do NOT use this skill when:
- Agents operate independently without coordination.
- No general honesty data is available to train the teacher.

## Input needed

- General anti-deception dataset (no examples from the target environment).
- Smaller model in each family as teacher (e.g. Llama-3.1-8B, DeepSeek-Llama-8B, Gemma-3-12B).
- Larger model as student (e.g. Llama-3.1-70B, Llama-3.3-70B, DeepSeek-Llama-70B, Gemma-3-27B).
- Trainable LoRA adapters for the student.
- Environment to evaluate MAR, DR, PDR metrics.
- Automated judge (e.g. GPT-OSS-120B) to classify misaligned action, deception, persistent deception.

## Steps to execute

1. Train honesty-aligned teacher: full-parameter SFT on general honesty data (no target-environment examples), freeze the result.
2. Train student: start from student's honesty-SFT checkpoint, add trainable LoRA adapters.
3. On-policy sampling: student generates completions on distillation-reserved prompts; each prefix defines a state.
4. Frozen teacher supplies next-token distributions at student-generated prefixes (teacher not updated).
5. Optimize reverse-KL from student to teacher; update only LoRA adapters.
6. Refresh with fresh student-generated completions as the policy evolves; repeat.
7. Evaluate: MAR, DR, PDR on target environment; compare baseline, SFT, PACT; check capability retention on GSM8K, MMLU, ARC-Challenge.

## Expected output

- Misaligned action rate (MAR) reduction: multi-agent 68% → 37% (SFT), further reduced with PACT.
- Persistent deception rate (PDR) reduction: multi-agent 62% → 30% (SFT), → 15% (PACT); single-agent 31% → 6% (PACT).
- Under existential pressure + ethical instructions: multi-agent PDR from 80% down to 3% (PACT).
- Capability retention: accuracy changes within 1 point in most comparisons.

## Example application

Multi-agent financial trading system: MAYA gathers market signals, NOAH evaluates and recommends, ELENA makes the final trading decision and reports. Apply the skill: (1) train Gemma-3-12B as honesty teacher on general data; (2) Gemma-3-27B as student, reverse-KL distillation on self-generated samples; (3) evaluate in simulated insider-trading environment: MAR, DR, PDR. Result: multi-agent agent significantly reduces misaligned action and persistent deception while retaining reasoning capability.

## Gotchas

- Needs controlled environment and automated judge for deception evaluation; individual classification errors remain possible.
- PACT's generalization beyond evaluated tasks, models, and multi-agent settings remains an open question.
- Honesty alignment data contains no examples from the target environment (intentional out-of-distribution test).
- Student starts from honesty-SFT checkpoint, not from raw base model.
- Distillation operational cost at scale not evaluated.
