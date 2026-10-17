# 2610.10827v2 Grammar Concept Annotation at Scale: Deployed Fine-Tuned Small Language Models Outperform Prompted Frontier Models

## Problem
- Corrective feedback (phản hồi sửa lỗi) là driver có bằng chứng mạnh nhất cho second-language acquisition (tiếp thu ngôn ngữ thứ hai), nhưng correction đưa ra trong bài học hiếm khi tích lũy thành view actionable về grammar mastery (mức độ nắm ngữ pháp). Prompted frontier model (GPT-5.4) có thể tạo view đó từ lesson transcript nhưng cost quá lớn khi scale: pilot prompt 3,810 token/request (liệt kê đủ 34 concept, edge case, example) vượt serving budget, gây prefill latency và chiếm KV-cache memory trong vLLM. Pattern chung của enterprise AI: nhiều sản phẩm nằm ở pilot, chỉ ~5% reach production.

## Contribution
- Hệ thống grammar mastery tracking end-to-end deploy cho TOÀN BỘ English learners trên Preply: speech-to-text transcript → extract learner utterance + upstream correction → annotation model dự đoán single-pass tập {(concept, exact span, correctness, explanation)}; aggregate thành overall và per-concept mastery score, weighted by concept frequency, CEFR level, forgetting curve; mọi evidence traceable đến highlighted span trong câu learner.
- Formulation grammar concept annotation (34 concepts) + 2 human-curated benchmark (Golden 689 utterances mirror production; Golden2 2,977 utterances error-enriched 95.6% error-bearing) + nested criteria L1 concept / L2 +exact span / L3 +correctness.
- Data quality pipeline (evidence-grounded review, deterministic validation, filtering, synthetic enrichment) — +36.9–40.7 pp strict L3 recall vs raw teacher supervision.
- Production serving: 0.8B SLM + prompt compaction (3,810 → 375 token, −90.2%) + native vLLM + autoscaling → ~16× serving cost reduction (cost/lesson còn 6.2% baseline GPT-5.4).

## Method
- Fine-tuning: Qwen3.5 base (0.8B và 4B reference), completion-only LoRA (r=128 all linear layers cho 0.8B, r=16 cho 4B); pack 5 utterance–correction pairs/1 conversation; 90/10 split; discard over-length; checkpoint chọn theo min teacher-forced validation loss, 4 evals/epoch, early-stop patience 3.
- Data pipeline 3 stages: (i) review production annotations (50k uniform + 50k heuristic sampling ưu tiên anomaly) bằng hybrid neuro-symbolic — spaCy deterministic linguistic anchors + hand-crafted rules + word-level edit diff từ correction, GPT-5.4 full review/re-annotation pass, deterministic post-validator enforce contract invariants (reject non-substring span, prune invalid label, enforce explanation consistency); (ii) synthetic enrichment: structural backbone (concept label + correctness flag sequence) sampling 3× 30k (uniform, error-weighted, smoothed inverse concept-frequency), inject pedagogical error vào generation plan (within-concept misuse, omission, confusable structure substitution), GPT-5.4 realize, post-validate; (iii) consolidation: dedup (1.4% overlap), loại bỏ mọi utterance trùng golden benchmark → ~187k utterance groups (100k reviewed production + 90k synthetic pre-dedup).
- Serving: vLLM trên autoscaled single-GPU g6.2xlarge SageMaker; packed 5-pair requests; failure route về GPT-5.4 fallback.
- Evaluation: micro precision/recall tại L1/L2/L3; 20,000 paired nonparametric cluster bootstrap CIs; two-sided paired randomization test 20,000 permutations; explanation do GPT-5.5 LLM-as-judge + human audit/reconcile.

