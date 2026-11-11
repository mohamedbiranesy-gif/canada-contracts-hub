#!/usr/bin/env python3
"""How a vendor bills, in its own words.

Owner's bar (2026-11-11): a relationship counts when the buyer "would be getting billed for something monthly … or every 3 months …
systematically by the vendor". A service seen in use (the buyer's DNS zone on the provider's name servers, the vendor's platform under the
buyer's site, a credit line) says that the relationship exists; it does not say how often the vendor bills. The vendor's own price list
and terms do: "$4.99/mo", "billed monthly", "facturé annuellement", "per booking". This tool opens the vendor's own site — its home page
and up to five pages its own menu names as prices / plans / hosting / membership / terms — and keeps every statement of a billing period
with the sentence around it (at most 300 characters), the page and the date. Nothing is derived: no statement, no period.

  read   --minutes M --workers W [--shard K/N] [--limit L] [--only dom,dom] [--redo]   -> out/vendor_billing_K.jsonl
  merge  DIR [--stamp S]        -> data/incoming/claude/vendor_billing/billing_S.gz (append-only shards, one JSON line per vendor read)
  show   dom …                  what is on file for these vendors, and the class cycle_of() gives them

Statement classes (field "c"): billed_month / billed_quarter / billed_year — the vendor says when it bills ("billed monthly", "invoiced
every 30 days", "renouvelé annuellement"); price_month / price_quarter / price_year — a price with its period ("$4.99/mo", "150 $ par an");
plan_month / plan_quarter / plan_year — a plan or fee named by its period ("monthly subscription", "cotisation annuelle"); price_txn — a
price per transaction / booking / order.

Version 2 adds three kinds of statement that an invoice needs or that make a live service a paid one: unpaid — what the vendor does when
a bill is not paid ("accounts 15 days overdue are suspended"); currency — "all prices in Canadian dollars"; paymethod — "we accept Visa,
Interac e-Transfer, cheque". lowest(rec) gives the lowest published price per month and per year (a floor for the amount of a bill).

Rules: robots.txt, the project's user agent, one request a second per host (tools/ap_crawler.py); a refusal is a status and the vendor is
not asked again for 30 days.
"""
import argparse, collections, datetime, glob, gzip, html, json, os, re, sys, time, urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "data/incoming/claude/vendor_billing")
TODAY = datetime.date.today().isoformat()
V = 3  # 2 (2026-11-11): what happens when a bill is not paid, the currency of the prices, the ways of paying; amounts parsed. 3: the site's own title and description of what the vendor sells

NUM = r"\d{1,3}(?:[ ,. ]\d{3})*(?:[.,]\d{1,2})?"
MONEY = r"(?:(?:CA|US|CAD|USD|C)?\s?\$\s?%s|%s\s?\$(?:\s?(?:CAD|USD|CA|US)\b)?|%s\s?(?:CAD|USD)\b)" % (NUM, NUM, NUM)
_PER = r"(?:per|a|each|every|par|chaque)\s+(?:(?:user|seat|site|mailbox|domain|location|agent|member|practitioner|licen[cs]e|utilisateur|site|bo[iî]te|domaine|membre)\s+(?:(?:and|et)\s+)?(?:per|a|par)\s+)?"
MONTH = r"(?:/\s?mo(?:nth|is|\.)?(?![a-zà-ÿ])|\b%s(?:month|mois)\b|\bmonthly\b|\bmensuel(?:le)?s?\b|\bmensuellement\b)" % _PER
QUARTER = (r"(?:/\s?(?:quarter|trimestre)(?![a-zà-ÿ])|\bquarterly\b|\b%s(?:quarter|trimestre)\b|\bevery\s+(?:3|three)\s+months\b|"
           r"\b(?:aux|tous\s+les)\s+(?:3|trois)\s+mois\b|\btrimestriel(?:le)?s?\b|\btrimestriellement\b)") % _PER
YEAR = r"(?:/\s?(?:yr|year|an|ann[ée]e)(?![a-zà-ÿ])|\b%s(?:year|annum|an|ann[ée]e)\b|\byearly\b|\bannually\b|\bannual\b|\bannuel(?:le)?s?\b|\bannuellement\b)" % _PER
TXN = (r"(?:\bper\s+(?:transaction|booking|order|ticket|registration|sale|invoice)\b|\bpar\s+(?:transaction|r[ée]servation|commande|billet|inscription|vente|facture)\b|"
       r"/\s?(?:transaction|booking|order|ticket)\b)")
