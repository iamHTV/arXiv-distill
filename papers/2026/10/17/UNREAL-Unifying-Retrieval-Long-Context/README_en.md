# [2610.08463v1] UNREAL: Unifying Retrieval and Long-Context with a Single Model

## Problem
- Long-context inference and Retrieval-Augmented Generation (RAG) handle evidence selection at vastly different scales — from a single long prompt to an entire corpus. Prior work does not address whether a single model-internal mechanism can select evidence across this range — the two approaches are studied as alternatives rather than two scales of one mechanism.

## Contribution
- UNREAL (UNifying REtrieval And Long-Context with a Single Model) — a model-native evidence selection framework spanning corpus retrieval and long-context inference.
- UNREAL encodes chunks and derives retrieval queries directly from the frozen LLM's internal representations.
- Adds fewer than 500K trainable parameters and leaves the backbone unchanged.

## Method (core summary)
- Builds on INTRA (Hoffer et al., 2026), but INTRA relies on a separate encoder and cross-attention, preventing direct application to decoder-only LLMs.
- UNREAL encodes candidate chunks and derives retrieval queries directly from the frozen LLM's internal states.
- UNREAL adds fewer than 500K trainable parameters, trained with contrastive loss, on top of the frozen LLM: a soft prompt that elicits retrieval mode and layer weights that combine internal states for evidence ranking.
- Because it reads from the residual stream, the same mechanism applies across dense-attention, linear-attention, and state-space architectures.
- At corpus scale: UNREAL retrieves from a 3B-token, 21M-chunk Wikipedia index.
- At long-context scale: UNREAL ranks chunks within a long-context prompt and returns only selected text to the same frozen LLM for answering.

## Key Findings
- 7 authors from NVIDIA and Technion, arXiv category: cs.CL.
- Wikipedia index: 3B tokens, 21M chunks.
- HotpotQA: recall 49.1% → 73.2%.
- 2WikiMultiHopQA: recall 31.7% → 60.1%.
- MuSiQue: recall 8.8% → 14.4%.
- NoLiMa: accuracy 1.0% → 24.83% at 128K tokens.
- LV-Eval: F1 49.97% → 54.66% at 256K words.
- UNREAL reduces FLOPs and time-to-first-token relative to full-context inference from ~32K tokens onward, with larger gains as context grows.

## Actionable Insights
1. Internal evidence selection can be applied across both corpus retrieval and long-context inference. Application: instead of two separate models (retriever + LLM), use one model to both rank evidence and generate answers.
2. Adding fewer than 500K trainable parameters on top of a frozen backbone can significantly improve evidence selection capability. Application: to add retrieval capability to an existing LLM, use UNREAL-style soft prompt + layer weights instead of retraining the entire model.

## Assumptions & Limitations
- Evaluated on 4 backbone models.
- Corpus is Wikipedia (3B tokens, 21M chunks).
- Long-context tasks: NoLiMa, LV-Eval, HELMET.

## Metadata
- Year: 2026, authors: Edan Kinderman, Elad Hoffer, Yochai Blau, Brian Chmiel, Ron Banner, Daniel Soudry, Boris Ginsburg (NVIDIA, Technion), arXiv category: cs.CL, PDF link: https://arxiv.org/pdf/2610.08463v1
