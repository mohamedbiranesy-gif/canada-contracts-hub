#!/usr/bin/env python3
"""Website candidates for trademark and patent owners from the Research Organization Registry (ROR) — open data, CC0 (no AI).

ROR (ror.org) is the registry of research organisations that publishers, funders and libraries use: 146,716 records in its dump of 2026-10-20
(universities, hospitals, institutes, funders, government laboratories, and 37,123 companies), each with its names (label, aliases), its country
and, for 141,340 of them, its website. An owner of Canadian trademarks or patents with no site on file whose very name (legal forms aside, as
tm_register.nkey_x compares names) is the name of ONE active ROR record with a website, in the owner's own country, gets that website as a
candidate. The candidate ties nothing by itself: tools/tm_register.py sites --ror reads the site and keeps it only when the site's own pages state
the owner's name with an address of the owner's state or country (abroad) or a Canadian postal code (in Canada), or print the owner's full legal
name with its legal form on its own legal page — the ROR listing being the second fact.

  python3 tools/ror_sites.py [--zip PATH]   -> data/incoming/claude/tm/tm_ror_sites.csv and data/incoming/claude/pt/pt_ror_sites.csv
"""
import argparse, collections, csv, gzip, json, os, re, sys, urllib.request, zipfile

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tm_register as TM  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
UA = TM.UA if hasattr(TM, "UA") else "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
COMMUNITY = "https://zenodo.org/api/communities/ror-data/records?q=&sort=newest&size=1"
COLS = ["owner_key", "site", "how", "place_id", "place_name", "place_postcode", "release"]
LANES = {"tm": (os.path.join(INC, "tm"), "tm_owners_abroad.csv.gz", "tm_owners_ca.csv.gz", "tm_sites_found.csv", "tm_ror_sites.csv"),
         "pt": (os.path.join(INC, "pt"), "pt_owners_abroad.csv.gz", "pt_owners_ca.csv.gz", "pt_sites_found.csv", "pt_ror_sites.csv")}


def get(url, path=None, timeout=300):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=timeout) as r:
        b = r.read()
    if path:
        open(path, "wb").write(b)
    return b


def host(u):
    h = re.sub(r"^https?://", "", (u or "").strip().lower()).split("/")[0].split(":")[0].split("?")[0]
    return h[4:] if h.startswith("www.") else h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", default="")
    a = ap.parse_args()
    release = ""
    zpath = a.zip
    if not zpath:
        rec = json.loads(get(COMMUNITY))["hits"]["hits"][0]
        f = next(x for x in rec["files"] if x["key"].endswith(".zip"))
        release = f["key"].replace("-ror-data.zip", "")
        zpath = os.path.join(os.environ.get("RUNNER_TEMP") or "/tmp", f["key"])
        get(f["links"]["self"], zpath, timeout=900)
        print("ROR %s: %d bytes" % (release, os.path.getsize(zpath)), flush=True)
    else:
        release = os.path.basename(zpath).replace("-ror-data.zip", "")
    with zipfile.ZipFile(zpath) as zf:
        n = next(i.filename for i in zf.infolist() if i.filename.endswith(".json"))
        recs = json.loads(zf.read(n))
    idx = collections.defaultdict(dict)
    for o in recs:
        if o.get("status") != "active":
            continue
        site = next((l["value"] for l in o.get("links") or [] if l.get("type") == "website"), "")
        h = host(site)
        if not h or "." not in h:
            continue
        cc = ((o.get("locations") or [{}])[0].get("geonames_details") or {}).get("country_code", "")
        disp = next((x["value"] for x in o.get("names") or [] if "ror_display" in (x.get("types") or [])), "")
        for x in o.get("names") or []:
            if "acronym" in (x.get("types") or []):
                continue
            k = TM.nkey_x(x["value"])
            if k and len(k.split()) + len(k) >= 7:
                idx[(cc, k)][h] = (o["id"], disp or x["value"])
    print("ROR %s: %d active records, %d names with a website" % (release, len(recs), len(idx)), flush=True)
    for lane, (d, abroad_f, ca_f, found_f, out_f) in LANES.items():
        found = {r["owner_key"] for r in csv.DictReader(open(os.path.join(d, found_f), encoding="utf-8", newline=""))} if os.path.exists(os.path.join(d, found_f)) else set()
        rows, cnt = [], collections.Counter()
        for fn, here in ((abroad_f, False), (ca_f, True)):
            p = os.path.join(d, fn)
            if not os.path.exists(p):
                continue
            with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh):
                    if r["owner_key"] in found:
                        continue
                    cc = "CA" if here else (r.get("country") or "").upper()
                    if not here and cc not in TM.ABROAD:
                        continue  # the site tests know the postal codes of these countries only
                    hits = idx.get((cc, TM.nkey_x(r.get("owner_name") or "")))
                    if not hits or len(hits) != 1:
                        cnt["no ROR record of that name in the owner's country, or several sites" if not hits else "several sites under that name"] += 1
                        continue
                    h, (rid, disp) = next(iter(hits.items()))
                    rows.append({"owner_key": r["owner_key"], "site": h, "how": "the owner's very name in its country (%s) in the Research Organization Registry" % cc,
                                 "place_id": rid, "place_name": disp, "place_postcode": "", "release": release})
                    cnt["candidate (%s)" % ("Canada" if here else "abroad")] += 1
        with open(os.path.join(d, out_f), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLS)
            w.writeheader()
            w.writerows(sorted(rows, key=lambda x: x["owner_key"]))
        print("%s: %d candidates -> %s (%s)" % (lane, len(rows), out_f, dict(cnt)), flush=True)


if __name__ == "__main__":
    main()
