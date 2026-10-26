#!/usr/bin/env python3
"""Normalize SaskTenders awarded competitions (parsed from listing pages) -> schema records.
Vendor country: from the 'Award Details' location line ("City, SK", "Saskatoon SK", "Regina, Saskatchewan", ...):
a Canadian province/territory code or name must be present (postal code alone also accepted); never the name.
Usage: python3 -I normalize_sasktenders.py <competitions.jsonl> <retrieved_at> <out_jsonl> <stats_json>
"""
import json, re, sys, hashlib, datetime as dt, collections

INP, RETRIEVED, OUT, STATS = sys.argv[1:5]
REF = dt.date(2026, 10, 25)
PROV_CODES = {"AB", "BC", "SK", "MB", "ON", "QC", "PQ", "NB", "NS", "PE", "PEI", "NL", "NF", "YT", "NT", "NU"}
PROV_NAMES = {"alberta": "AB", "british columbia": "BC", "saskatchewan": "SK", "sask": "SK", "manitoba": "MB",
              "ontario": "ON", "ont": "ON", "quebec": "QC", "québec": "QC", "new brunswick": "NB", "nova scotia": "NS",
              "prince edward island": "PE", "newfoundland and labrador": "NL", "newfoundland": "NL", "yukon": "YT",
              "northwest territories": "NT", "nunavut": "NU"}
US_STATES = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}
POSTAL_RE = re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d\b", re.I)
SK_CITIES = {"saskatoon", "regina", "prince albert", "moose jaw", "swift current", "yorkton", "north battleford", "estevan",
             "weyburn", "lloydminster", "martensville", "warman", "melfort", "humboldt", "meadow lake", "melville", "kindersley",
             "nipawin", "la ronge", "tisdale", "rosetown", "emerald park", "white city", "pilot butte", "balgonie", "lumsden",
             "outlook", "unity", "esterhazy", "canora", "moosomin", "assiniboia", "biggar", "kamsack", "maple creek", "shaunavon",
             "wynyard", "watrous", "rosthern", "hudson bay", "carlyle", "indian head", "fort qu'appelle", "battleford", "langham",
             "dalmeny", "osler", "hague", "wadena", "foam lake", "gravelbourg", "spy hill", "corman park", "rm of sherwood"}


def parse_location(loc):
    """Return (country, region, postal, basis) or (None, ...) when no structured Canadian token found."""
    if not loc:
        return None, None, None, None
    s = loc.strip()
    low = s.lower()
    postal = POSTAL_RE.search(s)
    # explicit foreign country words
    if re.search(r"\b(usa|u\.s\.a\.|united states|us)\b", low) and not re.search(r"\bcanada\b", low):
        return "foreign", None, None, "location contains USA/US"
    for name, code in sorted(PROV_NAMES.items(), key=lambda x: -len(x[0])):
        if re.search(r"\b" + re.escape(name) + r"\b", low):
            return "CA", code, postal.group(0) if postal else None, "province name '%s' in award location %r" % (name, s)
    toks = re.findall(r"\b([A-Za-z]{2,3})\b\.?", s)
    for t in reversed(toks):
        T = t.upper()
        if T in PROV_CODES and t not in ("on", "On", "no", "No") or (T == "ON" and (t == "ON" or re.search(r",\s*On\b|\sOn$", s))):
            code = {"PQ": "QC", "PEI": "PE", "NF": "NL"}.get(T, T)
            return "CA", code, postal.group(0) if postal else None, "province code '%s' in award location %r" % (t, s)
    if postal:
        return "CA", None, postal.group(0), "Canadian postal code '%s' in award location %r" % (postal.group(0), s)
    if re.search(r"\bcanada\b", low):
        return "CA", None, None, "word 'Canada' in award location %r" % s
    for t in toks:
        if t.upper() in US_STATES and t.isupper():
            return "foreign", None, None, "US state code in location"
    return None, None, None, None


def pdate(s):
    if not s:
        return None
    s = s.strip().split("\n")[0]
    for fmt in ("%b %d, %Y", "%B %d, %Y"):
        try:
            return dt.datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            pass
    return None


def money(s):
    if not s:
        return None
    t = re.sub(r"[^\d.\-]", "", s)
    try:
        return float(t) if t not in ("", "-", ".") else None
    except ValueError:
        return None


