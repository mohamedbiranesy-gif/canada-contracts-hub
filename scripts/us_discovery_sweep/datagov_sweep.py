#!/usr/bin/env python3
"""catalog.data.gov (new catalog) JSON search sweep, non-federal org types, honouring robots Crawl-Delay: 10.
usage: python3 -I datagov_sweep.py <out.jsonl.gz> [max_pages_per_term]"""
import sys, json, time, gzip, os, urllib.parse, urllib.request
UA = "contracts-research/1.0"
TERMS = ["contracts", "purchase orders", "procurement", "vendor payments", "checkbook", "vendors", "encumbrances",
         "contract awards", "expenditures", "supplier", "purchasing", "spending", "accounts payable", "agreements",
         "payments", "awards"]
ORG = ["City Government", "County Government", "State Government", "University", "Tribal"]
out = sys.argv[1]; maxp = int(sys.argv[2]) if len(sys.argv) > 2 else 15
seen = set()
if os.path.exists(out):
    for l in gzip.open(out, "rt"):
        seen.add(json.loads(l)["identifier"])
done_f = out + ".done"; done = set(l.strip() for l in open(done_f)) if os.path.exists(done_f) else set()
fo = gzip.open(out, "at"); log = open(out + ".log", "a"); df = open(done_f, "a")
for t in TERMS:
    if t in done: continue
    after = None
    for page in range(maxp):
        p = [("q", t)] + [("org_type", o) for o in ORG]
        if after: p.append(("after", after))
        u = "https://catalog.data.gov/search?" + urllib.parse.urlencode(p)
        j = None
        for a in range(3):
            try:
                j = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=90).read()); break
            except Exception as e:
                log.write(f"retry {t} p{page} {e}\n"); log.flush(); time.sleep(20)
        time.sleep(10.5)
        if j is None: break
        res = j.get("results", []); new = 0
        for r in res:
            org = r.get("organization") or {}
            dc = r.get("dcat") or {}
            rec = {"identifier": r.get("identifier"), "title": r.get("title") or dc.get("title"), "slug": r.get("slug"),
                   "org": org.get("name"), "org_type": org.get("organization_type"), "publisher": r.get("publisher"),
                   "keyword": r.get("keyword"), "last_harvested": r.get("last_harvested_date"),
                   "modified": dc.get("modified"), "landing": dc.get("landingPage"),
                   "dist": [{"url": d.get("downloadURL") or d.get("accessURL"), "fmt": d.get("format") or d.get("mediaType"),
                             "describedBy": d.get("describedBy"), "title": d.get("title")} for d in (dc.get("distribution") or [])][:12],
                   "description": (r.get("description") or "")[:400], "term": t}
            if rec["identifier"] in seen: continue
            seen.add(rec["identifier"]); new += 1
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
        fo.flush()
        log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%S')} {t} p{page} got={len(res)} new={new} seen={len(seen)}\n"); log.flush()
        after = j.get("after")
        if not res or not after: break
    df.write(t + "\n"); df.flush()
fo.close(); print("seen", len(seen))
