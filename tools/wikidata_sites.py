#!/usr/bin/env python3
"""Website candidates for trademark and patent owners from Wikidata's official website property (P856) — open data, CC0 (no AI).

Wikidata gives an official website (P856) to 784,918 items whose country (P17) is Canada, the United States, the United Kingdom, Australia or one
of the ten European countries the site tests know (2026-11-13). An owner of Canadian trademarks or patents with no site on file whose very name
(legal forms aside, as tm_register.nkey_x compares names) is the label (en, de, fr, it, es, nl, sv, da) or the official name (P1448) of items of
its own country that give ONE website gets that website as a candidate. The candidate ties nothing by itself: tools/tm_register.py sites --ror
reads the site and keeps it only when the site's own pages state the owner's name (with an address of its state or country abroad, a Canadian
postal code in Canada, or as the one owner of a distinctive name on the register), or print its full legal name on the site's own legal page.

The items are read from the QLever SPARQL endpoint for Wikidata (qlever.dev), one query per country and language, 12 seconds apart.

  python3 tools/wikidata_sites.py [--dir DIR]   -> data/incoming/claude/tm/tm_wd_sites.csv and data/incoming/claude/pt/pt_wd_sites.csv
                                                  (--dir: read p_<Qcountry>_<part>.tsv files already pulled there instead of pulling)
"""
import argparse, collections, csv, glob, gzip, os, re, sys, time, urllib.parse, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tm_register as TM  # noqa: E402
import hc_registers as HR  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
UA = HR.UA
ENDPOINT = "https://qlever.dev/api/wikidata"
QC = {"Q30": "US", "Q145": "GB", "Q408": "AU", "Q142": "FR", "Q183": "DE", "Q38": "IT", "Q29": "ES", "Q39": "CH", "Q40": "AT", "Q31": "BE", "Q35": "DK",
      "Q55": "NL", "Q34": "SE", "Q16": "CA",
      # 2026-11-13: the countries the site tests learned the same day (their owners' names are written in Latin letters on the register: the English
      # label and the official name only)
      "Q17": "JP", "Q884": "KR", "Q801": "IL", "Q20": "NO", "Q33": "FI", "Q664": "NZ", "Q865": "TW", "Q668": "IN", "Q148": "CN"}
SHORT = {"JP", "KR", "IL", "NO", "FI", "NZ", "TW", "IN", "CN"}
PARTS = ["en", "de", "fr", "it", "es", "nl", "sv", "da", "P1448"]
PREFIX = ("PREFIX wd: <http://www.wikidata.org/entity/> PREFIX wdt: <http://www.wikidata.org/prop/direct/> "
          "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> ")
COLS = ["owner_key", "site", "how", "place_id", "place_name", "place_postcode", "release", "source"]
LANES = {"tm": (os.path.join(INC, "tm"), "tm_owners_abroad.csv.gz", "tm_owners_ca.csv.gz", "tm_sites_found.csv", "tm_wd_sites.csv"),
         "pt": (os.path.join(INC, "pt"), "pt_owners_abroad.csv.gz", "pt_owners_ca.csv.gz", "pt_sites_found.csv", "pt_wd_sites.csv")}


def host(u):
    h = re.sub(r"^<?https?://", "", (u or "").strip().strip("<>").lower()).split("/")[0].split(":")[0].split("?")[0]
    return h[4:] if h.startswith("www.") else h


def pull(d, only=None, parts=None):
    os.makedirs(d, exist_ok=True)
    for q, cc in QC.items():
        if only and cc not in only:
            continue
        for part in (parts or (["en", "P1448"] if cc in SHORT else PARTS)):
            w = "?item wdt:P1448 ?name ." if part == "P1448" else "?item rdfs:label ?name . FILTER(LANG(?name) = \"%s\")" % part
            query = PREFIX + "SELECT ?item ?site ?name WHERE { ?item wdt:P856 ?site ; wdt:P17 wd:%s . %s }" % (q, w)
            out = os.path.join(d, "p_%s_%s.tsv" % (q, part))
            if os.path.exists(out) and os.path.getsize(out) > 100 and time.time() - os.path.getmtime(out) < 7 * 86400:
                continue  # pulled this week
            for attempt in range(4):
                req = urllib.request.Request(ENDPOINT, data=urllib.parse.urlencode({"query": query}).encode(),
                                             headers={"User-Agent": UA, "Accept": "text/tab-separated-values"})
                try:
                    with urllib.request.urlopen(req, timeout=300) as r:
                        b = r.read()
                except Exception as e:
                    print("%s %s: %s (attempt %d)" % (cc, part, str(e)[:100], attempt + 1), flush=True)
                    time.sleep(30 * (attempt + 1))
                    continue
                if b"An error has occurred while exporting" in b[-600:]:
                    print("%s %s: export cut short (attempt %d)" % (cc, part, attempt + 1), flush=True)
                    time.sleep(30 * (attempt + 1))
                    continue
                open(out, "wb").write(b)
                print("%s %s: %d lines" % (cc, part, b.count(b"\n")), flush=True)
                break
            time.sleep(12)


