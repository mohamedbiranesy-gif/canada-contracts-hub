#!/usr/bin/env python3
"""Discover vendors' official websites and published organisational contacts (role mailboxes, phones).

Usage: python3 -I vendor_web.py <vendor_master.jsonl> <registry.jsonl> <out_prefix> <shard> <nshards> [threads]
Writes <out_prefix>.shard<k> (append; resumable). Vendors ordered by contracts with high/medium confidence, then all.

Rules: candidate domains come only from the vendor's own distinctive name words; a site is accepted only if its
pages show the company name AND a location match (vendor postal code, city, or province name) from the contract
data or the business registry. robots.txt honoured. Only role mailboxes on the site's own domain are kept
(personal-looking addresses dropped, never constructed). Bot-check pages and obfuscated (protected) emails skipped.
"""
import sys, os, re, json, time, threading, queue, unicodedata, datetime, html as htmlmod
import urllib.parse, urllib.robotparser
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normname import tokens as name_tokens, norm_postal, norm_prov, norm_city, strip_accents  # noqa: E402

VM, REG, OUTP, SHARD, NSH = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
THREADS = int(sys.argv[6]) if len(sys.argv) > 6 else 8
OUT = "%s.shard%d" % (OUTP, SHARD)
UA = "contracts-research/1.0 (vendor website verification; polite, robots.txt honoured)"
TIMEOUT = 8
MAXBYTES = 600_000

LEGAL = {"INC", "LTD", "LTEE", "CORP", "CO", "CIE", "ENR", "SENC", "SENCRL", "SEC", "SRL", "LLC", "LLP", "LP", "ULC", "PLC", "GMBH", "SA", "SAS", "AG", "BV", "NV",
         "LIMITED", "INCORPORATED", "CORPORATION", "COMPANY", "COMPAGNIE", "THE", "LE", "LA", "LES", "L", "DE", "DU", "DES", "D", "ET", "AND", "OF", "A"}
GENERIC = {"SERVICES", "SERVICE", "CONSULTING", "CONSULTANTS", "CONSTRUCTION", "CONSTRUCTIONS", "SOLUTIONS", "TECHNOLOGIES", "TECHNOLOGY", "GROUP", "GROUPE",
           "ENTERPRISES", "ENTREPRISES", "HOLDINGS", "INDUSTRIES", "SYSTEMS", "SYSTEMES", "INTERNATIONAL", "CANADA", "MANAGEMENT", "ASSOCIATES", "GESTION",
           "LES", "INC", "SUPPLY", "SUPPLIES", "EQUIPMENT", "PRODUCTS", "COMPANY", "CANADIAN", "NATIONAL", "GLOBAL", "GENERAL", "NORTH", "AMERICA"}
PROV_NAMES = {"AB": ["ALBERTA"], "BC": ["BRITISH COLUMBIA", "COLOMBIE-BRITANNIQUE"], "MB": ["MANITOBA"], "NB": ["NEW BRUNSWICK", "NOUVEAU-BRUNSWICK"],
              "NL": ["NEWFOUNDLAND"], "NS": ["NOVA SCOTIA", "NOUVELLE-ECOSSE"], "ON": ["ONTARIO"], "PE": ["PRINCE EDWARD ISLAND"], "QC": ["QUEBEC"],
              "SK": ["SASKATCHEWAN"], "NT": ["NORTHWEST TERRITORIES"], "NU": ["NUNAVUT"], "YT": ["YUKON"]}
ROLE = re.compile(r"^(info|information|contact|contacts|contactus|hello|bonjour|allo|sales|ventes|vente|sales\.?ca|admin|administration|office|bureau|reception|accueil|"
                  r"accounting|accounts|comptabilite|compta|ar|a\.r|receivables|accountsreceivable|accounts\.receivable|billing|facturation|invoices?|factures?|finance|"
                  r"service|services|support|customerservice|customer\.service|serviceclient|service\.client|orders?|commandes?|quotes?|soumissions?|estimating|"
                  r"estimation|bids?|tenders?|appels?doffres|projects?|projets|inquiries|enquiries|general|mail|team|equipe|hr|careers|emplois|rh|marketing|media|"
                  r"press|purchasing|achats|procurement|dispatch|operations|ops|safety|tech|it|web|webmaster|privacy|legal|compliance)([._-].*)?$", re.I)
