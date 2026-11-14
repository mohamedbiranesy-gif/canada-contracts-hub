#!/usr/bin/env python3
"""Final correction of the built table — the corrections saved after the build of 2026-11-13 22:10Z, applied row by row to that table.

Why: the owner stopped the project on 2026-11-13 at 20:51 EST ("pull the plug"), after GitHub disabled Actions for the account at 23:39Z. The
rules written after the last build (buyer names, rule 19 by name, foundations, province conflicts, the CMEQ's and the CMMTQ's own fees, legal
names read on legal pages, one row per buyer) could never reach a build. This applies them to the last built table, the way the next build
would have: the same functions, read out of contrib/claude/rank_buyers/rank.py and tools/relationship_rows.py as they stand, then the owner's
test (tools/relationship_rows.owner_test) on every row, then the order of priority and one row per organisation (tools/priority_sort.py), then
one row per website and name (the fold rank.py does since 2026-11-14).

What it cannot do (it needs the inputs only a build has): municipalities' electricity estimated from their residents (tools/muni_energy.py),
rows that give way to a body's own record, new mailboxes the referee confirmed after 22:10Z, a legal name from another source where a junk one
is cleared (the cell is left empty, so the field shows as not published).

  python3 contrib/claude/final_correction/correct_table.py correct IN.csv.gz OUTDIR     -> OUTDIR/ranked_buyers.csv.gz, corrections.csv.gz, counts.json
  python3 tools/priority_sort.py OUTDIR                                                 -> ready first, by amount mark; one row per organisation
  python3 contrib/claude/final_correction/correct_table.py fold OUTDIR                  -> one row per website and name; folded_rows.csv
"""
import collections, csv, gzip, html, json, os, re, sys, unicodedata, urllib.parse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import relationship_rows as RR  # noqa: E402
import payee_billing as PB  # noqa: E402
from ap_crawler import registrable  # noqa: E402

csv.field_size_limit(1 << 30)
SRC = open(os.path.join(ROOT, "contrib/claude/rank_buyers/rank.py"), encoding="utf-8").read()


def _grab(a, b):
    i = SRC.index(a)
    if b is None:  # one statement: a def up to the next top-level line; anything else, the shortest run of lines from `a` that parses
        import ast
        lines = SRC[i:].split("\n")
        if lines[0].startswith(("def ", "try:")):
            k = 1
            while k < len(lines) and (not lines[k].strip() or lines[k][:1] in " \t" or lines[k].startswith(("except", "else:", "finally:"))):
                k += 1
            return "\n".join(lines[:k])
        for k in range(1, 400):
            try:
                ast.parse("\n".join(lines[:k]))
                return "\n".join(lines[:k])
            except SyntaxError:
                continue
        raise SystemExit("no statement at " + a)
    return SRC[i:SRC.index(b, i)]


NS = {"re": re, "csv": csv, "gzip": gzip, "unicodedata": unicodedata, "urllib": urllib, "ROOT": ROOT, "registrable": registrable, "os": os}
for _a, _b in (("norm = lambda s:", "\n"), ("def host_of(u):", "FREEMAIL = re.compile"), ("SHARED_GOV = re.compile", "GENERIC_TOK = {"),
               ("DOMAIN_NAME = re.compile", "\n"), ("_LEGAL_PERSON = re.compile", "_PLATFORM_CO = re.compile"),
               ("_JUNK_NAME = re.compile", "def _premises(a):"), ("_DUP_TYPE = {", "_by_site, merged, n_dup"), ("BAD_LOCAL = re.compile", None),
               ("_NOT_DUES = re.compile", None), ("try:\n    from buyer_pages import FIRST_NAMES as _GCR_FIRST", None),
               ("_GCR_ORGWORD = re.compile", None), ("def _GCR_PERSON(n):", None)):
    exec(_grab(_a, _b), NS)
import muni_energy as MUNI  # noqa: E402
import by_location as BYLOC  # noqa: E402
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import title_names as TN  # noqa: E402
import address_checks as AC  # noqa: E402
MUNI_MAIN = {p_: d_ for p_, (c_, d_) in MUNI.CITY.items()} if MUNI.load() else {}
# the ironclad rule (owner 2026-11-04): a webmail address is not an organisational mailbox (rank.py, the same list)
WEBMAIL = re.compile(r"^(?:gmail|googlemail|hotmail|outlook|live|msn|yahoo|ymail|rocketmail|aol|icloud|me|mac|protonmail|proton|gmx|mail|yandex|zoho|hush|hushmail|fastmail|tutanota|tuta|pm)\.(?:com|ca|net|org|fr|me|co\.uk|de|ch)$", re.I)
TYPE_LABEL = {"invoicing": ("invoicing/AP", 4), "accounts_payable": ("invoicing/AP", 4), "ap": ("invoicing/AP", 4), "finance": ("finance/accounting dept or supplier-payment office", 3),
              "procurement": ("purchasing", 2), "purchasing": ("purchasing", 2), "general": ("general", 1)}


