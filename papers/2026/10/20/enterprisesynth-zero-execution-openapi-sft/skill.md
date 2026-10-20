# Skill: EnterpriseSynth Bootstrap — dữ liệu SFT + eval agent tool-use từ OpenAPI spec (zero-execution)
Source: 2610.22412v1
Type: workflow / framework

## Khi nào dùng skill này
- Cần training data cho agent dùng công cụ nội bộ (CRM, ERP, HRIS, ticketing) mà KHÔNG có sandbox an toàn để gọi API thật.
- Bootstrap (khởi động) tool-use capability cho model nội bộ chỉ từ OpenAPI/Swagger docs đã có.
- Cần paired evaluation dataset cho agent tool-use mà không có ground-truth humain annotation.
- KHÔNG nên dùng: API đã có sẵn execution trace thật (dùng dữ liệu thật tốt hơn); spec không machine-readable (auth chỉ trong prose); tác vụ multi-step cascadingcomplex ở pilot — skill này hiện chỉ single-endpoint.

## Input cần có
- OpenAPI/Swagger spec file (JSON/YAML) của target API.
- Generation LLM (Claude Sonnet 5 class) cho intent agent + trajectory agent.
- Deterministic schema validator (JSON Schema) cho verification engine — KHÔNG dùng LLM làm gate.
- Open-weight model để fine-tune (Qwen2.5-0.5B class trở lên) + LoRA setup (rank 8, alpha 16, 3 epochs, LR 3e-4).
- Held-out specs (chưa dùng training) + ideally 5 never-published private specs để cold-start check.

## Các bước thực hiện
1. Parse spec: extract endpoints, parameters, descriptions, auth, response-schema presence. BẮT BUỘC 2 fix: (a) resolve $ref shared parameters (không resolve → miss đến 1,721 required params trên GitHub-class spec), (b) parse requestBody schema fields thành typed parameters (POST/PUT/PATCH thường chỉ khai báo field ở đây). Verify bằng ground truth recomputed độc lập, không reuse logic của parser.
2. Intent generation: mỗi endpoint sinh 3+ enterprise intents (business-scenario-specific, không generic). Manual-inspect mẫu — coverage/diversity aggregates (100%) là weak proxy, semantic clustering chưa có.
3. Trajectory synthesis: mỗi intent + candidate tool list (5 source endpoints + 10 seeded distractors, shuffle per trial) → 1 call chọn tool + params + reasoning + expected-response summary. CAVEAT: nếu cùng model sinh intent rồi chọn tool → TSA 100% là self-consistency, không phải generalization; dùng cross-model/human intents để đo accuracy thật.
4. Structural verification gate (deterministic, offline): check endpoint existence, HTTP method, required parameters, parameter types; chỉ admit trajectory valid. ADVERSARIAL-TEST chính verifier: plant corrupted variants (wrong method / missing required param / invalid path / type mismatch) — initial pass thường chỉ catch 57–80%; fix type-checker + harness + parser đến ≥98% (43/44) rồi mới dùng dataset.
5. Fine-tune LoRA trên verified trajectories; evaluate TSA + PV (parameter validity conditioned on correct selection) trên held-out specs. Multi-seed (≥5 seeds) vì per-seed variance cao (ví dụ DigitalOcean ±13.7 vs ±21.2 — single run vẫn có thể lose dù average thắng).
6. Argument-level eval: independent LLM judge đánh giá cả argument selection + values, không chỉ endpoint — endpoint accuracy 48.9% nhưng end-to-end chỉ 21.3%. Dùng con số end-to-end cho readiness decision.

## Output mong đợi
- Verified SFT dataset + EnterpriseSynth-style eval set + verification metadata (per-sample gate results). Readiness report: TSA/PV per held-out API, per-seed mean±std, private-cold-start accuracy (kỳ vọng: private ≈ public, ví dụ 40.0% vs 39.6% = genuine grounding), end-to-end argument-level accuracy.

## Ví dụ áp dụng
- Solopreneur có CRM REST API (10 endpoints): step 1 parse → resolve $ref + requestBody → 38 params; step 2: 15 intents (3/endpoint × 5 endpoints) all unique; step 3: 15 trajectories (TSA 100% nhưng flag self-consistency); step 4: corruption harness 15 variants → verifier catch 14/15 (93%) → fix type-checker → 15/15 (100%); step 5: LoRA fine-tune Qwen2.5-0.5B → held-out Jira-like spec TSA 12.5% → ~66%, private holdout 40%; step 6: arg-level judge → end-to-end ~21%. Result: deploy model nhỏ nội bộ, biết chính xác readiness thật.

## Gotchas
- Structural gate ≠ semantic: well-typed nonsense (negated charge −$100) vẫn PASS → thêm semantic/business-rule checks cho field có ý nghĩa nghiệp vụ.
- Auth thường không machine-readable (GitHub spec: zero securitySchemes) — auth-related trajectories unverifiable từ spec alone.
- Self-consistency confound: ĐỪNG report 100% TSA như generalization — cần cross-model intents.
- Multi-step workflows (cascading variables) chưa supported ở pilot — intent single-endpoint only.
- Fine-tune effect không uniform: luôn multi-seed; single-run loss là genuine variance, đừng rerun đến khi đẹp.

## Dry run test
- Test case giả (CRM 10 endpoints): step 1 → 10 endpoints + 38 typed params sau 2 fix (naive parse chỉ thấy 9 params). Step 2 → 15 unique intents, manual check: scenario-specific (grant discount approval to role X). Step 3 → 15 trajectories, TSA 100%/PV 100% (flag: self-consistency). Step 4 → corruption 15 → catch 14 (93%) < 98% → fix → 15/15; valid pass 15/15. Step 5 → LoRA Qwen2.5-0.5B, 5 seeds: held-out mean 66.2±18.0 vs base 12.5±0.0, SI 23.7±10.3; 1 seed lose (variance). Step 6 → arg-level 21% end-to-end. Output: dataset + eval set + readiness số liệu → có nghĩa, follow tốt → [SKILL VALID].
