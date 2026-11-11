#!/usr/bin/env python3
"""The Canadian biller that an organisation has by where it is: the electricity distributor of its address (2026-11-11).

Owner, 2026-11-11 16:01 EST: "1 million goal, think differently if need be … take all liberty as long as under what we laid down: invoice,
bank EFT, email, Canadian vendor, in simple terms, and just populate those fields as best as you can, don't just go empty". Earlier the
same day: "when do we know for a fact? When … something being where it is means that there's a relationship"; "any Canadian entity … whatever
month, year thing, okay, now you owe us so and so amount of money"; "billed for something monthly … systematically by the vendor".

One relationship holds for every organisation with premises in Canada outside Alberta: electricity at its address is distributed, and billed,
by ONE body — an exclusive franchise or a licensed service area set by law — every month, on an invoice, paid through a bank (Hydro-Québec and Manitoba Hydro refuse
credit cards in so many words). What is certain is the biller of the address. What is not published is whose name is on the account: an
occupant with its own meter is billed itself; where a landlord holds the meter, the landlord is. Every such row says so, in the column
relationship_fact_basis ("by where it is: …"), and `ship_ready` says "yes (by where the organisation is …)": these rows are never mixed
with the rows that rest on a record.

Ontario has some sixty licensed distributors and a postal area there is often shared by two: the postal code itself decides, by the Ontario
Energy Board's own map of the service areas (tools/on_ldc_table.py builds tools/data/on_postal_ldc.tsv.gz and, from the Board's page on each
distributor, tools/data/billers_by_location_on.json). A lane that reads one of those distributors' own billing and payment pages hands the
sentences in under "table_key" (the distributor's licensed name).

The table (tools/data/billers_by_location.json; another lane adds a distributor as contrib/<lane>/billers_by_location/<key>.json): the
distributor's name and its own printed address, the postal areas of its territory (prefixes, and the areas left out because a municipal
utility or another distributor serves them), the law of its franchise, and — each a sentence of its own page — how often it bills, the
least it bills, how the bill arrives and how it is paid. A distributor whose payment page is not read yet has those cells empty and the
test says its bill is paid "by the kind of bill".

  python3 tools/by_location.py count TABLE     organisations of a ranked table with a mailbox whose distributor can be named, by distributor
  python3 tools/by_location.py verify          another lane's files: every quoted sentence is looked for on the page named for it; only then are they used
"""
import collections, csv, glob, gzip, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PC = re.compile(r"(?<![A-Za-z0-9])([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z])[  -]?\d[ABCEGHJ-NPRSTV-Z]\d(?![A-Za-z0-9])")
NEED = ("key", "name", "site", "address", "address_url", "address_quote", "prefixes", "territory", "what")


VERIFIED = os.path.join(ROOT, "data/incoming/claude/billers_verified.json")
FACTS = ("period_basis", "amount_basis", "delivery", "payment", "terms", "remit_to", "unpaid", "what")


def _sig(b):
    import hashlib
    return hashlib.sha1(json.dumps({k: b.get(k) for k in NEED + FACTS + ("url",) + tuple(k + "_url" for k in FACTS)}, sort_keys=True, ensure_ascii=False, default=sorted).encode()).hexdigest()[:16]


