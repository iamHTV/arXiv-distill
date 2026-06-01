# 2602.06357 LLM-SAA: LLM-persona Generated Distributions for Decision Making

## Problem

Nhiều quyết định business phụ thuộc vào distribution of outcomes (phân phối kết quả): pricing cần willingness-to-pay distribution, inventory cần demand distribution, assortment cần preference distribution. LLMs có thể generate simulated distributions (phân phối mô phỏng) từ product descriptions, nhưng câu hỏi quan trọng: LLM-generated distributions có practically useful (hữu ích thực tế) cho downstream decision-making không? Và metrics nào đúng để evaluate chúng?

## Contribution

1. Define LLM-SAA (LLM Sample Average Approximation) — framework dùng LLM-generated distributions để optimize decisions. LLM simulates consumer preferences/demand từ product descriptions, decision optimized under simulated distribution.
2. Propose decision-aware metrics — evaluate LLM distributions based on QUALITY OF DECISIONS THEY INDUCE, not distribution similarity. Show Wasserstein distance (khoảng cách Wasserstein) can be MISLEADING for decision-making evaluation.
3. Demonstrate LLM-SAA is practically useful, especially trong low-data regimes (chế độ ít dữ liệu).

## Method (tóm tắt cốt lõi)

(1) Prompt LLM với product description, context → generate simulated consumer preferences/willingness-to-pay/demand; (2) Collect LLM-generated samples → construct empirical distribution F̂; (3) Optimize decision under F̂: assortment (chọn sản phẩm nào), pricing (đặt giá), newsvendor (quyết định tồn kho); (4) Evaluate: compare decision quality from LLM-SAA vs. decisions from real data, random, popularity baselines; (5) Test multiple prompting strategies: zero-shot, few-shot, persona-sampling, batch-generation, description-based.

## Key Findings

- LLM-generated distributions are practically useful for decision-making, especially in low-data regimes
- 3 canonical problems tested: assortment optimization, pricing, newsvendor
- Wasserstein distance (distribution similarity metric) can be MISLEADING — good distribution similarity ≠ good decision quality
- Decision-aware metrics (decision quality under the distribution) are more appropriate
- Persona-sampling and few-shot improve distribution quality
- LLM-SAA competitive with real data when data is scarce, degrades when real data abundant

## Actionable Insights

1. Khi thiếu real consumer data, dùng LLM để generate simulated preference distributions cho pricing/assortment decisions. Ví dụ: startup launching new product, không có historical sales data → prompt GPT-4 "simulate 100 consumers' willingness-to-pay for this product description" → optimize price from simulated distribution.
2. KHÔNG evaluate LLM-generated distributions bằng Wasserstein distance hoặc distribution similarity metrics — evaluate bằng DECISION QUALITY. Ví dụ: 2 distributions có Wasserstein distance giống nhau nhưng 1 dẫn đến optimal price tốt hơn nhiều → chỉ decision quality matters.
3. Persona-sampling improves LLM simulation — generate diverse personas (age, gender, location, income) để simulate diverse consumer preferences. Ví dụ: "Simulate willingness-to-pay from a 25-year-old female urban professional" vs "Simulate from a 45-year-old male rural worker" → aggregate cho realistic distribution.

## Assumptions & Limitations

- Giả sử: LLM has sufficient world knowledge about consumer preferences — may not hold for niche/novel products
- Limitation: Tested on 3 canonical problems — real business decisions are more complex
- Limitation: Distribution quality depends on product description quality — garbage in, garbage out
- Limitation: LLMs may have systematic biases in preference simulation (e.g., Western-centric training data)
- Limitation (tự thấy): SUSHI dataset (Japanese respondents) cho thấy cultural specificity matters — LLM trained on English data may not simulate Japanese preferences well

## Metadata

- Năm: 2026
- Tác giả: Jackie Baek, Yunhan Chen, Ziyu Chi, Will Ma
- Category: cs.AI, cs.CL, econ.GN
- Link PDF: https://arxiv.org/pdf/2602.06357
- Citation count: N/A
- Nhãn: [applied]
- Skill: llm-saa-decision-simulation
