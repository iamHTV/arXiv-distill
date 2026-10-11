# [2605.28409] Post-training Hiệu quả LLMs cho Tạo Code bằng Offline Reinforcement Learning

## Vấn đề
Post-training using online RL (học tăng cường trực tuyến) là important training step cho LLMs, including code-generating models. Nhưng online RL cho code generation involves LLM inference và verification — takes considerable time và resources. Prior work chưa explore offline RL cho code generation effectively.

## Đóng góp
1. **Offline RL cho code generation**: Leverages existing code datasets — avoids expensive online RL inference + verification
2. **Effective for small LLMs**: Especially beneficial cho small models và challenging coding problems
3. **Improves pass@1 và pass@10**: Under strict computational constraints với highly imbalanced dataset

## Phương pháp (tóm tắt cốt lõi)
Offline RL: leverage existing code datasets cho training. Apply on-policy online algorithms trong offline setting. Verifiable rewards: functional correctness (code passes tests). Train models without expensive online inference loops.

## Kết quả chính
- Improves both pass@1 và pass@10
- Pronounced gains (cải thiện rõ rệt) trên challenging problems
- Effective under strict computational constraints
- Works với highly imbalanced dataset
- Especially beneficial cho small LLMs

## Insight có thể áp dụng ngay
1. **Offline RL cho code generation**: Khi train code LLMs, use existing code datasets thay vì expensive online RL. Ví dụ: khi fine-tune code model, use offline RL với existing code solutions — cheaper, effective.

2. **Small LLMs benefit more**: Offline RL especially helpful cho smaller models. Ví dụ: khi deploy code assistant on edge devices (small model), use offline RL để improve performance without online costs.

3. **Challenging problems benefit most**: Gains most pronounced on hard problems. Ví dụ: when training code model for complex algorithms, offline RL provides biggest improvement on difficult tasks.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Existing code datasets available
- Verifiable rewards (functional correctness)
- Computational constraints acceptable

**Hạn chế paper thừa nhận:**
- No systematic exploration of learning rates, reward formulations, batch sizes
- Highly imbalanced dataset — simple heuristics only
- Purely offline — no online interaction
- Directly applies on-policy algorithms in offline setting

**Hạn chế paper KHÔNG nói:**
- Code quality beyond correctness (runtime, memory, security)
- Generalization to other domains
- Dataset quality dependency
- Long-term maintenance of offline-trained models

## Metadata
- Năm: 2026
- Tác giả: Mingze Wu, Abhinav Anand, Shweta Verma, Mira Mezini
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.28409
- Citation count: [EXTRACTION FAILED]