PERSONAL = re.compile(r"^[a-z]+[._-][a-z]+$|^[a-z]\.?[a-z]{3,}$|^[a-z]{2,}\d+$", re.I)
EMAIL_RE = re.compile(r"(?<![A-Za-z0-9._%+-])([A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,24})")
PHONE_RE = re.compile(r"(?:\+?1[\s.-]?)?\(?([2-9]\d{2})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})(?!\d)")
CHALLENGE = re.compile(r"cf-chl|challenge-platform|_incapsula_resource|<title>just a moment|perfdrive|radware bot|px-captcha|captcha-delivery|/cdn-cgi/l/email-protection", re.I)
CONTACT_LINK = re.compile(r"contact|nous-joindre|nousjoindre|joindre|contactez|coordonnees|about|a-propos|apropos|qui-sommes|company|entreprise|locations?|bureaux", re.I)
TAG_RE = re.compile(r"<script.*?</script>|<style.*?</style>|<[^>]+>", re.S | re.I)


def fold(s):
    return strip_accents(htmlmod.unescape(s or "")).upper()


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------- load inputs ----------
reg = {}
with open(REG, encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        best = [m for m in d.get("registry_matches") or [] if m.get("match_confidence") in ("exact", "strong")]
        if best:
            b = best[0]
            reg[d["vendor_key"]] = {"legal_name": b.get("legal_name"), "other_names": (b.get("other_names") or [])[:3],
                                    "registered_office": b.get("registered_office") or {},
                                    "domicile_address": {"lines": ((b.get("domicile_address") or {}).get("lines") or [])[:4]}}

import glob
done = set()
for _p in glob.glob(OUTP + ".shard*"):
    with open(_p, encoding="utf-8") as f:
        for line in f:
            try:
                done.add(json.loads(line)["vendor_key"])
            except Exception:
                pass

todo = []
with open(VM, encoding="utf-8") as f:
    for line in f:
        v = json.loads(line)
        if v["vendor_key"] in done:
            continue
        todo.append({"vendor_key": v["vendor_key"], "name": v.get("name"), "name_variants": (v.get("name_variants") or [])[:4],
                     "addresses": [{"value": {k: (a.get("value") or {}).get(k) for k in ("city", "region", "postal_code")}} for a in (v.get("addresses") or [])[:6] if isinstance(a.get("value"), dict)],
                     "record_count_high_or_medium": v.get("record_count_high_or_medium"), "record_count": v.get("record_count")})
todo.sort(key=lambda v: (-(v.get("record_count_high_or_medium") or 0), -(v.get("record_count") or 0)))
todo = todo[SHARD::NSH]
print("todo", len(todo), "done", len(done), file=sys.stderr, flush=True)


def domain_candidates(v):
    names = [v.get("name")] + (v.get("name_variants") or [])[:4]
    r = reg.get(v["vendor_key"])
    if r and r.get("legal_name"):
        names.append(r["legal_name"])
        names += (r.get("other_names") or [])[:3]
    cands, seen_tokens = [], []
    for n in names:
        if not n:
            continue
        n = re.split(r"\s+(?:o/a|dba|d/b/a|operating as|faisant affaire sous|s/n)\s+", str(n), flags=re.I)[-1]
        n = re.sub(r"\(.*?\)", " ", n)
        t = [x for x in name_tokens(n) if x not in LEGAL]
        if not t or (t[0].isdigit() and len(t[0]) >= 4):
            continue
        if all(x in GENERIC for x in t):
            continue
        seen_tokens.append(t)
        joined = "".join(t).lower()
        noncan = [x for x in t if x not in ("CANADA", "CANADIAN")]
        opts = []
        if 4 <= len(joined) <= 30:
            opts += [joined + ".ca", joined + ".com"]
        if noncan and noncan != t:
            j2 = "".join(noncan).lower()
            if 4 <= len(j2) <= 30:
                opts += [j2 + ".ca", j2 + ".com"]
        if len(t) >= 2 and 4 <= len("-".join(t)) <= 30:
            opts += ["-".join(t).lower() + ".ca", "-".join(t).lower() + ".com"]
        for o in opts:
            if re.fullmatch(r"[a-z0-9-]+\.(ca|com)", o) and o not in cands:
                cands.append(o)
    return cands[:6], seen_tokens


def location_signals(v):
    postals, cities, provs = set(), set(), set()
    for a in v.get("addresses") or []:
        val = a.get("value") or {}
        if not isinstance(val, dict):
            continue
        p = norm_postal(val.get("postal_code"))
        if p:
            postals.add(p)
        c = norm_city(val.get("city"))
        if c and len(c) >= 4:
            cities.add(c)
        pr = norm_prov(val.get("region"))
        if pr:
            provs.add(pr)
    r = reg.get(v["vendor_key"])
    if r:
        ro = r.get("registered_office") or {}
        p = norm_postal(ro.get("postal_code"))
        if p:
            postals.add(p)
        c = norm_city(ro.get("city"))
        if c and len(c) >= 4:
            cities.add(c)
        pr = norm_prov(ro.get("region"))
        if pr:
            provs.add(pr)
        for ln in ((r.get("domicile_address") or {}).get("lines") or []):
            m = re.search(r"[A-Z]\d[A-Z]\s?\d[A-Z]\d", ln.upper())
            if m:
                postals.add(norm_postal(m.group(0)))
            m2 = re.match(r"^(.*?)\s*\(([^)]*)\)", ln)
            if m2:
                c = norm_city(m2.group(1))
                if c and len(c) >= 4:
                    cities.add(c)
    postals.discard(None)
    return postals, cities, provs


robots_cache = {}
robots_lock = threading.Lock()


def allowed(sess, url):
    host = urllib.parse.urlsplit(url).netloc
    with robots_lock:
        rp = robots_cache.get(host)
    if rp is None:
        rp = urllib.robotparser.RobotFileParser()
        try:
            r = sess.get("https://%s/robots.txt" % host, timeout=8, headers={"User-Agent": UA})
            if r.status_code == 200 and len(r.content) < 500_000:
                rp.parse(r.text.splitlines())
            else:
                rp.parse([])
        except Exception:
            rp.parse([])
        with robots_lock:
            robots_cache[host] = rp
    try:
        return rp.can_fetch(UA, url)
    except Exception:
        return True


def fetch(sess, url):
    try:
        r = sess.get(url, timeout=TIMEOUT, headers={"User-Agent": UA, "Accept-Language": "en-CA,fr-CA;q=0.8"}, stream=True, allow_redirects=True)
        ctype = r.headers.get("content-type", "")
        if r.status_code != 200 or "html" not in ctype.lower():
            r.close()
            return r.status_code, None, r.url
        body = r.raw.read(MAXBYTES, decode_content=True)
        r.close()
        txt = body.decode(r.encoding or "utf-8", errors="replace")
        return 200, txt, r.url
    except Exception as e:
        return None, None, url


def page_text(h):
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", h))


def registrable(host):
    host = host.lower().split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    parts = host.split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def extract_contacts(h, url, site_dom):
    emails, phones = [], []
    for m in EMAIL_RE.finditer(htmlmod.unescape(h)):
        e = m.group(1).strip(".").lower()
        local, dom = e.split("@", 1)
        if registrable(dom) != site_dom:
            continue
        if not ROLE.match(local) or (PERSONAL.match(local) and not ROLE.match(local)):
            continue
        if any(x["email"] == e for x in emails):
            continue
        s = max(0, m.start() - 80)
        snip = re.sub(r"\s+", " ", TAG_RE.sub(" ", htmlmod.unescape(h[s:m.end() + 80])))[:200]
        emails.append({"email": e, "page_url": url, "snippet": snip.strip()})
    txt = page_text(h)
    for m in re.finditer(r'href=["\']tel:([^"\']+)', h, re.I):
        d = re.sub(r"\D", "", m.group(1))
        if len(d) in (10, 11):
            d = d[-10:]
            ph = "%s-%s-%s" % (d[:3], d[3:6], d[6:])
            if ph not in phones:
                phones.append(ph)
    if len(phones) < 2:
        for m in PHONE_RE.finditer(txt[:20000]):
            ph = "%s-%s-%s" % m.groups()
            if ph not in phones:
                phones.append(ph)
            if len(phones) >= 3:
                break
    return emails[:8], phones[:3]


def verify(txt_folded, tokens_list, postals, cities, provs):
    name_ok = None
    for t in tokens_list:
        sig = [x for x in t if x not in GENERIC and len(x) >= 3] or t
        if all(re.search(r"\b%s\b" % re.escape(x), txt_folded) for x in sig):
            name_ok = " ".join(t)
            break
    if not name_ok:
        return None
    flat = re.sub(r"[^A-Z0-9]", "", txt_folded)
    for p in postals:
        if p in flat:
            return name_ok, "postal code %s on site" % p
    for c in cities:
        if re.search(r"\b%s\b" % re.escape(c), re.sub(r"[^A-Z0-9 ]", " ", txt_folded)):
            return name_ok, "city %s on site" % c
    for pr in provs:
        for nm in PROV_NAMES.get(pr, []):
            if nm in txt_folded:
                return name_ok, "province %s on site" % nm
    return None


qin = queue.Queue()
for v in todo:
    qin.put(v)
wlock = threading.Lock()
outf = open(OUT, "a", encoding="utf-8")
stats = {"n": 0, "found": 0, "emails": 0}


def worker():
    sess = requests.Session()
    while True:
        try:
            v = qin.get_nowait()
        except queue.Empty:
            return
        cands, toks = domain_candidates(v)
        postals, cities, provs = location_signals(v)
        rec = {"vendor_key": v["vendor_key"], "name": v.get("name"), "candidates_checked": [], "website": None, "website_verification": None,
               "emails": [], "phones": [], "pages_fetched": [], "retrieved_at": now()}
        if cands and (postals or cities or provs):
            for dom in cands:
                url = "https://www." + dom + "/"
                if not allowed(sess, url):
                    rec["candidates_checked"].append({"domain": dom, "result": "robots.txt disallows"})
                    continue
                st, h, final = fetch(sess, url)
                if h is None:
                    st2, h, final = fetch(sess, "https://" + dom + "/")
                    st = st2 if h is not None else (st or st2)
                if h is None:
                    rec["candidates_checked"].append({"domain": dom, "result": "no page (%s)" % st})
                    continue
                if CHALLENGE.search(h[:20000]) and "email-protection" not in h[:20000].lower():
                    rec["candidates_checked"].append({"domain": dom, "result": "bot check, skipped"})
                    continue
                site_dom = registrable(urllib.parse.urlsplit(final).netloc)
                pages = [(final, h)]
                links = []
                for m in re.finditer(r'href=["\']([^"\'#]+)["\']', h, re.I):
                    u = urllib.parse.urljoin(final, m.group(1))
                    if registrable(urllib.parse.urlsplit(u).netloc) == site_dom and CONTACT_LINK.search(urllib.parse.urlsplit(u).path) and u not in links:
                        links.append(u)
                for u in links[:3]:
                    if not allowed(sess, u):
                        continue
                    time.sleep(0.8)
                    st3, h3, f3 = fetch(sess, u)
                    if h3 and not CHALLENGE.search(h3[:20000]):
                        pages.append((f3, h3))
                folded = fold(" ".join(page_text(p[1])[:200000] for p in pages))
                ver = verify(folded, toks, postals, cities, provs)
                if not ver:
                    rec["candidates_checked"].append({"domain": dom, "result": "page found but company name + location not confirmed"})
                    continue
                rec["website"] = "https://" + urllib.parse.urlsplit(final).netloc + "/"
                same = registrable(urllib.parse.urlsplit(final).netloc) == registrable(dom)
                rec["website_verification"] = {"name_tokens_found": ver[0], "location_signal": ver[1], "domain_guessed_from_name": dom,
                                               "confidence": "verified" if same else "verified_via_redirect",
                                               "note": None if same else "the guessed domain %s redirects to %s (often a parent company or brand site)" % (dom, registrable(urllib.parse.urlsplit(final).netloc))}
                for (pu, ph) in pages:
                    rec["pages_fetched"].append(pu)
                    em, phn = extract_contacts(ph, pu, site_dom)
                    for e in em:
                        if not any(x["email"] == e["email"] for x in rec["emails"]):
                            e["retrieved_at"] = now()
                            rec["emails"].append(e)
                    for p in phn:
                        if p not in rec["phones"]:
                            rec["phones"].append(p)
                rec["candidates_checked"].append({"domain": dom, "result": "verified"})
                break
        else:
            rec["candidates_checked"].append({"result": "skipped: no distinctive name words or no location to verify against"})
        with wlock:
            outf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            outf.flush()
            stats["n"] += 1
            stats["found"] += rec["website"] is not None
            stats["emails"] += bool(rec["emails"])
            if stats["n"] % 250 == 0:
                print(now(), stats, file=sys.stderr, flush=True)


ths = [threading.Thread(target=worker, daemon=True) for _ in range(THREADS)]
for t in ths:
    t.start()
for t in ths:
    t.join()
print("done", stats, file=sys.stderr)
