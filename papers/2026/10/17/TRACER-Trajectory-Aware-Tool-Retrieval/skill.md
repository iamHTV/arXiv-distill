# Skill: TRACER — Trajectory-Aware Tool Retrieval (trie retrieval cho agent)
Source: 2610.21267
Type: framework / retrieval-front-end

## Khi nào dùng skill này
- Agent có tool registry lớn (>50 tools) — expose toàn bộ tốn token + selection kém
- Có history successful trajectories (đã log)
- Multi-step tool-call workflows có thứ tự logic (prefix predict next call)

Tình huống KHÔNG nên dùng: registry nhỏ (<20 tools); không có trajectory history (cold start → mọi step là vector fallback, −38 points); tool usage tập trung vào generic utility tools (KB_search, grep) — dùng TRACER+G thay vì TRACER thuần.

## Input cần có
- Dataset D trajectories đã graded (chỉ successful runs; collapse mỗi task thành 1 canonical decision point)
- Registry tool descriptions
- Frozen embedder (vd text-embedding-3-small)
- Executor model (LLM chọn cuối cùng — TRACER chỉ là front-end)

## Các bước thực hiện
1. Trie construction: insert mọi prefix của mọi trajectory thành node; children C(Si) = tools observed ngay sau Si. Mỗi edge lưu: (a) empirical prior P_trie(t|Si) = normalized transition frequency (log + smoothing ε), (b) edge memory m(Si→t) = mean-pooled embedding của training contexts transition được thực hiện. Trie turn-local (reset ở turn boundary); edge memory embed FULL conversation (cross-turn).
2. Contextual prior: embed step context (previous turns + step reasonings, DROP tool-call signatures) → R(t) = cos(embedding, m(Si→t)); ReLU-normalize thành distribution (uniform nếu mọi similarity ≤0); L(t) = log(R̂(t)).
3. Learned blend: s(t) = (1/T)[(1−w)L(t) + wP(t)]; w, T do learned map trên 5-dim state feature vector (logistic head cho w, floored softplus cho T); fit bằng Adam + ℓ2 minimize NLL gold next call, inner-fold isolation (trie/edge memory built WITHOUT own trajectory).
4. Confidence gate: unseen state (C(Si)=∅) hoặc flat distribution (κ<τ=0.20) → global vector search over full registry, replace trie candidates.
5. Present top k (k=5 cho registry ~128 tools; sweep {3,5,10,20,30} per domain) — model chọn cuối cùng.
6. (Tùy chọn) TRACER+G: nếu generic utility tools chiếm large share calls → union |G|=3 tools có prefix entropy H(S|t) cao nhất vào mọi candidate set.

## Output mong đợi
- Teacher-forcing: +4.7 points over full-registry (GPT-5.4, Mixed Tau2 Large, 61.9 vs 57.2), CIC −80% (2.8k vs 14.2k tokens/step); beats full-registry 21/24 model-environment pairs (avg +6–10 points).
- Free-running: parity task success (58.3% vs 58.2%) với 23% tools, −61% per-step input tokens; +13.7–15.2 points cho weaker model (GPT-5.4-mini).
- Specificity trap 36.4%→16.4%; procedural ordering (unlock trước write) được enforce tự động.

## Ví dụ áp dụng
- E-commerce agent 128 tools (order management, shipping, returns): prefix "find_user → get_order_details" → trie node children = {split_order_shipment, add_gift_message, request_return_pickup, schedule_installation...} thay vì 128 tools; edge memory tách "order #W4821 invoice + separate addresses" (→ split_order_shipment) khỏi "espresso machine installation" (→ schedule_installation). GPT-5.4 chọn đúng 61.9% với 2.8k tokens thay vì 57.2% với 14.2k tokens.

## Gotchas
- Cold start: không có trajectory history → mọi step là vector fallback, accuracy −38 points average. Phải log successful runs trước khi dùng.
- Free-running errors compound: single early miss → unseen prefix → fallback; out-of-trie rate ~3× teacher-forcing. Mitigation (paper future work): present full registry trên out-of-trie steps alone (+38 points, giữ 84% reduction).
- Prefix-independent lookups (không prefix nào predict) là điểm yếu nhất — TRACER trails full-registry trên những steps này ngay cả teacher-forcing.
- Generic-utility registries: TRACER thuần kém (Tau3 Banking) — phải dùng +G; nhưng +G hurts diverse registries (thêm distractors). Phát hiện: nếu few tools chiếm >50% calls → bật +G.
- w không cố định: contextual prior dominant trên diverse tries (w≈0.02) nhưng empirical prior quan trọng hơn early trong conversation — cần learned blend, đừng hand-tune constant (TRACER-fixed −0.6–8.0 points).
- Edge memory > description matching: bỏ edge memory (description-only) −21 points. Đừng cache shortcut bằng tool-description similarity.
- Premise: mọi tool available mọi step — permission-gated registries vi phạm assumption.
- Trie key depth: full current-turn prefix; last-2 gần bằng (trong SD) nhưng 9.6% vs 12.4% out-of-trie — test cả hai per deployment.
- Inner-fold isolation bắt buộc khi fit blend: nếu dùng own trajectory trong trie → optimistic scores, generalization hỏng.
