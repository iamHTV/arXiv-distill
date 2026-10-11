# PIPELINE CHƯNG CẤT ARXIV — TÀI LIỆU ĐẦY ĐỦ

> Profile: `research-arxiv` · Repo: `~/work/arXiv-distill` · Model: ling-3.1-flash (free)
> Máy chạy 24/7 · Token free · Cập nhật: 2026-10-11

Tài liệu này mô tả TOÀN BỘ hệ thống: quy trình, tiêu chí lọc, tiêu chí chấm điểm,
quy trình distill để ra giá trị (knowledge/insight/idea/wisdom), và cách vận hành.

---

# PHẦN 1 — TỔNG QUAN HỆ THỐNG

## 1.1 Mục tiêu
Mỗi ngày tự động: quét paper arXiv mới → lọc → chấm điểm → gửi Telegram →
distill từ điểm cao xuống, chưng cất thành tri thức có giá trị dùng được.

## 1.2 Luồng chạy (1 vòng/ngày, 5h sáng)

```
[1] QUÉT      scripts/scan_arxiv.py
    └─ 7 category → ~1250 bài → lưu scans/<ngày>.json
[2] LỌC       (trong scan_arxiv.py)
    ├─ Tầng A: watermark (bài mới từ lần quét trước)
    ├─ Tầng B: category (bỏ physics/math/bio...)
    ├─ Tầng C: heuristic rất nhẹ (chỉ bỏ bài lạc đề hoàn toàn)
    └─ Tầng D: LLM chấm điểm 0-100
[3] GỬI TELE  scripts/send_telegram.py
    ├─ Nhóm 75+    → "DISTILL NGAY"
    └─ Nhóm 35-54  → "CẦN BẠN DUYỆT"
[4] DISTILL   hermes --profile research-arxiv chat
    └─ Từ điểm cao xuống, mỗi paper: 7 bước value-extraction
[5] LƯU       commit + push sau MỖI paper
```

## 1.3 Cấu trúc file

```
~/work/arXiv-distill/
├── PIPELINE-DOCS.md            # TÀI LIỆU NÀY — toàn bộ hệ thống
├── WORKFLOW-HANG-NGAY.md       # Hướng dẫn vận hành hằng ngày
├── report.md                   # Báo cáo tiến độ (cập nhật sau mỗi paper)
├── run-distill.sh              # Supervisor: chạy liên tục, tự khởi động lại
├── state/
│   └── last_scan.json          # Watermark lần quét cuối
├── scans/
│   └── <ngày>.json             # Kết quả quét + điểm từng ngày
├── scripts/
│   ├── scan_arxiv.py           # Quét + lọc + chấm điểm
│   ├── send_telegram.py        # Gửi Telegram
│   └── run_pipeline.sh         # (sắp có) Orchestrator 1 vòng đầy đủ
└── papers/
    └── <năm>/<tháng>/<ngày>/  # ngày = NGÀY DISTILL (commit), vd 2026/10/11/
        └── <tên-paper>/        # 5 files/paper (xem Phần 5)
```

---

# PHẦN 2 — QUÉT arXiv (BƯỚC 1)

## 2.1 Nguồn dữ liệu
- **API chính**: `https://export.arxiv.org/api/query` (PHẢI dùng https — http trả 301)
- **Query**: `search_query=cat:<category>&sortBy=submittedDate&sortOrder=descending`
- **Rate limit**: ~3 request rồi bị chặn → sleep 3s giữa các category
- **RSS** (`https://rss.arxiv.org/rss/cs.AI`): chỉ có bài ngày công bố, RỖNG cuối tuần

## 2.2 Sự thật quan trọng về arXiv
```
- arXiv NGHỈ CUỐI TUẦN (skipDays: Saturday, Sunday)
- Công bố ~20h ET các ngày trong tuần (~7-8h sáng VN hôm sau)
- Thứ 2 có bài dồn từ thứ 5,6 tuần trước
- cs.AI một mình: ~100-300 bài/ngày
```

