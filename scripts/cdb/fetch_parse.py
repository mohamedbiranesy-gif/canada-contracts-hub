#!/usr/bin/env python3
"""Caribbean Development Bank contract awards listing -> rows; keep winning bids prefixed 'Canada - '."""
import re, html, json, time, urllib.request, datetime, os, sys
UA = {"User-Agent": "contracts-research/1.0"}
BASE = "https://www.caribank.org/work-with-us/procurement/contract-awards"
dl = "downloads/cdb"; os.makedirs(dl, exist_ok=True)
log = open(dl + "/fetch.log", "a")
rows = []
def cell(td): return html.unescape(re.sub(r"\s+", " ", re.sub(r"<br\s*/?>", " | ", re.sub(r"<(?!br)[^>]+>", " ", td)))).strip()
for year in range(2026, 2011, -1):
    for page in range(0, 40):
        url = "%s?solr_publication_contract_awards_years_filter=%d&page=%d" % (BASE, year, page)
        fn = "%s/awards_%d_p%02d.html" % (dl, year, page)
        if os.path.exists(fn): s = open(fn, encoding="utf-8").read()
        else:
            try:
                s = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode("utf-8", "replace")
            except Exception as e:
                log.write("%s ERR %s %s\n" % (time.strftime("%FT%TZ", time.gmtime()), url, e)); break
            open(fn, "w", encoding="utf-8").write(s); time.sleep(0.7)
        tb = re.search(r"<tbody>(.*?)</tbody>", s, re.S)
        trs = re.findall(r"<tr>(.*?)</tr>", tb.group(1), re.S) if tb else []
        log.write("%s %s rows=%d\n" % (time.strftime("%FT%TZ", time.gmtime()), url, len(trs)))
        if not trs: break
        for tr in trs:
            tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
            if len(tds) < 5: continue
            link = re.search(r'href="([^"]+)"', tds[0])
            rows.append({"year_filter": year, "page": page, "listing_url": url, "project_name": cell(tds[0]), "document_url": ("https://www.caribank.org" + link.group(1)) if link and link.group(1).startswith("/") else (link.group(1) if link else None),
                         "sectors_themes": cell(tds[1]), "country": cell(tds[2]), "type": cell(tds[3]), "winning_bid": cell(tds[4])})
        if len(trs) < 10 and page > 0: break
json.dump(rows, open(dl + "/rows.json", "w"), ensure_ascii=False, indent=0)
print(len(rows), sum(1 for r in rows if re.match(r"\s*Canada\s*-", r["winning_bid"], re.I)))
