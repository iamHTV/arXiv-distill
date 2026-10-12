#!/usr/bin/env bash
# ============================================================================
# daily_scan.sh — Chạy bởi CRONJOB lúc 5h sáng (giờ VN).
# Quét arXiv → lọc → chấm điểm → ghi file tóm tắt + gửi Telegram.
# KHÔNG tự distill (user thức dậy duyệt rồi mới distill).
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
  echo "=== DAILY SCAN $(date '+%F %T %Z') ==="
  python3 scripts/scan_arxiv.py
  echo "--- ghi tóm tắt + gửi Telegram ---"
  python3 scripts/send_telegram.py "scans/$TODAY.json"
  echo "=== XONG $(date '+%F %T %Z') ==="
  echo "File tóm tắt: scans/$TODAY/SUMMARY.md"
} >> "$LOG" 2>&1
