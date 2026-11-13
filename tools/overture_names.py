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


def lane_cb():
    """buyers under a current contract with a Canada-located vendor that have neither a mailbox nor a website on file (rank.py writes the list:
    coord/results/ranked/contract_buyers_without_website.csv)"""
    p = os.path.join(ROOT, "coord/results/ranked/contract_buyers_without_website.csv")
    if not os.path.exists(p):
        return []
    have = set()
    sp = os.path.join(OUT, "cb_sites.csv")
    if os.path.exists(sp):
        have = {r["key"] for r in csv.DictReader(open(sp, encoding="utf-8", newline=""))}
    out = []
    for r in csv.DictReader(open(p, encoding="utf-8", newline="")):
        if r["buyer_key"] in have:
            continue
        cc = iso2(r.get("country")) or ("CA" if re.match(r"[A-Z]\d[A-Z]\s?\d[A-Z]\d$", (r.get("postal_code") or "").upper().strip()) else "")
        if not cc:
            continue
        pc = norm_pc(r.get("postal_code"), cc)
        st = (r.get("region") or "").upper().split("-")[-1] if re.match(r"^[A-Za-z-]{2,5}$", r.get("region") or "") else region_of(cc, pc, r.get("address"))
        out.append((r["buyer_key"], r["buyer_name"], cc, pc, st))
    return out


def lane_f55():
    """US employers whose benefit plan pays a Canadian insurer or a provider in Canada, without a site on file (tools/f5500_benefits.py); the
    Form 5500 gives the sponsor's mailing ZIP code"""
    p = os.path.join(INC, "f5500", "f5500_buyers.csv.gz")
    if not os.path.exists(p):
        return []
    have = set()
    sp = os.path.join(INC, "f5500", "f5500_sites.csv")
    if os.path.exists(sp):
        have = {r["key"] for r in csv.DictReader(open(sp, encoding="utf-8", newline=""))}
    out = []
    with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r["key"] in have or not re.fullmatch(r"\d{5}", r.get("zip") or ""):
                continue
            out.append((r["key"], r["name"], "US", r["zip"], r.get("state") or ""))
    return out


LANES = {"hc": lane_hc, "xc": lane_xc, "dian": lane_dian, "cb": lane_cb, "f55": lane_f55}


def verify(a):
    """lane cb: a candidate site is kept when its own home page carries the buyer's name in its title / site name, or prints the buyer's postal
    code -> data/incoming/claude/overture/cb_sites.csv (append-only; done list cb_done.tsv)"""
    import hc_registers as HR
    cand = collections.defaultdict(list)
    cp = os.path.join(OUT, "%s_candidates.csv" % a.lane)
    if not os.path.exists(cp):
        print("verify: no candidates (%s)" % cp, flush=True)
        return
    for r in csv.DictReader(open(cp, encoding="utf-8", newline="")):
        cand[r["key"]].append(r)
    meta = {}
    for k, name, cc, pc, st in LANES[a.lane]():
        meta[k] = (name, cc, pc)
    sp, dp = os.path.join(OUT, "%s_sites.csv" % a.lane), os.path.join(OUT, "%s_done.tsv" % a.lane)
    done = {l.split("\t")[0] for l in open(dp, encoding="utf-8")} if os.path.exists(dp) else set()
    new = not os.path.exists(sp)
    t_end, cnt = time.time() + 60 * a.minutes, collections.Counter()
    with open(sp, "a", encoding="utf-8", newline="") as f, open(dp, "a", encoding="utf-8") as dn:
        w = csv.DictWriter(f, fieldnames=["key", "site", "tied_by", "quote", "read"])
        if new:
            w.writeheader()
        for k, cs in cand.items():
            if k in done or k not in meta or time.time() > t_end:
                continue
            name, cc, pc = meta[k]
            n = HR.core(name)
            hit = None
            for c in cs:
                d = c["site"]
                if HR.BAD.search(d):
                    continue
                try:
                    said = HR.home_says(d, n)
                    pcs = "" if said else HR.pc_on_home(d, pc, "canada" if cc == "CA" else "united states" if cc == "US" else cc)
                except Exception:
                    said, pcs = "", ""
                if said or pcs:
                    hit = (c, said, pcs)
                    break
            dn.write("%s\t%s\n" % (k, hit[0]["site"] if hit else "")); dn.flush()
            cnt["asked"] += 1
            if hit:
                c, said, pcs = hit
                how = ("carries the buyer's name: “%s”" % said) if said else ("prints the buyer's postal code: “%s”" % HR.no_mail(pcs))
                w.writerow({"key": k, "site": "https://%s/" % c["site"], "read": time.strftime("%Y-%m-%d"), "quote": (said or HR.no_mail(pcs))[:300],
                            "tied_by": "an Overture Maps place lists %s under the buyer's name %s (“%s”, place %s; Overture Maps Foundation open data, release %s), "
                                       "and the site's own home page %s" % (c["site"], "at its postal code %s" % c["place_postcode"] if pc else "in its province or state",
                                                                            c["place_name"], c["place_id"], c["release"], how)})
                f.flush(); cnt["tied"] += 1
    print("verify %s: %s" % (a.lane, dict(cnt)), flush=True)


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


