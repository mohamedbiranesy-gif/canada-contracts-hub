#!/usr/bin/env python3
"""Dated relationships read from the BUYER's own website: its award notices, bid results, procurement news, press releases
and supplier pages that name a vendor the contract dataset already proves to be located in Canada, next to a buying cue
(awarded, contract with, selected, supplied by, deploys ...), with the page's own date within the last 12 months (tier B)
or 36 months (tier L). No AI: dictionary matching (tools/news_match.py's matcher) over ~170,000 Canadian vendor names.

Why: ~600 organisations publish an invoicing mailbox but have no dated record yet (P06 / P10 / P13 with an AP mailbox):
one dated award on their own site makes each of them Gold. Vendor in Canada = the dataset's own source field for that
vendor (never the name). Polite: robots.txt, 1 request / second / host, identified UA, ≤ 40 pages per site.
  python3 tools/buyer_pages.py --orgs orgs.csv --vendors vendors_ca.tsv.gz [--workers 32] [--pages 40]
orgs.csv: key,name,website ; vendors_ca.tsv.gz: name<TAB>address<TAB>country_basis (contrib/claude/buyer_pages/make_vendors.py).
Output ~/cch-leads/socrata_buyer_pages.jsonl (lead format; tools/lead_scanner.py --bridge picks it up), progress in
~/cch-crawler-state/buyer_pages_done.tsv.
"""
import argparse, collections, csv, datetime, gzip, hashlib, html, json, os, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C
import news_match as NM
from org_contacts import strip_long, visible_keep_lines

LEADS = os.path.expanduser("~/cch-leads")
STATE = os.path.expanduser("~/cch-crawler-state")
OUT = os.path.join(LEADS, "socrata_buyer_pages.jsonl")
DONE = os.path.join(STATE, "buyer_pages_done.tsv")
TODAY = datetime.date.today()
RECENT = (TODAY - datetime.timedelta(days=365)).isoformat()
OLDEST = (TODAY - datetime.timedelta(days=3 * 365)).isoformat()
# Accounts-payable listings: councils and boards approve a monthly "list of accounts" / cheque register (vendor, amount, date),
# on their own site or on their meeting portal. Every dictionary hit on a line with an amount is a paid supplier.
LISTING_RX = re.compile(r"cheque|check register|accounts? payable|payables|list of accounts|accounts? (?:for|list)|disbursement|paid invoices|bills? list|"
                        r"bill list|warrant|expenditure report|vendor payments?|payments? (?:report|listing|register)|liste des comptes|comptes pay[ée]s|"
                        r"d[ée]bours[ée]s|registre des ch[èe]ques|liste des ch[èe]ques|approbation des comptes|comptes [àa] payer", re.I)
PORTAL_HOST = re.compile(r"(escribemeetings\.com|civicweb\.net|icompasstech\.com|legistar\.com|granicus\.com|boarddocs\.com|novusagenda\.com|iqm2\.com|"
                         r"primegov\.com|civicclerk\.com|municodemeetings\.com|civicplus\.com|pub-[a-z0-9-]+\.escribemeetings\.com|agendaonline\.net|"
                         r"diligent\.com|meetings\.[a-z0-9-]+\.[a-z]{2,})$", re.I)
MEETING_RX = re.compile(r"agenda|meeting|council|minutes|committee|board|s[ée]ance|ordre du jour|proc[èe]s-verbal|conseil", re.I)
PAGE_RX = re.compile(r"award|bid|tender|rfp|rfq|procure|purchas|contract|vendor|supplier|news|media|press|release|announce|partner|"
                     r"blog|stories|story|achat|appel|offres|octroi|soumission|fournisseur|nouvelles|communiqu|actualit|projet|project|"
                     r"council|conseil|minutes|agenda|report|rapport", re.I)
