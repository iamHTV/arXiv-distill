#!/usr/bin/env bash
# ============================================================================
# run_pipeline.sh — MỘT VÒNG PIPELINE ĐẦY ĐỦ
#
# Bước: quét arXiv → lọc → chấm điểm → gửi Telegram → distill từ điểm cao xuống
#
# Cách dùng:
#   ./run_pipeline.sh              # chạy đầy đủ
#   ./run_pipeline.sh --scan-only  # chỉ quét + chấm + gửi tele, không distill
#   ./run_pipeline.sh --no-tele    # không gửi tele
#
# Đặt lịch 5h sáng: xem PIPELINE-DOCS.md §6 hoặc cronjob Hermes.
# ============================================================================
set -uo pipefail

REPO="/home/iamhtv/work/arXiv-distill"
PROFILE="research-arxiv"
cd "$REPO" || exit 1

TODAY="$(date +%F)"
SCAN_FILE="scans/$TODAY.json"
FILTER_FILE="scans/${TODAY}_filtered.json"
LOGDIR="$REPO/logs"
LOG="$LOGDIR/pipeline-$TODAY.log"
mkdir -p "$LOGDIR" "$REPO/state" "$REPO/scans"

log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

MODE="${1:-full}"

log "=========================================="
log "PIPELINE BẮT ĐẦU — mode=$MODE ngày $TODAY"
log "=========================================="

# ── Bước 1+2+3: Quét + lọc + chấm điểm abstract ─────────────────────────────
log "[1/5] Quét arXiv + lọc + chấm điểm LLM (abstract)..."
python3 scripts/scan_arxiv.py 2>&1 | tee -a "$LOG"
SCAN_RC=${PIPESTATUS[0]}
if [[ $SCAN_RC -ne 0 ]]; then
    log "LỖI: scan_arxiv.py thất bại (mã $SCAN_RC). Dừng pipeline."
    exit $SCAN_RC
fi

if [[ ! -f "$SCAN_FILE" ]]; then
    log "LỖI: Không thấy $SCAN_FILE sau khi quét."
    exit 1
fi

# ── Bước 2: Đọc full text + LLM đánh giá lại → chọn top 10 chuẩn nhất ───────
log "[2/5] Đọc full text PDF + LLM đánh giá lại → lọc top 10 chuẩn nhất..."
python3 scripts/filter_full_text.py "$TODAY" 2>&1 | tee -a "$LOG"
FILTER_RC=${PIPESTATUS[0]}
if [[ $FILTER_RC -ne 0 ]]; then
    log "LỖI: filter_full_text.py thất bại (mã $FILTER_RC). Dừng pipeline."
    exit $FILTER_RC
fi

if [[ ! -f "$FILTER_FILE" ]]; then
    log "LỖI: Không thấy $FILTER_FILE sau khi lọc full text."
    exit 1
fi

# ── Bước 3: Gửi Telegram ───────────────────────────────────────────────────
if [[ "$MODE" != "--no-tele" ]]; then
    log "[3/5] Gửi Telegram..."
    python3 scripts/send_telegram.py "$SCAN_FILE" 2>&1 | tee -a "$LOG"
else
    log "[3/5] Bỏ qua Telegram (--no-tele)"
fi

if [[ "$MODE" == "--scan-only" ]]; then
    log "Chế độ --scan-only: dừng sau khi quét. Xong."
    exit 0
fi

# ── Bước 4: Distill từ top 10 chuẩn nhất ────────────────────────────────────
log "[4/5] Chuẩn bị danh sách distill (top 10 từ full-text filter)..."

# Lấy paper từ file filtered (đã sắp điểm full_text_score cao xuống)
python3 - "$FILTER_FILE" "$REPO/state/distill_queue.txt" <<'PY'
import json, sys
scan = json.load(open(sys.argv[1]))
papers = scan.get("papers", [])
auto = [p for p in papers if p.get("full_text_verdict") == "KEEP"]
auto.sort(key=lambda x: -x.get("full_text_score", 0))
with open(sys.argv[2], "w") as f:
    for p in auto:
        f.write("%d\t%s\t%s\n" % (p.get("full_text_score", 0), p["id"], p["title"]))
print("Queue: %d bài (top 10 từ full-text filter)" % len(auto))
for p in auto[:10]:
    print("  %3d  %s  %s" % (p.get("full_text_score", 0), p["id"], p["title"][:60]))
PY

QUEUE="$REPO/state/distill_queue.txt"
N_QUEUE=$(wc -l < "$QUEUE" 2>/dev/null || echo 0)
log "Có $N_QUEUE bài trong queue distill."

if [[ "$N_QUEUE" -eq 0 ]]; then
    log "Không có bài nào cần distill. Xong."
    exit 0
fi

# ── Bước 5: Chạy distill ───────────────────────────────────────────────────
log "[5/5] Distill ($N_QUEUE bài, ưu tiên chất lượng, tuần tự)..."
log "Danh sách: $QUEUE"
log "Chạy hermes — agent đọc queue + report.md và distill từ cao xuống."

hermes --profile "$PROFILE" chat \
    -q "Đọc state/distill_queue.txt (danh sách paper cần distill, đã sắp điểm cao xuống) và report.md (tiến độ). Distill tuần tự từ đầu queue theo skill arxiv-distill-value-extraction (load skill TRƯỚC). Mỗi paper: đủ 7 bước + 5 file + commit+push. CHẠY LIÊN TỤC, KHÔNG dừng hỏi." \
    2>&1 | tee -a "$LOG"
RC=${PIPESTATUS[0]}

log "Hermes distill thoát (mã $RC). Pipeline xong."

# ── Bước 6: Sinh báo cáo tổng hợp ngày + gửi Telegram ─────────────────────
log "[6/6] Sinh README tổng hợp ngày + gửi Telegram..."
python3 scripts/daily_summary.py 2>&1 | tee -a "$LOG"
log "Báo cáo tổng hợp đã ghi vào scans/$TODAY/README.md"

log "=========================================="
