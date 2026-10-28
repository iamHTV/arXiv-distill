# 2610.36433v1 LM-DSB: A Lightweight Multi-agent System for Automated Daily Safety Bulletin Generation in Construction

## Core Value (1 sentence)
A planner-researcher-writer agent hierarchy running on a local Llama 3-8B model achieves document completeness (output/ground-truth length ratio) of 1.01 while single-agent RAG reaches only 0.39 — proving task decomposition compensates for the parameter limits of small models on grounded document-generation tasks.

## Problem
Prior work in construction-safety NLP across three eras — rule-based expert systems (1990s-2010s), data-driven perception systems (BIM, IoT sensors, risk prediction, 2010s-2020), and AI generative systems (2020-present) — all stopped at classification, compliance checking, and incident analysis; none automated Daily Safety Bulletin (DSB) generation. DSBs are currently written manually, taking 2-3 hours daily, with quality dependent on the superintendent, and 25% of crews never conduct pretask planning at all (Olson et al., 2016). US construction in 2024: 1,075 fatalities ≈ 20% of all workplace deaths; fatal injury rate 9.6 per 100,000 FTE workers, nearly triple the national average (BLS 2024). Existing LLM solutions rely on commercial ≥70B-parameter cloud APIs inaccessible to most construction firms. Gap: no system has empirically isolated the contributions of fine-tuning, RAG, and multi-agent orchestration under consumer-hardware deployment constraints in a controlled comparison.

## Contribution
1. First system to automate DSB generation — distinct from all prior analysis/retrieval/compliance work.
2. Controlled 4-configuration comparison (Llama-Base, Llama-FT, Llama-RAG, LM-DSB) across 3 standardized scenarios, isolating each component's contribution — never done before in this domain.
3. Feasibility proof on consumer-grade hardware (Intel i5-13600KF, RTX 4070 Ti 12GB VRAM, 32GB RAM) — no datacenter GPU required.

## Method
The LM-DSB pipeline has three components:
1. Multi-agent architecture on LangGraph: a Supervisor agent (routes requests, maintains workflow state, passes context between phases) → Planner agent (receives real-time weather data + project info + user-specified topic; outputs a JSON plan covering 11 standard DSB sections plus targeted research queries) → Researcher agent (queries the vector database for top-3 chunks and compiles point-form safety summaries prioritizing critical information) → Writer agent (integrates the planner draft with research into the final DSB in Markdown, concise and professional for site workers). The workflow enforces strict phase dependencies: the researcher cannot start before the planner finishes, and the writer cannot generate before research completes — preventing fragmented outputs.
2. RAG implementation: 37 HSE (health, safety, environment) documents chunked at 1024 tokens with 200-token overlap, encoded with BGE embedding model BAAI/bge-large-en-v1.5 (768-dimensional vectors), stored in ChromaDB with metadata (source filename, page number, category). Retrieval uses similarity threshold 0.65 and top-3 chunks; the threshold was tuned by iterative testing — lower admits noise, higher excludes critical details. Preserved metadata enables automatic citation of source documents for regulatory verification and compliance traceability.
3. Domain fine-tuning: base model Llama 3-8B-Instruct chosen for the highest MMLU (Massive Multitask Language Understanding, 57 subjects) among deployable ≤8B models — 66.6% (5-shot) vs Gemma-7B 64.3%, Mistral-8x7B MoE 70.6% (but 46.7B params too large), Phi-3-mini 3.8B 68.1% (too small to fine-tune well). SFT (supervised fine-tuning) with LoRA (Low-Rank Adaptation, 99.8% fewer trainable params) + 4-bit quantization: batch size 2, learning rate 5e-5, 3 epochs, gradient accumulation 4 steps, cosine scheduler with 0.1 warmup, LoRA+ ratio 16, max gradient norm 1, max samples 500. Training-data pipeline: the "unstructured" library segments documents (4000-char max, 3800 new-segment threshold, 2000 min consolidation); segments grouped in threes produce 6 question-answer pairs each via GPT-4 at temperature 0 → 10,837 training examples with ChunkID traceability; tables/images summarized via GPT-4 / GPT-4-Vision.

## KNOWLEDGE — Data & Concepts
- Corpus: 37 HSE documents — 3 core policy documents (1,240 pages, 313,958 words), 23 operational procedures (44 pages, 989 words), 11 PPE specifications (13 pages, 9,432 words).
- Phase 1 benchmark on 3 scenarios (crane operations in extreme cold; trenching + confined-space entry; hazardous energy control + compressed gas); ground-truth DSBs of 515-620 words authored by domain experts.
- Table 8 (4 metrics): LM-DSB TF-IDF 0.6960 / BLEU 0.3898 / ROUGE-1 0.6570 / ROUGE-2 0.4086; Llama-RAG 0.6292 / 0.2731 / 0.4804 / 0.3781; Llama-FT 0.4222 / 0.0814 / 0.3631 / 0.0651; Llama-Base 0.4870 / 0.1124 / 0.4099 / 0.0767.
- Length ratio (output words / ground-truth words): LM-DSB 1.01 vs Llama-RAG 0.39 — single-agent RAG produced only ~1/3 of expected content.
- LM-DSB vs Llama-RAG: TF-IDF +11%, BLEU +44%, ROUGE-1 +38%. RAG configurations' ROUGE-2 is 4-5× non-RAG (0.41/0.38 vs 0.08/0.07).
- Surprise: Llama-FT ranked BELOW Llama-Base on all 4 metrics (TF-IDF 0.4222 vs 0.4870) — narrow-domain fine-tuning degrades general generative capability on small models (Gekhman et al., 2024); also, lexical-overlap metrics underestimate fine-tuning's contribution.
- Phase 2 expert evaluation (N=40 construction-management professionals, 5-point Likert scale): Regulatory Compliance 4.20 (SD 0.65), Factual Accuracy 4.10 (SD 0.55), Completeness 3.98 (SD 0.62), Comprehensibility 3.77 (SD 0.86), Actionability 3.50 (SD 0.91) — lowest, with gaps in procedural specificity and responsibility assignment.
- Case studies: Case 1 (crane ops at -25°C) integrated weather + regulatory data well but hit corpus blind spots where documents were missing; Case 2 (trenching + cold + diesel heating → carbon monoxide buildup) — the 8B model failed to synthesize implicit connections despite having documents for each factor; Case 3 (hazardous energy control) — fine-tuning helped extrapolate cold-weather equipment risks from sparse documentation, but temporal reasoning stayed vague.

