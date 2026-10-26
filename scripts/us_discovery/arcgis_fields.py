import json, urllib.request, sys, re
UA = "contracts-research/1.0"
for u in sys.argv[1:]:
    base = u if re.search(r"/(FeatureServer|MapServer)/\d+$", u) else u.rstrip("/") + "/0"
    try:
        j = json.load(urllib.request.urlopen(urllib.request.Request(base + "?f=json", headers={"User-Agent": UA}), timeout=60))
        c = json.load(urllib.request.urlopen(urllib.request.Request(base + "/query?where=1%3D1&returnCountOnly=true&f=json", headers={"User-Agent": UA}), timeout=60))
        print(base, "| count", c.get("count"), "|", [f["name"] for f in j.get("fields", [])])
    except Exception as e:
        print(base, "ERR", e)
