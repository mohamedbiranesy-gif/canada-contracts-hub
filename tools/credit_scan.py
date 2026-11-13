#!/usr/bin/env python3
"""Credit scan (cloud): the relationship an organisation prints on its OWN home page — "Website by <agency>", "Site web réalisé par …",
"Hébergé par …", "Powered by …" — with a link to the vendor. When the vendor's own site prints a Canadian postal address, that is a
Canada-located vendor that was paid by the organisation, stated by the paying party itself, read live and dated.

Why (owner 2026-11-09 20:48 EST: "a Canadian entity gets paid because it provided a service … establish that relationship, get the other
party's contact"): 50,355 of the 64,539 delivered rows are tier I — an organisation with a confirmed mailbox and only an INFERRED
relationship. One request to each organisation's home page turns many of them into a relationship with evidence, and the same scan over
every .ca site in Common Crawl's index finds new buyers. Nothing here uses AI or a search engine.

  universe --shard K/N        every .ca registered domain with a captured page (Common Crawl columnar index) -> out/ca_domains_<K>.csv
  merge-universe DIR          -> data/incoming/claude/credit_scan/ca_domains.csv.gz
  scan --shard K/N            one polite read of each site's home page (robots.txt respected, identified user agent): credit links and the
                              vetted Canada-HQ software services (tools/tech_relationships.py) -> out/credit_seen_<K>.jsonl, out/credit_done_<K>.tsv
  vendors --shard K/N         each credited vendor's own home / contact page: its postal address (the Canada proof), its own name
                              -> out/credit_vendors_<K>.jsonl
  merge DIR --stamp S         shard outputs -> append-only files in data/incoming/claude/credit_scan/ (done_, seen_, vendors_<S>), then
                              leads: every sighting whose vendor is proven in Canada -> claude_buyer_leads_cc.csv + claude_lead_details_cc.jsonl.gz
                              (tools/lead_crawl.py then reads the buyer's site for its role mailbox; the referee re-fetches that page), and the
                              vetted-service sightings -> claude_tenant_candidates.csv.gz (tools/lead_crawl.py --candidates accepts or rejects)
Scan order: delivered rows (their relationship is upgraded), then leads, then the .ca universe (sites with the most captured pages first).

What counts as a credit (find_credits): an <a> to another organisation's domain whose own text, or the text right before it, is a service
credit. Three classes — W: a web noun is in the phrase ("website by", "site web par", "hébergé par", "web design by"): accepted anywhere on
the page; D: a design verb alone ("designed by", "conception :", "une réalisation de"): only in the footer zone; P: "powered by" /
"propulsé par": only in the footer zone, vendors with a free plan excluded. Sponsors, donors, hosts of events, themes, photo credits,
"developed by" / "built by" without a web noun (real-estate developers, builders) are not credits.
"""
import argparse, collections, csv, glob, gzip, hashlib, html, io, json, os, random, re, sys, threading, time, urllib.error, urllib.parse, urllib.request, urllib.robotparser

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402
import cc_clients as CCL  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "credit_scan")
UNIVERSE = os.path.join(DIR, "ca_domains.csv.gz")
TODAY = time.strftime("%Y-%m-%d")
CF_CREDIT = "service of a Canada-located vendor credited on the buyer's own site (tech)"  # "(tech)": rank.py files it as a service seen on the buyer's own site
PLATFORM = re.compile(r"(^|\.)(blogspot|wordpress|wixsite|weebly|squarespace|myshopify|godaddysites|webflow|github|tumblr|substack|jimdo|site123|webself|wix|godaddy|google|facebook|"
                      r"instagram|twitter|linkedin|youtube|pinterest|tiktok|apple|microsoft|amazon|cloudflare|shopify|w3|gravatar|automattic|woocommerce|elementor|bootstrap|jquery|"
                      r"mailchimp|hubspot|paypal|stripe|yelp|tripadvisor|eventbrite|vimeo|flickr|whatsapp|adobe|bit|goo|t|x|canada|gc)\.[a-z.]{2,8}$", re.I)
# Canada-based services with a free plan or no charge to the organisation: a "powered by" line is not proof of a payment
# (2026-11-10 review of the first 25,510 credit leads: Webador is a Dutch site builder with a free plan whose badge sits on 438 sites; Ratehub's
# rate widget is free for the site; the DirectAdmin licence is paid by the server operator, not by the site that shows its default page)
FREE_PLAN = re.compile(r"(^|\.)(webself\.net|zeffy\.com|thinkific\.com|vidyard\.com|wattpad\.com|fundrazr\.com|hootsuite\.com|wealthsimple\.com|canva\.com|linktr\.ee|carrd\.co|"
                       r"wildapricot\.(com|org)|cyberimpact\.com|canadahelps\.org|gofundme\.com|tithe\.ly|webador\.[a-z.]{2,6}|jouwweb\.[a-z]{2,3}|ratehub\.ca|directadmin\.com|"
                       r"elasticemail\.com|medimap\.ca|eventbrite\.ca|kijiji\.ca|"
                       # server software whose licence the hosting company pays, not the site that shows its default page ("Powered by cPanel"):
                       # cPanel's legal page lists a Vancouver affiliate, which made it a "Canadian vendor" linked from 91,892 domains
                       r"cpanel\.net|cpanel\.com|plesk\.com|webpros\.com|whmcs\.com|softaculous\.com|cloudlinux\.com|litespeedtech\.com|directadmin\.com|"
                       r"presscustomizr\.com)$", re.I)
# "Hosting: PlanetHoster, 4416 Louis B Mayer, Laval, Quebec" in a legal notice is the HOST's address, not the site owner's (legal notices in the
# French tradition must name the host): an address introduced by such a label is never the vendor's own
HOST_LABEL = re.compile(r"(?:(?:h[ée]bergeur|h[ée]bergement|hosting(?:\s+provider)?|web\s?host|\bhost)\s*(?::|[-–])|h[ée]berg[ée]e?s?\s+(?:par|chez)\b|hosted\s+(?:by|at|with|on)\b)[^.;]{0,90}$", re.I)
# a university's or school board's own web service credited by one of its units ("This website is powered by MacSites"): an internal service, no vendor
INTERNAL_RX = re.compile(r"\buniversit|\bcoll[èe]ges?\b|c[ée]gep|polytechni|school (?:board|district|division)|commission scolaire|centre de services scolaire|conseil scolaire", re.I)
# hosts of a vendor's own domain that are the vendor's pages; any other subdomain may be a customer's site (free-4409244.webador.ca printed a customer's address)
_COUNTRY_WORD = (r"(?:France|Germany|Deutschland|India|M[ée]xico|Netherlands|Nederland|Belgium|Belgique|Spain|Espa[ñn]a|Italy|Italia|Switzerland|Suisse|Schweiz|Ireland|Sweden|Singapore|"
                 r"Japan|China|Hong Kong|Brazil|Brasil|Israel|Dubai|UAE|United Arab Emirates|Saudi Arabia|Kuwait|Qatar|South Africa|Poland|Denmark|Norway|Finland|Austria|Portugal|"
                 r"New Zealand|Philippines|Pakistan|Bangladesh|Sri Lanka|Malaysia|Indonesia|Vietnam|Thailand|Nigeria|Kenya|Egypt|T[üu]rkiye|Colombia|Argentina|Chile|Peru|Ukraine|"
                 r"Romania|Bulgaria|Greece|Cyprus|Malta|Luxembourg|Estonia|Latvia|Lithuania|Czech(?:ia| Republic)|Hungary)")
_US_STATE = (r"(?:Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|"
             r"Massachusetts|Michigan|Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|"
             r"Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming)")
_NANP_PLUS = re.compile(r"\+\(?\d{3}\)?[\s.\-]?\d{3}[\s.\-]?\d{4}\b")  # a North American number written "+604-600-2377": not a country code
_INTL_PHONE = re.compile(r"\(?\+(?:2\d|3\d|4\d|5\d|6\d|7|8\d|9\d)\d?\)?[ \d(.)\-]{6,}")
_OFFICE_ABROAD = re.compile(r"\b%s\b(?=[\s,:;–—\-]{0,3}\d|.{0,60}?\b(?:office|branch|bureau|headquarters|HQ)\b)|\b\d{4,6},?\s+%s\b" % (_COUNTRY_WORD, _COUNTRY_WORD), re.I)
_US_IN_QUOTE = re.compile(r"\b%s,?\s+\d{5}(?:-\d{4})?\b|\b\d{5}(?:-\d{4})?,?\s+(?:USA|U\.S\.A\.?|United States)\b" % _US_STATE)


def offices_abroad(quote):
    """country codes of the offices outside Canada that an address quote itself shows — "Pakistan … BRANCH OFFICE CANADA", "France 50 rue
    Breteuil 13006 Marseille +33…", "Fountain Hills, Arizona 85268, USA Vancouver 580 Hornby Street" (US = a state name with a ZIP code; XX =
    another country named next to an address, a telephone number with a country code other than +1). Service-area sentences ("serving Canada
    and the United States") and neighbourhood names ("Little Italy, Toronto") are not offices."""
    q = quote or ""
    out = set()
    if _US_IN_QUOTE.search(q):
        out.add("US")
    if _INTL_PHONE.search(_NANP_PLUS.sub(" ", q)) or _OFFICE_ABROAD.search(q):
        out.add("XX")
    return out
OWN_SUB = re.compile(r"^(www\d?|support|help|aide|site|get|go|terms|legal|about|contact|info|docs|corp|corporate|company|home|web|en|fr|ca|global|group|groupe)$", re.I)
FREE_SIGNAL = re.compile(r"free plan|free forever|forever free|always free|create (?:a|your) free (?:web)?site|free website builder|build (?:a|your) free website|forfait gratuit|plan gratuit|"
                         r"site (?:web |internet )?gratuit|cr[ée]ez? (?:votre|un) site (?:web )?gratuit|\$\s?0\s*/\s*(?:mo|month)|0\s?\$\s*/\s*mois", re.I)

# ------------------------------------------------------------------------------------------------------------------- credit phrases
_WEBN = (r"(?:web\s?sites?|web\s?pages?|sites?\s?web|sites?\s+internet|pages?\s+web|web\s?design|web\s?development|web\s?hosting|web\s?marketing|design\s+web|"
         r"d[ée]veloppement\s+web|conception\s+web|h[ée]bergement(?:\s+web)?|h[ée]berg[ée]e?s?|r[ée]f[ée]rencement|seo|webmaster|webmestre|sites?|web)")
_DESN = (r"(?:design(?:ed)?|crafted|handcrafted|hand-crafted|coded|programmed|engineered|con[çc]u(?:e|s|es)?|conception|r[ée]alis[ée](?:e|s|es)?|r[ée]alisation|cr[ée]ation|"
         r"programmation|programm[ée](?:e|s|es)?|marketing|branding)")
_WEAK = (r"(?:develop(?:ed|ment)|built|created?|made|hosted|hosting|maintained|maintenance|cr[ée][ée](?:e|s|es)?|d[ée]velopp[ée](?:e|s|es)?|d[ée]veloppement|fait)")
_POW = r"(?:powered|propuls[ée](?:e|s|es)?)"
_HEAD = "(?:%s|%s|%s|%s)" % (_WEBN, _DESN, _WEAK, _POW)
_JOIN = r"(?:\s*(?:and|&|\+|et|,|/|-|–)\s*|\s+)"
_FILL = r"(?:graphique|internet|num[ée]rique|digital|du\s+site|de\s+site|de\s+ce\s+site|of\s+this\s+site|this\s+site|ce\s+site|is|was|est|a\s+[ée]t[ée])"
_WITH = (r"(?:(?:with|avec)\s+[^\s<>]{1,14}(?:\s+(?:and|&|et)\s+[^\s<>]{1,14})?\s+|proudly\s+|lovingly\s+|fi[èe]rement\s+|in\s+[A-Z][A-Za-zÀ-ÿ.\-]{2,20}(?:,?\s+[A-Z][A-Za-zÀ-ÿ.\-]{1,20})?\s+)")
_PH_BY = _HEAD + "(?:" + _JOIN + "(?:" + _HEAD + "|" + _FILL + "))*" + r"\s*(?:" + _WITH + r"){0,2}(?:by|par)(?![A-Za-zÀ-ÿ])"
_PH_COLON = (r"(?:web\s?design|design|conception|r[ée]alisation|cr[ée]ation|d[ée]veloppement|development|h[ée]bergement|hosting|programmation|webmaster|webmestre)"
             + "(?:" + _JOIN + "(?:" + _HEAD + "|" + _FILL + "))*" + r"\s*:")
_PH_DE = r"(?:une\s+)?(?:r[ée]alisation|cr[ée]ation|conception)(?:\s+web)?\s+(?:de\s+l['’][ée]quipe(?:\s+de)?|de|d['’]|sign[ée]e(?:\s+par)?)(?![A-Za-zÀ-ÿ])"
_PHRASE = "(?:" + _PH_BY + "|" + _PH_COLON + "|" + _PH_DE + ")"
BEFORE_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])(" + _PHRASE + r")[\s:\-–—|»›>]{0,6}(?:(?:the\s+(?:team|folks)\s+at|l['’][ée]quipe\s+(?:de|chez)|our\s+friends\s+at)[\s|]*)?$", re.I)
INNER_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])(" + _PHRASE + r")\s*(?!e-?mail|courriel|courrier|email|sms|t[ée]l[ée]phone)\S", re.I)  # not "marketing par e-mail" (a newsletter badge)
WEBN_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])" + _WEBN + r"(?![A-Za-zÀ-ÿ])", re.I)
DESN_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])" + _DESN + r"(?![A-Za-zÀ-ÿ])", re.I)
POW_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])" + _POW + r"(?![A-Za-zÀ-ÿ])", re.I)
WITH_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])(?:with|avec)\s+\S", re.I)
MAKE_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])(?:made|built|created|fait|cr[ée][ée]e?)(?![A-Za-zÀ-ÿ])", re.I)
# words right before / inside the phrase that make it something else than a service the organisation paid for
NEG_RX = re.compile(r"donat|sponsor|courtesy|gracieuset|offert|commandit|pro\s?bono|volunteer|b[ée]n[ée]vol|themes?\b|th[èe]mes?\b|templates?|gabarit|plugin|ic[oô]n|fonts?\b|polices?\b|photo|image|"
                    r"illustrat|vid[ée]o|map\b|carte\b|musi[cq]|recipe|recette|article|post\b|billet|written|[ée]crit|review|produit|product|collection|furniture|meuble|homes?\b|maisons?\b|condos?|"
                    r"project|projet|communit|communaut|building|immeuble|tower|tour\b|event|[ée]v[èé]nement|festival|concert|show|spectacle|tournament|tournoi|award|prix|study|[ée]tude|report|rapport", re.I)
# membership stated by the member itself: "Proud member of the Calgary Chamber of Commerce" (text or the alt text of a badge) linked to the body.
# Class M. Not: team / board / staff members of …, "a member of the X group of companies" (the body must be a chamber, association, federation …).
MEM_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])((?:(?:proud(?:ly)?|fi[èe]re?s?|active|actif|accredited|accr[ée]dit[ée]e?|certified|registered|corporate|business)\s+){0,2}(?:members?|membres?)\s+"
                    r"(?:of|de|du|des|de\s+la|de\s+l['’]|d['’])\s*(?:(?:the|la|le|les|l['’]|your|our|votre|notre)\s*)?)", re.I)
MEM_NEG = re.compile(r"team|board(?!\s+of\s+trade)|staff|family|famil|crew|band|cast|faculty|committee|comit[ée]|council\s+member|conseil\s+d|founding|honorary|community\s+member|"
                     r"parliament|parlement|legislat|assembl[ée]e\s+nationale|\bMPP?\b|\bMLA\b|\bMNA\b|d[ée]put[ée]|[ée]quipe|personnel|group\s+of\s+companies|groupe\s+d['’]entreprises", re.I)
BODY_RX = re.compile(r"chamber|chambre|board\s+of\s+trade|association|alliance|federation|f[ée]d[ée]ration|institute|institut\b|guild|\bordre\b|corporation\s+des|regroupement|r[ée]seau|"
                     r"society\s+of|soci[ée]t[ée]\s+(?:de|des|canadienne|qu[ée]b[ée]coise)|business\s+improvement|\bBIA\b|\bSDC\b|tourism|tourisme|\bCHBA\b|\bAPCHQ\b|\bACQ\b|\bCFIB\b|\bFCEI\b|"
                     r"home\s+builders|landscape\s+(?:ontario|alberta|nova)|destination\s+\w+|\bcouncil\s+of\b|conseil\s+(?:du|de\s+la|des|canadien|qu[ée]b[ée]cois)|coalition|consortium|co-?op[ée]rative\s+de|union\s+des", re.I)
A_RX = re.compile(r"<a\b([^>]*)>(.*?)</a\s*>", re.I | re.S)
HREF_RX = re.compile(r"""\bhref\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>"']+))""", re.I)
ATTR_RX = re.compile(r"""\b(?:alt|title|aria-label)\s*=\s*(?:"([^"]*)"|'([^']*)')""", re.I)
DROP_RX = re.compile(r"<(script|style|noscript)\b.*?</\1\s*>|<!--.*?-->", re.I | re.S)
TAG_RX = re.compile(r"<[^>]*>")


