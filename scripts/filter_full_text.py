#!/usr/bin/env python3
"""
filter_full_text.py — Nâng cấp bước lọc: đọc full text PDF trước khi chọn top 10.

Input:  scans/<ngày>.json  (từ scan_arxiv.py, đã chấm abstract)
Output: scans/<ngày>_filtered.json  (top 10 bài chuẩn nhất sau khi đọc full text)

Quy trình:
1. Lấy top FULL_TEXT_N bài theo llm_score từ file scan (mặc định 40).
2. Tải PDF từng bài, trích xuất text bằng pdfminer.six.
3. Gọi LLM đánh giá lại dựa trên full text (tiêu chí: áp dụng thực tế,
   insight rõ ràng, phù hợp solopreneur VN).
4. Chọn top FINAL_N bài (mặc định 10) ghi ra file filtered.
"""

import datetime as dt
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCANS_DIR = os.path.join(REPO, "scans")
ENV_FILE = "/home/iamhtv/.hermes/profiles/research-arxiv/.env"

# ── Cấu hình ────────────────────────────────────────────────────────────────
FULL_TEXT_N = 40      # số bài đọc full text từ abstract ranking
FINAL_N = 10          # số bài cuối cùng giữ lại để distill
PDF_TIMEOUT = 60      # giây tải PDF
LLM_TIMEOUT = 90      # giây gọi LLM
SLEEP_BETWEEN = 2     # giây nghỉ giữa các lần gọi LLM (tránh rate limit)
# ────────────────────────────────────────────────────────────────────────────


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


def call_openrouter(prompt, key, max_tokens=1200):
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
        with urllib.request.urlopen(req, timeout=LLM_TIMEOUT) as r:
            d = json.load(r)
        msg = d["choices"][0]["message"]
        content = msg.get("content", "") or ""
        reasoning = msg.get("reasoning", "") or ""
        parts = []
        if reasoning.strip():
            parts.append(reasoning.strip())
        if content.strip() and content.strip() not in reasoning:
            parts.append(content.strip())
        return "\n".join(parts)
    except Exception as ex:
        print("  Lỗi gọi LLM: %s" % ex)
        return ""


def extract_pdf_text(pdf_url):
    """Tải PDF và trích xuất text bằng pdfminer.six. Trả về text hoặc rỗng."""
    # scan json lưu link = abs page (/abs/<id>) → chuyển thành PDF URL (/pdf/<id>)
    if "/abs/" in pdf_url:
        pdf_url = pdf_url.replace("/abs/", "/pdf/")
    try:
        req = urllib.request.Request(
            pdf_url,
            headers={"User-Agent": "arxiv-distill-research/1.0"},
        )
        with urllib.request.urlopen(req, timeout=PDF_TIMEOUT) as r:
            pdf_bytes = r.read()
    except Exception as ex:
        print("    (tải PDF lỗi: %s)" % ex)
        return ""

    if not pdf_bytes or pdf_bytes[:4] != b"%PDF":
        print("    (không phải PDF hợp lệ)")
        return ""

    # Ghi ra file tạm rồi gọi pdfminer qua /tmp/pdfenv nếu có
    tmp_pdf = "/tmp/filter_%s.pdf" % os.path.basename(pdf_url).replace("/", "_")
    tmp_txt = "/tmp/filter_%s.txt" % os.path.basename(pdf_url).replace("/", "_")
    try:
        with open(tmp_pdf, "wb") as f:
            f.write(pdf_bytes)
    except Exception as ex:
        print("    (ghi PDF tạm lỗi: %s)" % ex)
        return ""

    pdfenv_python = "/tmp/pdfenv/bin/python"
    extract_cmd = [
        pdfenv_python, "-c",
        "import sys, pdfminer.high_level; "
        "sys.stdout.write(pdfminer.high_level.extract_text(sys.argv[1]))",
        tmp_pdf,
    ]
    try:
        import subprocess
        res = subprocess.run(
            extract_cmd,
            capture_output=True, text=True, timeout=120,
        )
        text = res.stdout or ""
        if len(text) < 100:
            print("    (PDF trích xuất ít text: %d ký tự)" % len(text))
            return ""
        return text
    except Exception as ex:
        print("    (pdfminer lỗi: %s)" % ex)
        return ""
    finally:
        try:
            os.remove(tmp_pdf)
        except Exception:
            pass