D30 = r"(?:\bevery\s+30\s+days\b|\b30[- ]day\s+(?:intervals?|cycles?|periods?|billing)\b|\btous\s+les\s+30\s+jours\b)"
_TAX = r"(?:\s?(?:\+\s?(?:tx|taxe?s?|gst|hst|tps|tvq)\b|plus\s+tax(?:es)?\b|CAD\b|USD\b|\*))*"
_GAP = r"[^.!?;:|•\n$]{0,24}?"
BILL = (r"\b(?:(?:billed|invoiced|charged|debited|billing\s+(?:cycle|period|frequency|interval)s?\s+(?:is|are|will\s+be)|billing\s+is|payable|"
        r"payments?\s+(?:are|is|will\s+be)\s+(?:due|made|processed|collected|charged)|renews?(?:\s+automatically)?|auto[- ]?renews?|"
        r"factur[ée]e?s?|pr[ée]lev[ée]e?s?|pr[ée]l[èe]vements?|payables?|renouvel[ée]e?s?(?:\s+automatiquement)?)(?![a-zà-ÿ])|"
        r"billing\s+(?:cycle|period|frequency|interval)s?\s*[(:])")
_BGAP = r"[^.!?;|•\n]{0,36}?"
# "paid" / "pay" only right before the period ("paid annually", "pay monthly", "payé chaque mois"): "paid ads, email, and monthly reporting" is not a bill
PAID = re.compile(r"\b(?:pre-?)?(?:paid|pay|pay[ée]e?s?)\s+(?:in\s+advance\s+|d['’]avance\s+)?(?:(?:on|at)\s+(?:an?|the)\s+)?(?:(?P<m>" + MONTH + "|" + D30 + ")|(?P<q>" + QUARTER + ")|(?P<y>" + YEAR + "))", re.I)
# the period that follows first decides ("billed yearly, though we show you the monthly rate" is a yearly bill)
BILLED = re.compile(BILL + _BGAP + "(?:(?P<m>" + MONTH + "|" + D30 + ")|(?P<q>" + QUARTER + ")|(?P<y>" + YEAR + "))", re.I)
PRICE = re.compile(MONEY + _TAX + r"\s?" + _GAP + "(?:(?P<m>" + MONTH + ")|(?P<q>" + QUARTER + ")|(?P<y>" + YEAR + ")|(?P<t>" + TXN + "))", re.I)
RX = [
    ("price_month", re.compile(r"\b(?:monthly|mensuel(?:le)?s?|par\s+mois|per\s+month)\b[^.!?;|•\n\d$]{0,22}?" + MONEY, re.I)),
    ("price_year", re.compile(r"\b(?:yearly|annual(?:ly)?|annuel(?:le)?s?|par\s+an(?:n[ée]e)?|per\s+year)\b[^.!?;|•\n\d$]{0,22}?" + MONEY, re.I)),
    ("price_txn", re.compile(r"\d{1,2}(?:[.,]\d{1,2})?\s?%\s?" + _GAP + TXN, re.I)),
    ("plan_month", re.compile(r"\b(?:monthly|month[- ]to[- ]month)\s+(?:subscriptions?|plans?|fees?|retainers?|maintenance|hosting|payments?|billing|invoic\w+|charges?|dues|"
                              r"instal?lments?|service\s+fees?|memberships?|contracts?)\b|\b(?:abonnements?|forfaits?|frais|paiements?|facturation|versements?|tarifs?|plans?)\s+mensuel(?:le)?s?\b|"
                              r"\bmensualit[ée]s?\b", re.I)),
    ("plan_quarter", re.compile(r"\bquarterly\s+(?:subscriptions?|plans?|fees?|payments?|billing|invoic\w+|dues|instal?lments?)\b|"
                                r"\b(?:abonnements?|forfaits?|frais|paiements?|facturation|versements?)\s+trimestriel(?:le)?s?\b", re.I)),
    ("plan_year", re.compile(r"\b(?:annual|yearly)\s+(?:subscriptions?|plans?|fees?|dues|memberships?(?:\s+(?:fees?|dues))?|renewals?|licen[cs]e(?:\s+fees?)?|billing|payments?|contracts?)\b|"
                             r"\b(?:cotisations?|frais|abonnements?|adh[ée]sions?|forfaits?|tarifs?|renouvellements?)\s+annuel(?:le)?s?\b", re.I)),
]
_OR_MORE = re.compile(r"^[\s,(]*(?:or|ou|and|et|/|,)\s*(?:(?P<m>" + MONTH + r"|months?\b|mois\b)|(?P<q>" + QUARTER + r"|quarters?\b|trimestres?\b)|(?P<y>" + YEAR + r"|years?\b|ans?\b|ann[ée]es?\b))", re.I)  # "monthly or annually"
# what is paid TO the reader of the page or given away, not billed by the vendor: a salary, a prize, a gift, an interest rate, a saving, a turnover
NEG = re.compile(r"newsletter|infolettre|\bdraw\b|tirage|giveaway|contest|concours|prize|\bwin\b|gagn|donat|\bdons?\b|monthly\s+giving|give\s+monthly|donor|donateur|salar|salaire|"
                 r"\bwage|payroll|\bpaie\b|income|revenus?\b|\bearn|interest|int[ée]r[êe]t|mortgage|hypoth|cash\s?back|rebate|\bsave\s|[ée]conomi[sz]|\boff\b|rabais|visitors?|visiteurs?|"
                 r"downloads?|views?\b|sessions?\b|traffic|listeners?|readers?|lecteurs?|[mb]illions?\b|collect(?:ing|ed)\b|raised|amass|revenue|chiffre\s+d|\bventes\b|\bsales\b|uptime|"
                 r"disponibilit", re.I)
