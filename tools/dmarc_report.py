#!/usr/bin/env python3
"""DMARC.md + dmarc_no_enforcement.csv for the delivered packages (owner 2026-11-04: which mailboxes have no DMARC record or p=none).
Run by the rank-buyers workflow after batches.py, so the report always matches the delivered rows.
  python3 tools/dmarc_report.py [out/ranked] [--dmarc data/incoming/claude/claude_dmarc_check.tsv]
"""
import argparse, collections, csv, glob, os, re

LABEL = {"no_record": "no DMARC record", "none": "v=DMARC1; p=none (monitor only)", "quarantine": "p=quarantine", "reject": "p=reject",
         "invalid": "invalid DMARC record", "error": "lookup error", "not_checked": "not checked"}


def main():
    a = argparse.ArgumentParser()
    a.add_argument("dir", nargs="?", default="out/ranked")
    a.add_argument("--dmarc", default="data/incoming/claude/claude_dmarc_check.tsv")
    a = a.parse_args()
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import parted_csv as _PC  # the DNS-posture file is written in parts (tools/dmarc_check.py)
    dm = {r["domain"]: r for r in _PC.rows(a.dmarc, delimiter="\t")}
    out_rows, tot, ap, perpkg = [], collections.Counter(), collections.Counter(), collections.defaultdict(collections.Counter)
    import batch_files as BF  # the package files are compressed since 2026-11-10 (plain ones are still read)
    for f in BF.files(os.path.join(a.dir, "batches")):
        pkg = BF.package(f)
        if pkg.startswith("Z_"):
            continue
        short = pkg.split("_")[0]
        for r in csv.DictReader(BF.open_text(f)):
            d = (r.get("email") or "").lower().split("@")[-1]
            x = dm.get(d) or {"policy": "not_checked", "record_domain": "", "record": "", "spf_policy": "", "checked_date": ""}
            lab = LABEL.get(x["policy"], x["policy"])
            tot[lab] += 1; perpkg[short][lab] += 1
            if (r.get("email_type") or "").startswith("invoicing"):
                ap[lab] += 1
            if x["policy"] in ("no_record", "none", "invalid"):
                out_rows.append({"package": short, "buyer": r.get("buyer", ""), "buyer_type": r.get("buyer_type", ""), "jurisdiction": r.get("jurisdiction", ""), "email": r.get("email", ""),
                                 "email_type": r.get("email_type", ""), "mail_domain": d, "dmarc_status": lab, "dmarc_record_domain": x.get("record_domain", ""), "dmarc_record": x.get("record", ""),
                                 "spf_policy": r.get("spf_policy", ""), "mail_provider": r.get("mail_provider", ""), "checked_date": x.get("checked_date", ""), "buyer_website": r.get("buyer_website", ""),
                                 "relationship_kind": r.get("relationship_kind", "")})
    with open(os.path.join(a.dir, "dmarc_no_enforcement.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()) if out_rows else ["package"]); w.writeheader(); w.writerows(out_rows)
    lines = ["# DMARC posture of the delivered mailboxes", "",
             "DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). "
             "Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; "
             "the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).", "",
             "| posture | delivered rows | of which invoicing/AP mailboxes |", "|---|---|---|"]
    for k in ("no DMARC record", "v=DMARC1; p=none (monitor only)", "p=quarantine", "p=reject", "invalid DMARC record", "lookup error", "not checked"):
        if tot.get(k):
            lines.append("| %s | %d | %d |" % (k, tot[k], ap.get(k, 0)))
    lines += ["", "Rows without enforcement (no record / p=none / invalid): **%d**" % len(out_rows), "", "## By package (no record / p=none / quarantine / reject)"]
    for pkg in sorted(perpkg):
        c = perpkg[pkg]
        lines.append("- %s: %d / %d / %d / %d" % (pkg, c.get("no DMARC record", 0), c.get("v=DMARC1; p=none (monitor only)", 0), c.get("p=quarantine", 0), c.get("p=reject", 0)))
    open(os.path.join(a.dir, "DMARC.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines[:12]))


if __name__ == "__main__":
    main()
