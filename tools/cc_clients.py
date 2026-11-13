#!/usr/bin/env python3
"""Row factory, cloud edition: NEW buyers from the client / case-study / portfolio pages of Canada-located vendors, at web scale, read from
the Common Crawl archive. No AI, no search engine, no request to the vendors' own sites.

Why (owner 2026-11-09 19:18 EST: "the 63,000 rows have not moved … the goal is 200,000"): the lead scanners that produced the relationship rows
(client_lists*.py, logo_walls.py, customer_stories.py) only ever ran on the owner's Mac, from vendor lists kept on that Mac. With the Mac off,
nothing produced a new buyer. This engine needs no local list and no Mac: Common Crawl's columnar URL index names every captured page of every
.ca host whose PATH is a client page (the same path rule contrib/claude/rank_buyers/rank.py uses for a "client listing"), and the page itself
is read from the archive with one HTTP range request to data.commoncrawl.org.

  index   --shard K/N            scan the index parts K mod N of the newest crawl                      -> out/cc_rel_pages_<K>.csv
  extract --shard K/N            read each page of the shard, keep its outbound client links           -> out/cc_leads_<K>.jsonl (+ noaddr, done)
  merge   SHARD_DIR              shard files + what is on main -> data/incoming/claude/claude_buyer_leads_cc.csv, claude_lead_details_cc.jsonl.gz,
                                 claude_cc_extract_done.tsv
Rules kept:
  1. Vendor in Canada (AGENTS.md hard rule 1): only when the vendor's OWN PAGE prints a Canadian postal address (province + postal code; the
     quote is kept as proof). A .ca domain alone is not enough (CIRA also admits foreign trademark owners): such pages go to a side file.
  2. Buyer named: the linked organisation's own domain and the label the vendor gave it; links without a label, generic labels, platforms,
     social networks, "website by" credits and directory pages (more than 150 linked sites) are dropped. A domain linked by more than 15
     vendors is a platform or a badge, not a client (same rule as tools/lead_scanner.py).
  3. Evidence: the vendor page URL, its capture date in the archive, the label, the address quote. The buyer's mailbox is NOT taken here: it
     is read on the buyer's own site by tools/lead_crawl.py and re-fetched by the referee like every other mailbox.
Polite: only data.commoncrawl.org is contacted, a few requests at a time, identified user agent, retries with back-off.
"""
import argparse, collections, csv, glob, gzip, hashlib, html, io, json, os, random, re, sys, time, urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INC = os.path.join(ROOT, "data/incoming/claude")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
CC = "https://data.commoncrawl.org/"
TODAY = time.strftime("%Y-%m-%d")
PAGES = os.path.join(INC, "claude_cc_rel_pages.csv.gz")
EXDONE = os.path.join(INC, "claude_cc_extract_done.tsv")
LEADS_CC = os.path.join(INC, "claude_buyer_leads_cc.csv")
DETAILS_CC = os.path.join(INC, "claude_lead_details_cc.jsonl.gz")
SIDE = os.path.join(INC, "claude_cc_leads_noaddr.jsonl.gz")   # client links of vendors whose page printed no address (never delivered from here)
VADDR = os.path.join(INC, "claude_cc_vendor_addr.jsonl.gz")   # the vendor's Canadian postal address read on its own home / contact page (address pass)
ADONE = os.path.join(INC, "claude_cc_addr_done.tsv")          # vendor domain, crawl, date, status, pages read
APAGES = os.path.join(INC, "claude_cc_addr_pages.csv.gz")      # home / contact pages (index rows) of non-.ca organisations located in Canada (universe index)
APAGE_COLS = ["dom", "url", "host", "path", "fetch_time", "warc_filename", "warc_record_offset", "warc_record_length", "crawl"]
CF_CA = "vendor located in Canada (cc: .ca domain + Canadian postal address on its own page)"
# domains whose subdomains belong to different organisations (site builders, association platforms): a page on one of them says nothing about
# the others, so such a domain is never one "vendor" — no address found on one tenant's page may promote the links of another (2026-11-10: 539
# member pages of US chambers sat under the key cc:chambermaster.com, waiting for any page of that domain to print a Canadian address)
MULTI_TENANT = re.compile(r"(^|\.)(chambermaster\.com|growthzoneapp\.com|growthzonesites\.com|micronetonline\.com|wildapricot\.(org|com)|memberclicks\.net|site-ym\.com|yourmembership\.com|"
                          r"wixsite\.com|squarespace\.com|weebly\.com|wordpress\.com|blogspot\.[a-z.]{2,6}|godaddysites\.com|webflow\.io|myshopify\.com|business\.site|github\.io|netlify\.app|"
                          r"herokuapp\.com|azurewebsites\.net|square\.site|bigcartel\.com|substack\.com|medium\.com|tumblr\.com|strikingly\.com|mystrikingly\.com|jimdofree\.com|jimdosite\.com|"
                          r"webnode\.[a-z.]{2,6}|ueniweb\.com|carrd\.co|notion\.site|wpengine\.com|kinsta\.cloud|pantheonsite\.io|webador\.[a-z.]{2,6}|site123\.me|yolasite\.com|"
                          r"clubexpress\.com|clubrunner\.ca|sportsengine\.com|teamsnap\.com|rampinteractive\.com|goalline\.ca|esportsdesk\.com)$", re.I)

# ---- whose address is it? (2026-11-11, row audit of the leads on file)
# A vendor is keyed by its registrable domain, and its Canadian address was taken from ANY host under that domain. Found on file: the address of
# a customer of Odoo (acie1.odoo.com, Sherbrooke) standing for odoo.com — Odoo is Belgian — on 358 leads; the Canadian Hockey League's office
# standing for three teams in Washington State whose sponsor pages sit under chl.ca/whl-…/ (214 leads); a platform's Vancouver address standing
# for American associations on its sub-sites (silkstart.com); a web agency's address standing for the client whose site it stages (new.webici.ca).
# Rule: the address that proves where a vendor is must be printed on that vendor's OWN site — the host of the page that names its clients, or a
# site of the same holder. A sub-site is the holder's own when it is named after a function (business., members., events., shop., fr. …) or
# after the domain itself; any other sub-site may be another body's.
OWN_LABEL = re.compile(r"^(?:www\d?|web|site|home|go|get|my|mon|app|apps|portal|portail|online|secure|support|help|aide|docs|terms|legal|about|contact|info|corp|corporate|"
                       r"company|global|group|groupe|business|members?|membres?|directory|annuaire|repertoire|extranet|intranet|events?|evenements?|conference|convention|congres|"
                       r"summit|sommet|forum|expo|gala|shop|store|boutique|blogs?|news|nouvelles|media|press|careers?|jobs|emplois|carrieres|community|connect|learn|training|"
                       r"formation|academy|register|inscription|tickets|billetterie|donate|dons|foundation|fondation|library|hub|archives?|past|old|[a-z]{2}|(?:19|20)\d\d)$", re.I)
STAGING_LABEL = re.compile(r"(?:^|[.\-])(?:new|dev|staging|stage|test|demo|preview|beta|sandbox|temp|wp\d+|clients?)(?:$|[.\-])", re.I)
GRAPH_MT = os.path.join(INC, "credit_scan", "graph_multitenant.csv.gz")  # domains with 150+ host names of their own in the web graph


def _reg(host):
    import ap_crawler as _C
    return _C.registrable((host or "").lower().strip("."))


def own_host(host, dom):
    """is `host` a site of the holder of the registrable domain `dom` itself (the bare domain, www, a sub-site named after a function or after
    the domain)? False for any other sub-site: a platform's customer, a league's team, a university's unit, an agency's client on a test host."""
    host = (host or "").lower().strip(".")
    if host == dom:
        return True
    if not dom or not host.endswith("." + dom):
        return False
    lab = re.sub(r"[^a-z0-9]", "", dom.split(".")[0])
    for part in re.split(r"[.\-]", host[:-len(dom) - 1]):
        if not part or not (OWN_LABEL.match(part) or (len(lab) >= 4 and lab in re.sub(r"[^a-z0-9]", "", part))):
            return False
    return True


_MANY = None


def many_hosts():
    """{domain: host names} of the domains with 150+ host names in the web graph: platforms, universities, governments, leagues"""
    global _MANY
    if _MANY is None:
        _MANY = {}
        if os.path.exists(GRAPH_MT):
            with gzip.open(GRAPH_MT, "rt", encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh):
                    try:
                        _MANY[r["dom"]] = int(r["hosts"] or 0)
                    except (KeyError, ValueError):
                        pass
    return _MANY


def proof_fits(dom, page_url, proof_url, several_bodies=()):
    """does the address printed on `proof_url` belong to the vendor whose page `page_url` (under the registrable domain `dom`) names the clients?
    -> (True | False | None, reason). None: the proof sits on another domain — a rename is the caller's to judge (credit_scan.proof_page_ok).
    several_bodies: domains known to carry the sites of several bodies (three or more named sub-sites with vendor pages)."""
    vh = (urllib.parse.urlparse(page_url or "").hostname or "").lower()
    ph = (urllib.parse.urlparse(proof_url or "").hostname or "").lower()
    if not ph or not vh or base(ph) == base(vh):
        return True, ""  # printed on the page itself, or on the same host
    if _reg(ph) != dom:
        return None, "address read on another domain"
    if own_host(vh, dom):
        return (True, "") if own_host(ph, dom) else (False, "address read on a sub-site that may be another body's")
    if not own_host(ph, dom):
        return False, "address read on another sub-site of the domain"
    sub = vh[:-len(dom) - 1] if vh.endswith("." + dom) else vh
    if dom in many_hosts() or dom in several_bodies or MULTI_TENANT.search(dom) or STAGING_LABEL.search(sub):
        return False, "page on a sub-site of a domain that carries the sites of several bodies; the address is the domain holder's"
    return True, ""


def path_tenants(pages):
    """{domain: {first path segment: site name}} for the domains whose own host carries the pages of several bodies under path prefixes
    (chl.ca/whl-silvertips/, chl.ca/whl-chiefs/ …): three or more site names, each under its own first path segment, no word in common.
    pages: iterable of (domain, page url, site name)."""
    by = collections.defaultdict(lambda: collections.defaultdict(set))
    for dom, url, name in pages:
        u = urllib.parse.urlparse(url or "")
        seg = (u.path or "/").strip("/").split("/")[0].lower()
        name = (name or "").strip()
        if not dom or not seg or not name or not own_host((u.hostname or "").lower(), dom) or re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", name.lower()):
            continue
        if re.fullmatch(r"[a-z]{2}(?:[-_][a-z]{2})?", seg):
            continue  # a language version of the site (/fr/, /zh/, /en-ca/): the same body under a translated name
        by[dom][name].add(seg)
    toks = lambda s: {w[:5] for w in re.findall(r"[a-zà-ÿ0-9]+", s.lower()) if len(w) >= 4}
    out = {}
    for dom, names in by.items():
        if len(names) < 3:
            continue
        segs = collections.Counter(s for ss in names.values() for s in ss)
        if any(len(ss) != 1 for ss in names.values()) or any(n != 1 for n in segs.values()):
            continue  # a name on several prefixes, or a prefix with several names: page titles of one site, not tenants
        ns = sorted(names)
        if any(toks(a) & toks(b) for i, a in enumerate(ns) for b in ns[i + 1:]):
            continue
        out[dom] = {next(iter(ss)): n for n, ss in names.items()}
    return out


