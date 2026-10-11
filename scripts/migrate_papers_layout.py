#!/usr/bin/env python3
"""
migrate_papers_layout.py — Di chuyển papers/<tên>/ → papers/<năm>/<tháng>/<ngày>/<tên>/

Ngày dùng = NGÀY COMMIT (ngày distill thật), lấy từ git log.
Chạy 1 lần: python3 scripts/migrate_papers_layout.py [--dry-run]
"""
import os
import re
import subprocess
import sys

REPO = "/home/iamhtv/work/arXiv-distill"
PAPERS = os.path.join(REPO, "papers")


def commit_date(paper_name):
    """Lấy ngày commit đầu tiên của paper (YYYY-MM-DD)."""
    p = "papers/%s" % paper_name
    try:
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--diff-filter=A", "--format=%ad",
             "--date=short", "--reverse", "--", p],
            capture_output=True, text=True, timeout=30).stdout.strip()
        if out:
            return out.split("\n")[0]
    except Exception:
        pass
    return None


def main():
    dry = "--dry-run" in sys.argv
    entries = sorted(os.listdir(PAPERS))
    moved = skipped = 0

    for name in entries:
        src = os.path.join(PAPERS, name)
        if not os.path.isdir(src):
            continue
        # Đã ở dạng năm/tháng/ngày? (tên là 4 chữ số)
        if re.fullmatch(r"\d{4}", name):
            print("  [skip] đã migrate: %s" % name)
            skipped += 1
            continue

        d = commit_date(name)
        if not d:
            print("  [skip] không có ngày commit: %s" % name)
            skipped += 1
            continue

        y, m, day = d.split("-")
        dst_dir = os.path.join(PAPERS, y, m, day)
        dst = os.path.join(dst_dir, name)
        print("  %s -> %s/%s/%s/%s" % (name, y, m, day, name))

        if not dry:
            os.makedirs(dst_dir, exist_ok=True)
            try:
                subprocess.run(["git", "-C", REPO, "mv", src, dst],
                               check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                print("    LỖI git mv: %s" % e.stderr[:100])
                continue
        moved += 1

    print("\n%s: %d paper di chuyển, %d bỏ qua." %
          ("DRY-RUN" if dry else "XONG", moved, skipped))


if __name__ == "__main__":
    main()
