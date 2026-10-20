# [2610.25954v1] CXBENCH: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows

## Giá trị cốt lõi (1 câu)
CXBENCH đánh giá tuân thủ quy trình (process compliance) và kết quả (outcome) riêng biệt cho agent LLM trong các quy trình chăm sóc khách hàng được điều chỉnh: 69.29% executions đạt outcome nhưng chỉ 13.81% đạt cả hai, 55.48% là false-pass (outcome đúng nhưng vi phạm quy trình).

## Problem
Các benchmark agent công cụ hiện tại chủ yếu chấm điểm trạng thái kinh doanh cuối cùng, chấp nhận các quỹ đạo đạt kết quả đúng thông qua quy trình không tuân thủ. Trong các trường hợp được điều chỉnh (ngân hàng, viễn thông, bảo hiểm, y học, tiện ích, trợ chính phủ), agent không chỉ cần đạt kết quả kinh doanh đúng mà còn phải cung cấp thông báo, lấy đồng ý và thủ tục yêu cầu.

## Contribution
1. Đề xuất CXBENCH, benchmark đánh giá outcome và process compliance riêng biệt trên 120 tác vụ trong 6 miền được điều chỉnh.
2. Mã quy tắc (rule cards) gắn nghĩa vụ quy định trích dẫn với bằng chứng quan sát có thể thấy trong vết tích; hybrid grader kết hợp kiểm tra định trị cho thứ tự và thẩm quyền với LLM judge cho yêu cầu ngữ nghĩa.
3. Định nghĩa false-pass: execution đạt outcome nhưng không đạt kiểm tra quy trình — chỉ ra những thất bại bị ẩn bởi chấm điểm chỉ outcome.
4. Chia sẻ thực thi với kiểm soát submitting: runtime chuẩn bị draft, chỉ submit sau khi khách xác nhận các trường khớp; direct-submit mode để nghiên cứu ảnh hưởng của thẩm quyền submit.

## Method
CXBENCH đánh giá mỗi episode trên hai trục: outcome (kết quả kinh doanh đã đạt hay chưa) và process (vết tích tương tác đã thỏa mãn các yêu cầu quy định hay chưa). Mỗi tác vụ bao gồm yêu cầu của khách, môi trường dựa trên công cụ, và yêu cầu quy trình rõ ràng. Agent tương tác với khách giả lập (gpt-5.4-mini) qua cuộc trò chuyện và sử dụng công cụ riêng miền thông qua runtime chung, ghi lại vết tích. Sau khi thực thi, outcome checker đánh giá trạng thái kinh doanh cuối cùng; hybrid process grader kết hợp kiểm tra định trị (thứ tự sự kiện, quyền công cụ, sự đồng nhất giữa trường đã xác nhận và đã gửi) và LLM judge (gpt-5.6-sol) cho yêu cầu ngữ nghĩa dựa trên danh sách kiểm tra riêng nhiệm vụ. Cả hai thành phần phải pass để process verdict pass. Overall success chỉ khi cả hai pass. False-pass = outcome pass ∧ process fail. Runtime default mode: agent chuẩn bị draft, runtime chỉ submit sau khi khách xác nhận các trường khớp theo xác nhận hợp đồng nhiệm vụ; direct-submit mode hiển thị công cụ submit cho agent và tắt submit được trung gian bởi runtime.

