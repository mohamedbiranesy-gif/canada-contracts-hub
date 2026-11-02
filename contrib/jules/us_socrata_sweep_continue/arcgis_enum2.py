#!/usr/bin/env python3
"""Enumerate public ArcGIS Online items (www.arcgis.com sharing REST search; hub.arcgis.com has Crawl-delay 60 so it
is not used) for contract/payment keywords, then fetch layer/table fields (per-host throttle 0.5 s).
usage: python3 -I arcgis_enum2.py <items_out.jsonl> <fields_out.jsonl>"""
import json, sys, time, re, threading, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
UA = "contracts-research/1.0"
TERMS = ["contracts", "contract", "procurement", "vendor", "vendors", "supplier", "suppliers", "purchasing",
         "checkbook", "expenditures", "expenditure", "encumbrance", "encumbrances", "payee", "invoices", "payments",
         "spending", "purchases", "awards", "agreements", "disbursements", "ledger", "\"purchase orders\"",
         "\"purchase order\"", "\"vendor payments\"", "\"accounts payable\"", "\"check register\"",
         "\"contract awards\"", "\"open checkbook\"", "\"awarded contracts\"", "\"active contracts\""]
TYPEF = '(type:"Feature Service" OR type:"Map Service")'
REL = re.compile(r"contract|purchas|procure|vendor|supplier|payment|payee|expend|checkbook|spend|invoice|encumb|award|"
                 r"ledger|disburs|agreement|bid|po\b|p\.o\.|accounts payable|check register|warrant", re.I)
locks = {}; last = {}; glock = threading.Lock()
def throttle(host, gap=0.5):
    with glock:
        if host not in locks: locks[host] = threading.Lock(); last[host] = 0
    with locks[host]:
        w = last[host] + gap - time.time()
        if w > 0: time.sleep(w)
        last[host] = time.time()
def getj(u, timeout=60, tries=3):
    host = urllib.parse.urlparse(u).netloc; err = None
    for a in range(tries):
        throttle(host)
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:
            err = str(e)[:150]; time.sleep(2 * (a + 1))
    return {"_error": err}

items = {}
for t in TERMS:
    start = 1; total = 0
    while start > 0 and start <= 10000:
        u = "https://www.arcgis.com/sharing/rest/search?" + urllib.parse.urlencode(
            {"f": "json", "num": 100, "start": start, "q": f"{t} AND {TYPEF}"})
        j = getj(u, 90, 4)
        if "_error" in j or "error" in j:
            print("ERR", t, start, j.get("_error") or j.get("error"), file=sys.stderr); break
        total = j.get("total", 0)
        for r in j.get("results", []):
            url = r.get("url") or ""
            if not url: continue
            k = r["id"]
            if k not in items:
                items[k] = {"id": k, "title": r.get("title"), "owner": r.get("owner"), "orgId": r.get("orgId"),
                            "url": url, "type": r.get("type"), "modified": r.get("modified"),
                            "snippet": (r.get("snippet") or "")[:300], "tags": (r.get("tags") or [])[:20],
                            "accessInformation": (r.get("accessInformation") or "")[:200], "hits": []}
            items[k]["hits"].append(t)
        start = j.get("nextStart", -1)
    print(f"q:{t}\t{total}", file=sys.stderr, flush=True)
with open(sys.argv[1], "w") as fo:
    for v in items.values(): fo.write(json.dumps(v, ensure_ascii=False) + "\n")
print("items", len(items), file=sys.stderr, flush=True)

cand = [it for it in items.values() if REL.search(" ".join([it["title"] or "", it["snippet"] or "", " ".join(it["tags"])]))]
print("relevant items", len(cand), file=sys.stderr, flush=True)
def layers_for(url):
    url = url.rstrip("/")
    if re.search(r"/(FeatureServer|MapServer)/\d+$", url, re.I):
        return [url]
    j = getj(url + "?f=json")
    out = []
    for key in ("layers", "tables"):
        for l in (j.get(key) or []):
            if isinstance(l, dict) and "id" in l: out.append(f"{url}/{l['id']}")
    return out[:15] or [url + "/0"]
fo2 = open(sys.argv[2], "w"); wl = threading.Lock()
def chk(it):
    try:
        for lu in layers_for(it["url"]):
            j = getj(lu + "?f=json")
            if "_error" in j or "error" in j:
                rec = {"item": it["id"], "layer": lu, "error": str(j.get("_error") or j.get("error"))[:200]}
            else:
                fs = [(x.get("name"), x.get("alias"), x.get("type")) for x in (j.get("fields") or [])]
                rec = {"item": it["id"], "layer": lu, "name": j.get("name"), "type": j.get("type"), "fields": fs,
                       "lastEditDate": (j.get("editingInfo") or {}).get("lastEditDate")}
            with wl:
                fo2.write(json.dumps(rec, ensure_ascii=False) + "\n"); fo2.flush()
    except Exception as e:
        with wl:
            fo2.write(json.dumps({"item": it["id"], "layer": it["url"], "error": str(e)[:200]}) + "\n")
with ThreadPoolExecutor(8) as ex:
    list(ex.map(chk, cand))
fo2.close()
print("done", file=sys.stderr)
