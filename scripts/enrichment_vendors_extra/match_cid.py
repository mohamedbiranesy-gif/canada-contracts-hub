#!/usr/bin/env python3
"""Match vendors to the Canadian Importers Database 2024 ('Major importers by city': company, city, province, postal code).
Used for address confirmation; a match needs city/postal agreement to be better than weak.
usage: python3 -I match_cid.py <cid-bdic-majorimportersbycity2024.xls> <retrieved_at>"""
import sys, os, json, collections
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vx_common as C  # noqa: E402

XLS, RETRIEVED = sys.argv[1], sys.argv[2]
FILE_URL = "https://ised-isde.canada.ca/site/ised/sites/default/files/documents/cid-bdic-majorimportersbycity2024.xls"
DATASET = "https://open.canada.ca/data/en/dataset/e5eae1d4-687c-4db2-9273-a8d2d711144c (Canadian Importers Database 2024)"
vendors, meta = C.load_index()
need = C.need_map(vendors)
df = pd.read_excel(XLS, engine="pyxlsb", dtype=str).fillna("")
cols = list(df.columns)
ents = {}
by_loose = collections.defaultdict(set)
for i, row in enumerate(df.to_dict("records")):
    name = row.get("COMPANY-ENTREPRISE")
    sk, lk = C.name_keys([name])
    lkn = {l for l in lk if l in need}
    if not lkn:
        continue
    p = C.norm_postal(row.get("POSTAL_CODE-CODE_POSTAL"))
    key = (C.strict_key(name), p or C.norm_city(row.get("CITY-VILLE")))
    E = ents.setdefault(key, {"sk": set(), "lk": set(), "postals": set(), "cities": set(), "provs": set(), "rows": []})
    E["sk"] |= sk
    E["lk"] |= lk
    if p:
        E["postals"].add(p)
    c = C.norm_city(row.get("CITY-VILLE"))
    if c:
        E["cities"].add(c)
    pr = C.norm_prov(row.get("PROVINCE_ENG"))
    if pr:
        E["provs"].add(pr)
    E["rows"].append(row)
    for l in lkn:
        by_loose[l].add(key)
print("rows", len(df), "candidate entities", len(ents), file=sys.stderr, flush=True)

out = C.Out("cid_importers")
for v in vendors:
    keys = set()
    for l in v["lk"]:
        keys |= by_loose.get(l, set())
    if not keys:
        continue
    cl = [{"ent": k, "idmatch": None, "strict": bool(v["sk"] & ents[k]["sk"]), "lkey_match": True,
           "loc": C.loc_eval(v, ents[k]["postals"], ents[k]["cities"], ents[k]["provs"]), "lkey": next(iter(ents[k]["lk"]), ""), "rec_provs": ents[k]["provs"]} for k in keys]
    matches = []
    for c in C.grade(v, cl, local_dataset=True):
        r = ents[c["ent"]]["rows"][0]
        matches.append({"match_confidence": c["match_confidence"], "match_basis": c["basis"], "legal_name": r.get("COMPANY-ENTREPRISE"), "identifiers": {},
                        "address": {"city": r.get("CITY-VILLE"), "region": C.norm_prov(r.get("PROVINCE_ENG")) or r.get("PROVINCE_ENG"),
                                    "postal_code": r.get("POSTAL_CODE-CODE_POSTAL"), "country": "CA"},
                        "phones": [], "emails": [], "website": None, "status": "listed as a major importer in %s" % r.get("DATA_YEAR-ANNÉE_DES_DONNÉES"),
                        "extra": {"data_year": r.get("DATA_YEAR-ANNÉE_DES_DONNÉES"), "province_fr": r.get("PROVINCE_FRA")},
                        "source_url": FILE_URL, "dataset_url": DATASET, "retrieved_at": RETRIEVED, "raw": ents[c["ent"]]["rows"]})
    out.write(v, matches)
res = out.close()
res["rows"] = len(df)
json.dump(res, open(C.WORK + "/cid_stats.json", "w"), indent=1)
print(json.dumps(res, indent=1))
