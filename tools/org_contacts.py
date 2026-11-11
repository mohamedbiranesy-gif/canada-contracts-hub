#!/usr/bin/env python3
"""Head-office address, phone and role mailboxes of an organisation from its OWN website, evidence or nothing.

Owner (2026-11-03): every entry of every package as complete as possible: the buyer's and the vendor's address, phone,
head office. This reads each organisation's home page and up to three contact-like pages (robots.txt, 1 request /
second / host, identified UA) and keeps, with the page URL, the date and a quote:
  - the postal address: schema.org JSON-LD / microdata PostalAddress first, then an <address> element, then a street
    address pattern (Canada: province + postal code; US: state + ZIP; UK postcode; Australia: state + postcode);
  - the phone: a tel: link, else a number next to "Tel" / "Phone" / "Téléphone" (never a fax);
  - role mailboxes on the organisation's own domain (info@, contact@, sales@, ventes@ ...; never a named person).
Input CSV: key,name,website,kind (kind = buyer | vendor). Output: one JSON line per registrable domain in
~/cch-crawler-state/org_contacts.jsonl (resume file, failures included) and, every 5 minutes, the found ones in
<crawler clone>/data/incoming/claude/claude_org_contacts.jsonl.gz, which contrib/claude/rank_buyers/rank.py reads.
  python3 tools/org_contacts.py --tasks tasks.csv [--workers 48] [--repo ~/cch-crawler]
"""
import argparse, csv, gzip, html, json, os, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C

STATE = os.path.expanduser("~/cch-crawler-state")
RESUME = os.path.join(STATE, "org_contacts.jsonl")
TODAY = time.strftime("%Y-%m-%d")
CONTACT_LINK = re.compile(r"contact|nous-joindre|joindre|coordonn|location|our-offices?|offices?$|about-?us|a-propos|find-us|"
                          r"visit|head-?office|siege|where-we-are|get-in-touch|reach-us|adresse|address", re.I)
CONTACT_LABEL = re.compile(r"^(contact(ez)?(-| )?(us|nous)?|nous joindre|pour nous joindre|coordonn[ée]es|locations?|our offices?|"
                           r"head office|si[èe]ge social|find us|visit us|get in touch|about( us)?|[àa] propos)$", re.I)
PROV = r"(?:ON|Ont\.?|Ontario|QC|Qu[ée]bec|AB|Alberta|BC|B\.C\.|British Columbia|MB|Manitoba|SK|Saskatchewan|NS|Nova Scotia|NB|" \
       r"New Brunswick|NL|Newfoundland(?: and Labrador)?|PE|PEI|Prince Edward Island|YT|Yukon|NT|NU)"
POSTAL = r"[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z] ?\d[ABCEGHJ-NPRSTV-Z]\d"
US_ST = r"(?:AL|AK|AZ|AR|CA|CO|CT|DE|DC|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|" \
        r"SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY)"
AU_ST = r"(?:NSW|VIC|QLD|SA|WA|TAS|NT|ACT)"
# Addresses are found from their rare tail (postal code / ZIP / postcode) backwards: a street-first pattern backtracks for
# minutes on digit-dense pages (schedules, financial tables).
TAILS = [("CA", re.compile(r"[,\s(]" + PROV + r"\)?\.?[,\s)]+(?:Canada[,\s]+)?" + POSTAL + r"(?![A-Za-z0-9])")),
         ("US", re.compile(r",?\s" + US_ST + r"\.?,?\s+\d{5}(?:-\d{4})?(?!\d)")),
         ("GB", re.compile(r"[,\s][A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}(?![A-Za-z0-9])")),
         ("AU", re.compile(r"[,\s]" + AU_ST + r"[,\s]+\d{4}(?!\d)"))]
STREET_START = re.compile(r"(?<![\d\-(.#/:])\d{1,6}[A-Za-z]?(?:-\d{1,6})?[ ,](?=[^\n|•]{2,})|G?P\.?O\.? Box \d|C\.? ?P\.? ?\d|(?:[A-Z][A-Za-z'.-]+ ){1,4}"
                          r"(?:Hall|House|Street|Road|Lane|Way|Square|Place|Court|Centre|Building|Park|Avenue|Gardens)\b")
