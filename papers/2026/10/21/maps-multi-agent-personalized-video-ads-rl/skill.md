# Skill: maps-multi-agent-video-ad-pipeline

Source: 2610.25748v1
Type: framework / workflow

## Khi nào dùng skill này
- Khi cần xây dựng hệ thống tạo quảng cáo video cá nhân hóa cho từng user, không phụ thuộc vào kho creative đã có sẵn.
- Khi muốn áp dụng multi-agent để phân chia công việc: phân tích user, viết kịch bản, sản xuất video, phản hồi chỉnh sửa.
- Khi cần hệ thống thích ứng liên tục với sở thích user thay đổi qua thời gian, qua vòng phản hồi trực tuyến.

## Tình huống KHÔNG nên dùng
- Khi chi phí sinh tạo video mỗi ấn tượng quá cao so với lợi ích personalization.
- Khi không có dữ liệu tương tác lịch sử của user hoặc tài sản visual sản phẩm.
- Khi tác vụ đơn giản, không cần personalization sâu.

## Input cần có
- Dữ liệu tương tác lịch sử của user (xem video, thời gian phát, like, bình luận, sưu tóm, chia sẻ, theo dõi).
- Tài sản visual sản phẩm (hình ảnh, logo, thông tin thương hiệu).
- Mô hình MLLM (Qwen3-VL-32B-Instruct hoặc tương đương) cho Profile và Reflector Agent.
- Mô hình ngôn ngữ-viết (Qwen3-VL-8B-Instruct hoặc tương đương) cho Scripter Agent.
- Mô hình sinh video (Kling-Omni hoặc tương đương) cho Director Agent.
- Tài nguyên GPU (khuyến nghị 8 H100 hoặc tương đương).

## Các bước thực hiện
1. Triển khai Profile Agent: trích xuất profile user có cấu trúc trên 4 chiều (mong quan điểm, phong cách trình bày, nhu cầu ngầm, xu hướng đưa ra quyết định) từ dữ liệu tương tác và ngữ cảnh thời gian thực; liên tục tinh chỉnh khi quan sát hành vi mới.
2. Huấn luyện Scripter Agent: SFT trên corpus kịch bản quảng cáo cá nhân hóa do con người viết (LoRA rank 32, AdamW LR 1.0e-5, batch 4, max seq 8192, 20 epochs); sau đó RL bằng GRPO (KL 0.04, AdamW LR 1.0e-6, batch 4, 5000 bước).
3. Thiết lập hàm thưởng đa chiều: Rtotal = 0.3·Rstruct + 0.4·Rpers + 0.3·Rprod; Rstruct kiểm tra định dạng/độ đầy đủ/nhất quán nhân vật cảnh/tính vật lý hợp lý; Rpers dùng LLM-as-a-Judge đánh giá phong cách trình bày + sở thích nội dung (0-10); Rprod dùng LLM-as-a-Judge đánh giá chính xác sản phẩm/yếu tố thương hiệu/tính nhất quán factual (0-10).
4. Triển khai Director Agent: nhận kịch bản từ Scripter, kết hợp với tài sản visual sản phẩm, sinh video quảng cáo hoàn chỉnh.
5. Triển khai Reflector Agent: thu thập tín hiệu tương tác trực tuyến (thời gian phát, like, bình luận, mua hàng) sau mỗi ấn tượng; gán về nguyên nhân cấp profile hoặc cấp script; định tuyến sửa chữa tối thiểu trở lại Profile và Scripter Agent.
6. Chạy vòng lặp kín khép: Profile → Scripter → Director → creative → Reflector → phản hồi → Profile/Scripter, lặp lại qua các ấn tượng liên tiếp.

## Output mong đợi
- Hệ thống tạo quảng cáo video cá nhân hóa theo yêu cầu cho từng user.
- Báo cáo đánh giá: CTR, CVR, ARPU, personalization score, product alignment score, diversity score.
- Quyết định triển khai: triển khai rộng, giữ nguyên, hoặc điều chỉnh hàm thưởng/agent.

## Ví dụ áp dụng
Một thương hiệu mỹ phẩm muốn chạy quảng cáo video trên Kuaishou/TikTok, mỗi user thấy video quảng cáo khác nhau phù hợp với sở thích và loại da của họ. Hệ thống MAPS phân tích profile user (mong quan điểm chăm sóc da, phong cách vídeo thích hợp), Scripter viết kịch bản quảng cáo sản phẩm dưỡng da, Director sinh video với hình ảnh sản phẩm thực tế, Reflector thu thập tương tác sau mỗi lần phát và điều chỉnh kịch bản cho lần tiếp theo. Kết quả mong đợi: CTR tăng 2–5%, CVR tăng 2–4%, ARPU tăng 9–13%.

## Gotchas
- Không để từ tiếng Anh không giải thích: multi-agent (đa agent), script-driven (dựa trên kịch bản), reinforcement learning (học học khoá chính)/RL, GRPO (Group Relative Policy Optimization — tối ưu hóa chính sách tương đối nhóm), LoRA (Low-Rank Adaptation — thích ứng cấp thấp), KL divergence (sự khác biệt Kullback-Leibler), LLM-as-a-Judge (LLM làm thẩm phán), on-demand generation (sinh tạo theo yêu cầu), closed-loop (vòng kín khép), retrieval-based (dựa trên truy xuất), generative (sinh tạo), ARPU (average revenue per user — doanh thu trung bình mỗi user), CTR (click-through rate — tỷ lệ nhấp chuột), CVR (conversion rate — tỷ lệ chuyển đổi), user profile (hồ sơ người dùng), implicit needs (nhu cầu ngầm), decision-making tendencies (xu hướng đưa ra quyết định), presentation styles (phong cách trình bày), topical interests (mong quan điểm chủ đề), physical rationality (tính vật lý hợp lý), scene and character consistency (nhất quán cảnh và nhân vật), format compliance (tuân thủ định dạng), script completeness (độ đầy đủ kịch bản), product identity accuracy (độ chính xác danh tính sản phẩm), brand elements (yếu tố thương hiệu), selling points (điểm bán hàng), factual consistency (tính nhất quán factual), inference (suy luận), on-premise (triển khai tại chỗ).
- Hàm thưởng cần cân bằng: nếu Rpers quá nhẹ so với Rprod, script sẽ đúng sản phẩm nhưng không cá nhân hóa; nếu ngược lại, script cá nhân hóa nhưng sai thông tin sản phẩm.
- GRPO cần mẫu K ứng dụng mỗi input, chi phí tính toán cao hơn DPO truyền thống.
- Vòng phản hồi trực tuyến cần độ trễ thấp; sửa chữa tối thiểu tránh sinh lại toàn bộ creative.
- Chỉ có kết quả online trong một kịch bản cụ thể tại Kuaishou, không thể generalize trực tiếp sang mọi nền tảng.
- Không có dữ liệu chi phí inference thực tế so với retrieval-based.