#!/usr/bin/env python3
"""Dated private buyers from Canada-located vendors' own news releases. No AI.

A Canadian company's newsroom announces its deals: "<Buyer> selects <Vendor>", "<Vendor> wins contract with <Buyer>",
"<Vendor> to provide <Buyer> with ...", "<Buyer> choisit <Vendor>", "<Vendor> remporte un contrat de <Buyer>". Each such
release names a buyer, is dated, and is published by the vendor itself. For every vendor of the crawler's local lists
(batch903 verified vendors, batch904 OpenStreetMap, batch902 Wikidata, plus the Canada-HQ list of customer_stories.py):
  1. the sitemap (robots.txt lines, /sitemap.xml, indexes, gzip) and a few newsroom pages give the release URLs whose
     path is a news / press / media / blog address and whose slug carries a deal word;
  2. each release (newest first, at most 3 years old, at most --per-vendor) is read once: title, publication date
     (article meta, JSON-LD, <time>, or the URL), the text for the place line;
  3. the title is parsed in the right direction, so that the site owner is the seller and the other party the buyer.
     Financing, investment, grants, acquisitions, mergers, MOU / LOI, distribution / reseller deals, prizes and
     rankings are dropped;
  4. the buyer's website comes from a link in the release whose domain spells the buyer, else from Wikidata
     (tools/logo_sites.find_any). Buyers without a website are logged, not kept.
Vendor in Canada: the vendor list's own basis (contract data country field, Wikidata country, OpenStreetMap address,
Canada-HQ list). A vendor whose site is not .ca and comes from Wikidata / OpenStreetMap must also show a Canadian place
line in the release (a global group's newsroom is not its Canadian office's).
Output, picked up by tools/lead_scanner.py --bridge (row.news_date is the record date, so the lead counts as recent):
~/cch-leads/socrata_vnews_<I>.jsonl ; progress ~/cch-leads/socrata_vnews_<I>.jsonl.done ; no-website buyers
~/cch-leads/vnews_nosite_<I>.jsonl. Polite: robots.txt, one request per second per site, identified user agent.
  python3 tools/vendor_news.py --shard I --of N [--workers 24] [--per-vendor 25] [--limit N]
"""
import argparse, csv, datetime, hashlib, html, json, os, re, sys, threading, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL
from customer_stories import fetch_xml, VENDORS as HQ_VENDORS

TODAY = datetime.date.today()
OLDEST = (TODAY - datetime.timedelta(days=3 * 365)).isoformat()
NEWS_PATH = re.compile(r"/(news|newsroom|press|press-releases?|pressroom|media|media-centre|media-center|medias|blog|"
                       r"nouvelles|communiques?|communiques-de-presse|salle-de-presse|actualites?|annonces?|announcements?|"
                       r"releases?|stories|articles?|insights|updates|events?-news|investors?/news|news-releases?)(/|$)", re.I)
DEAL_SLUG = re.compile(r"select|chose|choos|chosen|award|wins?\b|-win-|won|signs?|signed|contract|order|renew|extends?|"
                       r"extension|deploy|adopt|implement|secur|lands?|taps?|picks?|retain|engag|provide|supply|deliver|"
                       r"choisi|retien|remport|contrat|commande|decroch|obtien|selection|octroi|mandat|entente|attribu|confi", re.I)
NOT_SLUG = re.compile(r"/(tag|category|categorie|author|auteur|page|feed|search|wp-json)/|\.(pdf|jpg|png|xml|zip)$", re.I)
DROP = re.compile(r"financ|credit facilit|\bloan|\bprêt|invest|raises?\b|funding|fund\b|grant|subvention|acqui|merger|"
                  r"\bmerge|fusion|\bmou\b|memorand|letter of intent|\bloi\b|lettre d.intention|distribut|reseller|resell|"
                  r"revendeur|dealer|franchis|\bprize|\bprix\b|lauréat|laureat|winner|finalist|ranked|ranking|\bbest\b|"
                  r"\btop \d|\btop\b|recogni|certif|named (a|one|to)|joins|appoint|nomm|hires|ceo|cfo|president|board|"
                  r"dividend|earnings|results|quarter|trimestr|webinar|conference|congrès|listing|ipo\b|shares|"
                  r"partnership|partenariat|partners with|s'associe|alliance|sponsor|donat|don\b|charit", re.I)
