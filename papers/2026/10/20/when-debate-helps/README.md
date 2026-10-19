# [2610.04686v1] When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning

## Giá trị cốt lõi (1 câu)
Đäne đa agent giúp vượt qua bình chọn đa số chỉ khi cả hai điều kiện cùng xảy ra: đề xuất đúng được bề mặt (proposal supply tạo headroom có thể phục hồi) VÀ phần đọc (readout) nhận diện đề xuất đúng đó bằng bằng chứng xác thực (LVD — Latent Verification Debate).

## Problem
Prior work chưa giải quyết việc đäne đa agent thường thất bại so với bình chọn đa số đơn giản hoặc tự nhất quán (self-consistency), vì lý do chưa được tách biệt: có phải do đề xuất đúng không được bề mặt, hay do phần đọc không nhận diện đề xuất đúng khi bình chọn bỏ lỡ.

## Contribution
- Giới thiệu khung supply-readout: đäne cần (1) cung đề xuất bề mặt ít nhất một câu trả lời đúng, (2) phần đọc chọn đề xuất đúng chứ không chỉ đếm số agent lặp lại mỗi đề xuất.
- Formalize recoverable headroom: trường hợp đề xuất bước đầu có câu đúng nhưng bình chọn đa số chọn câu sai; phân tích chuẩn xác tách biệt recovered headroom, newly-correct cases, và damage đến vote-correct cases.
- Phát triển LVD (Latent Verification Debate): mô hình đọc nhận thức chứng thực, trong đó các đề xuất ứng viên nhận bằng chứng xác thực cụ thể theo câu trả lời trước khi sinh câu cuối; controlled fixed-proposal interventions ước lượng hiệu ứng latent bằng đơn vị hỗ trợ đồng đẳng tương đương.
- Xây dựng hội đồng agent từ neural-thicket agents bằng mục tiêu coverage có nhãn (AC-Greedy) và không nhãn (SC-Greedy), chọn agent có hành vi đề xuất bổ sung.

## Method
Khung supply-readout. Vòng t = 0 là đề xuất độc lập (initial proposals), vòng t ≥ 1 là cập nhật đäne. Mỗi agent sản xuất lý do và giá trị câu trả lời chuẩn hóa. Bình chọn đa số chọn câu trả lời phổ biến nhất. Chẩn đoán proposal-hit hỏi xem câu trả lời đúng đã được bề mặt chưa (không phải là đọc có sẵn). Recoverable headroom H(S) = Pr(P=1, V=0): tỉ lệ trường hợp hội đồng có câu đúng nhưng bình chọn bỏ lỡ. Phân tích chuẩn xác: Gη(S) = E[Dη − V] = H(S)·Rη(S) + Pr(P=0,V=0)·Iη(S) − Pr(V=1)·Lη(S), trong đó R = tỉ lệ phục hồi câu đúng bị bỏ lỡ, I = tỉ lệ chính xác mới xuất hiện sau bước đề xuất, L = tỉ lệ hư hại đến trường hợp bình chọn đúng. LVD tăng cường đọc chỉ đếm đề xuất bằng vector chuẩn triệu chứng xác thực Wη,t: pLVD,η(y=k|x,Ft,W) ∝ κq0θ(k|x) + C(k)t + W(k)η,t. Đäne giúp khi chứng thực xác thực phân bổ khối lượng hơn cho câu đúng so với đọc chỉ đếm đề xuất. Xây dựng hội đồng: neural-thicket agents (biến trọng số nhỏ xung quanh trọng số pretrained θm = θ0 + σmϵ(sm)); chọn hội đồng nhỏ K agent có phạm vi đề xuất bổ sung qua AC-Greedy (có nhãn: ψAC = 1{đáp án agent = đáp án đúng}) hoặc SC-Greedy (không nhãn: dùng hỗ trợ cụm đáp án). Đánh giá: Qwen3-4B-Instruct và OLMo-3-7B-Instruct, K=4 agent, T=5 vòng, ngân sách tính toán thống nhất (vote20 cho bình chọn, R3 cho đäne).

