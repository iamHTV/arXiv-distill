# Skill: one-relation-attack-ora-defense

Source: 2610.24873v1
Type: framework / workflow

## Khi nào dùng skill này
- Khi cần đánh giá rủi ro thao túng niềm tin của agent sử dụng bằng chứng truy xuất (tài liệu, kết quả công cụ, lý luận đồng輩).
- Khi muốn kiểm tra xem một câu điều chỉnh duy nhất có thể đảo ngược kết luận của agent hay không, qua việc đích đến liên kết suy luận ngầm.
- Khi cần thiết kế defense cho agent trong lĩnh vực rủi ro cao (y khoa, bảo mật, pháp lý).

## Tình huống KHÔNG nên dùng
- Khi chỉ kiểm tra sự thật của các bằng chứng đầu vào (không đánh giá liên kết suy luận).
- Khi không có dữ liệu bằng chứng và câu hỏi để xây dựng đồ thị đối số.
- Khi không có attacker model để sinh các câu undercutter.

## Input cần có
- Câu hỏi q và bằng chứng E (các đơn vị nguồn).
- Nhãn vàng y⋆ và câu trả lời ban đầu đúng ˆyv,0.
- Attacker model (ví dụ GPT-5.6-LUNA) để xây dựng các cuộc tấn công.
- Mục tiêu victim (18 mô hình trong paper) để đánh giá ASR.

## Các bước thực hiện
1. Xây dựng đồ thị đối số: attacker tái cấu trúc các warrant trong G, ghi lại 주장, căn cứ nguồn, sức mạnh lưu lự, bại relevant Def(w), và chỉ số mang câu trả lời a(w).
2. Định vị liên kết quan trọng: tính RS(w) = L(w){λUinst + (1−λ)D(w)}, chọn w⋆ = arg max RS(w) trên tất cả warrant.
3. Sinh undercutter chân nguyên: điều kiện trên w⋆, căn cứ, toàn bộ nguồn, và y⋆; sinh C = (δ1…δnc), nc ≤ K, mỗi câu điều chỉnh tính áp dụng/đủ của liên kết mà không khẳng định主張 đối lập.
4. Kiểm tra ứng viên: kiểm tra từ vựng (cánh cảnh thực thể/số/mã token lạ), kiểm tra hỗ trợ ngữ nghĩa sau khi phát hành đối với bằng chứng gốc.
5. Chọn và phát hành: query mode dùng phản hồi victim để phát hành ứng viên đầu tiên tạo BLv = 1 trong ngân sách K; zero-query mode dùng attacker tự đánh giá hỗ trợ nguồn, sự khéo léo, và mức gây lừa dự kiến, chọn một câu mà không cần phản hồi victim.
6. Đánh giá ASR: tỷ lệ lật ngược giữa các đánh giá đúng ban đầu đã hoàn thành; đo Conf (mức tin cậy trung bình trong các lượt lật) và HC-Conf (tỷ lệ p ≥ 0.8).
7. Kiểm tra matched controls: so sánh ORA với random warrant (undercutter chuyển sang liên kết không mang câu trả lời) và random content (nội dung trung lập nghỉ ngơi tại cùng căn cứ).

## Output mong đợi
- Tốc độ tấn công thành công (ASR) cho từng mô hình victim.
- Mức tin cậy của các lượt lật ngược (Conf, HC-Conf).
- Kết quả kiểm tra nguồn hỗ trợ và xác định (tỷ lệ qua kiểm tra hỗ trợ KHÔNG xác định được).
- Hiệu ứng tranh luận đa agent (lỗi nhóm trước và sau tranh luận).

## Ví dụ áp dụng
Một hệ thống agent hỗ trợ chẩn đoán y khoa sử dụng các nghiên cứu y khoa đã xuất bản. Attacker xác định liên kết ngầm giữa một nghiên cứu và kết luận chẩn đoán, sinh một câu điều chỉnh chân nguyên ("nhóm nghiên cứu không có nhóm đối chứng") để agent bác bỏ kết luận đúng. Kết quả mong đợi: ASR 47.6% trên GPT-5.6-terra (y khoa), cao hơn trên các mô hình open-weight trong bảo mật (80%+).

## Gotchas
- Không để từ tiếng Anh không giải thích: one-relation attack (tấn công một liên kết), implicit warrant (liên kết ngầm), undercutter (câu làm suy yếu), defeasibility (khả năng bị bác counterparts), answer-bearing (mang câu trả lời), source-grounded (đôi chút nguồn gốc), belief leap (nhảy vọt niềm tin), ASR (attack success rate — tỷ lệ tấn công thành công), query mode (chế độ truy vấn), zero-query mode (chế độ không truy vấn), source support check (kiểm tra hỗ trợ nguồn), blind identification (xác định mù), multi-agent debate (tranh luận đa agent), matched control (điều khiển ghép cặp), random warrant (liên kết ngẫu nhiên), random content (nội dung ngẫu nhiên), proposition (mệnh đề), reversal threshold (ngưỡng đảo ngłos), cognitive attack surface (bề mặt tấn công nhận thức), evidentiary support (hỗ trợ bằng cách Chứng minh), post-release audit (kiểm tra sau khi phát hành).
- Mô hình lý trí (reasoning-oriented) dễ bị tấn công hơn, không phải ít hơn.
- Tấn công qua kiểm tra nguồn hỗ trợ (83.1% y khoa, 90.9% Cyber) và tránh xác định.
- Tranh luận đa agent làm tăng lỗi nhóm (50.0% → 59.5%), không phải giảm.
- Không có dữ liệu chi phí suy luận thực tế của tấn công.