import json, urllib.request, urllib.parse, time, sys
UA = "contracts-research/1.0"
seen = {}
for q in ["purchase orders", "purchase order vendor", "contracts vendor", "vendor payments", "checkbook", "awarded contracts", "active contracts", "vendor list", "expenditures vendor"]:
    u = "https://hub.arcgis.com/api/search/v1/collections/dataset/items?" + urllib.parse.urlencode({"q": q, "limit": 60})
    try:
        j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60))
    except Exception as e:
        print("ERR", q, e); continue
    for f in j.get("features", []):
        p = f["properties"]
        if f["id"] in seen: continue
        seen[f["id"]] = 1
        print(f["id"], "|", (p.get("title") or "")[:60], "|", (p.get("owner") or "")[:25], "|", time.strftime("%Y-%m-%d", time.gmtime((p.get("modified") or 0) / 1000)), "|", (p.get("url") or "")[:110])
    time.sleep(0.5)
