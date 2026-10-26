#!/usr/bin/env python3
"""Normalize Canada-supplier OCDS compiled releases (output of ocds_filter.py) into the
SCHEMA.md record shape. One record per (ocid, Canadian-supplier award); when the release
has no awards[].suppliers, one record per ocid. All releases seen for the ocid go to raw.rows.
usage: normalize_ocds.py --source <key> --config <config.json> --out <jsonl> <matches.jsonl ...>
"""
import sys, json, argparse, re, datetime, glob, os, unicodedata
from collections import defaultdict

REF = datetime.date(2026, 10, 25)
CANADA_TOKENS = {"canada", "canadá", "kanada", "канада", "加拿大", "カナダ", "캐나다", "ca", "can", "cdn"}

def norm(s):
    s = unicodedata.normalize("NFKD", str(s))
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9Ѐ-ӿ一-鿿぀-ヿ가-힯]+", "", s.lower())

def country_vals(addr):
    out = []
    if not isinstance(addr, dict):
        return out
    for k in ("countryName", "country", "countryCode"):
        v = addr.get(k)
        if v is None:
            continue
        if isinstance(v, dict):
            for kk in ("id", "name", "description"):
                if v.get(kk):
                    out.append((k + "." + kk, str(v[kk])))
        else:
            out.append((k, str(v)))
    return out

def canada_basis(party):
    for k, v in country_vals(party.get("address")):
        if norm(v) in CANADA_TOKENS:
            return "parties[].address.%s = %r" % (k, v), v
    sch = (party.get("identifier") or {}).get("scheme")
    if isinstance(sch, str) and sch.upper().startswith("CA-"):
        return "parties[].identifier.scheme = %r" % sch, None
    return None, None

def d8(s):
    """ISO date (YYYY-MM-DD) from an OCDS datetime string, or None."""
    if not s or not isinstance(s, str):
        return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    if not m:
        return None
    try:
        return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None

def iso(d):
    return d.isoformat() if d else None

