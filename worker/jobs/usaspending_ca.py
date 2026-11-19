#!/usr/bin/env python3
"""US federal buyers of Canadian vendors, from USAspending (api.usaspending.gov, open, no key).

Two kinds of buyer, both with a contract of more than C$3,000 (US$2,200 at the fixed rate below) awarded or started on or
after 2023-11-19, the vendor located in Canada by the source's own recipient-location field:
  - prime contracts: the buyer is the awarding sub-agency ("Department of the Army", "National Park Service"), the vendor
    the prime recipient located in Canada;
  - subcontracts (FFATA): the buyer is the prime contractor (a company, a university), the vendor the sub-awardee located in
    Canada; the prime contractor's address comes from its USAspending recipient profile.

Writes to CCH_OUT: buyers.csv (one row per buyer, its largest qualifying contract), awards.csv.gz (every qualifying award),
summary.json. Polite: one request at a time, a pause between requests, the project user agent, retries with back-off.
"""
import csv
import gzip
import json
import os
import time
import urllib.error
import urllib.request

OUT = os.environ.get("CCH_OUT", ".")
WORK = os.environ.get("CCH_WORK", ".")
UA = "canada-contracts-hub-worker/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
API = "https://api.usaspending.gov"
SINCE = "2023-11-19"
USD_MIN = 2200  # C$3,000 at 1.38 CAD per USD
PAUSE = 1.0
MAX_PAGES = int(os.environ.get("CCH_MAX_PAGES") or 0)