BLOCK_RX = re.compile(r"</?(?:p|div|li|ul|ol|td|tr|th|table|section|footer|header|nav|aside|h[1-6]|br|hr|form|address|small)\b[^>]*>", re.I)


def vis(s, sep=False):
    """visible text of a piece of HTML that may start or end in the middle of a tag or a script; sep: block boundaries become " | " """
    for end in ("</script>", "</style>", "</noscript>", "-->"):
        i = s.lower().rfind(end)
        if i >= 0 and "<script" not in s[i:].lower() and "<style" not in s[i:].lower():
            s = s[i + len(end):]
    i, j = s.find(">"), s.find("<")
    if i >= 0 and (j < 0 or i < j):
        s = s[i + 1:]
    i, j = s.rfind("<"), s.rfind(">")
    if i >= 0 and i > j:
        s = s[:i]
    s = DROP_RX.sub(" ", s)
    if sep:
        s = BLOCK_RX.sub(" | ", s)
    s = TAG_RX.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()


CLAUSE_RX = re.compile(r"[|·•.©®™–—:;,()!?\[\]/]|\s-\s|\d{4}")


def phrase_class(ph, ctx):
    """W / D / P ('' = not a service credit). ctx: the text before the phrase; only the clause the phrase belongs to is tested
    ("Theme designed by", "This project was built by"), never the organisation's own name in the copyright line before it."""
    clause = CLAUSE_RX.split(ctx)[-1][-40:]
    if NEG_RX.search(clause + " " + ph):
        return ""
    if WEBN_RX.search(ph):
        return "W"
    if DESN_RX.search(ph):
        return "D"
    if POW_RX.search(ph):
        return "P"
    return "D" if WITH_RX.search(ph) and MAKE_RX.search(ph) else ""  # "made with love by", "built with care by" (an agency's signature), never "hosted with … by"


def find_credits(raw, page_url):
    """[{v: vendor registrable domain, vh: vendor host, k: W|D|P, q: quote (<= 300 chars), t: the link's own text}] — one per vendor domain"""
    site = C.registrable((urllib.parse.urlparse(page_url).hostname or "").lower())
    raw = raw[:1_500_000]
    low = raw.lower()
    foot = low.rfind("<footer")
    zone = min(foot if foot >= len(raw) * 0.5 else len(raw), int(len(raw) * 0.8))  # the footer zone: from the last <footer> (when it sits in the second half), at most the last 20 %
    out = {}
    for m in A_RX.finditer(raw):
        h = HREF_RX.search(m.group(1))
        if not h:
            continue
        href = (h.group(1) or h.group(2) or h.group(3) or "").strip()
        if not href.lower().startswith(("http://", "https://", "//")):
            continue
        try:
            host = (urllib.parse.urlparse(urllib.parse.urljoin(page_url, href)).hostname or "").lower()
        except ValueError:
            continue
        host = host[4:] if host.startswith("www.") else host
        if not host or "." not in host:
            continue
        v = C.registrable(host)
        if v == site or PLATFORM.search(v):
            continue
        inner = m.group(2)
        attrs = " ".join(a or b for a, b in ATTR_RX.findall(m.group(1) + " " + inner))
        itxt = vis(inner)
        label = (itxt or attrs).strip()[:120]
        before = vis(raw[max(0, m.start() - 700):m.start()], sep=True)[-200:]
        ph, cls, where = "", "", ""
        mb = BEFORE_RX.search(before)
        if mb:
            ph, cls, where = mb.group(1), phrase_class(mb.group(1), before[:mb.start()]), "before"
        if not cls:
            for cand in (itxt, attrs):
                mi = INNER_RX.search(cand or "")
                if mi:
                    ph, cls, where = mi.group(1), phrase_class(mi.group(1), (cand or "")[:mi.start()]), "inner"
                    if cls:
                        label = (cand or "").strip()[:120]
                        break
        if not cls:  # no service credit: a membership statement?
            mm = re.search(MEM_RX.pattern + r"[\s|]*$", before, re.I)
            if mm and not MEM_NEG.search(before[max(0, mm.start() - 30):] + " " + label) and BODY_RX.search(label):
                ph, cls, where = mm.group(1), "M", "before"
            else:
                for cand in (attrs, itxt):
                    mi = MEM_RX.search(cand or "")
                    if mi and not MEM_NEG.search(cand) and BODY_RX.search(cand[mi.end():]):
                        ph, cls, where, label = mi.group(1), "M", "inner", cand.strip()[:160]
                        break
        if not cls:
            continue
        if ph.rstrip().endswith(":") and re.fullmatch(r"(?:https?://)?(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)+/?\S*", label.strip().lower()):
            continue  # "Design: https://…" in a list of resources is an address, not a credit
        label = label or "[link to %s]" % host  # a logo without alt text: the link target names the vendor
        if cls in ("D", "P") and m.start() < zone:
            continue  # a bare "designed by" / "powered by" outside the footer zone is usually about a product, not about the site
        q = (before[-150:] + " " + label) if where == "before" else label
        q = re.sub(r"\s+", " ", re.sub(r"(?:\s*\|\s*)+", " | ", q)).strip(" |")[-300:]
        cur = out.get(v)
        if cur is None or "WDPM".index(cls) < "WDPM".index(cur["k"]):
            out[v] = {"v": v, "vh": host, "k": cls, "q": q, "t": label, "p": re.sub(r"\s+", " ", ph).strip()[:80]}
    return list(out.values())


# ------------------------------------------------------------------------------------------------------------------- fetching
def decode(data, ctype):
    m = re.search(r"charset=([\w-]+)", ctype or "", re.I)
    enc = m.group(1) if m else ""
    if not enc:
        mb = re.search(rb"<meta[^>]+charset=[\"']?([\w-]+)", data[:4000], re.I)
        enc = mb.group(1).decode("ascii", "replace") if mb else "utf-8"
    try:
        return data.decode(enc, "replace")
    except LookupError:
        return data.decode("utf-8", "replace")


FAST_TIMEOUT = 10
_PLAIN = {}  # host -> the address prefix that answered when https://host/ did not ("http://host", "https://www.host", "http://www.host"): asked directly from then on


