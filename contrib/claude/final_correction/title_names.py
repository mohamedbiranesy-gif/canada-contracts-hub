"""The last cleaning of a buyer's name read from a page title (2026-11-14, the corrected table of 2026-11-14 read row by row).

What a page's title or a crawler's cut leaves around an organisation's name, and the name inside it:
  "https://www.moversajax.ca/"                         → moversajax.ca              (an address written as the name)
  "info@couleursdenfants.ca", "@gabecaubvick"          → the site's domain name      (a mailbox or a social handle written as the name)
  "Sherway Academy Music School 416 259-0251"          → Sherway Academy Music School (a telephone number after the name)
  "SmarTech Engineering is under construction"         → SmarTech Engineering         (a placeholder page)
  "Welcome: Trustworthiness Research Alliance"         → Trustworthiness Research Alliance
  "Cadmus Home Page", "Page d'accueil du CCGV"         → Cadmus, CCGV
  "Site officiel des Super Recycleurs", "Metal Justice Official Site" → Super Recycleurs, Metal Justice
  "Victoria Plating Ltd. > Victoria, BC, Canada"      → Victoria Plating Ltd.        (a breadcrumb)
  "SaveOnBlanks.ca Canada's lowest priced supplier …"  → SaveOnBlanks.ca              (a slogan after the brand)
  "Christine Hennen Photography © 2016"                → Christine Hennen Photography
  "Stellar Upgrades · A trade name of Right Wire …"    → Stellar Upgrades
  "Mainville & Associates/AssociÃ©s Inc."              → Mainville & Associates/Associés Inc. (UTF-8 read as Latin-1)
A word that belongs to the name stays: the guard is the organisation's own domain ("Home Hardware" on homehardware.ca, "Welcome Jobs" on
welcomejobs.ca, "Homepage Property Management" on homepageproperty.com, "China \"Made in England\"" on chinamadeinengland.com), and a brand
written with an at sign stays ("Heal@Home", "Dentistry@Wendover"). Every rule was read against the rows it changes before it was kept.
"""
import re
import unicodedata

SEP = r"[\s,;:>|/·•»«~\-–—｜_^<★☆◆◇■□▶►✓✔]"
_FUNC_END = re.compile(r"(?i)\s(?:by|de|du|des|the|of|and|et|à|a|la|le|les|to|for|pour|par|est|is|in|en|at|au|aux|with|avec|vous|your|votre)$")
_PHONE = re.compile(r"(?:\+?1[\s.-]?)?\(?\b\d{3}\)?[\s.-]?\d{3}[\s.-]\d{4}\b|\b1[\s.-]?8\d\d[\s.-]\d{3}[\s.-]\d{4}\b")
_MAIL = re.compile(r"[A-Za-z0-9._+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+|\b(?:info|sales|contact|admin|office|hello|support|mail|email|courriel|bonjour|reception|ventes)@[a-z0-9-]{3,}\b", re.I)
_ROLE_LOCAL = re.compile(r"(?i)^(?:info|sales|contact|admin|office|hello|support|mail|email|courriel|bonjour|reception|ventes)@")
_URL = re.compile(r"(?i)^(?:https?:)?/{2,}(?:www\.)?([a-z0-9][a-z0-9.-]*\.[a-z]{2,})(?:/[\w./-]{0,40})?$")
_HOST = re.compile(r"(?i)^[a-z0-9-]+(?:\.[a-z0-9-]+)+$")
_QTRANS = re.compile(r"^\[:[a-z]{2}\](.+?)\[:[a-z]{2}\].*$")
_BRACKETS = re.compile(r"^[\[(]\s*(.+?)\s*[\])]$")
_DECOR = re.compile(r"^[\s.:]{2,}|[\s.:]{2,}$")
_CONSTRUCT = re.compile(r"(?i)^(.+?)\s*(?:[-–—:|,/]\s*)?(?:(?:is|est)\s+)?(?:temporarily\s+|temporairement\s+)?(?:(?:site|site web|web\s?site|new web\s?site)\s+)?"
                        r"(?:under construction|coming soon|en construction|en maintenance|under maintenance)\s*[!.…]*$")
