#!/usr/bin/env python3
"""Normalize bids&tenders awarded-bid detail pages into SCHEMA.md records.

Input : <downloads>/details.jsonl (from crawl_details.py), <downloads>/listing.jsonl
Output: normalized/ca_bidsandtenders.jsonl  (vendor Country == Canada)
        normalized/ca_bidsandtenders_unverified_country.jsonl (no country published)
        <downloads>/normalize_stats.json
One record per awarded vendor row (a bid can award several vendors, e.g. rosters).
Usage: python3 -I normalize.py <downloads_dir> <normalized_dir>
"""
import sys, os, re, json, datetime, collections
sys.path.insert(0, "scripts/_muni")
import terms
from datetime import date

REF = date(2026, 10, 25)
dl, outdir = sys.argv[1], sys.argv[2]
details_path = os.path.join(dl, "details.jsonl")
out_main = os.path.join(outdir, "ca_bidsandtenders.jsonl")
out_unv = os.path.join(outdir, "ca_bidsandtenders_unverified_country.jsonl")

MONTHS = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
DATE_RE = re.compile(r"(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+([A-Z][a-z]{2})\s+(\d{1,2}),\s+(\d{4})")


def parse_bt_date(s):
    """'Fri Oct 23, 2026 (MDT)' / 'Thu Oct 22, 2026 2:00:01 PM (MDT)' -> date"""
    if not s:
        return None
    m = DATE_RE.search(s)
    if not m:
        return None
    try:
        return date(int(m.group(3)), MONTHS[m.group(1)], int(m.group(2)))
    except Exception:
        return None


def add_months(d, n):
    y = d.year + (d.month - 1 + n) // 12
    mo = (d.month - 1 + n) % 12 + 1
    import calendar
    day = min(d.day, calendar.monthrange(y, mo)[1])
    return date(y, mo, day)


def parse_money(s):
    if not s:
        return None
    s2 = re.sub(r"<[^>]+>", " ", s)
    nums = re.findall(r"\$?\s*([\d,]+(?:\.\d+)?)", s2)
    vals = []
    for n in nums:
        try:
            v = float(n.replace(",", ""))
            if v > 0:
                vals.append(v)
        except Exception:
            pass
    return vals


PROV = {
    "ontario": "ON", "quebec": "QC", "québec": "QC", "british columbia": "BC", "alberta": "AB", "manitoba": "MB",
    "saskatchewan": "SK", "nova scotia": "NS", "new brunswick": "NB", "newfoundland and labrador": "NL",
    "newfoundland": "NL", "prince edward island": "PE", "yukon": "YT", "northwest territories": "NT", "nunavut": "NU",
}
US_HOST_RE = re.compile(r"\.(net|edu|com|org|us|gov)$")


def buyer_type(name):
    n = (name or "").lower()
    if re.search(r"school board|school district|school division|conseil scolaire|education|district school|k12", n):
        return "school board"
    if re.search(r"universit|college|polytechnic", n):
        return "university/college"
    if re.search(r"health|hospital|santé", n):
        return "hospital/health authority"
    if re.search(r"hydro|power|energy|utilit|water services|water board|epcor|entegrus|sjenergy|ntpower", n):
        return "utility"
    if re.search(r"police|transit|library|zoo|conservation|housing|port authority|public health|services board|airport", n):
        return "municipal agency/board"
    if re.search(r"city of|town of|township|municipality|county|region|village|district of|regional|united counties|municipal district|^the corporation", n):
        return "municipality"
    if re.search(r"government of|province|territor", n):
        return "province/territory"
    if re.search(r"first nation|métis|metis", n):
        return "indigenous government"
    if re.search(r"engineering|architect|consult|ltd|inc\.|corp|associates|construction|fitness", n):
        return "company (consultant/owner's agent portal)"
    return "public body"


stats = collections.Counter()
by_status = collections.Counter()
seen_ids = set()
orgs = collections.Counter()
n_main = n_unv = 0
samples = []