def build_index(d, only=None, parts=None):
    """{(country, nkey_x(name)): {host: (item, name)}} from the parts in d (pulled first when missing), for the countries asked (ISO codes);
    parts=["en", "P1448"] pulls only the English labels and the official names (two queries a country)"""
    pull(d, only, parts)
    idx = collections.defaultdict(dict)
    for p in glob.glob(os.path.join(d, "p_*.tsv")):
        cc = QC.get(os.path.basename(p).split("_")[1])
        if not cc or (only and cc not in only):
            continue
        with open(p, encoding="utf-8", errors="replace") as f:
            next(f, None)
            for l in f:
                t = l.rstrip("\n").split("\t")
                if len(t) < 3:
                    continue
                item = t[0].strip("<>").rsplit("/", 1)[-1]
                h = host(t[1])
                nm = re.sub(r'^"(.*)"(?:@[a-z-]+)?$', r"\1", t[2])
                if not h or "." not in h or HR.BAD.search(h) or not item.startswith("Q"):
                    continue
                k = TM.nkey_x(nm)
                if k and len(k.split()) + len(k) >= 7:
                    idx[(cc, k)].setdefault(h, (item, nm))
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="")
    a = ap.parse_args()
    d = a.dir or os.path.join(os.environ.get("RUNNER_TEMP") or "/tmp", "wikidata_parts")
    if not a.dir:
        pull(d)
    release = time.strftime("%Y-%m-%d", time.gmtime(max([os.path.getmtime(p) for p in glob.glob(os.path.join(d, "p_*.tsv"))] or [time.time()])))
    idx = collections.defaultdict(dict)
    for p in glob.glob(os.path.join(d, "p_*.tsv")):
        cc = QC.get(os.path.basename(p).split("_")[1])
        if not cc:
            continue
        with open(p, encoding="utf-8", errors="replace") as f:
            next(f, None)
            for l in f:
                t = l.rstrip("\n").split("\t")
                if len(t) < 3:
                    continue
                item = t[0].strip("<>").rsplit("/", 1)[-1]
                h = host(t[1])
                nm = re.sub(r'^"(.*)"(?:@[a-z-]+)?$', r"\1", t[2])
                if not h or "." not in h or HR.BAD.search(h) or not item.startswith("Q"):
                    continue
                k = TM.nkey_x(nm)
                if k and len(k.split()) + len(k) >= 7:
                    idx[(cc, k)].setdefault(h, (item, nm))
    print("Wikidata: %d names (country, name) with an official website" % len(idx), flush=True)
    for lane, (dd, abroad_f, ca_f, found_f, out_f) in LANES.items():
        found = {r["owner_key"] for r in csv.DictReader(open(os.path.join(dd, found_f), encoding="utf-8", newline=""))} if os.path.exists(os.path.join(dd, found_f)) else set()
        rows, cnt = [], collections.Counter()
        for fn, here in ((abroad_f, False), (ca_f, True)):
            p = os.path.join(dd, fn)
            if not os.path.exists(p):
                continue
            with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh):
                    if r["owner_key"] in found:
                        continue
                    cc = "CA" if here else (r.get("country") or "").upper()
                    if not here and cc not in TM.ABROAD:
                        continue
                    hits = idx.get((cc, TM.nkey_x(r.get("owner_name") or "")))
                    if not hits or len(hits) != 1:
                        cnt["no item of that name with a website in the owner's country" if not hits else "items of that name give several websites"] += 1
                        continue
                    h, (item, nm) = next(iter(hits.items()))
                    rows.append({"owner_key": r["owner_key"], "site": h, "how": "the owner's very name in its country (%s) in Wikidata" % cc,
                                 "place_id": "https://www.wikidata.org/wiki/%s" % item, "place_name": nm, "place_postcode": "", "release": release, "source": "wikidata"})
                    cnt["candidate (%s)" % ("Canada" if here else "abroad")] += 1
        with open(os.path.join(dd, out_f), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLS)
            w.writeheader()
            w.writerows(sorted(rows, key=lambda x: x["owner_key"]))
        print("%s: %d candidates -> %s (%s)" % (lane, len(rows), out_f, dict(cnt)), flush=True)


if __name__ == "__main__":
    main()
