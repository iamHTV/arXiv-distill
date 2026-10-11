# [2605.31408v1] Skill Availability and Presentation Granularity in LLM Agents

## Problem
Skill documents provide procedural knowledge to LLM agents at inference time. But prior work has not clarified: does presentation granularity of skill knowledge change downstream task success? Specifically: low-abstraction checklist vs high-abstraction principles — which is better?

## Contribution
1. **Skill availability is the strongest signal**: Compared to no skill, skill conditions increase task-mean pass rate +26.7-36.0 pp (GPT-5.5) and +18.0-26.0 pp (DeepSeek V4-Flash).
2. **Presentation granularity effects are small and uncertain**: Low-abstraction vs high-abstraction: +0.7 pp (GPT-5.5), -6.7 pp (DeepSeek) — both 95% CIs cross zero.
3. **Worked examples have small effect**: Adding 1 worked example: +0.7-1.3 pp — too small for a design rule.

## Method (core summary)
Controlled experiment on SkillsBench: 30 oracle-validated tasks, 2 model configs (GPT-5.5, DeepSeek V4-Flash), 6 skill conditions (no skill, low/medium/high abstraction, with/without worked examples), 5 trials per cell. 1,800 rows total. Paired contrasts estimated over 30 tasks. Bootstrap confidence intervals.

## Key Findings
- Skill availability: +26.7-36.0 pp (GPT-5.5), +18.0-26.0 pp (DeepSeek) — largest signal
- Low vs high abstraction: +0.7 pp (GPT-5.5), -6.7 pp (DeepSeek) — both CIs cross zero
- Worked examples: +0.7-1.3 pp — small, directionally stable
- Mean-reward robustness checks preserve same conclusion
- DeepSeek with thinking mode: low-level instructions may duplicate/constrain planning

## Actionable Insights
1. **Skill availability > presentation format**: When building AI agents, prioritize HAVING skill documents over optimizing format. Having skills is better than no skills, regardless of presentation. Example: when deploying customer service agent, having procedural knowledge about products/processes matters more than presentation style (checklist vs principles).

2. **Don't over-optimize presentation granularity**: Low-abstraction vs high-abstraction has no reliable advantage. Choose whichever format is convenient, don't invest too much in presentation optimization. Example: when writing skill documents for AI agents, use natural format — no need to convert everything to checklists or principles.

3. **Worked examples have small positive effect**: Adding 1 worked example may help (+0.7-1.3 pp) but effect is small. Include when convenient, not a priority. Example: when writing documentation for AI coding assistant, add 1-2 examples — slight help but not a game-changer.

## Assumptions & Limitations
**Conditions for experiment to work:**
- 30 oracle-validated tasks — subset-specific
- 5 trials per cell — limited samples
- 2 model configs — limited generalizability

**Limitations the paper acknowledges:**
- Subset-specific magnitude — SkillsBench headline average differs
- Model versions, harness settings differ
- Source of larger magnitude unresolved

**Limitations the paper does NOT mention:**
- 30 tasks too few for robust conclusions
- Only 2 models — generalizability unclear
- No domain-specific skills tested
- No example number, length, similarity variations explored
- Reasoning mode effect is hypothesis only — not tested

## Metadata
- Year: 2026
- Authors: Xiaonan Xu, Wenjing Wu
- Category: cs.CL, cs.AI, cs.LG
- PDF: https://arxiv.org/pdf/2605.31408v1
- Citation count: [EXTRACTION FAILED]
