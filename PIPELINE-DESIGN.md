# PIPELINE TỰ ĐỘNG HẰNG NGÀY — Thiết kế

> Trạng thái: DRAFT — chờ user duyệt trước khi build
> Ngày: 2026-10-11

## 0. Mục tiêu

5h sáng mỗi ngày, tự động:
1. Quét paper arXiv mới kể từ lần quét trước
2. Lọc bỏ chủ đề không liên quan
3. Chấm điểm liên quan
4. Gửi danh sách lên Telegram
5. Distill từ điểm cao xuống, ưu tiên chất lượng

Bạn dậy → xem tele → duyệt/bỏ các paper mơ hồ (điểm thấp) → agent đã làm xong phần điểm cao.

---

## 1. BỐI CẢNH THẬT (đã kiểm chứng, KHÁC giả định ban đầu)

### 1.1 arXiv nghỉ cuối tuần
`skipDays: Saturday, Sunday` trong RSS. Bài mới nhất lúc viết doc: 2026-10-08 (thứ Tư).
→ Chạy sáng thứ 2 sẽ gặp bài dồn từ thứ 5,6 tuần trước. Chạy sáng thứ 7, CN → **0 bài**.

### 1.2 Quét theo WATERMARK, không theo "24h cố định"
Lưu mốc "lần quét cuối" vào `state/last_scan.json`. Mỗi lần chạy query từ mốc đó đến nay.
- Ngày thường: lấy bài của ~1 ngày.
- Sau cuối tuần: lấy bài dồn 3 ngày.
- Không bao giờ bỏ sót, không bao giờ trùng.

### 1.3 Volume
cs.AI ~100-300 bài/ngày. Nếu quét nhiều category → 1000+/ngày. **BẮT BUỘC lọc** trước khi gửi tele, không thì spam.

### 1.4 API đúng (đã test)
```bash
# PHẢI dùng https + follow redirect (http trả 301)
curl -sL "https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=100"
# RSS: https://rss.arxiv.org/rss/cs.AI (chỉ có bài trong ngày công bố, rỗng cuối tuần)
```

---

## 2. CATEGORY QUÉT & TIÊU CHÍ CHẤM ĐIỂM

### 2.1 Category giữ lại

| Category | Lý do |
|---|---|
| cs.AI | AI tổng quát |
| cs.CL | Xử lý ngôn ngữ (LLM) |
| cs.LG | Học máy |
| cs.MA | Multi-agent |
| cs.IR | Tìm kiếm / RAG |
| cs.SE | Kỹ thuật phần mềm (agent tooling) |
| cs.HC | Human-computer interaction (UX agent) |

### 2.2 Category loại

`physics.*`, `math.*` (thuần), `q-bio.*` (sinh y), `q-fin.*` (tài chính thuần), `stat.ME`, `eess.SP`...

### 2.3 Tiêu chí chấm điểm — KIẾN TRÚC LAI (đã test heuristic)

**Test thực tế:** chấm heuristic 30 bài cs.AI → điểm cao nhất chỉ 58, nén ở 30-49.
Heuristic không hiểu ngữ nghĩa → không phân tầng được. Kết luận: **phải dùng LLM chấm.**

**Kiến trúc 2 tầng (tiết kiệm token):**
```
TẦNG 1 — HEURISTIC lọc thô (Python, miễn phí)
  - Bỏ bài ngoài category
  - Bỏ bài rõ ràng không liên quan (keyword score < 15)
  - Loại ~50-70% ngay

TẦNG 2 — LLM chấm điểm (chỉ ~30-50 bài còn lại)
  - Prompt: cho title+abstract, yêu cầu chấm 0-100 theo tiêu chí
  - Model rẻ (ling-3.1-flash hoặc deepseek) → tốn ít
  - Output: JSON {điểm, lý do, nhóm}
```

Tiêu chí LLM chấm (0-100):

| Tiêu chí | Điểm | Mô tả cho LLM |
|---|---|---|
| Liên quan cốt lõi | 0-35 | AI/LLM/agent/multi-agent/tool-use? |
| Ứng dụng thực tiễn | 0-25 | Có experiment/benchmark/dataset thật? |
| Liên quan business/content | 0-20 | Áp dụng được cho business/marketing/content/decision? |
| Insight hành động được | 0-20 | Đọc xong làm được gì? Có method/công thức cụ thể? |

