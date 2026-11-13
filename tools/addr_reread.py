#!/usr/bin/env python3
"""Where an organisation is, read again on its own pages: the organisations with a confirmed role mailbox whose address names no distributor (no AI).

The rows that stand on where the organisation is (tools/by_location.py: the electricity distributor of its address bills it by law, every month,
on an invoice, paid through a bank) need the organisation's own address. The mailbox reader keeps the first postal address it sees in the VISIBLE
text of the pages it reads (tools/lead_crawl.py install_hooks). The rank build of 2026-11-13 04:08Z left 185,837 organisations with a confirmed
mailbox out for that reason alone ("no biller can be named for where it is"), 136,177 of them under a .ca name. A sample of 60 of those read again
(home page and up to three contact / about / location pages): 2 print a postal code in their text, 6 show their address only on the map their own
contact page embeds (“maps.google.com/maps?q=1131 Gainsborough Rd, London, Ontario”), 4 state it only in the page's structured data (schema.org
PostalAddress) — the organisation's own statements of where it is, in its own page's source, which the reader did not look at.

This reads those organisations' home page and up to three pages its own menu names as contact / about / location / hours, and keeps the first of:
  text    a Canadian postal address in the visible text (the same pattern as the mailbox reader: province, then postal code);
  jsonld  a schema.org PostalAddress of the organisation itself (an Organization / LocalBusiness / … object of the page's JSON-LD — never an
          event's venue, a person, a job posting or a product), in Canada (addressCountry CA / Canada, or a Canadian postal code);
  map     the address of the Google map its own page embeds (the place asked for in the map's address: q= / query=, or the place name of an
          embed's pb= string), when it carries a Canadian postal code or a city with its province.
A key the map's address carries (an API key) is never kept: only the address asked for. robots.txt obeyed, the project's user agent, the
project's reader (tools/ap_crawler.py: one request a second per host). A site that refuses the reader is left.

  pick   [--out F]                         the keys to read: confirmed mailbox (claude_buyer_ap_results_cccrawl*.csv, status found), no postal
                                           code in the site's facts or the mailbox's page, no city that names a distributor, not done before
  read   --shard K/N --minutes M --workers W  -> out/addr_reread_K.jsonl (one line per site: what was found, or why nothing)
  merge  DIR --stamp S                     -> data/incoming/claude/site_facts/facts_<S>a.gz (site facts lines with the address, the earlier
                                              line's name kept) + data/incoming/claude/site_facts/addr_reread_done.tsv (append-only)
"""
import argparse, csv, glob, gzip, html, json, os, re, sys, time, urllib.parse
import concurrent.futures as cf

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402
import by_location as BL  # noqa: E402

csv.field_size_limit(1 << 30)
INC = os.path.join(ROOT, "data/incoming/claude")
FACTS_DIR = os.path.join(INC, "site_facts")
DONE = os.path.join(FACTS_DIR, "addr_reread_done.tsv")
TARGETS = os.path.join(ROOT, "out/addr_targets.csv")
TODAY = time.strftime("%Y-%m-%d")
CONTACT = re.compile(r"contact|joindre|about|propos|location|find-us|visit|coordonn|nous-trouver|directions|hours|heures|adresse|address|bureau|office", re.I)
LD = re.compile(r"""<script[^>]+type\s*=\s*["']application/ld\+json["'][^>]*>(.*?)</script>""", re.I | re.S)
IFRAME = re.compile(r"""<iframe\b[^>]*?\bsrc\s*=\s*["']([^"']+)["']""", re.I)
MAPHOST = re.compile(r"^https?://(?:www\.|maps\.)?google\.[a-z.]+/maps|^https?://maps\.google\.[a-z.]+/", re.I)
# the objects of a page's JSON-LD whose address is NOT the organisation's own
NOT_ORG = {"event", "person", "jobposting", "offer", "aggregateoffer", "product", "review", "course", "courseinstance", "musicevent", "sportsevent",
           "businessevent", "educationevent", "socialevent", "theaterevent", "festival", "exhibitionevent", "screeningevent", "foodevent", "creativework",
           "article", "blogposting", "newsarticle", "webpage", "website", "breadcrumblist", "residence", "apartment", "house", "singlefamilyresidence",
           "accommodation", "realestatelisting", "lodgingreservation", "reservation", "trip"}
PROV = {"ab", "bc", "mb", "nb", "nl", "ns", "nt", "nu", "on", "pe", "qc", "sk", "yt", "alberta", "british columbia", "colombie-britannique", "manitoba",
        "new brunswick", "nouveau-brunswick", "newfoundland and labrador", "terre-neuve-et-labrador", "nova scotia", "nouvelle-écosse", "northwest territories",
        "nunavut", "ontario", "prince edward island", "île-du-prince-édouard", "quebec", "québec", "saskatchewan", "yukon", "pq", "nfld", "pei"}


def _norm_space(s):
    return re.sub(r"\s+", " ", re.sub(r"[\u200b-\u200f\u2060\ufeff]", "", html.unescape(str(s or "")))).strip()


def _types(o):
    t = o.get("@type")
    if isinstance(t, str):
        return {t.lower()}
    if isinstance(t, list):
        return {str(x).lower() for x in t}
    return set()


