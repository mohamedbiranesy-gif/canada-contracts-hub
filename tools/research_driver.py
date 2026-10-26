#!/usr/bin/env python3
"""Deterministic research driver: Gemini (with Google Search grounding) proposes, this script verifies.

For each open task of a lane it asks Gemini one grounded question, then fetches the cited pages itself and keeps a value
only if it is literally on a page of the organisation (or its parent / central body). Rows are written in the exact
docs/RETURN_FORMATS.md format, one file per batch, as the run goes (a crash loses nothing).

Usage: GEMINI_API_KEY=... python3 tools/research_driver.py --lane gemini [--max 60] [--minutes 45]
       [--models gemini-x-flash,gemini-y-flash] [--rpm 8] [--kinds verify_buyer_ap,buyer_ap,vendor_contacts]
Exit code 0 always (the workflow decides from the counts it prints); quota exhaustion stops the run cleanly.
"""
import argparse, csv, datetime, glob, hashlib, html, json, os, re, subprocess, sys, time, unicodedata
import urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_returns import FORMATS, PERSONAL, ROLE_HINT, EMAIL  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--lane", required=True)
ap.add_argument("--max", type=int, default=60)
ap.add_argument("--minutes", type=float, default=45)
ap.add_argument("--models", default=os.environ.get("MODELS", ""))
ap.add_argument("--rpm", type=float, default=float(os.environ.get("GEMINI_RPM", "8")))
ap.add_argument("--kinds", default="verify_buyer_ap,buyer_ap,vendor_contacts")
args = ap.parse_args()
KEY = os.environ.get("GEMINI_API_KEY", "")
MODELS = [m for m in args.models.split(",") if m] or ["gemini-flash-latest"]
T0, TODAY = time.time(), datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
UA = {"User-Agent": "Mozilla/5.0 (compatible; contracts-research/1.0; evidence verification; polite)"}
CACHE = "work/evidence_cache"
os.makedirs(CACHE, exist_ok=True)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,24}")
AP_WORDS = re.compile(r"factur|invoice|payab|payable|comptes?[._-]?a?[._-]?payer|compta|^ap[._-]|^ap$|accounts|paiement|payment|"
                      r"fournisseur|supplier|vendor|achat|procure|purchas|approvision|finance", re.I)
TWO_LEVEL = {"qc.ca", "on.ca", "gc.ca", "bc.ca", "ab.ca", "mb.ca", "sk.ca", "ns.ca", "nb.ca", "nl.ca", "pe.ca", "nt.ca", "nu.ca", "yk.ca",
             "co.uk", "gov.uk", "ac.uk", "org.uk", "com.au", "gov.au", "org.au", "edu.au", "gouv.fr", "gob.mx", "gov.br"}
stats = {"entities": 0, "rows": 0, "found": 0, "portal_only": 0, "not_published": 0, "blocked": 0, "unclear": 0,
         "website_only": 0, "not_found": 0, "gemini_calls": 0, "model_errors": 0}


def log(*a):
    print("[%5.1fm]" % ((time.time() - T0) / 60), *a, flush=True)


def reg_domain(u):
    h = (urllib.parse.urlparse(u if "//" in u else "//" + u).hostname or "").lower()
    h = h[4:] if h.startswith("www.") else h
    parts = h.split(".")
    if len(parts) >= 3 and ".".join(parts[-2:]) in TWO_LEVEL:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


# ---------- page fetching (cached, polite) ----------
_last_host = {}


def fetch(url):
    """Return (final_url, raw_text) or (None, None)."""
    if not url or not url.startswith("http"):
        return None, None
    p = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest())
    if os.path.exists(p + ".json"):
        d = json.load(open(p + ".json"))
        return d["final"], d["text"]
    host = urllib.parse.urlparse(url).hostname or ""
    wait = _last_host.get(host, 0) + 0.6 - time.time()
    if wait > 0:
        time.sleep(wait)
    _last_host[host] = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
            final, data, ctype = r.geturl(), r.read(4_000_000), r.headers.get("content-type", "")
    except Exception:
        return None, None
    if "pdf" in ctype.lower() or final.lower().split("?")[0].endswith(".pdf"):
        tmp = p + ".pdf"
        open(tmp, "wb").write(data)
        try:
            text = subprocess.run(["pdftotext", "-layout", tmp, "-"], capture_output=True, timeout=60).stdout.decode("utf-8", "replace")
        except Exception:
            text = ""
        os.remove(tmp)
    else:
        text = html.unescape(data.decode("utf-8", "replace"))
    text = text.replace("&#64;", "@").replace("[at]", "@").replace("(at)", "@").replace(" [@] ", "@")
    if re.search(r"cf-chl|challenge-platform|captcha|<title>just a moment|access denied", text[:5000], re.I):
        text = ""  # blocked page: treat as unavailable, never work around it
    json.dump({"final": final, "text": text}, open(p + ".json", "w"))
    return final, text


