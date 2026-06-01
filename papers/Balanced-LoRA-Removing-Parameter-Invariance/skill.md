# Skill: BaLoRA — Balanced Low-Rank Adaptation
Nguồn: 2605.31484v1
Loại: workflow

## Khi nào dùng skill này
- Khi fine-tune (tinh chỉnh) LLMs bằng LoRA và muốn faster convergence (hội tụ nhanh hơn)
- Khi cần stable (ổn định) fine-tuning với ít hyperparameter tuning hơn
- Khi dùng high-rank LoRA (r=64, 128) và muốn tối ưu convergence

## KHÔNG nên dùng khi
- Dùng very low rank (r=2, 4) — advantage nhỏ
- Compute budget quá tight — projection step adds small overhead
- Đã dùng other LoRA variants (QLoRA, DoRA) mà work tốt

## Input cần có
- Pre-trained LLM cần fine-tune
- LoRA configuration: rank r, target layers
- Training data
- Optimizer: AdamW recommended
- BaLoRA implementation (projection step)

## Các bước thực hiện

### Bước 1 — Setup Standard LoRA (thiết lập LoRA chuẩn)
1. Chọn target layers (MLP layers recommended)
2. Chọn rank r (64-128 cho best BaLoRA advantage)
3. Initialize A, B matrices standard
4. Setup AdamW optimizer

### Bước 2 — Apply BaLoRA Projection (áp dụng phép chiếu BaLoRA)
1. Sau mỗi optimization step:
   - Compute current (A, B)
   - Project onto balanced manifold
   - Update (A, B) với balanced values
2. Projection preserves adapted matrix W + AB
3. Improves conditioning of loss landscape
4. Negligible compute overhead

### Bước 3 — Train với Balanced Updates (huấn luyện với cập nhật cân bằng)
1. Standard training loop với BaLoRA projection injected
2. Learning rate: constant (không cần schedule phức tạp)
3. Monitor convergence: BaLoRA expected converge faster
4. Compare với standard LoRA same config

### Bước 4 — Evaluate Performance (đánh giá hiệu suất)
1. Compare test loss: BaLoRA vs LoRA same iterations
2. Compare final accuracy: BaLoRA vs LoRA same compute budget
3. Check stability: BaLoRA expected more stable across hyperparameters
4. Advantage: largest at high ranks (r=64, 128)

## Output mong đợi
- Faster convergence than standard LoRA
- More stable training across hyperparameters
- Same hoặc better final performance
- Negligible computational overhead

## Ví dụ áp dụng
**Tình huống**: Fine-tune Llama-3.2-3B cho customer support chatbot. Limited compute budget.

**Áp dụng**:
1. Setup: LoRA r=64, MLP layers, AdamW
2. Standard LoRA: converge sau 1000 iterations
3. BaLoRA: converge sau 700 iterations (30% faster)
4. Same final accuracy, less compute
5. Bonus: less sensitive to learning rate choice

## Lưu ý quan trọng
1. **High ranks benefit most**: r=64, 128 có largest advantage. r=2, 4 advantage nhỏ
2. **Negligible overhead**: Projection step computationally lightweight — don't worry about cost
3. **More stable**: BaLoRA robust hơn với high learning rates và initialization scalings
4. **Starts slower**: BaLoRA có thể start slower than LoRA, nhưng converge faster eventually
5. **Preserves adapted matrix**: Projection không change W + AB — same output, better optimization path
6. **Not tested >3B**: Scalability to larger models unclear — test your use case
