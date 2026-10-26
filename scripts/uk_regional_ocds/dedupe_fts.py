#!/usr/bin/env python3
"""Drop uk_scotland_pcs / uk_wales_sell2wales records already present in uk_find_a_tender / uk_contracts_finder /
ted_eu (same normalized vendor+buyer prefix, same title prefix, publication dates within 45 days).
usage: dedupe_fts.py <key>..."""
import json, re, sys, datetime
B = "."
def n(s): return re.sub(r"[^a-z0-9]", "", (s or "").lower())
def d(s):
    try: return datetime.date.fromisoformat((s or "")[:10])
    except Exception: return None
idx = {}
for src in ["uk_find_a_tender", "uk_contracts_finder", "ted_eu"]:
    for l in open(f"{B}/normalized/{src}.jsonl", encoding="utf-8"):
        r = json.loads(l)
        idx.setdefault((n(r["vendor"]["name"])[:8], n(r["buyer"]["name"])[:8]), []).append(
            (r["record_id"], n(r["contract"].get("title")), d(r["contract"]["dates"].get("published"))))
for k in sys.argv[1:]:
    R = [json.loads(l) for l in open(f"{B}/normalized/{k}.jsonl", encoding="utf-8")]
    keep, drop = [], []
    for m in R:
        t = n(m["contract"].get("title")); pd = d(m["contract"]["dates"].get("published"))
        hit = None
        for rid, ht, hd in idx.get((n(m["vendor"]["name"])[:8], n(m["buyer"]["name"])[:8]), []):
            same_title = ht[:12] and (ht[:12] in t or t[:12] in ht)
            close = (pd is None or hd is None or abs((pd - hd).days) <= 45)
            if same_title and close: hit = rid; break
        if hit:
            drop.append((m["record_id"], hit))
        else:
            keep.append(m)
    open(f"{B}/normalized/{k}.jsonl", "w", encoding="utf-8").write("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in keep))
    json.dump(drop, open(f"{B}/downloads/{k}/dropped_as_fts_cf_ted_duplicates.json", "w"), indent=0)
    print(k, "in", len(R), "dropped", len(drop), "kept", len(keep))
