#!/usr/bin/env python3
"""Normalize Alberta Purchasing Connection (APC) awarded opportunities -> schema records.
One record per award row (an opportunity can have several awards / suppliers).
Vendor country: awards[].address.country (ISO2 'CA' or 'Canada'); province from address.stateProvince ('CA-AB').
Ongoing: opportunity.deliveryStartDate <= REF <= opportunity.deliveryEndDate (contract/delivery period published
with the opportunity), else end_date_unknown when no delivery dates.
Usage: python3 -I normalize_apc.py <download_dir> <out_jsonl> <stats_json>
"""
import glob, json, os, re, sys, datetime as dt, collections

DL, OUT, STATS = sys.argv[1:4]
REF = dt.date(2026, 10, 25)
RETRIEVED = open(os.path.join(DL, "started_at.txt")).read().split()[0]
CA = {"ca", "canada", "can"}


def d10(s):
    if not s:
        return None
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", str(s))
    return m.group(1) if m else None


def main():
    stats = collections.Counter()
    hits = {}
    for line in open(os.path.join(DL, "search_hits.jsonl")):
        try:
            h = json.loads(line); hits[h["referenceNumber"]] = h
        except Exception:
            pass
    out = open(OUT, "w")
    import gzip
    for path in sorted(glob.glob(os.path.join(DL, "details", "*.json")) + glob.glob(os.path.join(DL, "details", "*.json.gz"))):
        try:
            d = json.load(gzip.open(path, "rt") if path.endswith(".gz") else open(path))
        except Exception:
            stats["bad_json"] += 1; continue
        o = d.get("opportunity") or {}
        ref = o.get("referenceNumber") or os.path.basename(path).split(".json")[0]
        stats["opportunities"] += 1
        if o.get("statusCode") != "AWARD":
            stats["skip_status_" + str(o.get("statusCode"))] += 1
            continue
        awards = d.get("awards") or o.get("awards") or []
        if not awards:
            stats["skip_no_award_rows"] += 1
            continue
        hit = hits.get(ref, {})
        buyer = hit.get("contractingOrganization") or (d.get("contractingEntityContactInformation") or {}).get("name")
        if not buyer:
            # fall back: title prefix "Org - ..." is not reliable; use contact address line1 if it is an org name
            ci = o.get("contactInformation") or {}
            buyer = ci.get("addressLine1") if ci.get("addressLine1") and not re.match(r"^\d", ci.get("addressLine1")) else None
        if not buyer:
            stats["skip_no_buyer_name"] += 1
            continue
        start = d10(o.get("deliveryStartDate")); end = d10(o.get("deliveryEndDate"))
        awarded_on = d10(o.get("awardedOnUtc"))
        if o.get("cancelledOnUtc"):
            stats["skip_cancelled"] += 1
            continue
        for a in awards:
            stats["award_rows"] += 1
            addr = a.get("address") or {}
            country = (addr.get("country") or "").strip()
            if country.lower() not in CA:
                stats["skip_vendor_country_" + (country or "blank")] += 1
                continue
            sp = (addr.get("stateProvince") or "").strip()
            region = sp.split("-")[-1] if sp else None
            name = (a.get("alternativeSupplierDisplayName") or a.get("operatingOrTradeName") or "").strip()
            if not name:
                stats["skip_no_supplier_name"] += 1
                continue
            award_date = d10(a.get("awardDate"))
            anchor = start or award_date or awarded_on
            if start and end:
                if start > REF.isoformat():
                    stats["skip_not_started"] += 1; continue
                if end < REF.isoformat():
                    stats["skip_ended"] += 1; continue
                status = "ongoing"
                basis = "opportunity.deliveryStartDate %s <= 2026-10-25 <= opportunity.deliveryEndDate %s (delivery/contract period published on the APC posting); award date %s" % (start, end, award_date)
            elif end and not start:
                if end < REF.isoformat():
                    stats["skip_ended"] += 1; continue
                if anchor and anchor > REF.isoformat():
                    stats["skip_not_started"] += 1; continue
                status = "ongoing"
                basis = "deliveryEndDate %s >= 2026-10-25, award date %s <= 2026-10-25; no deliveryStartDate" % (end, award_date)
            else:
                if award_date and award_date > REF.isoformat():
                    stats["skip_future_award_date"] += 1; continue
                status = "end_date_unknown"
                basis = "No deliveryStartDate/deliveryEndDate on the APC posting; award date %s, awardedOnUtc %s" % (award_date, awarded_on)
            rid = "ca_alberta_apc:%s:%s" % (ref, a.get("id"))
            codes = d.get("commodityCodes") or []
            commodity = {}
            if codes:
                commodity["unspsc"] = ", ".join(str(c.get("segment") or c.get("family") or c.get("class") or c.get("commodity") or c.get("id")) for c in codes)
                commodity["unspsc_description"] = "; ".join(" > ".join(x for x in [c.get("segmentTitle"), c.get("familyTitle"), c.get("classTitle"), c.get("commodityTitle")] if x) for c in codes)
                gs = [c.get("gsinCode") for c in codes if c.get("gsinCode")]
                if gs:
                    commodity["gsin"] = ", ".join(gs)
            amount = a.get("amount")
            rec = {
                "record_id": rid,
                "source": {
                    "key": "ca_alberta_apc",
                    "name": "Alberta Purchasing Connection (APC) - awarded opportunities",
                    "publisher": "Government of Alberta (Service Alberta and Red Tape Reduction) - purchasing.alberta.ca",
                    "dataset_url": "https://purchasing.alberta.ca/search?status=awarded",
                    "record_url": "https://purchasing.alberta.ca/posting/" + ref,
                    "retrieved_at": RETRIEVED,
                },
                "status": status, "status_basis": basis,
                "contract": {
                    "identifiers": {"apc_reference_number": ref, "opportunity_id": o.get("id"), "solicitation_number": o.get("solicitationNumber"),
                                    "award_id": a.get("id"), "supplier_id": a.get("supplierId"), "parent_id": o.get("parentId")},
                    "title": o.get("title"), "description": o.get("projectDescription"),
                    "instrument_type": "contract award (%s)" % (o.get("postingTypeCode") or ""),
                    "procurement_method": o.get("postingTypeCode"), "solicitation_procedure": o.get("solicitationTypeCode"),
                    "commodity": commodity,
                    "value": float(amount) if isinstance(amount, (int, float)) else None, "currency": "CAD" if isinstance(amount, (int, float)) else None,
                    "value_detail": {"award_amount": amount, "opportunity_actual_value": o.get("actualValue"), "opportunity_estimated_value": o.get("estimatedValue"),
                                     "notice_of_award_total_value": o.get("noticeOfAwardTotalValue")},
                    "dates": {"published": d10(o.get("postDateTime")), "signed": None, "start": start, "end": end, "amended_last": d10(o.get("latestAmendedDate") or o.get("amendedOnUtc")),
                              "awarded": award_date, "awarded_on_utc": awarded_on, "tender_closing": d10(o.get("closeDateTime"))},
                    "related": {"region_of_delivery": o.get("regionOfDelivery"), "trade_agreement": o.get("actualTradeAgreement") or o.get("estimatedTradeAgreement"),
                                "trade_agreement_type_code": o.get("estimatedTradeAgreementTypeCode"), "is_direct_award": o.get("isDirectAward"),
                                "external_origin_link": o.get("externalOriginLink"), "award_description": a.get("description"), "award_comments": a.get("comments"),
                                "awards_on_opportunity": len(awards)},
                },
                "buyer": {
                    "name": buyer, "country": "CA", "type": "Alberta public body (GoA ministry, agency, municipality, school board, health or post-secondary) as named",
                    "identifiers": {"contracting_org_id": o.get("contractingOrgId")},
                    "address": ((d.get("contractingEntityContactInformation") or {}).get("addresses") or [{}])[0],
                    "contact": {k: (o.get("contactInformation") or {}).get(k) for k in ("firstName", "lastName", "title", "emailAddress", "phoneNumber")},
                },
                "vendor": {
                    "name": name, "country": "CA", "country_basis": "awards[].address.country == %r (stateProvince %r)" % (country, sp),
                    "identifiers": {"apc_supplier_id": a.get("supplierId")},
                    "address": {"line1": addr.get("streetAddress"), "line2": addr.get("streetAddress2"), "city": addr.get("city"), "region": region,
                                "postal_code": addr.get("postalCode"), "country": country},
                    "contact": {"email": a.get("emailAddress") or None, "phone": a.get("phoneNumber") or None,
                                "operating_or_trade_name": a.get("operatingOrTradeName"), "branch": a.get("branchOrRegionalOfficeName")},
                },
                "raw": {"search_hit": hit, "detail": d, "award": a},
            }
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            stats["emitted_" + status] += 1
    out.close()
    json.dump(dict(stats), open(STATS, "w"), indent=1)
    print(json.dumps(dict(stats), indent=1))


if __name__ == "__main__":
    main()
