# Skill: Multi-Agent Debate Annotation
Source: 2506.00549
Type: workflow

## Khi nào dùng skill này

- Khi cần annotate/evaluate LLM-generated content (summaries, code, answers) mà quality judgment phức tạp, cần nuanced reasoning — single-pass LLM evaluation không đủ
- Khi muốn giảm human annotator cognitive load bằng cách cung cấp structured arguments từ nhiều perspectives
- Khi phát hiện LLM evaluator có self-bias — cần cross-model evaluation với debate structure

- KHÔNG dùng khi: evaluation task đơn giản (binary pass/fail); budget không cho phép 3 LLM calls per evaluation; content quá ngắn (debate overhead không worth it)

## Input cần có

- Content to evaluate (summaries, code, answers)
- Source/reference materials
- Evaluation criteria (faithfulness, completeness, conciseness, or domain-specific)
- 2-3 LLM models (Advocate, Skeptic, Adjudicator — ideally different models to avoid self-bias)

## Các bước thực hiện

1. **Define Evaluation Criteria** — Xác định domain-specific criteria. Ví dụ summarization: faithfulness (no hallucination), completeness (all key info), conciseness (no redundancy). Ví dụ code review: correctness, readability, security.

2. **Advocate Phase** — LLM #1 (Advocate) reads source + generated content, argues FOR quality: "The summary correctly captures X because... The faithfulness is maintained because..." Output: structured argument with evidence.

3. **Skeptic Phase** — LLM #2 (Skeptic) reads same materials + Advocate's argument, argues AGAINST: "The summary misses Y... Hallucination detected in sentence Z because source says..." Output: structured counter-argument.

4. **Adjudicator Phase** — LLM #3 (Adjudicator) reads all arguments + source, makes final judgment: scores per criterion, resolves conflicts, notes which argument is stronger. Output: final scores + reasoning.

5. **Human Review** — Present structured debate (Advocate + Skeptic + Adjudicator) to human annotator. Human makes final decision informed by debate. Reduces cognitive load: human evaluates arguments rather than reading entire source from scratch.

## Output mong đợi

- Higher annotation quality than single-pass evaluation
- Reduced annotator time per item (structured arguments guide focus)
- Self-bias detection: if evaluator model == generator model, flag for cross-check

## Ví dụ áp dụng

Scenario: E-commerce company evaluates product description quality. (1) Advocate: "Description accurately lists specs matching product data sheet, uses appropriate tone for target audience"; (2) Skeptic: "Description omits battery life limitation mentioned in manual, uses subjective claim 'best in class' without evidence"; (3) Adjudicator: "Completeness: 85% (missing battery caveat), Faithfulness: 90% (specs accurate), Conciseness: 95%"; (4) Human reviewer quickly validates Adjudicator's assessment → 5 min/item vs 15 min without debate.

## Gotchas

- Model diversity matters: if all 3 agents are same model, debate may converge too quickly. Use 2+ different models.
- Adjudicator power: if Adjudicator is too strong, it may override valid arguments. Balance Adjudicator capability with Advocate/Skeptic.
- Cost: 3 LLM calls per evaluation. For large-scale eval, use cheaper models for Advocate/Skeptic, stronger for Adjudicator.
- Language: debate quality depends on LLM capability in target language. For non-English, ensure all 3 agents handle the language well.