def canada_field(dom, basis="", how=""):
    """the lead's Canada field: for a .ca host its domain + its own address; for another host the dataset's location basis + its own address.
    how == "CA-loc": the vendor's live site prints no postal code; its own location line (a Canadian province) and a Canadian telephone number"""
    if how == "CA-loc":
        return "vendor located in Canada (cc: %s + its own site gives its location in Canada and a Canadian telephone number)" % (".ca domain" if (dom or "").lower().endswith(".ca") else (basis or "an organisation the dataset locates in Canada").replace("=", ":"))
    if (dom or "").lower().endswith(".ca"):
        return CF_CA
    return "vendor located in Canada (cc: %s + Canadian postal address on its own page)" % ((basis or "an organisation the dataset locates in Canada").replace("=", ":"))


LEAD_COLS = ["buyer_key", "buyer_name", "website", "canadian_vendor_rows", "example_vendor", "canada_field_value", "evidence_dataset", "latest_record_date"]
PAGE_COLS = ["url", "host", "dom", "path", "fetch_time", "warc_filename", "warc_record_offset", "warc_record_length"]

# the path rule of rank.py (REL_PATH / NOT_REL_PATH): a page that passes it is a "client listing" there, so every lead found here ranks as one
REL_SQL = r"client|customer|case-stud|casestud|case_stud|temoignage|t%c3%a9moignage|testimonial|success-stor|portfolio|our-work|realisations?([^a-z]|$)|r%c3%a9alisations?|nos-realisations|clientele"
NOT_SQL = (r"terms|reference|support|service|product|letter|lettre|news|nouvelle|blog|article|press|media|document|conditions|bill|/loi|career|emploi|job|event|evenement|contact|about|a-propos|partner|partenaire"
           r"|login|log-in|signin|sign-in|account|compte|portal|portail|espace-client|zone-client|acces-client|clientarea|client-area|client-access|client-cent|client-zone|customer-care|customer-cent|customer/"
           r"|/tag/|/tags/|/category/|/categorie/|/author/|/page/[0-9]|/feed|wp-json|wp-content|wp-admin|/cart|/panier|/checkout|privacy|/search|/recherche|\.(pdf|jpe?g|png|gif|xml|json|css|js)$")
# 2026-11-10 (owner: "a Canadian entity gets paid … establish that relationship"): two more kinds of page where a Canada-located organisation
# lists the parties that PAY it — its sponsors / exhibitors (they pay the organiser) and its dealers / retailers / distributors (they buy
# from the supplier). "sponsorship", "become a sponsor", "dealership", supplier / brand pages are not that and are left out.
SPONSOR_SQL = r"/[^/]*(sponsors|commanditaires|exhibitors?|exposants|advertisers|annonceurs)([-_.][^/]*)?/?$"  # advertisers pay the outlet that lists them
# tenants of a landlord and merchants of a mall, market or business association (rent, stall fees, levy): only list forms ("our tenants",
# "tenant directory", "merchants"); pages written FOR tenants link to utilities and agencies and are not lists
TENANT_SQL = (r"/[^/]*(our-tenants|tenant-directory|tenant-list|nos-locataires|liste-des-locataires|repertoire-des-locataires|merchants|marchands|commer(c|%c3%a7)ants|store-directory|shop-directory"
              r"|repertoire-des-(magasins|boutiques|commerces|marchands))([-_.][^/]*)?/?$")
# "distributors" is left out: a distributor's own page of that name lists the brands it carries (the wrong direction)
DEALER_SQL = r"/[^/]*(dealers?|where-to-buy|ou-acheter|o%c3%b9-acheter|retailers|stockists|d(e|%c3%a9)taillants|revendeurs|points-de-vente)([-_.][^/]*)?/?$"
INVESTOR = re.compile(r"ventures?\b|venture capital|capital\b|invest|private equity|\bequity\b|\bfunds?\b|\bfonds\b|holdings?\b|incubat|accelerat|\bangels?\b|placements", re.I)
MAX_LIST_SEGMENT = 36  # "our-dealers", "2026-golf-tournament-sponsors": a list page has a short last path part; an article slug that merely contains the word does not
NOT2_SQL = (r"become|devenir|devenez|opportunit|package|forfait|prospectus|application|apply|form|kit|levels|niveaux|sponsorship|commandite|login|log-in|signin|sign-in|account|compte|portal|portail"
            r"|blog|news|nouvelle|article|actualit|press|communiqu|regist|casino|blackjack|poker|betting|roulette|slots"
            r"|/tag/|/tags/|/category/|/categorie/|/author/|/page/[0-9]|/feed|wp-json|wp-content|wp-admin|/cart|/panier|/checkout|privacy|/search|/recherche|register|inscription"
            r"|supplier|fournisseur|brand|marque|manufactur|fabricant|career|emploi|job|\.(pdf|jpe?g|png|gif|xml|json|css|js)$")
# 2026-11-10: member directories of a Canada-located body (chamber of commerce, board of trade, association): the members pay it dues.
#   - the member pages of GrowthZone / ChamberMaster directories (/list/member/<name>-<id>): one member per page, with its own website;
#   - a page whose last path part is a member-list word (members, nos-membres, member-directory …). People lists (board, council, team,
#     staff, students …), member areas, "become a member" and fee pages are left out.
MEMBER_ONE_SQL = r"^/list/member/[^/]+/?$"
MEMBER_SQL = r"/[^/]*(members|membres|member-directory|membership-directory|member-list|directory-of-members|repertoire-des-membres|liste-des-membres)([-_.][^/]*)?/?$"
NOT3_SQL = (r"board|council|committee|comit|conseil|team|equipe|%c3%a9quipe|staff|personnel|faculty|executive|ex%c3%a9cutif|directors|administrat|family|famil|only|area|zone|login|log-in|signin|sign-in"
            r"|account|compte|portal|portail|become|devenir|devenez|join|adh%c3%a9|adhesion|benefit|avantage|application|apply|form|renew|register|inscription|fees|dues|cotisation|tarif|news|nouvelle"
            r"|blog|event|evenement|honorary|honoraire|founding|fondateur|past|ancien|crew|band|cast|choir|chorale|caucus|mla|mpp|legislat|parliament|parlement|senat|assembl|elected|elus|%c3%a9lus"
            r"|student|etudiant|%c3%a9tudiant|alumni|lab|research|recherche|group|groupe|profile|profil|user|forum|/tag/|/tags/|/category/|/categorie/|/author/|/page/[0-9]|/feed|wp-json|wp-content"
            r"|wp-admin|/cart|/panier|/checkout|privacy|/search|/recherche|\.(pdf|jpe?g|png|gif|xml|json|css|js)$")
_REL_RX, _NOT_RX, _SP_RX, _DL_RX, _NOT2_RX, _M1_RX, _MB_RX, _NOT3_RX, _TN_RX = (re.compile(x) for x in (REL_SQL, NOT_SQL, SPONSOR_SQL, DEALER_SQL, NOT2_SQL, MEMBER_ONE_SQL, MEMBER_SQL, NOT3_SQL, TENANT_SQL))
PER_DOMAIN_MEMBER_PAGES = 3000  # a chamber's directory has one page per member
MIN_MEMBER_LINKS = 5            # a member-list page counts as a directory only when it names at least this many organisations
MIN_LIST_LINKS = 3              # sponsor / dealer / tenant pages: a list names several parties (one or two stray links are not a list)
# links injected into hacked pages (betting, pills …): the link is dropped, and a page with three of them is dropped whole
SPAM = re.compile(r"casino|blackjack|poker|roulette|\bslots?\b|betting|bahis|kumarhane|kumar site|canl[ıi] kumar|casibom|\b\w*(?:pasha|jojo|holigan|ultra|mat|mars|saha|tipo|meri|most|rest|bets)\w*bet\w*\b|\bbets?\d|\b1xbet|"
                  r"porn|escort|viagra|(?<!spe)(?<!so)(?<!offi)cialis|payday loan|forex|replica watch", re.I)  # 2026-11-10: "specialist" contains "cialis", Kumar is a surname


def page_class(path):
    """client | sponsor | dealer | member | '' for a URL path (the same tests the index query applies)"""
    p = (path or "").lower()
    if _M1_RX.search(p):
        return "member"
    if rel_path(p) and not _NOT_RX.search(p):
        return "client"
    if not _NOT2_RX.search(p) and len(p.rstrip("/").rsplit("/", 1)[-1]) <= MAX_LIST_SEGMENT:
        if _DL_RX.search(p):
            return "dealer"
        if _SP_RX.search(p):
            return "sponsor"
        if _TN_RX.search(p):
            return "tenant"
    if _MB_RX.search(p) and not _NOT3_RX.search(p) and len(p.rstrip("/").rsplit("/", 1)[-1]) <= MAX_LIST_SEGMENT:
        return "member"  # the length rule: ".../david-girouard-et-gilbert-emond-membres-du-temple-de-la-renommee" is a news article, not a directory
    return ""


_OURWORK_TOP = re.compile(r"^/(?:(?:en|fr|en-ca|fr-ca)/)?[^/]*our-work")


def rel_path(p):
    """the client-page words of REL_SQL; "our-work" only as the first path part (/our-work/…: a firm's portfolio) — deeper
    (/advocacy/our-work/policy-areas/…) it is an organisation describing its programmes, and the links there are partners"""
    q = p if _OURWORK_TOP.match(p) else p.replace("our-work", "our-w0rk")
    # … and only in a short path part ("/clients/", "/case-studies/acme", "/portfolio/x"): a long slug that merely contains the word
    # ("/story/abbyy-names-…-chief-customer-experience-officer", "/alleviate-customers-booking-frustrations-…") is an article
    return any(len(seg) <= 30 and _REL_RX.search(seg) for seg in q.split("/"))


CLASS_TEXT = {"client": "client page of a Canada-located vendor (Common Crawl capture)",
              "sponsor": "sponsor / exhibitor page of a Canada-located organiser: the parties listed pay it (Common Crawl capture)",
              "dealer": "dealer / retailer page of a Canada-located supplier: the parties listed buy from it (Common Crawl capture)",
              "tenant": "tenant / merchant list of a Canada-located landlord, market or business association: the parties listed pay it rent, fees or a levy (Common Crawl capture)",
              "member": "member directory of a Canada-located body (chamber, board of trade, association): the members listed pay it dues (Common Crawl capture)"}
