#!/usr/bin/env python3
"""Fetch ISO 20275 entity-legal-form names for the ELF codes used by Canadian LEI records (GLEIF API, ~1 request/second).
usage: python3 -I gleif_elf_fetch.py <lei2_ca.jsonl.gz> <out.json>"""
import sys, gzip, json, collections, time, urllib.request
elf = collections.Counter()
for l in gzip.open(sys.argv[1], "rt"):
    d = json.loads(l)
    elf[d.get("Entity.LegalForm.EntityLegalFormCode")] += 1
codes = [c for c, n in elf.most_common() if c and c not in ("8888", "9999")][:150]
out = {}
for c in codes:
    try:
        j = json.loads(urllib.request.urlopen(urllib.request.Request("https://api.gleif.org/api/v1/entity-legal-forms/" + c, headers={"User-Agent": "contracts-research/1.0"}), timeout=30).read())
        a = j["data"]["attributes"]
        out[c] = {"country": a.get("country"), "jurisdiction": a.get("jurisdiction"), "subdivision": a.get("subdivisionCode"), "names": [n.get("localName") for n in a.get("names") or []]}
    except Exception as e:
        out[c] = {"error": str(e)[:80]}
    time.sleep(1.1)
    json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=0)
print("done", len(out))
