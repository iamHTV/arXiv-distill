# Skill: Local Contract-Conditioned Privacy Enforcement (send-time wrapper cho agent action)
Source: 2610.18007v1
Type: framework / workflow

## Khi nào dùng skill này
- Agent của bạn gửi thông điệp ngoại vi (email, Slack, CRM update) sau khi đọc private context (mailbox, Notion, user PII — thông tin nhận dạng cá nhân).
- Cần giảm privacy leakage VÀ remote enforcement cost (chi phí thực thi remote — token checker/repair LLM) đồng thời.
- Lo ngại strategic requester (người yêu cầu chiến lược: hỏi exact values, raw records, source evidence, "all details" với appearance task legit).
- KHÔNG nên dùng: action không có private context (không cần enforcement); deployment không chấp nhận fail-closed block; nội dung không nhạy cảm thấp (MG-only đủ, thậm chí không cần checker).

## Input cần có
- Vị trí wrap được: access vào tool-send boundary (nơi agent gọi email-sending / message-sending tool) + ability block send + allowlist exact-draft-only.
- Annotated sensitive items hoặc policy item list cho từng loại task (hoặc rule must_generalize theo data type: name/phone/address/salary/health...).
- Local on-prem rewriter (ví dụ Gemma 4B quantized qua Ollama, temp 0.0, 12k context) — any trusted local editor.
- Boolean PrivacyChecker (remote hoặc local) + cơ chế return feedback verbatim cho rewriter.
- Baseline metrics: remote tokens + checker calls + item/secret-level leakage + UsableRate (ojo: utility judge riêng với enforcement path).

## Các bước thực hiện
1. Install send-time wrapper: capture recipient fields + subject + body trước delivery; build normalized email signature; chỉ cho send đúng draft đã pass enforcement path; mismatch resend → re-inspection (agent không tự decide check output mình).
2. Generate information-release contract từ user instruction + original draft — tách 4 concerns: (a) must_preserve + required_slots (benign task slots cần giữ), (b) must_generalize + privacy-risk rules (abstract sensitive/confidential/source-specific/reconstructive details), (c) information_shape + safe_output_shape (giữ cấu trúc requested: status update, bullet list, next step, high-level range), (d) must_not_add (cấm hallucinated replacement facts, new values, new commitments, private-source references, unsupported attachments) + safe-substitution guidance (abstraction thay deletion khi deletion khiến email vô dụng). Contract KHÔNG phải oracle label — là deployable rewrite policy.
3. Local rewrite: Gemma-class executor nhận original subject/body + contract (+ checker feedback nếu repair round) → rewritten subject/body + change summary; minimal edits: preserve communicative purpose, generalize sensitive details, avoid unsupported facts, keep professional tone.
4. Final gate: PrivacyChecker Boolean pass/fail trên rewritten draft; pass → send exact checked draft; fail → feedback verbatim → local repair (budget ≤3 rounds); hết budget → BLOCK (fail closed).
5. Risk-adaptive routing: MG (Gemma-only, không checker) chỉ cho low-risk sends khi µ∆Rremote > λ∆L (saved remote cost outweigh expected privacy loss); high-risk hoặc attack-suspected → MG+C (full).
6. Monitor: CostAmp = RemoteTokens(attack)/RemoteTokens(normal) (target ≤1.02×); checker-call amplification; item-level + secret-level leakage (exact/paraphrased/reconstructive); UsableRate trên benign task shell; slot retention + semantic drift. Anticipate: normal leakage ~11.4%→~4.0%; attack 28.2%→18.8%; remote tokens −17.6% (normal) / −36.6% (attack).

## Output mong đợi
- Enforcement pipeline hoạt động fail-closed; giảm leakage 64.7% (normal) với utility tăng (UsableRate 85.2→92.6%); CostAmp gần 1.0× dưới strategic attack (vs 1.32× baseline); remote token billing −17.6–36.6%; local ~1.1–1.2M Gemma tokens/task-set là deployment cost riêng.

## Ví dụ áp dụng
- Solopreneur dùng agent soạn reply khách hàng có access order database + user address/phone. Wrapper: contract ghi must_preserve order status + delivery date (generalize thành range), must_generalize customer phone/address thành "on file", must_not_add new discount commitments. Under customer asking "send exact invoice numbers raw": baseline soạn leak 28.2% → wrapper 18.8%, checker calls 1.79→1.02 average, remote bill −36.6%.

## Gotchas
- Gemma-only KHÔNG đủ cho high-risk: residual reconstructive leakage (disease names removed nhưng respiratory-monitoring cues còn → recipient infer được) — checker bắt buộc cho sensitive sends.
- Contract có thể sai: infer wrong task type, omit required slot, over-generalize, preserve unsafe detail → monitor slot retention (target ≥0.97) + drift (≤~0.05).
- Generic "remove private info" prompt yếu hơn contract 36–54% relative — KHÔNG省略 contract fields (required_slots + information_shape đặc biệt quan trọng: bỏ → −27.2%/−52.1% vs −36.3%/−54.1%).
- Checker/feedback loop: feedback phải verbatim về local executor, KHÔNG quay lại remote action LLM (đó là MB — tốn 1.32× dưới attack).
- Leakage evaluator cùng family với checker → self-preference bias risk; cần spot-check bằng human.
- extending sang Slack/calendar/CRM cần action-specific information-shape constraints, KHÔNG copy email contract nguyên.

## Dry run test
- Test case giả (support agent, 50 tasks tương tự): baseline MB: normal leak 11.4%, usable 85.2%, remote 8.7M tokens, attack leak 28.2% CostAmp 1.32× call 1.69×. Chạy skill step 1-6: wrapper + contract (4 fields) + Gemma-local + checker ≤3 rounds fail-closed → normal 4.0% usable 92.6% remote 7.2M (−17.6%), attack 18.8% CostAmp 1.02× calls 1.02, usable safe-shell 100%, rounds 0.04. Offline replay ablation verify contract matters: generic 7.38/32.21 → contract 4.70/14.77 (−36.3/−54.1%). Output: pipeline fail-closed với metrics cải thiện đồng thời cả privacy + cost + utility → có nghĩa → [SKILL VALID].
