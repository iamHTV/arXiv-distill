# [2610.22412v1] EnterpriseSynth: Zero-Execution SFT and Evaluation Data from OpenAPI Specs

## Problem
- Tool-using agent (agent dùng công cụ) cần nhiều dữ liệu training + evaluation, nhưng thu thập execution trace (dấu vết thực thi) từ enterprise API (API nội bộ doanh nghiệp) thường unsafe/expensive/infeasible: access control (kiểm soát truy cập), compliance constraint (ràng buộc tuân thủ), rate limit (giới hạn tần suất), risk modifying production data (nguy cơ sửa data production). Các state-of-the-art generator (ToolBench, API-Bank) đều gọi live server → sụp sau enterprise firewall. Paper gọi đây là Execution Paradox (nghịch lý thực thi): (1) sandbox (hộp cát thử nghiệm) high-fidelity hiếm có cho hệ thống nội bộ, (2) loop khám phá trên production risk corrupt state/violate compliance, (3) live call bị latency + rate limit giới hạn.

## Contribution
- EnterpriseSynth: framework zero-execution (không thực thi) chuyển OpenAPI specification thành SFT trajectories (quỹ đạo tinh chỉnh có giám sát) + paired evaluation instances (cặp dữ liệu đánh giá) KHÔNG gọi API nào.
- 3 tính chất không framework nào gộp đủ: grounding in real target spec (ăn spec thật, không hallucinate API surface như AgentInstruct seed từ code), hard per-sample structural gate (cổng kiểm tra cấu trúc cứng từng mẫu — không phải soft editorial loop + LLM judge), no live execution dependency (khác API-Bank/ToolBench).
- Phát hiện methodology general: correctness của verifier (bộ kiểm tra) KHÔNG thể xác lập bằng cách chỉ cho nó input tốt — phải test bằng input nó ĐANG PHẢI reject.

## Method (tóm tắt cốt lõi)
- Pipeline 4 stage: Spec Parser → Intent Generation Agent (Claude Sonnet 5) → Trajectory Generation Agent (chọn tool + sinh params + reasoning + expected-response summary trong 1 call) → Schema Verification Engine (compiler-style firewall, deterministic, KHÔNG phải LLM call: endpoint existence, HTTP method, required parameters, parameter types).
- Output joint dataset: SFT dataset + EnterpriseSynth-Eval (evaluation dataset) + verification metadata + intent specs từ 1 generation pass duy nhất.
- Fine-tune: Qwen2.5-0.5B-Instruct qua LoRA (rank 8, alpha 16, 3 epochs, LR 3e-4) — hardware substitute cho target 7-8B (Mistral-7B/Llama-3-8B).

