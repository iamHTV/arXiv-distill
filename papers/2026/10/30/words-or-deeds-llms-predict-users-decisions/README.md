# [2610.36813] Words or Deeds? How LLMs Predict Users' Decisions in Human-Agent Dialogue

## Giá trị cốt lõi (1 câu)

Khi agent cần dự đoán hành động người dùng từ nội dung hội thoại, nên ưu tiên lịch sử quyết định thực tế hơn lời hứa trong chat — vì LLM over-estimate mức độ người dùng giữ lời (dự đoán .69 giữ lời khi thực tế chỉ .40) và không bắt được sự thay đổi hành vi theo persona agent, khiến accuracy tổng hợp ẩn giấu lỗi lớn trên từng agent.

## Problem

Hệ thống web ngày càng dự đoán quyết định người dùng từ những gì người dùng nói trong hội thoại, nhưng khi lợi ích phần mâu thuẫn, người dùng có thể hứa hợp tác rồi không làm. Các hệ thống dựa trên lời hứa này — như agent bán hàng hay tư vấn quyết định đưa ra sự nhượng bộ — có thể nhượng bộ cho người dùng sau đó không giữ lời, gây thiệt hại cho bên agent đại diện. Các nghiên cứu hiện có không liên kết lời người dùng nói với quyết định trước đó của cùng người, với đối tượng phù hợp (counterpart), và với hành động sau đó. Tổng kết accuracy chung cũng không cho biết predictor đang mắc loại lỗi nào: dựa vào lời hứa giúp accuracy trên lời được giữ nhưng làm mất accuracy trên lời bị phá, hai thứ có thể bù nhau.

## Contribution

1. Thiết kế đánh giá gắn việc predictor sử dụng hội thoại với hành động được ghi lại riêng biệt, chia theo lời có được giữ hay không, theo lời có mâu thuẫn với quyết định trước đó của người dùng, và theo agent người dùng đối diện.
2. Bằng chứng tám LLM predictor dựa vào quyết định được nói ra (stated decisions) nhiều hơn mức chúng được giữ.
3. Bằng chứng dự đoán bỏ sót sự thay đổi hành vi của người dùng theo persona agent và sự tương thích tính cách (trait compatibility), và số liệu pooled (tổng hợp) ẩn giấu cả hai lỗi.
4. Nghĩa hình thiết kế cho mô hình người dùng dựa trên hội thoại: trọng số một lời người dùng nhận nên phụ thuộc vào quyết định trước đó của người dùng và vào agent, và dự đoán nên được kiểm tra theo những gì người sau đó làm với mỗi agent.

## Method

Nghiên cứu dùng bộ dữ liệu Personality-1260: 42 người dùng (sinh viên đại học Trung Quốc, 21 nữ, tuổi trung bình 22.1) hoàn thành bảng tính cách BFI-44 rồi chơi một ván với mỗi của năm agent, mỗi agent được prompt biểu diễn một đặc tính Big Five chiếm ưu thế (Mở rộng, Thận trọng, Hướng ngoại, Hòa nhã, Căng thẳng). Mỗi ván có 6 vòng, người dùng và agent có thể nói chuyện tự do rồi cả hai quyết định hợp tác hay phản bội, quyết định của agent được tiết lộ chỉ sau quyết định của người dùng. Hợp tác nhau trả 2 điểm mỗi bên, phản bội chống lại người hợp tác trả 3 (người hợp tác 0), phản bội đồng thời trả 0 mỗi bên. Tám LLM mở (Qwen3.5-9B, Qwen3.8-27B, Gemma-4-12B, Gemma-4-31B, Seed-OSS-36B, GLM-4-32B, Ministral-3-14B, Olmo-3.1-32B) dự đoán mỗi quyết định từ 19 tổ chức của hồ sơ quyết định (R — cả hai bên quyết định trước đó) và hội thoại (D — những gì người nói). Các điều kiện có 4 mức quyết định có tên (không, Ro, Rc, R) và 5 mức hội thoại (không, Do, Dc, Dt, D): 19 điều kiện, ô trống không chạy. Dự đoán dùng các ván 2–5 (1,008 vòng), hành vi người dùng so sánh với dự đoán trên cùng các vòng. Phân tích dùng user bootstrap (50,000 lần vét cạn 42 người dùng với thay thế).

