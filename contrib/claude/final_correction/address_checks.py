"""Two checks of a buyer's address against its own site and mailbox (2026-11-14, the corrected table read row by row).

1. A web platform's own address printed on an organisation's pages is not the organisation's address. Privacy and legal pages name the companies
   whose services the site uses — "Google LLC, 1600 Amphitheatre Parkway", "Cloudflare, Inc., 101 Townsend St.", "Shopify Inc., 151 O'Connor
   Street, Ottawa" (every Shopify store's legal notice) — and the address reader took them for the organisation's. On a row that stands on where the
   organisation is, that address named the electricity distributor (a Belgian store "in Ottawa", billed by Hydro Ottawa): the row has no relationship.
   The platform's part is taken out of the address; the rest of the address (a second address read elsewhere) stays.
2. A mailbox or a site of another country than the organisation's address: CARE USA (Atlanta) with care.org.au's mailbox, the U.S. Department of the
   Treasury with treasury.gov.au, Deloitte & Touche LLP (Arlington, VA) with deloitte.be's mailbox, a Québec contractor registered at the Régie with a
   French namesake's site (colortech.fr). Which of the two is wrong is read from where the address came from: an address read on the organisation's
   own site of another country is another office's or a third party's (taken out, the row stays); a mailbox on another country's domain than both the
   site and the address is an affiliate's or a namesake's (the row is held); a register's or a record's address in one country with a site and a
   mailbox of another is a namesake's site (held); a row that stands on where the organisation is has nothing else (held).
"""
import re
import unicodedata
import urllib.parse

PLATFORMS = [("Google", r"1600 amphitheatre"), ("Cloudflare", r"101 townsend st"), ("YouTube", r"901 cherry av"), ("Meta", r"\b1 hacker way|1601 willow r"),
             ("Microsoft", r"one microsoft way"), ("Amazon", r"410 terry av"), ("Apple", r"one apple park way|\b1 infinite loop"), ("X / Twitter", r"1355 market st"),
             ("LinkedIn", r"1000 w(?:est|\.)? maude"), ("Wix", r"500 terry a\.? francois"), ("Squarespace", r"\b225 varick st|\b8 clarkson st"),
             ("GoDaddy", r"2155 e(?:ast|\.)? godaddy way|14455 n(?:orth|\.)? hayden"), ("Automattic", r"\b60 29th st"), ("Mailchimp", r"675 ponce de leon av"),
             ("HubSpot", r"\b25 first st(?:reet)?,? cambridge|\b2 canal park"), ("Stripe", r"354 oyster point|\b510 townsend st"), ("PayPal", r"2211 n(?:orth|\.)? first st"),
             ("Zoom", r"\b55 almaden"), ("Salesforce", r"\b415 mission st"), ("Dropbox", r"1800 owens st"), ("Shopify", r"\b151 o['’]?\s?connor st"),
             ("Shopify", r"\b126 york st"), ("Lightspeed", r"\b700 (?:rue )?(?:saint|st)[- ]antoine (?:st(?:reet)? )?(?:e\b|east|est)"),
             ("Google", r"gordon house"), ("Meta", r"4 grand canal sq"), ("Amazon", r"38 av(?:enue)? john f\.? kennedy"), ("Yelp", r"\b350 mission st"),
             ("Weebly", r"460 bryant st"), ("eBay", r"2025 hamilton av"), ("Etsy", r"\b117 adams st"), ("Constant Contact", r"1601 trapelo")]
_PL = [(n, re.compile(p, re.I)) for n, p in PLATFORMS]
# the platforms themselves, and organisations whose own head office is in one of those buildings (read on their own sites, 2026-11-14)
_OWN = re.compile(r"(?i)google|cloudflare|youtube|facebook|meta platforms|instagram|microsoft|amazon|apple|twitter|linkedin|wix|squarespace|godaddy|automattic|"
                  r"wordpress|mailchimp|intuit|hubspot|stripe|paypal|zoom|salesforce|dropbox|shopify|lightspeed|yelp|weebly|ebay|etsy|constant contact")