## Key Findings
- Golden: fine-tuned 4B L3 P/R 81.28/83.49, fine-tuned 0.8B 80.84/78.89 — đều vượt prompted GPT-5.4 (67.81/62.87) và GPT-5.6 Sol (67.04/58.66); base model gần như không parse được (4B base L3 P/R 3.01/16.56; 0.8B base 3.10/10.73; parse fail 26.9–32.8% và 75.3–92.0%).
- Golden2 (error-enriched): 4B fine-tuned L3 82.74/85.16, 0.8B fine-tuned 82.55/80.88 vs GPT-5.4 74.37/76.04, GPT-5.6 Sol 74.97/72.39 — fine-tuned SLM thắng ở mọi matching level, precision và recall; mọi fine-tuned Qwen–GPT-5.4 difference significant p < 0.0001.
- Pipeline ablation: full pipeline vs raw supervision cùng size — Golden2 L3 P +28.37 (4B) / +29.93 (0.8B) pp, L3 R +36.91 [35.93, 37.87] / +39.95 [39.01, 40.89] pp; Golden L3 R +37.33 / +40.66 pp; Rare-9 recall lên tới +45.31/+45.81 pp (Golden2); raw supervision degrade L1→L2 23.64–23.78 pp vs 6.28–6.31 pp full pipeline (exact-span robustness).
- Explanation quality: uncalibrated GPT-5.5 judge chấm GPT-5.4 99.06% acceptable vs 4B 94.91%, 0.8B 93.88%; SAU human audit + reconcile: cả ba ≈95%, không significant difference — judge thiên vị frontier sibling.
- Online A/B 35 ngày, learner-level, 50% exposure: engagement with progress +15.80% (p<0.001), scheduled hours (CUPED) +2.06% (p=0.021), confirmed hours from new tutoring +10.87% (p=0.039), GMV from new lessons +13.20% (p=0.020) — mọi 95% CI loại trừ 0; gains thuộc end-to-end feature, không phải SLM đơn lẻ.
- Serving: 8 g6.2xlarge instances sustain throughput trên post-rollout peak; 31-day APM snapshot p95 latency 4.3 s; recurring detection cost/lesson = 6.2% GPT-5.4 baseline (≈16× reduction).

## Actionable Insights
- Prompt internalization: fine-tune small model trên teacher demonstrations để nén verbose system prompt vào adapter weights — prompt 3,810 → 375 token (−90.2%), max seq 7,000 → 2,500, cost ~16× trong khi quality TĂNG (L3 recall 62.87 → 78.89 trên Golden). Ví dụ: production feature nào có system prompt vài nghìn token là candidate fine-tuning.
- Budget cho data quality, không phải volume: review + deterministic validation + synthetic rebalancing cho +36.9–40.7 pp strict recall; raw teacher supervision degrade mạnh ở exact-span matching. Ví dụ: khi fine-tune trên LLM-generated labels, dành phần lớn effort cho review pass + post-validator, không phải sinh thêm data.
- Calibrate LLM judge bằng human audit trước khi tin comparative eval: uncalibrated judge chênh lệch 5.2 pp nghiêng về chính nó (99.06% vs 93.88%), human audit đưa về ≈95% hòa. Ví dụ: mọi eval "model A beats model B" dùng LLM-as-judge cần sample audit.

## Assumptions & Limitations
- Điều kiện: annotation model nhận utterance + upstream correction (không full transcript); fallback GPT-5.4 khi validation/service fail; curriculum 34 concepts (iteration sau >300 fine-grained concepts).
- Limitation paper thừa nhận: pipeline ablation không isolate từng component; single training run/config, không estimate across-seed variance — fine-grained metric differences không nên over-interpret; 4B và 0.8B dùng independently tuned recipes + prompt length khác nhau nên difference across sizes không phải isolated parameter ablation (0.6B là earlier Qwen generation); A/B đánh giá end-to-end feature; cost model loại trừ upstream transcription/correction/fallback; explanation eval vs gold rubrics chứ không perceptual study với teacher/learner; ASR transcription error cascade chưa isolate; systematic teacher (GPT-5.4) bias có thể tồn tại.
- Limitation CHƯA nói: benchmark Golden/Golden2 không public (privacy) → không replicate được; load test 8 instances có thể chưa cover tail traffic; fallback GPT-5.4 cost không tính vào 16× reduction; packed 5-pair batching giả định transcript đủ 5 utterances.

## Metadata
- 2026, Marjan Celikik, Ana Peleteiro Ramallo, Javier Morales (Preply), cs.CL, https://arxiv.org/pdf/2610.10827v2, citation count: không tìm thấy [NO BENCHMARK]
