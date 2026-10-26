#!/usr/bin/env python3
"""Coverage counts for vendors_extra_<source>.jsonl files.
usage: python3 -I coverage.py <source> [<source> ...]  -> prints JSON {source: stats}"""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vx_common as C  # noqa: E402

vendors, _ = C.load_index()
hm = {v["vendor_key"]: bool(v["rc_hm"]) for v in vendors}
res = {}
for src in sys.argv[1:]:
    st = collections.Counter()
    for l in open(C.V2 + "/vendors_extra_%s.jsonl" % src, encoding="utf-8"):
        d = json.loads(l)
        best = d["matches"][0]["match_confidence"]
        st["vendors_any"] += 1
        st["best_" + best] += 1
        if best not in ("exact", "strong"):
            continue
        st["vendors_exact_or_strong"] += 1
        st["hm_vendors_exact_or_strong"] += hm.get(d["vendor_key"], False)
        es = [m for m in d["matches"] if m["match_confidence"] in ("exact", "strong")]
        st["match_entries_exact_or_strong"] += len(es)
        f = collections.Counter()
        for m in es:
            a = m.get("address") or {}
            f["address_street"] |= bool(a.get("line1") or a.get("full"))
            f["address_postal"] |= bool(a.get("postal_code"))
            f["address_city"] |= bool(a.get("city"))
            f["phone"] |= bool(m.get("phones"))
            f["email"] |= bool(m.get("emails"))
            f["website"] |= bool(m.get("website"))
            ids = m.get("identifiers") or {}
            for k, v in ids.items():
                if v:
                    f["id:" + k] |= True
            ex = m.get("extra") or {}
            for k in ("direct_parent", "ultimate_parent", "parent_organization", "industry", "inception", "employees", "legal_form_name", "licences_sample", "licences"):
                if ex.get(k):
                    f["extra:" + k] |= True
            if "equals the" in m.get("match_basis", ""):
                f["identifier_join"] |= True
        for k, v in f.items():
            st["fill:" + k] += int(bool(v))
    res[src] = dict(st)
print(json.dumps(res, indent=1, sort_keys=True))
