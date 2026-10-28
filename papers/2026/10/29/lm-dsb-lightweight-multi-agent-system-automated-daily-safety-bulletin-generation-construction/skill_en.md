# Skill: planner-researcher-writer-content-pipeline
Source: 2610.36433v1 (LM-DSB)
Type: framework / workflow

## When to use this skill
- You need to generate recurring domain documents (daily/weekly bulletins, reports, guides) from your own corpus on local hardware (GPU with 12-16GB VRAM) instead of paid APIs.
- Output must be grounded (based on real sources) with auto citation for compliance checking.
- Do NOT use when: the task is a single simple prompt with no multi-source need; or the task requires implicit multi-factor reasoning — a ≤8B model will fail, use a larger model + human review.

## Inputs needed
- Domain corpus: hierarchically organized documents (policy → procedure → spec), ideally ~30+ documents; a predefined list of "standard sections" the output must contain (LM-DSB uses 11).
- A locally deployable ≤8B-parameter model (pattern: Llama 3-8B-Instruct, MMLU 66.6%) + 12-16GB VRAM GPU + 32GB RAM.
- Ground truth: a few expert-authored sample documents (LM-DSB: 515-620 words each) to measure length ratio and lexical-overlap metrics.
- Evaluation kit: a 5-point Likert form (Accuracy, Completeness, Comprehensibility, Actionability, Compliance) + ~N=40 internal raters.
- Tooling: LangGraph (agent orchestration), ChromaDB (vector database), BGE embeddings BAAI/bge-large-en-v1.5 (768-dimension), GPT-4 (only for training-data synthesis, not production), LoRA + 4-bit quantization for fine-tuning.

## Steps
1. Analyze the corpus: map the hierarchy and cross-referential dependencies; define the N standard output sections and the required input context (LM-DSB: weather data + project info + topic).
2. Build the vector DB: chunk documents at 1024 tokens with 200-token overlap → BGE 768-dim embeddings → ChromaDB with metadata (filename, page, category). Set similarity threshold 0.65 with top-3 retrieval; tune the threshold by iterative testing (too low admits noise, too high drops critical detail).
3. Synthesize SFT data: segment with the "unstructured" library (4000-char max / 3800 threshold / 2000 min consolidation); group 3 segments → 6 QA pairs via GPT-4 at temperature 0 → attach ChunkIDs → expect ~300 examples per document (LM-DSB: 10,837 from 37 docs). Summarize tables/images via GPT-4-Vision.
4. LoRA fine-tune the ≤8B model (for domain fluency ONLY — do NOT expect added factual knowledge): 4-bit quantization, batch size 2, lr 5e-5, 3 epochs, gradient accumulation 4, cosine warmup 0.1, max samples 500. WARNING: standalone fine-tuning can score below the base model on small models (Llama-FT TF-IDF 0.4222 < Llama-Base 0.4870) — fine-tuning must always accompany RAG.
5. Orchestrate the LangGraph graph: Supervisor (routing + workflow state) → Planner (JSON plan of N sections + research queries) → Researcher (top-3 chunks + point-form summaries) → Writer (final Markdown). Enforce strict phase dependencies: each phase runs only after the previous completes; context must pass fully between phases — do NOT parallelize.
6. Two-phase evaluation: Phase 1 quantitative — TF-IDF, BLEU, ROUGE-1/2, length ratio vs ground truth (targets: length ratio ≥ 0.95, ROUGE-2 4-5× non-RAG); Phase 2 expert Likert 5 dimensions with ~N=40 raters (targets: compliance + accuracy ≥ 4.0; actionability is usually the weakest — plan improvements in procedural specificity and responsibility assignment).

## Expected output
- A domain-document pipeline producing complete documents (length ratio ≈ 1.01) with automatic citations to source file + page, running on consumer hardware, with expert-acceptable quality (mean 3.50-4.20 / 5).

## Example application
A Vietnamese solopreneur producing a "weekly real-estate market brief": corpus = 30 planning + legal reports; the planner generates 8 standard sections (prices, transactions, legal highlights, new projects, risks, recommendations...); the researcher retrieves top-3 chunks per section; the writer assembles the Markdown brief with source/page citations; running on an RTX 4070 Ti with zero API fees.

## Gotchas
- Running agents in parallel produces fragmented outputs because later phases lack complete inputs from earlier ones — LM-DSB deliberately enforces sequential phases; don't "optimize" by parallelizing.
- Fine-tuning alone (without RAG) performs worse than the base model on small models — always ground with RAG first.
- A mis-set retrieval threshold causes duplicated output or missing critical details — test around 0.65 on representative scenarios before fixing it.
- ≤8B models cannot synthesize implicit multi-factor risks (e.g., excavation + cold weather + diesel heating → CO poisoning) — multi-hazard bulletins need a final human review.
- Lexical metrics (TF-IDF/BLEU/ROUGE) only measure word overlap against a single ground truth — they cannot prove factual correctness; always pair with expert Likert evaluation.
- Auto-citation depends on metadata (filename, page) preserved from the chunking step — losing metadata means losing traceability.
