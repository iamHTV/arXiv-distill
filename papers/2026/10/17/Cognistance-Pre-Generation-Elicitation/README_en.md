# 2610.09593 — Structured Pre-generation Elicitation vs Single-shot Prompting in AI-assisted Enterprise Decision-making

## Problem
- "Cognitive surrender": users delegate both production and evaluation of AI output, accepting weak results and engaging less with the reasoning. Prior interventions (unassisted practice, slowing adoption) sit OUTSIDE the working task — they do not fix the interaction itself.

## Contribution
- First RCT testing a metacognitive scaffolding layer integrated INTO the task: before the AI generates, the user answers clarifying questions, selects a strategic direction, and explains the reasoning
- Cognistance (OCIR prototype): 3 clarification questions + scaffold cards + free-text rationale feeding a synthesis step

## Method
- RCT on Prolific: 400 sessions (196 control / 204 treatment), simulated enterprise data-sovereignty crisis (Apex Global launching in Singapore/Malaysia; regulators demand domestic servers; centralised Frankfurt cloud). Control: single prompt → Gemini 3 1 Pro action plan. Treatment: the 3-step scaffold.
- Deliverables scored on 4 dimensions (1–10 each, total 4–40): strategic coherence, technical/regulatory specificity, trade-off articulation, information density. Raters: ChatGPT 6.1, Claude Sonnet 5.5, one human — all blind to condition.

## Key Findings
- Composite quality +32.2% (15.48→20.48; +4.99, 95% CI [4.03,5.96], d=1.02); same direction for every rater (ChatGPT +7.19, human +9.15, Claude +2.79).
- Gains concentrate in trade-off articulation (+1.90, d=1.57), strategic coherence (+1.94, d=1.28), information density (+0.89); technical specificity does NOT improve (+0.26, p=.300).
- Rescues weak prompts: floor-scored (off-task) deliverables fell 34.2%→4.9% (~59% of the aggregate effect). Participants whose own prompt already stated the problem still gained +20.9% (d=1.15).
- Involvement d=0.59, effort d=0.36, +2.4 minutes (10.46 min average). Self-rated quality did not track rated quality in either condition.

## Actionable Insights
- Elicit before generating: 3 questions (operational priority, infrastructure, audience) + posture choice + written rationale before AI drafts — apply to any content/strategy workflow: never single-shot prompt; insert one structured elicitation step.
- The scaffold rescues bad prompts but still helps good prompts (+20.9%) — not just for weak users; trade-off articulation is the most improved dimension.
- Do not trust self-ratings: user self-assessment does not correlate with rated quality — use an objective rubric with blind raters instead of asking users "was it good".

## Assumptions & Limitations
- Whole-workflow comparison — cannot isolate which component contributes; no unaided arm, no AI-alone arm, no faulty-output trials.
- Domain-specific rubric written by the study team; it names a split architecture as an example (overlapping a scaffold option) — mechanical bias.
- Immediate recall only (not robust to sensitivity); Prolific professionals, simulated task; 165/204 treatment chose the same posture → narrowed output diversity.

## Metadata
- 2026, William Scott-Jackson (Oxford Centre for Impact Research), cs.HC/cs.AI, working paper, https://arxiv.org/pdf/2610.09593
