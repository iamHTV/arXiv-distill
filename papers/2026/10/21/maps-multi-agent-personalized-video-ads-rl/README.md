# [2610.25748v1] MAPS: A Multi-Agent Personalized Script-Driven Video Advertising System Enhanced by Reinforcement Learning

## Giá trị cốt lõi (1句话)
MAPS (hệ thống quảng cáo video cá nhân hóa đa agent dựa trên kịch bản, tăng cường bằng RL) có 4 agent phối hợp (Profile, Scripter, Director, Reflector) tạo quảng cáo video cá nhân hóa theo yêu cầu, cải thiện CTR +2.87%, CVR +2.74%, ARPU +9.85% so với cơ sở generative trong A/B test thực tế tại Kuaishou.

## Problem
Prior work quảng cáo video cá nhân hóa dùng paradigm retrieval-based (tạo trước creative pool, sau đó truy xuất), giới hạn độ chi tiết của personalization và gây chênh lệch hiệu suất giữa các nhóm user; phản hồi từ user chỉ có thể làm nên chu kỳ sản xuất tiếp theo, không tối ưu hóa creative đang triển khai theo thời gian thực.

## Contribution
1. Đề xuất MAPS, hệ thống đa agent 4 thành phần (Profile, Scripter, Director, Reflector) biến quảng cáo video cá nhân hóa từ truy xuất tĩnh trên kho creative rời rạc thành tối ưu hóa sinh tạo không ngừng trong không gian creative liên tục.
2. Xây dựng khung RL (dựa trên GRPO) với hàm thưởng đa chiều cho Scripter Agent, đồng thời định hướng script phù hợp với sở thích nội dung của user và thông tin sản phẩm mục tiêu.
3. Cơ chế tiến hóa creative kín khép qua phản hồi trực tuyến sau khi triển khai: Reflector Agent gán tín hiệu tương tác của user về nguyên nhân cấp profile và cấp script, định tuyến sửa chữa tối thiểu trở lại Profile và Scripter Agent.
4. Thực hiện thí nghiệm ngoại tuyến trên hai tiêu chuẩn (PCG-Bench, PCI-Bench) và thử nghiệm A/B trực tuyến trong hệ thống quảng cáo Kuaishou, đạt cải thiện CTR/CVR/ARPU đáng kể.

## Method
MAPS gồm 4 agent phối hợp: (1) Profile Agent (Qwen3-VL-32B-Instruct) xây dựng profile user có cấu trúc từ dữ liệu tương tác lịch sử và ngữ cảnh thời gian thực, trên 4 chiều (mong quan điểm, phong cách trình bày, nhu cầu ngầm, xu hướng đưa ra quyết định), liên tục tinh chỉnh khi quan sát hành vi mới; (2) Scripter Agent (Qwen3-VL-8B-Instruct) tạo kịch bản quảng cáo video cá nhân hóa được điều kiện bởi profile user và thông tin sản phẩm,经过 SFT (LoRA rank 32, LR 1.0e-5, batch 4, 20 epochs) sau đó RL (GRPO, KL 0.04, LR 1.0e-6, batch 4, 5000 bước) trên 8 H100; (3) Director Agent (Kling-Omni) chuyển kịch bản thành video quảng cáo hoàn chỉnh với các tài sản visual của sản phẩm; (4) Reflector Agent (Qwen3-VL-32B-Instruct) gán tín hiệu tương tác trực tuyến về nguyên nhân cấp profile và cấp script, định tuyến sửa chữa tối thiểu. Hàm thưởng tổng hợp: Rtotal = 0.3·Rstruct + 0.4·Rpers + 0.3·Rprod, trong đó Rstruct kiểm tra định dạng/độ đầy đủ/ nhất quán nhân vật cảnh/tính vật lý hợp lý, Rpers dùng LLM-as-a-Judge đánh giá sự phù hợp phong cách trình bày và sở thích nội dung (0-10), Rprod dùng LLM-as-a-Judge đánh giá độ chính xác sản phẩm, yếu tố thương hiệu, tính nhất quán事实 (0-10). Qwen3-VL-32B-Instruct làm thẩm phán.

## KNOWLEDGE — Số liệu & khái niệm
- 4 agent: Profile (Qwen3-VL-32B-Instruct), Scripter (Qwen3-VL-8B-Instruct), Director (Kling-Omni), Reflector (Qwen3-VL-32B-Instruct)
- Huấn luyện Scripter: SFT LoRA rank 32, AdamW LR 1.0e-5, batch 4, max seq 8192, 20 epochs; RL GRPO KL 0.04, AdamW LR 1.0e-6, batch 4, 5000 bước; 8 NVIDIA H100 GPUs
- Hàm thưởng: Rtotal = 0.3·Rstruct + 0.4·Rpers + 0.3·Rprod; Rstruct: Format Compliance, Script Completeness, Scene & Character Consistency, Physical Rationality; Rpers: LLM-as-a-Judge trên phong cách trình bày + sở thích nội dung (4 aspect tone/lighting/texture/artistic, 6 aspect subject/scene/information angle/motivational appeal); Rprod: LLM-as-a-Judge trên product identity + brand elements + selling points factual consistency (0-10)
- GRPO group sampling: K script ứng dụng, Ưu đãi chuẩn hóa Ak = (Rk − R̄)/(σR + ε), KL penalty ngăn lệch lớn từ SFT
- Offline (PCG-Bench, PCI-Bench): 50 user, 5 sản phẩm/từng user → 250 cặp user-sản phẩm, thư viện 18 sản phẩm; MAPS đạt tốt nhất mọi chỉ số trên cả 2 tiêu chuẩn; Personalization 8.85, Product Alignment 9.78, Diversity 7.30; migliorie personalization +1.25 điểm và product alignment +1.04 điểm so với biến thể không SFT/RL
- Online A/B (Kuaishou): so với DLRM → CTR +4.88%, CVR +4.01%, ARPU +12.89%; so với GRM → CTR +2.87%, CVR +2.74%, ARPU +9.85%

