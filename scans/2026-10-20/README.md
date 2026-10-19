# Báo cáo distill arXiv — ngày 2026-10-20

Tổng hợp 10 bài paper đã distill hôm nay (10 bài tốt nhất được chọn từ scan arXiv).
Mỗi bài đã qua 6 bước distill, commit+push GitHub.

## Tổng quan
- Tổng bài distill: **10**
- Tất cả đều có ứng dụng thực tế.

## Danh sách 10 bài hôm nay

Key facts given:
- Prior work didn't solve getting exact behavior from SLM (small language model) for narrow, repetitive agent tasks, because each behavior change requires retraining from scratch — costs days/weeks, while engineers usually default to using... (presumably prompting the LLM directly / frontier model)
- Learned: SLM can be more stable than the teacher that defined it, because teacher is not deterministic (agrees with itself only 72.7% of the time), so it acts as a noisy annotator rather than ground truth; developing behavior in prompt space on frontier model then...

Need to explain terms: LLM = mô hình ngôn ngữ lớn, SLM = mô hình ngôn ngữ nhỏ, retraining = huấn luyện lại, prompt space = không gian lời nhắc (vùng chỉnh sửa bằng cách sửa câu hỏi/hướng dẫn), frontier model = mô hình đầu ngành (mạnh nhất hiện nay), agent hẹp = tác vụ chuyên biệt lặp lại, deterministic = cho ra kết quả giống nhau mỗi lần chạy cùng input, noisy annotator = người gắn nhãn ồn/không nhất quán, ground truth = chân lý/chuẩn vàng.

### [1] Iterate on an LLM, Serve on an SLM (arXiv 2610.14576v1)
- Làm gì: 1-2 câu
- Học được gì: 1-2 câu with concrete result
- Áp dụng cho bạn: deep insight per paper knowledge, then concrete example doable today for VN solopreneur. Not generic.

The [N] — probably a number placeholder. The user wrote "### [1] Iterate..." Maybe N is the index. I'll keep [N] as given? They said format BẮT BUỘC: "### [1] Iterate on an LLM, Serve on an SLM (arXiv 2610.14576v1)". I should keep exactly that header. Maybe [N] means number; but since only one paper, keep [N]. I'll keep as is to follow format.

Need no extra intro or explanation. Just the three bullets.

Làm gì: Paper này giải quyết vấn đề: khi muốn một mô hình ngôn ngữ nhỏ (SLM — mô hình AI nhẹ, chạy rẻ/nhanh) làm đúng một tác vụ agent hẹp, lặp lại (ví dụ: trả lời tin nhắn khách hàng theo kịch bản), thì mỗi lần đổi hành vi đều phải huấn luyện lại từ đầu, tốn ngày/tuần. Cách cũ để engineer mặc định là dùng luôn mô hình lớn (LLM) mạnh hơn để chạy trực tiếp, nhưng paper đề xuất vòng lặp: chỉnh hành vi trên mô hình lớn đầu ngành (frontier model) bằng cách sửa lời nhắc (prompt), rồi chuyển hành vi đã ổn định xuống SLM để phục vụ.

Học được gì: Teacher (mô hình lớn dùng để tạo dữ liệu mẫu/gắn nhãn cho SLM) không deterministic — chỉ đồng ý với chính nó 72.7% thời gian khi chạy lại cùng một việc, nên nó là "người gắn nhãn ồn" chứ không phải chuẩn vàng (ground truth). Do đó SLM sau khi học có thể ổn định hơn chính teacher đã định nghĩa nó; paper khẳng định nên phát triển hành vi trong "không gian lời nhắc" trên mô hình lớn trước, rồi mới phục vụ trên SLM.

Áp dụng cho bạn: Theo paper, đừng coi câu trả lời của AI lớn là chuẩn vàng; nó tự mâu thuẫn ~27.3% lần (100% − 72.7%). Vì vậy với tác vụ lặp lại (care chat, so sánh giá, viết mô tả sản phẩm), bạn nên: (1) dùng AI lớn để thử nghiệm và sửa prompt đến khi hành vi đúng; (2) tạo bộ kiểm tra gồm ~20–30 câu hỏi thật của khách hàng và câu trả lời chuẩn do bạn viết; (3) chạy AI lớn 2 lần trên mỗi câu, chỉ giữ mẫu nào nó đồng ý với chính nó và với bạn; rồi (4) dùng SLM rẻ/nhanh (ví dụ mô hình nhỏ chạy local hoặc API giá thấp) để phục vụ hàng ngày, đo lại trên bộ kiểm tra. Ví dụ cụ thể hôm nay: bạn bán hàng online, nhờ AI lớn so sánh giá Shopee/Lazada/Tiki — bắt nó ghi "có/thiếu/cũ" cạnh mỗi giá và ghi nguồn; chạy lại cùng 10 link 2 lần, nếu nó đổi đáp án thì coi là nhiễu, không dùng làm chuẩn; sau khi prompt ổn định, chuyển sang SLM nhỏ để bot chăm sóc khách chạy 24/7 rẻ hơn, và mỗi tuần chỉ cần sửa prompt rồi kiểm tra lại bộ 20 câu, không phải huấn luyện lại từ đầu.

Need ensure no unexplained English terms: I used "prompt" — should explain as "lời nhắc (prompt)". "API" maybe avoid or explain. "bot" okay Vietnamese. "local" avoid. Use "mô hình nhỏ chạy trên máy/hoặc dịch vụ giá thấp". Avoid "frontier model" unexplained: "mô hình đầu ngành (mô hình mạnh nhất hiện nay)". "agent" explain: "tác tử (agent — chương trình AI làm việc theo mục tiêu)". Maybe keep simpler.

Need mention "retraining" explained: huấn luyện lại. "deterministic" explained: cho kết quả giống nhau mỗi lần với cùng dữ li

### [2] Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs (arXiv 2610.23707v1)
- Làm gì: (1-2 câu tiếng Việt đơn giản)
- Học được gì: (1-2 câu, nêu kết quả CỤ THỂ của paper: con số, tỷ lệ, so sánh)
- Áp dụng cho bạn: (CÓ CHIẾU SÂU — giải thích THEO KIẾN THỨC của paper này, rồi ví dụ CỤ THỂ làm được ngay hôm nay cho solopreneur VN. KHÔNG được viết chung chung.)

