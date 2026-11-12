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
# 2026-11-12 — what is NOT a postal code although it has the shape of one. Found in the table of 00:14Z: 53 rows stood on a colour code or a
# form's placeholder, and the home-page scan held 2,284 such "codes" (291 greys: E6E 6E6, A1A 1A1 …; a Norwegian clinic had become a customer
# of NB Power).
#  - a colour code (#E6E6E6, "d6cdc0" in a page's data): six hexadecimal characters. Of the letters of a postal code only A, B, C and E are
#    hexadecimal, so a code whose three letters are all among them is taken only when it is printed as a postal code is — in capitals, with
#    a space or a hyphen between its halves — and is a code that exists (tools/data/pc_abce.txt.gz, from the GeoNames dump);
#  - a placeholder: three times the same pair (A1A 1A1, H0H 0H0, K1K 1K1 — some exist, and a form's example is what a page prints), the
#    alphabet's A1B 2C3, Canada Post's own example K1A 0B1.
_PCX = re.compile(r"(?<![A-Za-z0-9#])([ABCEGHJ-NPRSTVXYabceghj-nprstvxy]\d[ABCEGHJ-NPRSTV-Zabceghj-nprstv-z])([ \u00a0-]?)(\d[ABCEGHJ-NPRSTV-Zabceghj-nprstv-z]\d)(?![A-Za-z0-9])")
PLACEHOLDER = {"A1B2C3", "K1A0B1", "A2B3C4", "X0X0X0"}
_ABCE = None


def _abce():
    global _ABCE
    if _ABCE is None:
        _ABCE = set()
        try:
            with gzip.open(os.path.join(ROOT, "tools/data/pc_abce.txt.gz"), "rt", encoding="utf-8") as f:
                _ABCE = {l.strip() for l in f if l.strip() and not l.startswith("#")}
        except OSError:
            pass
    return _ABCE


def usable(pc, as_printed="", sep=None):
    """is this six-character code a postal code an address can stand on? as_printed / sep: how the page prints it, when that is known"""
    if len(pc) != 6 or pc in PLACEHOLDER or re.fullmatch(r"([A-Z]\d)\1\1", pc):
        return False
    if not re.search(r"[^ABCE0-9]", pc):  # its letters are all hexadecimal: it could be a colour
        if sep is None:
            return False  # kept without its context (the home-page scan's stored codes): not taken
        return bool(sep) and as_printed == as_printed.upper() and pc in _abce()
    return True


def codes(text):
    """the postal codes a text prints, in order: (code, match) — what is a colour code or a placeholder is left out"""
    for m in _PCX.finditer(text or ""):
        pc = (m.group(1) + m.group(3)).upper()
        if usable(pc, m.group(1) + m.group(3), m.group(2)):
            yield pc, m
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
            own_address = bool(b.get("address"))  # read on the distributor's own site by hand: its page, its quote and where it was read stay together
            for k, v in g.items():
                if k == "territory" or (not b.get(k) and not (own_address and k.startswith("address"))):
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
    pc = next((c for c, _ in codes(text)), "")
    return pc[:3]


def code_of(text):
    """the first postal code a text prints (six characters), or ''"""
    return next((c for c, _ in codes(text)), "")


# 2026-11-12 — a postal area left out of a distributor's territory because a municipal network lies in it is often shared with the towns around
# it (J6E: Joliette 901 postal codes, Saint-Charles-Borromée 375 and Notre-Dame-des-Prairies 309; H3Y/H3Z: Westmount 709, Montréal 78; E2H:
# Rothesay 207, Saint John 146). A postal code there names the distributor when its place (the GeoNames postal-code dump, by code:
# tools/data/pocket_places.tsv.gz, written by tools/on_ldc_table.py cities) is not one of the towns the distributor's own territory sentence
# leaves out. Not used: British Columbia (FortisBC's areas are not a list of towns) and J0L (the Saint-Jean-Baptiste-de-Rouville
# co-operative serves parts of several towns).
POCKET_TOWNS = {"hydro_quebec": {"alma", "amos", "baie comeau", "coaticook", "joliette", "magog", "saguenay", "jonquiere", "chicoutimi", "sherbrooke", "westmount",
                                 "saint jean baptiste"},
                "saskpower": {"saskatoon", "swift current"},
                "nb_power": {"saint john", "edmundston", "perth andover"},
                "ns_power": {"antigonish", "berwick", "lunenburg", "mahone bay", "riverport", "canso"},
                "maritime_electric": {"summerside"}}
