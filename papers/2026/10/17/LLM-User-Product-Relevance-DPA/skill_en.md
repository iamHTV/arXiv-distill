# Skill: Query-Free LLM Relevance Judge Pipeline
Source: 2610.14550
Type: evaluation-method (offline relevance metric for retrieval/ads without queries)

## When to use this skill
- Offline evaluation of retrieval/recommendation/ads systems with no explicit query (only engagement history)
- Need a metric that correlates with online KPIs (CTR/CVR) before running costly A/B tests
- LLM judging is too expensive to call on every event–candidate pair at production volume
- Do NOT use: search retrieval (has a query — use standard metrics), or small catalogs that do not need scaling

## Inputs required
- Engagement history H_u = {(product, event_type)} per user (view, add-to-cart, purchase...)
- Multimodal product embeddings (existing) + candidate set from retrieval
- Calibration split with human labels (enough for bootstrap)
- Teacher LLM (Gemini-2.5-Pro class) + a second verifier LLM + human auditors

## Steps
1. Compress history: assign each product a Semantic ID (SID) via RQ-kmeans (L=3 stages, 512-entry codebooks); group by (SID prefix, event type); representative = most recent product; weight w_g = log(1+|g|)·β(e_g) with β(purchase)=3, add-to-cart=2, others=1.
2. Agentic guideline discovery: seed prompt with 5-tier taxonomy (Exact/Similar/Substitute/Complementary/Irrelevant) with NO definitions → teacher labels calibration split → cluster misclassified pairs by confusion + rationale → reasoner proposes ≤3 sub-rules → accept iff paired-bootstrap 95% CI on Δaccuracy excludes zero and no per-class F1 regression >0.5pp; run multiple trials, keep only recurring rules.
3. Human business-alignment pass: audit 3 criteria (business-critical mismatches: demographics, regulated categories, advertiser exclusions; editorial standards; reproducibility on a 200-pair business-stratified sample); vetoed rules return to Phase A with a note.
4. Distillation: build corpus in 4 stages (stratified seed sampling; multi-source candidates: retrieval logs + conversion signals + advertiser groups; hard-case mining N=10/seed via multimodal embedding filter; teacher labels + rationales). Teacher + GPT-5-class verifier run in parallel; high-confidence agreement → accept, disagreement → human.
5. Fine-tune student (Gemini-2.5-Flash class): LoRA rank 16, lr multiplier 2, 5 epochs; multi-label classification + attribute-level rationale. Deploy the student as judge J.
6. Compute metric: MicroRel/MacroRel under threshold-k aggregation, k≈7 (peak [5,7]); validate Pearson vs online CTR/CVR/CP before using as a gate.

## Expected output
- An offline relevance metric correlating with conversion P/R, directionally aligned with CTR/CVR deltas; judge latency ~750ms p50, ~18 QPS (~9× faster than teacher); ~30× fewer LLM calls from SID compression.

## Example application
- App content recommendation: compress a 30-day interaction history into an intent set, judge each candidate content against intent tiers, use MicroRel as the gate before A/B testing a new feed algorithm.

## Gotchas
- Prompt-only student keeps teacher-like p95 tail (8,807ms) — you must fine-tune, not just prompt, to compress latency.
- Demographic rules are too rare in the calibration set for the agentic loop to prioritize — the human pass is load-bearing; do not skip it.
- Recency truncation (last 1-day) looks fine on online metrics (±0.03–0.06) but halves intent fidelity (Spearman 0.53) — do not use online metrics to choose the compression scheme.
- k too low (k=1) equates one weak intent match with broad coverage; k too high (>8) drops candidate pass-rate below 5%.
