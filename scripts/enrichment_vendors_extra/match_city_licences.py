#!/usr/bin/env python3
"""Match vendors to current municipal business-licence open data (Toronto, Calgary, Edmonton).  Organisations only:
licences whose licensee/business name looks like an individual's name are skipped; for home-based businesses the street
address is not carried (city only).  Toronto publishes a business phone, kept only for organisational licensees.
usage: python3 -I match_city_licences.py <download_dir> [cities=toronto,calgary,edmonton]
Writes enrichment/v2/vendors_extra_<city>_business_licences.jsonl."""
import sys, os, csv, json, re, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vx_common as C  # noqa: E402

D = sys.argv[1]
CITIES = (sys.argv[2] if len(sys.argv) > 2 else "toronto,calgary,edmonton").split(",")
csv.field_size_limit(10 ** 9)
vendors, meta = C.load_index()
need = C.need_map(vendors)
TODAY = "2026-10-25"


def rt(name):
    try:
        return open(os.path.join(D, name + "_retrieved_at.txt")).read().strip()
    except Exception:
        return None


def load_toronto():
    url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/57b2285f-4f80-45fb-ae3e-41a02c3a137f/resource/54bddc5e-92d9-4102-89c1-43e82f8f4d2d/download/business-licences-data.csv"
    page = "https://open.toronto.ca/dataset/municipal-licensing-and-standards-business-licences-and-permits/"
    rows, skipped = [], 0
    for r in csv.DictReader(open(os.path.join(D, "toronto_business_licences_data.csv"), encoding="utf-8", errors="replace")):
        client, oper = (r.get("Client Name") or "").strip(), (r.get("Operating Name") or "").strip()
        if not client and not oper:
            continue
        if client and C.looks_like_person(client):
            skipped += 1
            continue
        l2 = (r.get("Licence Address Line 2") or "").strip()
        m = re.match(r"^(.*?),\s*([A-Z]{2})$", l2)
        city, prov = (m.group(1), m.group(2)) if m else (l2 or None, None)
        cancel = (r.get("Cancel Date") or "").strip()
        ph = C.norm_phone(r.get("Business Phone"))
        if ph and (r.get("Business Phone Ext.") or "").strip():
            ph += " ext. " + r["Business Phone Ext."].strip()
        rows.append({"names": [n for n in (client, oper) if n], "legal_name": client or oper, "trade_name": oper or None, "licensee_names": [client] if client else [oper],
                     "line1": (r.get("Licence Address Line 1") or "").strip() or None, "city": city, "prov": prov,
                     "postal": (r.get("Licence Address Line 3") or "").strip() or None, "phone": ph, "home": False,
                     "licence": {"licence_no": r.get("Licence No."), "category": r.get("Category"), "issued": r.get("Issued"),
                                 "cancel_date": cancel or None, "last_record_update": r.get("Last Record Update"), "ward": r.get("Ward")},
                     "active": not cancel, "raw": {k: v for k, v in r.items() if v}})
    return rows, skipped, url, page


def load_calgary():
    url = "https://data.calgary.ca/api/views/vdjc-pybd/rows.csv?accessType=DOWNLOAD"
    page = "https://data.calgary.ca/Business-and-Economic-Activity/Calgary-Business-Licences/vdjc-pybd"
    rows, skipped = [], 0
    for r in csv.DictReader(open(os.path.join(D, "calgary_business_licences.csv"), encoding="utf-8", errors="replace")):
        nm = (r.get("TRADENAME") or "").strip()
        if not nm:
            continue
        if C.looks_like_person(nm):
            skipped += 1
            continue
        home = (r.get("HOMEOCCIND") or "").strip().upper() == "Y"
        exp = (r.get("EXP_DT") or "").replace("/", "-")
        raw = {k: v for k, v in r.items() if v and k not in ("GLOBALID",)}
        if home:
            raw.pop("ADDRESS", None)
            raw.pop("POINT", None)
        rows.append({"names": [nm], "licensee_names": [nm], "legal_name": nm, "trade_name": None, "line1": None if home else (r.get("ADDRESS") or None),
                     "city": "Calgary", "prov": "AB", "postal": None, "phone": None, "home": home,
                     "licence": {"business_id": r.get("GETBUSID"), "licence_types": r.get("LICENCETYPES"), "first_issued": r.get("FIRST_ISS_DT"),
                                 "expiry": r.get("EXP_DT"), "status": r.get("JOBSTATUSDESC"), "community_district": r.get("COMDISTNM"), "home_occupation": home},
                     "active": (r.get("JOBSTATUSDESC") or "").lower() in ("licensed", "renewal licensed", "pending renewal") or exp >= TODAY, "raw": raw})
    return rows, skipped, url, page


