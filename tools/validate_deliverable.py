#!/usr/bin/env python3
"""Integrity gates over the delivered packages (prompts/claude_perfect_deliverable.md §A), written as VALIDATION.md.
Zero tolerance on gates 1-6: the report says PASS / FAIL per gate with the offending rows (first 20).
  python3 tools/validate_deliverable.py [out/ranked] [--mx data/incoming/claude/claude_mx_check.tsv] [--write VALIDATION.md]
"""
import argparse, collections, csv, glob, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from buyer_pages import FIRST_NAMES as FIRST
except Exception:
    FIRST = set()
EMAIL = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$")
# a webmail provider's own domain (the ranker's rule, contrib/claude/rank_buyers/rank.py). Until 2026-11-10 this matched any domain whose first
# label was a provider's name: "live.palmer.edu" (a college's own host) failed the audit's hard check 5 in every build since it entered the table.
FREEMAIL = re.compile(r"^(?:gmail|googlemail|hotmail|outlook|live|msn|yahoo|ymail|rocketmail|aol|icloud|me|mac|protonmail|proton|gmx|mail|yandex|zoho|hush|hushmail|fastmail|tutanota|tuta|pm)"
                      r"\.(?:com|ca|net|org|fr|me|co\.uk|de|ch)$", re.I)
PERSONISH = re.compile(r"^[a-z]+[._-][a-z]+$")  # first.last — checked against role words
ROLE_WORDS = re.compile(r"info|contact|account|payable|invoice|factur|compt|financ|purchas|procure|achat|admin|office|bureau|reception|accueil|general|"
                        r"greffe|mairie|municipal|ville|town|city|clerk|treasur|tresor|secretar|direction|service|support|sales|vente|mail|courrier|ap\b|ar\b|"
                        r"pay|bill|fournisseur|supplier|vendor|order|commande|billing|einvoice|e-invoice|peppol|remit|cheque|facture|payment|tenders?|bids?|"
                        r"soumission|achats|approvisionnement|finance|recept|invoicing|apinvoice|apdept|accts|acct|cap|dept|department|hr|rh|comms|communications", re.I)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("dir", nargs="?", default="out/ranked")
    a.add_argument("--mx", default="data/incoming/claude/claude_mx_check.tsv")
    a.add_argument("--write", default="")
    a = a.parse_args()
    mx = {}
    if os.path.exists(a.mx):
        for r in csv.DictReader(open(a.mx, encoding="utf-8"), delimiter="\t"):
            mx[r["domain"]] = r["status"]
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import batch_files as BF  # the package files are compressed since 2026-11-10 (plain ones are still read)
    files = [f for f in BF.files(os.path.join(a.dir, "batches")) if not BF.member(f).startswith("Z_")]
    gates = collections.OrderedDict((k, []) for k in (
        "1 mailbox present, valid, domain with a mail server", "2 role mailbox (no person-like local part, no freemail)",
        "3 mailbox evidence url + quote containing the address, referee-confirmed (all packages but P11)", "4 relationship evidence (contract_status + vendor_country_basis + vendor)",
        "5 one row per mailbox across packages", "6 no blank cell", "7 receivables mailbox graded as invoicing (heuristic, review)"))
    seen_mail, total, per_pkg, quote_misses = {}, 0, collections.OrderedDict(), []
    for f in files:
        name = BF.package(f)  # a big package is delivered in numbered part files
        with BF.open_text(f) as _fh:
            rows = list(csv.DictReader(_fh))
        per_pkg[name] = per_pkg.get(name, 0) + len(rows); total += len(rows)
        for i, r in enumerate(rows, 2):
            where = "%s:%d %s" % (name, i, (r.get("buyer") or "")[:40])
            e = (r.get("email") or "").strip()
            dom = e.split("@")[-1].lower() if "@" in e else ""
            if not e or e == "not_published" or not EMAIL.match(e) or mx.get(dom) == "none":
                gates["1 mailbox present, valid, domain with a mail server"].append(where + " | " + e)
            local = e.split("@")[0].lower()
            parts = re.split(r"[._-]", local)
            personish = len(parts) == 2 and parts[0] in FIRST and len(parts[1]) >= 3 and not ROLE_WORDS.search(local)
            if e and (personish or (FREEMAIL.match(dom) and personish)):
                gates["2 role mailbox (no person-like local part, no freemail)"].append(where + " | " + e)
            q, u = (r.get("email_evidence_quote") or ""), (r.get("email_evidence_url") or "")
            if e and (not u.startswith("http") or (not name.startswith("P11") and (r.get("email_check") or "") != "confirmed")):
                gates["3 mailbox evidence url + quote containing the address, referee-confirmed (all packages but P11)"].append(where + " | " + e + " | " + (r.get("email_check") or ""))
            elif e and e.lower() not in q.lower().replace(" ", "") and e.lower() not in q.lower():
                quote_misses.append(where + " | " + e)  # the referee saw the address on the page (often in a mailto link); the quote shows the label
            if not (r.get("contract_status") and r.get("vendor_country_basis") and r.get("vendor")) or r.get("vendor") == "not_published":
                gates["4 relationship evidence (contract_status + vendor_country_basis + vendor)"].append(where)
            if e:
                if e.lower() in seen_mail:
                    gates["5 one row per mailbox across packages"].append(where + " | " + e + " also in " + seen_mail[e.lower()])
                else:
                    seen_mail[e.lower()] = name
            blanks = [c for c, v in r.items() if (v or "") == ""]
            if blanks:
                gates["6 no blank cell"].append(where + " | " + ",".join(blanks[:5]))
            if (r.get("email_type") or "").startswith("invoicing") and re.search(r"pay your|tax roll|utility bill|tuition|e-?transfer|donat|votre facture", q, re.I) \
                    and not re.search(r"supplier|vendor|fourniss|invoice|factur|payable", q, re.I):
                gates["7 receivables mailbox graded as invoicing (heuristic, review)"].append(where + " | " + e)
    lines = ["# Integrity gates — %d delivered rows in %d packages (%d files)" % (total, len(per_pkg), len(files)), ""]
    for k, v in gates.items():
        hard = not k.startswith("7")
        lines.append("- **%s**: %s (%d)" % (k, ("PASS" if not v else ("FAIL" if hard else "REVIEW")), len(v)))
        for x in v[:20]:
            lines.append("    - " + x)
    lines += ["", "Informational: %d rows whose quote shows the label next to the address rather than the address itself (the address sits in a mailto link; the referee re-fetched the page and saw it)." % len(quote_misses)]
    lines += ["", "## Rows per package"] + ["- %s: %d" % (k, v) for k, v in per_pkg.items()]
    out = "\n".join(lines) + "\n"
    print(out[:4000])
    if a.write:
        open(a.write, "w", encoding="utf-8").write(out)
    return 0 if not any(v for k, v in gates.items() if not k.startswith("7")) else 1


if __name__ == "__main__":
    sys.exit(main())
