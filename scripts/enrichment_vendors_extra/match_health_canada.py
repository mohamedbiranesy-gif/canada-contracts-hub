#!/usr/bin/env python3
"""Match vendors to Health Canada licence-holder lists:
  - MDALL (Medical Devices Active Licence Listing) companies = medical-device licence holders, with their device licences
  - DPD (Drug Product Database) companies = DIN owners (drug product licence holders)
usage: python3 -I match_health_canada.py <download_dir>
Writes enrichment/v2/vendors_extra_health_canada.jsonl.  (The MDEL establishment-licence listing web application was in maintenance
at retrieval time and Health Canada publishes no DEL list file; see the note.)"""
import sys, os, json, collections, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vx_common as C  # noqa: E402

D = sys.argv[1]
PROV = {"Ontario": "ON", "Quebec": "QC", "Québec": "QC", "British Columbia": "BC", "Alberta": "AB", "Manitoba": "MB", "Saskatchewan": "SK",
        "Nova Scotia": "NS", "New Brunswick": "NB", "Newfoundland and Labrador": "NL", "Newfoundland": "NL", "Prince Edward Island": "PE",
        "Northwest Territories": "NT", "Yukon": "YT", "Nunavut": "NU"}
TODAY = "2026-10-25"


def rtime(fn):
    try:
        return open(os.path.join(D, fn)).read().strip()
    except Exception:
        return None


vendors, meta = C.load_index()
need = C.need_map(vendors)

# ---------------- MDALL
mdall = json.load(open(os.path.join(D, "mdall_company.json")))
lic = collections.defaultdict(list)
for x in json.load(open(os.path.join(D, "mdall_licence.json"))):
    lic[x["company_id"]].append(x)
ents = {}
by_loose = collections.defaultdict(set)


def add_ent(key, names, addr_parts, rec_type, raw, extra, ids, source_url, dataset_url, retrieved, status):
    sk, lk = C.name_keys(names)
    p = C.norm_postal(addr_parts.get("postal_code")) if addr_parts.get("country") == "CA" else None
    ents[key] = {"sk": sk, "lk": lk, "postals": {p} if p else set(), "cities": {C.norm_city(addr_parts.get("city"))} - {None} if addr_parts.get("country") == "CA" else set(),
                 "provs": {addr_parts.get("region")} - {None, ""} if addr_parts.get("country") == "CA" else set(),
                 "streets": {(sn, p) for sn in C.street_numbers(addr_parts.get("line1"))} if p else set(),
                 "addr": addr_parts, "type": rec_type, "raw": raw, "extra": extra, "ids": ids, "source_url": source_url, "dataset_url": dataset_url,
                 "retrieved": retrieved, "status": status, "name": names[0], "foreign": addr_parts.get("country") != "CA"}
    for l in lk:
        if l in need:
            by_loose[l].add(key)


R_MD = rtime("mdall_company_retrieved_at.txt")
R_ML = rtime("mdall_licence_retrieved_at.txt")
for c in mdall:
    L = lic.get(c["company_id"], [])
    st = collections.Counter(x["licence_status"] for x in L)
    current = [x for x in L if not x.get("end_date") or x["end_date"] >= TODAY]
    sample = sorted(current or L, key=lambda x: x.get("first_licence_status_dt") or "", reverse=True)[:10]
    a = {"line1": c.get("addr_line_1") or None, "line2": ", ".join(x for x in (c.get("addr_line_2"), c.get("addr_line_3")) if x) or None,
         "city": c.get("city") or None, "region": c.get("region_cd") or None, "postal_code": c.get("postal_code") or None, "country": c.get("country_cd") or None}
    add_ent(("mdall", c["company_id"]), [c["company_name"]], a, "MDALL medical device licence holder", {"company": c, "licences_sample": sample},
            {"licence_count": len(L), "licence_count_by_status_code": dict(st), "licences_without_end_or_ending_after_2026_10_25": len(current),
             "licences_sample": [{"licence_no": x["original_licence_no"], "name": x["licence_name"], "risk_class": x["appl_risk_class"], "type": x["licence_type_desc"],
                                  "status_code": x["licence_status"], "first_licence_status_dt": x["first_licence_status_dt"], "end_date": x.get("end_date")} for x in sample],
             "company_status_code": c.get("company_status")},
            {"health_canada_mdall_company_id": c["company_id"]},
            "https://health-products.canada.ca/api/medical-devices/company/?id=%s&lang=en&type=json" % c["company_id"],
            "https://health-products.canada.ca/api/medical-devices/company/?lang=en&type=json (+ /licence/ list) - MDALL API, open.canada.ca dataset 'Medical Devices Active Licence Listing'",
            "%s (companies), %s (licences)" % (R_MD, R_ML), "MDALL company status code %s" % c.get("company_status"))

