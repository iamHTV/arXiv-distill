# [2605.26329v1] JobBench: Aligning Agent Work With Human Will (Căn chỉnh Công việc Tác nhân với Ý muốn Con người)

## Vấn đề
Current benchmarks cho occupational AI agents (tác nhân AI nghề nghiệp) được scope (phạm vi) chủ yếu bởi economic values (giá trị kinh tế), telling a replacement story (kể câu chuyện thay thế). GDPVal — benchmark hiện tại — đã approaching saturation (gần bão hòa): GPT-5.4 đạt 83.0. Nhưng benchmarks này không answer câu hỏi: workers thực sự MUỐN delegate (ủy thác) tasks nào cho AI? Prior work không align evaluation với human will (ý muốn con người).

## Đóng góp
1. **JobBench**: Benchmark aligns agentic evaluation với human will thay vì chỉ economic values. 130 agentic tasks across 35 occupations, mỗi task từ Workbank-elicited delegation preference (từ khảo sát 1,500+ workers)
2. **Fact-anchored rubric chain (chuỗi tiêu chíanchored bằng sự thật)**: 4,631 binary criteria, average 35.6 criteria per task. Award credit chỉ khi EVERY step trong chain hold together
3. **Heterogeneous workspaces (không gian làm việc đa dạng)**: Mỗi task packaged với heterogeneous reference files — agents phải locate, retrieve, reconcile source evidence trước khi produce artifact

## Phương pháp (tóm tắt cốt lõi)
Dựa trên Workbank survey (1,500+ workers rate work duties cho delegation desire). Chọn duties experts WANT delegated và spend most preparation time on. Mỗi task = workspace với reference files (CSVs, guidance documents, surveillance data, etc.) + fact-anchored rubric chain. Agent phải reason through cluttered information streams, produce artifact, graded bởi chained binary criteria. 36 model-scaffold configurations evaluated.

## Kết quả chính
- Strongest: Claude Opus 4.7 under Claude Code = 45.9%
- GPT-5.5 under Codex = 42.7%
- GPT-5.4 under Codex = 38.9%
- Beyond Claude/GPT families: no model exceeds 19%
- Weakest: Grok-4.2-Fast = 4.38%
- GDPVal approaching saturation (GPT-5.4 = 83.0) nhưng corresponding JobBench = 38.9
- GPT-5.4 under Codex takes 2.40× runtime của GDPVal, tool calls 1.3×

## Insight có thể áp dụng ngay
1. **Đo lường AI readiness theo delegation desire, không chỉ economic value**: Khi evaluate AI cho workplace automation, hỏi workers MUỐN delegate tasks nào — không chỉ tasks nào economically valuable nhất. Ví dụ: reporter muốn delegate "cross-source fact checking" — economically valuable nhưng workers cũng MUỐN offload. Prioritize automation theo worker satisfaction, không chỉ cost savings.

2. **Heterogeneous workspaces > clean task packets**: Real professional work có cluttered, conflicting information. Benchmark AI trên heterogeneous data, không chỉ clean inputs. Ví dụ: khi test AI cho financial analysis, cho nó reconcile conflicting reports từ multiple sources — không chỉ clean spreadsheet.

3. **Fact-anchored rubric chains cho evaluation**: Khi evaluate AI outputs, dùng chained binary criteria — mỗi step phải hold together. Không chỉ check final output. Ví dụ: khi evaluate AI-generated report, check: (1) sources located? (2) data reconciled? (3) analysis sound? (4) conclusion supported? — ALL must pass.

## Giả định & Hạn chế
**Điều kiện để benchmark work:**
- U.S.-centered, digital, document-heavy professional tasks
- 35 selected O*NET occupations — không represent all occupations
- English-only, non-physical work

**Hạn chế paper thừa nhận:**
- Limited to U.S.-centered, digital, document-heavy tasks
- Does not represent all occupations, non-U.S. markets, non-English workplaces
- Physical work, real-time collaboration, long-term workflows not covered
- Not for deployment validation — benchmark only

**Hạn chế paper KHÔNG nói:**
- 130 tasks có thể quá ít cho robust evaluation
- 35 occupations selection criteria opaque
- Rubric chain design có human bias
- Không test với real workers — chỉ benchmark
- Runtime comparison (2.40×) có thể unfair — different task complexity
- Không address cost-effectiveness của agent deployment

## Metadata
- Năm: 2026
- Tác giả: Yuetai Li, Yichen Feng, Zhangchen Xu, et al.
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.26329v1
- Citation count: [EXTRACTION FAILED]