def load_edmonton():
    url = "https://data.edmonton.ca/api/views/qhi4-bdpu/rows.csv?accessType=DOWNLOAD"
    page = "https://data.edmonton.ca/Externally-Sourced-Datasets/City-of-Edmonton-Business-Licences/qhi4-bdpu"
    rows, skipped = [], 0
    for r in csv.DictReader(open(os.path.join(D, "edmonton_business_licences.csv"), encoding="utf-8", errors="replace")):
        nm = (r.get("Business Name") or "").strip()
        if not nm:
            continue
        if C.looks_like_person(nm):
            skipped += 1
            continue
        addr = (r.get("Business Address") or "").strip()
        home = addr.startswith("<") or (r.get("Licence Type") or "").lower().startswith("home")
        raw = {k: v for k, v in r.items() if v}
        if home:
            for k in ("Business Address", "Latitude", "Longitude", "Location", "Geometry Point"):
                raw.pop(k, None)
        rows.append({"names": [nm], "licensee_names": [nm], "legal_name": nm, "trade_name": None, "line1": None if home else (addr or None),
                     "city": "Edmonton", "prov": "AB", "postal": None, "phone": None, "home": home,
                     "licence": {"licence_no": r.get("Licence Number"), "category": r.get("Business Licence Category"), "most_recent_issue": r.get("Most Recent Issue Date"),
                                 "expiry": r.get("Expiry Date"), "original_issue": r.get("Original Issue Date"), "licence_type": r.get("Licence Type"),
                                 "duration": r.get("Licence Duration"), "neighbourhood": r.get("Neighbourhood"), "ward": r.get("Ward")},
                     "active": True, "raw": raw})
    return rows, skipped, url, page


