# Skill: Execution-Grounded Query Refinement (detect-and-route loop cho structured-query agents)
Source: 2609.12746
Type: framework / agent-workflow

## Khi nào dùng skill này
- Agent generate executable queries (Text-to-Cypher/SPARQL/SQL) trên live database — well-formed-but-wrong queries execute silently và trả misleading data
- Cần recover failed queries mà KHÔNG tăng call budget cho successful queries
- Đang cân nhắc build feedback-synthesis module (LLM-synthesised hints) — paper chứng minh module này chỉ worth ~1 point exact match

Tình huống KHÔNG nên dùng: output space high-entropy (open-ended generation — sampling diversity có ích); KHÔNG có executor/validator (không có hard failure signal để detect).

## Input cần có
- Live database connection + schema (để EXPLAIN pre-validation + LIMIT 1 execution)
- Question + parsed schema (deterministic parser; LLM extraction chỉ fallback)
- Correction budget N=2 validation cycles, M=1 relaxation pass
- Fixed relaxation hint set H_relax (6 hints: case-insensitive regex, substring rather than equality, canonical datetime() formatting, dropping over-restrictive labels, simplifying RETURN)

## Các bước thực hiện
1. Schema Parsing (0 LLM calls): deterministic parse raw schema → normalized nodes/properties/relationships (8 formats; fallback LLM extraction chỉ khi parser fail).
2. Generation (1 LLM call): candidate query từ parsed schema + question.
3. Validation (0–2 calls): EXPLAIN against live schema; execute với LIMIT 1. Cả hai pass → RETURN NGAY (total 1 call, bằng single-pass). Fail → parse query (1 call) + deterministic schema check (labels/relationship types/properties tồn tại?); violations → synthesize grounded hints H_val (1 call).
4. Correction (1 call): rewrite query từ hints + schema Σ + correction history Γ (prompt instruction: KHÔNG repeat prior attempt). Route về bước 3; lặp đến valid hoặc N=2.
5. Execution (0 calls): run validated query. Non-empty → return. Empty → inject H_relax (constant, 0 calls) + 1 correction pass (M=1), rồi return kết quả (empty hay không).
6. KHÔNG build parallel sampling (Best-of-3 degrade 10.8–11.4% trong low-entropy spaces); KHÔNG invest vào feedback-synthesis sophistication — raw database error string equivalent within ±0.075 set-F1 (TOST p=0.002).

## Output mong đợ
- Recovery 91.7% single-pass failures (pooled 93.8%), hit retrieval +11.8%.
- Cost: successful query = 1 call; failed query thêm tối đa 3 calls/cycle; mean 1.1–2.5 calls/query tùy backbone.
- Per-metric caveats: order-sensitive GLEU over-reports vs set equivalence (65.9% pairs) và under-reports vs semantics (33.9% partial-BLEU fully correct); LLM judge optimistic ~9 points vs blind human labels.
- Ví dụ: `WHERE org.name CONTAINS "new energy technologies"` (returns ∅) → inject H_relax → `WHERE org.name =~ '(?i).*new energy technologies.*'`.

## Ví dụ áp dụng
- Graph RAG agent trên Neo4j knowledge graph: single-pass generation fail 1,917/14,826 model-query pairs (13%) → detect-and-route loop recover 91.7% với raw Neo4j error string (KHÔNG cần hint-synthesis module), mean 3.14–4.19 stages/query nhưng chỉ 1.1–2.5 LLM calls (Schema Parsing + Execution + short-circuit Validation = 0 calls).

## Gotchas
- Empty-reference trap: 12.0% queries có empty reference result — GLEU convention awards 1.0 cho non-empty output → query nên trả nothing lại score perfect; report strict set-theoretic metrics bên cạnh GLEU.
- Relaxation pass có thể INDUCE exactly failure này (returning something when nothing is correct) — monitor empty-result rate post-relaxation.
- Schema-only validation (KHÔNG execute) trigger unnecessary rewrites khi baseline quality cao — LAST-CQ schema-only giảm GLEU nhẹ trên 2 strongest models; execution evidence là cần thiết.
- Naive retry (raw error string) wins trên 1/6 models (DeepSeek 20.2% vs 17.9%) — schema-grounded hints KHÔNG luôn tốt hơn; measure before adopting.
- Best-of-3 với T=0.7 làm hit rate FALLS (87.6%→85.2%) — temperature moves mass OFF correct forms trong low-entropy output spaces.
- Judge κ=0.63 inter-model ≠ human agreement (human-judge κ=0.48 three-way, 0.59 valid/invalid) — LLM–LLM agreement overstates validity ~9 points.
- BLEU≥0.999 làm EM proxy understate order-invariant accuracy (naive 19.9%→22.6% under direct set equality); 2.9% set-identical results score <1.0 purely from row ordering.
- Comparison set conditioned on own failures: counterfactual retry measure relative correction quality under shared detector, không phải end-to-end system quality.
- M=1 single-shot latch — chưa đo larger M; KHÔNG extrapolate recovery rate sang multi-cycle relaxation.