BAD_BUYER = re.compile(r"^(a|an|one|two|three|several|multiple|many|major|leading|large|global|top|undisclosed|"
                       r"confidential|unnamed|new|its|their|our|his|her|customers?|clients?|un|une|des|plusieurs|"
                       r"grand|important|nouveau|nouvelle|\d)\b", re.I)
VERB_B = (r"selects?|selected|chooses|chose|picks|picked|taps|tapped|awards?|awarded|renews?|renewed|extends?|extended|"
          r"expands?\s+(?:contract|agreement|deployment|use)\s+with|deploys?|deployed|adopts?|adopted|implements?|implemented|"
          r"standardi[sz]es\s+on|goes\s+live\s+with|signs?\s+with|signs?|signed|orders?(?:\s+from)?|ordered|contracts?\s+with|"
          r"engages?|engaged|hires|hired|retains?|retained|choisit|a\s+choisi|retient|a\s+retenu|s[ée]lectionne|"
          r"octroie|attribue|confie|accorde|renouvelle|commande")
TAIL_B = re.compile(r"^(?P<b>.+?)\s+(?:" + VERB_B + r")(?:\s+(?:a|an|the|new|its|un|une|le|la|son|sa|\$?[\d.,]+\s*(?:m|million|b|billion|k)?|"
                    r"multi-?year|\d+-year|five-year|three-year|pluriannuel|major|large|second|additional|follow-on))*"
                    r"(?:\s+(?:contract|agreement|deal|order|purchase\s+order|mandate|contrat|entente|commande|mandat|"
                    r"march[ée]))?\s*(?:to|with|from|à|a|avec|au|aux)?$", re.I)
HEAD_V = [
    re.compile(r"^(?:has\s+been\s+|was\s+|is\s+|gets\s+|a\s+été\s+|est\s+)?(?:selected|chosen|picked|retained|tapped|contracted|"
               r"engaged|hired|awarded\s+.{0,60}?|choisie?s?|s[ée]lectionn[ée]e?s?|retenue?s?|mandat[ée]e?s?)\s+(?:by|par)\s+(?P<b>.+)$", re.I),
    re.compile(r"^(?:\w+\s+){0,2}?(?:wins?|won|secures?|secured|lands?|landed|signs?|signed|receives?|received|is\s+awarded|"
               r"awarded|obtains?|books?|inks?|bags?|captures?|clinches?|renews?|renewed|extends?|extended|expands?|"
               r"remporte|obtient|d[ée]croche|signe|conclut|re[çc]oit|renouvelle|prolonge)\b(?P<what>.{0,90}?)\b"
               r"(?:contracts?|orders?|agreements?|deal|award|mandate|tender|contrats?|commandes?|ententes?|mandats?|march[ée]s?|"
               r"appel\s+d.offres)(?:\s+[^\s]+){0,6}?\s+(?:with|from|by|avec|de|du|de\s+la|des|auprès\s+de|aupres\s+de|par|pour\s+le\s+compte\s+de)\s+"
               r"(?P<b>.+)$", re.I),
    re.compile(r"^(?:to|will|selected\s+to|chosen\s+to)\s+(?:provide|supply|deliver|equip|power|support|serve|build|design|"
               r"upgrade|modernize|modernise|digitize|digitise|outfit|furnish)\s+(?P<b>.+?)\s+with\b", re.I),
    re.compile(r"^(?:and|et)\s+(?P<b>.+?)\s+(?:sign|ink|conclude|signent|concluent)\w*\s+(?:a\s+|an\s+|une?\s+)?"
               r"(?:\S+\s+){0,3}?(?:contract|order|supply|services?\s+agreement|purchase|contrat|commande)", re.I),
]
CUT = re.compile(r"\s+(?:to|for|in|on|at|as|after|valued|worth|totaling|totalling|of\s+(?:\$|up|over|more)|under|through|"
                 r"via|pour|afin|dans|en\s|d.une\s+valeur|de\s+\d|d.une|following|amid|across)\b.*$|\s*[(\[–—:;,|!?].*$|\s+-\s.*$", re.I)