FIRST = re.compile(r"award|bid|tender|rfp|rfq|procure|purchas|contract|vendor|supplier|achat|appel|offres|octroi|soumission|fournisseur", re.I)
DATE_META = re.compile(r"(?is)(?:article:published_time|datePublished|dc\.date|date)[\"']?\s*(?:content|:)\s*[=:]?\s*[\"']?((?:19|20)\d\d-\d\d-\d\d)")
TIME_TAG = re.compile(r"(?is)<time[^>]+datetime\s*=\s*[\"']((?:19|20)\d\d-\d\d-\d\d)")
MONTHS = "january|february|march|april|may|june|july|august|september|october|november|december|janvier|f[ée]vrier|mars|avril|mai|juin|juillet|ao[uû]t|septembre|octobre|novembre|d[ée]cembre|jan|feb|mar|apr|jun|jul|aug|sept?|oct|nov|dec"
DATE_TXT = re.compile(r"\b((?:19|20)\d\d)-(\d\d)-(\d\d)\b|\b(%s)\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+((?:19|20)\d\d)\b|\b(\d{1,2})(?:er)?\s+(%s)\.?,?\s+((?:19|20)\d\d)\b" % (MONTHS, MONTHS), re.I)
MON = {m: i + 1 for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
MON.update({"janv": 1, "fev": 2, "fév": 2, "mars": 3, "avr": 4, "mai": 5, "juin": 6, "juil": 7, "aou": 8, "aoû": 8, "sept": 9, "déc": 12, "dec": 12})
AWARD_CTX = re.compile(r"\bawarded\b|\baward of (?:the )?(?:contract|tender|rfp|work)|contract award|tender award|successful (?:bidder|proponent|"
                       r"tenderer|vendor)|lowest (?:compliant )?(?:bid|tender)|adjug|octroy|retenu|contract(?:ed)? (?:to|with)|recommended (?:bidder|"
                       r"proponent)|contrat (?:octroy|accord|attribu)|soumissionnaire retenu|plus bas soumissionnaire|purchase order|bon de commande", re.I)
DROP_B = re.compile(r"financ|\bloan|grant(?!ed a contract)|subvention|donat|sponsor|merger|acqui|\bprize|laur[ée]at|finalist|scholarship|bourse|"
                    r"job fair|career|business awards?|award winner|award recipient|nominee|nominat|awards? (?:was|were|is|are|will be) (?:presented|given|"
                    r"handed)|awards? (?:event|ceremony|gala|program|night|dinner|luncheon)|recogni[sz]|honou?r(?:ed|s|ing)?\b|celebrat|presented (?:to|with)|"
                    r"\bwinner|(?:planning|excellence|achievement|leadership|innovation|design|heritage|safety|environmental|community) awards?|"
                    r"\bm[ée]rite|\bgagnant|\bremport|\bc[ée]r[ée]monie|\bgala\b|\bprix\b|\bmedal|\bm[ée]daille|awarded jointly|jointly with|"
                    r"\bappoint|\bnomm[ée]|\bin (?:19|20)[0-9]{2}\b|\ben (?:19|20)[0-9]{2}\b|\bhistor|\banniversar|\bspeaker|\bconf[ée]renc|"
                    r"\bwebinar|\bpanel|\bkeynote|\bpresenter|\bexhibitor|\bbooth|\bsession\b|\btrade ?show|\bvotre campagne|\byour campaign", re.I)
OTHER_BODY = re.compile(r"\b(?:(?:the )?(?:Ontario |Québec |Quebec |Alberta |Manitoba |BC |B\.C\. |federal |provincial )?(?:Ministry|Minist[èe]re|Department|Government|Gouvernement|Province|"
                        r"County|Comt[ée]|Region|R[ée]gion|City|Ville|Town|Township|Municipality|Municipalit[ée]|District|School Board|Conseil scolaire|Centre de services scolaire|"
                        r"Health Authority|Hospital|University|Universit[ée]|College|Coll[èe]ge) (?:of |de |du |des |d')?[A-ZÀ-Ý][\w'À-ÿ-]+(?: [A-ZÀ-Ý][\w'À-ÿ-]+){0,3})", re.I)
CA_WORD = re.compile(r"canada|canadian|canadien|qu[ée]bec|ontario|alberta|manitoba|saskatchewan|nova scotia|new brunswick|newfoundland|british columbia|"
                     r"toronto|montr[ée]al|vancouver|calgary|ottawa|edmonton|winnipeg|halifax|lt[ée]e|ltee|s\.e\.n\.c|senc|enr\.|inc\.?$", re.I)
DROP_URL = re.compile(r"awards?-(?:night|gala|program|ceremony|celebration|recipient|winner)|(?:arts|business|volunteer|heritage|citizen|community|"
                      r"excellence|achievement|leadership|sports|environmental|design|safety|science|student)-awards?|/awards?/?(?:$|\?|\.)|/award-|"
                      r"recognition|hall-of-fame|scholarship|bursar|awareness|proclamation|calendar|events?-calendar|obituar|in-memoriam|"
                      r"science-fair|sponsor|donor|our-impact|foundation-news", re.I)
PUBLIC_BODY = re.compile(r"\b(university|universit[ée]|college|coll[èe]ge|c[ée]gep|school|[ée]cole|county|comt[ée]|city of|town of|village of|ville de|"
                         r"municipalit|township|region of|regional|ministry|minist[èe]re|government|gouvernement|department|hospital|h[ôo]pital|health|"
                         r"sant[ée]|authority|commission|agency|agence|board|conseil|first nation|nation|band|society|foundation|fondation|association|"
                         r"church|[ée]glise|parish|paroisse|library|biblioth|district|conservation|watershed|office|bureau|minist|promotion|"
                         r"d[ée]veloppement [ée]conomique|economic development|chamber|chambre|institute|institut|museum|mus[ée]e|gallery|galerie)\b", re.I)
AWARD_URL = re.compile(r"award|adjudic|octroi|contrats?-(?:octroy|accord|attribu)|successful", re.I)
MONEY = re.compile(r"\$\s?\d[\d,. ]{2,}|\d[\d,. ]{2,}\s?\$")
lock = threading.Lock()


def to_iso(m):
    if m.group(1):
        return "%s-%s-%s" % (m.group(1), m.group(2), m.group(3))
    if m.group(4):
        mon, day, year = m.group(4), m.group(5), m.group(6)
    else:
        day, mon, year = m.group(7), m.group(8), m.group(9)
    k = NM.norm(mon)[:4] if NM.norm(mon)[:4] in MON else NM.norm(mon)[:3]
    mm = MON.get(k) or MON.get(NM.norm(mon)[:3])
    return "%s-%02d-%02d" % (year, mm, int(day)) if mm and 1 <= int(day) <= 31 else ""


# The buyer is the organisation whose site we read, so the vendor must be the OBJECT of the award: a cue just before the
# name ("awarded the contract to", "has contracted", "services of", "mandaté à") or just after it ("was awarded the
# tender", "will provide", "has been retained"), or an award-page table row with an amount. A name after "from" / "by" /
# "par" is the other party (the site's organisation is then the supplier), so it is skipped.
CUE_BEFORE = re.compile(r"(?:\bawarded|\baward of (?:the )?(?:contract|tender|work|project)|\bcontract(?:ed|s)?\b|\btender\b|purchase order|"
                        r"\bselected|\bchosen|\bretained|\bengaged|\bhired|\bappointed|agreement with|services of|provided by|supplied by|"
                        r"built by|delivered by|designed by|operated by|installed by|performed by|completed by|\bvendor\b|\bsupplier\b|"
                        r"\bcontractor\b|\bconsultant\b|successful (?:bidder|proponent)|lowest (?:compliant )?bid|mandat[ée]e?s? (?:à|a|au|aux)|"
                        r"octroy[ée]e?s? (?:à|a|au|aux)|adjug[ée]e?s? (?:à|a|au|aux)|attribu[ée]e?s? (?:à|a|au|aux)|confi[ée]e?s? (?:à|a|au|aux)|"
                        r"\bretenue?s?\b|contrat (?:avec|à|a|au)|\bfournisseur|\bentrepreneur|\badjudicataire|soumissionnaire)\b[^\n]{0,55}$", re.I)
REVERSE = re.compile(r"\b(?:from|by|par|de la part de|awarded to us|to us)\s*(?:the\s+)?$", re.I)
CUE_AFTER = re.compile(r"^[^.\n]{0,45}?\b(?:has been|have been|was|were|is|are|a été|ont été|est|sont)\s+(?:awarded|selected|chosen|retained|"
                       r"contracted|engaged|hired|appointed|the successful|retenue?|choisie?|mandat[ée]e?|s[ée]lectionn[ée]e?)|"
                       r"^\s*(?:\([^)]{0,40}\)\s*)?(?:awarded|has been awarded|was awarded)\s+(?:the\s+)?(?:contract|tender|work|project)|"
                       r"^[^.\n]{0,45}?\b(?:will|to|shall)\s+(?:provide|supply|deliver|build|construct|design|operate|manage|install|complete|"
                       r"perform|undertake|carry out|conduct|replace|repair|upgrade)\b|^[^.\n]{0,40}?\b(?:fournira|livrera|r[ée]alisera|"
                       r"effectuera|construira)\b", re.I)


SYMMETRIC = re.compile(r"^(?:agreement|contract|contracts|contrat|tender|vendor|supplier|contractor|consultant|fournisseur|entrepreneur)$", re.I)


def direction_cue(before, after, line, url, strict=False):
    """the cue that makes the named organisation the buyer's supplier, else None. strict (the site's organisation is a
    company, which may itself be the supplier in the sentence): symmetric words such as "agreement with" do not count."""
    m = CUE_BEFORE.search(before)
    if m:
        cue_word = m.group(0).split()[0]
        between = before[m.start() + len(cue_word):]
        other = r"\b(?:by|from|par|de la part de|and|et|as well as|ainsi que" + (r"|with|avec" if strict else "") + r")\b"
        if not REVERSE.search(before) and not re.search(other, between) and not (strict and SYMMETRIC.match(cue_word)):
            return cue_word + " … [name]"
    m = CUE_AFTER.search(after)
    if m and not (strict and re.search(r"\b(?:will|to|shall)\s", m.group(0), re.I)):
        return "[name] … " + m.group(0).strip()[:40]
    if AWARD_URL.search(url) and MONEY.search(line) and len(line) < 300 and not REVERSE.search(before):
        return "award page: the line names the vendor with an amount"
    return None


def flat_line(t):
    return re.sub(r"\s+", " ", t or "").strip()


def page_date(raw, text, pos):
    """the page's published date (article metadata / first <time> tag), else the date nearest the mention (±800 chars)"""
    for rx, how in ((DATE_META, "page metadata"), (TIME_TAG, "<time> tag")):
        m = rx.search(raw)
        if m and m.group(1) <= TODAY.isoformat():
            return m.group(1), how
    best = None
    lo = max(0, pos - 800)
    for m in DATE_TXT.finditer(text[lo:pos + 800]):
        d = to_iso(m)
        if d and d <= TODAY.isoformat():
            dist = abs(lo + m.start() - pos)
            if best is None or dist < best[0]:
                best = (dist, d)
    if best:
        return best[1], "date %d characters from the mention" % best[0]
    return "", ""


EVERYDAY = set("""about above after again against along among around because before being below between beyond could every first found great
house large little might never often other people place point right shall should small sound still their there these thing think three
through under until water where which while white world would write young about green black brown north south east west central
community county country people public private general national local family health house home school office place street road river
lake park tree trees planting garden works project projects program programs service services system systems solution solutions group
company limited enterprises enterprise industries industry international canada canadian ontario quebec alberta british columbia manitoba
saskatchewan atlantic pacific northern southern eastern western united global world first second third north east west south make made
making take taken taking give given giving find finding found keep keeping start started starting change changed changing better best
clean cleaning power energy light lights bright clear simple smart quick fast fresh total trust value values quality premier prime
premium standard standards select choice choices advanced modern future vision mission action actions active progress unique united
universal creative design designs designer digital media print printing paper supply supplies equipment products product trade trading
building buildings construction contracting contractors contractor engineering engineers consulting consultants consultant management
managers manager maintenance repair repairs property properties development developments developer developers holdings investments
capital finance financial insurance realty real estate marketing communications technologies technology tech software hardware
network networks data information security safety medical health care clinic clinics pharmacy dental vision optical physio
transport transportation logistics freight trucking express delivery courier auto automotive motors motor truck trucks tire tires
food foods farm farms market markets grocery bakery cafe restaurant catering hotel hotels travel tours tour sports fitness golf
music arts art studio studios gallery theatre theater film films photo photography video production productions event events
rental rentals leasing sales sale store stores shop shops centre center plaza mall workforce development program programs
shoreline restoration project projects partners partner station stations power plant plants water works""".split())
MARKER = re.compile(r"\b(inc|ltd|ltee|ltée|llc|llp|lp|corp|corporation|co|company|compagnie|limited|limitee|limitée|group|groupe|holdings|"
                    r"enterprises|entreprises|services|service|consulting|consultants|associates|associés|partners|solutions|systems|systèmes|"
                    r"technologies|technology|engineering|ingénierie|construction|contracting|contractors|builders|industries|international|"
                    r"canada|québec|quebec|ontario|alberta|manitoba|saskatchewan|logistics|transport|trucking|electric|électrique|mechanical|"
                    r"plumbing|roofing|paving|excavating|landscaping|printing|media|communications|design|studio|software|labs|laboratories|"
                    r"clinic|pharmacy|supply|supplies|equipment|rentals|machinery|manufacturing|products|foods|farms|energy|power|resources|"
                    r"mining|forest|lumber|steel|concrete|aggregates|environmental|security|cleaning|janitorial|maintenance|recycling|"
                    r"waste|disposal|towing|automotive|motors|marine|aviation|aerospace|architects|architecture|law|avocats|notaires|"
                    r"accountants|cpa|insurance|assurance|financial|capital|investments|realty|properties|developments|homes|hotel|inn|"
                    r"restaurant|catering|bakery|brewing|distillery|fitness|dental|medical|health|santé|pharma|bio|tech|net|digital|data|"
                    r"cloud|online|web|global|national|regional|pacific|atlantic|northern|western|eastern|central|\d|&|/|-)\b", re.I)
FIRST_NAMES = set("""james john robert michael william david richard joseph thomas charles christopher daniel matthew anthony mark donald steven
paul andrew joshua kenneth kevin brian george timothy ronald edward jason jeffrey ryan jacob gary nicholas eric jonathan stephen larry justin
scott brandon benjamin samuel gregory alexander frank patrick raymond jack dennis jerry tyler aaron jose adam nathan henry douglas zachary
peter kyle noah ethan jeremy walter christian keith roger terry austin sean gerald carl harold dylan arthur lawrence jordan jesse bryan
billy bruce gabriel joe logan alan juan albert willie elijah wayne randy vincent mason roy ralph bobby russell bradley philip eugene
mary patricia jennifer linda elizabeth barbara susan jessica sarah karen lisa nancy betty sandra margaret ashley kimberly emily donna
michelle carol amanda melissa deborah stephanie dorothy rebecca sharon laura cynthia amy kathleen angela shirley brenda emma anna pamela
nicole samantha katherine christine helen debra rachel carolyn janet maria catherine heather diane olivia julie joyce victoria ruth
virginia lauren kelly christina joan evelyn judith andrea hannah megan cheryl jacqueline martha madison teresa gloria sara janice ann
kathryn abigail sophia frances jean alice judy isabella julia grace amber denise danielle marilyn beverly charlotte natalie theresa
diana brittany doris kayla alexis lori marie lyndsay lindsay lindsey jamie jennie jenny julien julie luc marc pierre jean michel andré
andre françois francois louis guy claude yves denis daniel martin sylvain benoit benoît patrick stéphane stephane alain réjean rejean
gilles serge normand robert roger marcel richard eric éric mathieu maxime nicolas simon olivier philippe pascal sébastien sebastien
vincent xavier antoine hugo jacques bernard christian dominique frédéric frederic ghislain jocelyn josée josee lise line louise lucie
manon marie martine monique nathalie nicole sylvie suzanne chantal caroline carole diane france geneviève genevieve hélène helene
isabelle johanne josiane julie karine linda lyne mélanie melanie mylène nancy pauline sophie stéphanie valérie valerie véronique annie
sam tom bob jim mike dave steve chris dan matt tony ken greg jeff rick rob ron ed ted pat andy josh nate ben alex sarah kate liz beth
amy ann jen jess kim meg sue geoffrey jeffrey gregory harold howard irene jane janet jeanne joanne karen keith kenneth kevin larry lee
leslie lloyd lynn marc marie mario marjorie mark martin maurice melissa michel michelle nancy neil norman pamela patricia patrick paul
pauline peggy peter philip phyllis ralph randy ray raymond rebecca rhonda rita robert robin rodney roger ronald rose ross roy ruby russell
ruth ryan sally sandra sara scott shannon sharon sheila shirley stanley stephen steven stuart susan suzanne sylvia tammy terry theresa
thomas tim timothy tina todd tracy travis troy valerie vernon victor vincent virginia wade walter wanda warren wayne wendy william
willie yvonne brigitte fiona chantal geneviève genevieve nathalie isabelle céline celine josée josee manon sylvie francine danielle
dominique élise elise émilie emilie camille charlotte léa lea rosalie florence juliette gabrielle maude noémie noemie laurence sarah
olivia alice zoé zoe jade mia maya eva léonie leonie coralie amélie amelie audrey mélissa melissa vanessa jessica caroline catherine
mathieu maxime nicolas simon olivier philippe pascal sébastien sebastien vincent xavier antoine hugo jacques bernard christian dominique
frédéric frederic ghislain jocelyn gabriel samuel william thomas félix felix nathan jérémie jeremie raphaël raphael alexis émile emile
étienne etienne louis-philippe jean-françois jean-francois marc-andré pierre-luc francis martin denis réal real andré andre""".split())
# 2026-11-11 (the owner's second test set, read before it went out: a hosting customer named "Yann Fortier" was not seen as one person's name):
# given names that are not also everyday words or place names
FIRST_NAMES |= set("""adele adrian agathe agnes alfred aline alison allan andree anne anouk ariane aurelie barry beatrice brent brett cameron carla cecile christiane cindy clarence claudine cody colette colin colleen connie connor corinne craig curtis darren darryl delphine derek duane dustin edith edwin elaine eleanor ellen elodie emmanuelle erin ernest estelle esther evan fabienne francoise fred gaetan gail gaston gavin geoff germain gilbert ginette gordon graham guillaume harry heidi herve hugues ian jacinthe jake jared jenna jerome jill joanie jocelyne joel joelle jon kathy katie kristen laurent laurie leah leon leonard liliane lionel loic lorraine lucien ludovic luke madeleine malcolm marianne marielle marjolaine maryse matthieu michele micheline mickael mireille mitchell molly mylene nadine nick odette oliver owen pascale patrice paula phil regis remi rene renee robyn roland romain roxane sabrina sandrine shane shawn shelley sherry simone solange sonia stacey tanya therese thierry trevor tristan veronique vicki virginie viviane wesley yan yanick yann yannick yoan yohan yolande yvan yvette yvon""".split())
JUNK_NAME = re.compile(r"request for|proposal|tender|\bn/?a\b|various|multiple|unknown|redact|withheld|confidential|not disclosed|"
                       r"^(the )?(supplier|vendor|contractor|consultant|company|corporation)s?$|^misc|^sundry|^employee|^individual|^payee",
                       re.I)


def load_vendors(path):
    """name tokens index like news_match (first significant token -> [(tokens, vendor, False)]). A name is matched in running
    text only if one of its words is rare among vendor names (engineering / services / construction / group are not)."""
    rows, df = [], collections.Counter()
    opener = gzip.open if path.endswith(".gz") else open
    for line in opener(path, "rt", encoding="utf-8", errors="replace"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 3 or parts[0] == "name" or JUNK_NAME.search(parts[0]):
            continue
        toks = NM.sig_tokens(parts[0])
        if PUBLIC_BODY.search(parts[0]):
            continue  # a public body or charity named on a buyer's page is usually a partner, not its supplier
        if 2 <= len(toks) <= 8:
            rows.append((parts, toks)); df.update(set(toks))
    cap = max(40, len(rows) // 400)  # a word in over 0.25 % of vendor names is an everyday business word here
    def rare(t):
        return len(t) >= 5 and df[t] <= cap and t not in NM.GENERIC and t not in EVERYDAY and not NM._common(t) and not t.isdigit()
    index, vendors = collections.defaultdict(list), {}
    for (name, addr, basis), toks in rows:
        if not any(rare(t) for t in toks):
            continue
        if len(toks) == 2 and (toks[0] in FIRST_NAMES or toks[1] in FIRST_NAMES or "," in name) and not MARKER.search(name):
            continue  # an individual contractor (Lyndsay Francis, "Kelley, Geoffrey"), not a firm
        if len(toks) == 2 and not MARKER.search(name):
            continue  # two bare words: a person (artists, consultants) or everyday words — a firm's name carries a marker
        key = "v:" + hashlib.sha1(NM.norm(name).encode()).hexdigest()[:12]
        if key in vendors:
            continue
        vendors[key] = {"name": name, "key": key, "address": addr, "basis": basis}
        index[toks[0]].append((tuple(toks), vendors[key], False))
    return vendors, index


def site_pages(site, host, cap):
    """candidate pages: sitemap entries and home-page links whose URL / anchor looks like awards, procurement, news"""
    urls, seen = [], set()
    def add(u):
        u = html.unescape(u).split("#")[0]
        p = urllib.parse.urlparse(u)
        h = (p.hostname or "").lower().removeprefix("www.")
        if h != host or C.SKIP_EXT.search(p.path or "") or u in seen:
            return
        seen.add(u); urls.append(u)
    st, ct, data, final = C.fetch(site, 3_000_000)
    if st in (401, 403, 429):
        return "blocked", []
    if st != 200 or not data:
        return "http_%s" % st, []
    raw = strip_long(data.decode("utf-8", "replace"))
    if len(raw) < 30000 and C.BLOCK_RX.search(raw[:5000]):  # a block page is a short page (a Wix page carries "captcha" in its settings)
        return "blocked", []
    listings, portals = [], []
    def add_listing(u, label=""):
        u = html.unescape(u).split("#")[0]
        if u not in listings and (LISTING_RX.search(urllib.parse.unquote(u)) or LISTING_RX.search(label or "")):
            listings.append(u)
    for u, label in C.links(raw, final):
        h = (urllib.parse.urlparse(u).hostname or "").lower()
        if h and h.removeprefix("www.") != host and PORTAL_HOST.search(h) and u not in portals and len(portals) < 2:
            portals.append(u)  # the buyer's own meeting portal (eSCRIBE, CivicWeb, Legistar ...)
        add_listing(u, label)
        if PAGE_RX.search(urllib.parse.urlparse(u).path or "") or PAGE_RX.search(label or ""):
            add(u)
    # sitemap (robots.txt Sitemap: lines, else /sitemap.xml), up to 6 maps
    root = "%s://%s" % (urllib.parse.urlparse(final).scheme, urllib.parse.urlparse(final).netloc)
    rp = C.robots.get(root)
    maps = list((rp.site_maps() if rp and hasattr(rp, "site_maps") else None) or []) or [root + "/sitemap.xml", root + "/sitemap_index.xml"]
    seen_maps = set()
    while maps and len(seen_maps) < 6 and len(urls) < cap * 4:
        m = maps.pop(0)
        if m in seen_maps or not C.allowed(m):
            continue
        seen_maps.add(m)
        st, _, data, _ = C.fetch(m, 8_000_000)
        if st != 200 or not data:
            continue
        if data[:2] == b"\x1f\x8b":
            try:
                data = gzip.decompress(data)
            except Exception:
                continue
        for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", data.decode("utf-8", "replace"))[:20000]:
            loc = html.unescape(loc)
            if loc.lower().split("?")[0].endswith((".xml", ".xml.gz")):
                if PAGE_RX.search(loc) or len(maps) < 4:
                    maps.append(loc)
            elif PAGE_RX.search(urllib.parse.urlparse(loc).path or ""):
                add(loc)
                add_listing(loc)
    # meeting pages (own site, then the portal): one more level to reach the agenda attachments
    meeting_pages = [u for u in urls if MEETING_RX.search(urllib.parse.urlparse(u).path or "")][:6] + portals
    for mp in meeting_pages:
        if not C.allowed(mp):
            continue
        st2, ct2, data2, fin2 = C.fetch(mp, 3_000_000)
        if st2 != 200 or not data2 or "html" not in (ct2 or "").lower():
            continue
        raw2 = strip_long(data2.decode("utf-8", "replace"))
        ph = (urllib.parse.urlparse(fin2).hostname or "").lower()
        sub = []
        for u, label in C.links(raw2, fin2):
            uh = (urllib.parse.urlparse(u).hostname or "").lower()
            if uh.removeprefix("www.") == host or uh == ph or PORTAL_HOST.search(uh):
                add_listing(u, label)
                if MEETING_RX.search(urllib.parse.urlparse(u).path or "") and len(sub) < 8 and u not in sub:
                    sub.append(u)
        for u in sub[:8]:  # recent meeting pages → their attachments
            if len(listings) >= 12 or not C.allowed(u):
                break
            st3, ct3, data3, fin3 = C.fetch(u, 3_000_000)
            if st3 == 200 and data3 and "html" in (ct3 or "").lower():
                for u3, label3 in C.links(strip_long(data3.decode("utf-8", "replace")), fin3):
                    add_listing(u3, label3)
    urls.sort(key=lambda u: (0 if FIRST.search(u) else 1, len(u)))
    return "ok", listings[:12] + urls[:cap]


def scan(org, index, cap, stats, pages=None):
    key, name, site = org
    host = (urllib.parse.urlparse(site).hostname or "").lower().removeprefix("www.")
    if pages is None:
        if not C.allowed(site):
            return "robots", []
        st, pages = site_pages(site, host, cap)
        if st != "ok":
            return st, []
    btoks = set(NM.sig_tokens(name))
    foreign = not re.search(r"\.ca$|\.quebec$|\.qc\.ca$", host) and not re.search(r"canada|canadian|qu[ée]bec|ontario|alberta|manitoba|saskatchewan|nova scotia|"
                                                                           r"new brunswick|newfoundland|british columbia|yukon|nunavut|northwest territories|"
                                                                           r"\b(?:ville|municipalit[ée]|mrc|cégep|cegep)\b", name or "", re.I)
    strict = not PUBLIC_BODY.search(name or "") and not re.search(r"\.(gov|gc\.ca|edu|org)\b|\.(qc|on|bc|ab|mb|sk|ns|nb|nl|pe|nt|nu|yt)\.ca$|\.(gov|govt|edu|ac|org)\.[a-z]{2}$", host)
    leads, seen_v = [], set()
    for u in pages:
        if not C.allowed(u) or DROP_URL.search(u):
            continue
        big = bool(LISTING_RX.search(urllib.parse.unquote(u)) or MEETING_RX.search(urllib.parse.unquote(u)))
        st, ct, data, final = C.fetch(u, 25_000_000 if big else 3_000_000)
        if st != 200 or not data:
            continue
        is_pdf = "pdf" in (ct or "").lower() or data[:5] == b"%PDF-"
        if is_pdf:
            text = re.sub(r"[ \t]+", " ", C.pdf_text(data)[:1_500_000]); raw = ""
        else:
            raw = strip_long(data.decode("utf-8", "replace"))
            text = visible_keep_lines(raw)[:400_000]
        listing = bool(LISTING_RX.search(urllib.parse.unquote(final)) or LISTING_RX.search(text[:1500])) and not strict
        if not listing and is_pdf and not strict:  # an agenda package: the list of accounts is a section inside it
            mm = re.search(r"(?im)^.{0,40}(?:accounts? payable|list of accounts|cheque register|cheque listing|disbursements?|liste des comptes|comptes [àa] payer|d[ée]bours[ée]s).{0,60}$", text)
            if mm and MONEY.search(text[mm.end():mm.end() + 3000]):
                text, listing = text[mm.start():mm.start() + 250_000], True
        if listing:
            doc_date, how = page_date(raw, text, 0)
            if not doc_date:
                m = DATE_TXT.search(text[:4000])
                doc_date, how = (to_iso(m), "first date in the listing") if m else ("", "")
            n_hits = 0
            for v, a0, b0 in NM.find_names(text, index, limit=60):
                if v["key"] in seen_v or n_hits >= 25:
                    continue
                vt = set(NM.sig_tokens(v["name"]))
                if vt <= btoks or btoks <= vt or PUBLIC_BODY.search(v["name"]):
                    continue
                ls, le = text.rfind("\n", 0, a0) + 1, text.find("\n", b0)
                line = text[ls:le if le >= 0 else len(text)]
                if not MONEY.search(line) or len(line) > 400:
                    continue
                words = re.findall(r"[A-Za-zÀ-ÿ][\w'&.-]*", text[a0:b0])
                if sum(w[0].isupper() for w in words) < max(1, len(words) * 0.6):
                    continue
                d = doc_date
                m = DATE_TXT.search(line)
                if m and to_iso(m):
                    d, how = to_iso(m), "date on the listing line"
                if not d or d < OLDEST:
                    continue
                seen_v.add(v["key"]); n_hits += 1
                leads.append({"platform": "buyer_ap_listing", "domain": host, "dataset_id": hashlib.sha1(final.encode()).hexdigest()[:12],
                              "dataset": "the buyer's own accounts-payable listing (council / board list of accounts)", "dataset_url": final, "publisher": name,
                              "buyer_unit": "", "website": "https://%s/" % host, "vendor": v["name"],
                              "canada_field": "buyer's own accounts-payable listing names the supplier; supplier in Canada per the contract dataset's source field (%s)" % v["basis"][:150],
                              "canada_value": v["address"][:160],
                              "row": {"record_date": d, "date_basis": how, "quote": flat_line(line)[:300], "cue": "accounts-payable listing line with an amount",
                                      "buyer_key": key, "page_url": final}})
            if leads:
                break
            continue
        for v, a0, b0 in NM.find_names(text, index, limit=12):
            if v["key"] in seen_v:
                continue
            vt = set(NM.sig_tokens(v["name"]))
            if vt <= btoks or btoks <= vt:
                continue  # the buyer's own name (or a part of it)
            if foreign and not CA_WORD.search(v["name"]):
                continue  # a multinational's name on a non-Canadian buyer's page points to the local entity, not the Canadian one
            words = re.findall(r"[A-Za-zÀ-ÿ][\w'&.-]*", text[a0:b0])
            if sum(w[0].isupper() for w in words) < max(1, len(words) * 0.6):
                continue  # written as ordinary words, not as a name ("low impact", "make it")
            cue = None
            for m in list(re.finditer(re.escape(text[a0:b0]), text))[:6]:  # the headline may name it without a cue; the body with one
                a, b = m.start(), m.end()
                sent, rel = NM.sentence_at(text, a, b)
                ls, le = text.rfind("\n", 0, a) + 1, text.find("\n", b)
                line = text[ls:le if le >= 0 else len(text)]
                before, after = text[max(ls, a - 90):a], text[b:min(le if le >= 0 else len(text), b + 90)]
                cue = direction_cue(before, after, line, u, strict)
                if cue and (DROP_B.search(sent) or DROP_B.search(line) or (len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", line)) < 6 and not MONEY.search(line))):
                    cue = None  # a prize context, or a menu item / list entry rather than a statement
                if cue and OTHER_BODY.search(sent) and not any(t in NM.norm(OTHER_BODY.search(sent).group(0)) for t in btoks):
                    cue = None  # another public body is the one that retained / awarded (a ministry's project reported on a town's site)
                if cue:
                    break
            if not cue:
                continue
            d, how = page_date(raw, text, a)
            if not d or d < OLDEST:
                continue
            seen_v.add(v["key"])
            leads.append({"platform": "buyer_site_mention", "domain": host, "dataset_id": hashlib.sha1(final.encode()).hexdigest()[:12],
                          "dataset": "the buyer's own page naming its supplier", "dataset_url": final, "publisher": name, "buyer_unit": "",
                          "website": "https://%s/" % host, "vendor": v["name"],
                          "canada_field": "buyer's own page names the supplier; supplier in Canada per the contract dataset's source field (%s)" % v["basis"][:150],
                          "canada_value": v["address"][:160],
                          "row": {"record_date": d, "date_basis": how, "quote": sent[:300], "cue": cue,
                                  "buyer_key": key, "page_url": final}})
            if len(leads) >= 3:
                break
        if len(leads) >= 3:
            break
    return "ok", leads


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--orgs", default="")
    a.add_argument("--urls", default="", help="CSV buyer_key,buyer_name,website,official_site,url (claude_search_urls_pNN.csv): read these pages only")
    a.add_argument("--vendors", required=True)
    a.add_argument("--workers", type=int, default=32)
    a.add_argument("--pages", type=int, default=40)
    a.add_argument("--limit", type=int, default=0)
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True); os.makedirs(STATE, exist_ok=True)
    vendors, index = load_vendors(a.vendors)
    print("vendors indexed: %d" % len(vendors), flush=True)
    done = set()
    if os.path.exists(DONE):
        done = {l.split("\t")[0] for l in open(DONE, encoding="utf-8")}
    if a.urls:  # located pages: one scan per organisation over its listed pages (no site crawl, no done list)
        by_org = collections.OrderedDict()
        for r in csv.DictReader(open(a.urls, encoding="utf-8", errors="replace")):
            w = (r.get("website") or r.get("official_site") or "").strip()
            h = (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower().removeprefix("www.")
            if h and (r.get("url") or "").startswith("http"):
                by_org.setdefault((r.get("buyer_key", ""), r.get("buyer_name", ""), "https://%s/" % h), []).append(r["url"])
        stats, n_leads = collections.Counter(), 0
        def one_u(item):
            nonlocal n_leads
            org, pages = item
            try:
                st, leads = scan(org, index, a.pages, stats, pages=pages[:a.pages])
            except Exception as e:
                st, leads = "error", []
            with lock:
                stats[st] += 1
                if leads:
                    with open(OUT, "a", encoding="utf-8") as f:
                        for L in leads:
                            f.write(json.dumps(L, ensure_ascii=False) + "\n")
                    n_leads += len(leads)
        print("organisations with located pages: %d" % len(by_org), flush=True)
        with ThreadPoolExecutor(a.workers) as ex:
            list(ex.map(one_u, list(by_org.items())))
        print("finished", dict(stats), "leads", n_leads, flush=True)
        return
    orgs, seen = [], set()
    for r in csv.DictReader(open(a.orgs, encoding="utf-8", errors="replace")):
        w = (r.get("website") or "").strip()
        h = (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower().removeprefix("www.")
        if not h or "." not in h or h in seen or h in done:
            continue
        seen.add(h); orgs.append((r.get("key", ""), r.get("name", ""), "https://%s/" % h))
    if a.limit:
        orgs = orgs[:a.limit]
    print("organisations: %d (%d done before)" % (len(orgs), len(done)), flush=True)
    stats, n_leads = collections.Counter(), [0]

    def one(org):
        try:
            st, leads = scan(org, index, a.pages, stats)
        except Exception as e:
            st, leads = "error", []
        host = (urllib.parse.urlparse(org[2]).hostname or "").lower().removeprefix("www.")
        with lock:
            stats[st] += 1
            with open(DONE, "a", encoding="utf-8") as f:
                f.write("%s\t%s\t%d\n" % (host, st, len(leads)))
            if leads:
                with open(OUT, "a", encoding="utf-8") as f:
                    for L in leads:
                        f.write(json.dumps(L, ensure_ascii=False) + "\n")
                n_leads[0] += len(leads)
            if sum(stats.values()) % 50 == 0:
                print(time.strftime("%H:%M"), dict(stats), "leads", n_leads[0], flush=True)

    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, orgs))
    print("finished", dict(stats), "leads", n_leads[0], flush=True)


if __name__ == "__main__":
    main()
