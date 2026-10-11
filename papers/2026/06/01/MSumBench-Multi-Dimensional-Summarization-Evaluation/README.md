# 2506.00549 MSumBench: Towards Multi-dimensional Evaluation of LLM Summarization

## Problem

Existing text summarization benchmarks thiếu domain-specific assessment criteria (tiêu chí đánh giá theo lĩnh vực), predominantly English-centric (chỉ tập trung tiếng Anh), và face challenges với human annotation (gán nhãn thủ công) do complexity of reasoning (độ phức tạp của suy luận). LLM-generated summaries vẫn face hallucinations (ảo giác), omission of critical information (bỏ sót thông tin quan trọng), và redundancy (dư thừa). Không có benchmark nào evaluate summarization across multiple domains + multiple languages + domain-specific criteria simultaneously.

## Contribution

1. MSumBench — multi-dimensional, multi-domain evaluation benchmark cho summarization trong English và Chinese, với specialized assessment criteria (tiêu chí đánh giá chuyên biệt) cho mỗi domain.
2. Multi-agent debate annotation framework — 3 LLM agents (Advocate, Skeptic, Adjudicator) tạo structured arguments với contrasting viewpoints, reducing dependence on single viewpoint. Giúp human annotators focus on key aspects.
3. Discovery: systematic bias trong LLM evaluation — LLMs systematically rate self-generated summaries (tóm tắt do chính chúng tạo) higher than others.

## Method (tóm tắt cốt lõi)

(1) Multi-domain documents: cover multiple domains, mỗi domain có domain-specific key-fact categories (categories thông tin trọng tâm riêng); (2) Bilingual: English và Chinese documents; (3) Multi-agent debate: Advocate argues for summary quality, Skeptic argues against, Adjudicator reviews và finalize — produce structured arguments cho human annotators; (4) Human annotation: annotators score summaries trên 3 dimensions — faithfulness (trung thực), completeness (đầy đủ), conciseness (súc tích) — percentage scores; (5) LLM-as-evaluator: test 8 modern summarization models, analyze LLM evaluation correlation với summarization capabilities.

## Key Findings

- 8 summarization models evaluated, distinct performance patterns across domains and languages
- Multi-agent debate improves annotation quality — structured arguments reduce annotator cognitive load
- Domain-specific key-fact categories are essential — general evaluation criteria miss domain nuances
- Bilingual evaluation reveals language-specific performance patterns
- Systematic bias: LLMs rate self-generated summaries higher — evaluation capability NOT independent of generation capability
- LLM evaluators' correlation with human judgment varies by domain

## Actionable Insights

1. Khi evaluate LLM summarization, KHÔNG dùng single evaluation metric (ROUGE, BERTScore) — cần domain-specific criteria. Ví dụ: medical summarization cần evaluate "did it capture all contraindications?" (có nắm bắt đủ chống chỉ định?), legal summarization cần "did it capture all obligations?" (có nắm bắt đủ nghĩa vụ?).
2. LLM-as-evaluator có systematic self-bias — KHÔNG dùng cùng model để generate và evaluate. Ví dụ: nếu dùng GPT-4 để generate summaries, dùng Claude hoặc human để evaluate, KHÔNG dùng GPT-4 làm evaluator.
3. Multi-agent debate pattern cải thiện annotation quality — áp dụng cho bất kỳ evaluation task cần nuanced judgment. Ví dụ: code review — Agent A argues code is clean, Agent B finds issues, Agent C adjudicates → structured output cho human reviewer.

## Assumptions & Limitations

- Giả sử: multi-agent debate produces higher quality annotations — debate quality depends on underlying LLM capability
- Limitation: Only English và Chinese — chưa cover other languages
- Limitation: Domain coverage limited — may not generalize to all professional domains
- Limitation: Human annotation still needed (debate assists but doesn't replace)
- Limitation (tự thấy): Self-bias discovery chỉ tested trên summarization — có thể extend to other generation tasks? Paper không explore.

## Metadata

- Năm: 2026
- Tác giả: Hyangsuk Min, Yuho Lee, Minjeong Ban, Jiaqi Deng, Nicole Hee-Yeon Kim, Taewon Yun, Hang Su, Jason Cai, Hwanjun Song
- Category: cs.CL, cs.AI
- Link PDF: https://arxiv.org/pdf/2506.00549
- Citation count: N/A
- Nhãn: [applied]
- Skill: multi-agent-debate-annotation
