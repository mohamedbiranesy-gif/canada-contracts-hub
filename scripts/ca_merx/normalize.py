#!/usr/bin/env python3
"""Normalize MERX public award notices into SCHEMA.md records.
Input : <downloads>/details.jsonl (award tab + optional notice tab), listing rows embedded.
Output: normalized/ca_merx.jsonl  (awardee address country == Canada)
        <downloads>/normalize_stats.json
One record per awardee (a solicitation can have several awardees).
Usage: python3 -I normalize.py <downloads_dir> <normalized_dir>
"""
import sys, os, re, json, collections
sys.path.insert(0, "scripts/_muni")
import terms
from datetime import date

REF = date(2026, 10, 25)
dl, outdir = sys.argv[1], sys.argv[2]
out_main = os.path.join(outdir, "ca_merx.jsonl")
out_unv = os.path.join(outdir, "ca_merx_unverified_country.jsonl")
fu = open(out_unv, "w")
by_status_unv = collections.Counter()

PROV = {"ontario": "ON", "quebec": "QC", "québec": "QC", "british columbia": "BC", "alberta": "AB", "manitoba": "MB",
        "saskatchewan": "SK", "nova scotia": "NS", "new brunswick": "NB", "newfoundland and labrador": "NL",
        "newfoundland": "NL", "prince edward island": "PE", "yukon": "YT", "northwest territories": "NT", "nunavut": "NU"}


def pdate(s):
    """'2026/11/01' or '2026/10/23 12:00:00 AM EDT' -> date"""
    if not s:
        return None
    m = re.search(r"(\d{4})/(\d{2})/(\d{2})", s)
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except Exception:
        return None


def money(s):
    if not s:
        return None
    m = re.search(r"([\d,]+(?:\.\d+)?)", s)
    if not m:
        return None
    try:
        return float(m.group(1).replace(",", ""))
    except Exception:
        return None


def parse_address(lines):
    """MERX address block: [street..., 'City, Province, Postal', 'Country'] (variants exist)."""
    a = {"line1": None, "city": None, "region": None, "region_as_published": None, "postal_code": None, "country": None}
    if not lines:
        return a
    lines = [l.strip() for l in lines if l and l.strip()]
    if not lines:
        return a
    a["country"] = lines[-1]
    if len(lines) >= 2:
        cpp = lines[-2]
        parts = [p.strip() for p in cpp.split(",")]
        # try: City, Province, Postal
        if len(parts) >= 3:
            a["city"] = parts[0]
            a["region_as_published"] = parts[1]
            a["postal_code"] = parts[2]
        elif len(parts) == 2:
            a["city"] = parts[0]
            a["region_as_published"] = parts[1]
        else:
            a["city"] = cpp
        pc = re.search(r"\b([A-Z]\d[A-Z]\s?\d[A-Z]\d)\b", cpp)
        if pc:
            a["postal_code"] = pc.group(1)
        if a["region_as_published"]:
            a["region"] = PROV.get(a["region_as_published"].lower(), a["region_as_published"])
    if len(lines) >= 3:
        a["line1"] = "; ".join(lines[:-2])
    return a


def buyer_type(name, loc):
    n = (name or "").lower()
    if re.search(r"school board|school district|school division|conseil scolaire|csd|dsb", n):
        return "school board"
    if re.search(r"universit|college|polytechnic|cégep|cegep", n):
        return "university/college"
    if re.search(r"health|hospital|santé|shared services supply chain", n):
        return "hospital/health authority"
    if re.search(r"hydro|power|energy|utilit|saskpower|epcor|enmax|gas", n):
        return "utility"
    if re.search(r"transit|transport|metrolinx|go transit|airport|port authority|police|library|housing|lottery|liquor|insurance", n):
        return "public agency/crown corporation"
    if re.search(r"city of|town of|township|municipality|county|region|village|district of|ville de|regional", n):
        return "municipality"
    if re.search(r"government of|province|ministry|department|engineering services -|public service delivery|manitoba transportation", n):
        return "province/territory"
    if re.search(r"canada|federal|bgis|export development|business development bank|defence", n):
        return "federal/crown corporation or federal service provider"
    return "public body"