def main():
    stats = collections.Counter()
    out = open(OUT, "w")
    for line in open(INP):
        c = json.loads(line)
        stats["competitions"] += 1
        if not c.get("award_details"):
            stats["skip_no_award_details"] += 1
            continue
        for i, a in enumerate(c["award_details"]):
            stats["award_rows"] += 1
            supplier = (a.get("supplier") or "").strip()
            if not supplier or supplier.lower() in ("n/a", "none", "no award", "cancelled"):
                stats["skip_no_supplier"] += 1
                continue
            country, region, postal, basis = parse_location(a.get("location"))
            if country == "foreign":
                stats["skip_foreign"] += 1
                continue
            if country is None:
                stats["skip_no_country_info"] += 1
                continue
            award_date = pdate(a.get("award_date"))
            if award_date and award_date > REF.isoformat():
                stats["skip_future_award"] += 1
                continue
            amount = money(a.get("amount"))
            opens = pdate(c.get("opens")); closes = pdate(c.get("closes"))
            rid = "ca_saskatchewan:%s:%d" % (c["competition_guid"], i)
            loc = (a.get("location") or "").strip()
            city = None
            if loc:
                city = re.split(r",", loc)[0].strip() if "," in loc else re.sub(r"\b(SK|Sk|Saskatchewan|Sask|AB|BC|MB|ON|QC|NS|NB|PE|NL|YT|NT|NU)\b\.?\s*$", "", loc).strip() or None
                if city and (POSTAL_RE.search(city) or city.lower() in PROV_NAMES):
                    city = None
            rec = {
                "record_id": rid,
                "source": {
                    "key": "ca_saskatchewan",
                    "name": "SaskTenders - awarded competitions (Government of Saskatchewan public tender portal)",
                    "publisher": "Government of Saskatchewan, Ministry of SaskBuilds and Procurement (SaskTenders)",
                    "dataset_url": "https://www.sasktenders.ca/Search?statusId=83773de3-960f-416f-a511-bbd76ff1812f",
                    "record_url": c["print_url"],
                    "retrieved_at": RETRIEVED,
                },
                "status": "end_date_unknown",
                "status_basis": "SaskTenders publishes only the award date (%s), opening and closing dates; there is no contract start/end/term field, so the end date is unknown." % award_date,
                "contract": {
                    "identifiers": {"competition_number": c.get("competition_number"), "competition_guid": c["competition_guid"]},
                    "title": c.get("competition_name"),
                    "description": c.get("synopsis"),
                    "instrument_type": "contract award (tender competition)",
                    "procurement_method": c.get("competition_type"),
                    "solicitation_procedure": c.get("competition_type"),
                    "commodity": {},
                    "value": amount, "currency": "CAD" if amount is not None else None,
                    "value_detail": {"award_amount": amount} if amount is not None else {},
                    "dates": {"published": opens, "signed": None, "start": None, "end": None, "amended_last": None,
                              "awarded": award_date, "tender_closing": closes},
                    "related": {"agreement_type": c.get("agreement_type"), "public_opening": c.get("public_opening"),
                                "documents": c.get("documents"), "awards_on_competition": len(c["award_details"]),
                                "award_index": i},
                },
                "buyer": {
                    "name": c.get("organization"), "country": "CA",
                    "type": "Saskatchewan public body (ministry, Crown corporation, health, education or municipality) as named",
                    "identifiers": {}, "address": {"response_address": c.get("response_address")},
                    "contact": {"name": c.get("contact_name"), "email": c.get("contact_email"), "phone": c.get("contact_phone")},
                },
                "vendor": {
                    "name": supplier, "country": "CA", "country_basis": basis,
                    "identifiers": {},
                    "address": {"line1": None, "city": city, "region": region, "postal_code": postal, "country": None, "location_as_published": loc or None},
                    "contact": {},
                },
                "raw": dict(c, award_detail=a),
            }
            if not rec["buyer"]["name"]:
                stats["skip_no_buyer"] += 1
                continue
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            stats["emitted"] += 1
            stats["emitted_year_" + (award_date or "unknown")[:4]] += 1
            stats["region_" + str(region)] += 1
    out.close()
    json.dump(dict(stats), open(STATS, "w"), indent=1)
    print(json.dumps(dict(stats), indent=1))


if __name__ == "__main__":
    main()
