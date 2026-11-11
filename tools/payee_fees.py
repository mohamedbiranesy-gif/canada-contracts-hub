#!/usr/bin/env python3
"""The amount a body bills for ONE licence: from the body's own list of open invoices, or from its own fee schedule (2026-11-11).

Owner, 2026-11-11: a row carries "the amount that would be billed within that billing cadence … all the stuff that would be within an
invoice"; published first, a calculated value only labelled as calculated. A fee page says what a licence costs "from"; three cities
publish more than that, and this tool reads it with the project's reader (robots.txt, one request a second, identified):

  City of Toronto     every night, the list of its outstanding business-licence and permit invoices — licence number, invoice number,
                      amount due — and one page for each kind of licence with the sentence "The renewal fee is $…"
  The City of Calgary a fee schedule by licence type (base fee + fire fee for a renewal) and its rule for a licence of several types
  City of Edmonton    a tier for each business category, a fee for each tier, and its rule (the highest tier decides)

  python3 tools/payee_fees.py harvest     -> data/incoming/claude/payee_fees.json + payee_open_invoices.csv.gz (a source that fails keeps its last reading)
  python3 tools/payee_fees.py check FILE  -> what the amounts would be on the licence rows of a ranked table (nothing is written)

rank.py reaches it through payee_billing.fill(): amount(payee, row) returns the amount of that row with the line or the sentence it comes
from, or nothing. Nothing is estimated: a licence type that the schedule does not list under that name gets no amount; a licence of
several types gets the amount the schedule's own rule gives, in the column for calculated amounts.
"""
import collections, csv, gzip, html, io, json, os, re, subprocess, sys, time, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FEES = os.path.join(ROOT, "data/incoming/claude/payee_fees.json")
OPEN = os.path.join(ROOT, "data/incoming/claude/payee_open_invoices.csv.gz")
TORONTO_INVOICES = "https://www.toronto.ca/data/mls/invoices/index.html"
TORONTO_TYPES = "https://www.toronto.ca/services-payments/permits-licences-bylaws/find-licence-permit-types/"
CALGARY = "https://www.calgary.ca/content/dam/www/pda/pd/documents/fees/business-licence-fee-schedule.pdf"
EDMONTON = "https://www.edmonton.ca/sites/default/files/public-files/business-licence-fee-schedule-bylaw-20002.pdf"