STREET_W = re.compile(r"[a-z0-9]+")
STREET_SKIP = set("n s e w ne nw se sw north south east west st street ave avenue av blvd boulevard rd road dr drive ln lane way ct court pl place pkwy parkway "
                  "hwy highway cir circle ter terrace sq square plz plaza trl trail ste suite unit the of".split())
ORDINAL = {"first": "1st", "second": "2nd", "third": "3rd", "fourth": "4th", "fifth": "5th", "sixth": "6th", "seventh": "7th", "eighth": "8th",
           "ninth": "9th", "tenth": "10th", "eleventh": "11th", "twelfth": "12th"}
UNIT_SEG = re.compile(r"^(?:suite|ste|unit|floor|fl|level|lvl|shop|lot|apt|apartment|bldg|building|room|rm|dept|department|attn|c/o|p\.?\s*o\.?\s*box|box|#)\b")


def street_key(addr):
    """(street number, first distinctive word of the street name) of an address: the first comma-separated part that starts with a number and a
    word, a suite / floor / building part skipped. '767 Fifth Avenue, New York, NY 10153' -> ('767', '5th'); 'Suite 200, 100 Main St' ->
    ('100', 'main'); 'One Apple Park Way' -> None (a number written out is not read)"""
    for seg in (addr or "").lower().split(","):
        seg = re.sub(r"^\d{1,5}[a-z]?\s*/\s*(?=\d)", "", seg.strip())  # Australia: "6/3 Central Avenue" = unit 6, number 3
        if not seg or UNIT_SEG.match(seg):
            continue
        m = re.match(r"(\d{1,6})[a-z]?(?:-\d{1,5})?\s+(.+)", seg)
        if not m:
            continue
        words = [ORDINAL.get(w, w) for w in STREET_W.findall(m.group(2))]
        words = [w for w in words if w not in STREET_SKIP and not UNIT_SEG.match(w)]
        return (m.group(1), words[0]) if words else None
    return None


NOT_OWNER_SITE = re.compile(r"(^|\.)(gov|mil|state\.[a-z]{2}\.us|[a-z]{2}\.us|setmore|vagaro|booksy|mindbodyonline|schedulicity|calendly|acuityscheduling|squareup|square\.site|"
                            r"opentable|resy|toasttab|doordash|ubereats|grubhub|mapquest|manta|bbb|business\.site|sites\.google|linktr|carrd|regus|wework|davincivirtual|"
                            r"opus-virtual-offices|servcorp|iwgplc|spacesworks)(\.[a-z.]{2,8})?$", re.I)


EU_ADDR = ("DE", "FR", "IT", "ES", "CH", "AT", "BE", "DK", "SE")
EU_STREET_SKIP = set("""rue avenue av ave boulevard bd blvd chemin ch place pl impasse imp route rte quai allee cours square sq chaussee
via viale v piazza piazzale p za corso c so largo strada str vicolo loc localita frazione
calle c avenida avda avinguda av carrer c paseo po pg plaza pl carretera ctra rua travesia
strasse str gasse weg platz allee ring damm chaussee
gatan gata vagen vag torget
vej gade alle
straat laan plein
de la le les du des d l di del della dello dei degli delle el los las y et der die das am an im in zum zur auf van den het von""".split())
EU_SUFFIX = re.compile(r"(strasse|str|gasse|weg|platz|allee|ring|damm|gatan|vagen|gata|vej|gade|straat|laan|plein)$")


