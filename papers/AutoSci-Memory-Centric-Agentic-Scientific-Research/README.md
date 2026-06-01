# [2605.31468v1] AutoSci: Hệ thống Tác nhân Lõi Bộ nhớ cho Toàn bộ Vòng đời Nghiên cứu Khoa học

## Vấn đề
Scientific research (nghiên cứu khoa học) traditionally human-intensive (tốn công sức con người), requiring researchers coordinate literature (văn liệu), ideas (ý tưởng), experiments (thí nghiệm), manuscripts (bản thảo), và review responses (phản hồi phản biện) across long project cycles (chu kỳ dự án dài). Existing systems either partially satisfy hoặc fail to satisfy requirements cho unified automated scientific research system.

## Đóng góp
1. **SciMem**: Schema-governed research memory (bộ nhớ nghiên cứu được kiểm soát bởi lược đồ) — tách Long-Term Knowledge Memory (bộ nhớ tri thức dài hạn) cho reusable scientific knowledge và Active Research Memory (bộ nhớ nghiên cứu hoạt động) cho project-level artifacts (hiện vật cấp dự án)
2. **SciFlow**: Five-stage lifecycle executor (bộ thực thi vòng đời 5 giai đoạn): Literature Understanding → Ideation → Experiment → Writing → Rebuttal
3. **SciDAG**: DAG-shaped multi-agent operators (toán tử đa tác nhân dạng DAG) với reusable stage-specific templates (mẫu theo giai đoạn tái sử dụng)
4. **SciEvolve**: Converts feedback signals (tín hiệu phản hồi) thành versioned updates (cập nhật có phiên bản) cho SciMem, SciFlow, SciDAG

## Phương pháp (tóm tắt cốt lõi)
4 modules: SciMem tách memory thành long-term knowledge (accumulated across projects) và active research (current project state). SciFlow decompose project thành 5 stages với harness-based skill contracts. SciDAG augment difficult skills với DAG multi-agent operators — adaptive execution theo intermediate quality signals. SciEvolve collect signals từ user/task/open environments → detect patterns → trigger updates. Together: persistent research environment execute, remember, evolve across projects.

## Kết quả chính
- [NO BENCHMARK] — system paper, case studies thay vì benchmarks
- Case study 1: GPU kernel optimization — produce reviewable paper-level artifacts
- Case study 2: Biomedical drug discovery — end-to-end research process
- 4 modules operational: SciMem, SciFlow, SciDAG, SciEvolve

## Insight có thể áp dụng ngay
1. **Tách long-term memory và active memory**: Khi build AI research assistant, tách knowledge accumulated across projects (reusable) và current project state (temporary). Ví dụ: company knowledge base (long-term) vs current project docs (active).

2. **Five-stage lifecycle cho research automation**: Decompose research thành Literature → Ideation → Experiment → Writing → Rebuttal. Mỗi stage có specific harness contract. Ví dụ: khi automate market research, 5 stages: Market Understanding → Hypothesis → Testing → Report → Client Feedback.

3. **DAG-based multi-agent cho complex tasks**: Thay vì linear chain, dùng DAG operators cho tasks cần branching/retry. Adaptive execution theo quality signals. Ví dụ: content creation pipeline — generate → review → retry if quality low → finalize.

## Giả định & Hạn chế
**Điều kiện để system work:**
- General-purpose coding/reasoning agents phải available
- Structured memory schemas phải được define trước
- Five-stage lifecycle applicable cho research-type tasks

**Hạn chế paper thừa nhận:**
- Built on general-purpose agents, not science-specialized foundation
- Evaluation underdeveloped — rely on end-to-end case studies
- Existing benchmarks don't adequately measure full research system capabilities

**Hạn chế paper KHÔNG nói:**
- Case studies limited — không compare với human researchers
- Scalability unclear — complex projects có thể overwhelm system
- Memory management overhead — SciMem grow unbounded?
- Không address research ethics, plagiarism concerns
- Domain-specific knowledge requirements unclear

## Metadata
- Năm: 2026
- Tác giả: Weitong Qian, Beicheng Xu, et al.
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.31468v1
- Citation count: [EXTRACTION FAILED]
