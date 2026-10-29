# [2610.35981] Small agents should know what their tools do

## Giá trị cốt lõi (1 câu)

Huấn luyện agent nhỏ (small open language models — mô hình ngôn ngữ mở nhỏ) hiểu tác dụng của mỗi công cụ thông qua khai báo hiệu ứng (effect declarations — tuyên bố về tác dụng của công cụ đối với thế giới) giúp đạt 99% thành công tác vụ trong phân phối và chỉ tốn khoảng 1/3 token đầu ra, thay vì chỉ kiểm tra cú pháp gọi hàm như các benchmark công khai.

## Problem

Công cụ gọi hàm (tool-calling agent — agent có khả năng gọi công cụ bên ngoài) nhỏ có thể gọi công cụ nhưng không suy nghĩ xem một cuộc gọi làm gì đến thế giới: xóa mà không hỏi, ghi lại nhiều lần, đọc lại trạng thái đã có, và gọi một lần mỗi lượt thay vì viết chương trình ngắn. Các benchmark công khai như BFCL (Berkeley Function-Calling Leaderboard — bảng xếp hạng gọi hàm Berkeley) chỉ chấm xem một cuộc gọi có được định dạng đúng hay không, không chấm xem agent có đọc lại dữ liệu đã có, có serialise (chuyển đổi thành chuỗi) các tra cứu độc lập, hay hủy một cuộc họp mà không hỏi. Các công cụ đã được gắn nhãn chỉ đọc (read-only), hủy (destructive) hoặc idempotent (idempotent: gọi nhiều lần như gọi một lần) nhưng các mô hình mở nhỏ (small open models) không được huấn luyện để hành động theo các chú thích đó, và chú thích thường không bao giờ đến mô hình.

## Contribution

1. EffectWorld: một thế giới công cụ có kiểu hiệu ứng (effect-typed executable tool world — thế giới công cụ thực thi mà mỗi công cụ có loại hiệu ứng rõ ràng) với trình xác thực phát lại (replay verifier — công cụ kiểm tra bằng cách phát lại vết ghi thực thi), người dùng kịch bản (scripted user — người dùng được lập trình sẵn phản hồi định trước), một miền huấn luyện và hai phân đoạn chỉ kiểm tra (test-only splits): một phân đoạn khó (hard split) với loại tác vụ chưa thấy và công cụ gây nhiễu (distractor tools), và một phân đoạn mua sắm trực tuyến (commerce domain — miền mua sắm trực tuyến).
2. Tool programs: một quy ước $ref tối thiểu cho phép một lượt trợ lý (assistant turn — lượt phản hồi của mô hình trợ lý) biểu diễn mộtồ đồ phụ thuộc (dependency graph — đồ thị biểu diễn quan hệ phụ thuộc giữa các tác vụ) của các cuộc gọi bên trong các khối gọi công cụ gốc (native tool-call blocks), để các trình phân tích cú pháp (parsers) và benchmark hiện có vẫn hoạt động.
3. Trình tối ưu hóa vết dấu (trace optimizer — công cụ tối ưu hóa vết ghi thực thi) theo kiểu compiler (kiểu trình biên dịch) với tính hợp pháp dựa trên bước chân (footprint-based legality — tính hợp pháp dựa trên tập tài nguyên đọc/ghi), và một thóc phân (taxonomy — hệ phân loại) 19 lớp mẫu tiêu cực (negative classes — các mẫu hành động sai được gán nhãn là tiêu cực) được lấy từ các diffs (sự khác biệt giữa hai bản) của nó.
4. So sánh kiểm soát hai mục tiêu phân áp (UL — unlikelihood training, NPO — negative preference optimisation) đối với DPO (direct preference optimisation — tối ưu hóa ưu tiên trực tiếp) và một điều khiển SFT (SFT control — nhóm đối chứng chỉ huấn luyện giám sát), tất cả được tiếp tục từ cùng một bộ điều chỉnh SFT (SFT adapter — bộ điều chỉnh cấp thấp được huấn luyện theo phương pháp fine-tuning (huấn luyện giám sát tinh chỉnh)). Không có mục tiêu nào thắng nhóm đối chứng trên bất kỳ phân đoạn kiểm tra nào.
5. Hai phát hiện về dữ liệu: mẫu từ chối (refusal templates — mẫu câu từ chối kiểu sẵn có) trong dữ liệu công cụ sử dụng công khai làm sập sẵn sàng gọi công cụ của mô hình nhỏ trên BFCL, và lọc chúng khôi phục lại.

## Method

