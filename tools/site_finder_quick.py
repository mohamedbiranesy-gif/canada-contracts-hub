#!/usr/bin/env python3
"""Official websites for a short, high-value list of buyers, from Wikidata (P856 official website). No AI.

Like tools/site_finder.py, but for one given list (active contract buyers and recent relationship buyers without a
website), with US / legal names cleaned first ("Icf Incorporated, L.L.C." -> "ICF", "Salk Institute For Biological
Studies, San Diego, California, The" -> "Salk Institute For Biological Studies"). A match must be an item in Canada or the
US whose label or alias equals the cleaned name. One request per second.

    python3 tools/site_finder_quick.py in.csv out.csv     (in: buyer_key,buyer_name ; out: a crawler task list)
"""
import csv, json, re, sys, time, unicodedata, urllib.parse, urllib.request

API = "https://www.wikidata.org/w/api.php?"
UA = "canada-contracts-hub-sitefinder/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
LEGAL = re.compile(r"[,\s]+(inc|incorporated|l\.?l\.?c|llc|ltd|limited|corp|corporation|co|company|plc|lp|l\.?p)\.?$", re.I)
last = [0.0]


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()


def clean(name):
    n = re.split(r"\s+-\s+", name)[0].strip()                      # "Department Of X - Unit" -> "Department Of X"
    n = re.sub(r",\s*the$", "", n, flags=re.I)                      # "..., The"
    n = re.sub(r"^the\s+", "", n, flags=re.I)
    n = re.sub(r",\s*[A-Z][\w .]+,\s*[A-Z][\w .]+$", "", n)        # ", San Diego, California"
    n = re.sub(r"\s+in the state of\s+.*$", "", n, flags=re.I)
    for _ in range(2):
        n = LEGAL.sub("", n).strip(" ,.")
    return n


def get(params):
    wait = last[0] + 1.0 - time.time()
    if wait > 0:
        time.sleep(wait)
    last[0] = time.time()
    try:
        req = urllib.request.Request(API + urllib.parse.urlencode(dict(params, format="json")), headers={"User-Agent": UA})
        return json.load(urllib.request.urlopen(req, timeout=30))
    except Exception:
        return {}


def find(name):
    for v in dict.fromkeys([clean(name), name]):
        if len(norm(v).split()) < 2:
            continue
        res = get({"action": "wbsearchentities", "search": v, "language": "en", "limit": 7, "type": "item"}).get("search", [])
        ids = [x["id"] for x in res if norm((x.get("match") or {}).get("text")) == norm(v) or norm(x.get("label")) == norm(v)]
        if not ids:
            continue
        ents = get({"action": "wbgetentities", "ids": "|".join(ids[:5]), "props": "claims"}).get("entities", {})
        for qid in ids:
            c = (ents.get(qid) or {}).get("claims", {})
            countries = {(x["mainsnak"].get("datavalue") or {}).get("value", {}).get("id") for x in c.get("P17", [])}
            sites = [(x["mainsnak"].get("datavalue") or {}).get("value") for x in c.get("P856", [])]
            if countries & {"Q16", "Q30"} and sites and sites[0]:
                return sites[0], qid
    return None


def main():
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8-sig")))
    out = open(sys.argv[2], "w", newline="", encoding="utf-8")
    w = csv.writer(out)
    w.writerow(["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website", "known_general_email",
                "known_procurement_email", "contracts_in_dataset"])
    n = 0
    for i, r in enumerate(rows, 1):
        hit = find(r["buyer_name"])
        if hit:
            n += 1
            w.writerow(["CL-SQ-%05d" % i, "website from Wikidata %s" % hit[1], r["buyer_key"], r["buyer_name"], "", "", hit[0], "", "", ""])
            out.flush()
            print("found", r["buyer_name"][:60], hit, flush=True)
    print("site_finder_quick: %d of %d" % (n, len(rows)), flush=True)


if __name__ == "__main__":
    main()