NOT_START = re.compile(r"\d{3}[-.]\d{4}|\d{1,2}\s\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}|\d{3}[-.\s]\d{3}[-.\s]\d{4}|\d{1,2}:\d{2}|\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}|"
                       r"\d{4}-\d{2}-\d{2}|\d+(?:\.\d+)?\s?%")
BOX_START = re.compile(r"\d|G?P\.?O\.? Box|C\.? ?P\.? ?\d")  # a phone, a time, a date, a rate
NOT_ADDR = re.compile(r"copyright|©|all rights|tous droits|privacy|cookie", re.I)
TEL_LABEL = re.compile(r"(?:\bT[ée]l(?:[ée]phone)?\b|\bPhone\b|\bTel\b|\bT\s?:|\bCall(?: us)?\b|\bToll[- ]free\b|\bSans frais\b)[\s.:]*"
                       r"(\+?\d[\d\s().-]{8,20}\d)", re.I)
FAX = re.compile(r"\b(fax|t[ée]l[ée]c(opieur)?)\b", re.I)
ROLE = re.compile(r"^(?:info|infos|information|contact|contactus|contact-us|contactez|hello|hi|bonjour|sales|vente|ventes|enquiries|enquiry|"
                  r"inquiries|inquiry|office|admin|administration|reception|accueil|general|support|service|services|help|customerservice|"
                  r"customer|clients?|clientele|communications?|orders?|commandes?|accounts?|accounting|comptabilite|billing|facturation|"
                  r"factures?|invoices?|invoicing|ar|ap|team|mail|courrier|secretariat|direction|bureau|siege|headoffice|head\.office|"
                  r"corporate|quotes?|estimates?|estimating|soumissions?|rfq|bids?|tenders?|procurement|achats?|purchasing|export|"
                  r"international|canada|usa)(?=$|[^a-z])", re.I)
NOT_ROLE = re.compile(r"noreply|no-reply|donotreply|unsubscribe|abuse|postmaster|webmaster|privacy|dpo|security|career|jobs?|hr$|"
                      r"recruit|emploi|media|press|investor|^ir@|sentry|example|domain|email@|yourname|name@", re.I)
lock = threading.Lock()
STAGE = {}  # thread -> (domain, stage, since): a watchdog thread logs workers stuck for over a minute


def stage(dom, what):
    STAGE[threading.get_ident()] = (dom, what, time.time())


def watchdog():
    while True:
        time.sleep(60)
        now = time.time()
        stuck = sorted(((now - t, d, w) for d, w, t in list(STAGE.values()) if now - t > 60), reverse=True)[:8]
        if stuck:
            print(time.strftime("%H:%M"), "watchdog: %d workers over a minute on one step:" % len(stuck),
                  "; ".join("%s %s %ds" % (d, w, a) for a, d, w in stuck), flush=True)


LONG_TOKEN = re.compile(r"data:[a-z/+.-]+;base64,[A-Za-z0-9+/=]+|[A-Za-z0-9+/=_%-]{120,}")


def strip_long(raw):
    """inline base64 images and other very long tokens make the e-mail regex quadratic (and hold the GIL for minutes)"""
    return LONG_TOKEN.sub(" ", raw[:1_500_000])


def visible_keep_lines(raw):
    """visible text with line breaks kept at block boundaries (addresses are written over several lines)"""
    raw = raw[:1_500_000]
    t = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", raw)
    t = re.sub(r"(?i)<br\s*/?>|</(p|div|li|tr|td|th|h\d|address|span)>", "\n", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\r\f\v ]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t)


def flat(s):
    return re.sub(r",(\s*,)+", ",", re.sub(r"\s+", " ", s or "")).strip(" ,;|•-")


