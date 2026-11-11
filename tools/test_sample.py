#!/usr/bin/env python3
"""The owner's test set (2026-11-11 07:15 EST: "100 testing samples just to see the quality of the data … whether the data is actually
robust or not"): 100 rows of the published table drawn at random inside each kind of relationship, so that every kind is tested and none is
hand-picked. The draw is repeatable: the rows of a kind are sorted by their key and taken with random.Random(seed).

  python3 tools/test_sample.py ranked_buyers.csv.gz [--seed 20261111] [--out coord/pilot]
      -> <out>/TEST_SAMPLE_<build day>.csv        the 100 rows, every column, + sample_id, kind, what_to_check
      -> <out>/TEST_SAMPLE_<build day>.json       the same rows with the columns a reviewer reads, for the review page

What a reviewer checks on each row (the three links are in the row): (1) the mailbox is printed on the buyer's own page (email_evidence_url);
(2) the relationship is what the row says (contract_link, relationship_fact_basis); (3) the billing period and amount are what the vendor's
own page says (recurring_billing_basis, bill_amount_basis).
"""
import argparse, collections, csv, gzip, json, os, random, re, sys

csv.field_size_limit(1 << 30)

# kind -> (rows wanted, test on a row). First match wins, in this order.
KINDS = [
    ("public contract record", 10, lambda x: x["tier"] in ("A", "B") and "auditor of record" not in x["source"] and "customer story" not in x["source"]),
    ("Shopify store in Canada", 8, lambda x: x["tier"] == "T" and x["vendor"].startswith("Shopify") and _country(x) == "CA"),
    ("Shopify store in the United States", 7, lambda x: x["tier"] == "T" and x["vendor"].startswith("Shopify") and _country(x) == "US"),
    ("other subscription platform under the buyer's site", 10, lambda x: x["tier"] == "T" and "customer portal on the vendor's platform" in x["source"] and not x["vendor"].startswith("Shopify")),
    ("hosting / DNS / e-mail service in the buyer's DNS", 15, lambda x: x["tier"] == "T" and "public DNS records" in x["source"]),
    ("“powered by / hosted by” line on the buyer's site", 5, lambda x: x["tier"] == "T" and "credit line" in x["source"] and re.search(r"powered|propuls|host|h[ée]berg|maint", x["contract_status"] + " " + x.get("relationship_fact_basis", ""), re.I)),
    ("“website by” credit on the buyer's site", 5, lambda x: x["tier"] == "T" and "credit line" in x["source"]),
    (".ca domain name registration", 15, lambda x: x["tier"] == "R"),
    ("public register: licence, registration, accreditation", 6, lambda x: x["tier"] == "M" and re.match(r"holder of licence|registered with a Canadian regulatory|owner of |accredited business|client of a Canadian trademark agent", x["contract_status"])),
    ("member list of a Canadian body", 4, lambda x: x["tier"] == "M"),
    ("named as a client by the vendor", 10, lambda x: x["tier"] in ("C", "D")),
    ("link on the vendor's site", 3, lambda x: x["tier"] == "E"),
    ("inferred, no record", 2, lambda x: x["tier"] == "I"),
]
SHOW = ["buyer", "buyer_legal_name_as_published", "buyer_address", "buyer_phone", "buyer_website", "jurisdiction", "buyer_type",
        "email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote",
        "vendor", "vendor_legal_name", "vendor_address", "vendor_registered_address", "vendor_bn9", "vendor_gst_hst_derived", "vendor_website", "vendor_country_basis",
        "tier", "rank_group", "relationship_kind", "relationship_fact_basis", "contract_status", "contract_link", "source", "contract_title", "contract_reference",
        "contract_value", "currency", "award_date", "start_date", "end_date",
        "recurring_billing", "recurring_billing_basis", "billing_period_calculated", "bill_amount_indicative", "bill_amount_basis", "bill_items_as_published", "bill_currency_as_published",
        "bill_delivery_as_published", "bill_payment_method_as_published", "bill_tax_rule_as_published", "bill_identifier_format", "service_stops_if_unpaid",
        "invoice_readiness", "invoice_missing", "ap_grade", "payment_terms_as_published", "po_required_as_published", "invoice_portal_url", "invoicing_requirements",
        "invoice_reference_hint", "keys"]