POCKET_KEEP_OUT = {"J0L"}
POCKET_PLACES = os.path.join(ROOT, "tools/data/pocket_places.tsv.gz")
_PP = None


def _pocket_place(pc):
    global _PP
    if _PP is None:
        _PP = {}
        try:
            with gzip.open(POCKET_PLACES, "rt", encoding="utf-8") as f:
                for l in f:
                    if not l.startswith("#"):
                        a_, _, b_ = l.rstrip("\n").partition("\t")
                        _PP[a_] = b_
        except OSError:
            pass
    return _PP.get(pc, "")


def biller_for(text):
    """the distributor of the address, or None: no postal code, Alberta (the retailer is the customer's choice), an area left out"""
    pc = text if (isinstance(text, str) and len(text) == 6 and text.isalnum() and text == text.upper()) else code_of(text)
    if not pc:
        return None
    fsa = pc[:3]
    if fsa[0] in "KLMNP":
        # Ontario: some sixty distributors, and a postal area is often shared by two — the postal code itself decides (the Ontario Energy
        # Board's map of service areas; a code near an edge, or unknown in a shared area, gets none)
        nm = _on().get(pc) or _on().get(fsa)
        return BY_TABLE.get(nm) if nm else None
    for b in BILLERS:
        if b["prefixes"] and fsa not in b["except_fsas"] and any(fsa.startswith(p) for p in sorted(b["prefixes"], key=len, reverse=True)):
            return b
    for b in BILLERS:  # a postal area left out whole: the postal code's own place decides
        if fsa in b["except_fsas"] and b["key"] in POCKET_TOWNS and fsa not in POCKET_KEEP_OUT and any(fsa.startswith(p) for p in b["prefixes"]):
            place = _pocket_place(pc)
            if place and place not in POCKET_TOWNS[b["key"]]:
                return b
            return None
    return None


def biller_for_all(text):
    """the distributor of a text that may print several postal codes (a page, a quote): all of them must lie in one distributor's territory"""
    got = {}
    for pc, _ in codes(text):
        b = biller_for(pc)
        got[id(b)] = b
    return next(iter(got.values())) if len(got) == 1 else None


# ---- by the city the organisation's own page names, when it prints no postal code (2026-11-12) -------------------------------------------
# 126,561 organisations with a mailbox of their own print no postal code that was read; 15,459 of them print "City, Province" beside their
# mailbox ("261 Victoria St Kamloops, BC", "Laval (Québec)"). A city names a distributor when EVERY postal code of that city lies in one
# distributor's territory — counted over the postal-code dump's place names with the same rules as a postal code (tools/on_ldc_table.py
# cities -> tools/data/city_biller.tsv.gz: a city 98 % of whose codes have one distributor and none another). A city split between two
# distributors, a city of Alberta, a place the dump does not know, or two cities with two distributors in one text: no distributor.
_PROVN = (r"Qu[ée]bec|Ontario|British Columbia|Colombie-Britannique|Alberta|Manitoba|Saskatchewan|Nova Scotia|Nouvelle-[ÉE]cosse|New Brunswick|Nouveau-Brunswick|"
          r"Newfoundland(?: and Labrador)?|Terre-Neuve(?:-et-Labrador)?|Prince Edward Island|[ÎI]le-du-Prince-[ÉE]douard|Yukon|Nunavut|Northwest Territories")
CITY_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])([A-ZÀ-Ý][A-Za-zÀ-ÿ.'’\-]+(?:[ \-][A-ZÀ-Ýa-zà-ÿ][A-Za-zÀ-ÿ.'’\-]+){0,3})\s*(?:,\s*|\(\s*)(?:(" + _PROVN + r")|(QC|Qc|ON|BC|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NT|NU))\)?"
                     r"(?:,?\s*Canada)?(?![A-Za-zÀ-ÿ])(?!,?\s*(?:CA|California|USA?)\b)(?!\s+\d{5})")
