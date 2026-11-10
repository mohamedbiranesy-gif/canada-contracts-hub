#!/usr/bin/env python3
"""CHANGELOG.md + rows_changed.csv between two ranked files (downstream questions O2.1 / O2.2 / S3.1 / S3.2): rows added, removed,
mailbox changed, package moved — keyed by the organisation's first key. Run by tools/rank_tail.sh right after the table is written (until
2026-11-10 by rank.py itself, as a child process next to the ranker's own memory).
  python3 tools/release_diff.py <previous ranked_buyers.csv.gz> <new ranked_buyers.csv.gz> <out dir>
"""
import csv, datetime, gzip, os, subprocess, sys

csv.field_size_limit(1 << 30)


TRACKED = ["buyer_legal_name_as_published", "buyer_address", "buyer_phone", "buyer_website", "buyer_bn_as_published", "payment_terms_as_published", "po_required_as_published",
           "invoice_portal_url", "ap_phone", "invoice_mailing_address", "ap_contact_name_as_published", "vendor_legal_name", "vendor_bn9", "vendor_neq", "vendor_address",
           "contract_reference", "po_number_as_published", "email_check", "dmarc_policy", "ship_ready"]


def load(path):
    if not path or not os.path.exists(path):
        return {}
    out = {}
    keep = ["buyer", "rank_group", "email"] + TRACKED  # 2026-11-10: only the compared cells are kept (two whole tables in memory was 5 GB at 86,000 rows, next to rank.py's own)
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            k = (r.get("keys") or "").split("|")[0] or r.get("buyer", "")
            if k not in out:
                out[k] = {c: sys.intern(r.get(c) or "") for c in keep}  # most cells repeat ("", a DMARC policy, a package): each string is stored once
    return out


def main():
    prev, new, out = load(sys.argv[1]), load(sys.argv[2]), sys.argv[3]
    rows = []
    for k, r in new.items():
        p = prev.get(k)
        if not p:
            rows.append({"change": "row added", "buyer": r.get("buyer", ""), "rank_group": r.get("rank_group", ""), "email": r.get("email", ""), "detail": "new organisation in the ranked file"})
        else:
            if (p.get("email") or "") != (r.get("email") or ""):
                rows.append({"change": "mailbox changed", "buyer": r.get("buyer", ""), "rank_group": r.get("rank_group", ""), "email": r.get("email", ""), "detail": "was %s" % (p.get("email") or "(none)")})
            if (p.get("rank_group") or "") != (r.get("rank_group") or ""):
                rows.append({"change": "package moved", "buyer": r.get("buyer", ""), "rank_group": r.get("rank_group", ""), "email": r.get("email", ""), "detail": "was %s" % (p.get("rank_group") or "")})
            for f in TRACKED:  # field-level changes (downstream §9.3)
                a, b = (p.get(f) or ""), (r.get(f) or "")
                if a != b and (a or b):
                    rows.append({"change": "field changed: " + f, "buyer": r.get("buyer", ""), "rank_group": r.get("rank_group", ""), "email": r.get("email", ""),
                                 "detail": ("was '%s' → now '%s'" % (a[:120], b[:120])) if a else ("filled: '%s'" % b[:160])})
    for k, p in prev.items():
        if k not in new:
            rows.append({"change": "row removed", "buyer": p.get("buyer", ""), "rank_group": p.get("rank_group", ""), "email": p.get("email", ""), "detail": "no longer in the ranked file (folded into another row, mailbox rejected, or organisation dropped)"})
    with open(os.path.join(out, "rows_changed.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["change", "buyer", "rank_group", "email", "detail"]); w.writeheader(); w.writerows(rows)
    try:
        sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception:
        sha = ""
    c = {}
    for r in rows:
        c[r["change"]] = c.get(r["change"], 0) + 1
    gold_prev = sum(1 for r in prev.values() if r.get("rank_group") == "GOLD"); gold_new = sum(1 for r in new.values() if r.get("rank_group") == "GOLD")
    lines = ["# Changelog — build %s (%s)" % (datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"), sha or "source commit"), "",
             "Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.", "",
             "- rows: %d → %d" % (len(prev), len(new)), "- Gold (P01): %d → %d" % (gold_prev, gold_new)] + ["- %s: %d" % (k, v) for k, v in sorted(c.items())] + ["", "Row-level list: `rows_changed.csv` (change, buyer, rank_group, email, detail)."]
    if not prev:
        lines.append("\n(no previous ranked file was available to this build; the next build will carry a real delta)")
    open(os.path.join(out, "CHANGELOG.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines[:12]))


if __name__ == "__main__":
    main()
