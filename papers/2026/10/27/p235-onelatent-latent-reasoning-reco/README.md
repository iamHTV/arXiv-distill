# [2610.30675] OneLatent: Latent Reasoning cho Foundation Recommendation Models

## Problem
- FRM (foundation recommendation model — mô hình đề xuất nền tảng) dùng LLM làm backbone, prior work (OneReason, RecGPT) đều dùng explicit CoT (chain-of-thought — chuỗi lập luận hiển thị) theo kiểu Think-then-Answer. Prior work chưa giải quyết được 2 vấn đề: (1) overthinking (lập luận dư thừa): trace dài dòng ngay cả với request rõ intent, latency tăng mà gain marginal; (2) interest drift (lệch sở thích): template cố định 1 đường lý luận bỏ qua sở thích ngắn hạn theo context, 1 lỗi/hallucination trong rationale lan sang output cuối.

## Contribution
- Latent-Reason-then-Answer: nén trace lý luận thành 3 latent token (token ẩn) học được — cố định, shared mọi sample, không phải vector per-sample — nên reasoning-token overhead là hằng số chứ không tỉ lệ với độ dài trace.
- MV-ACoT (Multi-View Adaptive CoT — CoT đa góc nhìn thích ứng): teacher Qwen3-235B-A22B-Instruct-2507 tạo supervision từ 3 view (Exploration/Evaluation/Attribution) + tự điều chỉnh độ sâu lý luận theo độ phức tạp evidence, KHÔNG dùng classifier difficulty riêng.
- Production serving: FRM chạy làm retrieval channel riêng, off đường request online, refresh cache theo behavior event (user value + behavior strength).

## Method (tóm tắt cốt lõi)
- Item = 3-token SID (Semantic ID — mã ngữ nghĩa) xây bằng Res-Kmeans; vocab LLM bổ sung SID token + 3 latent token; full-parameter update, KHÔNG thêm encoder/projector/decoder nào.
- Stage I: prefix [profile; history; view-token; L] → reproduce rationale 1 view. Stage II: tất cả view, average token loss theo output (trace dài không nặng hơn); student prefix KHÔNG chứa candidate/target item dù teacher view Evaluation/Attribution dùng target (privileged supervision — supervision đặc quyền).
- Stage III: cùng interface nối với next-item prediction: [profile; history; context; L] → predict target SID. Post-training: curriculum SFT theo Dhigh→Dmedium→Dlow (user activity), rồi latent SFT trộn 1:1 với standard SFT (Lpost = ½·LLR + ½·LSFT).
- Serving: streaming interaction → value-aware admission → scheduler dedup, egress QPS cap → async gRPC inference → map SID→item → cache Redis; online path đọc cache, fallback result cũ khi update delayed.

## Key Findings
- Dataset: Kuaishou Locallife 7 ngày (SFT 100,063 / CoT 59,113 / test 20,393) + public Kuaishou LLM-Rec (60,000/30,000/10,000). Backbone Qwen3.5-0.8B và OneLatent-9B.
- Industrial SID@64 (Số lần SID đích nằm trong top 64): +17,44% vs Think–OR và +9,33% vs No-Think–OR (cùng checkpoint, khác control token). Public K=64 vs strongest baseline: SID +12,21%, ID +19,10%; industrial +1,58%/+0,45%. 9B: SID@64 0,2008 vs 0,1857 (+8,13%).
- Inference (872 instances): explicit CoT 55,59 s / 15,68 QPS (query/giây) vs OneLatent 3,17 s / 274,29 QPS → 17,49× speedup, ngang UnCoT.
- Codebook retrieval Hit@L1: 0,354 (CoT) → 0,401 (OneLatent); Hit@L3 0,043→0,071.
- Adaptive CoT giảm 35% độ dài trung bình (100→65 normalized), complex-case semantic similarity ~0,92 (Qwen3-Emb-8B). Reconstruction cosine theo view: 0,8027 / 0,8043 / 0,7878 (2.000 samples).
- Online A/B (7 ngày, 3–10/9/2026, 5%/5% traffic, quảng cáo local-services Kuaishou): impressions +2,566%, ad spend +5,157%, est. revenue +9,6% (global posterior estimator); đã roll out toàn traffic.
- Table LLM-as-judge (GPT-5.5, 9 rubric dimension) partially extracted — chỉ dùng kết luận multi-view complementary.

## Actionable Insights
- Đo trước khi thêm CoT: Think vs No-Think cùng checkpoint mà Think chỉ 0,354→SID Hit@L1 và tốn 17× latency — đừng mặc định " reasoning hiển thị = tốt hơn"; benchmark cả 2 mode rồi mới chọn. Ví dụ: ranking content cho newsletter, chạy thử without-CoT baseline trước.
- Distill rationale thành latent slot khi serving: nếu cần reasoning chất lượng nhưng latency nhỏ, generate teacher rationale offline → align vào 3-4 latent token → serve small model. Ví dụ: gợi ý bài viết tiếp theo chạy Qwen3.5-0.8B thay vì model 235B reasoning live.
- Refresh cache theo behavior event, không call model trên request path: trigger rerank khi user click/view mới (prioritize user value cao), cache Redis + fallback stale → recent behavior ảnh hưởng ranking ngay mà GPU bounded. Ví dụ: precompute "top 10 content" mỗi user sau mỗi interaction.

## Assumptions & Limitations
- Phải có item corpus ổn định để build SID (Res-Kmeans) và teacher 235B để sinh MV-ACoT (offline, one-time cost lớn).
- Paper thừa nhận: cosine reconstruction là semantic association, KHÔNG chứng minh strict information bottleneck (bottleneck thông tin); all-parameter update nên gain không cô lập được lý luận nằm ở latent token hay distributed cả backbone; QPS gain một mình không đủ latency sync full traffic → bắt buộc async serving.
- [MY OWN] A/B test chỉ 1 scenario (quảng cáo local-services); chưa chứng minh transfer sang domain khác; 7 ngày industrial data không public; adaptive length chỉ prompt-guided, teacher không emit difficulty label nên calibration phụ thuộc prompt engineering.

## Metadata
- 2026, Kuaishou Technology (Jiang, Du, Yao et al.), cs.IR, https://arxiv.org/abs/2610.30675, citation count: [NOT FOUND] (paper quá mới)