CANADA_LINE = re.compile(r"\b(TORONTO|MONTR[ÉE]AL|VANCOUVER|CALGARY|OTTAWA|EDMONTON|WINNIPEG|QU[ÉE]BEC|HALIFAX|VICTORIA|"
                         r"REGINA|SASKATOON|MISSISSAUGA|WATERLOO|KITCHENER|MARKHAM|BURLINGTON|OAKVILLE|LAVAL|GATINEAU|"
                         r"SHERBROOKE|LONDON,\s*ON|HAMILTON|MONCTON|FREDERICTON|ST\.?\s*JOHN.?S|CHARLOTTETOWN|WHITEHORSE|"
                         r"YELLOWKNIFE|IQALUIT|KELOWNA|SURREY|BURNABY|RICHMOND,\s*BC|LONGUEUIL|BROSSARD|BOUCHERVILLE|"
                         r"TROIS-RIVI[ÈE]RES|SAGUENAY|L[ÉE]VIS|[A-Z][A-Za-z.' -]{2,30},\s*(?:ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NT|NU|"
                         r"Ont\.?|Qu[ée]\.?|B\.C\.|Alta\.?|Man\.?|Sask\.?|N\.S\.|N\.B\.|Ontario|Qu[ée]bec|British Columbia|Alberta|"
                         r"Manitoba|Saskatchewan|Nova Scotia|New Brunswick|Newfoundland|Prince Edward Island|Canada))\b[^.\n]{0,60}?"
                         r"(?:20\d\d|/CNW/|/PRNewswire/|Newswire|GLOBE NEWSWIRE|–|—|-)")
BASIS = {"v": "contract data: vendor country Canada", "osm": "OpenStreetMap office in Canada",
         "wd": "Wikidata: country Canada", "hq": "Canada-headquartered company list"}
lock = threading.Lock()
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()
squash = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower())
LEGAL = re.compile(r"\b(inc|incorporated|ltd|limited|ltee|ltée|corp|corporation|co|company|llc|plc|sa|s a|gmbh|ag|group|"
                   r"groupe|holdings?|canada|technologies|technology|solutions|systems|international)\b\.?", re.I)


def vendor_names(v, host):
    """Strings that name the site owner in a title: its list name (with and without legal words) and its domain label."""
    out = []
    n = norm(v.get("buyer_name"))
    if len(n) >= 3:
        out.append(n)
        short = norm(LEGAL.sub(" ", n))
        if len(short) >= 4 and short != n:
            out.append(short)
    label = host.split(".")[0]
    if len(label) >= 3 and label.isalpha() or len(label) >= 4:
        out.append(label)
    return list(dict.fromkeys(out))


def find_vendor(title, names):
    """(start, end) of the first mention of the vendor in the title (word bounded, case-insensitive), else None."""
    t = title.lower()
    best = None
    for n in names:
        if " " not in n:  # the domain label: also matches "Geotab's" or "MDA Space" spelt together ("mdaspace")
            m = re.search(r"\b" + re.escape(n) + r"(?:'s|’s)?\b", t) or re.search(r"\b" + r"\s*".join(map(re.escape, n)) + r"\b", t)
        else:
            m = re.search(r"\b" + r"[\s\W]+".join(map(re.escape, n.split())) + r"(?:\s*(?:inc|ltd|corp|limited|ltée|ltee)\.?)?\b", t)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), m.end())
    return best


