#!/usr/bin/env python3
"""Print a random sample of exact/strong matches of one vendors_extra_<source>.jsonl for hand precision checking.
usage: python3 -I sample_check.py <source> [n=30] [seed=7] [confs=exact,strong]"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vx_common as C  # noqa: E402

src = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 30
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 7
confs = set((sys.argv[4] if len(sys.argv) > 4 else "exact,strong").split(","))
vendors, _ = C.load_index()
vk = {v["vendor_key"]: v for v in vendors}
rows = []
for l in open(C.V2 + "/vendors_extra_%s.jsonl" % src, encoding="utf-8"):
    d = json.loads(l)
    for m in d["matches"]:
        if m["match_confidence"] in confs:
            rows.append((d, m))
random.Random(seed).shuffle(rows)
for k, (d, m) in enumerate(rows[:n], 1):
    v = vk[d["vendor_key"]]
    a = m.get("address") or {}
    loc = ", ".join(str(x) for x in (a.get("line1") or a.get("full"), a.get("city"), a.get("region"), a.get("postal_code")) if x)
    print("%2d. [%s] VENDOR %r | cities=%s postals=%s provs=%s" % (k, m["match_confidence"], d["name"], sorted(v["cities"])[:3], sorted(v["postals"])[:3], sorted(v["provs"])))
    print("    SOURCE %r | %s | ids=%s" % (m.get("legal_name"), loc, {kk: vv for kk, vv in (m.get("identifiers") or {}).items() if vv and kk not in ("registration_authority_name",)}))
    print("    basis: %s" % m["match_basis"][:300])
print("total exact/strong match entries:", len(rows))