# read one by one on 2026-11-14 among the 37 candidates: what the crawler's type guess or the referee's re-read could not see
REVIEWED_OUT = {"aidefinanciere@cegepdrummond.ca": "the students' financial-aid office (aide financière), not accounts payable — the crawler took 'financière' for finance",
                "marie.paiement@cssa.gouv.qc.ca": "a person's own mailbox (Marie Paiement) — the crawler took the surname for 'payment'",
                "admin@airforce.com": "the administrator of a recruiting site, on its privacy page — not the United States Air Force's intake",
                "info.france@kavo.com": "the French office's mailbox, not KaVo Dental GmbH's own", "info@kavo.co.uk": "the British office's mailbox, not KaVo Dental GmbH's own",
                "info.benelux@kavo.com": "the Benelux office's mailbox, not KaVo Dental GmbH's own",
                "indigenousprocurement@epcor.com": "the mailbox of EPCOR's Indigenous procurement programme, not where its bills are taken in",
                "accueil-trotabas@univ-cotedazur.fr": "the front desk of one campus (the Trotabas law faculty), not the university's intake",
                "info@matapedia.ca": "the municipality of Matapédia's mailbox, on a page that lists several municipalities — not Saint-André-de-Restigouche's"}
# a mailbox the referee re-read that the page itself says is for queries only (2026-11-14): kept, under its true role
TYPE_OVERRIDE = {"ap.paymentsteam@durham.ac.uk": ("finance/accounting dept or supplier-payment office", 3,
                                                  "invoice queries only — the page: “Invoice queries should be sent to ap.paymentsteam@durham.ac.uk . Do not send invoices to "
                                                  "this address.”")}
# mailboxes on the table of 22:10Z that are a named person's (AGENTS.md §2.5), read one by one on 2026-11-14: taken off the row
PERSON_MAILBOX = {"cindy.accounting@allansgarage.ca": "Cindy's", "jen.accounting@lelc.ca": "Jen's", "mail-jiyeong.kim@matthey.com": "Jiyeong Kim's",
                  "account-name_gary@garymwentinhibbert.com": "Gary's", "paiement.eve-line@uqam.ca": "Ève-Line's"}
# a site matched by name to the wrong organisation, read one by one on 2026-11-14: the site and its mailbox come off the row
WRONG_SITE = {"berger-shk.com": "a German plumbing firm's site (“Berger & Co. GmbH”, Hamburg, telephone 04174 …) — not the U.S. exporter BERGER & CO of Pawtucket, RI"}
MAIL_COLS = ("email", "email_type", "email_check", "mailbox_confidence", "email_evidence_url", "email_evidence_quote", "email_evidence_context", "mailbox_provenance",
             "grade", "acc")


def _person_local(local):
    t = re.split(r"[._-]", local.lower())
    return len(t) == 2 and all(re.fullmatch(r"[a-z]{2,}", w) for w in t) and t[0] in NS["_GCR_FIRST"]


