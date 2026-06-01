# Skill: SAE Mean-Centering Fix cho Feature Death
Nguồn: 2605.31518v1
Loại: workflow

## Khi nào dùng skill này
- Khi train (huấn luyện) Sparse Autoencoder (SAE — tự mã hóa thưa) và gặp feature death (đặc trưng chết)
- Khi muốn improve (cải thiện) SAE interpretability (khả năng giải thích) mà không tăng model size (kích thước)
- Khi deploy (triển khai) SAE trên production model và cần maximize (tối đa hóa) feature utilization (sử dụng đặc trưng)

## KHÔNG nên dùng khi
- Model activations đã được pre-processed (xử lý trước) với normalization (chuẩn hóa)
- SAE không có bias terms
- Activation distribution đã zero-mean (trung bình bằng không) tự nhiên

## Input cần có
- Pre-trained model cần interpret (giải thích)
- SAE architecture (kiến trúc) với bias terms
- Calibration set: 500 tokens từ model activations
- Compute: đủ để run SAE training

## Các bước thực hiện

### Bước 1 — Compute γ (tính γ)
1. Forward pass (đi xuôi) 500 calibration tokens qua model
2. Extract activations tại layer muốn train SAE
3. Compute mean μ = E[activations] và std σ = std(activations)
4. Tính γ = ||μ|| / ||σ||
5. Nếu γ > 10 → BẮT BUỘC mean-centering. Nếu γ < 5 → optional

### Bước 2 — Compute Geometric Median (tính trung vị hình học)
1. Dùng Weiszfeld's algorithm trên 500 calibration tokens
2. Iterative: start với arithmetic mean, lặp: μ_GM = Σ(x_i / ||x_i - μ||) / Σ(1 / ||x_i - μ||)
3. Converge khi ||μ_new - μ_old|| < ε
4. Output: geometric median μ_GM
5. KHÔNG dùng arithmetic mean nếu có outlier tokens (attention sinks, register tokens)

### Bước 3 — Initialize SAE Bias (khởi tạo bias SAE)
1. Set encoder bias b_enc = μ_GM
2. Mathematically equivalent to runtime centering nhưng zero overhead
3. Pre-activation: z_i = w_i · (x - μ_GM) + b_enc → shift term triệt tiêu
4. Tất cả features centered around zero, chỉ vary theo input content

### Bước 4 — Verify (xác minh)
1. Train SAE với centered initialization
2. Check death rate: nên < 5% (so với baseline 70%+ nếu γ cao)
3. Compare feature quality: monosemanticity (đơn nghĩa), concept recovery
4. Nếu death rate vẫn cao → check nếu activations low-rank → cần PCA whitening thêm

### Bước 5 — PCA Whitening cho Low-Rank Layers (nếu cần)
1. Compute effective rank (hạng hiệu dụng) của activation covariance
2. Nếu effective rank < 2% hidden dimension → mean-centering alone không đủ
3. Apply PCA whitening trước khi train SAE
4. Alternative: Active Subspace Initialization (khởi tạo không gian con hoạt động)

## Output mong đợi
- Death rate giảm từ 70%+ → < 5%
- Feature quality cải thiện: mean-centered SAE match 4× larger baseline
- More monosemantic features (đặc trưng đơn nghĩa hơn)
- Better concept recovery (phục hồi khái niệm)

## Ví dụ áp dụng
**Tình huống**: Train SAE trên production LLM để interpret internal representations (biểu diễn nội bộ). Layer 24 có γ ≈ 8, baseline 75% dead features.

**Áp dụng**:
1. Compute γ = 8 → mandatory centering
2. Extract 500 calibration tokens, compute geometric median μ_GM
3. Initialize SAE bias = μ_GM
4. Train SAE → death rate ~0% (vs 75% baseline)
5. Interpret features: recover biological concepts (ESM3 example) hoặc language patterns (LLM example)
6. Deploy: same SAE size nhưng 4× effective capacity (dung lượng hiệu dụng)

## Lưu ý quan trọng
1. **Arithmetic mean có thể WORSE**: Trên models với outlier tokens (DINOv3, ModernBERT), AM centering → 91.7% dead. LUÔN dùng geometric median
2. **γ threshold**: γ > 10 = mandatory, γ < 5 = optional, giữa 5-10 = recommended
3. **Low-rank activations**: Nếu effective rank < 2% hidden dim, mean-centering alone insufficient → thêm PCA whitening
4. **Runtime overhead**: Bias initialization = zero runtime cost. Geometric median computation chỉ cần 1 lần trên calibration set
5. **Cross-layer methods**: Mean-centering stabilizes effective capacity → helps transcoders và cross-layer feature dictionaries
6. **Training revival**: Dead features có thể revive during training nhưng prohibitively slow ở high γ → better to fix at init