## KNOWLEDGE — Số liệu & khái niệm
- 120 tác vụ trên 6 miền được điều chỉnh: ngân hàng, viễn thông, bảo hiểm, y học, tiện ích, trợ chính phủ (20 tác vụ/miền)
- 7 mô hình được đánh giá, 840 bản ghi tổng thể
- Khách giả lập: gpt-5.4-mini; Judge: gpt-5.6-sol
- 53 rule cards (53 nghĩa vụ được trích xuất từ tài liệu quy định qua Legal Information Institute, phân loại thành 53 thẻ)
- 69.29% (582/840) executions đạt outcome check
- 13.81% (116/840) executions đạt cả outcome và process
- 466 false-passes = 55.48% tất cả evaluations, 80.07% của outcome passes
- Phân biệt theo miền: ngân hàng 94.29% outcome-pass nhưng 5.71% both-pass; trợ chính phủ 84.29% và 4.29%; y học 13.57% và 2.14%
- Phân tích false-pass: 329 bị từ chối chỉ bởi LLM judge, 38 chỉ bởi hard rules, 99 bởi cả hai; 35/53 hard rules thất bại ít nhất một lần; quy tắc thứ tự bảo hiểm lặp lại thất bại trong 47 bản ghi false-pass
- Kiểm soát submitting: mediated-submit both-pass 20.83%, direct-submit 0.83%, direct-submit (loại bỏ kiểm tra submitting) 18.33%; false-pass tăng từ 43.33% lên 66.67%
- Cấu hình judge: gpt-6-astra thay đổi pooled both-pass từ 13.89% lên 14.72%, giữ mọi thứ tự cặp nghiêm ngặt (Kendall's τb = 0.9661); hybrid verdicts đồng ý 92.22%
- Độ chính xác judge trên vết phát triển: 88.33%; process pass precision 69.70%, recall 85.19%, F1 76.67%; process failure precision 95.40%, recall 89.25%
- Bảng 3 kết quả theo mô hình: glm-5.1 (outcome 77.50%, both-pass 21.67%, false-pass 55.83%), gpt-5.4 (64.17%, 20.83%, 43.33%), gpt-5.4-mini (61.67%, 15.00%, 46.67%), qwen3.6-plus (70.83%, 15.00%, 55.83%), deepseek-v4-flash (77.50%, 13.33%, 64.17%), qwen3.5-plus (70.83%, 8.33%, 62.50%), gpt-4o-mini (62.50%, 2.50%, 60.00%)
- Stake: deepseek-v4-flash và glm-5.1 empate outcome rate 77.50% nhưng đạt both-pass 13.33% và 21.67%; gpt-5.4 có outcome thấp hơn (64.17%) nhưng both-pass cao hơn deepseek-v4-flash (20.83%)

## INSIGHT — Cơ chế & tại sao
[Outcome-only scoring gián đoạn quá trình tuân thủ] VÌ [các agent có thể đạt trạng thái cuối đúng thông qua quy trình không tuân thủ, chẳng hạn thiếu thông báo bắt buộc hoặc lấy đồng ý; chỉ kiểm tra trạng thái cuối không phát hiện được vi phạm trong tương tác]. Điều này nghĩa là [độ tin cậy của agent bị quá ước lượng nếu chỉ chấm điểm kết quả].
[Hybrid grader phát hiện các lỗi bổ sung nhau] VÌ [kiểm tra định trị đánh giá thứ tự và quyền, LLM judge đánh giá yêu cầu ngữ nghĩa; 329/466 false-pass chỉ bị LLM judge từ chối, 38 chỉ bởi hard rule, 99 bởi cả hai]. Điều này nghĩa là [cả hai loại kiểm tra cần thiết — không loại nào đủ đơn độc].
[Kiểm soát submitting ảnh hưởng lớn đến both-pass] VÌ [khi agent trực tiếp submit (direct-submit), both-pass rơi từ 20.83% xuống 0.83%, false-pass tăng từ 43.33% lên 66.67%; khi loại bỏ các kiểm tra submitting, both-pass là 18.33% — cho thấy khoảng cách gốc là nhạy cảm về cách chấm điểm]. Điều này nghĩa là [thẩm quyền submit là một biến can thiệp thực sự, không chỉ là manifact của đánh giá].
[Thứ tự mô hình thay đổi khi bao gồm process compliance] VÌ [mô hình với outcome cao có thể có process thấp (deepseek-v4-flash outcome 77.50% nhưng both-pass chỉ 13.33%), trong khi gpt-5.4 outcome thấp hơn (64.17%) nhưng both-pass cao hơn (20.83%)]. Điều này nghĩa là [chấm điểm chỉ outcome có thể xếp hạng sai mô hình].

## IDEA — Áp dụng được gì
1. Áp dụng [hybrid grader (định trị + LLM judge)] vào [đánh giá tuân quy trình của agent doanh nghiệp]: bước đầu là xây dựng rule cards gắn nghĩa vụ quy định với bằng chứng trong vết tích, sau đó kết hợp kiểm tra định trị cho thứ tự/quyền và LLM judge cho yêu cầu ngữ nghĩa.
2. Áp dụng [false-pass metric] vào [phát hiện thất bại bị ẩn bởi kết quả đúng]: bước đầu là theo dõi các execution đạt outcome nhưng không đạt kiểm tra quy trình, xem xét chúng là rủi ro tuân thủ tiềm ẩn.
3. Áp dụng [runtime mediated-submit] vào [kiểm soát thẩm quyền gửi hành động kinh doanh]: bước đầu là cấu hình runtime để chỉ submit draft sau khi khách xác nhận các trường khớp, không để agent tự submit trực tiếp.

## WISDOM — Nguyên tắc tổng quát
1. Nguyên tắc: Kết quả đúng không đồng nghĩa với quy trình đúng — agent có thể đạt mục tiêu kinh doanh mà vi phạm quy trình điều chỉnh. Áp dụng khi: đánh giá agent trong môi trường được điều chỉnh (tài chính, y tế, bảo hiểm). Không áp dụng khi: tác vụ không có yêu cầu quy trình rõ ràng.
2. Nguyên tắc: Đánh giá quy trình cần kết hợp kiểm tra định trị (thứ tự, quyền) và đánh giá ngữ nghĩa (LLM judge) — không loại nào đủ đơn độc. Áp dụng khi: xây dựng hệ thống đánh giá agent tuân thủ. Không áp dụng khi: chỉ cần kiểm tra trạng thái cuối đơn giản.

## Assumptions & Limitations
- Điều kiện phải đúng: có môi trường công cụ riêng miền, có khách giả lập, có yêu cầu quy trình được mã hóa thành rule cards.
- Limitation paper thừa nhận: đánh giá không tự lập điều chỉnh pháp lý của triển khai thực tế; judge development dùng 5 chuyên gia phần mềm cao cấp (một soạn thảo, ba đánh giá, một chú thích 120 vết gpt-5.4-mini); đây là vết định khía không phải tập xác thực độc lập.
- Limitation paper KHÔNG nói: không đánh giá trên các tác vụ ngoài dịch vụ khách hàng được điều chỉnh; không so sánh trực tiếp với các benchmark khác ngoài bảng 1; không có chi phí inference thực tế của hybrid grader.

## Metadata
- Năm: 2026
- Tác giả: Boxi Yu, Yuzhong Zhang, Zhenfeng Su, Linfu Xi, Yinghan Yao, Shitao Chen, Yang Cao, Liting Lin, Lionel Briand, Emir Muñoz (Lero/University of Limerick, CUHK-Shenzhen, Peking, Xi'an Jiaotong, South China Univ of Technology, Genesys Cloud)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.25954
- arXiv ID: 2610.25954v1
- Nhãn: [applied]
- Citation count: [không tìm được]