def _country(x):
    a = x.get("buyer_address") or ""
    if re.search(r"\b[ABCEGHJ-NPRSTVXY]\d[A-Z] ?\d[A-Z]\d\b", a.upper()) or (x.get("buyer_website") or "").rstrip("/").endswith(".ca") or re.search(r"\bCanada\b", a):
        return "CA"
    if re.search(r"\b[A-Z]{2} \d{5}(?:-\d{4})?\b", a) or re.search(r"\b(?:USA|United States)\b", a):
        return "US"
    return (x.get("jurisdiction") or "")[:2].upper() if (x.get("jurisdiction") or "")[:2].upper() in ("CA", "US") else ""


def main():
    a = argparse.ArgumentParser()
    a.add_argument("table")
    a.add_argument("--seed", type=int, default=20261111)
    a.add_argument("--out", default="coord/pilot")
    a.add_argument("--day", default="")
    a = a.parse_args()
    opener = gzip.open if a.table.endswith(".gz") else open
    kind_of = lambda x: next((kind for kind, n, test in KINDS if test(x)), "")
    ident = lambda x: (x.get("keys") or "", x.get("email") or "")
    pools, cols = collections.defaultdict(list), None
    with opener(a.table, "rt", encoding="utf-8", errors="replace", newline="") as f:  # first pass: who is in which kind (the table does not fit in memory)
        r = csv.DictReader(f)
        cols = r.fieldnames
        for x in r:
            if x.get("email") and (x.get("sensitivity_flag") or "") != "yes":
                k = kind_of(x)
                if k:
                    pools[k].append(ident(x))
    rng, chosen = random.Random(a.seed), {}
    for kind, n, _ in KINDS:
        pool = sorted(pools[kind])
        take = rng.sample(pool, min(n, len(pool)))
        print("%-58s %7d rows in the table, %2d drawn" % (kind, len(pool), len(take)))
        for i, t in enumerate(take):
            chosen[t] = (kind, i)
    got = {}
    with opener(a.table, "rt", encoding="utf-8", errors="replace", newline="") as f:  # second pass: the drawn rows
        for x in csv.DictReader(f):
            t = ident(x)
            if t in chosen and t not in got:
                x = dict(x)
                x["kind"] = chosen[t][0]
                got[t] = x
    order = {kind: i for i, (kind, _, _) in enumerate(KINDS)}
    rows = sorted(got.values(), key=lambda x: (order[x["kind"]], chosen[ident(x)][1]))
    for i, x in enumerate(rows, 1):
        x["sample_id"] = "T%03d" % i
    day = a.day or __import__("datetime").date.today().isoformat()
    os.makedirs(a.out, exist_ok=True)
    p = os.path.join(a.out, "TEST_SAMPLE_%s.csv" % day)
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["sample_id", "kind"] + cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    clean = lambda v: "" if (v or "").strip() in ("", "not_published") else v.strip()
    with open(os.path.join(a.out, "TEST_SAMPLE_%s.json" % day), "w", encoding="utf-8") as f:
        json.dump({"seed": a.seed, "day": day, "pools": {k: len(v) for k, v in pools.items()},
                   "rows": [dict({"sample_id": x["sample_id"], "kind": x["kind"]}, **{c: clean(x.get(c)) for c in SHOW if clean(x.get(c))}) for x in rows]}, f, ensure_ascii=False)
    print("%d rows -> %s (seed %d)" % (len(rows), p, a.seed))


if __name__ == "__main__":
    main()
