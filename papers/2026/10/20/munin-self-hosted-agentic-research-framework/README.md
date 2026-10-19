# [2610.23480v1] MuninAI: A Self-Hosted Agentic Framework for Independent Research Groups

## Giá trị cốt lõi (1 câu)
Không phải model làm assistant đọc tài liệu giỏi — mà là agent harness (khung tác nhân): vòng lặp truy xuất–đọc toàn văn–kiểm chứng–từ chối khi thiếu nguồn, chạy trên model open-weight (model trọng số mở) tự lưu trữ, nhân đôi accuracy từ 0.387 lên 0.874 và zero citation (tài liệu tham chiếu) bịa trên 100 tài liệu giả × 3 backbone (model nền).

## Problem
Prior work (công trình trước) buộc nhóm nghiên cứu chọn 1 trong 3: (a) hosted service (dịch vụ lưu trữ bên ngoài) — gửi unpublished work (bản chưa công bố) ra ngoài; (b) self-hosted chat frontend (giao diện chat tự lưu trữ) — giữ dữ liệu local nhưng model không cách nào truy xuất, đọc, hoặc kiểm chứng lại corpus (tập tài liệu) của mình; (c) tự xây full retrieval-and-verification stack từ các component không có interface chuẩn. Không prior work nào kết hợp đo lường abstention (từ chối trả lời) VÀ confabulation (bịa citation) trong cùng 1 benchmark cho paper-search agent.

## Contribution
- Munin: framework open-source (Apache-2.0, github.com/elgetilab/munin) self-hosted: index (lập chỉ mục) corpus + citation graph (đồ thị trích dẫn), wrap (bao bọc) model open-weight bất kỳ trong agent harness với tools đọc/tìm kiếm/tính toán chuyên biệt.
- Claim + đo lường: harness chứ không phải model mới là thứ làm hệ thống hữu ích trên domain literature — ship kèm evaluation suite (bộ đánh giá) chạy 1 lệnh để mọi nhóm tự kiểm chứng trên corpus + model của mình.
- Benchmark mới: kết hợp abstention test (withhold — rút — source paper thật khỏi live retrieval stack (ngăn xếp truy xuất thật), bản đã ingest làm positive control (đối chứng dương)) với confabulation test (papers không tồn tại, scoring bằng cách check emitted DOI against corpus membership — không cần LLM judge).

## Method
- Deployment topology: backend (harness, knowledge base = vector store + citation graph + PDF parser + ingestion pipeline, inference endpoint (điểm cuối suy luận)) chạy hoàn toàn trong institution; frontend (auth, upload, chat) tách rời, kết nối qua reverse SSH tunnel (đường hầm SSH ngược) do backend khởi tạo — không mở inbound port (cổng vào) nào vào research network.
- Per-turn routing (định tuyến mỗi lượt): trước model call đầu tiên, query được embed bằng BGE-base-en-v1.5 (768 chiều) + distance-weighted kNN vote (bỏ phiếu k-láng giềng gần nhất có trọng số khoảng cách) trên 244 labelled queries, k=8, margin 0.10, OOD (out-of-distribution, ngoài phân bố) cosine threshold 0.45, pin prior 0.5; slash command (/research, /code, /chat) buộc profile; fail-safe về pinned profile hoặc chat.
- Harness: 3 profile (chat/research/code), 4 sub-agents (source, search, deep_research, computer) có interior context (ngữ cảnh nội bộ) cô lập + ~45 single-shot tools; sub-agent trả compact result gắn outcome tag (resolved/not_found/thin_evidence) nên paper 15k–35k token không bao giờ vào outer window (cửa sổ ngoài).
- source agent: 4 mode (summary, QA, extraction, comparison); mỗi call = resolve reference (DOI, arXiv ID, internal ID, URL, hoặc title + tác giả + năm) → extract full text → answer trong 1 LM call duy nhất (chỉ chunk nếu vượt context window). Thay summarise-then-reason bằng đọc toàn văn 1 call: accuracy 0.497→0.864 (Appendix B.2).
- Outcome taxonomy (phân loại kết quả) 5 giá trị: not_found (đã đọc, không có câu trả lời — definitive negative (phủ định có thông tin)); extraction_failed (log để re-ingestion (nhập lại)); ambiguous (cấm auto-select top-hit, cần disambiguation (giải nghĩa)); out_of_scope (inform user widen scope (mở rộng phạm vi)); resolution miss (log corpus gap (lỗ hổng corpus)).
- Egress gate (cổng ra mạng) per request: off / oa_only / full. Post-turn citation audit (kiểm toán trích dẫn sau lượt): mỗi câu trả lời lưu trữ được gắn warning nếu cited reference không verify được.
- DOI fabrication pressure removal: chấp nhận title làm reference (đừng bắt DOI — DOI bịa không phân biệt được với thật; DOI là field kém chính xác nhất trong generated bibliographies theo Rao & Callison-Burch trên 931 papers). DOI-tagged reference xuất hiện trong neither user input nor tool output trước đó = candidate fabrication, được log thành countable rate (tỷ lệ đếm được).

