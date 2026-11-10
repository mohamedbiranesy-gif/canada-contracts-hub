#!/usr/bin/env python3
"""Every contract record behind the delivered buyers, with every identifier (owner 2026-11-06: "PO matters, all identifiers, max").

The package rows carry ONE record per buyer. This export lists ALL records of each delivered organisation with a dated or listed
relationship (tiers A, B, L, C, D, F — the rows that came from the contract dataset), most recent first, capped at 500 per
organisation, each with the classified identifiers of rank.py (PO / procurement number, contract number, solicitation number,
award id, the buyer's vendor id, vendor registry ids, commodity codes, amendments, and the full verbatim identifier list), the
delivered buyer name, mailbox and mailbox grade, so accounts-payable matching has every reference the source publishes.
Output: out/ranked/contracts/contracts_of_delivered_buyers_partN_of_M.csv.gz (45 MB parts, gzipped for git).
  python3 contrib/claude/rank_buyers/contracts_export.py
"""
import collections, csv, datetime, gzip, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rank.py"), encoding="utf-8").read()
ns = {"re": re, "json": json}
exec(src[src.index("ID_CLASSES = ("):src.index("def rec_extra(c):")], ns)  # the identifier classifier, same code as the package rows
import unicodedata
ns.update({"unicodedata": unicodedata, "collections": collections})
exec(src[src.index("norm = lambda s:"):src.index("GRADE = {")], ns)          # norm, LEGAL_END, SQ_STOP, parent — the organisation grouping of rank.py
exec(src[src.index("JUR_SRC = "):src.index("JUR_DOM = ")], ns)
exec(src[src.index("PLACE = re.compile("):src.index("BAD_LOCAL = re.compile(")], ns)
exec(src[src.index("def jur_of_record(r):"):src.index("def jur_of_mail(email):")], ns)
parent, PLACE, jur_of_record = ns["parent"], ns["PLACE"], ns["jur_of_record"]


def group_key(r):
    """same as rank.py step 2: parent(canonical name), or 'generic ministry name | jurisdiction'"""
    be = r.get("buyer_enrichment") or {}
    name = be.get("canonical_name") or (r.get("buyer") or {}).get("name") or ""
    p = parent(name)
    if not p:
        return ""
    j = jur_of_record(r)
    po = parent((r.get("buyer") or {}).get("name") or "")
    if po and len(po.split()) <= 3 and not PLACE.search(po) and j:
        p = po + " | " + j
    return p
classify_ids, classify_plus = ns["classify_ids"], ns["classify_plus"]
CAP = 500        # records per organisation (tiers A/B/L/C/D/F)
CAP_GOLD = 5000  # owner D7 (2026-11-06): Gold buyers practically uncapped
COLS = ["buyer", "rank_group", "tier", "email", "email_type", "jurisdiction", "record_id", "source", "record_url", "vendor", "vendor_address", "vendor_country_basis",
        "status", "status_basis", "award_date", "start_date", "end_date", "value", "currency", "instrument_type", "procurement_method", "title", "description",
        "invoice_reference_hint", "po_number_as_published", "contract_or_agreement_number", "solicitation_or_tender_number", "award_or_notice_id", "buyer_vendor_id",
        "vendor_ids_in_record", "commodity_codes", "buyer_org_codes", "amendment_or_modification", "identifier_count", "all_identifiers"]


def award_date(c):
    d = c.get("dates") or {}
    return max((str(d.get(k) or "")[:10] for k in ("awarded", "award", "signed", "start")), default="") or str(d.get("published") or "")[:10]


