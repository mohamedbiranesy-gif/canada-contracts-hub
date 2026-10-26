import json, re, sys
items = {}
for l in open(sys.argv[1]):
    j = json.loads(l); items[j["id"]] = j
VEN = re.compile(r"vendor|vend_|^vend|supplier|payee|contractor|merchant|company|firm|business|recipient|awardee|seller|bidder|remit|consultant", re.I)
LOC = re.compile(r"(state|province|prov\b|country|ctry|cntry|zip|postal|postcode)", re.I)
NOTLOC = re.compile(r"status|statement|estate|statewide|fips|ship|deliver|site|project|property|facility|parcel|owner|applicant|permit|incident|school|customer|buyer|agency", re.I)
out = []
for l in open(sys.argv[2]):
    j = json.loads(l)
    if "fields" not in j: continue
    fs = [f[0] or "" for f in j["fields"]]
    al = {f[0]: (f[1] or "") for f in j["fields"]}
    ftype = {f[0]: f[2] for f in j["fields"]}
    ven = [f for f in fs if VEN.search(f) or VEN.search(al.get(f, ""))]
    loc = [f for f in fs if (LOC.search(f) or LOC.search(al.get(f, ""))) and not NOTLOC.search(f) and ftype.get(f) == "esriFieldTypeString"]
    if ven and loc:
        it = items.get(j["item"], {})
        out.append({"item": j["item"], "layer": j["layer"], "title": it.get("title"), "owner": it.get("owner"), "modified": it.get("modified"),
                    "vendor_fields": ven[:6], "loc_fields": loc[:8], "fields": fs})
for o in out:
    print(json.dumps(o, ensure_ascii=False))
