import json, urllib.request, urllib.parse, sys, time
UA = "contracts-research/1.0"
portals = sys.argv[1].split(",")
for p in portals:
    for q in ("contracts", "purchase orders", "vendor payments", "checkbook"):
        u = f"https://{p}/api/3/action/package_search?" + urllib.parse.urlencode({"q": q, "rows": 15})
        try:
            j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=30))
        except Exception as e:
            print(p, "ERR", str(e)[:80]); break
        for d in j["result"]["results"]:
            res = [(r.get("format"), r.get("datastore_active"), r.get("id")) for r in d.get("resources", [])][:3]
            print(p, q, "|", d["name"][:60], "|", d.get("metadata_modified", "")[:10], res)
        time.sleep(0.4)