_ANY_PERIOD = re.compile("(?:(?P<m>" + MONTH + "|" + D30 + r"|months?\b|mois\b)|(?P<q>" + QUARTER + r"|quarters?\b|trimestres?\b)|(?P<y>" + YEAR + r"|semi-?annual\w*|semestriel\w*|years?\b|ans?\b|ann[ée]es?\b))", re.I)
_SUSP = r"(?:suspend\w*|terminat\w*|deactivat\w*|disabl\w*|interrupt\w*|cancel\w*|fr[eo]ez\w*|frozen|disconnect\w*|delet\w*|suspendu\w*|suspension|interromp\w*|r[ée]sili\w*|d[ée]sactiv\w*|supprim\w*)"
_UNPAID = r"(?:non-?payment|unpaid|overdue|past\s+due|fail(?:ure|s|ed)?\s+to\s+pay|not\s+(?:been\s+)?paid|delinquent|d[ée]faut\s+de\s+paiement|non-?paiement|impay[ée]e?s?|en\s+souffrance|payments?\s+(?:of\s+\w+\s+)?(?:is|are)\s+(?:unsuccessful|declined|not\s+received|late)|unable\s+to\s+(?:successfully\s+)?process\s+payment)"
EXTRA = [
    ("unpaid", re.compile(_SUSP + r"[^.!?|•]{0,90}?" + _UNPAID + "|" + _UNPAID + r"[^.!?|•]{0,90}?" + _SUSP, re.I)),
    ("currency", re.compile(r"\b(?:prices?|pricing|rates?|fees?|amounts?|charges?|tarifs?|prix|montants?|frais)\b[^.!?|•]{0,50}?\b(?:in|en)\s+(?:Canadian\s+(?:dollars?|funds|currency)|CAD\b|CDN\b|U\.?S\.?\s+(?:dollars?|funds|currency)|USD\b|"
                            r"dollars?\s+canadiens?|dollars?\s+am[ée]ricains?|devises?\s+canadiennes?)", re.I)),
    ("paymethod", re.compile(r"\b(?:we\s+accept|accepted\s+(?:payment\s+)?methods?|payment\s+(?:methods?|options?)|modes?\s+de\s+paiement|payable\s+by|pay(?:ments?)?\s+(?:can\s+be\s+made\s+)?by|nous\s+acceptons)\b[^.!?|•]{0,90}?"
                             r"\b(?:credit\s+cards?|visa|mastercard|interac|e-?transfers?|cheques?|checks?|pre-?authori[sz]ed|paypal|cartes?\s+de\s+cr[ée]dit|virements?|ch[èe]ques?|pr[ée]l[èe]vements?)\b", re.I)),
]
NO_RX = re.compile(r"(?:\bno|\bnot|\bnever|\bwithout|\bzero|\bsans|\baucune?|\bpas\s+de|\bni)\s+(?:\w+\s+)?$", re.I)  # "no monthly fees", "sans frais mensuels"
RESIDUE = re.compile(r"[<>{}=]|onmouse|javascript:|\bfunction\s*\(|&[a-z]{2,6};")  # markup or script left in the text: not a sentence a reader saw
PAGE_RX = [re.compile(p, re.I) for p in (
    r"pric|tarif|\bplans?(?:\b|[-_/])|forfaits?|packages?|abonnement|subscri",
    r"hosting|h[ée]bergement|membership|adh[ée]sion|devenir[-_ ]membre|become[-_ ]a[-_ ]member|\bjoin|\bfees?\b|\bfrais\b|cotisation|\bdues\b|\brates?\b|maintenance|care[-_ ]?plan|\bdomains?\b|\bdomaines?\b|e-?mail|courriel",
    r"\bterms|conditions|modalit|billing|facturation|\bfaq|\blegal|agreement|entente|contrat")]
