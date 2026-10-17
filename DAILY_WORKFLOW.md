# DAILY WORKFLOW — Distill paper arXiv (profile `research-arxiv`)

**Single source of truth** — tổng hợp từ `PIPELINE-DESIGN.md`, `WORKFLOW-HANG-NGAY.md`, `paper-sourcing-strategies.md`, `quality-standards.md`, `bilingual-format-and-git-workflow.md`, `api-extraction-techniques.md`, `model-ling-behavior.md`, và `arxiv-distill-protocol`.

Mục tiêu: ~300 papers, **chất lượng ưu tiên**, không rush. **10 bài tốt nhất/ngày** (không phải 30).

---

## PHASE 1 — BUỔI SÁNG: QUÉT VÀ LỌC PAPER

### 1.1 Khởi động
- Mở tmux, chạy `~/work/arXiv-distill/run-distill.sh` (supervisor tự khởi động lại khi chết).
- Đọc `report.md` để biết đã distill bao nhiêu paper (hiện tại: 66).
- Xem `state/last_scan.json` để biết watermark lần quét cuối.

### 1.2 Quét arXiv mới
Endpoint: `https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.CL+OR+cat:cs.LG+OR+cat:cs.MA+OR+cat:cs.IR+OR+cat:cs.SE+OR+cat:cs.HC&sortBy=submittedDate&sortOrder=descending&max_results=100`

- **Sleep 5-8 giây** giữa mỗi request API.
- Nếu "Rate exceeded" → chờ 10+ giây, retry.
- Nếu API rate-limit liên tục → chuyển sang `web_search` với các topic query (xem §1.4).
- **KHÔNG tin tưởng arXiv HTML version** — JS-rendered TOC, không có body text. Luôn dùng PDF + pdfminer.six.

### 1.3 Lọc category (cấp thô, trước khi đọc abstract)

| Giữ lại (cs.*) | Loại bỏ ngay |
|---|---|
| cs.AI — AI tổng quát | `physics.*` |
| cs.CL — Xử lý ngôn ngữ (LLM) | `math.*` thuần |
| cs.LG — Học máy | `q-bio.*` (sinh y) |
| cs.MA — Multi-agent | `q-fin.*` (tài chính thuần) |
| cs.IR — Tìm kiếm / RAG | `stat.ME` |
| cs.SE — Kỹ thuật phần mềm (agent tooling) | `eess.SP` |
| cs.HC — HCI (UX agent) | ... |

### 1.4 Lọc theo topic (đọc title + abstract, KHÔNG đọc full text)

**INCLUDE (giữ lại):**
- AI/ML applications, business, marketing
- Decision science, consumer behavior
- LLM enterprise, strategic thinking
- AI agents, recommendation systems, prompt engineering
- Safety, cost optimization, multi-agent systems

**EXCLUDE (bỏ ngay):**
- Y học (medical)
- Hoá học (chemistry)
- Vật lý thuần tuý (pure physics)
- Sinh học, pure math theory, agriculture, telecom, accelerator physics
- Ngôn ngữ cụ thể (ví dụ: chỉ về tiếng Bengali)

### 1.5 Chấm điểm LLM (0-100) — chỉ cho paper đã qua lưới topic

| Tiêu chí | Điểm |
|---|---|
| Liên quan cốt lõi (AI/LLM/agent/multi-agent/tool-use?) | 0-35 |
| Ứng dụng thực tiễn (có experiment/benchmark/dataset thật?) | 0-25 |
| Liên quan business/content/decision | 0-20 |
| Insight hành động được (đọc xong làm được gì?) | 0-20 |

**Phân loại sau chấm:**
- **75-100** → distill ngay
- **55-74** → distill sau khi xong nhóm cao
- **35-54** → mơ hồ, gửi Telegram để bạn duyệt
- **0-34** → loại, không gửi

### 1.6 Bước 0 — Đánh giá giá trị từ abstract (trước khi đọc full paper)
Trả lời 3 câu:
1. Paper giải quyết vấn đề gì? (1 câu)
2. Có áp dụng được cho business/content/agent không? (YES/NO + lý do)
3. Nếu YES → distill. Nếu NO → ghi lý do, bỏ.

