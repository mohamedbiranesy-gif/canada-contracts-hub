#!/usr/bin/env python3
"""Print Socrata dataset metadata: columns (field/type), row count, min/max of date columns, optional where-count.
usage: python3 -I meta.py <domain> <id> [where]"""
import sys, json, time, urllib.parse, urllib.request
UA = "contracts-research/1.0"


def get(u):
    for a in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=120) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            return {"_error": f"HTTP {e.code} {e.read()[:200]!r}"}
        except Exception as e:
            err = str(e); time.sleep(2)
    return {"_error": err}


dom, ds = sys.argv[1], sys.argv[2]
where = sys.argv[3] if len(sys.argv) > 3 else None
v = get(f"https://{dom}/api/views/{ds}.json")
if "_error" in v:
    print("views error", v["_error"])
    cols = []
else:
    print("NAME:", v.get("name"), "| updated:", time.strftime("%Y-%m-%d", time.gmtime(v.get("rowsUpdatedAt") or 0)),
          "| viewType:", v.get("viewType"), "| displayType:", v.get("displayType"), "| parent:", v.get("modifyingViewUid"))
    print("DESC:", (v.get("description") or "")[:300].replace("\n", " "))
    cols = [(c.get("fieldName"), c.get("dataTypeName"), c.get("name")) for c in v.get("columns", []) if not (c.get("fieldName") or "").startswith(":")]
    print("COLS:", ", ".join(f"{f}({t})" for f, t, n in cols))
time.sleep(0.4)
c = get(f"https://{dom}/resource/{ds}.json?" + urllib.parse.urlencode({"$select": "count(*) AS n"}))
print("ROWS:", c)
for f, t, n in cols:
    if t in ("calendar_date", "date"):
        time.sleep(0.4)
        r = get(f"https://{dom}/resource/{ds}.json?" + urllib.parse.urlencode({"$select": f"min(`{f}`) AS mn, max(`{f}`) AS mx"}))
        print("DATE", f, r)
if where:
    time.sleep(0.4)
    r = get(f"https://{dom}/resource/{ds}.json?" + urllib.parse.urlencode({"$select": "count(*) AS n", "$where": where}))
    print("WHERE COUNT:", r)
    time.sleep(0.4)
    r = get(f"https://{dom}/resource/{ds}.json?" + urllib.parse.urlencode({"$where": where, "$limit": 3}))
    print("SAMPLE:", json.dumps(r, ensure_ascii=False)[:1500])