## KNOWLEDGE — Số liệu & khái niệm

- 1,260 vòng, 42 người dùng, 5 agent persona, 8 LLM mở làm predictor.
- Hồ sơ quyết định đơn lẻ (R) đạt AUC = .80 [.76, .85] phân cách hợp tác từ phản bội; hội thoại đơn lẻ (D) AUC = .70 [.64, .76]; cả hai (R + D) AUC = .79 [.75, .83] — thêm hội thoại không mang lại lợi ích có thể đo được.
- Lời bản thân xếp hạng kém: với 96% lời thông báo hợp tác, lời tách hợp tác từ phản bội ở AUC = .55.
- Thêm hội thoại hiện tại vào quyết định ván hiện tại thay đổi accuracy trên vòng có lời khai báo từ .73 lên .74: nó nâng accuracy trên 470 vòng lời được giữ từ .76 lên .95 (+.20 [.15, .25]) và hạ nó trên 176 vòng lời bị phá từ .65 xuống .17 (−.48 [−.52, −.44]).
- Khi người dùng thông báo một quyết định họ chưa chọn trong ván đó (53 vòng, 20 người dùng), xác suất dự đoán giữ lời tăng từ .13 không có hội thoại lên .69 có hội thoại, trong khi người dùng giữ lời ở tỉ lệ .40 [.25, .58]: dự đoán chuyển từ .27 dưới mức quan sát lên .30 trên nó.
- Một câu chèn vào thông báo quyết định chuyển sự đồng ý với quyết định được ghi lại từ .75 lên .98 khi khớp và xuống .08 khi mâu thuẫn.
- Người dùng hợp tác 70.6% vòng với agent Hòa nhã và 54.5% với agent Hướng ngoại (+16.3 điểm); dự đoán hợp tác là 64.5% và 63.1% (không khác biệt đáng thấy).
- AUC dự đoán từ .76 (O) đến .82 (N), không cặp nào khác nhau; dự đoán trải qua 6.0 điểm trên các persona.
- Chênh lệch dự đoán (bias) về tỷ lệ hợp tác: +8.6 điểm với agent Hướng ngoại và −6.0 điểm với agent Hòa nhã; chênh lệch 14.6 điểm giữa chúng.
- Càng cao điểm người dùng trên đặc tính agent thể hiện, càng nhiều họ hợp tác với agent đó (+3.0 điểm mỗi độ lệch chuẩn); dự đoán càng càng thấp hơn mức hợp tác thực tế (−3.3 điểm mỗi độ lệch chuẩn).
- Thêm điểm BFI hoặc điểm tương thích vào prompt chỉ giảm độ dốc sai số khoảng một phần tư (từ −3.3 xuống −2.5), sai số phần lớn còn lại.

## INSIGHT — Cơ chế & tại sao

[LLM over-estimate mức người dùng giữ lời hứa] xảy ra VÌ [LLM cân nặng lời của người dùng nhiều hơn mức hành vi của người dùng bảo đảm: khi người dùng thông báo một quyết định chưa từng chọn, xác suất dự đoán giữ lời nhảy từ .13 lên .69 trong khi thực tế chỉ .40]. Điều này nghĩa là [dự đoán dựa trên hội thoại dễ tin lời hứa quá mức, dẫn đến nhượng bộ không xứng đáng].

[Thêm hội thoại không tăng AUC tổng (.80 → .79)] xảy ra VÌ [nó nâng accuracy trên lời giữ nhưng hạaccuracy trên lời phá, hai mức độ bù nhau, chất lỏng lỗi lên các vòng người phá lời — gần nửa tất cả phản bội]. Điều này nghĩa là [accuracy tổng hợp ẩn giấu việc predictor đang đưa ra sai lệch ngược chiều trên các vòng quan trọng nhất].

[LLM không bắt được sự thay đổi hành vi theo persona agent và tương thích tính cách] xảy ra VÌ [prediction hầu như không đổi giữa các agent (64.5% vs 63.1%) trong khi hành vi người dùng thay đổi mạnh (70.6% vs 54.5%), và pooled bias gần zéro ẩn giấu chênh lệch lên đến 14.6 điểm giữa agent]. Điều này nghĩa là [một user representation hấp thụ tất cả lựa chọn thành xu hướng hợp tác chung sẽ mất thông tin về đối tượng tương tác; cần đánh giá hành động liên quan đến đối tượng và lịch sử tương tác].