def visible(raw):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


def quote_around(raw, value):
    for t in (visible(raw), re.sub(r"\s+", " ", raw)):
        i = t.lower().find(value.lower())
        if i >= 0:
            a = max(0, i - 120)
            q = t[a:a + 290].strip()
            if value.lower() in q.lower():
                return q
    return ""


# ---------- Gemini ----------
_last_call = [0.0]


class QuotaExhausted(Exception):
    pass


def gemini(prompt):
    """Grounded generation. Returns (text, [source urls])."""
    for model in MODELS:
        for attempt in range(3):
            wait = _last_call[0] + 60.0 / args.rpm - time.time()
            if wait > 0:
                time.sleep(wait)
            _last_call[0] = time.time()
            body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}], "tools": [{"google_search": {}}],
                    "generationConfig": {"temperature": 0.2}}
            req = urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent" % model,
                                         data=json.dumps(body).encode(), headers={"x-goog-api-key": KEY, "Content-Type": "application/json"})
            stats["gemini_calls"] += 1
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    d = json.loads(r.read())
            except urllib.error.HTTPError as e:
                msg = e.read().decode("utf-8", "replace")[:400]
                stats["model_errors"] += 1
                if e.code == 429 and re.search(r"PerDay|per ?day|daily", msg, re.I):
                    if model == MODELS[-1]:
                        raise QuotaExhausted(msg)
                    log("model %s daily quota reached; switching model" % model)
                    break
                log("model %s HTTP %s (attempt %d): %s" % (model, e.code, attempt + 1, msg[:160].replace("\n", " ")))
                if e.code in (429, 500, 503, 504):
                    time.sleep(15 * (attempt + 1))
                    continue
                break  # other HTTP errors: try the next model
            except Exception as e:
                stats["model_errors"] += 1
                log("model %s error: %s" % (model, e))
                time.sleep(5)
                continue
            cand = (d.get("candidates") or [{}])[0]
            text = "".join(p.get("text", "") for p in (cand.get("content") or {}).get("parts") or [])
            urls = [c["web"].get("uri") for c in (cand.get("groundingMetadata") or {}).get("groundingChunks") or [] if c.get("web")]
            return text, [u for u in urls if u]
    return "", []


def parse_json(text):
    m = re.search(r"\{.*\}", text or "", re.S)
    if not m:
        return {}
    for t in (m.group(0), re.sub(r",\s*([}\]])", r"\1", m.group(0))):
        try:
            return json.loads(t)
        except Exception:
            pass
    return {}


# ---------- tasks and rows ----------
def done_ids():
    ids = set()
    for p in glob.glob("data/incoming/%s/*.csv" % args.lane):
        for r in csv.DictReader(open(p, encoding="utf-8-sig", newline="")):
            t = (r.get("task_id") or r.get("qa_id") or "").strip()
            if t:
                ids.add(t)
    return ids


def open_tasks():
    done = done_ids()
    for kind in [k for k in args.kinds.split(",") if k]:
        files = sorted(glob.glob("coord/tasks/%s/%s_%s_batch*.csv" % (args.lane, args.lane, kind)),
                       key=lambda p: int(re.search(r"batch(\d+)", p).group(1)))
        for p in files:
            n = re.search(r"batch(\d+)", p).group(1)
            out = "data/incoming/%s/%s_%s_results_batch%s.csv" % (args.lane, args.lane, kind, n)
            for r in csv.DictReader(open(p, encoding="utf-8-sig", newline="")):
                if r.get("task_id") and r["task_id"] not in done:
                    yield kind, r, out


