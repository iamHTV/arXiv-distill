# Skill: Recon — Đánh giá Chất lượng Suy luận qua Tái tạo Hành động
Nguồn: 2605.26969v1
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi evaluate (đánh giá) quality (chất lượng) của reasoning traces (dấu vết suy luận) trong user modeling (mô hình hóa người dùng)
- Khi cần distinguish (phân biệt) giữa post-hoc rationalization (hợp lý hóa hậu kỳ) và real reasoning (suy luận thật)
- Khi train (huấn luyện) reasoning synthesis model (mô hình tổng hợp suy luận) cho AI agents

## KHÔNG nên dùng khi
- Không có context-action pairs (cặp ngữ cảnh-hành động) để evaluate
- Task là verifiable domain (miền có thể xác minh) như math, coding — có metrics tốt hơn
- Reconstruction model quá yếu — không predict được actions

## Input cần có
- Corpus context-action pairs từ target user
- Reasoning synthesis model (M_r) — generate candidate reasoning
- Reconstruction model (M_a) — predict action từ context + reasoning
- Evaluation metric: action alignment (so sánh predicted vs ground-truth)

## Các bước thực hiện

### Bước 1 — Sample Candidate Reasoning (lấy mẫu suy luận ứng viên)
1. Với mỗi context-action pair (c, a*) trong test set
2. Sample N=4 candidate reasoning traces từ M_r
3. Conditioning: context + action → reasoning (post-hoc rationalization)
4. Output: N candidate reasoning traces r̂_1, ..., r̂_N

### Bước 2 — Reconstruct Actions (tái tạo hành động)
1. Với mỗi candidate reasoning r̂_i:
   - Input: context c + reasoning r̂_i
   - M_a predicts action: â_i = M_a(c, r̂_i)
2. Measure alignment giữa â_i và ground-truth a*
3. Dimensions: style, intent, values (kiểu dáng, ý định, giá trị)
4. Output: reconstruction score per candidate

### Bước 3 — Select Best Reasoning (chọn suy luận tốt nhất)
1. Recon-Select: chọn candidate có highest reconstruction score
2. Rationale: reasoning có predictive power = reasoning có causal power
3. Output: selected reasoning trace cho mỗi context-action pair

### Bước 4 — Train với Recon Reward (nếu cần)
1. Recon-GRPO: dùng reconstruction score làm reward signal
2. Train reasoning synthesis model M_r với GRPO
3. Reward = alignment giữa predicted action và ground-truth
4. Output: trained reasoning model với better quality reasoning

### Bước 5 — Validate (xác minh)
1. Compare selected reasoning vs baseline (Backward Synthesis)
2. Win rate: bao nhiêu % cases selected reasoning better?
3. Human validation: 100 random pairs, check LM judge agreement
4. Target: >50% win rate = improvement

## Output mong đợi
- Selected reasoning traces với higher predictive power
- Win rate: 54-70% over baseline
- Trained reasoning model (nếu dùng Recon-GRPO)
- Quality metric: reconstruction fidelity

## Ví dụ áp dụng
**Tình huống**: Train AI agent mimic (bắt chước) customer behavior cho market research. Agent cần predict customer decisions từ past interactions.

**Áp dụng**:
1. Corpus: customer context (browsing history, preferences) + action (purchase decision)
2. Generate N=4 reasoning traces: "Customer bought because X", "Customer preferred Y", etc.
3. Reconstruct: given context + reasoning → predict purchase decision
4. Select: reasoning trace nào predict đúng nhất = best reasoning
5. Result: selected reasoning có predictive power, không chỉ rationalization
6. Train: use Recon-GRPO để improve reasoning model → 70% win rate

## Lưu ý quan trọng
1. **Post-hoc rationalization là tempting nhưng sai**: Conditioning trên cả context + action → reasoning guaranteed justify action nhưng không có causal power. LUÔN test bằng reconstruction
2. **N=4 candidates đủ**: 4 candidates per pair là sufficient cho selection. Nhiều hơn = more compute nhưng diminishing returns
3. **Reconstruction model quality matters**: Nếu M_a yếu → reconstruction scores noisy → selection kém. Ensure M_a capable
4. **Transfers across models**: Reasoning tốt từ Recon transfer sang models khác — useful cho multi-model systems
5. **Compute cost**: Recon-Select cần 2N+1 LM calls per pair. Amortize over corpus lifetime
6. **Still conditioned on action**: Recon vẫn dùng ground-truth action để generate reasoning. Future: reasoning from context only