## KNOWLEDGE — Số liệu & khái niệm
- Đäne đa agent thường thất bại so với bình chọn đa số/tự nhất quán; đắn tương xứng trung lập về sự thật (symmetric truth-agnostic) không tạo sự drift dương dự kiến về độ chính xác (martingale null).
- Recoverable headroom: đề xuất bước đầu có câu đúng nhưng bình chọn bỏ lỡ.
- LVD: đọc nhận thức chứng thực, tạo drift phi-null chỉ khi bằng chứng xác thực phân bổ nhiều khối lượng hơn cho câu đúng so với đọc chỉ đếm đề xuất.
- Bảng 1 (Qwen3-4B): SC@20 91.20, Vanilla Debate 92.69, SC-Greedy Debate 92.29; Neural Thicket Vote 90.93, Top-4 Debate 92.15, AC-Greedy Debate 92.29.
- Bảng 1 (OLMo3-7B): SC@20 87.01, Vanilla Debate 86.33, SC-Greedy Debate 84.03; Neural Thicket Vote 86.87, Top-4 Debate 85.93, AC-Greedy Debate 85.25.
- Độ mạnh ngẫu nhiên (5seed): SC-Greedy +1.14 pts, AC-Greedy +1.46 pts trên Qwen3-4B; +0.96, +2.01 trên OLMo3-7B so với Vanilla Debate.
- Bảng 2 (chuyển miền AMC12 → MMLU-Redux): Qwen3-4B SC-Greedy Final 76.33 vs Init Vote 72.33 (+4.00 lift); OLMo SC-Greedy Final 59.67 vs Init Vote 55.33.
- Probe kiểm soát cố định đề xuất: hỗ trợ đúng cải thiện độ chính xác từ 0.325 lên 0.655 tại d=3 (trung bình 4 kết hợp backbone–tập dữ liệu); ảnh hưởng trace gốc dương trong 4 kết hợp; khoảng cách T−F (hỗ trợ đúng trừ sai, trích xuất đáp án) dương trong mọi kết hợp.
- Động lực: R0 76.09% → R2 78.34% → R3 78.52% (lễ finalizer ngay lập tức không giải thích được sự tăng); tương tác tạo thêm lợi ích ngoài việc áp dụng finalizer cùng một vào đề xuất ban đầu.
- Mã nguồn: github.com/Wang-ML-Lab/when-debate-helps
- Danh mục arXiv: cs.AI

## INSIGHT — Cơ chế & tại sao
[Đäne thường thua bình chọn đa số] VÌ [hoặc đề xuất đúng không được bề mặt (không có headroom), hoặc phần đọc không nhận diện câu đúng khi bình chọn bỏ lỡ; chỉ có một trong hai không đủ]. Điều này nghĩa là [đäne cần cả cung đề xuất đủ tốt lẫn đọc nhận thức chứng thực để vượt qua bình chọn].
[Headroom có thể phục hồi tạo cơ hội cho đọc] VÌ [khi đề xuất đúng có sẵn nhưng bình chọn bỏ lỡ, đọc có thể recuperar câu đúng nếu gán bằng chứng xác thực cao hơn cho đề xuất đúng]. Điều này nghĩa là [đäne giúp khi có headroom phục hồi và đọc có thể chuyển headroom thành độ chính xác cuối cùng].
[Hội đồng agent được chọn bằng coverage tạo nhiều đề xuất đúng bổ sung] VÌ [chọn agent có phạm vi đề xuất bổ sung thay vì xếp hạng chỉ theo độ chính xác cá nhân tạo ra nhiều câu trả lời đúng khác nhau, ít trùng lặp]. Điều này nghĩa là [đồng chất bổ sung hơn đồng chất trùng lặp].

## IDEA — Áp dụng được gì
Áp dụng LVD vào hệ thống đa agent doanh nghiệp: bước đầu là dùng bình chọn đa số làm bước đầu, rồi dùng verifier/LLM judge để gán bằng chứng xác thực cho từng đề xuất ứng viên trước khi sinh câu trả lời cuối.
Dùng neural thicket + coverage selection để xây dựng hội đồng agent bổ sung: bước đầu là lấy mẫu các biến trọng số nhỏ từ model cơ sở, chọn agent có phạm vi đề xuất bổ sung thay vì chọn agent cao điểm nhất.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Đäne giúp khi cung đề xuất bề mặt câu trả lời đúng (tạo headroom có thể phục hồi) VÀ đọc có thể nhận diện câu đúng khi bình chọn bỏ lỡ; một trong hai không đủ. Đäne không phải lúc nào cũng tốt hơn bình chọn — có thể hủy hoại các trường hợp bình chọn đúng hoặc loại bỏ các phương án hữu ích.

## Assumptions & Limitations
- Điều kiện đúng: tác vụ suy luận có giá trị đáp án so sánh được, hội đồng agent nhỏ (K=4), nhiều vòng đäne (T=5).
- Limitation paper thừa nhận: đắn không phải lúc nào cũng tốt hơn bình chọn; chuyển đổi headroom phụ thuộc vào tác vụ và backbone; chi phí suy luận là yếu tố thực tế; kết quả trên hai backbone (Qwen3-4B, OLMo3-7B) không đảm bảo tất cả model lớn hơn.
- Limitation paper KHÔNG nói: chi phí vận hành chạy nhiều vòng đäne tại quy mô lớn; tính ổn định qua nhiều lần chạy ngẫu nhiên nhiều hơn 5 seed; tác động lên độ trễ khi chạy verifier/LLM judge cho mỗi đề xuất ứng viên.

## Metadata
- Năm: 2026
- Tác giả: Zihao Zhao, Tunyu Zhang, Haizhou Shi, Yusong Zhao, Xinxi Zhang, Hao Wang (University of Illinois Urbana-Champaign, Rutgers University)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.04686v1
- arXiv ID: 2610.04686v1
- Nhãn: [applied]
- Skill: when-debate-helps | Test: [SKILL VALID]