def jsonld_address(raw, abroad=False):
    """(address text, quote) of the page's own organisation, or None; abroad=True: (address, quote, country) in a territory of rule 18"""
    for m in LD.finditer(raw[:3_000_000]):
        body = m.group(1).strip()
        body = re.sub(r"^\s*<!--|-->\s*$", "", body)
        try:
            data = json.loads(body)
        except ValueError:
            try:
                data = json.loads(re.sub(r"[\x00-\x1f]", " ", body))
            except ValueError:
                continue
        stack = [(data, set())]
        while stack:
            o, parent = stack.pop()
            if isinstance(o, list):
                stack.extend((x, parent) for x in o)
                continue
            if not isinstance(o, dict):
                continue
            ty = _types(o)
            for k_, v_ in o.items():
                if k_ in ("@graph", "mainEntity", "publisher", "provider", "author", "brand", "parentOrganization", "department", "subOrganization", "member", "itemListElement"):
                    stack.append((v_, ty if k_ in ("@graph", "mainEntity", "itemListElement") else ty | {"_nested_" + k_.lower()}))
            if ty & NOT_ORG or any(t_.startswith("_nested_author") for t_ in parent) or (not ty and parent & NOT_ORG):
                continue
            adr = o.get("address")
            if isinstance(adr, list):
                adr = next((a for a in adr if isinstance(a, dict)), None)
            if not isinstance(adr, dict):
                continue
            parts = [_norm_space(adr.get(k_)) for k_ in ("streetAddress", "addressLocality", "addressRegion", "postalCode")]
            ctry = adr.get("addressCountry")
            if isinstance(ctry, dict):
                ctry = ctry.get("name") or ctry.get("@id") or ""
            ctry = _norm_space(ctry)
            if abroad:
                cc_ = _ABROAD_CTRY.get(ctry.lower(), "" if ctry else "US")
                if not cc_:
                    continue
                txt = ", ".join(p for p in (parts[0], parts[1]) if p)
                tail = " ".join(p for p in (parts[2], parts[3]) if p)
                addr = (txt + (", " if txt and tail else "") + tail).strip(", ")
                probe = addr + ((", " + ctry) if ctry and cc_ != "US" else "")
                if not BL.abroad_where(probe)[0]:
                    continue
                quote = ", ".join("%s: %s" % (k_, v_) for k_, v_ in zip(("streetAddress", "addressLocality", "addressRegion", "postalCode"), parts) if v_)
                if ctry:
                    quote += ", addressCountry: %s" % ctry
                name = _norm_space(o.get("name"))[:80]
                return probe[:200], ("%s (schema.org PostalAddress%s in the page source)" % (quote, (" of “%s”" % name) if name else ""))[:300], cc_
            pcs = list(BL.codes(parts[3] or "")) if parts[3] else []
            in_ca = ctry.lower() in ("ca", "can", "canada") or bool(pcs) or (parts[2] or "").lower() in PROV
            if not in_ca or not (parts[3] or (parts[1] and parts[2])):
                continue
            if ctry and ctry.lower() not in ("ca", "can", "canada"):
                continue
            txt = ", ".join(p for p in (parts[0], parts[1]) if p)
            tail = " ".join(p for p in (parts[2], parts[3]) if p)
            addr = (txt + (", " if txt and tail else "") + tail).strip(", ")
            quote = ", ".join("%s: %s" % (k_, v_) for k_, v_ in zip(("streetAddress", "addressLocality", "addressRegion", "postalCode"), parts) if v_)
            if ctry:
                quote += ", addressCountry: %s" % ctry
            name = _norm_space(o.get("name"))[:80]
            return addr[:200], ("%s (schema.org PostalAddress%s in the page source)" % (quote, (" of “%s”" % name) if name else ""))[:300]
    return None


def map_address(raw, abroad=False):
    """(address text, quote) of the Google map the page embeds, or None — the address asked for, never the map's key; abroad=True:
    (address, quote, country) in a territory of rule 18"""
    for m in IFRAME.finditer(raw[:3_000_000]):
        src = html.unescape(m.group(1).strip())
        if src.startswith("//"):
            src = "https:" + src
        if not MAPHOST.search(src):
            continue
        u = urllib.parse.urlparse(src)
        q = urllib.parse.parse_qs(u.query)
        cands = q.get("q", []) + q.get("query", []) + q.get("daddr", [])
        for pb in q.get("pb", []):
            cands += [urllib.parse.unquote_plus(x) for x in re.findall(r"!2s([^!]+)", pb)]
        for c_ in cands:
            c_ = _norm_space(urllib.parse.unquote_plus(c_))
            if not c_ or len(c_) > 200 or re.fullmatch(r"[-\d.,\s]+", c_) or "0x" in c_[:4]:
                continue
            if abroad:
                b_ = BL.abroad_where(c_)[0]
                if b_:
                    return c_[:200], ("the map its own page embeds is of “%s” (Google Maps embed in the page source)" % c_)[:300], b_.get("country") or "US"
                continue
            if next(BL.codes(c_), None) or BL.CITY_RX.search(c_):
                return c_[:200], ("the map its own page embeds is of “%s” (Google Maps embed in the page source)" % c_)[:300]
    return None


# 2026-11-13 (AGENTS.md rule 18): an organisation abroad whose own address lies in the territory of a utility a Canadian company owns (Tampa Electric,
# Tucson Electric Power, Green Mountain Power … : tools/abroad_utilities.py, tools/data/us_zip_billers.csv) or on an island a Caribbean one serves
# whole. The same three statements of its own pages, read for a U.S. ZIP code after its state (or an island address), and kept only when
# tools/by_location.abroad_where names one such utility for it.
_ABROAD_CTRY = {"us": "US", "usa": "US", "u.s.": "US", "u.s.a.": "US", "united states": "US", "united states of america": "US",
                "ky": "KY", "cayman islands": "KY", "bb": "BB", "barbados": "BB", "bm": "BM", "bermuda": "BM"}


def abroad_text_address(raw):
    """(address, quote, country) of an address in a territory of rule 18 printed in the visible text, or None"""
    import lead_crawl as LC
    t = C.visible(raw)
    for cc, rx in (("US", LC.US_ADDR), ("KY", LC.KY_ADDR), ("BB", LC.BB_ADDR), ("BM", LC.BM_ADDR)):
        for m in rx.finditer(t):
            q = re.sub(r"^\S*\s", "", t[max(0, m.start() - 110):m.end()].strip())[-200:]
            if BL.abroad_where(q)[0]:
                return q, q[:300], cc
    return None


