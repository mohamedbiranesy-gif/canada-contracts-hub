#!/usr/bin/env python3
"""Extra facts an organisation prints on its own site (buyers and vendors), evidence or nothing:
  - legal name as printed in the copyright / footer line ("© 2026 Acme Holdings Inc.", "Tous droits réservés Ville de X");
  - Business Number / GST-HST / charity registration number as printed ("GST/HST # 123456789 RT0001", "BN 12345 6789 RR0001",
    "Numéro d'entreprise du Québec 1234567890" → NEQ); the GST/HST account is derived from a BN9 and always labelled so;
  - logo image URL (og:image or an <img> whose src / alt says logo);
  - language of the site (fr / en / fr-en from the html lang attribute and stopwords);
  - whether the site answers (status).
Reads the home page and up to two "about / legal / contact / donate" pages. Polite: robots.txt, 1 request / second / host,
identified UA. Output: ~/cch-crawler-state/org_extras.jsonl (resume) and <repo>/data/incoming/claude/claude_org_extras.jsonl.gz
(read by contrib/claude/rank_buyers/rank.py), one JSON per registrable domain with the page URL and a ≤300-char quote per fact.
  python3 tools/org_extras.py --tasks tasks.csv [--workers 48] [--repo ~/cch-crawler]
"""
import argparse, csv, gzip, html, json, os, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C
from org_contacts import strip_long, visible_keep_lines, flat

STATE = os.path.expanduser("~/cch-crawler-state")
RESUME = os.path.join(STATE, "org_extras.jsonl")
TODAY = time.strftime("%Y-%m-%d")
lock = threading.Lock()
COPY = re.compile(r"(?:©|&copy;|\(c\)|copyright|tous droits r[ée]serv[ée]s|all rights reserved)[\s,.]*(?:copyright\s*)?(?:(?:19|20)\d\d(?:\s*[-–]\s*(?:19|20)?\d\d)?)?[\s,.]*"
                  r"(?:by\s+|par\s+)?([A-Z0-9][^|•\n©]{2,90}?)(?=\s*(?:\.|\||•|all rights|tous droits|-|–|—|$|\n|privacy|confidentialit|terms|conditions|site|powered|design|web|\d{4}))", re.I)
COPY2 = re.compile(r"([A-Z0-9][^|•\n©]{2,90}?)\s*(?:©|&copy;)\s*(?:19|20)\d\d", re.I)
LEGAL_TAIL = re.compile(r"\b(inc|incorporated|ltd|limited|lt[ée]e|llc|llp|lp|corp|corporation|co|company|s\.?e\.?n\.?c|s\.?a|plc|gmbh|ag|srl|ulc|society|association|foundation|fondation|"
                        r"university|universit[ée]|college|coll[èe]ge|c[ée]gep|city of|town of|village of|municipality of|ville de|municipalit[ée] de|county of|district of|"
                        r"regional district of|township of|first nation|nation|band|school board|school division|school district|conseil scolaire|centre de services scolaire|"
                        r"commission scolaire|hospital|health|sant[ée]|authority|board|commission|agency|office|ministry|department|government|gouvernement|library|biblioth[èe]que|"
                        r"church|[ée]glise|parish|paroisse|trust|group|groupe|holdings|partners|partnership|cooperative|co-op|coop|credit union|caisse)\b", re.I)
BN = re.compile(r"(?:(?:GST|HST|GST/HST|TPS|TVH|TPS/TVH|business\s*number|numéro\s*d['’]entreprise(?:\s*(?:f[ée]d[ée]ral|du\s*Canada))?|\bBN\b|charitable\s*registration|registration\s*(?:no|number|#)|"
                r"num[ée]ro\s*d['’]enregistrement|num[ée]ro\s*d['’]organisme\s*de\s*bienfaisance|charity\s*(?:no|number|#)|RR\s*0001|RT\s*0001)[^\d/A-Za-z]{0,12}(?:[A-Za-z]{0,3}[^\d/A-Za-z]{0,6})?)"
                r"(?<![\dA-Za-z/])(\d{5}\s?\d{4}|\d{9})(?!\d)\s*((?:RT|RR|RP|RC)\s?\d{4})?", re.I)
