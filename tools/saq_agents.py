#!/usr/bin/env python3
"""Producers abroad (and in Canada) represented in Québec by a Canadian promotional agent: the Société des alcools du Québec's own product pages
(no AI).

Every wine, beer or spirit the SAQ (a Québec Crown corporation) sells has a public product page that names its producer ("Producteur") and the
promotional agent that represents it in Québec ("Agent promotionnel": a Québec agency — Breakthru Canada, Univins, Sélections François Fréchette,
Charton Hobbs …), with the country and region of the product. The agent is the producer's representative in Québec and is paid by it: a
relationship between a Canadian vendor and an organisation anywhere, published by a public body, current for as long as the product is listed.
Measured on 300 product pages (2026-11-13): 269 name a producer, 249 an agent; 254 different producers in 269 products; France 129, Italy 33,
United States 19, Canada 18, Spain 14 …; 78 different agents.

  pull  --shard K/N --minutes M   the product pages of the SAQ's own product sitemap (robots.txt obeyed, the project's reader: one request a second
                                  a runner) not read before -> out/saq_K.jsonl (code, name, country, region, producer, agent, format, colour, url, read)
  merge DIR                       -> data/incoming/claude/saq/saq_products.csv.gz (one line per product, the newest read wins) + saq_done.tsv
  producers                       -> data/incoming/claude/saq/saq_producers.csv (producer, country, the agents that represent it, products, a sample)
  sites                           the producers' own sites (a Foursquare place of the very name in the producer's country, kept when the site's own
                                  home page names the producer) -> saq_sites.csv
  agents                          each agent's own site and the address its own pages print -> saq_agents.csv
  leads                           -> data/incoming/claude/lead_shards/leads_saq_<stamp>.gz + details_saq_<stamp>.gz (the producer the buyer, its agent
                                  promotionnel the vendor; tools/relationship_rows.py kind "promotional agency")
"""
import argparse, collections, csv, glob, gzip, html, json, os, re, sys, time

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "saq")
PRODUCTS = os.path.join(DIR, "saq_products.csv.gz")
DONE = os.path.join(DIR, "saq_done.tsv")
PRODUCERS = os.path.join(DIR, "saq_producers.csv")
SITEMAP = "https://www.saq.com/media/sitemaps/fr/sitemap_product.xml"
TODAY = time.strftime("%Y-%m-%d")
FIELDS = ["Pays", "Région", "Appellation d'origine", "Désignation réglementée", "Classification", "Cépage", "Cépages", "Producteur", "Agent promotionnel",
          "Code SAQ", "Code CUP", "Format", "Couleur", "Degré d'alcool", "Taux de sucre", "Produit du Québec", "Producteur-transformateur", "Particularité"]
COLS = ["code", "name", "country", "region", "producer", "agent", "format", "colour", "url", "read"]


def product_urls():
    st, ct, data, final = C.fetch(SITEMAP)
    if st != 200 or not data:
        sys.exit("SAQ product sitemap not read (%s)" % st)
    urls = []
    for sm in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", data.decode("utf-8", "replace")):
        if not C.allowed(sm):
            continue
        st2, ct2, d2, f2 = C.fetch(sm, 30_000_000)
        if st2 == 200 and d2:
            urls += re.findall(r"<loc>\s*(https://www\.saq\.com/fr/\d+)\s*</loc>", d2.decode("utf-8", "replace"))
    return list(dict.fromkeys(urls))


def parse(raw, url):
    t = re.sub(r"\s+", " ", C.visible(raw))
    rec = {"url": url, "code": url.rstrip("/").rsplit("/", 1)[-1], "read": TODAY}
    m = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S)
    rec["name"] = re.sub(r"<[^>]+>|\s+", " ", m.group(1)).strip()[:160] if m else ""
    got = {}
    for f in FIELDS:
        j = t.find(" " + f + " ")
        if j < 0:
            continue
        rest = t[j + len(f) + 2:]
        nxt = min([rest.find(" " + g + " ") for g in FIELDS if rest.find(" " + g + " ") >= 0] + [140])
        got[f] = rest[:nxt].strip()[:140]
    rec.update(country=got.get("Pays", ""), region=got.get("Région", ""), producer=got.get("Producteur", ""), agent=got.get("Agent promotionnel", ""),
               format=got.get("Format", ""), colour=got.get("Couleur", ""))
    return rec


