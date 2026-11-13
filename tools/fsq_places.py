#!/usr/bin/env python3
"""Foursquare Open Source Places in Canada: websites, the one address a domain's places print, and the place that lists an organisation's own
telephone number (open data, Apache License 2.0, copyright Foursquare Labs, Inc.; no AI).

Foursquare published its places of interest as open data (2024-11-19: more than 100 million places worldwide; name, address, locality, region,
postal code, telephone, website, closing date, categories). The release read here is the geo-partitioned copy on Source Cooperative
(data.source.coop/fused/fsq-os-places/<release>/places/*.parquet: public, read with range requests, only the columns needed). Counted on the
release of 2025-02-06 (2026-11-13): 2,161,309 places in Canada, 1,046,347 with a website on 585,989 distinct hosts, 1,761,941 with a postal
code, 1,663,679 with a telephone number. Three uses, each the same as the Overture Maps places already serve (tools/credit_scan.py overture,
tools/phone_places.py), so that the rank build reads them without a new rule:

  ca      -> out/fsq_sites.csv      every host of an open place in Canada (dom, name, city, province, postcode, kind, objects): the scan's queue
                                    reads it beside the Overture list (organisations located in Canada whose sites no other list reached)
          -> out/fsq_addresses.csv  for every registrable domain whose open places in Canada all print ONE postal code: that place's street, city,
                                    province and postal code, its names and its place id (the Overture file's columns; datasets = Foursquare).
                                    A row by where the organisation is may stand on it only when nothing of the organisation's own pages located
                                    it and the place's name fits the organisation's (the ranker checks), and the cell says where it comes from.
  phones  -> out/fsq_phone_raw.csv  the open places in Canada whose telephone number is one an unlocated organisation prints on its own site
                                    (out/phone_targets.csv of tools/phone_places.py targets)
  pick    -> data/incoming/claude/fsq/phone_places.csv  one line per organisation located: the place bears its name or lists its website, and
                                    the places of that number print one postal code (tools/phone_places.py pick, the same tests)

A place Foursquare marks closed (date_closed) is never used. The email column of the places is never read: a mailbox is read only on the
organisation's own pages.

  python3 tools/fsq_places.py ca [--release R]
  python3 tools/fsq_places.py phones [--release R]   (after: python3 tools/phone_places.py targets)
  python3 tools/fsq_places.py pick
"""
import argparse, collections, csv, os, re, sys, time, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
OUT_PHONE = os.path.join(INC, "fsq", "phone_places.csv")
BUCKET = "https://data.source.coop/fused"
PREFIX = "fsq-os-places/"
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
DATASET = "Foursquare"


def _ls(prefix):
    req = urllib.request.Request("%s?list-type=2&prefix=%s&delimiter=/" % (BUCKET, prefix), headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=120).read().decode("utf-8", "replace")


def release_files(release=""):
    rels = sorted(re.findall(r"<Prefix>%s(\d{4}-\d{2}-\d{2})/</Prefix>" % re.escape(PREFIX), _ls(PREFIX)))
    if not rels:
        sys.exit("no Foursquare release listed at %s/%s" % (BUCKET, PREFIX))
    rel = release or rels[-1]
    keys = re.findall(r"<Key>([^<]+\.parquet)</Key>", _ls("%s%s/places/" % (PREFIX, rel)))
    if not keys:
        sys.exit("no place files in release %s" % rel)
    return rel, ["%s/%s" % (BUCKET, k) for k in keys]


def _con():
    import duckdb
    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs; SET enable_progress_bar=false; SET http_timeout=120000; SET memory_limit='3000MB'; SET threads=4;")
    return con