_OWN_SITES = {"audubon.org", "vir.bio"}
# a page that names a store's host: Shopify's old Ottawa address is a real office building; only a store's policy or legal page makes it the host's
_POLICY_PAGE = re.compile(r"(?i)/polic(?:y|ies)|legal|mentions|privacy|confidentialit|datenschutz|impressum|terms|cookies")
CC = {"de": "DE", "fr": "FR", "it": "IT", "es": "ES", "nl": "NL", "be": "BE", "ch": "CH", "at": "AT", "pl": "PL", "se": "SE", "dk": "DK", "no": "NO", "fi": "FI",
      "pt": "PT", "cz": "CZ", "hu": "HU", "ro": "RO", "gr": "GR", "ie": "IE", "uk": "GB", "au": "AU", "nz": "NZ", "jp": "JP", "cn": "CN", "in": "IN", "br": "BR",
      "mx": "MX", "za": "ZA", "ca": "CA", "us": "US", "ar": "AR", "cl": "CL", "kr": "KR", "sg": "SG", "il": "IL", "tr": "TR", "ru": "RU", "ua": "UA", "sk": "SK",
      "si": "SI", "hr": "HR", "bg": "BG", "lt": "LT", "lv": "LV", "ee": "EE", "lu": "LU", "is": "IS", "hk": "HK", "tw": "TW", "my": "MY", "th": "TH", "ph": "PH",
      "id": "ID", "vn": "VN", "pk": "PK", "ng": "NG", "ke": "KE", "eg": "EG", "sa": "SA", "ae": "AE", "co": None, "io": None, "ai": None, "me": None, "tv": None,
      "cc": None, "ws": None, "fm": None, "gg": None, "ly": None, "to": None, "la": None, "am": None, "nu": None, "eu": None}
_US_ST = r"(?:AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY|DC)"
_CA_POST = re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[A-Z]\s?\d[A-Z]\d\b", re.I)
_US_ZIP = re.compile(r"(?:,|\s)\s*" + _US_ST + r",?\s+\d{5}(?:-\d{4})?\b|\b(?:USA|United States(?: of America)?)\b")
# (a British postcode pattern is not used: a Canadian postal code typed with the letter O for a zero — "P0P 1HO", "M1R 1ZR" — reads as one)
_COUNTRY_WORD = [("AU", r"\bAustralia\b|\b(?:NSW|VIC|QLD|ACT)\s+\d{4}\b"), ("GB", r"\bUnited Kingdom\b|\bEngland\b|\bScotland\b|\bWales\b"),
                 ("DE", r"\bGermany\b|\bDeutschland\b"), ("FR", r"\bFrance\b"), ("IT", r"\bItaly\b|\bItalia\b"), ("ES", r"\bSpain\b|\bEspaña\b"),
                 ("CH", r"\bSwitzerland\b|\bSchweiz\b|\bSuisse\b"), ("NL", r"\bNetherlands\b|\bNederland\b"), ("BE", r"\bBelgium\b|\bBelgique\b|\bBelgië\b"),
                 ("AT", r"\bAustria\b|\bÖsterreich\b")]
_SITE_SRC = re.compile(r"as printed on https?://|as its own page|own page prints|structured data|PostalAddress|beside the organisation's mailbox|the address an? (?:Overture|Foursquare)|"
                       r"Overture Maps place|Foursquare place|the city the organisation|its own privacy|its home page", re.I)
