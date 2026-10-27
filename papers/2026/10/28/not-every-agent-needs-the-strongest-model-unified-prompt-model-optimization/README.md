# 2610.31743v2 Not Every Agent Needs the Strongest Model: Unified Prompt-Model Optimization for Heterogeneous LLM-based Multi-Agent Systems

## Giá trị cốt lõi (1 câu)
UniMASO đồng bộ tối ưu prompt và model assignment trong hệ thống đa agent (MAS) dị nhất — agent structured/summarization dùng model nhẹ (Qwen3.5-9B 43.5%), agent reasoning/verification dùng model mạnh hơn (DeepSeek-V4-Flash 45.5%) — giúp đạt điểm trung bình 70.40 với chi phí thấp hơn 85.2% so với cấu hình đồng nhất mạnh nhất.

## Problem
Prior work (các nghiên cứu trước) về tối ưu hóa prompt thường giữ model assignment cố định, để sự khác biệt về yêu cầu vai trò và chi phí suy luận liên quan nằm ngoài tìm kiếm. Điều này gây ra việc sai về khả năng của vai trò (role-capability misalignment): có thể lãng phí model mạnh cho vai trò thuần tuý hoặc tạo bottleneck cho vai trò đòi hỏi cao với model nhẹ, trong khi chỉnh sửa prompt không thể cung cấp khả năng bị thiếu. Các phương pháp hiện có tối ưu hóa prompt tự động hoặc định tuyến model, nhưng thườngFix prompts hoặc fix execution models, không tìm kiếm chung cả hai.

## Contribution
1. Formulalogia (đarbiểu toán học) tối ưu hóa MAS dị nhất trên cấu trúc prompt–model, làm rõ sai về khả năng của vai trò.
2. Phát triển tìm kiếm có ý thức chi phí và topologi, kết hợp đánh giá đa phân cấp cục bộ với hệ thống co-evolution theo topologi.
3. Giới thiệu bộ nhớ quỹ đạo xuyên cấp (cross-level trajectory memory) biến phản hồi cục bộ, kết quả toàn cục, và quan sát chi phí thành kinh nghiệm cho các vòng sau.
4. Thí nghiệm trên năm benchmark (AGIEval-MATH, GPQA-Diamond, BFCL-V3, LiveCodeBench v6, HotpotQA) và năm topologi thực thi (Independent, Centralized, Sequential, Decentralized, Dynamic): UniMASO đạtTrade-off chất lượng–chi phí tốt hơn cấu hình đồng nhất. Dưới thực thi tập trung, UniMASO nâng điểm trung bình từ 69.79 lên 70.40 trong khi giảm chi phí triển khai theo trọng số token xuống 85.2% so với DeepSeek-V4-Pro với MASPO.
5. Phân phối model theo vai trò: Qwen3.5-9B được chọn nhiều nhất cho nhóm structured/summarization (43.5%), DeepSeek-V4-Flash chiếm ưu thế cho nhóm reasoning/verification (45.5%).

