# Skill: Distill CoT into Latent Tokens for Efficient Recommenders (OneLatent Recipe)
Source: 2610.30675
Type: framework (training + serving recipe)

## When to use this skill
- You run an LLM-based recommender/ranker that needs reasoning quality but has a tight latency budget (real-time serving).
- You already generate explicit chain-of-thought (CoT) rationales for ranking and find traces long, costly, with unclear quality gains.
- You want distillation (compressing teacher knowledge) from a large teacher LLM into a small student model for production.

## Prerequisites (must have)
- A large/stable item corpus to build a 3-level Semantic ID (SID — hashed item code) with Res-Kmeans.
- Access to a strong teacher LLM (e.g. Qwen3-235B-A22B-Instruct) for one-time offline supervision generation.

## When NOT to use
- Continuously changing item corpus (SIDs would need constant rebuilds → fragile).
- No GPU budget for the offline teacher pass → supervision quality collapses.
- The task is not ranking / generative retrieval (this recipe optimizes next-item SID prediction).

## Inputs required
- Interaction dataset (user profile Pu, history Hu, request context Cu, next item).
- Item metadata + embeddings for Res-Kmeans clustering → 3-token SIDs.
- Teacher LLM + 3-view prompt templates (Exploration / Evaluation / Attribution).
- Pretrained LLM backbone as the student FRM (paper uses Qwen3.5-0.8B/9B).
- Infrastructure: Redis cache, async gRPC inference service, behavior event stream (clicks/views).

## Steps
1. **Build item SID**: encode item multimodal info → 3-level Res-Kmeans → each item = 3-token SID [s(1);s(2);s(3)]; bidirectionally align SID ↔ dense caption: Lsem = −log p(S|C) − log p(C|S).
2. **Generate MV-ACoT supervision (offline)**: per sample, the teacher produces three views: (a) Exploration — profile+history only, outputs rationale + intent list (no candidate); (b) Evaluation — adds the positive item as privileged info, outputs rationale + 1–5 match score; (c) Attribution — adds the positive item, outputs rationale explaining which prior signals caused the interaction. Prompts tell the teacher to self-assess evidence complexity (strong behaviors, conflicting interests, weak signals, noise) and calibrate length: simple → converge fast; complex → multi-dimensional comparison. No separate difficulty classifier.
3. **Stage I — single-view alignment**: add 3 latent token IDs ⟨L1⟩⟨L2⟩⟨L3⟩ to the vocabulary; train the student to reproduce one retained view's rationale from prefix [Pu; Hu; ⟨view⟩; L] (view control token selects rationale type).
4. **Stage II — multi-view alignment**: use all views; average token losses within each output (long traces don't dominate); student prefix contains no candidate/target item even when teacher views used it (prevents privileged-info leakage).
5. **Stage III — context alignment**: connect the latent interface to next-item prediction: prefix [Pu; Hu; Cu; L] → predict target SID sequence.
6. **Curriculum post-training**: standard SFT ordered high→medium→low activity users (Dhigh→Dmedium→Dlow); then latent-reasoning SFT mixed 1:1 with standard SFT (½·LLR + ½·LSFT) to keep both modes strong.
7. **Inference**: append the 3 latent token IDs to the input and decode the 3-level SID directly — never generate rationale text. Reasoning overhead = 3 fixed tokens.
8. **Async serving**: keep the FRM off the request path; behavior events → value-aware admission (user value × behavior strength) → dedup scheduler with egress QPS cap → async gRPC inference → SID-to-item mapping → Redis cache; online path reads the cache and falls back to the previous result on delay. Deploy the FRM as a separate retrieval channel; its candidates merge with the incumbent pipeline and compete in the fine-ranking stage.
9. **Evaluate**: SID Hit@K / ID Hit@K (K ∈ {1,16,32,64}); codebook retrieval Hit@L1/2/3; QPS vs explicit-CoT baseline (target ≥10×); LLM-as-judge with a 9-dimension rubric on 100 samples per view; per-view reconstruction cosine (target ≥0.78); latent-token-count ablation (1 vs 2 vs 3 vs 4+, pick the plateau); online A/B 5%/5% for ≥7 days (impressions, ad spend, estimated revenue).

## Expected output
- A small student model (0.8B class) matching or beating the explicit-CoT teacher recipe on SID@64 with ~274 QPS (vs ~16 for CoT) — 17× throughput; ~3 s latency on 872-instance batches, on par with the no-think baseline; measurable A/B gains (paper: impressions +2.566%, ad spend +5.157%, estimated revenue +9.6%).

## Example application
- A Vietnamese content site wants "next article" suggestions. Steps 1–6 offline: a big LLM teacher generates 3-view rationales over 60K click logs; train Qwen3.5-0.8B with 3 latent tokens. Steps 7–8: on each new reader click, trigger an async rerank → cache top-10 in Redis → the suggestion API reads the cache (<10 ms) instead of invoking a reasoning LLM per request.

## Gotchas
- **Privileged leakage**: student prefixes in Stage I/II must never contain the target item / candidates, even though teacher views used them — otherwise latent tokens learn to "read the answer" instead of reasoning.
- **Token loss weighting**: average losses per output, don't sum — long traces would otherwise dominate training.
- **Latent token count**: 3 is the paper's sweet spot (1→3 improves; >4 yields no consistent gain); don't add more "for safety".
- **CoT ≠ better**: the Think checkpoint can underperform No-Think (paper: marginal 0.350→0.354 Hit@L1 at 17× latency) — benchmark both modes before investing.
- **Synchronous full-traffic serving is impossible**: OneLatent alone cannot meet sync latency budgets — async behavior-triggered serving is mandatory, not optional.
- **Reconstruction cosine ≠ faithfulness**: ≥0.78 cosine proves semantic association only, NOT a strict information bottleneck — don't claim "reasoning fully lives in 3 tokens".
- Curriculum order: high→low activity; reversing it trains on noisy low-signal users first → unstable.
