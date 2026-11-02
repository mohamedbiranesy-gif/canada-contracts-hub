#!/usr/bin/env python3
"""Merge subagent search outputs (B_*_out.tsv batch searches or D_*_out.tsv single searches) not yet marked .done into
coord/tasks/claude/claude_search_urls_pNN.csv (read by tools/deep_pages.py --urls) and, for single searches, a crawl task
list contrib/claude/private_buyers/dated_buyer_sitesNN.csv (read by tools/crawl_some.py). URLs must be on the website /
official site found; directory and news sites are never an official site. Marks the inputs .done.
  python3 contrib/claude/private_buyers/merge_search.py <dir-with-*_out.tsv> <pNN> [<sitesNN>]
"""
import csv, glob, os, sys, urllib.parse

BAD = ("linkedin", "zoominfo", "dnb.com", "bloomberg", "crunchbase", "wikipedia", "govtribe", "usaspending", "sam.gov",
       "highergov", "opencorporates", "newswire", "businesswire", "facebook", "indeed", "glassdoor", "yelp")
d, pnn = sys.argv[1], sys.argv[2]
snn = sys.argv[3] if len(sys.argv) > 3 else ""
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
out, seen, sites, used = [], set(), {}, []
for f in sorted(glob.glob(os.path.join(d, "*_out.tsv"))):
    if os.path.exists(f.replace("_out.tsv", ".done")):
        continue
    used.append(f)
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
        u, k = (r.get("url") or "").strip(), (r.get("buyer_key") or "").strip()
        w, o = (r.get("website") or "").strip(), (r.get("official_site") or "").strip()
        site = w if w.startswith("http") else o
        if not k or not u.startswith("http") or not site.startswith("http") or any(b in site for b in BAD):
            continue
        sh = (urllib.parse.urlparse(site).hostname or "").lower().removeprefix("www.")
        uh = (urllib.parse.urlparse(u).hostname or "").lower().removeprefix("www.")
        if not sh or not (uh == sh or uh.endswith("." + sh)) or (k, u) in seen:
            continue
        seen.add((k, u))
        out.append([k, r.get("buyer_name", ""), w if w.startswith("http") else "", "" if w.startswith("http") else o, u])
        if not w.startswith("http"):
            sites[k] = (r.get("buyer_name", ""), o)
p = os.path.join(root, "coord/tasks/claude/claude_search_urls_%s.csv" % pnn)
with open(p, "w", newline="", encoding="utf-8") as fh:
    wr = csv.writer(fh)
    wr.writerow(["buyer_key", "buyer_name", "website", "official_site", "url"])
    wr.writerows(out)
print("%s: %d urls, %d buyers, from %d files" % (p, len(out), len({x[0] for x in out}), len(used)))
if snn and sites:
    q = os.path.join(root, "contrib/claude/private_buyers/dated_buyer_sites%s.csv" % snn)
    with open(q, "w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh)
        wr.writerow(["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
                     "known_general_email", "known_procurement_email", "contracts_in_dataset"])
        for i, (k, (n, o)) in enumerate(sorted(sites.items()), 1):
            wr.writerow(["CL-DT%s-%05d" % (snn, i), "", k, n, "", "", o, "", "", 1])
    print("%s: %d official sites" % (q, len(sites)))
for f in used:
    open(f.replace("_out.tsv", ".done"), "w").close()