## 2.3 WATERMARK (chống bỏ sót)
Lưu `state/last_scan.json` = mốc thời gian quét cuối. Mỗi lần chạy, query từ mốc
đó đến nay. **Quy tắc vàng:** chỉ cập nhật watermark khi quét được bài. Nếu quét
0 bài (arXiv nghỉ/lỗi mạng) → GIỮ watermark cũ, lần sau quét lại từ mốc đó.

---

# PHẦN 3 — TIÊU CHÍ LỌC (BƯỚC 2)

Lọc qua 4 tầng, từ thô đến tinh. **Nguyên tắc: thà giữ thừa còn hơn bỏ sót.**

## 3.1 Tầng A — Watermark
Giữ bài có `published >= last_scan`. Loại bài đã xử lý.

## 3.2 Tầng B — Category

**GIỮ (7 category cốt lõi):**
| Category | Nội dung |
|---|---|
| cs.AI | Trí tuệ nhân tạo tổng quát |
| cs.CL | Xử lý ngôn ngữ tự nhiên (LLM) |
| cs.LG | Học máy |
| cs.MA | Hệ đa tác tử (multi-agent) |
| cs.IR | Truy xuất thông tin (RAG, search) |
| cs.SE | Kỹ thuật phần mềm (agent tooling) |
| cs.HC | Tương tác người-máy (UX agent) |

**LOẠI (blocklist):**
`physics.*`, `math.*`, `q-bio.*` (sinh y), `q-fin.*` (tài chính thuần),
`stat.*`, `eess.*`, `cond-mat*`, `astro-ph*`, `gr-qc*`, `hep-*`, `nucl-*`

Logic: giữ bài nếu có ÍT NHẤT 1 category trong giữ VÀ KHÔNG có category trong block.

## 3.3 Tầng C — Heuristic (RẤT NHẸ — quan trọng!)

**Nguyên tắc: heuristic chỉ để loại bài LẠC ĐỀ HOÀN TOÀN, không lọc mạnh.**
Vì token free + máy 24/7 → không cần tiết kiệm → thà chấm thừa.

```
Điểm heuristic = core*4 + applied*3 + business*4 + số_liệu*2
Ngưỡng qua: HEURISTIC_MIN = 4  (rất thấp)
```

Từ khóa (chỉ dùng để ĐẾM, không loại trừ):
- **core**: llm, language model, agent, transformer, rag, retrieval, prompt,
  fine-tune, reasoning, inference, multi-agent, tool use, embedding, attention,
  neural, deep learning, foundation model, diffusion, reinforcement
- **applied**: experiment, benchmark, dataset, evaluation, we evaluate, results
  show, outperform, accuracy, baseline, case study
- **business**: business, marketing, customer, commerce, e-commerce, sales,
  advertising, decision, consumer, enterprise, revenue, pricing, recommendation,
  personalization, workflow, productivity

**CHỈ LOẠI khi điểm < 4** — tức bài hầu như không có từ khóa core/applied/business
nào. Đây là bài lạc đề rõ ràng.

## 3.4 Tầng D — LLM chấm điểm
Không lọc nữa, mà CHẤM ĐIỂM (xem Phần 4).

---

# PHẦN 4 — TIÊU CHÍ CHẤM ĐIỂM (BƯỚC 2.4)

## 4.1 Vì sao phải dùng LLM
Test thực tế: chấm heuristic 30 bài cs.AI → điểm cao nhất chỉ 58, nén ở 30-49.
Heuristic không hiểu ngữ nghĩa → không phân tầng được. **Bắt buộc LLM chấm.**

## 4.2 Thang điểm 0-100 (4 tiêu chí)

| Tiêu chí | Điểm | Câu hỏi cho LLM |
|---|---|---|
| Liên quan cốt lõi | 0-35 | Paper có về AI/LLM/agent/multi-agent/tool-use? |
| Ứng dụng thực tiễn | 0-25 | Có experiment/benchmark/dataset thật? Hay thuần lý thuyết? |
| Liên quan business/content | 0-20 | Áp dụng được cho business/marketing/content/decision? |
| Insight hành động được | 0-20 | Đọc xong làm được gì cụ thể? Có method/công thức? |

