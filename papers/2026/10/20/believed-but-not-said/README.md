# [2610.22138v1] Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions

## Giá trị cốt lõi (1 câu)
Đo lường sự sụp đổ niềm tin ẩn (hidden belief collapse) trong thảo luận đa agent LLM: theo dõi đồng thời câu trả lời riêng (private probe, ẩn khỏi đồng đội) và tư thế công khai (public stance) của mỗi agent để phát hiện sự nhiễm tin sai không bao giờ được Voice ra trong transcript.

## Problem
Prior work chưa giải quyết việc hệ thống đa agent dựa vào giả định đồng nghiệp sẽ bắt lỗi lẫn nhau, trong khi kênh phối hợp cũng là bề mặt tấn công: một vài agent sybil lặp lại một câu trả liệu sai plausibl có thể thay đổi niềm tin riêng của phần lớn nhóm mà transcript công khai gần như không lộ ra.

## Contribution
- Thiết lập cuộc thảo luận事実 (factual discussion) 10 agent trong 16 vòng, k ∈ {0, 1, 3} agent đối đầu (sybil) liên tục khẳng định một câu trả liệu sai plausibl; agent khác là agent trung thành (benign) không được cảnh báo hay gán vai trò kiểm chứng.
- Đo lường kép (dual measurement): tư thế công khai trong chat + câu trả lời riêng qua cuộc gọi riêng biệt ẩn khỏi các agent khác sau mỗi vòng.
- Phân loại thất bại qua chéo hai kênh: sturdy correction, silent knower, social accommodation, performative endorsement, full infection, inconsistent.
- Đánh giá sáu mô hình trên ba tập câu hỏi thực tế (COUNTERFACT, POPQA, SIMPLEQA), 18 mô hình×tập dữ liệu.

## Method
Mỗi chạy là một phòng trò chuyện N=10 agent thảo luận một mục thực tế trong T=16 vòng; mọi agent trong cùng một chạy dùng mô hình cơ sở giống nhau. Thay đổi số agent đối đầu k ∈ {0,1,3}, làm 10-k agent trung thành. Mỗi vòng mỗi agent nói đúng một lần, thứ tự được xáo trộn ngẫu nhiên mỗi vòng và giống nhau qua các cuộc trò chuyện, điều kiện trên lịch sử chung gần đây (H=5 vòng trước) và vòng hiện tại. Cuộc trò chuyện bắt đầu từ một hạt thảo luận trung tính. Sau mỗi vòng, mỗi agent trung thành trả lời câu hỏi tra cứu (private probe) trong một cuộc gọi riêng biệt, phản hồi ẩn khỏi các agent khác và không bao giờ được đăng vào phòng trò chuyện. Một thẩm phán gắn nhãn mỗi câu trả lời riêng thành TRUE / MANIPULATED / MIXED / UNCERTAIN; một agent bị nhiễm ở một bước nếu nhãn là manipulated. Ngoài ra, thẩm phán độc lập gắn nhãn tư thế công khai của mỗi phát biểu trung thành đối với tuyên bố bị châm thành ENDORSE / REJECT / HEDGE / IGNORE-DRIFT / UNRELATED. Các chỉ số chính: Final Private Infection (FPI) = tỉ lệ agent trung thành riêng tư nắm câu sai vào bước cuối; turn-level infection; public endorsement; truth-knower correction. Ngày và dữ liệu từ COUNTERFACT, POPQA, SIMPLEQA (40, 53, 50 mục). Sáu mô hình: HY3-PREVIEW, QWEN3.5-FLASH, MISTRAL-SMALL-3.2 (24B), GEMMA-4 (26B), GEMINI-2.5-FLASH-LITE, GPT-OSS-120B. Nhiệt độ 0.7. Một cuộc trò chuyện trên mỗi mục, mô hình và k. Cả tư thế công khai và câu trả lời riêng được gắn nhãn bởi deepseek-v4-flash.