## Key Findings
- Spec parsing: 4 extraction metrics 100% × 3 APIs (GitHub 845 methods, Stripe 446, Slack 174) — nhưng chỉ sau 2 fix: resolve $ref shared parameters (GitHub required-param count 67 → 1,721) và parse requestBody schema fields thành typed parameters (Stripe POST /v1/charges declare zero OpenAPI parameters, tất cả field trong requestBody).
- Intent generation: 5 endpoints × 3 intents/API (45 total): coverage 100%, exact-string diversity 100% (15/15 unique) — weak proxy (đại diện yếu), semantic clustering chưa implement; manual inspection: intents business-scenario-specific (rotate secret, restrict secret to specific repos).
- Trajectory: TSA (tool selection accuracy) 100% GitHub/Stripe, 93.3–100% Slack; PV (parameter validity) 100% — với caveat self-consistency: cùng Claude Sonnet 5 sinh intent rồi chọn tool → 100% chỉ measure recover own intent, KHÔNG phải generalization.
- Verification (cốt lõi): valid pass rate 100% (45/45); corrupted detection 98% (43/44) — wrong method 12/12, missing required param 11/11, invalid path 12/12, type mismatch 8/9; initial pass CHỈ 57–80%, đạt 98% sau khi adversarial testing (test đối kháng) buộc fix verifier type-checking + corruption harness + parser.
- Downstream (Zoom held-out, 16 intents, single run): Base 12.5% (2/16), Self-Instruct 25.0% (4/16), EnterpriseSynth 87.5% (14/16) — ~3.5× gain của SI; PV: 0.0% / 50.0% (2/4) / 57.1% (8/14).
- 5-seed sweep (mean±std): Zoom Base 12.5±0.0 / SI 23.7±10.3 / ES 66.2±18.0; DigitalOcean Base 31.2±0.0 / SI 37.5±21.2 / ES 53.7±13.7 (per-seed variance cao ±13.7 vs ±21.2 — 1 single run vẫn có thể lose); ES thắng trung bình cả 3 API (Spotify base 46.3±7.1; bảng extract lộn → per-cell Spotify không đáng tin, dùng prose averages).
- Cold-start: 5 hand-authored never-published specs (CRM, HRIS, Procurement, Ticketing, Asset Management; 28 endpoints): Base 23.3% → ES 40.0% (private) vs public held-out Base 18.8% → ES 39.6% (n=30/n=48) — gần như không degradation → evidence genuine schema-grounding, không phải pretraining familiarity. 6 public APIs nữa (Twilio, Notion, OpenAI, Jira, Asana, Trello) đều beat baseline → 17 APIs total.
- Cảnh báo readiness: independent LLM-based eval cho thấy endpoint-selection accuracy 48.9% FALLS xuống 21.3% khi argument selection + values cũng được đánh giá — endpoint metric substantially overestimates end-to-end correctness.

## Actionable Insights
- Bootstrap agent tool-use cho internal API chỉ từ OpenAPI spec (đã có sẵn docs): 45 verified trajectories đủ lift 0.5B model 12.5→87.5% trên held-out API — cold-start không cần sandbox production. Ví dụ: team có CRM REST spec → sinh SFT data overnight, fine-tune model nhỏ chạy nội bộ.
- Verifier phải được adversarial-test: plant corrupted trajectories (wrong method/missing param/invalid path/type mismatch) đo detection rate — initial 57–80% → 98% sau fix. Nếu chỉ check "valid passes" sẽ tin verifier lỗi. Ví dụ: mọi pipeline sinh data đều thêm corruption harness trước khi dùng dataset.
- Đánh giá readiness agent tool-use ở argument level, không chỉ endpoint level: metric TSA 48.9% nhưng end-to-end (arg + values) 21.3%. Ví dụ: eval agent chọn endpoint đúng nhưng tham số sai (wrong item ID) vẫn tính FAIL.

## Assumptions & Limitations
- Điều kiện: OpenAPI spec machine-readable exists; spec quality quyết định ceiling (GitHub documents auth bằng prose, zero securitySchemes → auth extraction có nothing to check).
- Paper thừa nhận: pilot scale (3–5 APIs, 45–89 examples/experiment, target ~65 specs); self-consistency confound (cùng model sinh intent + chọn tool); model-scale gap (0.5B substitute, untested at 7–8B); non-uniform generalization (DigitalOcean single-run loss genuine variance); structural gate không semantic — well-typed nhưng nonsense value (negated charge) vẫn PASS; workflow completeness (multi-step) N/A ở pilot (intent single-endpoint); prompt-only + AgentInstruct baselines chưa implement; dependency-graph planning layer (target architecture) chưa có.
- Limitation paper KHÔNG nói: intent diversity chỉ exact-string (semantic chưa đo); single-endpoint trajectories = không cover cascading multi-step variables (đúng failure mode đã nêu ở intro); Claude Sonnet 5 generation cost/quality dependence — open-source generator chưa test; chỉ OpenAPI, không GraphQL/gRPC.

## Metadata
- Năm: 2026 | Tác giả: Rashmi Thimmaraju (Long Island University), Natan Vidra (Anote AI), Spurthi Setty (Stevens Institute of Technology) | Category: cs.SE | PDF: https://arxiv.org/pdf/2610.22412v1 | Citation: [NO DATA — published 14 Oct 2026]