stats = collections.Counter()
by_status = collections.Counter()
buyers = collections.Counter()
countries = collections.Counter()
seen = set()
n_main = 0
samples = []

with open(out_main, "w") as fo, open(os.path.join(dl, "details.jsonl")) as f:
    for line in f:
        try:
            d = json.loads(line)
        except Exception:
            stats["bad_json"] += 1
            continue
        stats["details"] += 1
        mid = d.get("merx_id")
        if mid in seen:
            stats["dup"] += 1
            continue
        seen.add(mid)
        lst = d.get("listing", {})
        aw = (d.get("tabs") or {}).get("award", {})
        if aw.get("http_status") != 200 or not aw.get("parsed"):
            stats["no_award_tab"] += 1
            continue
        parsed = aw["parsed"]
        notice = ((d.get("tabs") or {}).get("notice") or {}).get("parsed")
        loc = lst.get("location") or ""
        if re.search(r",\s*QC\s*,|Quebec, CAN|^Quebec", loc) or re.search(r"\bQC\b", loc):
            stats["excluded_quebec_buyer_location"] += 1
            continue
        if not parsed.get("awardees"):
            stats["no_awardees"] += 1
            continue
        buyer_name = lst.get("buyer") or (notice or {}).get("fields", {}).get("Issuing Organization")
        if not buyer_name:
            stats["no_buyer"] += 1
            continue
        for i, a in enumerate(parsed["awardees"], 1):
            addr = parse_address(a.get("Address_lines"))
            country = (addr.get("country") or "").strip()
            countries[country] += 1
            unverified = country.lower() in ("", "undisclosed")
            addr_basis = None
            if unverified:
                _ca, _r, _pc, _b = terms.canadian_address(" ".join(a.get("Address_lines") or []))
                if _ca and _pc and _r:
                    unverified = False
                    addr_basis = f"MERX awardee address country line {country!r}; {_b} (region {_r}, postal {_pc})"
                    country = "Canada"
            if country.lower() not in ("canada", "ca") and not unverified:
                stats["excluded_vendor_country"] += 1
                continue
            cd = a.get("Contract Dates") or ""
            m = re.match(r"\s*(\d{4}/\d{2}/\d{2})\s*-\s*(\d{4}/\d{2}/\d{2})", cd)
            start = pdate(m.group(1)) if m else pdate(a.get("Contract Start Date"))
            end = pdate(m.group(2)) if m else None
            award_d = pdate(a.get("Award Date")) or pdate(lst.get("award_date"))
            anchor = start or award_d
            if start and start > REF:
                stats["excluded_not_started"] += 1
                continue
            if end:
                if end < REF:
                    stats["excluded_ended"] += 1
                    continue
                status = "ongoing"
                basis = (f"MERX award notice 'Contract Dates' = {cd!r}: start {start.isoformat() if start else 'n/a'} <= 2026-10-25 <= end {end.isoformat()}"
                         + (f" (award date {award_d.isoformat()})" if award_d else ""))
            else:
                if anchor and anchor > REF:
                    stats["excluded_future_award"] += 1
                    continue
                status = "end_date_unknown"
                basis = (f"MERX award notice published (Award Date {a.get('Award Date')!r}"
                         + (f", Contract Start Date {a.get('Contract Start Date')!r}" if a.get("Contract Start Date") else "")
                         + "); no contract end date published.")
            val = money(a.get("Awarded Value"))
            rec_url = "https://www.merx.com" + lst["href"] if lst.get("href", "").startswith("/") else lst.get("href")
            ident = {"merx_id": mid, "merx_reference_number": parsed.get("fields", {}).get("Reference Number"),
                     "contract_number": a.get("Contract Number"), "awardee_index": i}
            if notice:
                nf = notice.get("fields", {})
                for k in ("Solicitation Number", "Project Number", "Source ID"):
                    if nf.get(k):
                        ident[k.lower().replace(" ", "_")] = nf[k]
            rec = {
                "record_id": f"ca_merx:{mid}:{i}",
                "source": {
                    "key": "ca_merx",
                    "name": "MERX public Awarded Solicitations (award notices)",
                    "publisher": f"{buyer_name} via MERX (mdf commerce)",
                    "dataset_url": "https://www.merx.com/public/solicitations/awarded",
                    "record_url": rec_url,
                    "retrieved_at": d.get("retrieved_at"),
                },
                "status": status,
                "status_basis": basis,
                "contract": {
                    "identifiers": ident,
                    "title": parsed.get("fields", {}).get("Solicitation Title") or lst.get("title"),
                    "description": a.get("Description") or ((notice or {}).get("description")),
                    "instrument_type": "contract",
                    "procurement_method": ((notice or {}).get("fields", {}).get("Solicitation Type") or (notice or {}).get("fields", {}).get("Project Type")),
                    "solicitation_procedure": None,
                    "commodity": {"merx_categories": (notice or {}).get("categories")},
                    "value": val,
                    "currency": "CAD" if val is not None else None,
                    "value_detail": {"awarded_value_as_published": a.get("Awarded Value"), "awarded_items": a.get("Awarded Items"), "line_item_bids": a.get("Line Item Bids")},
                    "dates": {
                        "published": (pdate(lst.get("publication_date")).isoformat() if pdate(lst.get("publication_date")) else None),
                        "award_published": (pdate(parsed.get("fields", {}).get("Publication Date")).isoformat() if pdate(parsed.get("fields", {}).get("Publication Date")) else None),
                        "signed": None,
                        "awarded": award_d.isoformat() if award_d else None,
                        "closing": (pdate(parsed.get("fields", {}).get("Solicitation Closing Date")).isoformat() if pdate(parsed.get("fields", {}).get("Solicitation Closing Date")) else None),
                        "start": start.isoformat() if start else None,
                        "end": end.isoformat() if end else None,
                        "amended_last": None,
                    },
                    "related": {"award_tab_url": aw.get("url"), "notice_tab_url": ((d.get("tabs") or {}).get("notice") or {}).get("url"),
                                "agreement_types": (notice or {}).get("fields", {}).get("Agreement Types") or (notice or {}).get("fields", {}).get("Agreement Type"),
                                "purchase_type": (notice or {}).get("fields", {}).get("Purchase Type")},
                },
                "buyer": {
                    "name": buyer_name,
                    "country": "CA",
                    "type": buyer_type(buyer_name, loc),
                    "identifiers": {},
                    "address": {"location_as_published": loc},
                    "contact": {},
                },
                "vendor": {
                    "name": (a.get("Supplier Awarded") or "").strip() or None,
                    "country": "CA",
                    "country_basis": addr_basis or f"MERX award notice 'Address' block, last line = {country!r} (with city/province/postal code lines as published)",
                    "identifiers": {},
                    "address": addr,
                    "contact": {},
                },
                "raw": {"listing_row": lst, "award_tab": parsed, "awardee_row": a, "notice_tab": notice},
            }
            if unverified:
                rec["vendor"]["country"] = None
                rec["vendor"]["country_basis"] = "not published (MERX awardee address country = %r)" % country
                fu.write(json.dumps(rec, ensure_ascii=False) + "\n")
                by_status_unv[status] += 1
                continue
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n_main += 1
            by_status[status] += 1
            buyers[buyer_name] += 1
            if len(samples) < 5 and status == "ongoing":
                samples.append({"record_id": rec["record_id"], "vendor": rec["vendor"]["name"], "city": addr.get("city"),
                                "buyer": buyer_name, "title": rec["contract"]["title"], "value": val,
                                "start": rec["contract"]["dates"]["start"], "end": rec["contract"]["dates"]["end"], "url": rec_url})

stats["records"] = n_main
fu.close()
res = {"stats": dict(stats), "by_status": dict(by_status), "by_status_unverified": dict(by_status_unv), "n_buyers": len(buyers), "buyers": buyers.most_common(),
       "vendor_countries": countries.most_common(), "samples": samples}
json.dump(res, open(os.path.join(dl, "normalize_stats.json"), "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in res.items() if k != "buyers"}, indent=1, ensure_ascii=False))
