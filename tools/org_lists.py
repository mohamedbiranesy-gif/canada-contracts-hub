#!/usr/bin/env python3
"""Owner goal (2026-10-28): 30,000+ organisations doing business in Canada, each with a published invoicing / AP
(or, failing that, purchasing or general) role mailbox. No AI. Builds crawler task lists of organisations with an
official website:
  1. Wikidata: every item located in Canada (P17 = Q16) with an official website (P856); one per website host.
  2. Our own vendor table: Canadian vendors with a verified website (Canadian businesses also buy from Canadian vendors).
Writes coord/tasks/claude/claude_buyer_ap_batch902.csv and _batch903.csv in the crawler clone (local work lists);
tools/ap_crawler.py reads them and finds the mailbox on each organisation's own site.
Usage (from ~/cch-crawler): python3 tools/org_lists.py"""
import csv, gzip, json, os, time, urllib.parse, urllib.request
UA = "canada-contracts-hub-orglists/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
HDR = ["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
       "known_general_email", "known_procurement_email", "contracts_in_dataset"]
os.makedirs("coord/tasks/claude", exist_ok=True)


def sparql(q):
    url = "https://query.wikidata.org/sparql?" + urllib.parse.urlencode({"query": q, "format": "json"})
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/sparql-results+json"})
            return json.load(urllib.request.urlopen(req, timeout=300))["results"]["bindings"]
        except Exception as e:
            print("sparql retry", attempt, repr(e)[:200], flush=True)
            time.sleep(30)
    return []


def wikidata():
    rows = sparql("SELECT ?item ?site WHERE { ?item wdt:P17 wd:Q16 ; wdt:P856 ?site . }")
    print("wikidata items with website in Canada:", len(rows), flush=True)
    sites, hosts = {}, set()
    for r in rows:
        q, s = r["item"]["value"].rsplit("/", 1)[-1], r["site"]["value"]
        h = (urllib.parse.urlparse(s).hostname or "").lower().removeprefix("www.") if hasattr(str, "removeprefix") else (urllib.parse.urlparse(s).hostname or "").lower()
        if h and h not in hosts and q not in sites and not h.endswith(("facebook.com", "twitter.com", "instagram.com", "youtube.com", "linkedin.com", "wikipedia.org", "google.com", "gc.ca", "canada.ca")):
            hosts.add(h)
            sites[q] = s
    ids, names = list(sites), {}
    for i in range(0, len(ids), 50):
        time.sleep(1.0)
        try:
            u = "https://www.wikidata.org/w/api.php?" + urllib.parse.urlencode({"action": "wbgetentities", "ids": "|".join(ids[i:i + 50]), "props": "labels", "languages": "en|fr", "format": "json"})
            ents = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60)).get("entities", {})
            for q, e in ents.items():
                lab = e.get("labels", {})
                names[q] = (lab.get("en") or lab.get("fr") or {}).get("value", "")
        except Exception as e:
            print("labels retry later", repr(e)[:120], flush=True)
    with open("coord/tasks/claude/claude_buyer_ap_batch902.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(HDR)
        n = 0
        for q, s in sites.items():
            if names.get(q):
                n += 1
                w.writerow(["CL-WD-%06d" % n, "", "wd:" + q, names[q], "", "CA", s, "", "", 0])
    print("wikidata organisations queued:", n, flush=True)


def vendors():
    p = "data/release/vendors_enriched.jsonl.gz"
    if not os.path.exists(p):
        print("no vendor table", flush=True)
        return
    n, hosts = 0, set()
    with gzip.open(p, "rt", encoding="utf-8") as fin, open("coord/tasks/claude/claude_buyer_ap_batch903.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(HDR)
        for line in fin:
            v = json.loads(line)
            ve = v.get("vendor_enrichment") or v
            site = ve.get("website") or v.get("website") or ""
            ok = "verif" in str(ve.get("website_verification") or v.get("website_verification") or "").lower() or ve.get("website_lookup_status") == "found"
            h = (urllib.parse.urlparse(site).hostname or "").lower() if site else ""
            if site and ok and h and h not in hosts:
                hosts.add(h)
                n += 1
                name = v.get("name") or v.get("vendor_name") or ve.get("legal_name") or v.get("legal_name") or h
                w.writerow(["CL-VD-%06d" % n, "", "v:" + str(v.get("vendor_key") or h), name, "", "CA", site, "", "", 0])
    print("vendor organisations queued:", n, flush=True)


vendors()
wikidata()
