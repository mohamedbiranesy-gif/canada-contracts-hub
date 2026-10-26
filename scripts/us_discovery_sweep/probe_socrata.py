#!/usr/bin/env python3
"""Probe candidate Socrata datasets for Canadian vendor-location values (server-side SoQL, grouped counts).
usage: python3 -I probe_socrata.py <socrata_classified.jsonl> <out_probe.jsonl> [decision=probe]
Per-domain throttle 0.5 s; resumable (skips datasets already in out)."""
import sys, json, re, time, threading, urllib.parse, urllib.request, os
from concurrent.futures import ThreadPoolExecutor
UA = "contracts-research/1.0"
PROVS = ["ON", "ONT", "ONTARIO", "QC", "PQ", "QUE", "QUEBEC", "QUÉBEC", "BC", "B.C.", "BRITISH COLUMBIA", "AB", "ALTA",
         "ALBERTA", "MB", "MAN", "MANITOBA", "SK", "SASK", "SASKATCHEWAN", "NS", "N.S.", "NOVA SCOTIA", "NB", "N.B.",
         "NEW BRUNSWICK", "NL", "NF", "NFLD", "NEWFOUNDLAND", "NEWFOUNDLAND AND LABRADOR", "PE", "PEI", "P.E.I.",
         "PRINCE EDWARD ISLAND", "YT", "YUKON", "NT", "NWT", "NORTHWEST TERRITORIES", "NU", "NUNAVUT", "CANADA", "CAN", "CDN"]
PC = re.compile(r"^\s*[ABCEGHJ-NPRSTVXY]\d[A-Z][ -]?\d[A-Z]\d\s*$", re.I)
PCLOOSE = re.compile(r"[ABCEGHJ-NPRSTVXY]\d[A-Z][ -]?\d[A-Z]\d", re.I)
def q(s): return "'" + s.replace("'", "''") + "'"
def pred(col, kind):
    c = f"upper(`{col}`)"
    if kind == "country":
        return f"{c} in ('CA','CAN','CANADA','CDN') OR {c} like '%CANADA%'"
    if kind == "state":
        return f"{c} in ({','.join(q(p) for p in PROVS)}) OR {c} like '%CANADA%'"
    if kind == "zip":
        return f"{c} >= 'A' AND {c} < '['"
    if kind in ("address", "city"):
        return f"{c} like '%CANADA%'"
    return None
locks = {}; last = {}; glock = threading.Lock()
def throttle(host, gap=0.5):
    with glock:
        if host not in locks: locks[host] = threading.Lock(); last[host] = 0
    with locks[host]:
        w = last[host] + gap - time.time()
        if w > 0: time.sleep(w)
        last[host] = time.time()
def soql(domain, ds, params, tries=3):
    u = f"https://{domain}/resource/{ds}.json?" + urllib.parse.urlencode(params)
    err = None
    for a in range(tries):
        throttle(domain)
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=120) as r:
                return json.loads(r.read().decode("utf-8", "replace")), None
        except urllib.error.HTTPError as e:
            body = e.read()[:300].decode("utf-8", "replace")
            err = f"HTTP {e.code} {body}"
            if e.code in (400, 403, 404): break
            time.sleep(3 * (a + 1))
        except Exception as e:
            err = str(e)[:200]; time.sleep(3 * (a + 1))
    return None, err

inp, outp = sys.argv[1], sys.argv[2]
want = sys.argv[3] if len(sys.argv) > 3 else "probe"
done = set()
if os.path.exists(outp):
    for l in open(outp):
        j = json.loads(l); done.add((j["domain"], j["id"]))
cands = []
for l in open(inp):
    j = json.loads(l)
    if j["decision"] == want and (j["domain"], j["id"]) not in done:
        cands.append(j)
print("to probe", len(cands), file=sys.stderr, flush=True)
fo = open(outp, "a"); wl = threading.Lock()
def probe(j):
    res = {"domain": j["domain"], "id": j["id"], "name": j["name"], "cols": []}
    locs = sorted(j["loc_cols"], key=lambda x: (not x["vendorish"], x["kind"] not in ("country", "state", "zip")))[:8]
    for lc in locs:
        p = pred(lc["col"], lc["kind"])
        if not p: continue
        rows, err = soql(j["domain"], j["id"], {"$select": f"`{lc['col']}` AS v, count(*) AS n", "$where": p,
                                                "$group": f"`{lc['col']}`", "$order": "n DESC", "$limit": 2000})
        entry = {"col": lc["col"], "kind": lc["kind"], "vendorish": lc["vendorish"]}
        if err:
            entry["error"] = err
        else:
            vals = [(r.get("v"), int(float(r.get("n", 0)))) for r in rows]
            if lc["kind"] == "zip":
                vals = [(v, n) for v, n in vals if v and PCLOOSE.search(v)]
            elif lc["kind"] in ("address", "city"):
                pass
            entry["hits"] = sum(n for _, n in vals)
            entry["values"] = vals[:40]
        res["cols"].append(entry)
    res["total_hits"] = sum(c.get("hits", 0) for c in res["cols"])
    with wl:
        fo.write(json.dumps(res, ensure_ascii=False) + "\n"); fo.flush()
with ThreadPoolExecutor(12) as ex:
    list(ex.map(probe, cands))
print("done", file=sys.stderr)