_LOC_KINDS = ("utility account by location", "utility account by own report")
# the legal forms that say a company's country, to tell which of a mailbox and an address is the organisation's own (2026-11-14: "Rollsroller AB"
# with rollsroller.se and a Chicago office's address, "BorTec GmbH" with bortec.de and an Alberta office's: the mailbox is the company's own)
_FORM_CC = [(r"\bAB\b(?:\s*\(publ\))?$", 0, {"SE"}), (r"\bAG\b|\bKG\b", 0, {"DE", "AT", "CH"}), (r"\bGmbH\b|\bmbH\b|\be\.\s?V\.", re.I, {"DE", "AT", "CH"}),
            (r"\bS\.?A\.?S\.?$|\bSARL\b|\bS\.A\.R\.L\.|\bS\.?N\.?C\.?$", re.I, {"FR", "BE", "LU", "CH"}), (r"\bS\.?p\.?A\.?$|\bS\.?r\.?l\.?$", re.I, {"IT"}),
            (r"\bB\.?V\.?$|\bN\.?V\.?$", re.I, {"NL", "BE"}), (r"\bA/S\b|\bApS\b", re.I, {"DK", "NO"}), (r"\bAS\b$|\bASA\b$", 0, {"NO"}), (r"\bOyj?\b", 0, {"FI"}),
            (r"\bPty\.?\s+Ltd|\bPTY\b", re.I, {"AU"}), (r"\bS\.?L\.?U?\.?$|\bS\.? L\.?$", 0, {"ES"}), (r"\bKft\.?$|\bZrt\.?$", re.I, {"HU"}),
            (r"\bs\.?r\.?o\.?$", re.I, {"CZ", "SK"}), (r"\bsp\.?\s?z\s?o\.?\s?o\.?", re.I, {"PL"}), (r"\bK\.?K\.?$|Kabushiki", re.I, {"JP"}),
            (r"\bLtda\.?$", re.I, {"BR", "CO", "PT"})]
_MISSION = re.compile(r"(?i)\b(?:embassy|consulate|high commission|ambassade|consulat|haut-commissariat|delegation|délégation|permanent mission|mission permanente)\b")
_PLACEHOLDER = re.compile(r"(?i)here\s*we\s*are\s+st|vivas\s+2355|\b123 (?:fake|sample|your) st|1234 street name|your (?:street )?address here|lorem ipsum|"
                          r"street name,? city name|address line [12]\b|\bsample address")


def form_cc(name):
    n = (name or "").strip().rstrip(",.").strip()
    for rx, fl, cc in _FORM_CC:
        if re.search(rx, n, fl):
            return cc
    return set()


def is_placeholder(body):
    """a site template's sample address: "123 Main Street, New York, NY 10001", "123 Main Street Toronto, ON M1M 1M1", "1234 Street Name City Name",
    "Here Weare St, Melbourne, Vivas 2355", lorem ipsum — not a real "123 Main Street, White Plains, NY 10601" (the New York Power Authority's)"""
    b = body or ""
    if _PLACEHOLDER.search(b):
        return True
    if re.search(r"(?i)\b1234? main st", b):
        return bool(re.search(r"\b([A-Z])\d\1\s?\d\1\d\b|\b[A-Z]1[A-Z]\s?1[A-Z]1\b|\b[A-Z]\d[A-Z]\s?1A1\b|\bK1A\s?0A1\b|(?i:new york,? ny 10001|denver,? co 80202|anytown)", b))
    return False


def host(u):
    try:
        return (urllib.parse.urlsplit(u if "//" in u else "//" + u).hostname or "").lower()
    except Exception:
        return ""


def cc_of(h, name=""):
    """the country of a host's top-level domain, or None (generic, or a country-code domain used as generic: .co .io .ai .me .tv …, or a domain hack
    whose last letters finish the organisation's name: fullp.in for "Full Pin")"""
    tld = h.rsplit(".", 1)[-1] if "." in (h or "") else ""
    lab = h.rsplit(".", 2)[-2] if h.count(".") >= 1 else ""
    if name and lab and len(tld) == 2:
        sq = re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower())
        if sq and sq.startswith(re.sub(r"[^a-z0-9]", "", lab + tld)):
            return None
    return CC.get(tld)


def country_of_address(a):
    a = unicodedata.normalize("NFKC", a or "")
    if _CA_POST.search(a):
        return "CA"
    if _US_ZIP.search(a):
        return "US"
    for c, p in _COUNTRY_WORD:
        if re.search(p, a):
            return c
    return None


