# Skill: Latent Semantic Memory cho frozen LLM (K soft memory tokens, 3-stage training)
Source: 2610.21375v1
Type: framework / evaluation-method

## Khi nào dùng skill này
- Assistant/agent phải draw on accumulated history (user preferences, long docs, KB) mà KHÔNG muốn re-send toàn bộ history mỗi query (cost/latency) — full context dùng 1,974× (PMv2) token nhiều hơn và quality KHÔNG cao hơn.
- Query wording thường KHÔNG match stored wording (preference/indirect questions) → similarity RAG yếu.
- Cần multi-entity relational reasoning across documents (FactKG-style claim verification, personalization combining).
- Agent cần continual learning from own experience mà KHÔNG overwrite prior knowledge (TextWorld-style).
- KHÔNG nên dùng: corpus nhỏ (<~1,000 document tokens — PubMedQA MEMORILLA LOSES 59 vs 69); task cần exact entity recall 100% (names/IDs/numbers verbatim — dùng RAG hoặc hybrid); latency budget dominated by small corpora (LLM decoding dominates anyway — gains chỉ large collections); không có capacity train 3-stage curriculum (3.3M examples + 194M params + 2 frozen models).

## Input cần có
- Frozen document encoder (paper: Qwen3-Embedding-4B) + frozen query encoder + frozen LLM decoder (paper: Qwen3-8B; TextWorld: Qwen3-4B-Instruct-2507) — encoder+decoder phải compatible family (cross-family untested).
- Document collection chia chunks → ZD (N × he) — encode ONCE, persist; chỉ re-encode docs added/changed.
- Training data 3-stage: paraphrase reconstruction (~2M Wikipedia) → QA/RC/summarization mixture (~1.3M, 10 datasets) → target-benchmark train split mixture; loss chỉ answer positions.
- (Agent continual) environment với sparse reward + GRPO configs (G=16 rollouts); memory tokens K (16 supervised / 8 agent) prepended trong same input budget as ICL baseline.

## Các bước thực hiện
1. **Build persistent store**: embed corpus once với frozen doc encoder → ZD + persist on disk/memory. Query-independent → reuse every query.
2. **Build + train memory module**: K learned slots Q0 (shared) → query conditioning (LayerNorm(Q0 + CrossAttn(Q=Q0,K=zq,V=zq))) → L_ref Perceiver-style cross-attn over ALL N store embeddings → projection Wproj (he→hL) → M=[m1..mK] soft memory tokens; train 3-stage curriculum, NLL loss answer-only; freeze encoders + decoder.
3. **Inject + generate**: X_LLM = [m1..mK ; Pq], standard RoPE, frozen LLM generate T=0. Mỗi query chỉ trả K tokens vào context ( KHÔNG grows with corpus).
4. (Agent continual) **Mỗi turn**: append turn as new document to ZD; memory module (random init → GRPO trên environment reward ONLY) compress growing store thành K=8 tokens placed before prompt; keep input budget = ICL baseline → measure avg@3/pass@3.
5. **Monitor**: primary metric per benchmark + mean document tokens/query + Pareto position vs RAG + full-context; latency; check exact-entity recall (names/IDs/numbers) degradation → if critical, add retrieval hybrid (union oracle > either every benchmark); check decision-threshold calibration on claim verification (FactKG: true claims 89.5% joint errors → miscalibrated).

## Output mong đợi
- Frozen LLM với query-conditioned memory: average quality 49.68 vs compact baselines ≤41.92 (xRAG/LLMLingua-2/Mem0); 394×/113×/49× fewer tokens than full-context/RAG-50/MemoRAG (range 20×–4,212×); latency 0.74s vs 19.9s; Pareto frontier mọi benchmark; TextWorld avg@3 0.242/pass@3 0.375 vs ICL 0.186/0.250 (+30%/+50% relative); untrained memory UNDERPERFORMS ICL (0.153/0.225) — value nằm ở training.

## Ví dụ áp dụng
- Solopreneur customer-support assistant: embed 5,000 past conversations once; query "gift for my wife who likes hiking" → 16 soft tokens capture wife+hiking+past purchases malgré no lexical overlap → personalized answer; vs RAG misses (wording never repeated), vs full-context cost 1,974× tokens. Quality PMv2-like 44.6 vs RAG 30.9.

## Gotchas
- Lossy on fine-grained facts: exact names/IDs/numbers — RAG wins "who/which" +3.45/+2.93 ROUGE-L; hybrid memory+retrieval needed cho exact recall.
- Small corpora LOSE: PubMedQA (324 tokens) MEMORILLA 59.00 vs LLMLingua-2 69.00 — efficiency/quality gains chỉ large collections.
- KHÔNG drop-in: 194M trainable params + 3-stage curriculum (~3.3M examples) + 2 frozen models (4B + 8B); untrained memory HURTS (dưới ICL) — taps alone vô ích.
- Qwen-family pairing tested — encoder/decoder cross-family transfer untested; test before adopting other models.
- Miscalibrated claim-verification thresholds: true claims 89.5% joint errors on FactKG — calibrate threshold post-hoc.
- Joint errors = combining failures (PV4 linking facts) — memory alone không fix multi-hop linking; union with RAG cần.
- MemoRAG still wins where verbatim passages matter (NarrativeQA 21.80 ROUGE-1, PV4 67.88%) — measure per-task before betting.
- PMv2/PV4 eval = cosine-nearest-neighbor among predefined choices — free-form generation quality UNVERIFIED; synthetic personas (GPT-5) → real-user generalization untested.

## Dry run test
- Test case giả (support assistant, 800 past chats + KB 300 docs): step 1 ZD embed once (frozen Qwen3-Embedding-4B); step 2 train memory module K=16 (curriculum: 2M paraphrase + 1.3M QA + target mixture); step 3 query personalization + claim-verification 20 test cases: memory answers 8/10 preference questions (RAG 4/10), FactKG-like accuracy 84% vs full-context 80%, tokens 41/query vs 12,000 full-context; step 4 TextWorld-style agent loop 20 episodes: pass@3 0.35 vs ICL 0.24, budget-exhaust 58% vs 71%; step 5 monitor: Pareto frontier 7/8 tasks, exact-name recall check → add RAG hybrid cho 2 ID-heavy queries. Output: frozen LLM với memory persistent, metrics đo được → meaningful → [SKILL VALID].