def cmd_pull(a):
    k, n = (int(x) for x in a.shard.split("/"))
    done = set()
    if os.path.exists(DONE):
        done = {l.split("\t", 1)[0] for l in open(DONE, encoding="utf-8") if l.strip()}
    urls = [u for u in product_urls() if u.rstrip("/").rsplit("/", 1)[-1] not in done]
    mine = [u for i, u in enumerate(sorted(urls)) if i % n == k]
    print("SAQ: %d product pages in the sitemap not read before; %d for shard %s" % (len(urls), len(mine), a.shard), flush=True)
    os.makedirs("out", exist_ok=True)
    deadline = time.time() + a.minutes * 60
    cnt = collections.Counter()
    with open("out/saq_%d.jsonl" % k, "a", encoding="utf-8") as f:
        for u in mine:
            if time.time() > deadline:
                break
            if not C.allowed(u):
                cnt["robots"] += 1
                continue
            st, ct, data, final = C.fetch(u)
            if st != 200 or not data:
                f.write(json.dumps({"url": u, "code": u.rstrip("/").rsplit("/", 1)[-1], "status": "http_%s" % st, "read": TODAY}) + "\n")
                cnt["http_%s" % st] += 1
                continue
            rec = parse(html.unescape(data.decode("utf-8", "replace")), u)
            rec["status"] = "ok"
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            cnt["with a producer" if rec.get("producer") else "no producer named"] += 1
            cnt["with an agent"] += bool(rec.get("agent"))
            time.sleep(max(0.0, a.pause))
    print("SAQ shard %s: %s" % (a.shard, dict(cnt)), flush=True)