def clean_buyer(b):
    b = html.unescape(b or "").strip(" '\"“”‘’.")
    b = CUT.sub("", b).strip(" '\"“”‘’.,")
    b = re.sub(r"^(the|la|le|les|l')\s*", "", b, flags=re.I).strip()
    b = re.sub(r"(?:'s|’s)$", "", b)
    if not b or len(b) > 80 or len(b.split()) > 9 or BAD_BUYER.match(b) or not re.search(r"[A-Za-zÀ-ÿ]{2}", b):
        return ""
    if b == b.lower() and not re.search(r"[A-Z]", b):  # a buyer is a proper name
        return ""
    return b


def parse(title, names):
    """(buyer, relation) when the title says the site owner sells to a named buyer, else None."""
    if DROP.search(title) or re.search(r"of the year|honou?r|accolade", title, re.I) or (
            re.search(r"\bawards?\b|\bprix\b", title, re.I) and not re.search(r"contract|order|tender|contrat|commande", title, re.I)):
        return None  # prizes and rankings, not deals
    span = find_vendor(title, names)
    if not span:
        return None
    left, right = title[:span[0]].strip(" -–—:|\"“”"), title[span[1]:]
    right = re.sub(r"^(?:'s|’s)?[\s\"“”,]*(?:(?:inc|ltd|corp|limited|ltée|ltee)\.?,?\s+)?", "", right, flags=re.I).strip(" -–—:|")
    if left and not re.match(r"^(?:news|press release|communiqu[ée]|update)$", left, re.I):
        m = TAIL_B.match(left)
        if m:
            return clean_buyer(m.group("b")), "buyer_selects_vendor"
        return None
    for i, rx in enumerate(HEAD_V):
        m = rx.match(right)
        if m:
            return clean_buyer(m.group("b")), ("selected_by", "contract_with", "to_provide", "joint_signature")[i]
    return None


def page_date(page, url):
    for rx in (r"(?is)<meta[^>]+(?:property|name|itemprop)\s*=\s*[\"'](?:article:published_time|datePublished|pubdate|"
               r"publish[-_]?date|date|dc\.date|dcterms\.date|og:published_time|sailthru\.date|parsely-pub-date)[\"'][^>]*?"
               r"content\s*=\s*[\"']([^\"']+)",
               r"(?is)<meta[^>]+content\s*=\s*[\"']([^\"']+)[\"'][^>]+(?:property|name|itemprop)\s*=\s*[\"'](?:article:published_time|datePublished)[\"']",
               r"(?is)\"datePublished\"\s*:\s*\"([^\"]+)\"", r"(?is)<time[^>]*datetime\s*=\s*[\"']([^\"']+)"):
        m = re.search(rx, page[:600_000])
        if m:
            d = re.search(r"(20\d\d)-(\d\d)-(\d\d)", m.group(1))
            if d:
                return "-".join(d.groups())
    m = re.search(r"/(20\d\d)/(\d\d)/(?:(\d\d)/)?", url)
    if m:
        return "%s-%s-%s" % (m.group(1), m.group(2), m.group(3) or "01")
    return ""


def page_title(page):
    for rx in (r"(?is)<meta[^>]+property\s*=\s*[\"']og:title[\"'][^>]+content\s*=\s*[\"']([^\"']+)",
               r"(?is)<h1[^>]*>(.*?)</h1>", r"(?is)<title[^>]*>(.*?)</title>"):
        m = re.search(rx, page[:600_000])
        if m:
            t = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", html.unescape(m.group(1)))).strip()
            t = re.split(r"\s+[|•·]\s+|\s+[-–—]\s+(?=[^-–—]{0,40}$)", t)[0].strip()  # drop " | Site name" / " - Site name"
            if len(t) >= 15:
                return t[:300]
    return ""


def body_text(page):
    page = re.sub(r"(?is)<(script|style|nav|header|footer|noscript)[^>]*>.*?</\1>", " ", page[:1_500_000])
    m = re.search(r"(?is)<(article|main)[^>]*>(.*?)</\1>", page)
    t = re.sub(r"(?s)<[^>]+>", " ", m.group(2) if m else page)
    return re.sub(r"\s+", " ", html.unescape(t))


