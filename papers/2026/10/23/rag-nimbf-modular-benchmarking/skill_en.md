# Skill: Non-invasive RAG configuration analysis (RAG-NIMBF)
Source: 2610.27816
Type: framework

## When to use this skill
- Need to evaluate an existing production RAG system without modifying the pipeline.
- Want to systematically sweep the RAG configuration space (chunk size, retrieval strategy, prompt template, generation model).
- Do NOT use when you only need to score an already-fixed pipeline without sweeping the configuration space.

## Input needed
- Existing RAG pipeline (or RAG components that can be wrapped).
- Declarative specification of parameter ranges for each component.
- Evaluation dataset (e.g. SQuAD or your own QA set).
- Model endpoints (Ollama, OpenAI-compatible, vLLM, TGI).
- MLflow for experiment tracking.

## Steps
1. Attach RAG-NIMBF to your existing RAG pipeline as a non-invasive evaluation layer (no modification to model or retriever internals).
2. Define parameter sweep ranges for each component (chunking strategy, chunk size, overlap, retrieval method, prompt template, generation model).
3. Run the cartesian product of all combinations and evaluate each run with the multi-metric suite (faithfulness, nDCG@5, Recall@k, TTFT, TPS).
4. Log all parameters and metrics to MLflow for reproducible results.
5. Analyze interaction effects across pipeline stages (e.g. chunk size × retrieval strategy, prompt template × model size).

## Expected output
- MMR raises nDCG@5 by +4 to +11pp vs similarity search.
- Detailed prompts raise faithfulness by +10 to +13pp on capable/reasoning models but negligibly on small (20B) models.
- RAG configuration space transformed into reproducible, comparable experiments.

## Example application
- Enterprise RAG system over internal documents: attach RAG-NIMBF, sweep chunk sizes 500/1000 and short/detailed prompt templates, select configuration with highest faithfulness at acceptable runtime.

## Gotchas
- Only evaluated on SQuAD (short, single-passage QA); may not transfer to enterprise corpora.
- All quality assessments automated, relative to RAGAS critic.
- Reranking, HyDE, embedding-model comparisons left out; top-k and MMR λ fixed.