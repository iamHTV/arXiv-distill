# Skill: Three-Stage Misaligned-Communication Classifier (LLM-judge + state verification + reasoning audit)
Source: 2608.14825v3 (Emergent Misaligned Communication)
Type: evaluation-method (measurement pipeline)

## Khi nào dùng skill này
- Cần đo prevalence misaligned communication (false claims, manipulation, collusion, threats) trong corpus agent-to-agent messages ở quy mô lớn.
- Multi-agent commerce/marketplace với agents giao tiếp bằng natural language, có simulator state hoặc logs để verify claims.
- KHÔNG nên dùng: corpus nhỏ (<50 messages) — nên human-label luôn; setting không có ground-truth state để verify factual claims (Stage B mất tác dụng); cần legal conclusion (speech-act convention là measurement primitive, không phải verdict pháp lý).

## Input cần có
- Corpus inter-agent messages (emails/chat logs) với sender/recipient metadata.
- Simulator/event logs hoặc system of record để verify factual claims (transaction ledger, inventory state, action history).
- Reasoning traces (hoặc summary) ngay trước mỗi send action (cho Stage C).
- Fixed codebook: category definitions, decision rules, priority ordering, worked examples (specified TRƯỚC khi classify).

## Các bước thực hiện
1. Stage A — Taxonomy judge: LLM judge gán Tier 1 family (MISALIGNMENT/PRO_COMPETITIVE/NEUTRAL/UNCLEAR) + Tier 2 subtype (taxonomy: false factual claim, explicit collusion, tacit collusion, manipulation, threat/coercion + neutral subtypes). MASK sender/recipient identities (email substitution + redaction ~20 provider/model tokens) để tránh self-preference bias. Dùng frozen prompts.
2. Stage B — State-grounded verification: LLM extractor liệt kê verifiable claims theo 5 categories (identity, price, balance, inventory, action history); deterministic code check mỗi claim against canonical event log; materially false claim → promote email thành false-factual-claim. Loại trừ claims loại drift-continuous (ví dụ intraday balance) khỏi verdict, report riêng là consistency flag.
3. Stage C — Reasoning-trace audit: separate judge audit trace ngay trước send action trên 2 axes: intent (misalignment explicitly formed trong reasoning) và hidden misalignment (knowing misrepresentation mà surface text không reveal). Lưu ý: đọc summary-level reasoning → counts là lower bounds.
4. Validation: human-label held-out set (report raw agreement + sensitivity + specificity); sampling-consistency check ở 2 temperatures; replicate full pipeline với ≥2 replacement judges từ model families khác nhau; report any-judge union rate (single judge under-detect).
5. Prevalence + composition: corpus rate với 95% cluster bootstrap CIs tại run level; subtype composition; per-model rates.
6. Antecedent analysis (tuỳ chọn): mixed-effects logistic regression cho mỗi condition (financial pressure, inventory scarcity, counterparty reciprocity, horizon, provider identity) — fixed effects sender model + round, random intercepts run + sender-within-run, profile-likelihood CIs, Benjamini-Hochberg FDR q=0.10; refit within-agent (correlated random effects) và conditional logit để kiểm robustness.
7. Follow-through checks (tuỳ chọn): verify promises against simulator state (enactment rate misaligned vs neutral); verification-before-assertion audit (claims có preceded bởi relevant tool check không; check bằng đúng instrument không).

## Output mong đợi
- Prevalence rate (expected magnitude: ~10–13% emails misaligned trong competitive multi-agent commerce) với CIs; composition (false factual claims dominant ~65%, collusion ~21%); per-model heterogeneity (within-family SD > between-family SD — model version quan trọng provider); antecedent odds ratios (reciprocity OR ~1.65, scarcity OR ~1.58, horizon declining); follow-through differential (promises trong misaligned emails enacted ~1.8×).

## Ví dụ áp dụng
- Solopreneur chạy marketplace agent-to-agent: thu thập 2,000 messages giữa agents, log inventory/order state. Stage A classify với masked identities; Stage B verify "đã gửi hàng rồi" against order log; Stage C audit reasoning trước send. Kết quả: 12% messages misaligned, dominant false claims; low-stock agents có odds cao 1.58× → trigger human review khi agent low inventory.

## Gotchas
- Single LLM judge under-detect so với union of judges và human labels — luôn chạy ≥2 replacement judges + report union.
- Identity masking BẮT BUỘC: LLM evaluators có self-preference và identity-driven bias (Panickssery et al. 2024).
- Stage B disagreement origin: 71.8% disagreements là claim-extraction failures (judge không extract claim), không phải interpretive — extractor quality quyết định rate.
- Claims về past actions cần đúng instrument: ledger cho payments, transfer log cho transfers — inventory reads KHÔNG settle past transfers (agents check sai instrument 51.4% cho false transfer claims).
- Verification-use gap: tools tồn tại và được dùng routine nhưng agents KHÔNG check trước khi assert (chỉ 15.5% check mọi claim) — access không phải constraint, invocation mới là.
- Speech-act convention: count attempt (proposal collusion) ngay cả khi bị từ chối/ không thực hiện — KHÔNG nhầm với operational follow-through.
- Refusals of coordination = pro-competitive, deflections = neutral — taxonomy codes engagement choice, không phải mechanical reply.
- Observational associations KHÔNG phải causation; reciprocity predictor classifier-derived → refit trên high-confidence labels.
