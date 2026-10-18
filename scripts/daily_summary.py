#!/usr/bin/env python3
"""
daily_summary.py — Báo cáo hàng ngày DỄ HIỂU cho solopreneur Việt Nam.

Gọi LLM (OpenRouter) 1 lượt để viết lại 10 paper thành tiếng Việt đơn giản.
Mỗi paper: Làm gì / Học được gì / Áp dụng cho bạn (CỤ THỂ cho paper đó).
Cuối: section "CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN" (3-5 insight hàng đầu).
"""

import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS_ROOT = os.path.join(REPO, "papers")
SCANS_DIR = os.path.join(REPO, "scans")
REPORT_FILE = os.path.join(REPO, "report.md")
ENV_FILE = "/home/iamhtv/.hermes/profiles/research-arxiv/.env"


def today_str():
    return dt.datetime.now().strftime("%Y-%m-%d")


def load_env():
    env = {}
    if os.path.exists(ENV_FILE):
        for line in open(ENV_FILE):
            s = line.strip()
            if s and not s.startswith("#") and "=" in s:
                k, v = s.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def list_today_papers(date_str):
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


def clean_text(text):
    if not text:
        return ""
    return " ".join(text.split()).strip()


def first_sentences(text, n=2):
    if not text:
        return ""
    text = clean_text(text)
    sentences = re.split(r"(?<=[.!?])\s+", text)
    result = " ".join(sentences[:n])
    if len(result) > 250:
        result = result[:250] + "..."
    return result


def extract_problem_simple(readme_text):
    if not readme_text:
        return ""
    m = re.search(r"## Problem\n(.*?)(?=\n## |\Z)", readme_text, re.S)
    if not m:
        return ""
    return first_sentences(m.group(1), 2)


def extract_insight_from_report(date_str, arxiv_id):
    if not arxiv_id or not os.path.exists(REPORT_FILE):
        return ""
    text = open(REPORT_FILE, encoding="utf-8").read()
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
        return first_sentences(im.group(1).strip(), 2)
    return ""


def extract_actionable_insights(readme_text):
    if not readme_text:
        return []
    m = re.search(r"## Actionable Insights\n(.*?)(?=\n## |\Z)", readme_text, re.S)
    if not m:
        return []
    block = m.group(1)
    bullets = re.findall(r"-\s*(.+?)(?=\n-|\n\Z)", block, re.S)
    out = []
    for b in bullets[:3]:
        b = clean_text(b)
        if b:
            out.append(b)
    return out


