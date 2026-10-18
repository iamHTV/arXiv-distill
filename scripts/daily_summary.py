#!/usr/bin/env python3
"""
daily_summary.py — Sinh README tổng hợp cho 1 ngày distill (10 bài tốt nhất).

Chạy:  python3 scripts/daily_summary.py [YYYY-MM-DD]

Input:
  - papers/YYYY/MM/DD/*/metadata.json   (đã commit bởi hermes sau mỗi paper)
  - papers/YYYY/MM/DD/*/README.md       (để trích xuất 'làm gì' / Actionable Insights)
  - report.md                           (để trích xuất 'học được gì' — ✓ Insight)

Output:
  - scans/YYYY-MM-DD/README.md          (báo cáo tổng hợp ngày, tiếng Việt)
  - scans/YYYY-MM-DD/README_en.md       (bản tiếng Anh)

Mỗi paper hiển thị:
  ### [N] Tên paper (arXiv ID)
  **Làm gì:** <tóm tắt paper giải quyết vấn đề gì, từ section Problem/Method>
  **Học được gì:** <✓ Insight từ report.md>

Section cuối: 'CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN' — insights thực tế cho solopreneur VN.
"""

import datetime as dt
import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS_ROOT = os.path.join(REPO, "papers")
SCANS_DIR = os.path.join(REPO, "scans")
REPORT_FILE = os.path.join(REPO, "report.md")


def today_str():
    return dt.datetime.now().strftime("%Y-%m-%d")


def list_today_papers(date_str):
    """Trả về list các folder paper của ngày date_str (YYYY-MM-DD)."""
    y, m, d = date_str.split("-")
    pattern = os.path.join(PAPERS_ROOT, y, m, d, "*", "metadata.json")
    files = sorted(glob.glob(pattern))
    return [os.path.dirname(f) for f in files]


def read_meta(folder):
    mp = os.path.join(folder, "metadata.json")
    if os.path.exists(mp):
        return json.load(open(mp, encoding="utf-8"))
    return {}


def read_readme(folder):
    rp = os.path.join(folder, "README.md")
    if os.path.exists(rp):
        return open(rp, encoding="utf-8").read()
    return ""


def extract_problem_summary(readme_text):
    """Lấy 1-2 câu đầu từ section ## Problem để tóm tắt paper làm gì."""
    if not readme_text:
        return ""
    m = re.search(r"## Problem\n(.*?)(?=\n## |\Z)", readme_text, re.S)
    if not m:
        return ""
    block = " ".join(m.group(1).split())
    # Lấy 2 câu đầu (tách theo dấu chấm + khoảng trắng)
    sentences = re.split(r"(?<=[.!?])\s+", block)
    return " ".join(sentences[:2]).strip()


def extract_insight_from_report(date_str, arxiv_id):
    """Lấy '✓ Insight: ...' từ report.md cho arxiv_id."""
    if not arxiv_id or not os.path.exists(REPORT_FILE):
        return ""
    text = open(REPORT_FILE, encoding="utf-8").read()
    # Tìm entry chứa arxiv_id (format: ## Paper #N — Tên (arxiv-id) [label])
    pattern = re.compile(
        r"## Paper #\d+ — .*?\(%s\)[^\n]*\n(.*?)(?=\n## Paper #\d+|\Z)"
        % re.escape(arxiv_id),
        re.S,
    )
    m = pattern.search(text)
    if not m:
        return ""
    block = m.group(1)
    im = re.search(r"✓ Insight:\s*(.+)", block)
    if im:
        return im.group(1).strip()
    return ""


def build_paper_block_vn(i, meta, readme_text, insight):
    """Xây dựng block 1 paper tiếng Việt."""
    name = meta.get("name", "(không có tên)")
    arxiv_id = meta.get("arxiv_id", "")
    classification = meta.get("classification", "?")
    skill_name = meta.get("skill_name", "N/A")
    skill_status = meta.get("skill_status", "N/A")
    summary = extract_problem_summary(readme_text)

    lines = []
    lines.append("### [%d] %s (%s)" % (i, name, arxiv_id))
    lines.append("- Phân loại: `[%s]`" % classification)
    lines.append("- Skill: %s (%s)" % (skill_name, skill_status))
    if summary:
        lines.append("- **Làm gì:** %s" % summary)
    if insight:
        lines.append("- **Học được gì:** %s" % insight)
    pdf = meta.get("link_pdf", "")
    if pdf:
        lines.append("- PDF: %s" % pdf)
    lines.append("")
    return lines


