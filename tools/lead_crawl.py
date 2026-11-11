#!/usr/bin/env python3
"""Row factory, step 2 (cloud): the role mailbox of every NEW buyer, read on the buyer's own site.

tools/cc_clients.py and tools/cc_tenants.py find new buyers of Canada-located vendors. A buyer becomes a delivered row only with a mailbox the
organisation publishes itself. This runs tools/ap_crawler.crawl() — the same no-AI reader that ran on the owner's Mac — from GitHub runners:
robots.txt respected, at most one request per second per site, a small page budget, invoicing / AP / supplier / purchasing / finance mailboxes
first and, when the site publishes none, its general role mailbox (owner rule 2026-10-28). Never a named person, never a pattern-built address,
blocked sites are recorded as blocked and left alone.

  python3 tools/lead_crawl.py --shard K/N [--minutes 150] [--max-pages 25] [--workers 40]            leads of claude_buyer_leads_cc.csv
  python3 tools/lead_crawl.py --candidates data/incoming/claude/claude_tenant_candidates.csv.gz --shard K/N   candidates (tools/cc_tenants.py)
  python3 tools/lead_crawl.py --merge SHARD_DIR [--tenants]                                          append shard outputs to the files on main
Leads mode      in : claude_buyer_leads_cc.csv, resume claude_lead_crawl_done.tsv            out: out/lead_rows_<K>.csv, out/lead_done_<K>.tsv
Candidates mode in : claude_tenant_candidates.csv.gz, resume claude_tenant_crawl_done.tsv    out: out/lead_rows_<K>.csv, out/tenant_leads_<K>.jsonl,
                     out/tenant_done_<K>.tsv
  A candidate (an organisation with a live account at a Canada-HQ software vendor) is ACCEPTED only when its own site gives
  (1) a role mailbox on its own domain, (2) a postal address in a country the vendor's Canadian company contracts with (Canada; Canada or the
  United States for Shopify — tools/cc_tenants.SCOPE), the address quote and page kept, (3) a name, and (4) for Shopify: the store's pages still
  load Shopify today. Everything else is recorded with its reason and never becomes a lead.
Rows go to data/incoming/claude/claude_buyer_ap_results_cccrawl01.csv, where the referee re-fetches every evidence page before a mailbox counts.
"""
import argparse, collections, csv, glob, gzip, hashlib, json, os, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor, wait

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
DONE = os.path.join(INC, "claude_lead_crawl_done.tsv")
TDONE = os.path.join(INC, "claude_tenant_crawl_done.tsv")
OUT = os.path.join(INC, "claude_buyer_ap_results_cccrawl01.csv")
TODAY = time.strftime("%Y-%m-%d")
MYSHOPIFY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data/incoming/claude/credit_scan/graph_myshopify_hosts.txt.gz")  # <store> of every <store>.myshopify.com host name in the web graph
US_ADDR = re.compile(r"(?<![A-Za-z0-9])([A-Z][A-Za-z.'\- ]{2,30}),?\s+(AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY|DC)"
                     r"\.?,?\s+(\d{5})(?:-\d{4})?(?![A-Za-z0-9])")
GB_ADDR = re.compile(r"(?<![A-Za-z0-9])([A-Z][A-Za-z.'\- ]{2,30}),?\s+([A-Z]{1,2}\d[A-Z\d]?\s?\d[A-Z]{2})(?![A-Za-z0-9])")
AU_ADDR = re.compile(r"(?<![A-Za-z0-9])([A-Z][A-Za-z.'\- ]{2,30}),?\s+(NSW|VIC|QLD|TAS|ACT)\s+(\d{4})(?!\d)")
SFDONE = os.path.join(INC, "claude_site_facts_done.tsv")
_tl = threading.local()


def ok_mailbox(e):
    """the validator's own rule (tools/validate_returns.py): a first.last-shaped local part without a role word is treated as a person"""
    return bool(C.EMAIL.match(e or "")) and not (C.PERSONAL.match(e.split("@")[0]) and not C.ROLE_HINT.search(e.split("@")[0]))


GENERIC_SITE_WORDS = {"home", "accueil", "welcome", "bienvenue", "services", "service", "canada", "canadian", "online", "group", "groupe", "company", "solutions", "official", "site", "website",
                      "shop", "store", "boutique", "contact", "about", "page", "best", "quality", "professional", "toronto", "montreal", "vancouver", "calgary", "ottawa", "edmonton", "quebec"}


LSTATE = os.path.join(INC, "crawl_state")  # 2026-11-10: the lead crawl's done lines as append-only shards (lead_done_<stamp>.gz); the old single file is no longer rewritten


