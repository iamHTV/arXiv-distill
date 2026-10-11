# Skill: Multi-Agent Debate Annotation
Source: 2506.00549
Type: workflow

## When to use this skill

- When evaluating complex LLM-generated content requiring nuanced judgment — single-pass evaluation insufficient
- When wanting to reduce human annotator cognitive load with structured arguments from multiple perspectives
- When detecting LLM evaluator self-bias — need cross-model evaluation with debate structure

- Do NOT use when: simple binary pass/fail; budget doesn't allow 3 LLM calls per eval; content too short

## Input needed

- Content to evaluate (summaries, code, answers)
- Source/reference materials
- Evaluation criteria
- 2-3 LLM models (ideally different to avoid self-bias)

## Steps

1. **Define Criteria** — Domain-specific: faithfulness, completeness, conciseness, or custom.
2. **Advocate** — LLM #1 argues FOR quality with evidence.
3. **Skeptic** — LLM #2 argues AGAINST with counter-evidence.
4. **Adjudicator** — LLM #3 resolves, scores per criterion.
5. **Human Review** — Presents debate to human for final decision.

## Expected output

- Higher annotation quality than single-pass
- Reduced annotator time (5 min vs 15 min per item)
- Self-bias detection

## Example application

Scenario: E-commerce product description evaluation. Advocate: accurate specs, appropriate tone. Skeptic: omits battery limitation, unsupported claim. Adjudicator: Completeness 85%, Faithfulness 90%, Conciseness 95%. Human validates → 5 min/item.

## Gotchas

- Model diversity: use 2+ different models
- Adjudicator balance: not too powerful to override valid arguments
- Cost: 3 LLM calls per eval
- Language: all agents must handle target language well
