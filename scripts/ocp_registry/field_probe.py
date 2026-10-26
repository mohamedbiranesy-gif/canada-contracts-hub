#!/usr/bin/env python3
"""Read OCDS lines on stdin (first N), report supplier-party address/country field coverage.
usage: field_probe.py <label>"""
import sys, json, collections
sys.path.insert(0, "scripts/ocp_registry")
label = sys.argv[1]
n = sup = sup_country = sup_addr = 0
cvals = collections.Counter(); addr_keys = collections.Counter(); has_period_end = 0; awards_n = 0
for line in sys.stdin:
    try:
        d = json.loads(line)
    except Exception:
        continue
    rels = d.get("releases") if "releases" in d else ([d["compiledRelease"]] if "compiledRelease" in d else [d])
    for r in rels:
        n += 1
        sids = {str(s.get("id")) for a in r.get("awards") or [] for s in a.get("suppliers") or []}
        for p in r.get("parties") or []:
            if not isinstance(p, dict): continue
            if "supplier" in [str(x).lower() for x in p.get("roles") or []] or str(p.get("id")) in sids:
                sup += 1
                ad = p.get("address") or {}
                if ad: sup_addr += 1
                for k in ad: addr_keys[k] += 1
                c = ad.get("countryName") or ad.get("country") or ad.get("countryCode")
                if c:
                    sup_country += 1; cvals[str(c)[:30]] += 1
        for a in r.get("awards") or []:
            awards_n += 1
        for c in r.get("contracts") or []:
            if (c.get("period") or {}).get("endDate"): has_period_end += 1
print(json.dumps({"label": label, "releases": n, "supplier_parties": sup, "with_address": sup_addr, "with_country": sup_country,
  "addr_keys": dict(addr_keys.most_common(8)), "country_top": dict(cvals.most_common(8)), "awards": awards_n, "contracts_with_period_end": has_period_end}, ensure_ascii=False))