with open(out_main, "w") as fo, open(out_unv, "w") as fu, open(details_path) as f:
    for line in f:
        try:
            d = json.loads(line)
        except Exception:
            stats["bad_json"] += 1
            continue
        stats["details"] += 1
        if d.get("http_status") != 200:
            stats["http_not_200"] += 1
            continue
        tid = d.get("tender_id")
        if tid in seen_ids:
            stats["dup_tender"] += 1
            continue
        seen_ids.add(tid)
        lst = d.get("listing", {})
        bd = d.get("bid_details", {})
        stores = d.get("stores", {})
        awarded = stores.get("Awarded")
        if not isinstance(awarded, list) or not awarded:
            stats["no_awarded_vendors"] += 1
            continue
        award_date = parse_bt_date(bd.get("Bid Awarded Date"))
        closing = parse_bt_date(bd.get("Bid Closing Date"))
        published = parse_bt_date(bd.get("Published Date"))
        dur = bd.get("Duration in months")
        try:
            dur_n = int(re.sub(r"[^\d]", "", dur)) if dur and re.sub(r"[^\d]", "", dur) else None
        except Exception:
            dur_n = None
        anchor = award_date or closing
        if anchor and anchor > REF:
            stats["excluded_future_award"] += 1
            continue
        # status
        if dur_n and anchor:
            end_inf = add_months(anchor, dur_n)
            if end_inf < REF:
                status = None
                stats["excluded_ended_by_duration"] += 1
            else:
                status = "ongoing_inferred"
                basis = (f"No explicit contract dates published; portal field 'Duration in months' = {dur_n} and "
                         f"'Bid Awarded Date' = {bd.get('Bid Awarded Date')!r} (award {anchor.isoformat()}); "
                         f"inferred end = {anchor.isoformat()} + {dur_n} months = {end_inf.isoformat()} >= 2026-10-25.")
        else:
            end_inf = None
            status = "end_date_unknown"
            basis = (f"Award published ('Bid Status' = Awarded, 'Bid Awarded Date' = {bd.get('Bid Awarded Date')!r}); "
                     f"no contract start/end date and no usable 'Duration in months' value ({dur!r}) on the public page.")
        if status is None:
            continue
        portal_host = lst.get("portal_host") or (lst.get("portal", "") + ".bidsandtenders.ca")
        host_tld_us = bool(US_HOST_RE.search(portal_host or ""))
        buyer_name = lst.get("organization") or d.get("portal_org_meta") or (d.get("page_title") or "").replace("Bids and Tenders - ", "")
        orgs[buyer_name] += 1
        buyer_country = "US" if host_tld_us else "CA"
        values = parse_money(awarded[0].get("Value")) if awarded else None
        for i, a in enumerate(awarded, 1):
            country = (a.get("Country") or "").strip()
            if country.lower() in ("not available", "n/a", "na", "undisclosed", "unknown", "-"):
                country = ""  # treated as not published -> unverified file (original kept in raw)
            addr_basis = None
            if not country:
                _ca, _r, _pc, _b = terms.canadian_address(" ".join(str(a.get(k) or "") for k in ("Address1", "City", "ProvinceState", "PostalCode")))
                if _ca and _pc and _r:
                    country = "Canada"
                    addr_basis = f"Country field blank/placeholder; {_b} ({a.get('ProvinceState')!r}, {a.get('PostalCode')!r})"
            vals = parse_money(a.get("Value"))
            prov = (a.get("ProvinceState") or "").strip()
            region = PROV.get(prov.lower(), prov or None)
            rec = {
                "record_id": f"ca_bidsandtenders:{tid}:{i}",
                "source": {
                    "key": "ca_bidsandtenders",
                    "name": "bids&tenders (eSolutions) public procurement portals - awarded bids",
                    "publisher": f"{buyer_name} via bids&tenders portal {portal_host}",
                    "dataset_url": "https://opportunities.bidsandtenders.com/bid-opportunities/Embed?status=Awarded",
                    "record_url": lst.get("detail_url") or d.get("detail_url"),
                    "retrieved_at": d.get("retrieved_at"),
                },
                "status": status,
                "status_basis": basis,
                "contract": {
                    "identifiers": {
                        "bid_number": bd.get("Bid Number"),
                        "bidsandtenders_tender_id": tid,
                        "portal": portal_host,
                        "submission_name": a.get("SubmissionName"),
                    },
                    "title": bd.get("Bid Name") or lst.get("bid_name"),
                    "description": bd.get("Description"),
                    "instrument_type": ("prequalification / roster / supply arrangement" if re.search(r"prequalif|pre-qualif|supplier qualif|roster|standing offer|vendor of record", (bd.get("Bid Type") or "") + " " + (bd.get("Bid Name") or ""), re.I) else "contract"),
                    "procurement_method": bd.get("Bid Classification"),
                    "solicitation_procedure": bd.get("Bid Type"),
                    "commodity": {"bidsandtenders_categories": bd.get("Categories")},
                    "value": (vals[0] if vals else None),
                    "currency": ("CAD" if not host_tld_us else None),
                    "value_detail": {"awarded_values_published": vals, "value_as_published": a.get("Value")},
                    "dates": {
                        "published": published.isoformat() if published else None,
                        "signed": None,
                        "awarded": award_date.isoformat() if award_date else None,
                        "closing": closing.isoformat() if closing else None,
                        "start": None,
                        "end": None,
                        "end_inferred": end_inf.isoformat() if end_inf else None,
                        "amended_last": None,
                    },
                    "related": {
                        "duration_in_months": dur_n,
                        "trade_agreements": bd.get("Trade Agreements"),
                        "unofficial_bid_results_count": len(stores.get("Submitted") or []) if isinstance(stores.get("Submitted"), list) else None,
                        "plan_takers_count": len(stores.get("PlanTakers") or []) if isinstance(stores.get("PlanTakers"), list) else None,
                    },
                },
                "buyer": {
                    "name": buyer_name,
                    "country": buyer_country,
                    "type": buyer_type(buyer_name),
                    "identifiers": {"bidsandtenders_portal": portal_host},
                    "address": {},
                    "contact": {"purchasing_representatives": stores.get("PurchasingReps")} if isinstance(stores.get("PurchasingReps"), list) else {},
                },
                "vendor": {
                    "name": (a.get("CompanyName") or "").strip() or None,
                    "country": "CA" if country.lower() == "canada" else (None if not country else country),
                    "country_basis": addr_basis or ("bids&tenders 'Awarded' vendor table field 'Country' = 'Canada' (with ProvinceState/City/PostalCode as published)" if country.lower() == "canada" else ("not published" if not country else f"field 'Country' = {country!r}")),
                    "identifiers": {},
                    "address": {
                        "line1": a.get("Address1"),
                        "city": a.get("City"),
                        "region": region,
                        "region_as_published": prov or None,
                        "postal_code": a.get("PostalCode"),
                        "country": country or None,
                    },
                    "contact": {"primary_contact": a.get("PrimaryContact"), "email": a.get("Email")},
                },
                "raw": {
                    "listing_row": lst,
                    "bid_details": bd,
                    "awarded_row": a,
                    "stores": stores,
                    "page_title": d.get("page_title"),
                    "portal_org_meta": d.get("portal_org_meta"),
                    "restricted_sections_count": d.get("restricted_sections"),
                },
            }
            if country.lower() == "canada":
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n_main += 1
                by_status[status] += 1
                if len(samples) < 5 and vals:
                    samples.append(rec)
            elif not country:
                fu.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n_unv += 1
                stats["unverified_country_rows"] += 1
            else:
                stats["excluded_non_canada_vendor"] += 1
                stats["vendor_country:" + country] += 1

stats["records_main"] = n_main
stats["records_unverified"] = n_unv
res = {"stats": dict(stats), "by_status": dict(by_status), "n_orgs": len(orgs), "orgs": orgs.most_common(),
       "samples": [{"record_id": s["record_id"], "vendor": s["vendor"]["name"], "city": s["vendor"]["address"]["city"],
                    "buyer": s["buyer"]["name"], "title": s["contract"]["title"], "value": s["contract"]["value"],
                    "status": s["status"], "url": s["source"]["record_url"]} for s in samples]}
with open(os.path.join(dl, "normalize_stats.json"), "w") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in res.items() if k != "orgs"}, indent=1, ensure_ascii=False))
