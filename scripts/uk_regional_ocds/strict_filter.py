#!/usr/bin/env python3
"""Keep only matches whose Canadian party is actually referenced as a supplier of an award/contract in the
release (PCS / Sell2Wales compiled releases carry a batch-wide 'parties' list, so role='supplier' alone is not
evidence that the party won THIS award). usage: strict_filter.py in.jsonl... > out.jsonl"""
import sys, json
def sup_ids(r):
    s = set()
    for k in ("awards", "contracts"):
        for x in r.get(k) or []:
            for su in x.get("suppliers") or []:
                if su.get("id") is not None: s.add(str(su["id"]))
    return s
kept = dropped = 0
for fn in sys.argv[1:]:
    for l in open(fn, encoding="utf-8"):
        d = json.loads(l); r = d["release"]; ids = sup_ids(r)
        m = [h for h in d["match"] if str(h["party_id"]) in ids]
        if m:
            d["match"] = m; kept += 1; print(json.dumps(d, ensure_ascii=False))
        else: dropped += 1
print(json.dumps({"kept": kept, "dropped_party_not_award_supplier": dropped}), file=sys.stderr)