## 4.3 Phân nhóm theo điểm

```
75-100  → high   "DISTILL NGAY"      (điểm cao, chắc chắn giá trị)
55-74   → mid    "làm sau"           (distill tự động, không cần gửi tele)
35-54   → fuzzy  "CẦN BẠN DUYỆT"     (mơ hồ, gửi tele, chờ user quyết)
0-34    → drop   loại                (không gửi, không distill)
-1      → error  LLM lỗi             (gọi lại)
```

## 4.4 Prompt chấm điểm (cho LLM)
```
Chấm điểm mức độ liên quan của paper arXiv cho một solopreneur làm content/business về AI.
Chấm 0-100 theo 4 tiêu chí: [liệt kê 4 tiêu chí trên]
TITLE: <title>
ABSTRACT: <abstract>
Trả về DUY NHẤT JSON: {"score": <0-100>, "reason": "<1 câu>", "group": "<high|mid|fuzzy|drop>"}
```

---

# PHẦN 5 — QUY TRÌNH DISTILL RA GIÁ TRỊ (BƯỚC 4) — PHẦN CỐT LÕI

Đây là phần quan trọng nhất. **Tóm tắt abstract KHÔNG phải giá trị.**

## 5.0 Bốn tầng giá trị

```
KNOWLEDGE (biết)   — sự thật, số liệu, khái niệm.  "X đạt Y% trên Z"
      ↓
INSIGHT (hiểu)     — tại sao đúng/sai, cơ chế ẩn.   "X hiệu quả VÌ cơ chế W"
      ↓
IDEA (làm)         — hành động cụ thể áp dụng.      "Thử W vào việc V, bước đầu là…"
      ↓
WISDOM (phán đoán) — nguyên tắc tổng quát.          "Nguyên tắc: khi nào dùng/không"
```

## 5.1 Bước 0 — Đánh giá đáng đọc (trước khi tốn công)
3 câu từ title+abstract:
1. Vấn đề: paper giải quyết gì? (1 câu, KHÔNG dùng từ của abstract)
2. Ai cần: solopreneur content/business/AI dùng được không? (YES/NO)
3. Giá trị tiềm năng: đọc hết có rút ra idea gì? (đoán 1 câu)
→ Nếu (2)=NO: ghi lý do, DỪNG.

## 5.2 Bước 1 — Đọc sâu
Thứ tự: Abstract → Introduction → Related Work (cuối) → Method → Results →
Limitations → Conclusion.
Ghi chú 4 cột: | Số liệu | Cơ chế | Bất ngờ | Mâu thuẫn với niềm tin cũ |

## 5.3 Bước 2 — Chưng cất 4 tầng

### KNOWLEDGE — Biết gì?
- Số liệu thật, chính xác, có nguồn: "Trên dataset X, model Y đạt Z% vs baseline W% (+N%)"
- Khái niệm mới: định nghĩa + 1 câu giải thích
- Không có số → `[NO BENCHMARK]`, KHÔNG ước lượng

### INSIGHT — Hiểu gì? (hay bị bỏ sót — tầng tạo khác biệt)
- TẠI SAO nó đúng/sai? "X hoạt động VÌ cơ chế W"
- Cơ chế ẩn: điều gì thực sự xảy ra bên dưới?
- Điều kiện: insight chỉ đúng khi nào?
- Nghịch lý: có gì phản trực giác?
- Format: "[Hiện tượng] VÌ [cơ chế]. Nghĩa là [hệ quả]."

### IDEA — Làm gì? (tầng hành động)
2-3 idea, mỗi idea: Cái gì (hành động cụ thể) + Cho ai (việc gì của user) +
Bước đầu (bước 1 để bắt đầu).
- Format: "Áp dụng [X] vào [việc V]: bước đầu là [hành động]."

