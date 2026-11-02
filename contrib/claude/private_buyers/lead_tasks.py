#!/usr/bin/env python3
"""Crawl task list for the lead buyers of some lead files, with the same buyer keys as tools/lead_scanner.py --bridge, so
tools/crawl_some.py can read their sites now instead of waiting for the crawler's 6-hour reload.
  python3 contrib/claude/private_buyers/lead_tasks.py <out.csv> ~/cch-leads/socrata_irs990_*.jsonl ~/cch-leads/socrata_vnews_*.jsonl
"""
import csv, hashlib, json, sys

out, files = sys.argv[1], sys.argv[2:]
tasks = {}
for f in files:
    for line in open(f, encoding="utf-8", errors="replace"):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if not (r.get("website") or "").startswith("http"):
            continue
        name = (r["publisher"] if not r.get("buyer_unit") else "%s - %s" % (r["publisher"], r["buyer_unit"])).strip()
        key = "lead:" + hashlib.sha1(("%s|%s" % (r["domain"], name.lower())).encode()).hexdigest()[:16]
        tasks.setdefault(key, (name, r["website"]))
with open(out, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
                "known_general_email", "known_procurement_email", "contracts_in_dataset"])
    for i, (k, (n, site)) in enumerate(sorted(tasks.items()), 1):
        w.writerow(["CL-LT-%05d" % i, "", k, n, "", "", site, "", "", 1])
print(len(tasks), "buyers with a website")
