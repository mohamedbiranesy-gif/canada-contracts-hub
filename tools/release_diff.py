#!/usr/bin/env python3
"""CHANGELOG.md + rows_changed.csv between two ranked files (downstream questions O2.1 / O2.2 / S3.1 / S3.2): rows added, removed,
mailbox changed, package moved — keyed by the organisation's first key. Run by rank.py at the end of every build.
  python3 tools/release_diff.py <previous ranked_buyers.csv.gz> <new ranked_buyers.csv.gz> <out dir>
"""
import csv, datetime, gzip, os, subprocess, sys


def load(path):
    if not path or not os.path.exists(path):
        return {}
    out = {}
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            k = (r.get("keys") or "").split("|")[0] or r.get("buyer", "")
            out.setdefault(k, r)
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
