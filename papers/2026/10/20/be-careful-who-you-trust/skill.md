# Skill: be-careful-who-you-trust
Source: 2609.31704v1
Type: framework

## Khi nào dùng skill này
- Đánh giá độ mạnh phối hợp của nhóm agent LLM khi thông tin công khai có thể bị hỏng/biến đổi.
- Cần phân biệt rễ rễ của sự cố phối hợp: do agent thay đổi hành vi hay do biến đổi hành động công khai do hệ thống.
- Có hệ thống multi-agent với thông tin công khai được chia sẻ (transcript).

## Tình huống KHÔNG nên dùng
- Đánh giá chỉ dựa trên transcript công khai mà không ghi lại hành động gốc.
- Kết luận về "điểm lật nghịchBehavioral tipping point" chỉ từ mức sụp đổ trên transcript công khai.

## Input cần có
- Hệ thống multi-agent chơi trò chơi phối hợp (ví dụ Stag Hunt) với thông tin công khai.
- Cơ chế ghi lại hành động gốc (pre-flip) của mỗi agent trước khi biến đổi.
- Cơ chế ghi lại hành động công khai (post-flip) hiển thị trong transcript.
- Ngưỡng phối hợp M và tổng số agent N.
- Cấu trúc trả giá (payoff matrix) để tính ngưỡng cắt-off q*.

## Các bước thực hiện
1. Thiết lập trò chơi phối hợp N agent: mỗi agent chọn hành động gốc rt_i ∈ {Stag, Hare}, nói theo thứ tự cố định, căn cứ vào transcript công khai.
2. Ghi lại hành động gốc của mỗi agent (lựa chọn trước khi bất kỳ biến đổi nào xảy ra).
3. Nếu có agent bị chỉ định hỏng (corrupted), mô phỏng biến đổi hành động công khai (ví dụ đảo ngược Stag↔Hare) và sinh lý do mới phù hợp; agent sau đó chỉ nhận báo cáo đã biến đổi.
4. Tính thành công trước khi đảo (pre-flip success): áp ngưỡng M vào hành động gốc của tất cả agent.
5. Tính thành công công khai (public success): áp ngưỡng M vào hành động post-flip dùng để thực thi.
6. Tính lực thực hiện (realised payoff) từ hành động post-flip và lực thực thi thành thật (truthful-implementation payoff) từ hành động gốc; khoảng cách giữa hai giá trị cho biết thành phần cơ học.
7. Dùng benchmark báo cáo công khai đơn giản (naive aggregate): tính tỉ lệ báo cáo Stag công khai quan sát được, so sánh với ngưỡng q* (mức tỉ lệ Stag cần thiết để E[U_Stag] ≥ Hare payoff).
8. Đánh giá sự khớp mô tả: tỷ lệ lượt agent chọn hành động gốc khớp với hành động gợi ý bởi benchmark.

## Output mong đợi
- Phân tích rõ ràng mức độ sụp đổ phối hợp là do agent thay đổi hành vi hay do biến đổi hành động công khai; có thể dùng benchmark đơn giản để mô tả quyết định phối hợp của agent.

## Ví dụ áp dụng
- Hệ thống chăm sóc khách hàng đa agent: ghi lại cả quyết định gốc của mỗi agent và quyết định công khai gửi đến khách; khi tỷ lệ thành công giảm, dùng bước 4-6 để xem giảm do agent làm sai hay do hệ thống biến đổi tin nhắn công khai.

## Gotchas
- Không kết luận sự thay đổi hành vi chỉ từ sự sụp đổ trên transcript công khai — phần lớn có thể là cơ học (mechanical).
- Thành công trước khi đảo không phải반 Durchschnitt no-corruption, vì các hành động gốc sau có thể đã phản ứng với báo cáo hỏng trước đó.
- Benchmark là quy tắc mô tả chưa sửa theo mức hỏng; không dùng làm chính sách tối ưu chống hỏng.
- Nhóm đồng nhất và thứ tự nói cố định trong paper; kết quả có thể khác với nhóm lẫn mezcla thứ tự nói tự do.

## Kiểm tra kỹ năng (self-check)
- Người không đọc paper gốc có follow được 8 bước trên không? [YES] — từng bước là action cụ thể.
- Bước nào mơ hồ nhất? Bước 7 (tính ngưỡng q* từ payoff matrix) cần hiểu công thức Stag Hunt.
- Input section có đủ không? [YES] — hệ thống multi-agent, ghi hành động gốc/công khai, ngưỡng M, số agent N, trả giá.

## Dry run (tình huống giả)
- Tình huống: Công ty có 5 agent điều phối để chọn nhà cung cấp, ngưỡng M=3 agent đồng ý; thông tin công khai có thể bị biến đổi.
- Chạy skill: (1) Thiết lập trò chơi 5 agent, mỗi agent chọn đồng ý/không đồng ý; (2) ghi quyết định gốc của mỗi agent; (3) biến đổi quyết định công khai của 2 agent bị hỏng; (4) tính thành công trước khi đảo từ 5 quyết định gốc; (5) tính thành công công khai từ 3 quyết định chưa đổi + 2 đã đổi; (6) tính lực thực hiện và khoảng cách cơ học; (7) dùng benchmark naive aggregate so với ngưỡng q*; (8) nếu khoảng cách lớn chủ yếu là cơ học, sửa hệ thống truyền tin chứ không phải thay đổi prompt agent.

## Verdict: [SKILL VALID]
