# 2610.24718 — Neuro-Inspired Inhibitory Message Passing for Accurate and Token-Efficient Multi-Agent Reasoning

## Giá trị cốt lõi (1 câu)

Dùng một router truyền thông không cần huấn luyện để truyền chỉ câu bằng chứng người nhận chưa có, loại bỏ bản sao trùng lặp và các câu trả lời của người gửi → giúp nhóm agent chính xác hơn 39-77 điểm phần trăm và giảm 10-46% token mỗi chạy.

## Problem

Trong hệ thống multi-agent, các agent cùng sở hữu mọi bằng chứng cần thiết để giải quyết bài toán nhưng vẫn kết luận sai do bằng chứng chung bị lặp lại nhiều lần vùi lấp bằng chứng riêng hiếm có, quan trọng quyết định (hidden profile). Truyền thông chuẩn gửi toàn bộ tin nhắn của người gửi (kèm lý luận và câu trả lời) cho mọi người nhận, làm tăng đầu vào mỗi agent phải xử lý và làm sai lệch phán xét do sự lặp (data incest / tương quan dữ liệu). Giới hạn số người gửi nghe được giữ hộ thư nhỏ nhưng nguy cơ loại bỏ các agent nắm bằng chứng quyết định.

## Contribution

1. Đề xuất inhibitory message passing (truyền thông hạn chế), một router truyền thông miễn phí huấn luyện (training-free) với 3 quy tắc: (1) truyền câu bằng chứng gốc, không phải tin nhắn của người gửi; (2) mỗi câu bằng chứng được truyền tối đa một lần mỗi vòng cho mỗi người nhận; (3) chỉ truyền nếu người nhận chưa có câu đó.
2. Router loại bỏ bằng chứng mà người nhận đã có, không yêu cầu gọi mô hình bổ sung, không cần điều chỉnh trọng số.
3. Thử nghiệm trên 3 benchmark (HiddenBench, decoy puzzles, MuSiQue), 7 mô hình mở (4B-32B tham số) và 2 mô hình thương mại (GPT-6 Luna, Claude Haiku 5.5), nhóm lên đến 64 agent, 3 kiến trúc (peer-to-peer, orchestrator-worker, hierarchical).

## Method

Mỗi agent viết tin nhắn mỗi vòng. Router xây dựng hộ thư (inbox) cho mỗi người nhận từ các tin nhắn của người gửi theo 3 quy tắc:

1. **Evidence, not messages (bằng chứng, không phải tin nhắn)**: khi tin nhắn của người gửi diễn giải lại một câu bằng chứng mà người gửi nắm giữ, câu bằng chứng gốc (không phải tin nhắn) mới được truyền, không kèm lý luận hay câu trả lời của người gửi.
2. **Once per round (một lần mỗi vòng)**: bất kể bao nhiêu người gửi diễn giải lại cùng một câu bằng chứng, người nhận chỉ nhận được nó một lần mỗi vòng.
3. **Only if missing (chỉ nếu chưa có)**: câu bằng chứng đã có trong bằng chứng của người nhận sẽ không được gửi lại.

Router so sánh từ hiếm trong tin nhắn với các câu bằng chứng mỗi agent đã biết (Appendix C.1), không gọi mô hình và không cần huấn luyện. Công thức chính (Equation 2): n_iu = min(E_iu, θ_iu) với θ_iu = 1 nếu người nhận chưa có câu u, 0 nếu đã có — suy ra suppresses grows one-for-one với số bản sao đến, hộ thư không bao giờ chứa nhiều hơn các câu người nhận chưa có.

## KNOWLEDGE — Số liệu & khái niệm

- Độ chính xác nhóm tăng 39-77 điểm phần trăm trên 3 benchmark và cả 2 mô hình chính, so với truyền thông chuẩn.
- Token mỗi chạy giảm 10-46% so với truyền thông chuẩn (tính cả tất cả agent, bao gồm người quyết định).
- 7 mô hình mở từ 4B đến 32B tham số (Qwen3-4B/8B/14B/32B, Olmo-3-7B, Ministral-3-8B, Gemma-4-12B) và 2 mô hình thương mại (GPT-6 Luna, Claude Haiku 5.5).
- Nhóm lên đến 64 agent (HiddenBench).
- Trên HiddenBench, Qwen3-8B giữ độ chính xác 80-86% từ 4 đến 64 agent, trong khi truyền thông chuẩn thấp (23% ở N=4, giảm xuống 8% ở N=64).
- Nhóm độ chính xác tăng 63 và 59 điểm phần trăm trong đánh giá trước đăng ký (pre-registered) đối với 2 mô hình thương mại.
- Tại N=32, hủy bỏ giảm khoảng 4/5 phần nhắc nhở (prompt) của người quyết định trong nhóm orchestrator-worker và gần một nửa trong nhóm phân cấp (hierarchical).
- Xóa tất cả các quy tắc router làm độ chính xác rơi xuống 42-53% (HiddenBench) và 7-24% (đố décode), với 2.4-4.7 lần token của router.

