# 2610.33029v1 Lessons from Luck: Do LLM-Written Lessons Carry Chance into an Agent's Next Decision?

## Core Value (1 sentence)
Lessons self-written from an agent's past runs can carry chance into later decisions — after a chance failure of the better tool, readers who received the lesson written from that failure chose the worse tool in 11.6% of next runs, over 29 times the 0.4% rate with a success-written lesson or an irrelevant item.

## Problem
Prior work on self-improving agents writes lessons from past runs and reads them before later runs. However, outcomes are noisy: a sound decision can fail by chance, and an unsound decision can succeed by chance. If a lesson-writing step turns one outcome into a durable rule, it could carry chance forward: a lesson written after a chance failure of a sound decision may tell later runs to abandon it. No prior work measured whether a chance-assigned outcome, with decision quality held fixed, gets written into a lesson that changes a later decision by a fresh session of the same model.

## Contribution
1. A registered study with 256 synthetic worlds, each a recurring operational task with two interchangeable tools of recorded reliability.
2. One link of the chain measured: a model writes a lesson from a scripted run; a fresh session of the same model reads the lesson and chooses the tool for the next run. 11 LLM endpoints gave 90,084 answers.
3. Finding: after a chance failure of the better tool, lessons carried luck (interaction +0.112 [+0.097, +0.126]): readers chose the worse tool in 11.6% of next runs with the failure-written lesson, vs 0.4% with an irrelevant item and 0.4% with the success-written lesson.
4. Two remedies evaluated: a three-sentence decision-quality note in the writing instruction lowered the worse-tool rate after chance failure to 7.5%; one instruction for both outcomes with a no-change option lowered it to 3.1%; neither met the harm-reduction rule at every endpoint that carried luck.

## Method
The pipeline has these main steps:
1. Each world provides 4 scripted previous runs: good decision or bad decision, crossed with success or failure. Two interchangeable tools differ only in recorded reliability (success rates 0.80–0.93 for better, 0.50–0.70 for worse).
3. A model writes a lesson from the run using one of three lesson-writing instructions: RB (ReasoningBank deployed), RBD (RB + remedy), N (one instruction for both outcomes).
4. A fresh session of the same model, holding the authoritative log and previous result, chooses the next run's tool with one memory item: that lesson, the lesson from the other outcome, an irrelevant item, or an unreasoned directive (PLANTED).
5. Primary contrasts P2 (good decision) and P3m (bad decision) — outcome-by-memory interaction.
6. Protocol frozen, deposited publicly on Zenodo, and timestamped with Bitcoin block before any confirmatory call.

## KNOWLEDGE — Data & Concepts
- Luck-carrying: a lesson written from a chance outcome changes the tool a fresh session would choose next, beyond what the raw outcome alone does.
- Outcome bias: judging a decision by its outcome rather than by the information available when it was made.
- Hindsight bias: knowing an outcome makes it seem more predictable than it was.
- ReasoningBank (RB): outcome-routed writing instruction — success instruction after success, failure instruction after failure.
- RBD (RB plus remedy): RB plus one added 3-sentence bullet judging the decision before the outcome.
- N (neutral): one instruction for both outcomes (outcome-specific phrases made neutral) with an explicit no-change option.
- 256 synthetic worlds, 16 domains with 16 worlds each.
- 11 LLM endpoints via OpenRouter: Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, GPT-6.1 Sol, GPT-6 Luna, Gemini 3.8 Flash, Grok 4.7, Qwen 3.8 Max, DeepSeek V4 Pro, Mistral Large 4, Kimi K3.
- 90,084 valid reader answers; 33,789 writer lessons.
- P2 (good decision): +0.112 [+0.097, +0.126] — luck-carrying detected.
- P3m (bad decision): +0.002 [−0.001, +0.005] — bounded below 0.10.
- Worse-tool rate after chance failure of better tool: 11.6% with failure-written lesson, 0.4% with irrelevant item, 0.4% with success-written lesson.
- Descriptive split: +0.042 in worlds stating failures are independent vs +0.181 in worlds not stating it.
- 6 endpoints carried luck (Qwen 3.8 Max +0.352, DeepSeek V4 Pro +0.277, etc.); 5 bounded below 0.10.
- Remedy RBD: P2 reduced −0.039, worse-tool rate 7.5%; Remedy N: P2 reduced −0.085, worse-tool rate 3.1%.

## INSIGHT — Mechanism & Why
- [Lesson outweighs the record] occurs because every reader held the authoritative log showing the better tool remained better, and was told the previous run's result. When the log and previous-run line are the evidence, a matched lesson adds no observation the reader lacks, so for a reader knowing the lesson's source, matched contrasts have normative value zero. Yet the lesson together with the reported failure raised worse-tool rate from 0.4% to 11.6%. This means a lesson can outweigh the record it summarises.
- [Most of the effect where the record leaves room for doubt] occurs because interaction was +0.181 in worlds whose log did not state failures are independent, vs +0.042 in those that did. When independence is not stated, a recent failure can be read as a sign of a current fault, so choosing the worse tool is a deviation from the log-based benchmark rather than a clear error. Stating independence in the record reduces the effect (descriptive, not a test).
- [Outcome-routed writing needs testing] occurs because ReasoningBank's failure instruction asks the writer to "reflect and think why the trajectory failed", propose "strategies to prevent the failure", and prefer "concrete, actionable recovery procedures", presupposing something was at fault and inviting a change of action. After success, the log itself argues against the worse tool. This means memory-writing pipelines need testing with chance outcomes before deployment.

## IDEA — Actionable Applications
1. Apply luck-carrying testing to your self-improving agent's memory-writing pipeline: before deploying a lesson-writing instruction, run a test with chance outcomes (decision quality fixed) to see whether the lesson moves the next session's decision. First step: create a test with two tools of different reliability, script one run with a good decision and chance failure, then check whether the failure-written lesson makes the next session choose the worse tool more often.
2. Add a three-sentence decision-quality note to your lesson-writing instruction: before writing, ask the agent to judge whether the decision was sound given only pre-outcome information, and recommend a different action only if the decision was unsound. First step: insert the 3-sentence paragraph into your agent's memory-writing instruction, right before the lesson-writing question.
3. Use one instruction for both outcomes with a no-change option: the writing instruction does not depend on the outcome and includes "If nothing about how the task should be done needs to change, say so." First step: replace separate success/failure writing instructions with one unified instruction that has an explicit no-change option.

## WISDOM — General Principle
- Principle: Lessons self-written from chance outcomes can outweigh the authoritative record — before saving a lesson to memory, check whether the decision was sound given pre-outcome information.
- When to use: When designing self-improving agents that write lessons from past runs and read them before later runs.
- When NOT to use: For systems that do not write memory from past runs (read-only agents, non-self-improving agents).

## Assumptions & Limitations
- Required condition: Each world must have two interchangeable tools with recorded reliability; the log must show success rates of each tool over 180–365 previous runs.
- Paper-acknowledged limitations: Measures one link of the chain (one stored lesson, read once, after one scripted previous run); does not execute self-improvement, retrieval, or accumulated memory; does not estimate how often real agents encounter such situations; remedies tested only with outcomes that did not signal a change in tool reliability.
- Limitations the paper does NOT state: Cannot separate the lesson's advice from a second report of the failure — no reader saw the lesson without the previous-run line, and no memory item restated the failure without a lesson.

## Metadata
- Year: 2026
- Author: Kazuki Nakayashiki
- arXiv category: cs.LG
- PDF link: https://arxiv.org/pdf/2610.33029v1
- Classification: [applied]