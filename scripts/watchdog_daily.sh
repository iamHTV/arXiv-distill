#!/usr/bin/env bash
# ============================================================================
# watchdog_daily.sh — Kiểm tra báo cáo tổng hợp ngày, chạy lại nếu thiếu.
#
# Chạy bởi cronjob mỗi 30 phút trong khung giờ làm việc.
# Nếu scans/<hôm nay>/README.md chưa tồn tại → chạy lại run_pipeline.sh.
# Giới hạn tối đa 4 lần chạy lại/ngày để tránh loop vô ích.
# ============================================================================
set -uo pipefail

REPO="/home/iamhtv/work/arXiv-distill"
LOGDIR="$REPO/logs"
WATCH_LOG="$LOGDIR/watchdog-retry.log"
STATE_FILE="$REPO/state/watchdog_retry_count.json"
MAX_RETRY=4

mkdir -p "$LOGDIR" "$REPO/state"

TODAY="$(date +%F)"
SUMMARY="$REPO/scans/$TODAY/README.md"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$WATCH_LOG"
}

# ── Kiểm tra xem báo cáo hôm nay đã có chưa ─────────────────────────────────
if [[ -f "$SUMMARY" ]]; then
    log "Báo cáo hôm nay ($TODAY) đã tồn tại. Không cần chạy lại."
    exit 0
fi

# ── Kiểm tra pipeline có đang chạy không (tránh trùng instance) ─────────────
if pgrep -f "run_pipeline.sh" >/dev/null 2>&1 || pgrep -f "hermes.*chat" >/dev/null 2>&1; then
    log "Pipeline đang chạy (hermes hoặc run_pipeline.sh). Bỏ qua lượt này."
    exit 0
fi

# ── Đọc số lần retry hôm nay ───────────────────────────────────────────────
retry_count=0
if [[ -f "$STATE_FILE" ]]; then
    retry_count=$(python3 -c "import json; d=json.load(open('$STATE_FILE')); print(d.get('$TODAY', 0))" 2>/dev/null || echo 0)
fi

if [[ $retry_count -ge $MAX_RETRY ]]; then
    log "Đã retry $MAX_RETRY lần hôm nay. Dừng để tránh loop."
    exit 0
fi

# ── Chạy lại pipeline ──────────────────────────────────────────────────────
retry_count=$((retry_count + 1))
log "Báo cáo hôm nay chưa có. Chạy lại pipeline (lần retry #$retry_count)..."

cd "$REPO" || { log "FATAL: không vào được $REPO"; exit 1; }

# Ghi lại số retry trước khi chạy (để đánh dấu đã bắt đầu)
python3 - "$STATE_FILE" "$TODAY" "$retry_count" <<'PY'
import json, sys
state_file, today, count = sys.argv[1], sys.argv[2], int(sys.argv[3])
d = {}
try:
    d = json.load(open(state_file))
except Exception:
    pass
d[today] = count
json.dump(d, open(state_file, "w"), indent=2)
PY

bash scripts/run_pipeline.sh --no-tele 2>&1 | tee -a "$WATCH_LOG"
RC=${PIPESTATUS[0]}

if [[ $RC -eq 0 ]]; then
    log "Pipeline chạy lại thành công (mã 0). Chạy daily_summary để sinh báo cáo..."
    python3 scripts/daily_summary.py 2>&1 | tee -a "$WATCH_LOG"
else
    log "Pipeline chạy lại thất bại (mã $RC). Sẽ thử lại ở lượt tiếp theo."
fi

exit $RC