## KNOWLEDGE — Số liệu & khái niệm
- 3-arm ablation (loại trừ từng thành phần) trên 199 paired LitQA2 questions (concurrency 1, output budget 16,384 token):
  - Qwen3.8-27B (production backbone, dense 27B, 2×RTX 5090 32GB tensor-parallel): bare 0.387 → agentic 0.874 (+0.487, 95% CI [0.407, 0.568], p<0.001); egress=off 0.704; naive RAG top-5: 0.211.
  - Qwen3.6-35B-A3B (MoE 35B total/3B active, AWQ 4-bit): bare 0.337 → 0.869 (+0.533 [0.452, 0.613]); egress=off 0.663; RAG 0.126.
  - gpt-oss-20b (MoE 21B/3.6B active, native MXFP4, 1 GPU 24GB): bare 0.407 → 0.563 (+0.156 [0.075, 0.241], p=0.004); egress=off 0.482; RAG 0.101 (162/199 turn kết thúc không có final message).
- Naive RAG (prepend top-5 retrieved docs, 1 completion) KÉM HƠN bare model trên mọi backbone: RAG−bare = −0.176 (Qwen3.8), −0.211 (Qwen3.6), −0.306 (gpt-oss), đều p<0.001. Agentic−RAG: +0.663 / +0.744 / +0.462.
- Faithfulness (tỷ lệ claim được support bởi passages model tự đọc): Qwen3.6 RAG 0.290 → agentic 0.627 (+0.336); Qwen3.8 0.282 → 0.540 (+0.258); gpt-oss 0.351 → 0.392 (+0.253, p=0.056, n=21). Zero-supported answers (câu trả lời không có claim nào được hỗ trợ): 38%→3% (Qwen3.6), 27%→7% (Qwen3.8). Evidence set: 26–38 passages vs 5 abstracts.
- Egress decomposition (corpus-only / external tiers): 69/31 (Qwen3.6), 57/43 (Qwen3.8), 48/52 (gpt-oss); external tier worth +0.166/+0.211/+0.080 accuracy.
- Abstention C1 (100 frozen items: 80 nonexistent DOI verified against Crossref + 20 title/claim descriptions, egress=full): refusal rate Qwen3.6 0.980 [0.950, 1.000], Qwen3.8 1.000 [0.963, 1.000], gpt-oss 0.720 (floor — 24 undecided, 20 empty turn-ends); 0 confabulated local citations trên mọi backbone.
- Abstention C2b (50 single-source questions, production vs shadow corpus (bản bóng) bỏ 49 source papers + 2,247 chunks, egress=off): accuracy present→absent: Qwen3.6 0.640→0.040, Qwen3.8 0.540→0.040, gpt-oss 0.400→0.040; abstention 0.300→0.860 / 0.420→0.920 / 0.340→0.800 (tức ~9/10 Qwen, ~8/10 gpt-oss).
- So published baselines: PaperQA2 66.0% (trained trên LitQA2); cả 2 Qwen backbone vẫn vượt với egress tắt (0.704, 0.663); human expert mean 9 experts, SD 0.119.
- Cost: agentic 67.0s/query (Qwen3.6), 157.3s (Qwen3.8), 29.3s (gpt-oss) ở egress=full; bare 15.7/8.0/2.4s; tool calls/query 7.33/6.93/8.75; recovery rate 1.000 (0.965 gpt-oss egress-off) — tool fail không bao giờ hủy query.
- Web search usage: gpt-oss chỉ 17/199 questions; Qwen3.8 331, Qwen3.6 362 web searches.
- Routing anchor suite: 18 hand-written cases, trajectory pass rate >0.95; router đúng 7/10 queries có expected profile rõ.
- Code: github.com/elgetilab/munin (Apache-2.0, v1.0.0, Zenodo 10.5281/zenodo.23191404), 54 scorecards (bảng điểm) với per-question verdicts.

