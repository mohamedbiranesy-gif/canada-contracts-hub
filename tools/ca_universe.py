#!/usr/bin/env python3
"""Organisations already known to be located in Canada whose website is NOT on a .ca domain (owner 2026-11-09: "a Canadian entity gets paid").

The row factory (tools/cc_clients.py) reads the client / sponsor / dealer / member pages of every .ca host. Most Canadian businesses sit on
.com / .org hosts, and a host name proves nothing about a location, so those hosts are taken from what the dataset already holds:
  - the websites of the Canada-located vendors on delivered rows (their location is each row's `vendor_country_basis`);
  - the websites of delivered organisations located in Canada: the inferred-relationship package (located by a registry, OpenStreetMap,
    Wikidata or their own address) and any buyer whose address on file carries a Canadian postal code.
The universe only says WHICH hosts to look up in the Common Crawl index. A lead is still made only when the organisation's own page prints a
Canadian postal address (same proof as for .ca hosts), so each lead rests on two things: the dataset's location basis and its own address.

  python3 tools/ca_universe.py [--ranked coord/results/ranked/ranked_buyers.csv.gz]   ->  out/ca_universe.csv (dom, basis)
"""
import argparse, collections, csv, gzip, os, re, sys, urllib.parse

csv.field_size_limit(1 << 30)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ap_crawler import registrable  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
POSTAL = re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d\b")
SKIP = re.compile(r"(^|\.)(facebook|linkedin|twitter|instagram|youtube|google|wixsite|wordpress|blogspot|squarespace|weebly|godaddysites|myshopify|webflow|github|sites\.google|"
                  r"canada411|yellowpages|pagesjaunes|kijiji|indeed|eventbrite|amazon|ebay|yelp|tripadvisor|booking|airbnb|gov|gouv)\.", re.I)


def host_of(w):
    w = (w or "").strip()
    return (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower().removeprefix("www.") if w else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ranked", default=os.path.join(ROOT, "coord/results/ranked/ranked_buyers.csv.gz"))
    ap.add_argument("--out", default="out/ca_universe.csv")
    a = ap.parse_args()
    uni, n = {}, collections.Counter()
    with gzip.open(a.ranked, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            h = host_of(r.get("vendor_website"))
            d = registrable(h) if h and "." in h else ""
            if d and not d.endswith(".ca") and not SKIP.search(d + ".") and d not in uni and (r.get("vendor_country_basis") or "").strip():
                uni[d] = "a Canada-located vendor of the dataset"
                n["vendor sites"] += 1
            h = host_of(r.get("buyer_website"))
            d = registrable(h) if h and "." in h else ""
            if not d or d.endswith(".ca") or SKIP.search(d + ".") or d in uni:
                continue
            m = POSTAL.search((r.get("buyer_address") or "").upper())
            if m:
                uni[d] = "an organisation whose address in the dataset carries the Canadian postal code %s" % m.group(0)
                n["organisations with a Canadian postal code on file"] += 1
            elif r.get("tier") == "I":
                uni[d] = "an organisation the dataset locates in Canada (registry, OpenStreetMap, Wikidata or its own address)"
                n["organisations located in Canada (inferred-relationship package)"] += 1
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "basis"])
        for d in sorted(uni):
            w.writerow([d, uni[d]])
    print("Canada-located organisations on non-.ca domains: %d %s; top-level domains: %s" % (len(uni), dict(n), collections.Counter(d.rsplit(".", 1)[-1] for d in uni).most_common(8)))


if __name__ == "__main__":
    main()
