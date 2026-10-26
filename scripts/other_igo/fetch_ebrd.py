#!/usr/bin/env python3
"""EBRD ECEPP: download every 'Contract Award Notice' detail page listed on
https://ecepp.ebrd.com/delta/noticeSearch.html (the list page embeds all ~4 100 notices server-side).

Usage: python3 -I fetch_ebrd.py <out_dir>
Writes <out_dir>/noticeSearch.html, <out_dir>/award_list.json, <out_dir>/notices/<id>.html (checkpointed).
"""
import json, os, re, sys, time
import requests

H = {"User-Agent": "contracts-research/1.0"}
BASE = "https://ecepp.ebrd.com/delta/"


def main():
    out = sys.argv[1]
    os.makedirs(os.path.join(out, "notices"), exist_ok=True)
    retrieved = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    r = requests.get(BASE + "noticeSearch.html", headers=H, timeout=180)
    r.raise_for_status()
    with open(os.path.join(out, "noticeSearch.html"), "w", encoding="utf-8") as f:
        f.write(r.text)
    rows = re.findall(r'<tr>\s*<td><a href="viewNotice\.html\?displayNoticeId=(\d+)">(.*?)</a></td>(.*?)</tr>', r.text, re.S)
    awards = []
    for nid, title, rest in rows:
        tds = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', x)).strip() for x in re.findall(r'<td>(.*?)</td>', rest, re.S)]
        if tds and 'Award' in tds[0]:
            awards.append({"notice_id": nid, "title": title.strip(), "notice_type": tds[0], "exercise_title": tds[1] if len(tds) > 1 else None,
                           "published": tds[2] if len(tds) > 2 else None, "closing": tds[3] if len(tds) > 3 else None,
                           "state": tds[4] if len(tds) > 4 else None, "published_date": tds[5] if len(tds) > 5 else None,
                           "meta": tds[-1] if tds else None, "url": f"{BASE}viewNotice.html?displayNoticeId={nid}"})
    with open(os.path.join(out, "award_list.json"), "w", encoding="utf-8") as f:
        json.dump({"retrieved_at": retrieved, "list_url": BASE + "noticeSearch.html", "total_rows": len(rows), "award_notices": awards}, f, ensure_ascii=False, indent=0)
    print(f"{len(rows)} notices listed, {len(awards)} contract award notices", flush=True)
    todo = [a for a in awards if not os.path.exists(os.path.join(out, "notices", a["notice_id"] + ".html"))]
    print(f"{len(todo)} to fetch", flush=True)
    for k, a in enumerate(todo):
        for attempt in range(5):
            try:
                rr = requests.get(a["url"], headers=H, timeout=120)
                if rr.status_code == 200:
                    with open(os.path.join(out, "notices", a["notice_id"] + ".html"), "w", encoding="utf-8") as f:
                        f.write(rr.text)
                    break
                print("HTTP", rr.status_code, a["notice_id"], file=sys.stderr)
            except requests.RequestException as e:
                print("error", a["notice_id"], e, file=sys.stderr)
            time.sleep(3 * (attempt + 1))
        time.sleep(0.4)
        if (k + 1) % 100 == 0:
            print(f"{k+1}/{len(todo)}", flush=True)
    print("done")


if __name__ == "__main__":
    main()
