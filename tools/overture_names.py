#!/usr/bin/env python3
"""The website a public places dataset lists under an organisation's own name, at its own postal code or in its own province or state,
for the named organisations of several lanes that have no site yet. No AI.

Many lanes name an organisation without its website: Health Canada's registers (the holders of a medical device establishment licence, billed
$5,519 a year; the owners of drugs on the market; device makers), the exchanges' lists of listed issuers (billed a yearly or monthly listing
fee). Their mailbox can only come from their own site, and the company-name autocomplete ties a site to fewer than one in four. The Overture
Maps places (Overture Maps Foundation open data, a release a month) list, for tens of millions of businesses, a name, an address and a
website - published, not guessed. tools/tm_register.py overture-sites uses them for the trademark owners abroad; this tool does the same for
any lane, in one scan of the places for all of them:

  an organisation whose name (accents, case, punctuation and legal forms left out) is the place's name, in the same country, at the same
  postal code (rank 0) or, when the lane gives no postal code, in the same province or state (rank 1) -> the place's website, at most three
  a key, the same postal code first.

A candidate is not a tie: each lane's own `sites --overture` reads its file and keeps a site only when the site's own pages tie it to the
organisation by that lane's tests (hc: the name in the site's title or site name, or the register's postal code printed on its home page;
exchange issuers: the issuer's symbol on its exchange printed on its home page, or its name and its investors' pages).

  python3 tools/overture_names.py query [--lanes hc,xc] [--dir GLOB --release R]
      -> data/incoming/claude/overture/<lane>_candidates.csv  (key, site, how, place_name, place_postcode, place_region, place_id, release)
"""
import argparse, collections, csv, glob, gzip, os, re, sys, time

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
OUT = os.path.join(INC, "overture")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"

COUNTRY = {"canada": "CA", "united states": "US", "usa": "US", "united states of america": "US", "china": "CN", "germany": "DE", "united kingdom": "GB",
           "uk": "GB", "france": "FR", "south korea": "KR", "korea, republic of": "KR", "switzerland": "CH", "italy": "IT", "israel": "IL", "japan": "JP",
           "sweden": "SE", "ireland": "IE", "netherlands": "NL", "australia": "AU", "denmark": "DK", "spain": "ES", "india": "IN", "malaysia": "MY",
           "taiwan": "TW", "belgium": "BE", "finland": "FI", "singapore": "SG", "austria": "AT", "hong kong": "HK", "thailand": "TH", "mexico": "MX",
           "brazil": "BR", "norway": "NO", "new zealand": "NZ", "poland": "PL", "portugal": "PT", "czech republic": "CZ", "turkey": "TR", "colombia": "CO"}
CA_PROV = {"A": "NL", "B": "NS", "C": "PE", "E": "NB", "G": "QC", "H": "QC", "J": "QC", "K": "ON", "L": "ON", "M": "ON", "N": "ON", "P": "ON",
           "R": "MB", "S": "SK", "T": "AB", "V": "BC", "X": "NT", "Y": "YT"}


def iso2(c):
    c = (c or "").strip()
    if len(c) == 2 and c.isalpha():
        return c.upper()
    return COUNTRY.get(c.lower(), "")


def norm_pc(pc, cc):
    p = re.sub(r"[^A-Z0-9]", "", (pc or "").upper())
    if cc == "US":
        return p[:5] if re.match(r"\d{5}", p) else ""
    if cc == "CA":
        return p if re.match(r"[A-Z]\d[A-Z]\d[A-Z]\d$", p) else ""
    return p


def region_of(cc, pc, address):
    if cc == "CA" and pc:
        return CA_PROV.get(pc[0], "")
    if cc == "US":
        m = re.search(r",\s*([A-Z]{2})\s*,?\s*\d{5}", address or "")
        return m.group(1) if m else ""
    return ""


