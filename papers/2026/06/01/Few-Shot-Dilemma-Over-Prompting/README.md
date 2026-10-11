# [2509.13196] Few-shot Dilemma: Over-prompting LLMs

## Vấn đề
Over-prompting — hiện tượng excessive examples (quá nhiều ví dụ) trong prompts dẫn đến diminished performance (giảm hiệu suất) — challenges conventional wisdom (thách thức hiểu biết thông thường) về in-context few-shot learning. Prior empirical conclusion rằng "more relevant few-shot examples universally benefit LLMs" là KHÔNG ĐÚNG cho tất cả models.

## Đóng góp
1. **Few-shot dilemma identified**: Excessive domain-specific examples có thể paradoxically degrade (giáng cấp nghịch lý) performance trong certain LLMs
2. **TF-IDF selection outperforms**: TF-IDF vectors > random sampling > semantic embedding cho software requirement classification
3. **Optimal quantity per LLM**: Mỗi LLM có optimal number of examples. TF-IDF + stratified (phân tầng) → superior performance với fewer examples

## Phương pháp (tóm tắt cốt lõi)
3 few-shot selection methods: random sampling, semantic embedding, TF-IDF vectors. Test trên 7 LLMs (GPT-4o, GPT-3.5-turbo, DeepSeek-V3, Gemma-3, LLaMA-3.1, LLaMA-3.2, Mistral). Gradually increase number of TF-IDF-selected examples → identify optimal quantity per LLM. Dataset: software requirement classification (functional vs non-functional).

## Kết quả chính
- Over-prompting: excessive examples → diminished performance on certain LLMs
- TF-IDF outperforms random sampling và semantic embedding
- LLaMA-3.1-8B surpasses SOTA fine-tuned PRC-BERT by 1% với 10-20 selected examples
- Large models (DeepSeek-V3, GPT-4o): more consistent với lengthy contexts
- 8B parameters may be threshold for effective few-shot comprehension
- Gemma-3-4B: declining performance với more examples

## Insight có thể áp dụng ngay
1. **Less is more cho few-shot**: Không phải more examples = better. Tìm optimal quantity cho your LLM. Ví dụ: khi prompt LLM cho classification task, start với 5-10 examples, test performance, gradually increase until performance drops.

2. **TF-IDF selection > random**: Chọn examples bằng TF-IDF similarity thay vì random. Better relevance, fewer examples needed. Ví dụ: khi build few-shot prompt, use TF-IDF để find most relevant examples từ training set.

3. **Model size matters**: Models <8B parameters có over-prompting problem. Larger models handle more examples. Ví dụ: khi use small model (3-4B), limit examples to 10-20. Large model (70B+) → more examples OK.

## Giả định & Hạn chế
**Điều kiện để findings work:**
- Software requirement classification tasks
- TF-IDF selection applicable
- Model-specific optimal quantity

**Hạn chế paper thừa nhận:**
- Computational overhead of processing numerous examples
- Limited to specific tasks

**Hạn chế paper KHÔNG nói:**
- Task-specific optimal quantity may vary
- Domain dependency
- Prompt format effects
- Temperature/sampling effects

## Metadata
- Năm: 2025
- Tác giả: Yongjian Tang, Doruk Tuncel, Christian Koerner, Thomas Runkler
- Category: cs.CL
- Link PDF: https://arxiv.org/pdf/2509.13196
- Citation count: [EXTRACTION FAILED]