_PROV_NOTE = re.compile(r"\s\((?:as |the |its |registered|CRA |schema|structured|label|read |from |a public|registre|printed|it bears|regist)")


def body_of(p):
    """an address part without its provenance note ("Saguenay (Québec), G7G4V5 (as the organisation declares it …)" keeps "(Québec), G7G4V5")"""
    m = _PROV_NOTE.search(p or "")
    return (p[:m.start()] if m else (p or "")).strip()


def split_parts(addr):
    """the parts of a buyer_address cell ("A (as printed on …); B (the address an Overture Maps place …)")"""
    return [p for p in re.split(r";\s+(?=\S)", addr or "") if p.strip()] if addr else []


def platform_parts(x, registrable):
    """the parts of the buyer's address that are a web platform's own address: [(part, platform)]"""
    name = x.get("buyer") or ""
    site = registrable(host(x.get("buyer_website") or "")) if x.get("buyer_website") else ""
    if _OWN.search(name) or (site and (_OWN.search(site.split(".")[0]) or site in _OWN_SITES)):
        return []
    out = []
    for p in split_parts(x.get("buyer_address") or ""):
        body = unicodedata.normalize("NFKC", p).replace("\xa0", " ")
        for n, rx in _PL:
            if rx.search(body):
                if n == "Shopify" and "126 york" in body.lower() and not _POLICY_PAGE.search(body):
                    continue
                out.append((p, n))
                break
    return out


def own_ca_site(parts, mdd, name):
    """the address was printed on the organisation's own Canadian site, whose name is the mailbox's under another ending (etaya.ca and etaya.in,
    transportselectpro.ca and .fr) — not for "… Canada", a national office whose mailbox abroad is its parent's (Muslim Hands Canada, Koppert Canada)"""
    if not mdd or re.search(r"(?i)\bcanad", name or ""):
        return False
    lab = mdd.split(".")[0]
    for p in parts:
        m = re.search(r"(?:as printed on|on) https?://(?:www\.)?([^/ )]+)", p)
        if m:
            h = m.group(1).lower()
            if h.endswith(".ca") and h.split(".")[-2] == lab:
                return True
    return False


def located_by(x, parts):
    """does one of these address parts carry what named the distributor (the postal area, or the town all of whose codes are its)?"""
    b = x.get("relationship_fact_basis") or ""
    m = re.search(r"\(([A-Z]\d[A-Z])\)\s+lies in", b)
    c = re.search(r"\(city ([^,()]+),", b)
    for k in parts:
        kk = re.sub(r"\s", "", k.upper())
        if (m and m.group(1) in kk) or (c and c.group(1).strip().lower() in k.lower()):
            return True
    return False


