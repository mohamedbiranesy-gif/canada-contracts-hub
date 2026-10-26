#!/usr/bin/env python3
"""Crawl UNGM public contract awards whose supplier country is Canada.

1. GET https://www.ungm.org/Public/ContractAward -> anti-forgery token (hidden input + cookie)
2. POST https://www.ungm.org/Public/ContractAward/PublicSearch (JSON body as built by UNGM.ContractAwardSearch.buildOptions
   in /bundles/ungmcommon) with SupplierCountries=["2328"] (option value of "Canada" in #selContractAwardSupplierCountry),
   PageSize 15 (server-side page size; larger values are tested), paging PageIndex until no .dataRow is returned.
3. GET https://www.ungm.org/Public/ContractAward/<id> for every award (full detail HTML saved) and the Popup variant.

Checkpointed: list pages saved to <out>/search_pages/, details to <out>/details/<id>.html; existing files are skipped.
Usage: python3 -I fetch_ungm.py <out_dir> [page_size]
"""
import json, os, re, sys, time
import requests

H = {"User-Agent": "contracts-research/1.0"}
BASE = "https://www.ungm.org"


def session_with_token():
    s = requests.Session()
    s.headers.update(H)
    r = s.get(BASE + "/Public/ContractAward", timeout=60)
    r.raise_for_status()
    tok = re.search(r'name="__RequestVerificationToken" type="hidden" value="([^"]+)"', r.text).group(1)
    return s, tok, r.text


def main():
    out = sys.argv[1]
    page_size = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    os.makedirs(os.path.join(out, "search_pages"), exist_ok=True)
    os.makedirs(os.path.join(out, "details"), exist_ok=True)
    s, tok, page_html = session_with_token()
    with open(os.path.join(out, "ContractAward_page.html"), "w", encoding="utf-8") as f:
        f.write(page_html)
    retrieved = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    ids = []
    rows_meta = {}
    page = 0
    while True:
        opts = {"PageIndex": page, "PageSize": page_size, "Title": "", "Description": "", "Reference": "", "Supplier": "", "UngmNumber": "",
                "AwardFrom": "", "AwardTo": "", "Countries": [], "SupplierCountries": ["2328"], "Agencies": [], "UNSPSCs": [],
                "SortField": "AwardDate", "SortAscending": False}
        for attempt in range(5):
            try:
                r = s.post(BASE + "/Public/ContractAward/PublicSearch", json=opts,
                           headers={"RequestVerificationToken": tok, "Content-Type": "application/json", "X-Requested-With": "XMLHttpRequest"}, timeout=90)
                if r.status_code == 200:
                    break
                print("HTTP", r.status_code, "page", page, file=sys.stderr)
            except requests.RequestException as e:
                print("error", e, file=sys.stderr)
            time.sleep(2 * (attempt + 1))
            if attempt == 2:
                s, tok, _ = session_with_token()
        else:
            print("giving up on page", page, file=sys.stderr)
            break
        html = r.text
        with open(os.path.join(out, "search_pages", f"page_{page:04d}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        found = re.findall(r'data-contractawardid="(\d+)"', html)
        if not found:
            break
        # per-row summary (title, supplier, award date, agency, reference, destinations)
        for block in re.split(r'(?=<div role="row" tabindex="0" data-contractawardid=)', html):
            m = re.search(r'data-contractawardid="(\d+)"', block)
            if not m:
                continue
            cells = re.findall(r'<span>\s*(.*?)\s*</span>', block, re.S)
            title = re.search(r'ungm-title--small">\s*(.*?)\s*</span>', block, re.S)
            rows_meta[m.group(1)] = {"title_html": title.group(1).strip() if title else None, "cells_html": [c.strip() for c in cells], "page_index": page}
        ids += found
        page += 1
        if page % 20 == 0:
            print(f"page {page}, ids {len(ids)}", flush=True)
        time.sleep(0.4)
    ids_u = list(dict.fromkeys(ids))
    with open(os.path.join(out, "search_summary.json"), "w", encoding="utf-8") as f:
        json.dump({"retrieved_at": retrieved, "pages": page, "page_size": page_size, "ids": ids_u, "rows": rows_meta,
                   "request": {"url": BASE + "/Public/ContractAward/PublicSearch", "body_template": opts}}, f, ensure_ascii=False)
    print(f"{len(ids_u)} award ids over {page} pages", flush=True)
    # details
    todo = [i for i in ids_u if not os.path.exists(os.path.join(out, "details", f"{i}.html"))]
    print(f"{len(todo)} details to fetch", flush=True)
    for k, i in enumerate(todo):
        for attempt in range(8):
            try:
                r = s.get(f"{BASE}/Public/ContractAward/{i}", timeout=90)
                if r.status_code == 200:
                    with open(os.path.join(out, "details", f"{i}.html"), "w", encoding="utf-8") as f:
                        f.write(r.text)
                    break
                print("detail HTTP", r.status_code, i, "retry-after", r.headers.get("Retry-After"), file=sys.stderr)
                if r.status_code == 429:
                    ra = r.headers.get("Retry-After")
                    time.sleep(float(ra) if ra and ra.isdigit() else 15 * (attempt + 1))
                    continue
            except requests.RequestException as e:
                print("detail error", i, e, file=sys.stderr)
            time.sleep(3 * (attempt + 1))
        time.sleep(2.5)  # UNGM throttles detail pages (HTTP 429) above ~0.5 req/s
        if (k + 1) % 50 == 0:
            print(f"details {k+1}/{len(todo)}", flush=True)
    print("done")


if __name__ == "__main__":
    main()
