# 2610.27816 RAG-NIMBF: A Non-Invasive, Modular Benchmarking Framework for Automated RAG Configuration Analysis

## Problem
RAG practitioners face a vast configuration space (chunking, embedding, retrieval, reranking, prompting, generation models) with limited guidance on how components interact. Existing evaluation frameworks score a given pipeline rather than treating the configuration itself as the object of study.

## Contribution
- RAG-NIMBF: a non-invasive, modular benchmarking framework that attaches to existing RAG pipelines as an evaluation layer without modifying model or retriever internals. Evaluates configuration space through controlled ablation with end-to-end experiment tracking.
- Hybrid evaluation: combines LLM-based answer quality scores (RAGAS), retrieval correctness measures, and runtime indicators.
- Validated across multiple generation models on SQuAD (100-question sample). Reveals non-obvious interactions: MMR raises nDCG@5 by +4 to +11pp vs similarity search; detailed prompts raise faithfulness +10 to +13pp on capable/reasoning models (Qwen3.5-think +13pp, GPT-4o-mini +11pp, Qwen3.6-27B +10pp) but negligible on 20B generator.
- Local Qwen3.6-27B matches GPT-4o-mini at mean faithfulness 0.89; frontier reference does not dominate smaller generators on RAG-relevant metrics.

## Method
Six independent stages: configuration, data loading, chunking, retrieval, generation, evaluation. A declarative specification defines parameter ranges; the framework generates the cartesian product and benchmarks every combination. Intermediate artifacts (chunks, vector indices, retrieved contexts) are cached. All parameters and metrics logged to MLflow.

Three core principles:
1. Non-invasive integration: wraps existing RAG components without modifying internals; connects to Ollama and OpenAI-compatible endpoints via provider routing.
2. Systematic configuration exploration: exhaustive cartesian sweep instead of surrogate-based search, keeping interaction effects observable.
3. Hybrid evaluation: answer-quality, retrieval, NLG, and runtime metrics logged jointly to MLflow.

Configuration space: 6 LLMs × 2 chunking × 2 sizes × 2 overlaps × 2 retrieval × 2 templates = 192 configurations (study uses a smaller deliberate subset as controlled ablation).

Generation models: Qwen3-32B-AWQ (local), GPT-OSS-20B (DGX Spark), Qwen3.5-35B-A3B (GPU cluster), Qwen3.6-27B-NVFP4 (workstation), GPT-4o-mini (API), DeepSeek-V4-Pro (API). Critic: Qwen3.5-397B-A17B for RAGAS.

Metric layers: RAGAS (faithfulness), IR (context recall, semantic sim, Hit@k, Recall@k, nDCG@k), NLG (BERTScore-F1, METEOR, ROUGE-L, BLEU), Runtime (TTFT, TPS).

## KNOWLEDGE — Data & Concepts
- MMR raises nDCG@5 by +4 to +11pp (largest GPT-4o-mini +11pp: 0.68→0.79, Qwen3.5-think +10pp: 0.70→0.80, smallest GPT-OSS-20B +4pp).
- Detailed template raises faithfulness +10 to +13pp on cloud/large/reasoning models (Qwen3.5-think +13pp, GPT-4o-mini +11pp, Qwen3.6-27B +10pp); Qwen3-32B +7pp; GPT-OSS-20B +1pp.
- Mean faithfulness: GPT-4o-mini 0.89, Qwen3.6-27B 0.89, Qwen3.5-think 0.88, Qwen3-32B 0.83, GPT-OSS-20B 0.77. Best single config 0.96 (GPT-4o-mini).
- Global retrieval: nDCG@5 = 0.75, Hit@5 = 0.86, Recall@5 = 0.69.
- Qwen3.6-27B-NVFP4 leads local sequential throughput (127.5 TPS).
- 192 configurations in full sweep grid.

## INSIGHT — Mechanism & Why
[MMR balances relevance and diversity] happens BECAUSE MMR reduces redundancy in the retrieved set, providing a broader evidence mix. This means [smaller generators benefit from MMR's broader evidence, while stronger generators already ground well on the most similar passage and are diluted by additional context].
[Detailed prompts increase faithfulness] happens BECAUSE specific instructions ask for full-sentence answers with supporting reasoning, making answers adhere more closely to retrieved evidence. This means [faithfulness gain trades off against METEOR (10-22pp drop) because evidence-grounded answers diverge in surface form from short SQuAD references while staying semantically aligned].

## IDEA — Actionable Applications
1. Apply RAG-NIMBF to an existing production RAG pipeline: first step is to attach it as a non-invasive evaluation layer, define parameter sweeps for components (chunk size, retrieval strategy, prompt template, generation model), and track results in MLflow.
2. Apply multi-metric evaluation: first step is to track faithfulness, nDCG@5, and runtime simultaneously to avoid optimizing a single metric in isolation (e.g., optimizing METEOR alone would misleadingly favor under-specified answers).

## WISDOM — General Principle
Principle: In RAG configuration, no single metric suffices; answer quality, retrieval correctness, and runtime can move in different directions, so evaluation must use multiple metrics together. Use when: you need to systematically evaluate RAG configurations on consumer-grade hardware. Do NOT use when: you only need to score an already-fixed pipeline without sweeping the configuration space.

## Assumptions & Limitations
- Only evaluated on SQuAD (short, extractive, mostly single-passage QA); results may not transfer to long-document, multi-hop, noisy, or enterprise corpora.
- All quality assessments are automated, relative to the RAGAS critic.
- Prompt templates authored once and applied uniformly.
- Reranking, HyDE, and embedding-model comparisons left out; top-k and MMR λ fixed.

## Metadata
- Year 2026; authors: Niclas Hart, Nicolas Weeger (Ansbach University of Applied Sciences); category: cs.SE; PDF: https://arxiv.org/pdf/2610.27816v1; code: https://github.com/aiengineeringblueprints/RAG-NIMBF; citation count: [NO DATA — paper 2026-10-20]