def cmd_merge(a):
    recs = {}
    for p in sorted(glob.glob(os.path.join(a.dir, "**", "saq_*.jsonl"), recursive=True)):
        for l in open(p, encoding="utf-8"):
            try:
                o = json.loads(l)
            except ValueError:
                continue
            if o.get("code"):
                recs[o["code"]] = o
    os.makedirs(DIR, exist_ok=True)
    old = {}
    if os.path.exists(PRODUCTS):
        with gzip.open(PRODUCTS, "rt", encoding="utf-8", newline="") as f:
            old = {r["code"]: r for r in csv.DictReader(f)}
    n_new = 0
    for c, o in recs.items():
        if o.get("status") == "ok":
            old[c] = {k: o.get(k, "") for k in COLS}
            n_new += 1
    with gzip.open(PRODUCTS, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for c in sorted(old):
            w.writerow(old[c])
    with open(DONE, "a", encoding="utf-8") as f:
        for c, o in sorted(recs.items()):
            f.write("%s\t%s\t%s\n" % (c, o.get("status", ""), o.get("read", TODAY)))
    print("SAQ merge: %d product pages read this run, %d products on file -> %s" % (len(recs), len(old), os.path.relpath(PRODUCTS, ROOT)), flush=True)
    cmd_producers(a)


def cmd_producers(a):
    if not os.path.exists(PRODUCTS):
        print("no products on file"); return
    by = collections.defaultdict(lambda: {"agents": collections.Counter(), "n": 0, "sample": None, "regions": collections.Counter()})
    with gzip.open(PRODUCTS, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            p, cc = (r.get("producer") or "").strip(), (r.get("country") or "").strip()
            if not p or not r.get("agent"):
                continue
            g = by[(p, cc)]
            g["agents"][r["agent"].strip()] += 1
            g["n"] += 1
            g["regions"][r.get("region") or ""] += 1
            if g["sample"] is None or r["read"] > g["sample"]["read"]:
                g["sample"] = r
    with open(PRODUCERS, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["producer", "country", "region", "agent", "agents", "products", "sample_code", "sample_name", "sample_url", "read"])
        for (p, cc), g in sorted(by.items()):
            ag = g["agents"].most_common()
            s = g["sample"]
            w.writerow([p, cc, g["regions"].most_common(1)[0][0], ag[0][0], " | ".join("%s (%d)" % x for x in ag), g["n"], s["code"], s["name"], s["url"], s["read"]])
    print("SAQ producers with an agent: %d (%d abroad) -> %s" % (len(by), sum(1 for (p, cc) in by if cc and cc != "Canada"), os.path.relpath(PRODUCERS, ROOT)), flush=True)


COUNTRY = {"France": "FR", "Italie": "IT", "États-Unis": "US", "Espagne": "ES", "Portugal": "PT", "Chili": "CL", "Argentine": "AR", "Australie": "AU",
           "Nouvelle-Zélande": "NZ", "Allemagne": "DE", "Autriche": "AT", "Afrique du Sud": "ZA", "Royaume Uni": "GB", "Royaume-Uni": "GB", "Irlande": "IE",
           "Canada": "CA", "Grèce": "GR", "Hongrie": "HU", "Liban": "LB", "Israël": "IL", "Mexique": "MX", "Japon": "JP", "Belgique": "BE", "Pays-Bas": "NL",
           "Suisse": "CH", "Luxembourg": "LU", "Uruguay": "UY", "Brésil": "BR", "Slovénie": "SI", "Croatie": "HR", "Géorgie": "GE", "Moldavie": "MD",
           "Roumanie": "RO", "Bulgarie": "BG", "Arménie": "AM", "Chine": "CN", "Inde": "IN", "Corée du Sud": "KR", "Pologne": "PL", "Suède": "SE",
           "Danemark": "DK", "Norvège": "NO", "Finlande": "FI", "Islande": "IS", "Jamaïque": "JM", "Barbade": "BB", "Cuba": "CU", "Porto Rico": "PR",
           "Guyana": "GY", "Trinité-et-Tobago": "TT", "Pérou": "PE", "Venezuela": "VE", "Colombie": "CO", "Guatemala": "GT", "Nicaragua": "NI",
           "Philippines": "PH", "Thaïlande": "TH", "Taïwan": "TW", "Ukraine": "UA", "Lettonie": "LV", "Lituanie": "LT", "Estonie": "EE",
           "République tchèque": "CZ", "Tchéquie": "CZ", "Slovaquie": "SK", "Serbie": "RS", "Macédoine du Nord": "MK", "Monténégro": "ME", "Turquie": "TR",
           "Chypre": "CY", "Malte": "MT", "Maroc": "MA", "Tunisie": "TN", "Haïti": "HT", "République dominicaine": "DO", "Panama": "PA", "Bolivie": "BO",
           "Écosse": "GB", "Angleterre": "GB", "Pays de Galles": "GB", "Équateur": "EC", "Kenya": "KE", "Vietnam": "VN", "Singapour": "SG", "Indonésie": "ID"}
SITES = os.path.join(DIR, "saq_sites.csv")
AGENTS = os.path.join(DIR, "saq_agents.csv")
SITE_COLS = ["producer", "country", "site", "tied_by", "place_id", "place_name", "read"]


def _producers():
    with open(PRODUCERS, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def cmd_sites(a):
    """the producers' own websites: a Foursquare place of the producer's very name in its country that lists a website (tools/fsq_places.py), kept
    when the site's own home page names the producer (its title or site name carries every distinctive word of the producer's name)"""
    import concurrent.futures as cf
    import fsq_places as FQ
    import tm_register as TM
    import lead_crawl as LC
    import tech_relationships as T
    prods = [p for p in _producers() if COUNTRY.get(p["country"])]
    have = {}
    if os.path.exists(SITES):
        have = {(r["producer"], r["country"]): r for r in csv.DictReader(open(SITES, encoding="utf-8", newline=""))}
    want = {}
    for p in prods:
        nk = TM.nkey_x(p["producer"])
        if (p["producer"], p["country"]) not in have and nk and len(nk) >= 4:
            want[(p["producer"], p["country"])] = (COUNTRY[p["country"]], nk)
    print("SAQ producers without a site on file: %d (of %d)" % (len(want), len(prods)), flush=True)
    rel, files = FQ.release_files("")
    con = FQ._con()
    con.execute("CREATE TABLE own (k VARCHAR, cc VARCHAR, nk VARCHAR)")
    keys = {"%d" % i: k for i, k in enumerate(want)}
    con.executemany("INSERT INTO own VALUES (?, ?, ?)", [(i, want[k][0], want[k][1]) for i, k in keys.items()])
    norm_sql = ("trim(regexp_replace(regexp_replace(regexp_replace(regexp_replace(replace(lower(strip_accents(coalesce(p.name, ''))), '&', ' and '), '[^a-z0-9 ]+', ' ', 'g'), "
                "'%s', ' ', 'g'), '%s', ' ', 'g'), '\\s+', ' ', 'g'))" % (TM._SQL_FORMS, TM.EU_FORMS))
    ccs = ", ".join("'%s'" % c for c in sorted({v[0] for v in want.values()}))
    t0 = time.time()
    rows = con.execute("""WITH p AS (SELECT name, website, country, fsq_place_id FROM read_parquet([%s])
                                     WHERE website IS NOT NULL AND website <> '' AND date_closed IS NULL AND country IN (%s))
                          SELECT o.k, p.name, p.website, p.fsq_place_id FROM p JOIN own o ON o.cc = p.country AND o.nk = %s"""
                       % (", ".join("'%s'" % f for f in files), ccs, norm_sql)).fetchall()
    print("Foursquare places with a producer's very name in its country: %d (%.0f s)" % (len(rows), time.time() - t0), flush=True)
    cands = collections.defaultdict(dict)
    for i, name, web, pid in rows:
        h = re.sub(r"^https?://", "", (web or "").strip().lower()).split("/")[0].split(":")[0]
        h = h[4:] if h.startswith("www.") else h
        if h and "." not in h:
            continue
        dm = C.registrable(h) if h else ""
        if dm and not re.search(r"facebook|instagram|wix|wordpress|blogspot|google|yelp|tripadvisor", dm):
            cands[keys[i]].setdefault(dm, (name, pid))
    # a site that several producers' places list is nobody's own (a distributor, a tourism office)
    seen = collections.Counter(d for v in cands.values() for d in v)

    def check(item):
        k, ds = item
        prod, cc = k
        words = [w for w in TM.nkey_x(prod).split() if len(w) >= 3 and w not in TM.GENERIC]
        for dm, (name, pid) in list(ds.items())[:3]:
            if seen[dm] > 2 or not words:
                continue
            u = "https://%s/" % dm
            try:
                if not C.allowed(u):
                    continue
                st, ct, data, final = C.fetch(u)
            except Exception:  # noqa: BLE001
                continue
            if st != 200 or not data:
                continue
            raw = data.decode("utf-8", "replace")
            title, meta = T.page_meta(raw)
            head = TM.nkey_x(" ".join([title or "", meta.get("og:site_name") or "", meta.get("og:title") or ""]))
            lab = re.sub(r"[^a-z0-9]", "", dm.split(".")[0])
            if all(w in head.split() for w in words) or (len(lab) >= 6 and lab == "".join(words)):
                how = ("the site's own home page names the producer (“%s”)" % re.sub(r"\s+", " ", title or meta.get("og:site_name") or "")[:120]) if all(w in head.split() for w in words) \
                    else "the site's domain is the producer's name"
                return {"producer": prod, "country": cc, "site": "https://%s/" % (C.registrable(urllib_host(final) or dm) or dm), "place_id": pid, "place_name": name,
                        "tied_by": "a Foursquare place (Foursquare Open Source Places, release %s) lists this website under the producer's very name in %s, and %s" % (rel, cc, how),
                        "read": TODAY}
        return None
    found = []
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for r in ex.map(check, list(cands.items())):
            if r:
                found.append(r)
    allr = list(have.values()) + found
    with open(SITES, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=SITE_COLS)
        w.writeheader()
        for r in sorted(allr, key=lambda r: (r["producer"], r["country"])):
            w.writerow({c: r.get(c, "") for c in SITE_COLS})
    print("SAQ producers: %d candidates read, %d sites tied this run, %d on file -> %s" % (len(cands), len(found), len(allr), os.path.relpath(SITES, ROOT)), flush=True)


def urllib_host(u):
    import urllib.parse as _up
    h = (_up.urlparse(u or "").hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def cmd_agents(a):
    """each agent's own site and its own printed address: a Foursquare place in Québec of the agent's very name lists its website; the address is the
    one the agent's own home or contact page prints (tools/addr_reread.py, the same reading as for the organisations)"""
    import fsq_places as FQ
    import tm_register as TM
    import addr_reread as AR
    agents = collections.Counter()
    with gzip.open(PRODUCTS, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("agent"):
                agents[r["agent"].strip()] += 1
    have = {}
    if os.path.exists(AGENTS):
        have = {r["agent"]: r for r in csv.DictReader(open(AGENTS, encoding="utf-8", newline=""))}
    want = {ag: TM.nkey_x(ag) for ag in agents if ag not in have and TM.nkey_x(ag)}
    rel, files = FQ.release_files("")
    con = FQ._con()
    con.execute("CREATE TABLE ag (k VARCHAR, nk VARCHAR)")
    con.executemany("INSERT INTO ag VALUES (?, ?)", list(want.items()))
    norm_sql = ("trim(regexp_replace(regexp_replace(regexp_replace(regexp_replace(replace(lower(strip_accents(coalesce(p.name, ''))), '&', ' and '), '[^a-z0-9 ]+', ' ', 'g'), "
                "'%s', ' ', 'g'), '%s', ' ', 'g'), '\\s+', ' ', 'g'))" % (TM._SQL_FORMS, TM.EU_FORMS))
    rows = con.execute("""WITH p AS (SELECT name, website, address, locality, postcode, fsq_place_id FROM read_parquet([%s]) WHERE country = 'CA' AND date_closed IS NULL)
                          SELECT a.k, p.name, p.website, p.address, p.locality, p.postcode, p.fsq_place_id FROM p JOIN ag a ON a.nk = %s"""
                       % (", ".join("'%s'" % f for f in files), norm_sql)).fetchall()
    best = {}
    for k, name, web, addr, loc, pc, pid in rows:
        if web and k not in best:
            best[k] = (web, addr, loc, pc, pid, name)
    # the agents no Foursquare place names: the company-name autocomplete's domain, kept when the site's own home page names the agent
    import hc_registers as HR
    for ag in want:
        if ag in best:
            continue
        q = re.sub(r"(?i)\b(inc|ltée|ltee|limitée|limited|ltd|corp|corporation|s\.?e\.?n\.?c\.?)\b\.?", "", ag).strip(" ,.")
        for c in (HR.suggest(q) or [])[:4]:
            dm = (c.get("domain") or "").lower()
            if dm and HR.home_says(dm, HR.norm(q)):
                best[ag] = ("https://%s/" % dm, "", "", "", "", "the company-name autocomplete (Clearbit), the site's own home page naming the agent")
                break
    out = dict(have)
    for ag, (web, addr, loc, pc, pid, name) in best.items():
        h = urllib_host(web if web.startswith("http") else "https://" + web)
        site = "https://%s/" % h if h else ""
        own = ""
        if site:
            for fn in (AR.read_one, AR.read_one_legal):  # its home and contact pages, then its own legal pages (beside its own name)
                try:
                    got = fn({"key": "agent", "site": site})
                except Exception:  # noqa: BLE001
                    got = {}
                if got.get("status") == "found" and BL_fsa(got.get("address") or ""):
                    own = "%s (as printed on %s, read %s)" % (got["address"], got["address_url"], TODAY)
                    break
        out[ag] = {"agent": ag, "site": site, "address": own, "place_id": pid, "place_name": name, "products": agents[ag], "read": TODAY}
    with open(AGENTS, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["agent", "site", "address", "place_id", "place_name", "products", "read"])
        w.writeheader()
        for ag in sorted(out):
            w.writerow(out[ag])
    print("SAQ agents: %d named on the products, %d with a site, %d with their own printed address -> %s" % (
        len(agents), sum(1 for r in out.values() if r.get("site")), sum(1 for r in out.values() if r.get("address")), os.path.relpath(AGENTS, ROOT)), flush=True)


def BL_fsa(t):
    import by_location as BL
    return BL.fsa_of(t)


def cmd_leads(a):
    """one lead per producer with a site of its own: the producer is the buyer, its agent promotionnel the Canadian vendor"""
    import hashlib
    shards = os.path.join(INC, "lead_shards")
    os.makedirs(shards, exist_ok=True)
    sites = {(r["producer"], r["country"]): r for r in csv.DictReader(open(SITES, encoding="utf-8", newline=""))} if os.path.exists(SITES) else {}
    agents = {r["agent"]: r for r in csv.DictReader(open(AGENTS, encoding="utf-8", newline=""))} if os.path.exists(AGENTS) else {}
    have = set()
    for p in glob.glob(os.path.join(shards, "leads_saq_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            have |= {r["buyer_key"] for r in csv.DictReader(fh)}
    hosts = collections.Counter(s["site"] for s in sites.values())
    rows, dets, by = [], [], collections.Counter()
    for p in _producers():
        s = sites.get((p["producer"], p["country"]))
        if not s or hosts[s["site"]] > 1:
            by["no site of its own" if not s else "site shared by two producers: left out"] += 1
            continue
        ag = agents.get(p["agent"]) or {}
        if not ag.get("address"):
            by["agent's own printed address not read"] += 1
            continue
        key = "saq:" + hashlib.sha1(("%s|%s" % (p["producer"], p["country"])).encode()).hexdigest()[:16]
        if key in have:
            continue
        cfv = ("membership / statutory fee relationship: client of a Canadian promotional agent of record (%s=%s); the Société des alcools du Québec's product page names "
               "the producer and its agent promotionnel (%s, read %s)" % (p["agent"], ag["address"], p["sample_url"], p["read"]))
        rows.append({"buyer_key": key, "buyer_name": p["producer"], "website": s["site"], "canadian_vendor_rows": p["products"], "example_vendor": p["agent"],
                     "canada_field_value": cfv, "evidence_dataset": p["sample_url"], "latest_record_date": p["read"]})
        dets.append({"key": key, "platform": "saq_agent", "record_url": p["sample_url"], "vendor": p["agent"], "record_date": p["read"], "start": "", "end": "",
                     "reference": "SAQ %s" % p["sample_code"], "title": p["sample_name"], "saq_products": p["products"], "saq_agents": p["agents"],
                     "vendor_address": ag["address"], "vendor_site": ag.get("site") or "", "buyer_country": p["country"], "buyer_region": p.get("region") or "",
                     "buyer_register": {"legal_name": p["producer"], "trade_names": [], "registry_id": "", "label": "the SAQ's product page (producer)"},
                     "site_named_by": s["tied_by"], "site_tied_to_holder_by": s["tied_by"], "bill_items": "the agent's commission and fees for representing the producer's products in Québec"})
        have.add(key); by["new lead (%s)" % ("Canada" if p["country"] == "Canada" else "abroad")] += 1
    if rows:
        stamp = time.strftime("%Y%m%dT%H%M%S", time.gmtime())
        with gzip.open(os.path.join(shards, "leads_saq_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        with gzip.open(os.path.join(shards, "details_saq_%s.gz" % stamp), "wt", encoding="utf-8") as f:
            for d in dets:
                f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print("SAQ producer leads on file: %d (+%d this run: %s)" % (len(have), len(rows), dict(by)), flush=True)


def cmd_left(a):
    """the number of product pages of the sitemap not read yet (the workflow starts again while some are left)"""
    done = set()
    if os.path.exists(DONE):
        done = {l.split("\t", 1)[0] for l in open(DONE, encoding="utf-8") if l.strip()}
    print(sum(1 for u in product_urls() if u.rstrip("/").rsplit("/", 1)[-1] not in done))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["pull", "merge", "producers", "left", "sites", "agents", "leads"])
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=330)
    ap.add_argument("--pause", type=float, default=0.0, help="seconds to wait between pages, beyond the reader's own pace")
    a = ap.parse_args()
    {"pull": cmd_pull, "merge": cmd_merge, "producers": cmd_producers, "left": cmd_left, "sites": cmd_sites, "agents": cmd_agents, "leads": cmd_leads}[a.cmd](a)


if __name__ == "__main__":
    main()
