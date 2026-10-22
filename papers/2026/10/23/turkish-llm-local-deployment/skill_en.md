# Skill: Evidence-annotated evaluation protocol for local document QA
Source: 2609.28007
Type: workflow

## When to use this skill
- Deploying local document QA systems in non-English languages with hardware constraints.
- Need to separate retrieval errors from model reasoning errors.
- Do NOT use when cloud processing is acceptable or no target-language documents exist for evaluation.

## Input needed
- Domain documents in the target language (PDF, reports).
- Evaluation questions with supporting evidence recorded for each question.
- Candidate LLM models (7B–8B, 4-bit quantized).
- Retrieval system (character TF-IDF, BM25, dense, hybrid).
- Local hardware (GPU with limited VRAM).

## Steps
1. Convert documents to layout-preserving text, chunk, build retrieval index.
2. Build evaluation questions grouped by capability band (easy, medium, hard, abstention), each recording expected answer, supporting evidence, and grading rule.
3. Run retrieval once per question, keep retrieved context fixed across all models.
4. Evaluate each model with answer-type-specific grading rules (numeric, entity, keyword, Boolean, multiple-choice, date, abstention).
5. Measure evidence recall independently of answer grading — a question counts as recalled only when all recorded source figures appear in the retrieved context.
6. Attribute errors to model vs. retrieval apparatus based on evidence recall results.
7. Compare retrieval configurations with paired McNemar tests and 95% Wilson intervals.

## Expected output
- End-to-end accuracy, per-band accuracy, abstention score, evidence recall, latency.
- Separation of retrieval errors from model reasoning errors.

## Example application
- Turkish industrial document QA: record evidence for each question, measure evidence recall, discover retrieval is binding (57% recall on primary report), select model based on empirical results (Trendyol 75% accuracy but ~14x slower than Qwen2.5).

## Gotchas
- Language adaptation alone doesn't guarantee document-grounded performance (multilingual Qwen2.5 beats Turkish-adapted models).
- Retrieval can be binding for some documents (57% recall on primary) but not others (91% on secondary).
- No retrieval configuration significantly outperforms character TF-IDF baseline (all p > 0.05).