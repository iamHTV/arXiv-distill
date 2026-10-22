# 2609.28007 Evaluating Open-Weight LLMs for Turkish Domain Documents Under Retrieval and Hardware Constraints

## Problem
Turkish-capable open-weight LLMs are evaluated on general-purpose benchmarks rather than long, structurally complex domain documents. Need to evaluate open-weight models for Turkish document QA under resource-constrained local deployment.

## Contribution
- Evaluates five open-weight 7B–8B models for Turkish document QA under local deployment on NVIDIA RTX 3050 (6 GB VRAM), 4-bit quantisation, 4096-token context window, served via Ollama.
- Primary benchmark: 100 systematically validated questions from a 109-page Turkish industrial R&D report; replicated on a 112-page public-sector report and an independent 100-question set.
- Principal methodological contribution: evidence-annotated evaluation protocol separating retrieval failure from downstream model reasoning failure without extra model calls.
- End-to-end accuracy ranges 49%–75%. Seven retrieval configurations compared with 95% Wilson intervals and paired McNemar tests; none significantly outperforms character TF-IDF baseline on either document. Evidence recall saturates differently across the two reports — retrieval and effective context capacity can be binding constraints for some documents but not others.

## Method
Five models: Trendyol-LLM-8B-T1 (8.2B, Turkish–English reasoning on Qwen3-8B), Qwen2.5-7B (7.6B multilingual), Cosmos Turkish-Llama-8B-Instruct (8.0B Turkish-adapted Llama), Mistral-7B (7.2B multilingual), Kocdigital-LLM-8B (8.0B Turkish-adapted Llama). All use Q4_K_M quantisation, temperature 0, fixed seed, local Ollama serving.

Primary benchmark: 109-page Turkish industrial R&D report PDF converted to layout-preserving text, sectioned and chunked (452 chunks). 100 questions in four capability bands: 30 Easy factual retrieval, 30 Medium numerical reasoning, 20 Hard multi-step, 20 Abstention (answer absent). Each question records expected answer, supporting evidence, and grading rule.

Secondary cross-document validation: 112-page Turkish Personal Data Protection Authority 2024 activity report (348 chunks), separate 100-question set, same procedure.

Evaluation protocol: retrieval executed once per question, context fixed across all five models. 3,500-character context budget. Grading is answer-type-specific (numeric, entity, keyword, Boolean, multiple-choice, date, abstention). Evidence recall measured independently of answer accuracy — a question counts as recalled only when all recorded source figures are present in retrieved context.

## KNOWLEDGE — Data & Concepts
- Overall accuracy: Trendyol-8B 75%, Qwen2.5-7B 65%, Cosmos-8B 54%, Mistral-7B 51%, Kocdigital-8B 49% (26-point spread).
- Secondary report: Trendyol 82%, Qwen2.5 65%, Cosmos 60%, Kocdigital 58%, Mistral 51%. Top 3 retain ordering.
- Abstention: Qwen2.5 19/20 (best), Cosmos/Trendyol 18/20, Kocdigital 9/20 (worst — unsuitable for factual report search where unsupported answers are costly).
- Latency: Qwen2.5 mean 1.69s/question (fastest), Trendyol 23.86s/question (slowest, ~14x slower). Trendyol answers average 207 chars after scratchpad removal vs 44 for Qwen2.5.
- Evidence recall: primary 57% (31/54; Easy 74%, Medium 43%, Hard 58%), secondary 91% (70/77; Easy 96%, Medium 93%, Hard 79%).
- Diagnostic budgets 7,000/9,000 chars raise primary recall to 72%/76%, secondary to 94%/95%.
- Retrieval: character TF-IDF 57% (primary), 91% (secondary); no retrieval alternative significantly outperforms (all p > 0.05).

## INSIGHT — Mechanism & Why
[Turkish-specialized models not necessarily stronger than multilingual] happens BECAUSE Qwen2.5 (multilingual) outperforms Cosmos and Kocdigital (Turkish-adapted Llama), showing Turkish-specific adaptation alone doesn't guarantee stronger document-grounded performance. This means [model selection needs to be evaluated on real Turkish document tasks, not just based on language-adaptation labels].
[Retrieval failure and model reasoning failure need separation] happens BECAUSE when a model answers wrong, either the model failed to reason over supplied evidence, or the retrieval system failed to provide it. Reporting only end-to-end accuracy silently charges the model for the retriever's misses, though the two failure modes need different remedies. This means [recording specific evidence each question depends on lets evidence recall be measured independently of model output, enabling error attribution to model vs retrieval apparatus].

## IDEA — Actionable Applications
1. Apply evidence-annotated evaluation protocol to enterprise document QA systems: first step is to record specific evidence supporting each question and measure evidence recall independently of answer grading, separating retrieval errors from reasoning errors.
2. Apply model selection based on empirical results rather than language labels: first step is to run a small experiment on target-language documents with candidate models and select the best performer.

## WISDOM — General Principle
Principle: Deploying local LLMs for domain documents in non-English languages requires separate evaluation of model selection, retrieval behavior, and hardware limits; language adaptation alone doesn't guarantee performance, and retrieval can be a binding constraint for some documents but not others. Use when: deploying local document QA systems with hardware constraints and sensitive data. Do NOT use when: cloud processing is acceptable or no target-language documents exist for evaluation.

## Assumptions & Limitations
- Primary benchmark based on one industrial R&D report; public-sector report is a cross-document robustness check, not a comprehensive multi-domain benchmark. Replication on legal, medical, and other sector documents needed before broader conclusions.
- Only five 7B–8B models evaluated on one specific hardware setting (RTX 3050, 6 GB VRAM).
- 4,096-token context window and 3,500-character budget can be binding constraints for some documents.

## Metadata
- Year 2026; authors: Imtiaz Ul Hassan, Ardhendu Behera, Swagat Kumar, Peter Matthew, Yonghuai Liu (Edge Hill University, UK), Öykü Akbulut, Onur Kaya (Ermetal Otomotiv ve Eşya San. Tic. A.Ş., Turkey); category: cs.CL; PDF: https://arxiv.org/pdf/2609.28007v1; citation count: [NO DATA — paper 2026-09-23]