LOADERS = {"toronto": load_toronto, "calgary": load_calgary, "edmonton": load_edmonton}
allstats = {}
for city in CITIES:
    rows, skipped, url, page = LOADERS[city]()
    ents = {}
    by_loose = collections.defaultdict(set)
    trade_count = collections.defaultdict(set)   # trade-name loose key -> distinct licensees using it
    for r in rows:
        sk, lk = C.name_keys(r["names"])
        lkn = {l for l in lk if l in need}
        if not lkn:
            continue
        p = C.norm_postal(r["postal"])
        key = (C.strict_key(r["legal_name"]), p or (r["line1"] or "").upper() or ("home" if r["home"] else ""))
        E = ents.setdefault(key, {"sk": set(), "lk": set(), "lic_sk": set(), "lic_lk": set(), "postals": set(), "cities": set(), "provs": set(), "streets": set(), "rows": []})
        E["sk"] |= sk
        E["lk"] |= lk
        lsk, llk = C.name_keys(r["licensee_names"])
        E["lic_sk"] |= lsk
        E["lic_lk"] |= llk
        for t in (r["trade_name"],):
            if t:
                trade_count[C.loose_key(t)].add(key[0])
        if p:
            E["postals"].add(p)
            for sn in C.street_numbers(r["line1"]):
                E["streets"].add((sn, p))
        c = C.norm_city(r["city"])
        if c:
            E["cities"].add(c)
        if r["prov"]:
            E["provs"].add(r["prov"])
        E["rows"].append(r)
        for l in lkn:
            by_loose[l].add(key)
    out = C.Out("%s_business_licences" % city)
    nphone = 0
    for v in vendors:
        keys = set()
        for l in v["lk"]:
            keys |= by_loose.get(l, set())
        if not keys:
            continue
        cl = [{"ent": k, "idmatch": None, "strict": bool(v["sk"] & ents[k]["sk"]), "lkey_match": True,
               "loc": C.loc_eval(v, ents[k]["postals"], ents[k]["cities"], ents[k]["provs"], ents[k]["streets"]),
               "lkey": next(iter(ents[k]["lk"]), ""), "rec_provs": ents[k]["provs"]} for k in keys]
        matches = []
        for c in C.grade(v, cl, local_dataset=True):
            E = ents[c["ent"]]
            if not (v["sk"] & E["lic_sk"]) and not (v["lk"] & E["lic_lk"]):
                # matched only on the operating/trade name: the licensee is another legal entity (franchisee, numbered company...)
                nlic = max([len(trade_count.get(l, ())) for l in (v["lk"] & E["lk"])] or [0])
                lic_name = E["rows"][0]["legal_name"]
                if nlic > 3:
                    c["match_confidence"] = "weak"
                    c["basis"] += "; matched on operating (trade) name only, used by %d different licensees (chain/franchise): licensee %r is not the vendor" % (nlic, lic_name)
                elif not c["loc"]["pe"]:
                    c["match_confidence"] = "weak"
                    c["basis"] += "; matched on operating (trade) name only, licensee is %r and no postal-code agreement" % lic_name
                else:
                    if c["match_confidence"] == "exact":
                        c["match_confidence"] = "strong"
                    c["basis"] += "; matched on operating (trade) name at the same postal code; licensee (legal entity) is %r" % lic_name
            rs = sorted(E["rows"], key=lambda r: (not r["active"], str(r["licence"].get("issued") or r["licence"].get("first_issued") or r["licence"].get("most_recent_issue") or "")), reverse=False)
            r0 = rs[0]
            phones = []
            for r in rs:
                if r["phone"] and r["phone"] not in phones:
                    phones.append(r["phone"])
            if phones and c["match_confidence"] in ("exact", "strong"):
                nphone += 1
            matches.append({"match_confidence": c["match_confidence"], "match_basis": c["basis"], "legal_name": r0["legal_name"],
                            "identifiers": {"licence_numbers": [r["licence"].get("licence_no") or r["licence"].get("business_id") for r in rs][:20]},
                            "address": {"line1": r0["line1"], "city": r0["city"], "region": r0["prov"], "postal_code": r0["postal"], "country": "CA",
                                        "note": "home-based business: street address not carried" if r0["home"] else None},
                            "phones": phones, "emails": [], "website": None,
                            "status": "active licence on file" if any(r["active"] for r in rs) else "all licences cancelled/expired",
                            "extra": {"trade_names": sorted({r["trade_name"] for r in rs if r["trade_name"]}), "licences": [r["licence"] for r in rs][:20],
                                      "licence_count": len(rs), "phone_label": "business phone published in the City of Toronto business licence data" if phones else None},
                            "source_url": page, "dataset_url": url, "retrieved_at": rt(city), "raw": [r["raw"] for r in rs][:20]})
        out.write(v, matches)
    res = out.close()
    res.update({"rows": len(rows), "skipped_individual_rows": skipped, "candidate_entities": len(ents), "vendors_exact_strong_with_phone": nphone})
    allstats[city] = res
    print(city, json.dumps(res), file=sys.stderr, flush=True)
json.dump(allstats, open(C.WORK + "/city_licences_stats.json", "w"), indent=1)
print(json.dumps(allstats, indent=1))
