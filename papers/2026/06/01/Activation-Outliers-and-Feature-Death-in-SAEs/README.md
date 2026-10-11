# [2605.31518v1] Activation Outliers và Feature Death trong Sparse Autoencoders

## Vấn đề
Sparse Autoencoders (SAEs — tự mã hóa thưa) decompose (phân rã) neural network activations (kích hoạt) thành interpretable features (đặc trưng có thể giải thích), nhưng nhiều learned features (đặc trưng học được) never activate (không bao giờ kích hoạt) — gọi là feature death (chết đặc trưng). Death rates (tỷ lệ chết) khác biệt lớn giữa models: gần 0 trên GPT-2, hơn 70% trên AlphaFold3 với cùng cấu hình. Prior work chưa giải thích được tại sao và khi nào feature death xảy ra, và mean-centering (trung tâm hóa trung bình) có cần thiết không.

## Đóng góp
1. **Tìm nguyên nhân gốc**: Dimension-level activation outliers (outliers ở cấp chiều — các chiều có mean magnitude lớn so với per-token variation) gây feature death bằng cách shift (dịch chuyển) pre-activations tại initialization (khởi tạo). Features anti-aligned (đối lập phương hướng) với mean nhận pre-activations âm vĩnh viễn và never fire
2. **Metric γ dự đoán death**: Formalize outlier severity (độ nghiêm trọng) là γ = ||μ||/||σ|| — dự đoán initial death rates với Spearman ρ = 0.89 (dead-by-TopK), 0.82 (dead-by-ReLU) across 454 model-layer combinations
3. **Mean-centering eliminates death**: Khởi tạo SAE bias bằng geometric median (trung vị hình học) của activations → eliminate outlier-induced death across tất cả models tested

## Phương pháp (tóm tắt cốt lõi)
Phân tích geometric: pre-activation z_i = w_i · x + b. Nếu activations có mean μ ≠ 0, shift term w_i · μ dịch chuyển pre-activation. Features anti-aligned với μ nhận shift âm lớn → never activate. Formalize severity γ = ||μ||/||σ||. Dead-by-ReLU: feature chết khi shift quá âm, không input nào push pre-activation > 0. Dead-by-TopK: feature chết khi không thể rank trong top-k. Fix: initialize bias = geometric median của activations → shift term triệt tiêu, tất cả features centered around zero. Geometric median robust hơn arithmetic mean vì breakdown point 50% — chịu được outlier tokens.

## Kết quả chính
- γ predicts death rates: Spearman ρ = 0.89 (dead-by-TopK), 0.82 (dead-by-ReLU) across 454 model-layer combinations spanning language, vision, protein, genomic models
- Mean-centering achieves near-zero death trên synthetic data (γ=40): từ 75-90% dead → 0%
- ESM3 layer 24 (γ≈8): baseline 75% dead → mean-centering near zero
- Mean-centered SAEs match 4× larger baseline trên concept recovery và more monosemantic (đơn nghĩa hơn)
- Geometric median vs arithmetic mean: trên 4 models với outlier tokens, AM centering WORSE (91.7% dead trên DINOv3-B), GM centering 0% dead
- Dead features revive during training nhưng prohibitively slow ở high γ: γ≥30 plateau 75-90% dead even after 2M steps

## Insight có thể áp dụng ngay
1. **Luôn mean-center khi train SAE**: Khởi tạo encoder bias bằng geometric median của activations — zero runtime cost, eliminates feature death. Ví dụ: khi train SAE cho production model, compute geometric median trên calibration set 500 tokens, set bias = GM. Đơn giản nhưng eliminates 70%+ dead features.

2. **Dùng γ để diagnose (chẩn đoán) trước khi train**: Compute γ = ||μ||/||σ|| trên activation distribution. Nếu γ > 10 → expect high death rate, mean-centering mandatory (bắt buộc). Nếu γ < 5 → centering optional. Ví dụ: trước khi deploy SAE interpretability pipeline, check γ per layer — layers nào γ cao, prioritize centering.

3. **Geometric median robust hơn arithmetic mean**: Khi có outlier tokens (attention sinks, register tokens), arithmetic mean bị inflate (phóng đại) → centering反而 worse. Dùng geometric median (breakdown point 50%). Ví dụ: vision transformers thường có register tokens với extreme norms — dùng GM, không dùng AM.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Feature death phải do activation outliers gây ra (không phải training instability khác)
- SAE phải có bias terms để learn offset
- Cần calibration set (500 tokens) để compute geometric median

**Hạn chế paper thừa nhận:**
- Analysis focused on initialization-time death; training dynamics phức tạp hơn
- Low-rank activation layers cần thêm PCA whitening, không chỉ mean-centering
- Geometric median computation thêm overhead nhỏ (Weiszfeld's algorithm)

**Hạn chế paper KHÔNG nói:**
- Không test trên very large models (>70B) — unclear nếu γ vẫn predict ở scale lớn
- Không discuss interaction giữa mean-centering và other SAE techniques (residual stream, cross-layer)
- Geometric median có thể converge chậm trên very high-dimensional activations
- Không address feature death do other causes (e.g., dead gradients, learning rate issues)

## Metadata
- Năm: 2026
- Tác giả: Elana Simon, Etowah Adams, James Zou
- Category: cs.LG
- Link PDF: https://arxiv.org/pdf/2605.31518v1
- Citation count: [EXTRACTION FAILED]