## INSIGHT — Mechanisms & Why
- [Multi-agent decomposition compensates small-model capacity] happens BECAUSE each specialized agent operates on complete inputs from the previous phase, splitting task complexity below the context-window limit of a single model. This means the completeness gap 0.39→1.01 is orchestration's contribution, not fine-tuning's or RAG's alone.
- [RAG provides factual grounding; fine-tuning only fluency] happens BECAUSE RAG injects real regulatory text at inference time while fine-tuning only internalizes terminology and reasoning patterns; standalone fine-tuning on small models can even degrade general capability. This means priority order: RAG grounding first, fine-tuning second for domain conventions.
- [Implicit multi-factor synthesis remains a hard boundary for 8B] happens BECAUSE synthesizing implicit hazards (A+B+C → D) requires inferential reasoning beyond adaptive retrieval — Case 2 failed despite successful per-component retrieval. This means architecture cannot replace unlimited parameter capacity; human-in-the-loop is needed for multi-hazard scenarios.

## IDEA — What to Apply
1. Apply the planner-researcher-writer pipeline to your content automation (weekly newsletter, client reports, market briefs): split the job into three specialized agents with strict sequential phases instead of one giant prompt. First step: write a JSON schema for the planner listing the standard sections of the document you produce (mirroring the DSB's 11-section pattern).
2. Use the QA-pair synthesis pipeline to build SFT data from your own documents: group 3 text segments → 6 QA pairs (GPT-4, temperature 0) → attach source chunk IDs. First step: convert your domain documents (contracts, procedures, SOPs) into a training set of a few thousand examples following the paper's 10,837-examples-from-37-documents recipe.
3. Run RAG-first before considering fine-tuning: 1024-token chunks + 200-token overlap + 0.65 similarity threshold + top-3 retrieval on a local vector DB, with metadata for auto-citation. First step: set up ChromaDB + BGE embeddings on a 12-16GB VRAM PC and test against one document you wrote manually as ground truth.
4. Evaluate budget with a 5-dimension Likert rubric (accuracy, completeness, comprehensibility, actionability, compliance) using ~N=40 internal raters, not just automatic metrics; measure actionability first — it is consistently the weakest dimension (3.50/5 here).

## WISDOM — General Principles
- Principle: "Decomposition returns capability that parameters cannot" — on grounded document generation, specialized orchestration lets an 8B model reach expert-level output completeness, but only up to explicit knowledge; implicit synthesis still needs larger models or human review.
- Use when: generating domain documents with citation/compliance requirements on local, low-cost hardware.
- Do NOT use when: the task requires implicit multi-factor reasoning (e.g., combined risk assessment) — require human review or a larger model.

## Assumptions & Limitations
- Conditions that must hold: the domain corpus must have hierarchical structure (policy → procedure → spec) and cross-referential dependencies for the multi-agent design to pay off; minimum 12-16GB VRAM for Llama 3-8B in 4-bit.
- Limitations the paper acknowledges: single-organization knowledge base (limits generalizability); English-only (Llama 3-8B constraint); validation under controlled experimental conditions, not longitudinal field deployment; the 8B model's inferential-reasoning limits when synthesizing implicit multi-risk connections.
- Limitations the paper does NOT state: (a) the experimental design cannot fully isolate fine-tuning vs orchestration effects within LM-DSB — the paper admits this yet still concludes orchestration is dominant based on the length-ratio gain, which is not fully controlled; (b) end-to-end latency is never reported — a 4-agent sequential workflow may be much slower than implied; (c) TF-IDF/BLEU/ROUGE measure lexical overlap against a single ground truth, not actual factual correctness — the N=40 expert evaluation is the real quality evidence.

## Metadata
- Year: 2026 (arXiv 2026-10-27)
- Authors: Xianxiang Zhao (University of Washington), Advik Mehta (University of Alberta), Falak Sethi (PCL Industrial Management), Brian Gue (PCL Industrial Management), Qipei Mei (University of Alberta), Lingzi Wu (University of Washington)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.36433v1
- Citation count: [NOT FOUND — Semantic Scholar API rate-limited at distill time; paper published Oct 2026]
- Classification: [applied]