def abroad_jsonld_address(raw):
    """(address, quote, country) of the page's own organisation's schema.org PostalAddress in a territory of rule 18, or None"""
    return jsonld_address(raw, abroad=True)


def abroad_map_address(raw):
    """(address, quote, country) of the Google map the page embeds, in a territory of rule 18, or None"""
    return map_address(raw, abroad=True)


def text_address(raw):
    import cc_clients as CCL
    t = C.visible(raw)
    m = CCL.ADDR.search(t)
    if not m:
        return None
    q = re.sub(r"^\S*\s", "", t[max(0, m.start() - 110):m.end()].strip())[-200:]
    return (CCL.address_from(q) or q)[:200], q[:300]


def get(url):
    try:
        if not C.allowed(url):
            return None, url, "robots"
        st, ct, data, final = C.fetch(url)
        if st != 200 or not data:
            return None, final or url, "http_%s" % st
        if "html" not in (ct or "text/html").lower() and "xml" not in (ct or "").lower():
            return None, final or url, "not_html"
        return data.decode("utf-8", "replace"), final or url, "ok"
    except Exception as e:  # noqa: BLE001
        return None, url, "error:%s" % type(e).__name__


# 2026-11-13: the organisation's own telephone number, printed on its pages (a tel: link first, else the number its pages print most often) —
# tools/phone_places.py looks for the Overture Maps place that lists it when no address was found
PHONE = os.path.join(FACTS_DIR, "phones.tsv")
_PH = re.compile(r"(?<!\d)(?:\+?1[\s.\-]?)?\(?([2-9]\d{2})\)?[\s.\-]?([2-9]\d{2})[\s.\-]?(\d{4})(?!\d)")
_CA_AC = set("204 226 236 249 250 257 263 289 306 343 354 365 367 368 382 403 416 418 428 431 437 438 450 468 474 506 514 519 548 579 581 584 587 604 613 "
             "639 647 672 683 705 709 742 753 778 780 782 807 819 825 867 873 879 902 905".split())


def own_phone(pages):
    import collections as _c
    for u, r in pages:
        for m in re.finditer(r"""href\s*=\s*["']tel:([^"']{7,40})["']""", r[:3_000_000], re.I):
            d = re.sub(r"\D", "", m.group(1))[-10:]
            if len(d) == 10 and d[:3] in _CA_AC:
                return d, u
    cnt, where = _c.Counter(), {}
    for u, r in pages:
        for m in _PH.finditer(C.visible(r)):
            if m.group(1) in _CA_AC:
                d = m.group(1) + m.group(2) + m.group(3)
                cnt[d] += 1; where.setdefault(d, u)
    if cnt:
        d, _ = cnt.most_common(1)[0]
        return d, where[d]
    return "", ""


def read_one(t):
    key, site = t["key"], t["site"]
    raw, final, st = get(site)
    out = {"key": key, "site": site, "date": TODAY, "status": st}
    if raw is None:
        return out
    base = final if str(final).startswith("http") else site
    home_dom = C.registrable(urllib.parse.urlparse(base).hostname or "")
    pages = [(base, raw)]
    seen = {base.rstrip("/")}
    for u, lab in C.links(raw, base):
        if len(pages) >= 4:
            break
        p = urllib.parse.urlparse(u)
        if p.scheme not in ("http", "https") or C.registrable(p.hostname or "") != home_dom or u.rstrip("/") in seen:
            continue
        if not (CONTACT.search(p.path or "") or CONTACT.search(lab or "")) or re.search(r"\.(?:pdf|jpe?g|png|gif|zip|docx?)$", p.path or "", re.I):
            continue
        seen.add(u.rstrip("/"))
        r2, f2, s2 = get(u)
        if r2 is not None:
            pages.append((f2 if str(f2).startswith("http") else u, r2))
    try:
        ph, phu = own_phone(pages)
    except Exception:  # noqa: BLE001
        ph, phu = "", ""
    if ph:
        out.update(phone=ph, phone_url=phu)
    for how, fn in (("text", text_address), ("jsonld", jsonld_address), ("map", map_address)):
        for u, r in pages:
            try:
                got = fn(r)
            except Exception:  # noqa: BLE001
                got = None
            if got:
                addr, quote = got
                out.update(status="found", address=addr, address_quote=quote, address_url=u, address_how=how, address_country="CA")
                return out
    if BL.ABROAD:
        for how, fn in (("text", abroad_text_address), ("jsonld", abroad_jsonld_address), ("map", abroad_map_address)):
            for u, r in pages:
                try:
                    got = fn(r)
                except Exception:  # noqa: BLE001
                    got = None
                if got:
                    addr, quote, cc = got
                    out.update(status="found", address=addr, address_quote=quote, address_url=u, address_how=how, address_country=cc)
                    return out
    out["status"] = "nothing"
    out["pages"] = len(pages)
    return out


