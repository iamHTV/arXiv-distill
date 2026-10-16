# Skill: SCOUT MCP Meta-Tool Gateway (cổng tool discovery ngữ nghĩa)
Source: 2608.23992
Type: framework / architecture-pattern

## Khi nào dùng skill này
- Agent enterprise có >100 tools qua nhiều MCP server — tool schema chiếm >50% context window trước khi user hỏi
- Cần user discoverability bằng natural language qua catalog lớn (200+ server) mà không sửa client
- Cần access control per-user tại retrieval layer, không post-filter

Tình huống KHÔNG nên dùng: catalog <50 tools (full injection vẫn ổn); retrieval infra không có SLA (fallback full injection sẽ tốn context); cần feedback-loop learning (skill này không có).

## Input cần có
- Proxy MCP server (FastAPI hoặc tương đương) aggregate nhiều backend MCP server
- Vector DB có native BM25 + dense HNSW trong 1 query interface (paper dùng Milvus; RRFRanker built-in)
- Embedding API (paper dùng OpenAI text-embedding-3-large, 3,072 chiều) + 3-tier cache (memory → Redis → MySQL, TTL 24h)
- Per-user server permission mapping (User ↔ Proxy Server ↔ MCP Server)

## Các bước thực hiện
1. Định nghĩa 2 synthetic MCP meta-tool: tool_search (params: query string required, top_k int default 5 clamp [1,20], scope enum my_servers|all_servers) và execute_tool (params: tool_name, server_name, arguments — cả hai field đều guardrail "Do not guess", lấy verbatim từ tool_search).
2. Viết tool description theo pattern behavioral spec: tool_search gắn "REQUIRED FIRST STEP" + liệt kê domain categories + guardrail "Never guess a tool_name. Always get it from tool_search first."; execute_tool gắn "REQUIRED SECOND STEP"; thêm câu "After calling tool_search you can immediately call execute_tool — you already have its full schema above."
3. Ingestion pipeline (trigger: server ACTIVE, admin manual, hoặc catalog change): load schema từ 3-tier cache → chunk thành structured NL doc (Tool + Category + Server Description + Description + Parameters [type, enum, required/optional]) → embed batch 16 → upsert insert-before-delete (zero downtime). Chunk ID deterministic {server}_{tool}; entity_source = {server}.tool.
4. Retrieval pipeline: resolve session + 3-way injection gate (client config, proxy config, index non-empty) → scope filter thành Milvus metadata filter (enforce BÊN TRONG DB) → two-branch search: dense HNSW COSINE top_k×3 + BM25 top_k×3 → fuse RRF k=60 → top_k → hydrate full schema từ cache.
5. Lifecycle: 5 states (PENDING/ACTIVE/DEGRADED/INACTIVE/REJECTED) → thêm/xóa chunks trong Milvus; scheduled job probe DEGRADED sau cooldown; cron 15 phút poll catalog change.
6. Fallback theo tầng: embedding API fail → BM25-only; index absent → full tool injection (giữ MCP protocol compatibility). Instrument log events (tools_list_tool_search, tool_search_completed với results_count/latency_ms, tool_search_fallback WARNING, execute_tool_failed) cho observability.
7. Dual connector (prod/dev): mỗi connector surface own tool_search/execute_tool pair, gắn environment label trong description text ("production environment"/"development") — LLM tự route bằng NL intent, không config thêm.

## Output mong đợi
- tools/list trả 2 tool thay vì N; tool-token consumption giảm ~99% (140.2k → 1.3k token); retrieval Hit@5 ≥95% trên benchmark query của bạn; authorization enforced tại retrieval layer; graceful degradation khi infra fail.

## Ví dụ áp dụng
- PayPal MCP Hub: 2,000+ tools, 100+ servers. Sau SCOUT: 1,300 token (0.8% context), Hit@1 84.8% / Hit@5 95.6% / MRR 0.821 trên 49-query benchmark; production 24h: 31,701 sessions, fallback rate 0.0%, search-to-execution 1:4.5, latency median 440ms (P95 936ms — cao hơn mục tiêu 500ms, cần monitor).

## Gotchas
- P95 latency có thể vượt mục tiêu <500ms (thực tế 936ms) — over-fetch 3× + embedding API call nằm trong critical path; monitor p50/p95/p99.
- Over-fetch top_k×3 mỗi branch là BẮT BUỘC: doc rank 10 dense / rank 2 BM25 sẽ bị mất nếu chỉ fetch top_k.
- BM25-only fail class vocabulary gap (Q5 "Slack" → 0 match); dense-only fail class exact API name — đừng chạy single-modality.
- Tool description kém chất lượng bị under-retrieve bất kể modality — audit description trước khi tin retrieval metrics.
- Sync cron 15 phút → schema mới lag tới 15 phút; time-sensitive change cần manual force-refresh.
- Intra-domain ranking fail do lexical overlap (respond_to_meeting beat create_event) — nếu domain có nhiều tool cùng verb, cân nhắc intent-classification pre-filter.
