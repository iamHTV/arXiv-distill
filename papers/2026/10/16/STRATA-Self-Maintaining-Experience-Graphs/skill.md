# Skill: strata-self-maintaining-experience-graphs
Source: 2610.19386v1
Type: framework

## Khi nào dùng skill này
- Xây agent tự phát triển (self-evolving agent) tại test time bằng cách tích lũy kinh nghiệm từ các lần chạy trước.
- Muốn agent có thể truy xuất kinh nghiệm liên quan trước khi hành động và viết lại bài học mới sau đó.
- Muốn tránh negative transfer (chuyển consumo tiêu cực) khi kinh nghiệm cũ không liên quan làm sai kết quả.

## Tình huống KHÔNG nên dùng
- Chỉ dùng agent đơn lần (one-shot), không có quá trình tự phát triển.
- Không cần bộ nhớ kinh nghiệm, chỉ cần agent trả lời từ kiến thức nội bộ.

## Input cần có
- Các lần chạy trước của agent (trajectories, episodes, traces).
- Hệ thống lưu trữ và truy xuất kinh nghiệm (memory system).
- Cơ chế phân cấp (metas, episodes, traces) và cơ chế bảo trì (grow, generalize, forget).

## Các bước thực hiện
1. Thu thập các kinh nghiệm của agent từ các lần chạy trước (trajectories, episodes, traces).
2. Tổ chức kinh nghiệm thành hệ thống phân cấp ba cấp: metas (khái niệm cấp cao), episodes (tập sự kiện), traces (vết dấu chi tiết).
3. Xây năm cơ chế bảo trì: tạo ra (grow), tổng quát hóa (generalize), và quên (forget) kinh nghiệm.
4. Trước khi agent hành động, truy xuất kinh nghiệm liên quan từ metas/episodes/traces phù hợp.
5. Sau khi agent hành động, viết lại bài học mới vào bộ nhớ và áp dụng cơ chế quên để loại trừ kinh nghiệm không hữu ích.

## Output mong đợi
- Deletion precision: 13.2% → 4.8% (cải thiện gần ba lần trong độ chính xác xóa kinh nghiệm không liên quan).
- Churn: 28.6% → 3.1% (tỷ lệ thay đổi bộ nhớ giảm mạnh).
- Điểm số trung bình tốt nhất ở độ trễ thấp nhất và ít bước môi trường nhất so với mọi memory baseline.

## Ví dụ áp dụng
Solopreneur xây agent hỗ trợ khách hàng tự học: agent lưu lại các cuộc hội thoại trước thành các experiences, tổ chức thành metas (các loại vấn đề), episodes (các cuộc hội thoại cụ thể), traces (các bước chi tiết). Trước khi trả lời khách hàng mới, agent truy xuất kinh nghiệm liên quan từ metas/episodes phù hợp. Sau mỗi cuộc hội thoại, agent viết bài học mới và xóa các kinh nghiệm không còn hữu ích.

## Gotchas
- Không nên để tất cả kinh nghiệm nằm trong một bế không phân biệt: dễ bị negative transfer khi kinh nghiệm bề mặt tương tự nhưng hướng đi ngược lại được triệu hồi.
- Cần cơ chế quên và loại trừ kinh nghiệm cũ: không nên giữ mọi thứ vĩnh viễn trong bộ nhớ.
- Cần thiết kế hệ thống phân cấp (metas → episodes → traces) phù hợp với domen của bạn.