_PROV_CODE = {"quebec": "QC", "québec": "QC", "qc": "QC", "ontario": "ON", "on": "ON", "british columbia": "BC", "colombie-britannique": "BC", "bc": "BC", "alberta": "AB", "ab": "AB",
              "manitoba": "MB", "mb": "MB", "saskatchewan": "SK", "sk": "SK", "nova scotia": "NS", "nouvelle-ecosse": "NS", "nouvelle-écosse": "NS", "ns": "NS", "new brunswick": "NB",
              "nouveau-brunswick": "NB", "nb": "NB", "newfoundland": "NL", "newfoundland and labrador": "NL", "terre-neuve": "NL", "terre-neuve-et-labrador": "NL", "nl": "NL",
              "prince edward island": "PE", "ile-du-prince-edouard": "PE", "île-du-prince-édouard": "PE", "pe": "PE", "pei": "PE", "yukon": "YT", "yt": "YT", "nunavut": "NU", "nu": "NU",
              "northwest territories": "NT", "nt": "NT"}
CITY_TABLE = os.path.join(ROOT, "tools/data/city_biller.tsv.gz")
_CITY = None


def norm_city(s):
    import unicodedata
    t = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    t = re.sub(r"\b(?:ste?)[.]?(?=[ -])", lambda m: "sainte" if m.group(0).startswith("ste") else "saint", t)
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def _cities():
    """{(province code, city): (distributor key, share, postal codes)}"""
    global _CITY
    if _CITY is None:
        _CITY = {}
        try:
            with gzip.open(CITY_TABLE, "rt", encoding="utf-8") as f:
                for l in f:
                    if l.startswith("#"):
                        continue
                    q = l.rstrip("\n").split("\t")
                    if len(q) >= 5:
                        _CITY[(q[0], q[1])] = (q[2], float(q[3]), int(q[4]))
        except OSError:
            pass
    return _CITY


def biller_for_city(text):
    """(distributor, "City, PROV" as printed, the words it was read in) when every city the text names that the dump knows lies in one
    distributor's territory, else None"""
    tab, got, said = _cities(), {}, None
    if not tab:
        return None
    for m in CITY_RX.finditer(text or ""):
        prov = _PROV_CODE.get((m.group(2) or m.group(3) or "").lower())
        city = norm_city(m.group(1))
        if not prov or not city:
            continue
        words, raw = city.split(), m.group(1).split()
        e, name = None, ""
        for i in range(len(words)):  # "Contact 261 Victoria St Kamloops": the city is the last words of the match
            e = tab.get((prov, " ".join(words[i:])))
            if e is not None:
                # the words of the match as printed that spell it ("Notre-Dame-de-l'Île-Perrot" is one printed word and six normalised ones)
                name = next((" ".join(raw[j:]) for j in range(len(raw)) if norm_city(" ".join(raw[j:])) == " ".join(words[i:])), m.group(1))
                break
        if e is None:
            continue  # a place the dump does not know (a region, a country, a street)
        b = BY_KEY.get(e[0])
        if b is None:
            return None  # a city the dump knows that no single distributor serves (split, a pocket, Alberta)
        got[e[0]] = b
        said = said or ("%s, %s" % (name.strip(" ,.("), prov), (text or "")[max(0, m.start() - 60):m.end() + 10], e[1])
    return (next(iter(got.values())), said[0], said[1], said[2]) if len(got) == 1 else None


_KP = None


def _KNOWN_PLACES():
    """every (province, city) of the dump, also the ones no single distributor serves (written with them in the city table, distributor '-')"""
    global _KP
    if _KP is None:
        _KP = {k for k in _cities()}
    return _KP