_CONSTRUCT_HEAD = re.compile(r"(?i)^(?:en construction|under construction|coming soon)\s*[-–—:|]?\s+")
_SITE_TAIL = re.compile(r"(?i)(?:[\s\-–—,/]+)(?:site(?: web)?|web\s?site|new web\s?site|nouveau site)$")
_JUST_SITE = re.compile(r"(?i)^(?:site(?: web)?|web\s?site|new web\s?site|nouveau site|page|site internet)$")
_HOMEPAGE_TAIL = re.compile(r"(?i)\s*(?:[-–—|:•·»｜_]+\s*)?(?:['’]s\s+)?(?:home\s?page|page d['’]accueil)\s*$")
_HOMEPAGE_HEAD = re.compile(r"(?i)^(?:this is\s+)?(?:the\s+)?(?:home\s?page|page d['’]accueil)(?:\s+(?:du|de la|de l['’]|des|de|d['’]|of(?: the)?|for(?: the)?))?\s*(?:[-–—|:•·»｜_]+\s*)?")
_BARE_HOME = re.compile(r"(?i)^(?:home|accueil)\s+(?:[-–—|:•·»｜]\s*)?")
_OFFICIAL_HEAD = re.compile(r"(?i)^(?:le\s+)?site officiel\s+(?:de la\s+|de l['’]\s*|des\s+|du\s+|de\s+|d['’]\s*)?|^official (?:web\s?)?site of\s+(?:the\s+)?")
_OFFICIAL_TAIL = re.compile(r"(?i)\s*(?:[-–—|:•·»｜]+\s*)?(?:['’]s\s+)?(?:official (?:web\s?)?site|site officiel)\s*$")
_WELCOME = re.compile(r"(?i)^(?:register now\s+)?(?:welcome|bienvenue)(?:[\s_/|-]+(?:welcome|bienvenue))*(?:\s+home)?(?:\s+to)?"
                      r"(?:\s+(?:dans l['’]univers (?:du|de la|de l['’]|des|de)|chez|à|au|aux|sur (?:le site (?:de|du|des)|votre site)))?\s*[:\-–—|,_]?\s*")
_WELCOME_TAIL = re.compile(r"(?i)\s*(?:[-–—|:•·»｜]+\s*)?(?:vous souhaite (?:la )?bienvenue|welcomes you|welcome|bienvenue)(?:\s+sur votre site)?\s*[!.:]*$")
_WELCOME_GUESTS = re.compile(r"(?i)\s+(?:customers|clients|friends|everyone)\s*!?$")
_DOMAIN_LED = re.compile(r"^([A-Za-z0-9][A-Za-z0-9-]*\.(?:ca|com|net|org|biz|info|co|qc\.ca))\s+(?:[-–—:|]\s*)?(.+)$")
_ORG_WORD = (r"inc|ltd|ltée|limited|corp|corporation|society|soci[ée]t[ée]|association|foundation|fondation|cooperative|coop[ée]rative|institute|"
             r"council|club|centre|center|church|federation|f[ée]d[ée]ration|alliance|network|r[ée]seau")
_ORG_END = re.compile(r"(?i)\b(?:" + _ORG_WORD + r")\.?$")
_ORG_HEAD = re.compile(r"(?i)^(?:" + _ORG_WORD + r")\b")
_COPY = [re.compile(r"(?i)\s*(?:and\s+(?:are\s+)?)?(?:protected by copyright|copyright protected)\b.*$"), re.compile(r"(?i)\s+copyright(?:\s+scan qr code)?\s*$"),
         re.compile(r"(?i)[.,]?\s*(?:all rights reserved|tous droits r[ée]serv[ée]s)\.?\s*$"),
         re.compile(r"(?i)^x\s+copyright\s+"), re.compile(r"\s*©\s*(?:(?:19|20)\d{2})?\s*$")]
_LEAD_YEAR = re.compile(r"^(?:19|20)\d{2}(?:\s*[-–]\s*(?:19|20)\d{2}\s+|\s*[·•|\-–—]\s*)")
_DIVISION = re.compile(r"(?i)\s+(?:is a (?:division|subsidiary|trade name) of|a (?:division|trade name) of|is operated by|operated by|une division de|est une division de)\b.*$")
_DOT_SEP = re.compile(r"\s+[·•]\s+")
_HANDLE_TAIL = re.compile(r"\s+@[A-Za-z0-9_]{3,}$")
_QUOTED = re.compile(r"^(.*?)\s*[\"“«]\s*([^\"”»]{3,}?)\s*[\"”»]\s*$")
_CONTACT_TAIL = re.compile(r"(?i)\s+(?:e-?mail|courriel|t[ée]l(?:[ée]phone)?\.?|phone|call(?: us)?(?: now)?|contact(?: us)?(?: at)?|joignez-nous|☎|✆|📞)\s*:?\s*$")
# alone (no telephone number or mailbox removed before it), only the forms that cannot be a name's own word: "Drivers On Call", "Phoenix Contact" and
# "Electro Tel" keep their last word
_CONTACT_ALONE = re.compile(r"(?i)(?:\s+(?:contact us(?: at)?|call us(?: now)?|call now|e-?mail us|joignez-nous)|\s*:\s*(?:contact|contactez-nous|nous joindre)|\s+[☎✆📞])\s*:?\s*$")
_MENU_TAIL = re.compile(r"(?i)\s+(?:previous\s+next|skip to (?:main )?content|open menu|toggle navigation|close menu)$")
_STREET = re.compile(r"\s+\d{1,5}[A-Za-z]?,?\s+(?:[\w'’.-]+\s+){0,4}(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Dr|Drive|Line|Hwy|Highway|Way|Lane|Crescent|Cres|Court|Ct|"
                     r"Place|Pl|rue|chemin|boul|avenue|route|rang|Sideroad|Concession)\b.*$")
