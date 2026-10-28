#!/usr/bin/env python3
"""Find official websites for buyers that have none on file, from Wikidata (official website P856). No AI.
Only exact name matches (accents, case and punctuation ignored) of an item located in Canada (Q16) or the US (Q30).
Writes ~/cch-crawler-state/websites.tsv (buyer_key, website, Wikidata id); tools/ap_crawler.py reads it.
One request per second. Usage: python3 tools/site_finder.py   (run from the crawler clone)"""
import csv, glob, json, os, re, time, unicodedata, urllib.parse, urllib.request
OUT = os.path.expanduser("~/cch-crawler-state/websites.tsv")
UA = "canada-contracts-hub-sitefinder/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
API = "https://www.wikidata.org/w/api.php?"
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()

def get(params):
    time.sleep(1.0)
    try:
        req = urllib.request.Request(API + urllib.parse.urlencode(dict(params, format="json")), headers={"User-Agent": UA})
        return json.load(urllib.request.urlopen(req, timeout=30))
    except Exception:
        return {}

done = set(l.split("\t")[0] for l in open(OUT)) if os.path.exists(OUT) else set()
tried = os.path.expanduser("~/cch-crawler-state/websites_tried.txt")
done |= set(open(tried).read().split()) if os.path.exists(tried) else set()
for f in sorted(glob.glob("coord/tasks/*/*_buyer_ap_batch*.csv")):
    for r in csv.DictReader(open(f, encoding="utf-8-sig")):
        k, name = r.get("buyer_key"), r.get("buyer_name") or ""
        if not k or k in done or (r.get("known_website") or "").strip():
            continue
        done.add(k)
        open(tried, "a").write(k + "\n")
        variants = {name, re.split(r"\s+[-–(]\s*", name)[0]}
        hit = None
        for v in [x for x in variants if len(norm(x).split()) >= 3]:  # no one- or two-word names: too ambiguous
            for lang in ("fr", "en"):
                res = get({"action": "wbsearchentities", "search": v, "language": lang, "limit": 7, "type": "item"}).get("search", [])
                ids = [x["id"] for x in res if norm(x.get("match", {}).get("text")) == norm(v)]
                if not ids:
                    continue
                ents = get({"action": "wbgetentities", "ids": "|".join(ids), "props": "claims"}).get("entities", {})
                for qid, e in ents.items():
                    c = e.get("claims", {})
                    countries = {x["mainsnak"].get("datavalue", {}).get("value", {}).get("id") for x in c.get("P17", [])}
                    sites = [x["mainsnak"].get("datavalue", {}).get("value") for x in c.get("P856", [])]
                    if countries & {"Q16", "Q30"} and sites and sites[0]:
                        hit = (sites[0], qid)
                        break
                if hit: break
            if hit: break
        if hit:
            open(OUT, "a").write("%s\t%s\t%s\n" % (k, hit[0], hit[1]))
            print("found", name[:60], hit, flush=True)
print("site_finder finished", flush=True)
