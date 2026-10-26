#!/usr/bin/env python3
"""Normalize NYC 'Recent Contract Awards' (data.cityofnewyork.us qyyg-4tf5, City Record award notices) -> awards to
vendors with a Canadian address. The notice carries the award/publication date only; a contract term is sometimes stated
in the free-text description -> ongoing_inferred when it is, else end_date_unknown (kept only if published within the
last 3 years, since awards are typically multi-year contracts).
usage: python3 -I normalize.py <jsonl> <out.jsonl>
"""
import sys, json, re, html, collections
sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_city_nyc"
DSID = "qyyg-4tf5"
RECENT_CUTOFF = "2023-10-25"
PROVNAMES = r"(ONTARIO|QUEBEC|QU[ÉE]BEC|BRITISH COLUMBIA|ALBERTA|MANITOBA|SASKATCHEWAN|NOVA SCOTIA|NEW BRUNSWICK|NEWFOUNDLAND|PRINCE EDWARD ISLAND)"


def canadian(r):
    va = (r.get("vendor_address") or "")
    u = va.upper()
    if re.search(r"\bCANADA\b", u):
        return True, f"vendor_address contains 'Canada': '{va}'"
    if re.search(r"\b" + PROVNAMES + r"\b", u) and not re.search(r"\bNEW BRUNSWICK (ROAD|RD|AVE|AVENUE|ST|STREET)\b", u):
        return True, f"vendor_address contains a Canadian province name: '{va}'"
    if is_ca_postal(va) and re.search(r"\b(ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|PQ)\b", u):
        return True, f"vendor_address has Canadian province code + Canadian-format postal code: '{va}'"
    return False, None


def strip_html(s):
    if not s:
        return None
    t = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(re.sub(r"\s+", " ", t)).strip()


def infer_term(text, award):
    """Look for an explicit term in the description: 'N-year', 'through <date>', 'from <date> to <date>'."""
    if not text:
        return None, None
    t = text
    m = re.search(r"(?i)from\s+([A-Z][a-z]+ \d{1,2}(?:st|nd|rd|th)?,? \d{4})\s*(?:,|to|through|-|until)\s*([A-Z][a-z]+ \d{1,2}(?:st|nd|rd|th)?,? \d{4})", t)
    if m:
        def pd(s):
            s = re.sub(r"(\d)(st|nd|rd|th)", r"\1", s).replace(",", "")
            import datetime
            for fmt in ("%B %d %Y", "%b %d %Y"):
                try:
                    return datetime.datetime.strptime(s, fmt).date().isoformat()
                except ValueError:
                    pass
            return None
        a, b = pd(m.group(1)), pd(m.group(2))
        if a and b:
            return b, f"description states term from {a} to {b}"
    m = re.search(r"(?i)(\d+)\s*-?\s*year\b", t)
    if m and award:
        n = int(m.group(1))
        if 0 < n <= 10:
            y, mo, d = award.split("-")
            end = f"{int(y)+n}-{mo}-{d}"
            return end, f"description states a {n}-year contract; award/notice date {award} + {n} years = {end}"
    return None, None


def main():
    path, out = sys.argv[1], sys.argv[2]
    retrieved = file_mtime_iso(path)
    w = Writer(out)
    stats = collections.Counter()
    with open(path, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            stats["rows"] += 1
            ok, basis = canadian(r)
            if not ok:
                continue
            stats["canadian_rows"] += 1
            award = parse_date(r.get("start_date"))
            text = " ".join(strip_html(r.get(k)) or "" for k in ("additional_description_1", "additional_description_2", "additional_description_3", "other_info_1", "other_info_2", "other_info_3", "printout_1", "printout_2", "printout_3"))
            end, how = infer_term(text, award)
            if end:
                if end < REF_S:
                    stats["excluded_inferred_ended"] += 1
                    continue
                status = "ongoing_inferred"
                sb = f"{how}; {award} <= {REF_S} <= {end}"
            else:
                if not award or award < RECENT_CUTOFF:
                    stats["excluded_older_than_3y"] += 1
                    continue
                status = "end_date_unknown"
                sb = f"City Record award notice published {award} (within 3 years before {REF_S}); no contract term stated"
            amt = parse_amount(r.get("contract_amount"))
            dl = r.get("document_links")
            dl = dl.get("url") if isinstance(dl, dict) else dl
            contract = contract_block(
                identifiers={"request_id": r.get("request_id"), "pin": r.get("pin")},
                title=r.get("short_title"), description=strip_html(r.get("additional_description_1")) or r.get("short_title"),
                instrument_type="contract award notice (City Record)", procurement_method=r.get("selection_method_description"),
                commodity={"nyc_category": r.get("category_description")},
                value=amt, currency="USD", value_detail={"contract_amount": amt},
                dates={"published": award, "signed": award, "start": award, "end": end if status == "ongoing_inferred" else None},
                related={"special_case_reason": r.get("special_case_reason_description"), "document_links": dl, "type_of_notice": r.get("type_of_notice_description"),
                         "event_date": parse_date(r.get("event_date")), "due_date": parse_date(r.get("due_date"))},
            )
            buyer = buyer_block(f"City of New York - {r.get('agency_name')}", "city agency", "US", identifiers={"agency_name": r.get("agency_name")},
                                address={"building_name": r.get("building_name"), "line1": r.get("street_address_1"), "line2": r.get("street_address_2"), "city": r.get("city"), "region": r.get("state"), "postal_code": r.get("zip_code")},
                                contact={"name": r.get("contact_name"), "phone": r.get("contact_phone"), "email": r.get("email"), "fax": r.get("contact_fax"), "address_to_request": r.get("address_to_request")})
            vendor = vendor_block(r.get("vendor_name"), basis, address={"line1": r.get("vendor_address"), "country": "Canada (per address text)"})
            rec = record(SOURCE_KEY, "NYC Recent Contract Awards (City Record / NYC Open Data)", "NYC Department of Citywide Administrative Services (City Record) via NYC Open Data",
                         f"https://data.cityofnewyork.us/d/{DSID}", None, retrieved, r.get("request_id"), status, sb, contract, buyer, vendor, {"dataset_id": DSID, "row": r})
            w.write(rec)
            stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()