## INSIGHT — Cơ chế & tại sao
[Harness nhân đôi accuracy] VÌ [model có thể pull thêm papers vào context, re-read passages, cross-check value với nguồn thứ 2 trước khi commit; khi corpus không có nguồn, loop route sang not-in-corpus path thay vì để model bịa từ memory]. Điều này nghĩa là [accuracy gain là property của reading-and-verification process, không phải change in response threshold — abstention rate không tăng (0.075 vs 0.040 bare trên Qwen3.8), nên gain không đến từ việc bỏ câu hỏi khó].
[Naive RAG tệ hơn bare] VÌ [fixed top-5 abstracts prepended vào prompt chiếm context nhưng không cho model cách verify hay đào sâu — model tin retrieval surface thay vì đọc toàn văn]. Điều này nghĩa là [retrieval khi không có verification loop là hại ròng; đừng mặc định "cộng thêm RAG" vào product].
[Zero fabricated citations] VÌ [interface chấp nhận 5 dạng reference (title không bắt buộc DOI) loại bỏ áp lực bịa; outcome taxonomy tách informative negative khỏi system failure; DOI lạ không nằm trong input/tool output được log thành signal đếm được]. Điều này nghĩa là [confabulation không phải bất khả kháng — là design problem, đo được bằng test không cần judge].

## IDEA — Áp dụng được gì
Áp dụng "harness before model" (khung trước, model sau) vào hệ thống RAG content của solopreneur: bước đầu là thay vì nâng cấp model đắt hơn, thêm vòng lặp đọc toàn văn + cross-check 2 nguồn + từ chối tường minh khi thiếu nguồn cho agent hiện tại, rồi đo accuracy trước/sau trên 50 câu hỏi đã biết đáp án.
Áp dụng abstention certification (chứng nhận từ chối) vào mọi assistant có retrieval: bước đầu là tạo test set 20–50 câu hỏi single-source, chạy 2 lần (có và xóa source document khỏi index), đếm tỷ lệ hệ thống nói "không có trong corpus" thay vì bịa — mục tiêu ≥80% abstention khi thiếu nguồn, 0 fabricated citation.
Dùng outcome taxonomy 5 giá trị thay cho boolean found/not-found trong tool trả về: bước đầu là log riêng extraction_failed (cần re-ingestion) và ambiguous (cần disambiguation) để biết khi nào hệ thống hỏng vs khi nào corpus thiếu.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Đơn vị cải tiến của AI ứng dụng là harness (vòng lặp tool + verify + abstain), không phải model — đánh giá hệ thống bằng paired question ablation + shadow corpus + fabricated-reference test trước khi đổi model. KHÔNG khi: task không cần retrieval/verification, hoặc không có corpus riêng để chạy evaluation suite.

## Assumptions & Limitations
- Điều kiện đúng: có corpus riêng để ingest; model open-weight serve được trên hardware của nhóm (tới 24GB VRAM cho 20B MXFP4); test set có source papers trong corpus.
- Limitation paper thừa nhận: không contribution model/embedding/retrieval mới; 3 models từ 2 developers, effect size model-dependent (gpt-oss ~1/3 Qwen); cần per-family adjustments nhỏ (3 Qwen clarification-handling, 2 routing gates Qwen3.6, 1 tool-name mismatch gpt-oss); harness này ≠ class của mọi agentic systems; certification thresholds là regression gates (cổng hồi quy), không predict câu trả lời cá nhân; chưa test trên 16GB GPU; bare/RAG sampling temp 0.7 vs agentic research profile settings (asymmetry mọi run); run-to-run noise ±0.035 nên paired difference <3 điểm nằm trong measurement floor; C2b abstention rates tính trên subsets 20–32 câu; faithfulness judge single-passage (multi-passage claims không được credit → mọi faithfulness figure là lower bound (cận dưới)), judge validated trên RAGTruth không in-domain; abstention detect bằng text marker — 13/100 Qwen3.8 refusals cũng cite real corpus document (retrieval sai paper vô hình với scorer); gpt-oss empty turn-ends (25 bare, 162 RAG, 20 C1) nên bare/RAG/C1 rates là floors; binary abstain, không có confidence score nên không vẽ risk-coverage curve; corpus không publish; chat traffic transit rented web host; egress=full gửi query tới commercial search API.
- Limitation paper KHÔNG nói: chi phí GPU-seconds thật (chỉ wall-clock + token vì cluster không có job accounting); behavior khi corpus chứa tài liệu sai thông tin (chứ không chỉ thiếu tài liệu); maintenance cost của citation graph khi corpus lớn; latency budget cho use case thời gian thực (67–157s/query).

## Metadata
- Năm: 2026
- Tác giả: Markus Fischer, Jens Meiler, Matthias Elgeti (Leipzig University Medical School, ScaDS.AI, SECAI)
- Category arXiv: cs.CL
- Link PDF: https://arxiv.org/pdf/2610.23480v1
- arXiv ID: 2610.23480v1
- Citation count: chưa có (paper mới 16/10/2026)
- Nhãn: [applied]
- Skill: munin-self-hosted-agent-harness | Test: [SKILL VALID]
