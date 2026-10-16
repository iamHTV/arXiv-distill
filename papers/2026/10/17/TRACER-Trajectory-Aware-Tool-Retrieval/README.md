# 2610.21267 — TRACER: Trajectory-Aware Tool Retrieval for LLM Agents

## Problem
- Agent chọn tool từ registry lớn: expose toàn bộ registry → token cost cao + selection suy giảm khi registry lớn (dài, chi tiết làm relevant info khó dùng reliable). Description-based retrieval nhầm semantically similar tools; retrieval errors propagate xuống execution.
- Gap cốt lõi: mỗi step bị treat như independent search, trong khi tool retrieval là sequential prediction — call nào đến tiếp theo, given các call đã làm. τ² retail request resolve theo thứ tự logic: identify customer → pull account → open order → act on it. Các call đã làm constrain call tiếp.

## Contribution
- TRACER (Trie Retrieval Across Contextual Edges, Reweighted): state-conditioned retrieval front-end — 3 ý tưởng: (1) full-prefix conditioning (execution trie over observed tool-call sequences; prefix trong turn = node; tools thấy sau nó = candidates), (2) transition-specific usage memory (mỗi edge lưu conversations mà transition được thực hiện), (3) state-dependent weighting (learned per-step blend giữa empirical prior và contextual prior).
- Candidate set nhỏ (k ≪ |R|) mỗi step nhưng vẫn để model chọn cuối cùng. Beats full-registry selection 21/24 model-environment pairs, avg +6–10 points, cắt per-step tokens 55–90%.

## Method
- Trie construction: insert mọi prefix của mọi trajectory làm node; children C(Si) = tools observed ngay sau Si; mỗi edge mang P(trie)(t|Si) (empirical prior, normalized transition frequency, log + smoothing ε) và edge memory m(Si→t) (mean-pooled embedding của training contexts transition được thực hiện). Trie turn-local (reset ở turn boundary); edge memory KHÔNG turn-local (embed full conversation → cross-turn info tới retriever mà không vào trie structure).
- Contextual prior: embed step context (all previous turns + step reasonings, drop tool-call signatures để giới hạn length) bằng frozen embedder e; R(t) = cos(e(ctx(q,Si)), m(Si→t)); ReLU-normalize thành distribution (uniform nếu mọi similarity ≤0); L(t) = log(R̂(t)).
- Learned scoring: s(t) = (1/T)[(1−w)L(t) + wP(t)], top k presented. w, T do learned map fθ(x)=(w,T) trên state feature vector x ∈ R⁵ mỗi step (two linear heads: logistic head cho w — giữ blend convex; floored softplus head cho T — giữ temperature positive). Fit θ bằng Adam + ℓ2, minimize NLL of gold next call under softmax over C(Si), inner-fold isolation (mỗi step scored chống trie/edge memory built WITHOUT own trajectory).
- Confidence gate + OOD fallback: unseen state (C(Si)=∅) hoặc flat score distribution (κ<τ, τ=0.20) → global vector search over full registry (cosine embedded step context vs tool descriptions), replace trie candidates entirely.
- TRACER+G: registries tập trung vào generic utility tools → union global set G (|G|=3 tools có prefix entropy H(S|t) cao nhất) vào mọi candidate set. TRACER-fixed ablation: fixed blend s(t)=L(t)+P(t).
- Benchmarks: Mixed Tau2 R&T (retail+telecom, 128 deliberately confusable tools, real τ²-bench trajectories + vetted synthetic từ co-occurrence graph; 99.8% retail/99.9% telecom clear non-cloning gate; blind human study 67.8% chọn synthetic là human-authored), Tau3 Banking (~700 interconnected documents, compliance gating unlock:X), BFCL v3 (weakly-related API families), API-Bank (homogeneous reference). 4 models: GPT-5.4, GPT-5.4-mini, Grok-4-20-reasoning, Mistral-Large-3; embedder text-embedding-3-small; 5-fold CV; teacher-forcing (primary, đo front-end isolation) + free-running (errors compound, 20-step cap, grader score bằng database hash + required read ops).