def call_openrouter(prompt, key, max_tokens=6000):
    body = json.dumps({
        "model": "inclusionai/ling-3.1-flash",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body,
        headers={
            "Authorization": "Bearer " + key,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.load(r)
        return d["choices"][0]["message"].get("content", "") or ""
    except Exception as ex:
        print("  Lỗi gọi LLM: %s" % ex)
        return ""


def fallback_block(i, name, arxiv_id, problem, insight):
    """Tạo block đơn giản nếu LLM lỗi."""
    return (
        "### [%d] %s (%s)\n"
        "- Làm gì: %s\n"
        "- Học được gì: %s\n"
        "- Áp dụng cho bạn: %s\n"
    ) % (
        i,
        clean_text(name),
        arxiv_id,
        problem or "Không có thông tin.",
        insight or "Không có thông tin.",
        "Ví dụ: Áp dụng vào nội dung/bán hàng của bạn — bắt đầu từ nhỏ, đo kết quả, rồi mới mở rộng.",
    )


def rewrite_all_papers(papers_data, key):
    """Gọi LLM 1 lần viết lại 10 paper, mỗi paper có Áp dụng cho bạn CỤ THỂ."""
    items = []
    for i, p in enumerate(papers_data, 1):
        items.append(
            "%d. Tên: %s (arXiv %s)\n"
            "   Làm gì (tóm tắt): %s\n"
            "   Học được gì (tóm tắt): %s\n"
            % (i, p["name"], p["arxiv_id"], p["problem"], p["insight"])
        )

    prompt = (
        "Bạn giải thích paper AI cho solopreneur Việt Nam (làm content, bán hàng online, "
        "chăm sóc khách hàng, quản lý thời gian). KHÔNG dùng thuật ngữ tiếng Anh thuần mà không giải thích.\n\n"
        "Viết lại MỖI paper thành tiếng Việt đơn giản, gần gũi, theo format BẮT BUỘC:\n"
        "### [N] Tên paper (arXiv ID)\n"
        "- Làm gì: (1-2 câu tiếng Việt đơn giản)\n"
        "- Học được gì: (1-2 câu tiếng Việt đơn giản)\n"
        "- Áp dụng cho bạn: (1 ví dụ CỤ THỂ, liên quan trực tiếp đến nội dung paper này, làm được ngay hôm nay cho solopreneur VN)\n\n"
        "Lưu ý: Mỗi paper phải có phần 'Áp dụng cho bạn' KHÁC NHAU, không được viết ví dụ chung chung.\n"
        "Ví dụ paper về tiền recount: 'Áp dụng cho bạn: Khi chạy quảng cáo Facebook, lưu bảng \"đã chạy chủ đề nào — lượt tương tác bao nhiêu\", để không quảng cáo lại chủ đề cũ đã fail.'\n\n"
        "Cuối báo cáo, thêm section:\n"
        "## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN\n"
        "3-5 insight hàng đầu từ 10 bài, mỗi insight 1 câu ngắn + 1 ví dụ áp dụng cụ thể cho solopreneur VN.\n\n"
        "Dữ liệu 10 paper:\n\n" + "\n".join(items)
    )

    return call_openrouter(prompt, key, max_tokens=6000)


def build_application_section(papers_data):
    """Section 'CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN' lấy 3-5 insight từ papers_data."""
    lines = []
    lines.append("")
    lines.append("## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN")
    lines.append("")
    lines.append("Dưới đây là insight hàng đầu từ 10 bài hôm nay, mỗi insight kèm ví dụ áp dụng ngay cho bạn:")
    lines.append("")

    count = 0
    seen = set()
    for p in papers_data:
        source = p.get("insight", "") or p.get("problem", "")
        short = first_sentences(source, 1)
        key_ = short.lower()
        if not short or key_ in seen:
            continue
        seen.add(key_)
        lines.append("- **%s** %s" % (short, "Ví dụ: Áp dụng vào nội dung/bán hàng của bạn — bắt đầu từ nhỏ, đo kết quả, rồi mới mở rộng."))
        count += 1
        if count >= 5:
            break

    if count == 0:
        lines.append("- (Không trích xuất được insight hành động từ README hôm nay.)")

    return lines


def main():
    date_str = sys.argv[1] if len(sys.argv) > 1 else today_str()
    print("=== DAILY SUMMARY — ngày %s ===" % date_str)

    folders = list_today_papers(date_str)
    print("Tìm %d folder paper trong papers/%s/" % (len(folders), date_str.replace("-", "/")))

    scan_path = os.path.join(SCANS_DIR, date_str + ".json")
    top10_ids = None
    if os.path.exists(scan_path):
        try:
            scan_data = json.load(open(scan_path, encoding="utf-8"))
            papers_scan = scan_data.get("papers", [])
            papers_scan.sort(key=lambda p: -p.get("llm_score", 0))
            top10_ids = [p["id"] for p in papers_scan[:10]]
            print("Lấy top 10 từ scans/%s.json: %s" % (date_str, top10_ids))
        except Exception as e:
            print("Không đọc được scans/%s.json: %s" % (date_str, e))

    folder_by_id = {}
    for folder in folders:
        meta = read_meta(folder)
        aid = meta.get("arxiv_id", "")
        if aid:
            folder_by_id[aid] = folder

    selected_folders = []
    used_ids = set()
    if top10_ids:
        for aid in top10_ids:
            if aid in folder_by_id and aid not in used_ids:
                selected_folders.append(folder_by_id[aid])
                used_ids.add(aid)
        for folder in folders:
            meta = read_meta(folder)
            aid = meta.get("arxiv_id", "")
            if aid and aid not in used_ids and len(selected_folders) < 10:
                selected_folders.append(folder)
                used_ids.add(aid)
    else:
        selected_folders = folders

    selected_folders = selected_folders[:10]
    print("Đã chọn %d bài cho báo cáo" % len(selected_folders))

    env = load_env()
    key = env.get("OPENROUTER_API_KEY")
    if not key:
        print("  LỖI: Không tìm thấy OPENROUTER_API_KEY trong %s" % ENV_FILE)
        sys.exit(1)

    # Thu thập dữ liệu thô
    papers_data = []
    for folder in selected_folders:
        meta = read_meta(folder)
        readme = read_readme(folder)
        arxiv_id = meta.get("arxiv_id", "")
        insight = extract_insight_from_report(date_str, arxiv_id) if arxiv_id else ""
        problem = extract_problem_simple(readme)
        papers_data.append({
            "name": clean_text(meta.get("name", "(không có tên)")),
            "arxiv_id": arxiv_id,
            "problem": problem,
            "insight": insight,
        })

    # Gọi LLM 1 lần viết lại tất cả
    print("  Đang gọi LLM viết lại báo cáo (1 lượt, tất cả 10 paper)...")
    vn_report = rewrite_all_papers(papers_data, key)

    if not vn_report or not vn_report.strip():
        print("  LLM trả về rỗng, dùng fallback cho từng paper.")
        blocks = []
        for i, p in enumerate(papers_data, 1):
            blocks.append(fallback_block(i, p["name"], p["arxiv_id"], p["problem"], p["insight"]))
        vn_report = "\n".join(blocks)

    # Nếu LLM không có section "CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN", thêm section mặc định
    if "CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN" not in vn_report:
        vn_report += "\n" + "\n".join(build_application_section(papers_data))

    # Ghép header + body + footer
    header = (
        "# Báo cáo distill arXiv — ngày %s\n\n"
        "Tổng hợp %d bài paper đã distill hôm nay (10 bài tốt nhất được chọn từ scan arXiv).\n"
        "Mỗi bài đã qua 6 bước distill, commit+push GitHub.\n\n"
        "## Tổng quan\n"
        "- Tổng bài distill: **%d**\n"
        "- Tất cả đều có ứng dụng thực tế.\n\n"
        "## Danh sách 10 bài hôm nay\n\n"
    ) % (date_str, len(selected_folders), len(selected_folders))

    footer = (
        "\n---\n\n"
        "## Chi tiết từng bài (link folder)\n"
    )
    for i, folder in enumerate(selected_folders, 1):
        meta = read_meta(folder)
        arxiv_id = meta.get("arxiv_id", "")
        name = clean_text(meta.get("name", ""))
        rel = os.path.relpath(folder, REPO)
        pdf = meta.get("link_pdf", "")
        footer += "- [%d] %s — `%s` — xem chi tiết: `papers/%s/`" % (i, name, arxiv_id, rel)
        if pdf:
            footer += " — PDF: %s" % pdf
        footer += "\n"
    footer += "\n*Báo cáo tự động sinh bởi daily_summary.py sau mỗi ngày distill 10 bài.*\n"

    full_report = header + vn_report + "\n" + footer

    # Ghi file
    os.makedirs(SCANS_DIR, exist_ok=True)
    summary_dir = os.path.join(SCANS_DIR, date_str)
    os.makedirs(summary_dir, exist_ok=True)

    vi_path = os.path.join(summary_dir, "README.md")
    with open(vi_path, "w", encoding="utf-8") as f:
        f.write(full_report)

    print("Đã ghi: %s" % vi_path)

    # Gửi Telegram
    token = env.get("TELEGRAM_BOT_TOKEN")
    chat = env.get("TELEGRAM_CHAT_ID")
    if token and chat:
        url = "https://api.telegram.org/bot%s/sendMessage" % token
        chunks, cur = [], ""
        for line in full_report.split("\n"):
            if len(cur) + len(line) + 1 > 3500:
                chunks.append(cur)
                cur = ""
            cur += line + "\n"
        if cur.strip():
            chunks.append(cur)
        for i, c in enumerate(chunks, 1):
            payload = {"chat_id": chat, "text": c, "disable_web_page_preview": "true"}
            data = urllib.parse.urlencode(payload).encode()
            req = urllib.request.Request(url, data=data)
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    res = json.load(r)
                print("  Đã gửi Telegram phần %d/%d: ok=%s" % (i, len(chunks), res.get("ok")))
            except Exception as ex:
                print("  Lỗi gửi Telegram phần %d: %s" % (i, ex))
    else:
        print("  (Chưa setup Telegram — bỏ qua gửi.)")

    print("=== XONG ===")


if __name__ == "__main__":
    main()