def _files():
    for f in sorted(glob.glob(os.path.join(ROOT, "contrib/*/billers_by_location/*.json"))):
        try:
            b = json.load(open(f, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        # a new distributor (its postal areas, its own printed address, its territory), or — "table_key" — the own sentences of a distributor
        # that is already on file by a table (Ontario's licensed distributors: tools/on_ldc_table.py)
        if isinstance(b, dict) and b.get("key") and (all(b.get(k) for k in NEED) or b.get("table_key")):
            b["_file"] = os.path.relpath(f, ROOT)
            yield b


def _load():
    """the distributors read by lane claude (tools/data), then another lane's files — those only once `verify` found each quoted sentence on its page"""
    out = []
    try:
        out = json.load(open(os.path.join(ROOT, "tools/data/billers_by_location.json"), encoding="utf-8"))
    except (OSError, ValueError):
        pass
    try:  # Ontario's licensed distributors (tools/on_ldc_table.py): the Board's page gives each one's address and site; a distributor read by hand keeps its own sentences
        gen = {g["table_key"]: g for g in json.load(open(os.path.join(ROOT, "tools/data/billers_by_location_on.json"), encoding="utf-8"))}
    except (OSError, ValueError):
        gen = {}
    for b in out:
        g = gen.pop(b.get("table_key") or "", None)
        if g:
            for k, v in g.items():
                if k == "territory" or not b.get(k):
                    b[k] = v
            b["key"] = g["key"] if not b.get("key") else b["key"]
    out += list(gen.values())
    try:
        ok = json.load(open(VERIFIED, encoding="utf-8"))
    except (OSError, ValueError):
        ok = {}
    taken = {p for b in out for p in b.get("prefixes") or ()}
    by_table = {b["table_key"]: b for b in out if b.get("table_key")}
    for b in _files():
        if ok.get(b["_file"], {}).get("sig") != _sig(b):
            continue
        for k in FACTS:  # a lane's file names the page of a sentence beside it (delivery_url …, or url): the row prints it after the sentence
            if b.get(k) and "http" not in b[k] and (b.get(k + "_url") or b.get("url")):
                b[k] = "%s (%s)" % (b[k], b.get(k + "_url") or b["url"])
        if b.get("table_key"):
            t = by_table.get(b["table_key"])
            if t:  # the distributor is on file (address, territory): the lane's verified sentences fill what was not read yet
                for k in FACTS + ("period", "amount", "read"):
                    if b.get(k) and (not t.get(k) or k == "read" and any(b.get(f_) and not t.get(f_) for f_ in FACTS)):
                        t[k] = b[k]
        elif not (set(b["prefixes"]) & taken):
            out.append(b)
            taken |= set(b["prefixes"])
    out = [b for b in out if all(b.get(k) for k in NEED if k != "prefixes") and (b.get("prefixes") or b.get("table_key")) and PC.search((b["address"] + " " + b["address_quote"]).upper())]
    for b in out:
        b.setdefault("prefixes", [])
    for b in out:
        b["except_fsas"] = set(b.get("except_fsas") or ())
    return out


def verify():
    """open the pages a lane's file names and look for every quoted sentence on them; a file is used only after that (data/incoming/claude/billers_verified.json)"""
    import html, time
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ap_crawler as C
    flat = lambda t: re.sub(r"\s+", " ", t).strip()
    try:
        ok = json.load(open(VERIFIED, encoding="utf-8"))
    except (OSError, ValueError):
        ok = {}
    n, cache = collections.Counter(), {}

    def text(url):
        if url not in cache:
            cache[url] = ""
            if C.allowed(url):
                st, ct, data, final = C.fetch(url)
                time.sleep(1.0)
                if st == 200 and data:
                    cache[url] = flat(C.pdf_text(data) or "") if data[:5] == b"%PDF-" else flat(C.visible(C.quote_attrs(html.unescape(data.decode("utf-8", "replace")))))
        return cache[url]
    for b in _files():
        if ok.get(b["_file"], {}).get("sig") == _sig(b):
            n["verified before"] += 1
            continue
        pairs = [(b["address_url"], b["address_quote"])] if b.get("address_quote") else []
        for k in FACTS:
            url = b.get(k + "_url") or b.get("url") or ""
            pairs += [(url, q) for q in re.findall(r"“([^”]+)”", b.get(k) or "")]
        bad = [(u, q) for u, q in pairs if not u or len(q) > 300 or flat(q) not in text(u)]
        if (not b.get("table_key") and not PC.search(((b.get("address") or "") + " " + (b.get("address_quote") or "")).upper())) or not b.get("payment") or not b.get("delivery") or not pairs:
            n["no Canadian postal code in its address, or no sentence on how it bills and is paid"] += 1
        elif bad:
            n["a quoted sentence is not on the page named for it"] += 1
            print("not verified: %s — “%s” (%s)" % (b["_file"], bad[0][1][:100], bad[0][0]))
        else:
            ok[b["_file"]] = {"sig": _sig(b), "verified": time.strftime("%Y-%m-%d"), "quotes": len(pairs)}
            n["verified now"] += 1
    os.makedirs(os.path.dirname(VERIFIED), exist_ok=True)
    json.dump(ok, open(VERIFIED, "w", encoding="utf-8"), indent=1, sort_keys=True)
    print("billers by location handed in as files: %s" % dict(n))


BILLERS = _load()
BY_NAME = {b["name"]: b for b in BILLERS}
BY_KEY = {b["key"]: b for b in BILLERS}
BY_TABLE = {b["table_key"]: b for b in BILLERS if b.get("table_key")}
_ON = None


def _on():
    """Ontario: {postal code, or postal area that lies in one service area: distributor as licensed} (tools/on_ldc_table.py)"""
    global _ON
    if _ON is None:
        _ON, names = {}, {}
        try:
            with gzip.open(os.path.join(ROOT, "tools/data/on_postal_ldc.tsv.gz"), "rt", encoding="utf-8") as f:
                for l in f:
                    a, _, v = l.rstrip("\n").partition("\t")
                    if a.startswith("="):
                        names[a[1:]] = v
                    elif a and not a.startswith("#"):
                        _ON[a] = names.get(v, "")
        except OSError:
            pass
    return _ON


def fsa_of(text):
    """the postal area (first three characters of a Canadian postal code) of the first postal code printed in an address"""
    m = PC.search((text or "").upper())
    return m.group(1) if m else ""


def biller_for(text):
    """the distributor of the address, or None: no postal code, Alberta (the retailer is the customer's choice), an area left out"""
    m = PC.search((text or "").upper())
    if not m:
        return None
    fsa = m.group(1)
    if fsa[0] in "KLMNP":
        # Ontario: some sixty distributors, and a postal area is often shared by two — the postal code itself decides (the Ontario Energy
        # Board's map of service areas; a code near an edge, or unknown in a shared area, gets none)
        nm = _on().get(re.sub(r"[^A-Z0-9]", "", m.group(0))) or _on().get(fsa)
        return BY_TABLE.get(nm) if nm else None
    for b in BILLERS:
        if b["prefixes"] and fsa not in b["except_fsas"] and any(fsa.startswith(p) for p in sorted(b["prefixes"], key=len, reverse=True)):
            return b
    return None


def biller_for_all(text):
    """the distributor of a text that may print several postal codes (a page, a quote): all of them must lie in one distributor's territory"""
    got = {id(biller_for(m.group(0))): biller_for(m.group(0)) for m in PC.finditer((text or "").upper())}
    return next(iter(got.values())) if len(got) == 1 else None


def of_row(x):
    """the distributor of a row whose vendor is one of the table and whose buyer's printed address lies in its territory"""
    b = BY_NAME.get(re.sub(r"^inferred:\s*", "", (x.get("vendor") or "").strip()))
    if not b:
        return None
    if biller_for(x.get("buyer_address") or "") is b:
        return b
    if not fsa_of(x.get("buyer_address") or "") and biller_for_all(x.get("email_evidence_quote") or "") is b:
        # the organisation's own page prints its postal code beside its mailbox, and no fuller address was read: the postal code stands for it
        m = PC.search((x.get("email_evidence_quote") or "").upper())
        x["buyer_address"] = "postal code %s (as printed beside the organisation's mailbox on %s)" % (m.group(0), x.get("email_evidence_url") or "its own page")
        return b
    return None


def status(b, fsa):
    return ("billed by the electricity distributor of its address — by where the organisation is (postal area %s), not by a record: %s; an occupant with its own meter is billed "
            "by it every month, and where a landlord holds the meter the landlord is" % (fsa, b["territory"]))


def row_cells(b, x):
    """the cells of a by-location row: what is billed, how often, the least amount, how the bill arrives and is paid — each in the distributor's own words when read"""
    fsa = fsa_of(x.get("buyer_address") or "")
    src = lambda k: (" (read %s)" % b["read"]) if b.get(k) else ""
    out = {"relationship_kind": "electricity account, by where the organisation is (the distributor is certain for the address; the account holder is not published)",
           "relationship_fact_basis": ("by where it is: the organisation's own address (%s) lies in the exclusive territory of %s — %s. A fact about the address; whether the "
                                       "organisation or its landlord holds the account is not published" % (fsa, b["name"], b["territory"])),
           "contract_title": "Electricity service at the organisation's address",
           "bill_items_as_published": b["what"],
           "invoice_reference_hint": "the customer account number printed on the distributor's bill (not public)",
           "bill_currency_as_published": "Canadian dollars (a Canadian distributor's regulated rates)"}
    if b.get("period"):
        out["recurring_billing"], out["recurring_billing_basis"] = b["period"], b["period_basis"] + src("period")
    else:
        out["recurring_billing"], out["recurring_billing_basis"] = "2 monthly or yearly", ("an electricity distributor bills every month or every two months; this distributor's own "
                                                                                           "sentence on its billing period is not read yet")
    if b.get("amount"):
        out["bill_amount_indicative"], out["bill_amount_basis"] = b["amount"], b["amount_basis"]
    for col, k in (("bill_delivery_as_published", "delivery"), ("bill_payment_method_as_published", "payment"), ("bill_due_terms_as_published", "terms"),
                   ("bill_remit_to_as_published", "remit_to"), ("service_stops_if_unpaid", "unpaid")):
        if b.get(k):
            out[col] = b[k] + src(k)
    return out


def scan_postal_codes():
    """{site: (postal code, day the scan's file was written)} — the first Canadian postal code an organisation's own home page prints, as the
    home-page scan kept it (tools/credit_scan.py, detector 5: data/incoming/claude/credit_scan/links_<stamp>.gz, 4th column
    "site name|copyright name|legalName|postal code"). 377,262 home pages on 2026-11-11."""
    out = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "data/incoming/claude/credit_scan/links_*.gz"))):
        dm = re.search(r"links_(\d{4})(\d\d)(\d\d)", os.path.basename(p))
        day = "-".join(dm.groups()) if dm else ""
        try:
            with gzip.open(p, "rt", encoding="utf-8", errors="replace") as fh:
                for l in fh:
                    q = l.rstrip("\n").split("\t")
                    if len(q) >= 4 and q[3].count("|") == 3:
                        pc = q[3].rsplit("|", 1)[1].strip().upper()
                        if len(pc) == 6 and q[0]:
                            out[q[0].lower()] = (pc, day)
        except (OSError, EOFError) as e:
            print("scan postal codes: %s not read (%s)" % (os.path.basename(p), e), flush=True)
    return out


def count(path):
    csv.field_size_limit(1 << 30)
    n = collections.Counter()
    op = gzip.open if path.endswith(".gz") else open
    with op(path, "rt", encoding="utf-8", errors="replace", newline="") as f:
        for x in csv.DictReader(f):
            if not (x.get("email") or "").strip():
                continue
            b = biller_for(x.get("buyer_address") or "")
            n[b["name"] if b else ("no distributor can be named: " + ("no Canadian postal code in the address" if not fsa_of(x.get("buyer_address") or "") else "Alberta, or an area left out"))] += 1
    for k, v in n.most_common():
        print("%8d  %s" % (v, k))


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "count":
        count(sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == "verify":
        verify()
    else:
        for b in BILLERS:
            print("%-48s %-22s %s" % (b["name"][:48], ",".join(b["prefixes"]) or "Ontario, by postal code", ", ".join(k for k in ("period", "amount", "delivery", "payment", "terms", "remit_to", "unpaid") if b.get(k)) or "(address and territory only)"))
