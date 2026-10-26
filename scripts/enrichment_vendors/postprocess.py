"""Downgrade name-only REQ 'strong' matches (no city/postal agreement, no published NEQ) to 'weak'."""
import sys, json, re
inp, out = sys.argv[1], sys.argv[2]
LOC = re.compile(r"same postal code|same postal FSA|same city|NEQ published")
n = d = 0
with open(inp, encoding="utf-8") as f, open(out, "w", encoding="utf-8") as g:
    for line in f:
        r = json.loads(line); n += 1
        for m in r["registry_matches"]:
            if m["registry"] == "quebec_req" and m["match_confidence"] == "strong" and not LOC.search(m.get("match_basis") or ""):
                m["match_confidence"] = "weak"
                m["match_basis"] += "; downgraded to weak after precision review: no city/postal-code agreement"
                d += 1
        best = next((m for m in r["registry_matches"] if m["registry"] == "quebec_req" and m["match_confidence"] in ("exact", "strong")), None)
        r["best_match"]["quebec_req"] = best["neq"] if best else None
        g.write(json.dumps(r, ensure_ascii=False) + "\n")
print("vendors", n, "REQ matches downgraded", d)