## INSIGHT — Cơ chế & tại sao
[Chuyển từ retrieval sang sinh tạo creative trên yêu cầu] VÌ [kho creative cố định không thể kịp với sở thích user thay đổi nhanh, trong khi MAPS tạo creative mới mỗi lần ấn tượng, phù hợp từng user và sản phẩm]. Điều này nghĩa là [giá trị thương mại lớn hơn đến từ việc tạo native creative phù hợp từng user, không chỉ khớp tốt hơn].
[Hàm thưởng đa chiều tránh trade-off giữa personalization và product alignment] VÌ [Rpers và Rprod có trọng số bằng nhau (0.4 và 0.3), Scripter được hướng dẫn đồng thời tối ưu cả hai thay vì đánh đổi một cho kia]. Điều này nghĩa là [multi-agent collaboration cho phép tối ưu hóa toàn cầu qua các mục tiêu cạnh tranh].
[Reflector Agent tạo vòng kín khép creative evolution] VÌ [phản hồi trực tuyến được gán về nguyên nhân cấp profile hoặc cấp script, định tuyến sửa chữa tối thiểu thay vì sinh lại toàn bộ creative]. Điều này nghĩa là [sự thích ứng liên tục không cần chạy lại toàn bộ pipeline từ đầu].

## IDEA — Áp dụng được gì
1. Áp dụng [khung multi-agent 4 thành phần] vào [xây dựng hệ thống tạo creative quảng cáo video cá nhân hóa]: bước đầu là triển khai Profile Agent để trích xuất profile user từ lịch sử tương tác, sau đó thêm Scripter Agent tạo kịch bản theo profile và sản phẩm.
2. Áp dụng [GRPO với hàm thưởng đa chiều] vào [điều hướng LLM tạo nội dung theo nhiều mục tiêu]: bước đầu là thiết lập 3 thành phần thưởng (cấu trúc, personalization, product alignment) với trọng số 0.3/0.4/0.3, dùng LLM-as-a-Judge để chấm điểm.
3. Áp dụng [Reflector Agent phản hồi trực tuyến] vào [triển khai hệ thống creative thích ứng liên tục]: bước đầu là thu thập tín hiệu tương tác (play duration, like, comment, mua hàng) sau mỗi ấn tượng, gán về nguyên nhân cấp profile/script, định tuyến sửa chữa tối thiểu.

## WISDOM — Nguyên tắc tổng quát
1. Nguyên tắc: Tạo creative trên yêu cầu (on-demand generation) mang giá trị thương mại cao hơn việc khớp creative từ kho cố định, vì nó mở ra không gian creative liên tục thay vì giới hạn trong inventory tĩnh. Áp dụng khi: xây dựng hệ thống quảng cáo hoặc nội dung cá nhân hóa với inventory sản phẩm lớn. Không áp dụng khi: chi phí sinh tạo cao quá so với lợi ích personalization.
2. Nguyên tắc: Multi-agent với vòng phản hồi kín khép (profile → script → creative → feedback → profile) vượt qua hệ thống đơn agent vì mỗi agent chuyên biệt một khía cạnh và phản hồi đóng lặp lại cải thiện liên tục. Áp dụng khi: cần hệ thống thích ứng với sở thích user thay đổi theo thời gian. Không áp dụng khi: tác vụ đơn giản, không cần personalization sâu.

## Assumptions & Limitations
- Điều kiện phải đúng: có dữ liệu tương tác lịch sử của user, có tài sản visual sản phẩm (hình ảnh, logo), có tài nguyên GPU (8 H100), có mô hình video generation (Kling-Omni) và MLLM (Qwen3-VL).
- Limitation paper thừa nhận: thí nghiệm online chỉ trong một kịch bản cụ thể của hệ thống Kuaishou; chưa khám phá mô hình phản hồi trực tuyến chi tiết hơn và tiến hóa creative dài hạn trong kịch bản lớn hơn.
- Limitation paper KHÔNG nói: chi phí inference thực tế so với retrieval-based; thời gian sinh tạo creative mỗi ấn tượng; tính mở rộng khi số user và sản phẩm tăng lớn; không có so sánh với các hệ thống multi-agent khác ngoài DLRM và GRM.

## Metadata
- Năm: 2026
- Tác giả: Zhongyu Wang, Chen Zuo, Qingxuan Sun, Jiayang Qiao, Qiuhao Qian, Songyan Cui, Guocheng Chen (Beihang University, Kuaishou Technology)
- Category arXiv: cs.IR
- Link PDF: https://arxiv.org/pdf/2610.25748
- arXiv ID: 2610.25748v1
- Nhãn: [applied]
- Citation count: [không tìm được]