def buyer_site(buyer, page, final, vhost):
    """A link in the release whose domain spells the buyer (its name, its squashed name or its acronym), else Wikidata."""
    words = [w for w in norm(LEGAL.sub(" ", buyer)).split() if w not in ("of", "the", "de", "du", "des", "la", "le", "and", "et")]
    sq, acr = squash(" ".join(words)), "".join(w[0] for w in words)
    for href, label in CL.anchors(page, final):
        h = CL.base(urllib.parse.urlparse(href).hostname)
        if not h or h == vhost or h.endswith("." + vhost) or CL.SKIP.search(h) or "." not in h:
            continue
        lab = squash(h.split(".")[-2] if h.count(".") >= 1 else h)
        if len(lab) >= 4 and (lab in sq or (len(sq) >= 5 and sq in lab)) or (len(acr) >= 3 and lab == acr):
            return "https://%s/" % h, "link in the release"
    for name in dict.fromkeys([buyer, re.sub(r"[\s,]+(inc|incorporated|ltd|limited|llc|plc|corp|corporation|s\.?a\.?|ag|gmbh|ltée|ltee)\.?$", "", buyer, flags=re.I)]):
        try:
            hit = wikidata_site(name)
        except Exception:
            hit = None
        if hit:
            return hit[0], "Wikidata %s" % hit[1]
    return "", ""


def wikidata_site(name):
    """Official website of the Wikidata item whose label or alias is exactly the buyer's name, in any country (a release
    names its customer precisely; customers abroad count). A one-word name counts only when the website's domain spells it."""
    import site_finder_quick as SF
    n = SF.norm(name)
    if len(n) < 4:
        return None
    res = SF.get({"action": "wbsearchentities", "search": name, "language": "en", "limit": 7, "type": "item"}).get("search", [])
    ids = [x["id"] for x in res if SF.norm(x.get("label")) == n or SF.norm((x.get("match") or {}).get("text")) == n]
    if not ids:
        return None
    ents = SF.get({"action": "wbgetentities", "ids": "|".join(ids[:5]), "props": "claims"}).get("entities", {})
    for qid in ids:
        c = (ents.get(qid) or {}).get("claims", {})
        sites = [(x["mainsnak"].get("datavalue") or {}).get("value") for x in c.get("P856", [])]
        if not sites or not sites[0]:
            continue
        host = (urllib.parse.urlparse(sites[0]).hostname or "").lower()
        if len(n.split()) >= 2 or n.replace(" ", "") in host.replace("-", ""):
            return sites[0], qid
    return None