def lane_hc():
    """Health Canada's register companies without a site on file (hc_registers.py)"""
    p = os.path.join(INC, "hc", "hc_companies.csv.gz")
    if not os.path.exists(p):
        return []
    have = set()
    sp = os.path.join(INC, "hc", "hc_sites.csv")
    if os.path.exists(sp):
        have = {r["key"] for r in csv.DictReader(open(sp, encoding="utf-8", newline=""))}
    out = []
    with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r["key"] in have:
                continue
            cc = iso2(r.get("country"))
            if not cc:
                continue
            pc = norm_pc(r.get("postal_code"), cc)
            out.append((r["key"], r["name"], cc, pc, region_of(cc, pc, r.get("address"))))
    return out


def lane_xc():
    """listed issuers of the TSX / TSX Venture Exchange without a site on file (exchange_issuers.py); the list gives the head office's province
    or state, no postal code"""
    p = os.path.join(INC, "exchange", "issuers.csv.gz")
    if not os.path.exists(p):
        return []
    have = set()
    sp = os.path.join(INC, "exchange", "issuer_sites.csv")
    if os.path.exists(sp):
        have = {r["key"] for r in csv.DictReader(open(sp, encoding="utf-8", newline=""))}
    out = []
    with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r["key"] in have or r.get("exchange") == "CSE":
                continue
            cc = {"Canada": "CA", "USA": "US"}.get(r.get("hq_region") or "", "")
            st = (r.get("hq_location") or "").strip().upper()
            if cc and re.match(r"[A-Z]{2}$", st):
                out.append((r["key"], r["name"], cc, "", st))
    return out


def lane_dian():
    """Colombian importers of goods invoiced from Canada without a site on file (tools/dian_cloud.py). DIAN gives no postal code: any place of
    the same name in Colombia is a candidate ("*"), and the lane keeps a site only when its own pages print the importer's NIT."""
    p = os.path.join(INC, "dian", "dian_pairs.csv.gz")
    if not os.path.exists(p):
        return []
    have = set()
    sp = os.path.join(INC, "dian", "dian_sites.csv")
    if os.path.exists(sp):
        have = {r["key"] for r in csv.DictReader(open(sp, encoding="utf-8", newline=""))}
    out, seen = [], set()
    with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r["key"] in have or r["key"] in seen:
                continue
            seen.add(r["key"])
            out.append((r["key"], r["importer"], "CO", "", "*"))
    return out


LANES = {"hc": lane_hc, "xc": lane_xc, "dian": lane_dian}


