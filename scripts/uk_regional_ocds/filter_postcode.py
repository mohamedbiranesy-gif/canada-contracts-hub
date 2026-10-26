#!/usr/bin/env python3
"""Filter OCDS compiled releases (stdin, one per line) for supplier parties located in Canada when the
publisher gives NO country field (e.g. Public Contracts Scotland / Sell2Wales): supplier address
countryName/country = Canada, OR postalCode (or the tail of streetAddress/locality) is a Canadian postal code
(A9A 9A9 — impossible as a UK postcode, whose inward code is 9AA), OR region/locality is a Canadian province
name together with a Canadian postal code. Names are never used.
usage: filter_postcode.py --out matches.jsonl --label key:year"""
import sys, json, re, argparse
ap = argparse.ArgumentParser(); ap.add_argument("--out"); ap.add_argument("--label"); ap.add_argument("--stats")
a = ap.parse_args()
CA_PC = re.compile(r"\b([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z])[ -]?(\d[ABCEGHJ-NPRSTV-Z]\d)\b")
CA_PC_FULL = re.compile(r"^\s*[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d\s*$", re.I)
CA_NAMES = {"canada", "canadá", "kanada"}
def sup_ids(r):
    s = set()
    for k in ("awards", "contracts"):
        for x in r.get(k) or []:
            for su in x.get("suppliers") or []:
                if su.get("id") is not None: s.add(str(su["id"]))
    return s
n = kept = 0
out = open(a.out, "a", encoding="utf-8")
for line in sys.stdin:
    n += 1
    try: r = json.loads(line)
    except Exception: continue
    ids = sup_ids(r); hits = []
    for p in r.get("parties") or []:
        roles = [str(x).lower() for x in p.get("roles") or []]
        if "supplier" not in roles and str(p.get("id")) not in ids: continue
        ad = p.get("address") or {}
        cn = str(ad.get("countryName") or ad.get("country") or "").strip().lower()
        pc = str(ad.get("postalCode") or "")
        basis = None
        if cn in CA_NAMES or cn in ("ca", "can"):
            basis = "address.countryName=%r" % ad.get("countryName", ad.get("country"))
        elif pc and CA_PC_FULL.match(pc):
            basis = "address.postalCode=%r is a Canadian postal code (A9A 9A9 pattern; not a valid UK postcode)" % pc
        else:
            tail = " ".join(str(ad.get(k) or "") for k in ("streetAddress", "locality", "region"))
            m = CA_PC.search(tail.upper())
            if m and re.search(r"\b(canada|ontario|quebec|québec|british columbia|alberta|manitoba|saskatchewan|nova scotia|new brunswick|newfoundland|prince edward island|yukon|nunavut|northwest territories|\bON\b|\bQC\b|\bBC\b|\bAB\b|\bMB\b|\bSK\b|\bNS\b|\bNB\b|\bNL\b|\bPE\b)", tail, re.I):
                basis = "Canadian postal code %r with Canadian province/country token in address text" % m.group(0)
        if basis: hits.append({"party_id": p.get("id"), "name": p.get("name"), "basis": basis, "address": ad})
    if hits:
        kept += 1
        out.write(json.dumps({"label": a.label, "match": hits, "release": r}, ensure_ascii=False) + "\n")
out.close()
msg = {"label": a.label, "lines": n, "kept": kept}
print(json.dumps(msg))
if a.stats: open(a.stats, "a").write(json.dumps(msg) + "\n")
