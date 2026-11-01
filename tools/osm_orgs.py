#!/usr/bin/env python3
"""More organisations located in Canada with an official website, from OpenStreetMap (Overpass API). No AI.
Offices and companies, industry and trades first, then institutions (hospitals, clinics, schools, colleges, town
halls, libraries...) and hotels, then shops. One organisation per website host; hosts already queued are skipped.
Writes coord/tasks/claude/claude_buyer_ap_batch904.csv / 905 / 906 (local work lists for tools/ap_crawler.py).
Usage (from ~/cch-crawler): python3 tools/osm_orgs.py      Polite: one query at a time, pauses between queries."""
import csv, glob, json, subprocess, time, urllib.parse, urllib.request
UA = "canada-contracts-hub-osm/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
ENDPOINTS = ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter"]
HDR = ["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
       "known_general_email", "known_procurement_email", "contracts_in_dataset"]
SKIP = ("facebook.com", "instagram.com", "twitter.com", "x.com", "linkedin.com", "youtube.com", "google.com", "wikipedia.org",
        "yelp.", "tripadvisor.", "linktr.ee", "wixsite.com", "squarespace.com", "canada.ca", "gc.ca")
PROVINCES = ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "YT", "NT", "NU"]
GROUPS = [("904", ['["office"]', '["craft"]', '["industrial"]', '["man_made"="works"]', '["company"]']),
          ("905", ['["amenity"~"^(hospital|clinic|school|college|university|townhall|courthouse|library|community_centre|social_facility|dentist|doctors|veterinary|kindergarten|nursing_home)$"]',
                   '["healthcare"]', '["tourism"~"^(hotel|motel|museum)$"]', '["leisure"~"^(sports_centre|golf_course|marina)$"]']),
          ("906", ['["shop"]'])]


def overpass(q):
    for attempt in range(6):
        url = ENDPOINTS[attempt % 2]
        try:  # system curl: the Mac's Python 3.9 (LibreSSL) cannot complete TLS with overpass-api.de
            r = subprocess.run(["curl", "-s", "-f", "-m", "1000", "-A", UA, "--data-urlencode", "data=" + q, url],
                               capture_output=True, timeout=1100)
            if r.returncode:
                raise RuntimeError("curl exit %d" % r.returncode)
            return json.loads(r.stdout).get("elements", [])
        except Exception as e:
            print("overpass retry", attempt, repr(e)[:150], flush=True)
            time.sleep(60 * (attempt + 1))
    return []


hosts = set()
for f in glob.glob("coord/tasks/*/*_buyer_ap_batch*.csv"):
    for r in csv.DictReader(open(f, encoding="utf-8-sig")):
        h = (urllib.parse.urlparse((r.get("known_website") or "").strip()).hostname or "").lower()
        hosts.add(h[4:] if h.startswith("www.") else h)
for num, filters in GROUPS:
    rows = []
    for flt in filters:
        for prov in PROVINCES:  # one province per query: Canada-wide queries are cut off by the servers
            q = ('[out:json][timeout:600];area["ISO3166-2"="CA-%s"]->.a;(nwr["website"]%s(area.a);nwr["contact:website"]%s(area.a););out tags;'
                 % (prov, flt, flt))
            els = overpass(q)
            print(num, prov, flt[:40], len(els), flush=True)
            for e in els:
                t = e.get("tags", {})
                site, name = (t.get("website") or t.get("contact:website") or "").strip(), (t.get("name") or t.get("operator") or "").strip()
                if not site.startswith("http"):
                    site = "https://" + site if site and "." in site and " " not in site else ""
                h = (urllib.parse.urlparse(site).hostname or "").lower()
                h = h[4:] if h.startswith("www.") else h
                if site and name and h and h not in hosts and not any(s in h for s in SKIP):
                    hosts.add(h)
                    rows.append(("osm:%s%s" % (e["type"][0], e["id"]), name, site))
            time.sleep(10)
    with open("coord/tasks/claude/claude_buyer_ap_batch%s.csv" % num, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(HDR)
        for i, (k, name, site) in enumerate(rows, 1):
            w.writerow(["CL-OS%s-%06d" % (num, i), "", k, name, "", "CA", site, "", "", 0])
    print("batch", num, "organisations queued:", len(rows), flush=True)
