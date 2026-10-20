# Báo cáo distill arXiv — ngày 2026-10-21

Tổng hợp 4 bài paper đã distill hôm nay (10 bài tốt nhất được chọn từ scan arXiv).
Mỗi bài đã qua 6 bước distill, commit+push GitHub.

## Tổng quan
- Tổng bài distill: **4**
- Tất cả đều có ứng dụng thực tế.

## Danh sách 10 bài hôm nay

Key facts from the prompt:
- Paper: "Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations" (arXiv 2610.25461v1)
- What it does: Prior work hasn't tested whether a sales agent trained on real commercial conversations increases sales on live traffic — current benchmarks use fake customers (simulators) which can reorder leaderboards (correlation only r=0.24 between the two...). So the paper builds a benchmark and randomized field evidence.
- Learned: Training on 4.6 million real commercial conversations increases revenue per visitor +10.0% vs no agent, and engaged conversion +21.6% vs frontier with same scaffolding, at cost only 1.8% compared to sales staff.

Need to explain terms: "frontier" = mô hình AI hàng đầu (như GPT, Claude mới nhất); "scaffolding" = khung/kịch bản bao quanh AI; "engaged conversion" = tỷ lệ khách thực sự tương tác rồi mua; "revenue per visitor" = doanh thu mỗi khách truy cập; "simulator" = khách giả lập; "r=0.24" = hệ số tương quan thấp, nghĩa là thứ hạng benchmark giả lập gần như không đoán được kết quả thực.

"Áp dụng cho bạn" needs depth: explain per paper's knowledge, then concrete example doable today for Vietnamese solopreneur.

Key insight: benchmark with simulated customers doesn't predict real results (r=0.24 — very weak correlation). So don't trust AI demos/tests with fake customers; test on real traffic with A/B (randomized field experiment). Training on real conversations (4.6M) beats frontier models with same scaffolding — so fine-tuning/grounding AI on your own real chat logs (Zalo, Messenger, Shopee chat) beats using raw top models. Cost 1.8% of sales staff — cheap.

Cost: 1.8% of sales staff cost — so for a solopreneur, AI agent costs almost nothing vs hiring.

### [1] Title
- Làm gì: ...
- Học được gì: ...
- Áp dụng cho bạn: ...

Must not add intro or extra explanation. Write in Vietnamese, explain English terms inline.

### [1] Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations (arXiv 2610.25461v1)

- Làm gì: Kiểm tra xem một nhân viên bán hàng AI được đào tạo trên cuộc hội thoại thương mại thật có tăng doanh thu trên lượng khách thật hay không — vì các bảng xếp hạng hiện tại dùng khách giả lập (simulator, máy đóng vai khách) có thể đảo thứ hạng: mức tương quan giữa kết quả giả lập và thực chỉ r=0.24 (r gần 0 = gần như không đoán trước được).

- Học được gì: Đào tạo AI trên 4,6 triệu cuộc hội thoại thương mại thật giúp doanh thu mỗi khách truy cập (revenue per visitor) tăng +10,0% so với không có AI, tỷ lệ mua hàng của khách đã tương tác (engaged conversion) tăng +21,6% so với mô hình AI hàng đầu (frontier) cùng khung làm việc (scaffolding), với chi phí chỉ 1,8% so với nhân viên bán hàng.

- Áp dụng cho bạn: Bài học cốt lõi: đừng tin kết quả test AI với kịch bản giả — hãy thử trên khách thật, và hãy nuôi AI bằng chính đoạn chat thật của bạn thay vì chỉ dùng mô hình AI mới nhất. Làm ngay: xuất 2–3 tháng chat Zalo/Messenger/Shopee, đánh dấu đoạn nào chốt được đơn, đưa làm ví dụ cho AI (GPT/Claude) học cách trả lời; rồi chạy thử nghiệm A/B (chia đôi khách: một nửa AI trả lời, một nửa trả lời tay) trong 2 tuần, đo doanh thu mỗi khách và tỷ lệ mua của khách đã hỏi — nếu doanh thu/khách tăng ~10% là đạt chuẩn paper. Vì chi phí chỉ ~1,8% nhân viên, bạn nên để AI lo phần trả lời câu hỏi lặp (giá, ship, size) ngay khi khách nhắn, tập trung mình vào chốt đơn.

Check: "frontier" explained, "scaffolding" explained, "engaged conversion" explained, "revenue per visitor" explained, "simulator" explained, r=0.24 explained. Good.

