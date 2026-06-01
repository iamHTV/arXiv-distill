# 2605.10235 Pre-Route: Activating Latent Routing Abilities of LLMs for RAG vs. Long-Context

## Problem

LLMs have 128K+ token context windows, but choosing between RAG (Retrieval-Augmented Generation) and LC (Long Context) is a critical decision. RAG is efficient but constrained by retrieval quality; LC enables global reasoning but is expensive and suffers position sensitivity (lost-in-the-middle). Existing method Self-Route uses failure-driven fallback: try RAG first, if model outputs "unanswerable" then fallback to LC. Problems: passive, redundant overhead, depends on model self-assessment (which can be wrong), low interpretability.

## Contribution

1. Propose Pre-Route — proactive routing framework: structured reasoning BEFORE answering to decide RAG vs LC. Uses lightweight metadata (document type, length, initial snippet) for task analysis, coverage estimation, information-need prediction.
2. Discover LLMs have latent routing ability — can be elicited with structured prompts, single-sample performance approaches Best-of-N.
3. Linear probes reveal structured prompts sharpen separability of "optimal routing dimension" in representation space.
4. Distillation transfers routing reasoning structure to smaller models for lightweight deployment.

## Method (core summary)

Pre-Route has 3 stages: (1) Metadata Collection — gather lightweight metadata: document type, length, head snippet; (2) Structured Routing Reasoning — LLM analyzes task requirements, estimates RAG snippet coverage, predicts information-need pattern, outputs routing decision (RAG/LC) with explanation; (3) Execute chosen strategy — if RAG: retrieve + generate; if LC: full context → model. 2 modes: Prompt-only (structured prompt guides LLM routing) and Distillation (transfer routing ability from large teacher to 1.7B student). Metadata variants: Full-Meta (type+length+snippet), Head-only (length+head snippet), Generated-Meta (LLM infers metadata).

## Key Findings

- Pre-Route outperforms Self-Route on LaRA (in-domain) and LongBench-v2 (out-of-domain) — higher QA score, higher route accuracy, lower LC reliance
- All improvements statistically significant: paired t-test p < 0.01, Cohen's d: 0.19-0.26
- Prompt-only routing with Qwen3-235B and DeepSeek-R1: structured reasoning prompts reliably elicit latent routing, higher accuracy than Self-Route
- Small models (1.7B) can't directly inherit complex routing — 74.3% of errors tilt toward "safer" LC option
- Distillation: large teacher → 1.7B student successfully acquires structured routing logic
- Head-only metadata (just length + head snippet) closes gap to Full-Meta — routing works with minimal metadata
- Pre-Route achieves superior cost-effectiveness: better accuracy per unit cost

## Actionable Insights

1. When building RAG systems, instead of always-RAG or failure-driven fallback, use a structured reasoning prompt for the LLM to decide which queries need RAG vs long-context. Example: "Analyze: is this question answerable from retrieved snippets or does it need full document context? Consider: information distribution, comparison needs, reasoning depth." Single prompt → better routing than complex fallback logic.
2. Distill routing ability from large model to small model — deploy 1.7B model with routing capability of 235B model. Example: edge deployment uses Qwen3-1.7B with routing distilled from GPT-5, reducing cost while maintaining routing quality.
3. Minimal metadata (length + head snippet) is sufficient for accurate routing — no expensive metadata extraction needed. Example: when user uploads document, just check file size and read first 200 tokens to decide RAG vs LC.

## Assumptions & Limitations

- Assumption: LLMs have latent routing ability learned during pretraining — may not be true for all models
- Limitation: Binary routing (RAG vs LC) — doesn't capture hybrid approaches (adaptive retrieval granularity)
- Limitation: Depends on metadata quality — performance degrades when metadata is absent or unreliable
- Limitation: English-only evaluation — not tested multilingual
- Limitation: Distillation requires strong teacher model — accessibility constraint
- Limitation (observed): Routing accuracy ≠ answer accuracy — correct routing but model can still answer wrong. Paper focuses on routing decision, doesn't address answer quality separately.

## Metadata

- Year: 2026
- Authors: Yiwen Chen, Kuan Li, Fuzhen Zhuang, Deqing Wang, Zhao Zhang, Liwen Zhang, Yong Jiang, Shuai Wang, Minhao Cheng
- Category: cs.CL, cs.AI
- PDF: https://arxiv.org/pdf/2605.10235
- Citation count: N/A
- Classification: [applied]
- Skill: pre-route-rag-lc-routing
