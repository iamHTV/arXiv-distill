# Skill: DRIFT — Tối ưu Hóa Đa lượt với Importance-Weighted SFT
Nguồn: 2605.31455v1
Loại: workflow

## Khi nào dùng skill này
- Khi train (huấn luyện) multi-turn AI agents với correction feedback (phản hồi sửa chữa)
- Khi cần RL-level performance nhưng với SFT-level efficiency (hiệu quả)
- Khi repeated online rollouts quá tốn kém

## KHÔNG nên dùng khi
- Open-ended dialogue (hội thoại mở) không có clear correctness signal
- Stochastic hoặc preference-based feedback (phản hồi dựa trên sở thích)
- Long-horizon planning (>10 turns)

## Input cần có
- Base LLM cần fine-tune
- Reference policy (chính sách tham chiếu) — model đã trained
- Correction trajectories (lượt hành trình sửa chữa) từ reference policy
- Verifier function (hàm xác minh) cho correctness signal
- Training dataset

## Các bước thực hiện

### Bước 1 — Generate Offline Trajectories (tạo lượt hành trình offline)
1. Freeze reference policy (cố định chính sách tham chiếu)
2. Sample multi-turn correction trajectories từ reference
3. Mỗi trajectory: try → fail → fix → ... → succeed/fail
4. Record: actions, feedback, returns per trajectory
5. One-time generation — không cần repeated rollouts

### Bước 2 — Compute Importance Weights (tính trọng số quan trọng)
1. Derive return-based importance weights từ KL-regularized objective
2. Higher weight = trajectory có better correction behavior
3. Exponential weighting: successful corrections get higher weight
4. Normalize weights cho stable training

### Bước 3 — Weighted SFT Training (huấn luyện SFT có trọng số)
1. Standard SFT loop nhưng với importance-weighted loss
2. Trajectories với higher weight contribute more to gradient
3. Model learns to mimic successful correction patterns
4. Avoids distribution shift by using offline data

### Bước 4 — Evaluate Multi-Turn Performance (đánh giá hiệu suất đa lượt)
1. Test multi@k metric: cumulative accuracy with k turns
2. Compare: DRIFT vs single-turn SFT vs multi-turn RL
3. Check: correction rate per turn — DRIFT expected higher in early turns
4. Verify: training efficiency comparable to SFT

## Output mong đợi
- Multi-turn performance matching RL baselines
- Training efficiency comparable to SFT
- Higher correction rates in early turns
- Improved performance beyond training domain

## Ví dụ áp dụng
**Tình huống**: Train AI coding assistant với multi-turn corrections. Budget limited — can't afford online RL.

**Áp dụng**:
1. Reference policy: existing code model
2. Generate trajectories: model tries code → fails test → fixes → passes
3. Weight: trajectories with successful fixes get higher weight
4. DRIFT training: weighted SFT on correction trajectories
5. Result: model learns to correct errors efficiently, matches RL performance

## Lưu ý quan trọng
1. **Verifier availability**: DRIFT cần clear correctness signal. Without verifier, importance weights meaningless
2. **Short-horizon only**: Intended cho 2-5 turn corrections. Long conversations need different approach
3. **Offline coverage limitation**: Can only upweight behaviors in collected trajectories. May miss novel strategies
4. **Reference policy quality**: Trajectories quality limited by reference policy. Better reference → better DRIFT
5. **Much faster than RL**: Training efficiency comparable to SFT — main advantage over online RL
6. **Multi-turn > single-turn**: Single-turn only improves turn 1. Multi-turn training essential cho correction behavior