def street_key_eu(addr):
    """(house number, first distinctive word of the street) of a European address, whether the number comes before the street ('17, Rue De La
    Glacière', '17 rue …') or after it ('Zeppelinstraße 16', 'Leipziger Str.112', 'Avinguda Sant Jordi, 17', 'VIA BRANDIZZO 184/186'):
    'Zeppelinstraße 16' -> ('16', 'zeppelin'); '17, Rue De La Glacière' -> ('17', 'glaciere')"""
    import unicodedata
    t = unicodedata.normalize("NFKD", (addr or "").lower().replace("ß", "ss")).encode("ascii", "ignore").decode()
    segs = [x.strip(" .") for x in t.split(",") if x.strip(" .")]
    if not segs:
        return None
    street = segs[0]
    if len(segs) > 1 and (re.fullmatch(r"\d{1,5}[a-z]?", segs[0]) or re.fullmatch(r"\d{1,5}[a-z]?(\s*[-/]\s*\d{1,5})?", segs[1])):
        street = segs[0] + " " + segs[1]
    m = re.search(r"(?<![\d])(\d{1,5})(?![\d])", street)
    if not m:
        return None
    words = []
    for w in re.findall(r"[a-z]+", street.replace(".", " ")):
        w2 = EU_SUFFIX.sub("", w) if len(w) > 6 else w
        if w in EU_STREET_SKIP or w2 in EU_STREET_SKIP or len(w2) < 3:
            continue
        words.append(w2)
    return (m.group(1), words[0]) if words else None


def _host(web):
    h = re.sub(r"^https?://", "", (web or "").strip().lower()).split("/")[0].split(":")[0]
    return h[4:] if h.startswith("www.") else h


