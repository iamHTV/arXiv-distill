# Báo cáo distill arXiv — ngày 2026-10-21

Tổng hợp 10 bài paper đã distill hôm nay (10 bài tốt nhất được chọn từ quét arXiv, theo điểm LLM cao nhất).
Mỗi bài đã qua đủ 6 bước distill (xem paper → phân loại → tạo README → tạo skill → test skill → báo cáo), commit+push lên GitHub.
Báo cáo này viết lại bằng tiếng Việt đơn giản, gần gũi, dành cho solopreneur Việt Nam. Mọi từ chuyên ngành tiếng Anh có giải thích trong ngoặc.

## Tổng quan
- Tổng bài distill: **10**
- Tất cả đều có ứng dụng thực tế (nhãn [applied] — có experiment, dữ liệu thật, benchmark cụ thể).

## Danh sách 10 bài hôm nay
1. Selling in the Wild — Sales agent được đào tạo trên hội thoại thương mại thật (arXiv 2610.25461v1)
2. CHSM8 — Mô hình cờ vua tuân theo lệnh nhắc (prompt) tự nhiên (arXiv 2610.25356v1)
3. MAPS — Hệ thống tạo quảng cáo video cá nhân hóa bằng đa agent (arXiv 2610.25748v1)
4. Fake News, Real Crashes — Tấn công đưa tin giả vào agent giao dịch tài chính (arXiv 2610.26438v1)
5. NIOCIS — Định tuyến next-hop cho agent gọi công cụ, giảm chi phí suy luận (arXiv 2610.25985v1)
6. One-Pixel of Reasoning — Một liên kết suy luận ngầm đủ làm agent đi sai (arXiv 2610.24873v1)
7. CXBENCH — Tiêu chuẩn đánh giá agent tuân thủ quy trình trong kinh doanh (arXiv 2610.25954v1)
8. ScaleMAS — Phối hợp đa agent qua kho tin nhắn chung (arXiv 2610.16120v1)
9. Ask Less, Ask Better — Giới hạn số lần agent hỏi khách hàng (arXiv 2610.24411v1)
10. Explore or Confirm (Wellocate) — Agent phân bổ ngân sách thí nghiệm giữa khám phá và xác nhận (arXiv 2610.25111v1)

## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN
Dưới đây là 5 insight hàng đầu, mỗi insight 1 câu ngắn + 1 ví dụ áp dụng ngay cho solopreneur Việt Nam:

1. **Đào tạo AI sales agent trên cuộc trò chuyện thật của bạn** (chatlive, Zalo, Messenger) tăng doanh thu trên mỗi khách +10% và chuyển đổi khách tương tác +21.6%, nhưng chỉ tốn 1.8% chi phí so với nhân viên bán hàng. → Áp dụng: hôm nay hãy bắt đầu thu thập và ẩn danh 10.000+ cuộc trò chuyện cũ của website hoặc fanpage, gán nhãn kết quả (mua / hủy / lead), để sẵn sàng tinh chỉnh (fine-tuning) mô hình mở (ví dụ Qwen3) làm agent chăm sóc khách.

2. **Giới hạn agent hỗ trợ khách hàng chỉ hỏi 1–3 câu làm rõ mỗi phiên** và nhớ câu trả lời trước của khách, tránh hỏi lại và làm phiền khách. → Áp dụng: nếu bạn dùng agent chăm sóc khách, hãy cài đặt "ngân sách gián đoạn" (interruption budget) 1–3 câu hỏi mỗi phiên và lưu câu trả lời trước của khách vào bộ nhớ, không hỏi lại vấn đề đã biết.

3. **Dùng hai agent độc lập kiểm tra chéo trước khi thực hiện giao dịch quan trọng** (thanh toán, hợp đồng, chuyển tiền) để ngăn tin giả hoặc nội dung bị làm hỏng làm agent hành động sai (tấn công Inject lên 62%, hệ thống kiểm tra chéo giảm xuống 9–10%). → Áp dụng: thiết lập một agent phân tích và một agent kiểm tra yêu cầu phải đồng ý trước khi agent thực hiện thao tác kinh doanh rủi ro cao.

