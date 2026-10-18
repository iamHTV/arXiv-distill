#!/bin/bash
# watchdog_daily.sh — Kiểm tra báo cáo tổng hợp hôm nay đã sinh chưa.
# Nếu chưa → chạy lại pipeline (giới hạn 4 lần/ngày).
# Log: logs/watchdog-retry.log
# Count: state/watchdog_retry_count.json
#
# Được gọi bởi cron job watchdog-arxiv-daily-retry (*/30 * * * *).

set -uo pipefail

REPO_DIR="/home/iamhtv/work/arXiv-distill"
cd "$REPO_DIR" || { echo "[watchdog] KHÔNG vào được $REPO_DIR"; exit 1; }

TODAY=$(date +%Y-%m-%d)
REPORT="scans/$TODAY/README.md"
LOG_FILE="logs/watchdog-retry.log"
COUNT_FILE="state/watchdog_retry_count.json"
MAX_RETRY=4

mkdir -p logs state

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# 1. Nếu báo cáo hôm nay đã tồn tại → thoát im lẽ (không có gì mới)
if [ -f "$REPORT" ]; then
    log "Báo cáo hôm nay ($REPORT) đã tồn tại. Không làm gì."
    exit 0
fi

# 2. Kiểm tra pipeline đang chạy không (hermes hoặc run_pipeline.sh)
if pgrep -f "hermes.*chat" > /dev/null 2>&1 || pgrep -f "run_pipeline.sh" > /dev/null 2>&1; then
    log "Pipeline đang chạy (hermes hoặc run_pipeline.sh). Bỏ qua lượt này."
    exit 0
fi

# 3. Đọc số lần retry hôm nay
if [ -f "$COUNT_FILE" ]; then
    RETRY_COUNT=$(python3 -c "import json; d=json.load(open('$COUNT_FILE')); print(d.get('$TODAY', 0))" 2>/dev/null || echo 0)
else
    RETRY_COUNT=0
fi

if [ "$RETRY_COUNT" -ge "$MAX_RETRY" ]; then
    log "Đã đạt giới hạn retry ($MAX_RETRY) hôm nay. Bỏ qua."
    exit 0
fi

# 4. Chạy lại pipeline
log "Báo cáo hôm nay chưa tồn tại. Chạy lại pipeline (lần retry $((RETRY_COUNT + 1))/$MAX_RETRY)."

# Tăng count
NEW_COUNT=$((RETRY_COUNT + 1))
python3 -c "
import json, os
path='$COUNT_FILE'
d={}
if os.path.exists(path):
    d=json.load(open(path))
d['$TODAY']=$NEW_COUNT
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path,'w') as f:
    json.dump(d, f, indent=2)
"

# Chạy pipeline --no-tele
if [ -x "scripts/run_pipeline.sh" ]; then
    scripts/run_pipeline.sh --no-tele
else
    log "LỖI: scripts/run_pipeline.sh không tồn tại. Không thể chạy pipeline."
fi

# Chạy daily_summary.py
if [ -x "scripts/daily_summary.py" ]; then
    python3 scripts/daily_summary.py
else
    log "LỖI: scripts/daily_summary.py không tồn tại. Không thể sinh báo cáo tổng hợp."
fi

log "Hoàn thành lượt watchdog hôm nay ($TODAY)."