def check(x, kind, registrable):
    """(new buyer_address or None, fault or '', what) — None: the address is unchanged"""
    new_addr, fault, what = None, "", ""
    parts = split_parts(x.get("buyer_address") or "")
    pp = platform_parts(x, registrable)
    if pp:
        drop = {p for p, _ in pp}
        keep = [p for p in parts if p not in drop]
        new_addr = "; ".join(keep)
        names = sorted({n for _, n in pp})
        what = "buyer address: a web platform's own address taken out (%s)" % ", ".join(names)
        if kind in _LOC_KINDS:
            if not located_by(x, keep):
                fault = ("relationship: the address the distributor was named for is a web platform's own (%s's: “%s”), printed on the organisation's "
                         "pages because its site uses that service — not where the organisation is" % (names[0], pp[0][0].split(" (")[0][:90]))
                what = "location row on a web platform's address: no relationship"
        parts = keep
    # a template's sample words before a real address in the same part ("1234 Street Name City Name, Country Nam … 1815 Alta Vista Drive Ottawa"):
    # the sample words go, the address stays
    fixed = [re.sub(r"(?i)^.*?\b(?:contact us|address|adresse)\s*:?\s+(?=\d+\s+\w)", "",
                    re.sub(r"(?i)1234 street name,? city name,? country nam(?:e)?\s*", "", p)) if re.search(r"(?i)1234 street name|contact us\s+address", p) else p
             for p in parts]
    if fixed != parts:
        parts = fixed
        new_addr = "; ".join(parts)
        what = what or "buyer address: a site template's sample words taken out"
    ph = [p for p in parts if is_placeholder(body_of(p))]
    if ph:
        parts = [p for p in parts if p not in ph]
        new_addr = "; ".join(parts)
        what = what or "buyer address: a site template's sample address taken out"
        if kind in _LOC_KINDS and not fault and not located_by(x, parts):
            fault = "relationship: the address the distributor was named for is a site template's sample address (“%s”)" % body_of(ph[0])[:80]
    # 2. the country of the mailbox and the site against the address
    ac = None
    for p in parts:
        ac = ac or country_of_address(body_of(p))
    from_site = bool(parts) and all(_SITE_SRC.search(p) for p in parts)
    if not ac and not parts:
        j = (x.get("jurisdiction") or "")[:2].upper()
        ac = j if j in ("US", "CA") and kind == "public contract" else None
        from_site = False
    sh = host(x.get("buyer_website") or "") if x.get("buyer_website") else ""
    md = (x.get("email") or "").split("@")[-1].lower() if "@" in (x.get("email") or "") else ""
    scc, mcc = cc_of(sh, x.get("buyer") or ""), cc_of(md, x.get("buyer") or "")
    if ac and not fault:
        sd, mdd = (registrable(sh) or sh) if sh else "", (registrable(md) or md) if md else ""
        mail_off = mcc and mcc != ac and not (ac == "CA" and mcc == "US") and not (ac == "US" and mcc == "CA")
        site_off = scc and scc != ac and not (ac == "CA" and scc == "US") and not (ac == "US" and scc == "CA")
        fc = form_cc(x.get("buyer") or "") | form_cc((x.get("buyer_legal_name_as_published") or "").split(" (")[0])
        own_mail = bool(mcc and mcc in fc)   # the company's legal form is the mailbox's country: the mailbox is its own, the address another office's
        own_word = (bool(parts) and any(re.search(r"(?:as printed on|on) https?://(?:[^ /)]*\.)?" + re.escape(mdd) + r"\b", p) for p in parts) if mdd else False) \
            or any("lists its telephone number" in p for p in parts) \
            or own_ca_site(parts, mdd, x.get("buyer") or "")   # the place at the telephone number its own site prints; its own Canadian site
        if _MISSION.search(x.get("buyer") or ""):
            pass  # an embassy or a consulate: its mailbox and site are its government's
        elif mail_off and own_mail and kind not in _LOC_KINDS:
            new_addr = "; ".join(p for p in parts if country_of_address(body_of(p)) in (None, mcc))
            what = "buyer address: another office's (the company's legal form and its mailbox are of %s), taken out" % mcc
        elif mail_off and mdd != sd:
            fault = ("mailbox: on another country's domain (%s) than the organisation's site and its address (%s) — an affiliate's abroad or a namesake's"
                     % (md, ac))
            what = "mailbox of another country than the site and the address: held"
        elif mail_off or (site_off and (mdd == sd or not md)):
            if kind in _LOC_KINDS:
                if not own_word:
                    fault = ("relationship: the organisation's site and mailbox are another country's (%s) than the address the distributor was named for "
                             "(%s), which was not read on that site — the organisation is not shown to be at that address" % (md or sh, ac))
                    what = "location row whose site or mailbox is another country's: held"
            elif from_site:
                new_addr = ""
                what = "buyer address: another country's than its own site and mailbox, read on that site (another office or a third party), taken out"
            else:
                fault = ("site: the organisation's site and mailbox are another country's (%s) than the address its record gives (%s) — likely a namesake's site"
                         % (md or sh, ac))
                what = "record's address in one country, site and mailbox of another: held (a namesake's site)"
    if new_addr is not None and new_addr == (x.get("buyer_address") or ""):
        new_addr = None
    return new_addr, fault, what
