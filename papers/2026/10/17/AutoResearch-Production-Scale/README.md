# 2609.30541 — AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework

## Problem
- Karpathy's AutoResearch (LLM sửa training script, giữ bản cải thiện held-out metric) mới thử ở single-GPU, 5 phút/lần, 1 metric duy nhất. Prior work chưa trả lời: paradigm này sống được khi iteration tốn hours multi-GPU, evaluation nhiều tiêu chí, campaign vượt context window không?

## Contribution
- Taxonomy 5 failure mode (mẫu lỗi) production scale: infrastructure fragility (giòn hạ tầng), agent memory decay (suy giảm bộ nhớ tác nhân), search-direction stagnation (tắc hướng tìm kiếm), iteration-cost asymmetry (bất đối xứng chi phí), metric fixation (cố định metric)
- Khung 3 nguyên tắc prevent–persist–redirect thành 3 agent (Researcher, Code Fixer, Criticizer)
- Nguyên tắc cost-dependence: trọng số mỗi nguyên tắc tỷ lệ với chi phí iteration

## Method
- System A: embedding retrieval 128-dim cho 98% catalog sách, multi-GPU, iteration 9–19h, agent viết lại toàn bộ train.py, 60+ iteration/6 run. System B: Semantic ID phân cấp qua RQ-VAE, 1 GPU, 6–52 phút, agent sửa hyperparameter/kiến trúc, 150+ iteration/15 run. Chênh lệch chi phí ~760×.
- Code Fixer (claude-opus-4-6) rewrite script trước khi chạy — bắt lỗi ngữ nghĩa (GPU, DDP, OOM). Criticizer (Opus) chỉ bắn khi stagnation (ngưỡng lợi ích tương đối 8%, cửa sổ 5 iteration), ra directive 2–5 câu rồi clear khi Keep. program.md đẩy S3 cross-job storage. Context: sliding window, best train.py luôn đầy đủ.

## Key Findings
- 220+ experiment/12 tuần. System A peak 6.90% Recall@6 (iter-12) = 1.82× baseline hand-tuned 3.79%, 2.45× deployed baseline 2.82%; across-date mean vẫn 1.63×. System B weighted coherence 0.735 = 2.1× baseline 0.348 (random 0.26).
- Code Fixer bắt 14 latent bugs lượt đầu (3 DDP misconfig, 4 OOM precursor, 3 recomputation, 2 dataloader, 2 eval-loop); DDP wrapper bug sẽ phí 10+ giờ 8-GPU job.
- Directive Criticizer "input representation problem" → 5.48%→5.98% trong 3 iteration. Agent tự design text-only fallback: catalog coverage 5.8×.

## Actionable Insights
- Gate trước khi chạy tác vụ tốn kém: một bước review ngữ nghĩa pre-execution bắt 1 lỗi DDP = tiết kiệm cả chục giờ GPU — với workflow automation, luôn validate plan trước khi execute tốn cost.
- Chỉ can thiệp khi tắc: critic bắn mỗi iteration sinh noise; bắn trên plateau (8%/5 iteration) mới tạo paradigm shift — áp dụng cho content pipeline: trigger review chiến lược chỉ khi KPI đi ngang 5 chu kỳ.
- Bộ nhớ thất bại phải bền: ghi negative result vào storage cross-job ngày đầu — agent vẫn re-test 100-epoch 6 lần dù program.md đã cấm.

## Assumptions & Limitations
- Ablation observational (transition tự nhiên, không controlled A/B); single domain (book recommendation), single org.
- Metric offline (Recall@6, weighted coherence) chưa validate với customer outcome; online pilot đang chạy.
- Không nói: ngưỡng Criticizer (8%, 5) chọn empirical — có thể sai ở domain khác; metric fixation KHÔNG giải được (agent never questions the metric).

## Metadata
- 2026, Aparajith Chandran, Juwon Kim, Saurav Jha, Pablo Castells, Florian Hottier (Amazon Books Core Recs Science), cs.LG/cs.IR, ICDM 2026, https://arxiv.org/pdf/2609.30541
