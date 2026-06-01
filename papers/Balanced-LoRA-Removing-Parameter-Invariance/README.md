# [2605.31484v1] Balanced LoRA: Loại bỏ Bất biến Tham số để Tăng tốc Hội tụ

## Vấn đề
LoRA (Low-Rank Adaptation — Thích ứng Hạng thấp) là phương pháp fine-tuning (tinh chỉnh) phổ biến nhất cho LLMs. Nhưng LoRA inherently overparameterized (quá tham số bên trong): nhiều cặp low-rank factors (nhân tố hạng thấp) có thể yield (tạo ra) cùng adapted weight matrix (ma trận trọng số thích ứng). Các cặp khác nhau exhibit (trình hiện) condition numbers (số điều kiện) khác biệt đáng kể → ảnh hưởng trực tiếp đến convergence rate (tốc độ hội tụ). Prior work chưa address (giải quyết) parameter invariance (bất biến tham số) này.

## Đóng góp
1. **Phân tích lý thuyết**: Chứng minh LoRA overparameterization tạo ra varying condition numbers across minimizers (bộ tối thiểu). Balanced minimizers achieve optimal conditioning (điều kiện tối ưu)
2. **BaLoRA (Balanced Low-Rank Adaptation)**: Project iterates (lặp) onto balanced manifold (đa tạp cân bằng) → cải thiện conditioning của loss landscape while preserving adapted matrix. Projection step computationally lightweight (nhẹ)
3. **Empirical validation**: BaLoRA converge faster than standard LoRA, superior performance across fine-tuning tasks trên Llama-3.2-3B và Qwen-2.5-3B

## Phương pháp (tóm tắt cốt lõi)
LoRA: W_adapted = W + AB, trong đó A ∈ R^{a×r}, B ∈ R^{r×a}. Problem: nhiều (A,B) pairs cho cùng W_adapted nhưng condition numbers khác nhau. BaLoRA: sau mỗi optimization step, project (A,B) onto balanced manifold — enforce (ép buộc) balanced condition. Projection step: computationally lightweight, integrates seamlessly (tích hợp liền mạch) vào existing pipelines. Key: balanced minimizers có optimal conditioning → faster convergence.

## Kết quả chính
- Synthetic experiments: BaLoRA starts slower, sau đó enters fast convergence regime, significantly outperforms LoRA
- Llama-3.2-3B + Qwen-2.5-3B trên 10+ datasets: BaLoRA consistently outperforms standard LoRA
- Advantage lớn nhất ở high ranks (r=64, 128)
- BaLoRA more stable to high learning rates và initialization scalings
- Negligible computational overhead (overhead tính toán không đáng kể)
- Matches hoặc surpasses state-of-the-art variants (DoRA, OLoRA, LoRA-GA)

## Insight có thể áp dụng ngay
1. **Dùng BaLoRA thay vì standard LoRA**: Khi fine-tune LLM, thay vì LoRA standard, dùng BaLoRA — negligible overhead nhưng faster convergence. Ví dụ: khi fine-tune Llama-3B cho specific task, BaLoRA converge nhanh hơn với cùng compute budget.

2. **Higher ranks benefit more**: BaLoRA advantage lớn nhất ở r=64, 128. Nếu dùng high-rank LoRA, BaLoRA đặc biệt useful. Ví dụ: khi cần high-capacity adaptation (thích ứng dung lượng cao), dùng BaLoRA với r=128 thay vì LoRA r=128.

3. **More stable hyperparameter sensitivity**: BaLoRA robust hơn với high learning rates và initialization scalings. Ít cần tune hyperparameters. Ví dụ: khi fine-tune trong production setting với limited tuning budget, BaLoRA reliable hơn.

## Giả định & Hạn chế
**Điều kiện để method work:**
- LoRA overparameterization phải存在 (tồn tại)
- Balanced manifold phải computationally accessible
- Projection step phải preserve adapted matrix

**Hạn chế paper thừa nhận:**
- Synthetic experiments limited scope
- Focus on optimization speed, không phải final accuracy superiority
- Tested trên 3B models — larger models untested

**Hạn chế paper KHÔNG nói:**
- Không compare với full fine-tuning
- Không test trên models >3B — scalability unclear
- Không address interaction với other LoRA variants (QLoRA, etc.)
- Projection step có numerical stability issues trên very high ranks?
- Không discuss when NOT to use BaLoRA

## Metadata
- Năm: 2026
- Tác giả: Valérie Castin, Kimia Nadjahi, Pierre Ablin, Gabriel Peyré
- Category: cs.LG
- Link PDF: https://arxiv.org/pdf/2605.31484v1
- Citation count: [EXTRACTION FAILED]