EffectWorld xây dựng các công cụ có khai báo hiệu ứng (effect declarations): mỗi công cụ có loại hiệu ứng (pure — tính toán từ đối số, không đụng trạng thái; read — đọc trạng thái không thay đổi; write — thay đổi trạng thái có thể khắc phục; destructive — không thể hoàn tác: xóa dữ liệu, liên hệ người khác, chuyển tiền), cờ idempotent (idempotence flag — cờ cho biết gọi hai lần có giống gọi một lần hay không), và bước chân (footprint — tập tài nguyên công cụ đọc và ghi, dạng mẫu theo đối số). Các khai báo này cho phép: (1) trình xác thực phát lại (replay verifier) quyết định xem một vết dấu (trace — vết ghi chuỗi các cuộc gọi) có an toàn về hiệu ứng (effect-safe) hay không không cần nhãn hoặc mô hình phán xét (judge model — mô hình dùng để phán xét), (2) trình thực thi (executor) chạy chương trình công cụ của nhiều cuộc gọi phụ thuộc trong một lượt, và (3) trình tối ưu hóa theo kiểu compiler (compiler-style optimizer) biến vết dấu thải phế thành tín hiệu huấn luyện đã xác minh. Bộ điều chỉnh cấp thấp (LoRA adapter — bộ điều chỉnh låg hạng được thêm vào mô hình) được huấn luyện trên dữ liệu EffectWorld.

Ngôn ngữ mô hình chỉ được biết tên, mô tả và tham số của công cụ (không thấy khai báo hiệu ứng theo mặc định). System prompt nêu năm quy tắc: xác nhận trước hành động không thể đảo ngược, không lặp lại hành động tạo/gửi/thanh toán không idempotent, đọc trạng thái trước khi sửa, hỏi khi thiếu thông tin, và không gọi công cụ khi không cần.

## KNOWLEDGE — Số liệu & khái niệm

- Trên phân đoạn kiểm tra (test split) 498 tác vụ, Qwen3-4B đạt 53% thành công tác vụ ban đầu, SFT (supervised fine-tuning — huấn luyện giám sát tinh chỉnh) nâng lên 99% trong phân phối (in distribution — trên các tác vụ cùng loại dữ liệu huấn luyện).
- Trên phân đoạn khó (hard split) 775 tác vụ với loại tác vụ chưa thấy và công cụ gây nhiễu, từ 52% lên 81% (+29 điểm phần trăm).
- Trên phân đoạn mua sắm (commerce split) 547 tác vụ, công cụ chưa từng thấy trong huấn luyện, từ 74% lên 83%.
- Sử dụng khoảng 1/3 số token đầu ra so với mô hình cơ sở (base model — mô hình chưa được tinh chỉnh).
- Trên BFCL, adapter khớp độ chính xác trực tiếp (live accuracy — độ chính xác trên câu hỏi do người dùng gửi trực tiếp) của mô hình cơ sở và nâng độ chính xác đa lượt (multi-turn accuracy — độ chính xác trên nhiều lượt hội thoại) từ 21.9 lên 26.6, và công thức với near-miss declines (từ chối gần đúng) nâng trung bình BFCL lên 70.0 so với 68.7 của mô hình cơ sở.
- Mẫu từ chối (refusal templates) trong dữ liệu công cụ sử dụng công khai cắt độ chính xác phi trực tiếp (non-live accuracy — độ chính xác trên câu hỏi cố định do benchmark viết) BFCL từ 88.0 xuống 31.4, lọc chúng khôi phục 84.8.
- Ba họ mô hình (Qwen3-1.7B, Phi-4-mini, Falcon3-3B) được nâng từ 4–25% lên 69–99% trong phân phối và +26 đến 55 điểm trên phân đoạn kiểm tra giữ (held-out splits — phân đoạn dữ liệu không dùng trong huấn luyện).
- Trên phân đoạn khó, SFTclean (81.5%) và các biến thể khác đạt từ 77.8% đến 83.7% trong chế độ chương trình (program mode — nhiều cuộc gọi phụ thuộc trong một lượt).

## INSIGHT — Cơ chế & tại sao

[Agent nhỏ gọi công cụ thô thiển — xóa mà không hỏi, ghi lặp lại, đọc lại trạng thái đã có] xảy ra VÌ [chúng được huấn luyện trên dữ liệu chỉ chấm cú pháp gọi hàm, không có khai báo về tác dụng của mỗi cuộc gọi đến thế giới]. Điều này nghĩa là [kiểm tra cú pháp không đủ; agent cần hiểu effect (hiệu ứng) của công cụ trước khi gọi].

[Mẫu từ chối trong dữ liệu công khai dạy mô hình nhỏ không gọi công cụ] xảy ra VÌ [mô hình nhỏ generalizes (quy mô hóa — suy diễn từ một số mẫu sang trường hợp mới) từ các câu từ chối stylized (có kiểu dáng nhất quán)]. Điều này nghĩa là [in-domain metrics (chỉ số trong miền dữ liệu huấn luyện) có thể trông hoàn hảo trong khi năng lực gọi công cụ thực sự bị phá hủy, chỉ benchmark bên ngoài mới phát hiện].

