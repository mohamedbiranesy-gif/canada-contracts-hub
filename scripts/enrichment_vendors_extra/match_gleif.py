#!/usr/bin/env python3
"""Match vendors to GLEIF LEI records concerning Canada (golden copy 20261026-0000, filtered by gleif_filter.py).

usage: python3 -I match_gleif.py <gleif_dir>
Exact joins: registration-authority / validation-authority entity IDs equal to the vendor's federal corporation number (RA000072),
NEQ (RA000081/RA000842), BC registration number (RA000074/RA000833) or BN9 (BN-shaped IDs) taken from the vendor's exact/strong
Corporations Canada / REQ / OrgBook matches (or an NEQ published in the contract data).  Name matching otherwise (legal + other names,
legal/HQ address for location agreement).  Writes enrichment/v2/vendors_extra_gleif.jsonl.
"""
import sys, os, re, json, gzip, collections, random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vx_common as C  # noqa: E402

D = sys.argv[1]
RETRIEVED = open(os.path.join(D, "retrieved_at.txt")).read().strip()
DATASET = "https://www.gleif.org/en/lei-data/gleif-golden-copy/download-the-golden-copy (golden copy 20261026-0000: lei2, rr, repex)"
RA = {d["id"]: (d["attributes"].get("internationalOrganizationName") or "") + ((" - " + d["attributes"]["internationalName"]) if d["attributes"].get("internationalName") else "")
      for d in json.load(open(os.path.join(D, "registration_authorities.json")))}
try:
    ELF = json.load(open(os.path.join(D, "elf_codes_ca.json")))
except Exception:
    ELF = {}
ELF.update({"8888": {"names": ["(other legal form - see OtherLegalForm)"]}, "9999": {"names": ["(legal form not provided)"]}})

vendors, meta = C.load_index()
need = C.need_map(vendors)
print("vendors", len(vendors), meta, file=sys.stderr, flush=True)

# ---------------------------------------------------------------- load GLEIF CA records
recs = {}
by_id = collections.defaultdict(set)
by_loose = collections.defaultdict(set)
NAME_COLS = ["Entity.LegalName"] + ["Entity.OtherEntityNames.OtherEntityName.%d" % i for i in range(1, 6)] + \
            ["Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.%d" % i for i in range(1, 6)]


def ra_pairs(d):
    out = [(d.get("Entity.RegistrationAuthority.RegistrationAuthorityID"), d.get("Entity.RegistrationAuthority.RegistrationAuthorityEntityID"), "registration authority")]
    out.append((d.get("Registration.ValidationAuthority.ValidationAuthorityID"), d.get("Registration.ValidationAuthority.ValidationAuthorityEntityID"), "validation authority"))
    for i in range(1, 6):
        out.append((d.get("Registration.OtherValidationAuthorities.OtherValidationAuthority.%d.ValidationAuthorityID" % i),
                    d.get("Registration.OtherValidationAuthorities.OtherValidationAuthority.%d.ValidationAuthorityEntityID" % i), "other validation authority"))
    return [(a, e, w) for a, e, w in out if a and e]


def id_keys(ra, eid):
    keys = []
    s = re.sub(r"[\s\-\.]", "", eid.upper())
    if ra == "RA000072" and re.fullmatch(r"\d{5,9}", s):
        keys.append(("cc", s.lstrip("0")))
    if ra == "RA000081" and re.fullmatch(r"\d{10}", s):
        keys.append(("neq", s))
    if ra in ("RA000074", "RA000833") and re.fullmatch(r"[A-Z]{0,2}\d{6,8}", s):
        keys.append(("bc", s))
    m = re.fullmatch(r"(\d{9})(?:[A-Z]{2}\d{3,4})?", s)
    if m and not s.startswith("0"):
        keys.append(("bn9", m.group(1)))
    return keys


def addr(d, pfx):
    a = {k: d.get(pfx + "." + k) for k in ("FirstAddressLine", "AddressNumber", "AddressNumberWithinBuilding", "MailRouting",
                                           "AdditionalAddressLine.1", "AdditionalAddressLine.2", "AdditionalAddressLine.3", "City", "Region", "Country", "PostalCode")}
    if not any(a.values()):
        return None
    line2 = ", ".join(x for x in (a["AdditionalAddressLine.1"], a["AdditionalAddressLine.2"], a["AdditionalAddressLine.3"]) if x) or None
    reg = a["Region"] or ""
    return {"line1": " ".join(x for x in (a["AddressNumber"], a["FirstAddressLine"]) if x) or None, "line2": line2,
            "mail_routing": a["MailRouting"], "unit": a["AddressNumberWithinBuilding"], "city": a["City"],
            "region": reg.split("-", 1)[1] if reg.startswith(a["Country"] or "##") and "-" in reg else (reg or None),
            "region_iso": reg or None, "postal_code": a["PostalCode"], "country": a["Country"]}


