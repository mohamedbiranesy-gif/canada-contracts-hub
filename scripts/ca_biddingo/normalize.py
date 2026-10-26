#!/usr/bin/env python3
"""Normalize Biddingo awarded bids (details.jsonl from crawl.py) into SCHEMA.md records.
One record per successful bidder (bidInfo.bidAwardInfoList[].successfulBidderInfoList[]).
Vendor country: successfulBidder.country ('Canada' -> main file; blank -> unverified file; other -> excluded).
Status: Biddingo publishes no contract dates; a term stated in the bid description (detailPreview/tenderName)
is used for ongoing_inferred (anchor = award posted date of the successful bidder, else closing date); else end_date_unknown.
Usage: python3 -I normalize.py <downloads_dir> <normalized_dir>
"""
import sys, os, re, json, html, collections
from datetime import date
sys.path.insert(0, "scripts/_muni")
import terms

dl, outdir = sys.argv[1], sys.argv[2]
fo = open(os.path.join(outdir, "ca_biddingo.jsonl"), "w")
fu = open(os.path.join(outdir, "ca_biddingo_unverified_country.jsonl"), "w")
stats = collections.Counter()
by = collections.Counter()
seen = set()


def mdy(s):
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})", s or "")
    if m:
        try:
            return date(int(m.group(3)), int(m.group(1)), int(m.group(2)))
        except Exception:
            return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s or "")
    if m:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None


def text_of(h):
    if not h:
        return ""
    h = re.sub(r"(?is)<(script|style|title)[^>]*>.*?</\1>", " ", h)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()


PROV = terms.PROV_NAMES

for line in open(os.path.join(dl, "details.jsonl"), encoding="utf-8"):
    try:
        r = json.loads(line)
    except Exception:
        stats["bad_json"] += 1
        continue
    tid = r.get("biddingoTenderId")
    if tid in seen:
        stats["dup"] += 1
        continue
    seen.add(tid)
    stats["details"] += 1
    det = r.get("detail") or {}
    bi = det.get("bidInfo") or {}
    if not bi:
        stats["no_detail"] += 1
        continue
    lst = r.get("list_row") or {}
    buyer = bi.get("buyerName") or lst.get("buyerName") or bi.get("publishedBy")
    if not buyer:
        stats["no_buyer"] += 1
        continue
    awards = bi.get("bidAwardInfoList") or []
    winners = [(ai, w) for ai, a in enumerate(awards) for w in (a.get("successfulBidderInfoList") or [])]
    if not winners:
        stats["no_successful_bidder_published"] += 1
        continue
    desc = text_of(bi.get("detailPreview") or lst.get("detailPreview"))
    closing = mdy(bi.get("tenderClosingDate") or lst.get("tenderClosingEst"))
    for k, (ai, w) in enumerate(winners, 1):
        stats["winner_rows"] += 1
        name = (w.get("bidderName") or "").strip()
        if not name:
            stats["no_bidder_name"] += 1
            continue
        country = (w.get("country") or "").strip()
        unverified = country == ""
        if country.lower() not in ("canada", "ca") and not unverified:
            stats["excluded_country_" + country] += 1
            continue
        anchor = mdy(w.get("postedDate")) or closing
        status, basis, st, en, kind = terms.decide(anchor, (bi.get("tenderName") or "") + ". " + desc, "award/result posted date")
        if status is None:
            stats["excluded_" + basis] += 1
            continue
        prov = (w.get("province") or "").strip()
        region = PROV.get(prov.lower(), prov or None)
        val = w.get("totalPrice")
        val = float(val) if isinstance(val, (int, float)) and val > 0 else None
        url = r.get("detail_url")
        rec = {
            "record_id": f"ca_biddingo:{tid}:{w.get('suplId') or k}",
            "source": {"key": "ca_biddingo", "name": "Biddingo - awarded bids (public no-authorize API)", "publisher": f"{buyer} via Biddingo (Biddingo Inc.)",
                       "dataset_url": "https://www.biddingo.com/search", "record_url": url, "retrieved_at": r.get("retrieved_at")},
            "status": status, "status_basis": basis,
            "contract": {
                "identifiers": {"biddingo_tender_id": tid, "tender_number": bi.get("tenderNumber"), "procurement_id": bi.get("procurementId"),
                                "buyer_sys_id": bi.get("buyerSysId"), "buyer_org_id": bi.get("buyerOrgId"), "award_index": ai, "supplier_id": w.get("suplId")},
                "title": bi.get("tenderName"), "description": desc or None, "instrument_type": "contract",
                "procurement_method": bi.get("contractType"), "solicitation_procedure": bi.get("bidType"),
                "commodity": {"biddingo_categories": [c.get("categoryName") or c for c in (bi.get("categoryList") or [])]},
                "value": val, "currency": "CAD" if val is not None else None,
                "value_detail": {"successful_bidder_total_price": w.get("totalPrice"), "value_range": bi.get("valueRange")},
                "dates": {"published": mdy(bi.get("publishedDate")).isoformat() if mdy(bi.get("publishedDate")) else None, "signed": None,
                          "awarded": anchor.isoformat() if anchor else None, "closing": closing.isoformat() if closing else None,
                          "start": st.isoformat() if st and kind else None, "end": en.isoformat() if en else None, "amended_last": None},
                "related": {"landing_page": ("https://www.biddingo.com/" + bi["landingpageUrl"]) if bi.get("landingpageUrl") else None,
                            "awardee_display_type": (awards[ai] or {}).get("awardeeDisplayType")},
            },
            "buyer": {"name": buyer, "country": "US" if bi.get("regionId") == 5 else "CA", "type": "public body (municipality / school board / agency as named)",
                      "identifiers": {"buyer_sys_id": bi.get("buyerSysId"), "buyer_org_id": bi.get("buyerOrgId")}, "address": {}, "contact": {}},
            "vendor": {"name": name, "country": None if unverified else "CA",
                       "country_basis": "not published (successfulBidderInfoList.country blank)" if unverified else f"successfulBidderInfoList.country = {country!r} (province {prov!r}, city {w.get('city')!r})",
                       "identifiers": {"biddingo_supplier_id": w.get("suplId")},
                       "address": {"line1": w.get("address"), "city": w.get("city"), "region": region, "postal_code": None, "country": country or None},
                       "contact": {"first_name": w.get("firstName"), "last_name": w.get("lastName"), "email": w.get("email"), "phone": w.get("phoneNumber")}},
            "raw": {"list_row": lst, "bidInfo": bi, "successful_bidder": w},
        }
        (fu if unverified else fo).write(json.dumps(rec, ensure_ascii=False) + "\n")
        by[("unverified:" if unverified else "") + status] += 1

fo.close(); fu.close()
res = {"stats": dict(stats), "by_status": dict(by)}
json.dump(res, open(os.path.join(dl, "normalize_stats.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