def write_row(kind, out, row):
    cols = FORMATS["vendor_contact" if "vendor" in kind else "buyer_ap"].split(",")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    new = not os.path.exists(out) or os.path.getsize(out) == 0
    with open(out, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        if new:
            w.writeheader()
        w.writerow({c: ("" if row.get(c) is None else str(row.get(c))[:1000]) for c in cols})
    stats["rows"] += 1
    if row.get("status") in stats:
        stats[row["status"]] += 1


def role_ok(e):
    local = e.split("@")[0]
    return bool(EMAIL.match(e)) and not (PERSONAL.match(local) and not ROLE_HINT.search(local))


def ap_type(local):
    l = local.lower()
    if re.search(r"factur|invoice", l):
        return "invoice_submission"
    if re.search(r"payab|comptes|compta|^ap\b|^ap[._-]|accounts", l):
        return "accounts_payable"
    if re.search(r"paiement|payment|fournisseur|supplier|vendor", l):
        return "supplier_payment"
    if re.search(r"achat|procure|purchas|approvision", l):
        return "procurement"
    return "general"


RANK = {"invoice_submission": 0, "accounts_payable": 1, "supplier_payment": 2, "procurement": 3, "general": 4}


# ---------- buyers: accounts-payable / invoicing contact ----------
BUYER_PROMPT = """You are researching where suppliers must send invoices for this organisation.
Organisation: {name}
Other spellings: {other}
Country: {country}
Known website: {site}
Known general e-mail: {gen}
{hint}
Using Google Search, find on the organisation's own website or official documents (supplier or vendor guide, "doing business
with us", purchase-order terms and conditions, finance or accounts-payable page; in French: « Fournisseurs », « comptes à payer »,
« facturation », « conditions générales d'achat ») the e-mail address where suppliers send invoices or reach accounts payable,
or the online invoice-submission portal. If invoices go to a central or parent body (for example a CISSS/CIUSSS, a school service
centre, a ministry's central accounts payable, a city's finance department), give that body's published address and set
applies_to to parent_central_ap.
Rules: only addresses the organisation (or its parent) publishes itself; never a named person's mailbox; never invent or guess.
If nothing is published, say so. Reply with ONLY this JSON object:
{{"ap_email": "", "ap_email_type": "invoice_submission|accounts_payable|supplier_payment|procurement|general", "invoice_portal_url": "",
"ap_phone": "", "invoice_mailing_address": "", "invoicing_requirements_summary": "", "applies_to": "whole_organisation|this_unit_only|parent_central_ap",
"evidence_url": "", "evidence_quote": "", "status": "found|portal_only|not_published|unclear", "notes": ""}}"""


def research_buyer(kind, t, out):
    name = t.get("buyer_name") or t.get("org_group") or ""
    site = t.get("known_website") or ""
    hint = ""
    if kind.startswith("verify"):
        hint = "Another researcher reported: %s. Confirm it from the organisation's own page, or correct it." % (t.get("contracts_in_dataset") or "")
    prompt = BUYER_PROMPT.format(name=name, other=t.get("other_spellings") or "-", country=t.get("country") or "-", site=site or "-",
                                 gen=t.get("known_general_email") or "-", hint=hint)
    text, gurls = gemini(prompt)
    j = parse_json(text)
    org_dom = reg_domain(site) if site else ""
    pages = []
    for u in ([j.get("evidence_url")] if j.get("evidence_url") else []) + gurls[:6]:
        final, raw = fetch(u)
        if raw:
            pages.append((final, raw))

    def acceptable(page_url, em):
        pd, ed = reg_domain(page_url), reg_domain("http://" + em.split("@")[-1])
        return ed == pd or (org_dom and pd == org_dom)

    base = {"task_id": t["task_id"], "buyer_key": t.get("buyer_key"), "org_name_as_found": name, "retrieved_date": TODAY,
            "ap_phone": "", "applies_to": j.get("applies_to") if j.get("applies_to") in ("whole_organisation", "this_unit_only", "parent_central_ap") else "",
            "invoicing_requirements_summary": (j.get("invoicing_requirements_summary") or "")[:300],
            "queries_tried": "Gemini grounded search (%s); %d source pages checked" % (MODELS[0], len(pages))}
    email = (j.get("ap_email") or "").strip().strip(".").lower()
    if email and role_ok(email):
        for final, raw in pages:
            if email in raw.lower() and acceptable(final, email):
                q = quote_around(raw, email)
                if q:
                    typ = j.get("ap_email_type") if j.get("ap_email_type") in RANK else ap_type(email.split("@")[0])
                    write_row(kind, out, dict(base, ap_email=email, ap_email_type=typ, evidence_url=final, evidence_quote=q, status="found",
                                              invoice_portal_url=j.get("invoice_portal_url") or "", notes="verified on cited page"))
                    return
    best = None
    for final, raw in pages:
        for em in set(e.lower() for e in EMAIL_RE.findall(raw)):
            local = em.split("@")[0]
            if AP_WORDS.search(local) and role_ok(em) and acceptable(final, em):
                r = (RANK[ap_type(local)], em, final, raw)
                if best is None or r[0] < best[0]:
                    best = r
    if best:
        q = quote_around(best[3], best[1])
        if q:
            write_row(kind, out, dict(base, ap_email=best[1], ap_email_type=ap_type(best[1].split("@")[0]), evidence_url=best[2],
                                      evidence_quote=q, status="found", notes="role mailbox found on the organisation's page"))
            return
    portal = (j.get("invoice_portal_url") or "").strip()
    if portal.startswith("http"):
        for final, raw in pages:
            if portal.lower().rstrip("/") in raw.lower() and (not org_dom or reg_domain(final) == org_dom or reg_domain(final) == reg_domain(portal)):
                q = quote_around(raw, portal.rstrip("/"))
                write_row(kind, out, dict(base, invoice_portal_url=portal, evidence_url=final, evidence_quote=q, status="portal_only",
                                          notes="portal link found on the organisation's page"))
                return
    claimed = email or portal
    if claimed:
        status, note = "unclear", "unverified claim: %s (cited %s); not found on any fetched page of the organisation" % (claimed, j.get("evidence_url") or "-")
    elif j.get("status") == "not_published" or not pages:
        status, note = "not_published", (j.get("notes") or "")[:250]
    else:
        status, note = "not_published", (j.get("notes") or "no invoicing contact on the pages found")[:250]
    write_row(kind, out, dict(base, status=status, notes=note))


# ---------- vendors: official website and published contacts ----------
VENDOR_PROMPT = """Find the official website and the contact details published on it for this Canadian business.
Business name: {name}
Registered legal name: {legal}
Location: {city} {prov} {postal}
Registry id: {regid}
Domains already tried without success: {tried}
Using Google Search, find the business's own website (not a directory or a listing site). On that website, find the general contact
e-mail, the billing / accounts-receivable e-mail if one is published, the main phone number and the address shown.
Rules: only role mailboxes the business publishes (info@, sales@, ventes@, billing@, ar@, comptabilite@ ...); never a named
person's address; never guess. Reply with ONLY this JSON object:
{{"official_website": "", "contact_page_url": "", "general_email": "", "billing_or_ar_email": "", "main_phone": "", "address_on_site": "",
"business_number_if_published": "", "status": "found|website_only|not_found|ambiguous", "notes": ""}}"""
LEGAL = {"INC", "LTD", "LTEE", "LTÉE", "CORP", "CORPORATION", "CO", "CIE", "ENR", "SENC", "SENCRL", "LLP", "LP", "ULC", "LIMITED", "INCORPORATED",
         "COMPANY", "COMPAGNIE", "THE", "LE", "LA", "LES", "DE", "DU", "DES", "ET", "AND", "OF", "INTERNATIONAL", "CANADA", "GROUP", "GROUPE",
         "SERVICES", "SERVICE", "SOLUTIONS", "CONSTRUCTION", "TECHNOLOGIES", "SYSTEMS", "ENTERPRISES", "ENTREPRISES", "GESTION", "HOLDINGS"}


def fold(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().upper()


def research_vendor(kind, t, out):
    name, legal = t.get("vendor_name") or "", t.get("legal_name_in_registry") or ""
    city, prov, postal = t.get("city") or "", t.get("province") or "", (t.get("postal_code") or "").replace(" ", "").upper()
    prompt = VENDOR_PROMPT.format(name=name, legal=legal or "-", city=city, prov=prov, postal=postal, regid=t.get("registry_id") or "-",
                                  tried=t.get("domains_already_tried") or "-")
    text, gurls = gemini(prompt)
    j = parse_json(text)
    site = (j.get("official_website") or "").strip()
    base = {"task_id": t["task_id"], "vendor_key": t.get("vendor_key"), "retrieved_date": TODAY}
    if not site.startswith("http"):
        st = "ambiguous" if j.get("status") == "ambiguous" else "not_found"
        write_row(kind, out, dict(base, status=st, notes=("Gemini grounded search: " + (j.get("notes") or "no official website found"))[:250]))
        return
    dom = reg_domain(site)
    pages = []
    for u in [site, j.get("contact_page_url")] + [g for g in gurls[:6]]:
        if not u:
            continue
        final, raw = fetch(u)
        if raw and reg_domain(final) == dom:
            pages.append((final, raw))
    tokens = [w for w in re.split(r"[^A-Z0-9]+", fold(name + " " + legal)) if len(w) >= 3 and w not in LEGAL]
    proof = None
    for final, raw in pages:
        page = fold(visible(raw))
        tok = next((w for w in tokens if re.search(r"\b%s\b" % re.escape(w), page)), None)
        loc = None
        if postal and postal in page.replace(" ", ""):
            loc = "postal code " + postal
        elif city and re.search(r"\b%s\b" % re.escape(fold(city)), page):
            loc = "city " + fold(city)
        if tok and loc:
            proof = "name '%s' + %s on %s" % (tok, loc, final)
            break
    if not proof:
        write_row(kind, out, dict(base, status="ambiguous" if pages else "not_found", official_website="",
                                  notes=("candidate %s not confirmed (company name + location not both on its pages)" % site)[:250]))
        return
    found = {}
    for col in ("general_email", "billing_or_ar_email"):
        em = (j.get(col) or "").strip().lower()
        if em and role_ok(em) and reg_domain("http://" + em.split("@")[-1]) == dom:
            for final, raw in pages:
                if em in raw.lower():
                    q = quote_around(raw, em)
                    if q:
                        found[col] = (em, final, q)
                        break
    if not found:
        for final, raw in pages:
            for em in sorted(set(e.lower() for e in EMAIL_RE.findall(raw))):
                if role_ok(em) and reg_domain("http://" + em.split("@")[-1]) == dom and re.match(
                        r"(info|contact|hello|bonjour|sales|ventes|admin|office|bureau|reception|accueil|billing|facturation|ar|comptab|accounting)", em):
                    q = quote_around(raw, em)
                    if q:
                        found["billing_or_ar_email" if re.match(r"(billing|facturation|ar[._-]|comptab|accounting)", em) else "general_email"] = (em, final, q)
                        break
    phone = ""
    digits = re.sub(r"\D", "", j.get("main_phone") or "")[-10:]
    if len(digits) == 10 and any(digits in re.sub(r"\D", "", visible(raw)) for _, raw in pages):
        phone = j.get("main_phone")
    addr = j.get("address_on_site") or ""
    if addr and not any(fold(addr)[:12] in fold(visible(raw)) for _, raw in pages):
        addr = ""
    first = True
    for col, (em, final, q) in found.items():
        write_row(kind, out, dict(base, official_website=site if first else "", website_verification=proof if first else "",
                                  main_phone=phone if first else "", address_on_site=addr if first else "", **{col: em},
                                  evidence_url=final, evidence_quote=q, status="found", notes="verified on the company's own pages"))
        first = False
    if first:
        write_row(kind, out, dict(base, official_website=site, website_verification=proof, main_phone=phone, address_on_site=addr,
                                  evidence_url=pages[0][0], status="found" if phone else "website_only",
                                  notes="website confirmed; no role mailbox published on the pages checked"))


def main():
    if not KEY:
        log("GEMINI_API_KEY missing")
        return
    n = 0
    try:
        for kind, t, out in open_tasks():
            if n >= args.max or (time.time() - T0) / 60 > args.minutes:
                break
            n += 1
            stats["entities"] += 1
            try:
                (research_vendor if "vendor" in kind else research_buyer)(kind, t, out)
                log("%s %s -> %s" % (kind, t.get("task_id"), stats["rows"]))
            except QuotaExhausted:
                raise
            except Exception as e:
                log("task %s failed: %r" % (t.get("task_id"), e))
    except QuotaExhausted as e:
        log("daily quota exhausted; stopping cleanly:", str(e)[:200].replace("\n", " "))
    log("SUMMARY " + json.dumps(stats))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        open(os.environ["GITHUB_STEP_SUMMARY"], "a").write("research_driver lane %s: %s\n" % (args.lane, json.dumps(stats)))


if __name__ == "__main__":
    main()