def query(a):
    import duckdb
    import ap_crawler as C
    import tm_register as TM
    want = {}
    for lane in a.lanes.split(","):
        for k, name, cc, pc, st in LANES[lane]():
            nk = TM.nkey_x(name)
            if nk and len(nk) >= 4 and (pc or st):
                want[k] = (lane, cc, nk, pc, st, name)
    print("organisations without a site, with a name and a postal code or a province / state: %d (%s)" % (
        len(want), dict(collections.Counter(v[0] for v in want.values()))), flush=True)
    if not want:
        return
    con = duckdb.connect()
    con.execute("SET enable_progress_bar=false;")
    con.execute("CREATE TABLE own (k VARCHAR, cc VARCHAR, nk VARCHAR)")
    con.executemany("INSERT INTO own VALUES (?, ?, ?)", [(k, v[1], v[2]) for k, v in want.items()])
    if a.dir and glob.glob(a.dir):
        src, release = "read_parquet('%s')" % a.dir, (a.release or "a local copy")
        cols, where = "name, website, postcode, region, country, id", "website IS NOT NULL AND country"
    else:
        import urllib.request
        ls = lambda prefix: urllib.request.urlopen(urllib.request.Request("%s/?list-type=2&prefix=%s&delimiter=/" % (TM.OVT_BUCKET, prefix),
                                                                         headers={"User-Agent": UA}), timeout=120).read().decode()
        rel = sorted(re.findall(r"<Prefix>(release/[0-9]{4}-[0-9]{2}-[0-9]{2}\.[0-9]+/)</Prefix>", ls("release/")))[-1]
        keys = re.findall(r"<Key>([^<]+\.parquet)</Key>", ls(rel + "theme=places/type=place/"))
        con.execute("INSTALL httpfs; LOAD httpfs;")
        src = "read_parquet([%s])" % ", ".join("'%s/%s'" % (TM.OVT_BUCKET, k_) for k_ in keys)
        release = rel.rstrip("/").rsplit("/", 1)[-1]
        cols = ('names."primary" AS name, websites[1] AS website, addresses[1].postcode AS postcode, addresses[1].region AS region, '
                'addresses[1].country AS country, id')
        where = "websites IS NOT NULL AND len(websites) > 0 AND addresses[1].country"
    norm_sql = ("trim(regexp_replace(regexp_replace(regexp_replace(regexp_replace(replace(lower(strip_accents(coalesce(p.name, ''))), '&', ' and '), "
                "'[^a-z0-9 ]+', ' ', 'g'), '%s', ' ', 'g'), '%s', ' ', 'g'), '\\s+', ' ', 'g'))" % (TM._SQL_FORMS, TM.EU_FORMS))
    ccs = ", ".join("'%s'" % c_ for c_ in sorted({v[1] for v in want.values()}))
    t0 = time.time()
    rows = con.execute("""WITH p AS (SELECT %s FROM %s WHERE %s IN (%s))
                          SELECT o.k, p.name, p.website, p.postcode, p.region, p.id FROM p JOIN own o ON o.cc = p.country AND o.nk = %s""" % (
        cols, src, where, ccs, norm_sql)).fetchall()
    print("places under the name of one of them: %d (%.0f s, Overture release %s)" % (len(rows), time.time() - t0, release), flush=True)
    best = collections.defaultdict(dict)
    for k, name, web, pcode, region, pid in rows:
        lane, cc, nk, pc, st, oname = want[k]
        host = re.sub(r"^https?://", "", (web or "").strip().lower()).split("/")[0].split(":")[0]
        host = host[4:] if host.startswith("www.") else host
        if not host or "." not in host or TM.nkey_x(name) != nk:
            continue
        d = C.registrable(host)
        ppc = norm_pc(pcode, cc)
        reg = (region or "").upper().split("-")[-1]
        rank = 0 if (pc and ppc == pc) else 1 if (st and reg == st and not pc) else 2 if (st == "*" and not pc) else 9
        if rank == 9:
            continue
        if d not in best[k] or rank < best[k][d][0]:
            best[k][d] = (rank, name, pcode or "", region or "", pid or "")
    os.makedirs(OUT, exist_ok=True)
    n = collections.Counter()
    for lane in a.lanes.split(","):
        path = os.path.join(OUT, "%s_candidates.csv" % lane)
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["key", "site", "how", "place_name", "place_postcode", "place_region", "place_id", "release"])
            for k in sorted(x for x in best if want[x][0] == lane):
                for d, (rank, name, pcode, region, pid) in sorted(best[k].items(), key=lambda kv: kv[1][0])[:3]:
                    w.writerow([k, d, "the same name at the same postal code" if rank == 0 else "the same name in the same province or state" if rank == 1 else "the same name in the same country",
                                name, pcode, region, pid, release])
                n[lane] += 1
        print("%s: %d organisations with a website an Overture place lists under their name -> %s" % (lane, n[lane], os.path.relpath(path, ROOT)), flush=True)
    with open(os.path.join(OUT, "last_query_%s.txt" % a.lanes.replace(",", "_")), "w", encoding="utf-8") as f:
        f.write("%d %s %s\n" % (int(time.time()), release, a.lanes))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["query"])
    ap.add_argument("--lanes", default="hc,xc")
    ap.add_argument("--dir", default="", help="a glob of local parquet files with the columns name, website, postcode, region, country, id (tests)")
    ap.add_argument("--release", default="")
    a = ap.parse_args()
    query(a)


if __name__ == "__main__":
    main()