def quote_at(text, needle, n=300):
    i = text.find(needle) if needle else -1
    if i < 0:
        return flat(needle)[:n]
    a, b = max(0, i - 80), min(len(text), i + len(needle) + 80)
    return flat(text[a:b])[:n]


def walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from walk(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v)


def jsonld(raw):
    """(address string, country, telephone, email) from schema.org JSON-LD; the first PostalAddress of the page"""
    for m in re.finditer(r"(?is)<script[^>]+application/ld\+json[^>]*>(.*?)</script>", raw):
        try:
            data = json.loads(m.group(1).strip())
        except Exception:
            continue
        tel = mail = ""
        for o in walk(data):
            if not tel and isinstance(o.get("telephone"), str):
                tel = o["telephone"]
            if not mail and isinstance(o.get("email"), str):
                mail = o["email"].replace("mailto:", "")
        for o in walk(data):
            a = o.get("address")
            cands = a if isinstance(a, list) else [a]
            for a in cands:
                if isinstance(a, dict):
                    parts = [a.get("streetAddress"), a.get("addressLocality"), a.get("addressRegion"), a.get("postalCode")]
                    parts = [flat(p if isinstance(p, str) else " ".join(p) if isinstance(p, list) else "") for p in parts]
                    if parts[0] and (parts[1] or parts[3]):
                        country = a.get("addressCountry")
                        country = country.get("name", "") if isinstance(country, dict) else (country or "")
                        return ", ".join(p for p in parts if p), flat(str(country))[:40], flat(tel), flat(mail)
                elif isinstance(a, str) and re.search(r"\d", a) and 10 < len(a) < 200:
                    return flat(a), "", flat(tel), flat(mail)
    return "", "", "", ""


def microdata(raw):
    def prop(p):
        m = re.search(r"(?is)itemprop\s*=\s*[\"']%s[\"'][^>]*>(.*?)</" % p, raw)
        return flat(html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))) if m else ""
    s, l, r, p = prop("streetAddress"), prop("addressLocality"), prop("addressRegion"), prop("postalCode")
    return ", ".join(x for x in (s, l, " ".join(y for y in (r, p) if y)) if x) if s and (l or p) else ""


def address_tag(raw):
    for m in re.finditer(r"(?is)<address[^>]*>(.*?)</address>", raw):
        t = flat(visible_keep_lines(m.group(1)).replace("\n", ", "))
        t = re.sub(r"(?i)(t[ée]l[ée]phone|t[ée]l[ée]c\w*|phone|tel|fax|courriel|email|e-mail)\s*\.?:?[,\s]*(\+?[\d][\d\s().-]{7,})?", " ", t)
        t = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+", " ", t)
        t = re.sub(r"(?i)^(municipalit[ée] de|ville de|town of|city of|village de)\s*,\s*", "", flat(re.sub(r"\s*,\s*,+", ", ", t)))
        t = flat(t)
        if re.search(r"\d", t) and 12 < len(t) < 220 and not NOT_ADDR.search(t) and len(t.split()) >= 3:
            return t
    return ""


def country_of(addr):
    for cc, rx in TAILS:
        if rx.search(addr):
            return cc
    return ""


HQ_WORDS = re.compile(r"head ?office|headquarters|si[èe]ge social|city hall|h[ôo]tel de ville|town hall|main office|corporate office|"
                      r"mailing address|adresse postale|administration|civic centre|municipal office|county office|main campus", re.I)


