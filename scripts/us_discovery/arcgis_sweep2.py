import json, urllib.request, urllib.parse, time, re, sys
from concurrent.futures import ThreadPoolExecutor
UA = "contracts-research/1.0"
items = {}
for q in ["purchase orders", "contracts", "vendor payments", "checkbook", "procurement", "contract awards", "vendors", "supplier", "expenditures", "spend", "awarded", "bids", "invoices", "payments", "purchasing", "accounts payable", "contract list", "active contracts"]:
    for start in (1, 101):
        u = "https://hub.arcgis.com/api/search/v1/collections/dataset/items?" + urllib.parse.urlencode({"q": q, "limit": 100, "startindex": start})
        try:
            j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60))
        except Exception as e:
            break
        for f in j.get("features", []):
            p = f["properties"]
            url = p.get("url") or ""
            if not re.search(r"/(FeatureServer|MapServer)", url): continue
            if (p.get("modified") or 0) < 1735689600000: continue  # modified >= 2025-01-01
            items[f["id"]] = (p.get("title"), p.get("owner"), url)
        time.sleep(0.4)
print("items", len(items), file=sys.stderr)
def chk(kv):
    k, (t, o, url) = kv
    base = url if re.search(r"/(FeatureServer|MapServer)/\d+$", url) else url.rstrip("/") + "/0"
    try:
        j = json.load(urllib.request.urlopen(urllib.request.Request(base + "?f=json", headers={"User-Agent": UA}), timeout=30))
    except Exception:
        return None
    fs = [x.get("name", "") for x in j.get("fields", []) or []]
    loc = [x for x in fs if re.search(r"(state|province|country|postal|zip)", x, re.I) and not re.search(r"status|statement", x, re.I)]
    ven = [x for x in fs if re.search(r"(vendor|supplier|contractor|payee|merchant)", x, re.I)]
    if loc and ven:
        return f"{t} | {o} | {base} | {loc[:5]} | {ven[:3]}"
with ThreadPoolExecutor(3) as ex:
    for r in ex.map(chk, items.items()):
        if r: print(r, flush=True)
