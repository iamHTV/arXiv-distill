#!/usr/bin/env bash
# ============================================================================
# daily_scan.sh — Chạy bởi CRONJOB lúc 5h sáng.
# Quét arXiv → lọc → chấm điểm → gửi Telegram. KHÔNG tự distill.
# Distill do user khởi động khi thức dậy (để user duyệt nhóm mơ hồ trước).
#
# LƯU Ý: dùng đường dẫn TUYỆT ĐỐI, KHÔNG dùng $HOME — vì khi chạy trong cronjob
# dưới profile research-arxiv, $HOME bị override thành profile home.
# ============================================================================
set -uo pipefail
REPO="/home/iamhtv/work/arXiv-distill"
cd "$REPO" || exit 1
TODAY="$(date +%F)"
LOGDIR="$REPO/logs"; mkdir -p "$LOGDIR"
LOG="$LOGDIR/daily-scan-$TODAY.log"

{
  echo "=== DAILY SCAN $(date '+%F %T') ==="
  python3 scripts/scan_arxiv.py
  echo "--- gửi Telegram ---"
  python3 scripts/send_telegram.py "scans/$TODAY.json"
  echo "=== XONG $(date '+%F %T') ==="
} >> "$LOG" 2>&1