def news_urls(site, cap):
    """Release URLs from the sitemaps (newest first by lastmod / URL date) and from a few newsroom pages."""
    found = {}
    robots = fetch_xml(urllib.parse.urljoin(site, "/robots.txt"), 300_000) or ""
    queue = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", robots) + [urllib.parse.urljoin(site, p) for p in
            ("/sitemap.xml", "/sitemap_index.xml", "/news-sitemap.xml", "/post-sitemap.xml")]
    seen, readable = set(), 0
    while queue and len(seen) < 25:
        sm = queue.pop(0)
        if sm in seen or not CL.allowed(sm):
            continue
        seen.add(sm)
        txt = fetch_xml(sm)
        if not txt or "<" not in txt[:500]:
            continue
        readable += 1
        index = "<sitemapindex" in txt[:3000].lower()
        for blk in re.findall(r"(?is)<(?:url|sitemap)>(.*?)</(?:url|sitemap)>", txt):
            loc = re.search(r"<loc>\s*([^<\s]+)\s*</loc>", blk)
            if not loc:
                continue
            loc = html.unescape(loc.group(1))
            lm = re.search(r"<(?:lastmod|news:publication_date)>\s*(20\d\d-\d\d-\d\d)", blk)
            if index or loc.endswith((".xml", ".xml.gz")) or ".xml?" in loc:
                if re.search(r"news|press|post|media|blog|actualit|nouvell|communiq|release|article", loc, re.I):
                    if not (lm and lm.group(1) < OLDEST):
                        queue.insert(0, loc)
                elif len(queue) < 40 and not re.search(r"product|produit|image|video|categor|tag|author|page-sitemap", loc, re.I):
                    queue.append(loc)
                continue
            path = urllib.parse.urlparse(loc).path
            if NEWS_PATH.search(path) and DEAL_SLUG.search(path.rsplit("/", 2)[-1] or path) and not NOT_SLUG.search(path):
                d = lm.group(1) if lm else ""
                u = re.search(r"/(20\d\d)/(\d\d)/", path)
                d = d or ("%s-%s-01" % u.groups() if u else "")
                if not d or d >= OLDEST:
                    found[loc.split("#")[0]] = d
    if not readable:  # no usable sitemap: deal-titled links on the newsroom pages (/news, /press ...)
        vhost = CL.base(urllib.parse.urlparse(site).hostname)
        for p in ("news", "newsroom", "press", "media", "nouvelles"):
            u = urllib.parse.urljoin(site, "/" + p)
            if not CL.allowed(u):
                continue
            page, final = CL.fetch(u)
            if not page:
                continue
            for href, label in CL.anchors(page, final):
                pu = urllib.parse.urlparse(href)
                if CL.base(pu.hostname) == vhost and NEWS_PATH.search(pu.path) and (DEAL_SLUG.search(pu.path.rsplit("/", 2)[-1])
                        or DEAL_SLUG.search(label)) and not NOT_SLUG.search(pu.path) and len(pu.path) > len(p) + 8:
                    found.setdefault(href.split("#")[0], "")
            if len(found) >= cap:
                break
    best = {}
    for u, d in found.items():  # one URL per release across language copies, English first
        p = urllib.parse.urlparse(u).path
        m = re.match(r"^/([a-z]{2}(?:[-_][a-zA-Z]{2})?)(/.*)$", p)
        loc, rest = (m.group(1).lower(), m.group(2)) if m else ("", p)
        rank = 0 if loc in ("", "en", "en-us", "en-ca") else 1
        k = rest.rstrip("/").lower()
        if k not in best or rank < best[k][0]:
            best[k] = (rank, d, u)
    return [u for _, d, u in sorted(best.values(), key=lambda x: x[1], reverse=True)][:cap]


