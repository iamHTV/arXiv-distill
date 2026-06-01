# [2605.31514v1] If LLMs Have Human-Like Attributes, Then So Does Age of Empires II (Nếu LLM có thuộc tính giống người, thì Age of Empires II cũng vậy)

## Vấn đề
Nhiều nghiên cứu gán cho LLMs (mô hình ngôn ngữ lớn) các anthropomorphic attributes (thuộc tính nhân hình hóa) như morality (đạo đức) hoặc understanding (sự hiểu biết) ngôn ngữ tự nhiên. Tuy nhiên, các kết luận này có thể sai vì: không có measurement criteria (tiêu chí đo lường) rõ ràng — interpretation (cách diễn giải) bị phụ thuộc vào representation (biểu diễn) của người quan sát. Gán thuộc tính nhân hình hóa một cách generalized (tổng quát hóa) dẫn đến circular conclusions (kết luận vòng tròn) hoặc uninformative conclusions (kết luận không thông tin).

## Đóng góp
1. **Chứng minh tính non-unique (không duy nhất) của thuộc tính nhân hình hóa**: Xây dựng và train neural network đơn giản trên videogame Age of Empires II — bất kỳ entity (thực thể) nào trên substrate (nền tảng) đủ mạnh (LEGO, Greater Boston Area, hoặc game) đều có thể present (trình diện) các thuộc tính tương tự
2. **Propose "null assumption" (giả định không)**: Thay vì assume (giả định) LLM có thuộc tính nhân hình hóa, assume LLM non-uniqueness (không duy nhất) — thiết kế experiment (thí nghiệm) kiểm chứng ngược
3. **Proof of Turing-completeness (chứng minh tính đầy đủ Turing)**: Chứng minh Age of Empires II là functionally-complete và Turing-complete

## Phương pháp (tóm tắt cốt lõi)
Tác giả xây dựng neural network trên Age of Empires II, train nó thực hiện các tác vụ phức tạp, và chỉ ra rằng bất kỳ substrate đủ mạnh nào đều có thể exhibit (trình hiện) các thuộc tính tương tự mà người ta gán cho LLMs. Argument chính: nếu bạn gán "understanding" cho LLM vì nó trả lời đúng, thì bạn cũng phải gán "understanding" cho AoE2 vì nó cũng xử lý đúng — cả hai đều chỉ là computation (tính toán) trên substrate. Propose framework experiment: thay vì ask "does LLM have X?", ask "is X unique to LLM? Show substrate-independent measurement."

## Kết quả chính
- [NO BENCHMARK] — purely philosophical/theoretical argument
- Demonstrated: AoE2 neural network exhibit behaviors mà nếu interpret như LLM research, sẽ gán là "understanding", "planning", "strategy"
- Proved: AoE2 là functionally-complete và Turing-complete
- Showed: assuming anthropomorphic attributes exist independent of substrate → circular hoặc uninformative conclusions, regardless of experimenter's viewpoint

## Insight có thể áp dụng ngay
1. **Khi đánh giá AI capabilities (khả năng), luôn hỏi "có unique không?"**: Trước khi claim LLM "hiểu" hoặc "suy luận", kiểm tra: hành vi tương tự có xuất hiện trên substrate khác không? Ví dụ: khi vendor claim AI "understands" customer intent — hỏi: rule-based system có thể produce cùng output không? Nếu có, "understanding" chỉ là interpretation.

2. **Dùng null assumption trong AI evaluation (đánh giá AI)**: Thiết kế experiment với default assumption là AI KHÔNG có attribute X, và yêu cầu proof ngược. Ví dụ: khi evaluate AI creativity (sáng tạo) — assume AI không sáng tạo, yêu cầu demonstration rằng output không thể được explain bằng pattern matching (khớp khuôn mẫu) đơn giản.

3. **Substrate-independent measurement (đo lường độc lập nền tảng)**: Định nghĩa measurement criteria trước khi interpret behavior. Ví dụ: define "reasoning" = ability to solve novel problems with >80% accuracy on unseen distribution — không phải "AI trả lời như con người" vì con người cũng có thể dùng pattern matching.

## Giả định & Hạn chế
**Điều kiện để argument work:**
- Cần accept rằng computation trên substrate là substrate-independent (tính toán không phụ thuộc nền tảng)
- Cần accept rằng behavioral observation (quan sát hành vi) alone không đủ để infer (suy luận) internal attributes

**Hạn chế paper thừa nhận:**
- Không argue for hoặc against existence của attributes — chỉ argue conclusions có thể incorrect
- Proving Turing-completeness của AoE2 là supporting argument, không phải main contribution

**Hạn chế paper KHÔNG nói:**
- Không address practical differences giữa LLM và game substrate — LLM có scale và generalization mà AoE2 không có
- Argument có thể apply quá rộng — mọi AI system đều bị dismiss
- Không propose concrete alternative methodology cho AI evaluation
- Philosophical argument, không empirical — khó verify (xác minh)
- Turing-completeness proof có thể irrelevant — modern LLMs cũng Turing-complete nhưng argument vẫn đứng

## Metadata
- Năm: 2026
- Tác giả: Adrian de Wynter
- Category: cs.CL, cs.AI, cs.CY
- Link PDF: https://arxiv.org/pdf/2605.31514v1
- Citation count: [EXTRACTION FAILED]
