# 2608.26990v1 DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research

## Problem
- LLM có thể summarize thông tin tài chính, nhưng một hệ thống stock research vận hành được phải: assemble evidence heterogeneous, expose data không có sẵn và capability của model, kiểm soát cách generated opinion ảnh hưởng report cuối. Prior work (FinGPT, FinAgent, FinCon, TradingAgents) tập trung endpoint (trading, forecasting) — chưa ai tách riêng bài toán systems: market expose field không đều, provider expose structured-output/tool capability không đều, core role agent khác optional extension — những asymmetry này phải observable, không được giấu sau uniform conversational interface.

## Contribution
- Kiến trúc 5 stage evidence-to-report cho stock research lặp lại được across heterogeneous markets và data sources.
- Tách model routing khỏi research logic; phân biệt configured core role agent vs optional Strategy Skill extension với cơ chế output-admission khác nhau.
- Profile-level control semantics cho evidence state, capability admission, output validation, risk handling, observable failure — không claim một implementation chung cho mọi profile.
- Reference implementation open-source + frozen claim-mapped conformance evaluation (đánh giá tuân thủ) — boundary là software behavior, KHÔNG phải analytical/financial effectiveness.

## Method
- 5 stage: (1) evidence acquisition — market adapter lấy quotes, bars, fundamentals, announcements, news, sentiment; screening engine (deterministic filters, factor scores, risk constraints, optional LLM reranking) tạo bounded candidate set; (2) structured context construction — tính technical features, build bounded evidence block, normalize availability/degradation state (available, missing, not_supported, fallback, stale, estimated, partial, fetch_failed), retain source/timestamp metadata; (3) model and capability routing — resolve provider-specific request format và model name bên dưới workflow (hosted, compatible endpoint, provider-specific route, local model); capability admission route-specific; (4) optional role reasoning + controlled synthesis — core role agents (technical, intelligence, risk, decision) qua role-specific parser; Strategy Skill opinion qua signal-eligibility partition O_ext* = {o ∈ O_ext : valid_signal(o)}, invalid → diagnostics; disagreement summary D = Disagreement(O_core ∪ O_ext*); decision d_0 = Synthesize(E, O_core, O_ext*, D); (5) report + optional context và diagnostics.
- Hai execution profile: default report profile (bounded context → generation model → validation → safeguards → render; batch/scheduled, ít model call hơn) và agentic profile (thêm role agent, Strategy Skill, disagreement-aware synthesis, post-synthesis risk override RiskGuard). RiskGuard 3-state: veto buy→hold; downgrade buy→hold/sell, hold→sell; KHÔNG upgrade.
- 6 regional market path: mainland China, Hong Kong, US, Japan, South Korea, Taiwan; 15 Strategy Skill bundled (moving-average signals, trend following, volume breakouts, event-driven analysis, growth quality, expectation repricing, market themes, Chan theory, wave theory); surface: CLI, API, browser, desktop, scheduled job, messaging adapter.
- Evaluation: frozen Git revision 0ca56cbee2dff5cf23b1fc59c16e2d48e61ba85c (26/8/2026), Python 3.10.9, pytest 7.1.2, LiteLLM 1.89.3; manifest 1,458 case, deselect 1 (native-Windows route), execute 1,457 case — zero failures/errors/skips trong 102.532s; 596 case map retrospective về 6 contract family: evidence context 74, model backends/routing/config 194, agent orchestration/routing 85, runtime facts/disagreement/risk/guardrails 87, strategy registry/tool surface 60, strategy attribution/outcome lifecycle 96.

## Key Findings
- 1,457/1,457 portable backend contract test pass (zero failure/error/skip, 102.532s) — establishes implementation conformance cho tested software contracts.
- 596/596 case trong 6 contract family map tới LLM-agent architecture đều pass — evidence-state distinction, unsupported capability state, role sequencing, structured role output, disagreement vào synthesis, risk override conservative transition đều được exercise.
- [NO BENCHMARK] về report quality, forecasting accuracy, investment returns — paper KHÔNG claim superiority; rõ ràng: "This evidence establishes implementation conformance... not superior report quality, forecasting accuracy, or investment returns."
- Boundary probe: native-Windows route unsupported (Codex App Server), Unix-shell assumption trong Docker-entrypoint test — portability có giới hạn.
- Dependency sensitivity: 1 prompt-cache test timeout dưới LiteLLM 1.98.0 → pin 1.89.3.

## Actionable Insights
- Evidence-state discipline: never let missing data become neutral evidence — tag mỗi evidence block với state (available/missing/fallback/stale/partial/fetch_failed) và project state đó vào prompt. Ví dụ: agent research VN stocks khi nguồn dữ liệu fail → ghi "capital-flow: fetch_failed" trong context thay vì bỏ trống field (bỏ trống = model xử lý như neutral signal).
- Hai-profile architecture: giữ default path rẻ (report profile, batch/scheduled, ít call) và agentic path đắt (role + skill + disagreement + risk override) — không ép multi-agent cho mọi request; so sánh 2 profile trên cùng task với blinded rubric trước khi claim agentic tốt hơn.
- Gate extension opinions: output của skill/plugin optional phải qua validity partition trước khi vào evidence chain, invalid → diagnostics; disagreement phải explicit input cho decision agent; risk override chỉ downgrade (buy→hold→sell), never upgrade.

## Assumptions & Limitations
- Điều kiện: research report endpoint, không đặt lệnh; external strategy package là trusted input dưới permission model hiện tại.
- Limitation paper thừa nhận: analytical validity (conformance ≠ factual accuracy/forecast quality); temporal validity (provider thay đổi, không có immutable point-in-time dataset, look-ahead leakage không loại bỏ); inspection/provenance (snapshot optional, selected không phải complete context, không guarantee exact replay, không có claim-level provenance); model/strategy validity (valid schema ≠ correct conclusion; nhiều technical-analysis perspective bundled là disputed financial heuristics); security (external news/model output/skill package có thể chứa prompt injection, poisoned content, unsafe tool request, secrets); generalization (market coverage uneven, manifest selected post-exploration, pinned environment).
- Limitation CHƯA nói: test do contributor viết, assertion overlap nhiều — không phải independent observation; mocked service không establish semantic quality under live data; chưa có ablation isolating role decomposition, evidence-state disclosure, Strategy Skill, disagreement handling, risk control; chưa đo provider difference về quality/latency/token/cost dưới common protocol.

## Metadata
- 2026, Linsen Zhu, Yi Shi, cs.AI (file PDF ghi "Preprint", keywords: LLM agents; financial agents; multi-agent systems), https://arxiv.org/pdf/2608.26990v1, code: https://github.com/ZhuLinsen/daily_stock_analysis, citation count: không tìm thấy [NO BENCHMARK]