VENDOR_SKIP = re.compile(r"(^|\.)(gc|canada)\.ca$|\.gouv\.qc\.ca$|(^|\.)gov\.[a-z]{2}\.ca$|\.gov\.ca$|kijiji|yellowpages|pagesjaunes|canada411|indeed|eventbrite|amazon|ebay|walmart|bestbuy|costco|"
                         r"canadiantire|homedepot|(^|\.)cbc\.ca$|ctvnews|globalnews|radio-canada|lapresse|ledevoir|thestar|nationalpost|theglobeandmail|wikipedia|reddit|craigslist|linkedin|facebook|"
                         r"google|youtube|yelp|tripadvisor|booking|expedia|airbnb|realtor\.ca|centris|duproprio|autotrader|workopolis|glassdoor|monster|jobbank|canadapost|purolator|(^|\.)bell\.ca$|"
                         r"videotron|blogspot|wordpress|wixsite|weebly|squarespace|myshopify|godaddysites|webflow\.io|github\.io|tumblr|substack|medium\.com", re.I)
LABEL_SKIP = re.compile(r"\b(listed on|featured (?:on|in)|as seen (?:on|in)|reviewed on|rated on|find us on|verified|badge|award|winner|nominee|top rated|best of|voted|powered by|website by|site by|web ?site design|web design|design(?:ed)? by|developed by|built by|cr[ée]ation (?:de )?site|conception (?:de |du )?site|conception web|"
                        r"r[ée]alis[ée] par|propuls[ée] par|hosted by|h[ée]berg[ée]|theme by|template by|follow us|suivez|share|partager|privacy|confidentialit\w*|politique\w*|policy|policies|l[ée]gal\w*|mentions|terms|conditions|cookie\w*|"
                        r"sitemap|plan du site|accessibilit\w*|careers?|carri[èe]res?|emplois?|jobs?|log ?in|sign ?in|connexion|newsletter|infolettre|subscribe|abonne\w*|donate|faire un don|growthzone|chambermaster)\b", re.I)
PROV = (r"(?:QC|Qc|ON|BC|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NT|NU|Qu[ée]bec|Ontario|British Columbia|Colombie-Britannique|Alberta|Manitoba|Saskatchewan|Nova Scotia|Nouvelle-[ÉE]cosse|"
        r"New Brunswick|Nouveau-Brunswick|Newfoundland(?: and Labrador)?|Terre-Neuve(?:-et-Labrador)?|Prince Edward Island|[ÎI]le-du-Prince-[ÉE]douard|Yukon|Northwest Territories|Nunavut)")
PC = r"[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][  \-]?\d[ABCEGHJ-NPRSTV-Z]\d"
ADDR = re.compile(r"(?<![A-Za-z0-9])" + PROV + r"\)?[\s,. ]{0,6}(?:Canada[\s,. ]{0,4})?(" + PC + r")(?![A-Za-z0-9])")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:  # the same link reader and filters as the Mac scanners, so both produce the same kind of lead
    from client_lists import anchors, SKIP, base
except Exception:  # pragma: no cover
    SKIP = re.compile(r"facebook|linkedin|twitter|x\.com|instagram|youtube|youtu\.be|tiktok|pinterest|google|goo\.gl|apple\.com|microsoft|wordpress|wix|squarespace|shopify|godaddy|w3\.org", re.I)

    def base(host):
        host = (host or "").lower()
        return host[4:] if host.startswith("www.") else host

    def anchors(page, pageurl):
        for m in re.finditer(r"(?is)<a\s[^>]*?href\s*=\s*[\"']([^\"'#>]+)[\"'][^>]*>(.*?)</a>", page[:2_000_000]):
            href, inner = urllib.parse.urljoin(pageurl, m.group(1).strip()), m.group(2)
            alt = re.search(r"(?is)(?:alt|title)\s*=\s*[\"']([^\"']{2,120})[\"']", m.group(0) + inner)
            text = re.sub(r"(?s)<[^>]+>", " ", inner)
            yield href, re.sub(r"\s+", " ", (alt.group(1) if alt else "") or text).strip()
try:
    from lead_scanner import PLATFORMS, GENERIC_LABEL
except Exception:  # pragma: no cover
    PLATFORMS = re.compile(r"genially|issuu|canva|calameo|prezi|eventbrite|surveymonkey|typeform|jotform|dropbox|box\.com", re.I)
    GENERIC_LABEL = re.compile(r"^(read more|learn more|more|visit|website|site web|click here|here|cliquez ici|en savoir plus|voir|view|link|lien|home|accueil|\W*)$", re.I)


# a country / language selector ("USA", "Polska | Polski", "United States | English"): the organisation's own sites abroad, not its clients
COUNTRY_LABEL = re.compile(r"^(?:usa?|u\.s\.a?\.?|united states(?: of america)?|[ée]tats-unis|canada|uk|u\.k\.|united kingdom|royaume-uni|australia|australie|new zealand|ireland|irlande|france|germany|allemagne|deutschland|"
                           r"espa[ñn]a|spain|espagne|italia|italy|italie|polska|poland|pologne|china|chine|japan|japon|india|inde|brasil|brazil|br[ée]sil|m[ée]xico|mexique|chile|chili|argentina|argentine|colombia|"
                           r"colombie|peru|p[ée]rou|nigeria|south africa|slovenia|slov[ée]nie|latvia|lettonie|lithuania|estonia|sweden|su[èe]de|norway|norv[èe]ge|denmark|danemark|finland|finlande|netherlands|"
                           r"pays-bas|belgium|belgique|switzerland|suisse|austria|autriche|portugal|greece|gr[èe]ce|turkey|turquie|israel|uae|united arab emirates|saudi arabia|singapore|singapour|malaysia|"
                           r"indonesia|thailand|vietnam|philippines|korea|cor[ée]e|taiwan|hong kong|cura[çc]ao|costa rica|guatemala|honduras|panama|ecuador|uruguay|paraguay|bolivia|venezuela|"
                           r"global|international|worldwide|europe|asia|asie|africa|afrique|americas?|latin america|middle east|"
                           r"english|fran[çc]ais|french|espa[ñn]ol|spanish|deutsch|german|italiano|italian|portugu[êe]s|polski|nederlands|中文|日本語|한국어)(?:\s*[|/·(–-]\s*[\w\s().-]{1,30})?$", re.I)


def http_get(url, headers=None, timeout=90, tries=6, retry_http=()):
    h = {"User-Agent": UA}
    h.update(headers or {})
    err = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            err = e
            if e.code in (400, 401, 403, 404, 416) and e.code not in retry_http:
                raise
        except Exception as e:
            err = e
        time.sleep(min(60, 2 ** i + random.random() * 2))
    raise err


def newest_crawl(want=""):
    """(crawl id, parquet paths of its columnar index, subset=warc). The newest crawl whose index is published."""
    ids = [want] if want and want != "auto" else []
    if not ids:
        try:
            ids = [c["id"] for c in json.loads(http_get("https://index.commoncrawl.org/collinfo.json", tries=3))][:5]
        except Exception as e:
            print("collinfo not reachable (%s); falling back to the last crawl we mined" % type(e).__name__, flush=True)
        ids.append("CC-MAIN-2026-43")
    for cid in ids:
        try:
            raw = http_get(CC + "crawl-data/%s/cc-index-table.paths.gz" % cid, tries=3)
            paths = [l.strip() for l in gzip.decompress(raw).decode().split("\n") if "subset=warc/" in l and l.strip().endswith(".parquet")]
            if paths:
                return cid, sorted(paths)
        except Exception as e:
            print("index of %s not available: %s" % (cid, e), flush=True)
    sys.exit("no Common Crawl columnar index reachable")


def crawl_ids(spec):
    """'auto' -> [newest]; 'last:N' -> the newest N crawls (older captures hold pages the newest crawl missed); 'older:K:N' -> the N crawls after
    the newest K; 'id1,id2' -> those; otherwise the id given"""
    spec = (spec or "auto").strip()
    if "," in spec:  # 2026-11-13: an explicit list of crawl ids
        return [x.strip() for x in spec.split(",") if x.strip()]
    if spec.startswith("older:"):  # 2026-11-13: older:K:N = N crawls after the newest K (the newest K read before)
        try:
            k_, n_ = (int(x) for x in spec.split(":")[1:3])
            ids = [c["id"] for c in json.loads(http_get("https://index.commoncrawl.org/collinfo.json", tries=4))][k_:k_ + max(1, n_)]
            if ids:
                return ids
        except Exception as e:
            print("collinfo not reachable (%s): no older crawl read" % type(e).__name__, flush=True)
        return []
    if spec.startswith("last:"):
        try:
            ids = [c["id"] for c in json.loads(http_get("https://index.commoncrawl.org/collinfo.json", tries=4))][:max(1, int(spec.split(":")[1]))]
            if ids:
                return ids
        except Exception as e:
            print("collinfo not reachable (%s): only the newest crawl is read" % type(e).__name__, flush=True)
        return ["auto"]
    return [spec]


def shard_of(a):
    k, n = (a.shard.split("/") + ["1"])[:2] if a.shard else ("0", "1")
    return int(k), max(1, int(n))