def build_paper_block_en(i, meta, readme_text, insight):
    """Xây dựng block 1 paper tiếng Anh."""
    name = meta.get("name", "(no title)")
    arxiv_id = meta.get("arxiv_id", "")
    classification = meta.get("classification", "?")
    skill_name = meta.get("skill_name", "N/A")
    skill_status = meta.get("skill_status", "N/A")
    summary = extract_problem_summary(readme_text)

    lines = []
    lines.append("### [%d] %s (%s)" % (i, name, arxiv_id))
    lines.append("- Classification: `[%s]`" % classification)
    lines.append("- Skill: %s (%s)" % (skill_name, skill_status))
    if summary:
        lines.append("- **What it does:** %s" % summary)
    if insight:
        lines.append("- **Key insight:** %s" % insight)
    pdf = meta.get("link_pdf", "")
    if pdf:
        lines.append("- PDF: %s" % pdf)
    lines.append("")
    return lines


def build_report(date_str, papers):
    """Xây dựng nội dung README.md (tiếng Việt)."""
    lines = []
    lines.append("# Báo cáo distill arXiv — ngày %s" % date_str)
    lines.append("")
    lines.append("Tổng hợp %d bài paper đã distill hôm nay (10 bài tốt nhất được chọn từ scan arXiv)." % len(papers))
    lines.append("Mỗi bài đã qua 6 bước distill, bilingual (VI/EN), skill test (nếu đủ điều kiện), commit+push GitHub.")
    lines.append("")

    # Thống kê
    n_applied = sum(1 for p in papers if p["meta"].get("classification") == "applied")
    n_skill = sum(1 for p in papers if p["meta"].get("skill_status") == "created")
    lines.append("## Tổng quan")
    lines.append("- Tổng bài distill: **%d**" % len(papers))
    lines.append("- Nhãn [applied]: **%d**" % n_applied)
    lines.append("- Skill tạo được: **%d**" % n_skill)
    lines.append("")

    # Danh sách bài: mỗi bài có làm gì + học được gì
    lines.append("## Danh sách 10 bài hôm nay")
    lines.append("")
    for i, p in enumerate(papers, 1):
        meta = p["meta"]
        readme = read_readme(p["folder"])
        arxiv_id = meta.get("arxiv_id", "")
        insight = extract_insight_from_report(date_str, arxiv_id)
        lines.extend(build_paper_block_vn(i, meta, readme, insight))

    # Section áp dụng
    lines.append("## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN")
    lines.append("")
    lines.append("Dưới đây là những insight từ 10 bài hôm nay mà bạn — làm solopreneur content/AI tại Việt Nam — có thể **áp dụng ngay** mà không cần reproduce paper:")
    lines.append("")

    all_insights = []
    for p in papers:
        for ins in p.get("actionable_insights", []):
            all_insights.append(ins)

    if all_insights:
        seen = set()
        for ins in all_insights:
            key = ins.lower()
            if key in seen:
                continue
            seen.add(key)
            lines.append("- %s" % ins)
    else:
        lines.append("- (Không trích xuất được insight hành động từ README hôm nay.)")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Chi tiết từng bài (link folder)")
    for i, p in enumerate(papers, 1):
        meta = p["meta"]
        arxiv_id = meta.get("arxiv_id", "")
        name = meta.get("name", "")
        folder = p["folder"]
        rel = os.path.relpath(folder, REPO)
        lines.append("- [%d] %s — `%s` — xem chi tiết: `papers/%s/`" % (i, name, arxiv_id, rel))

    lines.append("")
    lines.append("*Báo cáo tự động sinh bởi daily_summary.py sau mỗi ngày distill 10 bài.*")
    return "\n".join(lines)


