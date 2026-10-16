# 2608.23992 — Hybrid Semantic Tool Discovery for Enterprise MCP Gateway (SCOUT)

## Problem
- Proxy MCP server (gộp nhiều backend sau 1 endpoint) tạo 2 vấn đề chồng chất: (1) context-engineering bottleneck (nghẽn cổ chai kỹ thuật ngữ cảnh) — toàn bộ tool schema được load đầu mỗi conversation: 140,200 token = 70.1% cửa sổ 200k trước khi user kịp hỏi; (2) user-facing discoverability barrier (rào cản khám phá) — 200+ MCP server, 2,000+ tool, không ai browse thủ công nổi. Prompt caching giảm cost reprocessing nhưng KHÔNG giải phóng context hay cải thiện accuracy.

## Contribution
- SCOUT (Selective Context Optimization for Universal Tooling): reframe tool exposure thành context-selection problem — inject chỉ tool liên quan current step. Hai synthetic MCP meta-tool: tool_search (agentic RAG: BM25 + dense vector, Reciprocal Rank Fusion, top-k) và execute_tool (route invocation tới backend server).
- 6 contribution: meta-tool protocol; hybrid retrieval engine; user-scoped authorization filter tại retrieval layer (không post-filter); zero-downtime index (insert-before-delete upsert); environment-aware dual-connector routing (prod/dev bằng NL intent); validated trên 6 MCP clients (Claude Code, Claude Desktop, ChatGPT Web/Desktop, GitHub Copilot VS Code, Cursor, OpenAI Codex CLI) — không cần client-side modification.

## Method
- Two-phase query protocol: tools/list trả stub list chỉ 2 tool. tool_search mô tả gắn nhãn "REQUIRED FIRST STEP" + liệt kê domain categories + guardrail "Never guess a tool_name. Always get it from tool_search first." execute_tool gắn "REQUIRED SECOND STEP". Cả hai chia sẻ semantic fingerprint (domain categories) → 1 search trả cả 2 schema.
- Ingestion pipeline 4 stage: load từ 3-tier cache (memory → Redis → MySQL tool_cache 24h TTL) → chunk thành structured NL document (tool name, server category, server description, tool description, parameter specs type/enum/required) → embed batch 16 bằng OpenAI text-embedding-3-large (3,072 chiều) → upsert insert-before-delete.
- Retrieval pipeline 4 stage: resolve session + 3-way injection gate (config tool_search_clients, tool_search_proxy_ids, index initialized) → resolve scope (my_servers/all_servers thành Milvus metadata filter BÊN TRONG vector DB) → two-branch search (dense HNSW COSINE top_k×3; sparse BM25 top_k×3; fuse RRF k=60 → top_k) → schema hydration từ cache. Fallback: embedding API fail → BM25-only; index absent → full injection.
- Index lifecycle: 5 server states (PENDING, ACTIVE, DEGRADED, INACTIVE, REJECTED) → action Milvus tương ứng; scheduled job probe DEGRADED sau cooldown; rolling-window poll catalog 15 phút.

## Key Findings
- Context: 140,200 token (70.1%) → 1,300 token (0.8%) = giảm 99%; spot-check avg ~2,500 token (~1.25%) với top-5.
- Retrieval quality (49-query benchmark, 9 domain, live catalog 2,000 tool, 45 evaluable): Hit@1 84.8% (38/45), Hit@5 95.6% (43/45), MRR 0.821. Original 15-Q: Hit@1 84.6%, Hit@5 100%, MRR 0.915. Expanded 35-Q (harder): Hit@1 75.6%, Hit@5 93.9%, MRR 0.784.
- Domain: analytics 11/11 Hit@1; SRE/infra 78% (7/9); productivity 75% (6/8); BI/reporting thấp nhất 50% (2/4) — Looker tool lên rank 4 khi query dùng payment-metric vocabulary.
- Latency (1,921 requests/24h): avg 572ms, median 440ms, P95 936ms — VƯỢT requirement p95 <500ms đã đặt ra (paper không bàn); min 232ms (warm-cache floor).
- Production 24h: 31,701 sessions, 55,314 tool calls, 1,926 tool_search invocations (43.1% invocation rate), avg 5.5 tools/search, 8,694 execute_tool completions, fallback rate 0.0%, search-to-execution ratio 1:4.5.
- Q5 "send a Slack message": BM25 pure = 0 matches (không có "Slack" trong catalog); dense branch bridge vocabulary gap → teams_send_message (Y*). PayPal dùng Microsoft Teams.

## Actionable Insights
- Meta-tool pattern: khi agent có >100 tools, collapse tools/list thành 2 meta-tool (search + execute) — model-agnostic, zero client change, orchestration nằm hết trong tool description text (label "REQUIRED FIRST/SECOND STEP" + guardrail), không fine-tune.
- Hybrid BM25+dense với 3× over-fetch mỗi branch (pool 30 candidate trước RRF k=60) — BM25 bắt exact API name, dense bắt paraphrase; thiếu 1 branch mất luôn class query (Q5).
- Enforce authorization bên trong vector DB (metadata filter), không post-filter — và degrade gracefully theo tầng (BM25-only → full injection) để retrieval infra failure không thành outage.

## Assumptions & Limitations
- Tool description chất lượng tác giả MCP server viết lên xuống, không có cơ chế detect/compensate — tool mô tả kém bị under-retrieve bất kể modality.
- Không có feedback-loop learning (successful invocations không refine embedding); sync cron 15 phút → schema change lag tới 15 phút; top-k tune thủ công (không auto-calibrate).
- Failure mode: intra-domain ranking (respond_to_meeting rank 1 trên create_event do lexical overlap "schedule/send"); workflow step confusion (approve_tests rank 1 trên entry-point generate_pr).

## Metadata
- 2026 (2026-08-25), Olympia Saha, Amy Wang, Srinivasan Manoharan (PayPal, Inc.), cs.IR + cs.AI, https://arxiv.org/pdf/2608.23992