NOT_PAGE = re.compile(r"login|log-in|signin|sign-in|connexion|cart|panier|checkout|blog|news|nouvelles|actualit|career|carri[èe]re|emploi|privacy|confidentialit|cookie|accessib|\.pdf(?:$|\?)|/tag/|/category/|/author/", re.I)
OWN_SUB = re.compile(r"^(?:www\d?|shop|store|boutique|billing|my|mon|portal|portail|clients?|secure|account|compte|hosting|support|help|aide|docs?|kb|info|site)$")


def page(url):
    """(status, html, final address)"""
    if not C.allowed(url):
        return "robots", "", url
    st, ct, data, final = C.fetch(url, 2_500_000)
    if st in (401, 403, 429):
        return "blocked_%s" % st, "", final
    if st != 200 or not data:
        return "http_%s" % st, "", final
    if "html" not in (ct or "").lower() and "text/plain" not in (ct or "").lower():
        return "not_html", "", final
    raw = data.decode("utf-8", "replace")
    if len(raw) < 30000 and C.BLOCK_RX.search(raw[:5000]):  # a block page is a short page
        return "blocked", "", final
    return "ok", raw, final


def text_of(raw):
    """visible text, block ends kept as sentence ends (a price table's cells must not run into each other)"""
    t = re.sub(r"(?is)<(script|style|noscript|svg|template)[^>]*>.*?</\1>", " ", raw)
    t = re.sub(r"(?i)</?(?:p|div|li|ul|ol|td|tr|th|table|section|footer|header|nav|aside|h[1-6]|br|hr|form|button|option|label|dt|dd)\b[^>]*>", " | ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"\s+", " ", t)  # a line break inside a block is white space of the markup ("$59 / month" printed on three lines is one price)
    return re.sub(r"(?:\s*\|\s*)+", " | ", t)


def quote_of(text, a, b):
    """the clause around text[a:b]: back and forward to a block end, at most 300 characters, the match always inside"""
    i = text.rfind(" | ", max(0, a - 160), a + 2)  # a match may begin with the space that ends a block mark
    lo = i + 3 if i != -1 else max(0, a - 160)
    if i == -1 and lo > 0:  # cut inside a long block: start at a word
        while lo < a and text[lo - 1] != " ":
            lo += 1
    hi_block = text.find(" | ", b, b + 140)
    hi = hi_block if hi_block != -1 else min(len(text), b + 140)
    q = text[lo:hi].strip(" |")
    if len(q) > 300:
        off = a - lo
        q = q[max(0, off - 120):max(0, off - 120) + 300]
    return re.sub(r"\s+", " ", q).strip()


def statements(text, url, cap=2):
    out, seen = [], collections.Counter()

    def add(cls, m):
        if seen[cls] >= cap:
            return
        q = quote_of(text, m.start(), m.end())
        if NEG.search(text[max(0, m.start() - 60):m.end() + 30]) or NO_RX.search(text[max(0, m.start() - 16):m.start()]) or len(q) < (5 if cls.startswith("price") else 12) or RESIDUE.search(q):
            return
        if cls.startswith("plan_") and "?" in text[m.end():m.end() + 70].split(" | ")[0]:
            return  # a question of a FAQ ("Are there monthly fees or minimum commitments?"), not a statement
        if any(o["q"] == q and o["c"] == cls for o in out):
            return
        seen[cls] += 1
        out.append({"c": cls, "q": q, "m": re.sub(r"\s+", " ", m.group(0))[:80], "u": url})
    for kind, rx in (("billed", BILLED), ("billed", PAID), ("price", PRICE)):
        for m in rx.finditer(text):
            g = next(k for k in ("m", "q", "y", "t") if m.groupdict().get(k))
            add(kind + {"m": "_month", "q": "_quarter", "y": "_year", "t": "_txn"}[g], m)
            # a choice of periods in the same breath: "billed monthly or annually", "paid quarterly semi-annually or annually", "billed at an
            # annual rate, quarterly payments may be made" — never "billed yearly, though we show you the monthly rate"
            rest, pos = re.split(r"[.!?|•]", text[m.end():m.end() + 70])[0], 0
            while kind == "billed" or pos == 0:
                m2 = _ANY_PERIOD.search(rest, pos)
                if not m2 or not re.fullmatch(r"[\s,(/]*(?:(?:or|ou|and|et|rate|basis|payments?)\b[\s,]*)*", rest[pos:m2.start()], re.I):
                    break
                g2 = next(k for k in ("m", "q", "y") if m2.groupdict().get(k))
                if g2 != g:
                    add(kind + {"m": "_month", "q": "_quarter", "y": "_year"}[g2], m)
                pos = m2.end()
                if kind != "billed":
                    break
    for cls, rx in EXTRA:
        for m in rx.finditer(text):
            if seen[cls] >= 1:
                break
            q = quote_of(text, m.start(), m.end())
            if len(q) >= 20 and not RESIDUE.search(q):
                seen[cls] += 1
                out.append({"c": cls, "q": q, "m": re.sub(r"\s+", " ", m.group(0))[:120], "u": url})
    for cls, rx in RX:
        for m in rx.finditer(text):
            add(cls, m)
    return out


def own_link(link, fhost):
    p = urllib.parse.urlparse(link)
    h = (p.hostname or "").lower()
    if p.scheme not in ("http", "https") or not h:
        return False
    if h == fhost or h == "www." + fhost or "www." + h == fhost:
        return True
    dom = C.registrable(fhost)
    return C.registrable(h) == dom and bool(OWN_SUB.match(h[:-len(dom)].rstrip(".") or "www"))


def read_vendor(dom, start="", extra=()):
    rec = {"dom": dom, "date": TODAY, "status": "", "pages": [], "stmts": [], "v": V}
    st, raw, final = page(start or "https://%s/" % dom)
    if st != "ok" and not start:
        st, raw, final = page("https://www.%s/" % dom) if st.startswith("http_0") or st == "http_None" else (st, raw, final)
    rec["status"] = st
    if st != "ok":
        return rec
    fhost = (urllib.parse.urlparse(final).hostname or dom).lower()
    rec["final"] = final
    # what the vendor says it sells, in its own words (its home page's title and description): the subject of a bill when the relationship
    # itself names none (a client listing, a credit line)
    mt = re.search(r"(?is)<title[^>]*>(.*?)</title>", raw[:200000])
    md = re.search(r"""(?is)<meta[^>]+(?:name|property)\s*=\s*["'](?:description|og:description)["'][^>]*content\s*=\s*["']([^"']{10,600})["']""", raw[:300000]) or \
        re.search(r"""(?is)<meta[^>]+content\s*=\s*["']([^"']{10,600})["'][^>]*(?:name|property)\s*=\s*["'](?:description|og:description)["']""", raw[:300000])
    rec["title"] = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", mt.group(1)))).strip()[:160] if mt else ""
    rec["desc"] = re.sub(r"\s+", " ", html.unescape(md.group(1))).strip()[:300] if md else ""
    rec["pages"].append(final)
    rec["stmts"] += statements(text_of(raw), final)
    cand, seen = [], {final.split("#")[0].rstrip("/")}
    for link, label in C.links(raw, final):
        u = link.split("#")[0]
        if u.rstrip("/") in seen or not own_link(u, fhost) or C.SKIP_EXT.search(urllib.parse.urlparse(u).path) or NOT_PAGE.search(u):
            continue
        hay = urllib.parse.urlparse(u).path + " " + (label or "")
        for pr, rx in enumerate(PAGE_RX):
            if rx.search(hay):
                seen.add(u.rstrip("/"))
                cand.append((pr, len(u), u))
                break
    todo = list(extra) + [u for _, _, u in sorted(cand)[:5]]
    for u in todo[:6]:
        st2, raw2, f2 = page(u)
        if st2 != "ok":
            continue
        rec["pages"].append(f2)
        have = {(s["c"], s["q"]) for s in rec["stmts"]}
        rec["stmts"] += [s for s in statements(text_of(raw2), f2) if (s["c"], s["q"]) not in have]
    # at most three statements a class: the pages named as prices come first after the home page
    kept, n = [], collections.Counter()
    for s in rec["stmts"]:
        if n[s["c"]] < 3:
            n[s["c"]] += 1
            kept.append(s)
    rec["stmts"] = kept
    return rec


# what the vendor says about WHEN it bills outranks the period its prices are quoted in: "$3/month … billed at $36 per year" is a yearly bill
ORDER = (("monthly", ("billed_month",)), ("quarterly", ("billed_quarter",)), ("yearly", ("billed_year",)),
         ("monthly_price", ("price_month", "plan_month")), ("quarterly", ("price_quarter", "plan_quarter")), ("yearly", ("price_year", "plan_year")),
         ("per_transaction", ("price_txn",)))


_OPTION = re.compile(r"\bsave\b|[ée]conomi[sz]|\bor\b|\bou\b|option|discount|rabais|%\s?off|free|gratuit|prefer|pr[ée]f[èe]r", re.I)


def cycle_of(rec):
    """(class, statement, other classes present). class: 'monthly' — the vendor says it bills by the month (or every 30 days); 'quarterly';
    'monthly_price' — its prices or plans are by the month (the customer may be offered a longer period); 'yearly'; 'per_transaction'; ''."""
    by = {}
    for s in (rec or {}).get("stmts") or []:
        by.setdefault(s["c"], s)
    found = [(cls, next(by[k] for k in keys if k in by)) for cls, keys in ORDER if any(k in by for k in keys)]
    if not found:
        return "", None, []
    if found[0][0] == "yearly" and found[0][1]["c"] == "billed_year" and _OPTION.search(found[0][1]["q"]):
        mp = next(((c, s2) for c, s2 in found[1:] if c == "monthly_price"), None)
        if mp:  # "Pay Yearly and Save!" beside "$129/month": the price is by the month, the year is an offer
            found = [mp] + [f for f in found if f is not mp]
    more = []
    for c, s2 in found[1:]:
        if c == found[0][0] or c in more:
            continue
        if found[0][1]["c"].startswith("billed") and s2["c"].startswith("plan") and s2["q"] == found[0][1]["q"]:
            continue  # "Annual Membership (Billed Quarterly)": the other period names the plan in the deciding sentence itself, it is not another way to be billed
        more.append(c)
    return found[0][0], found[0][1], more


_ADDON = re.compile(r"add-?ons?\b|additional|\bextra\b|suppl[ée]mentaires?|\beach\b|per\s+licen[cs]e|privacy|whois|\bssl\b|backups?\b|sauvegardes?|per\s+(?:gb|go|tb)\b|overage|d[ée]passement|"
                    r"\+\s?\$|\bper\s+(?:sms|text|lead|click|hour|heure)\b|/\s?(?:hr|hour|h)\b|setup|set-up|installation|one[- ]time|unique", re.I)
_MNUM = re.compile(r"\d[\d ,.\u00a0]*\d|\d")


def parse_money(m):
    """(value, currency or '') of the first amount in a matched price text: $1,200.50 · 4,99 $ · 1 500 $ · US$7.99 · C$4.16"""
    cur = "CAD" if re.search(r"C\$|CA\$|CAD\b|CDN|\$\s?CA\b", m) else "USD" if re.search(r"US\$|USD\b|\$\s?US\b", m) else ""
    hit = re.search(r"\$\s?(" + _MNUM.pattern + r")|(" + _MNUM.pattern + r")\s?(?:\$|CAD\b|USD\b)", m)
    if not hit:
        return None, cur
    n = re.sub(r"[ \u00a0]", "", hit.group(1) or hit.group(2)).rstrip(".,")
    try:
        if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d{1,2})?", n):
            v = float(n.replace(",", ""))
        elif re.fullmatch(r"\d{1,3}(?:\.\d{3})+(?:,\d{1,2})?", n):
            v = float(n.replace(".", "").replace(",", "."))
        elif re.fullmatch(r"\d+,\d{1,2}", n):
            v = float(n.replace(",", "."))
        else:
            v = float(n.replace(",", ""))
    except ValueError:
        return None, cur
    return v, cur