_PROV = (r"(?:ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NT|NU|Ont\.?|Ontario|Quebec|Québec|British Columbia|Alberta|Manitoba|Saskatchewan|Nova Scotia|New Brunswick|"
         r"Newfoundland(?: and Labrador)?|Prince Edward Island|Yukon)")
_PLACE_TAIL = re.compile(r"^([^,]{3,}?),\s+(?:[A-ZÀ-Ý][\w'’.-]*(?:[\s-]+[A-ZÀ-Ý][\w'’.-]*){0,3},?\s+)?" + _PROV + r"\.?(?:,?\s+Canada)?$")
_LOCATED = re.compile(r"(?i)\s+(?:located|situated|based|situ[ée]e?) (?:in|à|au)\b.*$")
_PART_OF = re.compile(r"(?i)\s+(?:a\s+)?part of (?:the\s+)?\S.*$")
_LEGAL_COMMA = re.compile(r"^(.{3,}?\b(?:Inc|Ltd|Ltée|Limited|Corp|Corporation|LLP|Incorporated)\.?),\s*(?!Brokerage\b)\S.*$")
_LEGAL_TAIL = re.compile(r"(?i)\b(?:inc|ltée|lt[ée]e|ltd|limited|limit[ée]e|corp|enr|s\.?e\.?n\.?c(?:\.?r\.?l)?|incorporated|incorpor[ée]e|naamloze vennootschap|"
                         r"besloten vennootschap|soci[ée]t[ée] anonyme|sociedad an[oó]nima|aktiengesellschaft|s\.?a\.?s?|s\.?r\.?l|gmbh|ag|nv|bv|oy|ab|plc|llc|lp|llp)\.?\s*$")
_CONTINUES = re.compile(r"(?i)^(?:de|du|des|d['’]|et|and|of|the|la|le|les|l['’]|en|pour|for|&)\b")
_LEADS = re.compile(r"(?i)^(?:for|since|depuis|pour|over|with|avec|plus de|more than|over)\b")
_TAGS = re.compile(r"<[^>]{1,200}>")
_COMMA_SLOGAN = re.compile(r"^([^,]{3,}),\s+(by\s+.+|[a-z][^,]{8,}.*)$")
_PAGE_WORD = re.compile(r"(?i)^(?:home|accueil|index|welcome|bienvenue|site|website|site web|page|untitled)$")
_MOJI = re.compile(r"Ã[\x80-\xbf¡-¿]|Â[\x80-\xbf¡-¿]|Ã\x81")


def _sq(t):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower())


def _strip_ends(b):
    return re.sub(r"^" + SEP + r"+|" + SEP + r"+$", "", b)


def demojibake(s):
    """UTF-8 read as Latin-1 / Windows-1252 ("AssociÃ©s" → "Associés"), when the reading back is clean"""
    if not s or not _MOJI.search(s):
        return s
    for enc in ("latin-1", "cp1252"):
        try:
            t = s.encode(enc).decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue
        if not _MOJI.search(t) and "�" not in t:
            return t
    return s


def _ok(t):
    t = (t or "").strip()
    return len(t) >= 3 and not _PAGE_WORD.match(t) and not _FUNC_END.search(t) and not re.fullmatch(r"[\W_]+", t)


