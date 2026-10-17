# arXiv Distill Daily Report — 2026-10-17

Summary of 10 papers distilled today (top 10 selected from arXiv scan).
Each paper went through 6 distill steps, bilingual (VI/EN), skill test (if eligible), commit+push to GitHub.

## Overview
- Total papers distilled: **10**
- Label [applied]: **10**
- Skills created: **10**

## Today's 10 papers

### 1. (When) Should a Software Factory be Lights-off? Benchmarking Code Review Agents on Bug Detection
- arXiv ID: `2610.13668v1`
- Classification: `[applied]`
- Skill: crbugbench-review-agent-evaluation (created)
- PDF: https://arxiv.org/pdf/2610.13668

### 2. AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework
- arXiv ID: `2609.30541v1`
- Classification: `[applied]`
- Skill: autoresearch-production-scaffolding (created)
- PDF: https://arxiv.org/pdf/2609.30541

### 3. Do Tool Calls Execute as Intended? Measuring and Repairing Intent-Execution Correspondence in LLM Agents
- arXiv ID: `2610.04375v1`
- Classification: `[applied]`
- Skill: IEC Hop-Witness Audit (created)
- PDF: https://arxiv.org/pdf/2610.04375

### 4. FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents
- arXiv ID: `2609.26048v1`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

### 5. Incremental Pooled LLM Evaluation for Cost-Effective Retrieval Model Selection
- arXiv ID: `2609.02745v1`
- Classification: `[applied]`
- Skill: Incremental Pooled LLM Evaluation (created)
- PDF: https://arxiv.org/pdf/2609.02745

### 6. LLM-based User-Product Relevance Evaluation for Dynamic Product Advertising
- arXiv ID: `2610.14550v1`
- Classification: `[applied]`
- Skill: query-free-relevance-judge-pipeline (created)
- PDF: https://arxiv.org/pdf/2610.14550

### 7. Learning How Much to Collaborate: Difficulty-Aware Topology Selection for Multi-Agent Code Generation (Dats)
- arXiv ID: `2609.13890v1`
- Classification: `[applied]`
- Skill: Dats Topology Router (created)
- PDF: https://arxiv.org/pdf/2609.13890

### 8. Structured pre-generation elicitation versus single-shot prompting in AI-assisted enterprise decision-making: a randomised online experiment
- arXiv ID: `2610.09593v1`
- Classification: `[applied]`
- Skill: pre-generation-elicitation-scaffold (created)
- PDF: https://arxiv.org/pdf/2610.09593

### 9. What Drives Recovery in Agentic Text-to-Cypher? LAST-CQ: An LLM Agent Self-Refinement Framework
- arXiv ID: `2609.12746v1`
- Classification: `[applied]`
- Skill: Execution-Grounded Query Refinement (created)
- PDF: https://arxiv.org/pdf/2609.12746

### 10. When the Model Retires: An Empirical Study of LLM Migration in Open-Source Applications
- arXiv ID: `2609.31288v1`
- Classification: `[applied]`
- Skill: LLM Retirement Readiness Audit (created)
- PDF: https://arxiv.org/pdf/2609.31288

## WHAT YOU CAN APPLY

Below are insights from today's 10 papers that you — a solopreneur doing content/AI in Vietnam — can **apply right away** without reproducing the paper:

- Scale review effort theo PR complexity: PR nhỏ homogeneous → config rẻ; PR lớn heterogeneous → model mạnh + reasoning cao + human review; tách unrelated change thành PR nhỏ.
- Steer agent bằng custom instruction theo priority (usability, portability, backward compatibility, maintainability) — default agent focus vào severe functional bug.
- Feed repository knowledge cho agent khi review proprietary/large repo — bug cần project context là nơi agent yếu nhất (-25.5%).
- Gate trước khi chạy tác vụ tốn kém: một bước review ngữ nghĩa pre-execution bắt 1 lỗi DDP = tiết kiệm cả chục giờ GPU — với workflow automation, luôn validate plan trước khi execute tốn cost.
- Chỉ can thiệp khi tắc: critic bắn mỗi iteration sinh noise; bắn trên plateau (8%/5 iteration) mới tạo paradigm shift — áp dụng cho content pipeline: trigger review chiến lược chỉ khi KPI đi ngang 5 chu kỳ.
- Bộ nhớ thất bại phải bền: ghi negative result vào storage cross-job ngày đầu — agent vẫn re-test 100-epoch 6 lần dù program.md đã cấm.
- Audit harness hop-by-hop, không chỉ end-to-end: mỗi harness đổi call tại hop riêng (Claude Code ở host wrapper, PowerShell paths ở process interface, typing harnesses ở shell parse). Ví dụ: chạy 20 payloads (quotes, backslashes, line breaks, special chars) qua argv sentry với mỗi harness trước khi tin benchmark score.
- Benchmark phải report launch và giữ fixed: cùng LLM, score chênh 29 chains chỉ vì transport (Qwen2.5-72B: 29 ahead với direct JSON, 2 behind trên PS 5.1). Ví dụ: đánh giá coding agent luôn chạy cả control transport (Git Bash from file) và direct JSON để tách LLM quality khỏi launch loss.
- Khi agent retry call đúng mà vẫn fail → nghi path, không phải LLM: 80.7% merged-backslash changes silent (không error), agent nhận "success" cho wrong action. Ví dụ: log received text tại wrapper (BASH_ENV witness) cho mọi Bash call có backslash pair/heredoc/≥1,000 chars — nếu received ≠ sent, quy cho path trước khi blame model.
- tool-call, inject hướng dẫn khi phát hiện trạng thái rủi ro (server chưa tách khỏi phiên, database mở trước khi sao chép). 2. Nội dung chính sách quan trọng hơn thời điểm — hướng dẫn chung chung như "xem lại công việc" không giúp. Áp dụng: viết chính sách cụ thể cho từng thất bại thủ tục (duy trì dịch vụ, bảo tồn bằng chứng database) thay vì dùng prompt chung chung.
- Bắt đầu benchmark với 3–5 systems, grow incrementally: mỗi model mới chỉ judge uniquely retrieved documents (65–80% reuse). Ví dụ: RAG system đánh giá embedding model mới — retrieve top-100, judge chỉ docs chưa có trong pool, so sánh ngay với all previous systems on equal footing.
- Pooled LLM judging tránh classical pool bias: judge mọi newly contributed document → removed all 19 ranking errors classical pooling introduced. Ví dụ: KHÔNG dùng TREC pooling unjudged-as-nonrelevant khi so sánh hybrid vs dense (novel behavior bị penalise 0.033–0.055 nDCG@10).
- Bootstrap qrels trước khi tin pairwise disagreement: 74% disagreements nằm trong gold's own sampling noise; chỉ 7/220 pairs genuine. Ví dụ: dashboard so sánh 2 retrieval models — compute bootstrap swap probability (10,000 resamples); nếu >5% thì pair "effectively tied", đừng quyết định model dựa trên cặp đó.
- Nén history trước khi dùng LLM judge: grouping semantic + weighting theo event strength giảm 30× cost mà vẫn giữ fidelity 0.99 — áp dụng cho mọi pipeline đánh giá content: đừng judge từng event, judge intent representative.
- Guideline quan trọng hơn model: guideline mang phần lớn lift (Pro không guideline thua cả student có guideline) — đầu tư viết taxonomy + rule trước khi đổi model.
- Fine-tune chứ đừng chỉ prompt: prompt-only giữ long-tail p95 như teacher; fine-tune nén p95 theo bậc — khi latency quan trọng, distillation là bắt buộc.
- Route topology per problem, not per system: trên 614 problems, fixed HRM tốn 10× budget để mua 2.4 điểm ở easy third nhưng mua 21.1 điểm ở hard third — router calibrated at 40% HRM cost beats always-HRM 4.07 points. Ví dụ: coding agent với 5 pipeline templates (single/chain/star/mesh/HRM): extract 39 features (difficulty rating + algorithmic category là 2 groups mang nhiều signal nhất, −4.24/−3.10 khi bỏ), train GNN predictor trên cached outcomes, bisection λ to budget → chọn topology trước khi call model nào.
- So sánh cost-aware routers phải báo realised spend bên cạnh accuracy và equalise spend: shared λ=0.2 để 6 methods spend 30.3%–51.9% budget (spread 21.6pp) và reverse rankings (RandomForest first ở shared λ, Dats first khi calibrated, gap 3.42 points). Ví dụ: dashboard đánh giá agent luôn in USD/problem + % of reference budget; calibrate mỗi method bằng bisection trước khi so sánh.
- Hard problems theo category khác nhau: graph problems 49% → HRM, implementation/string 65–73% → Single, greedy → Star (decomposes thành rule + exchange proof). Ví dụ: routing rule of thumb — trước khi chạy multi-agent, classify dominant technique; chỉ graph/DP/hard mới đáng trả 5–10× tokens.
- Elicit trước khi generate: 3 câu hỏi (ưu tiên vận hành, infra, audience) + chọn posture + viết rationale trước khi AI viết — áp dụng ngay cho mọi workflow content/strategy: đừng single-shot prompt, chèn 1 bước structured elicitation.
- Scaffold cứu prompt yếu nhưng vẫn giúp prompt tốt (+20.9%) — không chỉ dành cho user yếu; trade-off articulation là dimension được cải thiện nhiều nhất.
- Đừng tin self-rating: user tự đánh giá quality không tương quan rated quality — cần rubric客观 + rater blind, không hỏi user "thấy hay không".
- Invest in detector + router, không phải feedback generator: nơi environment trả hard failure signal, majority gain đến từ noticing failure + spending bounded retry budget; marginal call biến error thành eloquent guidance chỉ mua 1 point exact match. Ví dụ: Text-to-Cypher agent — EXPLAIN pre-validation + LIMIT 1 empty detection + 2-cycle budget + raw error string retry = 91.7% recovery mà KHÔNG cần LLM-synthesised hints module.
- First-time success phải cost đúng 1 call: short-circuit validation (0 calls khi both checks pass) để overhead chỉ rơi lên minority queries fail (53–97% need no correction). Ví dụ: pipeline agent — validate statically trước, chỉ call model khi fail, mean 1.1–2.5 calls/query thay vì fixed multi-call.
- KHÔNG dùng parallel sampling thay sequential correction trong low-entropy output spaces (structured queries có ít correct forms): Best-of-3 degrade 10.8–11.4%, temperature T=0.7 làm hit rate FALLS (87.6%→85.2%). Ví dụ: budget cho query agent → sequential retry với error feedback, KHÔNG k=3 sampling.
- Externalize model identifier (env var/registry): 94% migrations edit source vì identifier hard-coded — indirection biến majority migrations thành one-line change. Ví dụ: coding app dùng `MODEL_ID` env var + model registry map → retire event chỉ cần đổi 1 dòng config, không phải sửa 94% codebase.
- Static deprecation check trong CI: flag model identifiers against providers' deprecation tables, CI failure TRƯỚC shutdown date — would have prevented most post-shutdown commits in corpus. Ví dụ: nightly job query OpenAI/Anthropic/Google deprecation pages, fail CI nếu codebase chứa identifier nằm trong danh sách retire <90 days.
- Notice length là lever duy nhất predict được proactive migration (dose-response −74–78% odds per e-fold): 60-day notice → 86–98% reactive; 1-year notice → 13%. Ví dụ: với provider chỉ cho 60-day notice (Anthropic-style), đặt internal migration deadline tại announcement + 30 ngày, không phải shutdown − 7 ngày.