# ---------------- DPD
R_DPD = rtime("dpd_company_retrieved_at.txt")
for c in json.load(open(os.path.join(D, "dpd_company.json"))):
    ctry = "CA" if c.get("country_name") == "Canada" else c.get("country_name")
    line1 = " ".join(x for x in (c.get("suite_number"), c.get("street_name")) if x) or None
    a = {"line1": line1, "po_box": c.get("post_office_box") or None, "city": c.get("city_name") or None,
         "region": PROV.get(c.get("province_name"), c.get("province_name")) or None, "postal_code": c.get("postal_code") or None, "country": ctry}
    add_ent(("dpd", c["company_code"]), [c["company_name"]], a, "DPD drug company (%s)" % c.get("company_type"), c,
            {"company_type": c.get("company_type")}, {"health_canada_dpd_company_code": c["company_code"]},
            "https://health-products.canada.ca/api/drug/company/?id=%s&lang=en&type=json" % c["company_code"],
            "https://health-products.canada.ca/api/drug/company/?lang=en&type=json - Drug Product Database API (open.canada.ca dataset bf55e42a-63cb-4556-bfd8-44f26e5a36fe)",
            R_DPD, c.get("company_type"))
print("entities", len(ents), "name keys", len(by_loose), file=sys.stderr, flush=True)

out = C.Out("health_canada")
stats = collections.Counter()
for v in vendors:
    keys = set()
    for l in v["lk"]:
        keys |= by_loose.get(l, set())
    if not keys:
        continue
    matches = []
    for kind in ("mdall", "dpd"):
        cl = []
        for k in keys:
            if k[0] != kind:
                continue
            E = ents[k]
            c = {"ent": k, "idmatch": None, "strict": bool(v["sk"] & E["sk"]), "lkey_match": True,
                 "loc": C.loc_eval(v, E["postals"], E["cities"], E["provs"], E["streets"]), "lkey": next(iter(E["lk"]), ""), "rec_provs": E["provs"]}
            if E["foreign"]:
                c["loc"]["basis"].append("source address outside Canada (%s)" % E["addr"].get("country"))
                c["loc"]["pc"] = True
            cl.append(c)
        for c in C.grade(v, cl):
            E = ents[c["ent"]]
            conf = c["match_confidence"]
            if E["foreign"]:
                conf = "weak"
            matches.append({"match_confidence": conf, "match_basis": c["basis"], "legal_name": E["name"], "identifiers": E["ids"],
                            "address": E["addr"], "phones": [], "emails": [], "website": None, "status": E["status"],
                            "extra": dict(E["extra"], list=E["type"]), "source_url": E["source_url"], "dataset_url": E["dataset_url"],
                            "retrieved_at": E["retrieved"], "raw": E["raw"]})
    order = {"exact": 0, "strong": 1, "weak": 2}
    matches.sort(key=lambda m: order[m["match_confidence"]])
    if matches:
        out.write(v, matches[:6])
        for m in matches:
            if m["match_confidence"] in ("exact", "strong"):
                stats["es_" + m["extra"]["list"].split()[0]] += 1
res = out.close()
res.update(stats)
json.dump(res, open(C.WORK + "/health_canada_stats.json", "w"), indent=1)
print(json.dumps(res, indent=1))
