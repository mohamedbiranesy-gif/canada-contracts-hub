#!/usr/bin/env python3
"""Normalize Texas LBB Contracts Database (contracts.lbb.texas.gov) ACTIVE contracts whose vendor address (from the CMS
public detail page) is in Canada.
usage: python3 -I normalize.py <lbb_download_contracts_active.csv> <details_canadian.jsonl> <out.jsonl>
"""
import sys, csv, json, re, collections
sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_state_texas_lbb"


def canadian_basis(v):
    st = (v.get("State") or "").strip().upper()
    if norm_prov(st):
        return f"CMS detail page vendor State = '{st}' (Canadian province code)"
    txt = " | ".join(filter(None, [v.get("Address Line 1"), v.get("Address Line 2"), v.get("Address Line 3"), v.get("Address Line 4"), v.get("City")]))
    if re.search(r"(?i)\bcanada\b", txt):
        return f"CMS detail page vendor address/city names CANADA (State field '{st}'): '{txt}'"
    return f"CMS detail page vendor address has a Canadian province + postal code (State field '{st}'): '{txt}'"


OTHER_COUNTRIES = {"FRANCE", "UNITED KINGDOM", "UK", "ENGLAND", "GERMANY", "NETHERLANDS", "SWITZERLAND", "ISRAEL", "AUSTRALIA", "JAPAN",
                   "INDIA", "MEXICO", "SPAIN", "ITALY", "SWEDEN", "NORWAY", "DENMARK", "BELGIUM", "IRELAND", "CHINA", "SINGAPORE", "USA", "UNITED STATES"}


def confirm_ca(v):
    """Second check (added on resume after a false positive '1 AVENUE DU CANADA | LES ULIS, PARIS 91940 | FRANCE'):
    no address element may be another country name, and the address must contain a line/City equal to CANADA, or a Canadian
    province (code or name) together with a Canadian postal code, or a structured province State."""
    els = [(v.get(k) or "").strip().upper() for k in ("Address Line 1", "Address Line 2", "Address Line 3", "Address Line 4", "City")]
    if any(e in OTHER_COUNTRIES for e in els if e):
        return False
    if norm_prov((v.get("State") or "").strip()):
        return True
    if any(e == "CANADA" or e.endswith(" CANADA") and not e.startswith(tuple("0123456789")) for e in els):
        return True
    txt = " ".join(els)
    return bool(re.search(r"\b(ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|ONTARIO|QUEBEC|BRITISH COLUMBIA|ALBERTA|MANITOBA|SASKATCHEWAN|NOVA SCOTIA|NEW BRUNSWICK)\b", txt)) and is_ca_postal(txt)


def main():
    csv_p, det_p, out = sys.argv[1], sys.argv[2], sys.argv[3]
    retrieved_csv = file_mtime_iso(csv_p)
    w = Writer(out)
    stats = collections.Counter()
    for line in open(det_p, encoding="utf-8"):
        d = json.loads(line)
        stats["detail_pages"] += 1
        r = d["csv_row"]
        v = d["vendor_block"]
        award = parse_date(r.get("Award Date"))
        comp = r.get("Completion Date")
        end = parse_date(comp) if comp and comp != "-" else None
        if not confirm_ca(v):
            stats["excluded_not_canadian_on_recheck"] += 1
            continue
        if (r.get("Status") or "").strip() != "Active":
            stats["excluded_not_active"] += 1
            continue
        if end:
            status, basis = status_from_dates(award, end)
            if not status:
                stats["excluded_" + ("ended" if "ended" in basis else "future")] += 1
                continue
            basis = f"LBB Status = Active; Award Date {award} <= {REF_S} <= Completion Date {end}"
        else:
            if award and award > REF_S:
                stats["excluded_future"] += 1
                continue
            status = "end_date_unknown"
            basis = f"LBB Status = Active; Award Date {award}; Completion Date not reported ('-')"
        amt = parse_amount(r.get("Current Contract Value"))
        m = re.search(r"Max Value.*?\$([\d,\.]+)", d.get("vendor_block", {}).get("_summary_line") or "")
        nigp = r.get("NGIP Codes and Categories") or ""
        contract = contract_block(
            identifiers={"lbb_contract_id": d["cid"], "agency_id": d["aid"], "vendor_id": r.get("Vendor ID", "").strip('"')},
            title=r.get("Subject"), description=r.get("Subject"), instrument_type="state contract reported to LBB (>= $50,000)",
            procurement_method=r.get("Procurement Method"), commodity={"nigp_items_with_category": nigp, "lbb_category": r.get("Category")},
            value=amt, currency="USD", value_detail={"current_contract_value": amt},
            dates={"signed": award, "start": award, "end": end},
            related={"cms_detail_url": d["url"], "cms_final_url": d.get("final_url"), "summary_line": v.get("_summary_line")},
        )
        buyer = buyer_block(r.get("Agency"), "Texas state agency / institution", "US", identifiers={"lbb_agency_id": d["aid"]})
        vendor = vendor_block(v.get("Vendor Name") or r.get("Vendor"), canadian_basis(v), identifiers={"texas_vendor_id": v.get("Vendor: \xa0Vendor ID") or r.get("Vendor ID", "").strip('"')},
                              address={"line1": v.get("Address Line 1"), "line2": v.get("Address Line 2"), "line3": v.get("Address Line 3"), "line4": v.get("Address Line 4"),
                                       "city": v.get("City"), "region": v.get("State"), "postal_code": v.get("Postal Code"), "country": None},
                              contact={"phone": v.get("Phone")})
        raw = {"lbb_download_row": r, "cms_detail": {k: val for k, val in d.items() if k != "csv_row"}}
        rec = record(SOURCE_KEY, "Texas LBB Contracts Database (contracts.lbb.texas.gov) + CMS public detail pages", "Texas Legislative Budget Board",
                     "https://contracts.lbb.texas.gov/", d["url"], d.get("fetched_at") or retrieved_csv, f"{d['aid']}-{d['cid']}", status, basis, contract, buyer, vendor, raw)
        w.write(rec)
        stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()
