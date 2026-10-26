# Skill: Distill CoT thành latent token cho recommender hiệu quả (OneLatent recipe)
Source: 2610.30675
Type: framework (training + serving recipe)

## Khi nào dùng skill này
- Bạn có recommender/ranker dùng LLM và cần "reasoning quality" nhưng latency budget nhỏ (serving real-time).
- Bạn đang generate explicit CoT rationale cho ranking mà thấy trace dài, tốn kém, quality gain không rõ.
- Bạn muốn distillation (chưng cất) từ teacher LLM lớn sang student model nhỏ phục vụ production.

## Khi NÊN DÙNG
- Item corpus đủ lớn/ổn định để xây Semantic ID (SID — mã ngữ nghĩa item) 3 mức bằng Res-Kmeans.
- Bạn có access teacher LLM mạnh (vd Qwen3-235B) để sinh supervision offline (một lần).

## Khi KHÔNG nên dùng
- Corpus item thay đổi liên tục (SID phải rebuild liên tục → fragile).
- Không có budget GPU cho teacher offline → không có supervision chất lượng.
- Task không phải ranking/generative retrieval (skill này tối ưu next-item SID prediction).

## Input cần có
- Interaction history dataset (profile Pu, history Hu, request context Cu, next item).
- Item metadata + embeddings để phân cụm Res-Kmeans → SID 3 token.
- Teacher LLM + prompt template 3 view (Exploration/Evaluation/Attribution).
- Pretrained LLM backbone làm student FRM (paper dùng Qwen3.5-0.8B/9B).
- Cơ sở hạ tầng: Redis cache, async gRPC inference service, event stream (click/view).

## Các bước thực hiện
1. **Build item SID**: encode item multimodal info → Res-Kmeans 3 mức → mỗi item = 3-token SID [s(1);s(2);s(3)]; bidirectional align SID ↔ dense caption: Lsem = −log p(S|C) − log p(C|S).
2. **Sinh MV-ACoT supervision (offline)**: với mỗi sample, teacher sinh 3 view: (a) Exploration — chỉ profile+history, output rationale + intent list (no candidate); (b) Evaluation — + positive item làm privileged info, output rationale + score 1–5; (c) Attribution — + positive item, output rationale giải thích signal nào gây ra interaction. Prompt yêu cầu teacher tự đánh giá complexity evidence (strong behaviors, conflicting interests, weak signals, noise) rồi điều chỉnh độ dài: simple → converge nhanh; complex → multi-dimensional comparison. Reasoning dimension (geography, time, signal strength, industry constraints, conversion stage) chỉ chọn khi evidence hỗ trợ. KHÔNG dùng classifier difficulty riêng, teacher KHÔNG emit difficulty label.
3. **Stage I — single-view alignment**: thêm 3 latent token ID ⟨L1⟩⟨L2⟩⟨L3⟩ vào vocab; train student reproduce rationale 1 view từ prefix [Pu; Hu; ⟨view⟩; L] (view control token chỉ định loại rationale).
4. **Stage II — multi-view alignment**: dùng tất cả view; average token loss within mỗi output (trace dài không nặng hơn); prefix student KHÔNG chứa candidate/target dù teacher view có dùng (tránh leakage privileged info).
5. **Stage III — context alignment**: nối interface latent với next-item prediction: prefix [Pu; Hu; Cu; L] → predict target SID sequence.
6. **Curriculum post-training**: SFT standard theo Dhigh→Dmedium→Dlow (user activity giảm dần); rồi latent-reasoning SFT trộn 1:1 với standard SFT (½ LLR + ½ LSFT) → giữ performance cả 2 mode.
7. **Inference**: append 3 latent token ID vào input, decode thẳng 3-level SID — KHÔNG generate rationale text. Reasoning overhead = 3 token cố định.
8. **Serving async**: FRM off request path; behavior event → value-aware admission (user value × behavior strength) → scheduler dedup + egress QPS cap → gRPC inference async → map SID→item → cache Redis; online path đọc cache, fallback result cũ khi delayed. Deploy FRM làm retrieval channel riêng, candidate merge với pipeline hiện tại, compete ở fine-ranking stage.
9. **Evaluate**: SID Hit@K/ID Hit@K (K∈{1,16,32,64}); codebook retrieval Hit@L1/2/3; QPS vs explicit-CoT baseline (target ≥10×); LLM-as-judge 9-dimension rubric trên 100 samples/view; reconstruction cosine theo view (target ≥0,78); latent-token-count ablation (1 vs 2 vs 3 vs 4+, chọn điểm no-consistent-gain); online A/B 5%/5% ≥7 ngày (impressions, ad spend, est. revenue).

## Output mong đợi
- Student model nhỏ (0,8B class) đạt SID@64 ngang/over explicit-CoT teacher recipe với QPS ~274 (vs ~16 của CoT) — 17× throughput; latency ~3 s batch 872 instances ngang no-think baseline; + revenue lift measurable trên A/B (paper: impressions +2,566%, spend +5,157%, revenue +9,6%).

## Ví dụ áp dụng
- Trang content Việt: muốn gợi ý "bài tiếp theo" cho reader. Bước 1–6 offline: teacher (LLM lớn) sinh rationale 3 view cho 60K log click; train Qwen3.5-0.8B với 3 latent token. Bước 7–8: khi reader click bài mới → trigger async rerank → cache top-10 in Redis → API gợi ý đọc cache (latency <10 ms) thay vì call LLM reasoning mỗi request.

## Gotchas
- **Privileged leakage**: prefix student Stage I/II tuyệt đối không chứa target item/candidate dù teacher dùng → nếu không latent token học "đọc đáp án" chứ không phải lý luận.
- **Token loss weighting**: average per output, không sum — trace dài sẽ tự dominate loss.
- **Latent token count**: 3 là sweet spot paper (1→3 improve, >3 redundant no consistent gain); đừng thêm nhiều "cho chắc".
- **CoT ≠ tốt hơn**: Think checkpoint có thể KÉM No-Think (paper: 0,354→Hit@L1 marginal, latency 17×) → benchmark cả 2 mode trước khi đầu tư.
- **Sync full traffic impossible**: OneLatent một mình không đủ latency sync → async behavior-triggered serving là bắt buộc, không phải optional.
- **Reconstruction cosine ≠ faithfulness**: ≥0,78 cosine chỉ chứng minh semantic association, KHÔNG chứng minh bottleneck thông tin strict → đừng claim "lý luận ẩn hoàn toàn chứa trong 3 token".
- Curriculum order: high→low activity; đảo thứ tự sẽ train trên noisy low-signal user trước → unstable.
