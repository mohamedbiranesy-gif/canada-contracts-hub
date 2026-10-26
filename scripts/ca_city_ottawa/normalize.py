#!/usr/bin/env python3
"""City of Ottawa - 'Contracts awarded under delegation of authority' open-data feature services.
Nine half-year datasets (2022 H2 .. 2025 H2; separate Transit Commission tables for 2022-2024).
Fields: Item, Contract (number), Department, [Service], Description, Professional/Consulting Services designation,
Contract Approval Request Type (Initial/Amendment/Extension...), Amount, Vendor, Non-Competitive Rationale.
No vendor address/country is published -> records go ONLY to the unverified-country file
(vendor.country = null, country_basis = 'not published'). Status: duration parsed from Description when it
states a period (e.g. 'for a three-year period'); else end_date_unknown. Start anchored to the reporting half-year END
(the award date itself is not published; the dataset covers approvals in that half-year).
Usage: python3 -I normalize.py <downloads_dir> <normalized_dir>
"""
import sys, os, re, json, glob, collections, calendar
from datetime import date

REF = date(2026, 10, 25)
dl, outdir = sys.argv[1], sys.argv[2]
out_unv = os.path.join(outdir, "ca_city_ottawa_unverified_country.jsonl")

DATASETS = {
    "Contracts_25000_Awarded_DOA_Jul_Dec_2025": ("2025-07-01", "2025-12-31", "2025 Contracts Awarded greater than 25,000 Jul - Dec", "6d5248355ab64d49a3222f512710ebb7", "all departments"),
    "2025_Contracts_Awarded_greater_than_25000_Jan_-_Jun": ("2025-01-01", "2025-06-30", "2025 Contracts Awarded greater than 25,000 Jan - Jun", "14cca5b087f74d2d9eadc018c261d1b3", "all departments"),
    "Contracts_awarded_for_Q3_Q4_2024": ("2024-07-01", "2024-12-31", "2024 Contracts Awarded greater than 25,000 Jul - Dec", "31cafa0179134a859d57f1c14f516fe3", "all departments"),
    "Contracts_awarded_under_delegation_of_authority_for_Jan_June_2024_AODA_All_Departments": ("2024-01-01", "2024-06-30", "Contracts awarded under delegation of authority for Jan - June 2024 - All Departments", "64dfc00c6fab486eb0a45d6fe36efe51", "all departments"),
    "Contracts_awarded_under_delegation_of_authority_for_the_period_July_Dec_2023_AODA": ("2023-07-01", "2023-12-31", "Contracts awarded under delegation of authority for the period July-Dec 2023", "bd7380d28f7d4857a5d51cda4e752d61", "all departments"),
    "Ottawa_and_Open_data_Contracts_awarded_under_DA_January_1_2023_to_June_30_2023_AODA": ("2023-01-01", "2023-06-30", "Contracts awarded under DA January 1 2023 to June 30 2023", "d0c227869bb84d6999abb24eadb069c5", "all departments"),
    "Transit_Contracts_awarded_under_DOA_for_the_period_of_January1_2024_to_June_30_2024": ("2024-01-01", "2024-06-30", "Transit Contracts awarded under DOA for the period of Jan 1, 2024 - Jun 30, 2024", "ab9cb1e837b342ec917c7bf6351333af", "Transit Commission"),
    "Ottawa_and_Open_Data_Document_1___Contracts_for_Q3_Q4_2023_for_Transit_Commission_AODA": ("2023-07-01", "2023-12-31", "Contracts for Q3-Q4 2023 for Transit Commission", "ef5c0369926a49c48c8330d4627cde28", "Transit Commission"),
    "_Transit_Contracts_awarded_under_DOA_Q3_and_Q4_2022": ("2022-07-01", "2022-12-31", "Transit Contracts awarded under DOA Q3 and Q4 2022", "1063c22c959849008645b0b5c0c0b235", "Transit Commission"),
}

WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
         "eleven": 11, "twelve": 12, "eighteen": 18, "twenty": 20, "twenty-four": 24, "thirty-six": 36}
DUR_RE = re.compile(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|eighteen|twenty|\d{1,3})[\s\-?‐-―]*(?:\(\d+\)\s*)?[\-?‐-―\s]*(year|month|week)s?[\s\-?‐-―]*period", re.I)
DUR_RE2 = re.compile(r"\bfor\s+(?:a\s+|an\s+)?(?:period\s+of\s+)?(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|eighteen|twenty|\d{1,3})[\s\-?‐-―]*(?:\(\d+\)\s*)?(year|month|week)s?\b", re.I)


def parse_duration_months(desc):
    if not desc:
        return None, None
    d = desc.replace("?", "-")
    m = DUR_RE.search(d) or DUR_RE2.search(d)
    if not m:
        return None, None
    n = m.group(1).lower()
    n = WORDS.get(n) or (int(n) if n.isdigit() else None)
    if not n:
        return None, None
    unit = m.group(2).lower()
    months = n * 12 if unit == "year" else (n if unit == "month" else None)
    if unit == "week":
        months = round(n * 7 / 30.4, 2)
    return months, m.group(0)


def add_months(d, n):
    n_int = int(n) if float(n).is_integer() else None
    if n_int is None:
        from datetime import timedelta
        return d + timedelta(days=int(n * 30.4))
    y = d.year + (d.month - 1 + n_int) // 12
    mo = (d.month - 1 + n_int) % 12 + 1
    return date(y, mo, min(d.day, calendar.monthrange(y, mo)[1]))