def pattern_address(text):
    """the first street address on the page, unless a later one is labelled as the head office / city hall: the address's
    rare tail (province + postal code, state + ZIP, UK postcode, state + postcode) is found first, then the leftmost street
    start within 110 characters / 2 lines before it that is not a phone, time, date or rate"""
    best = None
    text = text[:400_000]
    for cc, rx in TAILS:
        for m in rx.finditer(text):
            w0 = max(0, m.start() - 110)
            win = text[w0:m.start()]
            cut = max(win.rfind("|"), win.rfind("•"), win.rfind(" · "))
            if cut >= 0:
                win = win[cut + 1:]; w0 += cut + 1
            start = None
            for x in STREET_START.finditer(win):
                if win.count("\n", x.start()) > 2 or NOT_START.match(win[x.start():]):
                    continue
                if BOX_START.match(x.group(0)):
                    start = x.start(); break
                if start is None:
                    start = x.start()
            if start is None:
                continue
            a = flat(text[w0 + start:m.end()].replace("\n", ", "))
            if NOT_ADDR.search(a) or not (10 <= len(a) < 200):
                continue
            hq = bool(HQ_WORDS.search(text[max(0, w0 + start - 140):w0 + start]))
            score = (2 if hq else 0, -m.start())
            if best is None or score > best[0]:
                best = (score, a, cc)
    return (best[1], best[2]) if best else ("", "")


def phones(raw, text):
    out = []
    for m in re.finditer(r"(?i)href\s*=\s*[\"']tel:([^\"']{7,30})[\"'][^>]*>(.*?)</a>", raw):
        num = html.unescape(urllib.parse.unquote(m.group(1))).strip()
        label = flat(html.unescape(re.sub(r"<[^>]+>", " ", m.group(2))))
        shown = label if re.search(r"\d{3}", label) else num
        if re.search(r"\d{7}", re.sub(r"\D", "", shown)) and shown not in out:
            ctx = text[max(0, text.find(shown) - 40):text.find(shown)] if shown in text else ""
            if not FAX.search(ctx):
                out.append(flat(shown)[:40])
    if not out:
        for m in TEL_LABEL.finditer(text):
            s = flat(m.group(1))
            if len(re.sub(r"\D", "", s)) >= 10 and not FAX.search(text[max(0, m.start() - 30):m.start()]) and s not in out:
                out.append(s[:40])
    return out[:2]


