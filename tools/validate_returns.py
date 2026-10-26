#!/usr/bin/env python3
"""Validate a result CSV before returning it.
Usage: python validate_returns.py <result.csv> [<task_file.csv>]
Prints problems; exit code 0 when clean.
"""
import csv, re, sys

FORMATS = {
    "buyer_ap": "task_id,buyer_key,org_name_as_found,ap_email,ap_email_type,invoice_portal_url,ap_phone,invoice_mailing_address,invoicing_requirements_summary,applies_to,evidence_url,evidence_quote,retrieved_date,status,queries_tried,notes",
    "vendor_contact": "task_id,vendor_key,official_website,website_verification,general_email,billing_or_ar_email,main_phone,address_on_site,business_number_if_published,other_identifiers,evidence_url,evidence_quote,retrieved_date,status,notes",
    "qa": "qa_id,record_id,link_opened,buyer_match,vendor_match,title_match,value_match,dates_match,status_supported,correct_values_if_mismatch,notes",
    "source_scouting": "source_name,publisher,url,coverage,data_access,supplier_location_field,award_or_start_date_field,end_date_or_term_field,approx_volume,login_required,bot_protection,already_in_covered_sources,how_to_pull,notes",
}
STATUS = {"buyer_ap": {"found", "portal_only", "not_published", "blocked", "unclear"},
          "vendor_contact": {"found", "website_only", "not_found", "blocked", "ambiguous"}}
EMAIL = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
# firstname.lastname style only; single-word locals (e.g. "dgfi", "approvisionnement") are often role mailboxes
PERSONAL = re.compile(r"^[a-z]{2,}[._-][a-z]{2,}$", re.I)
ROLE_HINT = re.compile(r"^citywpgap-(?:central|inquiries)$|^asg[.]payroll$|^ahs[.]vdhadapcontracts$|factur|invoice|payab|paiement|payment|compt|account|ap$|^ap[._-]|finance|achat|procure|purchas|approvision|supplier|fournisseur|vendor|info|contact|admin|billing|ar$|^ar[._-]|recevable|receivable|sales|ventes|service|support|bureau|office|reception|accueil|general|courrier|mail|treso|tresor|budget|contrat", re.I)


def main():
    path = sys.argv[1]
    kind = next((k for k in FORMATS if k in path), None)
    if not kind:
        sys.exit("file name must contain one of: " + ", ".join(FORMATS))
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig", newline="")))
    problems = []
    with open(path, encoding="utf-8-sig") as fh:
        header = fh.readline().strip()
    if header != FORMATS[kind]:
        problems.append("header differs from RETURN_FORMATS.md:\n  got:      %s\n  expected: %s" % (header, FORMATS[kind]))
    tasks = None
    if len(sys.argv) > 2:
        tasks = {r.get("task_id") or r.get("qa_id") for r in csv.DictReader(open(sys.argv[2], encoding="utf-8-sig", newline=""))}
    for i, r in enumerate(rows, 2):
        tid = r.get("task_id") or r.get("qa_id")
        if tasks is not None and tid not in tasks:
            problems.append("line %d: id %s is not in the task file" % (i, tid))
        st = r.get("status")
        if kind in STATUS and st not in STATUS[kind]:
            problems.append("line %d: status %r not allowed" % (i, st))
        for col in ("ap_email", "general_email", "billing_or_ar_email"):
            e = (r.get(col) or "").strip()
            if not e:
                continue
            if not EMAIL.match(e):
                problems.append("line %d: %s %r is not a single valid e-mail" % (i, col, e))
                continue
            local = e.split("@")[0]
            if PERSONAL.match(local) and not ROLE_HINT.search(local):
                problems.append("line %d: %s %r looks like a personal mailbox — remove it (role mailboxes only)" % (i, col, e))
            if not (r.get("evidence_url") or "").startswith("http"):
                problems.append("line %d: e-mail given without evidence_url" % i)
            if e.lower() not in (r.get("evidence_quote") or "").lower():
                problems.append("line %d: evidence_quote does not contain %s" % (i, e))
        if kind == "buyer_ap" and st == "found" and not (r.get("ap_email") or "").strip():
            problems.append("line %d: status found but ap_email empty" % i)
        if kind == "buyer_ap" and st == "portal_only" and not (r.get("invoice_portal_url") or "").startswith("http"):
            problems.append("line %d: status portal_only but no invoice_portal_url" % i)
        d = r.get("retrieved_date")
        if d is not None and d and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
            problems.append("line %d: retrieved_date must be YYYY-MM-DD" % i)
    print("%s: %d rows, %d problems" % (path, len(rows), len(problems)))
    for p in problems[:200]:
        print(" -", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
