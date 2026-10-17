# [2609.22476v1] A Governance-Aware Large Language Model Orchestrated Agentic Digital Twin for Transmission System Operator Control Room Decision Support

## Problem
Các hệ thống truyền tải điện (transmission system operators, TSO) đối mặt với độ phức tạp tăng cao từ việc tích hợp năng lượng tái tạo, độ quán tính giảm, và biên bảo mật chặt chẽ hơn. LLM hỗ trợ ra quyết định bằng ngôn ngữ tự nhiên nhưng ảo gezien (hallucination), sử dụng công cụ không kiểm soát (uncontrolled tool use), và kém khả năng truy xuất (traceability) xấp xống với yêu cầu phòng điều khiển. Cần một hệ thống agentic digital twin có lớp quản trị thời gian chạy (runtime governance layer) để ràng buộc hành vi LLM theo các quy tắc an toàn nghiêm ngặt.

## Contribution
- Trình bày một agentic digital twin có nhận thức quản trị (governance-aware) cho phòng điều khiển hệ thống truyền tải điện: LLM chỉ chọn và tham số hóa các công cụ phân tích được cho phép trắng danh (whitelisted), mọi hành động đề xuất đều đi qua lớp quản trị mà model không thể bỏ qua.
- Lớp quản trị thi hành 5 yêu cầu hệ thống (R1–R5) và 4 bất biến (invariants) trên mọi lần chạy: chỉ công cụ trắng danh được thực thi, không lần chạy nào vượt quá ngân sách bước, không hành động có tác dụng phụ thực thi mà không có sự chấp nhận rõ ràng từ toán tử, mọi con số trong câu trả lời được render từ kết quả backend.
- Đánh giá trên bộ benchmark 118 tác vụ (phiên bản迪지털 twin của mạng lưới truyền tải希腊) bao gồm phân tích, mô phỏng, luồng công việc nhiều bước, và 12 gia đình đầu vào đối kháng (adversarial inputs) qua 590 lần chạy của model chính và 1416 lần chạy trên 4 LLM.

## Method
- Kiến trúc: Agent gateway (Django REST, Python 3.10, Ollama model server) hosts LLM orchestration và governance layer; backend dịch vụ決定istik (pandapower, power flow simulation, contingency analysis, forecasting); lưu trữ phiên và kiểm tra duy trì (PostgreSQL 16, TimescaleDB).
- LLM chỉ sinh ra hành động hợp đồng JSON (tool invocation request hoặc final response), không truy cập trực tiếp backend dịch vụ.
- Lớp quản trị kiểm tra mọi hành động trước khi thực thi: whitelist tool, schema-validate arguments, execution step budget (MAX_AGENT_STEPS=5), approval token cho hành động có tác dụng phụ (APPROVAL_TTL_S=300s), numeric provenance từ backend.
- Mô hình chính: Mistral-Nemo 12B (temperature=0). Các mô hình khác: gpt-oss 20B, Qwen2.5 32B, Command-R 35B.

## Key Findings
- Trên 590 lần chạy của model chính (Mistral-Nemo 12B): tool selection 96.5%, task success 93.7%, tất cả 4 bất biến giữ 100% trên mọi lần chạy.
- Trên 1416 lần chạy qua 4 LLM: tất cả bất biến giữ trên mọi lần chạy, khoảng 95% lower bound 99.8%.
- Xóa lớp quản trị: cùng model thực thi tất cả 45 lần chạy yêu cầu chấp thuận mà không có phân quyền, chỉ 39.2% câu trả lời có con số được hỗ trợ bởi backend.
- Chi phí thi hành: 12 đến 16 milligiây mỗi yêu cầu.

## Actionable Insights
1. Đặt một lớp quản trị (governance layer) giữa LLM và các công cụ/backend — LLM không bao giờ được gọi trực tiếp công cụ hoặc backend. Áp dụng: khi xây dựng agent cho hệ thống quan trọng (tài chính, y tế, năng lượng), hãy thêm lớp interceptors kiểm tra mọi tool call trước khi thực thi. Bước đầu: Xây dựng một middleware kiểm tra tool name và arguments trước khi gửi đến backend.
2. Yêu cầu sự chấp thuận từ con người (human-in-the-loop) cho mọi hành động có tác dụng phụ (side-effect actions). Áp dụng: bất cứ công cụ nào có thể sửa đổi dữ liệu, gửi thông báo, hoặc khởi tạo quy trình bên ngoài phải chờ toán tử phê duyệt trước khi chạy. Bước đầu: Thêm bước chờ xác nhận từ người dùng trước khi thực hiện action ghi dữ liệu hoặc gửi thông báo.
3. Mọi con số hiển thị cho người dùng phải được render từ kết quả backend có xác định (deterministic), không được LLM tự sinh. Áp dụng: tách biệt suy luận (reasoning) khỏi tính toán (computation) — LLM chỉ đưa ra khuyến nghị, các con số thực tế được tính toán bởi backend và render kèm đơn vị, biến số, thời gian. Bước đầu: Không cho phép LLM sinh ra con số trong câu trả lời, thay bằng placeholder tham chiếu đến kết quả backend.

## Assumptions & Limitations
- Đánh giá trên digital twin của mạng lưới truyền tải希腊 (Greek transmission network), kết quả có thể khác đối với hệ thống điện quốc gia khác hoặc domain ngoài năng lượng.
- Chỉ đánh giá 4 LLM (Mistral-Nemo 12B, gpt-oss 20B, Qwen2.5 32B, Command-R 35B), không generalize sang tất cả LLM.
- Benchmark 118 tác vụ được thiết kế riêng cho domain điều khiển hệ thống điện, có thể không đại diện cho các tác vụ business/content chung.
- Chi phí thi hành 12-16ms mỗi yêu cầu, chưa xét chi phí khi tải cao đồng thời (concurrent load).

## Metadata
- Năm: 2026, tác giả: Costas Mylonas, Magda Foti, Emmanouel Varvarigos (UBITECH Energy Digitalization Group, Athens; National Technical University of Athens), category arXiv: cs.SE, link PDF: https://arxiv.org/pdf/2609.22476v1