[Mẫu dương (positive examples — ví dụ chính xác) mang theo hoạt động chúng chỉ ra, không phải nhãn] xảy ra VÌ [declines (từ chối gọi công cụ) khi công cụ bỏ lỡ không dạy declines khi công cụ được cung cấp nhưng không phù hợp]. Điều này nghĩa là [cần viết ví dụ dương cho mọi quyết định agent phải đưa ra, bao gồm từ chối, hỏi và xác nhận, thay vì dựa vào mẫu tiêu cực để loại bỏ chúng].

[Khai báo hiệu ứng (effect declarations) giúp chuyển an toàn và hiệu quả thành tính chất có thể kiểm tra của vết dấu] xảy ra VÌ [trình xác thực phát lại (replay verifier) có thể quyết định xem vết dấu có an toàn về hiệu ứng hay không bằng cách phát lại cuộc gọi đối với các khai báo, không cần nhãn hoặc mô hình phán xét]. Điều này nghĩa là [an toàn không cần đánh giá bằng con người hay mô hình phán xét, chỉ cần khai báo công cụ].

## IDEA — Áp dụng được gì

1. Áp dụng khai báo hiệu ứng (effect declarations) vào công cụ agent: mỗi công cụ trong schema nên có loại hiệu ứng (pure/read/write/destructive), cờ idempotent, và bước chân (footprint) tài nguyên đọc/ghi. Cho ai: solopreneur xây dựng agent gọi công cụ (ví dụ agent xử lý đơn hàng, lịch hẹn, email). Bước đầu: thêm trường effect vào định nghĩa công cụ MCP (Model Context Protocol — giao thức ngữ cảnh mô hình, tiêu chuẩn kết nối agent với công cụ) của agent.

2. Áp dụng quy tắc xác nhận trước khi gọi công cụ hủy (destructive call): agent phải đề xuất và chờ người dùng xác nhận trước khi xóa, gửi email hoặc hủy đơn hàng. Cho ai: agent thực hiện hành động không thể đảo ngược (irrevocable action — hành động không thể hoàn tác). Bước đầu: viết system prompt với 5 quy tắc của paper (confirm before destructive, never repeat non-idempotent write, read before write, ask when missing info, don't call when none needed).

3. Áp dụng lọc mẫu từ chối (refusal filter — bộ lọc câu từ chối kiểu sẵn có) trước khi trộn dữ liệu công cụ sử dụng công khai vào huấn luyện agent. Cho ai: đội xử lý dữ liệu huấn luyện agent gọi công cụ. Bước đầu: quét dữ liệu huấn luyện cho các câu từ chối kiểu mẫu như "I don't have access to a tool that can do that" và loại bỏ chúng.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Kiểm tra cú pháp gọi công cụ không đủ; agent phải biết tác dụng của mỗi cuộc gọi đối với thế giới. Áp dụng khi thiết kế agent gọi công cụ trong môi trường có hành động không thể đảo ngược (irrevocable action). Không áp dụng khi agent chỉ truy xuất thông tin chỉ đọc (read-only) và không có hành động ngoài hệ thống.

## Assumptions & Limitations

- Điều kiện phải đúng: công cụ có khai báo hiệu ứng rõ ràng, người dùng có sẵn để xác nhận các cuộc gọi hủy, mô hình nhỏ được huấn luyện trên dữ liệu có chú thích hiệu ứng.
- Limitation paper thừa nhận: EffectWorld nhỏ (9 loại tác vụ, một miền huấn luyện, một miền kiểm tra), người dùng kịch bản (scripted user) không bao giờ thay đổi ý và xác nhận mọi đề xuất, verifier kiểm tra bằng phát lại vết dấu đã ghi không phải chứng minh cho mọi trạng thái, phân tích chi tiết chỉ sử dụng một backbone (Qwen3-4B), tất cả mô hình tối đa 4B tham số, các mô hình từ một hạt giống huấn luyện (training seed) duy nhất.
- Limitation paper KHÔNG nói: khai báo hiệu ứng trên các công cụ thực tế ngoài mô phỏng (ví dụ API công cộng) có thể không nhất quán; chi phí vận hành của trình xác thực phát lại trên quy mô lớn chưa được đánh giá; hiệu ứng dichiaration chưa được kiểm tra trên các agent lớn hơn 4B tham số.

## Metadata

- Năm: 2026
- Tác giả: Alexander Kovalenko, Artem Redchych (Czech Technical University in Prague — Đại học Kỹ thuật Czech tại Prague)
- Category arXiv: cs.SE
- Link PDF: https://arxiv.org/pdf/2610.35981v1
- Citation count: [không tìm được]