def index(a):
    import duckdb
    k, n = shard_of(a)
    con = duckdb.connect()
    ver = tuple(int(x) for x in re.findall(r"\d+", duckdb.__version__)[:2])
    for st in ("INSTALL httpfs", "LOAD httpfs", "SET threads=4", "SET http_retries=8", "SET http_retry_wait_ms=2000",
               "SET http_timeout=%d" % (300 if ver >= (1, 1) else 300000), "SET enable_progress_bar=false"):
        try:
            con.execute(st)
        except Exception as e:
            print("duckdb setting skipped: %s (%s)" % (st, str(e)[:80]), flush=True)
    os.makedirs("out", exist_ok=True)
    rows, t0, shown = [], time.time(), False
    todo = []
    for spec in crawl_ids(a.crawl):
        try:
            cid, paths = newest_crawl(spec)
        except SystemExit as e:
            print("crawl %s skipped: %s" % (spec, e), flush=True)
            continue
        mine = paths[k::n]
        if a.limit_parts:
            mine = mine[:a.limit_parts]
        print("crawl %s: %d index parts, shard %d/%d reads %d" % (cid, len(paths), k, n, len(mine)), flush=True)
        todo += [(cid, i, len(mine), p) for i, p in enumerate(mine)]
    for cid, i, n_mine, p in todo:
        url = CC + p
        if not shown:
            try:
                cols = [r[0] for r in con.execute("DESCRIBE SELECT * FROM read_parquet('%s')" % url).fetchall()]
                print("index columns:", ", ".join(cols), flush=True)
            except Exception as e:
                print("describe failed:", str(e)[:300], flush=True)
            shown = True
        q = ("SELECT url, url_host_name, url_host_registered_domain, url_path, CAST(fetch_time AS VARCHAR), warc_filename, warc_record_offset, warc_record_length "
             "FROM read_parquet('%s') WHERE url_host_tld = 'ca' AND fetch_status = 200 AND content_mime_detected = 'text/html' AND url_query IS NULL "
             "AND length(url_path) BETWEEN 2 AND 90 AND ((regexp_matches(lower(url_path), '%s') AND NOT regexp_matches(lower(url_path), '%s')) "
             "OR (regexp_matches(lower(url_path), '%s') AND NOT regexp_matches(lower(url_path), '%s') AND length(regexp_extract(url_path, '[^/]+/?$')) <= 37) "
             "OR regexp_matches(lower(url_path), '%s') OR (regexp_matches(lower(url_path), '%s') AND NOT regexp_matches(lower(url_path), '%s')))") % (
                 url, REL_SQL.replace("'", "''"), NOT_SQL.replace("'", "''"), (SPONSOR_SQL + "|" + DEALER_SQL + "|" + TENANT_SQL).replace("'", "''"), NOT2_SQL.replace("'", "''"),
                 MEMBER_ONE_SQL.replace("'", "''"), MEMBER_SQL.replace("'", "''"), NOT3_SQL.replace("'", "''"))
        for attempt in range(3):
            try:
                got = con.execute(q).fetchall()
                rows += [tuple(r) + (cid,) for r in got]
                if got or i % 25 == 0:
                    print("%s %s part %d/%d: %d pages (total %d, %.0f s)" % (time.strftime("%H:%M:%S"), cid, i + 1, n_mine, len(got), len(rows), time.time() - t0), flush=True)
                break
            except Exception as e:
                print("part %d attempt %d failed: %s" % (i, attempt + 1, str(e)[:200]), flush=True)
                time.sleep(20 * (attempt + 1))
    by = collections.defaultdict(list)
    for r in rows:
        if r[2] and not VENDOR_SKIP.search(r[1] or ""):
            by[r[2]].append(r)
    with open("out/cc_rel_pages_%d.csv" % k, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(PAGE_COLS + ["crawl", "cls", "basis"])
        kept = 0
        for dom, rs in by.items():
            per = collections.Counter()
            seen_u = set()
            for r in sorted(rs, key=lambda r: (len(r[3] or ""), r[0], r[8])):
                c = page_class(r[3])
                c2 = "member1" if c == "member" and _M1_RX.search((r[3] or "").lower()) else c
                if not c or r[0] in seen_u or per[c2] >= (PER_DOMAIN_MEMBER_PAGES if c2 == "member1" else a.per_domain):
                    continue
                seen_u.add(r[0])
                per[c2] += 1
                w.writerow(list(r) + [c, ""])  # r ends with its crawl id; basis is empty for a .ca host (its domain + its own address)
                kept += 1
    print("shard %d: %d matching pages on %d .ca domains; kept %d (at most %d per domain)" % (k, len(rows), len(by), kept, a.per_domain), flush=True)


def index_u(a):
    """universe index: class pages AND home / contact pages of the non-.ca organisations the dataset locates in Canada (tools/ca_universe.py).
    One scan of the big top-level domains; the home / contact rows are kept for the address pass, so it never scans them again."""
    k, n = shard_of(a)
    uni = {}
    with open(a.universe, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            uni[r["dom"]] = r["basis"]
    os.makedirs("out", exist_ok=True)
    if not uni:
        print("empty universe", flush=True)
        return
    tlds = sorted({d.rsplit(".", 1)[-1] for d in uni if re.fullmatch(r"[a-z0-9.-]+", d)})
    con = _duck()
    con.execute("CREATE TEMP TABLE doms(d VARCHAR)")
    con.executemany("INSERT INTO doms VALUES (?)", [(d,) for d in sorted(uni)])
    rows, t0 = [], time.time()
    for spec in crawl_ids(a.crawl):
        try:
            cid, paths = newest_crawl(spec)
        except SystemExit as e:
            print("crawl %s skipped: %s" % (spec, e), flush=True)
            continue
        queue = list(enumerate(paths[k::n]))
        if a.limit_parts:
            queue = queue[:a.limit_parts]
        print("crawl %s: shard %d/%d reads %d index parts for %d organisations on %s" % (cid, k, n, len(queue), len(uni), ", ".join("." + t for t in tlds[:12])), flush=True)
        for rnd in range(5):
            if not queue:
                break
            if rnd:
                print("round %d: %d index parts to read again after a pause" % (rnd + 1, len(queue)), flush=True)
                time.sleep(60 * rnd + random.uniform(0, 30))
            nxt = []
            for i, p in queue:
                q = ("SELECT url, url_host_name, url_host_registered_domain, url_path, CAST(fetch_time AS VARCHAR), warc_filename, warc_record_offset, warc_record_length "
                     "FROM read_parquet('%s') WHERE url_host_tld IN (%s) AND url_host_registered_domain IN (SELECT d FROM doms) AND fetch_status = 200 "
                     "AND content_mime_detected = 'text/html' AND url_query IS NULL AND length(url_path) BETWEEN 1 AND 90 "
                     "AND ((regexp_matches(lower(url_path), '%s') AND NOT regexp_matches(lower(url_path), '%s')) "
                     "OR (regexp_matches(lower(url_path), '%s') AND NOT regexp_matches(lower(url_path), '%s')) "
                     "OR regexp_matches(lower(url_path), '%s') OR (regexp_matches(lower(url_path), '%s') AND NOT regexp_matches(lower(url_path), '%s')) "
                     "OR regexp_matches(lower(url_path), '%s'))") % (
                         CC + p, ", ".join("'%s'" % t for t in tlds), REL_SQL.replace("'", "''"), NOT_SQL.replace("'", "''"),
                         (SPONSOR_SQL + "|" + DEALER_SQL + "|" + TENANT_SQL).replace("'", "''"), NOT2_SQL.replace("'", "''"),
                         MEMBER_ONE_SQL.replace("'", "''"), MEMBER_SQL.replace("'", "''"), NOT3_SQL.replace("'", "''"), ADDR_PAGE_SQL.replace("'", "''"))
                try:
                    got = con.execute(q).fetchall()
                except Exception as e:
                    print("part %d failed (round %d): %s" % (i, rnd + 1, str(e)[:160]), flush=True)
                    nxt.append((i, p))
                    time.sleep(10)
                    continue
                rows += [tuple(r) + (cid,) for r in got]
                if got or i % 10 == 0:
                    print("%s %s part %d: %d pages (total %d, %.0f s)" % (time.strftime("%H:%M:%S"), cid, i, len(got), len(rows), time.time() - t0), flush=True)
            queue = nxt
        if queue:
            print("UNREAD index parts of %s after 5 rounds: %s" % (cid, ", ".join(str(i) for i, p in queue)), flush=True)
    by = collections.defaultdict(list)
    for r in rows:
        if r[2] in uni and not VENDOR_SKIP.search(r[1] or ""):
            by[r[2]].append(r)
    kept = kept_a = with_rel = 0
    with open("out/cc_rel_pages_%d.csv" % k, "a", newline="", encoding="utf-8") as f, open("out/cc_addr_pages_%d.csv" % k, "a", newline="", encoding="utf-8") as fa:
        w, wa = csv.writer(f), csv.writer(fa)
        if f.tell() == 0:
            w.writerow(PAGE_COLS + ["crawl", "cls", "basis"])
        if fa.tell() == 0:
            wa.writerow(APAGE_COLS)
        for dom, rs in by.items():
            per, seen_u, rel = collections.Counter(), set(), 0
            for r in sorted(rs, key=lambda r: (len(r[3] or ""), r[0], r[8])):
                c = page_class(r[3])
                c2 = "member1" if c == "member" and _M1_RX.search((r[3] or "").lower()) else c
                if not c or r[0] in seen_u or per[c2] >= (PER_DOMAIN_MEMBER_PAGES if c2 == "member1" else a.per_domain):
                    continue
                seen_u.add(r[0])
                per[c2] += 1
                w.writerow(list(r) + [c, uni[dom]])
                kept += 1
                rel += 1
            if not rel:
                continue  # no relationship page: its address is never needed
            with_rel += 1
            ad = [r for r in rs if not page_class(r[3]) and re.search(ADDR_PAGE_SQL, (r[3] or "/").lower())]
            for r in sorted(ad, key=lambda r: (0 if re.search(r"contact|joindre|coordonn", (r[3] or "").lower()) else 1, len(r[3] or ""), r[0]))[:4]:
                wa.writerow([dom, r[0], r[1], r[3], r[4], r[5], r[6], r[7], r[8]])
                kept_a += 1
    print("shard %d: %d matching pages on %d organisations; %d relationship pages kept on %d organisations, %d home / contact pages kept for the address pass" % (
        k, len(rows), len(by), kept, with_rel, kept_a), flush=True)


def warc_html(fn, off, ln):
    """(decoded page, "") from one range request, or (None, reason). The archive throttles busy clients (403 / 503 "SlowDown": two thirds of the
    first run's requests, 2026-11-10 00:47Z): those answers are retried with back-off, and an unreadable page is retried on a later cycle."""
    try:
        raw = http_get(CC + fn, headers={"Range": "bytes=%d-%d" % (off, off + ln - 1)}, timeout=60, tries=6, retry_http=(403, 429, 500, 502, 503, 504))
    except urllib.error.HTTPError as e:
        return None, "http%d" % e.code
    except Exception as e:
        return None, type(e).__name__
    try:
        rec = gzip.decompress(raw)
    except Exception:
        return None, "gzip"
    i = rec.find(b"\r\n\r\n")
    if i < 0:
        return None, "nowarc"
    resp = rec[i + 4:]
    j = resp.find(b"\r\n\r\n")
    if j < 0:
        return None, "nohttp"
    head, body = resp[:j].decode("latin-1", "replace"), resp[j + 4:]
    m = re.search(r"(?i)content-type:[^\r\n]*charset=[\"']?([\w-]+)", head)
    cs = m.group(1) if m else None
    if not cs:
        m2 = re.search(rb"(?i)<meta[^>]+charset=[\"']?([\w-]+)", body[:4000])
        cs = m2.group(1).decode("ascii", "replace") if m2 else "utf-8"
    try:
        text = body[:3_000_000].decode(cs, "replace")
    except LookupError:
        text = body[:3_000_000].decode("utf-8", "replace")
    return html.unescape(text), ""


def visible(page):
    t = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", page[:1_500_000])
    return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", t))


WEBSITE_LABEL = re.compile(r"^(?:visit (?:our |the )?(?:web ?site|site)|web ?site|site web|site internet|visiter le site(?: web)?|visitez le site(?: web)?|(?:https?://)?(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)+/?)$", re.I)


def member_page_hit(page, row, quote_of):
    """one-member page of a GrowthZone / ChamberMaster directory: (member name, its website host, the member's own address quote).
    The member's website is the single external link labelled as a website; the name is the page's <h1> (or the first part of <title>)."""
    vhost, dom = base(row["host"]), (row["dom"] or "").lower()
    sites = {}
    for href, label in anchors(page, row["url"]):
        try:
            h = base(urllib.parse.urlparse(href).hostname)
        except ValueError:
            continue
        label = (label or "").strip()
        if (not h or "." not in h or len(h) > 60 or h == vhost or h == dom or h.endswith("." + dom) or SKIP.search(h) or PLATFORMS.search(h) or VENDOR_SKIP.search(h)
                or re.search(r"growthzone|chambermaster|micronet", h) or not WEBSITE_LABEL.match(label)):
            continue
        sites.setdefault(h, href)
    if len(sites) != 1:
        return None
    h1 = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", page[:400_000])
    name = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", h1.group(1))).strip() if h1 else ""
    if not (2 <= len(name) <= 100):
        t = re.search(r"(?is)<title[^>]*>(.*?)</title>", page[:200_000])
        name = re.split(r"\s+[|–—-]\s+", re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", t.group(1))).strip())[0] if t else ""
    if not (2 <= len(name) <= 100) or GENERIC_LABEL.match(name):
        return None
    return name, next(iter(sites)), quote_of


def leads_of(page, row):
    """(hits, address quote). hits: one per linked organisation; the quote is the vendor's own Canadian postal address ('' when the page prints none)"""
    url, vhost, dom = row["url"], base(row["host"]), (row["dom"] or "").lower()
    text = visible(page)
    m = ADDR.search(text)
    quote = re.sub(r"^\S*\s", "", text[max(0, m.start() - 110):m.end()].strip())[-200:] if m else ""
    cls0 = row.get("cls") or page_class(row.get("path")) or "client"
    if cls0 == "member" and _M1_RX.search((row.get("path") or "").lower()):
        # a one-member page prints the MEMBER's address first; the body's own address is the last one on the page, and only when it is a
        # different postal code (otherwise the body's address is not on this page: the address pass reads it from the body's contact page)
        ms = list(ADDR.finditer(text))
        mq = quote
        quote = ""
        if len(ms) >= 2 and re.sub(r"[^A-Z0-9]", "", ms[-1].group(1).upper()) != re.sub(r"[^A-Z0-9]", "", ms[0].group(1).upper()):
            quote = re.sub(r"^\S*\s", "", text[max(0, ms[-1].start() - 110):ms[-1].end()].strip())[-200:]
        hit = member_page_hit(page, row, mq)
        if not hit:
            return [], quote
        name, h, mq = hit
        title = re.search(r"(?is)<title[^>]*>(.*?)</title>", page[:200_000])
        title = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", title.group(1))).strip()[:120] if title else ""
        site = re.search(r"(?is)<meta[^>]+property=[\"']og:site_name[\"'][^>]+content=(?:\"([^\"]{2,80})\"|'([^']{2,80})')", page[:200_000])
        return [{"platform": "vendor_site", "domain": h, "dataset_id": url, "dataset": CLASS_TEXT["member"], "dataset_url": url, "publisher": h, "buyer_unit": "", "website": "https://%s/" % h,
                 "vendor": (html.unescape(site.group(1) or site.group(2)).strip() if site else "") or vhost,
                 "canada_field": canada_field(dom, row.get("basis")), "canada_value": vhost,
                 "row": {"relationship_page": url, "page_title": title, "client_label": name[:120], "vendor_key": "cc:" + dom, "vendor_site": "https://%s/" % vhost, "pass": "cc_index", "basis": row.get("basis") or "",
                         "page_class": "member", "capture": (row.get("fetch_time") or "")[:19], "vendor_address_quote": quote, "member_address_quote": mq,
                         "warc": "%s:%s:%s" % (row["warc_filename"], row["warc_record_offset"], row["warc_record_length"])}}], quote
    title = re.search(r"(?is)<title[^>]*>(.*?)</title>", page[:200_000])
    title = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", title.group(1))).strip()[:120] if title else ""
    site = re.search(r"(?is)<meta[^>]+property=[\"']og:site_name[\"'][^>]+content=(?:\"([^\"]{2,80})\"|'([^']{2,80})')", page[:200_000])
    hits, n_spam = {}, 0
    vlabel = dom.split(".")[0]
    try:  # "Website by X" in the footer of a testimonials page: X is the page owner's web vendor (tools/credit_scan.py finds those the right way round)
        import credit_scan as _CS
        credited = {c["vh"] for c in _CS.find_credits(page, url)} | {c["v"] for c in _CS.find_credits(page, url)}
    except Exception:
        credited = set()
    for href, label in anchors(page, url):
        try:
            h = base(urllib.parse.urlparse(href).hostname)
        except ValueError:
            continue
        if h in credited:
            continue
        label = (label or "").strip()
        if COUNTRY_LABEL.match(label) or (len(vlabel) >= 4 and (h.split(".")[0] == vlabel or (len(vlabel) >= 6 and vlabel in h))):
            continue  # the organisation's own site in another country (rgis.pl on rgis.ca, catalystteambuilding.ng on catalystteambuilding.ca)
        n_spam += bool(h and h != vhost and (SPAM.search(h) or SPAM.search(label)))
        if (not h or "." not in h or len(h) > 60 or h == vhost or h == dom or h.endswith("." + dom) or re.fullmatch(r"[\d.]+", h)
                or SKIP.search(h) or PLATFORMS.search(h) or VENDOR_SKIP.search(h)
                or not label or len(label) > 120 or GENERIC_LABEL.match(label) or LABEL_SKIP.search(label) or SPAM.search(h) or SPAM.search(label)):
            continue
        hits.setdefault(h, {"platform": "vendor_site", "domain": h, "dataset_id": url, "dataset": CLASS_TEXT.get(row.get("cls") or page_class(row.get("path")) or "client", CLASS_TEXT["client"]),
                            "dataset_url": url, "publisher": h, "buyer_unit": "", "website": "https://%s/" % h, "vendor": (html.unescape(site.group(1) or site.group(2)).strip() if site else "") or vhost,
                            "canada_field": canada_field(dom, row.get("basis")), "canada_value": vhost,
                            "row": {"relationship_page": url, "page_title": title, "client_label": label[:120], "vendor_key": "cc:" + dom, "vendor_site": "https://%s/" % vhost,
                                    "pass": "cc_index", "basis": row.get("basis") or "", "page_class": row.get("cls") or page_class(row.get("path")) or "client", "capture": (row.get("fetch_time") or "")[:19], "vendor_address_quote": quote,
                                    "warc": "%s:%s:%s" % (row["warc_filename"], row["warc_record_offset"], row["warc_record_length"])}})
    if n_spam >= 3:
        return [], quote  # a hacked page: none of its links is taken
    if cls0 == "member" and len(hits) < MIN_MEMBER_LINKS:
        return [], quote  # a "members" page with a few stray links is a page FOR members (a church, a club), not a directory of member organisations
    if cls0 in ("sponsor", "dealer", "tenant") and len(hits) < MIN_LIST_LINKS:
        return [], quote
    return (list(hits.values()) if 0 < len(hits) <= (600 if cls0 == "member" else 150) else []), quote


def extract(a):
    k, n = shard_of(a)
    done, tries = set(), {}
    if os.path.exists(EXDONE):  # url, date, links, address(0/1), status, attempts — lines of the first run have 4 columns and no status
        for l in open(EXDONE, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            nh = int(q[2]) if len(q) > 2 and q[2].isdigit() else 0
            st = q[4] if len(q) > 4 else ("ok" if nh else "unknown")  # first-run lines with no link may have been unreadable: read them again once
            tries[q[0]] = int(q[5]) if len(q) > 5 and q[5].isdigit() else 1
            if st == "ok" or tries[q[0]] >= 4:
                done.add(q[0])
    pages = []
    with gzip.open(PAGES, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if r["url"] in done or int(hashlib.sha1((r["dom"] or r["host"]).encode()).hexdigest(), 16) % n != k:
                continue
            pages.append(r)
    random.Random(7).shuffle(pages)  # a time-boxed run samples all domains instead of one alphabetical slice
    if a.limit:
        pages = pages[:a.limit]
    os.makedirs("out", exist_ok=True)
    deadline = time.time() + a.minutes * 60
    stats = collections.Counter()
    fl = open("out/cc_leads_%d.jsonl" % k, "a", encoding="utf-8")
    fn = open("out/cc_leads_noaddr_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/cc_extract_done_%d.tsv" % k, "a", encoding="utf-8")
    import threading
    lock = threading.Lock()
    print("shard %d/%d: %d pages to read (%d done before)" % (k, n, len(pages), len(done)), flush=True)

    def one(r):
        if time.time() > deadline:
            return
        try:
            page, why = warc_html(r["warc_filename"], int(r["warc_record_offset"]), int(r["warc_record_length"]))
            hits, quote = leads_of(page, r) if page else ([], "")
        except Exception as e:
            page, why, hits, quote = None, "error:" + type(e).__name__, [], ""
        with lock:
            stats["pages"] += 1
            stats["unreadable"] += page is None
            if page is None:
                stats["fail:" + why] += 1
            stats["with_links"] += bool(hits)
            stats["with_address"] += bool(hits and quote)
            stats["leads"] += len(hits) if quote else 0
            stats["leads_noaddr"] += 0 if quote else len(hits)
            out = fl if quote else fn
            for h in hits:
                out.write(json.dumps(h, ensure_ascii=False) + "\n")
            fd.write("%s\t%s\t%d\t%d\t%s\t%d\n" % (r["url"], TODAY, len(hits), 1 if quote else 0, "ok" if page is not None else "unreadable:" + why, tries.get(r["url"], 0) + 1))
            if stats["pages"] % 500 == 0:
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, pages))
    for f in (fl, fn, fd):
        f.close()
    print("finished", dict(stats), flush=True)


ADDR_PAGE_SQL = (r"^/((en|fr|en-ca|fr-ca)/)?((contact|contacts|contact-us|contactez-nous|nous-joindre|nous-contacter|pour-nous-joindre|joindre|coordonnees|coordonn%c3%a9es"
                 r"|about|about-us|a-propos|%c3%a0-propos|qui-sommes-nous)[^/]{0,20}/?)?$")


def _duck():
    import duckdb
    con = duckdb.connect()
    ver = tuple(int(x) for x in re.findall(r"\d+", duckdb.__version__)[:2])
    for st in ("INSTALL httpfs", "LOAD httpfs", "SET threads=4", "SET http_retries=8", "SET http_retry_wait_ms=2000",
               "SET http_timeout=%d" % (300 if ver >= (1, 1) else 300000), "SET enable_progress_bar=false"):
        try:
            con.execute(st)
        except Exception as e:
            print("duckdb setting skipped: %s (%s)" % (st, str(e)[:80]), flush=True)
    return con


def _side_records():
    if os.path.exists(SIDE):
        for l in gzip.open(SIDE, "rt", encoding="utf-8"):
            if l.strip():
                try:
                    yield json.loads(l)
                except ValueError:
                    pass


def _vendor_addrs():
    """the address pass's results: {vendor domain: record}. A record read on a sub-site that is not the domain holder's own (see own_host) is
    left out — the address is that sub-site's body's; the domain then counts as still without an address and is read again on its own hosts."""
    out = {}
    if os.path.exists(VADDR):
        for l in gzip.open(VADDR, "rt", encoding="utf-8"):
            try:
                o = json.loads(l)
                if own_host((urllib.parse.urlparse(o.get("url") or "").hostname or o.get("host") or o["dom"]).lower(), o["dom"]):
                    out[o["dom"]] = o
            except (ValueError, KeyError):
                pass
    return out


def addr(a):
    """address pass: the vendors whose client page printed no postal address (two thirds of the client links found). Their home / contact /
    about page is read from the archive; a Canadian postal address printed there is the proof. Pages of non-.ca organisations were kept by
    the universe index (claude_cc_addr_pages.csv.gz); pages of .ca hosts are looked up in the index of the newest crawls."""
    k, n = shard_of(a)
    os.makedirs("out", exist_ok=True)
    found_now = set()  # domains this shard already read a page of (address found or not): older crawls are for the others
    deadline = time.time() + a.minutes * 60
    fa = open("out/cc_vendor_addr_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/cc_addr_done_%d.tsv" % k, "a", encoding="utf-8")
    # 1. stored home / contact pages (non-.ca organisations of the universe)
    if os.path.exists(APAGES):
        want = _addr_want("stored", found_now)
        pages = collections.defaultdict(list)
        with gzip.open(APAGES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                if r["dom"] in want and int(hashlib.sha1(r["dom"].encode()).hexdigest(), 16) % n == k:
                    pages[r["dom"]].append((r["url"], r["host"], r["dom"], r["path"], r["fetch_time"], r["warc_filename"], r["warc_record_offset"], r["warc_record_length"]))
        print("stored pages, shard %d/%d: %d organisations need an address, %d have a stored home / contact page in this shard" % (k, n, len(want), len(pages)), flush=True)
        _addr_read(a, pages, "stored", found_now, deadline, fa, fd)
    # 2. .ca hosts: the index of the newest crawls
    for spec in crawl_ids(a.crawl):
        try:
            cid, paths = newest_crawl(spec)
        except SystemExit as e:
            print("crawl %s skipped: %s" % (spec, e), flush=True)
            continue
        if time.time() < deadline:
            _addr_one_crawl(a, k, n, cid, paths, found_now, deadline, fa, fd)
    fa.close(); fd.close()


def _addr_want(cid, found_now):
    """vendor domains that still need an address and were not tried for this crawl ('stored' = the stored pages)"""
    have = _vendor_addrs()
    tried = set()
    if os.path.exists(ADONE):
        for l in open(ADONE, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) > 1 and q[1] == cid and not (len(q) > 3 and q[3] == "found" and q[0] not in have):
                tried.add(q[0])
    want = set()
    for o in _side_records():
        d = ((o.get("row") or {}).get("vendor_key") or "")[3:]
        if d and d not in have and d not in tried and d not in found_now and (d.endswith(".ca") != (cid == "stored")):
            want.add(d)
    return want


def _addr_read(a, pages, cid, found_now, deadline, fa, fd):
    """read each domain's pages (contact first, then home, then about) until one prints a Canadian postal address"""
    def order(r):
        path = (r[3] or "/").lower()
        return (0 if re.search(r"contact|joindre|coordonn", path) else 1 if re.fullmatch(r"/((en|fr|en-ca|fr-ca)/)?", path) else 2, len(path), (r[1] or "").startswith("www.") is False)
    stats = collections.Counter()
    import threading
    lock = threading.Lock()

    def one(dom):
        if time.time() > deadline:
            return
        found, n_read = None, 0
        own = [r for r in pages[dom] if own_host((r[1] or "").lower(), dom)]  # the holder's own hosts only (see own_host)
        if not own:  # pages on sub-sites only: nothing of the holder's own to read in this crawl
            with lock:
                stats["domains"] += 1
                stats["no page on the holder's own hosts"] += 1
                fd.write("%s\t%s\t%s\tno_own_page\t0\n" % (dom, cid, TODAY))
            return
        for r in sorted(own, key=order)[:4]:
            try:
                page, why = warc_html(r[5], int(r[6]), int(r[7]))
            except Exception as e:
                page, why = None, "error:" + type(e).__name__
            if page is None:
                continue
            n_read += 1
            text = visible(page)
            m = ADDR.search(text)
            if m:
                found = {"dom": dom, "host": base(r[1]), "url": r[0], "capture": (r[4] or "")[:19], "crawl": cid,
                         "quote": re.sub(r"^\S*\s", "", text[max(0, m.start() - 110):m.end()].strip())[-200:], "warc": "%s:%s:%s" % (r[5], r[6], r[7])}
                break
        with lock:
            stats["domains"] += 1
            stats["found"] += bool(found)
            stats["unreadable"] += n_read == 0
            if found:
                fa.write(json.dumps(found, ensure_ascii=False) + "\n")
            if n_read:
                found_now.add(dom)
            # an unreadable domain stays in the queue for the next run (merge-addr does not record that status)
            fd.write("%s\t%s\t%s\t%s\t%d\n" % (dom, cid, TODAY, "found" if found else "no_address" if n_read else "unreadable", n_read))
            if stats["domains"] % 500 == 0:
                fa.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, sorted(pages)))
    print("address pages read (%s): %s" % (cid, dict(stats)), flush=True)


def _addr_one_crawl(a, k, n, cid, paths, found_now, deadline, fa, fd):
    want = _addr_want(cid, found_now)
    print("crawl %s, shard %d/%d: %d .ca vendor domains need an address" % (cid, k, n, len(want)), flush=True)
    if not want:
        return
    con = _duck()
    con.execute("CREATE TEMP TABLE doms(d VARCHAR)")
    con.executemany("INSERT INTO doms VALUES (?)", [(d,) for d in sorted(want)])
    pages, t0 = collections.defaultdict(list), time.time()
    queue = list(enumerate(paths[k::n]))
    for rnd in range(5):
        if not queue:
            break
        if rnd:
            print("round %d: %d index parts to read again after a pause" % (rnd + 1, len(queue)), flush=True)
            time.sleep(60 * rnd + random.uniform(0, 30))
        nxt = []
        for i, p in queue:
            q = ("SELECT url, url_host_name, url_host_registered_domain, url_path, CAST(fetch_time AS VARCHAR), warc_filename, warc_record_offset, warc_record_length "
                 "FROM read_parquet('%s') WHERE url_host_tld = 'ca' AND fetch_status = 200 AND content_mime_detected = 'text/html' AND url_query IS NULL AND length(url_path) <= 45 "
                 "AND url_host_registered_domain IN (SELECT d FROM doms) AND regexp_matches(lower(url_path), '%s')") % (CC + p, ADDR_PAGE_SQL.replace("'", "''"))
            try:
                got = con.execute(q).fetchall()
            except Exception as e:
                print("part %d failed (round %d): %s" % (i, rnd + 1, str(e)[:160]), flush=True)
                nxt.append((i, p))
                time.sleep(10)
                continue
            for r in got:
                pages[r[2]].append(r)
            if got or i % 25 == 0:
                print("%s part %d: %d pages (domains with a page so far %d, %.0f s)" % (time.strftime("%H:%M:%S"), i, len(got), len(pages), time.time() - t0), flush=True)
        queue = nxt
    unread = len(queue)
    _addr_read(a, pages, cid, found_now, deadline, fa, fd)
    if not unread:  # every index part of this shard was read. A wanted domain is settled as "no page in this crawl" by merge-addr only when
        # ALL shards say so (a domain's pages sit in one index part, which may belong to any shard)
        open("out/cc_addr_complete_%d_%s.txt" % (k, cid), "w").write("%d/%d %s\n" % (k, n, cid))
        for d in sorted(d for d in want if d not in pages and int(hashlib.sha1(d.encode()).hexdigest(), 16) % n == k):
            fd.write("%s\t%s\t%s\tno_page_in_shard\t0\n" % (d, cid, TODAY))
    print("finished %s: %d domains had a page in this shard's index parts; unread index parts %d" % (cid, len(pages), unread), flush=True)


def merge_addr(a):
    have = _vendor_addrs()
    n0 = len(have)
    for f in sorted(glob.glob(os.path.join(a.dir, "cc_vendor_addr_*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                o = json.loads(l)
                if own_host((urllib.parse.urlparse(o.get("url") or "").hostname or o["dom"]).lower(), o["dom"]):  # a shard started before the rule
                    have.setdefault(o["dom"], o)
            except (ValueError, KeyError):
                pass
    if have:
        with gzip.open(VADDR, "wt", encoding="utf-8") as f:
            for d in sorted(have):
                f.write(json.dumps(have[d], ensure_ascii=False) + "\n")
    # a domain is "no page" for a crawl only when no shard found a page for it (each domain's pages sit in one index part)
    done, nopage = {}, collections.Counter()
    if os.path.exists(ADONE):
        for l in open(ADONE, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) >= 4:
                done[(q[0], q[1])] = l.rstrip("\n")
    marks = collections.defaultdict(set)  # crawl id -> shards that read every index part
    n_sh = 0
    for f in sorted(glob.glob(os.path.join(a.dir, "cc_addr_complete_*.txt"))):
        m = open(f).read().split()
        if len(m) >= 2:
            marks[m[1]].add(m[0])
            n_sh = int(m[0].split("/")[1])
    all_read_of = lambda cid: n_sh > 0 and len(marks.get(cid, ())) == n_sh
    seen_page, maybe_none = set(), []
    for f in sorted(glob.glob(os.path.join(a.dir, "cc_addr_done_*.tsv"))):
        for l in open(f, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) < 4:
                continue
            if q[3] == "no_page_in_shard":
                maybe_none.append(q)
                continue
            seen_page.add(q[0])
            if q[3] != "unreadable":
                done[(q[0], q[1])] = l.rstrip("\n")
    seen_page_c = set()
    for f in sorted(glob.glob(os.path.join(a.dir, "cc_addr_done_*.tsv"))):
        for l in open(f, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) >= 4 and q[3] != "no_page_in_shard":
                seen_page_c.add((q[0], q[1]))
    if True:
        for q in maybe_none:
            if all_read_of(q[1]) and (q[0], q[1]) not in seen_page_c and (q[0], q[1]) not in done:
                done[(q[0], q[1])] = "\t".join([q[0], q[1], q[2], "no_page", "0"])
    with open(ADONE, "w", encoding="utf-8") as f:
        for key in sorted(done):
            f.write(done[key] + "\n")
    st = collections.Counter(v.split("\t")[3] for v in done.values())
    print("address pass: %d vendor domains with an address on their own home / contact page (+%d this run); tried so far: %s" % (len(have), len(have) - n0, dict(st)))


def address_from(quote):
    """the address part of the quote: from the street number to the postal code (the whole quote when no street number is seen) — one
    implementation for every engine and for rank.py: tools/ap_crawler.py address_from"""
    import ap_crawler as _C
    return _C.address_from(quote)


def lead_key(domain):
    # the key tools/lead_scanner.py --bridge gives a vendor-site lead (publisher = the linked domain): the same buyer found by both gets one key
    return "lead:" + hashlib.sha1(("%s|%s" % (domain, domain.lower())).encode()).hexdigest()[:16]


def merge(a):
    d = a.dir
    recs = []
    for f in sorted(glob.glob(os.path.join(d, "cc_leads_[0-9]*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                recs.append(json.loads(l))
            except ValueError:
                pass
    # extraction progress
    seen = {}
    for f in [EXDONE] + sorted(glob.glob(os.path.join(d, "cc_extract_done_*.tsv"))):
        if os.path.exists(f):
            for l in open(f, encoding="utf-8"):
                p = l.rstrip("\n").split("\t")
                if p and p[0]:
                    seen[p[0]] = l.rstrip("\n")
    with open(EXDONE, "w", encoding="utf-8") as f:
        for u in sorted(seen):
            f.write(seen[u] + "\n")
    # side file: client links of .ca vendors whose page printed no address (kept for the address pass; never delivered from here)
    na = sorted(glob.glob(os.path.join(d, "cc_leads_noaddr_*.jsonl")))
    if na:
        side = SIDE
        have = set()
        if os.path.exists(side):
            have = set(gzip.open(side, "rt", encoding="utf-8").read().split("\n"))
        for f in na:
            have |= {json.dumps({k: v for k, v in json.loads(l).items() if k in ("domain", "dataset_url", "vendor", "canada_value", "row")}, ensure_ascii=False, sort_keys=True)
                     for l in open(f, encoding="utf-8") if l.strip()}
        have.discard("")
        with gzip.open(side, "wt", encoding="utf-8") as f:
            f.write("\n".join(sorted(have)) + "\n")
    known = set()
    main = os.path.join(INC, "claude_buyer_leads.csv")
    if os.path.exists(main):
        for r in csv.DictReader(open(main, encoding="utf-8", errors="replace")):
            known.add(r["buyer_key"])
            h = base(urllib.parse.urlparse(r.get("website") or "").hostname or "")
            if h:
                known.add(h)
    prev, pdet = {}, {}
    _stamp = getattr(a, "stamp", "") or ""
    if _stamp:
        # 2026-11-10 (tools/lead_store.py): the two files are a frozen base; the current state is base + shards, and this run writes only what it
        # changes as shards of lead_shards/ (the leads file was 58 MB and growing towards GitHub's 100 MB limit; the details file was stored whole
        # again at every merge). A run queued with the earlier workflow file passes no --stamp and writes the old files, as before.
        import lead_store as _LS
        _engine = getattr(a, "engine", "") or "cc"
        prev, pdet = _LS.load(exclude=(_engine, _stamp))
        _snap = _LS.snapshot(prev, pdet)
    else:
        if os.path.exists(LEADS_CC):
            prev = {r["buyer_key"]: r for r in csv.DictReader(open(LEADS_CC, encoding="utf-8"))}
        if os.path.exists(DETAILS_CC):
            for l in gzip.open(DETAILS_CC, "rt", encoding="utf-8"):
                try:
                    o = json.loads(l)
                    pdet[o["key"]] = o
                except (ValueError, KeyError):
                    pass
    # address pass: a client link whose vendor page printed no address becomes a lead once the vendor's own home / contact page gave one
    vaddr, promoted = _vendor_addrs(), 0
    _vlive, _page_ok = {}, None
    try:  # 2026-11-10: the vendor's own LIVE home / contact / legal page read by tools/credit_scan.py (postal address, schema.org address, or its
        # location line with a Canadian telephone number) — the archive had no contact page for 2,660 vendors and no postal code for 6,994
        import credit_scan as _CS
        _vlive, _page_ok = _CS.vendor_state(), _CS.proof_page_ok
        for vd_, o_ in _vlive.items():
            if vd_ not in vaddr and o_.get("status") in ("CA", "CA-loc") and o_.get("quote") and _page_ok(vd_, o_):
                vaddr[vd_] = {"dom": vd_, "quote": o_["quote"], "url": o_.get("url") or "", "capture": o_.get("date") or "", "live": o_["status"]}
    except Exception as e:
        print("live vendor proofs not loaded: %s" % e)
    side = list(_side_records())
    # whose address is it? (2026-11-11; see own_host / proof_fits) — the pages that name clients, per vendor domain: which sub-sites they sit on
    # (three or more named sub-sites = a domain that carries several bodies) and which path prefixes carry a body of their own
    _pages = [(((o.get("row") or {}).get("vendor_key") or "")[3:], o.get("dataset_url") or "", o.get("vendor") or "") for o in side]
    _pages += [(((r.get("row") or {}).get("vendor_key") or "")[3:], r.get("dataset_url") or "", r.get("vendor") or "") for r in recs]
    _pages += [(_reg(urllib.parse.urlparse(d.get("record_url") or "").hostname or ""), d.get("record_url") or "", d.get("vendor") or "")
               for d in pdet.values() if (d.get("platform") or "vendor_site_cc") == "vendor_site_cc"]
    _named = collections.defaultdict(set)
    for vd_, u_, _ in _pages:
        h_ = (urllib.parse.urlparse(u_).hostname or "").lower()
        if vd_ and h_ and not own_host(h_, vd_):
            _named[vd_].add(base(h_))
    several = {vd_ for vd_, hs in _named.items() if len(hs) >= 3}
    tenants = path_tenants(_pages)
    _seg = lambda u: (urllib.parse.urlparse(u or "").path or "/").strip("/").split("/")[0].lower()

    def whose(vd_, page_url, proof_url):
        """(ok, reason): is the address on proof_url this vendor's own? (the vendor's page page_url sits under the domain vd_)"""
        ok, why = proof_fits(vd_, page_url, proof_url, several)
        if ok is None:  # another domain: only a rename seen by the live check (the new site names the old one)
            o_ = _vlive.get(vd_) or {}
            ok = bool(_page_ok and o_.get("url") == proof_url and _page_ok(vd_, o_))
            why = "" if ok else "address read on another domain that is not shown to be the vendor's own"
        if ok and vd_ in tenants and _seg(page_url) in tenants[vd_] and proof_url and not (
                base(urllib.parse.urlparse(proof_url).hostname or "") == base(urllib.parse.urlparse(page_url).hostname or "") and _seg(proof_url) == _seg(page_url)):
            ok, why = False, "page of one of several bodies under path prefixes of one domain; the address is the domain holder's"
        return ok, why
    n_whose = collections.Counter()
    if vaddr:
        pages_of, link_pages = collections.defaultdict(set), collections.defaultdict(set)
        for o in side:
            vd_ = ((o.get("row") or {}).get("vendor_key") or "")[3:]
            pages_of[vd_].add(o.get("dataset_url"))
            link_pages[(vd_, o.get("domain"))].add(o.get("dataset_url"))
        n_boiler = 0
        for o in side:
            row = dict(o.get("row") or {})
            vd_ = (row.get("vendor_key") or "")[3:]
            va = vaddr.get(vd_)
            if not va or not o.get("domain") or not o.get("dataset_url") or MULTI_TENANT.search(vd_):
                continue
            if len(pages_of[vd_]) >= 3 and len(link_pages[(vd_, o["domain"])]) >= max(3, 0.6 * len(pages_of[vd_])):
                n_boiler += 1
                continue  # the same link on most pages of the site: its menu or footer (badges, partner networks), not a client named on a client page
            lab = (row.get("client_label") or "").strip()
            if COUNTRY_LABEL.match(lab) or LABEL_SKIP.search(lab) or (len(vd_.split(".")[0]) >= 4 and o["domain"].split(".")[0] == vd_.split(".")[0]):
                continue
            _ok, _why = whose(vd_, o["dataset_url"], va.get("url") or "")
            if not _ok:
                n_whose[_why] += 1
                continue
            row["vendor_address_quote"], row["vendor_address_url"], row["vendor_address_capture"] = va["quote"], va["url"], (va.get("capture") or "")[:10]
            row["vendor_address_how"] = va.get("live") or ""
            recs.append({"domain": o["domain"], "dataset_url": o["dataset_url"], "website": "https://%s/" % o["domain"], "vendor": o.get("vendor") or o.get("canada_value") or "",
                         "canada_field": canada_field(vd_, row.get("basis"), va.get("live") or ""), "canada_value": o.get("canada_value") or "", "row": row})
            promoted += 1
        if n_boiler:
            print("not promoted: %d links that sit on most pages of the vendor's site (menu / footer links)" % n_boiler)
        if n_whose:
            print("not promoted: %d links of vendors whose address on file is not shown to be their own (%s)" % (sum(n_whose.values()), "; ".join("%s: %d" % kv for kv in n_whose.most_common())))
    vendors_of = collections.defaultdict(set)
    for r in recs:
        vendors_of[r["domain"]].add(r["canada_value"])
    links_of_page = collections.Counter(r["dataset_url"] for r in recs)  # every organisation the page names, known or new
    new = 0
    cls_rank = lambda r: 0 if page_class(urllib.parse.urlparse(r["dataset_url"]).path) == "client" else 1  # a client page first, then member / dealer / sponsor pages
    for r in sorted(recs, key=lambda r: (cls_rank(r), len(r["dataset_url"]), r["dataset_url"])):
        dom = r["domain"]
        key = lead_key(dom)
        if len(vendors_of[dom]) > 15 or key in known or dom in known:
            continue
        row = r.get("row") or {}
        if key not in prev:
            new += 1
            prev[key] = {"buyer_key": key, "buyer_name": dom, "website": r["website"], "canadian_vendor_rows": 0, "example_vendor": r["vendor"],
                         "canada_field_value": "%s=%s" % (r["canada_field"], r["canada_value"]), "evidence_dataset": r["dataset_url"], "latest_record_date": ""}
            pdet[key] = {"key": key, "platform": "vendor_site_cc", "record_url": r["dataset_url"], "vendor": r["vendor"], "record_date": "", "title": "",
                         "vendor_address": ("%s (as printed on %s, %s %s)" % (address_from(row.get("vendor_address_quote")) if row.get("vendor_address_how") != "CA-loc" else "“%s”" % row.get("vendor_address_quote"),
                                                                             row.get("vendor_address_url") or r["dataset_url"], "read" if row.get("vendor_address_how") else "archive capture",
                                                                             row.get("vendor_address_capture") or (row.get("capture") or "")[:10])) if row.get("vendor_address_quote") else "",
                         "vendor_address_quote": row.get("vendor_address_quote") or "", "vendor_address_url": row.get("vendor_address_url") or r["dataset_url"],
                         "page_class": row.get("page_class") or page_class(urllib.parse.urlparse(r["dataset_url"]).path) or "client", "member_address_quote": row.get("member_address_quote") or "",
                         "page_links": links_of_page[r["dataset_url"]],
                         "vendor_site": row.get("vendor_site") or "", "client_label": row.get("client_label") or "", "page_title": row.get("page_title") or "", "capture": row.get("capture") or "", "warc": row.get("warc") or ""}
        prev[key]["canadian_vendor_rows"] = max(int(prev[key].get("canadian_vendor_rows") or 0), len(vendors_of[dom]))
    # member-list pages (not the one-member pages) that produced fewer than MIN_MEMBER_LINKS leads were pages FOR members, not directories
    # (first extraction 2026-11-10: a church's "members" page linking a facility-request form): their leads are withdrawn
    per_page = collections.Counter(d.get("record_url") for d in pdet.values() if d.get("page_class") in ("member", "sponsor", "dealer", "tenant"))
    # the rules below judge links read on a vendor's page: only this engine's own leads (platform vendor_site_cc). The file also holds the leads of
    # the credit / DNS scan and, read through the lead store, of every other engine — 2026-11-10: a test merge withdrew 10,748 licence leads because
    # they share one record_url (the register's address) and three holders' site names contained a "spam" word
    OWN = lambda d: (d.get("platform") or "vendor_site_cc") == "vendor_site_cc"
    is_spam = {k for k, d in pdet.items() if OWN(d) and (SPAM.search(d.get("client_label") or "") or SPAM.search(urllib.parse.urlparse((prev.get(k) or {}).get("website") or "").hostname or ""))}
    spam_page = collections.Counter(pdet[k].get("record_url") for k in is_spam)
    drop = [k for k, d in pdet.items() if OWN(d) and (k in is_spam or spam_page[d.get("record_url")] >= 3)]  # injected links, and every link of a hacked page (any class)
    for k, d in pdet.items():
        pc = d.get("page_class")
        if pc not in ("member", "sponsor", "dealer", "tenant") or not OWN(d) or k in is_spam or spam_page[d.get("record_url")] >= 3:
            continue
        path = urllib.parse.urlparse(d.get("record_url") or "").path.lower()
        n_links = max(int(d.get("page_links") or 0), per_page[d.get("record_url")])  # page_links counts the organisations already known too
        if (page_class(path) != pc  # the page no longer passes the path rule (article slugs, registration pages, distributor pages: rule tightened 2026-11-10)
                or (pc == "member" and not _M1_RX.search(path) and n_links < MIN_MEMBER_LINKS)
                or (pc != "member" and n_links < MIN_LIST_LINKS)):
            drop.append(k)
    # 2026-11-10 (row audit): (1) a "portfolio" page of an investor lists the companies it invested in, not clients; (2) a web agency named on
    # a vendor's client page is almost always that vendor's footer credit ("Website by …") — the agencies are known from the credit scan
    # (credited on the home pages of two or more other sites)
    try:
        import credit_scan as _CS
        _vn = collections.Counter(c["v"] for o in _CS.sightings().values() for c in (o.get("credits") or []))
    except Exception:
        _vn = collections.Counter()
    n_inv = n_cred = n_sis = 0
    for k, d in pdet.items():
        if d.get("platform") != "vendor_site_cc" or k in drop:
            continue
        _vl = base(urllib.parse.urlparse(d.get("vendor_site") or "").hostname or "").split(".")[0]
        _bh = base(urllib.parse.urlparse((prev.get(k) or {}).get("website") or "").hostname or "")
        _lab = (d.get("client_label") or "").strip()
        if COUNTRY_LABEL.match(_lab) or (_lab and LABEL_SKIP.search(_lab)) or (len(_vl) >= 4 and _bh.split(".")[0] == _vl):
            drop.append(k); n_sis += 1
            continue
        if (d.get("page_class") or "client") != "client":
            continue
        path = urllib.parse.urlparse(d.get("record_url") or "").path.lower()
        bdom = base(urllib.parse.urlparse((prev.get(k) or {}).get("website") or "").hostname or "")
        if "portfolio" in path and INVESTOR.search((d.get("page_title") or "") + " " + (d.get("vendor") or "")):
            drop.append(k); n_inv += 1
        elif bdom and _vn.get(bdom, 0) >= 2:
            drop.append(k); n_cred += 1
    if n_inv or n_cred or n_sis:
        print("withdrawn: %d companies listed in an investor's portfolio; %d web agencies named on a client page (footer credits of the page owner); %d country selectors, sister sites and badge links" % (n_inv, n_cred, n_sis))
    # whose address is it? (2026-11-11) — leads made before the rule: the address was read on a sub-site of another body, or the page is one of
    # several bodies' under one domain (see own_host / proof_fits / path_tenants)
    _dropped, n_w = set(drop), collections.Counter()
    for k, d in pdet.items():
        if d.get("platform") != "vendor_site_cc" or k in _dropped or not d.get("vendor_address_url") or not d.get("record_url"):
            continue
        vd_ = _reg(urllib.parse.urlparse(d["record_url"]).hostname or "")
        _ok, _why = whose(vd_, d["record_url"], d["vendor_address_url"]) if vd_ else (True, "")
        if not _ok:
            drop.append(k); n_w[_why] += 1
    if n_w:
        print("withdrawn: %d leads whose vendor address is not shown to be the vendor's own (%s)" % (sum(n_w.values()), "; ".join("%s: %d" % kv for kv in n_w.most_common())))
    for k in drop:
        prev.pop(k, None)
        pdet.pop(k, None)
    if drop:
        print("withdrawn: %d leads from pages that are not lists of paying parties (rule tightened), or spam links" % len(drop))
    if _stamp:
        _nu, _nd, _ng = _LS.save(_engine, _stamp, prev, pdet, _snap)
        print("lead shards of this run: %d rows, %d details, %d withdrawn" % (_nu, _nd, _ng))
    else:
        with open(LEADS_CC, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=LEAD_COLS)
            w.writeheader()
            for k in sorted(prev):
                w.writerow({c: prev[k].get(c, "") for c in LEAD_COLS})
        with gzip.open(DETAILS_CC, "wt", encoding="utf-8") as f:
            for k in sorted(pdet):
                f.write(json.dumps(pdet[k], ensure_ascii=False) + "\n")
    print("cc leads: %d link records read (%d of them through the address pass), %d new buyers, %d buyers in %s; pages read so far %d" % (len(recs), promoted, new, len(prev), os.path.basename(LEADS_CC), len(seen)))


def merge_index(a):
    rows, crawl = {}, ""
    for f in sorted(glob.glob(os.path.join(a.dir, "cc_rel_pages_*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if not r.get("url") or r["url"] == "url":
                continue  # a second header line (the .ca index and the universe index append to one shard file)
            rows[r["url"]] = r
            crawl = r.get("crawl") or crawl
    if not rows:
        sys.exit("no index rows in " + a.dir)
    by = collections.defaultdict(list)
    for r in rows.values():
        by[r["dom"]].append(r)
    n = 0
    cls_n = collections.Counter()
    if os.path.exists(PAGES):  # pages of an earlier scan (another crawl, or before a page class was added) stay: the archive still holds them
        with gzip.open(PAGES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                if r["url"] not in rows:
                    by[r["dom"]].append(r)
    ap_rows = {}
    if os.path.exists(APAGES):
        with gzip.open(APAGES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                ap_rows[r["url"]] = r
    n_ap0 = len(ap_rows)
    for f in sorted(glob.glob(os.path.join(a.dir, "cc_addr_pages_*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r.get("url") and r["url"] != "url":
                ap_rows.setdefault(r["url"], r)
    if ap_rows:
        with gzip.open(APAGES, "wt", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=APAGE_COLS, extrasaction="ignore")
            w.writeheader()
            for u in sorted(ap_rows):
                w.writerow(ap_rows[u])
        print("address pages of non-.ca organisations: %d (+%d)" % (len(ap_rows), len(ap_rows) - n_ap0))
    with gzip.open(PAGES, "wt", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=PAGE_COLS + ["crawl", "cls", "basis"], extrasaction="ignore")
        w.writeheader()
        for dom in sorted(by):
            per = collections.Counter()
            for r in sorted(by[dom], key=lambda r: (len(r["path"] or ""), r["url"])):
                c = r.get("cls") or page_class(r.get("path")) or "client"
                c2 = "member1" if c == "member" and _M1_RX.search((r.get("path") or "").lower()) else c
                if per[c2] >= (PER_DOMAIN_MEMBER_PAGES if c2 == "member1" else a.per_domain):
                    continue
                per[c2] += 1
                r["cls"] = c
                w.writerow(r)
                n += 1
                cls_n[c] += 1
    print("index %s: %d pages on %d domains (%d not .ca) (%s) -> %s" % (crawl, n, len(by), sum(1 for d in by if not d.endswith(".ca")), dict(cls_n), os.path.basename(PAGES)))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("index"); p.add_argument("--shard", default="0/1"); p.add_argument("--crawl", default="auto"); p.add_argument("--limit-parts", type=int, default=0); p.add_argument("--per-domain", type=int, default=6)
    p = sub.add_parser("index-u"); p.add_argument("--shard", default="0/1"); p.add_argument("--crawl", default="auto"); p.add_argument("--limit-parts", type=int, default=0)
    p.add_argument("--per-domain", type=int, default=6); p.add_argument("--universe", default="out/ca_universe.csv")
    p = sub.add_parser("merge-index"); p.add_argument("dir"); p.add_argument("--per-domain", type=int, default=6)
    p = sub.add_parser("extract"); p.add_argument("--shard", default="0/1"); p.add_argument("--minutes", type=float, default=120); p.add_argument("--workers", type=int, default=10); p.add_argument("--limit", type=int, default=0)
    p = sub.add_parser("merge"); p.add_argument("dir"); p.add_argument("--stamp", default="", help="write this run's changes as shards of lead_shards/ under this stamp (UTC YYYYMMDDTHHMMSS + a letter)")
    p.add_argument("--engine", default="cc", help="letters naming the workflow step that merges (rf, rfa, ml …): two steps never write the same shard file")
    p = sub.add_parser("addr"); p.add_argument("--shard", default="0/1"); p.add_argument("--crawl", default="last:3"); p.add_argument("--minutes", type=float, default=120); p.add_argument("--workers", type=int, default=4)
    p = sub.add_parser("merge-addr"); p.add_argument("dir")
    a = ap.parse_args()
    {"index": index, "index-u": index_u, "merge-index": merge_index, "extract": extract, "merge": merge, "addr": addr, "merge-addr": merge_addr}[a.cmd](a)


if __name__ == "__main__":
    main()
