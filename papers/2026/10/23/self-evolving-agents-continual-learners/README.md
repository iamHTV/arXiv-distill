# 2610.25858 Agent tự tiến hóa có phải học liên tục không?

## Problem
Các agent LLM thường được triển khai trong môi trường nơi kiến thức mới, công cụ và quy trình làm việc liên tục đến. Hy vọng agent thích ứng liên tục, học tác vụ mới khi xuất hiện mà không quên các tác vụ trước — vấn đề học liên tục (continual learning). Các agent tự tiến hóa phi tham số (nonparametric self-evolving agents) thích ứng bằng cách viết lại thành phần bao bọc (harness — hệ thống bao quanh mô hình: system prompt, bộ nhớ tích lũy, thư viện kỹ năng, mã điều khiển) từ phản hồi tác vụ, trong khi trọng số mô hình đóng băng. Câu hỏi: agent tự tiến hóa có hiệu quả là học viên liên tục không?

## Contribution
- Xây dựng bốn luồng tác vụ drifting (drifting task streams — luồng tác vụ chuyển phân phối theo thời gian) isolates các loại dịch chuyển: topic drift (chủ đề), workflow drift (quy trình làm việc), domain drift (môi trường/khu vực), compound drift (kết hợp tất cả), dựng từ BIRD, BFCL, ScienceWorld.
- Đánh giá ba phương pháp đại diện: ReasoningBank (truy xuất ký tự kinh nghiệm), GEPA (viết lại system prompt), Meta-Harness (chỉnh sửa toàn bộ workspace bao gồm prompt, bộ nhớ, kỹ năng, mã điều khiển).
- Đem ra ba phát hiện: (1) các phương pháp hiện nay ट्रेड-off ổn định để linh hoạt (plasticity-stability trade-off), (2) tự sửa đổi gây can thiệp chéo tác vụ và ghi đè (overwriting) kiến thức trước, (3) truy xuất dựa trên độ tương đồng (similarity-based retrieval) không thể ngăn can thiệp hay va chạm truy xuất (retrieval collision).

## Method
Một luồng tác vụ S_w là dãy đầu vào được vẽ từ hỗn hợp các họ tác vụ F_k, với lịch trình trọng số w_t là one-hot và piecewise-constant (mỗi block vẽ tất cả tác vụ từ một nhóm duy nhất, nhóm hoạt động chỉ thay đổi tại ranh giới block). Agent duy trì một harness chung xuyên suốt toàn bộ horizion, không được biết nhãn nhóm hay ranh giới block.

Chỉ số đánh giá:
- Terminal advantage (Term.): trung bình A[T,k] − B_k qua tất cả K họ tại cuối luồng.
- Average advantage (Δ̄): trung bình A[t_m,k] − B_k qua tất cả K họ và tất cả M điểm kiểm tra sau seed.
- Plasticity P: lợi thế so với seed tại kết thúc block của mỗi họ, trung bình qua K họ.
- Stability S: giảm sút mà một họ gặp phải khi luồng đào tạo các họ khác, kết hợp can thiệp trước block (Ī) và quên sau block (F̄).

Ba phương pháp: ReasoningBank distills đoạn hoàn thành thành mục ký tự trong kho bên ngoài và truy xuất mục tương tự nhất top-1 vào ngữ cảnh của các Abschnitt sau; GEPA viết lại phần chiến lược trong system prompt thông qua đột biến phản chiếu trên các thu thập rollout; Meta-Harness đề xuất chỉnh sửa đến workspace bền vững (bao gồm system prompt, tệp bộ nhớ và kỹ năng, mã điều khiển harness.py) thông qua tác nhân mã hóa và chấp nhận chỉnh sửa chỉ khi cải thiện độ chính xác xác nhận trên sub-block đang hoạt động.

Mô hình: Gemini 3.6 Flash trong vòng lặp ReAct-style. Mỗi stream có các block 50 tác vụ đào tạo mỗi nhóm, đánh giá trên các tập hold-out rời rạc Deval_k của 50 tác vụ mỗi nhóm (90 cho ScienceWorld).