def _pass(b, lab, domain):
    """one pass of every rule; (name, rule) — the rule of the last change"""
    rule = ""

    def take(t, why):
        nonlocal b, rule
        if (t or "").strip() == b:
            return False
        t = re.sub(r"\s{2,}", " ", (t or "").strip())
        if t != b and _ok(t):
            b, rule = t, why
            return True
        return False

    take(re.sub(r"\s{2,}", " ", b), "double spaces collapsed")
    if _TAGS.search(b):
        take(_TAGS.sub(" ", b), "HTML tags around the name removed")
    take(demojibake(b), "UTF-8 read as Latin-1, read back")
    m = _QTRANS.match(b)
    if m:
        take(m.group(1), "a multilingual plug-in's tags ([:en] … [:fr] …): the first language's name")
    m = _BRACKETS.match(b)
    if m:
        take(m.group(1), "the brackets around the name removed")
    t = _DECOR.sub("", b)
    if t != b:
        take(t, "decorative dots and colons around the name removed")
    m = _URL.match(b)
    if m:
        return (domain or m.group(1).lower()), "an address written as the name: the domain name"
    if domain and _HOST.match(b) and b.lower() == "www." + domain:
        return domain, "a host name written as the name (www. …): the domain name"
    if domain and (re.fullmatch(r"[A-Za-z0-9._+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+", b) or (_ROLE_LOCAL.match(b) and re.fullmatch(r"\S+@\S+", b))
                   or re.fullmatch(r"@[A-Za-z0-9_.]{3,}", b)):
        return domain, "a mailbox or a social handle written as the name: the domain name"
    if _PHONE.search(b) or _MAIL.search(b):
        t = _MAIL.sub(" ", b)
        p = _PHONE.search(t)
        if p:
            before, after = t[:p.start()], _PHONE.sub(" ", t[p.end():])
            t = before if _ok(_strip_ends(before)) else after
        t = _strip_ends(re.sub(r"\s+", " ", t))
        if ":" in t and _ok(re.split(r"\s*:\s+", t)[0]):
            t = re.split(r"\s*:\s+", t)[0]
        t = _strip_ends(_CONTACT_TAIL.sub("", _strip_ends(t)))
        if _ok(t) and (len(t.split()) > 1 or (lab and _sq(t) in lab)):
            take(t, "a telephone number or a mailbox beside the name, removed")
        elif domain:
            return domain, "a telephone number or a mailbox written as the name: the domain name"
    m = _CONSTRUCT.match(b)
    if m and "construction" not in lab and "comingsoon" not in lab:
        t = re.sub(r"\s+(?:19|20)\d{2}$", "", _strip_ends(m.group(1)))
        t = _strip_ends(_SITE_TAIL.sub("", t))
        if _JUST_SITE.match(t) and domain:
            return domain, "a placeholder page's words (under construction, coming soon): the domain name"
        take(t, "a placeholder page's words (under construction, coming soon) removed")
    t = _CONSTRUCT_HEAD.sub("", b)
    if t != b and "construction" not in lab:
        take(t, "a placeholder page's words (under construction, coming soon) removed")
    if "homepage" not in lab:
        t = _HOMEPAGE_HEAD.sub("", _HOMEPAGE_TAIL.sub("", b))
        if t != b:
            t = _strip_ends(_SITE_TAIL.sub("", _strip_ends(t)))
            take(t, "the words Home page / Page d'accueil removed")
    m = _BARE_HOME.match(b)
    if m and lab and not lab.startswith(("home", "accueil")):
        rest = b[m.end():]
        if _sq(rest) and (lab.startswith(_sq(rest)[:8]) or _sq(rest).startswith(lab[:8])):
            take(rest, "the page-title word Home / Accueil before the name removed")
    if "officiel" not in lab and "official" not in lab:
        t = _OFFICIAL_TAIL.sub("", _OFFICIAL_HEAD.sub("", b))
        if t != b:
            t = _strip_ends(t)
            m2 = re.match(r"^\S+\.(?:ca|com|org|net|qc\.ca)\s+(?:de la|de l['’]|du|des|de|of the|of)\s*(.{3,})$", t)
            take(m2.group(1) if m2 else t, "the words Official site / Site officiel removed")
    if "welcome" not in lab and "bienvenue" not in lab and not _HOST.match(b):
        t = _WELCOME_TAIL.sub("", _WELCOME.sub("", b))
        if t != b:
            t = _strip_ends(_WELCOME_GUESTS.sub("", _strip_ends(t)))
            if not re.match(r"(?i)^(?:&|and|et)\b", t) and (len(t.split()) > 1 or (lab and (lab.startswith(_sq(t)) or _sq(t) == lab))):
                take(t, "the words Welcome / Bienvenue removed")
    if " > " in b:
        parts = [p.strip() for p in b.split(" > ") if p.strip() and not _PAGE_WORD.match(p.strip())]
        if parts:
            if len(parts) >= 2 and parts[0].isupper() and len(parts[0]) <= 8 and len(parts[1]) > len(parts[0]) + 5:
                take("%s (%s)" % (parts[1], parts[0]), "a breadcrumb (A > B): the organisation's part")
            else:
                take(parts[0], "a breadcrumb (A > B): the organisation's part")
    m = _DOMAIN_LED.match(b)
    if m and len(m.group(2).split()) >= 3:
        rest = _strip_ends(m.group(2))
        good = not re.match(r"(?i)^(?:and|et|is|div|&|who we are)\b", rest) and (_ORG_HEAD.search(rest) or (len(rest.split()) <= 4 and _ORG_END.search(rest)))
        take(rest if good else m.group(1), "a slogan or a line after the site's brand, removed")
    for p in _COPY:
        t = p.sub("", b)
        if t != b:
            take(_strip_ends(t), "a copyright line removed")
    t = _LEAD_YEAR.sub("", b)
    if t != b:
        take(t, "a year before the name removed")
    t = _DIVISION.sub("", b)
    if t != b:
        take(_strip_ends(t), "who operates it or whose division it is, after the name, removed")
    if _DOT_SEP.search(b):
        take(_strip_ends(_DOT_SEP.split(b)[0]), "a line after a dot separator (address, trade-name note) removed")
    t = _HANDLE_TAIL.sub("", b)
    if t != b:
        take(t, "a social handle after the name removed")
    m = _QUOTED.match(b)
    if m:
        head, q = m.group(1).strip(), m.group(2).strip()
        hw = {_sq(w) for w in re.findall(r"[\w'’-]+", head)}
        own = lab and any(len(_sq(w)) >= 4 and _sq(w) in lab and _sq(w) not in hw for w in re.findall(r"[\w'’-]+", q))
        if own and len(head.split()) <= 2:
            take("%s %s" % (head, q) if _sq(head + q) == lab or not head else q, "the quotation marks of the name removed")
        elif own:
            take("%s %s" % (head, q), "the quotation marks of the name removed")
        else:
            take(head, "a quoted slogan after the name removed")
    t = _CONTACT_ALONE.sub("", b)
    if t != b:
        take(_strip_ends(t), "a contact word after the name removed (Contact us at, Call now …)")
    t = _MENU_TAIL.sub("", b)
    if t != b:
        take(t, "a menu's words after the name removed")
    t = _LOCATED.sub("", b)
    if t != b and len(t.split()) >= 1:
        take(_strip_ends(t), "where it is located, after the name, removed")
    t = _PART_OF.sub("", b)
    if t != b and len(t.split()) >= 1:
        take(_strip_ends(t), "the pavilion or group it is part of, after the name, removed")
    t = _STREET.sub("", b)
    if t != b and len(t.split()) >= 2:
        take(_strip_ends(t), "a street address after the name removed")
    m = _PLACE_TAIL.match(b)
    if m and len(m.group(1).split()) >= 2:
        take(_strip_ends(m.group(1)), "a town and province after the name removed")
    m = _LEGAL_COMMA.match(b)
    if m:
        take(m.group(1), "what follows the legal form after a comma, removed")
    m = _COMMA_SLOGAN.match(b)
    if m:
        head, tail = m.group(1).strip(), m.group(2)
        in_lab = lambda w: len(_sq(w)) >= 4 and lab and _sq(w) in lab
        if (not any(in_lab(w) for w in re.findall(r"[\w'’-]+", tail)) and not _CONTINUES.match(tail) and not _LEGAL_TAIL.search(tail) and not _LEADS.match(head)
                and (len(head.split()) >= 2 or (lab and (_sq(head) in lab or lab in _sq(head))))):
            take(re.split(r"\s*:\s+", head)[0] if ":" in head else head, "a description after a comma, removed")
    t = _strip_ends(b)
    if t != b:
        take(t, rule or "a separator left at either end removed")
    return b, rule


def clean_title_name(b, label, domain):
    """(the name, the rule that changed it or ''); label = the first label of the organisation's own registrable domain ('' with no site), domain = that domain"""
    b0 = b = (b or "").strip()
    lab = re.sub(r"[^a-z0-9]", "", (label or "").lower())
    rules = []
    for _ in range(3):
        nb, r = _pass(b, lab, domain or "")
        if nb == b:
            break
        b = nb
        rules.append(r)
    return (b, rules[0] if len(rules) == 1 else "; ".join(dict.fromkeys(rules))) if b != b0 else (b0, "")
