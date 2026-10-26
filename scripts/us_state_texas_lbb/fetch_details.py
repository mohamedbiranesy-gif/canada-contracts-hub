#!/usr/bin/env python3
"""Fetch LBB CMS public detail pages (vendor address block) for selected contracts.
usage: python3 -I fetch_details.py <lbb_download_csv> <out_dir> <vendor_id_prefix>
Fetches https://cms.lbb.texas.gov/Default.aspx?aid=<aid>&cid=<cid> (redirects to Public/SearchedList.aspx) for rows whose
Vendor ID starts with <prefix>; saves HTML per contract and a parsed JSONL of the Vendor block. Resumable.
"""
import sys, csv, re, os, json, time, html, urllib.request, urllib.parse, http.cookiejar

UA = "contracts-research/1.0"


def text_of(s):
    t = re.sub(r"<script.*?</script>", "", s, flags=re.S)
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return html.unescape(re.sub(r"\s+", " ", t))


def parse_vendor(htm):
    """Extract vendor table cells from the detail page."""
    out = {}
    # the vendor block is a table following the text 'Vendor:'; parse all tables and find one whose header has 'Vendor ID'
    tables = re.findall(r"<table.*?</table>", htm, flags=re.S)
    for tb in tables:
        if "Vendor ID" in tb and "Postal Code" in tb:
            rows = re.findall(r"<tr.*?</tr>", tb, flags=re.S)
            cells = [[text_of(c).strip() for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, flags=re.S)] for r in rows]
            cells = [c for c in cells if c]
            if len(cells) >= 2:
                hdr = cells[0]
                for data in cells[1:]:
                    if len(data) == len(hdr):
                        out = dict(zip(hdr, data))
                        break
            if out:
                break
    # summary block
    m = re.search(r"Completion Date.*?Competitively Procured\?\s*(.*?)\s*Vendor:", text_of(htm), flags=re.S)
    if m:
        out["_summary_line"] = m.group(1)[:600]
    return out


def main():
    path, out_dir, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(os.path.join(out_dir, "html"), exist_ok=True)
    parsed_path = os.path.join(out_dir, f"details_prefix{prefix}.jsonl")
    done = set()
    if os.path.exists(parsed_path):
        for line in open(parsed_path, encoding="utf-8"):
            try:
                done.add(json.loads(line)["cid"])
            except Exception:
                pass
    log = open(os.path.join(out_dir, "fetch.log"), "a")
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [("User-Agent", UA)]
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
    todo = [r for r in rows if r["Vendor ID"].strip('"').startswith(prefix)]
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} START prefix={prefix} todo={len(todo)} done={len(done)}\n"); log.flush()
    with open(parsed_path, "a", encoding="utf-8") as fo:
        for i, r in enumerate(todo):
            m = re.search(r"href='([^']+)'", r["Contract-ID"])
            if not m:
                continue
            url = m.group(1)
            q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
            aid, cid = q.get("aid", [""])[0], q.get("cid", [""])[0]
            if cid in done:
                continue
            htm = None
            for attempt in range(4):
                try:
                    with opener.open(url, timeout=120) as resp:
                        htm = resp.read().decode("utf-8", errors="replace")
                        final = resp.geturl()
                    break
                except Exception as e:
                    log.write(f"retry {attempt} {cid} {e}\n"); log.flush()
                    time.sleep(3 * (attempt + 1))
            if htm is None:
                continue
            fn = os.path.join(out_dir, "html", re.sub(r"[^A-Za-z0-9_.-]", "_", f"{aid}_{cid}") + ".html")
            open(fn, "w", encoding="utf-8").write(htm)
            v = parse_vendor(htm)
            rec = {"aid": aid, "cid": cid, "url": url, "final_url": final, "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                   "vendor_block": v, "csv_row": r}
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); fo.flush()
            done.add(cid)
            if (i + 1) % 25 == 0:
                log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {i+1}/{len(todo)}\n"); log.flush()
            time.sleep(0.4)
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} DONE\n"); log.close()


if __name__ == "__main__":
    main()