def of_row(x):
    """the distributor of a row whose vendor is one of the table and whose buyer's printed address lies in its territory"""
    b = BY_NAME.get(re.sub(r"^inferred:\s*", "", (x.get("vendor") or "").strip()))
    if not b:
        return None
    if biller_for(x.get("buyer_address") or "") is b:
        return b
    if not fsa_of(x.get("buyer_address") or "") and (biller_for_city(x.get("buyer_address") or "") or (None,))[0] is b:
        return b  # the organisation's own page names its city, and the whole city is this distributor's
    if not fsa_of(x.get("buyer_address") or "") and biller_for_all(x.get("email_evidence_quote") or "") is b:
        # the organisation's own page prints its postal code beside its mailbox, and no fuller address was read: the postal code stands for it
        pc = code_of(x.get("email_evidence_quote") or "")
        x["buyer_address"] = "postal code %s %s (as printed beside the organisation's mailbox on %s)" % (pc[:3], pc[3:], x.get("email_evidence_url") or "its own page")
        return b
    return None


def status(b, fsa):
    where = ("postal area %s" % fsa) if re.fullmatch(r"[A-Z]\d[A-Z]", fsa or "") else (fsa or "its city")
    return ("billed by the electricity distributor of its address — by where the organisation is (%s), not by a record: %s; an occupant with its own meter is billed "
            "by it every month, and where a landlord holds the meter the landlord is" % (where, b["territory"]))


# 2026-11-12 — an urban postal code is one side of a street block or one building. When many organisations print the same one on their own
# sites it is a tower, a campus, a business centre or a mail service (the table of 00:14Z: 133 rows on M5C 1C4, 67 on First Canadian Place's
# M5X 1C7, 34 sports federations on the Olympic stadium's H1S 2A7), and there the landlord holds the electricity account. Counted over the
# home pages the scan read and this build's rows, by registrable domain; a rural code (second character 0) stands for a whole town and is
# not counted. From SHARED_SAY organisations the row says so; from SHARED_FAIL it does not meet the test (tools/relationship_rows.py).
SHARED_SAY, SHARED_FAIL = 10, 50


def shared_sentence(n):
    return ("; %d organisations print this same postal code on their own sites — a shared building, where the landlord often holds the account" % n) if n >= SHARED_SAY else ""


def row_cells(b, x):
    """the cells of a by-location row: what is billed, how often, the least amount, how the bill arrives and is paid — each in the distributor's own words when read"""
    fsa = fsa_of(x.get("buyer_address") or "")
    if not fsa:
        _bc = biller_for_city(x.get("buyer_address") or "")
        if _bc and _bc[0] is b:
            fsa = "city %s, %s of whose postal codes lie in this distributor's territory (GeoNames postal codes by place)" % (_bc[1], ("all" if _bc[3] >= 0.9995 else "%.1f %%" % (100 * _bc[3])))
    src = lambda k: (" (read %s)" % b["read"]) if b.get(k) else ""
    out = {"relationship_kind": "electricity account, by where the organisation is (the distributor is certain for the address; the account holder is not published)",
           "relationship_fact_basis": ("by where it is: the organisation's own address (%s) lies in the exclusive territory of %s — %s. A fact about the address; whether the "
                                       "organisation or its landlord holds the account is not published%s" % (fsa, b["name"], b["territory"], shared_sentence(int(x.get("_pc_orgs") or 0)))),
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
                   ("bill_remit_to_as_published", "remit_to"), ("service_stops_if_unpaid", "unpaid"), ("bill_tax_rule_as_published", "tax")):
        if b.get(k):
            out[col] = b[k] + src(k)
    # 2026-11-12 (owner 20:04 and 20:14 EST: "what about estimated value per billing cadence and all other … invoice fields"; "an inference be
    # permissible … a fair estimate can be made"): what the bill comes to at a stated use, calculated from the distributor's own published rate
    # and labelled; the distributor's legal name as it or its regulator prints it; its number in the regulator's register where it has one
    if b.get("estimate"):
        out["bill_amount_calculated"] = b["estimate"]
    ln = b.get("legal_name") or b.get("legal_name_as_printed")
    if ln and not str(x.get("vendor_legal_name") or "").strip():
        out["vendor_legal_name"] = "%s (%s)" % (ln, b.get("legal_name_basis") or "as the distributor's own pages print it")
    if b.get("registration") and not any(str(x.get(c) or "").strip() for c in ("vendor_bn9", "vendor_neq", "vendor_registry_id")):
        out["vendor_registry_id"] = b["registration"]
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
                        if len(pc) == 6 and q[0] and usable(pc):  # (a colour code or a placeholder kept as a postal code is not one)
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
