# 2610.14550 — LLM-based User-Product Relevance Evaluation for Dynamic Product Advertising

## Problem
- Hệ thống retrieval quảng cáo sản phẩm động (DPA) thiếu metric offline đáng tin: engagement metric (metric tương tác) bị selection bias (lệch chọn lọc) + sparse (thưa); online evaluation tốn kém. Search có query rõ ràng, ads thì không — prior work không infer được user-level relevance từ engagement history dị biệt.

## Contribution
- Metric relevance query-free: nén engagement history thành intent set (tập ý định) qua Semantic ID (SID) grouping + event-stratified segmentation, LLM judge chấm từng cặp intent–candidate, aggregate thành user-level score
- Pipeline scalable: SID compression giảm 30× LLM calls; agentic guideline discovery + human alignment + teacher-student distillation
- Validate với online KPI thật: ranking 6 retrieval source nhất quán với conversion precision/recall, directionally aligned với CTR/CVR delta qua 4 A/B test

## Method
- Intent representation: RQ-kmeans (L=3 stage, codebook 512) trên multimodal product embedding → SID; nhóm theo (SID prefix, event type), đại diện = sản phẩm gần nhất; weight w_g = log(1+|g|)·β(e_g), β(purchase)=3, add-to-cart=2, khác=1.
- Judge: Phase A agentic rule discovery — seed prompt 5 tầng (Exact/Similar/Substitute/Complementary/Irrelevant), Gemini-2.5-Pro label calibration split, loop: cluster lỗi → propose ≤3 sub-rule → chấp nhận iff paired-bootstrap 95% CI trên Δaccuracy loại trừ 0, không F1 regression >0.5pp; giữ rule lặp lại qua nhiều trial. Phase B human alignment: audit business-critical mismatch (demographic gender/age, regulated category, advertiser exclusion) — demographic mismatch được nâng thành hard Irrelevant override.
- Distillation: teacher Gemini-2.5-Pro + GPT-5 verification agent, disagreement → human; student Gemini-2.5-Flash fine-tune LoRA rank 16, lr multiplier 2, 5 epochs. Metric: MicroRel/MacroRel, threshold-k aggregation (k=7).

## Key Findings
- SID grouping + event stratification: fidelity 0.99 Spearman với full sequence ở 3.4% pairwise cost (~30× reduction); weighted variant đạt P(CVR)=0.50, P(CR)=0.29, P(CP)=0.35, hơn Random baseline (+0.24 CVR, +0.16 CP) trong khi baseline tốn 7×.
- Student Flash-ft matching teacher F1 0.869 vs 0.860; +2.9% precision, +3.0% recall so với prompt-only; hơn SigLIP-2-mm 9% precision, 12% recall (dữ liệu ít 10×).
- Latency: Flash-ft 751ms p50 / 1,117ms p95 / 18 QPS vs teacher 6,963ms / 10,840ms / 2 QPS (~9× nhanh hơn). Prompt-only Flash giữ p95 dài 8,807ms — fine-tune nén cả p50 lẫn p95.
- Threshold k peak ở [5,7]; k=7 tất cả 95% bootstrap CI dương: P(CVR) [+0.29,+0.68].

## Actionable Insights
- Nén history trước khi dùng LLM judge: grouping semantic + weighting theo event strength giảm 30× cost mà vẫn giữ fidelity 0.99 — áp dụng cho mọi pipeline đánh giá content: đừng judge từng event, judge intent representative.
- Guideline quan trọng hơn model: guideline mang phần lớn lift (Pro không guideline thua cả student có guideline) — đầu tư viết taxonomy + rule trước khi đổi model.
- Fine-tune chứ đừng chỉ prompt: prompt-only giữ long-tail p95 như teacher; fine-tune nén p95 theo bậc — khi latency quan trọng, distillation là bắt buộc.

## Assumptions & Limitations
- Engagement-based iteration trộn ranker alignment với engagement signal → correlation yếu/noisy hơn.
- Metric là gate trước A/B, không thay thế online eval; demographic rule quá hiếm trong calibration set nên agentic loop không tự tìm ra — cần human pass.
- Không nói: validation chỉ 2 retrieval source cho Figure 2; threshold k peak có thể dịch ở catalog khác.

## Metadata
- 2026, Wen Zhang, Xiao Bai, Hsiang-wei Chao, Mengfan Zhu, Tong Zhao, Mingxuan Ju, Xiaodong Liu, Congfei Zhang, Yunzhi Zhou, Yajun Wang, Jinchao Li, Yu Zhang (Snap Inc.), cs.IR, CIKM '26, https://arxiv.org/pdf/2610.14550
