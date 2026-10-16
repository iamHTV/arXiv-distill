# 2608.28649 — Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution? (CIKM '26)

## Problem
- Conversion attribution (cấp credit cho conversion qua các touchpoint quá khứ) có 2 khía cạnh: (1) weight allocation (giới hạn touchpoint cùng item/shop), (2) touchpoint selection (identify meaningful touchpoints từ full user behavior sequence — Zeng et al. Meta). Prior selection methods dựa vào collaborative-filtering heuristics (taxonomy matching + CF similarity) → không align với user-perceived semantic intent, bỏ sót implicitly-related touchpoints (functional complementarity: camera + memory card; scenario/audience alignment: shared anime IPs).

## Contribution
- SILVA: benchmark đầu tiên cho touchpoint Selection In fuLl-path conVersion Attribution — 1,000 conversion events + touchpoint trong 3-day lookback window (69,680 touchpoints), multimodal (image, title, shop, category metadata), từ platform hàng trăm triệu DAU.
- Human annotation: 6 annotators, mỗi touchpoint 3 nhãn độc lập, Fleiss' κ > 0.70 (substantial agreement), majority voting; annotators KHÔNG thấy heuristic baseline outputs. Phân bố: explicit 19.09%, implicit 14.91% — implicit signals non-negligible, prior approaches blind với không gian này.
- Systematic evaluation 8 LLMs (GPT-5.5, Gemini-3.1-Pro, Claude-Opus-4.7, GLM-5.1, DeepSeek-V4-Pro/Flash, Qwen3.5-27B, Qwen3.5-30B-A3B) với pairwise vs listwise prompting.
- LOTUS (LLM-Oriented Touchpoint Understanding and Selection): internal foundation model + pairwise reasoning at scale → labels làm positive samples cho auxiliary indirect conversion prediction task trong production CVR model.

## Method
- Label space 3 lớp: Irrelevant / Explicit (taxonomy matching: identical item/shop/brand/leaf category; CF-based similar leaf categories) / Implicit (functional complementarity; scenario/audience alignment).
- Pairwise protocol: model nhận user profile + 1 candidate touchpoint + conversion → judge 3-way. Listwise: profile + full behavior log + conversion → relevant touchpoints + relation types. Cùng criteria trong prompt cả 2 protocols.
- Metrics: per-conversion precision/recall/F1 per class, macro-average; Overall F1 = (F1_Exp + F1_Imp)/2. Random-guessing F1 ≈ 0.1491 (implicit prevalence).

## Key Findings
- Finding 1 — implicit khó hơn nhiều: pairwise explicit F1 0.8979 vs implicit 0.4929; listwise 0.8372 vs 0.4608. Best implicit F1 0.5426 (Gemini-3.1-Pro pairwise) vs best explicit 0.9095 (Claude-Opus-4.7 pairwise).
- Finding 2 — pairwise beats listwise trên MỌI model: avg overall F1 0.6490 → 0.6954. Pairwise decompose noisy sequence-level selection thành candidate-level judgments; listwise over-filter → recall thấp.
- Finding 3 — strong open-weight competitive: GLM-5.1 0.7086, DeepSeek-V4-Pro 0.7056 (pairwise overall) gần GPT-5.5 0.7197; smaller Qwen lag (0.6636/0.6703), đặc biệt implicit.
- Finding 4 — model capability narrows pairwise-listwise gap: 1.3pp Gemini-3.1-Pro, 3.0pp GPT-5.5, nhưng 6.2pp Qwen3.5-27B, 11.9pp Qwen3.5-30B-A3B. Pairwise gain lớn hơn khi listwise F1 thấp.
- Thinking mode ablation: marginal — listwise +0.0196 avg overall gain, pairwise +0.0082; strongest gains từ smaller Qwen variants. Reasoning patterns chưa optimized cho touchpoint selection.
- LOTUS trên production-scale CVR model: GAUC +0.35pp absolute over Base (in-shop heuristic [4]), +0.15pp over CABB (heuristic cross-shop explicit-only [23]). 0.1pp absolute GAUC empirically sufficient để drive substantial growth in online sales/ad revenue.

## Actionable Insights
- Dùng pairwise prompting (1 candidate + conversion + profile) cho semantic relevance judgment, không listwise — recall cao hơn trên mọi model scale; gap chỉ 1.3–3.0pp với flagship models.
- Touchpoint selection nên dùng semantic criteria (functional complementarity, scenario/audience alignment) bên cạnh taxonomy/CF rules — implicit touchpoints = 14.91% hành trình, bỏ qua mất ~15% conversion signal.
- LLM-attributed labels làm auxiliary positive samples cho CVR training: +0.35pp GAUC offline chỉ bằng pairwise reasoning với internal model — không cần fine-tune, chỉ cần labels.

## Assumptions & Limitations
- Benchmark từ 1 platform (Alibaba e-commerce, hàng trăm triệu DAU) — generalization sang domain khác chưa test.
- Implicit F1 vẫn xa explicit (best 0.5426 vs 0.9095) — semantic relations (functional complementarity, scenario consistency) vẫn khó even for strong LLMs.
- Thinking mode marginal (+0.008–0.020) — current reasoning patterns chưa tối ưu; cần specialized fine-tuning cho semantic judgment nuances.
- Chỉ offline GAUC — chưa có online A/B test (paper không report); 0.1pp GAUC threshold dựa trên prior empirical findings [3,4,24].
- Smaller models (<100B) largely lag — touchpoint selection cần flagship-scale reasoning; không chạy được edge/small deployments.

## Metadata
- 2026 (2026-08-18), Jinqi Wu (NJU), Sishuo Chen (PKU), Zhangming Chan, Yong Bai, Chao Yi, Han Zhu, Shuodian Yu, Lei Zhang, Sheng Chen, Chenghuan Hou, Jian Xu (Taobao & Tmall Group, Alibaba), Chaoyou Fu (NJU); CIKM '26 Rome, Nov 07–11 2026, cs.CL, https://arxiv.org/pdf/2608.28649