def money(s):
    if s is None:
        return None
    m = re.search(r"([\d,]+(?:\.\d+)?)", str(s))
    try:
        return float(m.group(1).replace(",", "")) if m else None
    except Exception:
        return None


def pick(attrs, *cands):
    for c in cands:
        for k, v in attrs.items():
            if k.replace("_", "").lower() == c.replace("_", "").lower():
                return v
    return None


stats = collections.Counter()
by_status = collections.Counter()
n = 0
with open(out_unv, "w") as fo:
    for svc, (p_start, p_end, title, item_id, scope) in DATASETS.items():
        path = os.path.join(dl, svc + ".json")
        if not os.path.exists(path):
            stats["missing_" + svc] += 1
            continue
        d = json.load(open(path))
        pe = date.fromisoformat(p_end)
        ps = date.fromisoformat(p_start)
        for feat in d.get("features", []):
            a = feat["attributes"]
            stats["rows"] += 1
            vendor = (pick(a, "Vendor") or "").strip()
            if not vendor:
                stats["no_vendor"] += 1
                continue
            contract_no = (pick(a, "Contract", "Contract_") or "").strip()
            desc = pick(a, "Description") or ""
            amt = pick(a, "Amount", "F_Amount_")
            rtype = pick(a, "Contract_Approval_Request_Type", "Contract_Approval__Request_Type", "Contract_Approval_Request__Type")
            prof = pick(a, "Professional_Consulting_Services", "Professional_Consulting_Service", "Professional_Consulting__Servic", "Professional__Consulting_Servic", "Professional_Services_Designati")
            dept = (pick(a, "Department") or "").replace("\n", " ").strip()
            service = pick(a, "Service")
            ncr = pick(a, "Non_Competitive_Rationale", "Non_Competitive__Rationale")
            item = pick(a, "Item", "Item_", "Item__")
            oid = pick(a, "ObjectId", "FID")
            months, dur_txt = parse_duration_months(desc)
            if months:
                # the approval happened some time in [p_start, p_end]; earliest possible end = p_start + duration
                end_lo = add_months(ps, months)
                end_hi = add_months(pe, months)
                if end_hi < REF:
                    stats["excluded_ended_by_duration"] += 1
                    continue
                if end_lo >= REF:
                    status = "ongoing_inferred"
                    basis = (f"Award approved in reporting half-year {p_start}..{p_end}; description states {dur_txt!r} ({months} months); "
                             f"even from the period start, end >= {end_lo.isoformat()} >= 2026-10-25 (latest possible end {end_hi.isoformat()}). No explicit dates published.")
                else:
                    status = "ongoing_inferred"
                    basis = (f"Award approved in reporting half-year {p_start}..{p_end}; description states {dur_txt!r} ({months} months); "
                             f"inferred end between {end_lo.isoformat()} and {end_hi.isoformat()}, which straddles 2026-10-25 (uncertain). No explicit dates published.")
                    stats["straddling"] += 1
            else:
                status = "end_date_unknown"
                basis = f"Award approved in reporting half-year {p_start}..{p_end}; no dates, duration or term published for this row."
            rid = f"ca_city_ottawa:{svc}:{oid}"
            rec = {
                "record_id": rid,
                "source": {
                    "key": "ca_city_ottawa",
                    "name": f"City of Ottawa Open Data - {title}",
                    "publisher": "City of Ottawa (Finance and Corporate Services, Supply Services)",
                    "dataset_url": f"https://open.ottawa.ca/datasets/{item_id}",
                    "record_url": f"https://services.arcgis.com/G6F8XLCl5KtAlZ2G/arcgis/rest/services/{svc}/FeatureServer/0/query?where=OBJECTID%3D{oid}&outFields=*&f=json" if oid is not None else None,
                    "retrieved_at": "2026-10-25T17:57:30Z",
                },
                "status": status,
                "status_basis": basis,
                "contract": {
                    "identifiers": {"contract_number": contract_no or None, "item": item, "objectid": oid, "dataset": svc},
                    "title": desc[:160] if desc else None,
                    "description": desc or None,
                    "instrument_type": ("standing offer" if re.search(r"standing offer", desc, re.I) else "contract"),
                    "procurement_method": ("non-competitive" if ncr else None),
                    "solicitation_procedure": rtype,
                    "commodity": {"ottawa_professional_consulting_designation": prof},
                    "value": money(amt),
                    "currency": "CAD",
                    "value_detail": {"amount_as_published": amt, "approval_request_type": rtype},
                    "dates": {"published": None, "signed": None, "start": None, "end": None, "amended_last": None,
                              "approval_period_start": p_start, "approval_period_end": p_end},
                    "related": {"non_competitive_rationale": ncr, "duration_text": dur_txt, "duration_months": months, "service_area": service},
                },
                "buyer": {"name": "City of Ottawa" + (f" - {dept}" if dept else ""), "country": "CA", "type": "city",
                          "identifiers": {}, "address": {"city": "Ottawa", "region": "ON", "country": "CA"}, "contact": {},
                          "department": dept or None, "scope": scope},
                "vendor": {"name": vendor, "country": None, "country_basis": "not published",
                           "identifiers": {}, "address": {}, "contact": {}},
                "raw": a,
            }
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
            by_status[status] += 1
stats["records"] = n
print(json.dumps({"stats": dict(stats), "by_status": dict(by_status)}, indent=1))
json.dump({"stats": dict(stats), "by_status": dict(by_status)}, open(os.path.join(dl, "normalize_stats.json"), "w"), indent=1)