with gzip.open(os.path.join(D, "lei2_ca.jsonl.gz"), "rt", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        if d.get("Registration.RegistrationStatus") in ("DUPLICATE", "ANNULLED"):
            continue
        lei = d["LEI"]
        names = [d.get(c) for c in NAME_COLS if d.get(c)]
        sk, lk = C.name_keys(names)
        la, ha = addr(d, "Entity.LegalAddress"), addr(d, "Entity.HeadquartersAddress")
        postals, cities, provs, streets = set(), set(), set(), set()
        for a in (la, ha):
            if not a or a["country"] != "CA":
                continue
            p = C.norm_postal(a["postal_code"])
            if p:
                postals.add(p)
                for sn in C.street_numbers(a["line1"]):
                    streets.add((sn, p))
            c = C.norm_city(a["city"])
            if c:
                cities.add(c)
            pr = C.norm_prov(a["region"])
            if pr:
                provs.add(pr)
        hit = False
        for l in lk:
            if l in need:
                by_loose[l].add(lei)
                hit = True
        ids = []
        for ra, eid, why in ra_pairs(d):
            for k in id_keys(ra, eid):
                by_id[k].add(lei)
                ids.append((k, ra, eid, why))
        recs[lei] = {"d": d, "sk": sk, "lk": lk, "postals": postals, "cities": cities, "provs": provs, "streets": streets, "la": la, "ha": ha, "ids": ids}
print("gleif CA records", len(recs), "name keys hit", len(by_loose), "id keys", len(by_id), file=sys.stderr, flush=True)

# relationships / exceptions / related non-CA entities
related = {}
with gzip.open(os.path.join(D, "lei2_related.jsonl.gz"), "rt", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        related[d["LEI"]] = d
rels_of = collections.defaultdict(list)     # child LEI -> relationship rows (as start node)
children_of = collections.defaultdict(list)  # parent LEI -> rows (as end node)
with gzip.open(os.path.join(D, "rr_ca.jsonl.gz"), "rt", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        rels_of[d["Relationship.StartNode.NodeID"]].append(d)
        children_of[d["Relationship.EndNode.NodeID"]].append(d)
repex = collections.defaultdict(list)
with gzip.open(os.path.join(D, "repex_ca.jsonl.gz"), "rt", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        repex[d["LEI"]].append(d)


def ent_brief(lei):
    if lei in recs:
        d = recs[lei]["d"]
    else:
        d = related.get(lei) or {}
    return {"lei": lei, "name": d.get("Entity.LegalName"), "legal_country": d.get("Entity.LegalAddress.Country"),
            "legal_city": d.get("Entity.LegalAddress.City"), "hq_country": d.get("Entity.HeadquartersAddress.Country"),
            "entity_status": d.get("Entity.EntityStatus"), "registration_status": d.get("Registration.RegistrationStatus"),
            "gleif_url": "https://search.gleif.org/#/record/%s" % lei}


def rel_info(lei):
    out = {"direct_parent": None, "ultimate_parent": None, "fund_manager": [], "branch_of": None, "subfund_of": None, "feeder_to": None}
    for r in rels_of.get(lei, []):
        t = r.get("Relationship.RelationshipType")
        b = ent_brief(r["Relationship.EndNode.NodeID"])
        b.update({"relationship_status": r.get("Relationship.RelationshipStatus"), "relationship_start": r.get("Relationship.Period.1.startDate"),
                  "validation": r.get("Registration.ValidationSources"), "accounting_standard": r.get("Relationship.Qualifiers.1.QualifierCategory"),
                  "relationship_registration_status": r.get("Registration.RegistrationStatus")})
        if t == "IS_DIRECTLY_CONSOLIDATED_BY":
            out["direct_parent"] = b
        elif t == "IS_ULTIMATELY_CONSOLIDATED_BY":
            out["ultimate_parent"] = b
        elif t == "IS_FUND-MANAGED_BY":
            out["fund_manager"].append(b)
        elif t == "IS_INTERNATIONAL_BRANCH_OF":
            out["branch_of"] = b
        elif t == "IS_SUBFUND_OF":
            out["subfund_of"] = b
        elif t == "IS_FEEDER_TO":
            out["feeder_to"] = b
    ch = []
    for r in children_of.get(lei, []):
        if r.get("Relationship.RelationshipType") in ("IS_DIRECTLY_CONSOLIDATED_BY", "IS_ULTIMATELY_CONSOLIDATED_BY", "IS_INTERNATIONAL_BRANCH_OF"):
            b = ent_brief(r["Relationship.StartNode.NodeID"])
            b["relationship"] = r.get("Relationship.RelationshipType")
            ch.append(b)
    out["children_count"] = len(ch)
    out["children"] = ch[:25]
    out["reporting_exceptions"] = [{"category": x.get("Exception.Category"), "reasons": [x.get("Exception.Reason.%d" % i) for i in range(1, 6) if x.get("Exception.Reason.%d" % i)]}
                                   for x in repex.get(lei, [])]
    return out


BN15_RE = re.compile(r"(\d{9})([A-Z]{2})(\d{4})")


def record(lei, conf, basis, v=None):
    R = recs[lei]
    d = R["d"]
    ra_id = d.get("Entity.RegistrationAuthority.RegistrationAuthorityID")
    eid = d.get("Entity.RegistrationAuthority.RegistrationAuthorityEntityID")
    ident = {"lei": lei, "registration_authority_id": ra_id, "registration_authority_name": RA.get(ra_id),
             "registration_authority_other": d.get("Entity.RegistrationAuthority.OtherRegistrationAuthorityID"),
             "registration_authority_entity_id": eid, "legal_jurisdiction": d.get("Entity.LegalJurisdiction")}
    vbn = set((v or {}).get("ids", {}).get("bn9", {}).keys())
    for (kind, val), ra, e, why in R["ids"]:
        if kind != "bn9":
            ident.setdefault({"cc": "corporation_number", "neq": "neq", "bc": "bc_registration_number"}[kind], val)
            continue
        # A bare 9-digit authority ID is usually a provincial number (Ontario BIN, Alberta/Saskatchewan corporate numbers), not a
        # CRA Business Number.  It is labelled a BN only when the record itself shows BN form (BN9 + 2-letter program + 4 digits),
        # when the authority is the CRA (RA001121), or when it equals a BN9 already known for this vendor (Corporations Canada/OrgBook).
        s = re.sub(r"[\s\-\.]", "", e.upper())
        m15 = BN15_RE.fullmatch(s)
        if m15:
            ident.setdefault("business_number_bn9", val)
            ident.setdefault("cra_program_account", "%s%s%s" % m15.groups())
            ident.setdefault("business_number_basis", "BN with CRA program account published as the GLEIF %s ID (%s)" % (why, ra))
        elif ra == "RA001121":
            ident.setdefault("business_number_bn9", val)
            ident.setdefault("business_number_basis", "9-digit ID published under the Canada Revenue Agency authority (RA001121)")
        elif val in vbn:
            ident.setdefault("business_number_bn9", val)
            ident.setdefault("business_number_basis", "GLEIF %s ID (%s) equals the BN9 already known for this vendor" % (why, ra))
    validation = [{"authority_id": a, "authority_name": RA.get(a), "entity_id": e, "role": w} for a, e, w in ra_pairs(d)]
    other_names = [{"name": d.get(c), "type": d.get(c + ".type"), "lang": d.get(c + ".xmllang")} for c in NAME_COLS[1:] if d.get(c)]
    la, ha = R["la"], R["ha"]
    address = dict(la or {})
    address["headquarters"] = ha
    others = []
    for i in range(1, 6):
        oa = addr(d, "Entity.OtherAddresses.OtherAddress.%d" % i)
        if oa:
            oa["type"] = d.get("Entity.OtherAddresses.OtherAddress.%d.type" % i)
            others.append(oa)
    if others:
        address["other_addresses"] = others
    elf = d.get("Entity.LegalForm.EntityLegalFormCode")
    rel = rel_info(lei)
    raw = {"lei_record": d, "relationship_records": rels_of.get(lei, []) + [r for r in children_of.get(lei, [])][:25], "reporting_exceptions": repex.get(lei, [])}
    return {"match_confidence": conf, "match_basis": basis, "legal_name": d.get("Entity.LegalName"), "identifiers": ident,
            "address": address, "phones": [], "emails": [], "website": None,
            "status": "entity %s; LEI registration %s" % (d.get("Entity.EntityStatus"), d.get("Registration.RegistrationStatus")),
            "extra": {"other_names": other_names, "legal_form_code": elf, "legal_form_name": (ELF.get(elf) or {}).get("names"),
                      "legal_form_other": d.get("Entity.LegalForm.OtherLegalForm"), "entity_category": d.get("Entity.EntityCategory"),
                      "entity_sub_category": d.get("Entity.EntitySubCategory"), "entity_creation_date": d.get("Entity.EntityCreationDate"),
                      "entity_expiration_date": d.get("Entity.EntityExpirationDate"), "entity_expiration_reason": d.get("Entity.EntityExpirationReason"),
                      "successor": [x for x in [d.get("Entity.SuccessorEntity.1.SuccessorLEI"), d.get("Entity.SuccessorEntity.1.SuccessorEntityName")] if x] or None,
                      "initial_registration_date": d.get("Registration.InitialRegistrationDate"), "last_update_date": d.get("Registration.LastUpdateDate"),
                      "next_renewal_date": d.get("Registration.NextRenewalDate"), "managing_lou": d.get("Registration.ManagingLOU"),
                      "validation_sources": d.get("Registration.ValidationSources"), "authorities": validation,
                      "direct_parent": rel["direct_parent"], "ultimate_parent": rel["ultimate_parent"], "fund_manager": rel["fund_manager"] or None,
                      "branch_of": rel["branch_of"], "subfund_of": rel["subfund_of"], "feeder_to": rel["feeder_to"],
                      "children_count": rel["children_count"], "children": rel["children"], "reporting_exceptions": rel["reporting_exceptions"],
                      "conformity_flag": d.get("ConformityFlag")},
            "source_url": "https://search.gleif.org/#/record/%s" % lei, "api_url": "https://api.gleif.org/api/v1/lei-records/%s" % lei,
            "dataset_url": DATASET, "retrieved_at": RETRIEVED, "raw": raw}


def name_overlap(v, R):
    vt = set(" ".join(v["lk"]).split()) - C.GENERIC
    rt = set(" ".join(R["lk"]).split()) - C.GENERIC
    return bool(vt & rt) or bool(v["lk"] & R["lk"])


out = C.Out("gleif")
stats = collections.Counter()
KIND_LABEL = {"cc": "federal corporation number", "neq": "NEQ", "bc": "BC registration number", "bn9": "Business Number (BN9)"}
for i, v in enumerate(vendors):
    cand = {}
    # identifier joins
    for kind in ("cc", "neq", "bc", "bn9"):
        for val, (conf, why) in v["ids"][kind].items():
            key = (kind, val.lstrip("0") if kind == "cc" else val)
            for lei in by_id.get(key, ()):
                R = recs[lei]
                src = next(((ra, e, w) for k, ra, e, w in R["ids"] if k == key), None)
                ok = name_overlap(v, R)
                if kind == "bn9" and src and src[0] not in ("RA001121", "RA888888") and not re.search(r"[A-Z]{2}\d{3,4}$", re.sub(r"\s", "", src[1].upper())) and not ok:
                    continue  # bare 9-digit provincial number that happens to equal the BN9, names unrelated
                basis = "GLEIF %s %s entity ID %s (%s) equals the %s; %s" % (src[2] if src else "", src[0] if src else "", src[1] if src else val, RA.get(src[0], "") if src else "", why, "names consistent" if ok else "NAMES DIFFER")
                idm = (conf if ok else "weak", basis)
                prev = cand.get(lei)
                if prev is None or not prev.get("idmatch") or (prev["idmatch"][0] != "exact" and idm[0] == "exact"):
                    cand[lei] = {"ent": lei, "idmatch": idm}
    C.resolve_id_ambiguity(cand)
    # name candidates
    for l in v["lk"]:
        for lei in by_loose.get(l, ()):
            cand.setdefault(lei, {"ent": lei, "idmatch": None})
    if not cand:
        continue
    clist = []
    for lei, c in cand.items():
        R = recs[lei]
        c["strict"] = bool(v["sk"] & R["sk"])
        c["lkey_match"] = bool(v["lk"] & R["lk"])
        c["loc"] = C.loc_eval(v, R["postals"], R["cities"], R["provs"], R["streets"])
        c["lkey"] = next(iter(R["lk"]), "")
        c["rec_provs"] = R["provs"]
        if not c["idmatch"] and not c["lkey_match"]:
            continue
        clist.append(c)
    graded = C.grade(v, clist)
    matches = []
    for c in graded:
        st = recs[c["ent"]]["d"].get("Registration.RegistrationStatus")
        matches.append(record(c["ent"], c["match_confidence"], c["basis"], v))
        stats["id_join" if c.get("idmatch") else "name"] += 1
    out.write(v, matches)
    if matches:
        b = matches[0]["match_confidence"]
        stats["v_" + b] += 1
        if b in ("exact", "strong"):
            stats["v_es_with_parent"] += bool(matches[0]["extra"]["direct_parent"] or matches[0]["extra"]["ultimate_parent"])
            stats["v_es_hm"] += bool(v["rc_hm"])
            stats["v_es_idjoin"] += "equals the" in matches[0]["match_basis"]
    if i % 20000 == 0:
        print(i, dict(stats), file=sys.stderr, flush=True)
res = out.close()
res.update(dict(stats))
json.dump(res, open(C.WORK + "/gleif_stats.json", "w"), indent=1)
print(json.dumps(res, indent=1))
