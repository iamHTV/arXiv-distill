# arXiv scan 2026-10-16

_Nội dung này giống hệt đã gửi qua Telegram._

arXiv scan 2026-10-16
Quét 6043 → lọc 5506 bài → chấm 60 | 🔥57 ⏳3 ❓0

🔥 DISTILL NGAY (57) — máy tự làm

91 · Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows — http://arxiv.org/abs/2610.21411v1
   📄 Jev-LiteMAS thay routing/review trong multi-agent bằng lightweight decision model, giảm 12.7-54.6% generative tokens mà giữ accuracy trong 1.34 điểm.
   📝 Đa agent rất phù hợp content đa kênh, insight tách decision khỏi generation tiết kiệm chi phí trực tiếp, experiment 4 benchmark thật, dễ áp dụng workflow.
   2610.21411v1

90 · AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows — http://arxiv.org/abs/2609.22951v1
   📄 AgentRouter là classifier 12M tham số định tuyến từng bước agent đến đúng tier model, giảm 72% chi phí mà giữ 97.3% chất lượng so với dùng toàn frontier model.
   📝 Cực kỳ thực tiễn cho solopreneur: tiết kiệm 72% inference cost cho workflow agentic, có benchmark rõ ràng và insight hành động là đừng dùng model lớn cho mọi bư…
   2609.22951v1

90 · StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Ag… — http://arxiv.org/abs/2610.10942v1
   📄 StoreBench tạo environment thương mại điện tử live để đánh giá agent vận hành cửa hàng: 7 LLM frontier đều thua policy heuristic (tốt nhất 49% vs 97%), người thật vẫn dẫn đầu.
   📝 Cực kỳ sát agent + business với benchmark production-grade, insight hành động rõ: agent chưa thay thế được judgment kinh tế, nên dùng làm trợ thủ không phải tự …
   2610.10942v1

90 · Fabrication After Tool Failure: Tool-Augmented Agents Assert Values Their Tools Did Not Re… — http://arxiv.org/abs/2609.14758v1
   📄 Benchmark 1.024 mục cho thấy 14-24% agent framework (CrewAI...) bịa giá trị khi tool fail mà không báo trạng thái, và một câu yêu cầu emit retrieval\status OK/FAILED giảm mạnh fabrication.
   📝 Rất liên quan khi dùng agent cho content/business: phát hiện rủi ro hallucination sau tool failure + fix chỉ bằng 1 câu prompt, insight hành động tức thì, giá t…
   2609.14758v1

87 · Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Work… — http://arxiv.org/abs/2610.03010v1
   📄 Nghiên cứu so sánh hệ thống agentic LLM trên 5 task dev với 6 model, 2 prompt strategy, 3 nền tảng, cho thấy multi-agent tốn 6.36x năng lượng và 6.07x thời gian nhưng gain accuracy hạn chế.
   📝 Insight vàng cho solopreneur: đừng mặc định multi-agent, cấu hình nhẹ thường dominates Pareto front — trực tiếp tiết kiệm tiền và thời gian.
   2610.03010v1

87 · Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Age… — http://arxiv.org/abs/2609.26760v2
   📄 Học chính 'harness' agent từ feedback (failure-guided), biến control thành code tái sử dụng thay vì để LLM xử lý lặp lại, cắt 76–92% LLM calls và 74–98% inference cost mà vẫn giữ success ở model nhỏ 4B trên BrowseComp-Pl…
   📝 Insight cực hành động cho solopreneur: harness tích luỹ giúp tiết kiệm chi phí agent hàng chục % và chạy tốt model giá rẻ — đúng pain người đa kênh, experiment …
   2609.26760v2

86 · Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation — http://arxiv.org/abs/2609.38660v2
   📄 SMART là hệ multi-agent tự-tiến hóa dịch phụ đề dài: memory cấp series, dynamic router + Mixture-of-Agents, judge-refiner cập nhật prompt không retrain, thắng tất cả 15 hướng Subtitle Arena, giảm penalty 6.9%.
   📝 Xai cho content creator đa kênh: method test-time evolution + judge-refiner reuse được ngay, benchmark Subtitle Arena quy mô lớn (14 thể loại, 15 locale) rất th…
   2609.38660v2

86 · CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product Ads Retriev… — http://arxiv.org/abs/2608.30255v1
   📄 CAMIE dùng LLM/MLLM backbone fine-tune trên cặp item cùng tương tác để làm embedding multimodal cho quảng cáo DPA của Snap, cải thiện CTR/CVR thực tế.
   📝 Trúng ngành marketing/ads: deployed production, lift CTR +18.9% / CVR +13.1% so text control — bài học co-engagement tuning và multimodal embedding rất actionab…
   2608.30255v1

86 · CEO Arena: Evaluating Long-Horizon Multi-Agent Decision-Making in Competitive Markets — http://arxiv.org/abs/2609.34821v1
   📄 CEO Arena benchmark 8 CEO-agent LLM cạnh tranh 500 ngày mô phỏng trên giá, marketing, R&D, cho thấy多数 agent lỗ và private gain có thể đi kèm market loss.
   📝 Trực tiếp về multi-agent decision-making trong kinh doanh (pricing/marketing/R&D), experiment quy mô lớn, insight về chiến lược cạnh tranh rất giá trị cho conte…
   2609.34821v1