def call(path, body=None, tries=6):
    for i in range(tries):
        try:
            req = urllib.request.Request(API + path, data=json.dumps(body).encode() if body is not None else None,
                                         headers={"User-Agent": UA, "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                time.sleep(PAUSE)
                return json.load(r)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            wait = 10 * (i + 1)
            print("retry %s in %ss: %r" % (path, wait, e)[:300], flush=True)
            time.sleep(wait)
    raise RuntimeError("gave up on " + path)


def search(subawards, fields, sort):
    today = time.strftime("%Y-%m-%d", time.gmtime())
    filters = {"award_type_codes": ["A", "B", "C", "D"], "time_period": [{"start_date": SINCE, "end_date": today}],
               "recipient_locations": [{"country": "CAN"}], "award_amounts": [{"lower_bound": USD_MIN}]}
    page = 1
    while True:
        r = call("/api/v2/search/spending_by_award/", {"filters": filters, "fields": fields, "page": page, "limit": 100,
                                                        "sort": sort, "order": "desc", "subawards": subawards})
        rows = r.get("results") or []
        yield from rows
        print("%s page %d: %d rows" % ("subawards" if subawards else "primes", page, len(rows)), flush=True)
        if not (r.get("page_metadata") or {}).get("hasNext") or not rows:
            break
        if MAX_PAGES and page >= MAX_PAGES:  # a test run
            break
        page += 1


def money(v):
    try:
        return float(v or 0)
    except (TypeError, ValueError):
        return 0.0


awards = []
for a in search(False, ["Award ID", "Recipient Name", "Award Amount", "Start Date", "End Date", "Base Obligation Date",
                        "Awarding Agency", "Awarding Sub Agency", "Description", "Contract Award Type"], "Award Amount"):
    started = a.get("Base Obligation Date") or a.get("Start Date") or ""
    if started < SINCE or money(a.get("Award Amount")) < USD_MIN:
        continue
    gid = a.get("generated_internal_id") or ""
    awards.append({"kind": "prime contract", "buyer": a.get("Awarding Sub Agency") or a.get("Awarding Agency") or "",
                   "buyer_parent": a.get("Awarding Agency") or "", "buyer_type": "US federal agency", "buyer_address": "",
                   "buyer_country": "US", "vendor": a.get("Recipient Name") or "", "vendor_country_basis": "USAspending recipient location country = CAN",
                   "award_id": a.get("Award ID") or "", "amount_usd": money(a.get("Award Amount")), "started": started,
                   "end_date": a.get("End Date") or "", "description": (a.get("Description") or "")[:300],
                   "record_link": "https://www.usaspending.gov/award/%s" % gid if gid else ""})
primes_seen = {}
for s in search(True, ["Sub-Award ID", "Sub-Awardee Name", "Sub-Award Date", "Sub-Award Amount", "Awarding Agency",
                       "Awarding Sub Agency", "Prime Award ID", "Prime Recipient Name", "prime_award_recipient_id",
                       "Sub-Award Description"], "Sub-Award Amount"):
    started = s.get("Sub-Award Date") or ""
    if started < SINCE or money(s.get("Sub-Award Amount")) < USD_MIN:
        continue
    pid = s.get("prime_award_recipient_id") or ""
    gid = s.get("prime_award_generated_internal_id") or ""
    awards.append({"kind": "subcontract", "buyer": s.get("Prime Recipient Name") or "", "buyer_parent": "",
                   "buyer_type": "prime contractor of a US federal contract", "buyer_address": "", "buyer_country": "",
                   "buyer_recipient_id": pid, "vendor": s.get("Sub-Awardee Name") or "",
                   "vendor_country_basis": "USAspending sub-awardee location country = CAN", "award_id": s.get("Sub-Award ID") or "",
                   "prime_award_id": s.get("Prime Award ID") or "", "amount_usd": money(s.get("Sub-Award Amount")),
                   "started": started, "end_date": "", "description": (s.get("Sub-Award Description") or "")[:300],
                   "awarding_agency": s.get("Awarding Sub Agency") or s.get("Awarding Agency") or "",
                   "record_link": "https://www.usaspending.gov/award/%s" % gid if gid else ""})
    if pid:
        primes_seen[pid] = None

# the prime contractor's own address (its USAspending recipient profile), cached across runs
cache_p = os.path.join(WORK, "recipients.json")
cache = json.load(open(cache_p)) if os.path.exists(cache_p) else {}
for i, pid in enumerate(primes_seen):
    if pid not in cache:
        try:
            r = call("/api/v2/recipient/%s/" % pid)
            loc = r.get("location") or {}
            cache[pid] = {"name": r.get("name"), "uei": r.get("uei"), "address": ", ".join(
                x for x in (loc.get("address_line1"), loc.get("city_name"), loc.get("state_code"), loc.get("zip"),
                            loc.get("country_name")) if x), "country": loc.get("country_code") or "",
                "business_types": r.get("business_types") or []}
        except RuntimeError:
            cache[pid] = {}
        if i % 50 == 0:
            json.dump(cache, open(cache_p, "w"))
            print("recipient profiles: %d of %d" % (i + 1, len(primes_seen)), flush=True)
json.dump(cache, open(cache_p, "w"))
for a in awards:
    c = cache.get(a.get("buyer_recipient_id") or "") or {}
    if c:
        a["buyer_address"] = c.get("address") or ""
        a["buyer_country"] = {"USA": "US", "CAN": "CA", "GBR": "GB"}.get(c.get("country") or "", c.get("country") or "")
        a["buyer_uei"] = c.get("uei") or ""

cols = ["kind", "buyer", "buyer_parent", "buyer_type", "buyer_address", "buyer_country", "buyer_uei", "vendor", "vendor_country_basis",
        "award_id", "prime_award_id", "awarding_agency", "amount_usd", "started", "end_date", "description", "record_link"]
tmp = os.path.join(OUT, "awards.csv.gz.tmp")
with gzip.open(tmp, "wt", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    w.writerows(awards)
os.replace(tmp, os.path.join(OUT, "awards.csv.gz"))
best = {}
for a in awards:
    k = (a["kind"] == "prime contract", a["buyer"].strip().upper())
    if k[1] and (k not in best or a["amount_usd"] > best[k]["amount_usd"]):
        best[k] = a
tmp = os.path.join(OUT, "buyers.csv.tmp")
with open(tmp, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["vendors_in_canada"] + cols, extrasaction="ignore")
    w.writeheader()
    for k, a in sorted(best.items(), key=lambda z: -z[1]["amount_usd"]):
        n = len({x["vendor"] for x in awards if (x["kind"] == "prime contract", x["buyer"].strip().upper()) == k})
        w.writerow(dict(a, vendors_in_canada=n))
os.replace(tmp, os.path.join(OUT, "buyers.csv"))
summary = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "since": SINCE, "usd_min": USD_MIN,
           "awards": len(awards), "prime_contracts": sum(a["kind"] == "prime contract" for a in awards),
           "subcontracts": sum(a["kind"] == "subcontract" for a in awards), "buyers": len(best),
           "buyers_federal": sum(1 for k in best if k[0]), "buyers_prime_contractors": sum(1 for k in best if not k[0])}
json.dump(summary, open(os.path.join(OUT, "summary.json"), "w"), indent=1)
print(json.dumps(summary), flush=True)
