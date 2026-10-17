# Skill: Evidence-Aware Agent Orchestration (orchestration agent aware evidence + gate opinion)
Source: 2608.26990v1
Type: framework / workflow

## Khi nào dùng skill này
- Xây dựng LLM-agent system cho research/report (nghiên cứu, báo cáo) nơi evidence heterogeneous (nhiều nguồn, chất lượng khác nhau) và có nhiều model/provider.
- Muốn có 2 cấp độ: default path rẻ cho batch/scheduled, agentic path cho phân tích sâu — mà không ép multi-agent cho mọi request.
- Có optional skill/plugin extension mà output cần gate trước khi vào evidence chain.
- KHÔNG nên dùng: system chỉ cần 1 LLM call đơn giản; hoặc đã có evidence pipeline đồng nhất (đồng chất lượng, đồng nguồn) — không cần state tagging.

## Input cần có
- Danh sách data source + field mỗi source support (market adapter: quotes, bars, fundamentals, news, sentiment...).
- Danh sách model route (hosted, compatible endpoint, provider-specific, local) với capability mỗi route (structured output, tool calling, vision, context limit, latency, cost).
- Danh sách core role (ví dụ: technical, intelligence, risk, decision) và optional Strategy Skill với declared metadata + tool requirements.

## Các bước thực hiện
1. **Evidence acquisition + state tagging:** mỗi evidence block gắn state ∈ {available, missing, not_supported, fallback, stale, estimated, partial, fetch_failed}; retain source + timestamp metadata; screening engine (deterministic filters, factor scores, risk constraints, optional LLM reranking) tạo bounded candidate set.
2. **Structured context construction:** tính features, build bounded evidence block; project state vào prompt — model thấy "field X: fetch_failed" thay vì field trống.
3. **Model & capability routing:** tách routing layer khỏi research logic; resolve request format + model name theo route; report unsupported capability thay vì silently substitute operation khác; capability admission route-specific (generation route ≠ tool-capable agent route).
4. **Role + extension admission:** core role output qua role-specific parser; Strategy Skill output qua signal-eligibility partition O_ext* = {o : valid_signal(o)} — invalid → diagnostics, không vào evidence chain.
5. **Disagreement-aware synthesis:** xây disagreement summary D = Disagreement(O_core ∪ O_ext*) làm explicit input cho decision agent; d_0 = Synthesize(E, O_core, O_ext*, D).
6. **Conservative risk override (RiskGuard):** post-synthesis, risk step chỉ được downgrade — veto buy→hold; downgrade buy→hold/sell, hold→sell; KHÔNG upgrade.
7. **Freeze + conformance test:** pin git revision + environment (Python, pytest, LiteLLM version); chạy claim-mapped test manifest; báo cáo chính xác cái gì pass và cái gì KHÔNG được establish (quality, forecast, returns).

## Output mong đợi
- Structured research report + optional inspection record (selected context, evidence-quality summary, diagnostics).
- Conformance report: N/N contract test pass, mapped theo contract family, kèm boundary statement (platform unsupported, dependency pin).

## Ví dụ áp dụng
- Agent research chứng khoán VN: adapter HOSE/HNX + news + fundamentals, mỗi block gắn state; default profile chạy batch tối đa (1 generation call); agentic profile có technical/intelligence/risk/decision role + 2 skill (MA crossover, volume breakout); skill output invalid → diagnostics; disagreement summary cho decision agent; RiskGuard chỉ downgrade; freeze rev + pytest manifest 500 case → report conformance 500/500, KHÔNG claim forecast accuracy.

## Gotchas
- Mocked test pass ≠ semantic quality: test với mock service không chứng minh chất lượng dưới live data/model/credentials — phải nói rõ boundary này.
- Manifest selected post-exploration không phải prospective sample: đừng report "all tests pass" như thể đó là toàn bộ suite — ghi rõ case nào deselected và vì sao.
- Disputed heuristic: nhiều technical-analysis perspective (Chan theory, wave theory) là disputed financial heuristics — kết hợp với LLM KHÔNG tạo predictive value; valid schema ≠ correct conclusion.
- Trusted extension inputs: external strategy package là trusted input — prompt injection/poisoned content/unsafe tool request có thể lọt; registered interface giảm exposure nhưng không loại bỏ.
- Dependency pin: test có thể fail trên version trong declared range (DSA: timeout dưới LiteLLM 1.98.0) → pin version và ghi nhận.
- Optional snapshot giữ selected context, không phải complete context — không guarantee exact replay; đừng gọi đó là audit trail đầy đủ.
- Native platform probe riêng: platform-specific check tách ra khỏi portable manifest, không count là portable failure.
