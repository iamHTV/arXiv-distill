# 2605.25354 Context-CoT: Enhancing Context Learning via High-Quality Reasoning Synthesis

## Problem

Prior work về Chain-of-Thought (CoT) distillation (chưng cất suy luận chuỗi) tập trung vào reasoning tasks nhưng bỏ qua context learning (học từ ngữ cảnh) — khả năng extract (trích xuất), internalize (tiêu hóa), và apply (áp dụng) kiến thức mới từ context phức tạp. CL-Bench benchmark cho thấy frontier models như GPT-5.1 chỉ solve được 23.7% context-dependent tasks, open-source models chỉ 13-15%. Lý do: teacher models hay dùng parametric shortcuts (đường tắt tham số) thay vì ground reasoning trong context, và answer-conditioned CoT tạo ra post-hoc rationalization (hợp lý hóa hậu nghiệm) thay vì context-derived reasoning (suy luận rút ra từ ngữ cảnh).

## Contribution

1. Propose Context-CoT — framework 3 giai đoạn tạo high-quality CoT data cho context learning, khác biệt so với prior CoT distillation ở chỗ enforce contextual grounding (suy luận dựa trên ngữ cảnh) thay vì parametric recall (nhớ từ tham số).
2. Introduce rubric-based minimum-leakage filtering — ẩn reference answers và rubrics khi generate CoT, chỉ feedback minimal failed-rubric khi cần, filter out trajectories rò rỉ đáp án.
3. Student-aware CoT selection — chọn CoT paths align với distribution của target model, đảm bảo student học được thay vì chỉ mimic teacher.

## Method (tóm tắt cốt lõi)

Pipeline 3 giai đoạn: (1) Multi-stage CoT sampling — guide model distill long context thành task-relevant intermediate representations (biểu diễn trung gian liên quan đến task) trước khi reasoning, generate nhiều candidate CoT từ multiple teacher models; (2) Rubric-based minimum-leakage filtering — ẩn reference answers, chỉ provide minimal failed-rubric feedback, filter trajectories vi phạm context-specific criteria; (3) Student-aware CoT selection — tính step-wise alignment score (điểm căn chỉnh theo bước) và reasoning gain score, chọn CoT phù hợp với student model distribution. Fine-tune bằng SFT với LoRA adapters trên ~4K training samples.

## Key Findings

- Qwen3.5-4B: CL-Bench overall score từ 9.06% lên 12.85% (+3.79 absolute gain, 95% CI [1.68, 5.03])
- McNemar's exact test: b=83, c=143, p=7.95×10⁻⁵ (statistically significant)
- Answer-only SFT: chỉ marginal gains (không đáng kể)
- Answer-exposed CoT SFT: performance degradation (tệ hơn base model)
- Largest gains ở Domain Knowledge Reasoning category
- Llama3.2-3B cũng improve, chứng minh pipeline không phụ thuộc vào 1 model
- Ablation: bỏ minimum-leakage filtering gây drop lớn nhất
- Training data scaling: performance tăng đến ~3K samples, sau đó diminishing returns
- Optimal student-aware alignment weight λ=0.4

## Actionable Insights

1. Khi tạo synthetic training data cho LLM, KHÔNG expose reference answers cho teacher model khi generate CoT — thay vào đó dùng rubric-based feedback minimal. Ví dụ: khi build internal knowledge base Q&A training data, generate reasoning chains mà không cho model thấy đáp án đúng, chỉ cho biết rubric nào fail.
2. Fine-tune nhỏ (4K samples, LoRA) có thể大幅提升 open-source models trên context-dependent tasks. Ví dụ: enterprise có domain-specific documents (legal, technical manuals) chỉ cần ~4K high-quality context-grounded CoT samples để fine-tune model hiểu document đó tốt hơn.
3. Student-aware selection quan trọng — không phải mọi CoT từ teacher đều phù hợp với student. Ví dụ: khi distill từ GPT-4 xuống smaller model, filter CoT theo perplexity alignment score để chọn trajectories student thật sự học được.

## Assumptions & Limitations

- Giả sử: teacher models đủ mạnh để generate diverse CoT candidates (cần GPT-5.1-class models)
- Giả sử: rubric-based LLM judge đủ准确 để filter leakage
- Limitation (paper thừa nhận): High construction cost — sampling nhiều CoT từ multiple teachers tốn API cost
- Limitation (paper thừa nhận): Offline distillation — không có online feedback từ student model
- Limitation (paper thừa nhận): Dependence on rubric-based judgments — judge errors có thể ảnh hưởng selection
- Limitation (tự thấy): Paper chỉ test trên CL-Bench, chưa validate trên real-world enterprise tasks. CL-Bench tasks là synthetic, chưa chắc transfer sang production scenarios.

## Metadata

- Năm: 2026
- Tác giả: Hongbo Jin, Mingnan Zhu, Jingqi Tian, Xu Jiang, Zhongjing Du, Haoran Tang, Siyi Xie, Qiaoman Zhang, Jiayu Ding
- Institution: Peking University, Xiamen University, Tsinghua University
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.25354
- Citation count: N/A (mới publish 25/05/2026)
- Nhãn: [applied]
- Skill: context-cot-data-synthesis