---

## PHASE 2 — DISTILL TỪNG PAPER (6 BƯỚC, TUẦN TỰ)

Mỗi paper đi đủ 6 bước. **KHÔNG batch, KHÔNG song song.**

### Bước 1 — Kiểm tra paper
- Xác nhận thuộc chủ đề: AI/ML ứng dụng, business, marketing, decision science, LLM enterprise, consumer behavior, strategic thinking.
- Nếu y học / hoá học / vật lý thuần tuý → bỏ qua, tìm paper khác.
- Đọc theo thứ tự: Abstract → Introduction → Related Work (đoạn cuối) → Method → Results/Tables → Limitations → Conclusion.
- Nếu không extract được section nào → ghi `[EXTRACTION FAILED: tên section]` vào README, KHÔNG bỏ qua.

### Bước 2 — Phân loại paper
Gán 1 trong 3 nhãn:
- `[applied]` — có experiment, dataset thật, benchmark cụ thể
- `[theoretical]` — không có evaluation thực tế, chủ yếu framework/model toán
- `[survey]` — review literature, không có contribution mới

### Bước 3 — Tạo README.md (tiếng Việt, tối đa 400 từ)

Cấu trúc bắt buộc:

```
# [arxiv-id] Tên paper

## Problem
- Gap cụ thể trong literature paper này fill là gì?
- KHÔNG paraphrase abstract, phải trả lời: "Prior work chưa giải quyết được X vì Y"

## Contribution
- Paper làm gì khác so với prior work? (1-3 điểm, cụ thể)
- KHÔNG liệt kê related work

## Method (tóm tắt cốt lõi)
- Mô tả pipeline/approach trong 3-5 câu
- Nếu có công thức quan trọng: ghi rõ ý nghĩa, không cần reproduce toán

## Key Findings
- Số liệu thật từ paper: benchmark, dataset size, improvement %
- Format: "Model X đạt Y% trên dataset Z, so với baseline W% (+N%)"
- Nếu không có số liệu cụ thể → ghi [NO BENCHMARK]
- KHÔNG dùng từ "significantly", "substantially", "considerably" — thay bằng con số

## Actionable Insights
- 2-3 insight có thể áp dụng ngay cho business/AI mà không cần reproduce paper
- Mỗi insight: 1 câu mô tả + 1 câu ví dụ áp dụng cụ thể

## Assumptions & Limitations
- Điều kiện nào phải đúng thì method mới work?
- Limitation nào paper thừa nhận?
- Limitation nào paper KHÔNG nói nhưng mày thấy?

## Metadata
- Năm, tác giả, category arXiv, link PDF, citation count (nếu tìm được)
```

**Quy tắc ngôn ngữ (BẮT BUỘC):**
- MỌI từ chuyên ngành tiếng Anh phải có giải thích tiếng Việt trong ngoặc.
- Ví dụ ĐÚNG: `reward signal (tín hiệu phần thưởng)`, `structural trap (bẫy cấu trúc)`.
- Ví dụ SAI: `reward signal` (không giải thích).
- Tên riêng, tên method/framework, tên dataset, tên model giữ nguyên.

### Bước 3.5 — Tạo bản song ngữ
- `README_en.md`: full English version (không cần giải thích từ chuyên ngành).
- Cấu trúc giống hệt README.md, chỉ khác ngôn ngữ.

### Bước 4 — Tạo skill.md (chỉ khi đủ điều kiện)

**Điều kiện TẤT CẢ phải đúng:**
- Paper nhãn `[applied]` hoặc `[theoretical]` có workflow rõ ràng
- Method có ít nhất 3 bước action cụ thể
- Người đọc có thể follow mà KHÔNG cần đọc paper gốc
- Không phải survey

Nếu không đủ → ghi `"skill: N/A — lý do"` vào `metadata.json`, không tạo file.

Cấu trúc skill.md:

