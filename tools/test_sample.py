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

# 2026-11-11 13:00-14:20 EST, the owner: "a 100 pool definitely needs to be ship ready … a row that isn't ship ready isn't a row"; a row is a
# relationship billed on invoice and payable by bank transfer, its invoice fields tailored to its kind. The draw is made among the rows whose
# ship_ready says yes (tools/relationship_rows.py: owner_test), inside each kind of relationship so that every kind is tested and none is
# hand-picked. A kind with fewer ready rows than its share gives what it has; the rest of the hundred is drawn among all the other ready rows.
_K = lambda x: (x.get("invoice_fields_for_kind") or "").split(":")[0]
_AP = lambda x: (x.get("email_type") or "").startswith(("invoicing", "finance"))
# 2026-11-11 16:01 EST (AGENTS.md §1, rule 13): a row may also stand on where the organisation is — its own share of the draw, so that the
# kind that carries the most rows is the kind that is tested most.
KINDS = [
    ("public contract — invoicing, AP or finance mailbox", 12, lambda x: _K(x) == "public contract" and _AP(x)),
    ("public contract — purchasing or general mailbox", 12, lambda x: _K(x) == "public contract"),
    ("licence or registration with a Canadian public body", 18, lambda x: _K(x) == "licence or registration"),
    ("electricity account by where the organisation is", 26, lambda x: _K(x) == "utility account by location"),
    ("service of a Canadian vendor that takes a bank payment", 8, lambda x: _K(x) == "service seen on the buyer's side"),
    ("membership of a Canadian body", 10, lambda x: _K(x) == "membership"),
    ("dealer, tenant, sponsor or exhibitor of a Canadian body", 8, lambda x: _K(x) in ("dealership", "tenancy", "sponsorship")),
    ("client of a Canadian agent of record", 6, lambda x: _K(x) == "agent of record"),
]
SHOW = ["ship_ready", "payment_route", "payment_route_basis", "invoice_fields_for_kind", "invoice_fields_missing_for_kind", "vendor_tax_or_registration_number",
        "buyer", "buyer_legal_name_as_published", "buyer_address", "buyer_phone", "buyer_website", "jurisdiction", "buyer_type",
        "email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote",
        "vendor", "vendor_legal_name", "vendor_address", "vendor_registered_address", "vendor_bn9", "vendor_gst_hst_derived", "vendor_website", "vendor_country_basis",
        "tier", "rank_group", "relationship_kind", "relationship_fact_basis", "contract_status", "contract_link", "source", "contract_title", "contract_reference",
        "contract_value", "currency", "award_date", "start_date", "end_date",
        "amount_mark", "recurring_billing", "recurring_billing_basis", "billing_period_calculated", "bill_amount_indicative", "bill_amount_basis", "bill_amount_calculated", "bill_items_as_published", "bill_currency_as_published",
        "bill_delivery_as_published", "bill_payment_method_as_published", "bill_tax_rule_as_published", "bill_identifier_format", "service_stops_if_unpaid", "bill_due_terms_as_published", "bill_remit_to_as_published",
        "invoice_fields_present", "invoice_fields_missing", "invoice_readiness", "invoice_missing", "ap_grade", "payment_terms_as_published", "po_required_as_published", "invoice_portal_url", "invoicing_requirements",
        "invoice_reference_hint", "other_relationship_sources", "keys"]


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
    a.add_argument("--rows", type=int, default=100)
    a.add_argument("--built", default="", help="the build the table comes from (coord/results/ranked/BUILD.json: built), shown on the review page")
    a = a.parse_args()
    opener = gzip.open if a.table.endswith(".gz") else open
    kind_of = lambda x: next((kind for kind, n, test in KINDS if test(x)), "")
    ident = lambda x: (x.get("keys") or "", x.get("email") or "")
    pools, cols, n_ready = collections.defaultdict(list), None, 0
    with opener(a.table, "rt", encoding="utf-8", errors="replace", newline="") as f:  # first pass: who is in which kind (the table does not fit in memory)
        r = csv.DictReader(f)
        cols = r.fieldnames
        for x in r:
            if x.get("email") and (x.get("ship_ready") or "").startswith("yes"):
                k = kind_of(x)
                if k:
                    pools[k].append(ident(x))
                n_ready += 1
    rng, chosen = random.Random(a.seed), {}
    for kind, n, _ in KINDS:
        pool = sorted(pools[kind])
        take = rng.sample(pool, min(n, len(pool)))
        print("%-58s %7d rows in the table, %2d drawn" % (kind, len(pool), len(take)))
        for i, t in enumerate(take):
            chosen[t] = (kind, i)
    short = a.rows - len(chosen)
    if short > 0:  # a kind with fewer ready rows than its share: the rest of the hundred among all the other ready rows, each under its own kind
        rest = sorted((t, kind) for kind, _, _ in KINDS for t in pools[kind] if t not in chosen)
        for j, (t, kind) in enumerate(rng.sample(rest, min(short, len(rest)))):
            chosen[t] = (kind, 1000 + j)
    print("ship-ready rows in the table: %d; drawn: %d" % (n_ready, len(chosen)))
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
        json.dump({"seed": a.seed, "day": day, "built": a.built, "ready_in_table": n_ready, "pools": {k: len(v) for k, v in pools.items()},
                   "rows": [dict({"sample_id": x["sample_id"], "kind": x["kind"]}, **{c: clean(x.get(c)) for c in SHOW if clean(x.get(c))}) for x in rows]}, f, ensure_ascii=False)
    print("%d rows -> %s (seed %d)" % (len(rows), p, a.seed))


if __name__ == "__main__":
    main()
