# [2610.30675] OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models

## Problem
- FRMs (foundation recommendation models) use LLMs as backbones; prior work (OneReason, RecGPT family) relies on explicit CoT (chain-of-thought) under a Think-then-Answer paradigm. Two gaps prior work fails to close: (1) overthinking — lengthy redundant traces even for clear-intent requests raise latency while bringing marginal gains; (2) interest drift — a fixed single-path reasoning template overweights dominant historical preferences, misses short-term context-dependent interests, and a single rationale error/hallucination propagates to the final output.

## Contribution
- Latent-Reason-then-Answer: compresses explicit reasoning traces into 3 learnable latent tokens (fixed token IDs shared by all samples, not sample-specific latent vectors) so reasoning-token overhead is constant, not proportional to trace length.
- MV-ACoT (Multi-View Adaptive CoT): teacher LLM Qwen3-235B-A22B-Instruct-2507 produces supervision from three complementary views (Exploration / Evaluation / Attribution) and adaptively calibrates reasoning depth from evidence complexity — no separate difficulty classifier, no hand-set threshold, no difficulty label.
- Production serving system: FRM deployed as a dedicated retrieval channel, kept off the online request path, with behavior-triggered value-aware refresh.

## Method (core)
- Each item = 3-token SID (Semantic ID) built with Res-Kmeans; LLM vocabulary extended with SID tokens plus 3 latent tokens; full-parameter updates; no added encoder/projector/decoder.
- Stage I (single-view alignment): student prefix [profile; history; view-token; L] reproduces one retained teacher view's rationale. Stage II (multi-view): all views; token losses averaged within each output so longer traces are not overweighted; student prefix excludes candidate/target item even though Evaluation/Attribution teachers used it (privileged supervision).
- Stage III (context alignment): same latent interface connected to next-item prediction [profile; history; context; L] → target SID. Post-training: curriculum SFT from high- to low-activity users (Dhigh→Dmedium→Dlow), then latent-reasoning SFT mixed 1:1 with standard SFT (Lpost = ½·LLR + ½·LSFT).
- Serving: streaming interactions pass value-aware admission (user value + behavior strength) → dedup scheduler with egress QPS cap → async gRPC inference → SID-to-item mapping → Redis cache; online path reads cache, falls back to previous result on delay.

## Key Findings
- Datasets: Kuaishou Locallife industrial (7 days: SFT 100,063 / CoT 59,113 / test 20,393) + public Kuaishou LLM-Rec benchmark (60,000 / 30,000 / 10,000). Backbones Qwen3.5-0.8B and OneLatent-9B; public runs initialized from OneReason-0.8B-pretrain-competition checkpoint.
- Industrial SID@64: +17.44% vs Think–OR and +9.33% vs No-Think–OR (identical checkpoint, differing only by control token). At K=64 vs strongest non-OneLatent per column: public SID +12.21%, public ID +19.10%; industrial SID +1.58%, ID +0.45%. 9B: SID@64 0.2008 vs 0.1857 (+8.13%).
- Inference (872 instances): explicit CoT 55.59 s / 15.68 QPS vs OneLatent 3.17 s / 274.29 QPS → 17.49× speedup, on par with UnCoT (274.56 QPS).
- Codebook retrieval Hit@L1: 0.354 (CoT) → 0.401 (OneLatent); Hit@L2 0.124→0.143; Hit@L3 0.043→0.071.
- Adaptive CoT cuts average trace length 35% (normalized 100→65) with ~0.92 mean semantic similarity on top-decile complex cases (Qwen3-Emb-8B). View-conditioned reconstruction cosine: 0.8027 / 0.8043 / 0.7878 over 2,000 samples.
- Online A/B (Sep 3–10, 2026, 7 days, 5%/5% traffic, Kuaishou local-services advertising): impressions +2.566%, ad spend +5.157%, estimated revenue +9.6% (global posterior estimator); subsequently rolled out to all production traffic.
- LLM-as-judge table (GPT-5.5, 9-dimension rubric, 1–5 scale, 100 instances/view): partially extracted; only the conclusion (multi-view complementarity) is used.

## Actionable Insights
- Measure before adding CoT: Think vs No-Think share one checkpoint; Think only nudges codebook Hit@L1 (0.354 vs 0.350) while costing 17× latency — never assume visible reasoning helps ranking; benchmark both modes. Example: test a no-CoT baseline first for newsletter content ranking.
- Distill rationales into latent slots when serving: generate teacher rationales offline, align them into 3–4 latent tokens, then serve a small model. Example: serve "next article" suggestions with Qwen3.5-0.8B instead of a live 235B reasoning model.
- Refresh a cache on behavior events instead of invoking the model per request: rerank on new click/view events (prioritizing high-value users), cache in Redis, fall back to stale results — recent behavior affects ranking immediately while GPU stays bounded. Example: precompute a user's top-10 content after each interaction.

## Assumptions & Limitations
- Requires a stable item corpus to build SIDs (Res-Kmeans) and a 235B-class teacher for offline MV-ACoT generation (large one-time cost).
- Paper-stated: reconstruction cosine is semantic association, not proof of a strict information bottleneck; all-parameter updates mean gains cannot be isolated to the latent-token positions vs the distributed backbone; QPS gains alone cannot meet synchronous full-traffic latency — the async serving architecture is mandatory.
- [MY OWN] A/B ran in one scenario only (local-services advertising); cross-domain transfer unproven; 7-day industrial data is not public; adaptive length is purely prompt-guided (teacher emits no difficulty label), so calibration depends on prompt engineering.

## Metadata
- 2026, Kuaishou Technology (Hao Jiang, Peiru Du, Pengfei Yao et al.), cs.IR, https://arxiv.org/abs/2610.30675, citation count: [NOT FOUND] (paper too recent)