def addr(a):
    """owners abroad on the trademarks (tm) and patents (pt) registers with no site on file, no site found and no Overture candidate under
    their name: the Overture Maps places AT THE OWNER'S OWN ADDRESS that list a website. United States: the same ZIP code, the same street
    number and the same first word of the street name; United Kingdom: the same full postcode (a postcode covers about fifteen addresses).
    Where more than three websites are listed at that address (an office building), only those whose place name shares a distinctive word with
    the owner's name are kept. -> <lane>_overture_addr_sites.csv (rewritten each time). A candidate ties nothing: sites --abroad --overture
    reads it first and keeps it only when the site's own pages state the owner's name (tools/tm_register.py)."""
    import duckdb
    import ap_crawler as C
    import tm_register as TM
    import pt_register as PT
    files = {"tm": (TM.DIR, TM.OWN_XX, TM.MATCHES, TM.FOUND, TM.SDONE, TM.OVT_SITES, os.path.join(TM.DIR, "tm_overture_addr_sites.csv")),
             "pt": (PT.DIR, PT.OWN_XX, PT.MATCHES, PT.FOUND, PT.SDONE, os.path.join(PT.DIR, "pt_overture_sites.csv"), os.path.join(PT.DIR, "pt_overture_addr_sites.csv")),
             "f55": (None, None, None, None, None, None, os.path.join(OUT, "f55_addr_candidates.csv")),
             "hc": (None, None, None, None, None, None, os.path.join(OUT, "hc_addr_candidates.csv")),
             # 2026-11-13: owners IN CANADA of the two registers (the full postal code: a block face or one building)
             "tmca": (TM.DIR, TM.OWN_CA, TM.MATCHES, TM.FOUND, TM.SDONE, None, os.path.join(TM.DIR, "tm_overture_addr_ca_sites.csv")),
             "ptca": (PT.DIR, PT.OWN_CA, PT.MATCHES, PT.FOUND, PT.SDONE, None, os.path.join(PT.DIR, "pt_overture_addr_ca_sites.csv")),
             "rbq": (None, None, None, None, None, None, os.path.join(OUT, "rbq_addr_candidates.csv")),
             "reg": (None, None, None, None, None, None, os.path.join(OUT, "reg_addr_candidates.csv")),
             "radio": (None, None, None, None, None, None, os.path.join(OUT, "radio_addr_candidates.csv")),
             "lic": (None, None, None, None, None, None, os.path.join(OUT, "lic_addr_candidates.csv"))}
    want, words_of = {}, {}
    if "f55" in a.lanes.split(","):
        # 2026-11-13: US employers of the Form 5500 lane (tools/f5500_benefits.py) without a site: the sponsor's own street address and ZIP code
        import f5500_benefits as F5
        have_ = set(F5.sites_on_file())
        n_ = collections.Counter()
        for b in F5.buyers():
            if b["key"] in have_:
                continue
            sk = street_key(b.get("address") or "")
            z = (b.get("zip") or "")[:5]
            if not (sk and re.fullmatch(r"\d{5}", z)):
                n_["no street number or ZIP code read"] += 1
                continue
            want[("f55", b["key"])] = ("US", z, sk[0], sk[1])
            words_of[("f55", b["key"])] = {t for t in TM.nkey_x(b["name"]).split() if len(t) >= 4 and t not in TM.GENERIC}
            n_["US"] += 1
        print("f55: sponsors without a site, with an address to look at: %s" % dict(n_), flush=True)
    if "hc" in a.lanes.split(","):
        # 2026-11-13: Health Canada's companies (tools/hc_registers.py) without a site: in Canada the full postal code (a block face or one
        # building), in the United States the ZIP code with the street number and street
        hcf = os.path.join(INC, "hc", "hc_companies.csv.gz")
        hcs = os.path.join(INC, "hc", "hc_sites.csv")
        have_ = {r["key"] for r in csv.DictReader(open(hcs, encoding="utf-8", newline=""))} if os.path.exists(hcs) else set()
        n_ = collections.Counter()
        with gzip.open(hcf, "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if r["key"] in have_:
                    continue
                cc = iso2(r.get("country") or "")
                if cc == "CA":
                    pc = norm_pc(r.get("postal_code") or "", "CA")
                    if len(pc) == 6:
                        want[("hc", r["key"])] = ("CA", pc, "", "")
                        n_["CA"] += 1
                        words_of[("hc", r["key"])] = {t for t in TM.nkey_x(r["name"]).split() if len(t) >= 4 and t not in TM.GENERIC}
                elif cc == "US":
                    m = re.search(r"\b(\d{5})(?:-\d{4})?\b", r.get("postal_code") or r.get("address") or "")
                    sk = street_key(r.get("address") or "")
                    if m and sk:
                        want[("hc", r["key"])] = ("US", m.group(1), sk[0], sk[1])
                        n_["US"] += 1
                        words_of[("hc", r["key"])] = {t for t in TM.nkey_x(r["name"]).split() if len(t) >= 4 and t not in TM.GENERIC}
        print("hc: companies without a site, with an address to look at: %s" % dict(n_), flush=True)
    if "rbq" in a.lanes.split(","):
        # 2026-11-13: Québec construction licence holders (tools/rbq_licences.py) whose register entry gives no domain of their own, or whose
        # domain did not confirm: the full postal code
        import rbq_licences as RB
        rec = RB.checked()
        conf = {h["licence"] for o in rec.values() for h in (o.get("hits") or [])}
        n_ = collections.Counter()
        for h in RB.holders(RB.HOLDERS):
            if h["licence"] in conf:
                continue
            pc = TM.pc6(h.get("postal") or "")
            if pc:
                want[("rbq", h["licence"])] = ("CA", pc, "", "")
                words_of[("rbq", h["licence"])] = {t for t in TM.nkey((h.get("name") or "") + " " + (h.get("other_names") or "")).split() if len(t) >= 4 and t not in TM.GENERIC}
                n_["CA"] += 1
        print("rbq: holders without a confirmed site, with a postal code: %s" % dict(n_), flush=True)
    if "reg" in a.lanes.split(","):
        # 2026-11-13: registrants of the delegated authorities (tools/authority_registers.py: OMVIC, HCRA) with no tied site: the full postal code
        import authority_registers as AR
        tied_ = {k for k, o in AR.sites_on_file().items() if o.get("status") == "tied"}
        n_ = collections.Counter()
        for auth in AR.AUTH:
            for i, p_ in AR.profiles_on_file(auth).items():
                key = "%s:%s" % (auth, i)
                if key in tied_ or p_.get("status_http") != 200 or not re.search(r"corporation|partnership|limited|inc", p_.get("legal_type") or "", re.I):
                    continue
                pc = AR.postal_of(p_.get("address"))
                if pc:
                    want[("reg", key)] = ("CA", pc[0] + pc[1], "", "")
                    words_of[("reg", key)] = {t for t in TM.nkey((p_.get("business_name") or "") + " " + (p_.get("legal_name") or "")).split() if len(t) >= 4 and t not in TM.GENERIC}
                    n_[auth] += 1
        print("reg: registrants without a tied site, with a postal code: %s" % dict(n_), flush=True)
    if "radio" in a.lanes.split(","):
        # 2026-11-13: ISED's radio licensees (tools/radio_licences.py) without a site: the full postal code
        import radio_licences as RL
        have_ = set(RL.sites_on_file())
        n_ = collections.Counter()
        for o in RL.companies():
            if o["key"] in have_:
                continue
            pc = TM.pc6(o.get("postal_code") or "")
            if pc:
                want[("radio", o["key"])] = ("CA", pc, "", "")
                words_of[("radio", o["key"])] = {t for t in TM.nkey(o.get("name") or "").split() if len(t) >= 4 and t not in TM.GENERIC}
                n_["CA"] += 1
        print("radio: licensees without a site, with a postal code: %s" % dict(n_), flush=True)
    if "lic" in a.lanes.split(","):
        # 2026-11-13: municipal business licences and Québec permits (tools/biz_licences.py; out/licences_*.csv.gz of a pull, or --dir) that no
        # organisation on file matched: the licence's full postal code
        import hashlib
        ldir = a.lic_dir or "out"
        have_ = set()
        for p_ in glob.glob(os.path.join(INC, "lead_shards", "leads_lic_*.gz")):
            with gzip.open(p_, "rt", encoding="utf-8", newline="") as fh:
                have_ |= {r["buyer_key"] for r in csv.DictReader(fh)}
        n_ = collections.Counter()
        for f_ in sorted(glob.glob(os.path.join(ldir, "licences_*.csv.gz"))):
            with gzip.open(f_, "rt", encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh):
                    if len(r.get("postal") or "") != 6:
                        continue
                    if ("lead:" + hashlib.sha1(("lic|%s|%s" % (r["src"], r["number"])).encode()).hexdigest()[:16]) in have_:
                        continue
                    k = "%s:%s" % (r["src"], r["number"])
                    want[("lic", k)] = ("CA", r["postal"].upper(), "", "")
                    words_of[("lic", k)] = {t for t in TM.nkey((r.get("name") or "") + " " + (r.get("trade") or "")).split() if len(t) >= 4 and t not in TM.GENERIC}
                    n_[r["src"]] += 1
        print("lic: licensees not matched yet, with a postal code: %s" % dict(n_), flush=True)
    for lane in [x for x in a.lanes.split(",") if x in files and x not in ("f55", "hc", "rbq", "reg", "radio", "lic")]:
        d_, own, matches, found, sdone, ovt, _ = files[lane]
        skip = set()
        for p_ in (matches, found, ovt):
            if p_ and os.path.exists(p_):
                skip |= {r.get("owner_key") or "" for r in csv.DictReader(open(p_, encoding="utf-8", newline=""))}
        if os.path.exists(sdone):
            with gzip.open(sdone, "rt", encoding="utf-8") as f:
                for l in f:
                    q = l.rstrip("\n").split("\t")
                    if len(q) > 4 and q[4]:
                        skip.add(q[0])  # a site found by an earlier search
                    if len(q) > 5 and "overture" in q[5].split(","):
                        skip.add(q[0])  # read before with an Overture candidate
        n_ = collections.Counter()
        in_ca = lane in ("tmca", "ptca")
        with gzip.open(own, "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if in_ca:
                    if r["owner_key"] in skip or not TM.is_org(r["owner_name"]):
                        continue
                    pc = TM.pc6(r.get("postal_code") or "")
                    if pc:
                        want[(lane, r["owner_key"])] = ("CA", pc, "", "")
                        words_of[(lane, r["owner_key"])] = {t for t in TM.nkey(r["owner_name"]).split() if len(t) >= 4 and t not in TM.GENERIC}
                        n_["CA"] += 1
                    continue
                cc = r.get("country")
                if cc not in ("US", "GB", "AU", "NL") + EU_ADDR or r["owner_key"] in skip:
                    continue
                if not TM.is_org_abroad(r["owner_name"], cc):
                    continue
                if not (int(r["marks_in_force"] or 0) or (r["agent_name"] and int(r["marks_with_this_agent"] or 0))):
                    continue
                code, st = TM.place_abroad(r["address"], cc)
                if not code:
                    continue
                if cc in EU_ADDR:
                    sk = street_key_eu(r["address"])
                    if not sk:
                        n_["%s, no house number read" % cc] += 1
                        continue
                    want[(lane, r["owner_key"])] = (cc, code, sk[0], sk[1])
                elif cc in ("US", "AU"):
                    sk = street_key(r["address"])
                    if not sk:
                        n_["%s, no street number read" % cc] += 1
                        continue
                    want[(lane, r["owner_key"])] = (cc, code[:5] if cc == "US" else code[:4], sk[0], sk[1])
                else:
                    want[(lane, r["owner_key"])] = (cc, code, "", "")
                words_of[(lane, r["owner_key"])] = {t for t in TM.nkey_x(r["owner_name"]).split() if len(t) >= 4 and t not in TM.GENERIC}
                n_[cc] += 1
        print("%s: owners abroad without a site or a candidate under their name, with an address to look at: %s" % (lane, dict(n_)), flush=True)
    if not want:
        return
    con = duckdb.connect()
    con.execute("SET enable_progress_bar=false;")
    con.execute("CREATE TABLE own (lane VARCHAR, k VARCHAR, cc VARCHAR, z VARCHAR, num VARCHAR)")
    con.executemany("INSERT INTO own VALUES (?, ?, ?, ?, ?)", [(l_, k, *v[:3]) for (l_, k), v in want.items()])
    if a.dir and glob.glob(a.dir):
        src, release = "read_parquet('%s')" % a.dir, (a.release or "a local copy")
        sel = "name, website, street, postcode, country, id"
        where = "website IS NOT NULL AND country IN ('US', 'GB', 'CA', 'AU', 'NL', 'DE', 'FR', 'IT', 'ES', 'CH', 'AT', 'BE', 'DK', 'SE')"
    else:
        import urllib.request
        ls = lambda prefix: urllib.request.urlopen(urllib.request.Request("%s/?list-type=2&prefix=%s&delimiter=/" % (TM.OVT_BUCKET, prefix), headers={"User-Agent": UA}), timeout=120).read().decode()
        rel = sorted(re.findall(r"<Prefix>(release/[0-9]{4}-[0-9]{2}-[0-9]{2}\.[0-9]+/)</Prefix>", ls("release/")))[-1]
        keys = re.findall(r"<Key>([^<]+\.parquet)</Key>", ls(rel + "theme=places/type=place/"))
        if a.files:
            keys = keys[:a.files]
        con.execute("INSTALL httpfs; LOAD httpfs;")
        src = "read_parquet([%s])" % ", ".join("'%s/%s'" % (TM.OVT_BUCKET, k_) for k_ in keys)
        release = rel.rstrip("/").rsplit("/", 1)[-1]
        sel = 'names."primary" AS name, websites[1] AS website, addresses[1].freeform AS street, addresses[1].postcode AS postcode, addresses[1].country AS country, id'
        where = "websites IS NOT NULL AND len(websites) > 0 AND addresses[1].country IN ('US', 'GB', 'CA', 'AU', 'NL', 'DE', 'FR', 'IT', 'ES', 'CH', 'AT', 'BE', 'DK', 'SE')"
    t0 = time.time()
    con.execute("SET memory_limit='2500MB'; SET threads=2;")
    cur = con.execute(r"""WITH p AS (SELECT %s FROM %s WHERE %s),
                              q AS (SELECT name, website, street, country, id,
                                           CASE WHEN country = 'US' THEN left(postcode, 5) ELSE upper(regexp_replace(coalesce(postcode, ''), '[^A-Za-z0-9]', '', 'g')) END AS z,
                                           regexp_extract(lower(coalesce(street, '')), '(?:^|,)\s*(\d{1,6})[a-z]?(?:-\d{1,5})?\s+[a-z0-9]', 1) AS num,
                                           regexp_extract(coalesce(street, ''), '(\d{1,5})', 1) AS num_eu FROM p)
                         SELECT o.lane, o.k, q.name, q.website, q.street, q.z, q.id FROM q JOIN own o
                           ON o.cc = q.country AND o.z = q.z AND (CASE WHEN o.cc IN ('US', 'AU') THEN q.num = o.num WHEN o.cc IN ('DE', 'FR', 'IT', 'ES', 'CH', 'AT', 'BE', 'DK', 'SE') THEN q.num_eu = o.num ELSE TRUE END)""" % (sel, src, where))
    at, n_rows = collections.defaultdict(dict), 0

    def rows_of(c_):  # in batches: a million rows held at once do not fit a small machine
        while True:
            b_ = c_.fetchmany(100000)
            if not b_:
                return
            for x_ in b_:
                yield x_
    for lane, k, name, web, street, z, pid in rows_of(cur):
        n_rows += 1
        v = want[(lane, k)]
        if v[0] in EU_ADDR:
            sk = street_key_eu(street)
            if not sk or sk[0] != v[2] or sk[1] != v[3]:
                continue
        elif v[0] in ("US", "AU"):
            sk = street_key(street)
            if not sk or sk[0] != v[2] or sk[1] != v[3]:
                continue
        host = _host(web)
        if not host or "." not in host:
            continue
        at[(lane, k)].setdefault(C.registrable(host), (name or "", z, pid or "", street or ""))
    print("places that list a website at an owner's address (ZIP code and street number, or full postcode): %d (%.0f s, release %s)" % (
        n_rows, time.time() - t0, release), flush=True)
    # a website listed at the addresses of many owners is that of a shared office (a virtual office, a registered agent, a co-working floor); a
    # social network, a booking or site-builder platform, a directory or a government office is nobody's own site
    import credit_scan as CS
    import roster_ingest as RI
    many = collections.Counter((lk[0], d) for lk, ds in at.items() for d in ds)
    for lk in list(at):
        for d in list(at[lk]):
            if (many[(lk[0], d)] > 5 or CS.PLATFORM.search(d) or RI.NOT_OWN.search(d) or NOT_OWNER_SITE.search(d)):
                del at[lk][d]
    out, n = collections.defaultdict(list), collections.Counter()
    for lk, ds in at.items():
        if not ds:
            continue
        shares = {d: bool(words_of[lk] & {t for t in TM.nkey_x(x[0]).split() if len(t) >= 4}) for d, x in ds.items()}
        keep = list(ds) if len(ds) <= 3 else [d for d in ds if shares[d]]
        keep.sort(key=lambda d: (not shares[d], d))
        for d in keep[:3]:
            out[lk[0]].append((lk[1], d, ds[d]))
            n[(lk[0], "sites")] += 1
        n[(lk[0], "owners")] += bool(keep)
        n[(lk[0], "office buildings left out")] += (not keep)
    for lane in [x for x in a.lanes.split(",") if x in files]:
        path = files[lane][6]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["key" if lane in ("f55", "hc", "rbq", "reg", "radio", "lic") else "owner_key", "site", "how", "place_name", "place_postcode", "place_id", "release"])
            for k, d, (name, z, pid, street) in sorted(out[lane]):
                cc = want[(lane, k)][0]
                w.writerow([k, d, "the owner's own street address (%s, %s %s)" % (street[:60], "ZIP code" if cc == "US" else "postcode", z) if cc in ("US", "AU") + EU_ADDR else
                            "the owner's own %s (%s)" % ("postal code" if cc == "CA" else "postcode", z), name, z, pid, release])
        print("%s: %d owners with a place at their own address that lists a website (%d candidate sites; %d addresses with more than three websites and none under a word of the owner's name left out) -> %s" % (
            lane, n[(lane, "owners")], n[(lane, "sites")], n[(lane, "office buildings left out")], os.path.relpath(path, ROOT)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["query", "verify", "addr"])
    ap.add_argument("--lanes", default="hc,xc")
    ap.add_argument("--lane", default="cb", help="verify: the lane whose candidates to check (cb)")
    ap.add_argument("--minutes", type=float, default=30)
    ap.add_argument("--dir", default="", help="a glob of local parquet files with the columns name, website, postcode, region, country, id (tests)")
    ap.add_argument("--release", default="")
    ap.add_argument("--files", type=int, default=0, help="addr: read only the first N parquet files of the release (tests)")
    ap.add_argument("--lic-dir", default="", help="addr --lanes lic: the folder of the licence lists (out/ of tools/biz_licences.py pull)")
    a = ap.parse_args()
    {"verify": verify, "addr": addr}.get(a.cmd, query)(a)


if __name__ == "__main__":
    main()