def build_report_en(date_str, papers):
    """Bản tiếng Anh (không giải thích thuật ngữ)."""
    lines = []
    lines.append("# arXiv Distill Daily Report — %s" % date_str)
    lines.append("")
    lines.append("Summary of %d papers distilled today (top 10 selected from arXiv scan)." % len(papers))
    lines.append("Each paper went through 6 distill steps, bilingual (VI/EN), skill test (if eligible), commit+push to GitHub.")
    lines.append("")

    n_applied = sum(1 for p in papers if p["meta"].get("classification") == "applied")
    n_skill = sum(1 for p in papers if p["meta"].get("skill_status") == "created")
    lines.append("## Overview")
    lines.append("- Total papers distilled: **%d**" % len(papers))
    lines.append("- Label [applied]: **%d**" % n_applied)
    lines.append("- Skills created: **%d**" % n_skill)
    lines.append("")

    lines.append("## Today's 10 papers")
    lines.append("")
    for i, p in enumerate(papers, 1):
        meta = p["meta"]
        readme = read_readme(p["folder"])
        arxiv_id = meta.get("arxiv_id", "")
        insight = extract_insight_from_report(date_str, arxiv_id)
        lines.extend(build_paper_block_en(i, meta, readme, insight))

    lines.append("## WHAT YOU CAN APPLY")
    lines.append("")
    lines.append("Below are insights from today's 10 papers that you — a solopreneur doing content/AI in Vietnam — can **apply right away** without reproducing the paper:")
    lines.append("")

    all_insights = []
    for p in papers:
        for ins in p.get("actionable_insights", []):
            all_insights.append(ins)

    if all_insights:
        seen = set()
        for ins in all_insights:
            key = ins.lower()
            if key in seen:
                continue
            seen.add(key)
            lines.append("- %s" % ins)
    else:
        lines.append("- (No actionable insights extracted from today's READMEs.)")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Details per paper (folder links)")
    for i, p in enumerate(papers, 1):
        meta = p["meta"]
        arxiv_id = meta.get("arxiv_id", "")
        name = meta.get("name", "")
        folder = p["folder"]
        rel = os.path.relpath(folder, REPO)
        lines.append("- [%d] %s — `%s` — details: `papers/%s/`" % (i, name, arxiv_id, rel))

    lines.append("")
    lines.append("*Auto-generated by daily_summary.py after each 10-paper distill day.*")
    return "\n".join(lines)


def extract_actionable_insights(readme_text):
    """Trích xuất section ## Actionable Insights từ README.md (tối đa 3 bullet)."""
    if not readme_text:
        return []
    m = re.search(r"## Actionable Insights\n(.*?)(?=\n## |\Z)", readme_text, re.S)
    if not m:
        return []
    block = m.group(1)
    bullets = re.findall(r"-\s*(.+?)(?=\n-|\n\Z)", block, re.S)
    out = []
    for b in bullets[:3]:
        b = " ".join(b.split())
        if b:
            out.append(b)
    return out


def send_telegram(text):
    """Gửi text qua Telegram nếu có env."""
    env_file = "/home/iamhtv/.hermes/profiles/research-arxiv/.env"
    env = {}
    if os.path.exists(env_file):
        for line in open(env_file):
            s = line.strip()
            if s and not s.startswith("#") and "=" in s:
                k, v = s.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    token = env.get("TELEGRAM_BOT_TOKEN")
    chat = env.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        print("  (Chưa setup TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID — bỏ qua gửi Telegram.)")
        return False

    import urllib.error
    import urllib.parse
    import urllib.request

    url = "https://api.telegram.org/bot%s/sendMessage" % token
    chunks, cur = [], ""
    for line in text.split("\n"):
        if len(cur) + len(line) + 1 > 3500:
            chunks.append(cur)
            cur = ""
        cur += line + "\n"
    if cur.strip():
        chunks.append(cur)

    ok_all = True
    for i, c in enumerate(chunks, 1):
        payload = {
            "chat_id": chat,
            "text": c,
            "disable_web_page_preview": "true",
        }
        data = urllib.parse.urlencode(payload).encode()
        req = urllib.request.Request(url, data=data)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                res = json.load(r)
            print("  Đã gửi Telegram phần %d/%d: ok=%s" % (i, len(chunks), res.get("ok")))
        except Exception as ex:
            print("  Lỗi gửi Telegram phần %d: %s" % (i, ex))
            ok_all = False
    return ok_all