86 · Harness Engineering in LLM Tool Use via Agent-Native Reusable Tool Primitives — http://arxiv.org/abs/2609.01736v1
   📄 Giới thiệu Tool Primitives + ToolFace (kho 25.519 hàm) và framework HEART (Planner-Router-Verifier) để LLM gọi tool bằng ngôn ngữ tự nhiên, vượt benchmark trên 5 bộ test với tool calling đa bước.
   📝 Cực kỳ liên quan tool-use/agent, experiment mạnh và pattern Planner-Router-Verifier áp dụng trực tiếp cho solopreneur xây dựng pipeline AI/content automation.
   2609.01736v1

85 · Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents — http://arxiv.org/abs/2609.25991v1
   📄 Đề xuất tổ chức knowledge base theo 3 lớp (SKILL.md, index.md, frontmatter YAML) để LLM agent tự quyết định có truy vấn-gì-khi-nào, kèm pipeline chuyển PDF/Word/web thành cấu trúc này, beating RAG trên WixQA (0.889/0.816…
   📝 Cực kỳ actionable cho ai xây content-KB/agent: cấu trúc file cụ thể + pipeline chuyển đổi thật + benchmark WixQA rõ ràng; điểm trừ là đánh giá còn preliminary.
   2609.25991v1

85 · Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks — http://arxiv.org/abs/2610.05750v1
   📄 Agentic retrieval (ReAct loop + retriever) cải thiện nDCG@10 +8.7 điểm và generalize tốt trên ViDoRe v3/BRIGHT, nhưng tốn 107 giây và 764K tokens/query so với 0.67 giây retrieval thường.
   📝 Cực kỳ actionable cho content research: định lượng rõ cost/performance tradeoff, biết khi nào nên bật agentic search và khi nào không.
   2610.05750v1

85 · Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows — http://arxiv.org/abs/2609.32917v1
   📄 Planner-as-Router gán tier model (small/mid/frontier) ngay khi lập kế hoạch sub-task, giảm 44% cost so với all-frontier trên EntBench 54 task enterprise.
   📝 Rất thực tiễn cho ai chạy agent: benchmark thật (1157 evals, SQL/Mongo live), insight chọn model theo subtask tiết kiệm API cost rõ ràng, áp dụng ngay được vào …
   2609.32917v1

85 · A Hybrid Agentic AI Framework for Intelligent Supply Chain Analytics — http://arxiv.org/abs/2609.13561v1
   📄 Hệ thống agentic nhiều agent (coordinator + specialist) cho analytics chuỗi cung ứng, đạt 90% độ chính xác và giảm ~4x token so với single-agent.
   📝 Rất thực tiễn (đánh giá thật, case study), mẫu thiết kế modular agent + tiết kiệm chi phí là insight áp dụng trực tiếp cho solopreneur làm product AI.
   2609.13561v1

85 · Re-ranking and Late Interaction Drive Retrieval Quality: A Controlled Comparison of RAG St… — http://arxiv.org/abs/2609.38473v1
   📄 So sánh có kiểm soát 6 chiến lược RAG (top-k, rephrase, rerank, RRF, agentic tool-call, ColBERTv2) trên 463K paper arXiv với cùng generator và dataset 19.484 câu hỏi.
   📝 RAG là cốt lõi cho content AI, experiment quy mô lớn thật, insight chọn chiến lược retrieval áp dụng ngay được cho hệ thống knowledge của solopreneur.
   2609.38473v1
…và 42 bài nữa (xem scans/2026-10-16.json)

⏳ LÀM SAU (3) — máy tự làm sau khi xong nhóm trên

74 · A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems — http://arxiv.org/abs/2608.05791v1
   📄 TIPEX mô hình song song hóa inference multi-agent thành Replica và Structural parallelism, cho thấy song song cải thiện accuracy và giảm latency nhưng đổi lại tốn token.
   📝 Có benchmark GAIA và insight về trade-off latency/token, hữu ích khi thiết kế pipeline nhưng hơi học thuật.
   2608.05791v1

74 · Learning to Steer LLM Agents and Multi-Agent Systems — http://arxiv.org/abs/2610.22316v1
   📄 Paper đề xuất steering agent giám sát goal drift và can thiệp kịp thời cho agent/multi-agent, huấn luyện bằng RL kết hợp ranking + GRPO trên hai đường can thiệp nhanh/chậm.
   📝 Cực kỳ liên quan multi-agent và tool-use dài hạn, generalizes cross-domain, nhưng abstract thiếu số liệu cụ thể và business angle ở mức trung bình.
   2610.22316v1

74 · Robust Hierarchical Structures for Agentic Document Analysis — http://arxiv.org/abs/2609.33322v1
   📄 Đề xuất SHED, workflow 2 giai đoạn trích xuất cấu trúc phân cấp tài liệu PDF/Word để agent chỉ xử lý section liên quan, cải thiện F1 13-68%.
   📝 Insight hành động cụ thể (giảm cost agent nhờ cấu trúc tài liệu) kèm experiment thực tế, hữu ích cho ai làm product xử lý tài liệu bằng LLM.
   2609.33322v1
