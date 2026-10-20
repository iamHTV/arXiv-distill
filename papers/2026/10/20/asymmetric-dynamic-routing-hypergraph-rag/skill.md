# Skill: Asymmetric Dynamic Routing (ADR) — query-adaptive RAG với 3 toán tử traversal bất đối xứng
Source: 2609.29282v2
Type: framework / workflow

## Khi nào dùng skill này
- RAG pipeline trên corpus có cấu trúc (KG/hypergraph sẵn hoặc build được) mà hiện dùng 1 traversal config duy nhất cho mọi query — đang waste token trên simple queries + thiếu context trên complex queries.
- Cần cắt latency/token RAG mà KHÔNG giảm quality (ứng viên ideal: −45% latency, −49% prompt token đồng thời +1.86 điểm quality).
- Corpus chia vùng knowledge density khác nhau (sparse vs dense) → best mode khác nhau per domain.
- KHÔNG nên dùng: corpus không build KG/hypergraph (chỉ flatten chunks — dùng Adaptive-RAG/naive RAG routing thôi); query distribution nearly uniform (all simple hoặc all complex — routing gain ~0); latency budget yêu cầu classifier overhead = 0... classifier nhẹ nhưng vẫn là 1 call; corpus rất nhỏ (<100 docs).

## Input cần có
- Dual-hypergraph knowledge base (theo DHI): factual hypergraph HK (entities, pairwise edges |e|=2, higher-order factual hyperedges |e|≥3, mỗi hyperedge → atomic direct insight ι(e)) + insight mapping π (hyperedge → insight vertex) + deep insight hypergraph HD (insight vertices, insight edges ε kèm synthesized narrative insight I(ε)).
- Embedding model cho entities + insight edges (paper: text-embedding-3-small) + generation LLM (paper: GPT-4o-mini, T=0).
- Query-complexity classifier (lightweight structured classifier) giving {Simple, Moderate, Complex} + confidence; threshold γ (default 0.75).
- Evaluation judge (LLM-as-a-Judge 5 dims: Comprehensiveness/Diversity/Empowerment/Logicality/Readability, 0–100) + per-mode token/latency logging.

## Các bước thực hiện
1. **Build dual-hypergraph offline** (trước khi deploy): extract entities + factual relations (pairwise) + higher-order factual hyperedges (quan hệ liên hợp ≥3 entities); gắn ι(e) cho mỗi higher-order edge; map π → insight vertices; group insight vertices thành insight edges ε với narrative I(ε). Lưu upfront indexing cost — one-time.
2. **Classify query**: classifier → y ∈ {1,2,3} + confidence c. Nếu c < γ (0.75) → conservative fallback y=2 (Moderate). Calibrate γ: fallback rate >~68% → γ quá cao (giảm γ); ambiguous queries misroute (Logicality drop) → γ quá thấp (tăng γ; reference: 0.50 → Logicality −1.14).
3. **Route asymmetric**:
   - Simple → Operator 1: Vas = top-k_e entities max Σ cos(e_v, q); Esub = edges ∩ Vas ≠ ∅; DỪNG (zero-hop-like, không mở rộng neighborhood, không cross-layer).
   - Moderate → Operator 2: Useed = π(Esub higher-order edges); Eup = insight edges ∩ Useed ≠ ∅ (single adjacency expansion HD); context = facts Esub + narratives Eup.
   - Complex → Operator 3: E* = top-k_d insight edges max Σ cos(e_ε, q); Eground = π−1(E*) ⊆ EK; context = narratives E* + facts Eground.
4. **Generate**: format joint context → generation LLM T=0.
5. **Monitor + calibrate**: log per-query (mode, tokens, latency, judge scores); if Complex queries in sparse domain thấy insufficient facts → add dense-vector fallback branch; benchmark 3 frozen modes (Simple/Moderate/Complex-only) để verify dynamic gain (+1.39 to +2.11 points expected).

## Output mong đợi
- Per-query adaptive retrieval: average latency ~238ms + prompt tokens ~1,929 (vs 435ms + 3,760 nếu Complex-only) = −45.3% latency, −48.7% tokens, quality 83.91 vs 82.05 (+1.86); beats best static mode every domain (+0.94 – +2.11); complex causal queries coherent + 41.2% fewer tokens than always-deep.

## Ví dụ áp dụng
- Knowledge base product docs + blog (solopreneur content site): query "refund window bao lâu?" → Simple → anchor {refund policy, window} → 2 facts, context nhỏ; "returns interplay với loyalty points accrual?" → Moderate → facts + insight edges; "tại sao churn tăng sau pricing change?" → Complex → top-down insight edges (pricing→usage drop→churn) π−1-grounded về docs → causal chain + facts, ~41% token hơn always-complex.

## Gotchas
- Sparse-domain Complex queries: insight grounding có thể thiếu supporting facts (graph connectivity yếu) → PHẢI có dense-vector fallback branch (paper thừa nhận, chưa evaluate định lượng).
- γ sai: 0.50 → misroute ambiguous (Logicality −1.14); ≥0.85 → 68.4% fallback Moderate + 58ms latency vô ích. Đo fallback rate + Logicality khi đổi γ.
- Depth thừa hại quality trên dense corpus (Moderate-only thắng Complex-only +1.39–1.51): đừng mặc định "deeper = better".
- Upfront indexing cost: build HK+HD offline — trade-off construction time vs online savings; corpus nhỏ thì không đáng.
- Classifier independent of graph structure: classifier thấy query text KHÔNG thấy graph state → domain shift cần re-calibrate.
- Quality metric chỉ judge perception: thêm exact-match/F1 check riêng cho factual correctness critical domains.
- Complex-only naive path: 3,850 tangential tokens (EGFR irrelevant trong pathology example) — nếu không route, context dilution + hallucinated associations tăng.

## Dry run test
- Test case giả (KB 200 docs commerce): step 1 build KG (entities 1,800, edges 2,600, insight vertices 140) offline 1 lần; step 2 classifier 15 test queries → 5 Simple/6 Moderate/4 Complex, γ=0.75 fallback 1 query → Moderate; step 3 route: Simple queries avg 980 tokens (vs Complex-only 3,760), Complex query churn-pricing grounded causal chain 2,210 tokens + facts; step 4 T=0 generate; step 5 monitor: avg latency 240ms, tokens 1,950, judge 84.1; Complex-only-frozen baseline quality 82.3. Output: adaptive routing hoạt động, metrics đo được, gain +1.8 points/−48% tokens → meaningful → [SKILL VALID].
