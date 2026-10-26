#!/usr/bin/env python3
"""Union Socrata catalog metadata, classify domains and datasets, pick location columns to probe.
usage: python3 -I classify_socrata.py <out_dir> <meta1.jsonl[.gz]> [meta2 ...]
Writes <out_dir>/socrata_classified.jsonl (every dataset with decision fields)."""
import sys, json, gzip, re, collections
out_dir = sys.argv[1]
NONUS = re.compile(r"\.ca$|\.au$|\.co$|\.uk$|gnb\.socrata|novascotia|thedatazone|waterpointdata|datos\.|calgary|edmonton|winnipeg|ontario\.demo", re.I)
FEDERAL = {"data.bts.gov", "data.cdc.gov", "data.energystar.gov", "data.permits.performance.gov", "datadiscovery.nlm.nih.gov",
           "datahub.hhs.gov", "datahub.transportation.gov", "datahub.usac.org", "nih-ncats.data.socrata.com", "opendata.fcc.gov",
           "priv-data.ojp.usdoj.gov", "www.datahub.va.gov", "data.medicaid.gov", "data.cms.gov", "data.healthcare.gov",
           "healthdata.gov", "data.hrsa.gov", "data.usaid.gov", "data.nasa.gov", "data.sba.gov", "data.consumerfinance.gov",
           "data.transportation.gov", "data.ed.gov", "data.seattle.gov.fed", "opendata.usac.org", "data.medicare.gov",
           "chronicdata.cdc.gov", "data.usajobs.gov", "data.doe.gov", "data.nal.usda.gov", "data.acf.hhs.gov"}
TESTLIKE = re.compile(r"\.demo\.socrata|qa-|sandbox|-train\.|^internal|internal-|internal\.|^iop\.|celebratingcities|fusioncenter|budget-qa", re.I)
REL = re.compile(r"contract|purchas|procure|vendor|supplier|payment|payee|expend|checkbook|check register|spend|invoice|"
                 r"encumb|award|ledger|disburs|agreement|\bbids?\b|solicitation|blanket|accounts payable|warrant|"
                 r"p-?card|obligation|requisition|consultant|lease|concession|transaction", re.I)
VEN = re.compile(r"vendor|vend_|^vend|supplier|payee|contractor|merchant|company|firm|business_?name|recipient|awardee|"
                 r"seller|provider|bidder|consultant|lessor|remit|^name$|^name1$|^payee|_name$|entity_name|organization_name|org_name|corporation|"
                 r"^organization$|fsmc|^entity$|^company$", re.I)
LOCPAT = re.compile(r"(^|_)(state|st|province|prov|country|ctry|cntry|zip|zipcode|zip5|zip_code|postal|postal_code|postalcode|"
                    r"postcode|city|address|addr|address1|address_1|address_line_1|region|state_province|st_prov)(_|$|\d)|"
                    r"(vendor|vend|ven|supplier|payee|contractor|merchant|remit|company|business)_?(state|st|country|ctry|zip|"
                    r"postal|province|city|address|addr)", re.I)
NOTLOC = re.compile(r"status|statement|estate|statewide|state_agency|agency_state|state_fund|state_share|state_amount|"
                    r"state_dollar|state_match|state_id$|stateid|fips|state_code_fips|interstate|state_aid|state_total|"
                    r"state_funds|state_portion|^ship|shipping|ship_to|deliver|site_|project_|property_|facility_|"
                    r"incident|location_1|geocoded|_location$|buyer_|customer_|agency_addr|dept_addr|department_addr|"
                    r"recipient_city|patient|student|employee|owner_|applicant_|permit|parcel|school_", re.I)
VLOC = re.compile(r"vendor|vend|^ven_|supplier|payee|contractor|merchant|remit|company|business", re.I)

def kind(field, name, dtype):
    f = (field or "").lower(); n = (name or "").lower()
    if (dtype or "").lower() not in ("", "text", "url"): return None
    s = f + " " + n
    if re.search(r"country|ctry|cntry", s): return "country"
    if re.search(r"zip|postal|postcode", s): return "zip"
    if re.search(r"state|province|(^|_)st($|_)|(^|_)prov($|_)|region", s): return "state"
    if re.search(r"address|addr", s): return "address"
    if re.search(r"city", s): return "city"
    return None

rows = {}
for p in sys.argv[2:]:
    op = gzip.open if p.endswith(".gz") else open
    with op(p, "rt", encoding="utf-8") as f:
        for l in f:
            j = json.loads(l)
            k = (j["domain"], j["id"])
            cols = j.get("cols_field") or j.get("cols") or []
            names = j.get("cols_name") or j.get("col_names") or []
            types = j.get("cols_type") or j.get("col_types") or []
            r = rows.setdefault(k, {"domain": j["domain"], "id": j["id"], "name": j.get("name"), "description": j.get("description") or "",
                                    "updatedAt": j.get("updatedAt"), "data_updated_at": j.get("data_updated_at"),
                                    "category": j.get("category"), "tags": j.get("tags") or [], "cols": cols, "col_names": names,
                                    "col_types": types, "provenance": j.get("provenance"), "type": j.get("type"),
                                    "hits": set()})
            if not r["cols"] and cols: r["cols"], r["col_names"], r["col_types"] = cols, names, types
            for h in (j.get("hits") or []): r["hits"].add(h)
stats = collections.Counter()
with open(out_dir + "/socrata_classified.jsonl", "w") as fo:
    for k, r in sorted(rows.items()):
        d = r["domain"]
        if NONUS.search(d): dec = "excluded:non_us_domain"
        elif d in FEDERAL or d.endswith(".fed.us"): dec = "excluded:federal_domain"
        elif TESTLIKE.search(d): dec = "excluded:demo_or_internal_domain"
        else: dec = None
        text = " ".join([r["name"] or "", r["description"][:400], r["category"] or "", " ".join(r["tags"]), " ".join(r["cols"])])
        rel = bool(REL.search(text))
        ven = [c for c in r["cols"] if VEN.search(c)]
        locs = []
        for i, c in enumerate(r["cols"]):
            nm = r["col_names"][i] if i < len(r["col_names"]) else ""
            ty = r["col_types"][i] if i < len(r["col_types"]) else ""
            if LOCPAT.search(c) and not NOTLOC.search(c):
                kd = kind(c, nm, ty)
                if kd: locs.append({"col": c, "name": nm, "type": ty, "kind": kd, "vendorish": bool(VLOC.search(c + " " + nm))})
        if dec is None:
            if r["type"] not in (None, "dataset"): dec = "excluded:not_tabular"
            elif not rel: dec = "no_contracts:not_procurement_related"
            elif not ven and not any(l["vendorish"] for l in locs): dec = "no_vendor_location:no_vendor_column"
            elif not locs: dec = "no_vendor_location:no_location_column"
            else: dec = "probe"
        stats[dec] += 1
        r["hits"] = sorted(r["hits"]); r["decision"] = dec; r["vendor_cols"] = ven; r["loc_cols"] = locs
        fo.write(json.dumps(r, ensure_ascii=False) + "\n")
for k, v in stats.most_common(): print(v, k)