def num(v):
    try:
        if v is None or v == "":
            return None
        return float(v)
    except Exception:
        return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--stats", required=True)
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    cfg = json.load(open(a.config, encoding="utf-8"))[a.source]
    retrieved = cfg.get("retrieved_at")

    # 1. group releases by ocid
    by_ocid = defaultdict(list)
    for f in a.files:
        for line in open(f, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            rel = d.get("release", d)
            rel["_source_file"] = os.path.basename(f)
            by_ocid[rel.get("ocid")].append(rel)

    stats = defaultdict(int)
    excluded = []
    with open(a.out, "w", encoding="utf-8") as fo:
        for ocid, rels in by_ocid.items():
            rels.sort(key=lambda r: r.get("date") or "")
            latest = rels[-1]
            stats["ocids"] += 1
            parties = {str(p.get("id")): p for p in latest.get("parties") or [] if isinstance(p, dict)}
            # Canadian supplier parties
            can_parties = {}
            for pid, p in parties.items():
                roles = [str(r).lower() for r in (p.get("roles") or [])]
                basis, val = canada_basis(p)
                if basis and ("supplier" in roles or any(
                        str(s.get("id")) == pid for aw in latest.get("awards") or [] for s in aw.get("suppliers") or [])):
                    can_parties[pid] = (p, basis, val)
            # award-level units
            awards = latest.get("awards") or []
            units = []
            for aw in awards:
                sups = aw.get("suppliers") or []
                can_sups = [s for s in sups if str(s.get("id")) in can_parties]
                # supplier inline address
                for s in sups:
                    if str(s.get("id")) not in can_parties:
                        for k, v in country_vals(s.get("address")):
                            if norm(v) in CANADA_TOKENS:
                                can_parties[str(s.get("id"))] = (s, "awards[].suppliers[].address.%s = %r" % (k, v), v)
                                can_sups.append(s)
                if can_sups:
                    units.append((aw, can_sups))
            if not units and can_parties:
                # releases where awards don't name suppliers (e.g. eForms publishers): one record per ocid
                units.append((None, [p for p, _, _ in can_parties.values()]))
            if not units:
                stats["no_canadian_supplier_in_latest_release"] += 1
                continue
            buyer = latest.get("buyer") or {}
            bparty = parties.get(str(buyer.get("id"))) or next((p for p in parties.values() if "buyer" in [str(r).lower() for r in p.get("roles") or []]), {})
            tender = latest.get("tender") or {}
            contracts = latest.get("contracts") or []
            for aw, sups in units:
                stats["units"] += 1
                sup = sups[0]
                sp, basis, val = can_parties.get(str(sup.get("id")), (sup, None, None))
                if basis is None:
                    basis, val = canada_basis(sp)
                # linked contracts
                if aw is not None:
                    cons = [c for c in contracts if str(c.get("awardID")) == str(aw.get("id"))]
                else:
                    cons = contracts
                # dates
                start = end = signed = None
                dur_days = None
                for c in cons:
                    per = c.get("period") or {}
                    start = start or d8(per.get("startDate"))
                    end = end or d8(per.get("endDate"))
                    signed = signed or d8(c.get("dateSigned"))
                    dur_days = dur_days or per.get("durationInDays")
                if aw is not None:
                    cp = aw.get("contractPeriod") or {}
                    start = start or d8(cp.get("startDate"))
                    end = end or d8(cp.get("endDate"))
                    dur_days = dur_days or cp.get("durationInDays")
                # lot-level contractPeriod (eForms publishers), matched through awards[].relatedLots
                lot_ids = set(str(x) for x in ((aw or {}).get("relatedLots") or []))
                for lot in tender.get("lots") or []:
                    if lot_ids and str(lot.get("id")) not in lot_ids:
                        continue
                    if not lot_ids and len(tender.get("lots") or []) != 1:
                        # several lots and no award->lot link: use the period only if every lot states the same one
                        periods = {json.dumps(l.get("contractPeriod") or {}, sort_keys=True) for l in tender.get("lots") or []}
                        if len(periods) != 1:
                            continue
                    lcp = lot.get("contractPeriod") or {}
                    start = start or d8(lcp.get("startDate"))
                    end = end or d8(lcp.get("endDate"))
                    dur_days = dur_days or lcp.get("durationInDays")
                tcp = tender.get("contractPeriod") or {}
                start = start or d8(tcp.get("startDate"))
                end = end or d8(tcp.get("endDate"))
                dur_days = dur_days or tcp.get("durationInDays")
                award_date = d8(aw.get("date")) if aw else None
                pub_date = d8(latest.get("date"))
                anchor = start or signed or award_date or pub_date
                anchor_name = "period.startDate" if start else ("contract.dateSigned" if signed else ("award.date" if award_date else "release.date"))
                # award / contract status
                aw_status = (aw or {}).get("status")
                con_status = [c.get("status") for c in cons]
                if aw_status in ("cancelled", "unsuccessful"):
                    stats["excluded_award_status_" + aw_status] += 1
                    excluded.append((ocid, "award status " + aw_status)); continue
                if con_status and all(s == "cancelled" for s in con_status):
                    stats["excluded_contract_cancelled"] += 1
                    excluded.append((ocid, "contract cancelled")); continue
                status = basis_txt = None
                if end:
                    if end < REF:
                        stats["excluded_ended"] += 1
                        excluded.append((ocid, "end %s < ref" % end)); continue
                    if anchor and anchor > REF:
                        stats["excluded_future_start"] += 1
                        excluded.append((ocid, "start %s > ref" % anchor)); continue
                    status = "ongoing"
                    basis_txt = "%s %s <= 2026-10-25 <= period.endDate %s" % (anchor_name, iso(anchor), iso(end))
                    if any(s == "terminated" for s in con_status):
                        basis_txt += " (publisher marks contract status 'terminated' although end date is in the future; kept)"
                elif dur_days and anchor:
                    try:
                        inferred = anchor + datetime.timedelta(days=int(float(dur_days)))
                    except Exception:
                        inferred = None
                    if inferred:
                        if inferred < REF:
                            stats["excluded_inferred_ended"] += 1
                            excluded.append((ocid, "inferred end %s < ref" % inferred)); continue
                        if anchor > REF:
                            stats["excluded_future_start"] += 1
                            excluded.append((ocid, "start %s > ref" % anchor)); continue
                        status = "ongoing_inferred"
                        basis_txt = "no explicit end date; %s %s + durationInDays %s = %s >= 2026-10-25" % (anchor_name, iso(anchor), dur_days, iso(inferred))
                        end = inferred
                if status is None:
                    if anchor and anchor > REF:
                        stats["excluded_future_start"] += 1
                        excluded.append((ocid, "start %s > ref" % anchor)); continue
                    if cfg.get("lookback_years") and anchor and (REF - anchor).days > 365 * cfg["lookback_years"]:
                        stats["excluded_no_end_older_than_lookback"] += 1
                        excluded.append((ocid, "no end; %s older than %d y" % (anchor, cfg["lookback_years"]))); continue
                    status = "end_date_unknown"
                    basis_txt = "no period end or duration published; %s %s (award/contract status %s)" % (anchor_name, iso(anchor), aw_status or ",".join(str(s) for s in con_status) or "n/a")
                stats["status_" + status] += 1
                # value
                val_amt = cur = None
                vd = {}
                for c in cons:
                    v = c.get("value") or {}
                    if num(v.get("amount")) is not None:
                        vd["contract_value"] = num(v.get("amount")); cur = cur or v.get("currency")
                if aw and (aw.get("value") or {}).get("amount") is not None:
                    vd["award_value"] = num(aw["value"].get("amount")); cur = cur or aw["value"].get("currency")
                if (tender.get("value") or {}).get("amount") is not None:
                    vd["tender_value"] = num(tender["value"].get("amount")); cur = cur or tender["value"].get("currency")
                val_amt = vd.get("contract_value", vd.get("award_value"))
                # commodity
                comm = {}
                items = (aw or {}).get("items") or tender.get("items") or []
                for it in items[:1]:
                    cl = it.get("classification") or {}
                    if cl.get("scheme"):
                        comm[str(cl["scheme"]).lower()] = cl.get("id")
                        comm[str(cl["scheme"]).lower() + "_description"] = cl.get("description")
                    for ac in it.get("additionalClassifications") or []:
                        if ac.get("scheme"):
                            comm.setdefault(str(ac["scheme"]).lower(), ac.get("id"))
                            comm.setdefault(str(ac["scheme"]).lower() + "_description", ac.get("description"))
                # identifiers
                ids = {"ocid": ocid, "release_id": latest.get("id"), "tender_id": tender.get("id")}
                if aw:
                    ids["award_id"] = aw.get("id")
                if cons:
                    ids["contract_ids"] = [c.get("id") for c in cons]
                    ids["contract_descriptions"] = [c.get("description") for c in cons if c.get("description")]
                for c in cons:
                    for k in ("contractNumber", "number"):
                        if c.get(k): ids[k] = c[k]
                if tender.get("procurementMethodDetails"): pass
                # record url
                rec_url = None
                tmpl = cfg.get("record_url_template")
                if tmpl:
                    try:
                        rec_url = tmpl.format(ocid=ocid, ocid_suffix=ocid.split("-")[-1], ocid_mid=(ocid.split("-")[2] if len(ocid.split("-")) > 2 else ocid), ocid_po="-".join(ocid.split("-")[2:]), tender_id=tender.get("id"), award_id=(aw or {}).get("id"), release_id=latest.get("id"))
                    except Exception:
                        rec_url = None
                if cfg.get("record_url_from_document"):
                    for dcol in (tender.get("documents") or []):
                        if dcol.get("documentType") in cfg["record_url_from_document"] and dcol.get("url"):
                            rec_url = dcol["url"]
                            rp = cfg.get("record_url_doc_replace")
                            if rp and rec_url.startswith(rp[0]):
                                rec_url = rp[1] + rec_url[len(rp[0]):]
                            break
                sa = sp.get("address") or {}
                rec = {
                    "record_id": "%s:%s%s" % (a.source, ocid, (":" + str(aw.get("id"))) if aw and len(awards) > 1 else ""),
                    "source": {"key": a.source, "name": cfg["name"], "publisher": cfg["publisher"], "dataset_url": cfg["dataset_url"],
                               "record_url": rec_url, "retrieved_at": retrieved},
                    "status": status, "status_basis": basis_txt,
                    "contract": {
                        "identifiers": ids,
                        "title": (aw or {}).get("title") or tender.get("title"),
                        "description": (aw or {}).get("description") or tender.get("description"),
                        "instrument_type": cfg.get("instrument_type", "contract (OCDS award/contract)"),
                        "procurement_method": tender.get("procurementMethodDetails") or tender.get("procurementMethod"),
                        "solicitation_procedure": tender.get("procurementMethod"),
                        "commodity": comm,
                        "value": val_amt, "currency": cur, "value_detail": vd,
                        "dates": {"published": iso(pub_date), "signed": iso(signed), "start": iso(start), "end": iso(end),
                                  "award": iso(award_date), "amended_last": None},
                        "related": {"ocds_record_url": cfg.get("ocds_record_url_template", "").format(ocid=ocid) or None,
                                    "tender_documents": [d.get("url") for d in tender.get("documents") or [] if d.get("url")][:10],
                                    "other_suppliers_on_award": [s.get("name") for s in ((aw or {}).get("suppliers") or []) if str(s.get("id")) not in can_parties],
                                    "main_procurement_category": tender.get("mainProcurementCategory"),
                                    "tender_status": tender.get("status"), "award_status": aw_status, "contract_status": con_status},
                    },
                    "buyer": {"name": buyer.get("name") or bparty.get("name"), "country": cfg["buyer_country"], "type": cfg.get("buyer_type", "public body"),
                              "identifiers": {"ocds_party_id": buyer.get("id"), **({"scheme": (bparty.get("identifier") or {}).get("scheme"), "id": (bparty.get("identifier") or {}).get("id")} if bparty.get("identifier") else {})},
                              "address": bparty.get("address") or {}, "contact": bparty.get("contactPoint") or {}},
                    "vendor": {"name": sp.get("name"), "country": "CA", "country_basis": basis,
                               "identifiers": {"ocds_party_id": sp.get("id"), **({(sp.get("identifier") or {}).get("scheme") or "identifier": (sp.get("identifier") or {}).get("id")} if sp.get("identifier") else {}),
                                               **{ (ai.get("scheme") or "additional_%d" % i): ai.get("id") for i, ai in enumerate(sp.get("additionalIdentifiers") or [])}},
                               "address": {"line1": sa.get("streetAddress"), "city": sa.get("locality"), "region": sa.get("region"), "postal_code": sa.get("postalCode"), "country": val or sa.get("countryName")},
                               "contact": sp.get("contactPoint") or {}},
                    "raw": {"latest_release": latest, "rows": rels if len(rels) > 1 else [], "n_releases_seen": len(rels),
                            "canadian_supplier_party_ids": list(can_parties.keys())},
                }
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
    stats["excluded_examples"] = excluded[:40]
    json.dump(stats, open(a.stats, "w"), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in stats.items() if k != "excluded_examples"}, indent=1))

if __name__ == "__main__":
    main()