## Method
Pipeline (dòng xử lý) của UniMASO có các bước chính:
1. Mô hình hóa hệ thống N agent dưới dạng đồ thị có hướng G = (V, E). Mỗi agent vi có không gian prompt Pi và được gán một vai trò prompt pi ∈ Pi và một mô hình thực thi mi từ nhóm đồng chất M = {m(1), ..., m(K)}. Ghi nhãn nhiệm vụ này là zi = (pi, mi) và cấu hình hệ thống toàn bộ là z = (z1, ..., zN).
2. Sinh ứng viên từ quỹ đạo thực thi (trace-guided candidate generation): optimizer Mopt lấy mẫu quỹ đạo chứa đầu vào, bối cảnh, đầu ra, và phản hồi, sau đó đề xuất ứng viên từ cấu hình hiện tại.
3. Đánh giá đa phân cấp tương tác (multi-granularity interaction evaluation): so sánh thực thi ứng viên và tham chiếu ở ba phân cấp: độ hợp lệ cục bộ (local validity), tiện ích nhìn về trước (lookahead utility), và sự khớp toàn cục (global alignment). Công thức tiện ích: Ui(p') = α·qloc_i(p') + β·qlook_i(p') + γ·qglob_i(p'), với α + β + γ = 1.
4. Tìm kiếm beam có ý thức chi phí (cost-aware beam search): mở rộng ứng viên khi Ui(p')·ηi(p')−λ > uref, trong đó ηi(p') = Ci(p')/Ci(pi) là chi phí tương đối, λ ≥ 0 là trọng số chi phí, uref = 1/2 là điểm trung lập. Giữ các ứng viên không bị thống trị về chất lượng–chi phí.
5. Điều chỉnh mô hình dị nhất có ý thức topologi (topology-aware heterogeneous model adaptation): mở rộng ứng viên cục bộ thành cặp prompt–model z'i = (p'i, m'i). Cập nhật tốt nhất cục bộ ¯zi = (¯pi, ¯mi) sau đó được chuyển đến điều phối hệ thống.
6. Đề xuất đa견 theo điều kiện topologi (topology-conditioned multi-view proposals): mỗi agent logic tối ưu hóa tạo một quan điểm tiêu điểm điều kiện theo vai trò, phụ thuộc, thứ tự thực thi, kết quả tìm kiếm cục bộ, và thông tin khả năng–chi phí của mô hình.
7. Tín hiệu đồng đắc theo độ tập trung đề xuất (proposal-entropy consensus): đoán hỗ trợ thực nghiệm và trọng số theo độ tập trung đề xuất: πi(m) = (1/J)·Σj I[ˆm(j)i = m], Ai(m) = πi(m)(1 − H̄i). H̄i là entropy Shannon của πi chuẩn hóa bởi log|Mi|.
8. Bộ nhớ quỹ đạo xuyên cấp (cross-level trajectory memory): cho tối ưu hóa chuyển t, ghi lại cấu trúc trước đó, sự sửa đổi được đề xuất, và đánh giá: ξt = (zt, at, qt, Ct, bt). Gom các bản ghi thành thành công toàn cục chi phí thấp, thành công cục bộ với thất bại toàn cục, và thành công toàn cục chi phí cao. Truy xuất cân bằng theo loại (category-balanced retrieval).

## KNOWLEDGE — Số liệu & khái niệm
- Heterogeneous MAS (hệ thống đa agent dị nhất): hệ thống đa agent mà mỗi agent có thể sử dụng model khác nhau.
- Prompt–model optimization (tối ưu hóa prompt–model): tìm kiếm chung cả prompt và model assignment để đạt trade-off chất lượng–chi phí.
- Role-capability misalignment (sai về khả năng của vai trò): tình trạng model mạnh được lãng phí cho vai trò thuần tuý hoặc vai trò đòi hỏi cao bị bottleneck bởi model nhẹ.
- Cost-aware Pareto search (tìm kiếm Pareto có ý thức chi phí): giữ các ứng viên không bị thống trị về chất lượng và chi phí.
- Topology-aware co-evolution (co-evolution có ý thức topologi): điều phối cập nhật theo vai trò agent và phụ thuộc.
- Cross-level trajectory memory (bộ nhớ quỹ đạo xuyên cấp): cung cấp thành công/thất bại lịch sử để hướng dẫn tối ưu hóa sau.
- Model pool (nhóm mô hình): Qwen3.5-4B, Qwen3.5-9B, Qwen3.5-27B, DeepSeek-V4-Flash, DeepSeek-V4-Pro.
- 5 benchmark: AGIEval-MATH (độ khó 5), GPQA-Diamond, BFCL-V3, LiveCodeBench v6, HotpotQA.
- 5 topologi: Independent, Centralized, Sequential, Decentralized, Dynamic.
- Centralized execution: điểm trung bình 69.79→70.40, chi phí 208.28M→30.92M (giảm 85.2%).
- UniMASO dẫn trên AGIEval-MATH (82.42 vs 78.12) và HotpotQA (63.80 vs 62.80).
- Qwen3.5-9B được chọn 43.5% cho structured/summarization; DeepSeek-V4-Flash chiếm 45.5% cho reasoning/verification.
- Tổng tỷ lệ Qwen3.5-27B + DeepSeek-V4-Flash tăng từ 47.8% lên 78.8% giữa các nhóm.
- Chi phí tối ưu hóa: từ 4,710.6M xuống 206.3M (giảm 95.6%).
- Input tokens: 29.42M→23.33M (giảm 20.7%); output tokens: 0.439M→0.369M (giảm 15.9%).
- Chi phí truyền qua (Cost-of-Pass): 1.241→0.184 (giảm 85.2%).
- 3 vòng tối ưu hóa với độ tìm kiếm mỗi vòng 3–2–2.
- Trọng số chi phí λ = 0.2; Kmem = 2 bản ghi mỗi loại.