def lowest(rec):
    """{'month': (value, currency, statement), 'year': (…)} — the lowest published price of each period, 1 or more (a "$0" plan and a
    "$1 for the first month" offer are not prices of the service)"""
    out = {}
    for s in (rec or {}).get("stmts") or []:
        per = {"price_month": "month", "price_year": "year", "price_quarter": "quarter"}.get(s["c"])
        if not per:
            continue
        v, cur = parse_money(s.get("m") or s.get("q") or "")
        if v is None or v < 1 or v > 100000 or re.search(r"first|premier|trial|essai|intro|promo|then\s|puis\s|for\s+\d+\s+months|pendant", s.get("q") or "", re.I):
            continue
        if _ADDON.search(s.get("q") or ""):
            continue  # "$5 / month per license", "+$15 per additional mailbox", "domain privacy $9.99/yr": the price of an extra, not of the service
        if per not in out or v < out[per][0]:
            out[per] = (v, cur, s)
    return out


def extra_of(rec, cls):
    """the first statement of class 'unpaid' / 'currency' / 'paymethod' (version 2 records), or None"""
    return next((s for s in (rec or {}).get("stmts") or [] if s["c"] == cls), None)


def load():
    """{vendor domain: latest record}"""
    out = {}
    for p in sorted(glob.glob(os.path.join(DIR, "billing_*.gz"))):
        try:
            with gzip.open(p, "rt", encoding="utf-8") as fh:
                for l in fh:
                    try:
                        o = json.loads(l)
                    except ValueError:
                        continue
                    if o.get("dom") and (o["dom"] not in out or (o.get("date") or "") >= (out[o["dom"]].get("date") or "")):
                        out[o["dom"]] = o
        except (OSError, EOFError):
            continue
    return out


