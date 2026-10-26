#!/usr/bin/env python3
"""Quick validator for normalized/<source>.jsonl files (SCHEMA.md shape).
Usage: python3 -I validate.py <file.jsonl> [more files...]
Prints counts by status, vendor country, problems (ongoing with end < ref, missing buyer, duplicate record_id ...)."""
import sys, json, collections
REF = "2026-10-25"
for p in sys.argv[1:]:
    c = collections.Counter(); st = collections.Counter(); vc = collections.Counter(); ids = set(); buyers = collections.Counter()
    probs = collections.Counter(); ex = {}
    for i, line in enumerate(open(p, encoding="utf-8")):
        try:
            r = json.loads(line)
        except Exception:
            probs["bad_json"] += 1; continue
        c["records"] += 1
        rid = r.get("record_id")
        if rid in ids:
            probs["dup_record_id"] += 1; ex.setdefault("dup_record_id", rid)
        ids.add(rid)
        for k in ("record_id", "source", "status", "status_basis", "contract", "buyer", "vendor", "raw"):
            if k not in r:
                probs["missing_" + k] += 1
        s = r.get("status"); st[s] += 1
        if s not in ("ongoing", "ongoing_inferred", "end_date_unknown"):
            probs["bad_status"] += 1; ex.setdefault("bad_status", rid)
        d = (r.get("contract") or {}).get("dates") or {}
        end = d.get("end"); start = d.get("start") or d.get("signed")
        if s == "ongoing" and (not end or end < REF):
            probs["ongoing_end_missing_or_past"] += 1; ex.setdefault("ongoing_end_missing_or_past", rid)
        if s in ("ongoing", "ongoing_inferred") and start and start > REF:
            probs["future_start"] += 1; ex.setdefault("future_start", rid)
        if end and end < REF:
            probs["end_past_any_status"] += 1; ex.setdefault("end_past_any_status", rid)
        b = (r.get("buyer") or {}).get("name")
        if not b:
            probs["no_buyer_name"] += 1; ex.setdefault("no_buyer_name", rid)
        buyers[b] += 1
        v = r.get("vendor") or {}
        vc[v.get("country")] += 1
        if not v.get("name"):
            probs["no_vendor_name"] += 1; ex.setdefault("no_vendor_name", rid)
        if not v.get("country_basis"):
            probs["no_country_basis"] += 1
        src = r.get("source") or {}
        if not src.get("key") or not src.get("dataset_url"):
            probs["source_incomplete"] += 1
    print(json.dumps({"file": p, "counts": c, "by_status": st, "vendor_country": vc.most_common(5), "n_buyers": len(buyers),
                      "top_buyers": buyers.most_common(8), "problems": probs, "examples": ex}, ensure_ascii=False))
