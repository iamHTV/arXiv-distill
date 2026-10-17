# Skill: Prompt Internalization — Fine-tune SLM thay thế Prompted Frontier Model
Source: 2610.10827v2 (Grammar Concept Annotation at Scale, Preply)
Type: workflow (data pipeline + fine-tuning + serving)

## Khi nào dùng skill này
- Production feature đang prompt frontier model (GPT-class) với system prompt dài (hàng nghìn token) và cost vượt serving budget khi scale.
- Task có output cấu trúc xác định (schema cố định: nhãn, span, nhúng correctness) và có teacher model tạo supervision.
- KHÔNG nên dùng khi: task thay đổi liên tục (prompt flex hơn adapter weights); không có capacity fine-tune/serve GPU; output quá mở (free-form generation thuần).

## Input cần có
- Task schema contract: field definitions, output format (ví dụ pipe-delimited lines), invariants (span phải là substring của input, explanation non-empty iff INCORRECT).
- Teacher model access (GPT-class) để review/re-annotate và sinh synthetic.
- Production logs mẫu (production annotations) — vài chục nghìn records.
- Base SLM (Qwen3.5-class 0.8B/4B), LoRA infra, vLLM + autoscaling single-GPU instances.
- Human-curated golden benchmark ≥2 sets: 1 set mirror production distribution, 1 set error-enriched diagnostic.

## Các bước thực hiện
1. Formulate task thành structured annotation single-pass: input pair (raw utterance, upstream correction) → tập tuples (concept, exact span, correctness, explanation); định nghĩa nested eval criteria L1 (label) / L2 (+exact span) / L3 (+correctness).
2. Review production data: sample uniform + heuristic (ưu tiên anomaly: count bất thường so với length, low span coverage); hybrid neuro-symbolic — deterministic linguistic anchors (spaCy) + hand-crafted rules + word-level edit diff; teacher model full review/re-annotation pass (retain/correct/remove/add tuples); deterministic post-validator enforce invariants.
3. Synthetic enrichment cho rare classes: structural backbone (label + correctness flag sequences) từ production đã filter; sampling 3 chế độ (uniform, error-weighted, smoothed inverse concept-frequency); inject error type vào generation plan (misuse, omission, confusable substitution) thay vì post-hoc token corruption; teacher realize; post-validate.
4. Consolidate: dedup cross-source, loại bỏ mọi record trùng golden benchmark. Target ~187k groups từ ~190k raw.
5. Fine-tune completion-only LoRA: pack 5 input pairs/conversation; rank cao cho model nhỏ (r=128 cho 0.8B); chọn checkpoint theo min teacher-forced validation loss, early-stop patience 3 evals.
6. Prompt compaction: verbose teacher prompt (ví dụ 3,810 token) → compact prompt (375 token, −90%) chỉ giữ concept names + schema contract + brief rules; shrink max sequence (7,000 → 2,500).
7. Serve vLLM autoscaled single-GPU; packed requests; fallback về teacher model khi validation/service fail. Đo p95 latency + cost/request so với baseline.
8. Evaluate: micro P/R tại L1/L2/L3 trên cả 2 benchmarks; cluster bootstrap CIs; paired randomization test vs teacher; LLM-as-judge cho explanation NHƯNG phải human-audit trước khi kết luận.

## Output mong đợi
- Fine-tuned 0.8B vượt prompted teacher model ở mọi matching level (paper: L3 recall 78.89 vs 62.87 trên Golden; 80.88 vs 76.04 trên Golden2, p < 0.0001).
- Cost ~16× reduction (6.2% baseline), p95 latency ~4.3 s, parse failure < 0.1% (vs 75–92% base model).
- Online A/B: engagement +15.8%, GMV from new lessons +13.2% (end-to-end feature).

## Ví dụ áp dụng
- Solopreneur có SaaS hỗ trợ khách hàng: đang prompt GPT với 4,000-token prompt để classify + extract evidence span từ ticket. Áp dụng skill: review 50k tickets đã label, sinh synthetic cho category hiếm, LoRA fine-tune Qwen3.5-0.8B với compact prompt 400 token, vLLM 1 GPU, fallback GPT. Kỳ vọng: quality ngang hoặc hơn, cost ~1/16.

## Gotchas
- Raw teacher supervision KHÔNG đủ: degrade 23.6 pp khi chuyển L1→L2 (exact span) — phải có review pass + post-validator, không chỉ sinh data.
- Uncalibrated LLM judge thiên vị teacher của chính nó (99.06% vs 93.88%, sau human audit ≈95% hòa) — luôn audit judge trước khi công bố comparative result.
- Model nhỏ cần LoRA rank cao (r=128) để chứa rules; 0.6B earlier-generation có thể unparseable 57% dù validation loss hội tụ — test format adherence riêng, đừng tin validation loss.
- Single training run, no seed variance — đừng over-interpret difference nhỏ giữa các config.
- Cost reduction tính recurring detection compute thôi — upstream (transcription, correction, fallback) không tính vào.
