#!/usr/bin/env python3
"""Canadian vendor dictionary for tools/buyer_pages.py from the release: name, address text, the source's own country basis.
  python3 contrib/claude/buyer_pages/make_vendors.py  -> contrib/claude/buyer_pages/vendors_ca.tsv.gz"""
import gzip, json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
seen, n = {}, 0
for line in gzip.open(ROOT + "/data/release/canadian_vendor_contracts.jsonl.gz", "rt", encoding="utf-8"):
    r = json.loads(line); v = r.get("vendor") or {}
    name = re.sub(r"\s+", " ", (v.get("name") or "")).strip()
    if not name or name in seen or len(name) < 6:
        continue
    a = v.get("address") or {}
    addr = ", ".join(str(a.get(k)) for k in ("line1", "city", "region", "postal_code") if a.get(k)) if isinstance(a, dict) else str(a)
    basis = re.sub(r"\s+", " ", v.get("country_basis") or (r.get("vendor_enrichment") or {}).get("country_basis") or r.get("vendor_country_verified") or "source country field")
    seen[name] = (addr, str(basis)[:200]); n += 1
with gzip.open(ROOT + "/contrib/claude/buyer_pages/vendors_ca.tsv.gz", "wt", encoding="utf-8") as f:
    f.write("name\taddress\tcountry_basis\n")
    for name, (addr, basis) in sorted(seen.items()):
        f.write("%s\t%s\t%s\n" % (name.replace("\t", " "), addr.replace("\t", " "), basis.replace("\t", " ")))
print(n, "vendors")
