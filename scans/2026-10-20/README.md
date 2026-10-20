# Báo cáo distill arXiv — ngày 2026-10-20

Tổng hợp 20 bài paper đã distill hôm nay (#175–#194), được chọn từ scan arXiv và queue tương ứng. Mỗi bài đã qua quy trình distill (6 bước, song ngữ, kiểm tra skill), commit+push GitHub.

## Tổng quan
- Tổng bài distill: **20**
- Tất cả đều có ứng dụng thực tế (nhãn [applied] — có experiment, dataset thật, benchmark cụ thể).

## Danh sách 20 bài hôm nay

### [1] Iterate on an LLM, Serve on an SLM (arXiv 2610.14576v1)
- Làm gì: Nghiên cứu cho thấy một SLM nhỏ (mô hình ngôn ngữ nhỏ — fine-tuned từ dữ liệu thực) có thể ổn định hơn chính mô hình teacher lớn dùng để distillation, vì teacher không deterministik (không cố định — chỉ đồng ý với bản thân 72.7% thời gian) nên đóng vai trò chú thích ồn ào chứ không phải sự thật tuyệt đối.
- Học được gì: Không coi output của model lớn như realitas tuyệt đối; nên thu thập phản hồi thực tế từ vận hành (production) rồi distill vào SLM nhỏ, giảm chi phí vận hành.
- Áp dụng cho bạn: Thay vì để một AI lớn tự kiểm duyệt bài viết của mình, hãy thu thập các nội dung khách hàng thực tế đánh giá cao rồi dùng để huấn luyện model nhỏ rẻ hơn cho quy trình nội bộ.

### [2] Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs (arXiv 2610.23707v1)
- Làm gì: Khẳng định độ đầy đủ (completeness@10) quan trọng hơn độ thu hồi (recall@10) khi agent đa bước (tác nhân xử lý nhiều bước) — thiếu một công cụ trong chuỗi khiến tác vụ thất bại; mỗi lượt tìm kiếm thêm gửi lại toàn bộ cuộc trò chuyện, nên tần suất tìm kiếm quyết định chi phí so với danh sách công cụ tĩnh (ngưỡng ~0.63 tìm búsqueda/lệnh gọi công cụ).
- Học được gì: Khi xây agent nhiều bước, hãy đảm bảo agent tìm được đủ tất cả công cụ cần thiết, không chỉ tìm được công cụ tốt nhất từng bước.
- Áp dụng cho bạn: Khi dùng agent làm nhiều bước (ví dụ tra giá Shopee → so sánh → đặt hàng), hãy kiểm tra xem agent có đủ công cụ cần thiết cho toàn bộ chuỗi, không chỉ mỗi bước.

### [3] TRACER: Trace-Regularized Training Against Indirect Prompt Injection (arXiv 2610.19133v1)
- Làm gì: TRACER giảm tấn công chọc nhắc (prompt injection) gián tiếp qua RAG (truy xuất tăng tạo — tìm kiếm tài liệu rồi sinh câu trả lời) từ 65.5% xuống 6.1% vẫn giữ độ chính xác 78–82%, bằng phần thưởng gated bằng chứng + vết dấu học tập (trace alignment); đào tạo đa kênh (RAG+công cụ) đạt ASR trung bình 13.9% thấp nhất tại model 3B.
- Học được gì: Khi dùng RAG để truy xuất tài liệu, hãy thêm bước kiểm tra bằng chứng trước khi tin tưởng nội dung truy xuất, đặc biệt khi có lệnh ngầm từ bên ngoài.
- Áp dụng cho bạn: Khi AI trích xuất thông tin từ tài liệu khách hàng để lập báo cáo, hãy để AI trích dẫn đoạn gốc và bạn kiểm tra lại trích dẫn trước khi gửi, tránh bị lệnh ngầm trong tài liệu lừa AI.

### [4] Be Careful Who You Trust: Coordination Dynamics under Corrupted Communication in LLM Multi-Agent Games (arXiv 2609.31704v1)
- Làm gì: Sự sụp đổ phối hợp trong game đa agent (nhiều agent làm việc cùng nhau) dưới thông tin hỏng chủ yếu do cơ học (hành động bị đảo ngược thay đổi transcript và thực thi), không phải do hành vi agent; cần tách lựa chọn gốc / hành động công khai / kết quả thực thi khi đánh giá sức mạnh đa agent.
- Học được gì: Khi đánh giá một hệ thống đa agent, hãy xem xét cả hành động công khai và kết quả thực thi thực tế, không chỉ tin tưởng transcript.
- Áp dụng cho bạn: Khi dùng nhiều agent làm việc cùng nhau (ví dụ agent viết bài + agent chỉnh sửa), hãy kiểm tra kết quả cuối cùng gửi đến khách hàng, không chỉ tin lời agent nói họ đã làm xong.

### [5] Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning (arXiv 2609.14896v1)
- Làm gì: MODA dùng điều chỉnh theo vai trò (role conditioning) trong chính sách chia sẻ (mỗi chế độ = agent MARL cạnh tranh) + cổng chất lượng tùy lệnh nhắc (prompt) để tăng độ đa dạng (SBERT diversity) +265% và +75.9% so với DivPO, đồng thời giữ/tăng năng lực chung +10.3%.
- Học được gì: Thêm nhiều "khung nhìn" hoặc persona khác nhau khi sinh nội dung giúp tăng đa dạng mà không làm giảm chất lượng chung.
- Áp dụng cho bạn: Khi dùng AI sinh nhiều caption hoặc tiêu đề bài viết, hãy yêu cầu AI viết theo nhiều góc nhìn khác nhau (ví dụ: góc nhìn khách hàng, góc nhìn bán hàng, góc nhìn chuyên gia) để có nhiều lựa chọn đa dạng.

### [6] Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions (arXiv 2610.22138v1)
- Làm gì: Một agent đối đầu gây sụp đổ niềm tin 44.8% (ba agent 60.5%); nhiễm ẩn (51.6% tài liệu riêng vs 19.7% tán thành công khai) lớn gấp 2.6 lần transcript (bản ghi đối thoại) lộ; kiến thức không dự đoán được sự mạnh mẽ; nhiễm ổn định vào vòng thứ tư, cần can thiệp sớm.
- Học được gì: Trong cuộc thảo luận đa agent, sai sót ẩn ẩn lan rộng gấp nhiều lần so với những gì transcripts cho thấy, nên cần can thiệp sớm trước khi sai sót ổn định.
- Áp dụng cho bạn: Khi dùng nhiều agent thảo luận để ra quyết định kinh doanh, hãy can thiệp sớm nếu thấy việc thảo luận đi theo hướng sai, ch đợi đến khi kết luận ổn định rồi mới sửa (và sẽ muộn).

### [7] When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning (arXiv 2610.04686v1)
- Làm gì: Tranh luận (debate) giúp khi có đề xuất bề mặt câu đúng (không gian khôi phục có thể phục hồi) VÀ có thể nhận diện câu đúng khi bình chọn bỏ lỡ (LVD bằng chứng xác thực); một trong hai không đủ; hội đồng được chọn qua coverage (AC-Greedy/SC-Greedy) tạo nhiều đề xuất đúng bổ sung hơn top-score.
- Học được gì: Tranh luận đa agent chỉ hiệu quả khi kết hợp cả việc đưa ra nhiều đề xuất và việc kiểm tra xác thực, không chỉ đếm số phiếu.
- Áp dụng cho bạn: Khi dùng nhiều AI để cộng ý về một quyết định, hãy yêu cầu chúng cùng ra nhiều giải pháp khác nhau rồi bạn kiểm tra từng giải pháp, chứ không chỉ đếm số AI có ý kiến như nhau.

### [8] Candidate supply and answer selection shape the value of LLM judging in multi-agent systems (arXiv 2608.25937v2)
- Làm gì: Đáp án đúng thường đã có trong nhóm ứng viên nhưng hệ thống vẫn báo cáo sai (khoảng cách tạo–giữ 13–14 điểm phần trăm); độ tin cậy của giám khảo (judge — AI đánh giá) không cố định; kết hợp tần suất bình chọn + xếp hạng giám khảo nâng từ 63.82% lên 70.82–70.95%, cứu đáp án đúng bị loại bởi lỗi phổ biến.
- Học được gì: Không nên tin tưởng một giám khảo AI duy nhất; nên kết hợp nhiều lần bình chọn và xếp hạng để chọn đáp án tốt nhất.
- Áp dụng cho bạn: Khi dùng AI đánh giá hoặc xếp hạng các cơ hội bán hàng/dự án, hãy để AI đánh giá nhiều lần và xếp hạng, chứ không chỉ tin một lần đánh giá.

### [9] RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees (arXiv 2610.11370v2)
- Làm gì: RIT-RAG phân cách việc khám phá bằng chứng khỏi đọc nội dung — truy xuất đảm bảo độ thu hồi, cấu trúc truy xuất đảm bảo độ chính xác; không cam kết vào tài liệu duy nhất trước khi thấy nội dung; đạt kết quả cao nhất trên WixQA, QASPER, FinanceBench, EntQABench (2,84 triệu trang), cao hơn cơ sở tốt nhất +6.6–11.4 điểm.
- Học được gì: Khi dùng RAG, hãy tách việc tìm tài liệu ra khỏi việc đọc và suy luận, và không nên cam kết vào một tài liệu duy nhất quá sớm.
- Áp dụng cho bạn: Khi nghiên cứu đối thủ hoặc thị trường bằng AI, hãy để AI tìm nhiều nguồn khác nhau trước, sau đó mới đọc và tổng hợp, chứ không chỉ tin một nguồn đầu tiên tìm được.

### [10] Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense Retrieval (arXiv 2609.05110v1)
- Làm gì: Phẫu thuật embedding (cập nhật biểu diễn nhúng — cách máy hiểu văn bản) áp dụng cập nhật cục bộ, tối thiểu vào embedding tài liệu tại thời điểm truy vấn qua bài toán tối ưu hóa (bài toán tối ưu hàm bậc hai), ép buộc ràng buộc xếp hạng, tối thiểu hoá sự thay đổi biểu diễn; đối xứng hiệu quả nhất, lên đến +60.64% tương đối nDCG@10 (chỉ số đánh giá tìm kiếm top-10) trên DL-Hard.
- Học được gì: Thay vì huấn lại toàn bộ model, có thể cập nhật cục bộ phần biểu diễn cần thiết để cải thiện xếp hạng tìm kiếm với chi phí thấp.
- Áp dụng cho bạn: Khi dùng hệ thống tìm kiếm nội bộ (ví dụ tìm sản phẩm cũ trong kho ảnh/bài viết), hãy ưu tiên cập nhật các phần quan trọng thay vì làm lại từ đầu, tiết kiệm thời gian và chi phí.

### [11] MuninAI: A Self-Hosted Agentic Framework for Independent Research Groups (arXiv 2610.23480v1)
- Làm gì: Công cụ đóng gói (harness — khung công cụ đóng gói) chứ không phải model là đơn vị cải tiến — cùng harness nhân đôi độ chính xác trên 3 model xpung (backbone — mô hình nền) 2 nhà phát triển (0.387→0.874); naive RAG top-5 kém hơn model thô (bare model — model không bổ sung) trên mọi backbone vì retrieval không có vòng kiểm tra (verification loop) là hại ròng; hệ thống biết từ chối (abstention — từ chối trả lời khi không chắc): xóa tài liệu → hệ thống từ chối 86–92% với 0 trích dẫn bịa (0 citation fabricated — không đặt cite giả).
- Học được gì: Cách bạn đóng gói và sử dụng model quan trọng hơn chính model đó; RAG mà không kiểm tra có thể gây hại hơn không dùng.
- Áp dụng cho bạn: Khi xây dựng trợ lý tra cứu tài liệu nội bộ, hãy đầu tư vào quy trình kiểm tra (ví dụ AI trích dẫn và bạn kiểm tra lại) chứ không chỉ tập trung chọn model lớn nhất.

### [12] Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows (arXiv 2610.21411v2)
- Làm gì: Phân phối công việc đa agent (nhiều agent phối hợp trong quy trình) chỉ cần quyết định giới hạn (bounded decision — quyết định trong ranh giới chặt chẽ) — tách "ra quyết định" (mô hình quyết định Jev) khỏi "sinh văn bản" (LLM chuyên gia) cắt 12,7–54,6% token (đơn vị xử lý văn bản) với độ chính xác trong ±1,34 điểm, nhưng router (bộ điều hướng) phải nhìn thấy thực tế (artifact — sản phẩm thực) mới giữ được độ chính xác (mất 18 điểm nếu content-blind — không nhìn nội dung).
- Học được gì: Trong quy trình đa agent, hãy dùng model nhỏ rẻ để ra quyết định (điều hướng, đánh giá) và chỉ gọi model lớn khi cần sinh nội dung thực tế, từ đó cắt chi phí lớn.
- Áp dụng cho bạn: Khi xây quy trình nội dung bằng AI, hãy dùng quy tắc hoặc model nhỏ để phân loại tin nhắn khách hàng (khiếu nại / hỏi giá / đặt hàng), chỉ gọi model lớn để viết câu trả lời chi tiết, cắt chi phí API.

### [13] How language model agents reshape price competition (arXiv 2610.21711v1)
- Làm gì: Cùng model foundation (mô hình nền) có thể chọn chế độ đối lập hoàn toàn (0.88 vs 0.05 độ cao) chỉ bằng thay đổi giao diện triển khai (giao diện thông tin: ẩn giá cạnh tranh + tóm tắt lịch sử) chứ không phải loại đầu ra; một chiến lược lấy 71–72% lợi nhuận ngành qua cắt giá nhanh, chiến lược khác qua neo và thu hoạch; phần khách hàng 15% vs 95%.
- Học được gì: Cách bạn triển khai (hiển thị thông tin gì, ẩn gì) thay đổi hoàn toàn kết quả cạnh tranh, không chỉ phụ thuộc vào model bạn dùng.
- Áp dụng cho bạn: Khi đăng bán hàng trên sàn thương mại điện tử, hãy cân nhắc kỹ thông tin bạn hiển thị (giá, tồn kho, đánh giá) vì nó ảnh hưởng trực tiếp đến cách khách hàng và đối thủ phản ứng.

### [14] EnterpriseSynth: Zero-Execution SFT and Evaluation Data from OpenAPI Specs (arXiv 2610.22412v1)
- Làm gì: 45 đoạn trajectoire (chuỗi hành động) được xác thực từ đặc tả OpenAPI không cần thực thi (zero-execution — không chạy thật) nâng model 0.5B từ 12.5% lên 87.5% trên API giữ ngoài (held-out — dữ liệu kiểm tra chưa xem); trình xác thực (verifier) phải được kiểm tra đối đầu (adversarial — tấn công kiểm tra) (57–80% ban đầu → 98%); độ chính xác endpoint 48.9% nhưng end-to-end (tham số + giá trị) chỉ 21.3%.
- Học được gì: Có thể sinh dữ liệu huấn luyện từ đặc tả kỹ thuật (OpenAPI spec — mô tả giao diện API) mà không cần thực thi thật, nhưng phải kiểm tra đối đầu để đảm bảo chất lượng.
- Áp dụng cho bạn: Khi muốn AI làm việc với phần mềm nội bộ (ví dụ CRM, kế toán), hãy cung cấp đặc tả chi tiết các chức năng và kiểm tra kỹ trước khi đưa vào vận hành thực tế.

### [15] Cost-Efficient Privacy Enforcement for Email-Generating LLM Agents (arXiv 2610.18007v1)
- Làm gì: Viết lại điều hợp với hợp đồng địa phương (Gemma 4B local — model cục bộ + hợp đồng phát hành thông tin 4 trường) trước khi kiểm tra (checker): rò rỉ (leakage — sızın dữ liệu) 11.41→4.03% bình thường / 28.19→18.79% tấn công, token từ xa giảm −17.6%/−36.6%, số lần gọi checker tăng 1.69×→1.02×, hiệu ích TĂNG (85.2→92.6%) — hợp đồng chiến thắng lệnh nhắc bảo mật chung 36.3–54.1% tương đối.
- Học được gì: Áp dụng hợp đồng về việc phát hành thông tin (tên trường cụ thể) trước khi kiểm tra giúp giảm rò rỉ dữ liệu và tăng hiệu ích, tốt hơn lệnh nhắc bảo mật chung chung.
- Áp dụng cho bạn: Khi dùng AI viết email phản hồi khách hàng, hãy đưa ra quy tắc rõ ràng về những thông tin KHÔNG được để lại (ví dụ: số điện thoại, địa chỉ, mã thẻ) trước khi yêu cầu AI viết, thay vì chỉ nói "giữ bảo mật".

### [16] SAG2: Embedding-Free Multi-Hop Retrieval with BM25 and JEV (arXiv 2610.22588v1)
- Làm gì: SAG2 tìm kiếm nhiều bước (multi-hop retrieval — tìm kiếm nhiều nhảy) không cần cơ sở dữ liệu vector/dịch vụ embedding (biểu diễn nhúng) — chỉ 1 SQLite FTS5 + BM25 + mô hình quyết định (JEV) lưu trú: đạt độ thu hồi R@10 86.62%/97.43%/99.00% (MuSiQue/2Wiki/HotpotQA), đánh bại mọi model embedding 7B + SAG +3.25–3.86 điểm; index 11,656 đoạn trong 2.36s/25.87MiB/$0 không mạng; $4.33/1.000 truy vấn.
- Học được gì: Tìm kiếm nhiều bước không nhất thiết phải dùng vector DB (cơ sở dữ liệu vector) đắt tiền; có thể dùng tìm kiếm văn bản (FTS5) kết hợp mô hình quyết định nhỏ để giảm chi phí.
- Áp dụng cho bạn: Khi cần tra cứu nhiều bước trong tài liệu nội bộ (ví dụ chính sách bảo hành rồi tra mã sản phẩm), hãy dùng tìm kiếm văn bản đơn giản kết hợp quy tắc thay vì hệ thống vector DB phức tạp và đắt tiền.

### [17] Designing for Imperfect Prompts: KG Semantic Mediation for Enterprise Data Assistant (arXiv 2610.23304v1)
- Làm gì: Lệnh nhắc của doanh nghiệp cực ngắn (1–14 câu/~10 từ, 0/158 có tham chiếu sơ đồ); dùng đồ thị tri thức (KG — knowledge network, mạng biểu diễn kiến thức) tự xây từ sơ đồ (273 nút/540 cạnh) trung gian lệnh nhắc: GPT-4.1 độ chính xác 90.67% (sơ đồ thuần 69.05%, +21.62 điểm), F1 89.47% (71.02%); sơ đồ thuần bịmai kết nối (joins — nối bảng) ảo dẫn đến lỗi thực thi tin cậy.
- Học được gì: Khi lệnh nhắc của người dùng ngắn và không cấu trúc, hãy dùng đồ thị tri thức (KG) tự xây từ dữ liệu sẵn có để trung gian và hiểu ý định, tốt hơn dùng sơ đồ dữ liệu thô.
- Áp dụng cho bạn: Khi khách hàng gửi yêu cầu ngắn ngủng ("giá bao nhiêu", "gia hạn dịch vụ"), hãy xây dựng bảng tra cứu đơn giản từ dữ liệu doanh nghiệp để AI trả lời chính xác, chứ không để AI đoán từ cấu trúc cơ sở dữ liệu thô.

### [18] Asymmetric Dynamic Routing (ADR) for Hypergraph RAG (arXiv 2609.29282v2)
- Làm gì: "Sự sa mạc của việc truy xuất tĩnh" — độ sâu duyệt đồng nhất cho mọi truy vấn làm phnością token (truy vấn đơn giản) + thiếu ngữ cảnh (truy vấn phức tạp); ADR dùng trình phân loại + 3 toán tử bất đối xứng: giảm độ trễ 435→238ms (−45.3%), token lệnh nhắc 3,760→1,929 (−48.7%), chất lượng 82.05→83.91 (+1.86) trên cơ sở DHI; đánh bại mọi chế độ đóng băng trên mọi tập dữ liệu +0.94–+2.11 điểm.
- Học được gì: Không nên dùng cùng một độ sâu truy xuất cho mọi truy vấn; hãy điều chỉnh linh hoạt tùy từng truy vấn để tiết kiệm token và tăng chất lượng.
- Áp dụng cho bạn: Khi dùng AI tra cứu thông tin, hãy dùng câu hỏi đơn giản (ít từ khóa) cho việc tra cứu nhanh và câu hỏi chi tiết (nhiều từ khóa) cho việc tra cứu sâu, chứ không dùng cùng cách tiếp cận cho mọi câu hỏi.

### [19] MEMORILLA: Latent Semantic Memory for LLMs (arXiv 2610.21375v1)
- Làm gì: Tách lưu trữ bền vững (persistent storage) khỏi bối cảnh mỗi truy vấn (per-query context) — dùng model nhúng (embedding — biểu diễn nhúng văn bản) cố định nhúng corpus 1 lần, sau đó huấn module nhỏ (194 triệu tham số) trả K token ký niệm (soft memory tokens — ký niệm mềm) thêm vào đầu input của model lớn (Qwen3-8B) không đổi 1 lớp LSTM nào: trung bình 49.68 đánh bại mọi cơ sở, ranh giới Pareto trên mọi chuẩn trong 8, nén token 394× so với bối cảnh đầy đủ, độ trễ 0.74s vs 19.9s. Nhưng ký niệm không giúp nhớ chính xác từng từ (verbatim recall).
- Học được gì: Có thể nén kiến thức lớn thành ký niệm nhỏ và thêm vào đầu input để giảm chi phí suy luận lớn, nhưng không dùng cho việc nhớ chính xác từng chi tiết.
- Áp dụng cho bạn: Khi cần AI nhớ rất nhiều thông tin dài hạn (ví dụ lịch sử khách hàng, kiến thức sản phẩm), hãy dùng cách tóm tắt kiến thức thành ký niệm ngắn gọn rồi cung cấp cho AI, thay vì gửi toàn bộ lịch sử dài mỗi lần.

### [20] Can LLMs Fix It Without Code? No-Code Bug Fix Execution Verification (arXiv 2610.11963v1)
- Làm gì: Xác thực việc thực thi (execution-verify — kiểm tra bằng cách chạy thật) các bản sửa lỗi không mã (no-code fix) do AI sinh ra trong trình duyệt Brave thật: áp dụng bản sửa → cổng kiểm tra script #1 (không có lỗi) → hoàn tác (rollback) → cổng kiểm tra #2 (có lỗi) → tác nhân (executor — thực thi viên) áp dụng bản sửa qua giao diện GUI ≤20 bước -> trình kiểm tra quyết định — lời nhận DONE của tác nhân KHÔNG bao giờ là phán quyết. Độ phân giải (resolution) 49.7% Sonnet 5 / 45.7% OpenCUA / 14.6% Muse Glimmer.
- Học được gì: Không nên gửi bản sửa do AI tạo cho người dùng trước khi xác thực bằng cách thực thi thật; độ tương tự văn bản (BERTScore 0.83 cả hai lớp) hoàn toàn không phân biệt bản sửa đúng/sai.
- Áp dụng cho bạn: Khi dùng AI tạo ra quy trình hoặc bản sửa cho công việc của bạn (ví dụ cấu hình phần mềm, viết script tự động), hãy kiểm tra kết quả thực tế trên máy/trình duyệt thật trước khi áp dụng cho khách hàng, chứ không tin lời AI nói "đã xong".

## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN

Dưới đây là insight hàng đầu từ 20 bài hôm nay, mỗi insight kèm ví dụ áp dụng ngay cho bạn (solopreneur VN):

1. **Tách việc ra quyết định khỏi việc sinh nội dung:** dùng quy tắc hoặc model nhỏ để phân loại tin nhắn khách hàng (khiếu nại / hỏi giá / đặt hàng), chỉ gọi AI lớn khi viết câu trả lời chi tiết → cắt chi phí API (từ bài Jev-LiteMAS).
2. **Không để AI lớn tự kiểm duyệt chính mình:** thu thập phản hồi thực tế đánh giá cao rồi huấn luyện model nhỏ rẻ hơn cho quy trình nội bộ (từ bài Iterate on an LLM, Serve on an SLM).
3. **Không gửi bản sửa do AI tạo cho khách hàng trước khi kiểm tra thực tế trên máy thật** → tránh lỗi giả dương và bản sửa không thực sự hoạt động (từ bài No-Code Fix Execution Verification).
4. **Khi dùng RAG/tra cứu tài liệu, hãy để AI trích dẫn đoạn gốc và bạn kiểm tra lại trích dẫn trước khi sử dụng**, tránh bị lệnh ngầm trong tài liệu lừa AI (từ bài TRACER, RIT-RAG, SAG2).
5. **Xây dựng bảng tra cứu đơn giản từ dữ liệu doanh nghiệp** để AI trả lời yêu cầu ngắn của khách hàng ("giá bao nhiêu", "gia hạn dịch vụ"), chứ không để AI đoán từ cấu trúc cơ sở dữ liệu thô (từ bài Designing for Imperfect Prompts, MEMORILLA).

---

*Báo cáo tự động sinh bởi watchdog_daily.sh sau ngày distill 20 bài (#175–#194). Tất cả bài đã qua quy trình distill, commit+push GitHub.*