4. **Với agent gọi công cụ** (tra cứu đơn hàng, kiểm tra kho hàng, xử lý thanh toán), hãy dùng quy tắc rẻ cho yêu cầu phổ biến và chỉ gọi mô hình ngôn ngữ lớn (LLM, tốn tiền mỗi lần gọi) khi yêu cầu phức tạp hoặc không chắc chắn. → Áp dụng: giúp giảm chi phí gọi API LLM hàng tháng đáng kể.

5. **Tạo quảng cáo video / nội dung quảng cáo theo yêu cầu** với nhiều agent phối hợp (viết kịch bản → kiểm tra lại) thay vì dùng kho mẫu quảng cáo cố định, giúp cá nhân hóa cao hơn cho mỗi khách hàng. → Áp dụng: dùng một agent viết kịch bản video quảng cáo dựa trên hồ sơ khách hàng, rồi một agent khác kiểm tra lại trước khi đăng quảng cáo.

## Chi tiết từng bài

### [1] Selling in the Wild: Sales agent được đào tạo trên hội thoại thương mại thật (arXiv 2610.25461v1)
- **Làm gì:** Xây dựng một nhân viên bán hàng AI được tinh chỉnh trên 4,6 triệu cuộc hội thoại thương mại thật và kiểm tra trên 100 trang web bán hàng với khách hàng thật, so sánh với không agent, mô hình AI hàng đầu (frontier) và nhân viên chat trực tiếp.
- **Học được gì:** Dữ liệu hội thoại thật quan trọng hơn quy mô mô hình cho tác vụ bán hàng. Agent bán hàng tăng doanh thu trên mỗi khách +10% so với không agent và chuyển đổi khách tương tác +21.6% so với mô hình frontier cùng khung (scaffolding: giao diện, công cụ tra cứu, lệnh nhắc), nhưng chi phí chỉ 1.8% so với nhân viên bán hàng.
- **Áp dụng cho bạn:** Thu thập 10.000+ cuộc trò chuyện chatlive/Zalo/Messenger cũ, gán nhãn kết quả (mua/hủy/lead), rồi tinh chỉnh mô hình mở (ví dụ Qwen3) để làm agent bán hàng hoặc chăm sóc khách với chi phí gần không so với thuê nhân viên.

### [2] CHSM8: Mô hình cờ vua tuân theo lệnh nhắc tự nhiên (arXiv 2610.25356v1)
- **Làm gì:** Một mô hình cờ vua (transformer) được điều khiển bằng lệnh nhắc (prompt) bằng tiếng tự nhiên, dùng DPO (tối ưu hóa ưu tiên trực tiếp) để tuân theo phong cách cờ mà không cần mô hình phần thưởng (reward model).
- **Học được gì:** Có thể kiểm soát hành vi của agent qua tiếng tự nhiên dùng DPO với cặp dữ liệu (cùng đầu ra, điều kiện khác nhau) mà không cần reward model.
- **Áp dụng cho bạn:** Nếu bạn dùng agent viết content, hãy chuẩn bị cặp ví dụ (cùng bài viết, lệnh nhắc khớp vs không khớp phong cách thương hiệu) và dùng DPO để agent viết theo phong cách của bạn, không cần mô hình phần thưởng phức tạp.

### [3] MAPS: Hệ thống tạo quảng cáo video cá nhân hóa bằng đa agent (arXiv 2610.25748v1)
- **Làm gì:** Hệ thống tạo quảng cáo video cá nhân hóa theo yêu cầu với 4 agent (Profile, Scripter, Director, Reflector), dùng GRPO (thuật toán tối ưu hóa phần thưởng đa mục tiêu). Được thử nghiệm A/B thực tế tại Kuaishou: CTR (tỷ lệ nhấn chuột quảng cáo) +2.87%, CVR (tỷ lệ chuyển đổi quảng cáo) +2.74%, ARPU (doanh thu trên mỗi người dùng) +9.85%.
- **Học được gì:** Tạo quảng cáo video theo yêu cầu (on-demand) mang giá trị cao hơn khớp quảng cáo từ kho cố định; agent hỗ trợ nhau qua phản hồi trực tuyến (Reflector) cải thiện liên tục.
- **Áp dụng cho bạn:** Dùng một agent viết kịch bản video quảng cáo sản phẩm dựa trên hồ sơ khách hàng (Profile Agent), rồi một agent khác kiểm tra lại (Reflector Agent) trước khi đăng, giúp quảng cáo cá nhân hóa hơn mà không cần đội ngũ sáng tạo lớn.