def candidates():
    """vendor domains of the relationships on file, the vendors of live services first, then by the number of relationships"""
    import lead_store as LS
    import tech_relationships as T
    cnt, site, cls = collections.Counter(), {}, {}
    W = {"dns_service_cc": 0, "site_credit_cc": 1, "site_member_cc": 2, "vendor_site_cc": 3}
    for d in LS.load()[1].values():
        w = W.get(d.get("platform") or "")
        s = d.get("vendor_site") or ""
        if w is None or not s:
            continue
        h = (urllib.parse.urlparse(s).hostname or "").lower()
        dom = C.registrable(h) if h else ""
        if not dom:
            continue
        cnt[dom] += 1
        cls[dom] = min(w, cls.get(dom, 9))
        site.setdefault(dom, s)
    out, extra = [], {}
    for v in T.VENDORS.values():
        u = v.get("hq_url") or ""
        h = (urllib.parse.urlparse(u).hostname or "").lower()
        if not h:
            continue
        dom = C.registrable(h)
        if re.search(r"terms|conditions|legal|agreement|entente", urllib.parse.urlparse(u).path, re.I):
            extra.setdefault(dom, []).append(u)  # the vendor's own terms page, already quoted for its contracting party
        if dom not in cls or cls[dom] > -1:
            cls[dom], cnt[dom] = -1, max(cnt[dom], 10 ** 6)
            site.setdefault(dom, "https://%s/" % h)
    for dom in sorted(cnt, key=lambda d: (cls[d], -cnt[d], d)):
        out.append((dom, site[dom], cnt[dom], tuple(extra.get(dom, ()))))
    return out