# 2026-11-13: the organisation's own privacy / terms / legal page. A Canadian privacy policy names where to write to the organisation ("please
# contact us at the mailing address listed below: ERTH360 125 Villarboit Crescent Vaughan, Ontario L4K 4K2"), a Québec site its "mentions légales".
# Measured on 160 organisations that every earlier pass left unlocated: 7 such pages print a postal code — 4 of them the organisation's own address,
# beside its own name; the others the host's (Shopify's Ottawa office), an affiliate's, or a clause. So the address is kept ONLY when the
# organisation's own name (its domain's name, or the name its home page gives itself) stands in the 170 characters before the postal code, and
# never when that stretch names a host, a registrar, an affiliate or parent, an agent, or a public body (the Privacy Commissioner's office, the
# Commission d'accès à l'information …); a federal government postal code (K1A) is never taken.
LEGALP = re.compile(r"privacy|confidentialit|terms|conditions|legal|mentions|politique|disclaimer|imprint|avis[-_ ]?juridique|\bcgu\b|\bcgv\b|termes", re.I)
THIRD = re.compile(r"(?i)\b(?:host(?:ed|ing|s)?|h[ée]berg\w*|shopify|wix|squarespace|godaddy|ovh|weebly|registrar|commissioner|commissaire|commission|ombudsman|"
                   r"affiliate[sd]?|affili[ée]e?s?|parent|agent|agence du revenu|government|gouvernement|ministry|minist[èe]re|office of the|bureau du|"
                   # (a returns or shipping address is often a warehouse that someone else runs: 2026-11-13, first run's sample)
                   r"returns?|retours?|ship(?:ped|ping)?|warehouse|entrep[ôo]t|fulfil+ment)\b")


