# Skill: forty-shades-of-blue-moda
Source: 2609.14896v1
Type: framework

## Khi nào dùng skill này
- Cần tạo nhiều phản hồi khác nhau nhưng vẫn chất lượng cao từ cùng một prompt (ý tưởng content, giả thuyết nghiên cứu, viết sáng tạo).
- Muốn bảo toàn sự đa dạng đầu ra khi hậu huấn luyện LLM, tránh mode collapse.
- Có sẵn policy tham chiếu đóng băng để tính ngưỡng chất lượng tùy prompt.

## Tình huống KHÔNG nên dùng
- Truy vấn fact có một đáp án duy nhất (ví dụ ngày sinh Einstein) → dùng mode chuẩn, không cần đa dạng.
- Không có tài nguyên GPU để huấn luyện GRPO với nhiều role-response pairs mỗi prompt.

## Input cần có
- Model ngôn ngữ cơ sở (ví dụ Qwen3-8B-Instruct).
- Policy tham chiếu đóng băng (frozen reference policy) để tính điểm chất lượng tham chiếu.
- Bộ mã định danh vai trò abstract (numbered role identifiers).
- Hệ thống huấn luyện GRPO (verl + vLLM + FSDP hoặc tương đương).
- Mô hình thưởng (reward model) để đánh giá chất lượng phản hồi.
- Đo lường đa dạng (SBERT, E-Vendi, hoặc discriminator).

## Các bước thực hiện
1. Chuẩn bị dữ liệu huấn luyện (mixture 4:1 Tulu3-SFT-Mixture : Infinite-Chat hoặc tương đương) và tính điểm chất lượng tham chiếu (smin, smax, µref) từ policy đóng băng cho mỗi prompt.
2. Thêm mã định danh vai trò abstract vào đầu system prompt (ví dụ "You are role i."), tránh persona thủ công để khuyến khích chuyên biệt phát sinh.
3. Trong mỗi vòng huấn luyện, mỗi role tạo một phản hồi cho mỗi prompt trong batch, tạo thành nhóm phản hồi (ví dụ 6 role-response pairs).
4. Tính điểm chất lượng si = Sϕ(x, yi) từ mô hình thưởng; tính ngưỡng chất lượng tùy prompt τq(x) = smin + α(smax − µref) và hệ số σq(x) = γ(µref − smin + ϵ).
5. Áp cổng chất lượng nhị phân g(x, yi) = 1[si ≥ τq(x)]: chỉ phản hồi đạt ngưỡng mới nhận điểm đa dạng.
6. Tính điểm đa dạng d(x, yi, Y) = minj≠i (1 − cosine similarity embedding giữa yi và nearest neighbor trong nhóm).
7. Tính phần thưởng tổng hợp: phần thưởng chất lượng (tanh-bounded) + điểm đa dạng (gated bởi cổng chất lượng) + phạt (dộ dài, ngôn ngữ, định dạng).
8. Cập nhật policy chung bằng GRPO với ưu đãi tương đối nhóm và KL regularization đến policy cơ sở.
9. Suy luận: chế độ chuẩn (không mã role → phản hồi đơn) hoặc chế độ đa dạng (nhiều mã role → tập ứng viên đa dạng).

## Output mong đợi
- Model tạo ra nhiều phản hồi khác biệt và chất lượng cao từ cùng một prompt, đồng thời giữ hoặc cải thiện năng lực chung (pass@1), chống được mode collapse.

## Ví dụ áp dụng
- Doanh nghiệp nhỏ tạo ý tưởng bài viết blog: cùng một prompt "viết 5 chủ đề bài về marketing", MODA tạo ra 40 sắc xanh riêng biệt (ví dụ 40 shade of blue) thay vì 1 chủ đề lặp lại; dùng mode chuẩn cho câu trả lời fact, mode đa dạng cho brainstorming.

## Gotchas
- Không dùng phần thưởng đa dạng đơn độcWithout quality gate → reward hacking (ngoài chủ đề, verbosity, đổi ngôn ngữ).
- Không ép persona thủ công quá cụ thể; mã role abstract khuyến khích chuyên biệt phát sinh tốt hơn.
- Không áp dụng mode đa dạng cho truy vấn fact có đáp án duy nhất.
- Không quên KL regularization đến policy cơ sở để tránh policy quá lệch.

## Kiểm tra kỹ năng (self-check)
- Người không đọc paper gốc có follow được 9 bước trên không? [YES] — từng bước là action cụ thể.
- Bước nào mơ hồ nhất? Bước 4-5 (tính ngưỡng chất lượng tùy prompt) cần chi tiết triển khai smin/smax/µref.
- Input section có đủ không? [YES] — model cơ sở, policy tham chiếu, mã role, GRPO, mô hình thưởng, đo lường đa dạng.

## Dry run (tình huống giả)
- Tình huống: Solopreneur muốn tạo 10 ý tưởng video khác nhau từ cùng một chủ đề.
- Chạy skill: (1) Chuẩn bị 10K prompt về video content; (2) tính điểm chất lượng tham chiếu từ policy đóng băng; (3) thêm mã role abstract (role 1..6); (4) mỗi role tạo 1 phản hồi mỗi prompt → nhóm 6; (5) tính điểm chất lượng và ngưỡng tùy prompt; (6) chỉ trao điểm đa dạng cho phản hồi vượt ngưỡng; (7) tính điểm đa dạng theo khoảng cách ngữ nghĩa đến nearest neighbor; (8) tính phần thưởng tổng hợp với phạt độ dài/ngôn ngữ/định dạng; (9) cập nhật policy bằng GRPO; (10) suy luận mode đa dạng với 6 role tokens → 10 ý tưởng video khác biệt.

## Verdict: [SKILL VALID]