def main():
    key2row = {}
    _plain = os.path.join(ROOT, "out/ranked/ranked_buyers.csv")  # 2026-11-10: the ranker writes only the compressed table (disk); a local run may still have the plain one
    with (open(_plain, encoding="utf-8") if os.path.exists(_plain) else gzip.open(_plain + ".gz", "rt", encoding="utf-8")) as f:
        for r in csv.DictReader(f):
            if (r.get("tier") or "") not in ("A", "B", "L", "C", "D", "F") or not (r.get("email") or ""):
                continue
            for k in (r.get("keys") or "").split("|"):
                if k.startswith("b:"):
                    key2row[k] = r
            if r.get("org_group_key"):
                key2row["g:" + r["org_group_key"]] = r
    print("delivered organisations with dataset records:", len({id(v) for v in key2row.values()}), flush=True)
    # pass 1 (light): the most recent CAP record ids per organisation
    per_org = collections.defaultdict(list)  # row id -> [(award_date, record_id)]
    n = 0
    path = os.path.join(ROOT, "data/release/canadian_vendor_contracts.jsonl.gz")
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            n += 1
            r = json.loads(line)
            row = key2row.get("g:" + group_key(r)) or key2row.get((r.get("buyer_enrichment") or {}).get("buyer_key"))
            if row:
                per_org[id(row)].append((award_date(r.get("contract") or {}), r.get("record_id", "")))
    wanted = {}
    rows_by_id = {id(v): v for v in key2row.values()}
    for rid, lst in per_org.items():
        lst.sort(reverse=True)
        cap = CAP_GOLD if rows_by_id[rid].get("rank_group") == "GOLD" else CAP
        for ad, rec_id in lst[:cap]:
            wanted[rec_id] = rid
    total_matched = sum(len(v) for v in per_org.values())
    gold_matched = sum(len(v) for rid, v in per_org.items() if rows_by_id[rid].get("rank_group") == "GOLD")
    print("records read:", n, "matched:", total_matched, "kept (cap %d/org, %d for Gold):" % (CAP, CAP_GOLD), len(wanted), flush=True)
    out_rows = []
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            rid = wanted.get(r.get("record_id", ""))
            if rid is None:
                continue
            row = rows_by_id[rid]
            c, v, sdef = r.get("contract") or {}, r.get("vendor") or {}, r.get("source") or {}
            d = c.get("dates") or {}
            cl = classify_plus(c, sdef.get("key") or "")
            va = v.get("address") or {}
            addr = va if isinstance(va, str) else ", ".join(str(va.get(x)) for x in ("line1", "line2", "street", "city", "region", "postal_code", "country") if va.get(x))
            out_rows.append({"buyer": row["buyer"], "rank_group": row.get("rank_group", ""), "tier": row.get("tier", ""), "email": row.get("email", ""), "email_type": row.get("email_type", ""),
                             "jurisdiction": row.get("jurisdiction", ""), "record_id": r.get("record_id", ""), "source": sdef.get("name", ""), "record_url": sdef.get("record_url") or sdef.get("dataset_url") or "",
                             "vendor": v.get("name", ""), "vendor_address": addr, "vendor_country_basis": v.get("country_basis") or "", "status": r.get("status", ""), "status_basis": (r.get("status_basis") or "")[:300],
                             "award_date": award_date(c), "start_date": str(d.get("start") or "")[:10], "end_date": str(d.get("end") or "")[:10], "value": c.get("value", ""), "currency": c.get("currency", ""),
                             "instrument_type": str(c.get("instrument_type") or "")[:80], "procurement_method": str(c.get("procurement_method") or c.get("solicitation_procedure") or "")[:80],
                             "title": (c.get("title") or "")[:200], "description": re.sub(r"\s+", " ", str(c.get("description") or ""))[:200], **{k: cl[k] for k in cl}})
    out_rows.sort(key=lambda x: (x["rank_group"] != "GOLD", x["buyer"], x["award_date"]), reverse=False)
    os.makedirs(os.path.join(ROOT, "out/ranked/contracts"), exist_ok=True)
    approx = sum(len(str(v)) + 1 for x in out_rows[:2000] for v in x.values()) / max(1, min(2000, len(out_rows))) * len(out_rows)
    parts = max(1, int(approx // (45 * 1024 * 1024)) + 1)
    step = -(-len(out_rows) // parts)
    for pi in range(parts):
        path = os.path.join(ROOT, "out/ranked/contracts/contracts_of_delivered_buyers_part%d_of_%d.csv.gz" % (pi + 1, parts))
        with gzip.open(path, "wt", newline="", encoding="utf-8", compresslevel=6) as fh:
            w = csv.DictWriter(fh, fieldnames=COLS); w.writeheader(); w.writerows(out_rows[pi * step:(pi + 1) * step])
    po = sum(1 for x in out_rows if x["po_number_as_published"]); con = sum(1 for x in out_rows if x["contract_or_agreement_number"])
    summary = ["# Contracts of the delivered buyers — %s" % datetime.date.today().isoformat(), "",
               "%d contract records of %d delivered organisations (tiers A/B/L/C/D/F, most recent first, at most %d per organisation, %d for Gold buyers), in %d gzipped part files." % (len(out_rows), len(per_org), CAP, CAP_GOLD, parts),
               "- ceiling: the delivered organisations have %d records with Canada-located vendors in the dataset in all (%d of them Gold buyers'); the cap drops only the oldest records of the very largest buyers" % (total_matched, gold_matched),
               "- with a purchase-order / procurement number: %d" % po, "- with a contract / agreement number: %d" % con,
               "- with a solicitation / tender number: %d" % sum(1 for x in out_rows if x["solicitation_or_tender_number"]),
               "- with the buyer's own vendor id for the supplier: %d" % sum(1 for x in out_rows if x["buyer_vendor_id"]),
               "- Gold buyers' records: %d" % sum(1 for x in out_rows if x["rank_group"] == "GOLD"), ""]
    open(os.path.join(ROOT, "out/ranked/contracts/CONTRACTS.md"), "w", encoding="utf-8").write("\n".join(summary) + "\n")
    print("\n".join(summary), flush=True)


if __name__ == "__main__":
    main()