```
# Skill: [Tên skill ngắn gọn]
Source: [arxiv-id]
Type: [framework / workflow / evaluation-method / prompt-pattern]

## Khi nào dùng skill này
- Tình huống cụ thể trigger skill này (2-3 bullet)
- Tình huống KHÔNG nên dùng (1-2 bullet)

## Input cần có
- Liệt kê những gì cần chuẩn bị trước khi chạy skill

## Các bước thực hiện
1. [Bước 1 — action cụ thể, không mơ hồ]
2. [Bước 2]
3. [Bước 3]
...

## Output mong đợi
- Kết quả cụ thể sau khi chạy skill là gì?

## Ví dụ áp dụng
- 1 ví dụ thực tế ngắn gọn

## Gotchas
- Điều gì hay sai khi áp dụng skill này?
```

Tạo `skill_en.md` nếu skill được tạo.

### Bước 5 — Test skill (chỉ khi tạo được skill.md)

1. **SELF-CHECK:**
   - Nếu người không đọc paper gốc, họ có follow được không? [YES/NO + lý do]
   - Bước nào mơ hồ nhất? Sửa lại.
   - Input section có đủ không? Nếu thiếu → bổ sung.

2. **DRY RUN:** Tạo 1 test case giả, chạy skill step-by-step, ghi output.

3. **VERDICT:**
   - `[SKILL VALID]` nếu dry run cho output có nghĩa.
   - `[SKILL NEEDS REVISION]` + ghi cụ thể cần sửa gì → sửa rồi dry run lại 1 lần nữa.

### Bước 6 — Báo cáo sau mỗi paper

Format:
```
✓ Paper: [tên] ([arxiv-id])
✓ Nhãn: [applied/theoretical/survey]
✓ Skill tạo được: [tên skill] hoặc N/A
✓ Skill test: [VALID / NEEDS REVISION / N/A]
✓ Insight nổi bật nhất: [1 câu]
→ Tiếp tục paper tiếp theo? [YES/STOP]
```

**Tôi KHÔNG chờ câu trả lời cho dòng cuối** — tự động sang paper tiếp theo.

---

## PHASE 3 — SAU MỖI PAPER (GIT + REPORT)

