#!/usr/bin/env python3
"""Stream OCDS compiled releases (one JSON per line on stdin) and keep those whose
SUPPLIER party (roles contains 'supplier'; falls back to award.suppliers ids) has an
address country that denotes Canada. Writes matching lines to --out (append) and a
small stats json to --stats.
Country match is structural only: parties[].address.countryName / address.country /
address.country.id|name, or identifier.scheme starting with 'CA-' (OCDS org-id prefix)."""
import sys, json, argparse, re, time, unicodedata

CANADA_TOKENS = {"canada", "canadá", "kanada", "канада", "加拿大", "カナダ", "캐나다", "ca", "can", "cdn"}

def norm(s):
    s = unicodedata.normalize("NFKD", str(s))
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9Ѐ-ӿ一-鿿぀-ヿ가-힯]+", "", s.lower())

def country_of(addr):
    """return list of raw country strings found in an OCDS address object"""
    out = []
    if not isinstance(addr, dict):
        return out
    for k in ("countryName", "country", "countryCode", "pais", "country_name"):
        v = addr.get(k)
        if v is None:
            continue
        if isinstance(v, dict):
            for kk in ("id", "name", "description"):
                if v.get(kk):
                    out.append(str(v[kk]))
        else:
            out.append(str(v))
    return out

def is_canada(values):
    for v in values:
        if norm(v) in CANADA_TOKENS:
            return True
    return False

def supplier_ids(rel):
    ids = set()
    for a in rel.get("awards") or []:
        for s in a.get("suppliers") or []:
            if s.get("id") is not None:
                ids.add(str(s["id"]))
    for c in rel.get("contracts") or []:
        for s in c.get("suppliers") or []:
            if s.get("id") is not None:
                ids.add(str(s["id"]))
    return ids

def check(rel):
    """returns (matched: bool, basis: str|None, matched_party_names: list)"""
    parties = rel.get("parties") or []
    sids = supplier_ids(rel)
    hits = []
    for p in parties:
        if not isinstance(p, dict):
            continue
        roles = [str(r).lower() for r in (p.get("roles") or [])]
        is_sup = ("supplier" in roles) or (str(p.get("id")) in sids)
        if not is_sup:
            continue
        vals = country_of(p.get("address"))
        basis = None
        if is_canada(vals):
            basis = "parties[].address country field = %r" % vals
        else:
            sch = (p.get("identifier") or {}).get("scheme")
            if isinstance(sch, str) and sch.upper().startswith("CA-"):
                basis = "parties[].identifier.scheme = %r" % sch
        if basis:
            hits.append((p.get("name"), basis))
    # also award.suppliers embedded address (some publishers inline it)
    for a in rel.get("awards") or []:
        for s in a.get("suppliers") or []:
            vals = country_of(s.get("address"))
            if is_canada(vals):
                hits.append((s.get("name"), "awards[].suppliers[].address country field = %r" % vals))
    if hits:
        return True, hits
    return False, hits

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--stats", required=True)
    ap.add_argument("--label", default="")
    a = ap.parse_args()
    n = bad = kept = 0
    t0 = time.time()
    with open(a.out, "a", encoding="utf-8") as fo:
        for line in sys.stdin:
            n += 1
            line = line.strip()
            if not line:
                continue
            try:
                rel = json.loads(line)
            except Exception:
                bad += 1
                continue
            # a line may be a release package
            rels = rel.get("releases") if isinstance(rel, dict) and "releases" in rel else [rel]
            for r in rels:
                ok, hits = check(r)
                if ok:
                    kept += 1
                    fo.write(json.dumps({"_label": a.label, "_hits": hits, "release": r}, ensure_ascii=False) + "\n")
                    fo.flush()
    with open(a.stats, "a", encoding="utf-8") as fs:
        fs.write(json.dumps({"label": a.label, "lines_seen_after_prefilter": n, "bad_json": bad, "kept": kept,
                             "seconds": round(time.time() - t0, 1), "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}) + "\n")
    print(a.label, "lines", n, "kept", kept, "bad", bad, file=sys.stderr)

if __name__ == "__main__":
    main()
