#!/usr/bin/env python3
"""Probe ArcGIS candidate layers for Canadian vendor-location values (grouped counts via outStatistics).
usage: python3 -I probe_arcgis.py <arcgis_cands.jsonl> <out.jsonl>   (resumable by layer URL)"""
import sys, json, re, time, threading, urllib.parse, urllib.request, os
from concurrent.futures import ThreadPoolExecutor
UA = "contracts-research/1.0"
PROVS = ["ON", "ONT", "ONTARIO", "QC", "PQ", "QUE", "QUEBEC", "BC", "BRITISH COLUMBIA", "AB", "ALTA", "ALBERTA", "MB", "MANITOBA",
         "SK", "SASKATCHEWAN", "NS", "NOVA SCOTIA", "NB", "NEW BRUNSWICK", "NL", "NF", "NEWFOUNDLAND", "PE", "PEI",
         "PRINCE EDWARD ISLAND", "YT", "YUKON", "NT", "NU", "CANADA", "CAN"]
PC = re.compile(r"[ABCEGHJ-NPRSTVXY]\d[A-Z][ -]?\d[A-Z]\d", re.I)
locks = {}; last = {}; glock = threading.Lock()
def throttle(host, gap=0.5):
    with glock:
        if host not in locks: locks[host] = threading.Lock(); last[host] = 0
    with locks[host]:
        w = last[host] + gap - time.time()
        if w > 0: time.sleep(w)
        last[host] = time.time()
def q(layer, params):
    u = layer + "/query?" + urllib.parse.urlencode(params)
    host = urllib.parse.urlparse(u).netloc; err = None
    for a in range(3):
        throttle(host)
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=90) as r:
                j = json.loads(r.read().decode("utf-8", "replace"))
                if "error" in j: return None, str(j["error"])[:200]
                return j, None
        except Exception as e:
            err = str(e)[:150]; time.sleep(2 * (a + 1))
    return None, err
def kind(f):
    u = f.upper()
    if re.search(r"COUNTRY|CTRY|CNTRY", u): return "country"
    if re.search(r"ZIP|POSTAL|POSTCODE", u): return "zip"
    return "state"
inp, outp = sys.argv[1], sys.argv[2]
done = set()
if os.path.exists(outp):
    for l in open(outp): done.add(json.loads(l)["layer"])
cands = [json.loads(l) for l in open(inp)]
cands = [c for c in cands if c["layer"] not in done]
fo = open(outp, "a"); wl = threading.Lock()
def probe(c):
    res = {"layer": c["layer"], "title": c["title"], "owner": c["owner"], "cols": []}
    for f in c["loc_fields"][:6]:
        k = kind(f)
        if k == "country": w = f"UPPER({f}) IN ('CA','CAN','CANADA') OR UPPER({f}) LIKE '%CANADA%'"
        elif k == "zip": w = f"UPPER({f}) >= 'A' AND UPPER({f}) < '['"
        else: w = "UPPER(%s) IN (%s) OR UPPER(%s) LIKE '%%CANADA%%'" % (f, ",".join("'" + p + "'" for p in PROVS), f)
        st = json.dumps([{"statisticType": "count", "onStatisticField": f, "outStatisticFieldName": "n"}])
        j, err = q(c["layer"], {"where": w, "groupByFieldsForStatistics": f, "outStatistics": st, "f": "json"})
        if err:
            j, err2 = q(c["layer"], {"where": w, "returnCountOnly": "true", "f": "json"})
            if err2: res["cols"].append({"col": f, "kind": k, "error": err}); continue
            res["cols"].append({"col": f, "kind": k, "hits": j.get("count", 0), "values": []}); continue
        vals = [(ft["attributes"].get(f), next((v for k2, v in ft["attributes"].items() if k2.lower() == "n"), None)) for ft in j.get("features", [])]
        if k == "zip": vals = [(v, n) for v, n in vals if v and PC.search(str(v))]
        res["cols"].append({"col": f, "kind": k, "hits": sum(n or 0 for _, n in vals), "values": vals[:30]})
    res["total_hits"] = sum(x.get("hits", 0) for x in res["cols"])
    with wl:
        fo.write(json.dumps(res, ensure_ascii=False) + "\n"); fo.flush()
with ThreadPoolExecutor(6) as ex:
    list(ex.map(probe, cands))