NEQ = re.compile(r"(?:NEQ|num[ée]ro\s*d['’]entreprise\s*du\s*Qu[ée]bec)[^\d]{0,20}(\d{10})\b", re.I)
QST = re.compile(r"(?:TVQ|QST)[^\d]{0,15}(\d{10})\s*(TQ\s?\d{4})", re.I)
LOGO = re.compile(r"(?is)<img[^>]+(?:src|data-src)\s*=\s*[\"']([^\"']+)[\"'][^>]*>")
OG = re.compile(r"(?is)<meta[^>]+property\s*=\s*[\"']og:image[\"'][^>]+content\s*=\s*[\"']([^\"']+)")
OG2 = re.compile(r"(?is)<meta[^>]+content\s*=\s*[\"']([^\"']+)[\"'][^>]+property\s*=\s*[\"']og:image[\"']")
LANG = re.compile(r"(?is)<html[^>]+lang\s*=\s*[\"']([a-zA-Z]{2})")
FRW = re.compile(r"\b(de la|des|les|pour|avec|nous|vous|notre|votre|est|sont|une|dans|sur|à propos|accueil|nous joindre|services)\b", re.I)
ENW = re.compile(r"\b(the|and|for|with|our|your|about|home|contact|services|from|this|that|are|is|more)\b", re.I)
PAGE_LINK = re.compile(r"about|a-propos|apropos|legal|mentions|privacy|confidentialit|terms|conditions|contact|nous-joindre|donate|don\b|faire-un-don|give|charitable|tax-receipt|re[cç]u", re.I)


def quote_at(text, needle, n=300):
    i = text.find(needle)
    if i < 0:
        return flat(needle)[:n]
    return flat(text[max(0, i - 100):i + len(needle) + 100])[:n]


def legal_name(text, host):
    """the organisation's legal name as printed in the copyright line, if it looks like a legal name"""
    cands = []
    for rx in (COPY, COPY2):
        for m in rx.finditer(text):
            c = flat(m.group(1))
            c = re.sub(r"^(?:by|par)\s+", "", c, flags=re.I).strip(" .,-–—|")
            c = re.split(r"\s+(?:registered charity|charitable registration|accessibilit|privacy|confidentialit|terms|conditions|sitemap|plan du site|contact|"
                         r"disclaimer|avis|legal|mentions l[ée]gales|login|connexion|back to top|retour|website|site web|powered|design)\b", c, 1, flags=re.I)[0].strip(" .,-–—|:")
            if 3 <= len(c) <= 90 and LEGAL_TAIL.search(c) and not re.search(r"\b(?:website|site web|design|powered|theme|wordpress|squarespace|wix|shopify|developed|développ|réalis|created|made with|hosting)\b", c, re.I):
                cands.append(c)
    if not cands:
        return ""
    # prefer the shortest candidate that still ends with / contains a legal form word near its end
    cands.sort(key=lambda c: (not re.search(r"\b(inc|ltd|limited|lt[ée]e|llc|llp|corp|corporation|co|society|association|foundation|fondation)\.?$", c, re.I), len(c)))
    return cands[0]


