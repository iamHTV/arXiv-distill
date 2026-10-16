# Skill: ReST Rec-Native Transformer Scaling
Source: 2609.01240
Type: framework (kiến trúc + system co-design cho production ranking sequence model)

## Khi nào dùng skill này
- Scale behavior-sequence Transformer cho production ranking (CVR/CTR prediction) dưới latency budget chặt (P99 ~50ms)
- Sequence module hiện tại yếu hoặc bão hòa sớm khi scale depth/width, hoặc context dài thêm không cải thiện (dấu hiệu sequence starvation)
- KHÔNG nên dùng: task không có behavior sequence (chỉ static features); retrieval-stage model không phải discriminative ranking

## Input cần có
- Behavior sequence S_u = [(item, timestamp)] per user + non-sequential user/context features
- Production DLRM ranker làm baseline (đã optimized: fused kernels, mixed precision)
- Latency budget (P99) + offline AUC Δ measurement (0.05% đã meaningful)

## Các bước thực hiện
1. Chống sequence starvation: thêm auxiliary sequence CVR loss + sequence/non-sequence alignment objective (training-only, zero inference overhead) trước khi scale — nếu không main loss bị shortcut qua non-sequential branch.
2. Build rec-native encoder T (LLaMA-style base): (a) DGA — value gate σ(XW_gv)⊙(XW_V) trước attention + output gate σ(XW_go) sau, bounded sigmoid (KHÔNG dùng unbounded SiLU — diverge ở scale); (b) RoPE+RoTE — chia heads: Hpos RoPE ordinal, Htime RoTE bucketized timestamp τ_h (giây→phút→ngày→tuần); (c) SRN — Mix-LN depth-dependent + learnable scalar α_l nhỏ trên mỗi residual branch.
3. Factorize asymmetric: encoder T nặng chạy 1 lần/user history → memory; cross decoder C nhẹ: projection-free KV attention + token-specific parameterization cho N candidate.
4. System co-design: user-level shared-prefix training (amortize prefix computation qua samples cùng user → ~5.8× throughput) + shared-prefix serving (T executed once per request, reuse across candidates → ~20× inference cost reduction).
5. Scale verify theo 3 axes: length (đến 16k tokens), depth (ReST cải thiện đến 32 layers; LLaMA saturate >8, HSTU >16), width (d=512 vẫn monotonic; baseline flatten d=256). Fit power law ΔAUC=a·F^b để compare compute efficiency.
6. Deploy: cấu hình satisfy P99 budget, A/B test 1 tuần với revenue metric (Advv) + streaming AUC + guardrails.

## Output mong đợi
- Offline AUC Δ +0.9% (Large) trên production baseline; online AUC +1.31%, revenue +11.93% trong P99 budget; 5.8× training throughput, 20× inference cost reduction.

## Ví dụ áp dụng
- E-commerce ads ranking: thay sequence component của DLRM bằng ReST, keep rest fixed; A/B 20% traffic 1 tuần → đo Advv lift; nếu +revenue trong latency budget → rollout toàn bộ.

## Gotchas
- MoE trong encoder: +500% params, 0 AUC gain — capacity encoder không phải bottleneck; decoder candidate-conditioned mới lợi (+0.03% @ +0.2% FLOPs).
- Unbounded output gate (SiLU) diverge ở scale — luôn bounded sigmoid.
- Aux supervision lợi hơn khi module lớn (LLaMA +0.06% vs ReST +0.05%) — module càng lớn càng cần aux.
- RoTE phải shift timestamp theo sequence start (t̃_i = t_i − t_1) để tránh bucket index khổng lồ.
- Public benchmark phải cast pointwise chronological split mới align với CVR task.
