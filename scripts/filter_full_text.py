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
import subprocess
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
    # Dùng curl thay urllib: urlopen có thể hang vô hạn trên connection
    # stalled (Cloudflare keepalive) dù đã set timeout — bài học 2026-10-24.
    try:
        res = subprocess.run(
            ["curl", "-sS", "--max-time", str(LLM_TIMEOUT), "--retry", "1",
             "-X", "POST", "https://openrouter.ai/api/v1/chat/completions",
             "-H", "Authorization: Bearer " + key,
             "-H", "Content-Type: application/json",
             "-d", "@-"],
            input=body, capture_output=True, timeout=LLM_TIMEOUT + 30,
        )
        d = json.loads((res.stdout or b"").decode("utf-8", "replace"))
    except Exception as ex:
        print("  Lỗi gọi LLM (curl): %s" % ex)
        return ""
    try:
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
    tmp_pdf = "/tmp/filter_%s.pdf" % os.path.basename(pdf_url).replace("/", "_")
    tmp_txt = "/tmp/filter_%s.txt" % os.path.basename(pdf_url).replace("/", "_")
    # Dùng curl thay urllib: arxiv hay throttle/stall connection, urllib hang
    # không timeout được socket-read. curl --retry + --max-time 180 (pitfall 19).
    try:
        for f in (tmp_pdf, tmp_txt):
            try:
                os.remove(f)
            except OSError:
                pass
        curl_cmd = [
            "curl", "-sL", "--max-time", "180", "--retry", "2",
            "--retry-delay", "3", "-A", "arxiv-distill-research/1.0",
            "-o", tmp_pdf, pdf_url,
        ]
        subprocess.run(curl_cmd, capture_output=True, timeout=200)
    except Exception as ex:
        print("    (curl lỗi: %s)" % ex)
        return ""
    try:
        with open(tmp_pdf, "rb") as f:
            head = f.read(5)
        if head[:4] != b"%PDF":
            print("    (không phải PDF hợp lệ — arxiv trả HTML/403?)")
            return ""
    except Exception:
        return ""
    pdfenv_python = "/tmp/pdfenv/bin/python"
    extract_cmd = [
        pdfenv_python, "-c",
        "import sys, pdfminer.high_level; "
        "sys.stdout.write(pdfminer.high_level.extract_text(sys.argv[1]))",
        tmp_pdf,
    ]
    try:
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
    """Gọi LLM đánh giá lại bài dựa trên full text. Trả về điểm 0-120 + lý do."""
    # Cắt full text để không quá dài (LLM context hạn chế)
    text_preview = full_text[:6000] if full_text else "(không đọc được full text)"
    abs_preview = abstract[:1200] if abstract else ""

    prompt = (
        "Bạn là chuyên gia lọc paper AI cho solopreneur Việt Nam (content, bán hàng, "
        "chăm sóc khách hàng, quản lý thời gian).\n\n"
        "Tên paper: %s (arXiv %s)\n"
        "Abstract: %s\n\n"
        "Full text (cắt 6.000 ký tự đầu):\n%s\n\n"
        "Đánh giá bài này theo 3 tiêu chí, mỗi tiêu chí 0-40 điểm (tổng 0-120):\n"
        "1. Ứng dụng thực tiễn cho business/content/AI (có experiment, dataset, benchmark thật?)\n"
        "2. Insight hành động được (đọc xong làm được ngay mà không cần reproduce?)\n"
        "3. Phù hợp solopreneur Việt Nam (ít tài nguyên, cần kết quả nhanh, không cần nhóm lớn?)\n\n"
        "QUY TẮC OUTPUT BẮT BUỘC: Trả về DUY NHẤT 1 dòng JSON, KHÔNG có lời giải thích, "
        "KHÔNG có text nào khác trước hoặc sau:\n"
        "{\"score\": <0-120>, \"reason\": \"<1 câu lý do>\", \"verdict\": \"<KEEP/DROP>\"}\n"
        "KEEP nếu bài có thí nghiệm/benchmark thật VÀ rút ra được insight dùng được. "
        "DROP nếu không đọc được full text, hoặc bài lý thuyết thuần, lý thuyết toán, y học, hoá học.\n"
    ) % (name, arxiv_id, abs_preview, text_preview)

    raw = call_openrouter(prompt, key, max_tokens=2000)
    if not raw:
        return -1, "LLM lỗi", "DROP"

    # Parse robust: thử mọi block {...} KHÔNG lồng nhau, từ CUỐI về ĐẦU,
    # lấy block đầu tiên có field "verdict" (model hay thải prose trước JSON).
    import re as _re
    for cand in reversed(_re.findall(r"\{[^{}]*\}", raw, _re.S)):
        try:
            j = json.loads(cand)
        except Exception:
            continue
        if isinstance(j, dict) and "verdict" in j:
            try:
                score = int(j.get("score", 0))
            except Exception:
                score = -1
            reason = str(j.get("reason", ""))[:200]
            verdict = str(j.get("verdict", "DROP"))[:10].upper()
            return score, reason, verdict
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
        print("      full_text=%d ký tự → score=%s verdict=%s | %s" % (len(full_text), score, verdict, reason[:100]))

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
    all_evals = [
        {
            "id": p.get("id", ""),
            "title": p.get("title", ""),
            "llm_score": p.get("llm_score", -1),
            "full_text_score": p.get("full_text_score", -1),
            "full_text_verdict": p.get("full_text_verdict", "DROP"),
            "full_text_reason": p.get("full_text_reason", ""),
            "has_full_text": p.get("has_full_text", False),
        }
        for p in candidates
    ]
    out = {
        "date": date_str,
        "source_scan": scan_path,
        "total_in_scan": len(papers),
        "full_text_candidates": len(candidates),
        "kept_count": len(filtered),
        "final_count": len(final),
        "papers": final,
        "all_evaluations": all_evals,
    }
    out_path = os.path.join(SCANS_DIR, date_str + "_filtered.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("Đã ghi: %s" % out_path)
    print("=== XONG ===")


if __name__ == "__main__":
    main()
