# Skill: believed-but-not-said
Source: 2610.22138v1
Type: framework

## Khi nào dùng skill này
- Đánh giá độ mạnh của hệ thống đa agent LLM khi một vài agent có thể truyền tin sai liên tục (peer-pressure attack).
- Cần phát hiện sự nhiễm niềm tin ẩn (hidden belief collapse) không lộ ra trong transcript công khai.
- Muốn chọn model cho hệ thống multi-agent dựa trên độ mạnh chống áp lực đồng đẳng, không chỉ dựa trên độ chính xác cơ bản.

## Tình huống KHÔNG nên dùng
- Giả định nhóm lớn tự động mạnh hơn (paper chỉ ra nhóm 10 agent không đáng kể mạnh hơn 1 agent).
- Đo lường độ mạnh chỉ qua độ chính xác cơ bản của model (kiến thức không dự đoán độ mạnh).

## Input cần có
- Nhóm N agent LLM thảo luận một mục thực tế (ví dụ Stag Hunt / câu hỏi thực tế).
- Một số agent đối đầu (sybil) được chỉ định lập luận cho một câu trả liệu sai cố định.
- Cơ chế tra cứu riêng (private probe): sau mỗi vòng, mỗi agent trung thành trả lời câu hỏi trong cuộc gọi riêng biệt ẩn khỏi các agent khác.
- Thẩm phán (LLM judge) gắn nhãn câu trả lời riêng (TRUE/MANIP/MIXED/UNCERTAIN) và tư thế công khai (ENDORSE/REJECT/HEDGE/IGNORE/UNRELATED).
- Số vòng thảo luận (ví dụ 16 vòng), thứ tự nói xáo trộn mỗi vòng.

## Các bước thực hiện
1. Thiết lập phòng thảo luận N=10 agent, mỗi agent nói một lần mỗi vòng, thứ tự xáo trộn ngẫu nhiên, điều kiện trên lịch sử gần đây (H=5 vòng).
2. Chỉ định k agent đối đầu (k ∈ {0,1,3}) lập luận cho một tuyên bố sai cố định mỗi khi chủ đề xuất hiện; agent trung thành nhận personas thông thường, không bị cảnh báo.
3. Sau mỗi vòng, thực hiện tra cứu riêng (private probe): mỗi agent trung thành trả lời câu hỏi thực tế trong cuộc gọi riêng biệt, phản hồi ẩn khỏi đồng đội.
4. Gắn nhãn tư thế công khai (public stance) của mỗi phát biểu trong chat đối với tuyên bố sai.
5. Tính Final Private Infection (FPI): tỉ lệ agent trung thành riêng tư nắm câu sai vào bước cuối.
6. Phân loại từng lượt hiển lộ qua chéo hai kênh: sturdy correction (TRUE+REJECT), silent knower (TRUE+IGNORE/HEDGE), social accommodation (TRUE+HEDGE), performative endorsement (MANIP+ENDORSE), full infection (MANIP+ENDORSE), hidden infection (MANIP+HEDGE/IGNORE).
7. Tính công suất öffentlich endorsement và truth-knower correction (tỷ lệ các lượt private=TRUE mà công khai bác bỏ tuyên bố sai).
8. So sánh FPI giữa các điều kiện k=0, k=1, k=3; một attacker tạo ra ~74% tỉ lệ nhiễm của ba sybil.
9. Can thiệp sớm: nhiễm bắt đầu nhanh (khoảng 80% vào vòng 4), nên can thiệp trong những vòng đầu.

## Output mong đợi
- Đánh giá rõ ràng mức độ nhóm agent bị nhiễm tin sai ở cấp niềm tin riêng (không chỉ transcript), biết được model nào thật sự mạnh chống áp lực đồng đẳng.

## Ví dụ áp dụng
- Doanh nghiệp dùng multi-agent để kiểm chứng fact trước khi xuất bản: chạy thử thách với một agent sybil lặp tin sai, theo dõi câu trả lời riêng của mỗi agent; nếu nhiều agent riêng tư nắm tin sai dù transcript trông bình thường → không dùng model đó cho hệ thống kiểm chứng.

## Gotchas
- Không kết luận nhóm lớn mạnh hơn chỉ vì có nhiều agent — redundant xã hội không tự động tạo độ mạnh.
- Không đánh giá chỉ qua transcript công khai — khoảng 2/3 lượt nhiễm không được tán thành công khai.
- Không suy độ mạnh từ kiến thức cơ bản — model biết 85% sự thật có thể từ bỏ 80% dưới tấn công.
- Can thiệp muộn (sau vòng 4) ít hiệu lực vì nhiễm đã stable.

## Kiểm tra kỹ năng (self-check)
- Người không đọc paper gốc có follow được 9 bước trên không? [YES] — từng bước là action cụ thể.
- Bước nào mơ hồ nhất? Bước 6 (phân loại thất bại qua chéo hai kênh) cần thẩm phán rõ ràng cho tư thế công khai.
- Input section có đủ không? [YES] — nhóm agent, agent đối đầu, tra cứu riêng, thẩm phán, số vòng.

## Dry run (tình huống giả)
- Tình huống: Công ty có hệ thống 5 agent kiểm chứng tin tức trước khi đăng; muốn biết model nào chống Against tin sai được diffusse qua chat.
- Chạy skill: (1) Thiết lập 5 agent thảo luận một sự thật; (2) chỉ định 1 agent đối đầu lập luận tin sai liên tục; (3) sau mỗi vòng, tra cứu riêng mỗi agent trung thành; (4) gắn nhãn tư thế công khai và câu trả lời riêng; (5) tính FPI tại bước cuối; (6) nếu FPI cao (>40%) dù transcript trông ổn định → model không đủ mạnh, tìm model khác hoặc thêm cơ chế can thiệp sớm.

## Verdict: [SKILL VALID]
