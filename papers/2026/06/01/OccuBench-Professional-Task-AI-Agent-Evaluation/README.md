# 2604.10866 OccuBench: Evaluating AI Agents on Real-World Professional Tasks

## Problem

AI agents được kỳ vọng thực hiện professional work (công việc chuyên môn) across hundreds of occupational domains (lĩnh vực nghề nghiệp) — từ emergency department triage đến nuclear reactor safety monitoring đến customs import processing. Nhưng existing benchmarks chỉ evaluate trong vài domains có public environments. Không có systematic cross-industry evaluation (đánh giá liên ngành) nào cho AI agents trên professional tasks.

## Contribution

1. OccuBench — benchmark covering 100 real-world professional task scenarios across 10 industry categories và 65 specialized domains. Enabled by Language Environment Simulators (LESs) — LLM-driven tool response generation để simulate domain-specific environments.
2. Multi-agent synthesis pipeline — automatically produces evaluation instances với guaranteed solvability, calibrated difficulty, document-grounded diversity.
3. Two evaluation dimensions: task completion across domains và environmental robustness under controlled fault injection (explicit errors, implicit data degradation, mixed faults).

## Method (tóm tắt cốt lõi)

(1) 100 professional scenarios across 10 industries: Agriculture, Business, Commerce, Education, Healthcare, Industrial, Science, Transportation, etc.; (2) Language Environment Simulators (LESs): LLM simulates domain-specific tool responses (API returns, database queries, file systems) — agent interacts with simulated environment; (3) Multi-agent synthesis: one agent generates task scenarios, another validates solvability, difficulty calibration; (4) Fault injection: explicit (timeouts, 500 errors), implicit (truncated data, missing fields), mixed; (5) Evaluate 15 frontier models across 8 families: GPT-5.2, Gemini-3.1-Pro, Claude-Opus-4.6, Qwen-3.5-Plus, DeepSeek-V3.2, etc.

## Key Findings

- No single model dominates all industries — each has distinct occupational capability profile
- GPT-5.2 leads overall: 79.6%, highest in Agriculture (84%), Business (86%), Industrial (85%), Science (94%)
- But GPT-5.2 Commerce (67%) far below Qwen 3.5 Plus (81%)
- Gemini 3.1 Pro: 72.3% overall, highest in Education (84%)
- Claude Opus 4.6: 71.5%, strongest Transportation (77%), weakest Commerce (53%)
- Open-source models competitive: Qwen 3.5 Plus (69.9%) and DeepSeek V3.2 (69.6%) outperform most Claude variants
- Implicit faults (truncated data, missing fields) HARDER than explicit errors — lack overt error signals
- Higher reasoning effort helps: GPT-5.2 improves 27.5 points from minimal to maximum reasoning
- Strong agents ≠ strong environment simulators — simulator quality critical for LES reliability

## Actionable Insights

1. Khi chọn AI agent cho business, KHÔNG assume "best overall = best for your domain" — mỗi model có occupational specialty profile. Ví dụ: healthcare → Qwen 3.5 Plus (81%), commerce → Qwen 3.5 Plus (81%), science → GPT-5.2 (94%), education → Gemini 3.1 Pro (84%).
2. Implicit faults là biggest risk — agents struggle với silent data degradation (missing fields, truncated data) hơn explicit errors. Ví dụ: agent processing insurance claims — missing field trong claim data → agent doesn't detect → wrong decision. Need explicit data validation layer.
3. Higher reasoning effort (thinking budget) significantly improves professional task performance — GPT-5.2 +27.5 points. Ví dụ: complex legal analysis → set max reasoning budget, accept higher latency for better accuracy.

## Assumptions & Limitations

- Giả sử: LES (simulated environments) accurately represent real professional environments — may have simulation gap
- Limitation: 100 scenarios across 10 industries — real-world diversity much larger
- Limitation: Document-grounded tasks only — doesn't cover interpersonal/soft-skill tasks
- Limitation: Fault injection patterns may not cover all real-world failure modes
- Limitation (tự thấy): "Professional task" definition varies — some scenarios may be oversimplified versions of real professional work

## Metadata

- Năm: 2026
- Tác giả: Xiaomeng Hu, Yinger Zhang, Fei Huang, Jianhong Tu, Yang Su, Lianghao Deng, Yuxuan Liu, Yantao Liu, Dayiheng Liu, Tsung-Yi Ho
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2604.10866
- Citation count: N/A
- Nhãn: [applied]
- Skill: N/A — benchmark, no actionable workflow