Sau mỗi paper xong:
1. `git add -A`
2. `git commit -m "paper #N: Title"`
3. `git push`
4. Cập nhật `report.md` (format grouped: papers #1–10, #11–20, v.v.; entry mới nhất ghi đầy đủ ở cuối).
5. Sang paper tiếp theo. **KHÔNG batch nhiều paper rồi mới commit.**

---

## PHASE 4 — CUỐI NGÀY

- Dừng supervisor: `~/work/arXiv-distill/run-distill.sh --stop`
- Kiểm tra: `git status`, `git log --oneline -10`
- Đếm commit hôm nay: `git log --since="1 day ago" --oneline | wc -l`
- **Sinh báo cáo tổng hợp ngày:** `python3 scripts/daily_summary.py`
  - Tạo `scans/<ngày>/README.md` (VI) + `README_en.md` (EN) — báo cáo tổng hợp 10 bài distill hôm nay.
  - Có section **"CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN"** — insights thực tế cho solopreneur VN, áp dụng ngay không cần reproduce paper.
  - Tự động gửi qua Telegram (nếu đã setup TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID).
- Xác nhận file báo cáo đã xuất hiện: `ls scans/<ngày>/README.md`

---\n\n## WATCHDOG — CHẠY LẠI NẾU LỖI (MỚI)

Cron job `watchdog-arxiv-daily-retry` chạy mỗi **30 phút** (`*/30 * * * *`):

- Kiểm tra `scans/<hôm nay>/README.md` đã tồn tại chưa.
- Nếu chưa → chạy lại `scripts/watchdog_daily.sh` → `run_pipeline.sh --no-tele` → `daily_summary.py`.
- Giới hạn tối đa **4 lần chạy lại/ngày** (tránh loop vô íc).
- Nếu pipeline đang chạy (hermes hoặc run_pipeline.sh) → bỏ qua lượt này.
- Log ghi vào `logs/watchdog-retry.log`, đếm retry lưu trong `state/watchdog_retry_count.json`.


---

## PITFALLS (KHÔNG ĐƯỢC QUÊN)

1. **Repo phải tạo TRƯỚC khi bắt đầu:** Git init + remote + push là bước đầu tiên.
2. **Commit+push SAU MỖI paper:** KHÔNG batch nhiều papers rồi mới commit.
3. **Không paraphrase protocol:** Khi trình bày lại, phải chính xác 100% nguyên văn.
4. **Vietnamese format:** MỌI từ chuyên ngành tiếng Anh phải có giải thích tiếng Việt trong ngoặc.
5. **Bilingual files:** Mỗi paper = 5 files (README.md VI, README_en.md EN, skill.md VI, skill_en.md EN, metadata.json).
6. **ArXiv rate limit:** API bị rate limit sau ~3 requests. Cần sleep 5-8s giữa mỗi batch. Nếu "Rate exceeded", chờ 10s rồi thử lại.
7. **PDF extraction:** web_extract có thể không hoạt động. Fallback: PDF+pdfminer.six → abstract metadata extraction → ghi [EXTRACTION FAILED].
8. **Filter papers first:** Luôn lọc danh sách papers theo chủ đề TRƯỚC KHI đọc full text.
9. **Quality over quantity:** Chất lượng là ưu tiên. Mỗi paper phải đủ 6 steps, bilingual, skill test.
10. **Sequential processing:** KHÔNG batch processing hay execute_code để speed up.
11. **PDF extraction failure chain:** `uv pip install pdfminer.six --system` FAIL (PEP 668). Cách đúng: `uv venv /tmp/pdfenv --clear` → `uv pip install --python /tmp/pdfenv/bin/python pdfminer.six`.
12. **KHÔNG dừng hỏi:** User rất frustrated khi agent dừng giữa chừng để hỏi "tiếp tục không?". Agent phải tự động chạy liên tục.
13. **agent.max_turns:** Set `hermes config set agent.max_turns 500` trước session dài. Default 90 sẽ dừng giữa chừng.
14. **Topic queries rotation:** Khi web_search, luân phiên giữa các topic queries để tránh lặp lại cùng papers.

---

## MODEL BEHAVIOR (ling-3.1-flash qua OpenRouter)

- **Điểm mạnh:** tool-calling chuẩn, đọc-hiểu-trích-xuất tốt, giá $0.
- **Điểm yếu:** đôi khi nhả output RỖNG khi viết văn dài (2/3 lần test).
- **Xử lý output rỗng:** KHÔNG ghi file rỗng. Gọi lại. Chia nhỏ prompt (viết từng section rồi ghép). Retry tối đa 2 lần. Nếu vẫn rỗng → ghi `[MODEL OUTPUT FAILED — cần model khác]`, KHÔNG bịa nội dung.
- **Rate limit:** ~12 request liên tiếp → 429, hồi phục ~5 giây. Hermes đã config `api_max_retries: 8` để tự vượt.
- **Config:** `streaming: false`, `max_turns: 500`, `language: vi`.

---

## FILE STRUCTURE PER PAPER

```
papers/<NĂM>/<THÁNG>/<NGÀY>/<ten-paper>/
  README.md       # Tiếng Việt, English terms explained in parentheses
  README_en.md    # Full English
  skill.md        # Tiếng Việt (nếu đủ điều kiện)
  skill_en.md     # Full English (nếu skill được tạo)
  metadata.json   # name, authors, link, id, year, category, classification, skill_status
```

Ngày trong đường dẫn = NGÀY DISTILL (ngày commit), KHÔNG phải ngày paper xuất bản.

---

## COMMON TRANSLATIONS (dùng liên tục)

- reinforcement learning → học tăng cường
- fine-tuning → tinh chỉnh
- inference → suy luận
- benchmark → tiêu chuẩn đánh giá
- prompt → lệnh nhắc
- retrieval → truy xuất
- embedding → biểu diễn nhúng
- token → token (giữ nguyên)
- agent → tác nhân
- deployment → triển khai
- training → huấn luyện
- evaluation → đánh giá
- performance → hiệu suất
- accuracy → độ chính xác
- efficiency → hiệu quả
- pipeline → quy trình
- framework → khung phương pháp
- workflow → quy trình làm việc
- baseline → đường cơ sở
- state-of-the-art → tiên tiến nhất

---

**Tôi sẽ load file này làm skill trước khi distill paper nào.** Nếu cần điều chỉnh, bạn chỉ cần nói, tôi sẽ patch file này và commit ngay.