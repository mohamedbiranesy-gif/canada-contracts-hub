#!/usr/bin/env python3
"""Task list for tools/org_contacts.py: every buyer and vendor website of the ranked deliverable (and of the lead buyers
with a website) whose registrable domain is not yet in the engine's resume file. Buyers lacking an address first.
  python3 contrib/claude/org_contacts/make_tasks.py [--done ~/cch-crawler-state/org_contacts.jsonl] -> contrib/claude/org_contacts/tasks_round2.csv.gz"""
import argparse, csv, gzip, json, os, sys, urllib.parse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.insert(0, ROOT + "/tools"); sys.argv_backup = sys.argv[:]; 
a = argparse.ArgumentParser(); a.add_argument("--done", default=""); a.add_argument("--out", default=ROOT + "/contrib/claude/org_contacts/tasks_round2.csv.gz")
a = a.parse_args(); sys.argv = sys.argv[:1]
from ap_crawler import registrable
done = set()
if a.done and os.path.exists(a.done):
    for l in open(a.done, encoding="utf-8", errors="replace"):
        try:
            done.add(json.loads(l)["domain"])
        except Exception:
            pass
def host(u):
    return (urllib.parse.urlparse(u if "//" in u else "https://" + u).hostname or "").lower().removeprefix("www.")
rows = list(csv.DictReader(open(ROOT + "/coord/results/ranked/ranked_buyers.csv", encoding="utf-8")))
def pri(r):
    g = r["rank_group"]; t = r["tier"]
    return (0 if g.startswith("GOLD") else 1 if t in "AB" else 2 if t in "TML" else 3 if t in "CDE" else 4, 0 if not r["buyer_address"] else 1)
seen, out = set(done), []
for r in sorted(rows, key=pri):
    h = host(r["buyer_website"]) if r["buyer_website"] else ""
    if h and "." in h and registrable(h) not in seen:
        seen.add(registrable(h)); out.append((r["keys"].split("|")[0], r["buyer"], "https://" + h, "buyer"))
for r in sorted(rows, key=lambda r: (0 if not r["vendor_emails"] else 1, 0 if not r["vendor_address"] else 1)):
    h = host(r["vendor_website"]) if r["vendor_website"] else ""
    if h and "." in h and not r["vendor"].startswith("inferred") and registrable(h) not in seen:
        seen.add(registrable(h)); out.append(("vd:" + registrable(h), r["vendor"], "https://" + h, "vendor"))
lf = ROOT + "/data/incoming/claude/claude_buyer_leads.csv"
if os.path.exists(lf):
    for r in csv.DictReader(open(lf, encoding="utf-8", errors="replace")):
        h = host(r.get("website") or "") if r.get("website") else ""
        if h and "." in h and registrable(h) not in seen:
            seen.add(registrable(h)); out.append((r["buyer_key"], r["buyer_name"], "https://" + h, "buyer"))
with gzip.open(a.out, "wt", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["key", "name", "website", "kind"]); w.writerows(out)
print(a.out, len(out), "new domains (%d done before)" % len(done))