def lead_done_lines():
    """done lines of the lead crawl: the old single file, then the shards (a later line of the same key wins)"""
    if os.path.exists(DONE):
        for l in open(DONE, encoding="utf-8"):
            yield l.rstrip("\n")
    for p in sorted(glob.glob(os.path.join(LSTATE, "lead_done_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8") as fh:
            for l in fh:
                yield l.rstrip("\n")


def name_fit(c, label):
    """how well a candidate name agrees with a site's own domain label (0 = not at all). The whole name being the label scores highest;
    a slogan that merely contains one word of the label ("Hearing Aids in Surrey, White Rock & Vancouver" on puretonehearing.ca) scores low."""
    import unicodedata
    flat = unicodedata.normalize("NFKD", c or "").encode("ascii", "ignore").decode().lower()
    n = re.sub(r"[^a-z0-9]", "", flat)
    if not n or not label:
        return 0.0
    if n == label:
        return 100.0
    if len(label) >= 4 and label in n:
        return max(30.0, 80.0 - (len(n) - len(label)) / 2.0)
    if len(n) >= 4 and n in label:
        return 60.0 + 20.0 * len(n) / len(label)
    words = re.findall(r"[a-z0-9]+", flat)
    if len(label) == 3 and label in words and len(words) <= 4:
        return 40.0  # a three-letter domain that is one whole word of a short name: "CSV Architects" on csv.ca, "TSS Football Club" on tss.ca
    toks = [t for t in words if len(t) >= 4 and t not in GENERIC_SITE_WORDS]
    hit = [t for t in toks if t in label]
    if not hit:
        ini = "".join(w[0] for w in words if w not in ("of", "the", "and", "de", "du", "des", "la", "le", "les", "et", "for"))
        return 45.0 if len(ini) >= 3 and (ini == label or label.startswith(ini) and len(ini) >= 4) else 0.0  # "Feline Rescue Foundation of Alberta" on frfa.ca
    cover = min(1.0, sum(len(t) for t in hit) / float(len(label)))
    extra = sum(1 for w in words if len(w) >= 3 and w not in label)
    if extra and cover < 0.8:
        return 0.0  # other words around a part of the label: a description ("Marquage de stationnement" on marquage247.ca), not the name
    return max(0.0, 50.0 * cover - 3.0 * extra)


def site_name_for(host, og, title, T):
    """the name an organisation gives itself on its own home page, kept only when it agrees with its own domain (a slogan such as
    "Best Plumber in Toronto | 24/7 Service" is not a name): og:site_name and the parts of <title>, the best fit wins (2026-11-10: the first
    part that shared one word with the domain used to win — a slogan before the name in the title was taken for the name)"""
    label = re.sub(r"[^a-z0-9]", "", (T.base_domain(T.nowww(host or "")) or "").split(".")[0].lower())
    cands = []
    for s in (og, title):
        if s:
            cands += [q.strip(" -–—|:·•»>") for q in re.split(r"\s+[|–—:·•»>]\s+|\s+-\s+|\s*[|»]\s*|(?<=\w):\s+", s)]  # 2026-11-11: » and > cut a title too
    best, best_s, spelled = "", 0.0, ""
    for i, c in enumerate(cands):
        c = re.sub(r"^(?:welcome to|bienvenue (?:[àa]|au|aux|chez|sur)(?: le| la| l['’])?)\s+", "", c, flags=re.I)  # "Welcome to ABC"
        if not (2 <= len(c) <= 80) or T.BAD_TITLE.search(c):
            continue
        f = name_fit(c, label)
        sc = f - 0.01 * i  # equal fits: the earlier candidate (og:site_name first)
        if f == 45.0 and " " in c and not spelled:
            spelled = re.sub(r"\s+", " ", c).strip()  # a name whose initials are the domain ("Amalgamated Dairies Limited" on adl.ca)
        if sc > best_s:
            best, best_s = re.sub(r"\s+", " ", c).strip(), sc
    if spelled and best and " " not in best and len(best) <= 6 and re.sub(r"[^a-z0-9]", "", best.lower()) == label:
        best = spelled  # "ADL | Amalgamated Dairies Limited": the name spelled out, not the bare acronym
    if best_s >= 20.0 and label and len(best.split()) >= 3:
        # 2026-11-11: "Buy Domains & Email At Hover.com" was the name of 5,078 rows' vendor — a slogan that carries the site's own address is not
        # a name; the word in front of the dot is
        m = re.search(r"(?<![A-Za-z0-9])(%s)\.[a-z]{2,6}(?![A-Za-z0-9])" % re.escape(label), best, re.I)
        if m:
            best = m.group(1).capitalize() if m.group(1).islower() else m.group(1)
    return best if best_s >= 20.0 else ""


def install_hooks():
    """what the candidate rules need from the pages ap_crawler reads anyway: the site's own name, its postal address, the vendor's assets"""
    import cc_clients as CCL
    import tech_relationships as T
    shop_rx = T.VENDORS["shopify"]["asset_re_c"]
    orig_visible, orig_note = C.visible, C.note_ap_page

    def visible2(raw):
        st = getattr(_tl, "st", None)
        if st is not None:
            try:
                if not st.get("name") and st.get("name_tries", 0) < 3:  # the home page first; two more pages when it names nothing usable
                    st["name_tries"] = st.get("name_tries", 0) + 1
                    title, meta = T.page_meta(raw)
                    st["name"] = site_name_for(st.get("host") or "", meta.get("og:site_name"), title, T)
                    st.setdefault("title", (title or "")[:200])
                if "shopify" not in st:
                    m = shop_rx.search(raw)
                    if m:
                        st["shopify"] = re.sub(r"\s+", " ", raw[max(0, m.start() - 30):m.end() + 50])[:160]
            except Exception:
                pass
        return orig_visible(raw)

    def note2(key, name, site, final, text, is_pdf):
        st = getattr(_tl, "st", None)
        if st is not None and "addr" not in st and not is_pdf:
            try:
                m, cc = None, ""
                for cc_, rx in (("CA", CCL.ADDR), ("US", US_ADDR), ("GB", GB_ADDR), ("AU", AU_ADDR)):
                    m = rx.search(text)
                    if m:
                        cc = cc_
                        break
                if m:
                    st["addr"] = (cc, re.sub(r"^\S*\s", "", text[max(0, m.start() - 110):m.end()].strip())[-200:], final)
                if st.get("shopify") and "shopify_url" not in st:
                    st["shopify_url"] = final
            except Exception:
                pass
        if st is not None and "rbq" not in st and not is_pdf:
            try:  # a Québec contractor prints its RBQ licence number on its own site (tools/rbq_licences.py joins it to the Régie's list of active licences)
                m = RBQ_ID.search(text)
                if m:
                    st["rbq"] = (m.group(1) + m.group(2) + m.group(3), final, re.sub(r"\s+", " ", text[max(0, m.start() - 80):m.end() + 40]).strip()[:220])
            except Exception:
                pass
        return orig_note(key, name, site, final, text, is_pdf)
    C.visible, C.note_ap_page = visible2, note2
    return T


FACTS = os.path.join(INC, "claude_lead_site_facts.jsonl.gz")
# 2026-11-10: the facts file grew with every site read and was rewritten whole (compressed: git kept every version). New lines now go to append-only
# shards, site_facts/facts_<stamp>.gz; the single file is no longer rewritten. Readers take both through facts_records() (the latest line of a key wins).
FACTS_DIR = os.path.join(INC, "site_facts")


def facts_records():
    for p in ([FACTS] if os.path.exists(FACTS) else []) + sorted(glob.glob(os.path.join(FACTS_DIR, "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8") as f:
            for l in f:
                try:
                    o = json.loads(l)
                except ValueError:
                    continue
                if o.get("key"):
                    yield o


RBQ_ID = re.compile(r"(?<![A-Za-z])(?:R\.?\s?B\.?\s?Q\.?|R[ée]gie du b[âa]timent(?: du Qu[ée]bec)?)(?![A-Za-z])[^0-9]{0,30}?(\d{4})[\s\-.\u00a0\u2010-\u2014]{0,3}(\d{4})[\s\-.\u00a0\u2010-\u2014]{0,3}(\d{2})(?!\d)", re.I)


# 2026-11-11: a home page asked for at one domain name that answers at the HOME page of another domain is the organisation's own other
# site — a second name it registered (osfs.ca -> flyos.ca, feuer.ca -> valenciarisk.com, mathusee.ca -> mathcanada.ca). Measured on 130
# .ca sites that had given no mailbox: 18 are such names and the site they answer at prints a role mailbox of its own domain. Not such a
# case: a page INSIDE another site (an agent's profile on the brokerage's site, a dealer's page on the maker's), a platform or a network,
# a parking or for-sale service, the own domain of a registrar or host (a suspended or expired account), a site with 150+ host names.
MOVED_HOME = re.compile(r"/?(?:(?:en|fr|en-ca|fr-ca|en-us|ca|home|accueil|index\.(?:html?|php|aspx?)|default\.aspx?)/?)?", re.I)
# registrable domains that are never an organisation's own second site: parking and for-sale services, registrars and hosts, networks,
# marketplaces and directories (the whole name is compared: "canada.ca" is not found inside "mathcanada.ca")
NOT_A_SITE = re.compile(r"^(sedo|sedoparking|dan|afternic|hugedomains|bodis|parkingcrew|above|domainmarket|buydomains|uniregistry|squadhelp|atom|brandbucket|domainnamesales|efty|"
                        r"undeveloped|namecheap|name|dynadot|porkbun|gandi|ovh|ovhcloud|ionos|hostinger|bluehost|hostgator|dreamhost|siteground|registrar-servers|parklogic|domainsponsor|"
                        r"voodoo|skenzo|linktr|linktree|bitly|carrd|beacons|taplink|doubleclick|webnames|rebel|hover|tucows|opensrs|enom|networksolutions|register|web|domain|domains|"
                        r"canva|notion|medium|etsy|ebay|kijiji|booking|airbnb|expedia|opentable|doordash|ubereats|skipthedishes|yelp|houzz|homestars|facebook|instagram|linkedin|"
                        r"twitter|x|youtube|tiktok|pinterest|google|apple|microsoft|amazon|wordpress|wix|wixsite|squarespace|shopify|myshopify|godaddy|godaddysites|weebly|webflow|"
                        r"blogspot|tumblr|substack|github|yellowpages|pagesjaunes|canada411|indeed|eventbrite|walmart|bestbuy|costco|realtor|centris|autotrader|tripadvisor|"
                        r"canada|gc)\.[a-z]{2,6}(?:\.[a-z]{2})?$", re.I)
GOV_SHARED = re.compile(r"(^|\.)(gc|canada)\.ca$|\.gouv\.qc\.ca$|(^|\.)gov\.[a-z]{2}\.ca$|\.gov$|\.gov\.[a-z]{2}$", re.I)
_MOVED = {}


def moved_site_ok(start, final):
    """is `final` (where the home page asked for at `start` answered) the home page of the organisation's own other site?"""
    try:
        pf = urllib.parse.urlparse(final or "")
        h = (pf.hostname or "").lower()
        h = h[4:] if h.startswith("www.") else h
        if not h or "." not in h or pf.query or not MOVED_HOME.fullmatch(pf.path or "/"):
            return False
        d = C.registrable(h)
        if "tools" not in _MOVED:
            import cc_clients as CCL
            import credit_scan as CS
            _MOVED["tools"] = (CCL, CS, CCL.many_hosts(), CS.big_providers())
        CCL, CS, many, big = _MOVED["tools"]
        if (CS.PLATFORM.search(h) or NOT_A_SITE.match(d) or GOV_SHARED.search(h) or CCL.MULTI_TENANT.search(h) or CCL.SPAM.search(h)  # SPAM: a lapsed name bought to feed a betting site
                or d in many or big.get(d, 0) >= 200 or not CCL.own_host(h, d)):
            return False
        return True
    except Exception:
        return False


def facts_line(key, site, st):
    """what the buyer's own pages say about the buyer: its name (og:site_name / title of the home page) and its postal address (quote + page).
    contrib/claude/rank_buyers/rank.py uses it for the bill-to name and address of a lead that only carried a domain."""
    import cc_clients as CCL
    o = {"key": key, "site": site, "date": TODAY, "site_name": st.get("name") or "", "title": st.get("title") or ""}
    if st.get("moved"):  # the site on file is a second name of the organisation: the site that answers, and the name that was asked
        pf = urllib.parse.urlparse(st["moved"])
        o.update(site="%s://%s/" % (pf.scheme, pf.netloc), asked=site, moved=st["moved"])
    if st.get("addr"):
        o.update(address_country=st["addr"][0], address_quote=st["addr"][1], address_url=st["addr"][2], address=CCL.address_from(st["addr"][1]))
    if st.get("rbq"):
        o["ids"] = {"rbq": {"v": st["rbq"][0], "url": st["rbq"][1], "q": st["rbq"][2]}}
    return json.dumps(o, ensure_ascii=False) + "\n"


def run_pool(tasks, one, a, deadline, on_timeout):
    """a few sites answer so slowly that one thread can hold a runner for an hour (first cycle, 2026-11-10). When only stragglers are left and
    nothing finished for --straggler-seconds, they are recorded as "timeout" and the run ends; sites not started by the deadline stay queued."""
    ex = ThreadPoolExecutor(a.workers)
    def timed(t):
        t["_deadline"] = time.time() + a.site_seconds  # ap_crawler.crawl stops opening pages of this site after that
        return one(t)
    futs = {ex.submit(timed, t): t for t in tasks}
    pending, last, tail = set(futs), time.time(), 0
    while pending:
        fin, pending = wait(pending, timeout=min(30, max(1, a.straggler_seconds / 3)))
        if fin:
            last = time.time()
        if len(pending) <= a.workers and not tail:
            tail = time.time()  # only sites already being read are left
        if (len(pending) <= a.workers and (time.time() - last > a.straggler_seconds or time.time() - tail > a.site_seconds + a.straggler_seconds)) or time.time() > deadline + 300:
            for f in pending:
                if f.running():
                    on_timeout(futs[f])
            break
    return len(pending)


# Every Shopify store has these generated pages. "Contact information" prints the trade name, e-mail and address the merchant entered (first
# candidate crawls: 54 % of stores gave no mailbox from the linked pages alone). The privacy policy names the address to write to: measured
# 2026-11-10 on 120 stores that had given no mailbox, 22 print one of their own domain there, about two thirds of them a role mailbox.
STORE_PAGES = ("policies/contact-information", "pages/contact", "pages/contact-us", "policies/refund-policy", "policies/privacy-policy")


def store_task(second_look):
    """reading limits of a store (every request goes through the one queue towards Shopify's network): the home page, then the generated
    pages, and the reading stops once two pages are read and a mailbox is on file. A store that gave no mailbox before the privacy-policy
    page was part of the list gets that one page, nothing else."""
    if second_look:
        return {"_no_sitemap": True, "_max_pages": 1, "_only_paths": ("policies/privacy-policy",)}
    return {"_no_sitemap": True, "_max_pages": 7, "_stop_found": 2}


def shard_ok(h, k, n):
    return int(hashlib.sha1(h.encode()).hexdigest(), 16) % n == k


def host_of(site):
    site = (site or "").strip()
    return (urllib.parse.urlparse(site if "//" in site else "https://" + site).hostname or "").lower() if site else ""


def leads_mode(a, k, n):
    if os.environ.get("GITHUB_WORKFLOW") == "row-factory" and not a.registry:
        # a row-factory run queued before 2026-11-10 05:24Z still has the mailbox crawl as its last stage; mailbox-crawl.yml reads the same queue
        # back to back, and two readers on one queue would open every site twice
        print("the mailbox crawl runs in mailbox-crawl.yml now: nothing is read here", flush=True)
        return
    install_hooks()
    # 2026-11-10 (rule "r2"): front-office role mailboxes (sales@, service@, orders@ …) count when a site publishes nothing better; the sites that
    # gave "nothing_found" under the first rule are read once more (their done line has no "r2" mark)
    done = set()
    if True:
        latest = {}
        for l in lead_done_lines():
            q = l.split("\t")
            if q and q[0]:
                latest[q[0]] = q
        # 2026-11-11 (rule "r3"): the reader now follows a site to the domain its home page lives on, asks the www. twin of a bare name that
        # does not answer, starts where the home-page scan found the site, and knows more role words (gestion@, leasing@, membership@ …).
        # Sites that gave "nothing_found" before (no "r3" mark) are read once more — after every site that was never read.
        reread = set()
        for q in latest.values():
            if q and q[0] and len(q) > 2 and q[2] == "nothing_found" and "r3" not in q[5:]:
                reread.add(q[0])
            elif q and q[0]:
                done.add(q[0])
    # 2026-11-10: the leads found from the owner's Mac (claude_buyer_leads.csv) can be read here too: 33,600 of them have a website and no
    # mailbox row yet, and the Mac's own crawler is off. A lead that already has a mailbox row in any lane's results file is not read again.
    # … and a lead whose website domain already carries a mailbox row under another key (the same organisation delivered through a contract, a
    # registry or another lead — e.g. a delivered row whose own home page credits a Canadian vendor, tools/credit_scan.py) is not read either:
    # rank.py lends that organisation's confirmed mailbox to the lead (same registrable domain, one organisation)
    known, known_dom = set(), set()
    for p in glob.glob(os.path.join(ROOT, "data/incoming/*/*buyer_ap_results*.csv")):
        try:
            with open(p, encoding="utf-8", errors="replace", newline="") as f:
                for r in csv.DictReader(f):
                    if r.get("buyer_key") and (r.get("ap_email") or "").strip():
                        known.add(r["buyer_key"])
                        eh = host_of(r.get("evidence_url"))
                        if eh and "." in eh:
                            known_dom.add(C.registrable(eh))
        except Exception:
            pass
    try:
        import credit_scan as _CSV
        via = _CSV.site_via()  # sites that answer on plain http or on www. only (scan detector 5): the reader starts where the scan read them
    except Exception:
        via = {}
    sites = {}  # websites found later for leads that had none (tools/lead_sites.py: Wikidata official website, exact name match)
    lw = os.path.join(INC, "claude_lead_websites.csv")
    if os.path.exists(lw):
        for r in csv.DictReader(open(lw, encoding="utf-8")):
            sites[r["buyer_key"]] = r["website"]
    tasks, hosts, skipped = [], set(), 0
    try:  # tools/credit_scan.py (detector 4) notes which home pages print a role mailbox of their own: those sites are read first (near-certain rows)
        import credit_scan as CS
        hints = CS.site_hints()
    except Exception as e:
        print("no home-page hints: %s" % e, flush=True)
        hints = {}
    # the cloud leads file is read with its shards (tools/lead_store.py: lead_shards/ holds the rows added, changed or withdrawn since the base file —
    # the engines that always wrote shards, BBB / RBQ / business licences, and since 2026-11-10 every engine)
    import lead_store as LS
    for fi, path in enumerate([x.strip() for x in a.leads.split(",") if x.strip()]):
        if not os.path.exists(path):
            continue
        fi = min(fi, 2)
        for r in (csv.DictReader(gzip.open(path, "rt", encoding="utf-8", newline="")) if path.endswith(".gz") else LS.reader(path)):
            h = host_of(r.get("website") or sites.get(r["buyer_key"]))
            if not h or "." not in h or r["buyer_key"] in done or h in hosts or not shard_ok(h, k, n):
                continue
            if r["buyer_key"] in known or C.registrable(h) in known_dom:
                skipped += 1
                continue
            hosts.add(h)
            try:
                nv = int(float(r.get("canadian_vendor_rows") or 1))
            except ValueError:
                nv = 1
            hb = h[4:] if h.startswith("www.") else h
            tasks.append({"task_id": "CC-" + r["buyer_key"].split(":")[-1][:10], "buyer_key": r["buyer_key"], "buyer_name": r.get("buyer_name") or h,
                          "known_website": _CSV.site_url(hb, via) if (via.get(hb) and h == hb) else "https://%s/" % h,
                          "_n": nv, "_f": fi, "_em": 0 if (hints.get(hb) or ("", ""))[0] else 1, "_rr": int(r["buyer_key"] in reread)})
    # registry candidates (2026-11-10, tier R of rank.py): a .ca site whose home page prints a role mailbox of its own and that no lead names yet.
    # Its relationship is the registration of its .ca domain name (agreement with the Canadian Internet Registration Authority, paid for through a
    # CIRA-certified Canadian registrar); what is missing is the mailbox row with its page and quote. A light read: at most 8 pages.
    n_reg = 0
    if a.registry:
        lead_doms = {C.registrable(h[4:] if h.startswith("www.") else h) for h in hosts}
        rank_em = {"invoice_submission": 0, "accounts_payable": 0, "supplier_payment": 0, "finance": 1, "procurement": 1, "general": 2, "role": 3}
        cand = []
        for dom, (em, cc) in hints.items():
            if not em or not dom.endswith(".ca") or cc not in ("", "CA") or not shard_ok(dom, k, n):
                continue
            rd = C.registrable(dom)
            key = "lead:" + hashlib.sha1(("%s|reg:ca" % rd).encode()).hexdigest()[:16]
            if rd != dom or rd in lead_doms or rd in known_dom or key in done or key in known:
                continue
            cand.append((rank_em.get(em, 3) + (10 if key in reread else 0), dom, key))
        cand.sort()
        try:
            _via = CS.site_via()  # sites that answer on plain http or on www. only (scan detector 5): the reader starts where the scan read them
        except Exception:
            _via = {}
        for _, dom, key in cand[:a.registry]:
            tasks.append({"task_id": "CC-" + key.split(":")[-1][:10], "buyer_key": key, "buyer_name": dom, "known_website": CS.site_url(dom, _via), "_n": 0, "_f": 9, "_em": 0, "_max_pages": 8,
                          "_rr": int(key in reread)})
            n_reg += 1
        print("registry candidates (.ca sites whose home page prints a role mailbox, no lead yet): %d queued of %d" % (n_reg, len(cand)), flush=True)
    # second class of registry candidates (2026-11-10): .ca sites whose home page was read and prints NO role mailbox — 428,464 of them; the
    # organisation's mailbox, when it publishes one, is on its contact page. Measured on 200 such sites, 4 pages each: 10 % give a role mailbox.
    # Read last (after every lead and every first-class candidate), 4 pages at most, sites that print a Canadian postal address first.
    if getattr(a, "registry2", 0):
        try:
            lead_doms = {C.registrable(h[4:] if h.startswith("www.") else h) for h in hosts}
            taken = {host_of(t["known_website"])[4:] if host_of(t["known_website"]).startswith("www.") else host_of(t["known_website"]) for t in tasks}
            cand2 = []
            for dom, cc in CS.ca_sites_without_mailbox().items():
                if cc not in ("", "CA") or not shard_ok(dom, k, n):
                    continue
                rd = C.registrable(dom)
                key = "lead:" + hashlib.sha1(("%s|reg:ca" % rd).encode()).hexdigest()[:16]
                if rd != dom or rd in lead_doms or rd in known_dom or key in done or key in known or dom in taken:
                    continue
                cand2.append(((0 if cc == "CA" else 1) + (10 if key in reread else 0), dom, key))
            cand2.sort()
            _via2 = CS.site_via()
            for _, dom, key in cand2[:a.registry2]:
                tasks.append({"task_id": "CC-" + key.split(":")[-1][:10], "buyer_key": key, "buyer_name": dom, "known_website": CS.site_url(dom, _via2), "_n": 0, "_f": 10, "_em": 2, "_max_pages": 4,
                              "_rr": int(key in reread)})
            print("registry candidates, second class (.ca sites, no mailbox on the home page): %d queued of %d" % (min(len(cand2), a.registry2), len(cand2)), flush=True)
        except Exception as e:
            print("second-class registry candidates not queued: %s" % e, flush=True)
    # sites whose home page prints a role mailbox first; then the first leads file first; within a file, buyers named by several Canadian vendors first
    tasks.sort(key=lambda t: (t["_em"], t.get("_rr", 0), t["_f"], -t["_n"]))
    print("lead sites whose home page prints a role mailbox (read first): %d of %d; sites read before that gave nothing, read once more under the rules of 2026-11-11: %d" % (
        sum(1 for t in tasks if not t["_em"]), len(tasks), sum(1 for t in tasks if t.get("_rr"))), flush=True)
    print("leads with a mailbox row already, under their own key or their website domain (not read again): %d" % skipped, flush=True)
    if a.limit:
        tasks = tasks[:a.limit]
    print("shard %d/%d: %d new lead sites to read (%d done before)" % (k, n, len(tasks), len(done)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock = threading.Lock()
    stats = {"sites": 0, "with_mailbox": 0, "rows": 0, "blocked": 0, "errors": 0}
    fr = open("out/lead_rows_%d.csv" % k, "a", newline="", encoding="utf-8")
    w = csv.DictWriter(fr, fieldnames=C.COLS, extrasaction="ignore")
    w.writeheader()
    fd = open("out/lead_done_%d.tsv" % k, "a", encoding="utf-8")
    ff = open("out/lead_facts_%d.jsonl" % k, "a", encoding="utf-8")

    def one(t):
        if time.time() > deadline:
            return
        st = {"host": host_of(t["known_website"])}
        _tl.st = st

        def moved(start, final, st=st):
            ok = moved_site_ok(start, final)
            if ok:  # the name of the site is read against the domain that answers
                st["host"], st["moved"] = host_of(final), final
            return ok
        t["_moved_ok"] = moved
        try:
            result, pages, rows = C.crawl(t, t.get("_max_pages") or a.max_pages, general="any")
        except Exception as e:
            result, pages, rows = "error:%s" % type(e).__name__, 0, []
        _tl.st = None
        C.AP_PAGES.pop(t["buyer_key"], None)  # the walker's page memory is not needed here
        rows = [r for r in rows if ok_mailbox(r.get("ap_email"))]
        with lock:
            stats["sites"] += 1
            stats["with_mailbox"] += bool(rows)
            if t.get("_f") == 9:
                stats["registry_sites"] = stats.get("registry_sites", 0) + 1
                stats["registry_with_mailbox"] = stats.get("registry_with_mailbox", 0) + bool(rows)
            if t.get("_f") == 10:
                stats["registry2_sites"] = stats.get("registry2_sites", 0) + 1
                stats["registry2_with_mailbox"] = stats.get("registry2_with_mailbox", 0) + bool(rows)
            if not t.get("_em"):
                stats["hinted_sites"] = stats.get("hinted_sites", 0) + 1
                stats["hinted_with_mailbox"] = stats.get("hinted_with_mailbox", 0) + bool(rows)
            stats["rows"] += len(rows)
            stats["blocked"] += result == "blocked"
            stats["errors"] += str(result).startswith("error")
            w.writerows(rows)
            if rows and (st.get("name") or st.get("addr") or st.get("moved")):
                ff.write(facts_line(t["buyer_key"], t["known_website"], st))
            stats["front_office_role_only"] = stats.get("front_office_role_only", 0) + bool(rows and "front-office role mailbox" in (rows[0].get("notes") or ""))
            if st.get("moved"):
                stats["site_lives_at_another_domain"] = stats.get("site_lives_at_another_domain", 0) + 1
                stats["site_lives_at_another_domain_with_mailbox"] = stats.get("site_lives_at_another_domain_with_mailbox", 0) + bool(rows)
            if t.get("_rr"):
                stats["read_once_more"] = stats.get("read_once_more", 0) + 1
                stats["read_once_more_with_mailbox"] = stats.get("read_once_more_with_mailbox", 0) + bool(rows)
            fd.write("%s\t%s\t%s\t%d\t%d\tr2\tr3%s\n" % (t["buyer_key"], TODAY, result, pages, len(rows), ("\tmoved=" + host_of(st["moved"])) if st.get("moved") else ""))
            if stats["sites"] % 200 == 0:
                fr.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), stats, flush=True)

    def on_timeout(t):
        with lock:
            fd.write("%s\t%s\ttimeout\t0\t0\tr2\tr3\n" % (t["buyer_key"], TODAY))
            stats["errors"] += 1
    left = run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fr.close(); fd.close(); ff.close()
    print("finished", stats, "(stragglers left: %d)" % left, flush=True)


def candidates_mode(a, k, n):
    import cc_tenants as CT
    T = install_hooks()
    # candidates seen live by tools/credit_scan.py (a link to the organisation's Jane portal on its own page): the free single-practitioner
    # plan is ruled out on the portal itself, read at the end and only for candidates that passed everything else. All runners together stay
    # under 2 requests per second on the vendor's platform.
    _tfetch, _gap = T.fetch, max(1.0, n / 2.0)
    T.fetch = lambda url, gap=1.0, limit=2_000_000, _hops=0: _tfetch(url, max(gap, _gap), limit, _hops)
    # Shopify stores (2026-11-10): 9,024 of the first 23,437 stores read answered 403 / 429. Every store sits on Shopify's own network, which counts
    # requests per reader, not per store: one request per second per store was still a burst for the platform. Now every request to a store waits
    # its turn in ONE queue per runner (2 requests per second towards Shopify's network), and the stores that refused are read once more ("b2").
    shop_gate, shop_next = threading.Lock(), [0.0]

    def shop_turn():
        with shop_gate:
            t0 = max(time.time(), shop_next[0])
            shop_next[0] = t0 + 0.5
        w0 = t0 - time.time()
        if w0 > 0:
            time.sleep(w0)
    _cfetch = C.fetch

    def fetch_gated(url, *aa, **kw):
        st0 = getattr(_tl, "st", None)
        if st0 is not None and st0.get("_shop"):
            shop_turn()
        return _cfetch(url, *aa, **kw)
    C.fetch = fetch_gated

    def portal_owned(vkey, slug, purl, site_host, name):
        """(True, why) when the portal a site links to is the site's OWN account. An author links to a library's catalogue, a newspaper to a
        council's meeting portal, a practitioner's personal page to the clinic's booking page: none of them is the vendor's customer.
        Proof, in this order: the portal address carries the organisation's name (headwayphysio.janeapp.com on headwayphysio.com); the portal
        page links back to the site; the portal page names the same organisation. Jane: the portal must also list 2+ practitioners (free plan)."""
        import unicodedata
        flat = lambda x: re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", x or "").encode("ascii", "ignore").decode().lower())
        lab = flat(C.registrable(site_host).split(".")[0])
        core = flat(re.sub(r"^pub-", "", (slug or "").split(".")[0]))
        slug_ok = vkey != "jobber" and len(core) >= 4 and len(lab) >= 4 and (core == lab or (len(core) >= 5 and core in lab) or (len(lab) >= 5 and lab in core))
        if vkey == "jobber":  # a client-hub login or a work-request form is a business's own customer tool; its address is an id, not a name
            return True, "the site links its own Jobber client hub / request form"
        if slug_ok and vkey != "jane":
            return True, "the portal address carries the organisation's name"
        try:
            info, why = T.portal_info(vkey, purl)
        except Exception as e:
            info, why = None, "error:" + type(e).__name__
        if not info:
            return (slug_ok and vkey != "jane"), why  # Jane: unreadable or fewer than 2 practitioners -> not accepted
        if slug_ok:
            return True, "the portal address carries the organisation's name"
        w = info.get("website") or ""
        if w and C.registrable(host_of(w)) == C.registrable(site_host):
            return True, "the portal page links back to the organisation's site"
        ptoks = [t for t in re.findall(r"[a-z0-9]{5,}", unicodedata.normalize("NFKD", info.get("name") or "").encode("ascii", "ignore").decode().lower())
                 if t not in GENERIC_SITE_WORDS and t not in ("clinic", "clinique", "centre", "center", "health", "sante", "wellness", "physio", "physiotherapy", "massage", "therapy",
                                                               "library", "bibliotheque", "public", "county", "district", "school", "college", "university")]
        if any(t in lab or t in flat(name) for t in ptoks):
            return True, "the portal page names the same organisation"
        return False, "portal_of_another_organisation"
    done, second_look = set(), set()
    if True:  # candidates that gave "nothing_found" before the front-office role rule (no "r2" mark) are read once more
        latest = {}
        for l in CT.tenant_done_lines(TDONE):  # the old single file, then the shards of tenant_state/ (the latest line of a candidate decides)
            q = l.split("\t")
            if q and q[0]:
                latest[q[0]] = q
        for q in latest.values():
            if len(q) > 5 and q[5] == "shopify" and q[2] == "nothing_found" and "p2" in q[6:] and "p3" not in q[6:]:
                second_look.add(q[0])  # a store read before the privacy-policy page was part of the reading: that one page is read, nothing else
            if q and q[0] and not (len(q) > 2 and q[2] == "nothing_found" and ("r2" not in q[6:] or (len(q) > 5 and q[5] == "shopify" and "p3" not in q[6:]))) \
                    and not (len(q) > 5 and q[2].startswith("out_of_scope") and q[5] in ("jane", "jobber") and "s2" not in q[6:]) \
                    and not (len(q) > 5 and q[5] == "shopify" and q[2] in ("blocked", "no_address", "service_not_seen", "no_name") and "b2" not in q[6:]):
                done.add(q[0])  # Jane / Jobber candidates refused as "out of scope" before their terms were read (one contracting entity for every country) are read once more
    tasks, hosts = [], set()
    with gzip.open(a.candidates, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            h = host_of(r.get("website"))
            if not h or "." not in h or r["cand_key"] in done or h in hosts or not shard_ok(h, k, n):
                continue
            if a.vendors and r["vendor_key"] not in a.vendors.split(","):
                continue
            if a.skip_vendors and r["vendor_key"] in a.skip_vendors.split(","):
                continue
            hosts.add(h)
            tasks.append({"task_id": "TN-" + hashlib.sha1(r["cand_key"].encode()).hexdigest()[:10], "buyer_key": r["cand_key"], "buyer_name": r.get("name") or h,
                          "known_website": "https://%s/" % h, "_c": r,
                          # every Shopify store has these generated pages; "contact information" prints the trade name, e-mail and address the merchant entered
                          # (first candidate crawls: 54 % of stores gave no mailbox from the linked pages alone)
                          "_extra_paths": STORE_PAGES if r["vendor_key"] == "shopify" else (),
                          # a store: its sitemap lists products, and every request goes through the one queue towards Shopify's network (store_task)
                          **(store_task(r["cand_key"] in second_look) if r["vendor_key"] == "shopify" else {})})
    # organisations whose own address is an alias (CNAME record) of their account on a vetted platform — learn.example.org ->
    # example.docebosaas.com (tools/dns_services.py: the host sweep, and the www alias of the lookups; tools/tech_relationships.py
    # ALIAS_DOMAINS). The organisation's own DNS names the vendor; its site is read like any other candidate of that vendor.
    n_alias = 0
    try:
        import dns_services as DNS
        want_v = set(a.vendors.split(",")) if a.vendors else None
        skip_v = set((a.skip_vendors or "").split(","))
        if not (want_v and want_v <= {"shopify"}):
            for o in DNS.records():
                cn = (o.get("cn") or "").strip(".").lower()
                vk = T.ALIAS_DOMAINS.get(C.registrable(cn)) if cn else None
                if not vk or vk in skip_v or (want_v and vk not in want_v) or vk not in T.VENDORS:
                    continue
                h = C.registrable(o["d"])
                ck = "t:%s:%s" % (vk, h)
                if not h or h == C.registrable(cn) or ck in done or h in hosts or ("www." + h) in hosts or not shard_ok(h, k, n):
                    continue
                hosts.add(h)
                host_asked = o["d"] if o.get("sw") else "www." + o["d"]
                site = h if o.get("sw") else "www." + h  # the www alias IS the site's address (the bare name often does not answer)
                r = {"cand_key": ck, "vendor_key": vk, "name": "", "website": "https://%s/" % site, "evidence_url": "https://dns.google/resolve?name=%s&type=CNAME" % host_asked, "capture": o.get("t") or "",
                     "name_basis": "", "website_basis": "the organisation's own address %s is an alias (CNAME record) of %s, looked up %s" % (host_asked, cn, o.get("t") or ""),
                     "slug": "asset", "extra": json.dumps({"dns_alias": "%s is an alias (CNAME record) of %s, looked up %s" % (host_asked, cn, o.get("t") or "")})}
                tasks.append({"task_id": "TN-" + hashlib.sha1(ck.encode()).hexdigest()[:10], "buyer_key": ck, "buyer_name": h, "known_website": "https://%s/" % site, "_c": r, "_extra_paths": ()})
                n_alias += 1
    except Exception as e:
        print("DNS alias candidates not loaded: %s" % e, flush=True)
    if n_alias:
        print("organisations whose own address is an alias of a vetted platform account queued: %d" % n_alias, flush=True)
    # stores the DNS lookups found on Shopify's storefront addresses (tools/dns_services.py): candidates made here, never written to the
    # candidates file (they number in the hundreds of thousands); their done lines go to the shards like every other candidate's
    n_dns = n_my = 0
    if a.dns_stores and (not a.vendors or "shopify" in a.vendors.split(",")) and "shopify" not in (a.skip_vendors or "").split(","):
        try:
            import dns_services as DNS
            # 2026-11-10, measured on the first 32,989 stores read: accepted 43 % on .ca, 38 % on .us, 26 % on .com, 0-2 % on another country's
            # ending (.uk 672 of 703 out of scope, .au 641 of 654, .de 421 of 436 …: those stores contract with Shopify's Irish or Singapore
            # company). A run reads a bounded number of stores: the endings where a store is most often in scope come first.
            GEN = {"com", "co", "net", "org", "shop", "store"}
            GEN2 = {"io", "me", "tv", "cc", "ai", "gg", "ly", "fm", "to", "la", "vc", "ws", "sh", "so", "xyz", "info", "biz", "online", "site", "club", "life", "world", "love", "art", "design", "boutique"}
            def cls_of(h):
                e = h.rsplit(".", 1)[-1]
                return 0 if e in ("ca", "us") else 1 if e in GEN else 2 if (e in GEN2 or len(e) > 2) else 3
            cand = []
            for o in DNS.records():
                if not o.get("shop"):
                    continue
                h = o["d"]
                ck = "t:shopify:%s" % h
                if ck in done or h in hosts or ("www." + h) in hosts or not shard_ok(h, k, n):
                    continue
                hosts.add(h)
                cand.append((cls_of(h), hashlib.sha1(h.encode()).hexdigest(), h, o))
            cand.sort()
            print("stores from the DNS lookups not read yet: %d (by ending: %s)" % (len(cand), dict(sorted(collections.Counter(c[0] for c in cand).items()))), flush=True)
            dns_tasks = []
            for _, _, h, o in cand[:a.dns_stores]:
                ck = "t:shopify:%s" % h
                r = {"cand_key": ck, "vendor_key": "shopify", "name": "", "website": "https://%s/" % h, "evidence_url": "https://dns.google/resolve?name=%s&type=A" % h, "capture": o.get("t") or "",
                     "name_basis": "", "website_basis": "the domain's address record points to Shopify's storefront network (A %s, looked up %s)" % (o.get("a") or "", o.get("t") or ""),
                     "slug": "asset", "extra": "{}"}
                dns_tasks.append({"task_id": "TN-" + hashlib.sha1(ck.encode()).hexdigest()[:10], "buyer_key": ck, "buyer_name": h, "known_website": "https://%s/" % h, "_c": r,
                                  "_extra_paths": STORE_PAGES, **store_task(ck in second_look)})
                n_dns += 1
        except Exception as e:
            dns_tasks = []
            print("DNS store candidates not loaded: %s" % e, flush=True)
        print("stores from the DNS lookups queued: %d" % n_dns, flush=True)
        # stores named by their myshopify.com address only (2026-11-10): the host-level web graph holds 206,386 <store>.myshopify.com names. A store
        # with a domain of its own answers its myshopify.com address with that domain (a redirect; "domain" in its meta.json): one request tells
        # whether there is a store, where it is and which site is its own. The site is then read like any other store's.
        if getattr(a, "myshopify", 0) and os.path.exists(MYSHOPIFY):
            try:
                with gzip.open(MYSHOPIFY, "rt", encoding="utf-8") as fh:
                    names = [l.strip().lower() for l in fh if l.strip()]
                names = sorted((hashlib.sha1(x.encode()).hexdigest(), x) for x in names if re.fullmatch(r"[a-z0-9][a-z0-9-]{1,60}", x) and shard_ok(x + ".myshopify.com", k, n))
                for _, x in names:
                    if n_my >= a.myshopify:
                        break
                    h = x + ".myshopify.com"
                    ck = "t:shopify:%s" % h
                    if ck in done or h in hosts:
                        continue
                    hosts.add(h)
                    r = {"cand_key": ck, "vendor_key": "shopify", "name": "", "website": "https://%s/" % h, "evidence_url": "https://%s/meta.json" % h, "capture": TODAY,
                         "name_basis": "", "website_basis": "the store's own myshopify.com address (%s, a host name of the web graph) answers with this domain as its own" % h, "slug": "asset", "extra": "{}"}
                    tasks.append({"task_id": "TN-" + hashlib.sha1(ck.encode()).hexdigest()[:10], "buyer_key": ck, "buyer_name": h, "known_website": "https://%s/" % h, "_c": r,
                                  "_extra_paths": STORE_PAGES, **store_task(False)})
                    n_my += 1
            except Exception as e:
                print("myshopify.com addresses not loaded: %s" % e, flush=True)
            print("stores named by their myshopify.com address queued: %d (read before the DNS stores: a bounded number a run)" % n_my, flush=True)
        tasks.extend(dns_tasks)
    for i, t in enumerate(tasks):
        t["_i"] = i
    tasks.sort(key=lambda t: (t["_c"]["vendor_key"] == "shopify", t["_i"] if t["_c"]["vendor_key"] == "shopify" else 0, t["buyer_key"]))  # customer portals (organisation named by the portal) before stores; stores in the order queued
    if a.limit:
        tasks = tasks[:a.limit]
    print("shard %d/%d: %d candidate sites to read (%d done before)" % (k, n, len(tasks), len(done)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock = threading.Lock()
    stats = collections.Counter()
    fr = open("out/lead_rows_%d.csv" % k, "a", newline="", encoding="utf-8")
    w = csv.DictWriter(fr, fieldnames=C.COLS, extrasaction="ignore")
    w.writeheader()
    fl = open("out/tenant_leads_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/tenant_done_%d.tsv" % k, "a", encoding="utf-8")
    ff = open("out/lead_facts_%d.jsonl" % k, "a", encoding="utf-8")

    def one(t):
        if time.time() > deadline:
            return
        c = t["_c"]
        vkey = c["vendor_key"]
        scope = CT.SCOPE.get(vkey, ("CA",))
        st = {"host": host_of(t["known_website"]), "_shop": vkey == "shopify"}
        _tl.st = st
        meta, mu = None, "https://%s/meta.json" % st["host"]
        if vkey == "shopify":
            # every Shopify store answers /meta.json with what the merchant entered: the store's name, city, province, country, and its
            # myshopify.com address — the store's own statement of where it is (many stores print no postal address) and proof of the service
            try:
                if C.allowed(mu):
                    s_, _, d_, _ = C.fetch(mu, 200_000)
                    if s_ == 200 and d_[:1] == b"{":
                        mj = json.loads(d_.decode("utf-8", "replace"))
                        if isinstance(mj, dict) and str(mj.get("myshopify_domain") or "").endswith(".myshopify.com"):
                            meta = mj
            except Exception:
                meta = None
            if st["host"].endswith(".myshopify.com"):
                # the candidate is the store's myshopify.com address: the site to read is the domain the store gives as its own
                own = re.sub(r"^https?://", "", str((meta or {}).get("domain") or "")).strip("/").lower()
                why = "" if meta else "no_store"
                if meta and (not own or own.endswith(".myshopify.com") or not re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", own)):
                    why = "no_own_domain"
                elif meta and ("t:shopify:%s" % own in done or "t:shopify:%s" % (own[4:] if own.startswith("www.") else own) in done):
                    why = "known_store"
                if why:
                    _tl.st = None
                    with lock:
                        stats["sites"] += 1
                        stats["myshopify_" + why] += 1
                        fd.write("%s\t%s\t%s\t1\t0\t%s\tr2\ts2\tp2\tb2\tp3\n" % (t["buyer_key"], TODAY, why + (":" + own if own and why == "known_store" else ""), vkey))
                    return
                t["known_website"] = "https://%s/" % own
                st["host"], mu = own, "https://%s/meta.json" % own
                with lock:
                    stats["myshopify_own_domain_found"] += 1
            mcc = str((meta or {}).get("country") or "").upper()
            if meta and mcc and mcc not in scope:  # a store abroad contracts with Shopify's Irish or Singapore company: no further page is read
                _tl.st = None
                with lock:
                    stats["sites"] += 1
                    stats["out_of_scope"] += 1
                    stats["shopify_meta_json"] += 1
                    fd.write("%s\t%s\tout_of_scope:%s\t1\t0\t%s\tr2\ts2\tp2\tb2\tp3\n" % (t["buyer_key"], TODAY, mcc, vkey))
                return
        try:
            result, pages, rows = C.crawl(t, t.get("_max_pages") or a.max_pages, general="any")
        except Exception as e:
            result, pages, rows = "error:%s" % type(e).__name__, 0, []
        _tl.st = None
        C.AP_PAGES.pop(t["buyer_key"], None)
        rows = [r for r in rows if ok_mailbox(r.get("ap_email"))]
        name = (c.get("name") or st.get("name") or "").strip()
        if meta:
            where = ", ".join(str(meta.get(x)) for x in ("city", "province", "country") if meta.get(x))
            st.setdefault("shopify", '"myshopify_domain":"%s" in the store\'s own %s' % (meta["myshopify_domain"], mu))
            st.setdefault("shopify_url", mu)
            if "addr" not in st and mcc in scope:
                st["addr"] = (mcc, "%s (city, province and country the store states in %s)" % (where, mu), mu)
            name = name or str(meta.get("name") or "").strip()[:120]
        try:
            ex = json.loads(c.get("extra") or "{}")
        except ValueError:
            ex = {}
        if not rows:
            res = result if result != "found" else "no_role_mailbox"
        elif "addr" not in st:
            res = "no_address"
        elif st["addr"][0] not in scope:
            res = "out_of_scope:" + st["addr"][0]
        elif vkey == "shopify" and not st.get("shopify"):
            res = "service_not_seen"
        elif not name:
            res = "no_name"
        else:
            res = "accepted"
        own_why = ""
        if res == "accepted" and ex.get("seen_on") and T.VENDORS.get(vkey, {}).get("kind") == "portal" and (c.get("slug") or "") != "asset":
            # seen live by tools/credit_scan.py as a link on the site: is it the site's OWN portal? (checked last: one request to the vendor's platform)
            own, own_why = portal_owned(vkey, c.get("slug") or "", ex.get("portal") or "https://%s/" % (c.get("slug") or ""), st.get("host") or "", name)
            if not own:
                res = "portal_not_its_own:" + (own_why or "")[:40]
        rec = None
        if res == "accepted":
            site = t["known_website"]
            seen_url = st.get("shopify_url") or site
            row = {"portal_slug": c.get("slug") or "", "capture": c.get("capture") or "", "tenant_url": c.get("evidence_url") or "", "name_basis": c.get("name_basis") or ("og:site_name / title of the organisation's own home page" if not c.get("name") else ""),
                   "website_basis": c.get("website_basis") or "", "buyer_country": st["addr"][0], "buyer_address_quote": st["addr"][1], "buyer_address_url": st["addr"][2],
                   "service_seen": ("%s (in the page source of %s, %s)" % (st.get("shopify"), seen_url, TODAY)) if vkey == "shopify" else
                                   ("%s: the organisation's own address %s (public DNS)" % (T.VENDORS[vkey]["name"], ex["dns_alias"])) if ex.get("dns_alias") else
                                   ("%s: %s — on the organisation's own page %s (read %s)%s" % (T.VENDORS[vkey]["name"], ex.get("portal") or ex.get("via") or "", ex.get("seen_on"), c.get("capture"),
                                                                                                    ("; " + own_why) if own_why else "")) if ex.get("seen_on") else
                                   "customer portal %s captured %s (Common Crawl)" % (c.get("evidence_url"), c.get("capture"))}
            rec = T.lead(vkey, name, site, seen_url if vkey == "shopify" else (c.get("evidence_url") or site), row)
            if vkey != "shopify" and c.get("capture"):  # a customer portal: the day the archive saw it; a store: today, on its own pages
                rec["row"]["observed_date"] = rec["row"]["record_date"] = c["capture"]
            key, _ = CT.lead_row(rec)
            for r in rows:
                r["buyer_key"], r["task_id"], r["org_name_as_found"] = key, "TN-" + key.split(":")[-1][:10], name
        with lock:
            stats["sites"] += 1
            stats[res.split(":")[0]] += 1
            stats["rows"] += len(rows) if rec else 0
            stats["shopify_meta_json"] += bool(meta)
            stats["accepted_on_meta_json_location"] += bool(rec and meta and st.get("addr", ("", "", ""))[2] == mu)
            if rec:
                w.writerows(rows)
                fl.write(json.dumps(rec, ensure_ascii=False) + "\n")
                ff.write(facts_line(key, t["known_website"], dict(st, name=name)))
            fd.write("%s\t%s\t%s\t%d\t%d\t%s\tr2\ts2\tp2\tb2\tp3\n" % (t["buyer_key"], TODAY, res, pages, len(rows), vkey))
            if stats["sites"] % 200 == 0:
                fr.flush(); fd.flush(); fl.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    def on_timeout(t):
        with lock:
            fd.write("%s\t%s\ttimeout\t0\t0\t%s\tr2\n" % (t["buyer_key"], TODAY, t["_c"]["vendor_key"]))
            stats["timeout"] += 1
    left = run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fr.close(); fd.close(); fl.close(); ff.close()
    print("finished", dict(stats), "(stragglers left: %d)" % left, flush=True)


def facts_mode(a, k, n):
    """Completeness pass over rows ALREADY delivered (owner 2026-11-09 20:48 EST: "complete data … all the details that go within an invoice"):
    33,136 delivered rows lacked a bill-to name and / or address. For every delivered row with a website and no address, read the home and
    contact pages (same polite reader) and keep what the organisation prints about itself: its name and its postal address, quoted, plus a
    better mailbox (invoicing / AP / finance / purchasing) when the row only has a general one. rank.py turns that into the bill-to block."""
    install_hooks()
    done = {l.split("\t")[0] for l in open(SFDONE, encoding="utf-8")} if os.path.exists(SFDONE) else set()
    have = {o["key"] for o in facts_records()}
    tasks, hosts = [], set()
    import ranked_io  # the ranked table is committed in parts (GitHub's 100 MB limit)
    if True:
        for r in ranked_io.rows(a.facts_ranked):
            key = (r.get("keys") or "").split("|")[0]
            h = host_of(r.get("buyer_website"))
            if not r.get("email") or not key or key in done or key in have or not h or "." not in h or h in hosts or not shard_ok(h, k, n):
                continue
            if (r.get("buyer_address") or "").strip() and ((r.get("buyer_legal_name_as_published") or "").strip() or (r.get("buyer_trade_name_as_published") or "").strip()):
                continue  # bill-to already complete
            hosts.add(h)
            tasks.append({"task_id": "SF-" + hashlib.sha1(key.encode()).hexdigest()[:10], "buyer_key": key, "buyer_name": r.get("buyer") or h, "known_website": "https://%s/" % h,
                          "_general": (r.get("email_type") or "").startswith("general"), "_tier": r.get("tier") or ""})
    tasks.sort(key=lambda t: (t["_tier"] == "I", t["buyer_key"]))  # rows with a relationship record before the inferred ones
    if a.limit:
        tasks = tasks[:a.limit]
    print("shard %d/%d: %d delivered rows without a complete bill-to block to read (%d done before)" % (k, n, len(tasks), len(done)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock = threading.Lock()
    stats = collections.Counter()
    fr = open("out/lead_rows_%d.csv" % k, "a", newline="", encoding="utf-8")
    w = csv.DictWriter(fr, fieldnames=C.COLS, extrasaction="ignore")
    w.writeheader()
    ff = open("out/lead_facts_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/site_facts_done_%d.tsv" % k, "a", encoding="utf-8")

    def one(t):
        if time.time() > deadline:
            return
        st = {"host": host_of(t["known_website"])}
        _tl.st = st
        try:
            result, pages, rows = C.crawl(t, a.max_pages, general=False)
        except Exception as e:
            result, pages, rows = "error:%s" % type(e).__name__, 0, []
        _tl.st = None
        C.AP_PAGES.pop(t["buyer_key"], None)
        better = [r for r in rows if ok_mailbox(r.get("ap_email")) and r.get("ap_email_type") != "general"] if t["_general"] else []
        with lock:
            stats["sites"] += 1
            stats["with_address"] += "addr" in st
            stats["with_name"] += bool(st.get("name"))
            stats["better_mailbox"] += bool(better)
            stats["blocked"] += result == "blocked"
            if st.get("name") or st.get("addr"):
                ff.write(facts_line(t["buyer_key"], t["known_website"], st))
            w.writerows(better)
            fd.write("%s\t%s\t%s\t%d\t%d\n" % (t["buyer_key"], TODAY, result if result != "found" else "read", pages, 1 if "addr" in st else 0))
            if stats["sites"] % 500 == 0:
                fr.flush(); ff.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    def on_timeout(t):
        with lock:
            fd.write("%s\t%s\ttimeout\t0\t0\n" % (t["buyer_key"], TODAY))
            stats["timeout"] += 1
    left = run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fr.close(); ff.close(); fd.close()
    print("finished", dict(stats), "(stragglers left: %d)" % left, flush=True)


def merge(a):
    """append the shard rows to the results file (never a row the validator would reject, never a duplicate) and union the done files"""
    cols, have, rows = None, set(), []
    n_signed = 0
    # the results file grows by ~700 bytes a row and GitHub refuses files over 100 MB: cccrawl01, 02 … each closed at 30 MB (every reader globs
    # data/incoming/*/*buyer_ap_results*.csv)
    outs = sorted(glob.glob(OUT.replace("cccrawl01", "cccrawl[0-9][0-9]")))
    for op in outs:
        with open(op, encoding="utf-8", newline="") as f:
            rd = csv.DictReader(f)
            cols = cols or rd.fieldnames
            for r in rd:
                have.add((r["buyer_key"], (r.get("ap_email") or "").lower(), r.get("evidence_url") or ""))
    out_path = outs[-1] if outs else OUT
    if os.path.exists(out_path) and os.path.getsize(out_path) > 30 * 1024 * 1024:
        out_path = OUT.replace("cccrawl01", "cccrawl%02d" % (len(outs) + 1))
    for p in sorted(glob.glob(os.path.join(a.merge, "lead_rows_*.csv"))):
        with open(p, encoding="utf-8", newline="") as f:
            rd = csv.DictReader(f)
            cols = cols or rd.fieldnames
            for r in rd:
                key = (r.get("buyer_key"), (r.get("ap_email") or "").lower(), r.get("evidence_url") or "")
                if not r.get("buyer_key") or r["buyer_key"] == "buyer_key" or key in have or not ok_mailbox(r.get("ap_email")):
                    continue
                if C.SIGNED_URL.search(r.get("evidence_url") or ""):
                    n_signed += 1  # a pre-signed storage address (valid a few minutes): not evidence — a runner on the earlier crawler code wrote it
                    continue
                if a.tenants and not r["buyer_key"].startswith("lead:"):
                    continue  # a candidate that was not accepted never reaches the results file
                have.add(key)
                rows.append(r)
    if rows:
        # the file is changed while the rows are written, not only before: one merge brought 52,000 rows (35 MB) on 2026-11-10 and cccrawl01 closed
        # at 71 MB; a merge of 100,000 rows would have passed GitHub's 100 MB limit in one step
        k = int(re.search(r"cccrawl(\d+)", os.path.basename(out_path)).group(1))
        f = w = None
        for r in rows:
            if f is None or f.tell() > 30 * 1024 * 1024:
                if f is not None:
                    f.close()
                    k += 1
                    out_path = OUT.replace("cccrawl01", "cccrawl%02d" % k)
                first = not os.path.exists(out_path)
                f = open(out_path, "a", encoding="utf-8", newline="")
                w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
                if first:
                    w.writeheader()
            w.writerow(r)
        f.close()
    if n_signed:
        print("rows left out, their evidence address is a pre-signed storage address that cannot be opened again: %d" % n_signed)
    done_path, pat = (TDONE, "tenant_done_*.tsv") if a.tenants else (SFDONE, "site_facts_done_*.tsv") if a.site_facts else (DONE, "lead_done_*.tsv")
    seen = {}
    # --stamp (the workflows since 2026-11-10) = shard mode. A run that was queued with the earlier workflow file calls --merge without --stamp
    # and only commits the old single files: for it the old behaviour is kept, so nothing it found is lost.
    if a.tenants and a.stamp:  # the candidates' done lines go to an append-only shard (tenant_state/done_<stamp>.gz); the old single file is no longer rewritten
        import cc_tenants as CT
        new_lines = {}
        for p in sorted(glob.glob(os.path.join(a.merge, pat))):
            for l in open(p, encoding="utf-8"):
                q = l.rstrip("\n").split("\t")
                if q and q[0]:
                    new_lines[q[0]] = l.rstrip("\n")
        if new_lines:
            os.makedirs(CT.TSTATE, exist_ok=True)
            with gzip.open(os.path.join(CT.TSTATE, "done_%s.gz" % (a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime()))), "wt", encoding="utf-8") as f:
                f.write("\n".join(new_lines[k] for k in sorted(new_lines)) + "\n")
        for l in CT.tenant_done_lines(TDONE):
            q = l.split("\t")
            if q and q[0]:
                seen[q[0]] = l
    elif not a.site_facts and not a.tenants and a.stamp:  # the lead crawl: this run's done lines go to a new shard (crawl_state/lead_done_<stamp>.gz)
        new_lines = {}
        for p in sorted(glob.glob(os.path.join(a.merge, pat))):
            for l in open(p, encoding="utf-8"):
                q = l.rstrip("\n").split("\t")
                if q and q[0]:
                    new_lines[q[0]] = l.rstrip("\n")
        if new_lines:
            os.makedirs(LSTATE, exist_ok=True)
            with gzip.open(os.path.join(LSTATE, "lead_done_%s.gz" % (a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime()))), "wt", encoding="utf-8") as f:
                f.write("\n".join(new_lines[k] for k in sorted(new_lines)) + "\n")
        for l in lead_done_lines():
            q = l.split("\t")
            if q and q[0]:
                seen[q[0]] = l
    else:
        for p in [done_path] + sorted(glob.glob(os.path.join(a.merge, pat))):
            if os.path.exists(p):
                for l in open(p, encoding="utf-8"):
                    q = l.rstrip("\n").split("\t")
                    if q and q[0]:
                        seen[q[0]] = l.rstrip("\n")
        with open(done_path, "w", encoding="utf-8") as f:
            for key in sorted(seen):
                f.write(seen[key] + "\n")
    new_facts = {}
    for p in sorted(glob.glob(os.path.join(a.merge, "lead_facts_*.jsonl"))):
        for l in open(p, encoding="utf-8"):
            try:
                o = json.loads(l)
                new_facts[o["key"]] = o
            except (ValueError, KeyError):
                pass
    if a.stamp and a.facts_shards:  # this run's lines as one new shard (the kind of run in the name: two merges of one workflow run share a stamp)
        kind = "t" if a.tenants else "s" if a.site_facts else "l"
        n_before = len({o["key"] for o in facts_records()})
        if new_facts:
            os.makedirs(FACTS_DIR, exist_ok=True)
            with gzip.open(os.path.join(FACTS_DIR, "facts_%s%s.gz" % (a.stamp, kind)), "wt", encoding="utf-8") as f:
                for key in sorted(new_facts):
                    f.write(json.dumps(new_facts[key], ensure_ascii=False) + "\n")
        n_after = len({o["key"] for o in facts_records()})
        print("site facts (buyer's own name / address): %d (+%d)" % (n_after, n_after - n_before))
    else:  # a run queued before 2026-11-10 08:15Z (its workflow file does not pass --facts-shards and commits only the single file): as before
        facts = {}
        if os.path.exists(FACTS):
            for l in gzip.open(FACTS, "rt", encoding="utf-8"):
                try:
                    o = json.loads(l)
                    facts[o["key"]] = o
                except (ValueError, KeyError):
                    pass
        nf = len(facts)
        facts.update(new_facts)
        if facts:
            with gzip.open(FACTS, "wt", encoding="utf-8") as f:
                for key in sorted(facts):
                    f.write(json.dumps(facts[key], ensure_ascii=False) + "\n")
        print("site facts (buyer's own name / address): %d (+%d)" % (len(facts), len(facts) - nf))
    res = collections.Counter((l.split("\t") + ["?", "?", "?"])[2].split(":")[0] for l in seen.values())
    print("%s sites read so far: %d (%s); mailbox rows added this run: %d; buyers with a mailbox row: %d" % (
        "candidate" if a.tenants else "delivered-row" if a.site_facts else "lead", len(seen), ", ".join("%s %d" % kv for kv in res.most_common(7)), len(rows), len({x[0] for x in have})))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--leads", default=os.path.join(INC, "claude_buyer_leads_cc.csv"))
    a.add_argument("--candidates", default="", help="claude_tenant_candidates.csv.gz (tools/cc_tenants.py): accept-or-reject mode")
    a.add_argument("--vendors", default="", help="candidates mode: only these vendor keys (comma separated)")
    a.add_argument("--skip-vendors", default="", help="candidates mode: not these vendor keys (the stores are read by a process that rides along the mailbox crawl)")
    a.add_argument("--merge", default="", help="directory of shard outputs to append to the files on main")
    a.add_argument("--tenants", action="store_true", help="with --merge: the shard outputs come from candidates mode")
    a.add_argument("--site-facts", action="store_true", help="with --merge: the shard outputs come from --facts-ranked mode")
    a.add_argument("--facts-ranked", default="", help="ranked_buyers.csv.gz: completeness pass over delivered rows without a bill-to name / address")
    a.add_argument("--shard", default="0/1")
    a.add_argument("--minutes", type=float, default=150)
    a.add_argument("--max-pages", type=int, default=25)
    a.add_argument("--workers", type=int, default=40)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--stamp", default="", help="with --merge: the name of this run's shard files")
    a.add_argument("--facts-shards", action="store_true", help="with --merge --stamp: the site facts go to site_facts/facts_<stamp>.gz (the workflow commits that folder)")
    a.add_argument("--myshopify", type=int, default=0, help="candidates mode: also read up to this many stores per shard named only by their myshopify.com address (host names of the web graph)")
    a.add_argument("--dns-stores", type=int, default=0, help="candidates mode: also read up to this many stores per shard that the DNS lookups found on Shopify's storefront addresses")
    a.add_argument("--registry", type=int, default=0, help="leads mode: also read up to this many registry candidates per shard (.ca sites whose home page prints a role mailbox)")
    a.add_argument("--registry2", type=int, default=0, help="leads mode: then up to this many second-class registry candidates per shard (.ca sites whose home page prints no mailbox; 4 pages each)")
    a.add_argument("--straggler-seconds", type=float, default=240, help="when only slow sites are left and nothing finished for this long, stop")
    a.add_argument("--site-seconds", type=float, default=420, help="wall-clock budget for one site: no new page is opened after that (what was read so far counts)")
    a = a.parse_args()
    if a.merge:
        merge(a)
        return
    k, n = int(a.shard.split("/")[0]), max(1, int(a.shard.split("/")[1]))
    os.makedirs(C.STATE, exist_ok=True)
    os.makedirs("out", exist_ok=True)
    (candidates_mode if a.candidates else facts_mode if a.facts_ranked else leads_mode)(a, k, n)
    sys.stdout.flush()
    os._exit(0)  # do not wait for straggler threads


if __name__ == "__main__":
    main()
