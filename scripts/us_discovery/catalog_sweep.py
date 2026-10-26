import json, urllib.request, urllib.parse, time, re, sys
UA = "contracts-research/1.0"
qs = ["contracts", "contract awards", "purchase orders", "vendor payments", "procurement", "checkbook", "expenditures vendor", "purchasing", "awarded contracts", "active contracts", "vendor", "supplier", "accounts payable"]
seen = {}
for q in qs:
    for off in (0, 100, 200):
        u = "https://api.us.socrata.com/api/catalog/v1?" + urllib.parse.urlencode({"q": q, "only": "dataset", "limit": 100, "offset": off})
        try:
            j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60))
        except Exception as e:
            print("ERR", q, e, file=sys.stderr); break
        for x in j.get("results", []):
            r = x["resource"]; d = x["metadata"]["domain"]
            cols = r.get("columns_field_name", [])
            loc = [c for c in cols if re.search(r"(state|province|country|zip|postal|address|city)", c, re.I)]
            if not loc: continue
            if not re.search(r"(vendor|supplier|contractor|payee|merchant|company|firm)", " ".join(cols), re.I): continue
            seen[r["id"]] = (d, r["name"], r.get("updatedAt", "")[:10], loc[:6])
        time.sleep(0.4)
        if len(j.get("results", [])) < 100: break
for k, (d, n, up, loc) in sorted(seen.items(), key=lambda kv: kv[1][0]):
    print(d, k, up, n[:60], loc)