def _fast_one(url, limit, tried):
    """(status, content type, bytes, final url, the address that was asked last)"""
    req = urllib.request.Request(url, headers={"User-Agent": C.UA, "Accept-Language": "fr-CA,fr;q=0.9,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=FAST_TIMEOUT) as r:
            return r.status, r.headers.get("content-type", ""), r.read(limit), r.geturl(), url
    except urllib.error.HTTPError as e:
        return e.code, "", b"", url, url
    except Exception as ex:
        msg, p = str(ex).lower(), urllib.parse.urlparse(url)
        host = p.hostname or ""
        if "temporary failure" in msg and "again" not in tried:
            time.sleep(1.5)
            return _fast_one(url, limit, tried + ("again",))
        if any(k in msg for k in ("nodename", "name or service", "getaddrinfo", "no address", "temporary failure")):
            if "www" not in tried and host and not host.startswith("www."):
                return _fast_one(url.replace("://" + host, "://www." + host, 1), limit, tried + ("www",))  # bare host without a DNS record, www. has one
            return 0, "", b"", url, url
        if p.scheme == "https" and "http" not in tried:
            return _fast_one("http://" + url[8:], limit, tried + ("http",))  # closed or silent port 443, broken TLS: the plain-http copy is the same public page
        return 0, "", b"", url, url


def fast_fetch(url, limit=1_500_000):
    """(status, content type, bytes, final url) for the scan: each site is met once, so no per-host waiting list; a 10-second timeout, because
    a list of a million domains holds many that no longer answer (ap_crawler.fetch waits 20 s and keeps a growing table of hosts).
    When https://host/ does not answer (2026-11-10, measured on 5,000 domains the scan had called unreachable: 1,005 answered, 691 of them on
    plain http only — port 443 silent 299, reset 130, refused 105, broken TLS 157): the plain-http copy is asked once, whatever the failure;
    a name without an address is asked once as www.; a resolver's "try again" is asked again once. The address that answered is remembered
    for the host, so its next page (robots.txt first, then the home page) does not wait for the dead port again."""
    p0 = urllib.parse.urlparse(url)
    if p0.scheme == "https" and p0.hostname in _PLAIN:
        return _fast_one(_PLAIN[p0.hostname] + url[8 + len(p0.netloc):], limit, ("http", "www"))[:4]
    st, ctype, data, final, asked = _fast_one(url, limit, ())
    if st and asked != url and p0.scheme == "https" and p0.hostname and len(_PLAIN) < 2_000_000:
        pa = urllib.parse.urlparse(asked)
        _PLAIN[p0.hostname] = "%s://%s" % (pa.scheme, pa.netloc)
    return st, ctype, data, final


_fetch = C.fetch  # the vendor step reads several pages of one site: ap_crawler's polite fetch (one request per second per host); the scan switches to fast_fetch


def robots_ok(root, url, cache=None):
    """(allowed, reachable). No shared cache: a scan meets each host once — a caller that reads several pages of one site passes its own
    `cache` dict, and the site's robots file is read once for all of them."""
    if cache is not None and root in cache:
        rp = cache[root]
    else:
        st, _, data, _ = _fetch(root + "robots.txt", 300_000)
        rp = True
        if st in (401, 403):
            rp = False
        elif st == 0:
            rp = None
        elif st == 200 and data:
            rp = urllib.robotparser.RobotFileParser()
            try:
                rp.parse(data.decode("utf-8-sig", "replace").splitlines())
            except Exception:
                rp = True
        if cache is not None:
            cache[root] = rp
    if rp is None:
        return True, False
    if rp is True or rp is False:
        return rp, True
    try:
        return rp.can_fetch(C.UA, url), True
    except Exception:
        return True, True


def get_page(url, check_robots=True, cache=None):
    """(status word, final url, html) — status: ok | robots | unreachable | blocked | http_<code> | not_html"""
    p = urllib.parse.urlparse(url)
    root = "%s://%s/" % (p.scheme, p.netloc)
    if check_robots:
        ok, reach = robots_ok(root, url, cache)
        if not reach:
            return "unreachable", url, ""
        if not ok:
            return "robots", url, ""
    st, ctype, data, final = _fetch(url, 1_500_000)
    if st == 0:
        return "unreachable", final, ""
    head = data[:20000].decode("utf-8", "replace") if data else ""
    if st in (401, 403, 429) or (st == 503 and C.BLOCK_RX.search(head)) or (C.BLOCK_RX.search(head) and len(data) < 30000):
        return "blocked", final, ""
    if st != 200 or not data:
        return "http_%s" % st, final, ""
    if data[:5] == b"%PDF-" or "pdf" in (ctype or "").lower() or ("html" not in (ctype or "html").lower() and b"<html" not in data[:3000].lower() and b"<a " not in data[:20000].lower()):
        return "not_html", final, ""
    fh = (urllib.parse.urlparse(final).hostname or "").lower()
    if C.registrable(fh) != C.registrable(p.hostname or "") and check_robots:  # redirected to another organisation's domain: its robots.txt decides
        fp = urllib.parse.urlparse(final)
        ok, _ = robots_ok("%s://%s/" % (fp.scheme, fp.netloc), final, cache)
        if not ok:
            return "robots", final, ""
    return "ok", final, C.quote_attrs(html.unescape(decode(data, ctype)))


def host_of(site):
    site = (site or "").strip()
    h = (urllib.parse.urlparse(site if "//" in site else "https://" + site).hostname or "").lower() if site else ""
    return h[4:] if h.startswith("www.") else h


def shard_ok(h, k, n):
    return int(hashlib.sha1(h.encode()).hexdigest(), 16) % n == k


def state_lines(prefix):
    """every line of the append-only state files data/incoming/claude/credit_scan/<prefix>_*.gz"""
    for p in sorted(glob.glob(os.path.join(DIR, prefix + "_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                if l.strip():
                    yield l.rstrip("\n")


# ------------------------------------------------------------------------------------------------------------------- universe
def universe(a):
    k, n = CCL.shard_of(a)
    os.makedirs("out", exist_ok=True)
    con = CCL._duck()
    out = collections.Counter()
    for spec in CCL.crawl_ids(a.crawl):
        cid, paths = CCL.newest_crawl(spec)
        queue, t0 = list(enumerate(paths[k::n])), time.time()
        for rnd in range(5):
            if not queue:
                break
            if rnd:
                print("round %d: %d index parts to read again after a pause" % (rnd + 1, len(queue)), flush=True)
                time.sleep(60 * rnd + random.uniform(0, 30))
            nxt = []
            for i, p in queue:
                q = ("SELECT url_host_registered_domain, count(*) FROM read_parquet('%s') WHERE url_host_tld IN ('ca', 'quebec') AND fetch_status = 200 "
                     "AND content_mime_detected = 'text/html' GROUP BY 1") % (CCL.CC + p)
                try:
                    got = con.execute(q).fetchall()
                except Exception as e:
                    print("part %d failed (round %d): %s" % (i, rnd + 1, str(e)[:160]), flush=True)
                    nxt.append((i, p))
                    time.sleep(10)
                    continue
                for d, c in got:
                    if d:
                        out[d.lower()] += c
                if got or i % 25 == 0:
                    print("%s %s part %d: %d .ca domains (total %d, %.0f s)" % (time.strftime("%H:%M:%S"), cid, i, len(got), len(out), time.time() - t0), flush=True)
            queue = nxt
        if queue:
            print("UNREAD index parts of %s after 5 rounds: %s" % (cid, ", ".join(str(i) for i, p in queue)), flush=True)
    with open("out/ca_domains_%d.csv" % k, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "pages"])
        for d, c in sorted(out.items()):
            w.writerow([d, c])
    print("shard %d: %d .ca registered domains with a captured page" % (k, len(out)), flush=True)


def merge_universe(a):
    doms = collections.Counter()
    if os.path.exists(UNIVERSE):
        with gzip.open(UNIVERSE, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                doms[r["dom"]] = int(r["pages"] or 0)
    n0 = len(doms)
    for f in sorted(glob.glob(os.path.join(a.dir, "ca_domains_*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r.get("dom") and not PLATFORM.search(r["dom"]):
                doms[r["dom"]] = max(doms[r["dom"]], int(r["pages"] or 0))
    os.makedirs(DIR, exist_ok=True)
    with gzip.open(UNIVERSE, "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["dom", "pages"])
        for d in sorted(doms):
            w.writerow([d, doms[d]])
    print(".ca universe: %d registered domains with a captured page (+%d this run)" % (len(doms), len(doms) - n0))


# ------------------------------------------------------------------------------------------------------------------- web graph
GRAPH_CA = os.path.join(DIR, "graph_ca_domains.csv.gz")      # .ca / .quebec domains the web graph knows (linked from somewhere), beyond the crawled ones
GRAPH_IN = os.path.join(DIR, "graph_inlinks.csv.gz")         # domains that link to a vendor proven in Canada (most footer credits are such links)


def newest_graph():
    try:
        for g in json.loads(CCL.http_get("https://index.commoncrawl.org/graphinfo.json", tries=3)):
            if g.get("id"):
                return g["id"]
    except Exception as e:
        print("graphinfo not reachable (%s): falling back to the last release we read" % type(e).__name__, flush=True)
    return "cc-main-2026-may-jun-jul"


def graph(a):
    """Common Crawl's domain-level web graph (one vertices file, one edges file; 118 M domains, 2.8 G links):
    (1) every .ca / .quebec domain it knows; (2) every domain that links to a vendor already proven in Canada. Both only say which home pages
    are worth one read — a lead still needs the credit line seen live on the site and the vendor's own address."""
    import shutil, subprocess
    rel = a.release if a.release and a.release != "auto" else newest_graph()
    base = a.base or "%sprojects/hyperlinkgraph/%s/domain/%s-domain-" % (CCL.CC, rel, rel)
    cands = [d for d in (a.work, "/mnt/cs", os.environ.get("RUNNER_TEMP") or "", ".") if d]
    work, free = ".", 0
    for d in cands:
        try:
            os.makedirs(d, exist_ok=True)
            st = os.statvfs(d)
            if os.access(d, os.W_OK) and st.f_bavail * st.f_frsize > free:
                work, free = d, st.f_bavail * st.f_frsize
        except OSError:
            pass
    print("web graph %s; work dir %s (%.1f GiB free)" % (rel, work, free / 2 ** 30), flush=True)
    os.makedirs("out", exist_ok=True)
    awk = shutil.which("mawk") or "awk"
    unz = (shutil.which("pigz") or "gzip") + " -dc"
    W = lambda name: os.path.join(work, name)
    sh = lambda cmd: subprocess.run(["bash", "-o", "pipefail", "-c", cmd], check=True)
    curl = "curl -sS -L --fail --retry 10 --retry-delay 10 --retry-all-errors -C - -A '%s'" % CCL.UA

    targets = set(proven_elsewhere()) | {d for d, o in vendor_state().items() if o.get("status") in ("CA", "CA-loc")}
    targets = {d for d in targets if d and not PLATFORM.search(d) and not FREE_PLAN.search(d)}
    tech_t = set()
    try:  # the customer-portal domains of the vetted Canada-HQ software vendors (<clinic>.janeapp.com …): a site that links to its portal is a customer
        import cc_tenants as CT
        tech_t = set(CT.portal_domains())
        import tech_relationships as _TR
        tech_t |= {d for v in _TR.VENDORS.values() for d in v.get("graph") or ()}  # vendors seen as a loaded widget: the sites that link to them ("Powered by …") are read too
    except Exception as e:
        print("portal domains not loaded: %s" % e, flush=True)
    targets |= tech_t
    # stores: a domain that links to shopify.com / myshopify.com ("Powered by Shopify" in the footer of the default themes, links to the
    # shop's own myshopify.com address) is very probably a store on Shopify. They are listed apart (graph_shopify.csv): the DNS lookups confirm
    # the storefront address, the candidate crawl reads the store's own /meta.json. Not credits, not capped.
    SHOP_T = {"shopify.com", "myshopify.com"}
    rev = lambda d: ".".join(reversed(d.split(".")))
    with open(W("targets.txt"), "w") as f:
        f.write("\n".join(sorted(rev(d) for d in targets | SHOP_T)) + "\n")
    print("targets: %d vendor domains proven in Canada" % len(targets), flush=True)
    t0 = time.time()
    sh("%s -o %s %svertices.txt.gz" % (curl, W("v.gz"), base))
    print("vertices downloaded: %.0f MiB in %.0f s" % (os.path.getsize(W("v.gz")) / 2 ** 20, time.time() - t0), flush=True)
    # one pass over the vertices: ids of the targets; every .ca / .quebec domain
    sh("%s %s | %s 'BEGIN{while((getline l < \"%s\") > 0) t[l]=1} {if ($2 in t) print $1\"\\t\"$2 > \"%s\"; if (substr($2,1,3)==\"ca.\" || substr($2,1,7)==\"quebec.\") print $2\"\\t\"$3 > \"%s\"; "
       "if ($3+0 >= 150) print $2\"\\t\"$3 > \"%s\"}'"
       % (unz, W("v.gz"), awk, W("targets.txt"), W("tv.txt"), W("ca.txt"), W("mt.txt")))
    # domains with 150+ host names of their own in the graph: multi-tenant platforms (<customer>.janeapp.com, <shop>.myshopify.com …) and large
    # organisations. The vendor step reads each one's own site: those that print a Canadian address are the Canada-based platforms whose
    # customer portals can be enumerated — candidates for the vetted vendor table (free plan? contracting company per country? read by hand once)
    n_mt = 0
    with open("out/graph_multitenant.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "hosts"])
        if os.path.exists(W("mt.txt")):
            for l in open(W("mt.txt"), encoding="utf-8", errors="replace"):
                q = l.split()
                if len(q) == 2 and re.fullmatch(r"[a-z0-9.-]+", q[0]) and q[0].count(".") <= 2 and q[1].isdigit():
                    w.writerow([rev(q[0]), q[1]])
                    n_mt += 1
    print("domains with 150+ host names (multi-tenant platforms and large organisations): %d" % n_mt, flush=True)
    tid = {}
    if os.path.exists(W("tv.txt")):
        for l in open(W("tv.txt")):
            q = l.split()
            if len(q) >= 2:
                tid[q[0]] = rev(q[1])
    n_ca = 0
    with open("out/graph_ca_domains.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "hosts"])
        if os.path.exists(W("ca.txt")):
            for l in open(W("ca.txt"), encoding="utf-8", errors="replace"):
                q = l.split()
                if q and re.fullmatch(r"[a-z0-9.-]+", q[0]) and q[0].count(".") <= 3:
                    d = rev(q[0])
                    if not PLATFORM.search(d):
                        w.writerow([d, q[1] if len(q) > 1 else ""])
                        n_ca += 1
    print("vertices read in %.0f s: %d of %d targets are in the graph; %d .ca / .quebec domains" % (time.time() - t0, len(tid), len(targets), n_ca), flush=True)
    with open(W("tid.txt"), "w") as f:
        f.write("\n".join(sorted(tid)) + "\n")
    # the edges: links INTO a target
    t0 = time.time()
    flt = "%s 'BEGIN{while((getline l < \"%s\") > 0) t[l]=1} ($2 in t)' > %s" % (awk, W("tid.txt"), W("hits.txt"))
    if free > 14 * 2 ** 30:
        sh("%s -o %s %sedges.txt.gz" % (curl, W("e.gz"), base))
        print("edges downloaded: %.1f GiB in %.0f s" % (os.path.getsize(W("e.gz")) / 2 ** 30, time.time() - t0), flush=True)
        sh("%s %s | %s" % (unz, W("e.gz"), flt))
        os.remove(W("e.gz"))
    else:  # not enough disk for the 10 GiB file: stream it (a broken stream is started again, at most 3 times)
        for attempt in range(3):
            try:
                sh("curl -sS -L --fail -A '%s' %sedges.txt.gz | %s | %s" % (CCL.UA, base, unz, flt))
                break
            except subprocess.CalledProcessError as e:
                print("edge stream attempt %d failed (%s)" % (attempt + 1, e.returncode), flush=True)
                if attempt == 2:
                    raise
                time.sleep(60)
    print("edges read in %.0f s" % (time.time() - t0), flush=True)
    indeg = collections.Counter()
    for l in open(W("hits.txt")):
        q = l.split()
        if len(q) == 2:
            indeg[q[1]] += 1
    ok_t = {t for t, c in indeg.items() if (c <= a.max_indegree or tid.get(t) in tech_t) and tid.get(t) not in SHOP_T}  # no cap for the vetted portals: their in-links ARE customers
    print("links into targets: %d; targets linked: %d; targets with more than %d linking domains (platform-like, left out): %d — %s"
          % (sum(indeg.values()), len(indeg), a.max_indegree, len(indeg) - len(ok_t), ", ".join("%s %d" % (tid.get(t, t), c) for t, c in indeg.most_common(12))), flush=True)
    src, src_tech = collections.Counter(), collections.defaultdict(set)
    try:
        vkey_of = CT.portal_domains()
    except Exception:
        vkey_of = {}
    for l in open(W("hits.txt")):
        q = l.split()
        if len(q) == 2 and q[1] in ok_t and q[0] not in tid:
            src[q[0]] += 1
            if tid.get(q[1]) in tech_t:
                src_tech[q[0]].add(vkey_of.get(tid[q[1]], tid[q[1]]))
    src = {f: c for f, c in src.items() if c <= 5 or f in src_tech}  # a domain linking to many vendors is a directory, not a client
    shop_ids = {i for i, d in tid.items() if d in SHOP_T}
    shop_src = set()
    for l in open(W("hits.txt")):
        q = l.split()
        if len(q) == 2 and q[1] in shop_ids and q[0] not in tid:
            shop_src.add(q[0])
    with open(W("fid.txt"), "w") as f:
        f.write("\n".join(set(src) | shop_src) + "\n")
    sh("%s %s | %s 'BEGIN{while((getline l < \"%s\") > 0) t[l]=1} ($1 in t){print $1\"\\t\"$2\"\\t\"$3}' > %s" % (unz, W("v.gz"), awk, W("fid.txt"), W("fv.txt")))
    n_in = n_shop = 0
    with open("out/graph_inlinks.csv", "w", newline="", encoding="utf-8") as f, open("out/graph_shopify.csv", "w", newline="", encoding="utf-8") as fsh:
        w, wsh = csv.writer(f), csv.writer(fsh)
        w.writerow(["dom", "targets", "hosts", "tech"])
        wsh.writerow(["dom", "hosts"])
        for l in open(W("fv.txt"), encoding="utf-8", errors="replace"):
            q = l.split()
            if len(q) < 2 or not re.fullmatch(r"[a-z0-9.-]+", q[1]) or q[1].count(".") > 3:
                continue
            d = rev(q[1])
            try:
                hosts = int(q[2]) if len(q) > 2 else 1
            except ValueError:
                hosts = 1
            if hosts > 30 or PLATFORM.search(d):
                continue
            if q[0] in shop_src:
                wsh.writerow([d, hosts])
                n_shop += 1
            if q[0] in src:
                w.writerow([d, src.get(q[0], 1), hosts, ",".join(sorted(src_tech.get(q[0], ())))])
                n_in += 1
    print("graph %s: %d domains link to shopify.com / myshopify.com (store candidates for the DNS lookups)" % (rel, n_shop), flush=True)
    print("graph %s: %d domains link to a vendor proven in Canada (1-5 such vendors each); %d of them link to a vetted customer portal: %s"
          % (rel, n_in, len(src_tech), dict(collections.Counter(v for vs in src_tech.values() for v in vs))), flush=True)


OSM_SITES = os.path.join(DIR, "osm_sites.csv.gz")  # websites of OpenStreetMap objects in Canada (shops, offices, clinics, restaurants …), any TLD
OVERTURE_SITES = os.path.join(DIR, "overture_sites.csv.gz")  # websites of the Overture Maps places in Canada (open data, monthly), any TLD
FSQ_SITES = os.path.join(DIR, "fsq_sites.csv.gz")  # websites of Foursquare's open places in Canada (tools/fsq_places.py ca; Apache 2.0), any TLD
GRAPH_SHOP = os.path.join(DIR, "graph_shopify.csv.gz")  # domains that link to shopify.com / myshopify.com (web graph): store candidates
GRAPH_MT = os.path.join(DIR, "graph_multitenant.csv.gz")  # domains with 150+ host names of their own (multi-tenant platforms, large organisations)
PLATFORM_CANDS = os.path.join(DIR, "platform_candidates.csv")  # those of them whose own site prints a Canadian address: to vet for the vendor table


def osm(a):
    """OpenStreetMap, Canada extract (Geofabrik): every object with a website tag -> its host, name and place. Organisations located in
    Canada whose site is on .com / .org as well as .ca: more home pages worth one read (the credit line and the mailbox come from the site)."""
    import shutil, subprocess
    work = a.work or os.environ.get("RUNNER_TEMP") or "."
    for d in (a.work, "/mnt/cs"):
        if d and os.path.isdir(d) and os.access(d, os.W_OK):
            work = d
            break
    os.makedirs("out", exist_ok=True)
    if not shutil.which("osmium"):
        sys.exit("osmium-tool is not installed (apt-get install osmium-tool)")
    W = lambda name: os.path.join(work, name)
    sh = lambda cmd: subprocess.run(["bash", "-o", "pipefail", "-c", cmd], check=True)
    url = a.base or "https://download.geofabrik.de/north-america/canada-latest.osm.pbf"
    t0 = time.time()
    sh("curl -sS -L --fail --retry 8 --retry-delay 10 --retry-all-errors -C - -A '%s' -o %s %s" % (CCL.UA, W("canada.osm.pbf"), url))
    print("extract downloaded: %.1f GiB in %.0f s" % (os.path.getsize(W("canada.osm.pbf")) / 2 ** 30, time.time() - t0), flush=True)
    sh("osmium tags-filter %s nwr/website nwr/contact:website nwr/url -o %s --overwrite" % (W("canada.osm.pbf"), W("sites.osm.pbf")))
    sh("osmium cat %s -f opl -o %s --overwrite" % (W("sites.osm.pbf"), W("sites.opl")))
    print("objects with a website tag extracted in %.0f s" % (time.time() - t0), flush=True)
    unq = lambda v: re.sub(r"%([0-9a-fA-F]+)%", lambda m: chr(int(m.group(1), 16)), v)
    KIND = ("shop", "amenity", "office", "craft", "tourism", "healthcare", "leisure", "club", "industrial", "man_made", "emergency", "landuse", "building")
    sites, n_obj = {}, 0
    for l in open(W("sites.opl"), encoding="utf-8", errors="replace"):
        m = re.search(r" T(\S*)", l)
        if not m:
            continue
        tags = {}
        for kv in m.group(1).split(","):
            k, _, v = kv.partition("=")
            tags[unq(k)] = unq(v)
        w = tags.get("website") or tags.get("contact:website") or tags.get("url") or ""
        h = host_of(w.split(";")[0].strip())
        if not h or "." not in h or PLATFORM.search(h) or not re.fullmatch(r"[a-z0-9.-]+", h):
            continue
        n_obj += 1
        kind = next(("%s=%s" % (k, tags[k]) for k in KIND if tags.get(k) and tags[k] != "yes"), "")
        o = sites.get(h)
        if o is None:
            sites[h] = [h, (tags.get("name") or tags.get("operator") or "")[:100], tags.get("addr:city") or "", tags.get("addr:province") or tags.get("addr:state") or "", tags.get("addr:postcode") or "", kind, 1]
        else:
            o[6] += 1
    with open("out/osm_sites.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "name", "city", "province", "postcode", "kind", "objects"])
        for h in sorted(sites):
            w.writerow(sites[h])
    tl = collections.Counter(h.rsplit(".", 1)[-1] for h in sites)
    print("OpenStreetMap Canada: %d objects with a website, %d distinct hosts (%s)" % (n_obj, len(sites), ", ".join("%s %d" % kv for kv in tl.most_common(6))), flush=True)


OVERTURE_BUCKET = "https://overturemaps-us-west-2.s3.amazonaws.com"


def overture(a):
    """Overture Maps Foundation, places theme (open data: CDLA Permissive 2.0 / ODbL by source; one release a month): every place whose
    address is in Canada and that names a website -> the site's host, the place's name, city, province, postal code and category. 2026-11-12:
    1,288,492 such places on 734,503 registrable domains, 345,712 of them neither read by the scan nor on any list (307,833 not .ca) —
    organisations in Canada whose sites the other lists do not reach. The mailbox a row stands on is still read on the organisation's own
    pages; so is its address, unless its own pages located nothing (below). Read with DuckDB over HTTPS (range requests on the release's parquet files; only the files
    whose places lie in Canada's box, only the columns needed).
    2026-11-12 (owner 2026-11-11 16:01 EST: "populate those fields as best as you can, don't just go empty … 1 million"; coord/DECISIONS.md of
    2026-11-12 04:39Z): also out/overture_addresses.csv — for every registrable domain whose open places in Canada all print ONE postal code,
    that place's street, city, province and postal code, its names, the datasets Overture took it from and its place id. A row by where the
    organisation is may stand on it when nothing of the organisation's own pages gave a postal code or a city, and says so (the ranker checks
    that the place's name fits the organisation's). A domain whose places print several postal codes (a chain, several sites) gives none.
    40 MB compressed (629,062 domains, release 2026-10-21.0): kept out of git, in the release "harvest-state" (credit-scan.yml, job overture),
    which the rank builds download."""
    import duckdb
    import xml.etree.ElementTree as ET
    os.makedirs("out", exist_ok=True)
    t0 = time.time()
    ls = lambda prefix: urllib.request.urlopen(urllib.request.Request("%s/?list-type=2&prefix=%s&delimiter=/" % (OVERTURE_BUCKET, urllib.parse.quote(prefix, safe="/=")),
                                                                      headers={"User-Agent": CCL.UA}), timeout=120).read().decode("utf-8", "replace")
    rel = sorted(re.findall(r"<Prefix>(release/[0-9]{4}-[0-9]{2}-[0-9]{2}\.[0-9]+/)</Prefix>", ls("release/")))
    if not rel:
        sys.exit("no Overture release listed")
    release = a.base or rel[-1]
    keys = re.findall(r"<Key>([^<]+\.parquet)</Key>", ls(release + "theme=places/type=place/"))
    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs; SET enable_progress_bar=false;")
    BOX = "bbox.xmin < -52 AND bbox.xmax > -141 AND bbox.ymin < 84 AND bbox.ymax > 41.6"
    files = []
    for k in keys:  # the files whose places lie in Canada's box (the release is sorted in space: three files of sixteen on 2026-11-12)
        f = "%s/%s" % (OVERTURE_BUCKET, k)
        if con.execute("SELECT count(*) FROM read_parquet('%s') WHERE %s" % (f, BOX)).fetchone()[0]:
            files.append(f)
    print("Overture %s: %d place files, %d in Canada's box (%.0f s)" % (release, len(keys), len(files), time.time() - t0), flush=True)
    rows = con.execute("""SELECT names."primary", websites[1], addresses[1].locality, addresses[1].region, addresses[1].postcode, basic_category, coalesce(operating_status, ''),
                                 id, addresses[1].freeform, list_transform(sources, lambda s: s.dataset), confidence
                          FROM read_parquet([%s]) WHERE %s AND addresses[1].country = 'CA' AND websites IS NOT NULL AND len(websites) > 0""" % (", ".join("'%s'" % f for f in files), BOX)).fetchall()
    sites, n_obj = {}, 0
    PCV = re.compile(r"[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]\d[ABCEGHJ-NPRSTV-Z]\d")
    by_dom = {}  # registrable domain -> [set of postal codes, best place, names, datasets, places]
    for name, w, city, prov, pc, kind, status, pid, street, ds, conf in rows:
        if status in ("permanently_closed",):
            continue
        h = host_of((w or "").split(";")[0].strip())
        if not h or "." not in h or PLATFORM.search(h) or not re.fullmatch(r"[a-z0-9.-]+", h):
            continue
        n_obj += 1
        o = sites.get(h)
        if o is None:
            sites[h] = [h, (name or "")[:100], city or "", prov or "", pc or "", kind or "", 1]
        else:
            o[6] += 1
        d = C.registrable(h)
        p = re.sub(r"[^A-Z0-9]", "", (pc or "").upper())
        g = by_dom.setdefault(d, [set(), None, [], set(), 0])
        g[4] += 1
        g[3].update(x for x in (ds or ()) if x)
        if name and name not in g[2] and len(g[2]) < 3:
            g[2].append(name[:100])
        if PCV.fullmatch(p):
            g[0].add(p)
            if g[1] is None or (conf or 0) > g[1][6]:
                g[1] = (re.sub(r"\s+", " ", street or "").strip()[:120], city or "", prov or "", p, pid or "", kind or "", conf or 0)
    n_addr = 0
    with open("out/overture_addresses.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "names", "street", "city", "province", "postcode", "datasets", "place_id", "kind", "places", "release"])
        for d in sorted(by_dom):
            g = by_dom[d]
            if len(g[0]) != 1 or not g[1]:
                continue  # several postal codes (a chain, several sites) or none: no address is given for the domain
            st, city, prov, p, pid, kind, _ = g[1]
            w.writerow([d, " | ".join(g[2]), st, city, prov, p, "+".join(sorted(g[3] - {"Overture"})) or "Overture", pid, kind, g[4], release.rstrip("/").rsplit("/", 1)[-1]])
            n_addr += 1
    print("Overture: %d registrable domains whose places all print one postal code (an address each in out/overture_addresses.csv); %d with several, %d with none"
          % (n_addr, sum(1 for g in by_dom.values() if len(g[0]) > 1), sum(1 for g in by_dom.values() if not g[0])), flush=True)
    with open("out/overture_sites.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "name", "city", "province", "postcode", "kind", "objects"])
        for h in sorted(sites):
            w.writerow(sites[h])
    tl = collections.Counter(h.rsplit(".", 1)[-1] for h in sites)
    print("Overture places in Canada: %d with a website, %d distinct hosts (%s) — release %s, %.0f s" % (n_obj, len(sites), ", ".join("%s %d" % kv for kv in tl.most_common(6)), release,
                                                                                                        time.time() - t0), flush=True)


def lists(a):
    """more .ca names than the web graph knows (1.05 M of the ~3.4 M registered): a public list of domain names collected by other crawlers
    (github.com/tb0hdan/domains, folder data/canada, Git LFS). Names only — each is read once by the scan like any other; most dead ones cost
    one failed request. Written as extra rows of the graph's .ca list (out/graph_ca_domains.csv)."""
    import shutil, subprocess
    work = next((d for d in (a.work, "/mnt/cs", os.environ.get("RUNNER_TEMP") or "", ".") if d and os.path.isdir(d) and os.access(d, os.W_OK)), ".")
    os.makedirs("out", exist_ok=True)
    repo = os.path.join(work, "domains-list")
    sh = lambda cmd: subprocess.run(["bash", "-o", "pipefail", "-c", cmd], check=True)
    known = set()
    for path in (UNIVERSE, GRAPH_CA):
        if os.path.exists(path):
            with gzip.open(path, "rt", encoding="utf-8", newline="") as fh:
                known |= {r["dom"] for r in csv.DictReader(fh)}
    try:
        if not os.path.isdir(repo):
            sh("GIT_LFS_SKIP_SMUDGE=1 git clone -q --depth 1 --filter=blob:none --sparse %s %s" % (a.base or "https://github.com/tb0hdan/domains.git", repo))
        sh("cd %s && git sparse-checkout set data/canada && git lfs pull --include 'data/canada/*' && ls -la data/canada | head -20" % repo)
    except subprocess.CalledProcessError as e:
        print("the public list could not be fetched (%s): nothing added" % e, flush=True)
        return
    n_seen = n_new = 0
    with open("out/graph_ca_domains.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "hosts"])
        seen = set()
        for path in sorted(glob.glob(os.path.join(repo, "data/canada/*"))):
            opener = "xz -dc" if path.endswith(".xz") else "cat"
            proc = subprocess.Popen(["bash", "-c", "%s '%s'" % (opener, path)], stdout=subprocess.PIPE, text=True, errors="replace")
            for l in proc.stdout:
                h = l.strip().lower().rstrip(".")
                if not h.endswith(".ca") or not re.fullmatch(r"[a-z0-9.-]+", h) or h.count(".") > 3:
                    continue
                n_seen += 1
                d = C.registrable(h[4:] if h.startswith("www.") else h)
                if d in seen or d in known or not d.endswith(".ca") or PLATFORM.search(d):
                    continue
                seen.add(d)
                w.writerow([d, ""])
                n_new += 1
            proc.wait()
    print("public list: %d .ca host names read, %d registrable .ca domains that neither the index nor the web graph had" % (n_seen, n_new), flush=True)


def merge_graph(a):
    os.makedirs(DIR, exist_ok=True)
    for name, path, cols in (("graph_ca_domains.csv", GRAPH_CA, ["dom", "hosts"]), ("graph_inlinks.csv", GRAPH_IN, ["dom", "targets", "hosts", "tech"]),
                             ("osm_sites.csv", OSM_SITES, ["dom", "name", "city", "province", "postcode", "kind", "objects"]),
                             ("overture_sites.csv", OVERTURE_SITES, ["dom", "name", "city", "province", "postcode", "kind", "objects"]), ("graph_shopify.csv", GRAPH_SHOP, ["dom", "hosts"]),
                             ("graph_multitenant.csv", GRAPH_MT, ["dom", "hosts"])):
        rows = {}
        if not glob.glob(os.path.join(a.dir, name)):
            print("%s: no new list from this run — left as it is" % os.path.basename(path))
            continue  # (rewriting it would change only the gzip header's time, and commit tens of megabytes of the same rows)
        if os.path.exists(path):
            with gzip.open(path, "rt", encoding="utf-8", newline="") as fh:
                rows = {r["dom"]: r for r in csv.DictReader(fh)}
        n0, changed = len(rows), False
        for f in sorted(glob.glob(os.path.join(a.dir, name))):
            for r in csv.DictReader(open(f, encoding="utf-8")):
                if r.get("dom"):
                    r = {c: r.get(c) or "" for c in cols}
                    if {c: (rows.get(r["dom"]) or {}).get(c) or "" for c in cols} != r:
                        changed = True
                    rows[r["dom"]] = r
        if rows and changed:
            # mtime 0: the same rows give the same bytes (2026-11-12: a run that added nothing committed the 20 MB list again)
            with io.TextIOWrapper(gzip.GzipFile(path, "wb", mtime=0), encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
                w.writeheader()
                for d in sorted(rows):
                    w.writerow(rows[d])
        print("%s: %d domains (+%d this run%s)" % (os.path.basename(path), len(rows), len(rows) - n0, "" if changed else "; no row changed, left as it is"))


# ------------------------------------------------------------------------------------------------------------------- scan
# 1: credit lines + the vendor table of 2026-11-02; 2 ("t2"): + Jobber; 3 ("t3"): + membership statements (class M);
# 4 ("t4"): + two facts about every readable home page, kept on its done line: em=<kind> when the page itself prints a role mailbox of the
#    organisation (the mailbox crawl reads those sites first: near-certain rows), cc=<CA|US|GB|AU> the country of the postal address it prints
DETECTOR = 5  # 5 (2026-11-10): the home page's outside links and embedded services (per host), own name facts (site name, copyright-line name, legalName, postal code), "sponsors / clients / members" sections, the register numbers it prints (RBQ, charity, TICO, ECRA/ESA, FSRA …) and the affiliations it states are kept (links_*.gz, sections_*.gz); the plain-http copy is asked when https does not answer
MARK = "t%d" % DETECTOR


def done_versions():
    """{site: detector version of its latest read} from the append-only done files"""
    ver = {}
    for l in state_lines("done"):
        q = l.split("\t")
        v = line_version(q)
        if v > ver.get(q[0], 0):
            ver[q[0]] = v
    return ver


def line_version(q):
    return next((int(x[1:]) for x in q[5:] if re.fullmatch(r"t\d", x)), 1)


def site_hints():
    """{site: (role-mailbox kind printed on its home page or "", country of the postal address it prints or "")} from the done lines (detector 4+)"""
    out = {}
    for l in state_lines("done"):
        q = l.split("\t")
        if len(q) > 6:
            em = next((x[3:] for x in q[6:] if x.startswith("em=")), "")
            cc = next((x[3:] for x in q[6:] if x.startswith("cc=")), "")
            if em or cc:
                out[q[0]] = (em, cc)
    return out


def ca_sites_without_mailbox():
    """{site: country of the postal address it prints or ""} — .ca sites whose home page the scan read (detector 4+) and that print NO role mailbox
    there (the latest read of each site counts). The mailbox, if the organisation publishes one, is on its contact page."""
    latest = {}
    for l in state_lines("done"):
        q = l.split("\t")
        if len(q) > 5 and q[0].endswith(".ca"):
            latest[q[0]] = (q[2] == "ok" and any(re.fullmatch(r"t[4-9]", x) for x in q[5:]),
                            next((x[3:] for x in q[6:] if x.startswith("em=")), ""), next((x[3:] for x in q[6:] if x.startswith("cc=")), ""))
    return {d: cc for d, (ok, em, cc) in latest.items() if ok and not em}


def sites_without_mailbox_any():
    """{site: country of the postal address it prints or ""} — sites of another ending than .ca whose home page the scan read (detector 4+) and
    that print NO role mailbox there (the latest read counts); the .ca ones are ca_sites_without_mailbox(). 552,175 of them print no Canadian
    address either on 2026-11-12; those an Overture Maps place's address locates are read for their contact page (tools/lead_crawl.py)."""
    latest = {}
    for l in state_lines("done"):
        q = l.split("\t")
        if len(q) > 5 and not q[0].endswith(".ca"):
            latest[q[0]] = (q[2] == "ok" and any(re.fullmatch(r"t[4-9]", x) for x in q[5:]),
                            next((x[3:] for x in q[6:] if x.startswith("em=")), ""), next((x[3:] for x in q[6:] if x.startswith("cc=")), ""))
    return {d: cc for d, (ok, em, cc) in latest.items() if ok and not em}


# ---- what a home page links to and loads (detector 5) --------------------------------------------------------------------------------
# Kept once per site so that a new lane does not need 1.3 million home pages read again: a vendor added to tools/tech_relationships.py is
# found by a join (which sites link or load its domain), a badge that links to a register (bbb.org profile) names the site's own entry.
# Not kept: the networks and tools nearly every site carries (they say nothing about a paid relationship and are four fifths of the volume).
LINK_STOP = re.compile(r"(^|\.)(google|googleapis|gstatic|googletagmanager|google-analytics|googleusercontent|googlesyndication|googleadservices|doubleclick|ggpht|goo|youtube|youtu|ytimg|"
                       r"facebook|fb|fbcdn|facebook|instagram|cdninstagram|twitter|x|twimg|t|linkedin|licdn|pinterest|pinimg|tiktok|snapchat|whatsapp|wa|telegram|threads|reddit|tumblr|flickr|vimeo|"
                       r"vimeocdn|apple|microsoft|bing|live|office|amazon|amazonaws|cloudfront|cloudflare|cloudflareinsights|jsdelivr|unpkg|cdnjs|jquery|bootstrapcdn|fontawesome|typekit|"
                       r"fonts|w3|wp|wordpress|w|gravatar|wixstatic|parastorage|wix|squarespace|squarespace-cdn|sqspcdn|weebly|editmysite|godaddy|wsimg|secureserver|sentry-cdn|sentry|"
                       r"addtoany|sharethis|addthis|hs-scripts|hsforms|hubspot|list-manage|mailchimp|recaptcha|hcaptcha|cookielaw|cookiebot|cdn-cookieyes|onetrust|osano|schema|ogp|"
                       r"creativecommons|wikipedia|wikimedia|archive|adobe|adobedtm|mapbox|openstreetmap|gmpg|rawgit|github|githubusercontent|bit|tinyurl|linktr|youtube-nocookie|"
                       r"paypal|paypalobjects|stripe|yelp|tripadvisor|trustpilot|spotify|soundcloud|canva|zoom|eventbrite|issuu|dropbox|statcounter|hotjar|clarity|newrelic|nr-data)"
                       r"\.[a-z.]{2,7}$", re.I)
LINK_PATH = re.compile(r"(^|\.)(owlpractice\.ca|bbb\.org|canadahelps\.org|getjobber\.com|amilia\.com|showpass\.com|raceroster\.com|webrez\.com|clio\.com|checkfront\.com|rezgo\.com|tbdine\.com|libroreserve\.com|"
                       r"gorendezvous\.com|lepointdevente\.com|skipthedishes\.com|chronogolf\.com|qidigo\.com|cognisantmd\.com|medeohealth\.com|wellnessliving\.com|membee\.com|keela\.co|e2rm\.com|"
                       r"akaraisin\.com|trellis\.org|myhelcim\.com|moneris\.com|bambora\.com|pheedloop\.com|eventmobi\.com|universe\.com|ticketpro\.ca|trackie\.com|zone4\.ca|uplifterinc\.com|"
                       r"powerupsports\.com|rampinteractive\.com|booxi\.com|petalmd\.com|carfax\.ca|autotrader\.ca|kijiji\.ca|homestars\.com|houzz\.com|indeed\.com|jobillico\.com|charityvillage\.com)$", re.I)
_MT_DOMS = None


def _multi_tenant_doms():
    """domains with 150+ host names of their own in the web graph (graph_multitenant.csv.gz): for those the full host is the customer's own address"""
    global _MT_DOMS
    if _MT_DOMS is None:
        _MT_DOMS = set()
        try:
            with gzip.open(GRAPH_MT, "rt", encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh):
                    _MT_DOMS.add(r["dom"])
        except Exception:
            pass
    return _MT_DOMS


def _link_key(h, path, d):
    """how one outside address is kept: host + start of the path for a watched service (the path names the account), otherwise the host as
    written without "www." (clinic.janeapp.com, careers.example.org: a host of its own is where a customer's account or a unit lives)"""
    h = h[4:] if h.startswith("www.") else h
    if LINK_PATH.search(d):
        return h + re.sub(r"[\s\t]+", "", (path or "/"))[:70]
    return h


def site_links(raw, final, site_dom, T, cap=40):
    """(embedded, linked): the outside addresses a home page loads (script / iframe / form targets) and links to (<a href>), common networks
    left out. Kept per host (clinic.janeapp.com); a link into a watched service keeps the start of its path too
    (bbb.org/ca/ab/calgary/profile/…): that is where the site's own account is named."""
    emb, lnk = {}, {}
    for rx in (T.SRC_RE, T.FORM_RE):
        for x in rx.findall(raw)[:400]:
            try:
                p = urllib.parse.urlparse(urllib.parse.urljoin(final, html.unescape(x).strip()))
                h = (p.hostname or "").lower()
            except ValueError:
                continue
            d = C.registrable(h) if h and "." in h else ""
            if d and d != site_dom and not LINK_STOP.search(d) and re.fullmatch(r"[a-z0-9.-]{4,80}", h):
                emb.setdefault(_link_key(h, p.path, d), 1)
                if len(emb) >= cap:
                    break
    for a_ in T.anchors_of(raw, final)[:1500]:
        try:
            p = urllib.parse.urlparse(a_[0])
        except ValueError:
            continue
        h = (p.hostname or "").lower()
        if p.scheme not in ("http", "https") or not h or "." not in h:
            continue
        d = C.registrable(h)
        if not d or d == site_dom or LINK_STOP.search(d) or not re.fullmatch(r"[a-z0-9.-]{4,80}", h):
            continue
        lnk.setdefault(_link_key(h, p.path, d), 1)
        if len(lnk) >= cap:
            break
    return sorted(emb), sorted(lnk)


# ---- what a home page states about itself: register numbers and affiliations (detector 5) -------------------------------------------
# A licence holder must print its number (Québec contractors: RBQ; Ontario travel agencies: TICO; Ontario electrical contractors: ECRA/ESA;
# mortgage brokerages: FSRA; Québec travel agents: the permit of the Office de la protection du consommateur), a charity prints its
# registration number for receipts. The number ties the site to the register's own entry exactly — no name matching. Kept as printed.
_NUM = (
    ("charity", re.compile(r"(?<![\d-])(\d{5})[\s\u00a0-]?(\d{4})[\s\u00a0-]?RR[\s\u00a0-]?(\d{4})(?!\d)", re.I)),
    ("gst", re.compile(r"(?<![\d-])(\d{5})[\s\u00a0-]?(\d{4})[\s\u00a0-]?RT[\s\u00a0-]?(\d{4})(?!\d)", re.I)),
    ("neq", re.compile(r"\bN\.?E\.?Q\.?(?![A-Za-z])[\s:#.]*(?:n[o°]\.?\s*)?((?:11|22|33|88)\d{8})(?!\d)", re.I)),
    ("rbq", re.compile(r"\bR\.?B\.?Q\.?(?![A-Za-z])[^0-9]{0,25}(\d{4})[\s\u00a0-]?(\d{4})[\s\u00a0-]?(\d{2})(?!\d)", re.I)),
    ("tico", re.compile(r"\bTICO\b[^0-9]{0,30}(\d{7,8})(?!\d)", re.I)),
    ("esa", re.compile(r"\b(?:ECRA\s*/\s*ESA|ESA\s*/\s*ECRA|ECRA|ESA)\b[^0-9]{0,25}(7\d{6})(?!\d)")),
    ("fsra", re.compile(r"\b(?:FSRA|FSCO)\b[^0-9]{0,30}(\d{5})(?!\d)")),
    ("opc", re.compile(r"(?:permis du Qu[ée]bec|Qu[ée]bec (?:permit|licen[cs]e)(?: holder)?)[^0-9]{0,25}(\d{6})(?!\d)", re.I)),
    ("cpbc", re.compile(r"(?:Consumer Protection B\.?C\.?|\bCPBC)\b[^0-9]{0,40}(\d{4,6})(?!\d)", re.I)),
    ("dealer", re.compile(r"\b(?:Dealer|DL|D)\s?(?:Lic(?:en[cs]e)?\.?\s?|No\.?\s?|Number\s?)?#\s?:?\s?(D?\d{4,5})(?![\d-])")),
)
# what the site says of itself, in its own words: "Proud member of …", "Accredited by …", "Authorized dealer of …", "independently owned and
# operated" (a franchise). Kept with the outside address the words link to, when they are a link. No lead is made from them here.
_CAP = r"[A-ZÀ-Ý][\w'’&.-]+"
_STATED = (
    ("member", re.compile(r"\b(?i:members?|membres?)\s+(?i:of|de|du|des|de\s+la|de\s+l['’])\s*(?i:the\s+)?" + _CAP)),
    ("accredited", re.compile(r"\b(?i:accredited|accr[ée]dit[ée]e?s?|certified|certifi[ée]e?s?|licen[cs]ed|agr[ée][ée]e?s?)\s+(?i:by|with|par|aupr[eè]s\s+d[eu])\s+(?i:the\s+|l[ae]\s+|l['’])?" + _CAP)),
    ("dealer", re.compile(r"\b(?i:authori[sz]ed|official|exclusive)\s+(?:" + _CAP + r"\s+){1,3}(?i:dealer|distributor|retailer|reseller|installer|applicator|service\s+(?:centre|center))s?\b|"
                          r"\b(?i:authori[sz]ed|official|exclusive)\s+(?i:dealer|distributor|retailer|reseller|installer|applicator|service\s+(?:centre|center))s?\s+(?i:of|for)\s+(?i:the\s+)?" + _CAP + "|"
                          r"\b(?i:d[ée]positaire|d[ée]taillant|distributeur|concessionnaire|installateur|revendeur|marchand)s?\s+(?i:autoris[ée]s?|agr[ée][ée]s?|officiels?|exclusifs?)\s+(?i:de|des|du|d['’])\s*"
                          r"(?i:la\s+|les\s+)?" + _CAP)),
    ("franchise", re.compile(r"(?i:independently\s+owned\s+and\s+operated|d[ée]tenue?s?\s+et\s+exploit[ée]e?s?\s+de\s+fa[cç]on\s+ind[ée]pendante|\ba\s+franchise\s+of\b|\bfranchis[ée]e?s?\s+(?:of|de|du)\s)")),
)
_STATED_NOT = re.compile(r"\b(?:become|devenir|devenez|join|login|log in|sign in|connexion|portal|portail|only|seulement|benefits?|avantages?|directory|r[ée]pertoire|our members|nos membres|"
                         r"team|[ée]quipe|staff|board|conseil|parliament|parlement|legislat\w*|council|congress|family|famille|community|communaut[ée]|public|church|[ée]glise|band|groupe|"
                         r"not affiliated|n['’]est pas affili)\b", re.I)
# a line such as "Members of:" / "Proud member of" / "Affiliations" / "Accreditations" standing alone above a row of badges
_BLOCK = re.compile(r"(?i)>\s*((?:we\s+are\s+)?(?:proud(?:ly)?\s+)?members?\s+of|(?:our\s+)?(?:affiliations|accreditations)|(?:nous\s+sommes\s+)?(?:fiers?\s+)?membres?\s+(?:de|du|des)|"
                    r"nos\s+(?:affiliations|accr[ée]ditations))\s*:?\s*<")
_A_LABEL = re.compile(r"(?is)<a\b([^>]*)>(.*?)</a>")
T_HREF = re.compile(r"""(?is)\bhref\s*=\s*["']([^"'>]+)["']""")
_ALT = re.compile(r"""(?is)\b(?:alt|title|aria-label)\s*=\s*["']([^"']{6,160})["']""")


def site_numbers(text):
    """[[kind, number, as printed] …] — the register numbers a page prints: ["rbq", "5760390401", "RBQ : 5760-3904-01"]. The number without its
    separators is the key of the join; the words as printed are the quote."""
    out, seen = [], set()
    for kind, rx in _NUM:
        n_kind = 0
        for m in rx.finditer(text):
            v = "".join(m.groups())
            if kind in ("charity", "gst"):
                v = "%s%s%s%s" % (m.group(1), m.group(2), "RR" if kind == "charity" else "RT", m.group(3))
            if (kind, v) in seen:
                continue
            seen.add((kind, v))
            out.append([kind, v, re.sub(r"\s+", " ", text[max(0, m.start() - 12):m.end()]).strip()[-70:]])
            n_kind += 1
            if n_kind >= 3:
                break
    return out[:8]


def site_stated(raw, final, site_dom, text, cap=6):
    """[[class, the words, the outside address they link to or ""] …] — affiliations a home page states: links whose own label says it
    (text, or the alt text of the badge), then sentences of the page."""
    out, seen = [], set()
    for m in _A_LABEL.finditer(raw[:1_500_000]):
        attrs, inner = m.group(1), m.group(2)
        hm = T_HREF.search(attrs)
        if not hm:
            continue
        label = re.sub(r"\s+", " ", html.unescape(re.sub(r"(?s)<[^>]+>", " ", inner))).strip()
        alts = " ".join(html.unescape(x) for x in _ALT.findall(attrs + " " + inner))
        words = (label + " " + alts).strip()
        if len(words) < 8:
            continue
        cls = next((c for c, rx in _STATED if rx.search(words)), "")
        if not cls or _STATED_NOT.search(words):
            continue
        try:
            h = (urllib.parse.urlparse(urllib.parse.urljoin(final, html.unescape(hm.group(1)).strip())).hostname or "").lower()
        except ValueError:
            continue
        d = C.registrable(h) if h and "." in h else ""
        if not d or d == site_dom or LINK_STOP.search(d):
            continue
        h = h[4:] if h.startswith("www.") else h
        if (cls, h) not in seen:
            seen.add((cls, h))
            out.append([cls, re.sub(r"[\t\r\n]+", " ", words)[:160], h])
        if len(out) >= cap:
            return out
    for m in _BLOCK.finditer(raw[:1_500_000]):  # the badges under a line "Members of:"
        seg = raw[m.end() - 1:m.end() + 5000]
        ft = re.search(r"(?i)<footer\b|<h[1-6]\b", seg[1:])
        if ft:
            seg = seg[:ft.start() + 1]
        for href, label in CCL.anchors(seg, final):
            try:
                h = (urllib.parse.urlparse(href).hostname or "").lower()
            except ValueError:
                continue
            d = C.registrable(h) if h and "." in h else ""
            if not d or d == site_dom or LINK_STOP.search(d) or CCL.SKIP.search(h) or CCL.PLATFORMS.search(h):
                continue
            h = h[4:] if h.startswith("www.") else h
            if ("member", h) not in seen and ("affil", h) not in seen:
                seen.add(("affil", h))
                out.append(["affil", (re.sub(r"\s+", " ", m.group(1)).strip() + ": " + re.sub(r"[\t\r\n]+", " ", label or "").strip())[:160], h])
            if len(out) >= cap + 4:
                return out
    for cls, rx in _STATED:
        for m in rx.finditer(text):
            a0 = max(text.rfind(". ", 0, m.start()) + 2, text.rfind(" | ", 0, m.start()) + 3, m.start() - 90, 0)
            snip = text[a0:m.end() + 110]
            cut = re.search(r"[.!?|•]\s", snip[m.end() - a0:])
            if cut:
                snip = snip[:m.end() - a0 + cut.start() + 1]
            snip = snip.strip()
            if _STATED_NOT.search(snip) or any(snip[:60] in o[1] or o[1][:60] in snip for o in out if o[0] == cls):
                continue
            out.append([cls, snip[:200], ""])
            if len(out) >= cap or len([o for o in out if o[0] == cls and not o[2]]) >= 2:
                break
        if len(out) >= cap:
            break
    return out


_SEC = {
    "sponsor": re.compile(r"^(?:(?:our|nos|les|merci (?:à|a) nos|thank you to our|thanks to our|proud(?:ly)?|presenting|title|platinum|gold|silver|bronze|major|event|corporate|community|official|20\d\d|"
                          r"principaux)\s+)*(?:sponsors?|commanditaires?|exhibitors?|exposants?|advertisers?|annonceurs?)\b[^.?!]{0,30}$", re.I),
    "client": re.compile(r"^(?:(?:some of |a few of |quelques-uns de )?(?:our|nos)\s+(?:valued\s+|happy\s+|satisfied\s+)?(?:clients?|customers?)|clients?|trusted by|they trust us|"
                         r"ils nous font confiance|elles nous font confiance|who we work with|clients? we(?:'ve| have) worked with)\b[^.?!]{0,30}$", re.I),
    "member": re.compile(r"^(?:(?:our|nos|les)\s+(?:members?|membres?)\b[^.?!]{0,25}|(?:member|membership) directory|r[ée]pertoire des membres)$", re.I),
}
_SEC_NOT = re.compile(r"become|devenir|devenez|opportunit|package|forfait|sponsorship|commandite\b|why|pourquoi|how to|comment|login|log in|connexion|area|zone|espace|portal|portail|only|seulement|"
                      r"benefit|avantage|testimonial|t[ée]moignage|say|disent|review|avis|service|support|care", re.I)
_HEAD = re.compile(r"(?is)<h([1-6])\b[^>]*>(.*?)</h\1\s*>")


def home_sections(raw, final, site_dom, skip=()):
    """[{"c": class, "h": heading, "l": [[outside domain, label] …]}] — the parts of a home page under a heading such as "Our Sponsors",
    "Nos clients", "Our Members": the outside organisations linked there (logo or text links with a label), until the next heading of the same
    or a higher level. Kept as read (detector 5); a lead is made from them only by a rule of its own, later."""
    heads = [(m.start(), m.end(), int(m.group(1)), re.sub(r"\s+", " ", html.unescape(re.sub(r"(?s)<[^>]+>", " ", m.group(2)))).strip()) for m in _HEAD.finditer(raw[:1_500_000])]
    out = []
    for i, (st, en, lvl, text) in enumerate(heads):
        if not (3 <= len(text) <= 60) or _SEC_NOT.search(text):
            continue
        cls = next((c for c, rx in _SEC.items() if rx.match(text)), "")
        if not cls:
            continue
        end = next((s2 for s2, _, l2, _ in heads[i + 1:] if l2 <= lvl), len(raw))
        seg = raw[en:min(end, en + 60_000)]
        ft = re.search(r"(?i)<footer\b|<(?:div|section)[^>]+(?:id|class)=[\"'][^\"']*\bfooter\b", seg)
        if ft:
            seg = seg[:ft.start()]  # the page's footer (credits, networks) is not part of the list
        got = {}
        for href, label in CCL.anchors(seg, final):
            try:
                h = CCL.base(urllib.parse.urlparse(href).hostname)
            except ValueError:
                continue
            label = re.sub(r"\s+", " ", label or "").strip()
            if (not h or "." not in h or len(h) > 60 or C.registrable(h) == site_dom or C.registrable(h) in skip or CCL.SKIP.search(h) or CCL.PLATFORMS.search(h) or CCL.VENDOR_SKIP.search(h)
                    or not label or len(label) > 100 or CCL.GENERIC_LABEL.match(label) or CCL.LABEL_SKIP.search(label) or CCL.SPAM.search(h) or CCL.SPAM.search(label)):
                continue
            got.setdefault(C.registrable(h), label[:80])
            if len(got) >= 60:
                break
        if len(got) >= 3:
            out.append({"c": cls, "h": text[:60], "l": [[d, lab] for d, lab in got.items()]})
        if len(out) >= 4:
            break
    return out


# the name a site states for itself, kept for every readable home page (detector 5): the key that ties a register entry (a licence holder, a
# trademark owner, a corporation: legal name + postal code) to the organisation's own site. Same two expressions as tools/org_extras.py.
_COPY = re.compile(r"(?:©|&copy;|\(c\)|copyright|tous droits r[ée]serv[ée]s|all rights reserved)[\s,.]*(?:copyright\s*)?(?:(?:19|20)\d\d(?:\s*[-–]\s*(?:19|20)?\d\d)?)?[\s,.]*"
                   r"(?:by\s+|par\s+)?([A-Z0-9][^|•\n©]{2,90}?)(?=\s*(?:\.|\||•|all rights|tous droits|\s[-–—]\s|$|\n|privacy|confidentialit|terms|conditions|site|powered|design|web|\d{4}))", re.I)
_COPY2 = re.compile(r"([A-Z0-9][^|•\n©]{2,90}?)\s*(?:©|&copy;)\s*(?:19|20)\d\d", re.I)
_LEGALNAME = re.compile(r'"legalName"\s*:\s*"([^"\\]{2,120})"')
_PC_ONLY = re.compile(r"(?<![A-Za-z0-9])([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z])[ \u00a0-]?(\d[ABCEGHJ-NPRSTV-Z]\d)(?![A-Za-z0-9])")


def name_facts(raw, name, addr):
    """"site name|name in the copyright line|schema.org legalName|first Canadian postal code" of a home page (pipes and tabs removed)"""
    foot = C.visible(raw[-30000:])[-1500:]
    m = _COPY.search(foot) or _COPY2.search(foot)
    cp = re.sub(r"\s+", " ", m.group(1)).strip(" .,-–|") if m else ""
    if len(cp) < 3 or re.fullmatch(r"[\d\s.,-]+", cp):
        cp = ""
    ml = _LEGALNAME.search(raw[:800_000])
    pc = _PC_ONLY.search(addr or "") or _PC_ONLY.search(foot)
    cl = lambda x: re.sub(r"[|\t\r\n]+", " ", html.unescape(x or "")).strip()[:100]
    return "%s|%s|%s|%s" % (cl(name), cl(cp), cl(ml.group(1) if ml else ""), (pc.group(1) + pc.group(2)).upper() if pc else "")


def refused_sites():
    """sites whose latest verdict is a refusal (robots.txt or a block): they are not read again when the detector changes"""
    latest = {}
    for l in state_lines("done"):
        q = l.split("\t")
        if len(q) > 2:
            latest[q[0]] = q[2]
    return {d for d, st in latest.items() if st in ("blocked", "robots")}


def site_via():
    """{site: "http" | "www" | "httpwww"} — the address that answered when https://site/ did not (done lines of detector 5+)"""
    out = {}
    for l in state_lines("done"):
        q = l.split("\t")
        if len(q) > 6:
            v = next((x[4:] for x in q[6:] if x.startswith("via=")), "")
            if v:
                out[q[0]] = v
            else:
                out.pop(q[0], None)
    return out


def site_url(dom, via=None):
    v = (via if via is not None else {}).get(dom, "")
    return "%s://%s%s/" % ("http" if "http" in v else "https", "www." if "www" in v else "", dom)


def scan_queue(k, n, limit=0):
    ver = done_versions()
    refused = refused_sites()
    seen, tasks = set(), []

    def add(host, pri, extra=0, again=False):
        """a site read by an older detector (done line without the current mark) is read once more: right away when the web graph says it
        links to a vetted portal (again), otherwise after every site that was never read"""
        if not host or "." not in host or host in seen or PLATFORM.search(host) or not shard_ok(host, k, n):
            return
        v = ver.get(host)
        if v is not None:
            if v >= DETECTOR or host in refused:  # a site that refused the reader (robots.txt, a block) is left alone
                return
            pri = pri if again else pri + 10
        seen.add(host)
        tasks.append((pri, -extra, host))
    import ranked_io  # the ranked table is committed in parts (GitHub's 100 MB limit): read them wherever they are
    for r in ranked_io.rows():  # 1. delivered rows: the inferred-relationship rows first (a credit gives them a relationship with evidence)
        add(host_of(r.get("buyer_website")), 0 if r.get("tier") == "I" else 1)
    import lead_store as LS
    for p in (CCL.LEADS_CC, os.path.join(INC, "claude_buyer_leads.csv")):  # 2. leads (a credit is a second, first-party relationship)
        if os.path.exists(p):
            for r in LS.reader(p):
                add(host_of(r.get("website")), 2)
    if os.path.exists(GRAPH_IN):  # 3. sites that link to a vendor proven in Canada (web graph): most footer credits are such links
        with gzip.open(GRAPH_IN, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 2 if r.get("tech") else 3, int(r.get("targets") or 1), again=bool(r.get("tech")))
    if os.path.exists(OSM_SITES):  # 3. organisations OpenStreetMap places in Canada (any TLD); chains with hundreds of branches last
        with gzip.open(OSM_SITES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 3, -min(int(r.get("objects") or 1), 400))
    if os.path.exists(OVERTURE_SITES):  # 3. organisations of the Overture Maps places in Canada (any TLD; 2026-11-12); chains with hundreds of branches last
        # at the front of priority 3: a place with an address in Canada is an organisation located in Canada (a row by where it is once its own
        # site gives a mailbox and an address), where a site of the web graph is only one that links to a Canadian vendor
        with gzip.open(OVERTURE_SITES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 3, 100000 - min(int(r.get("objects") or 1), 400))
    if os.path.exists(FSQ_SITES):  # 3. organisations of Foursquare's open places in Canada (any TLD; 2026-11-13), after the Overture ones
        with gzip.open(FSQ_SITES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 3, 50000 - min(int(r.get("objects") or 1), 400))
    if os.path.exists(UNIVERSE):  # 4. every .ca site of the archive, the sites with the most captured pages first
        with gzip.open(UNIVERSE, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 4, min(int(r.get("pages") or 0), 500))
    try:  # 4. .ca names of the certificate logs (tools/ct_names.py): sites that hold a web certificate today and that no list above has
        import ct_names as _CT
        for d in _CT.ct_ca_names():
            add(d, 4)
    except Exception as e:
        print("certificate-log .ca names not read: %s" % e, flush=True)
    if os.path.exists(GRAPH_CA):  # 5. .ca domains the web graph knows only as link targets (many are gone: one failed request each)
        with gzip.open(GRAPH_CA, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 5)
    tasks.sort()
    if limit:
        tasks = tasks[:limit]
    return [{"dom": h, "pri": pri} for pri, _, h in tasks], len(ver)


def scan(a):
    import lead_crawl as LC
    import tech_relationships as T
    global _fetch
    _fetch = fast_fetch
    k, n = CCL.shard_of(a)
    os.makedirs("out", exist_ok=True)
    tasks, n_done = scan_queue(k, n, a.limit)
    print("shard %d/%d: %d sites to read (%d read before): %s" % (k, n, len(tasks), n_done, dict(collections.Counter(t["pri"] for t in tasks))), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fs = open("out/credit_seen_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/credit_done_%d.tsv" % k, "a", encoding="utf-8")
    flk = open("out/site_links_%d.tsv" % k, "a", encoding="utf-8")       # detector 5: what each home page loads and links to
    fsec = open("out/site_sections_%d.jsonl" % k, "a", encoding="utf-8")  # detector 5: its "sponsors / clients / members" sections ("s"), printed register numbers ("n"), stated affiliations ("st")
    assets_of = lambda b: " ".join(T.SRC_RE.findall(b) + T.LINKTAG_RE.findall(b) + T.INLINE_RE.findall(b)[:40])
    # which outside services do these sites load or post to? (script / iframe / form targets, counted per registrable domain) — the frequency
    # table shows which Canada-based platforms are worth vetting for the vendor table of tools/tech_relationships.py
    ext = collections.Counter()

    def embedded(raw, final, site_dom):
        out = set()
        for rx in (T.SRC_RE, T.FORM_RE):
            for x in rx.findall(raw)[:400]:
                try:
                    h = (urllib.parse.urlparse(urllib.parse.urljoin(final, html.unescape(x).strip())).hostname or "").lower()
                except ValueError:
                    continue
                d = C.registrable(h) if h and "." in h else ""
                if d and d != site_dom:
                    out.add(d)
        return out

    COUNTRY = (("CA", CCL.ADDR), ("US", LC.US_ADDR), ("GB", LC.GB_ADDR), ("AU", LC.AU_ADDR))

    def home_facts(raw, fhost, name):
        """(kind of the best role mailbox the home page prints for this organisation, country of the postal address it prints, that address)"""
        text = C.visible(raw)
        best = ""
        for e in C.page_emails(raw[:600_000]):
            if e.rsplit(".", 1)[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp") or not LC.ok_mailbox(e):
                continue
            try:
                if not C.same_org(e, "https://%s/" % fhost, name or ""):
                    continue
                i = C.find_tok(text, e)
                kind = C.classify(e, text[max(0, i - 400):i + 400] if i >= 0 else "", "any")
            except Exception:
                continue
            if kind and (not best or C.RANK[kind] < C.RANK[best]):
                best = kind
        for cc, rx in COUNTRY:
            m = rx.search(text)
            if m:
                return best, cc, re.sub(r"\s+", " ", text[max(0, m.start() - 90):m.end()]).strip()[-170:]
        return best, "", ""

    def one(t):
        if time.time() > deadline:
            return
        dom = t["dom"]
        try:
            res, final, raw = get_page("https://%s/" % dom)
        except Exception as e:
            res, final, raw = "error:" + type(e).__name__, "", ""
        rec, em, cc = None, "", ""
        via, lk_line, sec_line, sec_kinds = "", "", "", (False, False, False)
        if res == "ok":
            try:
                fhost = host_of(final) or dom
                if C.registrable(fhost) == C.registrable(dom):  # which address answered: plain http, the www. host (lead readers start there)
                    via = ("http" if final.startswith("http://") else "") + ("www" if (urllib.parse.urlparse(final).hostname or "").lower() == "www." + dom else "")
                title, meta = T.page_meta(raw)
                name = LC.site_name_for(fhost, meta.get("og:site_name"), title, T)
                try:
                    em, cc, addr = home_facts(raw, fhost, name)
                except Exception:
                    em, cc, addr = "", "", ""
                credits = find_credits(raw, final)
                tech = []
                for u in T.all_urls(raw, final)[:3000]:
                    for vk, slug, purl in T.portal_hits(u):
                        if not any(x["v"] == vk and x["slug"] == slug for x in tech):
                            tech.append({"v": vk, "slug": slug, "purl": purl, "via": u[:200], "how": "link / embed on the organisation's own page"})
                if C.registrable(fhost) == C.registrable(dom) or not PLATFORM.search(fhost):
                    assets = assets_of(raw)
                    for vk, v in T.VENDORS.items():
                        if v["kind"] == "asset" and v.get("asset_re_c"):
                            ma = v["asset_re_c"].search(assets)
                            if ma:
                                x = {"v": vk, "slug": "asset", "purl": "", "via": re.sub(r"\s+", " ", assets[max(0, ma.start() - 40):ma.end() + 60])[:160], "how": "asset loaded by the organisation's own page"}
                                if vk == "shopify":
                                    mc = re.search(r'Shopify\.country\s*=\s*"([A-Z]{2})"', raw)
                                    x["country"] = mc.group(1) if mc else ""
                                tech.append(x)
                emb = embedded(raw, final, C.registrable(fhost))
                with lock:
                    ext.update(emb)
                if C.registrable(fhost) == C.registrable(dom) or not PLATFORM.search(fhost):
                    try:
                        e_l, l_l = site_links(raw, final, C.registrable(fhost), T)
                        nf = name_facts(raw, name, addr)
                        if e_l or l_l or nf.strip("|"):
                            lk_line = "%s\t%s\t%s\t%s\n" % (dom, " ".join(e_l), " ".join(l_l), nf)
                        secs = home_sections(raw, final, C.registrable(fhost), {C.registrable(c_["vh"]) for c_ in credits} | {c_["v"] for c_ in credits})
                        vis = C.visible(raw[:1_500_000])
                        nums = site_numbers(vis)
                        said = site_stated(raw, final, C.registrable(fhost), vis)
                        if secs or nums or said:
                            o_ = {"dom": dom, "page": final, "date": TODAY, "name": name, "cc": cc, "addr": addr}
                            if secs:
                                o_["s"] = secs
                            if nums:
                                o_["n"] = nums
                            if said:
                                o_["st"] = said
                            sec_line = json.dumps(o_, ensure_ascii=False) + "\n"
                            sec_kinds = (bool(secs), bool(nums), bool(said))
                    except Exception:
                        pass
                if credits or tech:
                    rec = {"dom": dom, "site": fhost, "page": final, "date": TODAY, "name": name, "title": (title or "")[:160], "credits": credits, "tech": tech, "em": em, "cc": cc, "addr": addr}
            except Exception as e:
                res = "error:" + type(e).__name__
        with lock:
            stats["sites"] += 1
            stats[res.split(":")[0] if not res.startswith("http_") else "http_error"] += 1
            if rec:
                stats["with_credit"] += bool(rec["credits"])
                stats["with_vetted_service"] += bool(rec["tech"])
                fs.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fd.write("%s\t%s\t%s\t%d\t%d\t%s%s%s%s\n" % (dom, TODAY, res, len(rec["credits"]) if rec else 0, len(rec["tech"]) if rec else 0, MARK,
                                                       "\tem=" + em if em else "", "\tcc=" + cc if cc else "", "\tvia=" + via if via else ""))
            if lk_line:
                flk.write(lk_line)
            if sec_line:
                fsec.write(sec_line)
                stats["with_a_sponsors_clients_members_section"] += sec_kinds[0]
                stats["prints_a_register_number"] += sec_kinds[1]
                stats["states_an_affiliation"] += sec_kinds[2]
            stats["home_page_prints_role_mailbox"] += bool(em)
            if stats["sites"] % 2000 == 0:
                fs.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    def on_timeout(t):
        with lock:
            fd.write("%s\t%s\ttimeout\t0\t0\t%s\n" % (t["dom"], TODAY, MARK))
            stats["timeout"] += 1
    left = LC.run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fs.close(); fd.close(); flk.close(); fsec.close()
        with open("out/credit_ext_%d.tsv" % k, "w", encoding="utf-8") as f:
            for d, c in ext.most_common(30000):
                if c >= 2:
                    f.write("%s\t%d\n" % (d, c))
    print("finished", dict(stats), "(stragglers left: %d)" % left, flush=True)


# ------------------------------------------------------------------------------------------------------------------- vendors
CONTACT_RX = re.compile(r"contact|joindre|coordonn|about|propos|qui-sommes|nous-trouver|find-us|location|bureaux|offices?|impressum|legal|mentions|privacy|confidentialit|terms|conditions|politique", re.I)
_PROVN = (r"Qu[ée]bec|Ontario|British Columbia|Colombie-Britannique|Alberta|Manitoba|Saskatchewan|Nova Scotia|Nouvelle-[ÉE]cosse|New Brunswick|Nouveau-Brunswick|"
          r"Newfoundland(?: and Labrador)?|Terre-Neuve(?:-et-Labrador)?|Prince Edward Island|[ÎI]le-du-Prince-[ÉE]douard|Yukon|Nunavut|Northwest Territories")
# "Halifax, Nova Scotia" · "Montréal (Québec)" · "Toronto, ON" · "Saskatchewan, Canada": the vendor's own statement of where it is (no postal code)
LOC_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])([A-ZÀ-Ý][A-Za-zÀ-ÿ.'’\-]+(?:[ \-][A-ZÀ-Ý][A-Za-zÀ-ÿ.'’\-]+){0,3})\s*(?:,\s*|\(\s*)(?:(" + _PROVN + r")|(QC|Qc|ON|BC|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NT|NU))\)?"
                    r"(?:,?\s*Canada)?(?![A-Za-zÀ-ÿ])(?!,?\s*(?:CA|California|USA?)\b)(?!\s+\d{5})")
CANADA_LINE_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])(" + _PROVN + r"),?\s+Canada(?![A-Za-zÀ-ÿ])")
CA_PHONE_RX = re.compile(r"(?<![\d.])(?:\+?1[\s.\-]?)?\(?(204|226|236|249|250|263|289|306|343|354|365|367|368|382|403|416|418|428|431|437|438|450|468|474|506|514|519|548|579|581|584|587|604|613|639|"
                         r"647|672|683|705|709|742|753|778|780|782|807|819|825|867|873|879|902|905)\)?[\s.\-]{0,2}\d{3}[\s.\-]?\d{4}(?![\d.])")
LD_PC_RX = re.compile(r'"postalCode"\s*:\s*"\s*([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ \-]?\d[ABCEGHJ-NPRSTV-Z]\d)\s*"', re.I)
LD_FIELD_RX = re.compile(r'"(streetAddress|addressLocality|addressRegion|postalCode|addressCountry)"\s*:\s*"([^"]{1,90})"')


def jsonld_address(raw):
    """a schema.org PostalAddress with a Canadian postal code in the page source: 'streetAddress: …, addressLocality: …, postalCode: …'"""
    m = LD_PC_RX.search(raw)
    if not m:
        return ""
    seg, got = raw[max(0, m.start() - 500):m.end() + 300], {}
    for k, v in LD_FIELD_RX.findall(seg):
        got.setdefault(k, v.strip())
    return ", ".join("%s: %s" % (k, got[k]) for k in ("streetAddress", "addressLocality", "addressRegion", "postalCode", "addressCountry") if got.get(k))[:220]


def location_line(text):
    """(quote, phone) when the page states a Canadian province next to a place name AND prints a telephone number with a Canadian area code"""
    ph = CA_PHONE_RX.search(text)
    if not ph:
        return "", ""
    m = CANADA_LINE_RX.search(text) or LOC_RX.search(text)
    if not m:
        return "", ""
    return re.sub(r"\s+", " ", text[max(0, m.start() - 40):m.end()]).strip(), ph.group(0).strip()
SERVICE_RX = re.compile(r"web|site|design|digital|num[ée]rique|marketing|agenc[ey]|studio|cr[ée]ati|d[ée]velop|software|logiciel|h[ée]berg|hosting|seo|r[ée]f[ée]rencement|branding|"
                        r"graphi|communication|m[ée]dia|informati|\bIT\b|\bTI\b|technolog|app|cloud|e-?commerce|consult", re.I)


_PROVIDERS = None


def big_providers():
    """{domain: client domains} of the domains that other domains' DNS records name (tools/dns_services.py table). A vendor whose address
    leads to one that serves 200+ domains is on a parking page of its registrar or host ("cag2025.ca is registered at …"), not under a new
    name — unless the vendor's domain is itself such a technical domain (easymail.ca -> easydns.com: one company's second domain)"""
    global _PROVIDERS
    if _PROVIDERS is None:
        _PROVIDERS = {}
        p = os.path.join(DIR, "dns_providers_seen.csv")
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding="utf-8")):
                try:
                    _PROVIDERS[r["provider_domain"]] = int(r.get("client_domains") or 0)
                except (KeyError, ValueError):
                    pass
    return _PROVIDERS


def proof_page_ok(v, o):
    """the page that carries the address must be the vendor's own: on its domain's own hosts (the bare domain, www, a sub-site named after a
    function or after the domain — never a customer's, a team's or a unit's sub-site: tools/cc_clients.py own_host), or on the domain its own
    address redirects to when that is a rename (shared name, or the new site names the old one) and not a registrar's or host's parking page"""
    ph = host_of(o.get("url") or "")
    pd = C.registrable(ph) if ph else v
    if pd == v:
        return not ph or CCL.own_host(ph, v)
    if big_providers().get(pd, 0) >= 200 and v not in big_providers():
        return False
    if o.get("renamed"):
        return True
    a_, b_ = re.sub(r"[^a-z0-9]", "", v.split(".")[0]), re.sub(r"[^a-z0-9]", "", pd.split(".")[0])
    if (len(a_) >= 3 and a_ in b_) or (len(b_) >= 3 and b_ in a_):
        return True
    return any(a_[i:i + 5] in b_ for i in range(max(0, len(a_) - 4)))  # five letters in a row in common: intrigueme.ca -> intriguemedia.com


def proven_elsewhere():
    """vendor domains whose Canadian postal address the row factory already read on the vendor's own page: {domain: (address text, url, name)}"""
    out = {}
    if True:
        import lead_store as LS
        for d in LS.load()[1].values():  # details of the cloud leads: base file + shards
            if d.get("platform") == "vendor_site_cc" and d.get("vendor_address") and d.get("vendor_site"):
                vh = host_of(d["vendor_site"])
                dom = C.registrable(vh)
                ah = host_of(d.get("vendor_address_url") or d.get("record_url") or "")
                if not CCL.own_host(vh, dom) or (ah and C.registrable(ah) == dom and not CCL.own_host(ah, dom)):
                    continue  # 2026-11-11: the address of a body on a sub-site (a platform's customer, a team, a unit) is not the domain holder's
                nm = d.get("vendor") or ""
                out.setdefault(dom, (d["vendor_address"], d.get("vendor_address_url") or d.get("record_url") or "", "" if re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", nm.lower()) else nm))
    for dom, o in CCL._vendor_addrs().items():
        out.setdefault(C.registrable(dom), ("%s (as printed on %s, archive capture %s)" % (CCL.address_from(o.get("quote") or ""), o.get("url") or "", (o.get("capture") or "")[:10]), o.get("url") or "", ""))
    return out


def vendor_state():
    """latest live check per vendor domain"""
    out = {}
    for l in state_lines("vendors"):
        try:
            o = json.loads(l)
            out[o["dom"]] = o
        except (ValueError, KeyError):
            pass
    return out


def sightings():
    """one record per site: the latest read, plus what an earlier read saw and the latest did not (a site read again by a newer detector)"""
    out = {}
    for l in state_lines("seen"):
        try:
            o = json.loads(l)
        except ValueError:
            continue
        if not o.get("dom"):
            continue
        old = out.get(o["dom"])
        if old:
            have = {c["v"] for c in o.get("credits") or []}
            o["credits"] = (o.get("credits") or []) + [c for c in old.get("credits") or [] if c["v"] not in have]
            havet = {(t["v"], t["slug"]) for t in o.get("tech") or []}
            o["tech"] = (o.get("tech") or []) + [t for t in old.get("tech") or [] if (t["v"], t["slug"]) not in havet]
        out[o["dom"]] = o
    return out


def vendors(a):
    import lead_crawl as LC
    import tech_relationships as T
    k, n = CCL.shard_of(a)
    os.makedirs("out", exist_ok=True)
    # rule 2 (2026-11-10): schema.org address data, privacy / terms pages, the location line. Vendors that gave "no_address" under rule 1 are read again
    # rule 3 (2026-11-10, after reading the first 25,510 leads): the record also says where the vendor's domain redirects ("final") and whether
    # that site names the old one ("renamed": a rebrand, not a dropped domain bought by somebody else), and whether a "powered by" platform
    # advertises a free plan ("free_signal"); contact pages are read on the vendor's own hosts only. Read again under rule 3: proofs found on
    # another domain, and platforms credited with "powered by" on 3+ sites.
    cnt, pcnt = collections.Counter(), collections.Counter()
    for o in sightings().values():
        for c in o.get("credits") or []:
            cnt[c["v"]] += 1
            pcnt[c["v"]] += c.get("k") == "P"

    def settled(d, o):
        r = o.get("rule") or 1
        if o.get("status") == "no_address" and r < 2:
            return False
        if r < 3 and o.get("status") in ("CA", "CA-loc") and (C.registrable(host_of(o.get("url") or "") or d) != d or pcnt[d] >= 3):
            return False
        return True
    have, known = {d: o for d, o in vendor_state().items() if settled(d, o)}, proven_elsewhere()
    tasks = [{"dom": v, "n": c} for v, c in cnt.most_common() if v not in have and v not in known and shard_ok(v, k, n) and not PLATFORM.search(v)]
    try:  # providers named by many organisations' DNS records (tools/dns_services.py): the same live proof of location decides
        import dns_services as DNS
        queued = {t["dom"] for t in tasks}
        tasks += [{"dom": v, "n": c} for v, c in DNS.candidates() if v not in have and v not in queued and shard_ok(v, k, n)]
    except Exception as e:
        print("DNS providers not queued: %s" % e, flush=True)
    if os.path.exists(GRAPH_MT):  # multi-tenant platforms of the web graph: which of them are in Canada? (the most host names first)
        queued = {t["dom"] for t in tasks}
        with gzip.open(GRAPH_MT, "rt", encoding="utf-8", newline="") as fh:
            mt = sorted(((int(r["hosts"] or 0), r["dom"]) for r in csv.DictReader(fh)), reverse=True)
        tasks += [{"dom": d, "n": h} for h, d in mt if d not in have and d not in queued and shard_ok(d, k, n)]
    # the row factory's vendors whose client page (and archived contact page) printed no address: 11,096 domains, 39,313 buyer domains wait on them.
    # Their live home / contact / legal page is read the same way; tools/cc_clients.py merge promotes their client links when the proof is found.
    rf = collections.Counter()
    for o in CCL._side_records():
        vd = ((o.get("row") or {}).get("vendor_key") or "")[3:]
        if vd:
            rf[vd] += 1
    queued = {t["dom"] for t in tasks}
    arch = CCL._vendor_addrs()
    tasks += [{"dom": v, "n": c} for v, c in rf.most_common() if v not in have and v not in arch and v not in queued and shard_ok(v, k, n) and not PLATFORM.search(v)]
    if a.limit:
        tasks = tasks[:a.limit]
    print("shard %d/%d: %d credited vendor domains to check (%d checked before, %d proven by the row factory)" % (k, n, len(tasks), len(have), len(known)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fv = open("out/credit_vendors_%d.jsonl" % k, "a", encoding="utf-8")
    ADDRS = (("CA", CCL.ADDR), ("US", LC.US_ADDR), ("GB", LC.GB_ADDR), ("AU", LC.AU_ADDR))

    def addresses_in(raw):
        """{country: quote} for every postal address form found on one page (visible text, then schema.org data in the source), + the location line"""
        text, out = C.visible(raw), {}
        for cc, rx in ADDRS:
            for m in rx.finditer(text):
                if HOST_LABEL.search(text[max(0, m.start() - 130):m.start()]):
                    continue  # the address of the site's hosting provider, named in its legal notice
                out[cc] = re.sub(r"^\S*\s", "", text[max(0, m.start() - 110):m.end()].strip())[-200:]
                break
        if "CA" not in out:
            j = jsonld_address(raw)
            if j:
                out["CA"] = "%s (schema.org PostalAddress in the page source)" % j
        loc, phone = location_line(text)
        if loc:
            out["loc"] = "%s … tel. %s" % (loc, phone)
        return out

    def one(t):
        if time.time() > deadline:
            return
        dom = t["dom"]
        rec = {"dom": dom, "date": TODAY, "seen_on": t["n"], "status": "", "quote": "", "url": "", "name": "", "title": "", "desc": "", "service_words": "", "also_prints": "", "rule": 3}
        try:
            res, final, raw = get_page("https://%s/" % dom)
            if res != "ok":
                rec["status"] = res
            else:
                fhost = host_of(final) or dom
                title, meta = T.page_meta(raw)
                home_text = C.visible(raw)
                if C.registrable(fhost) != dom:  # the credited domain now leads to another one: a rebrand when that site still names the old one
                    lab = re.sub(r"[^a-z0-9]", "", dom.split(".")[0])
                    flat = re.sub(r"[^a-z0-9]", "", home_text.lower())
                    rec["final"] = C.registrable(fhost)
                    rec["renamed"] = bool(dom in raw.lower() or (len(lab) >= 5 and lab in flat))
                fs_ = FREE_SIGNAL.search(home_text)
                if fs_:
                    rec["free_signal"] = re.sub(r"\s+", " ", home_text[max(0, fs_.start() - 40):fs_.end() + 40]).strip()
                rec["name"] = LC.site_name_for(fhost, meta.get("og:site_name"), title, T)
                rec["title"], rec["desc"] = (title or "")[:160], (meta.get("description") or meta.get("og:description") or "")[:240]
                sw = SERVICE_RX.search(rec["title"] + " " + rec["desc"])
                rec["service_words"] = sw.group(0) if sw else ""
                found = {}  # country (or "loc") -> (quote, url); a Canadian postal address anywhere on the pages read wins
                for cc, q in addresses_in(raw).items():
                    found[cc] = (q, final)
                if "CA" not in found:
                    links, seen_l = [], set()
                    for link, label in C.links(raw, final):
                        p = urllib.parse.urlparse(link)
                        lh = (p.hostname or "").lower()
                        own = lh == fhost or lh == "www." + fhost or (C.registrable(lh) == C.registrable(fhost) and OWN_SUB.match(lh[:-len(C.registrable(fhost))].rstrip(".") or "www"))
                        if p.scheme in ("http", "https") and own and not C.SKIP_EXT.search(p.path) \
                                and CONTACT_RX.search(p.path + " " + label) and link.split("#")[0] not in seen_l and link.split("#")[0].rstrip("/") != final.rstrip("/"):
                            seen_l.add(link.split("#")[0])
                            links.append((0 if re.search(r"contact|joindre|coordonn", p.path + " " + label, re.I) else 1, len(p.path), link.split("#")[0]))
                    todo = [u for _, _, u in sorted(links)[:4]] or ["https://%s/contact" % fhost, "https://%s/contact-us" % fhost, "https://%s/nous-joindre" % fhost]
                    for u in todo:
                        if time.time() > deadline + 120:
                            break
                        r2, f2, raw2 = get_page(u, check_robots=False) if C.allowed(u) else ("robots", u, "")
                        if r2 != "ok":
                            continue
                        for cc, q in addresses_in(raw2).items():
                            found.setdefault(cc, (q, f2))
                        if "CA" in found:
                            break
                other = sorted(c for c in found if c not in ("CA", "loc"))
                rec["also_prints"] = ",".join(other)
                if "CA" in found:
                    rec["status"], rec["quote"], rec["url"] = "CA", found["CA"][0], found["CA"][1]
                elif other:  # a postal address elsewhere and none in Canada: located there
                    rec["status"], rec["quote"], rec["url"] = other[0], found[other[0]][0], found[other[0]][1]
                elif "loc" in found:  # no postal code anywhere: the site's own location line (a Canadian province) + a Canadian telephone number
                    rec["status"], rec["quote"], rec["url"] = "CA-loc", found["loc"][0], found["loc"][1]
                else:
                    rec["status"] = "no_address"
        except Exception as e:
            rec["status"] = "error:" + type(e).__name__
        with lock:
            stats["vendors"] += 1
            stats[rec["status"].split(":")[0] if not rec["status"].startswith("http_") else "http_error"] += 1
            fv.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if stats["vendors"] % 500 == 0:
                fv.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    def on_timeout(t):
        with lock:
            fv.write(json.dumps({"dom": t["dom"], "date": TODAY, "seen_on": t["n"], "status": "timeout"}) + "\n")
            stats["timeout"] += 1
    left = LC.run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fv.close()
    print("finished", dict(stats), "(stragglers left: %d)" % left, flush=True)


# ------------------------------------------------------------------------------------------------------------------- merge
def credit_key(dom):
    """its own key: the same organisation may also be a client-listing lead (key of the linked domain); rank.py keeps one row per website domain"""
    return "lead:" + hashlib.sha1(("%s|credit:%s" % (dom, dom)).encode()).hexdigest()[:16]


def _append_state(prefix, stamp, lines):
    lines = [l for l in lines if l.strip()]
    if not lines:
        return 0
    os.makedirs(DIR, exist_ok=True)
    with gzip.open(os.path.join(DIR, "%s_%s.gz" % (prefix, stamp)), "wt", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return len(lines)


def merge(a):
    d, stamp = a.dir, a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    ver_before = done_versions()
    done_before = set(ver_before)
    new_done, st_count = {}, collections.Counter()
    for f in sorted(glob.glob(os.path.join(d, "credit_done_*.tsv"))):
        for l in open(f, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if q and q[0] and len(q) >= 3 and line_version(q) > ver_before.get(q[0], 0):
                new_done[q[0]] = l.rstrip("\n")
                st_count[q[2].split(":")[0] if not q[2].startswith("http_") else "http_error"] += 1
    n_done = _append_state("done", stamp, [new_done[k] for k in sorted(new_done)])
    new_seen = {}
    for f in sorted(glob.glob(os.path.join(d, "credit_seen_*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                o = json.loads(l)
                new_seen[o["dom"]] = json.dumps(o, ensure_ascii=False)
            except (ValueError, KeyError):
                pass
    n_seen = _append_state("seen", stamp, [new_seen[k] for k in sorted(new_seen)])
    vstate, new_v = vendor_state(), {}
    for f in sorted(glob.glob(os.path.join(d, "credit_vendors_*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                o = json.loads(l)
                old = vstate.get(o["dom"])
                if old is None or ((o.get("rule") or 1) > (old.get("rule") or 1) and o.get("status") in ("CA", "CA-loc", "US", "GB", "AU", "no_address")):
                    new_v[o["dom"]] = json.dumps(o, ensure_ascii=False)
            except (ValueError, KeyError):
                pass
    n_v = _append_state("vendors", stamp, [new_v[k] for k in sorted(new_v)])
    extc = collections.Counter()
    for f in sorted(glob.glob(os.path.join(d, "credit_ext_*.tsv"))):
        for l in open(f, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) == 2 and q[1].isdigit():
                extc[q[0]] += int(q[1])
    if extc:  # outside services loaded by the sites read in this run (top 20,000): a table to vet new Canada-based platforms from
        _append_state("ext", stamp, ["%s\t%d" % kv for kv in extc.most_common(20000)])
    new_lk, new_sec = {}, {}
    for f in sorted(glob.glob(os.path.join(d, "site_links_*.tsv"))):
        for l in open(f, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) in (3, 4) and q[0]:
                new_lk[q[0]] = l.rstrip("\n")
    for f in sorted(glob.glob(os.path.join(d, "site_sections_*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                new_sec[json.loads(l)["dom"]] = l.rstrip("\n")
            except (ValueError, KeyError):
                pass
    n_lk = _append_state("links", stamp, [new_lk[k] for k in sorted(new_lk)])
    n_sec = _append_state("sections", stamp, [new_sec[k] for k in sorted(new_sec)])
    if n_done or n_seen:
        print("credit scan: %d sites read this run (%s); %d with a credit or a vetted service" % (n_done, ", ".join("%s %d" % kv for kv in st_count.most_common(8)), n_seen))
    if n_lk or n_sec:
        n_num = sum('"n": [' in v for v in new_sec.values())
        n_st = sum('"st": [' in v for v in new_sec.values())
        print("home pages whose outside links / embedded services were kept: %d; with a sponsors / clients / members section, a printed register number or a stated affiliation: %d "
              "(register number %d, stated affiliation %d)" % (n_lk, n_sec, n_num, n_st))
    # ---- leads: sightings whose vendor is proven in Canada
    vstate, known_v, seen = vendor_state(), proven_elsewhere(), sightings()
    # 2026-11-11 (row audit): "also_prints" knew only American, British and Australian postal addresses. A vendor whose address quote itself shows
    # an office elsewhere ("Pakistan … BRANCH OFFICE CANADA", "France 50 rue Breteuil 13006 Marseille +33…  Montreal, Canada …") prints addresses
    # abroad too (offices_abroad): the same condition applies — its Canadian address counts only for a buyer shown to be in Canada
    for _o in vstate.values():
        if _o.get("status") in ("CA", "CA-loc"):
            _codes = {x for x in (_o.get("also_prints") or "").split(",") if x} | offices_abroad(_o.get("quote"))
            _o["also_prints"] = ",".join(sorted(_codes))
    n_multi = collections.Counter()
    hints = site_hints()

    def in_canada(site, o=None):
        """is the organisation behind this site in Canada? Asked only for vendors that also print addresses abroad (the buyer abroad may deal with the
        vendor's foreign company): a .ca / .quebec domain, or a Canadian postal address on its own home page"""
        return site.endswith((".ca", ".quebec")) or (o or {}).get("cc") == "CA" or (hints.get(site) or ("", ""))[1] == "CA"

    def proof(v):
        o = vstate.get(v)
        if FREE_PLAN.search(v) and re.search(r"cpanel|plesk|webpros|whmcs|softaculous|cloudlinux|litespeed|directadmin|presscustomizr", v):
            return None  # server software paid by the hosting company; a theme author whose legal notice printed its host's address
        if o and o.get("status") in ("CA", "CA-loc") and (not proof_page_ok(v, o) or HOST_LABEL.search((o.get("quote") or "")[:-12])):
            return None
        if o and o.get("status") in ("CA", "CA-loc") and len([x for x in (o.get("also_prints") or "").split(",") if x]) >= 2 and not v.endswith((".ca", ".quebec")):
            # addresses in two or more other countries and no .ca domain: a multinational whose Canadian address is one office among others
            # (Cloudflare's representative in Vancouver, Zoho's office in Cornwall, Mimecast's in Mississauga) — which of its companies a customer
            # deals with is not shown. Vendors read by hand (their own agreement names the contracting company) do not come through here.
            n_multi[v] += 1
            return None
        if o and INTERNAL_RX.search("%s %s" % (o.get("name") or "", o.get("title") or "")) and not o.get("service_words"):
            return None
        if o and o.get("status") == "CA" and o.get("quote"):
            return ("%s (as printed on %s, read %s)" % (CCL.address_from(o["quote"]) if "schema.org" not in o["quote"] else o["quote"], o.get("url") or "", o.get("date") or ""), o.get("url") or "", o.get("name") or "",
                    bool(o.get("service_words")), "the vendor's own site prints its Canadian postal address")
        if o and o.get("status") == "CA-loc" and o.get("quote"):
            return ("“%s” (as printed on %s, read %s)" % (o["quote"], o.get("url") or "", o.get("date") or ""), o.get("url") or "", o.get("name") or "",
                    bool(o.get("service_words")), "the vendor's own site gives its location in Canada and a Canadian telephone number (no postal code printed)")
        if v in known_v:
            return known_v[v] + (True, "the vendor's own site prints its Canadian postal address")  # the row factory read its client / portfolio page: a firm that sells services
        return None
    main_keys = set()
    mp = os.path.join(INC, "claude_buyer_leads.csv")
    if os.path.exists(mp):
        main_keys = {r["buyer_key"] for r in csv.DictReader(open(mp, encoding="utf-8", errors="replace"))}
    prev, pdet = {}, {}
    _lead_shards = bool(getattr(a, "lead_shards", False))
    if _lead_shards:
        # 2026-11-10 (tools/lead_store.py): base files frozen; this run's changes go to lead_shards/ (see cc_clients.merge)
        import lead_store as _LS
        _lstamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
        prev, pdet = _LS.load(exclude=("cs", _lstamp))
        _snap = _LS.snapshot(prev, pdet)
    else:
        if os.path.exists(CCL.LEADS_CC):
            prev = {r["buyer_key"]: r for r in csv.DictReader(open(CCL.LEADS_CC, encoding="utf-8"))}
        if os.path.exists(CCL.DETAILS_CC):
            for l in gzip.open(CCL.DETAILS_CC, "rt", encoding="utf-8"):
                try:
                    o = json.loads(l)
                    pdet[o["key"]] = o
                except (ValueError, KeyError):
                    pass
    stats, kept = collections.Counter(), set()
    try:
        import tech_relationships as T
        VETTED = set(T.VENDOR_BASES)
    except Exception:
        VETTED = set()
    vend_n = collections.Counter(c["v"] for o in seen.values() for c in (o.get("credits") or []))
    for dom in sorted(seen):
        o = seen[dom]
        site = o.get("site") or dom
        best = None
        for c in o.get("credits") or []:
            if c["k"] == "M":
                stats["membership statements seen"] += 1
                continue
            stats["credit links seen"] += 1
            v = c["v"]
            if v == C.registrable(site) or (c["k"] == "P" and FREE_PLAN.search(v)) or vend_n[v] > 20000 or v in VETTED:
                continue  # the vetted software vendors have their own acceptance rules (tools/tech_relationships.py): never through a credit line
            pr = proof(v)
            if not pr:
                stats["vendor not proven in Canada (yet)"] += 1
                continue
            vo = vstate.get(v) or {}
            if c["k"] == "P" and vo.get("free_signal"):
                stats["'powered by' platform that advertises a free plan (kept out)"] += 1
                continue
            if vo.get("also_prints") and not in_canada(site, o):
                stats["vendor also prints addresses abroad and the buyer is not shown to be in Canada (kept out)"] += 1
                continue
            if c["k"] in ("D", "P") and vend_n[v] < 2 and not pr[3]:
                stats["design / powered-by credit of a vendor seen once whose own site names no web / design / software service (kept out)"] += 1
                continue
            if best is None or "WDP".index(c["k"]) < "WDP".index(best[0]["k"]):
                best = (c, pr)
        # membership stated on the member's own site -> its own lead (dues: the member pays the body), when the body is proven in Canada
        for c in o.get("credits") or []:
            if c["k"] != "M" or c["v"] == C.registrable(site) or c["v"] in VETTED:
                continue
            pr = proof(c["v"])
            if not pr or ((vstate.get(c["v"]) or {}).get("also_prints") and not in_canada(site, o)):
                continue
            bname = pr[2] or re.sub(r"^.*?(?:members?|membres?)\s+(?:of|de|du|des|de\s+la|de\s+l['’]|d['’])\s*(?:(?:the|la|le|les|l['’])\s*)?", "", c.get("t") or "", flags=re.I).strip()[:90] or c["v"]
            if not BODY_RX.search(bname + " " + (c.get("t") or "")):
                continue
            mkey = "lead:" + hashlib.sha1(("%s|member:%s" % (site, c["v"])).encode()).hexdigest()[:16]
            if mkey in main_keys:
                continue
            stats["new member leads" if mkey not in prev else "member leads kept"] += 1
            kept.add(mkey)
            prev[mkey] = {"buyer_key": mkey, "buyer_name": o.get("name") or site, "website": "https://%s/" % site, "canadian_vendor_rows": 1, "example_vendor": bname,
                          "canada_field_value": "membership / statutory fee relationship (member badge on the buyer's own site)=%s; %s: %s" % (c["v"], pr[4], pr[0][:240]),
                          "evidence_dataset": o.get("page") or "https://%s/" % site, "latest_record_date": o.get("date") or TODAY}
            pdet[mkey] = {"key": mkey, "platform": "site_member_cc", "record_url": o.get("page") or "", "vendor": bname, "record_date": o.get("date") or "",
                          "title": "membership of %s — stated on the member's own site: “%s”" % (bname, c["q"][-180:]),
                          "vendor_address": pr[0], "vendor_address_url": pr[1], "vendor_site": "https://%s/" % c["v"], "credit_quote": c["q"], "credit_class": "M",
                          "credit_link_text": c.get("t") or "", "vendor_location_basis": pr[4], "page_title": o.get("title") or ""}
            break
        if not best:
            continue
        c, pr = best
        key = credit_key(site)
        if key in main_keys:
            continue
        vname = pr[2] or c["v"]
        what = {"W": "website / web services", "D": "design / web services", "P": "software / platform"}[c["k"]]
        if key not in prev:
            stats["new leads"] += 1
        stats["leads (%s)" % what] += 1
        kept.add(key)
        prev[key] = {"buyer_key": key, "buyer_name": o.get("name") or site, "website": "https://%s/" % site, "canadian_vendor_rows": 1, "example_vendor": vname,
                     "canada_field_value": "%s=%s; %s: %s" % (CF_CREDIT, c["v"], pr[4], pr[0][:260]),
                     "evidence_dataset": o.get("page") or "https://%s/" % site, "latest_record_date": o.get("date") or TODAY}
        pdet[key] = {"key": key, "platform": "site_credit_cc", "record_url": o.get("page") or "", "vendor": vname, "record_date": o.get("date") or "",
                     "title": "%s by %s — credit printed on the buyer's own site: “%s”" % (what, vname, c["q"][-180:]),
                     "vendor_address": pr[0], "vendor_address_url": pr[1], "vendor_site": "https://%s/" % c["v"], "credit_quote": c["q"], "credit_class": c["k"], "credit_phrase": c.get("p") or "",
                     "credit_link_text": c.get("t") or "", "credit_link_host": c.get("vh") or c["v"], "vendor_seen_on_sites": vend_n[c["v"]], "page_title": o.get("title") or "",
                     "vendor_location_basis": pr[4], "vendor_also_prints_addresses_in": (vstate.get(c["v"]) or {}).get("also_prints") or ""}
    # ---- services the organisations' own DNS records show (tools/dns_services.py), same proof of the provider's location
    try:
        import dns_services as DNS
        DNS.leads(prev, pdet, proof, main_keys, vstate, stats, {d: (o.get("name") or "") for d, o in seen.items()}, in_canada, kept)
    except Exception as e:
        print("DNS leads skipped: %s" % e)
    if n_multi:
        stats["vendors that print addresses in two or more other countries and have no .ca domain (multinational: its Canadian office is not shown to be the contracting company; kept out)"] = len(n_multi)
    # a credit / member-badge / DNS lead of an earlier run that the rules of this run no longer make is withdrawn (rules get stricter as leads are read)
    gone = [k for k, r in prev.items() if k not in kept and (pdet.get(k) or {}).get("platform") in ("site_credit_cc", "site_member_cc", "dns_service_cc")]
    for k in gone:
        prev.pop(k, None)
        pdet.pop(k, None)
    if gone:
        stats["leads of earlier runs withdrawn (no longer pass the rules)"] = len(gone)
    if _lead_shards:
        _nu, _nd, _ng = _LS.save("cs", _lstamp, prev, pdet, _snap)
        stats["lead shards of this run: rows"] = _nu; stats["lead shards of this run: details"] = _nd; stats["lead shards of this run: withdrawn"] = _ng
    else:
        with open(CCL.LEADS_CC, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CCL.LEAD_COLS)
            w.writeheader()
            for k in sorted(prev):
                w.writerow({c: prev[k].get(c, "") for c in CCL.LEAD_COLS})
        with gzip.open(CCL.DETAILS_CC, "wt", encoding="utf-8") as f:
            for k in sorted(pdet):
                f.write(json.dumps(pdet[k], ensure_ascii=False) + "\n")
    # ---- vetted Canada-HQ software services seen on the site -> candidates (accepted only with a role mailbox + an address in the vendor's scope)
    n_c = 0
    try:
        import cc_tenants as CT
        cands = {}
        if os.path.exists(CT.CANDS):
            with gzip.open(CT.CANDS, "rt", encoding="utf-8", newline="") as fh:
                cands = {r["cand_key"]: r for r in csv.DictReader(fh)}
        by_host = {CCL.base((urllib.parse.urlparse(r["website"]).hostname or "").lower()) for r in cands.values()}
        n_shop = 0
        lead_hosts = {host_of(r.get("website")) for r in prev.values() if "(tech)" in (r.get("canada_field_value") or "") and "credited" not in (r.get("canada_field_value") or "")}
        lead_hosts |= {host_of(r.get("website")) for r in CT.tenant_leads()}  # accepted since 2026-11-10: in the shards of tenant_state/
        for dom in sorted(seen):
            o = seen[dom]
            site = o.get("site") or dom
            for x in o.get("tech") or []:
                vk = x["v"]
                if vk == "shopify" and (x.get("country") or "") not in ("", "CA", "US"):
                    continue
                ck = "t:%s:%s" % (vk, site if x["slug"] == "asset" else x["slug"])
                if ck in cands or site in by_host or site in lead_hosts or (vk == "shopify" and n_shop >= a.max_shopify):
                    continue
                n_shop += vk == "shopify"
                cands[ck] = {"cand_key": ck, "vendor_key": vk, "name": o.get("name") or "", "website": "https://%s/" % site, "evidence_url": o.get("page") or "", "capture": o.get("date") or "",
                             "name_basis": "og:site_name / title of the organisation's own home page" if o.get("name") else "",
                             "website_basis": "%s (%s, read %s)" % (x.get("how") or "seen on the organisation's own page", o.get("page") or "", o.get("date") or ""),
                             "slug": x["slug"], "extra": json.dumps({"seen_on": o.get("page"), "via": x.get("via"), "portal": x.get("purl"), "portal_check": 1 if vk == "jane" else 0,
                                                                     "shopify_country": x.get("country") or ""}, ensure_ascii=False)}
                by_host.add(site)
                n_c += 1
                stats["vetted service candidates: " + vk] += 1
        # 2026-11-11: the outside links the scan keeps for every home page (detector 5: links_<stamp>.gz) name the site's account at a vetted service
        # too. A vendor vetted after a page was read gets its candidates from the links on file — no new read of the page; the candidate reader
        # then reads the site (role mailbox, address in the vendor's scope) and checks that the account is the site's own.
        try:
            import tech_relationships as _T
            # asset vendors whose pattern can be told from an embedded host alone (the links file keeps the host of what a page loads, and the path
            # only for the watched services); Shopify has its own, larger path
            _assets = [(k_, v_["asset_re_c"]) for k_, v_ in _T.VENDORS.items() if v_.get("kind") == "asset" and v_.get("asset_re_c") and k_ != "shopify"]
            for lf in sorted(glob.glob(os.path.join(DIR, "links_*.gz"))):
                _day = re.sub(r"^(\d{4})(\d\d)(\d\d).*$", r"\1-\2-\3", os.path.basename(lf)[6:])
                with gzip.open(lf, "rt", encoding="utf-8", errors="replace") as fh:
                    for l in fh:
                        q = l.rstrip("\n").split("\t")
                        if len(q) < 3 or not q[0] or q[0] in by_host or q[0] in lead_hosts:
                            continue
                        site = q[0]
                        for key in q[1].split() + q[2].split():
                            hits = [h for h in _T.portal_hits("https://" + key) if h[0] != "shopify"]
                            if not hits:
                                continue
                            vk, slug, purl = hits[0]
                            ck = "t:%s:%s" % (vk, slug)
                            if ck in cands:  # the same account linked from another site, or a portal host shared by every customer: one candidate per site
                                ck = "t:%s:%s" % (vk, site)
                            if ck in cands:
                                break
                            nm = (q[3].split("|")[0] if len(q) > 3 else "").strip()
                            cands[ck] = {"cand_key": ck, "vendor_key": vk, "name": nm, "website": "https://%s/" % site, "evidence_url": "https://%s/" % site, "capture": _day,
                                         "name_basis": "og:site_name / title of the organisation's own home page" if nm else "",
                                         "website_basis": "the organisation's own home page links its account at the service: %s (https://%s/, read %s)" % (key[:120], site, _day),
                                         "slug": slug, "extra": json.dumps({"seen_on": "https://%s/" % site, "via": "link on the home page (%s)" % key[:120], "portal": purl,
                                                                            "portal_check": 1 if vk == "jane" else 0}, ensure_ascii=False)}
                            by_host.add(site)
                            n_c += 1
                            stats["vetted service candidates (links on file): " + vk] += 1
                            break
                        # … and the services whose scripts or images the page loads (asset vendors vetted after the page was read: Commerce7's
                        # cdn.commerce7.com, myRealPage's iss-cdn.myrealpage.com …): the embedded hosts are on file too
                        if site in by_host or not q[1]:
                            continue
                        for key in q[1].split():
                            vk = next((k_ for k_, v_ in _assets if v_.search("//" + key)), "")
                            if not vk:
                                continue
                            ck = "t:%s:%s" % (vk, site)
                            if ck in cands:
                                break
                            nm = (q[3].split("|")[0] if len(q) > 3 else "").strip()
                            cands[ck] = {"cand_key": ck, "vendor_key": vk, "name": nm, "website": "https://%s/" % site, "evidence_url": "https://%s/" % site, "capture": _day,
                                         "name_basis": "og:site_name / title of the organisation's own home page" if nm else "",
                                         "website_basis": "asset loaded by the organisation's own home page: %s (https://%s/, read %s)" % (key[:120], site, _day),
                                         "slug": "asset", "extra": json.dumps({"seen_on": "https://%s/" % site, "via": "loaded by the home page (%s)" % key[:120]}, ensure_ascii=False)}
                            by_host.add(site)
                            n_c += 1
                            stats["vetted service candidates (assets on file): " + vk] += 1
                            break
        except Exception as e:
            print("candidates from the links on file skipped: %s" % e)
        if n_c:
            with gzip.open(CT.CANDS, "wt", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=CT.CAND_COLS)
                w.writeheader()
                for k in sorted(cands):
                    w.writerow({c: cands[k].get(c, "") for c in CT.CAND_COLS})
    except Exception as e:  # the credit leads must land even when the candidates file cannot be read
        print("vetted-service candidates skipped: %s" % e)
    try:
        if os.path.exists(GRAPH_MT):
            with gzip.open(GRAPH_MT, "rt", encoding="utf-8", newline="") as fh:
                mt = {r["dom"]: int(r["hosts"] or 0) for r in csv.DictReader(fh)}
            vetted_dom = set()
            try:
                import tech_relationships as _T
                vetted_dom = set(_T.VENDOR_BASES)
            except Exception:
                pass
            pc = [(h, d, vstate[d]) for d, h in mt.items() if d in vstate and vstate[d].get("status") in ("CA", "CA-loc")]
            with open(PLATFORM_CANDS, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["domain", "host_names_in_web_graph", "in_vendor_table", "name", "title", "description", "address_quote", "address_url", "also_prints_addresses_in", "free_plan_signal", "checked"])
                for h, d, o in sorted(pc, reverse=True):
                    w.writerow([d, h, "yes" if d in vetted_dom or C.registrable(o.get("final") or d) in vetted_dom else "", o.get("name") or "", o.get("title") or "", o.get("desc") or "",
                                (o.get("quote") or "")[:200], o.get("url") or "", o.get("also_prints") or "", (o.get("free_signal") or "")[:80], o.get("date") or ""])
            print("multi-tenant domains of the web graph: %d; checked live %d; printing a Canadian address %d (platform_candidates.csv — to vet for the vendor table)"
                  % (len(mt), sum(1 for d in mt if d in vstate), len(pc)))
    except Exception as e:
        print("platform candidates skipped: %s" % e)
    vs = collections.Counter((o.get("status") or "?").split(":")[0] for o in vstate.values())
    todo_v = sum(1 for v in vend_n if v not in vstate and v not in known_v)
    print("credit leads: %s" % dict(stats))
    print("credit scan totals: sites read %d, sites with a credit or vetted service %d, credited vendor domains %d (checked live %d: %s; proven by the row factory %d; waiting %d), %d (+%d new) vendor checks this run; "
          "credit leads in %s: %d" % (len(done_before) + n_done, len(seen), len(vend_n), len(vstate), dict(vs.most_common(6)), sum(1 for v in vend_n if v in known_v), todo_v, n_v, n_v,
                                      os.path.basename(CCL.LEADS_CC), sum(1 for r in prev.values() if "credited on the buyer's own site" in (r.get("canada_field_value") or ""))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["universe", "merge-universe", "graph", "osm", "overture", "lists", "merge-graph", "scan", "vendors", "merge"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--crawl", default="auto")
    ap.add_argument("--minutes", type=float, default=150)
    ap.add_argument("--workers", type=int, default=120)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default="")
    ap.add_argument("--release", default="auto", help="graph: web-graph release id (auto = newest)")
    ap.add_argument("--work", default="", help="graph: directory for the downloaded files")
    ap.add_argument("--base", default="", help="graph: URL prefix of the vertices / edges files (tests)")
    ap.add_argument("--max-indegree", type=int, default=5000, help="graph: a vendor linked from more domains than this is platform-like (its links are not credits)")
    ap.add_argument("--max-shopify", type=int, default=15000, help="merge: at most this many new Shopify-store candidates per run (owner 2026-11-09: no lane may crowd out the others)")
    ap.add_argument("--lead-shards", action="store_true", help="merge: write this run's lead changes as shards of lead_shards/ (tools/lead_store.py) instead of rewriting the two big files")
    ap.add_argument("--straggler-seconds", type=float, default=180)
    ap.add_argument("--site-seconds", type=float, default=150)
    a = ap.parse_args()
    if a.cmd in ("scan", "vendors"):
        os.makedirs(C.STATE, exist_ok=True)
        {"scan": scan, "vendors": vendors}[a.cmd](a)
        sys.stdout.flush()
        os._exit(0)  # do not wait for straggler threads
    {"universe": universe, "merge-universe": merge_universe, "graph": graph, "osm": osm, "overture": overture, "lists": lists, "merge-graph": merge_graph, "merge": merge}[a.cmd](a)


if __name__ == "__main__":
    main()
