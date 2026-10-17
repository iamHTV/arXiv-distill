# Skill: Prompt Internalization — Fine-tune an SLM to Replace a Prompted Frontier Model
Source: 2610.10827v2 (Grammar Concept Annotation at Scale, Preply)
Type: workflow (data pipeline + fine-tuning + serving)

## When to use this skill
- A production feature is prompting a frontier model (GPT-class) with a long system prompt (thousands of tokens) and the cost exceeds the serving budget at scale.
- The task has a well-defined structured output (fixed schema: labels, spans, correctness flags) and a teacher model available to generate supervision.
- Do NOT use when: the task changes constantly (a prompt is more flexible than adapter weights); you lack GPU capacity to fine-tune/serve; the output is purely open-ended free-form generation.

## Inputs required
- A task schema contract: field definitions, output format (e.g., pipe-delimited lines), invariants (spans must be substrings of the input, explanation non-empty iff INCORRECT).
- Teacher model access (GPT-class) for review/re-annotation and synthetic generation.
- Sample production logs (production annotations) — tens of thousands of records.
- A base SLM (Qwen3.5-class 0.8B/4B), LoRA infrastructure, vLLM + autoscaling on single-GPU instances.
- Two human-curated golden benchmarks: one mirroring the production distribution, one error-enriched diagnostic set.

## Steps
1. Formulate the task as single-pass structured annotation: input pair (raw utterance, upstream correction) → a set of tuples (concept, exact span, correctness, explanation); define nested evaluation criteria L1 (label) / L2 (+exact span) / L3 (+correctness).
2. Review production data: uniform + heuristic sampling (prioritize anomalies — counts abnormal vs length, low span coverage); hybrid neuro-symbolic review — deterministic linguistic anchors (spaCy) + hand-crafted rules + word-level edit diff; a teacher-model full review/re-annotation pass (retain/correct/remove/add tuples); a deterministic post-validator enforcing invariants.
3. Synthetic enrichment for rare classes: structural backbones (label + correctness-flag sequences) from filtered production data; three sampling modes (uniform, error-weighted, smoothed inverse concept-frequency); inject error types into the generation plan (misuse, omission, confusable substitution) instead of post-hoc token corruption; teacher realizes; post-validate.
4. Consolidate: dedup across sources, remove every record overlapping the golden benchmarks. Target ~187k groups from ~190k raw.
5. Fine-tune with completion-only LoRA: pack 5 input pairs per conversation; high rank for the small model (r=128 for 0.8B); select checkpoints by minimum teacher-forced validation loss with early-stopping patience of 3 evaluations.
6. Prompt compaction: verbose teacher prompt (e.g., 3,810 tokens) → compact prompt (375 tokens, −90%) keeping only concept names + schema contract + brief rules; shrink max sequence (7,000 → 2,500).
7. Serve with vLLM autoscaled on single-GPU; packed requests; fall back to the teacher model on validation/service failure. Measure p95 latency and cost per request vs the baseline.
8. Evaluate: micro precision/recall at L1/L2/L3 on BOTH benchmarks; cluster bootstrap CIs; paired randomization test vs the teacher; LLM-as-a-judge for explanations BUT with human audit before concluding.

## Expected output
- The fine-tuned 0.8B beats the prompted teacher model at every matching level (paper: Golden L3 recall 78.89 vs 62.87; Golden2 80.88 vs 76.04, p < 0.0001).
- ~16× cost reduction (6.2% of baseline), p95 latency ~4.3 s, parse failure < 0.1% (vs 75–92% for the base model).
- Online A/B: engagement +15.8%, GMV from new lessons +13.2% (end-to-end feature).

## Example application
- A solopreneur runs a customer-support SaaS prompting GPT with a 4,000-token prompt to classify tickets and extract evidence spans. Applying the skill: review 50k labeled tickets, synthesize data for rare categories, LoRA fine-tune Qwen3.5-0.8B with a 400-token compact prompt, serve on 1 GPU with vLLM and GPT fallback. Expected: equal or better quality at ~1/16 the cost.

## Gotchas
- Raw teacher supervision is NOT enough: it degrades 23.6 pp when moving L1→L2 (exact span) — you need the review pass and post-validator, not just more generated data.
- An uncalibrated LLM judge favors its own teacher (99.06% vs 93.88%; after audit ≈95% parity) — always audit the judge before publishing comparative results.
- Small models need high LoRA rank (r=128) to hold the rules; an earlier-generation 0.6B can be 57% unparseable despite smooth validation loss — test format adherence separately, don't trust validation loss.
- Single training run, no seed variance — do not over-interpret small differences between configurations.
- The cost reduction counts recurring detection compute only — upstream work (transcription, correction, fallback) is not included.