def _nm(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


def names_of(site, raw):
    """the organisation's names as they can stand beside its address: its domain's name (5 characters or more) and the name its home page gives itself"""
    out = []
    dom = C.registrable(urllib.parse.urlparse(site).hostname or "")
    lab = _nm(dom.rsplit(".", 1)[0] if "." in dom else dom)
    if len(lab) >= 5:
        out.append(lab)
    try:
        import tech_relationships as T
        import lead_crawl as LC
        title, meta = T.page_meta(raw)
        sn = LC.site_name_for((urllib.parse.urlparse(site).hostname or "").lower(), meta.get("og:site_name"), title, T) or ""
    except Exception:  # noqa: BLE001
        sn = ""
    if len(_nm(sn)) >= 6 and _nm(sn) not in out:
        out.append(_nm(sn))
    return out


_TITLED = re.compile(r"\b(?:Me|Mr|Mrs|Ms|Mme|Mlle|Dr|Pr)\.?\s+[A-Z][a-zà-ÿ'’\-]+|\b(?:Attn|Attention|c/o|a/s)\b|\b(?:LL\.?B|B\.?C\.?L|Esq)\b")
_GIV = None


def _given():
    global _GIV
    if _GIV is None:
        try:
            from buyer_pages import FIRST_NAMES as _fn
            import relationship_rows as _rr
            _GIV = set(_fn) | set(getattr(_rr, "_MORE_GIVEN", set()))
        except Exception:  # noqa: BLE001
            _GIV = set()
    return _GIV


def _fold_index(w):
    """the letters and digits of w, folded to ASCII lower case, and the index in w of each"""
    import unicodedata
    out, idx = [], []
    for i, ch in enumerate(w):
        f = unicodedata.normalize("NFKD", ch).encode("ascii", "ignore").decode().lower()
        for c in f:
            if c.isalnum():
                out.append(c); idx.append(i)
    return "".join(out), idx


def legal_address(raw, names):
    """(address, quote) the page prints beside the organisation's own name, or None. The quote starts at that name (what stands before it —
    a privacy officer's name, a heading — is not quoted) and is not kept when it names a person (a title, "Attn", a given name and surname)"""
    import cc_clients as CCL
    if not names:
        return None
    t = C.visible(raw)
    for pc, m in BL.codes(t):
        if pc.startswith("K1A"):
            continue
        w = t[max(0, m.start() - 170):m.end()]
        if THIRD.search(w):
            continue
        fw, idx = _fold_index(w)
        best = -1
        for n in sorted(names, key=len, reverse=True):
            j = fw.rfind(n, 0, max(0, len(fw) - 6))  # before the postal code itself
            if j >= 0:
                best = max(best, idx[j])
        if best < 0:
            continue
        q = html.unescape(w[best:].strip())[-300:]
        if _TITLED.search(q):
            continue
        toks = re.findall(r"[A-Za-zÀ-ÿ'’\-]+", q)
        if any(toks[i].lower() in _given() and toks[i][:1].isupper() and toks[i + 1][:1].isupper() for i in range(1, len(toks) - 1)):
            continue  # a given name and a surname after the organisation's name: a person's
        return (CCL.address_from(q) or q[-200:])[:200], q


def read_one_legal(t):
    key, site = t["key"], t["site"]
    raw, final, st = get(site)
    out = {"key": key, "site": site, "date": TODAY, "status": st}
    if raw is None:
        return out
    base = final if str(final).startswith("http") else site
    home_dom = C.registrable(urllib.parse.urlparse(base).hostname or "")
    names = names_of(base, raw)
    seen, n_read = {base.rstrip("/")}, 0
    for u, lab in C.links(raw, base):
        if n_read >= 3:
            break
        p = urllib.parse.urlparse(u)
        if p.scheme not in ("http", "https") or C.registrable(p.hostname or "") != home_dom or u.rstrip("/") in seen:
            continue
        if not (LEGALP.search(p.path or "") or LEGALP.search(lab or "")) or re.search(r"\.(?:pdf|jpe?g|png|gif|zip|docx?)$", p.path or "", re.I):
            continue
        seen.add(u.rstrip("/"))
        r2, f2, s2 = get(u)
        n_read += 1
        if r2 is None:
            continue
        got = None
        try:
            got = legal_address(r2, names)
        except Exception:  # noqa: BLE001
            got = None
        if got:
            addr, quote = got
            out.update(status="found", address=addr, address_quote=quote, address_url=f2 if str(f2).startswith("http") else u, address_how="legal",
                       address_country="CA")
            return out
    out["status"] = "legal_nothing"
    out["pages"] = n_read
    return out


# 2026-11-13: a street address printed with its city and province but no postal code ("147 Wyndham Street North, Suite 302, Guelph, ON"), or the
# one city the organisation's own contact page names. Two samples of 148 organisations that every earlier pass (text, JSON-LD, map, legal pages)
# left unlocated, read again: 16 print a street address with its city and province and no postal code — 8 of them in a city every postal code of
# which lies in one distributor's territory; 10 name one such city on their contact page. The city names the distributor
# (tools/by_location.py biller_for_city: every postal code of the city in one territory; never a city split between two distributors, never
# Alberta, never two cities of two distributors on one page). The quote starts at the street number (what stands before it is not quoted) and is
# not kept when it names a person.
_PROV_W = (r"(?:ON|Ont\.?|Ontario|QC|Qc|Qu[ée]bec|BC|B\.C\.|British Columbia|Colombie-Britannique|MB|Manitoba|SK|Sask\.?|Saskatchewan|NS|N\.S\.|Nova Scotia|"
           r"Nouvelle-[ÉE]cosse|NB|N\.B\.|New Brunswick|Nouveau-Brunswick|NL|Newfoundland(?: and Labrador)?|PE|PEI|P\.E\.I\.|Prince Edward Island|YT|Yukon|NT|"
           r"Northwest Territories|NU|Nunavut)")
STREET_EN = re.compile(r"(?<![\w\-/()])(\d{1,6}[A-Za-z]?(?:-\d{1,6})?,?\s+(?:[A-ZÀ-Ý][\w'’.\-]*\s+|\d{1,3}(?:st|nd|rd|th)?\s+){0,5}?(?:Street|St\.?|Avenue|Ave\.?|"
                       r"Road|Rd\.?|Boulevard|Blvd\.?|Boul\.?|Drive|Dr\.?|Way|Lane|Ln\.?|Crescent|Cres\.?|Court|Ct\.?|Place|Pl\.?|Highway|Hwy\.?|Parkway|Pkwy\.?|Trail|Line|"
                       r"Sideroad|Concession|Circle|Square|Terrace|Gate|Row)\b(?:\s+(?:North|South|East|West|N|S|E|W|NE|NW|SE|SW)\.?)?"
                       r"(?:[,\s·\-–]+(?:Suite|Unit|Bureau|Ste\.?|Apt\.?|Local|Floor|Room|#)\s*[\w\-]{1,6})?[^<>|\d]{0,45}?\b" + _PROV_W + r"\)?(?:\s*[,(]\s*" + _PROV_W + r"\)?)?)(?![\w])", re.U)
STREET_FR = re.compile(r"(?<![\w\-/()])(\d{1,6}[A-Za-z]?,?\s+(?:rue|avenue|av\.|boulevard|boul\.?|chemin|ch\.|route|rang|place|mont[ée]e|c[ôo]te|promenade|all[ée]e)\s+"
                       r"[^<>|\d]{2,60}?(?:[,\s\-–]+(?:bureau|local|suite|app\.?|#)\s*[\w\-]{1,6})?[^<>|\d]{0,45}?\b" + _PROV_W + r"\)?(?:\s*[,(]\s*" + _PROV_W + r"\)?)?)(?![\w])", re.I | re.U)
_STREET_WORD = re.compile(r"\b(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Boul|Drive|Dr|Way|Lane|Ln|Crescent|Cres|Court|Ct|Place|Pl|Highway|Hwy|Parkway|Pkwy|"
                          r"Trail|Line|Sideroad|Concession|Circle|Square|Terrace|Gate|Row|rue|avenue|av|boulevard|chemin|ch|route|rang|place|mont[ée]e|c[ôo]te|"
                          r"promenade|all[ée]e)\b\.?", re.I)
# a city named as a service area, not as where the organisation is ("Serving Winnipeg, Manitoba", "partout à Laval, QC")
_SERVING = re.compile(r"(?i)\b(?:serv(?:ing|ice|ices|icing|ed)?|desserv\w*|across|throughout|surrounding|areas?|r[ée]gions?|partout|clients?|customers?|"
                      r"deliver\w*|livr\w*|near|pr[èe]s de|from|depuis|to)\W*$")
# a contact page, as its address or its menu label names it (not an "about" page, a client list or a portfolio)
CONTACT_STRICT = re.compile(r"contact|joindre|coordonn|nous-trouver|find-us|location|directions|visit|hours|heures|adresse|address", re.I)


def _person_in(q, street=False):
    """a title or "Attn" anywhere; a given name and a surname — in a street address only between the street and the city (a street named after
    a person, "990 Victoria Street", or a city, "Victoria, BC", is not a person)"""
    if _TITLED.search(q):
        return True
    if street:
        m = _STREET_WORD.search(q)
        cm = list(BL.CITY_RX.finditer(q))
        q = q[m.end() if m else 0:cm[-1].start() if cm else len(q)]
    toks = re.findall(r"[A-Za-zÀ-ÿ'’\-]+", q)
    return any(toks[i].lower() in _given() and toks[i][:1].isupper() and toks[i + 1][:1].isupper() for i in range(len(toks) - 1))


# a date and an event, not an address ("Aug 22 Capital Pride Street Festival Ottawa, Ontario")
_EVENT = re.compile(r"(?i)\b(?:festival|fair|foire|expo|market|march[ée]|show|concert|gala|parade|d[ée]fil[ée]|tournament|tournoi|conference|congr[èe]s|summit|"
                    r"workshop|atelier|event|[ée]v[ée]nement|party|soir[ée]e|race|course|walk|marche|run)\b")
_DATE_BEFORE = re.compile(r"(?i)\b(?:jan(?:uary|vier)?|feb(?:ruary)?|f[ée]v(?:rier)?|mar(?:ch|s)?|apr(?:il)?|avr(?:il)?|may|mai|june?|juin|july?|juil(?:let)?|aug(?:ust)?|ao[uû]t|"
                         r"sept?(?:ember|embre)?|oct(?:ober|obre)?|nov(?:ember|embre)?|dec(?:ember)?|d[ée]c(?:embre)?|mon(?:day)?|tue(?:sday)?|wed(?:nesday)?|thu(?:rsday)?|fri(?:day)?|sat(?:urday)?|sun(?:day)?|lundi|mardi|mercredi|jeudi|"
                         r"vendredi|samedi|dimanche)\.?,?\s*$")


def street_city(raw):
    """(address, quote) of a street address with its city and province, no postal code, in a city one distributor serves whole — or None.
    A page that prints more than two different street addresses (a listing, a list of branches) gives none."""
    t = re.sub(r"\s+", " ", C.visible(raw))
    got, seen = None, set()
    for rx in (STREET_EN, STREET_FR):
        for m in rx.finditer(t):
            q = html.unescape(m.group(1)).strip(" ,·|-–")
            num = re.match(r"[\d\-A-Za-z]+", q).group(0)
            seen.add((num, (_STREET_WORD.split(q, 1)[0].split()[1:2] or [""])[0].lower()))
            if (got or len(q) > 200 or re.fullmatch(r"\d{3}-\d{4}", num) or BL.fsa_of(q) or _person_in(q, street=True) or THIRD.search(q) or _EVENT.search(q)
                    or _DATE_BEFORE.search(t[max(0, m.start(1) - 16):m.start(1)])):
                continue
            if BL.biller_for_city(q):
                got = (q, q)
    return got if got and len(seen) <= 2 else None


def contact_city(raw):
    """("City, Province" as printed, the same words) when the page names cities of one distributor only, that distributor serves each city
    whole, and the city is not named as a service area"""
    t = re.sub(r"\s+", " ", C.visible(raw))
    if not BL.biller_for_city(t):
        return None
    for m in BL.CITY_RX.finditer(t):
        bc = BL.biller_for_city(m.group(0))
        if not bc:
            continue
        city = bc[1].rsplit(",", 1)[0].strip()  # the city's words as printed ("Markham" of "Cartagena Software Limited Markham, Ontario")
        j = m.group(0).rfind(city)
        if j < 0:
            continue
        if _SERVING.search(t[max(0, m.start() + j - 40):m.start() + j]):
            continue
        q = html.unescape(m.group(0)[j:]).strip(" ,(")
        if not _person_in(q):
            return q, q
    return None


def read_one_city(t):
    """the home page and up to three contact / about / location pages: a street address with its city (any of them), else the city a contact page
    names"""
    key, site = t["key"], t["site"]
    raw, final, st = get(site)
    out = {"key": key, "site": site, "date": TODAY, "status": st}
    if raw is None:
        return out
    base = final if str(final).startswith("http") else site
    home_dom = C.registrable(urllib.parse.urlparse(base).hostname or "")
    pages, contact = [(base, raw)], []
    seen = {base.rstrip("/")}
    for u, lab in C.links(raw, base):
        if len(pages) >= 4:
            break
        p = urllib.parse.urlparse(u)
        if p.scheme not in ("http", "https") or C.registrable(p.hostname or "") != home_dom or u.rstrip("/") in seen:
            continue
        if not (CONTACT.search(p.path or "") or CONTACT.search(lab or "")) or re.search(r"\.(?:pdf|jpe?g|png|gif|zip|docx?)$", p.path or "", re.I):
            continue
        seen.add(u.rstrip("/"))
        r2, f2, s2 = get(u)
        if r2 is not None:
            pages.append((f2 if str(f2).startswith("http") else u, r2))
            if CONTACT_STRICT.search(p.path or "") or CONTACT_STRICT.search(lab or ""):
                contact.append(pages[-1])
    for how, fn, which in (("street_city", street_city, pages), ("city_contact", contact_city, contact)):
        for u, r in which:
            try:
                got = fn(r)
            except Exception:  # noqa: BLE001
                got = None
            if got:
                addr, quote = got
                out.update(status="found", address=addr, address_quote=quote, address_url=u, address_how=how, address_country="CA")
                return out
    out["status"] = "city_nothing"
    out["pages"] = len(pages)
    return out


def pick_legal(a):
    """the sites every earlier pass read without finding an address: their own privacy / terms / legal pages (read_one_legal)"""
    last = {}
    if os.path.exists(DONE):
        with open(DONE, encoding="utf-8") as f:
            for l in f:
                p_ = l.rstrip("\n").split("\t")
                if len(p_) >= 2:
                    last[p_[0]] = p_[1]
    need = {k for k, st in last.items() if st == ("legal_nothing" if getattr(a, "city", False) else "nothing")}
    site = {}
    for p in sorted(glob.glob(os.path.join(FACTS_DIR, "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                if d.get("key") in need and d.get("site") and d["key"] not in site:
                    site[d["key"]] = d["site"]
    for p in sorted(glob.glob(os.path.join(INC, "claude_buyer_ap_results_cccrawl*.csv"))):
        with open(p, encoding="utf-8", errors="replace", newline="") as f:
            for r in csv.DictReader(f):
                k = r.get("buyer_key")
                if k in need and k not in site and r.get("status") == "found" and "@" in (r.get("ap_email") or ""):
                    site[k] = "https://%s/" % r["ap_email"].strip().lower().partition("@")[2]
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    n = 0
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["key", "site"])
        for k in sorted(need):
            if site.get(k):
                w.writerow([k, site[k]]); n += 1
    print("addr-reread pick --%s: %d sites read before with no address (of %d) -> %s" % ("city" if getattr(a, "city", False) else "legal", n, len(need), a.out))


def pick_phones(a):
    """the sites read before that gave no address, whose telephone number is not on file: read again for the number (and the address)"""
    have = set()
    if os.path.exists(PHONE):
        with open(PHONE, encoding="utf-8") as f:
            have = {l.split("\t", 1)[0] for l in f if l.strip()}
    last = {}
    if os.path.exists(DONE):
        with open(DONE, encoding="utf-8") as f:
            for l in f:
                p_ = l.rstrip("\n").split("\t")
                if len(p_) >= 2:
                    last[p_[0]] = p_[1]
    site = {}
    for p in sorted(glob.glob(os.path.join(FACTS_DIR, "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                if d.get("key") and d.get("site") and d["key"] not in site:
                    site[d["key"]] = d["site"]
    need = {k for k, st in last.items() if st == "nothing" and k not in have and not site.get(k)}
    if need:  # no site facts: the mailbox's own domain (the organisation's site, as cmd_pick took it)
        for p in sorted(glob.glob(os.path.join(INC, "claude_buyer_ap_results_cccrawl*.csv"))):
            with open(p, encoding="utf-8", errors="replace", newline="") as f:
                for r in csv.DictReader(f):
                    k = r.get("buyer_key")
                    if k in need and r.get("status") == "found" and "@" in (r.get("ap_email") or "") and k not in site:
                        site[k] = "https://%s/" % r["ap_email"].strip().lower().partition("@")[2]
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    n = 0
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["key", "site"])
        for k, st in sorted(last.items()):
            if st == "nothing" and k not in have and site.get(k):
                w.writerow([k, site[k]]); n += 1
    print("addr-reread pick --phones: %d sites read before with no address and no telephone number on file -> %s" % (n, a.out))


def cmd_pick(a):
    if getattr(a, "phones", False):
        return pick_phones(a)
    if getattr(a, "legal", False) or getattr(a, "city", False):
        return pick_legal(a)
    done = set()
    if os.path.exists(DONE):
        with open(DONE, encoding="utf-8") as f:
            done = {l.split("\t", 1)[0] for l in f if l.strip()}
    found = {}
    for p in sorted(glob.glob(os.path.join(INC, "claude_buyer_ap_results_cccrawl*.csv"))):
        with open(p, encoding="utf-8", errors="replace", newline="") as f:
            for r in csv.DictReader(f):
                if r.get("status") == "found" and r.get("ap_email") and "@" in r["ap_email"]:
                    found[r["buyer_key"]] = (r["ap_email"].strip().lower(), r.get("evidence_url") or "", r.get("evidence_quote") or "")
    facts = {}
    for p in sorted(glob.glob(os.path.join(FACTS_DIR, "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                k = d.get("key")
                if not k:
                    continue
                o = facts.setdefault(k, {})
                for c_ in ("site", "address", "address_quote", "address_country", "city_quote"):
                    if d.get(c_) and not o.get(c_):
                        o[c_] = d[c_]
    n = {"found": len(found), "located": 0, "city": 0, "abroad": 0, "done": 0, "webmail": 0, "picked": 0}
    # --abroad (2026-11-13, rule 18): only the organisations of the places abroad (tools/abroad_utilities.py leads, engine "usb") — read again even
    # when an earlier pass read them, since the abroad passes are new; left out when what is on file already names a utility of rule 18
    abroad_keys = None
    if getattr(a, "abroad", False):
        abroad_keys, gone = set(), set()
        for p in glob.glob(os.path.join(INC, "lead_shards", "leads_usb_*.gz")):
            with gzip.open(p, "rt", encoding="utf-8", errors="replace", newline="") as f:
                abroad_keys |= {r.get("buyer_key") for r in csv.DictReader(f) if r.get("buyer_key")}
        for p in glob.glob(os.path.join(INC, "lead_shards", "gone_usb_*.gz")):  # leads withdrawn since (a ZIP code area no longer its utility's)
            with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
                gone |= {l.rstrip("\n").split("\t")[-1] for l in f if l.startswith("L\t")}
        abroad_keys -= gone
        n["abroad_leads"] = len(abroad_keys)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["key", "site"])
        for k, (e, url, q) in sorted(found.items()):
            if abroad_keys is not None:
                if k not in abroad_keys:
                    continue
                fa = facts.get(k, {})
                _t = " ".join([fa.get("address") or "", fa.get("address_quote") or ""])
                if BL.abroad_where(_t)[0] or BL.abroad_point(C.registrable(urllib.parse.urlparse(fa.get("site") or "").hostname or ""), _t)[0]:
                    n["located"] += 1; continue
                site = fa.get("site") or ("https://%s/" % e.partition("@")[2])
                w.writerow([k, site]); n["picked"] += 1
                continue
            if k in done and not getattr(a, "include_done", False):  # (tools/phone_places.py: every organisation still unlocated, read again or not)
                n["done"] += 1; continue
            fa = facts.get(k, {})
            txt = " ".join([fa.get("address") or "", fa.get("address_quote") or "", q])
            if BL.fsa_of(txt):
                n["located"] += 1; continue
            if fa.get("address_country") and fa["address_country"] != "CA":
                n["abroad"] += 1; continue
            if BL.biller_for_city(" ".join([fa.get("address_quote") or "", fa.get("city_quote") or "", q])):
                n["city"] += 1; continue
            dom = e.partition("@")[2]
            site = fa.get("site") or ""
            if not site:
                if re.match(r"(?:gmail|hotmail|outlook|yahoo|live|icloud|me|msn|aol|videotron|sympatico|shaw|telus|rogers|bell|cogeco|eastlink|sasktel)\.", dom):
                    n["webmail"] += 1; continue
                site = "https://%s/" % dom
            w.writerow([k, site])
            n["picked"] += 1
    print("addr-reread pick: %s -> %s" % (n, a.out))


def cmd_read(a):
    k_, n_ = (int(x) for x in a.shard.split("/"))
    with open(a.targets, encoding="utf-8", newline="") as f:
        rows = [r for i, r in enumerate(csv.DictReader(f)) if i % n_ == k_]
    if a.limit:
        rows = rows[:a.limit]
    os.makedirs("out", exist_ok=True)
    path = "out/addr_reread_%d.jsonl" % k_
    deadline = time.time() + a.minutes * 60
    cnt = {}
    with open(path, "a", encoding="utf-8") as f, cf.ThreadPoolExecutor(a.workers) as ex:
        it = iter(rows)
        futs = set()
        def feed():
            while len(futs) < a.workers * 2 and time.time() < deadline:
                try:
                    futs.add(ex.submit(read_one_city if getattr(a, "city", False) else read_one_legal if getattr(a, "legal", False) else read_one, next(it)))
                except StopIteration:
                    return False
            return True
        more = feed()
        while futs:
            done, _ = cf.wait(futs, timeout=60, return_when=cf.FIRST_COMPLETED)
            for fu in done:
                futs.discard(fu)
                try:
                    o = fu.result()
                except Exception:  # noqa: BLE001
                    continue
                f.write(json.dumps(o, ensure_ascii=False) + "\n")
                st = o["status"] if o["status"] in ("found", "nothing", "robots") else o["status"].split(":")[0]
                cnt[st] = cnt.get(st, 0) + 1
                if o["status"] == "found":
                    cnt["by_" + o["address_how"]] = cnt.get("by_" + o["address_how"], 0) + 1
            f.flush()
            if more:
                more = feed()
            if time.time() > deadline + 300:
                break
    print("addr-reread shard %s: %d sites asked; %s" % (a.shard, sum(v for k2, v in cnt.items() if not k2.startswith("by_")), cnt))


def cmd_merge(a):
    recs = {}
    for p in sorted(glob.glob(os.path.join(a.dir, "**", "addr_reread_*.jsonl"), recursive=True)):
        with open(p, encoding="utf-8") as f:
            for l in f:
                try:
                    o = json.loads(l)
                except ValueError:
                    continue
                if o.get("key") and (o["key"] not in recs or o.get("status") == "found"):
                    recs[o["key"]] = o
    if not recs:
        print("addr-reread merge: nothing to merge"); return
    prev = {}
    need = {k for k, o in recs.items() if o.get("status") == "found"}
    for p in sorted(glob.glob(os.path.join(FACTS_DIR, "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                if d.get("key") in need:
                    o = prev.setdefault(d["key"], {})
                    for c_, v_ in d.items():
                        if v_ and not o.get(c_):
                            o[c_] = v_
    os.makedirs(FACTS_DIR, exist_ok=True)
    out = os.path.join(FACTS_DIR, "facts_%sa.gz" % a.stamp)
    n = {"found": 0, "text": 0, "jsonld": 0, "map": 0, "legal": 0, "street_city": 0, "city_contact": 0}
    with gzip.open(out, "wt", encoding="utf-8") as f:
        for k in sorted(need):
            o = recs[k]
            line = {c_: v_ for c_, v_ in (prev.get(k) or {}).items() if c_ in ("key", "site", "site_name", "title", "asked", "moved", "ids")}
            line.update(key=k, site=line.get("site") or o.get("site"), date=o.get("date") or TODAY, address_country=o.get("address_country") or "CA", address=o["address"],
                        address_quote=o["address_quote"], address_url=o["address_url"], address_how=o["address_how"])
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
            n["found"] += 1; n[o["address_how"]] = n.get(o["address_how"], 0) + 1
    with open(DONE, "a", encoding="utf-8") as f:
        for k, o in sorted(recs.items()):
            f.write("%s\t%s\t%s\n" % (k, o.get("status") or "", o.get("date") or TODAY))
    have_ph = set()
    if os.path.exists(PHONE):
        with open(PHONE, encoding="utf-8") as f:
            have_ph = {l.split("\t", 1)[0] for l in f if l.strip()}
    n_ph = 0
    with open(PHONE, "a", encoding="utf-8") as f:
        for k, o in sorted(recs.items()):
            if o.get("phone") and k not in have_ph:
                f.write("%s\t%s\t%s\t%s\n" % (k, o["phone"], o.get("phone_url") or "", o.get("date") or TODAY)); n_ph += 1
    print("addr-reread: %d telephone numbers of the organisations' own pages -> %s" % (n_ph, os.path.relpath(PHONE, ROOT)))
    tot = sum(1 for _ in open(DONE, encoding="utf-8"))
    print("addr-reread: %d sites read this run, %d addresses found (%s) -> %s; sites done so far: %d" % (len(recs), n["found"], n, os.path.relpath(out, ROOT), tot))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["pick", "read", "merge"])
    ap.add_argument("dir", nargs="?")
    ap.add_argument("--out", default=TARGETS)
    ap.add_argument("--targets", default=TARGETS)
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=150)
    ap.add_argument("--workers", type=int, default=40)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default=time.strftime("%Y%m%dT%H%M%S"))
    ap.add_argument("--phones", action="store_true", help="pick: the sites read before with no address and no telephone number on file")
    ap.add_argument("--legal", action="store_true", help="pick / read: the sites read before with no address — their own privacy / terms / legal pages")
    ap.add_argument("--city", action="store_true", help="pick / read: the sites the legal pass left — a street address with its city and no postal code, or the city of the contact page")
    ap.add_argument("--abroad", action="store_true", help="pick: only the organisations of the places abroad (rule 18), read again for an address in a utility's territory")
    a = ap.parse_args()
    {"pick": cmd_pick, "read": cmd_read, "merge": cmd_merge}[a.cmd](a)


if __name__ == "__main__":
    main()