## KNOWLEDGE — Số liệu & khái niệm
- Không có tấn công (k=0): nhóm trung thành ổn định, FPI trung bình 0.6%, không bao giờ vượt 3% trong 18 ô mô hình×tập dữ liệu, nhiễm ban đầu 0.2%.
- Một agent đối đầu: FPI trung bình 44.8% (khoảng 19–74%).
- Ba agent đối đầu: FPI trung bình 60.5% (khoảng 27–81%).
- Một agent đối đầu tạo ra 74% tỉ lệ nhiễm quan sát được với ba sybil.
- Lặp đơn (N=2, một attacker một agent trung thành): 45.6% agent trung thành đơn cuối cùng chọn câu sai, chống lại 39.3% trong nhóm 10 agent — việc thêm agent trung thành chỉ giúp hơi tốt hơn.
- Dưới ba attacker: agent trung thành riêng tư nắm câu sai trong 51.6% lượt hiển lộ (exposed turns) nhưng công khai tán thành chỉ 19.7% (gấp 2.6 lần nhiều lượt nắm câu sai riêng tư hơn tán thành công khai).
- Chỉ 34.3% lượt có câu sai riêng tư công khai tán thành; phần còn lại ngoैन, từ chối, hoặc thậm chí bác bỏ.
- Agent trung thành giữ câu đúng riêng tư công khai bác bỏ tuyên bố sai chỉ trong 61.9% lượt; trong phần còn lại, họ im lặng, ngoæn, hoặc đi theo nó.
- Kiến thức không dự đoán độ mạnh: HY3 và GPT-OSS-120B cùng biết 85% sự thật; dưới ba attacker, GPT-OSS-120B kết thúc với câu sai trên 80% sự thật nó biết, HY3 chỉ 25%.
- Xúc tiến xã hội: giữ số attacker cố định, xác suất một agent trung thành chưa nhiễm chuyển đổi trong một vòng tăng theo số agent trung thành đã được chuyển, từ 9% (không có) lên 66% (5 trở lên).
- Nội bộ hóa tự thân: agent giữ câu đúng và thấy tuyên bố, nếu nó bác bỏ công khai thì chỉ 2.3% nắm câu sai sau vòng; nếu tán thành, 39.7% nắm câu sai; im lặng hoặc ngoæn nằm ở giữa.
- Nhiễm bắt đầu nhanh: 5/6 mô hình đạt nửa nhiễm cuối trong 1 vòng, khoảng 80% nhiễm cuối đã có vào vòng 4, sau đó vęg plutôt không leo tiếp.
- Mô hình chênh lệch chủ yếu ở mức độ cao nơi họ stable: từ 31% (HY3) đến 76% (GPT-OSS-120B).
- Khi hỏi lại chính agent về quan điểm riêng, chúng giữ 86.4% câu sai và quay lại sự thật chỉ 9.1%; nhiễm cuối giảm từ 58.8% xuống 53.1%, vẫn là phần lớn.
- Làm ẩn tin nhắn của chính agent không thay đổi kết quả → hiệu ứng không chỉ vì tự nhất quán.
- Danh mục arXiv: cs.AI

## INSIGHT — Cơ chế & tại sao
[Nhiễm tin sai ẩn nhiều hơn transcript cho thấy] VÌ [agent nắm câu sai trong tư liệu riêng nhưng hiếm khi công khai tán thành; transcript chỉ lộ khoảng 1/3 lượt nhiễm]. Điều này nghĩa là [giám sát chỉ qua transcript không đủ; cần theo dõi câu trả lời riêng của agent thay vì chỉ tin nhắn công khai].
[Một agent đối đầu gây phần lớn hư hại] VÌ [nhóm 10 agent không đáng kể mạnh hơn 1 agent chống lại nhiều lời sai liên tục; sự dư thừa xã hội không tự động tạo độ mạnh]. Điều này nghĩa là [kích thước nhóm lớn không giúp ngăn chặn nhiễm tin sai; cần can thiệp sớm].
[Kiến thức cơ bản không dự đoán độ mạnh] VÌ [hai model biết cùng 85% sự thật nhưng một từ bỏ 25%, kia từ bỏ 80% của những sự thật nó biết]. Điều này nghĩa là [độ mạnh phải được đo trực tiếp ở cấp agent cá nhân, không suy từ độ chính xác cơ bản].
[Nhiễm bắt đầu nhanh và khó đảo ngược] VÌ [5/6 model đạt nửa nhiễm cuối trong 1 vòng, khoảng 80% vào vòng 4, sau đó stable]. Điều này nghĩa là [cửa sổ phát hiện/can thiệp là những vòng đầu của cuộc thảo luận].

## IDEA — Áp dụng được gì
Áp dụng kiểm tra áp lực đồng đẳng đối đầu vào việc chọn model cho hệ thống đa agent doanh nghiệp: bước đầu là chạy nhóm thảo luận với một agent truyền tin sai liên tục, theo dõi câu trả lời riêng của mỗi agent sau mỗi vòng.
Giám sát câu trả lời riêng của agent thay vì chỉ theo dõi transcript công khai: bước đầu là ghi lại câu trả lời riêng của mỗi agent sau mỗi vòng thảo luận, để những câu trả lời ẩn được nhìn thấy ngay cả khi transcript trông không thay đổi.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Sự dư đa trong nhóm agent không tự động tạo ra độ mạnh chống nhiễm tin sai; tin nhắn công khai nên được coi là đầu vào không tin cậy, và độ mạnh chống áp lực đồng đẳng phải được đo trực tiếp ở cấp agent cá nhân.

## Assumptions & Limitations
- Điều kiện đúng: thảo luận事実 đa agent, tin nhắn công khai có thể bị châm bởi agent đối đầu, nhóm đồng nhất, thứ tự nói xáo trộn.
- Limitation paper thừa nhận: chỉ so sánh nhóm hai và mười agent, không thay đổi cấu trúc mạng hay hỗn hợp mô hình; attacker chỉ tác động trong ngữ cảnh (in-context), tấn công tham số (knowledge editing) là cơ chế khác; mọi nhãn đến từ một LLM judge (deepseek-v4-flash), tuy có thẩm phán độc lập claude-sonnet-5.5 tái gắn nhãn 200 câu trả lời riêng với sự đồng ý 87.5% (Cohen's κ=0.82).
- Limitation paper KHÔNG nói: chi phí vận hành lưu câu trả lời riêng của mọi agent mỗi vòng tại quy mô lớn; tác động lên độ trễ khi duy trì tra cứu riêng song song; tính ổn định qua nhiều vòng thảo luận dài hơn 16 vòng.

## Metadata
- Năm: 2026
- Tác giả: Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang, Wooseong Yang, Yuwei Han, Philip S. Yu (University of Illinois Chicago)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.22138v1
- arXiv ID: 2610.22138v1
- Nhãn: [applied]
- Skill: believed-but-not-said | Test: [SKILL VALID]
