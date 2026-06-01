# 2605.10235 Pre-Route: Activating Latent Routing Abilities of LLMs for RAG vs. Long-Context

## Problem

LLM có context window 128K+ tokens, nhưng choosing giữa RAG (Retrieval-Augmented Generation — tạo sinh được tăng cường truy xuất) và LC (Long Context — ngữ cảnh dài) là quyết định quan trọng. RAG efficient nhưng constrained bởi retrieval quality (chất lượng truy xuất); LC cho phép global reasoning (suy luận toàn cục) nhưng expensive và suffer position sensitivity (nhạy cảm vị trí — lost-in-the-middle). Existing method Self-Route dùng failure-driven fallback (phản ứng khi thất bại): thử RAG trước, nếu model output "unanswerable" thì fallback sang LC. Vấn đề: passive (bị động), redundant overhead (phí tổn dư thừa), depend on model self-assessment (tự đánh giá có thể sai), low interpretability (khó giải thích).

## Contribution

1. Propose Pre-Route — proactive routing framework (khung định tuyến chủ động): structured reasoning TRƯỚC KHI answer để quyết định RAG hay LC. Dùng lightweight metadata (document type, length, initial snippet) để task analysis, coverage estimation, information-need prediction.
2. Discover LLMs có latent routing ability (khả năng định tuyến tiềm ẩn) — có thể elicited (kích hoạt) bằng structured prompts, single-sample performance gần bằng Best-of-N.
3. Linear probes reveal structured prompts sharpen separability (khả năng phân tách) của "optimal routing dimension" trong representation space (không gian biểu diễn).
4. Distillation transfers routing reasoning structure sang smaller models cho lightweight deployment.

## Method (tóm tắt cốt lõi)

Pre-Route gồm 3 stages: (1) Metadata Collection — gather lightweight metadata: document type, length, head snippet (đoạn mở đầu); (2) Structured Routing Reasoning — LLM phân tích task requirements, ước lượng coverage (phạm vi bao phủ) của RAG snippets, predict information-need pattern, output routing decision (RAG/LC) với explanation; (3) Execute chosen strategy — nếu RAG: retrieve + generate; nếu LC: full context → model. 2 modes: Prompt-only (structured prompt guide LLM routing) và Distillation (transfer routing ability từ large teacher sang 1.7B student model). Metadata variants: Full-Meta (type+length+snippet), Head-only (length+head snippet), Generated-Meta (LLM infer metadata).

## Key Findings

- Pre-Route outperforms Self-Route trên LaRA (in-domain) và LongBench-v2 (out-of-domain) — higher QA score, higher route accuracy, lower LC reliance
- All improvements statistically significant: paired t-test p < 0.01, Cohen's d: 0.19-0.26
- Prompt-only routing with Qwen3-235B và DeepSeek-R1: structured reasoning prompts reliably elicit latent routing, higher accuracy than Self-Route
- Small models (1.7B) can't directly inherit complex routing — 74.3% of errors tilt toward "safer" LC option
- Distillation: large teacher → 1.7B student successfully acquires structured routing logic
- Head-only metadata (just length + head snippet) closes gap to Full-Meta — routing works with minimal metadata
- Pre-Route achieves superior cost-effectiveness: better accuracy per unit cost

## Actionable Insights

1. Khi build RAG system, thay vì always-RAG hoặc failure-driven fallback, dùng structured reasoning prompt để LLM tự quyết định query nào cần RAG, query nào cần long-context. Ví dụ: "Analyze: is this question answerable from retrieved snippets or does it need full document context? Consider: information distribution, comparison needs, reasoning depth." Single prompt → better routing than complex fallback logic.
2. Distill routing ability từ large model xuống small model — deploy 1.7B model với routing capability của 235B model. Ví dụ: edge deployment dùng Qwen3-1.7B đã distilled routing từ GPT-5, giảm cost mà giữ routing quality.
3. Metadata tối thiểu (length + head snippet) đủ để route accurately — không cần expensive metadata extraction. Ví dụ: khi user upload document, chỉ cần check file size và đọc 200 tokens đầu để quyết định RAG vs LC.

## Assumptions & Limitations

- Giả sử: LLM có latent routing ability learned during pretraining — có thể không true cho tất cả models
- Limitation: Binary routing (RAG vs LC) — không capture hybrid approaches (adaptive retrieval granularity)
- Limitation: Depend on metadata quality — performance degrade khi metadata absent hoặc unreliable
- Limitation: English-only evaluation — chưa test multilingual
- Limitation: Distillation cần strong teacher model — accessibility constraint
- Limitation (tự thấy): Routing accuracy ≠ answer accuracy — routing đúng nhưng model vẫn có thể answer sai. Paper focus vào routing decision, không address answer quality separately.

## Metadata

- Năm: 2026
- Tác giả: Yiwen Chen, Kuan Li, Fuzhen Zhuang, Deqing Wang, Zhao Zhang, Liwen Zhang, Yong Jiang, Shuai Wang, Minhao Cheng
- Category: cs.CL, cs.AI
- Link PDF: https://arxiv.org/pdf/2605.10235
- Citation count: N/A
- Nhãn: [applied]
- Skill: pre-route-rag-lc-routing
