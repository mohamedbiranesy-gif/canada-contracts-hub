#!/usr/bin/env python3
"""Validate normalized/usaspending.jsonl: JSON parse, required keys, unique ids, status rules, counts."""
import json
import sys
from collections import Counter

REF = "2026-10-25"
path = sys.argv[1]
n = 0
ids = Counter()
status = Counter()
instr = Counter()
problems = []
required_top = ["record_id", "source", "status", "status_basis", "contract", "buyer", "vendor", "raw"]
with open(path, encoding="utf-8") as f:
    for line in f:
        n += 1
        try:
            rec = json.loads(line)
        except Exception as e:
            problems.append((n, f"json error {e}"))
            continue
        for k in required_top:
            if k not in rec:
                problems.append((n, f"missing {k}"))
        ids[rec["record_id"]] += 1
        status[rec["status"]] += 1
        instr[rec["contract"]["instrument_type"]] += 1
        if rec["vendor"]["country"] != "CA":
            problems.append((n, "vendor country != CA"))
        if rec["source"]["key"] != "usaspending":
            problems.append((n, "source key"))
        if not rec["source"]["record_url"] or not rec["source"]["record_url"].startswith("https://www.usaspending.gov/award/"):
            problems.append((n, f"record_url {rec['source']['record_url']}"))
        d = rec["contract"]["dates"]
        if rec["status"] == "ongoing":
            if not (d["end"] and d["end"] >= REF):
                problems.append((n, f"ongoing but end {d['end']}"))
            st = d["start"] or d["signed"]
            if not (st and st <= REF):
                problems.append((n, f"ongoing but start {st}"))
        if rec["status"] == "end_date_unknown" and rec["contract"]["instrument_type"] != "subcontract" and d["end"]:
            problems.append((n, "end_date_unknown but has end"))
        if rec["status"] == "ongoing_inferred" and rec["contract"]["instrument_type"] != "subcontract":
            problems.append((n, "ongoing_inferred on prime"))
        if "rows" not in rec["raw"] or not rec["raw"]["rows"]:
            problems.append((n, "raw.rows missing"))
        if not rec["vendor"]["name"]:
            problems.append((n, "vendor name blank"))
        if not rec["buyer"]["name"]:
            problems.append((n, "buyer name blank"))
dups = {k: v for k, v in ids.items() if v > 1}
print("records:", n)
print("unique ids:", len(ids), "duplicates:", len(dups))
print("status:", dict(status))
print("instrument types:", dict(instr.most_common()))
print("problems:", len(problems))
for p in problems[:20]:
    print("  ", p)
