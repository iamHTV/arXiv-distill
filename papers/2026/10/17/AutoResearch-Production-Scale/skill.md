# Skill: AutoResearch Production Scaffolding
Source: 2609.30541
Type: framework (multi-agent orchestration cho long-horizon experiment loop)

## Khi nào dùng skill này
- Chạy agent loop tự động tối ưu hóa (ML training script, content pipeline, automation) mà mỗi iteration tốn compute/chi phí thật
- Campaign dài vượt context window, cần nhiều run/job nối tiếp
- KHÔNG nên dùng: tác vụ 1 bước, iteration rẻ và discard được (chỉ cần auto-revert), hoặc evaluation đơn giản không cần agent

## Input cần có
- Tác vụ lặp được: script/code hoặc config cần agent sửa (train.py, config)
- Evaluator immutable: metric (scalar hoặc multi-criteria) agent KHÔNG được sửa
- program.md: research program + accumulated findings + constraints (negative results đã biết)
- Compute budget + ngưỡng keep (τkeep), ngưỡng stagnation (τstag), window

## Các bước thực hiện
1. Xác định loop nhỏ nhất (hypothesis → run → evaluation) vẫn tạo signal — over-broad loop phí budget, over-narrow loop không đạt improvement.
2. Thêm Code Fixer gate (pre-execution): agent Opus-class review + rewrite single-pass script của Researcher trước khi chạy; bắt DDP/multi-GPU misconfiguration, OOM precursor, recomputation, dataloader bug, eval-loop error. KHÔNG dùng two-step Reviewer→JSON→author (lỗi malformed JSON liên tiếp).
3. Persist cross-job: sau mỗi Keep, cập nhật program.md + iteration summary → durable storage (S3); encode constraints và known failures. Mỗi job mới inherit toàn bộ history.
4. Cấu hình Criticizer (stagnation-only): bắn khi best metric không cải thiện >8% relative trong 5 iteration; ra directive 2–5 câu gợi ý VÙNG design space mới (không phải code cụ thể); clear directive khi Keep. 3 iteration = noise, 8 iteration = quá muộn.
5. Chia model theo vai trò: Sonnet-class cho đường sinh code khối lượng lớn; Opus-class cho gate/critic where wrong call tốn hours compute.
6. Scale theo chi phí: iteration đắt (giờ) → pre-execution gate; iteration rẻ (phút) → post-execution automatic revert. Multi-metric reporting + human QA giữa các run để giảm metric fixation.

## Output mong đợi
- Agent loop chạy hàng trăm experiment mà không mất iteration vào coordination failure; catch paradigm shift qua directive; negative results không bị re-test (giảm, không hết).

## Ví dụ áp dụng
- Pipeline tối ưu content: mỗi iteration = agent chỉnh chiến lược đề xuất + đo CTR. Code Fixer validate plan trước khi launch; Criticizer trigger "bài toán không phải nội dung mà là representation" khi CTR đi ngang 5 chu kỳ.

## Gotchas
- Two-step review (Reviewer trả JSON → agent khác viết lại) dễ lỗi malformed JSON 14 lần liên tiếp — luôn single-pass rewrite.
- Ngưỡng 8%/5 chọn empirical trên recommendation — calibrate lại domain khác.
- Agent vẫn re-test cấu hình bị cấm ~6 lần dù program.md ghi rõ — memory decay giảm chứ không hết.
- Metric fixation KHÔNG giải được: agent never questions the metric — phải có human QA giữa các run.