## INSIGHT — Cơ chế & tại sao
- [Joint prompt–model adaptation cần thiết] xảy ra VÌ việc tối ưu hóa prompt trước rồi gán model sau có thể làm prompt phù hợp với executor gốc hơn so với model cuối cùng được gán cho vai trò. Nghĩa là đánh giá chung cả hai quyết định là nhất quán với sự cải thiện quan sát được về chất lượng và chi phí.
- [Co-evolution hữu ích khi thay đổi ở một agent ảnh hưởng đến người kế nhiệm] xảy ra VÌ các cập nhật cục bộ được đánh giá với cấu hình còn lại cố định, vì vậy sự kết hợp của chúng có thể thay đổi hành vi giữa các agent. Điều phối hệ thống giải quyết sự không khớp này. Nghĩa là khi một thay đổi ở một agent ảnh hưởng đến người kế nhiệm, điều phối các đề xuất cục bộ là hữu ích.
- [Tìm kiếm có ý thức chi phí cải thiện operating point] xảy ra VÌ chất lượng đơn lẻ không xác định cấu trúc hiệu quả — việc loại bỏ tìm kiếm Pareto có ý thức chi phí làm điểm trung bình giảm từ 70.40 xuống 69.42 trong khi chi phí triển khai tăng từ 30.92M lên 62.40M. Nghĩa là cần tính đến cả chi phí thực thi cũng như tiện ích tác vụ khi chọn ứng viên.

## IDEA — Áp dụng được gì
1. Áp dụng UniMASO vào hệ thống đa agent của doanh nghiệp: đồng bộ tối ưu prompt và model assignment thay vì tối ưu hóa prompt với model cố định. Bước đầu: xác định các vai trò agent trong hệ thống và nhóm mô hình có sẵn, sau đó chạy tìm kiếm chung prompt–model cho mỗi vai trò.
2. Phân phối model theo yêu cầu vai trò: gán model nhẹ cho vai trò structured/summarization (ví dụ: Qwen3.5-9B) và model mạnh hơn cho vai trò reasoning/verification (ví dụ: DeepSeek-V4-Flash). Bước đầu: phân loại các agent trong hệ thống thành nhóm structured/summarization và nhóm reasoning/verification, sau đó gán model phù hợp.
3. Sử dụng bộ nhớ quỹ đạo xuyên cấp: lưu lại các bản ghi về cấu hình trước, sự sửa đổi được đề xuất, và đánh giá (chất lượng, chi phí, kết quả chấp nhận) để tái sử dụng trong các vòng tối ưu hóa sau. Bước đầu: thiết lập cơ chế lưu trữ quỹ đạo tối ưu hóa và truy xuất cân bằng theo loại (category-balanced retrieval) với Kmem = 2.

## WISDOM — Nguyên tắc tổng quát
- Nguyên tắc: Không phải mọi agent trong hệ thống đa agent đều cần model mạnh nhất — hãy gán khả năng mô hình theo yêu cầu của vai trò và tối ưu hóa chung prompt với model assignment.
- Khi nào dùng: Khi thiết kế hệ thống đa agent LLM với nhiều vai trò khác nhau và muốn tối ưu hóa trade-off chất lượng–chi phí.
- Khi nào KHÔNG dùng: Khi hệ thống chỉ có một agent đơn lẻ hoặc tất cả agent đều có cùng yêu cầu về khả năng.

## Assumptions & Limitations
- Điều kiện phải đúng: Cần có hệ thống đa agent với cấu trúc đồ thị có hướng (topologi thực thi) và nhóm mô hình đồng chất để chọn lựa.
- Limitation paper thừa nhận: Thí nghiệm giới hạn ở năm benchmark và năm topologi cụ thể; kết quả có thể không tổng quát sang các tác vụ hoặc topologi khác.
- Limitation paper KHÔNG nói: Không nói rõ chi phí tính toán để chạy quá trình tối ưu hóa UniMASO bản thân (chi phí meta-optimization) so với tác vụ mục tiêu.

## Metadata
- Năm: 2026
- Tác giả: Mingxiu Cai, Haoyang Xian, Xinyu Ma, Yutong Wang, Zhenxi Song, Jing Li, Xuebo Liu
- Category arXiv: cs.MA
- Link PDF: https://arxiv.org/pdf/2610.31743v2
- Classification: [applied]