def cmd_ca(a):
    import credit_scan as CS
    import ap_crawler as C
    os.makedirs("out", exist_ok=True)
    t0 = time.time()
    rel, files = release_files(a.release)
    con = _con()
    cur = con.execute("""SELECT name, website, locality, region, postcode, address, fsq_category_labels[1], fsq_place_id
                         FROM read_parquet([%s]) WHERE country = 'CA' AND website IS NOT NULL AND website <> '' AND date_closed IS NULL"""
                      % ", ".join("'%s'" % f for f in files))
    sites, by_dom, n_obj = {}, {}, 0
    PCV = re.compile(r"[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]\d[ABCEGHJ-NPRSTV-Z]\d")
    while True:
        batch = cur.fetchmany(100000)
        if not batch:
            break
        for name, w, city, prov, pc, street, kind, pid in batch:
            h = CS.host_of((w or "").split(";")[0].strip())
            if not h or "." not in h or CS.PLATFORM.search(h) or not re.fullmatch(r"[a-z0-9.-]+", h):
                continue
            n_obj += 1
            o = sites.get(h)
            if o is None:
                sites[h] = [h, (name or "")[:100], city or "", prov or "", pc or "", (kind or "")[:80], 1]
            else:
                o[6] += 1
            d = C.registrable(h)
            p = re.sub(r"[^A-Z0-9]", "", (pc or "").upper())
            g = by_dom.setdefault(d, [set(), None, [], 0])
            g[3] += 1
            if name and name not in g[2] and len(g[2]) < 3:
                g[2].append(name[:100])
            if PCV.fullmatch(p):
                g[0].add(p)
                if g[1] is None or (street and not g[1][0]):
                    g[1] = (re.sub(r"\s+", " ", street or "").strip()[:120], city or "", prov or "", p, pid or "", (kind or "")[:80])
    n_addr = 0
    with open("out/fsq_addresses.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "names", "street", "city", "province", "postcode", "datasets", "place_id", "kind", "places", "release"])
        for d in sorted(by_dom):
            g = by_dom[d]
            if len(g[0]) != 1 or not g[1]:
                continue  # several postal codes (a chain, several sites) or none: no address is given for the domain
            st, city, prov, p, pid, kind = g[1]
            w.writerow([d, " | ".join(g[2]), st, city, prov, p, DATASET, pid, kind, g[3], rel])
            n_addr += 1
    with open("out/fsq_sites.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "name", "city", "province", "postcode", "kind", "objects"])
        for h in sorted(sites):
            w.writerow(sites[h])
    tl = collections.Counter(h.rsplit(".", 1)[-1] for h in sites)
    print("Foursquare %s: %d open places in Canada with a website, %d distinct hosts (%s); %d registrable domains whose places print one postal code "
          "(%d with several, %d with none) — %.0f s" % (rel, n_obj, len(sites), ", ".join("%s %d" % kv for kv in tl.most_common(5)), n_addr,
                                                       sum(1 for g in by_dom.values() if len(g[0]) > 1), sum(1 for g in by_dom.values() if not g[0]), time.time() - t0), flush=True)


def cmd_phones(a):
    phones = sorted({r["phone"] for r in csv.DictReader(open(a.targets, encoding="utf-8"))})
    rel, files = release_files(a.release)
    con = _con()
    con.execute("CREATE TABLE t (phone VARCHAR)")
    con.executemany("INSERT INTO t VALUES (?)", [(p,) for p in phones])
    t0 = time.time()
    cur = con.execute(r"""WITH q AS (SELECT fsq_place_id AS id, name, website, address AS street, locality AS city, region, postcode,
                                            right(regexp_replace(tel, '[^0-9]', '', 'g'), 10) AS phone
                                     FROM read_parquet([%s]) WHERE country = 'CA' AND tel IS NOT NULL AND date_closed IS NULL)
                          SELECT q.* FROM q JOIN t ON t.phone = q.phone""" % ", ".join("'%s'" % f for f in files))
    n = 0
    with open(a.raw, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["place_id", "name", "website", "street", "city", "region", "postcode", "phone", "release"])
        while True:
            b = cur.fetchmany(50000)
            if not b:
                break
            for r in b:
                w.writerow(list(r) + ["Foursquare %s" % rel])
                n += 1
    print("Foursquare %s: %d open places in Canada carry a target's number (%d numbers asked, %.0f s)" % (rel, n, len(phones), time.time() - t0), flush=True)


def cmd_pick(a):
    """tools/phone_places.py pick, on the Foursquare places, into data/incoming/claude/fsq/phone_places.csv"""
    import shutil
    import phone_places as PP
    os.makedirs(os.path.dirname(OUT_PHONE), exist_ok=True)
    PP.OUT = OUT_PHONE
    # phone_places.cmd_pick reads out/phone_places_raw.csv: the Foursquare listings go there for the pick, the Overture ones are kept aside
    keep = "out/phone_places_raw.overture.csv"
    had = os.path.exists("out/phone_places_raw.csv")
    if had:
        shutil.move("out/phone_places_raw.csv", keep)
    shutil.copy(a.raw, "out/phone_places_raw.csv")
    try:
        PP.cmd_pick(argparse.Namespace())
    finally:
        os.remove("out/phone_places_raw.csv")
        if had:
            shutil.move(keep, "out/phone_places_raw.csv")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["ca", "phones", "pick"])
    ap.add_argument("--release", default="")
    ap.add_argument("--targets", default="out/phone_targets.csv")
    ap.add_argument("--raw", default="out/fsq_phone_raw.csv")
    a = ap.parse_args()
    {"ca": cmd_ca, "phones": cmd_phones, "pick": cmd_pick}[a.cmd](a)


if __name__ == "__main__":
    main()
