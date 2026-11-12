#!/usr/bin/env python3
"""The published table's rows, tested again with the rules as they stand in the repository now (2026-11-11).

  python3 tools/retest_rows.py ranked_buyers.csv.gz out.csv.gz

What for: a rule of the owner's test changes (tools/relationship_rows.py), a payee's payment page or fee schedule is added
(tools/payee_billing.py, tools/payee_fees.py), and the next build is an hour away — or GitHub Actions is down, as on 2026-11-11 20:40Z.
The published rows go through the same functions the ranker uses: the payee facts it would add to a row's empty cells, then the owner's
test. Five faults found by reading the owner's second test set are applied the way the ranker applies them from its next build on (an amount
that rests on a change of price or a discount is not a price; an owner-builder's licence is not billed by the contractors' fee table; an
access-to-information office is not an intake mailbox; a buyer that carries one person's name is flagged). No row is added and no value is
invented; the output is a table of the same columns, to draw a test set from (tools/test_sample.py) or to count what a rule changes.
"""
import collections, csv, gzip, re, sys, unicodedata
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
csv.field_size_limit(1 << 30)
import payee_billing as PB, relationship_rows as RR, vendor_billing as VB
from buyer_pages import FIRST_NAMES
ATI = re.compile(r"(?:^|[._-])ati(?:office)?(?:$|[._-])|foip|(?:^|[._-])foi(?:$|[._-])|acces-?(?:a-?l-?)?info", re.I)
LEGAL = re.compile(r"\b(inc|ltd|lt[ée]e|limited|corp|corporation|llc|llp|lp|enr|s\.?e\.?n\.?c|co|company|compagnie|cie|group|groupe|services?|construction|entreprises?|association|club|centre|center|studio|design|consult\w*)\b\.?", re.I)
n = collections.Counter()
src, dst = sys.argv[1], sys.argv[2]
with gzip.open(src, "rt", encoding="utf-8", errors="replace", newline="") as f, gzip.open(dst, "wt", encoding="utf-8", newline="") as g:
    r = csv.DictReader(f)
    cols = list(r.fieldnames)
    for c in ("bill_due_terms_as_published", "bill_remit_to_as_published"):
        if c not in cols:
            cols.insert(cols.index("service_stops_if_unpaid") + 1, c)
    w = csv.DictWriter(g, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    for x in r:
        before = (x.get("ship_ready") or "").startswith("yes")
        kind0 = RR.kind_of(x)
        cs = x.get("contract_status") or ""
        # 1. the body's own payment page and fee schedule (what bill_profile adds to rows whose cells are empty)
        if kind0 in ("licence or registration", "membership", "agent of record", "sponsorship", "dealership", "tenancy", "exchange listing"):
            out = {}
            if PB.fill(out, x, x.get("vendor") or "", x.get("vendor_website") or ""):
                for k, v in out.items():
                    if v and (not (x.get(k) or "").strip() or k == "bill_delivery_as_published"):
                        x[k] = v
                        n["cells written from the payee's own page or fee schedule"] += 1
        # 2. an owner-builder's licence is not billed by the contractors' fee table
        if "Régie du bâtiment" in (x.get("vendor") or "") and re.search(r"constructeur-propri", x.get("contract_title") or "", re.I) and "tarification-pour-lentrepreneur" in (x.get("bill_amount_basis") or ""):
            x["bill_amount_indicative"] = x["bill_amount_basis"] = ""
            n["owner-builder licences: the contractors' fee removed"] += 1
        # 3. an amount that rests on a change of price is not a price
        q = re.search(r"“(.*)”", x.get("bill_amount_basis") or "")
        if q and (x.get("bill_amount_basis") or "").startswith("the vendor's lowest published price") and VB._NOT_A_PRICE.search(q.group(1)):
            x["bill_amount_indicative"] = x["bill_amount_basis"] = ""
            n["amounts that rested on a sentence that is not a price: removed"] += 1
        # 4. the access-to-information office of a body is not its intake mailbox
        if ATI.search((x.get("email") or "").split("@")[0]):
            x["email_check"] = "not used: the mailbox of an access-to-information office"
            n["access-to-information mailboxes: not used"] += 1
        # 5. a buyer that carries one person's name (a given name and a surname, no word of an organisation)
        b = (x.get("buyer") or "").strip()
        t = re.findall(r"[A-Za-zÀ-ÿ'’.-]+", b)
        if kind0 != "public contract" and len(t) == 2 and len(b) <= 34 and not re.search(r"\d|[|/@&]", b) and t[0][:1].isupper() and t[1][:1].isupper():
            f0 = re.split(r"[-.]", unicodedata.normalize("NFKD", t[0]).encode("ascii", "ignore").decode().lower())[0]
            if f0 in FIRST_NAMES and not LEGAL.search(b + " " + (x.get("buyer_legal_name_as_published") or "").split(" (")[0]) and (x.get("sensitivity_flag") or "") != "yes":
                x["sensitivity_flag"], x["sensitivity_tag"] = "yes", "high-sensitivity buyer (one person's name: the site may be a person's own and not an organisation's)"
                n["buyers that carry one person's name: flagged"] += 1
        RR.owner_test(x)
        after = x["ship_ready"].startswith("yes")
        n["ready before"] += before
        n["ready now"] += after
        if before != after:
            n[("no longer ready: " if before else "ready now, was not: ") + kind0 + " — " + (x["ship_ready_missing"].split(";")[0][:70] if before else (x.get("vendor") or "")[:40])] += 1
        w.writerow(x)
for k, v in sorted(n.items(), key=lambda kv: -kv[1]):
    print("%7d  %s" % (v, k))