def due(o):
    """a vendor on file is read again after 45 days; one that refused after 30; one that did not answer after 3"""
    try:
        age = (datetime.date.today() - datetime.date.fromisoformat(o.get("date") or "")).days
    except ValueError:
        return True
    st = o.get("status") or ""
    if st == "ok" and int(o.get("v") or 1) < V:
        return age >= 0 and (o.get("date") or "") < TODAY  # read by an earlier version of the reader: again, from the next day on
    return age >= (45 if st == "ok" else 30 if st.startswith(("robots", "blocked")) else 3)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("cmd", choices=["read", "merge", "show"])
    a.add_argument("args", nargs="*")
    a.add_argument("--minutes", type=float, default=50)
    a.add_argument("--workers", type=int, default=30)
    a.add_argument("--shard", default="0/1")
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--only", default="")
    a.add_argument("--redo", action="store_true")
    a.add_argument("--stamp", default="")
    a = a.parse_args()
    if a.cmd == "show":
        have = load()
        for d in a.args:
            o = have.get(d)
            print(d, "—", "not on file" if not o else "%s, read %s, %d pages" % (o.get("status"), o.get("date"), len(o.get("pages") or [])))
            if o:
                c, s, more = cycle_of(o)
                print("   class:", c or "(no statement)", "| also:", ", ".join(more))
                for s in o.get("stmts") or []:
                    print("   %-14s %s  [%s]" % (s["c"], s["q"][:200], s["u"]))
        return
    if a.cmd == "merge":
        src = a.args[0] if a.args else "out"
        stamp = a.stamp or datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S")
        have, new = load(), {}
        for p in sorted(glob.glob(os.path.join(src, "**", "vendor_billing_*.jsonl"), recursive=True)):
            for l in open(p, encoding="utf-8", errors="replace"):
                try:
                    o = json.loads(l)
                except ValueError:
                    continue
                if o.get("dom"):
                    new[o["dom"]] = o
        new = {d: o for d, o in new.items() if d not in have or have[d].get("date") != o.get("date") or have[d].get("stmts") != o.get("stmts") or have[d].get("status") != o.get("status")}
        if new:
            os.makedirs(DIR, exist_ok=True)
            with gzip.open(os.path.join(DIR, "billing_%s.gz" % stamp), "wt", encoding="utf-8") as f:
                for d in sorted(new):
                    f.write(json.dumps(new[d], ensure_ascii=False) + "\n")
        allv = dict(have, **new)
        k = collections.Counter(cycle_of(o)[0] or ("no statement" if o.get("status") == "ok" else "not read: " + (o.get("status") or "?").split("_")[0]) for o in allv.values())
        print("vendor billing: %d vendors newly read or changed; on file %d: %s" % (len(new), len(allv), ", ".join("%s %d" % kv for kv in k.most_common())))
        return
    import run_box
    k, n = (int(x) for x in a.shard.split("/"))
    have = {} if a.redo else load()
    only = {d.strip() for d in a.only.split(",") if d.strip()}
    if only:
        tasks = [(d, "", 0, ()) for d in sorted(only)]
    else:
        import zlib
        tasks = [t for t in candidates() if (t[0] not in have or due(have[t[0]])) and zlib.crc32(t[0].encode()) % n == k]
    if a.limit:
        tasks = tasks[:a.limit]
    os.makedirs("out", exist_ok=True)
    print("shard %d/%d: %d vendors to read (%d on file)" % (k, n, len(tasks), len(have)), flush=True)
    import threading
    lock, stats = threading.Lock(), collections.Counter()
    fo = open("out/vendor_billing_%d.jsonl" % k, "a", encoding="utf-8")
    box = run_box.Box(a.minutes)

    def one(t):
        try:
            rec = read_vendor(t[0], extra=t[3])
        except Exception as e:
            rec = {"dom": t[0], "date": TODAY, "status": "error:" + type(e).__name__, "pages": [], "stmts": [], "v": V}
        rec["leads"] = t[2]
        with lock:
            stats["vendors"] += 1
            stats[cycle_of(rec)[0] or ("no statement" if rec["status"] == "ok" else rec["status"].split("_")[0].split(":")[0])] += 1
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if stats["vendors"] % 200 == 0:
                fo.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    whole = box.run(one, tasks, a.workers)
    with lock:
        fo.flush()
        os.fsync(fo.fileno())
    print("finished" if whole else "stopped by the time box: %d of %d vendors read" % (stats["vendors"], len(tasks)), dict(stats), flush=True)
    box.leave(0)


if __name__ == "__main__":
    main()