## KNOWLEDGE — Số liệu & khái niệm
- Trên 4 luồng drifting, lợi thế trung bình (Δ̄) dao động từ +1.8 đến +3.1 pp, lợi thế cuối (Term.) đạt +3.7 (GEPA), +2.5 (ReasoningBank), +1.4 (Meta-Harness).
- Chỉ topic drift cho thay đổi gần bằng không hoặc hơi âm (−1.7 GEPA, +0.3 ReasoningBank, −1.5 Meta-Harness).
- Plasticity: GEPA cao nhất mỗi kịch bản (+6.2 trung bình, đạt +11.0 workflow drift, +7.5 compound drift). ReasoningBank khoảng nửa plasticity của GEPA (+3.3 trung bình).
- Stability: ReasoningBank cao nhất (−1.9 trung bình, −0.4 domain drift, −1.4 compound drift). GEPA lớn nhất tổn thất ổn định (−4.3 trung bình). Meta-Harness ít ổn nhất trên domain và compound drift (S = −3.1 và −4.4).
- Can thiệp trước block: trên domain drift, đào tạo ScienceWorld làm giảm BFCL-Base tại vị trí 50 bởi 5.5 (GEPA) và 1.5 (Meta-Harness). Trên compound drift, đào tạo hai block BIRD làm suy yếu BFCL-Miss trước khi tác vụ BFCL nào đến, đạt −6.8 (GEPA) và −4.8 (Meta-Harness) tại vị trí 100.
- Quên sau block: trên compound drift, GEPA nén bảy phần SQL BIRD (3.386 ký tự tại vị trí 100) thành một phần chung 1.034 ký tự, làm giảm phần BIRD-F1 từ 59.5% (vị trí 100) xuống 5.8% (vị trí 150), xóa bỏ lợi thế +4.0.
- Va chạm truy xuất (retrieval collision): trên workflow drift, BFCL-Miss và BFCL-Base dùng cùng katalog API và câu truy vấn gần như giống nhau (cosine similarity 0.667 pairwise, 0.835–0.840 nearest-match), không có ngưỡng tương đồng nào tách hai nhóm; 52% Abschnitt BFCL-Miss tại cuối luồng truy xuất ký tự BFCL-Base, làm giảm độ chính xác BFCL-Miss 8.0 điểm (+12.5 → +4.5).

## INSIGHT — Cơ chế & tại sao
[Tự sửa đổi áp dụng chỉnh sửa chung toàn cầu vào prompt hoặc workspace dùng chung] xảy ra VÌ mọi cập nhật viết lên một bề mặt chỉ thị hoặc workspace dùng chung được tiêm vào mọi bản chạy sau đó, tạo ra can thiệp trước block (quy tắc chuyên biệt cho một block áp dụng vô điều kiện vào tác vụ chưa thấy) và quên sau block (block sau tiếp tục sửa prompt/workspace chung, nén hoặc ghi đè hướng dẫn trước). Điều này nghĩa là [các quy tắc học được trên một block can thiệp vào tác vụ không thấy và bị nén/ghi đè bởi block sau, nhất là khi các block liên tiếp dùng cùng domain nhưng đòi hỏi quy trình nghịch đảo].
[Truy xuất dựa trên độ tương đồng truy vấn] xảy ra VÌ việc lấy mục ký tự gần nhất theo cosine similarity không có ngưỡng lọc, nên cualquier segment được đánh giá trước khi block của mình bắt đầu nhận ký tự nước ngoài 100% Abschnents; và khi các nhóm khác nhau chiếm cùng vùng không gian embeddings, không có ngưỡng nào tách chúng được. Điều này nghĩa là [tương đồng ngữ nghĩa giữa các truy vấn chỉ bắt chước sự chồng chéo chủ đề, không thể xác định liệu quy trình làm việc của một đoạn quỹ tích đã lưu có tương thích với tác vụ đến hay không].

## IDEA — Áp dụng được gì
1. Áp dụng nguyên tắc tách biệt cập nhật theo tác vụ vào harness agent: bước đầu là thiết kế harness agent sao cho cập nhật cho tác vụ A không ảnh hưởng đến tác vụ B (ví dụ dùng namespace hoặc module riêng cho từng nhóm tác vụ thay vì prompt toàn cục duy nhất).
2. Áp dụng điều kiện truy xuất vượt quá độ tương đồng bề mặt: bước đầu là thêm bộ lọc ngữ cảnh (context filter) trước khi đưa ký tự truy xuất vào prompt, kiểm tra xem quy trình làm việc của ký tự đã lưu có phù hợp với tác vụ đến hay không.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Trong học liên tục cho agent, tính linh hoạt (plasticity) và tính ổn định (stability) luôn đối ngược nhau; cập nhật toàn cục vào harness dùng chung mang lại học nhanh nhưng quên nhanh, còn truy xuất cục bộ ngăn quên nhưng vẫn bị va chạm khi các tác vụ khác nhau dùng cùng không gian embeddings. Khi nào dùng: khi cần agent thích ứng liên tục với tác vụ mới mà không quên cũ. Khi nào KHÔNG: khi tác vụ đến từ cùng domain nhưng đòi hỏi quy trình nghịch odio (ví dụ hỏi suy cho cùng vs gọi công cụ trực tiếp) — cần cơ chế tách biệt rõ ràng hơn.

## Assumptions & Limitations
- Mô hình base cố định (Gemini 3.6 Flash), không quét rộng họ mô hình và kích thước.
- Các block tác vụ là contiguous (liên tiếp), không bao gồm tác vụ xen kẽ均匀 (nhiều dòng ghi đè vẫn xảy ra khi xen kẽ).
- Đánh giá trên các benchmark agent (BIRD, BFCL, ScienceWorld), chưa mở rộng sang domain khác.
- Không có mục Limitations riêng trong paper; các hạn chế được nêu trong Conclusion và thảo luận.

## Metadata
- Năm 2026; tác giả: Xiaoyin Chen (Mila, Université de Montréal), Yizheng Huang, Yinglun Xu, Ziyun Zhao, Emmett McQuinn, Julie Liu, Hope Yao (Google DeepMind); category: cs.AI; PDF: https://arxiv.org/pdf/2610.25858v1; citation count: [NO DATA — paper 2026-10-19]