def verified_mailboxes():
    """the mailboxes of $5,000+ buyers read on their own sites on 2026-11-13 (contrib/claude/c5k_mailboxes.py) that the referee re-read before Actions
    stopped (coord/results/verification_log_claude*.csv, outcome verified): {buyer key: (email, type label, grade, page, quote)}, the best one per buyer"""
    import glob as _g
    import parted_csv as _P
    ok = set()
    for f in sorted(_g.glob(os.path.join(ROOT, "coord/results/verification_log_claude*.csv"))):
        it = _P.rows(f) if ".part" in f else csv.DictReader(open(f, encoding="utf-8"))
        for r in it:
            if isinstance(r, dict) and (r.get("task_id") or "").startswith(("C5K-", "C5S-")) and r.get("outcome") == "verified":
                ok.add(((r.get("buyer_key") or ""), (r.get("value") or "").lower(), (r.get("page_url") or "")))
    reread = {}
    try:  # quotes cut short in the crawl's results, read again on 2026-11-14 (the address and its surroundings, visible text)
        reread = json.load(open(os.path.join(ROOT, "data/incoming/claude/c5k_quote_rereads.json"), encoding="utf-8"))
    except (OSError, ValueError):
        pass
    cands = collections.defaultdict(list)
    for f in sorted(_g.glob(os.path.join(ROOT, "data/incoming/claude/claude_buyer_ap_results_c5k*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            k, e, u = (r.get("buyer_key") or ""), (r.get("ap_email") or "").strip().lower(), (r.get("evidence_url") or "")
            if (k, e, u) not in ok or "@" not in e or WEBMAIL.match(e.split("@")[-1]) or NS["BAD_LOCAL"].search(e.split("@")[0]) or e in REVIEWED_OUT \
                    or _person_local(e.split("@")[0]):
                continue
            lab, gr = TYPE_LABEL.get((r.get("ap_email_type") or "general").lower(), ("general", 1))
            q = re.sub(r"(?i)href\s*=\s*[\"']?mailto:([^\"'>\s?]+)[^>]*>", r"> \1 ", r.get("evidence_quote") or "")  # a mailto link: its address is what the page prints
            q = re.sub(r"<[^>]*>|<[^>]*$|^[^<>]*>", " ", q)  # tags, and a tag cut at either end of the quote
            q = re.sub(r"\s+", " ", html.unescape(q)).strip()
            i = q.lower().find(e)
            q = (q[max(0, i - 140): i + len(e) + 140] if i >= 0 else q).strip()
            if e not in q.lower() and k in reread and e in reread[k]["quote"].lower():
                q = reread[k]["quote"]
            if e in q.lower():  # §2.4: the quote carries the value — a mailbox whose quote does not show it is not written
                cands[k].append((gr, e, lab, u, q[:300], r.get("retrieved_date") or "2026-11-13"))
    best = {}
    for k, l in cands.items():
        gr, e, lab, u, q, d = sorted(l, key=lambda t: -t[0])[0]
        best[k] = (e, lab, gr, u, q, d)
    return best


VERIFIED = verified_mailboxes()
norm, host_of, SHARED_GOV, DOMAIN_NAME = NS["norm"], NS["host_of"], NS["SHARED_GOV"], NS["DOMAIN_NAME"]
KIND_N, HOW_N = "no relationship record", "no relationship record"
assert KIND_N in SRC and NS["generic_name_not_this_org"] and NS["_DUP_PLATFORM"]

LOGGED = ("buyer", "buyer_website", "buyer_address", "vendor_website", "vendor_address", "buyer_legal_name_as_published", "email", "email_type", "contract_title", "vendor_legal_name", "bill_amount_indicative", "bill_amount_calculated", "bill_amount_basis", "bill_items_as_published",
          "bill_delivery_as_published", "bill_payment_method_as_published", "bill_due_terms_as_published", "service_stops_if_unpaid",
          "bill_remit_to_as_published", "ship_ready", "ship_ready_missing", "amount_mark", "payment_route", "payment_route_basis", "tier",
          "relationship_kind", "invoice_fields_missing_for_kind")

# the CMEQ's and the CMMTQ's own fees (contrib/claude/rank_buyers/rank.py bill_profile, 2026-11-14), word for word
RBQ_TAB = ("the Régie du bâtiment du Québec's fee table “Maintien d’une licence – 2026” (droits + frais = total): “Général (annexe I) 884,54 $ 105,27 $ 989,81 $”, "
           "“Général et spécialisé (annexes I, II et III) 884,54 $ 105,27 $ 989,81 $”, “Spécialisé (annexes II et III) 442,26 $ 105,27 $ 547,53 $” "
           "(https://www.rbq.gouv.qc.ca/licence/tarification-et-amendes/tarification-pour-lentrepreneur-de-construction/, read 2026-11-11)")
assert "Maintien d’une licence – 2026" in SRC and "Cotisation annuelle de 881 $" in SRC  # the same words as rank.py's


def corporation_fees(x):
    vn = norm(x.get("vendor") or "")
    if not str(x.get("bill_amount_basis") or "").startswith("the Régie du bâtiment du Québec's fee table"):
        return {}
    gen = bool(re.search(r"g[ée]n[ée]ral", x.get("contract_title") or "", re.I))
    mt = "989.81" if gen else "547.53"
    if "maitres mecaniciens en tuyauterie" in vn:
        return {"bill_amount_indicative": "881 $ a year in dues + %s $ a year to keep the licence" % mt,
                "bill_amount_calculated": "calculated — %s $ a year: the CMMTQ's two yearly fees added, its dues (881 $) and the fee to keep the licence (%s $)" % (format(881 + float(mt), ",.2f"), mt),
                "bill_amount_basis": ("the CMMTQ's own leaflet “Taux horaires de référence — Tuyauteur” of 1 January 2026: “Cotisation annuelle de 881 $ à la Corporation” … “des maîtres "
                                      "mécaniciens en tuyauterie du Québec (CMMTQ).” and “Frais annuel de maintien de licence de 547,53 $.” (https://www.cmmtq.org/client_file/upload/pdf/Taux/"
                                      "Taux-horaires-tuyauteurs-janvier-2026.pdf, read 2026-11-14)%s" % (("; this licence also carries general categories: " + RBQ_TAB) if gen else "")),
                "bill_items_as_published": "the CMMTQ's yearly dues (“Cotisation annuelle”) and the yearly fee to keep the contractor's licence (“Frais annuel de maintien de licence”)"}
    if "maitres electriciens" in vn:
        return {"bill_amount_indicative": "837.94 $ a year in dues (1 August 2022) + %s $ a year to keep the licence (2026)" % mt,
                "bill_amount_calculated": ("calculated — about %s $ a year: the CMEQ's dues, 837.94 $ (its latest published figure, 1 August 2022), and the fee to keep the "
                                           "licence in 2026, %s $" % (format(837.94 + float(mt), ",.2f"), mt)),
                "bill_amount_basis": ("the CMEQ's own leaflet of January 2023: “Corporation des maîtres électriciens du Québec Cotisation annuelle 837,94 $ au 1er août 2022 Maintien de "
                                      "licence 507,51 $” (https://www.cmeq.org/fileadmin/user_upload/documents/Documents_administratifs/DE%CC%81PLIANT_janv2023_02.pdf, read 2026-11-14); "
                                      "the fee to keep the licence in 2026: " + RBQ_TAB),
                "bill_items_as_published": ("the CMEQ's yearly dues (“Cotisation annuelle”) and the yearly fee to keep the contractor's licence (“Maintien de licence”), on its yearly "
                                            "notice (“avis de cotisation”)")}
    return {}


def fix_name(x):
    """the buyer-name rules of rank.py's row stage (2026-11-13/14), in the same order; (new name, fault or '')"""
    g = NS
    b, w, fault = (x.get("buyer") or "").strip(), x.get("buyer_website") or "", ""
    dom = (registrable(host_of(w) or "") or "") if w else ""
    if re.search(r"&(?:amp|#\d+|#x[0-9a-f]+|quot|apos|lt|gt|nbsp|rsquo|lsquo|eacute|egrave|agrave|ccedil);", b, re.I):
        b = html.unescape(html.unescape(b)).strip()
    if re.search(r"\s[·•|–—:-]+$", b):
        b = re.sub(r"\s[·•|–—:-]+$", "", b).strip()
    if g["_IMG_NAME"].search(b):
        if w:
            b = dom or b
        else:
            fault = "the name is an image's file name (“%s”), not the organisation's name" % b[:80]
    m = re.match(r"(?i)visit\s+(.{3,90}?)[’']s\s+(?:web\s?site|site|page)$", b)
    if m:
        b = m.group(1).strip()
    hb = g["strip_home_word"](b)
    if hb != b and len(hb) >= 3 and not re.search(r"home|accueil", re.sub(r"[^a-z]", "", dom.lower())):
        b = hb
    lb = g["_LOGO_WORD"].sub("", b)
    lb = lb.strip(" -–—|:/.") if lb != b else b
    if lb != b and len(lb) >= 3 and "logo" not in dom.lower():
        b = lb
    if "�" in b and w:
        b = dom or b
    b = g["name_from_page_words"](b, w)
    if g["place_name_not_this_org"](b, w):
        b = dom or b
    if g["generic_name_not_this_org"](b, w):
        if w and not SHARED_GOV.match(dom):
            b = dom or b
        else:
            fault = "the name is one word of a trade (“%s”), not the organisation's name" % b[:80]
    if g["_JUNK_NAME"].match(b) and w:
        b = dom or b
    else:
        b2 = g["_TITLE_PREFIX"].sub("", b)
        if b2 != b and len(b2) >= 3:
            b = b2
    if b.endswith("/") and DOMAIN_NAME.fullmatch(b.rstrip("/").lower()):
        b = b.rstrip("/")
    # what a cut title leaves at either end ("Luxe Bistro > Home" → "Luxe Bistro >", "McNeil Designs, Home" → "McNeil Designs,", "World Bank Group - IBRD - -")
    b2 = re.sub(r"^[\s,;:>|/·•»«~\-–—]+|[\s,;:>|/·•»«~\-–—]+$", "", b)
    if b2 != b and len(b2) >= 3:
        b = b2
    # the last cleaning of a name read from a page title (title_names.py: an address, a mailbox, a telephone number, "Home page", "Official site",
    # "under construction", a slogan, a breadcrumb, a town and province after the name …), each rule read against the rows it changes
    b, rule = TN.clean_title_name(b, (dom.split(".")[0] if dom else ""), dom)
    # 2026-11-14: a person-name test (a first name and a surname, the site named after them) was tried and left out: it took "Tim Hortons" and "Paul Davis"
    # (companies named after their founders) and missed "Gidget Ovsenek" (a first name not on the list) — a one-person practice that presents itself as a
    # business, with its own site and a role mailbox, stays a buyer; natural persons on registers and rosters were left out at harvest (coord/DECISIONS.md)
    return b, fault, rule


# a mail provider's or an internet provider's domain is no organisation's own site: written as the buyer's site from the domain of its mailbox
# (2026-11-14: "Municipalité Village Saint-Pierre" with videotron.ca, "Long Point First Nation" with sympatico.ca) — unless the buyer is that provider
MAIL_PROVIDER = re.compile(r"^(?:videotron\.(?:ca|com|net)|bell\.net|bellnet\.ca|sympatico\.ca|shaw\.ca|rogers\.com|cogeco\.(?:ca|net)|telus\.net|eastlink\.ca|"
                           r"globetrotter\.net|xplornet\.(?:ca|com)|tbaytel\.net|mts\.net|sasktel\.net|nbnet\.nb\.ca|gmail\.com|hotmail\.(?:com|ca)|outlook\.com|"
                           r"yahoo\.(?:com|ca)|live\.(?:com|ca)|icloud\.com|aol\.com|msn\.com)$")
BUYER_SITE_FIELDS = ("buyer_logo_url", "buyer_linkedin_url", "buyer_supplier_portals_linked")
VENDOR_SITE_FIELDS = ("vendor_emails", "vendor_phone", "vendor_contact_evidence_url", "vendor_logo_url", "vendor_linkedin_url", "vendor_billing_ar_email")


def _dom(u):
    return (registrable(host_of(u) or "") or "") if u else ""


def _sqn(t):
    return re.sub(r"[^a-z0-9]", "", norm(re.sub(r"^inferred:\s*", "", t or "")))


def provider_site(x):
    """the buyer's site that is a mail provider's domain: the cells to clear ({} if none) — before the name is cleaned, which falls back on the site"""
    bd = _dom(x.get("buyer_website") or "")
    if bd and MAIL_PROVIDER.match(bd) and bd.split(".")[0] not in _sqn(x.get("buyer") or ""):
        return {"buyer_website": "", **{c: "" for c in BUYER_SITE_FIELDS},
                "buyer_website_status": "removed 2026-11-14: %s is a mail provider's domain, taken from the organisation's mailbox — not its own site" % bd}
    return {}


def site_faults(x):
    """a vendor's site that is the buyer's own, and a body billing itself: (cells to clear, row fault or '', what was found)"""
    bd, vd = _dom(x.get("buyer_website") or ""), _dom(x.get("vendor_website") or "")
    sq = _sqn
    out, fault, what = {}, "", ""
    same_name = sq(x.get("buyer")) and sq(x.get("buyer")) == sq(x.get("vendor"))
    same_site = bd and vd and bd == vd and not SHARED_GOV.match(bd) and not NS["_DUP_PLATFORM"].search(bd)
    if same_name or (same_site and (RR.kind_of(x) == "service seen on the buyer's side" or sq(x.get("buyer")) in sq(x.get("vendor")) or sq(x.get("vendor")) in sq(x.get("buyer")))):
        fault = ("relationship: the organisation and the biller are one (%s) — a body does not bill itself; a chapter or a branch named by its parent's name"
                 % ("the same name" if same_name else "the same website, %s" % bd))
        what = "the organisation and the biller are one: no relationship"
    elif same_site:
        for c in ("vendor_legal_name", "vendor_address"):  # read on that site: the buyer's words, not the vendor's
            if vd in (x.get(c) or "").lower():
                out[c] = ""
        out.update({"vendor_website": "", **{c: "" for c in VENDOR_SITE_FIELDS},
                    "vendor_website_status": "removed 2026-11-14: %s is the buyer's own site, not the vendor's" % vd,
                    "vendor_website_basis": "removed 2026-11-14: the vendor's site was the buyer's own (%s); what was read on it is not written" % vd})
        what = "vendor's site: the buyer's own, removed with what was read on it"
    return out, fault, what


def weak_legal_page_name(x):
    """a vendor legal name read on a legal page by a shared word alone: no legal form, and not the vendor's own name (rank.py, 2026-11-14)"""
    m = re.match(r"^(.*?) \(stated on the vendor's legal page", x.get("vendor_legal_name") or "")
    if not m:
        return False
    return NS["weak_legal_page_name"](m.group(1).strip(), x.get("vendor") or "", x.get("vendor_website") or "")


def patch_invoice_views(x, old_buyer, old_vlegal, old_amount, old_blegal=None):
    """the draft invoice header and card the build wrote from the old cells: the corrected names and amount written into them"""
    t = x.get("invoice_text") or ""
    if t:
        lines = t.split("\n")
        for i, l in enumerate(lines):
            if l.startswith("BILL TO: ") and old_buyer and old_buyer != x.get("buyer") and old_buyer in l:
                l = lines[i] = l.replace(old_buyer, x.get("buyer") or "", 1)
            if l.startswith("BILL TO: ") and old_blegal and old_blegal in l:
                lines[i] = l.replace(old_blegal, x.get("buyer") or "", 1)
            if l.startswith("FROM / REMIT TO: ") and old_vlegal is not None:
                lines[i] = l.replace(old_vlegal, re.sub(r"^inferred:\s*", "", x.get("vendor") or "") or "(vendor legal name not confirmed)", 1)
            if l.startswith("DESCRIPTION: ") and old_amount and old_amount in l:
                lines[i] = l.replace(old_amount, x.get("bill_amount_indicative") or "", 1)
        x["invoice_text"] = "\n".join(lines)[:1500]
    c = x.get("invoice_card_json") or ""
    if c:
        try:
            card = json.loads(c)
        except ValueError:
            card = None
        if isinstance(card, dict):
            bt, vi = card.get("bill_to") or {}, card.get("vendor_identity") or {}
            if old_buyer and old_buyer != x.get("buyer") and bt.get("legal_name") == old_buyer:
                bt["legal_name"] = x.get("buyer") or ""
            if old_blegal and bt.get("legal_name") == old_blegal:
                bt["legal_name"], bt["legal_name_is_published"] = x.get("buyer") or "", False
            if old_vlegal is not None and vi.get("legal_name") == old_vlegal:
                vi["legal_name"] = re.sub(r"^inferred:\s*", "", x.get("vendor") or "")
            x["invoice_card_json"] = json.dumps(card, ensure_ascii=False)
    if old_vlegal is not None and x.get("invoice_readiness"):
        m = re.match(r"(\d+)/(\d+) (.*)", x["invoice_readiness"])
        if m and "vendor legal name" not in (x.get("invoice_missing") or ""):
            x["invoice_readiness"] = "%d/%s %s" % (max(0, int(m.group(1)) - 1), m.group(2), m.group(3))
            x["invoice_missing"] = "; ".join(p for p in ((x.get("invoice_missing") or ""), "vendor legal name") if p)


def correct(src, outdir):
    os.makedirs(outdir, exist_ok=True)
    n, ex = collections.Counter(), collections.defaultdict(list)
    fin = gzip.open(src, "rt", encoding="utf-8", newline="")
    rd = csv.DictReader(fin)
    head = rd.fieldnames
    fo = gzip.open(os.path.join(outdir, "ranked_buyers.csv.gz"), "wt", encoding="utf-8", newline="", compresslevel=6)
    wr = csv.DictWriter(fo, fieldnames=head, extrasaction="ignore")
    wr.writeheader()
    fl = gzip.open(os.path.join(outdir, "corrections.csv.gz"), "wt", encoding="utf-8", newline="")
    wl = csv.writer(fl)
    wl.writerow(["row_key", "buyer", "field", "before", "after"])
    for x in rd:
        n["rows"] += 1
        before = {c: x.get(c) or "" for c in LOGGED}
        old_ready = before["ship_ready"].startswith("yes")
        # 1. the buyer's name
        pclear = provider_site(x)
        if pclear:
            x.update(pclear)
            n["buyer's site: a mail provider's domain, removed"] += 1
        nb, fault, trule = fix_name(x)
        old_buyer = x.get("buyer") or ""
        if nb != old_buyer.strip():
            x["buyer"] = nb
            n["buyer name corrected"] += 1
            for r_ in (trule.split("; ") if trule else []):
                n["buyer name corrected — " + r_] += 1
            if len(ex["name"]) < 12:
                ex["name"].append((old_buyer[:60], nb[:60]))
        # 1b. a mail provider's domain as the buyer's site; the buyer's own site as the vendor's; a body billing itself
        sclear, sfault, swhat = site_faults(x)
        if sclear:
            x.update(sclear)
        if swhat:
            n[swhat] += 1
        if sfault:
            x["row_fault"] = sfault
        # 1c. a named person's mailbox (§2.5) comes off; a mailbox for queries only says so
        em = (x.get("email") or "").strip().lower()
        if em in PERSON_MAILBOX:
            for c in MAIL_COLS:
                x[c] = ""
            x["mailbox_recheck_note"] = "removed 2026-11-14: %s own mailbox (a named person's; AGENTS.md §2.5)" % PERSON_MAILBOX[em]
            n["mailbox removed: a named person's"] += 1
        elif _dom(x.get("buyer_website") or "") in WRONG_SITE:
            why_ = WRONG_SITE[_dom(x.get("buyer_website") or "")]
            for c in MAIL_COLS + ("buyer_website",) + BUYER_SITE_FIELDS:
                x[c] = ""
            x["buyer_website_status"] = x["mailbox_recheck_note"] = "removed 2026-11-14: " + why_
            n["site and mailbox removed: a namesake's site"] += 1
        elif em in TYPE_OVERRIDE:
            x["email_type"], x["grade"], x["email_evidence_context"] = TYPE_OVERRIDE[em][0], str(TYPE_OVERRIDE[em][1]), TYPE_OVERRIDE[em][2]
            n["mailbox: its role corrected from its own page"] += 1
        # 1d. a U.S. EPA hazardous-waste export notice: the vendor is the receiving facility in Canada (FINAL ADDRESS); the address in the vendor's cell
        # was the exporter's own (the shipper) — it is the buyer's
        vb = x.get("vendor_country_basis") or ""
        mf = re.search(r"FINAL ADDRESS / FINAL COUNTRY \(EPA WIETS WT_NOTICES_EXPORTS\)=(.+)$", vb)
        if mf and "SHIPPER COUNTRY" in (x.get("vendor_address") or ""):
            ship = re.sub(r";\s*SHIPPER COUNTRY:.*$", "", x.get("vendor_address") or "").strip()
            x["vendor_address"] = "%s (the receiving facility: FINAL ADDRESS of the U.S. EPA hazardous-waste export notice)" % mf.group(1).strip()
            if not (x.get("buyer_address") or "").strip():
                x["buyer_address"] = "%s (the exporter's facility: the shipper's address in the same U.S. EPA export notice)" % ship
            n["vendor address: the receiving facility of an EPA export notice (the shipper's address was in its place)"] += 1
        # 1e. the buyer's address against web platforms' own addresses and against the country of its site and mailbox (address_checks.py)
        try:
            na_, afault, awhat = AC.check(x, RR.kind_of(x), registrable)
        except Exception as e_:  # never seen on the 362,839 rows of the first corrected copy
            na_, afault, awhat = None, "", "address check failed on the row (kept as it was): %s" % type(e_).__name__
        if na_ is not None:
            removed = [q for q in AC.split_parts(x.get("buyer_address") or "") if q not in AC.split_parts(na_)]
            for q in removed:
                bq = AC.body_of(q)
                if bq and bq in (x.get("invoice_text") or ""):
                    x["invoice_text"] = x["invoice_text"].replace(bq, "(address not published)", 1)
                if bq and bq in (x.get("invoice_card_json") or ""):
                    x["invoice_card_json"] = x["invoice_card_json"].replace(json.dumps(bq, ensure_ascii=False)[1:-1], "", 1)
            x["buyer_address"] = na_
        if awhat:
            n[awhat] += 1
        if afault:
            x["row_fault"] = " ;; ".join(f_ for f_ in ((x.get("row_fault") or ""), afault) if f_)
        if fault:
            x["buyer_name_fault"] = fault
            n["buyer name: not a name and no site of its own (the row is not ready)"] += 1
        # 2. a vendor legal name read on a legal page by a shared word only
        old_vlegal = None
        if weak_legal_page_name(x):
            old_vlegal = (x.get("vendor_legal_name") or "").split(" (stated on")[0]
            x["vendor_legal_name"] = ""
            n["vendor legal name cleared (a sentence of a legal page, no legal form, not the vendor's name)"] += 1
            if len(ex["vlegal"]) < 12:
                ex["vlegal"].append((old_vlegal[:60], (x.get("vendor") or "")[:40]))
        # 3. the CMEQ's and the CMMTQ's own fees
        old_amount = x.get("bill_amount_indicative") or ""
        cf = corporation_fees(x)
        if cf:
            x.update(cf)
            n["CMEQ / CMMTQ licence: the corporation's own dues and fee"] += 1
        else:
            old_amount = ""
        # 4. what the bodies read by hand publish about their bills (tools/payee_billing.py; only cells left empty, as the build does)
        if (x.get("tier") or "") != "T":
            out = {}
            PB.fill(out, x, x.get("vendor") or "", x.get("vendor_website") or "")
            added = [c for c, v in out.items() if v and not str(x.get(c) or "").strip()]
            for c in added:
                x[c] = out[c]
            if added:
                n["bill details added from a body's own page (payee entries verified after the build)"] += 1
        # 5a. a mailbox the referee re-read on 2026-11-13 for a buyer that had none on the row
        if not (x.get("email") or "").strip():
            hit = next((VERIFIED[k] for k in (x.get("keys") or "").split("|") if k in VERIFIED), None)
            if hit:
                e, lab, gr, u, q, d = hit
                x.update({"email": e, "email_type": lab, "email_check": "confirmed (the referee re-read the page; coord/results/verification_log_claude.csv)",
                          "email_evidence_url": u, "email_evidence_quote": q, "grade": str(gr), "acc": "True",
                          "mailbox_provenance": "read on the organisation's own site by contrib/claude/c5k_mailboxes.py on %s, re-read by the referee; written by the final "
                                                "correction (contrib/claude/final_correction/correct_table.py)" % d})
                n["mailbox added (re-read by the referee before Actions stopped)"] += 1
                if e in TYPE_OVERRIDE:
                    x["email_type"], x["grade"], x["email_evidence_context"] = TYPE_OVERRIDE[e][0], str(TYPE_OVERRIDE[e][1]), TYPE_OVERRIDE[e][2]
                    n["mailbox: its role corrected from its own page"] += 1
        # 5b. municipalities outside Ontario that stand on where they are: their electricity from their own residents (tools/muni_energy.py)
        if MUNI_MAIN and (x.get("tier") or "") == "I" and RR.kind_of(x) == "utility account by location":
            pc = BYLOC.code_of(x.get("buyer_address") or "")
            pv = BYLOC._PROV_OF_FIRST.get(pc[0], "") if pc else ((x.get("jurisdiction") or "")[:2] if (x.get("jurisdiction") or "")[:2] in MUNI_MAIN else "")
            if pv in MUNI_MAIN and re.sub(r"^inferred:\s*", "", x.get("vendor") or "") == MUNI_MAIN[pv]:
                mm = MUNI.match(x.get("buyer") or "", pv, x.get("buyer_website") or "")
                ee = MUNI.estimate(mm["pop"], pv) if mm else None
                if ee:
                    x["bill_amount_calculated"] = MUNI.sentence(mm, ee, pv)
                    x["contract_title"] = "Electricity service to the municipality's facilities (its town hall's address: %s)" % ((x.get("buyer_address") or "").split(" (")[0][:120])
                    n["municipality outside Ontario: electricity estimated from its residents" + (" ($5,000 a month or more)" if ee["p25"] >= 5000 else "")] += 1
        # 5c. the price or value of a member benefit is not the dues (rank.py _NOT_DUES, 2026-11-13)
        mq = re.search(r"lowest published (?:membership )?fee by the (?:year|month): “(.+?)” \(", x.get("bill_amount_basis") or "")
        if mq and NS["_NOT_DUES"].search(mq.group(1)):
            x["bill_amount_indicative"], x["bill_amount_basis"] = "", ""
            n["member dues amount cleared (a benefit's price or value, not the dues)"] += 1
        # 5d. a federal grant recipient whose legal name is a person's own name (a sole proprietor) is not written
        old_blegal = None
        mb = re.match(r"^(.*) \(recipient legal name in the federal grants & contributions disclosure\)$", x.get("buyer_legal_name_as_published") or "")
        if mb and NS["_GCR_PERSON"](mb.group(1)):
            old_blegal = mb.group(1)
            x["buyer_legal_name_as_published"] = ""
            n["buyer legal name cleared (a sole proprietor's own name)"] += 1
        # 5. a row with no vendor at all is no relationship record
        if not (x.get("vendor") or "").strip() and (x.get("tier") or "") not in ("N", "I", "R"):
            x["tier"], x["rank_group"] = "N", "N%s" % (x.get("grade") or 0)
            x["relationship_kind"], x["how_relationship_was_found"] = KIND_N, HOW_N
            n["row with no vendor at all: no relationship record"] += 1
        # 6. the owner's test, as it stands now (rule 19 by name, foundations, province conflicts, no address, buyer not named …)
        try:
            kind, route, faults = RR.owner_test(x)
        except Exception as e:  # never seen on the 362,875 rows of 22:10Z; kept as it was if it happens
            n["owner test failed on the row (kept as it was): %s" % type(e).__name__] += 1
            faults = None
        x.pop("buyer_name_fault", None)
        x.pop("row_fault", None)
        if faults is not None:
            new_ready = not faults
            if old_ready and not new_ready:
                n["ready -> not ready"] += 1
                for f in faults:
                    n["ready -> not ready: " + re.sub(r"\s*\(.*", "", f)[:90]] += 1
            elif new_ready and not old_ready:
                n["not ready -> ready"] += 1
        patch_invoice_views(x, old_buyer.strip(), old_vlegal, old_amount, old_blegal)
        key = next((k for k in (x.get("keys") or "").split("|") if k), "")
        for c in LOGGED:
            a = x.get(c) or ""
            if a != before[c]:
                wl.writerow([key, (x.get("buyer") or "")[:120], c, before[c][:300], a[:300]])
                n["cells changed: " + c] += 1
        n["ready after"] += (x.get("ship_ready") or "").startswith("yes")
        wr.writerow(x)
    fin.close(); fo.close(); fl.close()
    rep = {"counts": dict(n), "examples": {k: v for k, v in ex.items()}}
    json.dump(rep, open(os.path.join(outdir, "counts.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k, v in sorted(n.items()):
        print(v, k)


def fold(outdir):
    """one row per website and name (rank.py, 2026-11-14), on the table in its order of priority: the first row of an organisation stands for it"""
    path = os.path.join(outdir, "ranked_buyers.csv.gz")
    first, extra, drop = {}, collections.defaultdict(set), {}
    with gzip.open(path, "rt", encoding="utf-8", newline="") as f:
        for i, x in enumerate(csv.DictReader(f)):
            h = host_of(x.get("buyer_website") or "") if x.get("buyer_website") else ""
            c = " ".join(w for w in norm(re.sub(r"\s*\([^()]*\)?\s*$", "", x.get("buyer") or "")).split() if w not in NS["_DUP_TYPE"])
            if h and len(c) >= 3 and not NS["_DUP_PLATFORM"].search(h) and not SHARED_GOV.match(registrable(h) or h):
                k = (h, c)
                if k in first:
                    drop[i] = first[k]
                    extra[first[k]] |= {kk for kk in (x.get("keys") or "").split("|") if kk}
                else:
                    first[k] = i
    tmp = path + ".fold"
    n = collections.Counter()
    with gzip.open(path, "rt", encoding="utf-8", newline="") as f, gzip.open(tmp, "wt", encoding="utf-8", newline="", compresslevel=6) as fo, \
            open(os.path.join(outdir, "folded_rows.csv"), "w", encoding="utf-8", newline="") as fd:
        rd = csv.DictReader(f)
        wr = csv.DictWriter(fo, fieldnames=rd.fieldnames)
        wr.writeheader()
        wd = csv.writer(fd)
        wd.writerow(["dropped_buyer", "dropped_website", "dropped_kind", "dropped_ready", "kept_row_number"])
        for i, x in enumerate(rd):
            if i in drop:
                wd.writerow([x.get("buyer"), x.get("buyer_website"), (x.get("invoice_fields_for_kind") or "").split(":")[0], (x.get("ship_ready") or "")[:3], drop[i] + 1])
                n["folded (ready)" if (x.get("ship_ready") or "").startswith("yes") else "folded (not ready)"] += 1
                continue
            if i in extra:
                ks = sorted({kk for kk in (x.get("keys") or "").split("|") if kk} | extra[i])
                x["keys"], x["buyer_keys"] = "|".join(ks), str(len(ks))
            wr.writerow(x)
            n["rows"] += 1
    os.replace(tmp, path)
    print("one row per website and name:", dict(n))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["correct"] and len(a) == 3:
        correct(a[1], a[2])
    elif a[:1] == ["fold"] and len(a) == 2:
        fold(a[1])
    else:
        print(__doc__)