[Lưu lại mỗi lời nói kèm kết quả hành động sửa lại phần lớn việc over-estimate] xảy ra VÌ [khi gắn mỗi lời nói trước đó với kết quả, xác suất dự đoán giữ lời giảm từ .69 xuống .40, bằng mức quan sát]. Điều này nghĩa là [cái record liên kết lời nói với kết quả giúp predictor dùng thông tin thêm tốt nhất khi nó nói rõ quan hệ cần dự đoán].

## IDEA — Áp dụng được gì

1. Áp dụng theo dõi tỷ lệ giữ lời của mỗi người dùng: trước khi agent quyết định nhượng bộ dựa trên lời hứa của user, agent tra cứu lịch sử lời hứa trước đó của user đó và tỷ lệ chúng được giữ. Cho ai: agent bán hàng/tư vấn quyết định concessions. Bước đầu: lưu cho mỗi user một cặp (lời hứa, hành động thực tế) trong mỗi vòng tương tác.

2. Áp dụng đánh giá dự đoán quyết định người dùng theo từng persona agent và theo loại lời (giữ/phá), không chỉ dùng accuracy tổng hợp. Cho ai: đội xây dựng agent mô hình người dùng (user model). Bước đầu: báo cáo accuracy riêng cho lời được giữ và lời bị phá, và riêng cho mỗi agent/persona.

3. Áp dụng ưu tiên lịch sử quyết định thực tế hơn nội dung hội thoại khi xây dựng model dự đoán hành động user. Cho ai: ML engineer xây dựng user model. Bước đầu: trong input của model dự đoán, đưa hồ sơ quyết định trước (cả hai bên) trước nội dung hội thoại hiện tại, vì hội thoại ít tăng AUC.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Lời hứa của người dùng trong hội thoại không nên được coi bằng hành động thực tế; hệ thống cần theo dõi tỷ lệ giữ lời của mỗi người dùng và cân nhắc lời hứa mới dựa trên lịch sử. Áp dụng khi agent quyết định nhượng bộ hoặc chuyển nhượng dựa trên lời hứa người dùng. Không áp dụng khi chỉ cần ước lượng xu hướng chung mà không cần chi tiết từng người dùng.

## Assumptions & Limitations

- Điều kiện phải đúng: có lời nói và hành động được ghi lại riêng lẻ, có nhiều quyết định lặp lại tạo thành hồ sơ để so sánh với lời nói, có đối tượng thay đổi trong khi hành động và phần thưởng giữ nguyên.
- Limitation paper thừa nhận: nghiên cứu 42 sinh viên đại học Trung Quốc trong các ván ngắn, thấp rủi ro; tám predictor zero-shot dùng prompt tiếng Trung với reasoning bị tắt; mọi đối tượng dùng GPT-4o; persona prompts thay đổi ngôn ngữ và quyết định, làm trộn lẫn sự biểu diễn tính cách với reciprocity hành vi; tương thích dùng một đặc tính; phân tích khám phá và chưa can thiệp; một số nhóm con nhỏ (53 vòng từ 20 người dùng); sửa đổi prompt đo nhạy cảm model, trong khi kết hợp lời-hành động không xác định hiệu ứng nhân quả.
- Limitation paper KHÔNG nói: kết quả có thể khác đối với các dân cư khác, các mối quan hệ dài hơn, và các tác vụ web; hiệu ứng của prompt engineering có thể khác trên các model có reasoning bật; chi phí vận hành của việc lưu lịch sử lời-hành động trên quy mô lớn chưa được đánh giá.

## Metadata

- Năm: 2026
- Tác giả: Baiqiao Zhang, Shuai Ma, Zhifeng Liao, Chao Zhou, Jianshu Wang, Yuhan Zhao, Chaoyue Zhang, Tongjun Si, Yuying Tang, Xiangxian Li, Yong-Jin Liu, Yulong Bian
- Category arXiv: cs.CL
- Link PDF: https://arxiv.org/pdf/2610.36813v1
- Citation count: [không tìm được]