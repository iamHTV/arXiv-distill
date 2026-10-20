# Skill: KG Semantic Mediation Layer — auto-build KG từ schema + mediation prompt cho enterprise data assistant
Source: 2610.23304v1
Type: framework / workflow

## Khi nào dùng skill này
- Build enterprise data assistant (assistant dữ liệu doanh nghiệp LLM) cho business users KHÔNG biết SQL; user prompts ngắn, goal-oriented, không reference schema.
- Database multi-table với joins phức tạp; schema-similarity retrieval alone gây hallucinated joins.
- Cần replace hand-curated few-shot examples per table (brittle, labor-intensive) bằng mechanism tự động, low-maintenance.
- KHÔNG nên dùng: schema đơn table (không có joins — mediation dư thừa); user đã fluent SQL + luôn reference schema; database metadata không có PK-FK cũng không name/type heuristic đáng tin (joins_on edges không xây được); org cấm gửi schema data ra embedding API external.

## Input cần có
- Database schema metadata (information schema: tables, columns, PK-FK constraints; fallback: name matching + type-compatible heuristics) + column descriptions/metadata.
- Embedding model + vector store (paper: OpenAI text-embedding-3-large + ChromaDB 1.3.4; self-host tương đương dùng được).
- Prompt-refinement LLM (GPT-4.1 / Claude Sonnet 4 class) + LLM-as-Judge cho completeness gate (Pydantic structured output, 3 few-shot examples).
- 2 human analysts cho audit vòng 1-2 (TP/FP/FN) — hoặc sampled audit nếu scale nhỏ.
- Sample real user interaction logs ( ideally ≥100 ) cho evaluation.

## Các bước thực hiện
1. **Auto-build KG** (NetworkX class): nodes = tables + columns (từ information schema); edges = has_column (table→columns) + joins_on (PK-FK trước, fallback name-matching + type-compatible); deliberately KHÔNG thêm domain constructs (metrics, filters) ở vòng đầu — isolate structural knowledge. Paper scale: 273 nodes/540 edges.
2. **Vector-store nodes**: embed mỗi node (identifier + type + name + description) vào ChromaDB-class store cho semantic matching user phrasing → canonical KG nodes (entry points).
3. **Mediation pipeline** mỗi query: (a) segment prompt thành intent units; (b) similarity_search per segment → entry nodes, retrieve table→all columns + column→parent table; (c) traverse KG direct + indirect join paths → subgraph (target ~54 nodes/99 edges — "just-right" context); (d) LLM refine: mediated prompt giữ original intent + explicit table/column/join specs.
4. **Completeness gate**: LLM-as-Judge binary COMPLETED/NOT COMPLETED (3 few-shot examples, structured output); NOT COMPLETED → block hoặc clarify thay vì execute sai.
5. **Human audit**: 2 analysts, 2 iterations (analyst 1 review → analyst 2 review results → compare/discuss/resolve) → Precision/Recall/F1 trên mediated prompts (TP = database info đúng, FN = thiếu, FP = sai).
6. **Monitor + governance**: F1 ≥ baseline target (paper: KG F1 89-90%); completeness ≥ no-mediation baseline; annotator agreement ≥95%; KG versioning + change management khi schema evolves; end-to-end spot-check (TP prompts phải execute KHÔNG cần discovery thêm).

## Output mong đợi
- Mediated prompts với correct tables/columns/joins cho imperfect user prompts: Precision ~87-91%, Recall ~88-94%, F1 ~89-90% (2 LLMs), completeness ≥ baseline (93.04% vs 91.14% GPT-4.1), latency ~2.7s/query mediation (vs 1.1s schema-only), annotator agreement 95.57-98.73%. User intent preserved mặc dù inject database content.

## Ví dụ áp dụng
- Assistant analytics cho solopreneur (DB 15 tables orders/customers/products): user hỏi "revenue từ returning customers Q3 theo product category" → mediator segments → retrieve customers (returning = repeat buyers), orders, products nodes → join path customers→orders→order_items→products → mediated prompt explicit joins → assistant trả đúng category breakdown. Schema-only: pick đúng tables nhưng join customers.created_at sai → group customers sai (hallucinated join → kết quả sai silent).

## Gotchas
- Schema-only mediation hallucinated joins trên complex schemas — JOINS SAI ONCE ENCODED → downstream planning + execution reliably fail: KHÔNG ship schema-only cho multi-join enterprise DB.
- KG auto-built thiếu domain constructs (metrics, filters) — mediation có thể minimal-change khi thiếu knowledge (completeness metric KHÔNG catch được case này → cần sampled human audit).
- "Just-right" subgraph beats flooding: inject toàn schema → overwhelm LLM + false assumptions tăng.
- Polysemous domain terms (VD "fiscal unity" income-tax vs VAT) cần KG-level disambiguation cues — schema similarity không phân biệt được.
- Latency trade: KG 2.7s vs schema 1.1s — chấp nhận cho precision gain; inference cost mediation LLM/query không được paper report — tự đo.
- Embedding OpenAI → schema text gửi external: enterprise data lake privacy cần self-host embedding nếu dữ liệu nhạy.
- Single-enterprise validation (158 interactions/29 users): test trên corpus riêng trước khi tin số.

## Dry run test
- Test case giả (DB commerce 15 tables, ~90 columns, 12 FK joins; 20 user prompts thật ngắn): step 1 build KG ~15 table nodes + ~90 column nodes + ~40 edges trong ~2 phút; step 2 embed nodes; step 3 mediation 20 prompts: 17/20 mediated prompts đủ context → LLM judge COMPLETED 18; human audit TP-only 15, FN 2 (thiếu join path), FP 1 (wrong column) → Precision 15/(15+1)=93.75%, Recall 15/17=88.24%, F1 90.9%; completeness 95% ≥ baseline 90%; demo case 3-table join đúng nơi schema-only hallucinated join → wrong result. Output: mediated prompts + metrics đo được → meaningful → [SKILL VALID].
