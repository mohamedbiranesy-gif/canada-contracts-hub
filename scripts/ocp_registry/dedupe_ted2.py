#!/usr/bin/env python3
"""Second pass: drop OpenTender records whose TED notice ids are in ted_eu's EXCLUDED list (ended by ted_eu's duration logic)."""
import json, re, sys
B = "."
ex = {e["publication_number"]: e["reason"] for e in json.load(open(B + "/downloads/ted_eu/normalize_stats.json"))["excluded"]}
for k in sys.argv[1:]:
    R = [json.loads(l) for l in open(B + "/normalized/%s.jsonl" % k)]
    keep, drop = [], []
    for r in R:
        hit = [i for i in r["contract"]["related"].get("ted_notice_ids", []) if i in ex]
        if hit: drop.append((r["record_id"], hit[0], ex[hit[0]][:200]))
        else: keep.append(r)
    open(B + "/normalized/%s.jsonl" % k, "w").write("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in keep))
    json.dump(drop, open(B + "/downloads/%s/dropped_as_ended_per_ted_eu.json" % k, "w"), ensure_ascii=False)
    print(k, len(R), "dropped (ted_eu says ended)", len(drop), "kept", len(keep))