## Key Findings
- Teacher-forcing Mixed Tau2 Large k=5: GPT-5.4 TRACER 61.9% vs LLM-ONLY 57.2% (+4.7) vs VECTOR 27.7%; CIC 2.8k vs 14.2k prompt tokens/step (−80%). Gains >1 SD trong 31/34 winning cells. Grok trails 0.3 (trong 3.8 SD).
- 21/24 model-environment pairs cải thiện over full-registry (avg +6–10 points); 3 exceptions trail ≤2.2. CIC reduction 55%→80% khi Mixed Tau2 pool lớn lên; 31% (Tau3 Banking — long conversation histories dominate prompt) đến 90% (BFCL v3).
- Free-running: GPT-5.4 parity — Large +0.1 points tại 23% registry, Medium +1.2 tại 33%, Small +2.3 tại 43%; GPT-5.4-mini +13.7→+15.2 trên Large (từ 3.9% registry). Full-turn: task success 58.3% vs 58.2% (match), 23% tools, −61% per-step input tokens. 16/24 cells within 3 points (median 2.2); GPT-5.4 below LLM-ONLY tại 8/12 budgets (single early miss → unseen prefix → vector fallback).
- Specificity trap: LLM-ONLY fallback vào generic hub get_order_details trên 36.4% steps (5 order-management APIs: split_order_shipment 14%, add_gift_message 32%, request_return_pickup 16%, schedule_installation 29%, file_shipping_insurance_claim 49%); TRACER cắt trap rate 16.4%. Example: prepaid return label — LLM-ONLY gọi destructive return_delivered_order_items, TRACER rank tool đó thứ 9 → chọn đúng get_return_label.
- Procedural controls: banking unlock:X trước write — trie withholds raw write (không successful trajectory nào đạt open_bank_account mà không qua unlock); LLM-ONLY bỏ unlock.
- Ablations: description-only Trie-Bayesian −21 points vs TRACER-fixed (API-Bank, GPT-5.4-mini) — contextual prior là yếu tố chính; learned vs constant blend +8.0/+5.9/+6.0/+7.6 (Mixed Tau2), +3.9/+3.5/+7.1/+5.8 (BFCL), chỉ +0.6–1.1 (Tau3 — generic tools dominate); w trung bình 0.019 (contextual prior dominant), tăng early trong conversation và nơi empirical prior confident; last-2 trie +1.5–2.9 (trong SD), 9.6% out-of-trie vs 12.4%.
- TRACER+G: Tau3 Banking +5.8 (generic KB_search/grep dominate); hurts τ²/BFCL (thêm distractors).

## Actionable Insights
- Đừng expose toàn bộ registry: 5/128 tools (k=5) beats full-registry +4.7 points với −80% tokens — smaller candidate set cải thiện chính model selection accuracy, không chỉ cost.
- Index execution history thành trie (prefix → candidates) thay vì query→tool similarity: prefix conditioning tách được "tool giống nhau nhưng mục đích khác nhau ở bước khác nhau" (specificity trap 36.4%→16.4%) và enforce procedural ordering (unlock trước write) miễn phí.
- Blend 2 signals per-state, đừng fix toàn cục: learned blend worth +0.6–8.0 points tùy benchmark; contextual prior (conversations transition được thực hiện) quan trọng hơn empirical prior trên diverse tries (w≈0.02) — edge memory là thành phần không thể bỏ (−21 points khi description-only).

## Assumptions & Limitations
- Cold start: cần dataset graded trajectories — registry không usage history → mọi step fall về vector fallback (accuracy 38 points below); method giả định deployment đã log successful runs. Trie cần bao lâu mới useful — chưa đo được với fixed-size corpora.
- Free-running regressions: single early miss → unseen prefix → vector fallback (out-of-trie rate ~3× teacher-forcing); prefix-independent lookups (không prefix nào predict) là điểm yếu nhất — paper đề xuất future: present full registry ONLY on out-of-trie steps (+38 points avg, giữ 84% token reduction).
- Premise: mọi tool available at mọi step (edge count phản ánh what agent chose, not what offered) — không áp dụng cho permission-gated registries.
- Trie key depth fixed (full current-turn prefix); last-2 trie gần bằng (trong SD). Budget k và global set G fixed — nên adapt per domain/model (future work).
- Mixed Tau2 có synthetic trajectories (dù validated: 67.8% human study).

## Metadata
- 2026 (2026-10-15), Tanish Kher (UC Berkeley, internship at Microsoft), Sarvesh DK Abedelkadir Asi, Sparsha Chennarayapatna Sundaresh Dezhi Hong (Microsoft), cs.CL, https://arxiv.org/pdf/2610.21267