### WISDOM — Nguyên tắc gì? (tầng cao nhất, hiếm)
0-2 nguyên tắc tổng quát, đúng ngoài phạm vi paper:
- Nguyên tắc: phát biểu 1 câu (như châm ngôn)
- Khi nào dùng / khi nào KHÔNG
- Ví dụ ngoài domain gốc
- Không đủ tầm → `[NO WISDOM]` — KHÔNG bịa

## 5.4 Bước 3 — Cấu trúc README (bắt buộc)
```markdown
# [arxiv-id] Tên paper
## Giá trị cốt lõi (1 câu)   ← phải là IDEA/INSIGHT, không phải mô tả
## Problem                    ← gap, KHÔNG paraphrase abstract
## Contribution               ← khác prior work thế nào
## Method                     ← pipeline 3-5 câu
## KNOWLEDGE — Số liệu & khái niệm
## INSIGHT — Cơ chế & tại sao
## IDEA — Áp dụng được gì
## WISDOM — Nguyên tắc tổng quát  (hoặc [NO WISDOM])
## Assumptions & Limitations
## Metadata
```

## 5.5 Bước 4 — Tạo skill (nếu đủ điều kiện)
Điều kiện (tất cả phải đúng): [applied]/[theoretical] + method ≥3 bước cụ thể +
đọc skill là follow được + không phải survey.
Format: Khi nào dùng / KHÔNG dùng / Input / Các bước / Output / Ví dụ / Gotchas.

## 5.6 Bước 5 — Test skill
Self-check (người không đọc paper theo được?) → Dry run → Verdict
([SKILL VALID] / [SKILL NEEDS REVISION]).

## 5.7 Bước 6 — Song ngữ
README_en.md + skill_en.md (tiếng Anh đầy đủ).

## 5.8 Bước 7 — Báo cáo + commit + push
```
✓ Paper: [tên] ([id]) | Nhãn: [applied/theoretical/survey]
✓ Giá trị: K[n] I[n] Id[n] W[n]   (số tầng rút ra được)
✓ Idea nổi bật: [1 câu]
✓ Skill: [tên]/N/A | Test: [VALID/NEEDS REVISION]
→ Tiếp tục paper tiếp theo
```
Sau đó: `git add -A` → `git commit` → `git push` → paper tiếp theo.

## 5.9 Cấu trúc 5 file/paper
```
papers/<tên-paper>/
├── README.md       # tiếng Việt, từ chuyên ngành Anh có giải thích ngoặc
├── README_en.md    # tiếng Anh đầy đủ
├── skill.md        # tiếng Việt (nếu đủ điều kiện)
├── skill_en.md     # tiếng Anh
└── metadata.json   # name, arxiv_id, authors, year, categories, links,
                    # classification, skill_status, skill_name
```

---

# PHẦN 6 — VẬN HÀNH

## 6.1 Chạy tự động

**Cronjob đã setup:** `arxiv-daily-scan` (job_id a4f281f16f13), chạy **5h sáng mỗi ngày**.
```
Chạy: scan → lọc → chấm điểm → gửi Telegram (KHÔNG tự distill)
     → để user thức dậy duyệt rồi tự chạy distill
Lịch: 0 5 * * *  (cron)  |  profile: research-arxiv  |  no_agent: true
Log : ~/work/arXiv-distill/logs/daily-scan-<ngày>.log
```

Quản lý cronjob:
```bash
hermes --profile research-arxiv cron list
hermes --profile research-arxiv cron run arxiv-daily-scan    # chạy ngay
hermes --profile research-arxiv cron pause arxiv-daily-scan
hermes --profile research-arxiv cron remove arxiv-daily-scan
```

## 6.1b Distill thủ công (khi thức dậy)
Sau khi nhận Telegram + duyệt nhóm mơ hồ:
```bash
cd ~/work/arXiv-distill
hermes --profile research-arxiv chat       # agent đọc queue + distill
# hoặc chạy supervisor cho cả ngày:
./run-distill.sh
```

