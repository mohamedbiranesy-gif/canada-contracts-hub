#!/usr/bin/env python3
"""Normalize Delaware 'Awarded Vendor Contact Info' (data.delaware.gov h9bb-iyu6): vendors currently under award for a
State of Delaware central contract, with contract title, contract URL (mmp.delaware.gov) and expiration date.
usage: python3 -I normalize.py <jsonl> <out.jsonl>
"""
import sys, json, re, collections
sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_state_delaware"
DSID = "h9bb-iyu6"


def canadian(r):
    st = (r.get("state") or "").strip()
    city = r.get("city") or ""
    a = " ".join(filter(None, [r.get("address1"), r.get("address2"), city]))
    if norm_prov(st):
        return True, f"state = '{st}' (Canadian province code)"
    if re.search(r"(?i)\bcanada\b", a) and (is_ca_postal(a) or re.search(r"(?i)\b(ontario|quebec|qc|british columbia|alberta|nova scotia|manitoba|saskatchewan|new brunswick|newfoundland|prince edward island)\b", a)):
        return True, f"address/city text contains 'Canada' with a Canadian province/postal code ('{city}')"
    return False, None


def load_pages(path):
    """Optional: contract_pages.jsonl produced by fetching each mmp.delaware.gov Contracts/Details page."""
    import os
    pages = {}
    if path and os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            j = json.loads(line)
            pages[j["mmp_id"]] = j
    return pages


def main():
    path, out = sys.argv[1], sys.argv[2]
    pages = load_pages(sys.argv[3] if len(sys.argv) > 3 else None)
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
            end = parse_date(r.get("expiredate"))
            status, b2 = status_from_dates(None, end)
            if not status:
                stats["excluded_ended"] += 1
                continue
            basis = (f"dataset lists vendors currently under award; expiredate {end} >= {REF_S}" if end else "dataset lists vendors currently under award; no expiredate published")
            cu = r.get("contracturl")
            curl = cu.get("url") if isinstance(cu, dict) else cu
            m = re.search(r"/Contracts/Details/(\d+)", curl or "")
            cid = m.group(1) if m else None
            pg = pages.get(cid, {})
            start = parse_date(pg.get("effective_date"))
            if pg.get("expiration_date"):
                end_pg = parse_date(pg["expiration_date"])
                if end_pg:
                    end = end_pg
                    basis = f"contract page: Contract Effective Date {start} <= {REF_S} <= Contract Expiration Date {end}; dataset lists vendors currently under award (expiredate {parse_date(r.get('expiredate'))})"
            contract = contract_block(
                identifiers={"mmp_contract_id": cid, "contract_number": pg.get("contract_number"), "contract_title": r.get("contracttitle")},
                title=r.get("contracttitle"), instrument_type="statewide central contract award (vendor under award)",
                value=None, currency="USD", dates={"start": start, "end": end},
                related={"contract_url": curl, "awarded_vendor_flag": r.get("awarded_vendor"), "delaware_vendor": r.get("delawarevendor"),
                         "mwbe_certified": r.get("mwbecertified"), "veteran_service_disabled": r.get("vetservdisabled")},
            )
            buyer = buyer_block("State of Delaware - Government Support Services (Contracting)", "state central procurement", "US")
            vendor = vendor_block(r.get("companyname"), basis,
                                  address={"line1": r.get("address1"), "line2": r.get("address2"), "city": r.get("city"), "region": r.get("state"),
                                           "postal_code": r.get("zipcode"), "country": None},
                                  contact={"name": r.get("contact1"), "phone": r.get("phone1"), "fax": r.get("fax1"), "email": r.get("email1"), "website": r.get("website")})
            rid = f"{cid or 'na'}:{re.sub(r'[^A-Za-z0-9]+', '_', r.get('companyname') or '')}"
            rec = record(SOURCE_KEY, "Delaware Awarded Vendor Contact Info (Delaware Open Data)", "Delaware Office of Management and Budget - Government Support Services",
                         f"https://data.delaware.gov/d/{DSID}", curl, retrieved, rid, status, basis, contract, buyer, vendor, {"dataset_id": DSID, "row": r, "contract_page": pg or None})
            w.write(rec)
            stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()