def role_emails(raw, text, site, name):
    out = []
    vis = C.page_emails(text)
    for e in sorted(C.page_emails(raw) | vis):
        local = e.split("@")[0]
        if e.split(".")[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp", "js", "css"):
            continue
        if not ROLE.match(local) or NOT_ROLE.search(e) or not C.same_org(e, site, name):
            continue
        if re.fullmatch(r"[a-z]+[._-][a-z]+", local) and not ROLE.match(local.split(".")[-1]) and local.split(".")[0] not in ("info", "contact", "sales", "ventes", "service", "support"):
            continue  # first.last
        if e not in out:
            out.append(e)
    return out[:4]


def contact_links(raw, base, host, name=""):
    seen, out = set(), []
    for u, label in C.links(raw, base):
        u = html.unescape(u)
        p = urllib.parse.urlparse(u)
        lh = (p.hostname or "").lower().removeprefix("www.")
        if not lh or C.SKIP_EXT.search(p.path or "") or (lh != host and not (C.registrable(lh) == C.registrable(host) or C.same_org("x@" + lh, "https://%s/" % host, name))):
            continue
        if CONTACT_LINK.search((p.path or "") + "?" + (p.query or "")) or CONTACT_LABEL.match(label or "") or \
                (len(label or "") <= 60 and re.search(r"contact|nous joindre|joindre|coordonn", label or "", re.I)):
            key = u.split("#")[0].rstrip("/")
            if key not in seen:
                seen.add(key); out.append(key)
    out.sort(key=lambda u: (not re.search(r"contact|joindre|coordonn", u, re.I), len(u)))
    return out[:3]


def read_site(site, name, start_url=""):
    site = site if site.startswith("http") else "https://" + site
    res = {"status": "no_contact", "pages": 0}
    dom = urllib.parse.urlparse(site).hostname or site
    stage(dom, "robots")
    if not C.allowed(start_url or site):
        res["status"] = "robots"; return res
    stage(dom, "fetch home")
    st, ct, data, final = C.fetch(start_url or site, 4_000_000)  # shared hosts (canada.ca …): the organisation's own page, not the host root
    if st in (401, 403, 429):
        res["status"] = "blocked"; res["http"] = st; return res
    if st != 200 or not data:
        res["status"] = "http_%s" % st; return res
    if data[:5] == b"%PDF-" or "html" not in (ct or "").lower():
        res["status"] = "not_html"; return res
    raw0 = strip_long(data.decode("utf-8", "replace"))
    m = re.search(r"(?is)<meta[^>]+http-equiv\s*=\s*[\"']?refresh[^>]+url\s*=\s*[\"']?([^\"'>\s]+)", raw0[:3000]) or \
        re.search(r"(?is)(?:window\.location|location\.href)\s*=\s*[\"']([^\"']+)", raw0[:3000]) if len(raw0) < 3000 else None
    if m:  # a redirect page: follow once
        st, ct, data, final = C.fetch(urllib.parse.urljoin(final, html.unescape(m.group(1))), 4_000_000)
        if st != 200 or not data or "html" not in (ct or "").lower():
            res["status"] = "http_%s" % st; return res
        raw0 = strip_long(data.decode("utf-8", "replace"))
    host = (urllib.parse.urlparse(final).hostname or "").lower().removeprefix("www.")
    # 2026-11-11: a block page is a SHORT page. The words were looked for in the first 5,000 characters of any page: every Wix site carries
    # "captcha" in the settings at the top of its page, and any site that loads reCAPTCHA early — 40 of 60 sites this reader had never
    # managed to read were ordinary pages called "blocked" (about 24,000 delivered rows without their own address and telephone).
    if (len(raw0) < 30000 and C.BLOCK_RX.search(raw0[:5000])) or (len(raw0) < 2500 and re.search(r"_Incapsula_Resource|incapsula|imperva|distil_r|perimeterx|datadome|akamai|bot ?detect", raw0, re.I)):
        res["status"] = "blocked"; return res
    pages = [(final, raw0)]
    stage(dom, "links")
    for u in contact_links(raw0, final, host, name):
        if not C.allowed(u):
            continue
        stage(dom, "fetch " + u[:60])
        st, ct, data, fin = C.fetch(u, 4_000_000)
        if st == 200 and data and "html" in (ct or "").lower():
            pages.append((fin, strip_long(data.decode("utf-8", "replace"))))
    res["pages"] = len(pages)
    order = pages[1:] + pages[:1]  # contact pages first: home-page footers often list several offices
    for url, raw in order:
        stage(dom, "visible %d" % len(raw))
        text = visible_keep_lines(raw)
        if not res.get("address"):
            stage(dom, "address %d" % len(text))
            a, cc, tel, mail = jsonld(raw)
            method = "json-ld"
            if not a:
                a, method = microdata(raw), "microdata"
            if not a:
                a, method = address_tag(raw), "address-tag"
            if not a:
                (a, cc), method = pattern_address(text), "pattern"
            if a:
                flat_text = re.sub(r"\s+", " ", text)
                needle = next((n for n in (re.search(POSTAL, a) and re.search(POSTAL, a).group(0), a.split(",")[0]) if n and n in flat_text), "")
                res.update({"address": a[:200], "address_country": cc or country_of(a), "address_url": url, "address_method": method,
                            "address_quote": quote_at(flat_text, needle) if needle else ("JSON-LD PostalAddress on the page: " + a)[:300]})
                if tel and not res.get("phone"):
                    res.update({"phone": tel[:40], "phone_url": url})
        if not res.get("phone"):
            stage(dom, "phones")
            ph = phones(raw, text)
            if ph:
                res.update({"phone": ph[0], "phone_url": url})
        if not res.get("emails"):
            stage(dom, "emails")
            em = role_emails(raw, text, "https://%s/" % host, name)
            if em:
                res.update({"emails": "; ".join(em), "emails_url": url})
        if res.get("address") and res.get("phone") and res.get("emails"):
            break
    res["status"] = "ok" if (res.get("address") or res.get("phone") or res.get("emails")) else "no_contact"
    return res


RETRY_STATUS = ("http_308", "http_307", "http_301", "http_302", "http_0", "error")
SHARED_HOSTS = re.compile(r"(?:^|\.)(canada\.ca|gc\.ca|gov\.bc\.ca|ontario\.ca|gouv\.qc\.ca|quebec\.ca|alberta\.ca|gov\.ab\.ca|novascotia\.ca|gnb\.ca|gov\.mb\.ca|"
                          r"saskatchewan\.ca|gov\.sk\.ca|gov\.nl\.ca|gov\.pe\.ca|yukon\.ca|gov\.nt\.ca|gov\.nu\.ca|gov\.au|gov\.uk|nhs\.uk|[a-z]{2}\.gov|[a-z]{2}\.us|wordpress\.com|wixsite\.com|squarespace\.com|weebly\.com|godaddysites\.com|google\.com|sites\.google\.com)$", re.I)


def task_key(h, w):
    """the site's host (www. dropped), or domain + path on shared hosts (canada.ca/en/environment-climate-change → one record per organisation).
    Until 2026-11-10 the key was the registrable domain, so one record served every host of a domain: the record read on tdi.texas.gov was
    handed to five other Texas agencies, one municipality's to the sixteen others on ao.ca, one church's to another on churchcenter.com. Each
    host is read for itself now; a record made before that day stays the record of the host it was read on (done_for)."""
    dom = C.registrable(h)
    if SHARED_HOSTS.search(h) or SHARED_HOSTS.search(dom):
        p = urllib.parse.urlparse(w if "//" in w else "https://" + w).path.rstrip("/")
        seg = "/".join(p.split("/")[:3]) if p else ""
        return (dom + seg) if seg else (h if h != dom else dom), h + seg
    return h, ""


def _host_of_site(w):
    w = w or ""
    return (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower().removeprefix("www.")


def done_for(done, key, h):
    """the record of this site, if this very host was read: under its own key, or — read before 2026-11-10 — under its registrable domain.
    A record kept under the host's name but read on another host of the domain (the domain's record, read on bookstore.upei.ca, is not
    upei.ca's) does not count: the host is read for itself and its record takes the key."""
    old = done.get(key)
    if key == h:
        if old is not None and _host_of_site(old.get("website")) not in ("", h):
            old = None
        if old is None:
            o2 = done.get(C.registrable(h))
            if o2 is not None and _host_of_site(o2.get("website")) == h:
                return o2
    return old


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--tasks", required=True)
    a.add_argument("--workers", type=int, default=48)
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--refresh", action="store_true", help="re-read domains that failed on a redirect / network error, and shared-host organisations keyed by path")
    a.add_argument("--shard", default="", help="K/N: only domains that hash to shard K of N (parallel runners never share a host)")
    a.add_argument("--seed-resume", default="", help="a jsonl(.gz) of organisations already read (the repo copy): skipped as if in the resume file")
    a.add_argument("--minutes", type=float, default=0, help="time box: at its end no new site is started, the state file is written once more and the reader leaves (0 = none)")
    a.add_argument("--out", default="", help="write the state file here, not to <repo>/data/incoming/claude/claude_org_contacts.jsonl.gz (several readers on one runner, each with a file and a resume file of its own)")
    a.add_argument("--delta", action="store_true", help="write only the records this run made or changed (the merge joins them with the file on main)")
    a.add_argument("--tried", default="", help="folder of org_tried_*.gz shards: the sites this reader could not read before are not asked again until their wait is over (run_box.Tried)")
    a.add_argument("--tried-out", default="", help="this run's failed tries go here (the workflow adds them to the folder)")
    a = a.parse_args()
    os.makedirs(STATE, exist_ok=True)
    resume = (a.out + ".resume.jsonl") if a.out else RESUME
    done = {}
    if os.path.exists(resume):
        for l in open(resume, encoding="utf-8"):
            try:
                d = json.loads(l); done[d["domain"]] = d
            except Exception:
                pass
    if a.seed_resume and os.path.exists(a.seed_resume):
        import hashlib  # noqa: F811
        with (gzip.open if a.seed_resume.endswith(".gz") else open)(a.seed_resume, "rt", encoding="utf-8") as fh:
            for l in fh:
                try:
                    d = json.loads(l)
                    if d.get("domain") and d["domain"] not in done:
                        done[d["domain"]] = d
                except Exception:
                    pass
    import hashlib
    shard_k, shard_n = (int(a.shard.split("/")[0]), int(a.shard.split("/")[1])) if a.shard else (0, 1)
    tasks, seen = [], set()
    import run_box
    tried, waiting = run_box.Tried("contacts", a.tried), 0
    for r in csv.DictReader(open(a.tasks, encoding="utf-8", errors="replace")):
        w = (r.get("website") or "").strip()
        h = (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower().removeprefix("www.")
        if not h or "." not in h:
            continue
        dom, start_path = task_key(h, w)
        if dom in seen:
            continue
        old = done_for(done, dom, h)
        if old is not None and not (a.refresh and (old.get("status") in RETRY_STATUS or old.get("status") == "no_contact" and start_path)):
            continue
        if old is None and tried.wait(dom):
            waiting += 1
            continue
        if shard_n > 1 and int(hashlib.md5((C.registrable(h) or h).encode()).hexdigest(), 16) % shard_n != shard_k:  # every host of a domain on one runner
            continue
        seen.add(dom); tasks.append((dom, r.get("key", ""), r.get("name", ""), "https://%s/" % h, r.get("kind", ""), ("https://%s/" % start_path) if start_path else ""))
    if a.limit:
        tasks = tasks[:a.limit]
    print("tasks: %d domains to read (%d in resume file; refresh=%s); %d that could not be read before wait for their turn" % (len(tasks), len(done), a.refresh, waiting), flush=True)
    out_gz = a.out or os.path.join(a.repo, "data/incoming/claude/claude_org_contacts.jsonl.gz")
    touched = set()
    stats = {}

    def rows():
        with lock:
            r = [d for d in ([done[k] for k in touched if k in done] if a.delta else done.values()) if d.get("status") == "ok"]
        return sorted(r, key=lambda d: d["domain"])

    import run_box
    state = run_box.StateFile(out_gz, rows)   # one write at a time, a path of its own each (run_box.py says what the five-minute writes did)
    box = run_box.Box(a.minutes)

    def one(t):
        dom, key, name, site, kind, start = t
        try:
            res = read_site(site, name, start_url=start)
        except Exception as e:
            res = {"status": "error", "error": str(e)[:100]}
        res.update({"domain": dom, "key": key, "name": name, "website": start or site, "kind": kind, "date": TODAY})
        with lock:
            old = done.get(dom)
            if old and _host_of_site(old.get("website")) not in ("", _host_of_site(res.get("website"))):
                old = None  # the record under this key was read on another host of the domain: this host's own record replaces it, facts are not mixed
            if old and old.get("status") == "ok" and res.get("status") != "ok":
                res = dict(old, last_recheck=TODAY, last_recheck_status=res.get("status"))
            if res.get("status") != "ok":
                # no record comes of this try: remembered, so that the next runs do not ask at once ("blocked_429" is a rate limit, asked again sooner than a refusal)
                tried.note(dom, "%s%s" % (res.get("status"), ("_%s" % res["http"]) if res.get("status") == "blocked" and res.get("http") else ""))
            done[dom] = res
            touched.add(dom)
            stats[res["status"]] = stats.get(res["status"], 0) + 1
            with open(resume, "a", encoding="utf-8") as f:
                f.write(json.dumps(res, ensure_ascii=False) + "\n")
        state.maybe(str(dict(stats)))

    threading.Thread(target=watchdog, daemon=True).start()
    whole = box.run(one, tasks, a.workers)
    state.final(str(dict(stats)))
    tried.save(a.tried_out)
    if whole:
        print("finished", dict(stats), flush=True)
    else:
        print("stopped by the time box: %d of %d sites read" % (sum(stats.values()), len(tasks)), dict(stats), flush=True)
        box.leave(0)


if __name__ == "__main__":
    main()