## 6.2 Chạy 1 vòng pipeline thủ công
```bash
cd ~/work/arXiv-distill
python3 scripts/scan_arxiv.py              # quét + chấm điểm
python3 scripts/send_telegram.py scans/$(date +%F).json   # gửi tele
hermes --profile research-arxiv chat       # distill
```

## 6.3 Cấu hình đã set (profile research-arxiv)
```
model.default      = inclusionai/ling-3.1-flash (openrouter, $0)
agent.max_turns    = 500      (session dài)
agent.api_max_retries = 8     (vượt 429, backoff tự động)
display.streaming  = false    (ling ổn định hơn)
display.language   = vi
```

## 6.4 Hành vi của ling-3.1-flash (đã đo THỰC TẾ)

```
Rate limit : ~12 request liên tiếp → 429, hồi phục ~5s
             → giãn 3s/request khi batch; Hermes tự backoff + retry 8 lần
```

**PHÁT HIỆN QUAN TRỌNG — ling là model REASONING, không phải chat:**
```
Khi gọi với max_tokens nhỏ (200-300):
├─ content = None (RỖNG)                    ← không có câu trả lời
├─ reasoning_tokens = 333 (đã dùng)         ← dồn hết vào suy nghĩ
├─ finish_reason = "length"                 ← hết token giữa lúc suy nghĩ
└─ KẾT QUẢ: mọi lần gọi đều trả về rỗng

Khi gọi với max_tokens = 2000:
├─ reasoning_tokens = 360 → suy nghĩ xong
├─ content = '{"score": 97, "reason": "...", ...}'   ← JSON ĐÚNG
└─ finish_reason = "stop"                   ← hoàn thành sạch
```

**QUY TẮC BẮT BUỘC: luôn set `max_tokens >= 2000` cho ling.** Model này suy nghĩ
200-500 token TRƯỚC khi viết câu trả lời. max_tokens nhỏ = reasoning ăn hết =
content rỗng. Đây là nguyên nhân của mọi "output rỗng" gặp trước đây.

**Fallback:** nếu `content` rỗng mà có `reasoning`, parse JSON từ `reasoning`.
Script `scan_arxiv.py` đã có fallback này.

Nếu vẫn thấy "API call failed after 8 retries": tăng `api_max_retries` lên 12-15,
hoặc cấu hình fallback provider (đổi model khác khi 429).

## 6.5 Xử lý sự cố
| Triệu chứng | Xử lý |
|---|---|
| Scan 0 bài | Bình thường nếu cuối tuần. Kiểm tra watermark. |
| 429 liên tục | Hermes tự retry; nếu >10 phút không tiến → kiểm tra credit |
| README/skill rỗng | Chia nhỏ section, gọi lại. Không ghi file rỗng. |
| Supervisor dừng | Sau 12 lỗi liên tiếp → sửa nguyên nhân gốc, chạy lại |
| Paper dở (thiếu file) | Session sau tự bù, hoặc chạy lại distill paper đó |

---

# PHẦN 7 — NGUYÊN TẮC VÀNG

1. **Chạy liên tục, không dừng hỏi.** User bực khi agent dừng xin phép.
2. **Chất lượng > số lượng.** Mỗi paper đủ 7 bước. Không rush.
3. **Thà giữ thừa hơn bỏ sót.** Heuristic chỉ loại bài lạc đề hoàn toàn.
4. **Tóm tắt ≠ giá trị.** Bắt buộc có INSIGHT (tại sao) + IDEA (làm gì).
5. **Không bịa.** Số liệu sai nguồn → [NO BENCHMARK]. Wisdom không đủ tầm → [NO WISDOM].
6. **Commit + push sau MỖI paper.** Không batch.
7. **Số hóa mọi thứ.** Trạng thái trong file, không trong đầu.
8. **Việc ra tiền = số paper giá trị hoàn thành**, không phải config đẹp.
