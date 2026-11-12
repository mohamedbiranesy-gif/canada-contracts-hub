#!/usr/bin/env python3
"""Small dated-buyer categories (owner, 2026-11-03: "add them all"), each clearly labelled in canada_field. No AI.

    python3 tools/small_sources.py fir      [--years 2025,2024]   Ontario FIR Schedule 02: municipality -> audit firm
    python3 tools/small_sources.py fnfta    [--bands 1-820]       First Nations FNFTA audited statements -> audit firm
    python3 tools/small_sources.py bcsofi   [--proof site]        BC FIA schedules of payments -> suppliers proven by the address on their own site
    python3 tools/small_sources.py pubs                           Canada-HQ publishers' institutional agreements
    python3 tools/small_sources.py aci                            ACI World (Montreal) dated airport programmes
    python3 tools/small_sources.py tasks <lead.jsonl> <out.csv>   crawl task list for tools/crawl_some.py

Lead files: $CCH_LEADS (default ~/cch-leads)/socrata_<key>.jsonl. Cache: $CCH_SMALL_CACHE (default ~/cch-sources/small).
Rules kept in the code: robots.txt, <= 1 request / 1.1 s per host, project user agent, a 401/403/429 or a challenge page
is "blocked" and skipped, every value quoted (<= 300 chars) from a page actually fetched, named persons' e-mails never
written (FIR lines 0020-0028, 0090, 0091, 0093, 0095 are dropped).
"""
import argparse, csv, datetime as dt, hashlib, html, io, json, os, re, subprocess, sys, tempfile, threading, time
import urllib.error, urllib.parse, urllib.request, urllib.robotparser, zipfile

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
LEADS = os.path.expanduser(os.environ.get("CCH_LEADS", "~/cch-leads"))
CACHE = os.path.expanduser(os.environ.get("CCH_SMALL_CACHE", "~/cch-sources/small"))
WINDOW = "2025-11-02"          # record dated on/after this day (12 months before 2026-11-02)
TODAY = dt.date.today().isoformat()
GAP = 1.1                      # seconds between two requests to one host (<= 1 request/second)
_last, _locks, _robots, _glock = {}, {}, {}, threading.Lock()
CHALLENGE = re.compile(r"cf-chl|challenge-platform|Just a moment\.\.\.|Verifying you are human|Attention Required|"
                       r"captcha|Access denied", re.I)
GENERIC_MAIL = {"gmail.com", "outlook.com", "hotmail.com", "yahoo.com", "yahoo.ca", "bell.net", "sympatico.ca",
                "rogers.com", "live.com", "icloud.com", "me.com", "shaw.ca", "telus.net", "cogeco.ca", "eastlink.ca",
                "xplornet.com", "msn.com", "aol.com", "execulink.com", "tbaytel.net", "ontera.net", "nexicom.net"}


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, file=sys.stderr, flush=True)


def _wait(host):
    with _glock:
        lk = _locks.setdefault(host, threading.Lock())
    lk.acquire()
    w = _last.get(host, 0) + GAP - time.time()
    if w > 0:
        time.sleep(w)
    _last[host] = time.time()
    lk.release()


def _cpath(url):
    return os.path.join(CACHE, "http", hashlib.sha1(url.encode()).hexdigest()[:2], hashlib.sha1(url.encode()).hexdigest())


def robots_ok(url):
    p = urllib.parse.urlparse(url)
    key = "%s://%s" % (p.scheme, p.netloc)
    if key not in _robots:
        rp = urllib.robotparser.RobotFileParser()
        st, body, _, _ = get(key + "/robots.txt", check_robots=False, limit=500_000)
        if st in (401, 403):
            rp.disallow_all = True
        rp.parse((body or b"").decode("utf-8-sig", "replace").splitlines() if st == 200 else [])
        _robots[key] = rp
    try:
        return _robots[key].can_fetch(UA, url)
    except Exception:
        return True


def get(url, check_robots=True, limit=60_000_000, data=None, headers=None, cache=True):
    """(status, body bytes, final url, content type). Cached on disk. status 'robots' / 'blocked' / 0 (network)."""
    ck = url if data is None else url + "#" + hashlib.sha1(data).hexdigest()
    cp = _cpath(ck)
    if cache and os.path.exists(cp + ".json"):
        meta = json.load(open(cp + ".json"))
        body = open(cp, "rb").read() if os.path.exists(cp) else b""
        return meta["status"], body, meta["final"], meta["ctype"]
    if check_robots and not robots_ok(url):
        return "robots", b"", url, ""
    host = urllib.parse.urlparse(url).hostname or ""
    _wait(host)
    h = {"User-Agent": UA, "Accept-Language": "en-CA,en;q=0.8,fr;q=0.5"}
    h.update(headers or {})
    status, body, final, ctype = 0, b"", url, ""
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h), timeout=40) as r:
            status, final, ctype = r.status, r.geturl(), r.headers.get("content-type") or ""
            body = r.read(limit)
    except urllib.error.HTTPError as e:
        status = e.code
        try:
            body = e.read(200_000)
        except Exception:
            pass
    except Exception as e:
        status = 0
        body = str(e).encode()[:500]
    if status in (401, 403, 429) or (status == 503 and CHALLENGE.search(body[:20000].decode("latin-1"))):
        status = "blocked"
    elif status == 200 and "html" in ctype and CHALLENGE.search(body[:6000].decode("latin-1")) and len(body) < 30000:
        status = "blocked"
    if cache and status != 0:
        os.makedirs(os.path.dirname(cp), exist_ok=True)
        with open(cp, "wb") as fh:
            fh.write(body)
        json.dump({"url": url, "status": status, "final": final, "ctype": ctype, "fetched": TODAY}, open(cp + ".json", "w"))
    return status, body, final, ctype


def text_of(body):
    t = body.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</h\d>|</td>|</tr>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"[ \t\r\f\v\xa0]+", " ", t)


def pdf_text(body, layout=True):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
        fh.write(body)
        fh.flush()
        try:
            r = subprocess.run(["pdftotext"] + (["-layout"] if layout else []) + [fh.name, "-"], capture_output=True,
                               timeout=120)
            return r.stdout.decode("utf-8", "replace")
        except Exception:
            return ""


def quote(s, n=300):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"


