# [2605.29668] GRASP: Gated Regression-Aware Skill Proposer for Self-Improving LLM Agents

## Problem
LLM agents fail in operational ways, not conversational ways. Reliability depends on procedural knowledge of the environment. Prior self-improvement methods accumulate natural-language guidance without checking that each new item preserves previously correct behavior — a note fixing one trajectory can silently regress another.

## Contribution
1. **GRASP**: Gated Regression-Aware Skill Proposer — treats agent improvement as edits to bounded skill library, admitting each candidate only if net improvement on balanced held-out probe under hard regression budget.
2. **Failure-Driven Skill Proposal**: Classifies failures by mechanism, generates grouped proposals.
3. **Frozen libraries transfer**: Skills from stronger model improve weaker executors — asymmetry no baseline reproduces.

## Method (core summary)
GRASP: (1) After each batch, classify failing traces by mechanism-specific failure mode; (2) Skill-writing model proposes ADD/MODIFY/REMOVE edits for most frequent modes; (3) Each candidate evaluated on held-out probe — admit only if net improvement under hard regression budget; (4) Skills = structured behavioral instructions: trigger condition, behavioral rule, verification step, contrastive example; (5) Library bounded — ADD blocked at capacity unless paired REMOVE frees slot.

## Key Findings
- MedAgentBench: gpt-oss-120b from 40.6% to 88.8% (+48.2 points)
- Exceeds strongest baseline by 21.0 points
- Improves every model by 17.2 to 40.3 points
- Gains from: comparative proposal generation, acceptance gate, hard regression budget
- Frozen libraries transfer: stronger → weaker improves, reverse doesn't
- Skill writing alone without validation = no better than no skills

## Actionable Insights
1. **Validate before accepting skills**: Don't accumulate guidance blindly. Test each skill on held-out probe before admitting. Example: when AI agent learns new skill, validate on previous tasks — if regresses → reject.

2. **Failure-driven proposals**: Classify failures by mechanism, not outcome. Example: "date_filter_omitted" not "wrong_answer" — mechanism-specific labels point to corrective actions.

3. **Frozen library transfer**: Skills from stronger model improve weaker ones. Example: develop skills on GPT-5, deploy on GPT-4.1 — weaker model benefits from stronger model's skills.

## Assumptions & Limitations
**Conditions for method to work:**
- Structured environments with verifiable tasks
- FHIR/state-based evaluation
- Held-out probe available

**Limitations the paper acknowledges:**
- Benchmark-specific, not clinical correctness
- Validation cost dominant (440 agent calls per batch)
- English-language FHIR only
- Skills need clinician review for clinical deployment

**Limitations the paper does NOT mention:**
- Open-ended action spaces don't benefit
- Probe size trade-off
- Skill library size management

## Metadata
- Year: 2026
- Authors: Johannes Moll, Jean-Philippe Corbeil, et al.
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.29668
- GitHub: https://github.com/jomoll/GRASP
- Citation count: [EXTRACTION FAILED]
