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
NOT_START = re.compile(r"\d{3}[-.]\d{4}|\d{1,2}:\d{2}|\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}|\d{4}-\d{2}-\d{2}|\d+(?:\.\d+)?\s?%")
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
    vis = {x.lower().rstrip(".") for x in C.EMAIL_RX.findall(text)}
    for e in sorted({x.lower().rstrip(".") for x in C.EMAIL_RX.findall(raw)} | vis):
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


def read_site(site, name):
    site = site if site.startswith("http") else "https://" + site
    res = {"status": "no_contact", "pages": 0}
    dom = urllib.parse.urlparse(site).hostname or site
    stage(dom, "robots")
    if not C.allowed(site):
        res["status"] = "robots"; return res
    stage(dom, "fetch home")
    st, ct, data, final = C.fetch(site, 4_000_000)
    if st in (401, 403, 429):
        res["status"] = "blocked"; return res
    if st != 200 or not data:
        res["status"] = "http_%s" % st; return res
    if data[:5] == b"%PDF-" or "html" not in (ct or "").lower():
        res["status"] = "not_html"; return res
    raw0 = data.decode("utf-8", "replace")
    m = re.search(r"(?is)<meta[^>]+http-equiv\s*=\s*[\"']?refresh[^>]+url\s*=\s*[\"']?([^\"'>\s]+)", raw0[:3000]) or \
        re.search(r"(?is)(?:window\.location|location\.href)\s*=\s*[\"']([^\"']+)", raw0[:3000]) if len(raw0) < 3000 else None
    if m:  # a redirect page: follow once
        st, ct, data, final = C.fetch(urllib.parse.urljoin(final, html.unescape(m.group(1))), 4_000_000)
        if st != 200 or not data or "html" not in (ct or "").lower():
            res["status"] = "http_%s" % st; return res
        raw0 = data.decode("utf-8", "replace")
    host = (urllib.parse.urlparse(final).hostname or "").lower().removeprefix("www.")
    if C.BLOCK_RX.search(raw0[:5000]) or (len(raw0) < 2500 and re.search(r"_Incapsula_Resource|incapsula|imperva|distil_r|perimeterx|datadome|akamai|bot ?detect", raw0, re.I)):
        res["status"] = "blocked"; return res
    pages = [(final, raw0)]
    stage(dom, "links")
    for u in contact_links(raw0, final, host, name):
        if not C.allowed(u):
            continue
        stage(dom, "fetch " + u[:60])
        st, ct, data, fin = C.fetch(u, 4_000_000)
        if st == 200 and data and "html" in (ct or "").lower():
            pages.append((fin, data.decode("utf-8", "replace")))
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


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--tasks", required=True)
    a.add_argument("--workers", type=int, default=48)
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--limit", type=int, default=0)
    a = a.parse_args()
    os.makedirs(STATE, exist_ok=True)
    done = {}
    if os.path.exists(RESUME):
        for l in open(RESUME, encoding="utf-8"):
            try:
                d = json.loads(l); done[d["domain"]] = d
            except Exception:
                pass
    tasks, seen = [], set()
    for r in csv.DictReader(open(a.tasks, encoding="utf-8", errors="replace")):
        w = (r.get("website") or "").strip()
        h = (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower().removeprefix("www.")
        if not h or "." not in h:
            continue
        dom = C.registrable(h)
        if dom in seen or dom in done:
            continue
        seen.add(dom); tasks.append((dom, r.get("key", ""), r.get("name", ""), "https://%s/" % h, r.get("kind", "")))
    if a.limit:
        tasks = tasks[:a.limit]
    print("tasks: %d new domains (%d done before)" % (len(tasks), len(done)), flush=True)
    out_gz = os.path.join(a.repo, "data/incoming/claude/claude_org_contacts.jsonl.gz")
    stats, last_dump = {}, [time.time()]

    def dump():
        with lock:
            rows = [d for d in done.values() if d.get("status") == "ok"]
        os.makedirs(os.path.dirname(out_gz), exist_ok=True)
        with gzip.open(out_gz + ".tmp", "wt", encoding="utf-8") as f:
            for d in sorted(rows, key=lambda d: d["domain"]):
                f.write(json.dumps(d, ensure_ascii=False) + "\n")
        os.replace(out_gz + ".tmp", out_gz)
        print(time.strftime("%H:%M"), "wrote", out_gz, len(rows), "organisations", dict(stats), flush=True)

    def one(t):
        dom, key, name, site, kind = t
        try:
            res = read_site(site, name)
        except Exception as e:
            res = {"status": "error", "error": str(e)[:100]}
        res.update({"domain": dom, "key": key, "name": name, "website": site, "kind": kind, "date": TODAY})
        with lock:
            done[dom] = res
            stats[res["status"]] = stats.get(res["status"], 0) + 1
            with open(RESUME, "a", encoding="utf-8") as f:
                f.write(json.dumps(res, ensure_ascii=False) + "\n")
            due = time.time() - last_dump[0] > 300
            if due:
                last_dump[0] = time.time()
        if due:
            dump()

    threading.Thread(target=watchdog, daemon=True).start()
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, tasks))
    dump()
    print("finished", dict(stats), flush=True)


if __name__ == "__main__":
    main()