Number format: paper uses +10.0% and +21.6%, 1.8%. Vietnamese uses comma decimals but keeping as in paper is fine; I'll use +10,0% or +10.0%? Keep consistent with paper: +10.0%. Either fine. I'll use +10,0% for Vietnamese style? The prompt wrote +10.0%. I'll keep +10.0% to match.

The [N] — number of the paper, presumably [1]. Use [1].

No intro, no extra. Format exactly.
### [1] Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations (arXiv 2610.25461v1)
- Làm gì: Kiểm tra xem một nhân viên bán hàng AI được đào tạo trên cuộc hội thoại thương mại thật có tăng doanh thu trên lượng khách thật hay không — vì các bảng xếp hạng hiện tại dùng khách giả lập (simulator, máy đóng vai khách hàng) có thể đảo lộn thứ hạng: mức tương quan giữa kết quả giả lập và kết quả thực chỉ r=0.24 (r gần 0 n

Key facts from the paper summary:
- Prior work controlled chess models via rating or player identity, not open-ended natural language style requests like "castle queenside and storm the enemy king with your pawns"
- DPO (Direct Preference Optimization) improves style adherence: queens traded early 53%→67%, queenside castling 97.3%→99.7%, without weakening unprompted strength (1792 vs 1797 Elo)
- Uses pairs of same output under different descriptions, no reward model needed

Format required:
### [2] CHSM8: A Chess Transformer that Follows Natural-Language Style Prompts (arXiv 2610.25356v1)
- Làm gì: (1-2 câu tiếng Việt đơn giản)
- Học được gì: (1-2 câu, with specific numbers)
- Áp dụng cho bạn: (deep insight based on paper knowledge, then concrete example for Vietnamese solopreneur, not generic)

Constraints:
- No English terms without explanation
- No extra intro or explanation
- Must follow format exactly

- DPO = Direct Preference Optimization — need to explain in Vietnamese: "tối ưu hóa theo sở thích trực tiếp" — a method to teach AI to prefer certain outputs without a separate reward-scoring model
- Elo = điểm xếp hạng cờ vua (need explanation)
- Style adherence = mức độ tuân thủ phong cách
- Queenside castling = nhập thành bên hậu (or "nhập thành cánh hậu")
- Queens traded early = hậu được đổi sớm
- Reward model = mô hình thưởng (mô hình chấm điểm riêng)

The [N] in format — probably a placeholder for a number or category. The user wrote "### [2] CHSM8..." — I should keep it as is, maybe [N] is a placeholder. I'll keep [N] literally since the format says so. Actually it might mean a number. The instruction says "theo format BẮT BUỘC sau" — so I should reproduce the format including [N]. I'll keep [N].

Now the "Áp dụng cho bạn" section needs depth: explain based on the paper's knowledge, then a concrete example.

Paper insight: You can steer an AI's behavior/style through plain-language instructions, and you can train/fine-tune with preference pairs (same output described differently) without needing a reward model. For a solopreneur, the transferable lesson: instead of relying on the AI's default "personality," write explicit style instructions, and when building your own AI assistant (or prompt library), create preference pairs — same situation, two phrasings, one marked preferred — to teach the AI your house style without needing a scoring system.

Concrete example for Vietnamese solopreneur:
- Content creator: Instead of "viết bài về skincare," write "viết như đang tư vấn cho bạn thân, câu dưới 15 từ, không dùng từ 'cách mạng'".
- Online seller: customer care scripts — instruct AI: "trả lời khách phàn nàn: xin lỗi trước, đề xuất đổi hàng, không dùng từ 'lỗi của bạn'".
- The DPO lesson: collect pairs — same customer question, two answers, mark which one fits your brand — feed to AI as examples (few-shot) so it learns your style without a scoring tool.

The example in the user's prompt: "Paper khẳng định việc gắn nhãn trạng thái dữ liệu... Áp dụng: Khi nhờ AI so sánh giá Shopee, bắt nó ghi 'có/thiếu/cũ' cạnh mỗi giá..."

So my apply section should mirror: "Paper khẳng định [insight]. Áp dụng: [concrete action]."

Better: The paper shows style instructions like "đổi hậu sớm" measurably change behavior (53%→67%). Apply: when asking AI for customer service replies, give measurable style rules: "mỗi câu trả lời dưới 3 câu, mở đầu bằng lời xin lỗi, kết bằng câu hỏi" — then check the output counts, like the paper measured percentages.

### [2] CHSM8: A Chess Transformer that Follows Natural-Language Style Prompts (arXiv 2610.25356v1)
- Làm gì: Trước đây chỉ có thể điều khiển AI chơi cờ bằng điểm xếp hạng hoặc tên kỳ thủ, không thể yêu cầu mở như "nhập thành cánh hậu rồi dùng tốt tràn lên tấn công vua đối phương". Paper này tạo mô hình cờ vua hiểu và làm theo yêu cầu phong cách viết bằng ngôn ngữ tự nhiên.
- Học được gì: Dùng phương pháp tối ưu theo sở thích trực tiếp (DPO — so sánh từng cặp đáp án, không cần mô hình chấm điểm riêng) giúp AI tuân thủ phong cách tốt hơn: tỷ lệ đổi hậu sớm tăng 53%→67%, nhập thành cánh hậu 97,3%→99,7%, mà sức mạnh chơi không cần nhắc phong cách gần như không giảm (1792 so 1797 điểm Elo — thang điểm xếp hạng cờ vua).
- Áp dụng cho bạn: Paper chứng minh hai điều: (1) chỉ cần

Key constraints:
1. Don't use English terms without explaining them
2. Follow the exact format with ### header and three bullet points
3. No opening or extra explanation
4. "Áp dụng cho bạn" must have depth — explain based on the paper's knowledge, then give a concrete example doable today for a Vietnamese solopreneur. Not generic.
5. The example given shows the style: paper claims X. Applied: when doing Y, tell AI to do Z specifically.

- Prior work on personalized video ads used "retrieval-based paradigm" — create a pool of creatives in advance, then retrieve from it. This limits personalization granularity and causes performance gaps between user groups. User feedback can only... (the text is cut off, but presumably only influence after production cycle, i.e., slow feedback loop).
- MAPS: 4-agent system (Profile, Scripter, Director, Reflector) creates personalized video ads on demand. Results: CTR +2.87%, CVR +2.74%, ARPU +9.85% in real A/B test at Kuaishou.

Key concepts to explain in Vietnamese without raw English terms:
- Multi-agent: hệ thống nhiều "tác tử" AI, mỗi tác tử một vai trò
- Personalized: cá nhân hóa
- Script-driven: viết kịch bản trước rồi mới làm video
- Reinforcement learning: học tăng cường — AI học từ phản hồi (thưởng/phạt) để cải thiện
- Retrieval-based: tạo sẵn kho video rồi tìm chọn, thay vì tạo mới theo yêu cầu
- CTR (click-through rate): tỷ lệ nhấp
- CVR (conversion rate): tỷ lệ chuyển đổi (mua hàng)
- ARPU (average revenue per user): doanh thu trung bình mỗi người dùng
- A/B test: thử nghiệm so sánh hai phiên bản

### [3] MAPS: ...
- Làm gì: 1-2 câu
- Học được gì: 1-2 câu with specific numbers
- Áp dụng cho bạn: deep, with concrete example

For "Áp dụng cho bạn", I need to extract the paper's insight: instead of pre-making a pool of creatives and picking from them (retrieval), generate the ad on-demand per customer segment with a 4-role pipeline:
1. Profile agent: builds user profile from data
2. Scripter agent: writes the ad script based on profile
3. Director agent: turns script into video (visuals, voice, scenes)
4. Reflector agent: reviews output, learns from feedback (reinforcement learning) to improve next round

The insight for solopreneur: don't make one video for everyone; build a small pipeline where AI plays 4 roles: (1) read customer data/segment, (2) write script tailored to that segment, (3) produce the video, (4) review against results (CTR, comments, sales) and feed back to improve the next script.

Concrete example for Vietnamese solopreneur: e.g., selling skincare on TikTok/Shopee. Instead of one video, create 3 customer profiles (học sinh/sinh viên, dân văn phòng, mẹ bỉm sữa), then ask AI to write 3 scripts with different hooks, then generate video with tools like CapCut AI / Kling / Sora... but must be doable today. Tools available: ChatGPT/Claude for script, CapCut for editing, or AI video tools. The reflection loop: after 3-7 days, check which script got more clicks/sales, then tell AI "script A bán được, script B không — viết lại theo hướng A" — that's the reinforcement learning feedback loop.

The example in the prompt style: "Paper khẳng định... Áp dụng: Khi nhờ AI..., bắt nó ghi..."

- Làm gì: 1-2 câu
- Học được gì: 1-2 câu with numbers
- Áp dụng cho bạn: deep with concrete example

Also must not use unexplained English terms. So: "học tăng cường (reinforcement learning)" — the instruction says don't use English terms without explaining. I can mention the term with explanation, or avoid. Safer: explain in Vietnamese, maybe with the English in parentheses once. Actually "KHÔNG dùng thuật ngữ tiếng Anh thuần mà không giải thích" means don't use bare English terms without explanation. So I can use them if explained. I'll minimize.

CTR +2.87% — explain: tỷ lệ người xem nhấp vào quảng cáo. CVR: tỷ lệ người xem mua hàng. ARPU: doanh thu trung bình mỗi người dùng. A/B test: thử nghiệm so sánh hai phiên bản trên hai nhóm khách.

- Prior LLM safety work focused on control-plane (system prompt, role, tool routing, jailbreak), but data-plane — the information the agent is built to act on — is not defended. A fabricated headline can push multiple agents reading the same source...
- Information injection achieves ASR 62% (4.5× prompt injection 14%), two samples of 30 words achieve 100% on 15 stock tickers, only star pipeline (hierarchical) reduces ASR to 9-10%.

Wait, "star pipeline phân cấp" — hierarchical star pipeline. Let me think. The paper mentions "star topology" or "hierarchical" defense. The user wrote "chỉ star pipeline phân cấp giảm ASR xuống 9–10%". I should explain this in Vietnamese without pure English terms.

ASR = Attack Success Rate (tỷ lệ tấn công thành công). I need to explain it.

Format required:
### [4] Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents (arXiv 2610.26438v1)
- Làm gì: (1-2 câu tiếng Việt đơn giản)
- Học được gì: (1-2 câu, nêu kết quả CỤ THỂ)
- Áp dụng cho bạn: (CÓ CHIẾU SÂU — explain per paper knowledge, then specific example doable today for VN solopreneur. NOT generic.)

No intro, no extra explanation.

The [N] — probably a number placeholder. The user wrote "### [4]" in the format. I should keep it as [N] or maybe put a number. The format says "### [4] Fake News..." — I'll keep [N] as is since it's the required format. Actually maybe [N] means the paper number in a series. I'll keep it literally as [N].

Now, "KHÔNG dùng thuật ngữ tiếng Anh thuần mà không giải thích" — don't use English terms without explaining. So ASR must be explained: "tỷ lệ tấn công thành công (ASR — Attack Success Rate, phần trăm lần AI làm theo thông tin giả)". Prompt injection — "tiêm lệnh qua lời nhắc" or explain. Jailbreak — "vượt rào an toàn". Control-plane/data-plane — "mặt điều khiển / mặt dữ liệu" with explanation.

### [4] Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents (arXiv 2610.26438v1)

- Làm gì: Trước đây người ta chỉ bảo vệ "lớp chỉ huy" của AI (lời nhắc hệ thống, vai trò, cách chọn công cụ, chống vượt rào an toàn), còn "lớp dữ liệu" — chính những thông tin AI được tạo ra để hành động — thì bỏ ngỏ. Paper chỉ ra rằng một tiêu đề tin giả bịa ra có thể khiến nhiều AI cùng đọc cùng một nguồn cùng hành động sai.

- Học được gì: Tiêm thông tin giả vào dữ liệu đạt tỷ lệ tấn công thành công 62% (ASR — phần trăm lần AI làm theo thông tin sai), gấp 4,5 lần tiêm lệnh qua lời nhắc (14%); chỉ hai mẫu tin 30 từ đã đạt 100% trên 15 mã cổ phiếu; chỉ có cách xếp pipeline hình sao phân cấp (cho nhiều AI độc lập kiểm tra chéo rồi mới quyết định) hạ ASR xuống 9–10%.

- Áp dụng cho bạn: Paper chứng minh AI không bị lỏng ở chỗ "nói gì với AI" mà ở chỗ "AI đọc gì để làm" — tức tin tức, đánh giá, bình luận mà nó nuốt vào rồi hành động. Áp dụng: Khi nhờ AI viết bài quảng cáo hoặc trả lời khách hàng dựa trên review/comment trên Shopee–TikTok, đừng để nó tin một nguồn duy nhất: bắt nó trích dẫn kèm "nguồn + ngày + số lượng đánh giá" mỗi thông tin, và dùng hai AI (hoặc hai lần hỏi với hai vai trò: một lần tìm bằng chứng ủng hộ, một lần tìm bằng chứng phản bác) trước khi đăng; cụ thể, trước khi đăng bài "sản phẩm X bán chạy nhất", yêu cầu AI ghi rõ "đúng/sai/chưa kiểm chứng" cạnh mỗi claim và chỉ đăng những dòng đã có ≥2 nguồn độc lập xác nhận — cách này chính là phòng vệ lớp dữ liệu, không phải chỉ dặn "hãy trung thực".

Hmm, need to be careful: the paper's defense is "star pipeline phân cấp" — hierarchical star pipeline. I should explain it: nhiều agent độc lập đọc/kiểm tra, một agent trung tâm tổng hợp/phán quyết — like a star topology where leaf agents gather and a central one decides, with hierarchy. Let me explain accurately: "pipeline hình sao phân cấp" — các agent nhỏ độc lập thu thập/kiểm tra, một agent đầu não ở giữa tổng hợp và ra quyết định, tạo thành cấu trúc hình sao nhiều tầng. That reduces ASR to 9-10%.

For the solopreneur application, I need something concrete and doable today: content, selling online, customer care.

- Content: AI viết bài từ tin tức/trend — check nguồn.
- Bán hàng: AI so sánh giá/đánh giá đối thủ — một đánh giá giả (do đối thủ hoặc bot cài) có thể khiến AI của bạn hạ giá hoặc viết sai thông tin sản phẩm.
- Chăm sóc khách hàng: chatbot đọc review/ticket — một tin nhắn chứa thông tin sai lệch (ví dụ "mã giảm giá là X" hoặc "shop đã đồng ý hoàn 100%") có thể khiến bot hành động theo.

The paper's key insight: data-plane defense — verify the information itself, not just the instructions. So the application: before AI acts on any external info (review, news, customer message claiming facts), require it to label each piece of info with source/


## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN

Dưới đây là insight hàng đầu từ 10 bài hôm nay, mỗi insight kèm ví dụ áp dụng ngay cho bạn:

- **Đào tạo trên 4,6 triệu cuộc hội thoại thương mại thật tăng revenue per visitor +10.0% so với không agent và engaged conversion +21.6% so với frontier cùng scaffolding, tại chi phí chỉ 1.8% so với nhân viên bán hàng.** Áp dụng theo kết quả paper vào workflow nội dung/bán hàng của bạn.


- **DPO cải thiện style adherence (queens traded early 53%→67%, queenside castling 97.3%→99.7%) mà không làm suy yếu sức mạnh không prompt (1792 vs 1797 Elo), dùng cặp cùng output dưới mô tả khác nhau không cần reward model.** Áp dụng theo kết quả paper vào workflow nội dung/bán hàng của bạn.


- **4-agent hệ thống (Profile, Scripter, Director, Reflector) tạo quảng cáo video cá nhân hóa theo yêu cầu, CTR +2.87%, CVR +2.74%, ARPU +9.85% trong A/B test thực tế tại Kuaishou.** Áp dụng theo kết quả paper vào workflow nội dung/bán hàng của bạn.


- **Thông tin injection đạt ASR 62% (gấp 4.5× prompt injection 14%), hai mẫu 30 từ 100% trên 15 mã cổ phiếu, chỉ star pipeline phân cấp giảm ASR xuống 9–10%.** Áp dụng theo kết quả paper vào workflow nội dung/bán hàng của bạn.



---

## Chi tiết từng bài (link folder)
- [1] Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations — `2610.25461v1` — xem chi tiết: `papers/papers/2026/10/21/selling-in-the-wild-sales-agent-commercial-conversations/`
- [2] CHSM8: A Chess Transformer that Follows Natural-Language Style Prompts — `2610.25356v1` — xem chi tiết: `papers/papers/2026/10/21/chsm8-chess-transformer-natural-language-style-prompts/`
- [3] MAPS: A Multi-Agent Personalized Script-Driven Video Advertising System Enhanced by Reinforcement Learning — `2610.25748v1` — xem chi tiết: `papers/papers/2026/10/21/maps-multi-agent-personalized-video-ads-rl/`
- [4] Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents — `2610.26438v1` — xem chi tiết: `papers/papers/2026/10/21/fake-news-real-crashes-information-injection/`

*Báo cáo tự động sinh bởi daily_summary.py sau mỗi ngày distill 10 bài.*