def one(v, out, nosite, done, cap, stats):
    site = (v.get("known_website") or "").strip()
    if not site.startswith("http") or site in done:
        return
    vhost = CL.base(urllib.parse.urlparse(site).hostname)
    basis = v["buyer_key"].split(":")[0]
    names = vendor_names(v, vhost)
    rows, nos = [], []
    try:
        urls = news_urls(site, cap) if CL.allowed(site) else []
    except Exception:
        urls = []
    for u in urls:
        if not CL.allowed(u):
            continue
        page, final = CL.fetch(u)
        if not page:
            continue
        title = page_title(page)
        sn = re.search(r"(?is)<meta[^>]+property\s*=\s*[\"']og:site_name[\"'][^>]+content\s*=\s*[\"']([^\"']{3,60})", page[:300_000])
        pnames = names + [n for n in (norm(sn.group(1)) if sn else "", norm(LEGAL.sub(" ", sn.group(1))) if sn else "") if len(n) >= 3]
        hit = parse(title, list(dict.fromkeys(pnames))) if title else None
        if not hit or not hit[0]:
            continue
        buyer, relation = hit
        d = page_date(page, final)
        if not d or d < OLDEST or d > TODAY.isoformat():
            continue
        text = body_text(page)
        place = CANADA_LINE.search(text[:1500])
        place = place.group(0)[:160] if place else ""
        if basis in ("wd", "osm") and not vhost.endswith(".ca") and not place:
            stats["no_canada_line"] += 1
            continue
        if squash(buyer) in squash(" ".join(pnames)) or any(squash(n) in squash(buyer) for n in pnames if len(n) >= 4):
            continue  # the vendor itself (its subsidiary, its own brand)
        web, how = buyer_site(buyer, page, final, vhost)
        lead = {"title": title, "news_date": d, "relation": relation, "quote": title[:300], "place_line": place,
                "vendor_key": v["buyer_key"], "vendor_site": site, "vendor_canada_basis": BASIS.get(basis, basis),
                "buyer_site_basis": how, "retrieved": TODAY.isoformat()}
        if not web:
            nos.append({"buyer": buyer, "vendor": vhost, "page": final, "row": lead})
            continue
        h = CL.base(urllib.parse.urlparse(web).hostname)
        if not h or h == vhost or h.endswith("." + vhost):
            continue
        rows.append({"platform": "vendor_news", "domain": h, "dataset_id": final,
                     "dataset": "deal announced in a Canada-located vendor's own news release", "dataset_url": final,
                     "publisher": buyer, "buyer_unit": "", "website": "https://%s/" % h,
                     "vendor": v.get("buyer_name") or vhost, "canada_field": "own news release of the vendor (%s)" % basis,
                     "canada_value": place or vhost, "row": lead})
    with lock:
        if rows:
            with open(out, "a", encoding="utf-8") as f:
                for r in {r["domain"]: r for r in rows}.values():
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        if nos:
            with open(nosite, "a", encoding="utf-8") as f:
                for r in nos:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        with open(out + ".done", "a", encoding="utf-8") as f:
            f.write("%s\t%d\t%d\n" % (site, len(urls), len(rows)))
        stats["vendors"] += 1; stats["releases"] += len(urls); stats["leads"] += len(rows); stats["nosite"] += len(nos)
        if stats["vendors"] % 200 == 0:
            print("%s %s" % (datetime.datetime.now().strftime("%H:%M"), dict(stats)), flush=True)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--shard", type=int, default=0)
    a.add_argument("--of", type=int, default=1)
    a.add_argument("--workers", type=int, default=24)
    a.add_argument("--per-vendor", type=int, default=25)
    a.add_argument("--limit", type=int, default=0)
    a = a.parse_args()
    os.makedirs(CL.LEADS, exist_ok=True)
    out = os.path.join(CL.LEADS, "socrata_vnews_%02d.jsonl" % a.shard)
    nosite = os.path.join(CL.LEADS, "vnews_nosite_%02d.jsonl" % a.shard)
    done = set(l.split("\t")[0] for l in open(out + ".done", encoding="utf-8")) if os.path.exists(out + ".done") else set()
    vendors, seen = [], set()
    hq = [{"buyer_key": "hq:" + h, "buyer_name": "", "known_website": "https://www.%s/" % h} for h in dict.fromkeys(HQ_VENDORS)]
    lists = [os.path.expanduser("~/cch-crawler/coord/tasks/claude/claude_buyer_ap_batch90%d.csv" % n) for n in (3, 4, 2)]
    for rows in [hq] + [csv.DictReader(open(f, encoding="utf-8-sig")) for f in lists if os.path.exists(f)]:
        for r in rows:
            h = CL.base(urllib.parse.urlparse(r.get("known_website") or "").hostname)
            if h and h not in seen and int(hashlib.sha1(h.encode()).hexdigest(), 16) % a.of == a.shard:
                seen.add(h)
                vendors.append(r)
    if a.limit:
        vendors = vendors[:a.limit]
    print("shard %d: %d vendor sites (%d done before)" % (a.shard, len(vendors), len(done)), flush=True)
    import collections
    stats = collections.Counter()
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda v: one(v, out, nosite, done, a.per_vendor, stats), vendors))
    print("shard %d finished %s" % (a.shard, dict(stats)), flush=True)


if __name__ == "__main__":
    main()