def main():
    date_str = sys.argv[1] if len(sys.argv) > 1 else today_str()
    print("=== DAILY SUMMARY — ngày %s ===" % date_str)

    folders = list_today_papers(date_str)
    print("Tìm %d folder paper trong papers/%s/" % (len(folders), date_str.replace("-", "/")))

    # ── Lấy top 10 bài cao điểm nhất từ file scans/<ngày>.json (có llm_score) ──
    scan_path = os.path.join(SCANS_DIR, date_str + ".json")
    top10_ids = None
    if os.path.exists(scan_path):
        try:
            scan_data = json.load(open(scan_path, encoding="utf-8"))
            papers_scan = scan_data.get("papers", [])
            papers_scan.sort(key=lambda p: -p.get("llm_score", 0))
            top10_ids = [p["id"] for p in papers_scan[:10]]
            print("Lấy top 10 từ scans/%s.json (điểm LLM): %s" % (date_str, top10_ids))
        except Exception as e:
            print("Không đọc được scans/%s.json: %s" % (date_str, e))

    # Ánh xetch arxiv_id -> folder để match
    folder_by_id = {}
    for folder in folders:
        meta = read_meta(folder)
        aid = meta.get("arxiv_id", "")
        if aid:
            folder_by_id[aid] = folder

    # Chọn 10 folder: ưu tiên top10_ids, nếu thiếu thì bổ sung từ remaining
    selected_folders = []
    used_ids = set()
    if top10_ids:
        for aid in top10_ids:
            if aid in folder_by_id and aid not in used_ids:
                selected_folders.append(folder_by_id[aid])
                used_ids.add(aid)
        # Bổ sung nếu top10 không đủ 10 (vì một số bài chưa distill thành folder)
        for folder in folders:
            meta = read_meta(folder)
            aid = meta.get("arxiv_id", "")
            if aid and aid not in used_ids and len(selected_folders) < 10:
                selected_folders.append(folder)
                used_ids.add(aid)
    else:
        # Fallback: tất cả folder (sắp theo skill_status rồi tên)
        selected_folders = folders

    selected_folders = selected_folders[:10]
    print("Đã chọn %d bài cho báo cáo" % len(selected_folders))

    papers = []
    for folder in selected_folders:
        meta = read_meta(folder)
        readme = read_readme(folder)
        arxiv_id = meta.get("arxiv_id", "")
        insight = extract_insight_from_report(date_str, arxiv_id) if arxiv_id else ""
        actionable = extract_actionable_insights(readme)
        papers.append({
            "folder": folder,
            "meta": meta,
            "insight": insight,
            "actionable_insights": actionable,
        })

    # Sắp theo skill_status (created trước) rồi theo tên
    papers.sort(key=lambda p: (p["meta"].get("skill_status", "") != "created", p["meta"].get("name", "")))

    # Tạo báo cáo
    os.makedirs(SCANS_DIR, exist_ok=True)
    summary_dir = os.path.join(SCANS_DIR, date_str)
    os.makedirs(summary_dir, exist_ok=True)

    vi_path = os.path.join(summary_dir, "README.md")
    en_path = os.path.join(summary_dir, "README_en.md")

    vi_text = build_report(date_str, papers)
    en_text = build_report_en(date_str, papers)

    with open(vi_path, "w", encoding="utf-8") as f:
        f.write(vi_text)
    with open(en_path, "w", encoding="utf-8") as f:
        f.write(en_text)

    print("Đã ghi: %s" % vi_path)
    print("Đã ghi: %s" % en_path)

    # Gửi Telegram (bản tiếng Việt, tóm tắt gọn)
    send_telegram(vi_text)

    print("=== XONG ===")


if __name__ == "__main__":
    main()
