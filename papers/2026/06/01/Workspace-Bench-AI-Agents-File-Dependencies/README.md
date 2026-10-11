# 2605.03596 Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies

## Problem

Existing AI agent benchmarks evaluate trên pre-specified hoặc synthesized files với limited real-world dependencies. Trong thực tế, workers phải navigate complex workspaces với hàng chục file types khác nhau, cross-file dependencies (phụ thuộc liên file), và multi-step tasks yêu cầu holistic workspace understanding (hiểu biết toàn diện về không gian làm việc). Không có benchmark nào evaluate agents trên realistic workspace learning — khả năng identify, reason over, exploit, và update explicit/implicit dependencies (phụ thuộc tường minh/ngầm) giữa heterogeneous files (tập tin đa dạng).

## Contribution

1. Introduce Workspace-Bench — benchmark lớn nhất cho AI agents trên workspace learning, với 5 worker profiles, 74 file types, 20,476 files (up to 20GB), 388 tasks, 7,399 evaluation rubrics. Realistic digital workspaces thay vì synthesized test files.
2. Curate tasks với explicit file dependency graphs — mỗi task có dependency graph cho phép evaluate cross-file retrieval (truy xuất liên file), contextual reasoning (suy luận theo ngữ cảnh), và adaptive decision-making (ra quyết định thích ứng).
3. Five-stage Workspace Learning framework — formalize quá trình agents navigate workspaces: Exploration → Task-Supporting File Utilization → Heterogeneous File Understanding → Lineage Tracing → Semantic Relations Understanding.

## Method (tóm tắt cốt lõi)

Xây dựng workspace thực tế với 5 worker personas (Finance, Engineering, Marketing, HR, Legal), mỗi persona có workspace ~4GB files spanning 74 file types (Excel, Word, PDF, code, images, emails, chat logs). 388 tasks curated bởi human annotators, mỗi task có dependency graph specifying file relationships. Evaluation: 7,399 rubrics — mỗi rubric là binary pass/fail criterion. Task counted correct only if ALL rubrics pass. Test 4 agent harnesses (OpenClaw, DeepAgent, Codex, Hermes) × 7 foundation models (GPT-5.4, Gemini-3.1-Pro, Grok-4.3, MiniMax-M2.7, Qwen-3.6-Plus, GLM-5.1, Kimi-2.5) = 28 configurations. Also provide Workspace-Bench-Lite (100 tasks, ~70% cost reduction).

## Key Findings

- Best agent (DeepAgent + GLM-5.1): ~60% rubrics pass rate on Workspace-Bench-Lite
- Human expert baseline: 80.7% — gap of ~20 points
- Average across all agents: 43.3% (only 45.1% mean pass rate)
- Performance degrades with difficulty: Easy 51.4% → Medium 46.0% → Hard 35.7%
- 3 primary capability bottlenecks: Heterogeneous File Understanding, Lineage Tracing, Semantic Relations Understanding
- 2 dimensions agents handle well: Workspace Exploration, Result-Providing File Utilization
- Harness framework choice significantly impacts performance (same backbone LLM)
- DeepAgent + GLM-5.1 highest, followed by Hermes + GLM-5.1, OpenClaw + GLM-5.1
- 15 agent configurations tested total
- Workspace-Bench-Lite preserves distribution while reducing eval cost ~70%

## Actionable Insights

1. Agent architectures cần invest vào cross-file dependency reasoning (suy luận phụ thuộc liên file) — current tool-use capabilities (file navigation, terminal commands) đủ tốt, nhưng parsing cross-format content và reasoning over deep cross-file dependencies là bottleneck. Ví dụ: enterprise agent cần đọc Excel + Word + PDF cùng lúc để answer questions về quarterly report, nhưng agents hiện tại fail ở việc link data giữa các file.
2. Khi evaluate AI agent cho workplace tasks, cần test trên realistic workspaces với diverse file types — synthesized benchmarks inflate performance. Ví dụ: company evaluating coding agent nên test trên real codebase với configs, docs, tests, CI files, không chỉ coding challenges.
3. Task difficulty stratification (phân tầng độ khó) quan trọng — agents perform well trên simple atomic operations nhưng degrade sharply trên tasks requiring dynamic file relationship reasoning. Ví dụ: agent có thể summarize 1 file tốt, nhưng fail khi cần trace version lineage (lịch sử phiên bản) qua 5 files liên quan.

## Assumptions & Limitations

- Giả sử: rubric-based evaluation captures task completion accurately — có thể miss nuances trong qualitative output
- Limitation: Benchmark hiện tại chỉ cover 5 worker personas, chưa exhaust all workplace scenarios
- Limitation: 20GB workspace sizes — smaller companies có thể có workspaces lớn hơn nhiều
- Limitation (tự thấy): Paper focus vào English-language workspaces, chưa test multilingual environments. File dependency graphs được annotators construct manually — có thể miss implicit dependencies mà humans tự nhiên understand.

## Metadata

- Năm: 2026
- Tác giả: Zirui Tang, Xuanhe Zhou, Yumou Liu, Linchun Li, Yukai Wu, Weizheng Wang, Hongzhang Huang, Wei Zhou, Jun Zhou, Jiachen Song
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.03596
- Citation count: N/A
- Nhãn: [applied]
- Skill: N/A — benchmark evaluation framework, không có workflow actionable cho practitioners
