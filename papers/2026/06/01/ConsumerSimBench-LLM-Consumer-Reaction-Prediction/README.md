# 2605.17079 Can LLMs Think Like Consumers? ConsumerSimBench

## Problem

LLMs ngày càng được dùng như "digital consumers" (người tiêu dùng kỹ thuật số) để simulate public opinion (mô phỏng dư luận), pre-test marketing decisions (kiểm thử trước quyết định marketing), và anticipate audience response (dự đoán phản ứng khán giả). Nhưng existing evaluations hiếm khi hỏi: liệu model có reconstruct được concrete reaction patterns (mẫu phản ứng cụ thể) mà real consumers surface trong public discourse (thảo luận công cộng)? Technical benchmarks đánh giá reasoning/math/code, nhưng không đánh giá socially grounded consumer intuition (trực giác người tiêu dùng dựa trên bối cảnh xã hội).

## Contribution

1. ConsumerSimBench — benchmark từ 1,553 real Chinese social-media topics và 23,122 atomic, rule-audited criteria spanning 4 reaction families (sentiment flashpoints, emotion keywords, positive aspects, negative aspects). Decompose thành auditable yes-no decisions thay vì holistic preference judgment.
2. Evaluation innovation: three-judge agreement tăng từ 65.8% lên 92.1% khi decompose thành atomic criteria. 98.4% agreement giữa pointwise judge decisions và human-majority labels.
3. Discovery: sharp gap giữa technical-benchmark performance và consumer intuition — models strong trên math/reasoning nhưng fail trên consumer prediction.

## Method (tóm tắt cốt lõi)

(1) Collect 1,553 hot topics từ Chinese social media (March-September 2025); (2) Human annotators decompose mỗi topic thành atomic reaction criteria — concrete things real consumers said (14.9 criteria/topic avg); (3) 4 reaction families: sentiment flashpoints (3,779), emotion keywords (8,749), positive aspects (5,666), negative aspects (4,928); (4) 13 frontier models evaluated: Gemini-3.1-Pro, GPT-5.2, Claude-Opus-4.6, Qwen3.5-397B, Grok-4.2, DeepSeek-V3, etc.; (5) Evaluation: model predicts consumer reactions → compare against real reactions using rule-audited binary criteria; (6) GPT-5.2 as fixed judge with cross-judge validation.

## Key Findings

- Best model (Gemini-3.1-Pro): covers only 47.8% of real reaction criteria
- GPT-5.2 và Claude-4.6 trail far behind despite strength on technical benchmarks
- Sharp gap between technical-benchmark performance và consumer intuition
- Structured reasoning prompt DECREASES coverage (hurts rather than helps)
- Generate-reflect multi-agent pipeline improves: MiMo-V2.5-Pro from 32.9% → 37.6%
- 13 frontier models evaluated total
- 4 topic categories: Society/public-issue (37%), Entertainment (33%), Sports/gaming (17%), Lifestyle goods (12%)
- Three-judge agreement: 65.8% → 92.1% with atomic decomposition

## Actionable Insights

1. KHÔNG dùng LLM làm sole digital consumer simulator cho marketing decisions — best model chỉ cover 47.8% real reactions. Ví dụ: company test marketing message bằng LLM simulation → LLM miss 52% reactions real consumers sẽ có → false confidence.
2. Structured reasoning prompts có thể HURT consumer prediction — LLM over-reason thay vì rely on intuition. Ví dụ: "Analyze consumer sentiment step by step" → worse than simple "What will consumers say about X?"
3. Multi-agent generate-reflect pipeline improves prediction — 1 agent generates predictions, 1 agent reflects and critiques, iterate. Ví dụ: marketing team deploy 2-agent pipeline — Agent A predicts reactions, Agent B checks against past campaigns, improves from 32.9% to 37.6%.

## Assumptions & Limitations

- Giả sử: Chinese social media reactions represent general consumer behavior — may not transfer to other markets/cultures
- Limitation: Chinese-language only — English/multilingual not tested
- Limitation: Social media reactions ≠ purchase decisions — consumers say different things than they do
- Limitation: Topics from 2025 — model knowledge cutoff may affect older topics
- Limitation (tự thấy): "Coverage" metric doesn't measure accuracy of predictions — model could predict reactions consumers DIDN'T have (false positives). Paper focuses on recall, not precision.

## Metadata

- Năm: 2026
- Tác giả: Tianyu Wang, Jiajun Li, Jianghao Lin
- Category: cs.AI, cs.CL
- Link PDF: https://arxiv.org/pdf/2605.17079
- Citation count: N/A
- Nhãn: [applied]
- Skill: N/A — benchmark, cautionary finding about LLM consumer simulation limits