## INSIGHT — Cơ chế & tại sao

[Sự lặp lại của bằng chứng chung] xảy ra VÌ [mỗi tin nhắn gửi đi mang cả bằng chứng và câu trả lời của người gửi, làm việc cho bằng chứng chung trở nên quá đại diện trong hộ thư của người nhận]. Điều này nghĩa là [phán xét của mô hình bị sai lệch theo 동의 opinión chung, bằng chứng riêng hiếm có bị bỏ qua, nhóm kết luận sai mặc dù cùng sở hữu mọi bằng chứng cần thiết].

[Loại bỏ bằng chứng người nhận đã có] xảy ra VÌ [mỗi câu bằng chứng chỉ cần được truyền một lần cho mỗi người nhận, bất kể số người gửi diễn giải lại]. Điều này nghĩa là [kích thước hộ thư không tăng theo nhóm, mọi người nắm giữ bằng chứng riêng vẫn có thể được nghe, độ chính xác ổn định khi nhóm lớn hơn].

[Đưa ra câu bằng chứng gốc thay vì câu diễn giải lại của người gửi] xảy ra VÌ [câu của người gửi kèm theo câu trả lời ưu thích của họ, đói d diffuse sai lầm chung]. Điều này nghĩa là [người nhận cân bằng bằng chứng mà không bị ảnh hưởng bởi quyết định sẵn có của người khác, đóng một con đường mà sự nhầm lầm chung lan truyền].

## IDEA — Áp dụng được gì

1. Áp dụng inhibitory message passing vào nhóm agent nghiên cứu/phân tích: xây dựng router nhẹ truyền chỉ câu bằng chứng gốc mỗi người nhận chưa có, loại bỏ lý luận và câu trả lời của người gửi. Bước đầu: ghi lại các câu bằng chứng mỗi agent nắm giữ, so sánh từ hiếm trong tin nhắn gửi với câu bằng chứng đã知 để lọc hộ thư.
2. Áp dụng vào quy trình khảo sát thị trường multi-agent: mỗi agent thu thập nguồn độc lập, router truyền chỉ bằng chứng còn thiếu cho người quyết định, tránh sự trùng lặp làm sai lệch kết luận. Bước đầu: định dạng đầu ra của mỗi agent thành danh sách câu bằng chứng có mã nguồn (source tag), router trừ đi những câu người quyết định đã có.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Trong hệ thống multi-agent, thiết kế truyền thông quan trọng hơn kích thước mô hình — việc giới hạn đầu vào dư thừa cho mỗi người nhận giúp độ chính xác mở rộng độc lập với kích thước nhóm.
- Khi nào dùng: Nhóm agent cần tổng hợp bằng chứng phân tán để đưa ra quyết định được chấm điểm (ví dụ nghiên cứu, phân tích, chẩn đoán).
- Khi nào KHÔNG dùng: Công việc đòi hỏi agent trao đổi kết quả trung gian không chứa trong bằng chứng gốc (lập trình, lập kế hoạch, tính toán phân tán) — loại trừ chúng có thể cản trở hợp tác.
- Ví dụ áp dụng ngoài domain gốc: Trong nhóm hợp tác con người, tóm tắt chỉ thông tin mới mẻ mỗi thành viên chưa biết thay vì đưa toàn bộ nội dung thảo luận, giúp họp ngắn gọn và tránh lệch theo ý kiến đa số sớm.

## Assumptions & Limitations

- Điều kiện phải đúng: cần liên kết đáng tin cậy giữa tin nhắn và bằng chứng nó đề cập (provenance), cần phân biệt giữa các báo cáo lặp lại một quan sát và các quan sát độc lập về cùng một 주장.
- Limitation paper thừa nhận: thí nghiệm tập trung vào nhiệm vụ kết hợp bằng chứng phân tán để đạt được câu trả lời được chấm điểm; router chỉ giới hạn sự lặp lại, bằng chứng riêng biệt người nhận phải xử lý vẫn có thể tăng theo nhóm; router không đánh giá độ tin cậy của bằng chứng nó truyền (câu bằng chứng sai được gieo ra sẽ làm giảm độ chính xác); không thể rút lại bằng chứng đã bị sửa lỗi hoặc lỗi thời.
- Limitation paper KHÔNG nói: không thiết lập được khi loại trừ lý luận và câu trả lời sẽ cản trở hợp tác trên công việc cần trao đổi kết quả trung gian (code, kế hoạch); hiệu quả trên tác vụ không có bằng chứng rõ ràng để khớp (ví dụ viết sáng tạo) chưa được kiểm chứng.

## Metadata

- Năm: 2026
- Tác giả: Nima H. Siboni, Magdalena Springer, Vahid Rostami
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.24718
- Citation count: chưa có (paper mới, Oct 2026)
