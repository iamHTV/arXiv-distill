# 2610.28909 DiffResearch: Accelerating Deep Research with Diffusion Language Models

## Problem
Deep research systems (systems that autonomously plan, gather evidence, synthesize, and revise long reports) today are almost all built on autoregressive language models (models that generate text left-to-right, one token at a time). This creates high end-to-end latency in planning and long-form writing, because each section is written sequentially and errors in early structural decisions propagate forward. Commercial systems such as OpenAI Deep Research, Gemini Deep Research, and Perplexity Deep Research share this problem.

## Contribution
- DiffResearch: an open-source multi-agent (multiple agents coordinating) deep research framework that places a diffusion language model (a model that generates text through iterative denoising, updating the entire sequence in parallel over a few steps) at the core of every stage. The backbone (the core generation model) can be swapped between diffusion and autoregressive within the same agentic scaffold (agent framework) for a controlled comparison.
- dFast: a fast decomposition mode (breaking a large query into subqueries — sub-queries) that reads intermediate denoising states to extract subqueries before generation finishes, achieving a 1.99× median speedup for decomposition in isolation without losing report quality.
- Leaderboard snapshot: a DiffResearch instance built on a stronger diffusion model (Mercury) ranks above several publicly listed commercial deep research systems.

## Method
The framework has 9 agents, each an instance of a diffusion LLM sharing a common backbone and implementing a single generate method. The backbone is interchangeable: google/diffusiongemma-26B-A4B-it for diffusion-native deployment, google/gemma-4-26B-A4B-it for the AR baseline. Five core stages: intent classification, query reformulation, planning, retrieval (searching external information sources), and writing, plus optional judging (quality assessment). Retrieval uses the Semantic Scholar API and Serper API, is deterministic (non-random), and has no LLM in the loop. Two operating modes: full (dFull) and fast decomposition (dFast). In full mode, the model runs to completion and the output is parsed as JSON. In fast mode, a custom streamer scans each intermediate denoising state and accepts a valid draft as soon as a JSON object with the exact requested number of subqueries appears.

## KNOWLEDGE — Data & Concepts
- Across 100 Deep Research Bench tasks (a benchmark of 100 PhD-level research tasks, 50 Chinese, 50 English, spanning 22 fields), the diffusion backbone is roughly 6× faster end-to-end than AR (mean 71.45s vs 11.89s, p90 111.87s vs 16.13/16.33s).
- Planning stage is 10.7× faster (39.32s → 3.6–3.7s), writing stage is 11.7× faster (59.78s → 5.1–5.3s).
- dFast extracts subqueries from intermediate denoising states: 1.99× faster at the median (243.4ms vs 484.9ms); the stable object matches the final answer in 91 of 100 cases.
- RACE quality (report evaluation scale, 0–1): dFast 0.3969, dFull 0.3895, AR 0.3904 — diffusion does not lower report quality.
- Public leaderboard: the Mercury-backed instance scores 48.03 (0–100 scale), ahead of OpenAI Deep Research (46.45), Dr. Tulu (45.49), and Claude Research (45.00).
- Source-grounded audit: only 28% of sampled claims were fully supported, 52% were not established by the stored source packet — retrieval grounding (grounding outputs in real sources) is a shared system bottleneck.

## INSIGHT — Mechanism & Why
[Diffusion backbone generates text through iterative denoising] happens BECAUSE diffusion updates the entire text sequence in parallel over a few denoising steps instead of generating token-by-token sequentially like AR. This means [model-bound stages such as planning and long-form writing are sharply reduced, while deterministic retrieval (not using a generative model) keeps its cost unchanged].
[dFast reads intermediate denoising states] happens BECAUSE diffusion emits drafts at intermediate steps of the denoising process, and for structured outputs like subquery lists, topical coverage matters more than exact wording. This means [queries can be dispatched for retrieval before generation finishes, but because decomposition is only a small fraction of total time, it does not reduce end-to-end latency].

## IDEA — Actionable Applications
1. Apply a diffusion backbone to an internal deep research / report-writing system: first step is to replace the current autoregressive LLM with a diffusion LLM (e.g. LLaDA, Dream, Mercury) while keeping the same agent scaffold, and measure latency before/after on the same task set.
2. Apply dFast to the search-query generation step: first step is to read intermediate diffusion states to extract subqueries early, dispatching retrieval calls in parallel instead of waiting for generation to complete.

## WISDOM — General Principle
Principle: Replacing the text-generation backbone is the fastest way to reduce latency in model-bound stages, but it does not solve retrieval quality or evidence sufficiency problems. Use when: latency is the main issue and retrieval is already stable. Do NOT use when: the problem is source accuracy or when the final output needs to be exactly correct word-by-word.

## Assumptions & Limitations
- Measured on an H200 pod (powerful GPU system) with local retrieval, Semantic Scholar only — results will differ on other hardware or tight consumer-grade latency budgets.
- Only one backbone pair (diffusiongemma-26B vs gemma-4-26B), not a broad sweep across model families and sizes.
- dFast does not reduce end-to-end latency in the current setup because retrieval is rate-limited to 1 request/second.
- Source-grounded audit is a small sample (10 reports), not sufficient for cross-mode comparison.
- Parallel retrieval dispatch is not evaluated.

## Metadata
- Year 2026; authors: Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov, Sergey Muravyov (ITMO University, Russia); category: cs.AI; PDF: https://arxiv.org/pdf/2610.28909v1; accepted to EMNLP 2026 Industry Track; code: https://github.com/alanrbtx/DiffResearch; citation count: [NO DATA — paper 2026-10-20]