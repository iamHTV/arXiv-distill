# [2605.23071] Efficiency Frontier: Khung Thống nhất cho Tối ưu Chi phí-Hiệu suất trong Quản lý Ngữ cảnh LLM

## Vấn đề
LLMs increasingly rely trên long-context processing, nhưng expanding context windows introduces substantial computational và financial costs. Existing context reduction approaches (retrieval, memory compression) typically evaluated using performance và efficiency metrics independently — limiting systematic comparison và deployment-aware decision-making.

## Đóng góp
1. **Efficiency Frontier framework**: Unified framework cho cost-performance optimization trong LLM context management. Models context strategy selection as deployment-aware optimization problem
2. **Amortized cost modeling**: Jointly accounts cho task performance, token cost, preprocessing reuse. Distinguishes intrinsic cost từ amortized cost under context reuse
3. **Decision-oriented analysis**: Reveals operational regimes và transition boundaries giữa retrieval-based và preprocessing-based strategies

## Phương pháp (tóm tắt cốt lõi)
Framework: (1) Cost Model: EffectiveTokens = T_stage2 + T_stage1/N (amortized preprocessing cost); (2) Efficiency Score: w·F1 - (1-w)·log(EffectiveTokens) — parameterized utility trade-off performance vs cost; (3) Optimization: 3 stages — intra-strategy, cross-strategy, frontier construction. Deployment-aware: select strategy based on operational conditions.

## Kết quả chính
- 5,000 HotpotQA instances evaluation
- Deployment-aware optimization: ~25% token reduction at comparable performance (F1 ≈ 0.78)
- Amortized memory compression: >50% lower token cost vs full-context prompting
- Distinct operational regimes giữa strategies
- Transition boundaries identified

## Insight có thể áp dụng ngay
1. **Deployment-aware optimization**: Khi choose context strategy, jointly optimize performance + cost + reuse. Don't evaluate in isolation. Ví dụ: khi build RAG system, compare retrieval vs memory compression dựa trên effective token cost, không chỉ accuracy.

2. **Amortized cost matters**: Preprocessing cost amortized across queries. High reuse = lower effective cost. Ví dụ: khi deploy LLM chatbot, preprocess context once, reuse across many queries — amortized cost giảm dramatic.

3. **Efficiency Frontier cho strategy selection**: Plot performance vs cost, find frontier. Choose strategy trên frontier. Ví dụ: khi decide giữa retrieval và preprocessing, plot F1 vs token cost — whichever on frontier is optimal cho your deployment preference.

## Giả định & Hạn chế
**Điều kiện để framework work:**
- HotpotQA evaluation — may generalize
- Token cost measurable
- Preprocessing reuse possible

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn paper KHÔNG nói:**
- Latency not modeled — only token cost
- Quality of preprocessing not fully explored
- Real-world deployment costs may differ
- Framework assumes static preferences

## Metadata
- Năm: 2026
- Tác giả: Binqi Shen, Lier Jin, Hanyu Cai, Lan Hu, Yuting Xin
- Category: cs.CL
- Link PDF: https://arxiv.org/pdf/2605.23071
- Citation count: [EXTRACTION FAILED]