def host_of(url):
    h = (urllib.parse.urlparse(url if "//" in url else "http://" + url).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def site_url(raw):
    raw = (raw or "").strip().strip("/")
    if not raw or " " in raw or "." not in raw:
        return ""
    if not raw.lower().startswith("http"):
        raw = "https://" + raw
    p = urllib.parse.urlparse(raw)
    return "https://%s/" % (p.hostname or "").lower() if p.hostname else ""


def write_leads(key, leads):
    os.makedirs(LEADS, exist_ok=True)
    path = os.path.join(LEADS, "socrata_%s.jsonl" % key)
    seen, n = set(), 0
    with open(path + ".tmp", "w", encoding="utf-8") as fh:
        for r in leads:
            k = (r["domain"], r["publisher"].lower(), r["vendor"].lower(), r["row"].get("record_date", ""))
            if k in seen:
                continue
            seen.add(k)
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            n += 1
    os.replace(path + ".tmp", path)
    buyers = {(r["publisher"].lower()) for r in leads}
    sited = {(r["publisher"].lower()) for r in leads if r.get("website")}
    dated = {(r["publisher"].lower()) for r in leads if r["row"].get("record_date", "") >= WINDOW}
    st = {"key": key, "leads": n, "buyers": len(buyers), "with_website": len(sited), "dated_in_window": len(dated),
          "written": time.strftime("%Y-%m-%d %H:%M")}
    json.dump(st, open(path + ".stats", "w"))
    log("wrote", path, st)
    return st


# ----------------------------------------------------------------------------------------------------------------
# Canadian address finder (vendor's own site)
PROV = r"(?:ON|Ont\.?|Ontario|QC|Qu[ée]bec|AB|Alberta|BC|B\.C\.|British Columbia|MB|Manitoba|SK|Saskatchewan|NS|" \
       r"Nova Scotia|NB|New Brunswick|NL|Newfoundland(?: and Labrador)?|PE|PEI|Prince Edward Island|YT|Yukon|NT|NU)"
POSTAL = r"[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d"
ADDR = re.compile(r"(?:\d{1,6}[A-Za-z]?[ ,\-][^\n]{2,110}?(?:\n\s*[^\n]{2,60}?)?|P\.?O\.? Box[^\n]{1,100}?)[,\s]+" + PROV +
                  r"\.?[,\s]+" + POSTAL)
CONTACT_LINK = re.compile(r"contact|location|office|about|nous-joindre|coordonn|find-us|our-firm|qui-sommes", re.I)


def canada_address_on_site(site, max_pages=6):
    """First Canadian street address (province + postal code) on the site's home / contact pages: (quote, url)."""
    queue, seen = [site], set()
    while queue and len(seen) < max_pages:
        u = queue.pop(0)
        if u in seen:
            continue
        seen.add(u)
        st, body, final, ct = get(u, limit=3_000_000)
        if st != 200 or "html" not in ct:
            continue
        t = text_of(body)
        m = ADDR.search(t)
        if m:
            return quote(m.group(0)), final
        if len(seen) == 1:
            links = re.findall(r'href="([^"#]+)"', body.decode("utf-8", "replace"), re.I)
            for l in links:
                a = urllib.parse.urljoin(final, html.unescape(l))
                if host_of(a) == host_of(site) and CONTACT_LINK.search(urllib.parse.urlparse(a).path) and a not in queue:
                    queue.append(a)
    return "", ""


# ----------------------------------------------------------------------------------------------------------------
# 1a. Ontario FIR Schedule 02: auditor of record
FIR_BASE = "https://efis.fma.csc.gov.on.ca/fir/index.php/en/"
FIR_PAGES = {"2025": FIR_BASE + "reports-and-dashboards/fir-by-year-and-municipality/",
             "2024": FIR_BASE + "year-municipality/year-2024-2-2-2-2/"}
FIR_TYPES = {"Tp": "Township of", "T": "Town of", "ST": "Town of", "C": "City of", "V": "Village of",
             "M": "Municipality of", "Co": "County of", "County": "County of", "UCo": "United Counties of",
             "R": "Regional Municipality of", "D": "District Municipality of", "CoR": "County of", "Mu": "Municipality of"}
FIR_DROP = {"0020", "0022", "0028", "0090", "0091", "0093", "0095"}   # named persons, their phones and e-mails
# The big firms' Canadian legal names; their Canada proof is read live from their own Canadian site (FIRM_PROOF).
FIRM_CANON = [(r"^MNP\b", "MNP LLP", "mnp.ca"), (r"^KPMG\b", "KPMG LLP", "kpmg.com"),
              (r"^BDO\b", "BDO Canada LLP", "bdo.ca"), (r"^DELOITTE\b", "Deloitte LLP", "deloitte.ca"),
              (r"^BAKER TILLY\b", None, None), (r"^GRANT THORNTON\b", "Grant Thornton LLP", "grantthornton.ca"),
              (r"^(PWC|PRICEWATERHOUSE)", "PricewaterhouseCoopers LLP", "pwc.com"),
              (r"^(EY|ERNST)\b", "Ernst & Young LLP", "ey.com"), (r"^RSM\b", "RSM Canada LLP", "rsmcanada.com"),
              (r"^COLLINS BARROW\b", None, None)]


def fir_index(year):
    st, body, final, _ = get(FIR_PAGES[year], cache=False)
    if st != 200:
        log("FIR index", year, st)
        return []
    t = body.decode("utf-8", "replace")
    urls = sorted(set(re.findall(r'https?://[^"\']*by-year-and-municipality/%s//[^"\']+?\.zip' % year, t)))
    return urls


def _xlsx_sheet_rows(xbytes, sheet_name, max_row=150):
    """Rows (lists of cell strings, in column order) of one sheet, read straight from the xlsx XML (openpyxl takes ~6 s
    per FIR workbook; this takes ~0.05 s)."""
    x = zipfile.ZipFile(io.BytesIO(xbytes))
    wb = x.read("xl/workbook.xml").decode("utf-8", "replace")
    m = re.search(r'<sheet [^>]*name="%s"[^>]*r:id="(rId\d+)"' % re.escape(sheet_name), wb)
    rels = x.read("xl/_rels/workbook.xml.rels").decode("utf-8", "replace")
    tgt = re.search(r'<Relationship [^>]*Id="%s"[^>]*Target="([^"]+)"' % m.group(1), rels) or \
        re.search(r'<Relationship [^>]*Target="([^"]+)"[^>]*Id="%s"' % m.group(1), rels)
    path = "xl/" + tgt.group(1).lstrip("/").replace("xl/", "")
    shared = []
    if "xl/sharedStrings.xml" in x.namelist():
        for si in re.findall(r"<si>(.*?)</si>", x.read("xl/sharedStrings.xml").decode("utf-8", "replace"), re.S):
            shared.append(html.unescape("".join(re.findall(r"<t[^>]*>(.*?)</t>", si, re.S))))
    xml = x.read(path).decode("utf-8", "replace")
    rows = []
    for rm in re.finditer(r'<row [^>]*r="(\d+)"[^>]*>(.*?)</row>', xml, re.S):
        if int(rm.group(1)) > max_row:
            break
        cells = []
        for cm in re.finditer(r'<c ([^>]*?)(?:/>|>(.*?)</c>)', rm.group(2), re.S):
            attrs, inner = cm.group(1), cm.group(2) or ""
            v = re.search(r"<v>(.*?)</v>", inner, re.S)
            t = re.search(r'\bt="(\w+)"', attrs)
            if t and t.group(1) == "s" and v:
                val = shared[int(v.group(1))]
            elif t and t.group(1) == "inlineStr":
                val = html.unescape("".join(re.findall(r"<t[^>]*>(.*?)</t>", inner, re.S)))
            else:
                val = html.unescape(v.group(1)) if v else ""
            if val.strip():
                cells.append(val.strip())
        rows.append((int(rm.group(1)), cells))
    return rows


def _excel_date(v):
    try:
        f = float(v)
        if 30000 < f < 60000:
            return (dt.date(1899, 12, 30) + dt.timedelta(days=int(f))).isoformat()
    except ValueError:
        pass
    return v


def fir_parse(zbody):
    z = zipfile.ZipFile(io.BytesIO(zbody))
    name = [n for n in z.namelist() if n.lower().endswith(".xlsx")][0]
    head, lines = {}, {}
    for rn, s in _xlsx_sheet_rows(z.read(name), "02"):
        if not s:
            continue
        if rn == 1:
            head["printed"] = _excel_date(s[-1].split(".")[0]) if re.fullmatch(r"[\d.]+", s[-1]) else s[-1]
        for lab, key in (("Municipality:", "municipality"), ("Tier:", "tier"), ("Asmt Code:", "asmt_code"),
                         ("Area:", "area"), ("MAH Code:", "mah_code"), ("MSO Office:", "mso_office")):
            if lab in s and s.index(lab) + 1 < len(s):
                head[key] = s[s.index(lab) + 1]
        if re.fullmatch(r"\d{4}", s[0]) and len(s) >= 3:
            val = s[2] if s[0] in ("0075", "0077") else s[-1]
            lines[s[0]] = (re.sub(r"\s+", " ", s[1]).strip(), _excel_date(val) if s[0] == "0094" else val)
    return name, head, lines


def fir_buyer_name(fir_name):
    p = fir_name.strip().rsplit(" ", 1)
    if len(p) == 2 and p[1] in FIR_TYPES:
        return "%s %s" % (FIR_TYPES[p[1]], p[0])
    return fir_name.strip()


def firm_key(name):
    s = re.sub(r"[^A-Z0-9& ]", " ", (name or "").upper().replace("’", "'"))
    s = re.sub(r"\b(LLP|LLP\.|PROFESSIONAL CORPORATION|PROF CORP|PC|CHARTERED PROFESSIONAL ACCOUNTANTS|CHARTERED "
               r"ACCOUNTANTS|CPAS?|CA|LICENSED PUBLIC ACCOUNTANTS|LPA|INC|LTD|THE)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _dom_fits_firm(d, k):
    lab = re.sub(r"[^a-z]", "", d.split(".")[0] if not d.startswith("www.") else d.split(".")[1])
    words = [w.lower() for w in k.split() if w not in ("AND", "&", "CO", "COMPANY", "GROUP", "ASSOCIATES")]
    if any((len(w) >= 4 and w in lab) or (len(w) >= 3 and w == lab) for w in words):
        return True
    ini = "".join(w[0] for w in words if w)
    return len(ini) >= 2 and lab.startswith(ini)


def resolve_firm(name, domains, proofs, exclude=()):
    """(legal name, proof quote, proof url, firm site) from the firm's own site; ('','','','') when not proven."""
    k = firm_key(name)
    if k in proofs:
        return proofs[k]
    legal, site = name.strip(), ""
    for pat, canon, dom in FIRM_CANON:
        if re.search(pat, k):
            if canon:
                legal = canon
            if dom:
                site = "https://www.%s/" % dom
            break
    doms = [d for d in domains if d and d not in GENERIC_MAIL and d not in exclude and _dom_fits_firm(d, k)]
    res = ("", "", "", "")
    for p in FIRM_PROOF:
        if re.search(p["pat"], k) or (p.get("dom") and doms and doms[0] == p["dom"]):
            got = _firm_proof(p, k)
            if got:
                res = (got[0] or re.sub(r"\s+", " ", name).strip(" ,."), got[1], got[2], "https://%s/" % host_of(p["url"]))
            elif re.search(p["pat"], k):
                proofs[k] = res
                return res
            break
    if not res[0]:
        cands = (["https://www.%s/" % d for d in doms[:2]] if doms else []) + ([site] if site else [])
        for c in cands:
            q, u = canada_address_on_site(c)
            if q:
                res = (legal, q, u, c)
                break
    proofs[k] = res
    return res


# Firms with many offices: one Canadian office page each, read live (the regex must match on the page). mnp.ca and
# bdo.ca answer a Cloudflare challenge (403) to this crawler, so MNP LLP / BDO Canada LLP stay unproven (rule 6).
FIRM_PROOF = [
    {"pat": r"^(KPMG|KMPG|KPMH)\b", "dom": "kpmg.ca", "legal": "KPMG LLP",
     "url": "https://kpmg.com/ca/en/about/offices/toronto.html",
     "rx": r"Bay Adelaide Centre,?\s*333 Bay Street,?\s*Suite 4600,?\s*Toronto,?\s*M5H ?2S5"},
    {"pat": r"^DELOITTE\b", "dom": "deloitte.ca", "legal": "Deloitte LLP",
     "url": "https://www.deloitte.com/ca/en/offices/canada-offices.html",
     "rx": r"\d[^\n]{0,60}\s+(?:[^\n]{0,60}\s+)?Toronto,? (?:ON|Ontario)\s+M\d[A-Z] ?\d[A-Z]\d(?:\s+Canada)?"},
    {"pat": r"^DOANE GRANT|^GRANT THORNTON", "dom": "doanegrantthornton.ca", "legal": "Doane Grant Thornton LLP",
     "url": "https://www.doanegrantthornton.ca/contact-us",
     "rx": r"Doane Grant Thornton LLP\s+20th Floor, 200 King Street West\s+Toronto, ON M5H ?3T4"},
    {"pat": r"^BAKER ?TILLY", "dom": "bakertilly.ca", "legal": "", "url": "https://www.bakertilly.ca/locations",
     "rx": r"Baker Tilly {member}[A-Za-z ]*?(?: LLP)?\s+[^\n]{3,60}\s+(?:[^\n]{3,60}\s+)?[A-Za-z .'-]+, ON\s+" + POSTAL},
]


def _firm_proof(p, k):
    rx = p["rx"]
    generic = False
    if "{member}" in rx:
        mem = re.sub(r"^BAKER ?TILLY\s*", "", k).split(" ")[0] if re.sub(r"^BAKER ?TILLY\s*", "", k) else ""
        if not mem:   # member firm not named in the record: national office of the Canadian network, name as written
            generic = True
            rx = r"National office\s+130 Eileen Stubbs Ave\s+Suite 201\s+Dartmouth, NS\s+B3B ?2C4"
        rx = rx.replace("{member}", re.escape(mem) if mem else "[A-Z]{2,4}")
        if mem and not re.fullmatch(r"[A-Z]{2,4}", mem):
            rx = rx.replace(re.escape(mem), r"(?i:%s)" % re.escape(mem))
    st, body, final, ct = get(p["url"], limit=5_000_000)
    if st != 200:
        return None
    m = re.search(rx, text_of(body).replace("\r", ""))
    if not m:
        return None
    legal = p["legal"] or ("" if generic else re.match(r"Baker Tilly [A-Za-z ]*?(?: LLP)?(?=\s)", m.group(0)).group(0).strip())
    return legal, quote(m.group(0)), final


FS_LINK = re.compile(r"financial[-_ %20]*statements?|audited|consolidated[-_ %20]*financial|\bfs[-_ ]?2025", re.I)
FS_FIRM = {"MNP": ("MNP LLP", r"MNP\s+LLP"), "BDO": ("BDO Canada LLP", r"BDO\s+Canada\s+LLP")}


def fs_auditor_proof(site, firm):
    """(legal name, quote, pdf url): the auditor's report signature in the municipality's 2025 audited statements,
    e.g. "MNP LLP ... Chartered Professional Accountants ... Cornwall, Ontario ... September 9, 2026"."""
    legal, frx = FS_FIRM[firm_key(firm).split()[0]]
    for url, anchor in find_sofi(site, False, max_pages=25, link_rx=FS_LINK)[:3]:
        st, body, final, ct = get(url, limit=60_000_000)
        if st != 200 or not body.startswith(b"%PDF"):
            continue
        txt = pdf_text(body)
        m = re.search(frx + r"[^\n]*\n\s*[^\n]{3,120}?" + PROV + r"\.?,?\s+" + POSTAL, txt) or re.search(
            frx + r"[^\n]*\n(?:[^\n]*\n){0,8}?[^\n]*?\b([A-Z][A-Za-z.'\- ]{2,40}),\s*(?:Ontario|ON|Canada)\b"
                      r"(?:[^\n]*\n){0,4}?[^\n]*?\b(?:%s)\s+\d{1,2},\s+202[56]" % MONTHS, txt)
        if not m:
            m = re.search(r"\b([A-Z][A-Za-z.'\- ]{2,40}),\s*(?:Ontario|ON|Canada)\b[^\n]*\n(?:[^\n]*\n){0,4}?[^\n]*?\b(?:%s)"
                          r"\s+\d{1,2},\s+202[56](?:[^\n]*\n){0,6}?[^\n]*?" % MONTHS + frx, txt)
        if m:
            return legal, quote(re.sub(r"\s{2,}", " | ", m.group(0))), final
    return None


def cmd_fir(a):
    years = a.years.split(",")
    proofs_path = os.path.join(CACHE, "fir_firm_proofs.json")
    proofs = {k: tuple(v) for k, v in json.load(open(proofs_path)).items()} if os.path.exists(proofs_path) and not a.refresh_firms else {}
    recs, have = [], set()
    for y in years:
        urls = fir_index(y)
        log("FIR", y, len(urls), "zips")
        for u in urls:
            code = re.search(r"/FI\d\d(\d{4})", u)
            code = code.group(1) if code else u
            if code in have:
                continue
            st, body, final, ct = get(u)
            if st != 200 or not body.startswith(b"PK"):
                log("FIR zip", st, u)
                continue
            try:
                fname, head, lines = fir_parse(body)
            except Exception as e:
                log("FIR parse", type(e).__name__, u)
                continue
            date = str(lines.get("0094", ("", ""))[1])[:10]
            if y != years[0] and date < WINDOW:
                continue
            have.add(code)
            recs.append((y, u, fname, head, lines, date))
    # firm resolution (audit firm's own Canadian site)
    doms = {}
    for y, u, fname, head, lines, date in recs:
        firm = lines.get("0092", ("", ""))[1]
        em = str(lines.get("0095", ("", ""))[1])
        d = em.split("@")[-1].strip().lower() if "@" in em else ""
        doms.setdefault(firm_key(firm), []).append(d)
    leads, nofirm, noproof, fs_todo = [], 0, {}, []
    muni_doms = {host_of(site_url(str(r[4].get("0030", ("", ""))[1]))) for r in recs} - {""}
    for y, u, fname, head, lines, date in recs:
        firm = str(lines.get("0092", ("", ""))[1]).strip()
        if not firm or firm.lower() in ("none", "n/a", "0"):
            nofirm += 1
            continue
        dl = [d for d, _ in __import__("collections").Counter(doms.get(firm_key(firm), [])).most_common()]
        legal, pq, pu, fsite = resolve_firm(firm, dl, proofs, muni_doms)
        if not legal:
            noproof[firm] = noproof.get(firm, 0) + 1
            web0 = site_url(str(lines.get("0030", ("", ""))[1]))
            if web0 and re.search(r"^(MNP|BDO)\b", firm_key(firm)):
                fs_todo.append((y, u, fname, head, lines, date, firm, web0))
            continue
        muni = head.get("municipality", "").strip() or fname
        web = site_url(str(lines.get("0030", ("", ""))[1]))
        row = {"fir_year": y, "fir_file": fname, "record_date": date}
        row.update({("head_" + k): v for k, v in head.items()})
        for code, (lab, val) in sorted(lines.items()):
            if code not in FIR_DROP:
                row["%s %s" % (code, lab)] = str(val)
        row["vendor_proof_url"], row["vendor_proof_quote"] = pu, pq
        row["evidence_quote"] = quote("Municipality: %s | 0092 Municipal Audit Firm | %s | 0094 Date | %s" % (muni, firm, date))
        leads.append({"platform": "on_fir_auditor", "domain": host_of(web) if web else "",
                      "dataset_id": "FIR%s-S02-%s" % (y, head.get("asmt_code", "")),
                      "dataset": "Ontario Financial Information Return %s, Schedule 02 (Declaration of the Municipal "
                                 "Treasurer), line 0092 Municipal Audit Firm" % y,
                      "dataset_url": u, "publisher": fir_buyer_name(muni), "buyer_unit": "", "website": web,
                      "vendor": legal, "canada_field": "auditor of record (Ontario FIR %s Schedule 02)" % y,
                      "canada_value": pq, "row": row})
    # MNP / BDO sites answer a challenge: prove the firm's Canadian office from the municipality's own audited statements
    todo = [(i, r) for i, r in enumerate(fs_todo)]
    if todo:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(12) as ex:
            for (i, (y, u, fname, head, lines, date, firm, web)), got in zip(todo, ex.map(
                    lambda t: fs_auditor_proof(t[1][7], t[1][6]), todo)):
                if not got:
                    continue
                legal, q, pdf = got
                noproof[firm] = noproof.get(firm, 1) - 1
                muni = head.get("municipality", "").strip() or fname
                row = {"fir_year": y, "fir_file": fname, "record_date": date}
                row.update({("head_" + k): v for k, v in head.items()})
                for code, (lab, val) in sorted(lines.items()):
                    if code not in FIR_DROP:
                        row["%s %s" % (code, lab)] = str(val)
                row["vendor_proof_url"], row["vendor_proof_quote"] = pdf, q
                row["vendor_proof_source"] = "the municipality's own audited financial statements (auditor's report signature)"
                row["evidence_quote"] = quote("Municipality: %s | 0092 Municipal Audit Firm | %s | 0094 Date | %s" % (muni, firm, date))
                leads.append({"platform": "on_fir_auditor", "domain": host_of(web), "dataset_id": "FIR%s-S02-%s" % (
                    y, head.get("asmt_code", "")), "dataset": "Ontario Financial Information Return %s, Schedule 02 "
                    "(Declaration of the Municipal Treasurer), line 0092 Municipal Audit Firm" % y,
                    "dataset_url": u, "publisher": fir_buyer_name(muni), "buyer_unit": "", "website": web, "vendor": legal,
                    "canada_field": "auditor of record (Ontario FIR %s Schedule 02)" % y, "canada_value": q, "row": row})
        log("FIR: MNP/BDO proven from audited statements:", sum(1 for l in leads if l["row"].get("vendor_proof_source")),
            "of", len(todo))
    json.dump(proofs, open(proofs_path, "w"), indent=0)
    log("FIR records", len(recs), "no firm", nofirm, "firm not proven", sum(noproof.values()), sorted(noproof.items())[:40])
    return write_leads("on_fir_auditor", leads)


# ----------------------------------------------------------------------------------------------------------------
# 1b. First Nations FNFTA audited consolidated financial statements: auditor of record (address in the report itself)
FNP = "https://fnp-ppn.aadnc-aandc.gc.ca/fnp/Main/Search/"
FN_PDF = FNP + "DisplayBinaryData.aspx?BAND_NUMBER_FF={band}&FY={fy}&DOC=Audited%20consolidated%20financial%20statements&lang=eng"
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DATE_RX = re.compile(r"\b(%s)\s+(\d{1,2}),?\s+(20\d\d)\b" % MONTHS)
FIRMISH = re.compile(r"\bLLP\b|L\.L\.P|Professional Corporation|Prof(?:essional)? Corp|Chartered|\bCPA|Accounting|"
                     r"Accountants|& Associates|Partners|\bInc\b|\bLtd\b|Group", re.I)


def wikidata_sites(prop_value_query):
    """{key: website} from one SPARQL query returning ?k ?site."""
    st, body, _, _ = get("https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(prop_value_query),
                         check_robots=False, headers={"Accept": "application/sparql-results+json"})
    out = {}
    if st == 200:
        for b in json.loads(body)["results"]["bindings"]:
            out.setdefault(b["k"]["value"], b["site"]["value"])
    return out


def fn_bands():
    """Band numbers and names. canadaspends.com lists every FNFTA First Nation (used ONLY to enumerate; evidence is ISC)."""
    st, body, _, _ = get("https://canadaspends.com/en/first-nations")
    bands = {}
    if st == 200:
        for num, name in re.findall(r'href="/en/first-nations/ISC_(\d+)"[^>]*>([^<]+)</a>', body.decode("utf-8", "replace")):
            bands[int(num)] = html.unescape(name).strip()
    if len(bands) < 400:
        log("band list from canadaspends:", st, len(bands), "-> probing 1..800")
        for i in range(1, 801):
            bands.setdefault(i, "")
    return bands


def _segs(line):
    return [(m.start(), m.group(0).strip()) for m in re.finditer(r"\S(?:.*?\S)?(?=\s{3,}|$)", line)]


FIRM_LINE = re.compile(r"\bLLP\b|L\.L\.P|Professional Corporation|Prof(?:essional)?\.? Corp|\bCPA|Accounting|"
                       r"Accountants?\b|& Associates|& Company|Partners\b", re.I)


def fn_parse(txt, fy_end_year):
    """(firm, address, report date, quote) from the independent auditor's report; None when not all three are found."""
    lines = txt.splitlines()
    low = txt.lower()
    m0 = re.search(r"independent auditors?['’]?s?['’]? report|auditors?['’]?s?['’]? report|report of the independent", low)
    if not m0:
        return None
    start = txt.count("\n", 0, m0.start())
    lo, hi = max(0, start - 60), min(len(lines), start + 260)
    flat = re.sub(r"\s+", " ", txt[: m0.start() + 30000])
    firm = ""
    for rx in (r"([A-Z][A-Za-z0-9&'’.,\- ]{2,80}?)\s+(?:is|was|were|are|has been|have been)\s+(?:appointed|engaged|retained)\s+by",
               r"external auditors?,\s+([A-Z][A-Za-z0-9&'’.\- ]{2,70}?),\s+(?:conduct|have|has|is|are|were|was)",
               r"([A-Z][A-Za-z0-9&'’.,\- ]{2,70}?(?:LLP|Professional Corporation|CPA Inc\.?|Chartered Professional Accountants)),?\s+"
               r"(?:the )?(?:independent|external) auditors?"):
        m = re.search(rx, flat)
        if m:
            firm = re.split(r"[.:;]\s+(?=[A-Z])", m.group(1).strip(" ,"))[-1].strip(" ,.")
            firm = re.sub(r"^(?:The\s+)?(?:external auditors?,?\s*)", "", firm, flags=re.I).strip()
            if firm.lower() in ("the auditor", "the auditors", "auditors", "the external auditors", "external auditors",
                                "the independent auditors", "independent auditors"):
                firm = ""
            if firm:
                break
    segs = {j: _segs(lines[j]) for j in range(lo, hi)}
    addrs = []
    for j in range(lo, hi):
        for c, sg in segs[j]:
            if not re.search(POSTAL, sg):
                continue
            addr = sg
            if not re.search(PROV + r"\b", sg):
                prev = [s2 for jj in (j - 1, j - 2) if jj in segs for c2, s2 in segs[jj] if abs(c2 - c) < 30 and re.search(PROV + r"\b", s2)]
                if not prev:
                    continue
                addr = prev[0] + ", " + sg
            street = [s2 for jj in (j - 1, j - 2) if jj in segs for c2, s2 in segs[jj] if abs(c2 - c) < 30 and
                      re.match(r"(?:Suite|Unit|PO|P\.O\.|Box|\d)", s2) and s2 not in addr]
            if street and not re.match(r"(?:Suite|Unit|PO|P\.O\.|Box|\d)", addr):
                addr = street[0] + ", " + addr
            near = [s2 for jj in range(j - 5, j + 2) if jj in segs for c2, s2 in segs[jj]
                    if abs(c2 - c) < 40 and FIRM_LINE.search(s2) and not re.search(POSTAL, s2) and len(s2) < 90
                    and not re.search(r"^Chartered Professional Accountants|^Licensed Public|Tel|Fax|Phone|www\.|@", s2)]
            addrs.append((j, re.sub(r"\s+", " ", addr).strip(), near))
    if not addrs:
        return None
    pick = None
    for j, addr, near in addrs:
        if firm and any(firm.lower()[:12] in n.lower() for n in near):
            pick = (firm, addr)
            break
    if not pick:
        for j, addr, near in addrs:
            if near:
                pick = (firm if firm and firm.lower()[:10] in " ".join(near).lower() else near[0], addr)
                break
    if not pick and firm:
        pick = (firm, addrs[0][1])
    if not pick:
        return None
    firm_name, addr = re.sub(r"\s+", " ", pick[0]).strip(" ,."), pick[1]
    firm_name = re.sub(r",?\s*Chartered Professional Accountants.*$", "", firm_name).strip(" ,") or firm_name
    firm_name = re.sub(r"^(.*?\bLLP)\b.*$", r"\1", firm_name)
    dates = []
    for l in lines[lo:hi]:
        for m in DATE_RX.finditer(l):
            pre = l[: m.start()].lower()[-25:]
            if re.search(r"as at|ended|year|end of|march 31|for the|to |from ", pre):
                continue
            try:
                d = dt.datetime.strptime("%s %s %s" % m.groups(), "%B %d %Y").date()
            except ValueError:
                continue
            if fy_end_year <= d.year <= fy_end_year + 1 and not (d.month == 3 and d.day == 31) and d.isoformat() <= TODAY:
                dates.append((d, l.strip()))
    if not dates:
        return None
    d, dline = max(dates)
    return firm_name, addr, d.isoformat(), quote("%s, %s ... %s" % (firm_name, addr, re.sub(r"\s{2,}", " | ", dline)))


def cmd_fnfta(a):
    bands = fn_bands()
    lo, hi = (int(x) for x in a.bands.split("-")) if a.bands else (0, 10 ** 6)
    nums = sorted(b for b in bands if lo <= b <= hi)
    sites = wikidata_sites('SELECT ?k ?site WHERE { ?i wdt:P2865 ?k; wdt:P856 ?site. ?i wdt:P31 wd:Q2882257. }')
    log("FNFTA", len(nums), "bands;", len(sites), "Wikidata websites by band number")
    leads, stats = [], {"pdf": 0, "no_doc": 0, "no_text": 0, "unparsed": 0, "old_date": 0, "blocked": 0}
    unparsed = []
    for b in nums:
        got = None
        for fy, fy_end in (("2025-2026", 2026), ("2024-2025", 2025)):
            if fy == "2024-2025" and not a.late:
                continue
            url = FN_PDF.format(band=b, fy=fy)
            st, body, final, ct = get(url, check_robots=False)   # robots.txt: no /fnp rule (checked once below)
            if st == "blocked":
                stats["blocked"] += 1
                break
            if st != 200 or len(body) < 5000 or not body.startswith(b"%PDF") or "ainc-inac" in final:
                continue
            stats["pdf"] += 1
            txt = pdf_text(body[:40_000_000])
            if len(txt.strip()) < 500:
                stats["no_text"] += 1
                continue
            p = fn_parse(txt, fy_end)
            if not p:
                stats["unparsed"] += 1
                unparsed.append((b, fy))
                continue
            if p[2] < WINDOW:
                stats["old_date"] += 1
                continue
            got = (fy, url, p, txt)
            break
        if not got:
            if not any(True for _ in []):
                stats["no_doc"] += 0
            continue
        fy, url, (firm, addr, rdate, q), txt = got
        title = bands.get(b) or re.sub(r"\s+", " ", txt.strip().splitlines()[0]).strip()
        web = site_url(sites.get(str(b), ""))
        leads.append({"platform": "fnfta_auditor", "domain": host_of(web) if web else "",
                      "dataset_id": "FNFTA-%s-%s" % (b, fy),
                      "dataset": "First Nations Financial Transparency Act: audited consolidated financial statements "
                                 "FY%s (Indigenous Services Canada), independent auditor's report" % fy,
                      "dataset_url": url, "publisher": title, "buyer_unit": "", "website": web, "vendor": firm,
                      "canada_field": "auditor of record (FNFTA audited statements FY%s, ISC)" % fy,
                      "canada_value": quote("%s, %s" % (firm, addr)),
                      "row": {"band_number": b, "fiscal_year": fy, "auditor_firm": firm, "auditor_address": addr,
                              "report_date": rdate, "record_date": rdate, "evidence_quote": q,
                              "fnp_profile": FNP + "FNMain.aspx?BAND_NUMBER=%d&lang=eng" % b,
                              "website_source": "Wikidata P856 (band number P2865 = %d)" % b if web else ""}})
        if len(leads) % 25 == 0:
            log("FNFTA", b, "leads", len(leads), stats)
    log("FNFTA done", stats, "unparsed sample", unparsed[:20])
    return write_leads("fnfta_auditor", leads)


# ----------------------------------------------------------------------------------------------------------------
# 2. BC Financial Information Act: schedule of payments to suppliers -> supplier proven Canadian by an exact registry
#    match (BC OrgBook: entity type + home jurisdiction a Canadian province / federal). A separately labelled class.
BC_WD_QUERY = ('SELECT DISTINCT ?i ?iLabel ?site ?c WHERE { VALUES ?c {wd:Q60458065 wd:Q3327871 wd:Q60740115 '
               'wd:Q85796467 wd:Q3957 wd:Q532 wd:Q15284} ?i wdt:P31 ?c. { ?i wdt:P131 wd:Q1973 } UNION { ?i wdt:P131 ?rd. '
               '?rd wdt:P31 wd:Q85796467 } ?i wdt:P856 ?site. SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }')
BC_CLASS = {"Q60458065": "City of", "Q3327871": "District of", "Q60740115": "Resort Municipality of",
            "Q3957": "Town of", "Q532": "Village of", "Q15284": "Municipality of", "Q85796467": ""}
# Public bodies with a March 31 fiscal year (FY2025-26 SOFI). Names and sites as the bodies publish them.
BC_MARCH = [("University of British Columbia", "https://www.ubc.ca/"), ("Simon Fraser University", "https://www.sfu.ca/"),
            ("University of Victoria", "https://www.uvic.ca/"), ("University of Northern British Columbia", "https://www.unbc.ca/"),
            ("Thompson Rivers University", "https://www.tru.ca/"), ("Vancouver Island University", "https://www.viu.ca/"),
            ("Royal Roads University", "https://www.royalroads.ca/"), ("Capilano University", "https://www.capilanou.ca/"),
            ("Emily Carr University of Art + Design", "https://www.ecuad.ca/"), ("Kwantlen Polytechnic University", "https://www.kpu.ca/"),
            ("University of the Fraser Valley", "https://www.ufv.ca/"), ("British Columbia Institute of Technology", "https://www.bcit.ca/"),
            ("Camosun College", "https://camosun.ca/"), ("Douglas College", "https://www.douglascollege.ca/"),
            ("Langara College", "https://langara.ca/"), ("Okanagan College", "https://www.okanagancollege.ca/"),
            ("Selkirk College", "https://selkirk.ca/"), ("College of New Caledonia", "https://cnc.bc.ca/"),
            ("Coast Mountain College", "https://www.coastmountaincollege.ca/"), ("College of the Rockies", "https://cotr.bc.ca/"),
            ("North Island College", "https://www.nic.bc.ca/"), ("Northern Lights College", "https://www.nlc.bc.ca/"),
            ("Nicola Valley Institute of Technology", "https://www.nvit.ca/"), ("Justice Institute of British Columbia", "https://www.jibc.ca/"),
            ("Vancouver Community College", "https://www.vcc.ca/"), ("Fraser Health Authority", "https://www.fraserhealth.ca/"),
            ("Vancouver Coastal Health Authority", "https://www.vch.ca/"), ("Interior Health Authority", "https://www.interiorhealth.ca/"),
            ("Vancouver Island Health Authority", "https://www.islandhealth.ca/"), ("Northern Health Authority", "https://www.northernhealth.ca/"),
            ("Provincial Health Services Authority", "https://www.phsa.ca/"), ("First Nations Health Authority", "https://www.fnha.ca/")]
SOFI_LINK = re.compile(r"sofi|statement[-_ %20]*of[-_ %20]*financial[-_ %20]*information|financial[-_ %20]*information[-_ %20]*"
                       r"(?:act|return|report)|schedule[-_ %20]*of[-_ %20]*(?:payments|remuneration)|\bfia\b|fia[-_ ]report", re.I)
NAV_LINK = re.compile(r"financ|report|sofi|statement|transparen|accountab|budget|publication|corporate|governance|"
                      r"city-hall|town-hall|municipal-hall|about|administration|disclosure|documents|freedom-of-information", re.I)
CORP_SUFFIX = re.compile(r"\b(LTD|LIMITED|INC|INCORPORATED|CORP|CORPORATION|ULC|LLP|COMPANY|CO|LTEE|LTÉE)\.?\s*$", re.I)
CA_JUR = {"BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL", "YT", "NT", "NU", "CA", "FD", "CANADA", "FEDERAL"}
ENTITY_TYPES = {"A": "Extraprovincial company", "BC": "BC company", "ULC": "BC unlimited liability company",
                "CC": "BC community contribution company", "BEN": "BC benefit company", "C": "Continued-in company",
                "CP": "Cooperative", "LLP": "Limited liability partnership", "XL": "Extraprovincial LLP",
                "LP": "Limited partnership", "XP": "Extraprovincial limited partnership", "S": "Society",
                "XS": "Extraprovincial society", "CUL": "Continued-in ULC"}


def norm_co(s):
    s = (s or "").upper().replace("&", " AND ").replace("’", "'")
    s = re.sub(r"[^A-Z0-9 ]", " ", s)
    rep = {"LIMITED": "LTD", "INCORPORATED": "INC", "CORPORATION": "CORP", "COMPANY": "CO", "LTEE": "LTD", "LIMITEE": "LTD"}
    return " ".join(rep.get(w, w) for w in s.split())


def _nav_score(path, txt):
    b = (path + " " + txt).lower()
    if SOFI_LINK.search(b):
        return 0
    if re.search(r"financ|annual-report|annual report|financial-statement|statement", b):
        return 1
    if re.search(r"budget|report|transparen|accountab|disclosure|freedom|publication|documents", b):
        return 2
    return 3 if NAV_LINK.search(b) else 9


def find_sofi(site, march, max_pages=22, link_rx=None):
    """PDF links that look like the body's SOFI for the right fiscal year: [(url, anchor)]. Best-first, <= 22 pages."""
    want = re.compile(r"2025[-_ /]?(?:20)?26|fy[-_ ]?2026|2026|25[-_]26" if march else r"2025", re.I)
    avoid = None if march else re.compile(r"2025[-_ /]?(?:20)?26|2024[-_ /]?(?:20)?25", re.I)
    import heapq
    heap, seen, hits, n = [(0, 0, site, 0)], set(), [], 0
    while heap and len(seen) < max_pages:
        _, _, u, d = heapq.heappop(heap)
        if u in seen:
            continue
        seen.add(u)
        st, body, final, ct = get(u, limit=4_000_000)
        if st != 200 or "html" not in ct:
            continue
        page = body.decode("utf-8", "replace")
        for href, inner in re.findall(r'<a\s[^>]*?href="([^"#]+)"[^>]*>(.*?)</a>', page, re.S | re.I):
            a = urllib.parse.urljoin(final, html.unescape(href)).split("#")[0]
            txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", inner))).strip()
            blob = urllib.parse.unquote(a) + " " + txt
            same = host_of(a).split(".")[-2:] == host_of(site).split(".")[-2:]
            filelike = re.search(r"\.pdf(\?|$)|documentcenter/view|/download|/files/|/media/|/sites/default/|/assets/|"
                                 r"/uploads/|/docs?/|getmedia|/file/", a, re.I)
            if (link_rx or SOFI_LINK).search(blob) and filelike:
                yblob = urllib.parse.unquote(a.split("?")[0].rstrip("/").rsplit("/", 1)[-1]) + " " + txt   # not the upload path
                if want.search(yblob) and not (avoid and avoid.search(yblob)):
                    hits.append((a, txt))
                continue
            if same and d < 3 and not re.search(r"\.(pdf|jpe?g|png|docx?|xlsx?|zip|mp4)(\?|$)", a, re.I) and a not in seen:
                sc = _nav_score(urllib.parse.urlparse(a).path, txt)
                if sc < 9:
                    n += 1
                    heapq.heappush(heap, (sc, n, a, d + 1))
        if hits:
            break
    return hits


def sofi_suppliers(txt):
    """(name, amount) lines of the schedule of payments to suppliers of goods and services."""
    low = txt.lower()
    m = re.search(r"(suppliers? of goods and services|payments? (?:made )?to suppliers|schedule of (?:payments|"
                  r"expenditures) (?:to|for) (?:suppliers|goods)|goods and services|statement of payments)", low)
    if not m:
        return []
    out = []
    for l in txt[m.start():].splitlines():
        mm = re.match(r"^\s*([A-Z0-9][A-Za-z0-9&'’.,()/\- ]{2,80}?[A-Za-z.)])\s{2,}\$?\s?(\d{1,3}(?:,\d{3})+(?:\.\d{2})?)\s*$", l)
        if mm:
            out.append((re.sub(r"\s+", " ", mm.group(1)).strip(), float(mm.group(2).replace(",", ""))))
    return out


def orgbook_exact(name):
    """Exact-name active OrgBook registration with a Canadian home jurisdiction, or None."""
    url = "https://orgbook.gov.bc.ca/api/v4/search/topic?q=%s&inactive=false&revoked=false&page_size=10" % \
          urllib.parse.quote(name)
    st, body, _, _ = get(url, check_robots=False)   # the documented public API; see notes in the report
    if st != 200:
        return None
    try:
        res = json.loads(body).get("results", [])
    except ValueError:
        return None
    k = norm_co(name)
    for r in res:
        names = [n["text"] for n in r.get("names", []) if n.get("type") == "entity_name"]
        if not any(norm_co(n) == k for n in names):
            continue
        at = {x["type"]: x["value"] for x in r.get("attributes", [])}
        if at.get("entity_status") not in ("ACT", "Active"):
            continue
        et, hj = at.get("entity_type", ""), (at.get("home_jurisdiction") or "").upper()
        if et in ("SP", "GP") or (hj and hj not in CA_JUR) or (et == "A" and not hj):
            continue
        if not hj:
            hj = "BC"
        bn = [n["text"] for n in r.get("names", []) if n.get("type") == "business_number"]
        return {"registry": "OrgBook BC", "registration": r["source_id"], "legal_name": names[0], "entity_type": et,
                "entity_type_label": ENTITY_TYPES.get(et, et), "home_jurisdiction": hj, "status": "Active",
                "business_number": bn[0] if bn else "", "registry_url": "https://orgbook.gov.bc.ca/entity/%s" % r["source_id"],
                "api_url": url, "registration_date": (at.get("registration_date") or "")[:10]}
    return None


_site_proofs, _sp_lock, _cb_last = {}, threading.Lock(), [0.0]
CB_LEGAL = re.compile(r"\b(inc|incorporated|ltd|limited|ltee|ltée|corp|corporation|co|company|llc|lp|llp|ulc|the|group|holdings?|canada)\b\.?", re.I)


def site_proof(name):
    """The supplier's own website (Clearbit's name autocomplete, exact name once legal suffixes are ignored) and the
    Canadian street address printed on it: a match dict like orgbook_exact's, or None. Cached per name."""
    k = norm_co(name)
    with _sp_lock:
        if k in _site_proofs:
            return _site_proofs[k]
    res = None
    short = re.sub(r"\s+", " ", CB_LEGAL.sub(" ", name)).strip(" ,.")
    with _sp_lock:
        wait = _cb_last[0] + 1.0 - time.time()
        if wait > 0:
            time.sleep(wait)
        _cb_last[0] = time.time()
    try:
        req = urllib.request.Request("https://autocomplete.clearbit.com/v1/companies/suggest?query=" + urllib.parse.quote(short[:80]),
                                     headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as r:
            sugg = json.loads(r.read().decode("utf-8", "replace"))
    except Exception:
        sugg = []
    want = norm_co(short)
    for sg in sugg[:5]:
        dom = (sg.get("domain") or "").lower().strip()
        if not dom or norm_co(CB_LEGAL.sub(" ", sg.get("name") or "")) != want or dom in GENERIC_MAIL:
            continue
        q, u = canada_address_on_site("https://%s/" % dom)
        if q:
            res = {"registry": "the supplier's own website", "registration": dom, "legal_name": name.strip(), "entity_type": "",
                   "entity_type_label": "address on its own site", "home_jurisdiction": "CA", "status": "", "business_number": "",
                   "registry_url": u, "api_url": "", "registration_date": "", "site_quote": q}
            break
    with _sp_lock:
        _site_proofs[k] = res
    return res


PROOF = "orgbook"


def bc_bodies():
    out = []
    st, body, _, _ = get("https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(BC_WD_QUERY),
                         check_robots=False, headers={"Accept": "application/sparql-results+json"})
    items = {}
    if st == 200:
        for b in json.loads(body)["results"]["bindings"]:
            it = items.setdefault(b["i"]["value"], {"label": b["iLabel"]["value"], "site": b["site"]["value"], "c": set()})
            it["c"].add(b["c"]["value"].rsplit("/", 1)[-1])
    for q, it in items.items():
        lab = it["label"]
        pre = next((BC_CLASS[c] for c in ("Q85796467", "Q60458065", "Q3327871", "Q60740115", "Q3957", "Q532", "Q15284")
                    if c in it["c"]), "")
        name = lab if (not pre or lab.lower().startswith(("city of", "district of", "town of", "village of",
                                                          "regional district", "municipality of", "resort municipality"))) \
            else "%s %s" % (pre, lab)
        out.append({"name": name, "site": site_url(it["site"]), "march": False, "wikidata": q})
    for n, s in BC_MARCH:
        out.append({"name": n, "site": s, "march": True, "wikidata": ""})
    return [b for b in out if b["site"]]


def bc_one(b, max_queries=14, want=3):
    hits = find_sofi(b["site"], b["march"])
    if not hits:
        return b, None, [], "no_sofi_link"
    for url, anchor in hits[:3]:
        st, body, final, ct = get(url, limit=80_000_000)
        if st != 200 or not body.startswith(b"%PDF"):
            continue
        txt = pdf_text(body)
        sup = sofi_suppliers(txt)
        if not sup:
            continue
        cands = sorted({(n, v) for n, v in sup if CORP_SUFFIX.search(n) and len(n) < 60}, key=lambda x: -x[1])
        matches, tried = [], 0
        for n, v in cands:
            if tried >= max_queries or len(matches) >= want:
                break
            tried += 1
            m = site_proof(n) if PROOF == "site" else orgbook_exact(n)
            if m:
                line = next((l for l in txt.splitlines() if n in re.sub(r"\s+", " ", l)), n)
                matches.append((n, v, m, quote(re.sub(r"\s{2,}", " ", line.strip()))))
        return b, (final, anchor, len(sup)), matches, "ok" if matches else "no_registry_match"
    return b, None, [], "no_supplier_schedule"


def cmd_bcsofi(a):
    from concurrent.futures import ThreadPoolExecutor
    bodies = bc_bodies()
    log("BC SOFI:", len(bodies), "bodies with a website")
    leads, stats = [], {}
    with ThreadPoolExecutor(a.workers) as ex:
        for b, doc, matches, status in ex.map(bc_one, bodies):
            stats[status] = stats.get(status, 0) + 1
            if not matches:
                continue
            fy = "FY2025-26 (April 1, 2025 - March 31, 2026)" if b["march"] else "FY2025 (January 1 - December 31, 2025)"
            rdate = "2026-03-31" if b["march"] else "2025-12-31"
            for n, v, m, q in matches:
                web = b["site"]
                leads.append({"platform": "bc_sofi_registry", "domain": host_of(web), "dataset_id": "BCSOFI-%s-%s" % (
                    host_of(web), m["registration"]),
                    "dataset": "BC Financial Information Act, Statement of Financial Information %s: schedule of payments "
                               "to suppliers of goods and services" % fy,
                    "dataset_url": doc[0], "publisher": b["name"], "buyer_unit": "", "website": web,
                    "vendor": m["legal_name"],
                    "canada_field": ("supplier's own site address (%s SOFI %s schedule of payments)" if m.get("site_quote") else
                                     "registry match: %s (%s SOFI %s schedule of payments)") % tuple(([] if m.get("site_quote") else [m["registry"]]) +
                                                                                                   [b["name"], "FY2025-26" if b["march"] else "FY2025"]),
                    "canada_value": m["site_quote"] if m.get("site_quote") else "%s %s: %s, %s, home jurisdiction %s, status Active%s" % (
                        m["registry"], m["registration"], m["legal_name"], m["entity_type_label"], m["home_jurisdiction"],
                        (", BN " + m["business_number"]) if m["business_number"] else ""),
                    "row": {"supplier_as_printed": n, "amount": v, "fiscal_year": fy, "record_date": rdate,
                            "evidence_quote": q, "sofi_link_text": doc[1], "suppliers_listed": doc[2],
                            "registry_url": m["registry_url"], "registry_api_url": m["api_url"],
                            "registry_entity_type": m["entity_type"], "registry_home_jurisdiction": m["home_jurisdiction"],
                            "registry_registration_date": m["registration_date"],
                            "match_rule": "exact legal name (case, punctuation, Ltd/Limited, Inc/Incorporated, "
                                          "Corp/Corporation, & / and normalised), active, Canadian home jurisdiction"}})
            log("BC", b["name"], len(matches), "matches;", stats)
    log("BC SOFI done", stats)
    return write_leads("bc_sofi_registry", leads)


# ----------------------------------------------------------------------------------------------------------------
# 3. Canada-HQ publishers' institutional agreements; 4. ACI World (Montreal) dated airport programme
def wikidata_by_label(labels, extra=""):
    """{label: website} for exact English labels (one SPARQL query per 80 labels)."""
    out = {}
    labels = sorted(set(l for l in labels if l and '"' not in l))
    for i in range(0, len(labels), 80):
        vals = " ".join('"%s"@en' % l.replace("\\", "") for l in labels[i:i + 80])
        q = 'SELECT ?k ?site WHERE { VALUES ?k {%s} ?i rdfs:label ?k; wdt:P856 ?site. %s }' % (vals, extra)
        st, body, _, _ = get("https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(q),
                             check_robots=False, headers={"Accept": "application/sparql-results+json"})
        if st == 200:
            for b in json.loads(body)["results"]["bindings"]:
                out.setdefault(b["k"]["value"], b["site"]["value"])
    return out


def _vendor_proof(url, rx):
    st, body, final, ct = get(url)
    if st != 200:
        return "", ""
    m = re.search(rx, text_of(body))
    return (quote(m.group(0)), final) if m else ("", "")


def cmd_pubs(a):
    leads = []
    # JMIR Publications (Toronto): "Institutional Publishing Agreements" table, institution + consortium + term.
    jq, ju = _vendor_proof("https://www.jmir.org/fees/institutional-partners",
                           r"JMIR Publications[^\n]{0,80}?130 Queens Quay East[^\n]{0,60}?Toronto[^\n]{0,30}?M5A ?0P6[^\n]{0,20}")
    if not jq:
        jq, ju = _vendor_proof("https://jmirpublications.com/contact",
                               r"[^\n]{0,60}130 Queens Quay East[^\n]{0,80}?M5A ?0P6[^\n]{0,20}")
    st, body, final, ct = get("https://www.jmir.org/fees/institutional-partners")
    rows = []
    if st == 200:
        page = body.decode("utf-8", "replace")
        tb = page[page.find('id="panel-agreements"'):]
        tb = tb[: tb.find("</table>")]
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", tb, re.S):
            tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
            if len(tds) < 4:
                continue
            cell = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip() for x in tds]
            link = re.search(r'href="(https?://[^"]+)"', tds[1])
            m = re.search(r"(20\d\d-\d\d-\d\d)\s*[–-]\s*(20\d\d-\d\d-\d\d)", cell[3])
            if not m:
                continue
            rows.append((cell[0], cell[1], cell[2], m.group(1), m.group(2), link.group(1) if link else "", cell))
    wd = wikidata_by_label([r[0] for r in rows])
    for name, policy, consortium, start, end, link, cell in rows:
        rdate = end if end >= WINDOW else (start if start >= WINDOW else "")
        if not rdate:
            continue
        web = site_url(link) if link and "jmir" not in link else site_url(wd.get(name, ""))
        leads.append({"platform": "pub_agreements", "domain": host_of(web) if web else "",
                      "dataset_id": "JMIR-IPA-" + hashlib.sha1(name.encode()).hexdigest()[:10],
                      "dataset": "JMIR Publications: Institutional Publishing Agreements table (institution, open access "
                                 "policy, consortium, term)", "dataset_url": final, "publisher": name, "buyer_unit": "",
                      "website": web, "vendor": "JMIR Publications Inc.",
                      "canada_field": "publisher's institutional agreement (JMIR Publications, Toronto)",
                      "canada_value": jq, "row": {"open_access_policy": policy, "consortium": consortium,
                                                  "term_start": start, "term_end": end, "record_date": rdate,
                                                  "evidence_quote": quote(" | ".join(cell)), "vendor_proof_url": ju,
                                                  "website_source": "policy link on the JMIR table" if link and "jmir" not in link
                                                  else ("Wikidata P856 (exact label)" if web else "")}})
    # Canadian Science Publishing (Ottawa) x CAUL: participating institutions, page dated "last updated on <date>".
    cq, cu = _vendor_proof("https://www.cdnsciencepub.com/contact", r"[^\n]{0,80}Ottawa[^\n]{0,40}K\d[A-Z] ?\d[A-Z]\d")
    st, body, final, ct = get("https://caul.libguides.com/read-and-publish/canadian-science-publishing")
    if st == 200:
        t = text_of(body)
        upd = re.search(r"last updated on (\d{1,2} \w+ 20\d\d)", t)
        start = re.search(r"Starting (\w+ \d{1,2}, 20\d\d), Canadian Science Publishing", t)
        blk = re.search(r"The following institutions participate in this agreement:(.*?)Authors who do not see", t, re.S)
        if upd and blk:
            udate = dt.datetime.strptime(upd.group(1), "%d %B %Y").date().isoformat()
            names = [re.sub(r"\s+", " ", x).strip() for x in blk.group(1).split("\n") if x.strip()]
            wd = wikidata_by_label(names)
            for n in names:
                web = site_url(wd.get(n, ""))
                leads.append({"platform": "pub_agreements", "domain": host_of(web) if web else "",
                              "dataset_id": "CSP-CAUL-" + hashlib.sha1(n.encode()).hexdigest()[:10],
                              "dataset": "CAUL: Open Access Agreements negotiated by CAUL, Canadian Science Publishing "
                                         "(participating institutions)", "dataset_url": final, "publisher": n,
                              "buyer_unit": "", "website": web, "vendor": "Canadian Science Publishing",
                              "canada_field": "publisher's institutional agreement (Canadian Science Publishing, Ottawa; CAUL)",
                              "canada_value": cq or "Canadian Science Publishing, Ottawa (publisher's own site blocked: "
                                                    "403); see row.vendor_proof_note",
                              "row": {"agreement_start": start.group(1) if start else "", "page_last_updated": udate,
                                      "record_date": udate, "evidence_quote": quote(
                                          "This page was last updated on %s. ... The following institutions participate in "
                                          "this agreement: ... %s" % (upd.group(1), n)),
                                      "vendor_proof_url": cu, "vendor_proof_note": "" if cq else
                                      "cdnsciencepub.com answers 403 to this crawler; Canada HQ not proven from the "
                                      "vendor's own site in this run",
                                      "website_source": "Wikidata P856 (exact label)" if web else ""}})
    leads = [l for l in leads if l["canada_value"] and not l["canada_value"].startswith("Canadian Science Publishing, Ottawa (")]
    return write_leads("pub_agreements", leads)


def cmd_aci(a):
    url = "https://aci.aero/programs-and-services/asq/asq-customer-experience-awards/"
    st, body, final, ct = get(url)
    if st != 200:
        log("ACI", st)
        return
    t = text_of(body)
    hq = re.search(r"1500-800 rue du Square Victoria\s*Montr[ée]al, Qu[ée]bec\s*H3C 0B4\s*Canada", t)
    hq_url = final
    if not hq:
        st2, b2, f2, _ = get("https://aci.aero/about-aci/contact-us/")
        hq = re.search(r"1500-800 rue du Square Victoria\s*Montr[ée]al, Qu[ée]bec\s*H3C 0B4\s*Canada", text_of(b2))
        hq_url = f2
    if not hq:
        log("ACI HQ address not found")
        return
    i0 = t.find("2025 ASQ CUSTOMER EXPERIENCE AWARD WINNERS")
    if i0 < 0:
        log("ACI: no 2025 winners block")
        return
    seg = t[i0:]
    cat, out = "", {}
    for l in seg.split("\n"):
        l = l.strip()
        m = re.match(r"^(.{3,90}?) \(([^()]{2,40}), ([^()]{2,40})\)$", l)
        if m:
            out.setdefault(m.group(1), (m.group(2), m.group(3), cat, l))
        elif l and len(l) < 80 and not re.search(r"\(", l):
            cat = (cat.split(" | ")[0] + " | " + l) if re.search(r"passengers|Under|Over|million", l, re.I) else l
    wd = wikidata_by_label(list(out), extra="?i wdt:P31/wdt:P279* wd:Q1248784.")
    leads = []
    for name, (city, country, cat, line) in out.items():
        web = site_url(wd.get(name, ""))
        leads.append({"platform": "aci_asq2025", "domain": host_of(web) if web else "",
                      "dataset_id": "ACI-ASQ2025-" + hashlib.sha1(name.encode()).hexdigest()[:10],
                      "dataset": "ACI World: 2025 ASQ Customer Experience Award winners (airports in the paid Airport "
                                 "Service Quality programme, survey year 2025)", "dataset_url": final,
                      "publisher": name, "buyer_unit": "", "website": web, "vendor": "Airports Council International (ACI World)",
                      "canada_field": "paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025)",
                      "canada_value": quote(hq.group(0)),
                      "row": {"city": city, "country": country, "award_category": cat, "survey_year": "2025",
                              "record_date": "2025-12-31", "evidence_quote": quote("2025 ASQ CUSTOMER EXPERIENCE AWARD "
                                                                                    "WINNERS ... " + line),
                              "vendor_proof_url": hq_url,
                              "website_source": "Wikidata P856 (exact label, instance of airport)" if web else ""}})
    return write_leads("aci_asq2025", leads)


# ----------------------------------------------------------------------------------------------------------------
def cmd_tasks(a):
    tasks = {}
    for f in a.lead_files:
        for line in open(f, encoding="utf-8", errors="replace"):
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if not (r.get("website") or "").startswith("http"):
                continue
            name = (r["publisher"] if not r.get("buyer_unit") else "%s - %s" % (r["publisher"], r["buyer_unit"])).strip()
            key = "lead:" + hashlib.sha1(("%s|%s" % (r["domain"], name.lower())).encode()).hexdigest()[:16]
            tasks.setdefault(key, (name, r["website"]))
    with open(a.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
                    "known_general_email", "known_procurement_email", "contracts_in_dataset"])
        for i, (k, (n, site)) in enumerate(sorted(tasks.items()), 1):
            w.writerow(["CL-SM-%05d" % i, "", k, n, "", "", site, "", "", 1])
    log(len(tasks), "buyers with a website ->", a.out)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("fir")
    p.add_argument("--years", default="2025,2024")
    p.add_argument("--refresh-firms", action="store_true")
    p = sp.add_parser("fnfta")
    p.add_argument("--bands", default="")
    p.add_argument("--late", action="store_true", help="also FY2024-25 reports dated on/after the window start")
    p = sp.add_parser("bcsofi")
    p.add_argument("--workers", type=int, default=12)
    p.add_argument("--proof", default="site", choices=["site", "orgbook"], help="vendor Canada proof: its own site's address (default) or OrgBook (robots-disallowed /api/)")
    sp.add_parser("pubs")
    sp.add_parser("aci")
    p = sp.add_parser("tasks")
    p.add_argument("out")
    p.add_argument("lead_files", nargs="+")
    a = ap.parse_args()
    if a.cmd == "bcsofi":
        globals()["PROOF"] = a.proof
    globals()["cmd_" + a.cmd](a)


if __name__ == "__main__":
    main()