Phân loại:
- **75-100** → distill NGAY (điểm cao)
- **55-74** → distill sau khi xong nhóm cao
- **35-54** → MƠ HỒ, gửi tele để user duyệt khi dậy
- **0-34** → loại, không gửi

### 2.4 QUYẾT ĐỊNH (tự chốt do user không phản hồi kịp)
- **(a) Category**: dùng 7 category §2.1
- **(b) Gửi tele**: gửi 2 nhóm — 75+ ("distill ngay") + 35-54 ("CẦN BẠN DUYỆT"). Nhóm 55-74 làm tự động, không cần gửi.
- **(c) Giới hạn/ngày**: KHÔNG giới hạn cứng, nhưng distill tuần tự từ cao xuống — hết ngày còn bao nhiêu thì dừng chỗ đó, tiếp hôm sau.
- **(d) Telegram**: viết sẵn hàm `send_telegram.py`, chờ user setup bot token.

---

## 3. LUỒNG CHẠY (5h sáng hằng ngày)

```
[Bước 1] Quét arXiv (watermark → now)
   ↓ lưu: state/last_scan.json
[Bước 2] Lọc category → bỏ chủ đề ngoài
   ↓
[Bước 3] Chấm điểm (heuristic trước, LLM nếu cần)
   ↓ lưu: scans/<ngày>.json
[Bước 4] Gửi Telegram: danh sách đã sắp theo điểm
   ├─ Nhóm 80+: "distill ngay"
   ├─ Nhóm 50-79: "làm sau"
   └─ Nhóm 30-49: "CẦN BẠN DUYỆT"
   ↓
[Bước 5] Distill từ điểm cao xuống (chất lượng ưu tiên, tuần tự)
   ↓ mỗi paper: commit+push
[Bước 6] Hết nhóm chắc chắn → dừng, chờ user dậy duyệt nhóm mơ hồ
```

---

## 4. QUY TRÌNH DISTILL (giữ nguyên protocol 6 bước + nâng cấp)

Protocol hiện tại (`arxiv-distill-protocol`) đã tốt. Nâng cấp thêm:

### Bước 0 (MỚI) — Đánh giá giá trị TRƯỚC khi đọc full
Trước khi tốn token đọc paper, trả lời 3 câu từ abstract:
1. Paper giải quyết vấn đề gì? (1 câu)
2. Có áp dụng được cho business/content/agent không? (YES/NO + lý do)
3. Nếu YES → distill. Nếu NO → ghi lý do, bỏ.

### Bước 1-6 — Giữ nguyên protocol hiện tại
(kiểm tra topic → phân loại → README → skill → test skill → bilingual → báo cáo)

### Bổ sung: "Giá trị cốt lõi" mỗi paper
Thêm section vào README:
```markdown
## Giá trị cốt lõi (1 câu)
[Nếu chỉ đọc 1 câu về paper này, đọc câu này]
```

---

## 5. CẤU TRÚC FILE

```
~/work/arXiv-distill/
├── state/
│   └── last_scan.json          # watermark lần quét cuối
├── scans/
│   └── 2026-10-11.json         # kết quả quét + điểm ngày hôm đó
├── scripts/
│   ├── scan_arxiv.py           # quét + lọc + chấm điểm
│   ├── score_papers.py         # logic chấm điểm
│   └── send_telegram.py        # gửi tele (chờ user setup bot)
├── papers/                     # (đã có) kết quả distill
├── report.md                   # (đã có)
└── WORKFLOW-HANG-NGAY.md       # (đã có)
```

---

## 6. CÁI CẦN QUYẾT TRƯỚC KHI BUILD

1. **Số category** — danh sách ở §2.1 đã đủ chưa? Thêm/bớt?
2. **Ngưỡng gửi tele** — gửi cả nhóm 30-49 (mơ hồ) hay chỉ 50+?
3. **Số paper distill/ngày** — giới hạn không? (chất lượng > số lượng)
4. **Telegram** — user setup bot sau, pipeline viết sẵn chỗ chèn token
