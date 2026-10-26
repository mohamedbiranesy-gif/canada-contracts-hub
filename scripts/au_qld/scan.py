#!/usr/bin/env python3
"""Queensland contract disclosure reports (data.qld.gov.au CKAN): stream every CSV/XLSX resource, keep rows whose
supplier address/country columns contain 'Canada' or a Canadian postal code. Only matching rows + per-file metadata stored."""
import json, urllib.request, urllib.parse, time, re, csv, io, sys, os
UA = {"User-Agent": "contracts-research/1.0"}
dl = "downloads/au_qld"
PC = re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z] ?\d[ABCEGHJ-NPRSTV-Z]\d\b")
def get(url, timeout=120):
    for i in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()
        except Exception as e:
            err = e; time.sleep(2 + 2 * i)
    raise err
pk = []
for q in ["contract disclosure", "contracts disclosure", "contract disclosure report"]:
    start = 0
    while True:
        u = "https://www.data.qld.gov.au/api/3/action/package_search?" + urllib.parse.urlencode({"q": q, "rows": 500, "start": start})
        r = json.loads(get(u))["result"]; pk += r["results"]
        start += 500
        if start >= r["count"]: break
seen = {}
for p in pk: seen[p["id"]] = p
json.dump([{"name": p["name"], "title": p["title"], "org": (p.get("organization") or {}).get("title"), "resources": [{"id": r["id"], "name": r.get("name"), "url": r.get("url"), "format": r.get("format"), "last_modified": r.get("last_modified")} for r in p["resources"]]} for p in seen.values()], open(dl + "/packages.json", "w"), indent=0)
log = open(dl + "/scan_log.jsonl", "a"); out = open(dl + "/matches.jsonl", "a")
done = set()
if os.path.exists(dl + "/scan_log.jsonl"):
    for l in open(dl + "/scan_log.jsonl"):
        try: done.add(json.loads(l)["url"])
        except Exception: pass
for p in seen.values():
    for r in p["resources"]:
        fmt = (r.get("format") or "").lower(); url = r.get("url") or ""
        if fmt not in ("csv", "xlsx", "xls") and not re.search(r"\.(csv|xlsx|xls)$", url, re.I): continue
        if url in done: continue
        t = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()); rec = {"url": url, "package": p["name"], "org": (p.get("organization") or {}).get("title"), "resource": r.get("name"), "format": fmt, "retrieved_at": t}
        try:
            b = get(url, 90)
            rows = []
            if fmt == "csv" or url.lower().endswith(".csv"):
                s = b.decode("utf-8-sig", "replace")
                rows = list(csv.reader(io.StringIO(s)))
            else:
                import openpyxl
                wb = openpyxl.load_workbook(io.BytesIO(b), read_only=True, data_only=True)
                for ws in wb.worksheets:
                    rows += [[("" if c is None else str(c)) for c in row] for row in ws.iter_rows(values_only=True)]
            # header = first row containing 'supplier' or 'contractor'
            hi = next((i for i, row in enumerate(rows[:15]) if any(re.search(r"supplier|contractor|vendor", c or "", re.I) for c in row)), 0)
            hdr = rows[hi] if rows else []
            addr_cols = [i for i, h in enumerate(hdr) if re.search(r"address|suburb|postcode|post code|country|state|city|location|town", h or "", re.I) and not re.search(r"description|delivery|work", h or "", re.I)]
            rec.update({"bytes": len(b), "rows": len(rows) - hi - 1, "header": hdr, "addr_cols": [hdr[i] for i in addr_cols]})
            n = 0
            for row in rows[hi + 1:]:
                vals = " | ".join(row[i] for i in addr_cols if i < len(row))
                if re.search(r"canad", vals, re.I) or PC.search(vals):
                    n += 1; out.write(json.dumps({"url": url, "package": p["name"], "org": rec["org"], "resource": r.get("name"), "retrieved_at": t, "header": hdr, "row": row}, ensure_ascii=False) + "\n"); out.flush()
            rec["matches"] = n
        except Exception as e:
            rec["error"] = str(e)[:200]
        log.write(json.dumps(rec, ensure_ascii=False) + "\n"); log.flush()
        time.sleep(0.4)
log.write(json.dumps({"url": "__DONE__", "t": time.strftime("%FT%TZ", time.gmtime())}) + "\n")