def read_site(site, kind):
    res = {"status": "no_page"}
    if not C.allowed(site):
        res["status"] = "robots"; return res
    st, ct, data, final = C.fetch(site, 3_000_000)
    if st in (401, 403, 429):
        res["status"] = "blocked"; return res
    if st != 200 or not data or "html" not in (ct or "").lower():
        res["status"] = "http_%s" % st; return res
    raw0 = strip_long(data.decode("utf-8", "replace"))
    if C.BLOCK_RX.search(raw0[:5000]) or (len(raw0) < 2500 and re.search(r"incapsula|imperva|datadome|perimeterx", raw0, re.I)):
        res["status"] = "blocked"; return res
    host = (urllib.parse.urlparse(final).hostname or "").lower().removeprefix("www.")
    pages = [(final, raw0)]
    seen = set()
    for u, label in C.links(raw0, final):
        p = urllib.parse.urlparse(u)
        if (p.hostname or "").lower().removeprefix("www.") != host or C.SKIP_EXT.search(p.path or "") or u.split("#")[0] in seen:
            continue
        if PAGE_LINK.search(p.path or "") or PAGE_LINK.search(label or ""):
            seen.add(u.split("#")[0])
            if len(seen) >= 3:
                break
    for u in list(seen)[:3]:
        if not C.allowed(u):
            continue
        st, ct, data, fin = C.fetch(u, 3_000_000)
        if st == 200 and data and "html" in (ct or "").lower():
            pages.append((fin, strip_long(data.decode("utf-8", "replace"))))
    res["status"] = "ok"
    res["pages"] = len(pages)
    m = LANG.search(raw0)
    lang = (m.group(1).lower() if m else "")
    t0 = visible_keep_lines(raw0)
    fr, en = len(FRW.findall(t0)), len(ENW.findall(t0))
    res["language"] = "fr-en" if (fr and en and 0.5 <= fr / max(en, 1) <= 2) else ("fr" if (lang == "fr" or fr > en) else "en" if (lang == "en" or en > fr) else lang)
    for url, raw in pages:
        text = visible_keep_lines(raw)
        ftext = re.sub(r"\s+", " ", text)
        if not res.get("legal_name"):
            ln = legal_name(ftext, host)
            if ln:
                res.update({"legal_name": ln, "legal_name_url": url, "legal_name_quote": quote_at(ftext, ln)})
        if not res.get("bn"):
            for m in BN.finditer(ftext):
                digits = re.sub(r"\D", "", m.group(1))
                if len(digits) == 9 and digits != "000000000" and not re.fullmatch(r"(\d)\1{8}", digits):
                    prog = (m.group(2) or "").replace(" ", "").upper()
                    label = m.group(0)[:40]
                    res.update({"bn": digits, "bn_program": prog, "bn_label": flat(label), "bn_url": url, "bn_quote": quote_at(ftext, m.group(0))})
                    break
        if not res.get("neq"):
            m = NEQ.search(ftext)
            if m:
                res.update({"neq": m.group(1), "neq_url": url, "neq_quote": quote_at(ftext, m.group(0))})
        if not res.get("qst"):
            m = QST.search(ftext)
            if m:
                res.update({"qst": (m.group(1) + " " + m.group(2).replace(" ", "")).strip(), "qst_url": url, "qst_quote": quote_at(ftext, m.group(0))})
        if not res.get("logo_url"):
            m = OG.search(raw) or OG2.search(raw)
            cand = ""
            for im in LOGO.finditer(raw):
                src = re.sub(r"\s+", "", im.group(1))
                tag = im.group(0)
                if re.search(r"logo", src + " " + tag, re.I) and not re.search(r"partner|sponsor|client|award|badge|icon-|payment|visa|mastercard|facebook|twitter|linkedin|instagram|youtube", src, re.I):
                    cand = urllib.parse.urljoin(url, html.unescape(src)); break
            if cand or m:
                res.update({"logo_url": cand or urllib.parse.urljoin(url, html.unescape(m.group(1))), "logo_basis": "logo image on the site" if cand else "og:image of the home page"})
    return res


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--tasks", required=True)
    a.add_argument("--workers", type=int, default=48)
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
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
    print("tasks: %d new domains (%d done before)" % (len(tasks), len(done)), flush=True)
    out_gz = os.path.join(a.repo, "data/incoming/claude/claude_org_extras.jsonl.gz")
    stats, last = {}, [time.time()]

    def dump():
        with lock:
            rows = [d for d in done.values() if d.get("status") == "ok" and any(d.get(k) for k in ("legal_name", "bn", "neq", "qst", "logo_url", "language"))]
        for attempt in range(3):
            try:
                tmp = out_gz + ".%d.tmp" % os.getpid()
                with gzip.open(tmp, "wt", encoding="utf-8") as f:
                    for d in sorted(rows, key=lambda d: d["domain"]):
                        f.write(json.dumps(d, ensure_ascii=False) + "\n")
                os.replace(tmp, out_gz); break
            except Exception as e:
                print(time.strftime("%H:%M"), "dump failed (%s), retrying" % e, flush=True); time.sleep(20)
        print(time.strftime("%H:%M"), "wrote", out_gz, len(rows), "organisations", dict(stats), flush=True)

    def one(t):
        dom, key, name, site, kind = t
        try:
            res = read_site(site, kind)
        except Exception as e:
            res = {"status": "error", "error": str(e)[:100]}
        res.update({"domain": dom, "key": key, "name": name, "website": site, "kind": kind, "date": TODAY})
        with lock:
            done[dom] = res
            stats[res["status"]] = stats.get(res["status"], 0) + 1
            with open(RESUME, "a", encoding="utf-8") as f:
                f.write(json.dumps(res, ensure_ascii=False) + "\n")
            due = time.time() - last[0] > 300
            if due:
                last[0] = time.time()
        if due:
            try:
                dump()
            except Exception as e:
                print("dump error", e, flush=True)

    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, tasks))
    dump()
    print("finished", dict(stats), flush=True)


if __name__ == "__main__":
    main()