---

## Details per paper (folder links)
- [1] (When) Should a Software Factory be Lights-off? Benchmarking Code Review Agents on Bug Detection — `2610.13668v1` — details: `papers/papers/2026/10/17/CRBugBench-Code-Review-Agents/`
- [2] AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework — `2609.30541v1` — details: `papers/papers/2026/10/17/AutoResearch-Production-Scale/`
- [3] Do Tool Calls Execute as Intended? Measuring and Repairing Intent-Execution Correspondence in LLM Agents — `2610.04375v1` — details: `papers/papers/2026/10/17/IntAct-Intent-Execution-Correspondence/`
- [4] FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents — `2609.26048v1` — details: `papers/papers/2026/10/17/FIRE-Failure-Informed-Runtime-Engineering/`
- [5] Incremental Pooled LLM Evaluation for Cost-Effective Retrieval Model Selection — `2609.02745v1` — details: `papers/papers/2026/10/17/Incremental-Pooled-LLM-Evaluation/`
- [6] LLM-based User-Product Relevance Evaluation for Dynamic Product Advertising — `2610.14550v1` — details: `papers/papers/2026/10/17/LLM-User-Product-Relevance-DPA/`
- [7] Learning How Much to Collaborate: Difficulty-Aware Topology Selection for Multi-Agent Code Generation (Dats) — `2609.13890v1` — details: `papers/papers/2026/10/17/DATS-Difficulty-Aware-Topology/`
- [8] Structured pre-generation elicitation versus single-shot prompting in AI-assisted enterprise decision-making: a randomised online experiment — `2610.09593v1` — details: `papers/papers/2026/10/17/Cognistance-Pre-Generation-Elicitation/`
- [9] What Drives Recovery in Agentic Text-to-Cypher? LAST-CQ: An LLM Agent Self-Refinement Framework — `2609.12746v1` — details: `papers/papers/2026/10/17/LAST-CQ-Text-to-Cypher-Recovery/`
- [10] When the Model Retires: An Empirical Study of LLM Migration in Open-Source Applications — `2609.31288v1` — details: `papers/papers/2026/10/17/LLM-Migration-Retirement-Study/`

*Auto-generated by daily_summary.py after each 10-paper distill day.*