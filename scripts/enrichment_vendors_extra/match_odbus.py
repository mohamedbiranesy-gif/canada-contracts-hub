#!/usr/bin/env python3
"""Match vendors to Statistics Canada's Open Database of Businesses (ODBus v1, 2023 release; harmonised municipal/provincial
business-licence open data from ~30 providers).  Organisations only: rows whose business name looks like a personal name are skipped.
usage: python3 -I match_odbus.py <ODBus_2023.zip> <retrieved_at>
Writes enrichment/v2/vendors_extra_statcan_odbus.jsonl."""
import sys, os, io, csv, json, zipfile, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vx_common as C  # noqa: E402

ZIP, RETRIEVED = sys.argv[1], sys.argv[2]
DATASET = "https://www150.statcan.gc.ca/n1/pub/21-26-0003/212600032023001-eng.htm (ODBus_2023.zip, ODBus_v1.csv)"
csv.field_size_limit(10 ** 9)
vendors, meta = C.load_index()
need = C.need_map(vendors)
z = zipfile.ZipFile(ZIP)
src_link = {}
with z.open("ODBus_v1/ODBus_Sources.csv") as fh:
    for row in csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8", errors="replace")):
        src_link[(row.get("City") or "").strip().lower()] = row.get("Link to Dataset")


def val(x):
    return None if x in (None, "", "..") else x


ents = {}
by_loose = collections.defaultdict(set)
skipped_person = 0
with z.open("ODBus_v1/ODBus_v1.csv") as fh:
    for row in csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8", errors="replace")):
        names = [n for n in (val(row.get("business_name")), val(row.get("alt_business_name"))) if n]
        if not names:
            continue
        sk, lk = C.name_keys(names)
        lk_need = {l for l in lk if l in need}
        if not lk_need:
            continue
        if all(C.looks_like_person(n) for n in names):
            skipped_person += 1
            continue
        p = C.norm_postal(val(row.get("postal_code")))
        city = C.norm_city(val(row.get("city")))
        prov = C.norm_prov(val(row.get("prov_terr")))
        sn = val(row.get("street_no"))
        key = (row.get("provider"), C.strict_key(names[0]), p or (sn or "") + " " + (val(row.get("street_name")) or ""))
        E = ents.get(key)
        if E is None:
            E = ents[key] = {"sk": set(), "lk": set(), "postals": set(), "cities": set(), "provs": set(), "streets": set(), "rows": []}
        E["sk"] |= sk
        E["lk"] |= lk
        if p:
            E["postals"].add(p)
            if sn:
                E["streets"].add((sn.lstrip("0") or "0", p))
        for c in (city, C.norm_city(val(row.get("CSDNAME")))):
            if c:
                E["cities"].add(c)
        if prov:
            E["provs"].add(prov)
        if len(E["rows"]) < 10:
            E["rows"].append({k.strip(): v for k, v in row.items() if val(v) is not None})
        for l in lk_need:
            by_loose[l].add(key)
print("entities", len(ents), "skipped personal-name rows", skipped_person, file=sys.stderr, flush=True)


def record(key, conf, basis):
    E = ents[key]
    r0 = E["rows"][0]
    addr = {"full": r0.get("full_address"), "unit": r0.get("unit"), "line1": " ".join(x for x in (r0.get("street_no"), r0.get("street_name"), r0.get("street_type"), r0.get("street_direction")) if x) or None,
            "city": r0.get("city"), "region": r0.get("prov_terr"), "postal_code": r0.get("postal_code"), "country": "CA",
            "latitude": r0.get("latitude"), "longitude": r0.get("longitude")}
    ids = {"odbus_idx": [r.get("idx") for r in E["rows"]]}
    bid = sorted({r.get("business_id_no") for r in E["rows"] if r.get("business_id_no")})
    lic = sorted({r.get("licence_number") for r in E["rows"] if r.get("licence_number")})
    if bid:
        ids["municipal_business_id"] = bid
    if lic:
        ids["municipal_licence_number"] = lic
    prov_name = (r0.get("provider") or "").strip()
    link = src_link.get((r0.get("city") or "").strip().lower())
    return {"match_confidence": conf, "match_basis": basis, "legal_name": r0.get("business_name"), "identifiers": ids, "address": addr,
            "phones": [], "emails": [], "website": None, "status": r0.get("status"),
            "extra": {"alt_business_name": r0.get("alt_business_name"), "provider": prov_name, "licence_type": sorted({r.get("licence_type") for r in E["rows"] if r.get("licence_type")}),
                      "business_sector": r0.get("business_sector"), "business_subsector": r0.get("business_subsector"), "business_description": r0.get("business_description"),
                      "derived_NAICS": r0.get("derived_NAICS"), "source_NAICS_primary": r0.get("source_NAICS_primary"), "NAICS_descr": r0.get("NAICS_descr"),
                      "total_no_employees": r0.get("total_no_employees"), "rows_for_this_business": len(E["rows"]), "provider_dataset": link},
            "source_url": link or DATASET, "dataset_url": DATASET, "retrieved_at": RETRIEVED, "raw": {"rows": E["rows"]}}


out = C.Out("statcan_odbus")
stats = collections.Counter()
for v in vendors:
    keys = set()
    for l in v["lk"]:
        keys |= by_loose.get(l, set())
    if not keys:
        continue
    cl = []
    for k in keys:
        E = ents[k]
        cl.append({"ent": k, "idmatch": None, "strict": bool(v["sk"] & E["sk"]), "lkey_match": True,
                   "loc": C.loc_eval(v, E["postals"], E["cities"], E["provs"], E["streets"]), "lkey": next(iter(E["lk"]), ""), "rec_provs": E["provs"]})
    g = C.grade(v, cl, local_dataset=True)
    matches = [record(c["ent"], c["match_confidence"], c["basis"]) for c in g]
    out.write(v, matches)
    if matches:
        stats["phone_none"] += 0
res = out.close()
res["skipped_personal_name_rows"] = skipped_person
json.dump(res, open(C.WORK + "/odbus_stats.json", "w"), indent=1)
print(json.dumps(res, indent=1))