norm = lambda s: re.sub(r"[^A-Z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().upper()).strip()
flat = lambda t: re.sub(r"\s+", " ", (t or "").replace("​", "")).strip()
_PAREN = re.compile(r"\([^()]*\)")
_STATUS = re.compile(r"\s*\((?:Renewal Licensed|Pending Renewal|Licensed|Renewal Invoiced|Renewal Notification Sent|Close in Progress|Move in Progress|Issued|Active|Pending|Invoiced|Inactive)\)\s*$", re.I)


def _title_kinds(x):
    """the kind(s) of licence a register row names: the part of its title after the dash, without the status the register adds in brackets"""
    t = (x.get("contract_title") or x.get("contract_description") or "")
    t = t.split(" (the record's title")[0]
    if " — " not in t:
        return "", ""
    kinds = t.split(" — ", 1)[1]
    st = _STATUS.search(kinds)
    return _STATUS.sub("", kinds).strip(), (st.group(0).strip(" ()") if st else "")


# ---- reading ---------------------------------------------------------------------------------------------------------------------------
def _get(url):
    import ap_crawler as C
    if not C.allowed(url):
        return None, "robots.txt does not allow the reader"
    st, ct, data, final = C.fetch(url)
    time.sleep(1.0)
    if st != 200 or not data:
        return None, "status %s" % st
    return (data, ct or ""), ""


def _pdf_raw(data):
    """pdftotext in reading order (the two-column lists of a schedule come out one entry a line); poppler's layout mode as the fallback"""
    try:
        r = subprocess.run(["pdftotext", "-raw", "-", "-"], input=data, capture_output=True, timeout=60)
        if r.stdout.strip():
            return r.stdout.decode("utf-8", "replace")
    except Exception:
        pass
    import ap_crawler as C
    return C.pdf_text(data) or ""


def harvest_toronto_invoices():
    import ap_crawler as C
    got, why = _get(TORONTO_INVOICES)
    if not got:
        return None, why
    text = flat(C.visible(C.quote_attrs(html.unescape(got[0].decode("utf-8", "replace")))))
    gen = re.search(r"generated on ([A-Z][a-z]+ \d{1,2}(?:st|nd|rd|th)?, \d{4})", text)
    rows = re.findall(r"\b([A-Z]\d{2}-\d{7}|[A-Z]\d{6})\s+([A-Z]{1,2}\d{5,6})\s+\$([\d,]+\.\d{2})(?=\s)", text)
    if not gen or len(rows) < 50:
        return None, "the list was not found on the page (%d lines)" % len(rows)
    return {"generated": gen.group(1), "rows": rows}, ""


def harvest_toronto_fees(limit=0):
    import ap_crawler as C
    got, why = _get(TORONTO_TYPES)
    if not got:
        return None, why
    raw = html.unescape(got[0].decode("utf-8", "replace"))
    links = collections.OrderedDict()
    for m in re.finditer(r'href="((?:https://www\.toronto\.ca)?/services-payments/permits-licen[cs]es-bylaws/[^"#?]+)"[^>]*>(.*?)</a>', raw, re.S):
        u, t = m.group(1), flat(re.sub(r"<[^>]+>", " ", m.group(2)))
        u = u if u.startswith("http") else "https://www.toronto.ca" + u
        if t and not t.startswith("{") and "/sidebar/" not in u and "find-licence-permit-types" not in u:
            links.setdefault(u, t)
    pages = []
    for u, t in list(links.items())[:limit or None]:
        got, why = _get(u)
        if not got:
            continue
        text = flat(C.visible(C.quote_attrs(html.unescape(got[0].decode("utf-8", "replace")))))
        fees = re.findall(r"(The renewal fee is \$[\d,]+(?:\.\d{2})?)", text)
        yearly = re.search(r"Your licen[cs]e will expire annually[^.]{0,120}\.", text)
        if fees:
            pages.append({"name": t, "url": u, "renewal": sorted(set(re.search(r"\$[\d,.]+\d", f).group(0) for f in fees)), "quote": fees[0], "yearly": yearly.group(0) if yearly else ""})
    if len(pages) < 10:
        return None, "only %d pages state a renewal fee" % len(pages)
    return {"index": TORONTO_TYPES, "pages": pages}, ""


def harvest_calgary():
    got, why = _get(CALGARY)
    if not got:
        return None, why
    import ap_crawler as C
    text = C.pdf_text(got[0]) or ""
    title = re.search(r"\d{4} Business Licence Fee Schedule[^\n]*", text)
    note = re.search(r"Note 3: Multiple licence types:.*?charged once\.", flat(text))
    money = r"(\$[\d,]+|--)"
    types = {}
    for line in text.splitlines():
        m = re.match(r"\s*(.+?)\s+" + r"\s+".join([money] * 10) + r"\s*$", flat(line))
        if not m:
            continue
        v = [int(g.replace("$", "").replace(",", "")) if g != "--" else 0 for g in m.groups()[1:]]
        if not m.group(11).startswith("$") or v[1] + v[3] + v[5] + v[7] != v[9]:
            continue  # no renewal total, or the columns do not add up to it: the line was not read as its ten columns
        types[norm(_PAREN.sub(" ", m.group(1)))] = {"name": m.group(1), "line": flat(line), "base": v[1], "fire": v[3], "other": v[5] + v[7], "total": v[9]}
    if len(types) < 40 or not title or not note:
        return None, "the schedule was not read (%d types)" % len(types)
    return {"url": CALGARY, "title": flat(title.group(0)), "rule": note.group(0), "types": types}, ""


def harvest_edmonton():
    got, why = _get(EDMONTON)
    if not got:
        return None, why
    text = _pdf_raw(got[0]).replace("​", "")
    tiers = {}
    for m in re.finditer(r"^\s*Tier (\d) \$([\d,]+) \$([\d,]+) \$([\d,]+) \$([\d,]+)\s*$", text, re.M):
        n = [int(g.replace(",", "")) for g in m.groups()[1:]]
        tiers[m.group(1)] = {"line": flat(m.group(0)), "fee1": n[0], "renew1": n[1], "fee2": n[2], "renew2": n[3]}
    rule = re.search(r"If multiple Business Categories apply,.*?section 13 of the Bylaw\.", flat(text))
    head = re.search(r"Category 1 Year Licence Fee 1 Year Renewal Fee\*? 2 Year Licence Fee 2 Year Renewal Fee\*?", flat(text))
    cats = {}
    body = text.split("BUSINESS CATEGORIES BY TIER", 1)[-1]
    for m in re.finditer(r"^\s*Tier (\d)\s*$(.*?)(?=^\s*Tier \d\s*$|^\s*No Charge\s*$|\Z)", body, re.M | re.S):
        for c in re.split(r"[○●•]", m.group(2)):
            c = flat(c)
            if c and len(c) < 90:
                cats[norm(c)] = {"name": c, "tier": m.group(1)}
    if len(tiers) < 5 or len(cats) < 40 or not rule or not head:
        return None, "the schedule was not read (%d tiers, %d categories)" % (len(tiers), len(cats))
    return {"url": EDMONTON, "tiers": tiers, "rule": rule.group(0), "head": head.group(0), "categories": cats}, ""


def harvest(a):
    try:
        old = json.load(open(FEES, encoding="utf-8"))
    except (OSError, ValueError):
        old = {}
    today = time.strftime("%Y-%m-%d", time.gmtime())
    out = dict(old)
    for key, fn in (("calgary", harvest_calgary), ("edmonton", harvest_edmonton), ("toronto", harvest_toronto_fees)):
        if key == "toronto" and old.get(key) and old[key].get("read", "") >= time.strftime("%Y-%m-%d", time.gmtime(time.time() - 6 * 86400)) and not a.all:
            print("%-9s kept (read %s; its pages are read again after a week)" % (key, old[key]["read"]))
            continue
        got, why = fn()
        if got:
            got["read"] = today
            out[key] = got
            print("%-9s read: %s" % (key, {k: (len(v) if isinstance(v, (list, dict)) else v) for k, v in got.items() if k in ("types", "categories", "tiers", "pages", "title")}))
        else:
            print("%-9s NOT read (%s): the last reading is kept (%s)" % (key, why, (old.get(key) or {}).get("read") or "none"))
    os.makedirs(os.path.dirname(FEES), exist_ok=True)
    json.dump(out, open(FEES, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    got, why = harvest_toronto_invoices()
    if got:
        buf = io.StringIO()
        w = csv.writer(buf, lineterminator="\n")
        w.writerow(["payee", "number", "invoice", "amount_due", "generated", "url", "read"])
        for num, inv, amt in got["rows"]:
            w.writerow(["City of Toronto", num, inv, "$" + amt, got["generated"], TORONTO_INVOICES, today])
        with gzip.GzipFile(OPEN, "wb", mtime=0) as fh:
            fh.write(buf.getvalue().encode("utf-8"))
        print("toronto   open invoices on the City's list generated %s: %d" % (got["generated"], len(got["rows"])))
    else:
        print("toronto   open invoices NOT read (%s): the last list is kept" % why)


# ---- the amount of one row -------------------------------------------------------------------------------------------------------------
_fees = _open = None


def _load():
    global _fees, _open
    if _fees is None:
        try:
            _fees = json.load(open(FEES, encoding="utf-8"))
        except (OSError, ValueError):
            _fees = {}
        _open = {}
        try:
            with gzip.open(OPEN, "rt", encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh):
                    _open.setdefault((norm(r["payee"]), r["number"].upper()), []).append(r)
        except (OSError, ValueError):
            pass
    return _fees, _open


def _split_types(kinds, known):
    """the licence types of a Calgary title: the register separates them with a comma, and some type names hold a comma themselves"""
    if "\n" in kinds:
        return [p.strip(" ,") for p in kinds.split("\n") if p.strip(" ,")]
    toks, out, i = [p.strip() for p in kinds.split(",")], [], 0
    while i < len(toks):
        for j in range(len(toks), i, -1):
            cand = ", ".join(toks[i:j])
            if norm(_PAREN.sub(" ", cand)) in known or j == i + 1:
                out.append(cand)
                i = j
                break
    return out


def _singular(s):
    return " ".join(w[:-1] if len(w) > 3 and w.endswith("S") and not w.endswith("SS") else w for w in s.split())


def amount(payee, x):
    """{'amount', 'basis', 'calculated', 'bill_number', 'delivery'} for one licence row of that payee, or None"""
    F, O = _load()
    p = norm(payee)
    kinds, status = _title_kinds(x)
    ref = (x.get("contract_reference") or "").strip().upper()
    if p == "CITY OF TORONTO":
        T = F.get("toronto") or {}
        for r in O.get((p, ref), [])[:1]:
            return {"amount": "%s due (open invoice %s)" % (r["amount_due"], r["invoice"]), "calculated": False, "bill_number": "invoice %s" % r["invoice"],
                    "basis": ("the City's own list of outstanding business licence and permit invoices, generated %s, has this licence number: “%s %s %s” (%s, read %s); "
                              "the amount is the one due on that day's list" % (r["generated"], r["number"], r["invoice"], r["amount_due"], r["url"], r["read"])),
                    "delivery": ("an invoice of the City, open on its list of outstanding licence invoices generated %s: “Find Your Outstanding Business Licence or Permit Invoice Amount” (%s, read %s)"
                                 % (r["generated"], r["url"], r["read"]))}
        k = _singular(norm(kinds))
        if not k:
            return None
        pages = T.get("pages") or []
        names = lambda g: {_singular(norm(g["name"])), _singular(norm(g["name"]).replace(" LICENCE", "").replace(" PERMIT", "")), _singular(norm(g["url"].rstrip("/").rsplit("/", 1)[-1]))}
        hit = [g for g in pages if k in names(g)]
        if not hit:
            hit = [g for g in pages if any((" " + k + " ") in (" " + n + " ") for n in names(g))]
        if len(hit) == 1 and len(hit[0]["renewal"]) == 1:
            g = hit[0]
            return {"amount": "%s a year" % g["renewal"][0], "calculated": False, "bill_number": "",
                    "basis": "the City's own page for this kind of licence (%s): “%s” (%s, read %s)" % (g["name"], g["quote"], g["url"], T.get("read") or "")}
        return None
    if p in ("THE CITY OF CALGARY", "CITY OF CALGARY"):
        S = F.get("calgary") or {}
        known = S.get("types") or {}
        parts = _split_types(kinds, known) if kinds else []
        got = [known.get(norm(_PAREN.sub(" ", t))) for t in parts]
        if not parts or not all(got):
            return None
        note = " The register's own status of this licence: “%s”." % status if status else ""
        if len(got) == 1:
            g = got[0]
            return {"amount": "$%d a year" % g["total"], "calculated": False, "bill_number": "",
                    "basis": ("the City's “%s”, the line of this licence type — base fee, fire fee, planning fee, building safety, total, each as new / renewal — the last amount is the "
                              "renewal total: “%s” (%s, read %s).%s" % (S.get("title") or "Business Licence Fee Schedule", g["line"], S["url"], S.get("read") or "", note))}
        if any(g["other"] for g in got):
            return None
        total = max(g["base"] for g in got) + max(g["fire"] for g in got)
        lines = "; ".join("“%s”" % g["line"] for g in got[:3])
        return {"amount": "$%d a year" % total, "calculated": True, "bill_number": "",
                "basis": ("calculated — the licence has %d types and the City's schedule says how they are charged: “%s”; so the highest renewal base fee ($%d) and the highest renewal fire fee ($%d) "
                          "of its lines, each once: %s%s (%s, read %s).%s"
                          % (len(got), S.get("rule") or "", max(g["base"] for g in got), max(g["fire"] for g in got), lines, " …" if len(got) > 3 else "", S["url"], S.get("read") or "", note))}
    if p in ("CITY OF EDMONTON", "THE CITY OF EDMONTON"):
        S = F.get("edmonton") or {}
        cats, tiers = S.get("categories") or {}, S.get("tiers") or {}
        parts = [c.strip() for c in re.split(r"[;\n]", kinds) if c.strip()] if kinds else []
        got = [cats.get(norm(c)) for c in parts]
        if not parts or not all(got):
            return None
        g = max(got, key=lambda c: c["tier"])
        t = tiers.get(g["tier"])
        if not t:
            return None
        many = len(got) > 1
        return {"amount": "$%d for one year, or $%d for two years" % (t["renew1"], t["renew2"]), "calculated": False, "bill_number": "",
                "basis": ("the City's fee schedule under its Business Licence Bylaw 20002: “%s” is a Tier %s category%s; the line of that tier under the heading “%s”: "
                          "“%s” (%s, read %s); the renewal fee applies when the licence is renewed on or before its expiry date"
                          % (g["name"], g["tier"], (" — the highest tier of this licence's %d categories, and “%s”" % (len(got), S.get("rule") or "")) if many else "", S.get("head") or "", t["line"], S["url"], S.get("read") or ""))}
    return None


def check(a):
    op = gzip.open if a.file.endswith(".gz") else open
    n, ex = collections.Counter(), collections.defaultdict(list)
    with op(a.file, "rt", encoding="utf-8", newline="") as fh:
        rows = (json.loads(l) for l in fh) if ".jsonl" in a.file else csv.DictReader(fh)
        for x in rows:
            v = norm(x.get("vendor"))
            if v not in ("CITY OF TORONTO", "THE CITY OF CALGARY", "CITY OF EDMONTON"):
                continue
            r = amount(x.get("vendor"), x)
            key = (x.get("vendor"), "open invoice" if r and r["bill_number"] else "calculated" if r and r["calculated"] else "published" if r else "none")
            n[key] += 1
            if len(ex[key]) < 3:
                ex[key].append(((x.get("contract_title") or "")[:90].replace("\n", " "), (r or {}).get("amount"), ((r or {}).get("basis") or "")[:330]))
    for key in sorted(n):
        print("%-22s %-13s %5d" % (key[0], key[1], n[key]))
        for t, am, b in ex[key]:
            print("      %s -> %s\n         %s" % (t, am, b))


if __name__ == "__main__":
    import argparse
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["harvest", "check"])
    ap.add_argument("file", nargs="?", default="")
    ap.add_argument("--all", action="store_true", help="read Toronto's licence pages again even when they were read this week")
    a = ap.parse_args()
    {"harvest": harvest, "check": check}[a.cmd](a)