### [4] Fake News, Real Crashes: Tấn công đưa tin giả vào agent giao dịch tài chính (arXiv 2610.26438v1)
- **Làm gì:** Một cuộc tấn công đưa tin giả (information injection) lừa agent giao dịch tài chính, khiến tỷ lệ tấn công thành công (ASR) lên 62% (gấp 4.5 lần prompt injection 14%). Một hệ thống điều phối phân cấp (star pipeline) giảm ASR xuống 9–10%.
- **Học được gì:** Thông tin mà agent hành động dựa trên đó (dữ liệu) là bề mặt tấn công lớn hơn lệnh hệ thống (control-plane); cần nhiều agent độc lập kiểm tra chéo trước khi thực hành giao dịch rủi ro cao.
- **Áp dụng cho bạn:** Nếu bạn dùng agent xử lý thanh toán/giao dịch, hãy thiết lập hai agent độc lập (một agent phân tích, một agent kiểm tra yêu cầu) phải đồng ý trước khi thực hiện, để ngăn tin giả lừa agent chuyển tiền sai.

### [5] NIOCIS: Định tuyến next-hop cho agent gọi công cụ, giảm chi phí suy luận (arXiv 2610.25985v1)
- **Làm gì:** Một lớp định tuyến kiểu quyết định (typed-decision) giúp agent gọi công cụ với chi phí suy luận (inference) thấp: chỉ gọi mô hình ngôn ngữ lớn (LLM) khi không chắc chắn, dùng một "readout" rẻ để chọn bước tiếp theo trong không gian tùy chọn giới hạn.
- **Học được gì:** Với các quyết định lặp lại, một readout rẻ có thể thay thế phần lớn cuộc gọi LLM, chỉ giữ LLM cho trường hợp không chắc chắn.
- **Áp dụng cho bạn:** Nếu bạn xây dựng agent gọi nhiều công cụ (tra cứu đơn hàng, kiểm tra kho), hãy dùng một quy tắc rẻ để xử lý các yêu cầu phổ biến và chỉ gọi LLM (tốn tiền) khi yêu cầu phức tạp hoặc không chắc chắn, giúp giảm chi phí gọi API LLM.

### [6] One-Pixel of Reasoning: Một liên kết suy luận ngầm đủ làm agent đi sai (arXiv 2610.24873v1)
- **Làm gì:** Một cuộc tấn công thay đổi một mối liên kết suy luận ngầm (one pixel of reasoning) đủ để làm agent đi sai, ngay cả khi bằng chứng đầu vào đúng. Tranh luận đa agent không tự động khắc phục.
- **Học được gì:** Liên kết suy luận ngầm giữa bằng chứng và kết luận là bề mặt tấn công độc lập; cần kiểm tra xem một câu điều chỉnh nhỏ có thể đảo ngược kết luận của agent hay không.
- **Áp dụng cho bạn:** Nếu bạn dùng agent để tổng hợp báo cáo hoặc đưa ra khuyến nghị từ nhiều nguồn, hãy thường xuyên kiểm tra lại xem một thay đổi nhỏ trong thông tin đầu vào có thể làm agent đổi ý hay không, đặc biệt trong y tế, pháp lý, bảo mật.

