# [2609.26048v1] FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents

## Problem
- Ngôn ngữ mô hình (language-model agent) thường đạt giải pháp hoạt động rồi thất bại trong việc triển khai đi triển khai lại (delivered success). Prior work chưa giải quyết được mất mát thủ tục (procedural loss) — model đã tạo ra chất của giải pháp nhưng hệ thống mất đi nó trong giao hàng — vì tập trung vào hỏi model tự kiểm tra (reflection, self-refinement) hoặc tăng năng lực model, thay vì can thiệp tại tầng điều khiển (agent harness).

## Contribution
- Runtime policies: hướng dẫn ngôn ngữ mục tiêu và từ chối hành động (action denial) do agent harness áp dụng tại trạng thái trước thất bại, không thay đổi trọng số model hay prompt người dùng.
- Política abstraction P = (E, G, A, R, S): điều kiện đủ điều kiện (eligibility predicate), điều kiện thời gian chạy (runtime predicate), can thiệp (intervention), điều kiện giải phóng (release condition), theo dõi trạng thái (state tracking).
- Phương pháp xây dựng và đóng băng (freeze) danh sách chính sách (policy portfolio) từ lần thử thất bại.

## Method (tóm tắt cốt lõi)
- Chạy agent không chính sách hai lần trên mỗi nhiệm vụ, kiểm tra thất bại 1/2 và 0/2 để tìm bỏ sót thủ tục rõ ràng.
- Nhóm theo cơ chế, đăng ký chuỗi trạng thái → can thiệp → hành động → điều kiện trình xác minh (verifier condition), viết predicate không ghi tên nhiệm vụ.
- Sàng lọc ứng cử viên trên nhiệm vụ dương và gần-am (nearby-negative), sửa hoặc nghỉ hưu (retire) ứng cử viên vô dụng, quá rộng, hoặc có hại.
- Chính sách vào danh sách đóng băng chỉ khi có trạng thái thất bại có thể quan sát, kết quả tập trung tích cực, và kiểm tra định tuyến (routing audit).
- Danh sách Terra đóng băng: 8 họ (families) trong 7 tệp nguồn và 11 quy tắc.

## Key Findings
- Terminal-Bench 2.1, 87 nhiệm vụ, 2 lần thử: Luna pass∧2 50.6%→54.0%, Terra 55.2%→60.9%, Sol 64.4%→73.6%.
- Sol: pass@2 gần như không đổi (+1.2 điểm) nhưng pass∧2 tăng 9.2 điểm — chính sách chuyển thành công giữa-turn thành thành công lặp đi lặp lại.
- Thử nghiệm năm cánh (five-arm panel): chính sách thực đạt 61% trên 14 nhiệm vụ đủ điều kiện, so với 39% không chính sách, 36% giả (sham), 39-43% xác minh / xem xét chung chung.
- Hành động khắc phục được ghi nhận trong 22/24 lần thử chính sách thực, đối với tối đa 14 trong mọi cánh khác.
- Terra với chính sách đạt 71.4% trên 14 nhiệm vụ được bao phủ, so với 64.3% Sol không hỗ trợ, với khoảng một nửa chi phí ($7.19 vs $14.48).

## Actionable Insights
1. Chính sách thời gian chạy (runtime policy) làm cho khả năng model đã có lặp lại được nhiều hơn, không cần thay đổi model. Áp dụng: thêm Policy Engine vào agent harness, lắng nghe sự kiện stop và before-tool-call, inject hướng dẫn khi phát hiện trạng thái rủi ro (server chưa tách khỏi phiên, database mở trước khi sao chép).
2. Nội dung chính sách quan trọng hơn thời điểm — hướng dẫn chung chung như "xem lại công việc" không giúp. Áp dụng: viết chính sách cụ thể cho từng thất bại thủ tục (duy trì dịch vụ, bảo tồn bằng chứng database) thay vì dùng prompt chung chung.

## Assumptions & Limitations
- Hai lần thử mỗi nhiệm vụ, pass∧2 là tỷ lệ quan sát, không phải ước tính dài hạn.
- Nhiệm vụ bảng điều khiển đến từ dân số phát triển (development population).
- Rằng buộc: một bản tiếng Anh (Terminal-Bench 2.1), một harness (Codex CLI), một họ model, một nỗ lực suy luận (reasoning effort).
- Model nhận dạng bởi tuyến cung cấp (provider route) thay vì mã điểm kiểm tra bất biến (immutable checkpoint hash).
- Chính sách chỉ nhắm vào mất mát thủ tục, không phải kiến thức hoặc năng lực bị thiếu.
- Không nói rõ: xây dựng chính sách đòi hỏi quan sát thất bại trước; danh sách chính sách riêng cho từng model.

## Metadata
- Năm: 2026, tác giả: Nikita Agarwal, Nivedit Jain (Failproof AI), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2609.26048v1
