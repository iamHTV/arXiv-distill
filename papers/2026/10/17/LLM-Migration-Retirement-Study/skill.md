# Skill: LLM Retirement Readiness Audit (kiểm toán readiness trước model retirement)
Source: 2609.31288
Type: evaluation-method / audit-workflow

## Khi nào dùng skill này
- Production app gọi commercial LLM API (OpenAI/Anthropic/Google) — provider retire model theo schedule riêng
- Đánh giá dependency risk của LLM product trước khi đầu tư/adopt model mới (đặc biệt fine-tuned)
- Cần migration playbook theo architecture khi deprecation notice xuất hiện

Tình huống KHÔNG nên dùng: self-hosted open-weight model (không có shutdown date do provider kiểm soát); app không production (không có breakage cost).

## Input cần có
- Danh sách model identifiers/endpoints đang dùng trong codebase (grep model names, dated snapshots như claude-3-5-sonnet-20241022)
- Providers' deprecation pages (OpenAI, Anthropic, Google) — announcement date, shutdown date, notice length
- Architecture classification: prompt-only / agent-tools / RAG / fine-tuned (từ patch content hoặc code review)
- Repository metadata (stars, archived flag) — KHÔNG dùng stars làm proxy cho readiness (82% reactive ở mọi tier)

## Các bước thực hiện
1. Inventory: grep codebase cho model identifiers (word boundaries; short ids như o1 cần delimiters 2 bên) + dated snapshot identifiers (pinned for reproducibility — 6/118 genuine migrations có proximate cause là pinned snapshot). Record files chứa identifier (median 1 file, 26% ≥3 files).
2. Externalize: nếu identifier hard-coded (94% cases) → env var hoặc model registry map. Sau externalize, migration = 1-line config change thay vì 2 files/6 lines (prompt-only) đến 14 files/693 lines (fine-tuned).
3. CI deprecation check: nightly job query deprecation pages, fail CI nếu identifier trong danh sách retire <90 days (hoặc < notice length). Đặt internal migration deadline = announcement + (notice − 30 days), KHÔNG phải shutdown − 7 days.
4. Architecture-aware migration budget: prompt-only 2 files/6 lines; agent 5 files/63 lines; RAG 7 files/155 lines; fine-tuned 14 files/693 lines + retrain (replacement base model invalidates tuned checkpoint). Kiểm tra parameter compatibility: replacement model có thể reject max tokens hoặc non-default temperature (7.5% migrations) — rename alone không restore service.
5. Silent-failure guard: audit exception handlers around LLM calls — retirement error có bị convert thành apologetic message/null/demo-mode fallback/constant answer không (8% genuine migrations)? Monitoring alert trên fallback/demo-mode response rate, không chỉ error rate.
6. Abstraction layer assessment: nếu đã có LiteLLM/OpenRouter/gateway/model map → fix nhỏ hơn (4 files/20 lines) nhưng VẪN 70% reactive — layer giảm size KHÔNG đảm bảo timely. Thêm retirement watch + migration drill định kỳ.

## Output mong đợ
- Retirement watch list: identifiers + shutdown dates + internal deadlines.
- Migration estimate: files/lines theo architecture + parameter compatibility check + retrain cost (fine-tuned).
- CI gate fail trước shutdown date.
- Ví dụ: app dùng claude-3-5-sonnet (76-day notice, 91% reactive) → audit tại announcement, internal deadline announcement+46 days, migrate 2 files/6 lines (prompt-only), 0 silent failures.

## Ví dụ áp dụng
- E-commerce chatbot dùng GPT-4 Turbo Preview (181-day notice, 59% reactive): inventory → identifier hard-coded trong 3 files → externalize thành MODEL_ID env var → CI check nightly → khi OpenAI announce shutdown, internal deadline announcement+151 days → migration 1-line config + regression test (16% migrations touch test file; 4.5% mention eval suite — nên thêm harness reveal item-level regressions).

## Gotchas
- KHÔNG tin "we support multiple providers" (abstraction layer) như evidence of resilience — 70% still reactive, layer chỉ giảm fix size.
- KHÔNG tin "we survived a previous retirement" — 85 repos hit ≥2 retirements: 73% reactive first event, 73% later ones (CI −13 to +13pp). Later migrations land sooner (22 vs 45 days) nhưng vẫn sau shutdown.
- KHÔNG dùng repo popularity (stars) làm readiness proxy — 82% reactive ở mọi star tier (reweighted 82/80/81/82).
- Soft/movable shutdown dates (Google "earliest" style) KHÔNG tạo deadline effect: migrations trickle 23–29/tuần, không spike — cần internal deadline cứng riêng.
- Beware migrations INTO the retired model (gemini-1.5-flash → gemini-2.0-style) — direction filter loại 33% candidates; verify arrow direction trước khi đếm.
- Short identifier matching cần word boundaries 2 bên (o1 match trong "o1-preview" vs "gpt-4o" sai).
- 38% keyword-matched commits non-genuine (catalogue refreshes, doc updates) — validate sample trước khi kết luận ecosystem-level.
- Fine-tuned adoption: retirement cost (693 lines + retrain) vượt deployment cost — budget migration trước khi adopt.
