# [2602.01684] Strategic Foresight (Tầm nhìn chiến lược) của LLMs: Bằng chứng từ Giải đấu Dự đoán Hoàn toàn Tương lai

## Vấn đề
Các nghiên cứu trước chưa trả lời được câu hỏi AI có thể outperform (vượt trội) con người trong strategic foresight (tầm nhìn chiến lược) — khả năng đưa ra đánh giá chính xác về kết quả kinh doanh uncertain (không chắc chắn), high-stakes (cao trước khi chúng xảy ra. Vấn đề chính: hầu hết real-world outcomes đã biết nên khó区分 genuine prediction (dự đoán thật) từ pattern retrieval (truy xuất mẫu). Prior work dùng retrospective data (dữ liệu hồi tố) hoặc synthetic data (dữ liệu tổng hợp) — không test trên outcomes genuinely unknowable (thực sự không thể biết).

## Đóng góp
1. **Fully prospective prediction tournament (giải đấu dự đoán hoàn toàn tương lai)**: Test trên 30 Kickstarter projects launched SAU training cutoffs của tất cả models — outcomes unknown khi predictions được made
2. **Benchmark humans vs LLMs**: 346 experienced managers (Prolific) + 3 MBA-trained investors vs frontier LLMs (GPT-5, Claude 4.5, Gemini 2.5, Grok 4, etc.) trên identical task
3. **Prospective benchmarking methodology (phương pháp đánh giá tương lai)**: Design template cho strategy research — giải quyết training-data leakage problem (vấn đề rò rỉ dữ liệu huấn luyện)

## Phương pháp (tóm tắt cốt lõi)
30 U.S.-based technology ventures trên Kickstarter, fundraising đang diễn ra. LLMs hoàn thành 870 pairwise comparisons (so sánh từng cặp) — double round-robin tournament (mỗi project so với mọi project khác, cả hai thứ tự). Humans cũng làm identical task. So sánh predicted ranking vs realized outcome ranking (thứ hạng kết quả thực tế) bằng Spearman's rank correlation (tương quan hạng Spearman).

## Kết quả chính
- Gemini 2.5 Pro: ρ=0.74 (correlation cao nhất) — correctly ordered ~79% venture pairs
- GPT-5 family: ρ=0.67-0.71
- Best human (Expert 3 — MBA investor): ρ=0.45 — correctly ordered ~60% pairs
- Prolific crowd: ρ=0.19 (gần random)
- Expert 1: ρ=0.04 (random)
- LLMs captured >83% top-5 value; best human captured 50%
- Human-AI aggregation KHÔNG cải thiện so với best standalone model — "augmentation trap" (bẫy tăng cường)
- Difference Gemini 2.5 Pro vs Expert 3: 0.29 points (p=0.063)
- Difference Gemini 2.5 Pro vs Prolific crowd: 0.55 points (p=0.001)

## Insight có thể áp dụng ngay
1. **LLM làm first-pass filter cho deal flow**: Khi screening venture investments, acquisitions, hoặc R&D projects, dùng LLM để rank opportunities trước khi human review. Ví dụ: VC firm nhận 1000 pitches/tháng → LLM filter top 50 → human chỉ review 50 đó. LLM correctly ordered 79% pairs vs human 60%.

2. **Augmentation trap — cẩn thận khi thêm human vào AI pipeline**: Khi AI đã outperform human trên well-defined evaluation task, thêm human judgment có thể làm GIẢM performance bằng cách reintroduce noise. Ví dụ: nếu AI screening accuracy = 79%, human = 60%, thì AI+human có thể < 79%. Giá trị của human nằm ở shaping AI inputs (câu hỏi, dữ liệu), không phải filtering AI outputs.

3. **Consistency matters — LLM ổn định, human biến động**: Expert correlations ranged 0.04-0.45 under identical conditions — không thể identify reliable expert. LLMs produce stable rankings. Ví dụ: khi hire strategist, không nên rely vào single human expert — dùng LLM làm baseline, human làm challenger.

## Giả định & Hạn chế
**Điều kiện để kết quả apply:**
- Task phải là early-stage screening với standardized information (thông tin tiêu chuẩn)
- Outcomes determined by external market response, không phải evaluator's implementation
- Structurally similar: venture scouts, corporate development, innovation committees

**Hạn chế paper thừa nhận:**
- Kickstarter fundraising là incomplete proxy cho venture performance
- LLMs evaluated trên standardized summaries, không phải full noisy information
- Sample 30 projects — đủ detect large differences nhưng limited power phân biệt models tương tự
- Cần replication trên diverse contexts

**Hạn chế paper KHÔNG nói:**
- Không test trên non-U.S. markets — cultural bias?
- Không address LLM training data contamination (ô nhiễm) — dù post-cutoff, models có thể có prior knowledge về Kickstarter patterns
- Không discuss cost — running 870 comparisons với frontier models tốn bao nhiêu?
- Không test sequential decision making (quyết định tuần tự) — chỉ one-shot ranking
- Không address ethical implications của AI replacing human strategic judgment

## Metadata
- Năm: 2026
- Tác giả: Felipe A. Csaszar (University of Michigan), Aticus Peterson (NYU Stern), Daniel Wilde (Indiana University)
- Category: cs.AI, econ.GN
- Link PDF: https://arxiv.org/pdf/2602.01684
- Citation count: [EXTRACTION FAILED]