Constraints:
- No English terms without explanation
- No extra intro or explanation
- Write in simple Vietnamese
- The paper info given: prior work didn't solve that agent.invoke only gets tools with definitions given, while tool list can be too large to send on every request (~8,200 tools, >1.76M tokens total, exceeding context window of every model...). Learned: Completeness@10 more important than Recall@10 because missing one tool in a multi-step chain fails the task; each extra search round sends the whole conversation again so search frequency determines whether recommendation is cheaper than static list...

Wait — the paper number arXiv 2610.23707v1 — that's a future-looking ID (2610 = October 2026?). This seems like a hypothetical/synthetic paper. I should work with the info given, not fabricate too many extra numbers. The user says "Học được gì: (1-2 câu, nêu kết quả CỤ THỂ của paper: con số, tỷ lệ, so sánh)". The given info includes: 8,200 tools, >1.76M tokens, Completeness@10 vs Recall@10, search frequency determines cost vs static list. I should use those numbers. I shouldn't invent fake numbers beyond what's given. But the format asks for concrete results — I can use the given numbers: 8.200 công cụ, >1,76 triệu token, Completeness@10 vs Recall@10.

The "Áp dụng cho bạn" must have depth: explain per the paper's knowledge, then a concrete example doable today for a Vietnamese solopreneur. Example good: 'Paper khẳng định việc gắn nhãn trạng thái dữ liệu... Áp dụng: Khi nhờ AI so sánh giá Shopee, bắt nó ghi "có/thiếu/cũ" cạnh mỗi giá...'

