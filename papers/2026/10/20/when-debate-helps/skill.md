# Skill: when-debate-helps
Source: 2610.04686v1
Type: framework

## Khi nào dùng skill này
- Có hệ thống đa agent suy luận (reasoning) và muốn biết đäne có giúp vượt qua bình chọn đa số hay không.
- Cần tách biệt cung đề xuất (proposal supply) và phần đọc (readout) để chẩn đoán lý do đäne thất bại.
- Có tài nguyên chạy nhiều vòng đắn và verifier/LLM judge để gán bằng chứng xác thực.

## Tình huống KHÔNG nên dùng
- Giả định đắn luôn tốt hơn bình chọn đa số (đắn có thể hủy hoại trường hợp bình chọn đúng).
- Tác vụ không có giá trị đáp án so sánh được (open-ended không chấm điểm tự động).

## Input cần có
- Nhóm agent LLM nhỏ (K=4) thảo luận tác vụ suy luận (toán, Khoa học, đa môn).
- Cơ chế bình chọn đa số làm bước đọc đầu tiên.
- Verifier hoặc LLM judge để gán bằng chứng xác thực cho từng đề xuất ứng viên.
- Neural-thicket pool: các biến trọng số nhỏ từ model cơ sở (θm = θ0 + σmϵ(sm)).
- Mục tiêu coverage (có nhãn hoặc không nhãn) để chọn hội đồng agent bổ sung.

## Các bước thực hiện
1. Xác định tác vụ suy luận có giá trị đáp án so sánh được (AMC12, MATH500, GPQA, MMLU-Redux...).
2. Xây dựng neural-thicket pool: lấy mẫu các biến trọng số nhỏ xung quanh trọng số pretrained, mỗi biến là một agent đặc biệt gần kề.
3. Chọn hội đồng nhỏ K agent bằng coverage selection: AC-Greedy (có nhãn: chọn agent có đáp án đúng trên tập xây dựng) hoặc SC-Greedy (không nhãn: dùng hỗ trợ cụm đáp án), thay vì chọn agent cao điểm nhất.
4. Chạy đäne K agent, T vòng; mỗi agent đề xuất lý do + đáp án chuẩn hóa mỗi vòng; bình chọn đa số làm đọc ban đầu.
5. Tính recoverable headroom: tỉ lệ trường hợp hội đồng có đáp án đúng nhưng bình chọn đa số chọn sai.
6. Áp dụng LVD (đọc nhận thức chứng thực): verifier/LLM judge gán bằng chứng xác thực cụ thể theo đáp án cho từng đề xuất ứng viên trước khi sinh câu trả lời cuối; pseudo-count vector Wη,t phân bổ khối lượng xác thực cho đáp án đúng.
7. Phân tích gain phân rã: G = H·R + Pr(P=0,V=0)·I − Pr(V=1)·L (phục hồi headroom + chính xác mới − hư hại vote-correct).
8. Đánh giá độ mạnh qua nhiều seed ngẫu nhiên (matched stochastic evaluations).

## Output mong đợi
- Đäne vượt qua bình chọn đa số khi có headroom phục hồi và đọc nhận thức chứng thực; biết được đắn thất bại do cung đề xuất hay do phần đọc.

## Ví dụ áp dụng
- Hệ thống giải quyết toán đa agent: thay vì chỉ bình chọn đa số, chạy đắn 4 agent 5 vòng, rồi dùng LLM judge để xác thực từng đề xuất ứng viên trước khi đưa đáp án cuối; hội đồng được chọn bằng coverage (không chọn 4 agent cao điểm nhất).

## Gotchas
- Không giả định đắn luôn tốt hơn bình chọn — đắn có thể hủy hoại trường hợp bình chọn đúng hoặc loại bỏ phương án hữu ích.
- Không bỏ qua cung đề xuất: nếu không có đề xuất đúng nào được bề mặt, đọc tốt cũng không phục hồi được.
- Không chọn hội đồng agent chỉ theo độ chính xác cá nhân; cần bổ sung về phạm vi đề xuất.
- Can thiệp phải sớm: tương tác tạo thêm lợi ích ở các vòng đầu, cobertura đề xuất có thể sụt đổ ở vòng sau.

## Kiểm tra kỹ năng (self-check)
- Người không đọc paper gốc có follow được 8 bước trên không? [YES] — từng bước là action cụ thể.
- Bước nào mơ hồ nhất? Bước 6 (LVD với pseudo-count vector) cần triển khai verifier/LLM judge cụ thể.
- Input section có đủ không? [YES] — nhóm agent, bình chọn, verifier, neural-thicket pool, mục tiêu coverage.

## Dry run (tình huống giả)
- Tình huống: Doanh nghiệp có hệ thống 4 agent giải quyết bài toán GKS; muốn biết đắn có giúp không.
- Chạy skill: (1) Xác định tác vụ toán có đáp án chuẩn; (2) xây neural-thicket pool từ model cơ sở; (3) chọn 4 agent qua SC-Greedy (không nhãn); (4) chạy đắn 5 vòng, bình chọn đa số mỗi vòng; (5) tính recoverable headroom; (6) áp dụng LVD: LLM judge xác thực từng đề xuất trước khi đưa đáp án cuối; (7) phân tích rã gain; (8) đánh giá qua 5 seed; nếu đắn vượt bình chọn và headroom cao → triển khai.

## Verdict: [SKILL VALID]