### [7] CXBENCH: Tiêu chuẩn đánh giá agent tuân thủ quy trình trong kinh doanh (arXiv 2610.25954v1)
- **Làm gì:** Một tiêu chuẩn đánh giá agent làm việc trong quy trình tuân thủ (tài chính, y tế, bảo hiểm) với híbrid grader (định trị + LLM judge — LLM làm vai trò người chấm điểm) và metric false-pass (kết quả đúng nhưng vi phạm quy trình).
- **Học được gì:** Kết quả đúng không đồng nghĩa quy trình đúng; agent có thể đạt mục tiêu kinh doanh mà vi phạm quy trình điều chỉnh, nên phải đánh giá cả quy trình lẫn kết quả.
- **Áp dụng cho bạn:** Nếu bạn dùng agent trong lĩnh vực có quy định (tài chính, bảo hiểm, y tế), hãy kiểm tra không chỉ kết quả cuối mà cả quy trình agent tuân thủ (thứ tự bước, quyền hạn), không chỉ xem kết quả có đúng hay không.

### [8] ScaleMAS: Phối hợp đa agent qua kho tin nhắn chung (arXiv 2610.16120v1)
- **Làm gì:** Hệ thống đa agent phối hợp qua kho dữ liệu tin nhắn chung (substrate-centric): agent chỉ tương tác qua publish/search/visit, mỗi đọc giới hạn số tin nhắn; tin nhắn tồn tại sau khi tác giả rời đi.
- **Học được gì:** Phối hợp đa agent nên thiết kế vào chất dữ liệu chung (shared datastore, đọc có giới hạn, tin nhắn bền vững) thay vì gắn chặt vào logic từng agent, giúp hệ thống mở rộng và kháng lại sự cố agent.
- **Áp dụng cho bạn:** Nếu bạn vận hành nhiều agent cùng lúc, hãy để chúng giao tiếp qua một bảng tin nhắn chung (shared inbox) với tin nhắn lưu trữ lâu dài, nên agent mới có thể gia nhập và agent cũ rời đi không làm hỏng hệ thống.

### [9] Ask Less, Ask Better: Giới hạn số lần agent hỏi khách hàng (arXiv 2610.24411v1)
- **Làm gì:** Giới hạn số lần agent hỏi làm rõ (interruption budget) 1–3 câu hỏi mỗi phiên và đo cả tần suất lẫn chất lượng câu hỏi, không chỉ đếm số câu hỏi.
- **Học được gì:** Số lần hỏi không phải chỉ số tốt cho gánh nặng người dùng; cần đo tần suất và chất lượng câu hỏi, và agent tránh hỏi lại câu đã có câu trả lời qua bộ nhớ bền vững.
- **Áp dụng cho bạn:** Nếu bạn dùng agent hỗ trợ khách hàng hỏi khách nhiều câu, hãy giới hạn chỉ 1–3 câu hỏi làm rõ mỗi phiên và nhớ câu trả lời trước của khách để không hỏi lại, tránh làm phiền khách hàng.

### [10] Explore or Confirm (Wellocate): Agent phân bổ ngân sách thí nghiệm giữa khám phá và xác nhận (arXiv 2610.25111v1)
- **Làm gì:** Một tiêu chuẩn (Wellocate) đo lường agent phân bổ ngân sách thí nghiệm giữa khám phá (explore) và xác nhận (confirm) dưới độ ồn; agent thường lạm dụng xác nhận (chạy lại ứng viên hàng đầu) và bỏ sót ứng viên tốt hơn.
- **Học được gì:** Không có quy tắc cố định nào tốt ở mọi nơi; phân bổ ngân sách đo lường phải đọc mức độ ồn và tự nhiên cảnh quan; agent cần danh sách ứng viên bên ngoài để không cạn kiệt không gian tìm kiếm.
- **Áp dụng cho bạn:** Nếu bạn chạy thử nghiệm quảng cáo hoặc A/B test, hãy không chỉ kiểm tra lại ứng viên tốt nhất mà cũng khám phá các ứng dụng mới, và thiết lập vòng kiểm tra lại ứng viên hàng đầu vào cuối chiến dịch để tránh chọn sai do đọc may mắn.

---

*Báo cáo này được viết lại theo quy trình fallback (pitfall 27) sau khi phát hiện bản xuất bản đầu tiên của daily_summary.py bị nhiễm logic nội bộ của LLM (reasoning leakage, header trùng lặp, sai số lượng bài). Dữ liệu lấy từ 10 bài đã distill trong ngày.*