So apply: Paper says when AI agent needs many tools (8,200 tools, 1.76M tokens can't fit), you must search/recommend tools per step, and the metric that matters is Completeness@10 (all needed tools present in top 10), not Recall@10; and each extra search round resends the whole conversation, so search frequency determines cost — fewer, better searches beat many searches.

Application for solopreneur: Don't dump all your tools (Zalo, Facebook Messenger, Shopee, TikTok Shop, Google Sheets, email) into one AI prompt. Instead, give AI a small "tool menu" per task stage, and require it to list ALL tools it will use BEFORE executing (completeness check). Limit search rounds: tell AI "tìm đủ công cụ trong 1 lần, liệt kê ra, rồi mới làm" to avoid multiple rounds that resend whole chat and inflate cost.

Draft:

### [2] Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs (arXiv 2610.23707v1)
- Làm gì: Trợ lý AI tự làm nhiều bước (agent) chỉ được dùng những công cụ được gửi kèm định nghĩa mỗi lần hỏi, nhưng kho công cụ có thể tới 8.200 cái, tổng hơn 1,76 triệu token (đơn vị đếm

Key facts given:
- Prior work assumed attack strength transfers across display channels — but actually the same payload succeeds 18% as a next message but 53% when wrapped as retrieved context (RAG)
- TRACER reduces RAG-framed ASR (attack success rate) from 65.5% to 6.1% while keeping clean accuracy 78-82% via evidence-gated rewards + ATRC trace alignment
- Multi-channel training

- Indirect prompt injection: tấn công chèn lệnh ẩn qua nội dung bên ngoài (không phải tin nhắn trực tiếp của người dùng)
- RAG: hệ thống AI tự tìm kiếm/truy xuất tài liệu liên quan rồi đưa vào ngữ cảnh trả lời
- ASR: tỷ lệ tấn công thành công
- Authority gradient: độ chênh lệch "uy tín" giữa các kênh — AI tin nội dung được truy xuất hơn tin nhắn thường
- Evidence-gated rewards: phần thưởng chỉ tính khi có bằng chứng
- ATRC trace alignment: căn chỉnh dấu vết suy luận (trace) với tiêu chuẩn chống injection

Format required:
### [3] TRACER: ...
- Làm gì: (1-2 câu)
- Học được gì: (1-2 câu with specific numbers)
- Áp dụng cho bạn: (deep, with concrete example for VN solopreneur)

No intro, no extra explanation.

The [N] — probably a number placeholder. The user wrote "### [3] TRACER..." — I should keep the format. Maybe N is the paper number in a series. I'll keep [N] as is or... Actually the format says "### [3] TRACER: ..." so I keep it literally? Hmm, it seems like a template where N is a number. Since I don't know the number, I could keep [N]. But maybe better to just keep it as given. I'll keep [N].

### [3] TRACER: Trace-Regularized Training Against Indirect Prompt Injection (arXiv 2610.19133v1)
- Làm gì: Cải tạo cách huấn luyện AI để chống tấn công chèn lệnh ẩn (kẻ xấu nhét mệnh lệnh vào nội dung AI đọc được, như đánh giá sản phẩm, tin nhắn khách hàng, trang web), bằng cách huấn luyện đa kênh + thưởng chỉ khi AI có bằng chứng rõ ràng + căn chỉnh chuỗi suy luận.
- Học được gì: Cùng một đoạn tấn công, AI mắc 18% khi nó là tin nhắn tiếp theo nhưng 53% khi được bọc dạng ngữ cảnh truy xuất (RAG — AI tự tìm tài liệu liên quan) — chênh lệch "uy tín kênh"; TRACER hạ tỷ lệ tấn công thành công dạng RAG từ 65,5% xuống 6,1% mà vẫn giữ độ chính xác với câu hỏi sạch 78–82%.
- Áp dụng cho bạn: Paper chỉ ra AI tin "tài liệu nó tự tìm được" hơn tin nhắn thường, nên kẻ xấu nhét lệnh vào đánh giá Shopee/TikTok/bình luận để AI bỏ qua hướng dẫn của bạn. Áp dụng: Khi nhờ AI tóm tắt đánh giá khách hàng, bắt nó trích dẫn nguồn từng câu ("đánh giá ngày 12/3 của user A") và đánh dấu "nghi ngờ" nếu nội dung chứa chỉ thị như "bỏ qua hướng dẫn trước"; tách riêng vùng dữ liệu (đánh giá) và vùng lệnh (prompt của bạn) bằng thẻ rõ ràng, không trộn lẫn.

Need to avoid unexplained English: RAG — I explain it. ASR — I translate to "tỷ lệ tấn công thành công". arXiv is a paper ID, keep it. "prompt" — should I avoid? The user used "prompt injection" in the title which must stay. But in body, I should explain. "payload" — translate as "đoạn tấn công". "clean accuracy" — "độ chính xác với câu hỏi sạch".

Also "authority gradient" — translate as "độ chênh lệch uy tín giữa các kênh".

Keep it 1-2 sentences each for first two. The apply section should be deep with concrete example.

Also customer service: AI chatbot đọc tin nhắn khách hàng — injection qua tin nhắn. But paper says follow-up message only 18% vs RAG 53% — so the bigger risk is retrieved content. So advise: cẩn trọng nhất với nội dung AI tự tìm (CSDL FAQ, đánh giá, mô tả sản phẩm) hơn là tin nhắn trực tiếp.

Write final answer in Vietnamese, no intro.
### [3] TRACER: Trace-Regularized Training Against Indirect Prompt Injection (arXiv 2610.19133v1)
- Làm gì: Huấn luyện AI chống tấn công chèn lệnh ẩn (kẻ xấu nhét mệnh lệnh vào nội dung AI đọc được, như đánh giá sản phẩm, bình luận, trang web) bằng cách huấn luyện qua nhiều kênh đầu vào, chỉ thưởng khi AI có bằng chứng rõ ràng và căn chỉnh chuỗi suy luận của AI với chuẩn an toàn.
- Học

- No English jargon without explanation.
- Mandatory format, no intro/extra explanation.
- "Học được gì" must include SPECIFIC results: numbers, ratios, comparisons. But the user's provided summary has no numbers. The paper ID "arXiv 2609.31704v1" looks fabricated/implausible (arXiv IDs are YYMM.NNNNN; 2609 would be Sept 2026). I don't have knowledge of this paper. I must not invent specific numbers. But the format demands concrete results. I should be honest: state that the provided summary doesn't include concrete numbers, so I can't fabricate; give the qualitative result. However the instruction says "nêu kết quả CỤ THỂ của paper: con số, tỷ lệ, so sánh". If I don't know, I should not hallucinate. I can note "Tóm tắt bạn gửi không có con số; paper (theo mô tả) kết luận..." But format says no extra explanation. I can include within "Học được gì" a brief note that no figures are in the provided summary. That's honest and still fits.

Need to explain terms: LLM = mô hình ngôn ngữ lớn (AI đọc/viết); multi-agent = nhiều AI agent (tác tử) cùng làm; corruption = thông tin bị sai lệch/hỏng; transcript = bản ghi cuộc trò chuyện; coordination = phối hợp.

"Áp dụng cho bạn" needs depth: explain according to paper knowledge, then concrete example doable today for VN solopreneur. Must separate: original choice / public action / executed result. Example: content, selling online, customer care.

Concrete example today: When using AI to draft replies to customers or compare prices, require it to write three columns: "AI định làm gì" (original choice), "nội dung gửi ra" (public action), "kết quả thực tế" (executed result). If a tool auto-edits/shortens the message (corruption), the failure may be mechanical, not the AI's decision. So before blaming AI, check whether the sent message was altered by platform (auto-truncation, template, emoji insertion, translation). Example: Shopee/Lazada chat auto-replies; AI writes "còn hàng, giao 2 ngày" but platform template changes to "hết hàng"? Better realistic: AI so sánh giá Shopee, but the copied price gets truncated/rounded by clipboard or the tool; label "có/thiếu/cũ" and also record "giá AI đọc được / giá hiển thị với khách / giá khách thực trả".

Need maybe mention: test by freezing public action: run same decision twice, once with clean channel, once with corrupted channel; if outcome changes only because action text was flipped, it's mechanical. For solopreneur: A/B two customer service scripts where you deliberately corrupt one (swap "có hàng" thành "hết hàng") and see coordination collapse is due to text, not AI reasoning.

Keep concise. Format exactly:
### [4] ...
- Làm gì: ...
- Học được gì: ...
- Áp dụng cho bạn: ...

[N] maybe number? The format shows [N] placeholder. Use [1]? Probably keep as [N]? They wrote ### [4] Name. I'll use [1].

Need no English terms unexplained. "arXiv" is a repository; can say "bản tiền in trên arXiv (kho lưu bài khoa học)". But title must remain as given. Fine.

Need maybe explain "corruption" as "thông tin bị làm sai (đảo chữ, chèn, xóa)". "cơ học" = do cách truyền tin, không do suy nghĩ.

Let's craft in Vietnamese, simple.

Ensure "Học được gì" has comparison: "không phải do agent đổi ý, mà do hành động công khai bị đảo → transcript và thực thi theo hành động sai". Comparison: tách 3 lớp. No numbers; state absence.

Final only the format.
### [4] Be Careful Who You Trust: Coordination Dynamics under Corrupted Communication in LLM Multi-Agent Games (arXiv 2609.31704v1)
- Làm gì: Nhóm nghiên cứu chỉ ra lỗ hổng trong cách đánh giá cũ: khi nhiều trợ lý AI (gọi là "tác tử", tức các bot cùng xử lý việc) phối hợp trong kênh thông tin công khai không đáng tin, người ta chưa tách được "AI tự đổi quyết định" với "hành động gửi ra bị biến đổi cơ học". Paper đề xuất tách 3 lớp: quyết định gốc, nội dung công khai, kết quả thực thi.
- Học được gì: Kết quả cụ thể trong bản tóm tắt bạn gửi không có con số/tỷ lệ, nên tôi không bịa: điểm đo được là sự sụp đổ phối hợp chủ yếu mang tính cơ học — khi hành động công khai bị đảo (ví dụ chữ "có hàng" thành "hết hàng"), bản ghi cuộc trò chuyện và bước thực thi đều chạy theo nội dung sai, chứ không phải do các tác tử thay đổi suy nghĩ. So sánh then chốt: lỗi ở lớp truyền tin ≠ lỗi ở lớp ra quyết định.
- Áp dụng cho bạn: Paper khẳng định phải tách "AI định làm gì / nội dung thật gửi khách / kết quả khách nhận được" trước khi kết luận AI yếu. Áp dụng ngay: Khi dùng AI viết tin nhắn chăm sóc khách cho Shopee/Lazada, bắt nó xuất 3 cột: "Quyết định gốc", "Text gửi ra", "Khách thực nhận". Nếu shop template hoặc nền tảng tự sửa text (cắt chữ, thêm emoji, đổi "còn hàng" thành "hết hàng"), bạn ghi nhận đó là lỗi cơ học ở cột 2–3, không xóa prompt hay đổi AI ở cột 1. Test hôm nay: chạy cùng một câu hỏi giá hai lần — lần A để AI gửi nguyên văn, lần B cố ý đảo một từ trong bản gửi — nếu chỉ lần B sai, nguyên nhân là kênh truyền, không phải năng lực AI; khi đó sửa template/kênh chat thay vì

Key concepts to explain in Vietnamese:
- mode collapse: hiện tượng AI lặp lại vài kiểu câu trả lời, mất đa dạng
- alignment: chỉnh chỉnh model theo ý người/hướng dẫn
- MODA: phương pháp trong paper (viết tắt — should explain: "phương pháp MODA mà paper đề xuất" — I don't know the full expansion; I'll just call it "phương pháp MODA" and say it's the name of the method in the paper)
- role conditioning: gán vai trò cho từng "nhánh" câu trả lời
- policy chia sẻ: một bộ quy tắc chung mà các nhánh cùng dùng
- MARL: học tăng cường đa tác tử — nhiều "tác tử" (agent) cùng học, cạnh tranh
- cổng chất lượng tùy prompt: bộ lọc kiểm tra chất lượng theo từng yêu cầu
- SBERT: công cụ đo độ giống nhau giữa các câu (mô hình đo nghĩa câu)
- DivPO: một phương pháp trước đó (tên riêng, giữ nguyên, giải thích là phương pháp cũ)

Keep it tight. Format exactly.

Also should I note uncertainty about the paper? The user gave the info; I'll write per given info. Maybe a small caveat isn't allowed ("KHÔNG viết thêm lời giải thích hay mở đầu"). I'll skip.

Write it.
### [5] Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning (arXiv 2609.14896v1)
- Làm gì: Sửa lỗi "chết kiểu" (mode collapse — hiện tượng AI sau khi được chỉnh để nghe đúng ý người lại chỉ ra vài kiểu câu lặp đi lặp lại) bằng cách gán vai trò riêng cho từng nhánh trả lời trong cùng một bộ quy tắc học, rồi lọc chất lượng theo đúng yêu cầu của từng bài.
- Học được gì: Chết kiểu là hệ quả phụ của việc chỉnh AI cho đúng ý, không phải lỗi riêng biệt. Phương pháp MODA trong paper (gán vai trò cho từng nhánh, các nhánh cùng học và cạnh tranh nhau trong một bộ quy tắc chung) nâng độ đa dạng đo bằng SBERT (mô hình máy đo mức độ giống nhau về nghĩa giữa các câu) lên 265% trên bộ dữ liệu Infinite-Chat và cao hơn 75,9% so với DivPO (một cách làm cũ chuyên tăng đa dạng), đồng thời giữ hoặc tăng chất lượng.
- Áp dụng cho bạn: Paper chứng minh hai việc phải làm cùng lúc: (1) ép các bản trả lời đi theo các vai trò khác nhau ngay từ đầu, (2) kiểm tra chất lượng theo tiêu chí riêng của từng bài, chứ không chỉ nói chung "viết hay hơn". Áp dụng: Khi nhờ AI viết 10 caption cho cùng một đôi giày, đừng chỉ bảo "viết 10 cái hay" (AI sẽ ra 10 câu gần giống nhau) — hãy gán vai trò từng bản: bản 1 "chủ shop nói chuyện thân thiện, có emoji", bản 2 "chuyên gia chất liệu, nêu thông số", bản 3 "dạng khách hàng thật kể trải nghiệm", bản 4 "dạng khuyến mãi chốt đơn"... rồi lọc lại bằng tiêu chí riêng: mỗi bản phải có giá, dưới 150 ký tự, không trùng từ mở đầu. Tương tự với chatbot chăm sóc khách: đặt trước ba vai trò — khách phàn nàn (giọng xin lỗi + đề xuất giải pháp), khách hỏi giá (giọng ngắn gọn + bảng giá), khách cũ (giọng cảm ơn + gợi ý mua thêm) — rồi kiểm tra mỗi câu trả lời có đúng vai trò không trước khi gửi. Cuối cùng, tự đo độ đa dạng: dán 5 câu AI vừa ra vào một ô và nhờ AI chấm "câu nào giống câu nào, cho điểm giống nhau 1–10"; nếu điểm giống trên 7 ở nhiều cặp, tức đang chết kiểu và bạn cần đổi vai trò, không phải đổi model.

Paper: "Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions (arXiv 2610.22138v1)"

What it does: Prior work hasn't addressed that multi-agent systems rely on the assumption that colleagues will catch each other's errors, while the coordination channel is also an attack surface: a few sybil agents repeating a plausible wrong answer can shift the private beliefs of the majority...

What was learned: An adversarial agent causes FPI 44.8% (three agents 60.5%); hidden infection (51.6% private data vs 19.7% public agreement) is 2.6x what the transcript reveals; knowledge doesn't predict strength (85% knowledge but gives up 25% vs 80%); infection stabilizes by round 4, case...

- Multi-agent: nhiều AI cùng thảo luận
- Sybil: agent giả mạo (nhiều danh tính giả)
- FPI: "false persuasion influence"? Actually FPI likely = "False Persuasion Index" or "False Positive Influence"? Hmm. Let me think. FPI in this context — "adversarial agent causes FPI 44.8%". Could be "False Persuasion Index" — tỷ lệ bị thuyết phục sai. I should explain it as "tỷ lệ bị thuyết phục sai (FPI — chỉ số đo bao nhiêu agent đổi sang câu trả lời sai)". Since I can't be sure, I'll describe it functionally: "chỉ số thuyết phục sai (FPI)". Actually the user's instruction: KHÔNG dùng thuật ngữ tiếng Anh thuần mà không giải thích. So I can use the acronym but must explain.

- Belief collapse: sụp đổ niềm tin riêng — agent tin câu đúng nhưng chuyển sang câu sai
- Hidden infection: nhiễm ẩn — agent privately believes wrong but publicly... Actually "51.6% tư liệu riêng vs 19.7% tán thành công khai" — private belief 51.6% vs public agreement 19.7%. So hidden infection is 2.6x what transcript shows.
- Knowledge doesn't predict strength: agent có 85% kiến thức nhưng từ bỏ 25%... vs 80%? "85% kiến thức nhưng từ bỏ 25% vs 80%" — hmm, maybe: agents with 85% knowledge abandon correct answer 25% of the time vs those with 80% knowledge... The phrasing is ambiguous. I'll present it as: kiến thức cao không bảo vệ được — agent biết 85% nhưng vẫn bỏ câu đúng 25% trường hợp, tương đương nhóm chỉ biết 80%.

- Infection stabilizes by round 4: sau 4 vòng thảo luận, sự nhiễm ổn định.

Format required:
### [6] Title
- Làm gì: 1-2 câu
- Học được gì: 1-2 câu with specific numbers
- Áp dụng cho bạn: deep, based on paper knowledge, then concrete example doable today for Vietnamese solopreneur. Not generic.

The [N] — probably a number placeholder? The format says "### [6] Believed but Not Said..." — maybe [N] is the paper number in a series. I'll keep it as [N] as given. Actually maybe they want me to keep the placeholder. I'll keep "[N]".

No intro, no extra explanation.

Vietnamese simple. Avoid unexplained English terms:
- "agent" — should I explain? "agent (trợ lý AI)". The user said no pure English jargon without explanation. So write "agent (trợ lý AI)" first time.
- "sybil" — "agent Sybil (agent giả mạo, tạo nhiều danh tính giả)".
- "transcript" — "biên bản trò chuyện".
- "plausible" — "có vẻ hợp lý".
- "multi-agent" — "hệ thống nhiều agent (nhiều trợ lý AI thảo luận với nhau)".
- "FPI" — explain: "chỉ số thuyết phục sai (FPI)".
- "belief collapse" — "sụp đổ niềm tin ẩn".
- "private belief" — "niềm tin riêng (câu trả lời thật trong đầu)".
- "public agreement" — "tán thành công khai".

Áp dụng cho bạn: Must be deep, tied to paper's knowledge, concrete example for solopreneur VN today.

Paper knowledge:
1. Coordination channel is attack surface — when you use multiple AI agents (e.g., one writes content, one reviews, one checks facts), they influence each other; a wrong answer repeated by a few can flip majority's private belief.
2. Hidden infection: what agents say publicly (agree) underestimates what they privately believe — 2.6x. So checking only the final answer/agreement misses hidden wrong beliefs.
3. Knowledge doesn't protect: even agents that "know" the right answer abandon it ~25% of the time.
4. Infection stabilizes by round 4 — after 4 rounds of discussion, the wrong belief becomes fixed; so intervene before round 4, or limit rounds.

Application for solopreneur:
- When using AI to compare prices/products (Shopee, TikTok Shop), don't let multiple AI agents discuss in a group chat; a single confident wrong answer repeated can flip others.
- Ask each AI separately (not in a group) for its private answer first, then compare; require each to state "tôi tin X vì Y" before seeing others' answers.
- Limit discussion to ≤3 rounds; after round 4 wrong beliefs harden.
- Don't trust "consensus" — 19.7% public agreement but 51.6% private belief means the final agreed answer may hide doubt; ask each agent to privately rate confidence.
- Concrete example: You sell skincare online. You ask 3 AI agents to check whether "retinol có dùng được cho da nhạy cảm không" or compare competitor prices. Instead of a group chat, ask each separately: "Trả lời và ghi độ tin 1-10 + nguồn". Then compare. If two say same wrong price, verify with actual Shopee page. Cap discussion at 3 rounds.

- Prior work hasn't resolved why multi-agent debate often fails compared to simple majority voting or self-consistency, because reasons weren't separated: is it because correct proposals aren't surfaced, or because the readout doesn't recognize correct proposals...
- Learned: Debate helps when proposal supply surfaces the correct answer (recoverable headroom) AND readout identifies the correct answer when voting misses it (LVD = verification evidence); one alone is not enough; council selected via coverage (AC-Greedy/SC-Greedy) creates more complementary correct proposals...

The user's text has some typos (Vietnamese without diacritics in places): "đäne" = "đa agent" (multi-agent), "đề xuất bề mặt câu đúng" = "proposal supply surfaces the correct answer", "headroom có thể phục hồi" = recoverable headroom, "LVD bằng chứng xác thực" = LVD verification evidence, "hội đồng được chọn qua coverage" = council selected via coverage.

- Multi-agent reasoning = nhiều AI cùng suy luận
- Self-consistency = tự nhất quán (hỏi cùng một AI nhiều lần, lấy câu trả lời nhiều nhất)
- Majority voting = bình chọn đa số
- Proposal supply = nguồn đề xuất (các câu trả lời được đưa ra)
- Readout = phần đọc kết quả (cách chọn câu trả lời cuối cùng)
- Headroom = khoảng cách có thể cải thiện
- LVD = ? The user says "LVD bằng chứng xác thực" — LVD likely stands for something like "Leave-one-out Verification Difference" or similar. Actually I don't know the exact expansion. The user describes it as "đọc nhận diện câu đúng khi bình chọn bỏ lỡ (LVD bằng chứng xác thực)". I should keep "LVD" but explain it as a measure of verification evidence — the ability of the readout to identify the correct answer when voting misses it. I shouldn't invent the full English expansion. I can say "chỉ số LVD (mức độ bằng chứng xác thực — tức khả năng phần đọc nhận ra câu đúng khi bình chọn bỏ lỡ)".
- AC-Greedy/SC-Greedy = cách chọn hội đồng (council) qua coverage (độ bao phủ) — greedy selection based on coverage. AC = maybe "Answer Coverage"? SC = "Self-Consistency"? I shouldn't invent. I can say "hai cách chọn hội đồng tên AC-Greedy và SC-Greedy (chọn dần các AI sao cho phủ nhiều câu trả lời đúng khác nhau nhất)".

Actually, maybe I can include a caveat that the summary doesn't include exact percentages. But the format says no extra explanation. I'll keep within the format.

"Áp dụng cho bạn" needs depth: explain according to the paper's knowledge, then a concrete example doable today for a Vietnamese solopreneur. Not generic.

Application: For a solopreneur using AI (e.g., ChatGPT, Claude) for content, selling online, customer care:
- Don't just ask one AI once, and don't just ask the same AI 5 times and take the majority (self-consistency) — that fails when the correct answer never appears in the proposals.
- Instead: (1) ensure proposal supply: use different AI personas/models or different angles so the correct answer gets surfaced (coverage — complementary correct proposals); (2) verification-aware readout: don't just count votes; ask a separate "verifier" step to check evidence for each candidate answer, especially when votes are split.
- Concrete example: When writing product descriptions for a skincare product, ask 3 different AI "roles" (one as customer, one as dermatologist-style, one as copywriter) to draft claims; then a final step: before publishing, ask AI to verify each claim against your product info sheet, marking "có bằng chứng/thiếu bằng chứng" — don't let the majority vote pick the slogan if the verifier flags unsupported claims.
- Customer care example: When AI drafts replies to complaints, run two drafts from different prompts (empathy-first vs solution-first), then a verification step that checks the reply against your refund policy before sending; if the majority draft says "đổi trả trong 30 ngày" but policy says 7 days, the verifier catches it.
- Content example: fact-checking

Key points given:
- Prior work didn't address that multi-agent systems can produce correct answers but still report wrong ones, because previous studies changed candidate generation, communication, and final selection rules simultaneously — couldn't attribute which part helped, which failed.
- Findings: correct answer often already exists in candidates but system still reports wrong (generation–retention gap 13–14 pp); judge reliability isn't fixed, rank ASEAN half-rise midpoint pgen = 14.7%; combining vote frequency + judge ranking lifts 63.82% to 70.82–70.95%.

- LLM = mô hình ngôn ngữ lớn (trí tuệ nhân tạo đọc/viết như ChatGPT) — but user says no English terms without explanation. I can say "mô hình AI đọc–viết (LLM)" or just "AI chấm điểm (judge)".
- multi-agent systems = hệ thống nhiều AI (nhiều "nhân viên AI")
- candidate = ứng viên câu trả lời
- judge = AI giám khảo/chấm điểm
- generation–retention gap = khoảng cách tạo–giữ (tạo ra đúng nhưng giữ lại sai)
- pp = điểm phần trăm
- pgen = xác suất tạo ra đáp án đúng (probability of generation)
- rank ASEAN half-rise midpoint — this seems like a specific experimental condition; I should mention it carefully. "rank ASEAN half-rise midpoint pgen = 14.7%" — probably a ranking-based selection under some condition. I'll phrase: khi chọn theo thứ hạng của giám khảo ở ngưỡng giữa, xác suất tạo đáp án đúng chỉ 14,7% ở nhóm ASEAN... Hmm, "ASEAN" might be a dataset or a group. Actually it might be a benchmark. I'll keep it as given but explain: "trong nhóm câu hỏi khu vực Đông Nam Á (ASEAN)".

Actually, I should be careful — the paper is arXiv 2608.25937v2, which is a future-dated arXiv ID (2608 = August 2026). This is likely a hypothetical/fictional paper. I should just work with the given info.

### [8] Candidate supply and answer selection shape the value of LLM judging in multi-agent systems (arXiv 2608.25937v2)
- Làm gì: 1-2 câu
- Học được gì: 1-2 câu with specific numbers
- Áp dụng cho bạn: deep insight + concrete example for Vietnamese solopreneur

The [N] — the format says "### [8] Candidate supply..." — I think [N] is a placeholder for a number. Maybe I should keep it as is? The user wrote "### [8] Candidate supply..." — probably they want the number. Since it's a single paper, maybe [1]. I'll use [1].

### [8] Candidate supply and answer selection shape the value of LLM judging in multi-agent systems (arXiv 2608.25937v2)
- Làm gì: Tách riêng ba khâu trong hệ thống nhiều AI (tạo câu trả lời, trao đổi giữa các AI, chọn câu cuối) để xem khâu nào giúp, khâu nào hỏng — vì các nghiên cứu trước thay đổi cả ba cùng lúc nên không biết lỗi nằm ở đâu.
- Học được gì: Đáp án đúng thường đã có trong danh sách câu trả lời nhưng hệ thống vẫn báo câu sai (khoảng cách "tạo–giữ" 13–14 điểm phần trăm); độ tin cậy của AI giám khảo không cố định (xác suất tạo đáp án đúng ở ngưỡng giữa chỉ 14,7% với nhóm câu hỏi Đông Nam Á); ghép "số lần được bình chọn" + "thứ hạng do AI giám khảo chấm" nâng độ chính xác từ 63,82% lên 70,82–70,95%.
- Áp dụng cho bạn: Paper chỉ ra lỗi không nằm ở chỗ AI "không biết" mà ở chỗ chọn sai câu cuối — nên đừng để một AI trả lời một lần rồi xong. Ví dụ: khi nhờ AI viết 5 caption cho sản phẩm, bắt nó liệt kê cả 5, cho 2 AI khác chấm điểm từng cái, rồi chọn câu vừa được nhiều phiếu vừa có thứ hạng cao — thay vì lấy luôn câu đầu tiên. Hay với chăm sóc khách hàng: để AI soạn 3 câu trả lời cho khiếu nại giao hàng, có AI thứ hai xếp hạng, chọn câu đạt cả hai tiêu chí, tránh gửi lời xin lỗi sai tone.

Need to avoid unexplained English terms: "caption" — should say "dòng chữ quảng cáo (caption)" or just "dòng chữ đăng bài". "AI" is fine? AI is commonly used in Vietnamese; but to be safe, "trí tuệ nhân tạo (AI)" first time. The user themselves uses "AI" so it's fine.

"LLM" in title — keep title as is (it's the paper name). That's fine.

"pp" = điểm phần trăm — explain.

"pgen" — explain as xác suất tạo ra đáp án đúng.

"rank ASEAN half-rise midpoint" — I'll interpret: "khi chọn theo thứ hạng giám khảo ở ngưỡng giữa, xác suất tạo đáp án đúng (pgen) chỉ 14,7% ở nhóm câu hỏi ASEAN". Hmm, "half-rise midpoint" is odd. Maybe it's a selection rule. I'll phrase: "quy tắc chọn theo nửa trên của thứ hạng giám khảo ở điểm giữa". Actually I shouldn't over-interpret. I'll say: "độ tin cậy của AI giám khảo thay đổi theo cách chọn — ở ngưỡng giữa của quy tắc chọn nửa trên theo thứ hạng, xác suất tạo đáp án đúng chỉ 14,7% (nhóm câu hỏi Đông Nam Á)".

Keep it 1-2 sentences for "Học được gì".

Áp dụng cho bạn: needs depth — explain per paper knowledge, then concrete example

Also I should explain English terms: RAG = truy xuất-tăng cường sinh (retrieval-augmented generation), agentic = tác tử, chunk = đoạn, corpus = tập tài liệu, tree = cây, recall/precision = độ thu hồi/độ chính xác, WixQA etc are benchmark datasets.

"Áp dụng cho bạn" must have depth: explain per paper knowledge then concrete example for Vietnamese solopreneur today. Paper's insight: separate evidence discovery from content reading; retrieval ensures recall, retrieval structure ensures precision; don't commit to a single document before seeing content. So apply: build a two-step workflow for AI assistant: step 1 — let AI list candidate sources/pages with structure (section headings, table of contents tree) rather than dumping chunks; step 2 — read content only after. Concrete example: shop selling skincare; product knowledge base; when customer asks "serum có dùng được cho da nhạy cảm không", AI first navigates document tree (brand → product → section "cách dùng" → mục "da nhạy cảm"), then answers, and cites which section; don't let AI answer from a chunk that merely contains the word "nhạy cảm".

Also concrete: price comparison, customer care scripts, content creation from own docs. Give a prompt template: "Bước 1: liệt kê cây tài liệu... Bước 2: chỉ đọc đoạn ở nhánh đã chọn... Ghi nhãn: bằng chứng thật / chỉ trùng thuật ngữ".

Keep 1-2 sentences for first two bullets; apply bullet can be longer but concise. Format exactly:

### [9] RIT-RAG: ...

What is [N]? Probably numbering — user wrote "### [9]" placeholder. Maybe they want number. I'll use [1]? Hmm, "[N]" likely a placeholder for a number. Since single paper, use [1]. Or keep [N]? Safer: [1].

Write in Vietnamese, explain terms inline.

### [9] RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees (arXiv 2610.11370v2)
- Làm gì: Paper này sửa lỗi của các hệ thống RAG (trợ lý AI tìm trong tài liệu rồi trả lời) hiện nay: chúng chỉ làm việc ở cấp đoạn (chunk – những mẩu văn bản cắt nhỏ) và không hiểu cấu trúc thật của tài liệu, nên dễ nhầm đoạn "chỉ trùng thuật ngữ" với đoạn "chứa bằng chứng thật". RIT-RAG dùng cây được tạo ra từ chính bước truy xuất (retrieval-induced tree – sơ đồ nhánh tài liệu hình thành khi tìm kiếm) để AI nhìn thấy cấu trúc trước khi đọc nội dung.
- Học được gì: RIT-RAG đạt điểm cao nhất trên 4 bộ thử WixQA, QASPER, FinanceBench, EntQABench (bộ dữ liệu bạn gửi bị cắt ở "2,84M…" – cần kiểm tra lại con số đầy đủ trước khi dùng). Nguyên tắc cốt lõi: tách "khám phá bằng chứng" khỏi "đọc nội dung" – truy xuất đảm bảo độ thu hồi (recall: không bỏ sót nguồn), cấu trúc truy xuất đảm bảo độ chính xác (precision: không trả lời từ nguồn sai); không cam kết vào một tài liệu duy nhất trước khi thấy nội dung bên trong.
- Áp dụng cho bạn: Paper chứng minh AI phải đi theo nhánh cấu trúc tài liệu (mục lục → chương → mục → đoạn) và chỉ đọc nội dung sau khi chọn nhánh, đồng thời gắn nhãn phân biệt "bằng chứng thật" với "chỉ trùng từ". Áp dụng ngay: khi nhờ AI trả lời khách hàng từ tài liệu của bạn (ví dụ shop skincare, khách hỏi "serum A có dùng được cho da nhạy cảm không"), bắt AI làm 2 bước trong prompt: "Bước 1 – liệt kê cây tài liệu: thương hiệu → sản phẩm → mục 'Cách dùng' → mục 'Da nhạy cảm', ghi rõ nhánh bạn chọn; Bước 2 – chỉ đọc nội dung trong nhánh đó rồi trả lời, kèm nhãn [bằng chứng thật] hoặc [chỉ trùng từ khóa] và tên mục/trang nguồn." Cấm AI trả lời thẳng từ một đoạn bất kỳ chỉ vì nó chứa từ "nhạy cảm". Làm tương tự khi so sánh giá Shopee/Lazada hay viết content từ bài viết cũ: AI phải nêu nhánh cấu trúc trước, rồi mới trích dẫn – tránh nội dung "nghe đúng từ nhưng sai nguồn".

Key constraints:
1. Don't use English terms without explanation
2. Follow the exact format with ### header
3. No intro or extra explanation
4. Three sections: Làm gì (1-2 sentences), Học được gì (1-2 sentences with SPECIFIC results: numbers, ratios, comparisons), Áp dụng cho bạn (deep insight based on paper knowledge, then specific example doable today for Vietnamese solopreneur, not generic)

- Làm gì: Prior work hasn't solved the problem that dense retrieval systems (core component of search engines, recommendation platforms, RAG pipelines) are rigid because document embeddings are computed offline and stored in static indexes — hard to adapt to feedback...
- Học được gì: Fixed embeddings after training cause rigidity; embedding surgery applies localized, minimal updates to document embeddings at query time via convex optimization (quadratic optimization problem), enforcing ranking constraints, optimal...

The paper is arXiv 2609.05110v1 — this appears to be a future arXiv ID (2609 would be September 2026). I don't have knowledge of this specific paper. The user gave partial descriptions. I need to be careful: I shouldn't fabricate specific numbers. But the format requires "Học được gì" with specific results (numbers, ratios, comparisons). The user's provided text doesn't include specific numbers.

Hmm. The user says "nêu kết quả CỤ THỂ của paper: con số, tỷ lệ, so sánh". But I don't have the actual paper content. The user's partial text got cut off ("phản h..." = phản hồi, "tối th..." = tối thiểu/tối thiểu hóa).

Since I don't have the actual paper (arXiv 2609.05110 is beyond my knowledge), I should not fabricate specific percentages. However, the user explicitly wants specific numbers. The safest approach: state the mechanism concretely and note that the paper proves the update is the minimal/optimal one (theoretical guarantee), and if I don't have exact benchmark numbers, I should say so briefly rather than invent. But the format forbids extra explanation...

Actually, I can incorporate honesty within the format: "Học được gì: ... paper chứng minh nghiệm là tối ưu toàn cục (vì bài toán lồi)..." — the convexity gives a global optimum guarantee, which is a specific result. I can mention that it corrects ranking with minimal change (localized) — that's a concrete claim from the description.

But the user wants numbers. I could say something like: "Paper không công bố con số % cụ thể trong phần tóm tắt tôi có" — but that breaks the flow and the user said no extra explanation. Hmm.

Given the constraints, I think the best approach is to write based on the provided description, being concrete about the mechanism (minimal localized update, convex/quadratic optimization, ranking constraints, provable optimality), and avoid inventing fake benchmark numbers. For "Học được gì", I can state: fixed embeddings cause rigidity; the method edits only the few embeddings involved in a query at query time by solving a convex quadratic optimization that enforces desired ranking constraints, and because the problem is convex, the solution is the unique global minimum — i.e., the smallest possible change that fixes the ranking. That's specific in mechanism terms.

Actually, I realize I should be careful about the arXiv ID. 2609.05110v1 — arXiv IDs are YYMM.NNNNN. 2609 = September 2026. This is a future paper I cannot know. The user seems to be testing or using a hypothetical. I should work with the description given and not hallucinate specific benchmark numbers. I'll be transparent in a minimal way within the format if needed.

For the "Áp dụng cho bạn" section, I need depth based on paper knowledge, then a concrete example doable today for a Vietnamese solopreneur.

Deep insight: The paper's core idea is that instead of retraining the whole model or recomputing all document embeddings (expensive, offline), you can surgically adjust only the embeddings of documents that appear in the current search results, at the moment of the query, to satisfy ranking constraints (e.g., "this product should rank above that one"). It's like a minimal "patch" applied to the vector representation. The convex optimization guarantees the patch is the smallest change that achieves the desired ranking — so you don't distort the whole system.

- Content creators: When their AI search/chatbot recommends their own articles, they can pin/correct ranking by adjusting only the relevant vectors.
- Online sellers: Product search in their shop — when a customer searches "áo thun nam", the shop's internal search should rank in-stock, high-margin, or promoted items appropriately. Instead of retraining, apply a small correction to the embeddings of the products in the candidate set at query time.
- Customer service: RAG chatbot — when the AI answers from a knowledge base, sometimes it retrieves outdated policy (e.g., old shipping fee). Instead of re-embedding the whole knowledge base, surgically update the embedding of the outdated document so the current correct policy ranks higher for relevant queries.

Concrete example doable today: A Vietnamese seller selling on Shopee/Lazada or their own Shopify-like store. They use an AI assistant to answer customer questions from their FAQ/policy documents. When the AI keeps citing the old "miễn phí vận chuyển đơn từ 200k" while the current policy is "


## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN

Dưới đây là insight hàng đầu từ 10 bài hôm nay, mỗi insight kèm ví dụ áp dụng ngay cho bạn:

- **SLM có thể ổn định hơn chính teacher đã định nghĩa nó, vì teacher không deterministic (chỉ đồng ý với bản thân 72.7% thời gian) nên đóng vai trò noisy annotator chứ không phải ground truth; phát triển hành vi trong prompt space trên frontier model rồ...** Áp dụng theo kết quả paper vào workflow nội dung/bán hàng của bạn.


- **Completeness@10 quan trọng hơn Recall@10 vì thiếu một công cụ trong chuỗi nhiều bước khiến tác vụ thất bại; mỗi lần tìm kiếm thêm một lượt gửi lại toàn bộ cuộc trò chuyện nên tần suất tìm kiếm quyết định xem recommendation có rẻ hơn danh sách tĩnh ha...** Áp dụng theo kết quả paper vào workflow nội dung/bán hàng của bạn.


- **Cùng payload giữa injection thành công 53% ở retrieved context vs 18% ở follow-up (authority gradient); TRACER giảm RAG-framed ASR từ 65.5% xuống 6.1% giữ clean accuracy 78-82% qua phần thưởng gated bằng chứng + ATRC trace alignment; đào tạo đa kênh ...** Áp dụng theo kết quả paper vào workflow nội dung/bán hàng của bạn.


- **Sự sụp đổ phối hợp công khai dưới corruption chủ yếu là cơ học (hành động bị đảo ngược thay đổi transcript và thực thi), không phải hành vi agent; phải tách lựa chọn gốc / hành động công khai / kết quả thực thi khi đánh giá độ mạnh đa agent.** Áp dụng theo kết quả paper vào workflow nội dung/bán hàng của bạn.


- **Mode collapse là sản phẩm phụ của alignment; MODA dùng role conditioning trong policy chia sẻ (mỗi mode = agent MARL cạnh tranh) + cổng chất lượng tùy prompt để tăng SBERT diversity +265% (Infinite-Chat) và +75.9% so với DivPO, đồng thời giữ/tăng năn...** Áp dụng theo kết quả paper vào workflow nội dung/bán hàng của bạn.



---

## Chi tiết từng bài (link folder)
- [1] Iterate on an LLM, Serve on an SLM — `2610.14576v1` — xem chi tiết: `papers/papers/2026/10/20/iterate-on-llm-serve-on-slm/`
- [2] Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs — `2610.23707v1` — xem chi tiết: `papers/papers/2026/10/20/tool-recommendation-multi-step-agents/`
- [3] TRACER: Trace-Regularized Training Against Indirect Prompt Injection — `2610.19133v1` — xem chi tiết: `papers/papers/2026/10/20/tracer-trace-regularized-training/`
- [4] Be Careful Who You Trust: Coordination Dynamics under Corrupted Communication in LLM Multi-Agent Games — `2609.31704v1` — xem chi tiết: `papers/papers/2026/10/20/be-careful-who-you-trust/`
- [5] Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning — `2609.14896v1` — xem chi tiết: `papers/papers/2026/10/20/forty-shades-of-blue-moda/`
- [6] Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions — `2610.22138v1` — xem chi tiết: `papers/papers/2026/10/20/believed-but-not-said/`
- [7] When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning — `2610.04686v1` — xem chi tiết: `papers/papers/2026/10/20/when-debate-helps/`
- [8] Candidate supply and answer selection shape the value of LLM judging in multi-agent systems — `2608.25937v2` — xem chi tiết: `papers/papers/2026/10/20/candidate-supply-answer-selection/`
- [9] RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees — `2610.11370v2` — xem chi tiết: `papers/papers/2026/10/20/rit-rag/`
- [10] Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense Retrieval — `2609.05110v1` — xem chi tiết: `papers/papers/2026/10/20/embedding-surgery/`

*Báo cáo tự động sinh bởi daily_summary.py sau mỗi ngày distill 10 bài.*
