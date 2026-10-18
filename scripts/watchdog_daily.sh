#!/usr/bin/env bash
# watchdog_daily.sh — Kiểm tra báo cáo tổng hợp hôm nay; nếu thiếu → chạy lại pipeline.
# Giới hạn 4 lần retry/ngày. Bỏ qua nếu pipeline đang chạy.
# Theo daily-workflow-arxiv-distill (WATCHDOG + pitfalls 24, 25).
set -uo pipefail

REPO=/home/iamhtv/work/arXiv-distill
TODAY=$(date +%F)
REPORT="$REPO/scans/$TODAY/README.md"
LOG="$REPO/logs/watchdog-retry.log"
COUNT_FILE="$REPO/state/watchdog_retry_count.json"
RUN_PIPELINE="$REPO/scripts/run_pipeline.sh"
DAILY_SUMMARY="$REPO/scripts/daily_summary.py"

log() {
  echo "[$(date +%F\ %T)] $*" | tee -a "$LOG"
}

# --- Bước 0 (nhẹ): phát hiện agent distill đang chạy giữa chừng (pitfall 22) ---
HERMES_PID=$(pgrep -f "hermes.*research-arxiv.*chat" 2>/dev/null | head -n1)
if [ -n "$HERMES_PID" ]; then
  # Pitfall 24: stale hermes process (idle >1h, no git activity) chặn watchdog → kill rồi tiếp tục
  CPU=$(ps -p "$HERMES_PID" -o %cpu= 2>/dev/null | tr -d ' ' || echo "0")
  GIT_RECENT=$(git -C "$REPO" log --oneline --since="1 hour ago" 2>/dev/null | wc -l)
  GIT_DIRTY=$(git -C "$REPO" status --short 2>/dev/null | grep -E '^\s*(M\|\?\?).*report.md|^\s*\?\?\s*papers/' || true)
  if [ "${CPU:-0}" = "0" ] && [ "$GIT_RECENT" -eq 0 ] && [ -z "$GIT_DIRTY" ]; then
    log "Hermes PID $HERMES_PID lạ thời (CPU=0, không git activity 1h, không dang viết paper) -> kill stale process."
    kill "$HERMES_PID" 2>/dev/null || true
    sleep 2
  else
    log "Pipeline/hermes dang chay (PID=$HERMES_PID, CPU=$CPU, git_recent=$GIT_RECENT) -> bo qua lut watchdog."
    exit 0
  fi
fi

if pgrep -f "run_pipeline.sh" >/dev/null 2>&1; then
  log "run_pipeline.sh dang chay -> bo qua lut watchdog."
  exit 0
fi

# --- Kiểm tra báo cáo hôm nay đã tồn tại chưa ---
if [ -f "$REPORT" ]; then
  log "Bao cao hom nay da ton tai: $REPORT -> ket thuc."
  exit 0
fi

# --- Đọc số lần retry hôm nay ---
if [ -f "$COUNT_FILE" ]; then
  COUNT=$(python3 -c "import json,sys; d=json.load(open('$COUNT_FILE')); print(int(d.get('$TODAY', 0)))" 2>/dev/null || echo 0)
else
  COUNT=0
fi

if [ "$COUNT" -ge 4 ]; then
  log "Da dat gioi han 4 lan retry hom nay ($TODAY) -> bo qua."
  exit 0
fi

COUNT=$((COUNT + 1))
log "Bao cao hom nay chua ton tai. Chay lai pipeline (lan retry $COUNT/4)."

# Cap nhat so lan retry
python3 - <<'PY' "$COUNT_FILE" "$TODAY" "$COUNT"
import json, os, sys
f, today, count = sys.argv[1], sys.argv[2], int(sys.argv[3])
d = json.load(open(f)) if os.path.exists(f) else {}
d[today] = count
with open(f, "w") as fh:
    json.dump(d, fh, indent=2)
PY

# --- Chạy lại pipeline ---
if [ -x "$RUN_PIPELINE" ] && [ -f "$DAILY_SUMMARY" ]; then
  "$RUN_PIPELINE" --no-tele
  python3 "$DAILY_SUMMARY"
  if [ -f "$REPORT" ]; then
    log "Da sinh bao cao hom nay: $REPORT"
  else
    log "CHU-Y: pipeline chay xong nhung $REPORT van chua xuat hien."
  fi
else
  log "LOI: scripts/run_pipeline.sh hoac scripts/daily_summary.py khong ton tai. Khong the chay pipeline."
fi

log "Hoan thanh lut watchdog hom nay ($TODAY)."
exit 0
