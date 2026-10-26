#!/usr/bin/env python3
"""simap.ch public API: list award publications (award_tender, award_study_contract, award_competition, direct_award)
month by month (newest first), fetch publication-details for each, keep those with a vendor whose vendorAddress.countryId == 'CA'."""
import json, urllib.request, urllib.parse, time, datetime, os, sys
UA = {"User-Agent": "contracts-research/1.0", "Accept": "application/json"}
dl = "downloads/ch_simap"
API = "https://www.simap.ch/api/publications"
def get(url):
    for i in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        except Exception as e:
            err = e; time.sleep(2 + 3 * i)
    raise err
state_f = dl + "/state.json"
state = json.load(open(state_f)) if os.path.exists(state_f) else {"done_months": [], "seen_pubs": 0}
SEEN = set()
if os.path.exists(dl + "/listing.jsonl"):
    for _l in open(dl + "/listing.jsonl"):
        try: SEEN.add(json.loads(_l)["publicationId"])
        except Exception: pass
listing = open(dl + "/listing.jsonl", "a"); matches = open(dl + "/matches.jsonl", "a"); log = open(dl + "/crawl.log", "a")
# usage: crawl.py <worker_tag> <YYYY-MM> [<YYYY-MM> ...]   (months processed in the order given)
tag = sys.argv[1]
months = [datetime.date(int(a[:4]), int(a[5:7]), 1) for a in sys.argv[2:]]
state_f = dl + "/state_%s.json" % tag
state = json.load(open(state_f)) if os.path.exists(state_f) else {"done_months": [], "seen_pubs": 0}
for m in months:
    key = m.isoformat()[:7]
    if key in state["done_months"]: continue
    end = (m.replace(day=28) + datetime.timedelta(days=4)).replace(day=1) - datetime.timedelta(days=1)
    last = None; n = 0; nca = 0
    while True:
        q = [("newestPubTypes", t) for t in ("award_tender", "award_study_contract", "award_competition")] + [("newestPublicationFrom", m.isoformat()), ("newestPublicationUntil", end.isoformat())]
        if last: q.append(("lastItem", last))
        r = get(API + "/v2/project/project-search?" + urllib.parse.urlencode(q)); time.sleep(0.5)
        prs = r.get("projects") or []
        for p in prs:
            n += 1
            if p["publicationId"] in SEEN: continue   # already examined by an earlier (interrupted) run
            SEEN.add(p["publicationId"])
            listing.write(json.dumps({k: p.get(k) for k in ("id", "publicationId", "publicationDate", "pubType", "projectNumber", "publicationNumber")}) + "\n")
            try:
                det = get(API + "/v1/project/%s/publication-details/%s" % (p["id"], p["publicationId"])); time.sleep(0.5)
            except Exception as e:
                log.write("ERR detail %s %s\n" % (p["id"], e)); continue
            vs = (det.get("decision") or {}).get("vendors") or []
            if any(((v.get("vendorAddress") or {}).get("countryId") or "").upper() == "CA" for v in vs) or \
               any(((v.get("vendorAddress") or {}).get("countryId") or "").upper() == "CA" for lot in (det.get("lots") or det.get("lot") or []) if isinstance(lot, dict) for v in ((lot.get("decision") or {}).get("vendors") or [])):
                nca += 1
                matches.write(json.dumps({"search_row": p, "details": det, "retrieved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, ensure_ascii=False) + "\n"); matches.flush()
        last = (r.get("pagination") or {}).get("lastItem")
        if not prs or not last or len(prs) < (r.get("pagination") or {}).get("itemsPerPage", 20): break
    state["done_months"].append(key); state["seen_pubs"] += n
    json.dump(state, open(state_f, "w"))
    log.write("%s month %s awards=%d canada=%d\n" % (time.strftime("%FT%TZ", time.gmtime()), key, n, nca)); log.flush(); listing.flush()
log.write("DONE\n")
