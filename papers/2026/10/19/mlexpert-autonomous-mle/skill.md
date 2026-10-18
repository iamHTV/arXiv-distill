# Skill: Windowed Interaction RL (WIRL) cho Long-Horizon Agentic Tasks
Source: 2610.22344v1
Type: training-method / workflow

## Khi nào dùng skill này
- Cần train/fine-tune một LLM agent cho tác vụ dài hạn (long-horizon) mà feedback (phản hồi) chỉ đến sau nhiều decisions — MLE, data pipeline, content optimization, nghiên cứu tự động.
- Trajectory-level reward (phần thưởng cấp trajectory) quá thưa hoặc không ổn định; cần học từ intermediate outcomes (kết quả trung gian).
- Tình huống KHÔNG nên dùng: tác vụ có feedback sau mỗi action (dùng RL thông thường); tác vụ không có verifiable execution feedback (không có execution success/score đo được); không đủ infrastructure cho long-running experiments (paper: 12h × 20 vCPUs × 220GB RAM × H200 GPU/task).

## Input cần có
- Task executable với verifiable feedback: execution success/failure, scorable submission, quality thresholds (paper dùng medal thresholds của Kaggle tasks).
- Interaction harness: ReAct-style loop, tools (execute_code, update_answer, analyze sub-agent), experiment tree (solution nodes: code, logs, metadata), context compaction.
- Teacher trajectories cho SFT (2 stage: general coding/tool-use + domain-specific), đã lọc quality.
- Training infra cho async rollout collection + policy updates; log-probabilities của rollout policy.

## Các bước thực hiện
1. **Build task factory:** chuyển tài liệu lịch sử (Kaggle competitions, logs, cases) thành executable tasks — public workspace + hidden test split + unified evaluator; multi-agent pipeline (discovery → analyzer → generator) + validator checks (data integrity, submission format, evaluation behavior) + manual review.
2. **Hierarchical SFT Stage 1:** train trên coding + tool-use trajectories từ diverse agentic tasks → general tool-use + code revision capabilities.
3. **Hierarchical SFT Stage 2:** train trên domain teacher trajectories (task initialization + sustained optimization + analysis sub-agent trajectories). Outcome-guided selection: với trajectory đạt quality threshold, xác định first best-performing submission; nếu post-peak degradation vượt threshold → retain prefix đến anchor; else dùng last submission. Loss chỉ trên newly generated reasoning/text/tool-call tokens; mask tool feedback + inherited history.
4. **WIRL windows:** khi agent chạy, group consecutive model decisions giữa 2 successive experiment results thành execution window u_m; window conditioned on accumulated history.
5. **Window reward:** R_m = −1.0 (execution error do model), −0.6 (không lỗi nhưng không có scorable submission), −0.4 + T_m (dưới threshold), 1.0 + T_m (bronze/silver), 2.0 + T_m (gold); T_m ∈ {−0.2, 0, 0.2} theo trend vs previous valid submission, 0 cho first submission. Dùng R_m làm shared optimization weight cho MỌI output token trong window (KHÔNG group-relative normalization).
6. **Async collection:** asynchronously collect windows có trusted execution feedback thành training batches (không chờ trajectory kết thúc).
7. **Policy correction:** cho token t của model call j, tính q = exp(ℓ_old − ℓ_roll); weight token by q nếu q ∈ [q_min, q_max], loại token ngoài interval khỏi policy-gradient update (c = sg(q · 1[q_min ≤ q ≤ q_max])).
8. **Optimize:** loss = trung bình cửa sổ của (1/N_m) Σ c·L_PG + λ_KL·KL(vs fixed SFT reference) − λ_H·entropy; N_m = số valid output tokens trong window.

## Output mong đợi
- Agent policy học được long-horizon optimization: tự organize experiments, revise từ execution feedback, maintain submission candidates.
- Mỗi training stage thêm gain (paper: 37.9% → 47.0% → 62.1% → 72.7% medal rate); WIRL vượt GRPO (56.1%) và PPO-style (60.6%) khi cả hai đều dưới MLE-SFT baseline (62.1%).
- Capability generalizes: NatureBench Lite Surpass-SOTA 0%→50%, scaffold optimization 23.3%→43.7% held-out, algorithm-component reward 0.322→0.425.

## Ví dụ áp dụng
- Solopreneur fine-tune agent tối ưu email marketing: build task factory từ các campaign lịch sử (A/B test results làm verifiable feedback); SFT trên trajectories của chính mình (Stage 1 tool-use, Stage 2 marketing domain với outcome-guided trimming); WIRL windows group decisions giữa 2 lần gửi campaign; reward −0.4/1.0/2.0 theo conversion threshold + trend ±0.2; async collect khi campaign chạy qua đêm.

## Gotchas
- Cắt trajectory sai: nếu KHÔNG trim degraded tails, model học luôn decisions sau peak (gây退化); phải đo post-peak degradation và anchor tại first best submission.
- Reward hacking: T_m trend bonus có thể khuyến khích micro-improvements vô nghĩa — verify metric direction (tăng/giảm) theo task trước khi set T_m.
- Policy mismatch khi async: KHÔNG bỏ policy correction — tokens ngoài [q_min, q_max] phải bị loại, không thì off-policy data phá update (GRPO/PPO-style trong paper đều dưới baseline).
- Window boundary: window chỉ kết thúc khi experiment trả kết quả — nếu experiments quá dài, windows quá lớn → credit assignment lại thưa; tune tần suất execute_code.
- Medal thresholds task-specific: domain không có threshold → phải tự define quality tiers trước khi chạy.
- Cost: calls tăng 1.00→9.39 cho scaffold optimization — accuracy-cost tradeoff cần đo riêng.
- Contamination: loại training tasks overlapping benchmark trước khi collect trajectories.
