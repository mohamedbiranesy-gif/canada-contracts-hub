import sys, json, urllib.request, urllib.parse
# usage: soql.py domain id "select" "where" "group" [limit]
d, i, sel, where, grp = sys.argv[1:6]
lim = sys.argv[6] if len(sys.argv) > 6 else "200"
p = {"$limit": lim}
if sel: p["$select"] = sel
if where: p["$where"] = where
if grp: p["$group"] = grp; p["$order"] = "count(*) desc"
u = f"https://{d}/resource/{i}.json?" + urllib.parse.urlencode(p)
print(json.dumps(json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "contracts-research/1.0"}), timeout=120))))