def llm_rerank(name, arxiv_id, abstract, full_text, key):
    """Gọi LLM đánh giá lại bài dựa trên full text. Trả về điểm 0-100 + lý do."""
    # Cắt full text để không quá dài (LLM context hạn chế)
    text_preview = full_text[:6000] if full_text else "(không đọc được full text)"
    abs_preview = abstract[:1200] if abstract else ""

    prompt = (
        "Bạn là chuyên gia lọc paper AI cho solopreneur Việt Nam (content, bán hàng, "
        "chăm sóc khách hàng, quản lý thời gian).\n\n"
        "Tên paper: %s (arXiv %s)\n"
        "Abstract: %s\n\n"
        "Full text (cắt 6.000 ký tự đầu):\n%s\n\n"
        "Hãy đánh giá lại bài này theo 3 tiêu chí, mỗi tiêu chí 0-40 điểm (tổng 0-120):\n"
        "1. Ứng dụng thực tiễn cho business/content/AI (có experiment, dataset, benchmark thật?)\n"
        "2. Insight hành động được (đọc xong làm được ngay mà không cần reproduce?)\n"
        "3. Phù hợp solopreneur Việt Nam (ít tài nguyên, cần kết quả nhanh, không cần 팀 lớn?)\n\n"
        "Trả về DUY NHẤT JSON:\n"
        "{\"score\": <0-120>, \"reason\": \"<1 câu lý do>\", \"verdict\": \"<KEEP/DROP>\"}\n"
        "Nếu không đọc được full text hoặc bài lý thuyết thuần, teoría toán, y học, hoá học → verdict DROP.\n"
    ) % (name, arxiv_id, abs_preview, text_preview)

    raw = call_openrouter(prompt, key, max_tokens=800)
    if not raw:
        return -1, "LLM lỗi", "DROP"

    # Parse JSON
    try:
        m = re.search(r"\{.*\}", raw, re.S)
        if not m:
            return -1, "JSON parse lỗi", "DROP"
        j = json.loads(m.group(0))
        score = int(j.get("score", 0))
        reason = j.get("reason", "")
        verdict = j.get("verdict", "DROP")
        return score, reason, verdict
    except Exception:
        return -1, "JSON parse lỗi", "DROP"


def main():
    date_str = sys.argv[1] if len(sys.argv) > 1 else today_str()
    print("=== FILTER FULL TEXT — ngày %s ===" % date_str)

    scan_path = os.path.join(SCANS_DIR, date_str + ".json")
    if not os.path.exists(scan_path):
        print("LỖI: Không tìm thấy %s" % scan_path)
        sys.exit(1)

    scan = json.load(open(scan_path, encoding="utf-8"))
    papers = scan.get("papers", [])
    if not papers:
        print("File scan rỗng.")
        sys.exit(1)

    # Sắp theo llm_score giảm dần, lấy top FULL_TEXT_N
    papers.sort(key=lambda p: -p.get("llm_score", 0))
    candidates = papers[:FULL_TEXT_N]
    print("Tổng %d bài trong scan, chọn top %d đọc full text" % (len(papers), len(candidates)))

    env = load_env()
    key = env.get("OPENROUTER_API_KEY")
    if not key:
        print("LỖI: Không tìm thấy OPENROUTER_API_KEY")
        sys.exit(1)

    filtered = []
    for idx, p in enumerate(candidates, 1):
        arxiv_id = p.get("id", "")
        name = p.get("title", "(không có tên)")
        abstract = p.get("abstract", "")
        link_pdf = p.get("link", "")

        print("  [%d/%d] %s ..." % (idx, len(candidates), arxiv_id))

        # Đọc full text
        full_text = ""
        if link_pdf:
            full_text = extract_pdf_text(link_pdf)

        # LLM đánh giá lại
        score, reason, verdict = llm_rerank(name, arxiv_id, abstract, full_text, key)

        p["full_text_score"] = score
        p["full_text_reason"] = reason
        p["full_text_verdict"] = verdict
        p["has_full_text"] = bool(full_text)

        if verdict == "KEEP" and score >= 0:
            filtered.append(p)

        # Nghỉ giữa các lần gọi LLM
        if idx < len(candidates):
            time.sleep(SLEEP_BETWEEN)

    # Sắp theo full_text_score giảm dần, giữ top FINAL_N
    filtered.sort(key=lambda p: -p.get("full_text_score", 0))
    final = filtered[:FINAL_N]

    print("Đã chọn %d bài KEEP, giữ top %d" % (len(filtered), len(final)))

    # Ghi file filtered
    out = {
        "date": date_str,
        "source_scan": scan_path,
        "total_in_scan": len(papers),
        "full_text_candidates": len(candidates),
        "kept_count": len(filtered),
        "final_count": len(final),
        "papers": final,
    }
    out_path = os.path.join(SCANS_DIR, date_str + "_filtered.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("Đã ghi: %s" % out_path)
    print("=== XONG ===")


if __name__ == "__main__":
    main()
