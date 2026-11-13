"""One row per distinct buyer, ranked by proof quality and completeness (see README.md). Run from anywhere:
    gh release download dataset-latest -D data/release   # once (needs canadian_vendor_contracts; vendors_enriched, buyers_enriched,
                                                          # vendor_country_unverified_contracts and ended_* are optional: P12 + field fill)
    python3 contrib/claude/rank_buyers/rank.py && python3 contrib/claude/rank_buyers/batches.py
"""
import csv, gzip, json, re, io, collections, unicodedata, datetime, sys, os, zlib, html
import builtins as _bi, time as _tm
_T0 = _TL = _tm.time()
def print(*a, **k):
    """every progress line carries the seconds since the start and since the line before: the row count is meant to grow tenfold, and this
    shows which step stops scaling (2026-11-10: a build took 30+ minutes at 69,000 rows)"""
    global _TL
    _now = _tm.time()
    try:  # the process's memory right now (GB): the row count is meant to grow tenfold and the runner has 16 GB
        with open("/proc/self/statm") as _f:
            _rss = int(_f.read().split()[1]) * 4096 / 1073741824
    except Exception:
        _rss = 0.0
    _bi.print("[%5.0fs +%4.0fs %4.1fG]" % (_now - _T0, _now - _TL, _rss), *a, **k)
    _TL = _now


def _memstat(label, rows, g=None):
    """RANK_MEMSTAT=1: what a row costs in memory right now, by tier and by column (1 row in 25; a string object shared by several rows counts once)"""
    import os as _os, sys as _s, json as _j, collections as _c
    if not _os.environ.get("RANK_MEMSTAT"):
        return
    seen, by_col, by_tier = set(), _c.Counter(), _c.defaultdict(lambda: [0, 0, 0])
    smp = rows[::25]
    for x in smp:
        b = _s.getsizeof(x)
        for c, v in x.items():
            if c == "_org" or v == "" or id(v) in seen:
                continue
            seen.add(id(v))
            sz = _s.getsizeof(v) if isinstance(v, (str, int, float, bool)) else len(_j.dumps(v, default=str))
            by_col[c] += sz; b += sz
        t = by_tier[x.get("tier") or "?"]
        t[0] += 1; t[1] += b; t[2] += len(x)
    tot = sum(t[1] for t in by_tier.values())
    _bi.print("    memstat %s: %d rows sampled, %.1f KB a row (dict + its own strings); all rows ~%.2f GB" % (label, len(smp), tot / 1024 / max(1, len(smp)), tot * 25 / 1073741824))
    _bi.print("    by tier (rows, KB a row, columns a row):", "; ".join("%s %d %.1f %d" % (k, v[0], v[1] / 1024 / max(1, v[0]), v[2] / max(1, v[0])) for k, v in sorted(by_tier.items())))
    _bi.print("    heaviest columns (KB a row):", "; ".join("%s %.2f" % (c, n / 1024 / max(1, len(smp))) for c, n in by_col.most_common(28)))
    if g is None:
        return
    # every big table the script holds at this point (dict / list / set of the module): estimated from 1 entry in 40. An object shared by several
    # entries counts once; another table of the module, or a row, reached from an entry is not followed (it is counted where it lives).
    stop = {id(o) for o in g.values() if isinstance(o, (dict, list, set, tuple))} | {id(x) for x in rows}
    seen2, budget = set(), [0]
    def deep(o, d=0):
        if id(o) in seen2 or id(o) in stop or budget[0] > 3000000:
            return 0
        seen2.add(id(o)); budget[0] += 1
        n = _s.getsizeof(o)
        if d > 5:
            return n
        if isinstance(o, dict):
            for k, v in o.items():
                n += deep(k, d + 1) + deep(v, d + 1)
        elif isinstance(o, (list, tuple, set, frozenset)):
            for v in o:
                n += deep(v, d + 1)
        return n
    hold, rid = [], {id(x) for x in rows}
    for name, o in list(g.items()):  # a table that still refers to rows keeps them alive after they are written
        if name == "rows" or not isinstance(o, (dict, list, set, tuple)):
            continue
        n = 0
        for v in (o.values() if isinstance(o, dict) else o):
            if id(v) in rid:
                n += 1
            elif isinstance(v, (list, tuple)):
                n += sum(1 for w in v if id(w) in rid)
        if n > 1:
            hold.append("%s %d" % (name, n))
    _bi.print("    tables that still refer to rows:", "; ".join(hold) or "none")
    out = []
    for name, o in list(g.items()):
        if name == "rows" or not isinstance(o, (dict, list, set, tuple)) or len(o) < 2000:
            continue
        step = 40 if len(o) >= 4000 else 1
        n = _s.getsizeof(o)
        for i, e in enumerate(o.items() if isinstance(o, dict) else o):
            if i % step == 0:
                n += (deep(e[0]) + deep(e[1]) if isinstance(o, dict) else deep(e)) * step
        out.append((n, name, len(o)))
    out.sort(reverse=True)
    _bi.print("    tables held (name entries ~MB):", "; ".join("%s %d %.0f" % (nm, ln, n / 1048576) for n, nm, ln in out[:40] if n > 8 * 1048576))
    _bi.print("    all tables ~%.2f GB (objects visited: %d)" % (sum(n for n, _, _ in out) / 1073741824, budget[0]))


def _free(g, *names):
    """a table is dropped right after its last use: the tables around the rows are most of the memory (2026-11-10: 4.2 GB of 5.8 GB)"""
    import gc
    for n in names:
        g.pop(n, None)
    gc.collect()


def _money(v):
    """contract_value as it should print on an invoice: 2 decimals, thousands separators (the records carry floats such as 416594.66000000003)"""
    try:
        return "{:,.2f}".format(float(str(v).replace(",", "").replace("$", "").strip()))
    except (TypeError, ValueError):
        return str(v)


ROOT = __import__("os").path.abspath(__import__("os").path.join(__import__("os").path.dirname(__file__), "../../.."))
sys.path.insert(0, ROOT + "/tools"); sys.argv = sys.argv[:1]
import urllib.parse
import relationship_rows as _RR  # (imported again below where the owner's test is used) — here for is_ceiling while a buyer's record is chosen
from ap_crawler import same_org, registrable  # the buyer's own mailbox, not a contractor's or partner's named on its pages
from ap_crawler import OTHER_ROLE as _CRAWL_ROLE, GENERAL as _CRAWL_GENERAL
# 2026-11-10: the big files that engines rewrite whole are release assets, not git blobs (tools/state_io.py, coord/STATE_ASSETS.json):
# a fresh checkout fetches the current version of each before it is read
try:
    import state_io as _state_io
    for _sp in ("coord/results/team_buyers.jsonl.gz", "data/incoming/claude/claude_org_extras.jsonl.gz", "data/incoming/claude/claude_org_contacts.jsonl.gz",
                "data/incoming/claude/claude_ap_terms_pages.csv.gz"):
        if not _state_io.ensure(os.path.join(ROOT, _sp), quiet=False):
            print("state asset not available:", _sp)
except Exception as _e:
    print("state assets not checked:", _e)
today = datetime.date.today().isoformat()
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()
LEGAL_END = re.compile(r"\s+(corporation|corp|incorporated|inc|limited|ltd|llc|co|company|ltee|ltée)$")
SQ_STOP = {"sante", "quebec", "universitaire", "etablissement", "ciusss", "cisss", "de", "du", "des", "d", "l", "la", "le", "les", "et"}
def parent(n):
    if norm(n).startswith("sante quebec"):  # Santé Québec's regional establishments (former CISSS / CIUSSS / CHU) stay distinct
        words = [w for w in norm(re.sub(r"\(.*?\)|[’']", " ", n)).split() if w not in SQ_STOP]
        return "sante quebec " + " ".join(words) if words else "sante quebec"
    p = norm(re.split(r"\s+[-–—(/|]\s*", n or "")[0])
    p = re.sub(r"^the\s+", "", p)
    for _ in range(2):
        p = LEGAL_END.sub("", p)
    return p.strip()
GRADE = {"invoice_submission": 4, "accounts_payable": 4, "supplier_payment": 4, "finance": 3, "procurement": 2, "general": 1}
LABEL_G = {4: "invoicing/AP", 3: "finance/accounting dept or supplier-payment office", 2: "purchasing", 1: "general", 0: ""}  # one label per grade, everywhere
FIN = re.compile(r"compt|financ|tresor|treasur|account|fiscal", re.I)  # finance / accounting department mailbox
STRONG = re.compile(r"^cap$|[._-]cap$|(?<!manu)factur|invoic|invsub|inv[._-]sub|payable|payables|compt\w*pay|comptesapayer|^ap$|^ap[._-]|[._-]ap$|[._-]ap[._-]|accounts?[._-]?pay|fournisseur|supplier|vendor|paiement|payment|paymt|apinvoice", re.I)
QUOTE_AP = re.compile(r"(?<!manu)factur|invoice|payable|comptes? (à|a) payer|accounts payable|paiement des fournisseurs|supplier payment", re.I)
ROLEISH = re.compile(r"(?<!manu)factur|invoic|bill|payable|compt|account|financ|tresor|treasur|fourniss|supplier|vendor|approv|achat|purchas|procure|"
                     r"paiement|payment|acquisition|^ap$|^ap[._-]|[._-]ap$|info|contact|reception|admin|general|greffe|mairie|municipal|"
                     r"townhall|cityhall|clerk|office|bureau|secretar|accueil|hello|inquir|enquir|renseign|direction|courrier|mail|service|"
                     r"support|commande|order|depot|deposit|ddenrol|dpf|cap$|contrat|contract|appel|tender|soumission|ville|city|town|"
                     r"^dg$|^dg[._-]|directeur|directrice|director|maire|mayor|secretai|inspect|assistan|registr|communic|taxe|^tax|parc|park|"
                     r"^mun|mrc|^crd|^rcm|capital|works|travaux|urbanis|loisir|recreat|biblio|librar|clerk|operat|technique|informatique|"
                     r"helpdesk|aide|help|desk|soutien|centre|center|office|bureau|projet|project|program|dept|division|team|equipe|group|"
                     r"^pacs|admission|registraire|evaluation|assessment|engineering|genie|environnement|environment|transport|public|"
                     r"police|fire|incendie|securite|safety|sante|health|hr$|rh$|paie|payroll|legal|juridique|planning|permis|permit|"
                     r"water|eau|aqueduc|egout|sewer|waste|dechet|matieres|council|conseil|board|commission|municipalit|village|canton|"
                     r"paroisse|county|comte|regie|corporation|society|societe|association|federation|institut|universit|college|cegep|ecole|school|"
                     r"customer|care|client|rfp|rfq|procserv|^proc|invsub|inv[._-]sub|guichet|adjoint|^fin$|^acc$|^accts?$|^acct$|^pay$|^inv$|^fact$|^ar$|^cp$|^cap$|^finance$|^payables?$|"
                     # 2026-11-10: the front-office role mailboxes tools/ap_crawler.py keeps as the last resort (OTHER_ROLE: sales@, bookings@, bonjour@ …)
                     r"sales|vente|bonjour|^allo$|^salut$|welcome|bienvenue|connect|^ask$|question|demande|request|booking|reserv|siege|corporate|management|^gm$|^ops$|^shop|^store|"
                     r"boutique|magasin|estimat|^quotes?$|^devis$|rental|^parts$|^pieces$|courriel|^sac$|^hi$|^main$", re.I)
STRONG_ANY = re.compile(r"(?<!manu)factur|invoic|payable|comptesapayer|accountspayable|comptespayables|apinvoice|invsub", re.I)
try:
    from buyer_pages import FIRST_NAMES as _FIRST
except Exception:
    _FIRST = set()
PERSON_OK2 = {"payables", "payable", "invoices", "invoice", "factures", "facturation", "comptabilite", "finance", "finances", "ap", "ar", "accounting", "accounts", "achats", "purchasing"}
def roleish(local, org=""):
    toks = [t for t in re.split(r"[._+-]+", local.lower()) if t]
    if len(toks) == 2 and toks[0] in _FIRST and len(toks[1]) >= 3 and not STRONG_ANY.search(local) and toks[1] not in PERSON_OK2:
        return False  # first.last: a person (Marie Paiement, Jean Comptois) even when the surname looks like a role word
    if STRONG_ANY.search(local) or any(ROLEISH.match(t) or ROLEISH.match(t[1:] if len(t) > 3 and t[0].isdigit() else t) for t in toks):
        return True
    if _CRAWL_ROLE.search(local.lower()) or _CRAWL_GENERAL.search(local.lower()):
        return True  # the mailbox reader's own lists of role words (tools/ap_crawler.py OTHER_ROLE / GENERAL): one list, kept there (2026-11-11: gestion@, leasing@, membership@ …)
    words = [w for w in re.split(r"[^a-z0-9]+", norm(org)) if w]
    acr = "".join(w[0] for w in words if w not in ("de", "du", "des", "la", "le", "les", "of", "the", "and", "et", "d", "l"))
    flat = re.sub(r"[^a-z0-9]", "", local.lower())
    return any(len(w) >= 4 and w in flat for w in words) or (len(acr) >= 2 and acr in flat)
def invoice_near(email, quote):
    q = (quote or "").lower(); i = q.find(email.lower())
    return bool(QUOTE_AP.search(q[max(0, i - 110):i] if i >= 0 else ""))  # the words just before the address send invoices there
def real_grade(email, etype, quote, org=""):
    g = GRADE.get(etype, 1)
    local = email.split("@")[0]
    if not roleish(local, org):
        return -1  # looks like a person's mailbox: never used
    q = (quote or "").lower(); i = q.find(email.lower()); near = q[max(0, i - 160):i + len(email) + 160] if i >= 0 else q[:320]
    if g >= 3 and re.search(r"receivable|recevable|tuition|student account|pay your|pay online|your bill|utility bill|donat|customer service|client payment|paiement de votre|"
                            r"votre facture|vos factures|facture d.imp[ôo]t|compte de taxes|taxes municipales|paiement des? taxes|facture d.eau|imp[ôo]t foncier|"
                            r"droits de scolarit|frais de scolarit|relev[ée] de compte", near) \
            and not re.search(r"payable|payer|supplier|vendor|fournisseur", near):
        g = 1  # a receivable / customer-payment mailbox (customers pay the organisation), not where suppliers send invoices
    if g >= 3 and re.search(r"water|sewer|hydro|utilit|tax|parking|ticket|fine|permit|tuition|fee|donat|rent|licen|bill", local, re.I) \
            and re.search(r"pay|bill", local, re.I) and not re.search(r"payable|supplier|vendor|fourniss", local, re.I):
        g = 1  # waterpayment@, taxpayments@, utilitybilling@: residents pay the organisation
    if g >= 3 and re.search(r"e-?transfer|interac|by cheque|cheque or|cost is \$|fee is \$|\$\s?\d[\d,.]* (?:is )?payable|payable (?:by|via|to the) (?:cheque|e-?transfer|cash|credit|debit|town|village|city|municipalit)|"
                            r"tax roll|late fees|your account number|your tax|your utility|utility and tax|utilities and taxes|pay (?:their|your) bills", near) \
            and not re.search(r"supplier|vendor|fourniss|invoice|factur|payable[s]? (?:department|clerk|inquir)", near) and not STRONG_ANY.search(local):
        g = 1  # spot-check 2026-11-04: payments@ / accounting@ mailboxes published where residents e-transfer their taxes and fees to the town
    if g == 4 and not (STRONG.search(local) or invoice_near(email, quote)):
        g = 2 if re.search(r"procure|purchas|achat|approv", email, re.I) else 1   # labelled AP but nothing says invoicing
    if g < 3 and FIN.search(local) and not re.search(r"procure|purchas|achat|approv|aid|bourse|scholar|tuition|student|etudiant|soutien|financement|funding|grant|subvention|invest|sustainab|bank|loan|pret|credit|client", local, re.I):
        g = 3
    if g == 3 and (STRONG_ANY.search(local) or re.search(r"^ap$|^ap[._-]|[._-]ap$|accounts?[._-]?pay|^cap$|[._-]cap$", local, re.I)):
        g = 4  # named for invoices / accounts payable, whatever label the lane gave it (accountspayable@ filed as "finance")
    if g == 4 and re.search(r"^payments?$|^payment[._-]|[._-]payments?$|^paiements?$", local, re.I) and not re.search(r"invoice|factur|supplier|vendor|fourniss|payable", near):
        g = 3  # deep audit 2026-11-04: payments@ is as often the box residents pay as the one suppliers invoice; without invoice words nearby it is finance-grade
    return g
# 1. best mailbox per buyer key (referee export)
WRONG_ENTITY = {"ptvi.invoice@vale.com": "PT Vale Indonesia's invoicing mailbox (an overseas shipping instruction on vale.com), not Vale Canada's"}
mail = {}
# 2026-11-12: every verified mailbox of a buyer under contract (key "b:…"), not only the best-graded one. `mail` keeps one row per key, and a
# lane's mailbox of ANOTHER organisation (one university's AP box credited to dozens of buyers) with the highest grade hid the buyer's own
# mailbox: 1,400 buyers under contract had a verified mailbox and none on their row (table of 00:14Z). emailcols() tries them all, best first.
MAIL_ALL = {}
from validate_returns import TLDS as _TLDS  # IANA's list of top-level domains (tools/data/iana_tlds.txt)
N_BAD_TLD = collections.Counter()
def repair_mailbox(m, page_url):
    """2026-11-10: text glued to an address in a page's source — "ap@rmofheadingley.caDevelopment", "accountspayable@trmh.ca.Accounts",
    "403-335-3391accountspayable@didsbury.caAccounts" (a description or a search index made by stripping tags without spaces). The referee found
    the glued string on the page, so it was "verified". The address is cut back to a real top-level domain and kept ONLY when its domain is then
    the domain of the page it was read on; anything else is dropped ("" returned)."""
    loc, _, dom = (m or "").rpartition("@")
    labels = dom.lower().split(".")
    t, cands = labels[-1], []
    if len(labels) >= 3 and labels[-2] in _TLDS:
        cands.append(".".join(labels[:-1]))  # site.ca.include -> site.ca
    for n in range(len(t) - 1, 1, -1):
        if t[:n] in _TLDS:
            cands.append(".".join(labels[:-1] + [t[:n]]))  # site.cadevelopment -> site.ca (the longest real TLD first)
    try:
        pd = registrable((urllib.parse.urlparse(page_url or "").hostname or "").lower().removeprefix("www."))
    except ValueError:
        pd = ""
    for d in cands:
        if pd and registrable(d) == pd:
            loc2 = re.sub(r"^(?:u00a0|u003e|u003c|u0026|u2028)+", "", loc, flags=re.I)
            loc2 = re.sub(r"^.*\d[\d().\s-]{5,}(?=[a-z])", "", loc2)  # a telephone number glued in front of the address
            return (loc2 + "@" + d) if re.fullmatch(r"[A-Za-z0-9._%+-]+", loc2 or "") else ""
    return ""
def mail_entry(r):
    """(accepted, grade) of one referee mailbox row, or None when rank.py never uses it"""
    r["mailbox"] = re.sub(r"^(?:u003e|u003c|u00a0|u0026|u0022|u0027|%[0-9a-f]{2}|>|<|[-._])+", "", (r.get("mailbox") or "").strip(), flags=re.I)  # JSON / URL escape debris glued to the address ("%20payments@", "u003ebilling@")
    acc = r["check_status"] in ("verified", "cross_verified")
    if _TLDS and r["mailbox"].rsplit(".", 1)[-1].lower() not in _TLDS:
        _fixed = repair_mailbox(r["mailbox"], r.get("evidence_url") or "")
        N_BAD_TLD["cut back to the address the page prints" if _fixed else "left out"] += 1
        if not _fixed:
            return None  # "info@site.comphone" on another domain's page, "info@site.or": no real address can be told from it
        r["mailbox"] = _fixed
    g = real_grade(r["mailbox"], r["mailbox_type"], r["evidence_quote"], r.get("org_name") or "")
    if g < 0:
        return None
    if re.search(r"direct-deposit|depot-direct", r.get("evidence_url") or "") and g < 3:
        g = 3  # PSPC's table of each federal institution's supplier-payment office: finance tier, not invoicing
    if r["mailbox"].lower() in WRONG_ENTITY:
        return None  # a mailbox of another entity on the group's shared domain (spot-check 2026-11-04)
    if g >= 3 and re.search(r"property-tax|paying-|pay-your|pay-online|payonline|tax-pay|taxes|utility-bill|utilit|water-bill|billing|fines|tickets|tuition|donat|fees|"
                            r"make-a-payment|payment-method|payment-option|/payments?(?:/|$|\.)|e-?transfer|how-to-pay|ways-to-pay|pay-?bills?|pay-?my",
                            (r.get("evidence_url") or "").lower()) and not re.search(r"payable|supplier|vendor|fourniss|invoice|factur|procure|purchas|finance|accounting",
                                                                                     ((r.get("evidence_url") or "") + " " + (r.get("evidence_quote") or "")).lower()):
        g = 1  # a mailbox published on the page where residents / customers pay the organisation
    return (acc, g)
import glob as _g0
raw = "".join(open(_p, encoding="utf-8", errors="replace").read() for _p in [ROOT + "/coord/results/org_mailboxes.csv"] + sorted(_g0.glob(ROOT + "/coord/results/org_mailboxes.part*.csv"))).replace("\0", "")  # written in parts under 45 MB (tools/export_orgs.py)
for r in csv.DictReader(io.StringIO(raw)):
    s = mail_entry(r)
    if not s:
        continue
    for ok in (r["org_key"] or "").split("|"):  # a results row may carry several keys of one organisation joined by "|"
        ok = ok.strip()
        if ok and (ok not in mail or s > mail[ok][0]):
            mail[ok] = (s, r)
        if ok and ok.startswith("b:"):
            MAIL_ALL.setdefault(ok, []).append((s, r))
# 1a. the other mailboxes the referee verified for a key: org_mailboxes.csv keeps ONE row per key, so a verified
# invoicing mailbox can hide behind a general one (or behind one rank.py rejects as person-like: Dalhousie's fin.pay@
# kept, apinvoice@ verified too). The verification log names every verified (key, mailbox); the lane's own row gives
# its type, page and quote.
import glob as _glob
LANE_ROWS = {}
for path in _glob.glob(ROOT + "/data/incoming/*/*buyer_ap*results*.csv"):
    try:
        for r in csv.DictReader(io.StringIO(open(path, encoding="utf-8", errors="replace").read().replace("\0", ""))):
            e = (r.get("ap_email") or "").strip().lower()
            u = (r.get("evidence_url") or "").strip()
            if e and u.startswith("http"):
                for k in (r.get("buyer_key") or "").split("|"):
                    LANE_ROWS.setdefault((k.strip(), e, u), r); LANE_ROWS.setdefault((k.strip(), e, ""), r)
    except Exception as ex:
        print("lane rows skipped:", path, type(ex).__name__)
TYPE_MAP = {"invoicing": "invoice_submission", "finance": "finance", "procurement": "procurement", "general": "general"}
n_vl = 0
import parted_csv as _PCSV  # the log: the team lanes' file, then the claude lane's file and its parts (tools/ingest_results.py, 2026-11-10)
for _vl in (ROOT + "/coord/results/verification_log.csv", ROOT + "/coord/results/verification_log_claude.csv"):
    for r in _PCSV.rows(_vl):
        if r.get("outcome") not in ("verified", "cross_verified") or "@" not in (r.get("value") or ""):
            continue
        e = r["value"].strip().lower()
        for k in (r.get("buyer_key") or "").split("|"):
            k = k.strip()
            lr = LANE_ROWS.get((k, e, (r.get("page_url") or "").strip())) or LANE_ROWS.get((k, e, ""))
            if not k or not lr:
                continue
            ent = {"org_key": k, "org_name": lr.get("org_name_as_found") or "", "mailbox": e, "mailbox_type": TYPE_MAP.get((lr.get("ap_email_type") or "").strip().lower(), "general"),
                   "check_status": r["outcome"], "evidence_url": lr.get("evidence_url") or "", "evidence_quote": (lr.get("evidence_quote") or "")[:300], "found_by": r.get("found_by") or ""}
            s = mail_entry(ent)
            if s and (k not in mail or s > mail[k][0]):
                mail[k] = (s, ent); n_vl += 1
            if s and k.startswith("b:"):
                MAIL_ALL.setdefault(k, []).append((s, ent))
print("mailboxes taken from the verification log (better than org_mailboxes' single pick):", n_vl, "| referee mailbox rows whose last label is not a top-level domain:", dict(N_BAD_TLD))
_free(globals(), "LANE_ROWS", "raw")
# 1b. optional release tables (each skipped when absent): vendor registry facts / websites / addresses (field fill),
# buyer websites / addresses, and the weaker-relationship inputs of P12 (registry-match contracts, ended contracts)
REL = ROOT + "/data/release/"
def jl(*paths):
    for path in paths:
        if os.path.exists(path):
            with gzip.open(path, "rt", encoding="utf-8") as fh:
                for line in fh:
                    yield json.loads(line)
_t = datetime.date.today()
CUT5 = (_t.replace(year=_t.year - 5) if not (_t.month == 2 and _t.day == 29) else _t.replace(year=_t.year - 5, day=28)).isoformat()  # owner 2026-11-03: P12 = up to 5 years old
POSTAL = re.compile(r"\b([ABCEGHJKLMNPRSTVXY])\d[ABCEGHJ-NPRSTV-Z] ?\d[ABCEGHJ-NPRSTV-Z]\d\b")
PC1 = {"A": "NL", "B": "NS", "C": "PE", "E": "NB", "G": "QC", "H": "QC", "J": "QC", "K": "ON", "L": "ON", "M": "ON", "N": "ON", "P": "ON",
       "R": "MB", "S": "SK", "T": "AB", "V": "BC", "Y": "YT"}
def prov_of_postal(pc):
    pc = pc.upper().replace(" ", "")
    return ("NU" if pc[:3] in ("X0A", "X0B", "X0C") else "NT") if pc[:1] == "X" else PC1.get(pc[:1], "")
REGION = {"quebec": "QC", "qc": "QC", "ontario": "ON", "on": "ON", "british columbia": "BC", "bc": "BC", "alberta": "AB", "ab": "AB",
          "manitoba": "MB", "mb": "MB", "saskatchewan": "SK", "sk": "SK", "nova scotia": "NS", "ns": "NS", "new brunswick": "NB", "nb": "NB",
          "newfoundland and labrador": "NL", "newfoundland": "NL", "nl": "NL", "prince edward island": "PE", "pe": "PE", "pei": "PE",
          "yukon": "YT", "yt": "YT", "northwest territories": "NT", "nt": "NT", "nunavut": "NU", "nu": "NU"}
def region_code(a):
    """province of an address dict (region field, else its postal code)"""
    a = a or {}
    r = REGION.get(norm(a.get("region") or ""), "")
    if not r:
        m = POSTAL.search(" ".join(str(x) for x in ([a.get("postal_code")] + list(a.get("lines") or [])) if x).upper())
        r = prov_of_postal(m.group(0)) if m else ""
    return r
def addr_text(a):
    a = a or {}
    if a.get("lines"):
        return ", ".join(x for x in a["lines"] if x)
    return ", ".join(str(x) for x in (a.get("line1"), a.get("line2"), a.get("city"), a.get("region"), a.get("postal_code"), a.get("country")) if x)
def host_of(u):
    h = (urllib.parse.urlparse(u if "//" in (u or "") else "https://" + (u or "")).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h
FREEMAIL = re.compile(r"^(gmail|hotmail|outlook|live|yahoo|ymail|msn|aol|icloud|me|mac|videotron|sympatico|bell|rogers|shaw|telus|cogeco|eastlink|"
                      r"globetrotter|qc\.aira|aira|tlb|xplornet|nbnet\.nb|nb\.aibn|mts|sasktel|protonmail|proton|gmx|mail|bellnet|cgocable|"
                      r"derytele|axion|tbaytel|execulink|personainternet|primus|distributel|teksavvy|ciril|netrevolution|b2b2c|live\.ca|outlook\.fr)\.", re.I)
VEN, VEN_NAME, VEN_DOM = {}, {}, {}
# 2026-11-10: a partnership and a corporation are different legal persons even when the rest of the name is the same. The registry match of the
# dataset build ignores the legal form, so "KPMG LLP" carried the identity of KPMG INC., "Deloitte LLP" of DELOITTE INC., "MNP LLP" of MNP LTD.,
# "BDO Canada LLP" of BDO Canada Limited — their corporation number, BN and derived GST/HST number on every row of the audit firms. Such a
# match is not used (the vendor's registry cells stay empty until a registry names the partnership itself).
_PARTNERSHIP = {"llp", "lp", "gp", "sencrl", "senc", "srl"}
_CORPORATION = {"inc", "incorporated", "incorporee", "ltd", "limited", "ltee", "limitee", "corp", "corporation", "ulc", "llc", "co", "company", "compagnie", "cie"}
def form_conflict(name, legal):
    _abbr = lambda t: re.sub(r"\b((?:[A-Za-z]\.){2,})", lambda m: m.group(1).replace(".", "") + " ", t or "")  # "L.P." -> "LP", "S.E.N.C.R.L." -> "SENCRL"
    a, b = set(norm(_abbr(name)).split()[-2:]), set(norm(_abbr(legal)).split()[-2:])
    return bool((a & _PARTNERSHIP and b & _CORPORATION and not b & _PARTNERSHIP) or (b & _PARTNERSHIP and a & _CORPORATION and not a & _PARTNERSHIP))
_VE_REG_KEYS = ("legal_name", "registry_status", "registry_match_level", "corporation_number_federal", "neq_quebec", "bc_registration_number", "business_number_bn9",
                "business_number_source", "gst_hst_account_derived", "registered_address", "incorporation_or_registration_date", "governing_legislation_or_regime",
                "legal_form_quebec", "employees_in_quebec", "main_activity", "matches", "full_detail")
n_ve_form = 0
def clean_ve(r):
    """a contract record whose vendor enrichment pairs a partnership with a corporation of the same name: the registry cells are dropped"""
    global n_ve_form
    ve = r.get("vendor_enrichment")
    if ve and ve.get("legal_name") and form_conflict((r.get("vendor") or {}).get("name") or "", ve["legal_name"]):
        for k in _VE_REG_KEYS:
            ve.pop(k, None)
        n_ve_form += 1
    if ve and ve.get("website") and site_is_a_host((r.get("vendor") or {}).get("name") or "", ve.get("legal_name") or "", ve["website"]):
        for k in ("website", "website_verification", "contact_emails_published", "phones_published"):
            ve.pop(k, None)
    return r
n_form = n_dom_unfit = n_dom_host = 0
from lead_crawl import name_fit as _name_fit
# web hosts, registrars and site builders: when a vendor's name no longer leads to its own site, the dataset's website finder followed the old
# domain's redirect to the company that hosts or parks it ("mutek.ca redirects to whc.ca … city MONTREAL on site") and kept that as the vendor's
# website — and with it the host's e-mail addresses, telephone and logo. Known hosts: the providers that serve the DNS of 20 or more of the
# domains we looked up (tools/dns_services.py), plus the common parking and site-builder domains.
HOST_DOMS = set("""godaddy.com sedo.com sedoparking.com hugedomains.com dan.com afternic.com namecheap.com bodis.com parkingcrew.net squarespace.com wix.com weebly.com wordpress.com
shopify.com register.com networksolutions.com hover.com rebel.ca rebel.com webnames.ca hostpapa.ca hostpapa.com web.com ionos.com ionos.ca bluehost.com hostgator.com dreamhost.com name.com
tucows.com enom.com canspace.ca namespro.ca sibername.com easydns.com whc.ca funio.com likuid.com planethoster.com ovh.com ovhcloud.com kinsta.com netfirms.com doteasy.com 10dollar.ca
domain.com google.com facebook.com linkedin.com""".split())
try:
    with open(ROOT + "/data/incoming/claude/credit_scan/dns_providers_seen.csv", encoding="utf-8") as _fh:
        for _r in csv.DictReader(_fh):
            if (_r.get("ns") or "0").isdigit() and int(_r["ns"]) >= 20:
                HOST_DOMS.add(_r["provider_domain"])
except OSError:
    pass
def site_is_a_host(name, legal, website):
    """the 'website' of this vendor is a web host's / registrar's / site builder's own domain, and the vendor is not that company"""
    wd = registrable(host_of(website or ""))
    wl = re.sub(r"[^a-z0-9]", "", wd.split(".")[0])
    return bool(wd) and wd in HOST_DOMS and not any(_name_fit(n, wl) >= 20 for n in (name, legal) if n)
for v in jl(REL + "vendors_enriched.jsonl.gz"):
    s = v.get("summary") or {}
    reg = s.get("registry_match_level") in ("exact", "strong")  # registry facts only from a confident match
    if reg and form_conflict(v.get("name") or "", s.get("legal_name") or ""):
        reg = False; n_form += 1
    ra = (s.get("registered_address") or {}) if reg else {}
    ca = next((x["value"] for x in v.get("addresses_in_contract_data") or [] if (x.get("value") or {}).get("line1") or (x.get("value") or {}).get("city")), {})
    bn = s.get("business_number_bn9") if reg else None
    rec = {"name": v.get("name") or "", "legal_name": (s.get("legal_name") or "") if reg else "", "bn9": bn or "",
           "gst": (s.get("gst_hst_account_derived") or (bn + "RT0001" if bn else "")) if reg else "",
           "address": addr_text(ca) or addr_text(ra), "region": region_code(ca) or region_code(ra), "website": s.get("website") or "",
           "emails": "; ".join(e if isinstance(e, str) else (e.get("email") or "") for e in s.get("contact_emails_published") or []),
           "registry": next(({"registry": m.get("registry"), "id": m.get("id"), "legal_name": m.get("legal_name"), "url": m.get("source_url")}
                             for m in s.get("matches") or [] if m.get("match_confidence") in ("exact", "strong")), None) if reg else None,
           "reg_address": addr_text(ra), "reg_region": region_code(ra), "full": b""}
    if reg:  # the full registry records behind the confident matches (REQ: NEQ, trade names, legal form, CAE activity, employees; Corporations Canada: BN, act, directors range; OrgBook: entity type)
        _full = {}
        for m in v.get("registry_matches_full") or []:
            if m.get("match_confidence") in ("exact", "strong") and m.get("registry") not in _full:
                _full[m["registry"]] = m
        if _full:  # kept compressed (58,000 vendors x ~3.5 KB of JSON were ~0.7 GB as objects); vend_fill opens the one it needs
            rec["full"] = zlib.compress(json.dumps(_full, ensure_ascii=False).encode("utf-8"), 1)
    VEN[v["vendor_key"]] = rec
    for n in {norm(v.get("name")), norm(rec["legal_name"])} - {""}:
        VEN_NAME[n] = v["vendor_key"] if VEN_NAME.get(n, v["vendor_key"]) == v["vendor_key"] else None  # ambiguous name: no lookup
    if rec["website"]:
        # a vendor is looked up by a site's domain only when its name fits that domain (2026-11-10: the dataset's website finder had given the
        # festival MUTEK the address of its web host, and every DNS row of that host carried MUTEK's legal name and street address)
        _wd = registrable(host_of(rec["website"]))
        _wl = re.sub(r"[^a-z0-9]", "", _wd.split(".")[0])
        _wv = s.get("website_verification") if isinstance(s.get("website_verification"), dict) else {}
        if site_is_a_host(rec["name"], rec["legal_name"], rec["website"]):
            rec["website"], rec["emails"] = "", ""  # the host's site and the host's own mailboxes: not this vendor's
            n_dom_host += 1
        elif (_wl and any(_name_fit(_n, _wl) >= 20 for _n in (rec["name"], rec["legal_name"]) if _n)) or _wv.get("confidence") in ("verified", "verified_via_redirect"):
            VEN_DOM.setdefault(_wd, v["vendor_key"])  # the name fits the domain, or the finder saw the vendor's name and place on the site
        else:
            n_dom_unfit += 1
# the team's vendor contacts (lane gemini, referee-verified: coord/results/team_vendors.jsonl) — role mailboxes, billing/AR boxes, websites
TEAMV = {}
if os.path.exists(ROOT + "/coord/results/team_vendors.jsonl"):
    for line in open(ROOT + "/coord/results/team_vendors.jsonl", encoding="utf-8"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        gen, bill, pages, by = [], [], [], set()
        for e in d.get("evidence") or []:
            if e.get("verification") not in ("verified", "cross_verified") or not e.get("email"):
                continue
            (bill if e.get("kind") == "billing_or_ar_email" else gen).append(e["email"].lower()); pages.append(e.get("page_url") or ""); by.add(e.get("found_by") or "team")
        if gen or bill or d.get("website"):
            TEAMV[d.get("vendor_key")] = {"emails": sorted(set(gen)), "billing": sorted(set(bill)), "pages": [p for p in pages if p][:3], "website": d.get("website") or "", "by": ",".join(sorted(by))}
print("vendor table: registry matches not used because the legal form differs (partnership vs corporation):", n_form, "| 'websites' that are a web host's own site (dropped with their mailboxes):", n_dom_host, "| websites not used for a look-up by domain (unverified, name does not fit):", n_dom_unfit, "| look-ups by domain:", len(VEN_DOM))
print("team vendor contacts (referee-verified):", len(TEAMV), "vendors;", sum(1 for v in TEAMV.values() if v["billing"]), "with a billing / AR mailbox")
BUY = {b["buyer_key"]: b for b in jl(REL + "buyers_enriched.jsonl.gz") if b.get("buyer_key")}
def vend_fill(key="", name="", domain=""):
    """vendor columns from the release's vendor table: by vendor key, by website domain, then by exact name"""
    k = key if key in VEN else VEN_DOM.get(registrable(domain)) if domain else None
    if not k and name:
        k = VEN_NAME.get(norm(name)) or VEN_NAME.get(parent(name))
    v = VEN.get(k) or {}
    rg = v.get("registry") or {}
    REGN = {"quebec_req": "Québec REQ (NEQ)", "corporations_canada": "Corporations Canada (corporation number)", "bc_orgbook": "BC OrgBook (BC registration)",
            "rbq": "RBQ licence", "cra_charities": "CRA charities (BN)", "alberta": "Alberta corporate registry", "ontario": "Ontario business registry"}
    full = json.loads(zlib.decompress(v["full"]).decode("utf-8")) if v.get("full") else {}
    req, cc, ob = full.get("quebec_req") or {}, full.get("corporations_canada") or {}, full.get("bc_orgbook") or {}
    def _names(x):
        x = x.get("other_names") or []
        return [n for n in (x if isinstance(x, list) else [x]) if n and str(n) != "[]"]
    trade = "; ".join(dict.fromkeys(str(n) for n in _names(req) + _names(cc) + _names(ob)))[:300]
    extra = {"vendor_neq": (req.get("neq") + " (Registraire des entreprises du Québec, bulk register %s; retrieved %s)" % (req.get("dataset_url") or "", (req.get("retrieved_at") or "")[:10])) if req.get("neq") else "",
             "vendor_trading_name": (trade + " (other names in the registry)") if trade else "",
             "vendor_legal_form": (req.get("legal_form") or "") + ((" — " + (req.get("jurisdiction") or "")) if req.get("jurisdiction") else "") if req else ((cc.get("governing_legislation") or "") + (" (%s)" % cc.get("jurisdiction") if cc.get("jurisdiction") else "") if cc else ((ob.get("entity_type") or "") + ((" (home jurisdiction %s)" % ob.get("home_jurisdiction")) if ob.get("home_jurisdiction") else "") if ob else "")),
             "vendor_registry_status": "; ".join("%s: %s%s" % (REGN.get(k, k), m.get("status") or "", (" (%s)" % m.get("status_date")) if m.get("status_date") else "") for k, m in full.items() if m.get("status"))[:200],
             "vendor_incorporation_date": (req.get("constitution_date") or req.get("registration_date") or "")[:10] or (ob.get("registration_date") or "")[:10],
             "vendor_activity_code": ("CAE %s — %s" % (req.get("main_activity_code_cae"), req.get("main_activity")) if req.get("main_activity_code_cae") else (req.get("main_activity") or "")) + ((" | secondary: " + req["secondary_activity"]) if req.get("secondary_activity") else ""),
             "vendor_employees_quebec": req.get("employees_in_quebec") or "",
             "vendor_last_annual_filing": (("REQ annual declaration %s" % req["last_annual_declaration_year"]) if req.get("last_annual_declaration_year") else "") + (("; Corporations Canada anniversary %s" % cc["anniversary_date"]) if cc.get("anniversary_date") else ""),
             "vendor_directors_range": ("%s to %s directors (Corporations Canada)" % tuple(cc["directors_min_max"][:2])) if isinstance(cc.get("directors_min_max"), list) and len(cc["directors_min_max"]) >= 2 else "",
             "vendor_establishments_quebec": "; ".join(("%s: %s" % (e.get("name") or "", ", ".join(e.get("address_lines") or []))) for e in (req.get("establishments") or [])[:3] if isinstance(e, dict))[:300]}
    return {**extra, "vendor_legal_name": v.get("legal_name", ""), "vendor_address": v.get("address", ""), "vendor_bn9": v.get("bn9", ""),
            "vendor_gst_hst_derived": v.get("gst", ""), "vendor_website": v.get("website", "") or ("https://" + domain if domain else ""),
            "vendor_emails": v.get("emails", ""),
            "vendor_registry_id": ("%s: %s" % (REGN.get(rg.get("registry"), rg.get("registry")), rg.get("id"))) if rg.get("id") else "",
            "vendor_registry_url": rg.get("url") or "", "vendor_registered_address": v.get("reg_address", "") if v.get("reg_address") and v.get("reg_address") != v.get("address") else ""}
# owner 2026-11-06 ("PO matters, all identifiers possible, max"): every identifier the record carries, verbatim, plus a classification
ID_CLASSES = (
    ("po", re.compile(r"(?:^|[_.\- ])(?:po|pon|purchase[_\- ]?orders?|orders?|bons?[_\- ]?de[_\- ]?commande|commandes?)(?:[_\- ]?(?:number|no|num|nbr|id|identifier))?(?:$|[_.\- ])|^pd_procurement_id$|^piid$", re.I)),
    ("buyer_vendor_id", re.compile(r"(?:supplier|vendor|fournisseur|payee|recipient|contractor)[_\- ]?(?:id|number|no|code|num)", re.I)),
    ("vendor_registry", re.compile(r"(?:^|[_\- ])uei(?:$|[_\- ])|duns|cage|business[_\- ]?number|^bn$|neq|(?:^|[_\- ])(?:gst|hst|vat|ein|abn|acn|kvk|cvr)(?:$|[_\- ])|tax[_\- ]?id|siret|siren|companies[_\- ]?house", re.I)),
    ("commodity", re.compile(r"unspsc|gsin|naics|\bcpv\b|commodity|economic_object|\bpsc\b|product_service_code|category", re.I)),
    ("org_code", re.compile(r"agency_code|sub_agency|owner_org|department_code|org_code|office_code|ministry_code|entity_code|business_unit|agency_id", re.I)),
    ("modification", re.compile(r"modification|amendment|\bmod\b|version|revision", re.I)),
    ("contract", re.compile(r"contract|agreement|entente|contrat|reference[_\- ]?numbers?|no[_\- ]?reference|standing[_\- ]?offer|supply[_\- ]?arrangement|framework|^num[eé]ro$|^numero$|^reference$|^ref(?:erence)?[_\- ]?(?:no|id)?$|parent_award_id|^cn[_\- ]?(?:id|number|no)$|agency[_\- ]?ref|buyer[_\- ]?ref|internal[_\- ]?ref|your[_\- ]?ref|reference[_\- ]?id|^ref[_\- ]?id$", re.I)),
    ("solicitation", re.compile(r"solicitation|tender|\bbid|appel|rfp|rfq|rfx|competition|opportunit|numero_appel|notice[_\- ]?(?:number|no|id)|^avis", re.I)),
    ("award", re.compile(r"award|ocid|ocds|seao_item_id|numeroseao|merx_id|record_id|tender_id|notice_id|item_id|guid|unique_key|transaction|^id$|_id$", re.I)),
)
ID_EXCLUDE = re.compile(r"year|type|desc|date|status|count|amount|total|flag|url|name|title|text|_keys$|^transaction_unique_keys$", re.I)
CLASS_LABEL = {"po": "purchase order / procurement number", "contract": "contract or agreement number", "solicitation": "solicitation / tender number",
               "award": "award or notice id", "buyer_vendor_id": "the buyer's own vendor id", "vendor_registry": "vendor registry id", "commodity": "commodity code",
               "org_code": "buyer organisation code", "modification": "amendment / modification"}
def _flat(v):
    if isinstance(v, list):
        return "|".join(_flat(x) for x in v if x not in (None, ""))[:200]
    if isinstance(v, dict):
        return "; ".join("%s=%s" % (k, _flat(x)) for k, x in v.items() if x not in (None, ""))[:200]
    return str(v).strip()
def classify_ids(ids, src_key="", instrument=""):
    """columns po_number_as_published, contract_or_agreement_number, solicitation_or_tender_number, award_or_notice_id, buyer_vendor_id,
    vendor_ids_in_record, commodity_codes, buyer_org_codes, amendment_or_modification, all_identifiers, identifier_count, invoice_reference_hint"""
    out = {k: [] for k in ("po", "contract", "solicitation", "award", "buyer_vendor_id", "vendor_registry", "commodity", "org_code", "modification")}
    allid = []
    for k, v in (ids or {}).items():
        fv = _flat(v)
        if not fv or fv.lower() in ("none", "null", "nan", "n/a", "[]", "{}"):
            continue
        allid.append("%s=%s" % (k, fv))
        kl = str(k).lower()
        if ID_EXCLUDE.search(kl) and kl not in ("po", "piid", "order", "order_no", "po_no"):
            continue
        cls = next((c for c, rx in ID_CLASSES if rx.search(kl)), None)
        if cls == "po" and kl == "piid" and not re.search(r"purchase order|delivery order|\bpo\b|\bdo\b|call", instrument or "", re.I):
            cls = "contract"  # a PIID on a definitive contract is the contract number; on a PO / delivery order it is the order number
        if cls:
            systemish = ("unique" in kl or "guid" in kl or "item_id" in kl or kl.endswith("_key") or "transaction" in kl or kl in ("ocid", "release_id")
                         or re.fullmatch(r"(?:prod-|ocds-)?[0-9a-f]{20,}(?:-[0-9a-f]+)*", fv.lower()) is not None or re.fullmatch(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", fv.lower()) is not None)
            out[cls].append((systemish, len(kl), "%s (%s)" % (fv, k)))
    if src_key == "seao_quebec":  # 2026-11-08: SEAO's "numero" is the reference the organisation gives its notice (appel d'offres), i.e. the tender number; the concluded contract is published under it
        _num = [t for t in out["contract"] if t[2].endswith("(numero)")]
        out["contract"] = [t for t in out["contract"] if not t[2].endswith("(numero)")]
        out["solicitation"] = _num + out["solicitation"]
    if not out["award"] and out["solicitation"]:  # the portal's own id of the tender notice is a notice id (bidsandtenders_tender_id, competition_guid, opportunity_id): award_or_notice_id
        _sys = [t for t in out["solicitation"] if t[0] or re.search(r"_(?:guid|id)\)$", t[2])]
        if _sys:
            out["award"] = [(t[0], t[1], t[2] + " — notice id; the award is published within this notice, the source assigns no separate award id") for t in _sys]
            out["solicitation"] = [t for t in out["solicitation"] if t not in _sys] or out["solicitation"]
    out = {c: [t[2] for t in sorted(v)] for c, v in out.items()}  # human-usable numbers first, system keys last
    if not [t for t in out["contract"] if not re.search(r"\((?:ocds_contract_ids|contract_ids|collapsed_duplicate_contract_ids)\)$", t)] and out["solicitation"]:
        _sol = out["solicitation"][0]
        if not re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-", _sol):
            out["contract"] = out["contract"] + ["%s — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference" % _sol]
    res = {"po_number_as_published": "; ".join(out["po"])[:300], "contract_or_agreement_number": "; ".join(out["contract"])[:300],
           "solicitation_or_tender_number": "; ".join(out["solicitation"])[:300], "award_or_notice_id": "; ".join(out["award"])[:300],
           "buyer_vendor_id": "; ".join(out["buyer_vendor_id"])[:200], "vendor_ids_in_record": "; ".join(out["vendor_registry"])[:200],
           "commodity_codes": "; ".join(out["commodity"])[:200], "buyer_org_codes": "; ".join(out["org_code"])[:200],
           "amendment_or_modification": "; ".join(out["modification"])[:200], "all_identifiers": "; ".join(allid)[:1500], "identifier_count": str(len(allid))}
    for cls in ("po", "contract", "solicitation", "award"):
        if out[cls]:
            res["invoice_reference_hint"] = "%s: %s%s" % (CLASS_LABEL[cls], out[cls][0], (" — source %s" % src_key) if src_key else "")
            break
    else:
        res["invoice_reference_hint"] = "no identifier published with the record" if not allid else "only system ids published (see all_identifiers)"
    return res
COMMODITY_KEYS = (("unspsc", "UNSPSC"), ("gsin", "GSIN"), ("naics", "NAICS"), ("cpv", "CPV"), ("psc", "PSC"), ("product_service_code", "PSC"), ("economic_object_code", "economic object"),
                  ("nigp", "NIGP"), ("unspsc_description", None), ("gsin_description", None), ("economic_object_description", None))
def classify_plus(c, src_key=""):
    """classify_ids of the record's identifiers plus commodity codes taken from the record's own commodity block (owner D14)"""
    res = classify_ids(c.get("identifiers") or {}, src_key, str(c.get("instrument_type") or ""))
    com = c.get("commodity") or {}
    if isinstance(com, dict):
        codes = []
        for k, lab in COMMODITY_KEYS:
            v = com.get(k)
            if not lab or v in (None, "", [], {}):
                continue
            v = _flat(v)
            v = ", ".join(dict.fromkeys(t.strip() for t in re.split(r"[,|;]\s*", v) if t.strip()))  # the source repeats the code per line item
            desc = com.get(k + "_description") or ""
            codes.append("%s %s%s" % (lab, v[:120], (" (%s)" % str(desc)[:80]) if desc and k != "economic_object_code" else ""))
        if codes:
            res["commodity_codes"] = "; ".join(([res["commodity_codes"]] if res.get("commodity_codes") else []) + codes)[:300]
    return res
def rec_extra(c):
    """owner 2026-11-04: every field the record gives — instrument (standing offer / blanket order / contract), method, commodity, description"""
    com = c.get("commodity") or {}
    com = " ".join(str(com.get(k)) for k in ("unspsc", "unspsc_description") if com.get(k)) if isinstance(com, dict) else str(com)
    return {"instrument_type": str(c.get("instrument_type") or c.get("canadabuys_instrument_type") or c.get("instrument_type_source_code") or "")[:120],
            "procurement_method": str(c.get("procurement_method") or c.get("solicitation_procedure") or "")[:120],
            "commodity": com[:160], "contract_description": re.sub(r"\s+", " ", str(c.get("description") or ""))[:300],
            "number_of_bids": str(c.get("number_of_bids") or "")}
# 2. contracts: best proof record per parent organisation
TIER = {"ongoing": "A", "ongoing_inferred": "B", "end_date_unknown": "C"}
TS = {"A": 3, "B": 2, "T": 1.8, "L": 1.5, "M": 1.2, "C": 1, "D": 1, "R": 0.7, "E": 0.5}
CUTOFF = (datetime.date.today() - datetime.timedelta(days=365)).isoformat()
CUR = {"FED": "CAD", "AB": "CAD", "NT": "CAD", "NL": "CAD", "SK": "CAD", "QC": "CAD", "NS": "CAD", "NB": "CAD", "MB": "CAD", "ON": "CAD", "BC": "CAD",
       "YT": "CAD", "NU": "CAD", "PE": "CAD", "US": "USD", "AU": "AUD", "UK": "GBP"}
def award_date(r):
    d = r["contract"].get("dates") or {}
    return max((str(d.get(k) or "")[:10] for k in ("awarded", "award", "signed", "start")), default="") or str(d.get("published") or "")[:10]
CUTOFF3 = (datetime.date.today() - datetime.timedelta(days=3 * 365)).isoformat()
def tier_of(r):
    t = TIER.get(r["status"], "C")
    if t == "B" and award_date(r) < CUTOFF3:  # "no closing notice" says little about a contract awarded over 3 years ago
        t = "C"
    if t == "C" and CUTOFF <= award_date(r) <= today:
        return "B"
    if t == "C" and CUTOFF3 <= award_date(r) < CUTOFF and r["status"] != "ended":
        return "L"  # owner's rule (2026-11-01): multi-year contracts awarded 12-36 months ago, no end date: "likely active", own package
    return t
_DEAD_REG = re.compile(r"dissol|inactive|radi[ée]|cancel|revoked|struck|annul|liquidat|discontinued|amalgamated|historical", re.I)
_LIVE_REG = re.compile(r"\bactive\b|immatricul|en vigueur|in good standing|registered\b|existing|current", re.I)
def contract_score(r):
    c, v = r["contract"], r.get("vendor") or {}
    ve, d = r.get("vendor_enrichment") or {}, (r["contract"].get("dates") or {})
    ids = c.get("identifiers") or {}
    pts = [bool(ids.get("reference_number") or any(ids.values())), bool(c.get("value")), bool(d.get("start") or d.get("awarded") or d.get("award")),
           bool(d.get("end")), bool(r.get("link")), bool(v.get("address")), bool(ve.get("business_number_bn9")),
           bool(ve.get("gst_hst_account_derived")), bool(ve.get("website")), bool(ve.get("contact_emails_published") or (v.get("contact") or {}).get("email"))]
    return TS[tier_of(r)] * 10 + sum(pts), sum(pts)
# jurisdiction of a record (from its source) and of a mailbox (from its domain): ministries with the same short name in
# different governments ("Justice", "Health", "Education" ...) share a buyer key upstream, so they are split here and a
# mailbox is attached only when its domain fits that government
JUR_SRC = [(r"CanadaBuys|Proactive Publication|Standing Offers|Government of Canada|Public Services and Procurement", "FED"),
           (r"Alberta", "AB"), (r"Northwest Te", "NT"), (r"NL Public|Newfoundland", "NL"), (r"SaskTenders|Saskatchewan", "SK"),
           (r"appel d'offres du Qu|Hydro-Qu", "QC"), (r"Nova Scotia", "NS"), (r"New Brunswick|NBON", "NB"), (r"Manitoba", "MB"),
           (r"Ontario Tenders|Supply Ontario", "ON"), (r"BC Bid|British Columbia", "BC"), (r"Yukon", "YT"), (r"Nunavut", "NU"),
           (r"Prince Edward", "PE"), (r"USAspending|SAM\.gov|FPDS", "US"), (r"Tenders Electronic", "EU"), (r"Contracts Finder|Find a Tender", "UK"),
           (r"AusTender", "AU")]
JUR_DOM = [(r"\.(gc\.ca|canada\.ca|forces\.ca)$", "FED"), (r"\.(gov\.ab\.ca|alberta\.ca)$", "AB"), (r"\.gov\.nt\.ca$", "NT"), (r"\.gov\.nl\.ca$", "NL"),
           (r"\.gov\.sk\.ca$", "SK"), (r"\.(gouv\.qc\.ca|quebec\.ca)$", "QC"), (r"\.novascotia\.ca$", "NS"), (r"\.gnb\.ca$", "NB"), (r"\.gov\.mb\.ca$", "MB"),
           (r"\.ontario\.ca$", "ON"), (r"\.gov\.bc\.ca$", "BC"), (r"\.(gov\.yk\.ca|yukon\.ca)$", "YT"), (r"\.gov\.nu\.ca$", "NU"), (r"\.gov\.pe\.ca$", "PE")]
# anchored on a dot (2026-11-03): "aicanada.ca" or "visitquebec.ca" are not government mail domains
PLACE = re.compile(r"canada|quebec|alberta|ontario|saskatchewan|manitoba|scotia|brunswick|newfoundland|labrador|yukon|northwest|nunavut|"
                   r"british columbia|prince edward|county|city|ville|town|municipal|college|cegep|universit|hydro|\b(bc|nl|ns|nb|pei)\b")
BAD_LOCAL = re.compile(r"recrut|recruit|emploi|career|carriere|job|plainte|complaint|frais|accessoire|patient|usager|media|presse|press|"
                       r"privacy|confidential|aiprp|atip|benevol|volunteer|fondation|foundation|donat|webmaster|^rh$|^hr$|recevable|receivable|revenue|revenu|"
                       r"billing|taxation|^taxe|vie-?privee|accessibilit|billetterie|boxoffice|box-office|tickets?$|^tickets|admission|registrar|newsletter|abonnement|"
                       r"unsubscribe|no-?reply|donotreply|^events?$|^news$|alumni|scholarship|bourse|^social$|^marketing$|^comms?$|^communications?$|"
                       r"(?:^|[._-])ati(?:office)?(?:$|[._-])|foip|(?:^|[._-])foi(?:$|[._-])|acces-?(?:a-?l-?)?info|"
                       # 2026-11-12 (rows read for the owner): a service-quality / complaints box (qualite.services@), a register's (registretap@), a
                       # programme's funding box (financementpompiers@), stakeholder engagement, surveys, recruiting (acquisition.talents@), a hospital's
                       # sales ledger (customers pay it), access to information written with a dot (acces.information.cstu@)
                       r"qualit[eé]|registre|financement|(?<!supplier[._-])(?<!suppliers[._-])(?<!vendor[._-])(?<!vendors[._-])engage|feedback|commentaire|suggestion|ombuds|sondage|survey|talent|sales[._-]?ledger|"
                       r"acc[eè]s[._-]?(?:[àa][._-]?l[._-]?)?information", re.I)
def jur_of_record(r):
    s = (r.get("source") or {}).get("name", "")
    return next((j for rx, j in JUR_SRC if re.search(rx, s)), "")
def jur_of_mail(email):
    d = "." + (email or "").split("@")[-1].lower()
    return next((j for rx, j in JUR_DOM if re.search(rx, d)), "")
orgs = {}
for l in gzip.open(ROOT + "/data/release/canadian_vendor_contracts.jsonl.gz", "rt", encoding="utf-8"):
    r = clean_ve(json.loads(l)); be = r.get("buyer_enrichment") or {}
    key = be.get("buyer_key"); name = be.get("canonical_name") or (r.get("buyer") or {}).get("name") or ""
    p = parent(name)
    if not p: continue
    j = jur_of_record(r)
    own = (r.get("buyer") or {}).get("name") or ""
    po = parent(own)
    if po and len(po.split()) <= 3 and not PLACE.search(po) and j:  # generic ministry-style name: one group per government
        p, name = po + " | " + j, own
    sc, fields = contract_score(r)
    o = orgs.setdefault(p, {"p": p, "keys": set(), "best": None, "bs": -1, "n": 0, "name": name, "be": be, "jur": collections.Counter(),
                            "vendors": collections.Counter(), "n12": 0, "latest": "", "value": 0.0, "nval": 0, "cur": collections.Counter(), "sources": collections.Counter()})
    o["keys"].add(key); o["n"] += 1; o["jur"][j] += 1
    _vn = ((r.get("vendor") or {}).get("name") or "").strip()
    if _vn:
        o["vendors"][_vn] += 1
    _ad = award_date(r) or ""
    if _ad >= CUTOFF:
        o["n12"] += 1
    _ids = (r.get("contract") or {}).get("identifiers") or {}
    _cl = classify_ids(_ids, "", str((r.get("contract") or {}).get("instrument_type") or ""))
    _ref = _cl["po_number_as_published"] or _cl["contract_or_agreement_number"] or _cl["solicitation_or_tender_number"] or _cl["award_or_notice_id"]
    if _ad > o["latest"]:
        o["latest"] = _ad
    if _ref and _ad >= o.get("latest_ref_date", ""):
        o["latest_ref"] = "%s — %s — %s%s" % (_ref.split(";")[0][:100], _vn or "vendor not named", (r.get("source") or {}).get("name") or "", (" [%s]" % _ad) if _ad else "")
        o["latest_ref_date"] = _ad
    _val = 0.0
    try:
        _val = float(str((r.get("contract") or {}).get("value") or "").replace(",", ""))
    except ValueError:
        _val = 0.0
    if _val > 0:
        o["value"] += _val; o["nval"] += 1; o["cur"][(r.get("contract") or {}).get("currency") or CUR.get(j, "") or "?"] += 1
        o.setdefault("vals", []).append(_val)
    if _ad:
        o.setdefault("dates", []).append(_ad)
        if _val > 0:
            o.setdefault("yv", collections.Counter())[_ad[:4]] += _val
    _dd = (r.get("contract") or {}).get("dates") or {}
    _ds, _de = _dd.get("start") or _dd.get("signed") or _dd.get("awarded"), _dd.get("end") or _dd.get("end_inferred") or _dd.get("end_computed")  # end_inferred / end_computed = award + the duration the source publishes
    if _ds and _de and len(str(_ds)) >= 10 and len(str(_de)) >= 10:
        try:
            _dur = (datetime.date.fromisoformat(str(_de)[:10]) - datetime.date.fromisoformat(str(_ds)[:10])).days
            if 0 < _dur < 7400:
                o.setdefault("durs", []).append(_dur)
        except ValueError:
            pass
    _com = (r.get("contract") or {}).get("commodity") or {}
    if isinstance(_com, dict):
        _cd = _com.get("unspsc_description") or _com.get("gsin_description") or _com.get("economic_object_description") or _com.get("commodity_type") or ""
        if _cd:
            o.setdefault("coms", collections.Counter())[str(_cd)[:60]] += 1
    o["sources"][(r.get("source") or {}).get("name") or ""] += 1
    if _vn:
        _lst = o.setdefault("vrefs", {}).setdefault(_vn, [])
        if _ref and len(_lst) < 12:
            _lst.append("%s%s%s" % (_ref.split(";")[0][:80], (" [%s]" % _ad) if _ad else "", (" %.2f %s" % (_val, (r.get("contract") or {}).get("currency") or "")).rstrip() if _val > 0 else ""))
        _pl = o.setdefault("pairs", {}).setdefault(_vn, [])
        if len(_pl) < 60:
            _pl.append((_ad, _val))
        # claude 2026-11-08 (downstream §5 / §1): the richest facts any record of this SAME buyer-vendor pair publishes, most recent first;
        # the row's proof record may lack a value or dates that a sibling record of the pair carries
        _pb = o.setdefault("pairbest", {}).setdefault(_vn, {})
        _c = r.get("contract") or {}
        _cp = classify_plus(_c, (r.get("source") or {}).get("key") or "")
        _cands = {"contract_value": _c.get("value"), "currency": _c.get("currency"), "start_date": _dd.get("start"), "end_date": _dd.get("end"), "contract_title": _c.get("title"),
                  "contract_description": re.sub(r"\s+", " ", str(_c.get("description") or ""))[:300] if _c.get("description") else "", "instrument_type": _c.get("instrument_type"),
                  "procurement_method": _c.get("procurement_method") or _c.get("solicitation_procedure"), "number_of_bids": _c.get("number_of_bids"),
                  "po_number_as_published": _cp.get("po_number_as_published"), "contract_or_agreement_number": _cp.get("contract_or_agreement_number"),
                  "solicitation_or_tender_number": _cp.get("solicitation_or_tender_number"), "award_or_notice_id": _cp.get("award_or_notice_id"),
                  "buyer_vendor_id": _cp.get("buyer_vendor_id"), "commodity_codes": _cp.get("commodity_codes"), "buyer_org_codes": _cp.get("buyer_org_codes")}
        _refid = (_ref.split(";")[0][:80] if _ref else "") or (r.get("record_id") or "")[:80]
        for _k, _v in _cands.items():
            if _v not in (None, "", {}, []) and (_k not in _pb or _ad > _pb[_k][3]):
                _pb[_k] = (str(_v), _refid, (r.get("source") or {}).get("name") or "", _ad, r.get("record_id") or "")
    # owner 2026-11-11 20:36 EST ("no buyer twice is hard rule … mark everything, prioritise over 5000"): a buyer has one row, and the record
    # that stands on it is, among the records of its best tier, one whose published value is $5,000 or more — then the most complete, then the
    # latest. Before, the most complete record stood on the row also when a contract of that size with the same or another vendor was current.
    # 2026-11-12: within the best tier, a record whose vendor the registers show alive and whose record prints the vendor's address comes first —
    # 254 buyers' rows failed on a registry warning and 166 on a missing vendor address (13:24Z table) while other contracts of theirs were clean
    _rs0 = [t_.strip() for t_ in str((r.get("vendor_enrichment") or {}).get("registry_status") or "").split(";") if t_.strip()]
    _dead0 = bool(_rs0) and bool((_DEAD_REG.search(_rs0[0]) and not _LIVE_REG.search(_rs0[0])) or (not any(_LIVE_REG.search(t_) for t_ in _rs0) and any(_DEAD_REG.search(t_) for t_ in _rs0)))
    _clean = 0 if (_dead0 or not ((r.get("vendor") or {}).get("address"))) else 1
    # 2026-11-13 (owner 13:20 EST: "add as much over 5000 as possible"): among the records that stand for a current relationship (tiers A, B, L — a
    # published end date ahead, no end date and awarded within three years: rule 11), a clean record with a published $5,000 or more comes before
    # a record of a surer tier with less; a record older than that (tier C) never comes before a current one. A ceiling (a framework, a roster) is
    # not a bill (tools/relationship_rows.is_ceiling).
    _tr = tier_of(r)
    _big = 1 if (_val >= 5000 and not _RR.is_ceiling({"instrument_type": (r.get("contract") or {}).get("instrument_type") or "", "contract_title": (r.get("contract") or {}).get("title") or "",
                                                       "procurement_method": (r.get("contract") or {}).get("procurement_method") or ""})) else 0
    _bk = (1 if _tr in ("A", "B", "L") else 0, _clean, _big, TS[_tr], sc, award_date(r) or "")
    if o["best"] is None or _bk > o["bk"]:
        o["best"], o["bs"], o["fields"], o["bk"] = r, sc, fields, _bk
        if len(name) < len(o["name"]) or not o["name"]: o["name"] = name
# 3. one row per organisation
rows = []
n_pair = collections.Counter()
MTL_KEYS = {r["buyer_key"] for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_buyer_ap_results_manual01.csv", encoding="utf-8"))}
SHARED_GOV = re.compile(r"^(?:[a-z]{2}\.gov|state\.[a-z]{2}\.us|[a-z]+\.state\.[a-z]{2}\.us|gov\.[a-z]{2}\.ca|gnb\.ca|novascotia\.ca|ontario\.ca|gouv\.qc\.ca|canada\.ca|gc\.ca|"
                        r"alberta\.ca|saskatchewan\.ca|manitoba\.ca|gov\.uk|service\.gov\.uk|nsw\.gov\.au|vic\.gov\.au|qld\.gov\.au|wa\.gov\.au|sa\.gov\.au|gov\.au|govt\.nz)$", re.I)
GENERIC_TOK = {"department", "dept", "ministry", "ministere", "ministère", "state", "province", "government", "gouvernement", "services", "service", "office", "bureau", "agency",
               "agence", "commission", "board", "authority", "canada", "ontario", "quebec", "québec", "alberta", "british", "columbia", "manitoba", "saskatchewan", "nova", "scotia",
               "brunswick", "newfoundland", "labrador", "tennessee", "texas", "california", "florida", "york", "north", "south", "west", "east", "public", "general", "national",
               "federal", "regional", "division", "branch", "secretariat", "secrétariat", "direction", "the", "and", "of", "for", "des", "du", "de", "la", "le", "les", "et"}
GENERIC_LOCAL = re.compile(r"^(?:ap|a\.?p|accounts?[._-]?payables?|payables?|invoices?|e-?invoic\w*|ap[._-]?invoices?|financial[._-]?shared[._-]?services?|shared[._-]?services?|vendors?\w*|suppliers?\w*|"
                           r"comptes?[._-]?payables?|comptes?[._-]?a[._-]?payer|factures?|facturation|accounting|finance|treasury|payments?)$", re.I)
GENERIC_PATH = {"gov", "content", "en", "fr", "sites", "default", "files", "about", "contact", "contacts", "departments", "department", "ministries", "ministry", "agencies", "agency",
                "organizations", "organisations", "fin", "finance", "shared", "services", "service", "doing-business", "business", "vendors", "vendor", "suppliers", "supplier",
                "procurement", "purchasing", "payments", "payment", "accounts-payable", "ap", "invoices", "invoice", "forms", "documents", "publications", "media", "uploads",
                "pdf", "pdfs", "assets", "docs", "government", "governments", "topics", "programs", "program", "index", "home", "www", "www2", "wp-content", "portal", "treasury", "treasury-board"}
def shared_gov_page_names_buyer(e, page, quote, name):
    """on a government-wide mail domain (tn.gov, canada.ca, gov.bc.ca…) a mailbox counts for THIS body when (a) it is the government's generic
    AP / shared-services mailbox, or (b) the page or quote names the body, and never when the page sits under another agency's path
    (spot-check 2026-11-04: tn.gov/correction/… credited to the Department of Transportation)"""
    local = e.split("@")[0].lower()
    nm = norm(re.sub(r"\(.*?\)", " ", name))
    words = [w for w in re.split(r"[^a-z0-9]+", nm) if w]
    toks = [t for t in words if len(t) >= 5 and t not in GENERIC_TOK]
    acrs = {"".join(w[0] for w in words if w not in ("of", "the", "and", "de", "du", "des", "la", "le", "les", "et", "for")), "".join(w[0] for w in words)}
    acrs |= {m.lower() for m in re.findall(r"\(([A-Z]{3,6})\)", name)}
    acrs = {a for a in acrs if len(a) >= 3}
    hay = ((page or "") + " " + (quote or "")).lower()
    named = any(t in hay for t in toks) or any(re.search(r"(?<![a-z])%s(?![a-z])" % re.escape(a), hay) for a in acrs) or any(a in local for a in acrs)
    segs = [sg for sg in (urllib.parse.urlparse(page or "").path or "").lower().split("/") if sg]
    first = next((sg for sg in segs if not re.match(r"^[a-z]{2}(?:-[a-z]{2})?$", sg)), "")  # the first path segment names the agency on a shared site (tn.gov/correction)
    conflict = bool(first) and first not in GENERIC_PATH and len(re.sub(r"[^a-z]", "", first)) >= 4 and not named and not any(t in first for t in toks) and not any(a in first for a in acrs)
    if named:
        return True
    if GENERIC_LOCAL.match(local) and not conflict:
        return True  # the government's own AP / shared-services box, published on a government page that names no other agency
    return False
# 2026-11-12 (rows read for the owner, AGENTS.md §2.5 "role mailboxes the organisation publishes itself"): where a mailbox was read decides
# whose it is. Read on the organisation's own pages — its site's or its mailbox's domain, another domain whose name spells it, an archive
# capture of one of them, its pages on a hosting service, or its government's page that names it — it is the organisation's. Read on another
# organisation's page — a community directory (211, CIOC), a regional body's list, a tourism or business directory, Wikivoyage — it is not
# used: such a page put a neighbouring parish's mailbox on Sainte-Marie-Madeleine's row. The mailbox reader reads the organisation's own site.
_HOSTING_HOST = re.compile(r"(^|\.)(wixsite\.com|wix\.com|filesusr\.com|squarespace\.com|squarespace-cdn\.com|square\.site|wordpress\.com|wp\.com|webflow\.io|"
                           r"website-files\.com|myshopify\.com|janeapp\.com|churchcenter\.com|clubrunner\.ca|wildapricot\.org|weebly\.com|godaddysites\.com|"
                           r"site123\.me|amazonaws\.com|cloudfront\.net|googleusercontent\.com|ctfassets\.net|hubspotusercontent[\w-]*\.net|hs-sites\.com|"
                           r"azurewebsites\.net|azureedge\.net|windows\.net|netlify\.app|vercel\.app|github\.io|herokuapp\.com|sharepoint\.com|canva\.site|"
                           r"carrd\.co|strikingly\.com|jimdosite\.com|jimdo\.com|yolasite\.com|edan\.io|govstack\.com|civicweb\.net|escribemeetings\.com|"
                           r"google\.com|merx\.com|bidsandtenders\.ca|bonfirehub\.ca|bonfirehub\.com)$", re.I)
_GOV_PAGE_HOST = re.compile(r"(^|\.)(gc\.ca|canada\.ca|gouv\.qc\.ca|quebec\.ca|gov\.[a-z]{2}\.ca|alberta\.ca|ontario\.ca|saskatchewan\.ca|manitoba\.ca|novascotia\.ca|"
                            r"gnb\.ca|yukon\.ca|princeedwardisland\.ca|gov\.uk|gov\.au|govt\.nz|gov|gouv\.fr|europa\.eu)$", re.I)
_DIR_HOST = re.compile(r"(?:^|\.)(?:211[a-z-]*|[a-z-]*cioc|informalberta|municipalites-du-quebec|lecegep|lappui|leslibraires|maillon[a-z-]*|arboquebec|"
                       r"wikivoyage|wikipedia|yellowpages|pagesjaunes|canada411|411|yelp|tripadvisor|facebook|linkedin|instagram|eventbrite|growthzoneapp|"
                       r"chambermaster|micronetonline|bbb|manta|zoominfo|cylex|hotfrog|mtl|reseaucapital)\.[a-z.]+$|(?:^|\.)(?:directory|annuaire|repertoire|bottin)\.|"
                       r"peppol|tourism|tourisme|visit[a-z]|chamber|chambre", re.I)
_DIR_PATH = re.compile(r"/(?:findhealth|directory|directories|repertoire|r%c3%a9pertoire|annuaire|bottin|members?|membres?|member-directory|list/member|record)(?:/|\b|-)", re.I)
_LIST_PATH = re.compile(r"director|r[ée]pertoire|repertoire|annuaire|bottin|members?\b|membres|listing|commerces|entreprises|businesses", re.I)
_INVOICE_PATH = re.compile(r"invoic|factur|payable|supplier|vendor|fournisseur|procure|purchas|achat|approvision|financ|accounts|comptab|doing-business|"
                           r"faire-affaire|paiement|payment|contrat|contract", re.I)
def names_in_text(text, name):
    """the text names the organisation: a distinctive word of its name (five letters and more) or its acronym, as a whole word"""
    nm = norm(re.sub(r"\(.*?\)", " ", name or ""))
    words = [w for w in nm.split() if w]
    toks = [t for t in words if len(t) >= 5 and t not in GENERIC_TOK]
    acrs = {"".join(w[0] for w in words if w not in ("of", "the", "and", "de", "du", "des", "la", "le", "les", "et", "for")), "".join(w[0] for w in words)}
    acrs |= {m.lower() for m in re.findall(r"\(([A-Z]{3,6})\)", name or "")}
    t = " " + norm(text) + " "
    return any((" %s " % x) in t for x in toks) or any(len(a) >= 3 and (" %s " % a) in t for a in acrs)
def table_row_names(e, quote, name):
    """in a table of institutions and their mailboxes, the institution named just before this mailbox (after the one before it) is the buyer"""
    q = quote or ""
    i = q.lower().find((e or "").lower())
    if i < 0:
        return False
    before = re.split(r"\S+@\S+", q[:i])[-1][-160:]
    return names_in_text(before, name)
def sibling_domain(md, sh, name):
    """@tamuk.edu (Texas A&M–Kingsville) on tamu.edu's page: a sister body's mail domain is the site's name and one or two letters more —
    unless those letters are the buyer's own acronym (@eosda.com for EOS Data Analytics on eos.com)"""
    flat = lambda x: re.sub(r"[^a-z0-9]", "", x or "")
    core, bcore = flat(registrable(md or "").split(".")[0]), flat(registrable(sh or "").split(".")[0])
    if not (len(bcore) >= 2 and core != bcore and core.startswith(bcore) and len(core) - len(bcore) <= 2):
        return False
    words = [w for w in norm(name).split() if w]
    acr = "".join(w[0] for w in words if w not in ("of", "the", "and", "de", "du", "des", "la", "le", "les", "et"))
    return not (acr.startswith(core) or core == flat(norm(name)))
def mail_page_own(e, page, site, name, quote=""):
    if not page:
        return True  # no page: the other checks decide (a mailbox with no page is never confirmed in the first place)
    ph = host_of(page) or ""
    pd = registrable(ph) if ph else ""
    md = registrable((e or "").split("@")[-1].lower())
    sd = registrable(host_of(site) or "") if site else ""
    if pd and pd in (md, sd):
        return True
    if _DIR_HOST.search(ph) or _DIR_PATH.search(urllib.parse.urlparse(page).path or ""):
        return False  # a directory or roster (211, CIOC, a chamber's or a register's list, Wikivoyage, the PEPPOL directory): never the organisation's own page
    if md and (md == sd or (sd and md.split(".")[0] == sd.split(".")[0])):
        return True  # the mailbox is on the organisation's own domain (or its twin: baskinsulation.com for baskinsulation.ca); the page is another site or file of its own (braudio.ca read on brianreimeraudio.com)
    _a = re.search(r"archive\.org/web/\d+[a-z_]*/(https?://\S+)", page)
    if _a and registrable(host_of(_a.group(1)) or "") in (md, sd):
        return True
    _cores = {x.split(".")[0] for x in (md, sd) if x}
    if any(lab in _cores for lab in ph.split(".")[:-2]):
        return True  # metrolinx.merx.com, sts.saguenay.ca: a host whose own label is the organisation's
    if pd and same_org("x@" + pd, site or "https://unknown.invalid", name) and not _HOSTING_HOST.search(ph) and not _GOV_PAGE_HOST.search(ph):
        return True  # another domain of its own whose name spells it (ville.montreal.qc.ca for montreal.ca, nlliquorcorp.com)
    if _HOSTING_HOST.search(ph):
        return md == sd or bool(sd and sd.split(".")[0] in ph) or same_org(e, site or "https://unknown.invalid", name)  # its own pages or files on a hosting service
    if _GOV_PAGE_HOST.search(ph):
        return names_in_text((quote or "") + " " + re.sub(r"[/_.-]+", " ", urllib.parse.urlparse(page).path or ""), name) or same_org(e, "https://unknown.invalid", name)
    return False
n_mailrej, n_mailrej_ex = collections.Counter(), []
CB_NOMAIL = []  # (buyer key, name, website, records) of buyers under a current contract with no confirmed mailbox of their own
CB_NOSITE = []  # (buyer key, name, address) of buyers under a current contract with no mailbox and no website on file (2026-11-12)
# the website an Overture Maps place lists under such a buyer's very name at its postal code, kept only when the site's own home page carries the
# name or prints the postal code (tools/overture_names.py query --lanes cb, then verify --lane cb): data/incoming/claude/overture/cb_sites.csv
CB_SITES = {}
if os.path.exists(ROOT + "/data/incoming/claude/overture/cb_sites.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/overture/cb_sites.csv", encoding="utf-8", newline="")):
        if _r.get("site"):
            CB_SITES[_r["key"]] = _r
# 2026-11-13: a buyer under contract with no website on file whose very name is the label of one Wikidata item giving an official website (P856):
# 72 Québec cégeps, agencies, museums and Ontario hospitals (data/incoming/claude/cb_sites_wd.csv); the mailbox reader then reads that site, and
# the mailbox must still fit the buyer's name there (same_org)
if os.path.exists(ROOT + "/data/incoming/claude/cb_sites_wd.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/cb_sites_wd.csv", encoding="utf-8", newline="")):
        if _r.get("site") and _r["key"] not in CB_SITES:
            CB_SITES[_r["key"]] = dict(_r, _src="wikidata")
n_cbsite = collections.Counter()
_AP_LOCAL = re.compile(r"invoic|factur|payables?|acctpay|accountspayable|accounts[._-]?pay|comptes?[._-]?(?:payables?|a[._-]?payer|fournisseurs?)|comptesapayer|(?:^|[._-])a\.?p(?:$|[._-])|^ap[a-z]{0,3}invoice", re.I)
_WEBMAIL = re.compile(r"^(?:gmail|googlemail|hotmail|outlook|live|msn|yahoo|ymail|icloud|me|aol|protonmail|proton|gmx|videotron|sympatico|bell|rogers|shaw|telus|eastlink|cogeco)\.(?:com|ca|net|fr|co\.uk)$", re.I)
def emailcols(keys, be, gj="", name="", site=""):
    def own(e, page="", quote=""):
        if keys & MTL_KEYS and re.search(r"@(ville\.)?montreal\.(ca|qc\.ca)$", e or "", re.I):  # units of the Ville de Montréal (manual01)
            return True
        if "direct-deposit" in page or "depot-direct" in page:  # PSPC's table maps each federal institution to its mailbox
            # 2026-11-12: the row of THIS institution — the one named just before the mailbox. The Privy Council Office had taken the Privacy
            # Commissioner's finances@priv.gc.ca, the line above its own in the table.
            return table_row_names(e, quote, name) or bool(site and registrable((e or "").split("@")[-1].lower()) == registrable(host_of(site) or ""))
        md = (e or "").split("@")[-1].lower()
        # 2026-11-12: where a buyer's OWN site says invoices go is its invoicing mailbox, also on another mail domain — its health network's
        # (ssss.gouv.qc.ca for every establishment of Québec's network), its parent's (nlh.nl.ca on nlhydro.com), its shared-service centre's or
        # its e-invoicing provider's (…@pdf.basware.com, …coupahost.com). 331 buyers under contract had such a mailbox, verified, and no
        # mailbox on their row (table of 00:14Z). Only an invoicing local part, only a page of the buyer's own site (never a government-wide
        # site), never a webmail address.
        _ph, _sh = (urllib.parse.urlparse(page or "").hostname or "").lower(), (urllib.parse.urlparse(site if "//" in (site or "") else "https://" + (site or "")).hostname or "").lower()
        # 2026-11-12 (rows read for the owner): not a page that lists other organisations — a town's business directory printed a contractor's
        # ap@ (Crossfield took Boom Construction's), a university system's contacts page a sister campus's (Texas A&M took Kingsville's
        # invoices@tamuk.edu): not a list page, and the mail domain is not a sibling's
        if (_ph and _sh and registrable(_ph) == registrable(_sh) and not SHARED_GOV.match(registrable(_ph)) and _AP_LOCAL.search((e or "").split("@")[0])
                and not _WEBMAIL.search(md) and not SHARED_GOV.match(md) and not _LIST_PATH.search(urllib.parse.urlparse(page).path or "")
                and not sibling_domain(md, _sh, name)):
            n_mailrej["(taken) an invoicing mailbox the buyer's own site prints, on another mail domain"] += registrable(md) != registrable(_sh)
            return True
        if SHARED_GOV.match(md) and not shared_gov_page_names_buyer(e, page, quote, name):
            return False  # another agency's mailbox on the same government domain (spot-check 2026-11-04: tn.gov/correction credited to TDOT)
        if gj and gj != "FED" and jur_of_mail(e) == gj and re.search(r"@(gov\.[a-z]{2}\.ca|gnb\.ca|novascotia\.ca|ontario\.ca)$", e or "", re.I):
            return True  # a provincial government's shared mail domain, for a body of that same government
        if not site and page:  # no known website: the page counts as the buyer's own site only if its domain names the buyer
            h = (urllib.parse.urlparse(page).hostname or "").lower()
            if h and same_org("x@" + registrable(h[4:] if h.startswith("www.") else h), "https://unknown.invalid", name):
                return same_org(e, "https://" + h, name)
        return same_org(e, site or "https://unknown.invalid", name)
    fits = lambda e, page="", quote="": (not gj or jur_of_mail(e) in ("", gj)) and not BAD_LOCAL.search((e or "").split("@")[0]) and own(e, page, quote) \
        and mail_page_own(e, page, site or ("https://" + (e or "").split("@")[-1]), name, quote)
    LABEL = {4: "invoicing/AP", 3: "finance/accounting dept or supplier-payment office", 2: "purchasing", 1: "general"}
    opts = []  # (accepted, grade, row) from the referee's mailboxes and from earlier enrichment; the best accepted one wins
    for k in sorted(k for k in keys if k):  # sorted: equal mailboxes are broken the same way on every run (a set's order is random)
        _alt = next(((s_, m_) for s_, m_ in sorted(MAIL_ALL.get(k, ()), key=lambda sm: sm[0], reverse=True)
                     if fits(m_["mailbox"], m_.get("evidence_url") or "", m_.get("evidence_quote") or "")), None) if k in mail and not fits(
                         mail[k][1]["mailbox"], mail[k][1].get("evidence_url") or "", mail[k][1].get("evidence_quote") or "") else None
        if _alt:
            (acc, g), m = _alt
            n_mailrej["(taken) another verified mailbox of the buyer, the best-graded one being another organisation's"] += 1
            opts.append(((acc, g), (m["mailbox"], LABEL[g], "confirmed" if acc else m["check_status"], m["evidence_url"], m["evidence_quote"], g, acc)))
        elif k in mail and fits(mail[k][1]["mailbox"], mail[k][1].get("evidence_url") or "", mail[k][1].get("evidence_quote") or ""):
            (acc, g), m = mail[k]
            opts.append(((acc, g), (m["mailbox"], LABEL[g], "confirmed" if acc else m["check_status"], m["evidence_url"], m["evidence_quote"], g, acc)))
        elif k in mail:
            # 2026-11-12: why a mailbox the referee holds for this buyer is not taken — counted (1,400 buyers under contract had one and no
            # mailbox on their row in the table of 00:14Z; behind them 77,330 buyer-vendor relationships)
            _e = mail[k][1]["mailbox"]
            _md = (_e or "").split("@")[-1].lower()
            n_mailrej["another government's mail domain" if (gj and jur_of_mail(_e) not in ("", gj)) else
                      "a mailbox for something else (press, complaints, admissions, receivables …)" if BAD_LOCAL.search((_e or "").split("@")[0]) else
                      "a government-wide mail domain, and the page does not name this body" if SHARED_GOV.match(_md) else
                      "read on another organisation's page (a directory, a regional body's, a partner's), not on its own" if not mail_page_own(
                          _e, mail[k][1].get("evidence_url") or "", site or ("https://" + _md), name, mail[k][1].get("evidence_quote") or "") else
                      "the mail domain is not the buyer's own"] += 1
            if len(n_mailrej_ex) < 60:
                n_mailrej_ex.append("%s | %s | %s | %s" % (name[:50], _e, site[:40], (mail[k][1].get("evidence_url") or "")[:70]))
    for kind in ("ap_contact", "procurement_contact", "general_contact"):  # earlier enrichment, evidence kept
        c = be.get(kind) or {}
        if c.get("emails") and fits(c["emails"][0]) and roleish(c["emails"][0].split("@")[0], name):
            ev = (c.get("evidence") or [{}])[0] if isinstance(c.get("evidence"), list) else {}
            if not ev.get("page_url"):
                continue  # evidence or nothing: an enrichment contact without the page it was read on is not delivered
            g = real_grade(c["emails"][0], {"ap_contact": "accounts_payable", "procurement_contact": "procurement", "general_contact": "general"}[kind], (ev.get("quote") or ev.get("snippet") or ""), name)
            if g >= 1:  # owner 2026-11-04 ("ironclad"): only a mailbox the referee saw on the page counts as confirmed; the dataset
                # build's mailboxes are re-submitted as claude_buyer_ap_results_dsenrich01.csv and come back as referee rows above.
                # Until then they rank below any confirmed mailbox and never make Gold (batches.py routes them to P11).
                opts.append(((False, g), (c["emails"][0], LABEL[g], "from dataset enrichment", ev.get("page_url", ""), (ev.get("quote") or ev.get("snippet") or "")[:300], g, False)))
    if opts:
        return max(opts, key=lambda x: x[0])[1]
    return "", "", "", "", "", 0, False
def fill_contract(x, r, keys):
    """owner 2026-11-03: every field the record or the release tables give is filled (the rest becomes not_published in batches.py)"""
    v, ve, src = r.get("vendor") or {}, r.get("vendor_enrichment") or {}, r.get("source") or {}
    _vd = (r.get("contract") or {}).get("value_detail") or {}
    if x.get("contract_value") and _vd.get("value_basis") and "(" not in str(x["contract_value"]):  # reviewer 2026-11-08: a submitted price must not look like an award value
        x["contract_value"] = "%s (%s)" % (x["contract_value"], str(_vd["value_basis"])[:200])
    if x.get("currency") == "CAD" and (r.get("contract") or {}).get("currency_basis"):
        x["currency"] = "CAD (%s)" % (r["contract"]["currency_basis"])
    x["buyer_address"] = addr_text(json.loads(x["buyer_address"]) if x["buyer_address"].startswith("{") and x["buyer_address"].endswith("}") else {}) \
        or addr_text((r.get("buyer") or {}).get("address")) or next((addr_text(BUY[k].get("address")) for k in keys if k in BUY and BUY[k].get("address")), "")
    if not x["buyer_website"]:
        x["buyer_website"] = next((BUY[k]["official_website"] for k in keys if k in BUY and BUY[k].get("official_website")), "")
    tv = TEAMV.get(ve.get("vendor_key") or "")
    if tv:
        have = set(e.strip().lower() for e in (x.get("vendor_emails") or "").split(";") if e.strip())
        x["vendor_emails"] = "; ".join(sorted(have | set(tv["emails"]) | set(tv["billing"])))
        x["vendor_billing_ar_email"] = "; ".join(tv["billing"])
        if not x.get("vendor_website") and tv["website"]:
            x["vendor_website"] = tv["website"]
        x["vendor_contacts_found_by"] = "%s lane, referee-verified on %s" % (tv["by"], "; ".join(tv["pages"])[:300])
    for col, val in vend_fill(ve.get("vendor_key") or "", v.get("name") or "").items():
        if not x.get(col) and val:
            x[col] = val
    if not x["vendor_legal_name"] and ve.get("legal_name"):
        x["vendor_legal_name"] = ve["legal_name"]
    if x["vendor_bn9"] and not x["vendor_gst_hst_derived"]:
        x["vendor_gst_hst_derived"] = x["vendor_bn9"] + "RT0001"
    if x["contract_value"] and not x["currency"] and CUR.get(jur_of_record(r)):
        x["currency"] = CUR[jur_of_record(r)] + " (derived from the source's government)"
    if not x["contract_link"]:
        x["contract_link"] = src.get("record_url") or src.get("dataset_url") or ""
    if x["contract_reference"] in ("{}", "") and r.get("record_id"):
        x["contract_reference"] = json.dumps({"record_id": r["record_id"]}, ensure_ascii=False)
    x["_jur"] = (r.get("buyer") or {}).get("country") or ""  # filled after the one-row-per-body merge, which keys on jurisdiction
for p, o in orgs.items():
    r, be = o["best"], o["be"]
    c, v, ve, d = r["contract"], r.get("vendor") or {}, r.get("vendor_enrichment") or {}, (r["contract"].get("dates") or {})
    gj = o["jur"].most_common(1)[0][0] if o["jur"] else ""
    if not (be.get("official_website") or "").strip():
        _cbs = next((CB_SITES[k_] for k_ in sorted(k for k in o["keys"] if k) if k_ in CB_SITES), None)
        if _cbs:
            be = dict(be, official_website=_cbs["site"], _site_basis=_cbs.get("tied_by") or "")
            o["be"] = be; n_cbsite["buyer under contract: website from %s" % ("its Wikidata item (P856, the item's label is its name)" if _cbs.get("_src") == "wikidata" else "an Overture Maps place, tied on its own home page")] += 1
    em, et, es, eu, eq, g, acc = emailcols(o["keys"], be, gj, o["name"], be.get("official_website") or "")
    tier = tier_of(r)
    if not (em and acc) and tier in ("A", "B", "L") and not (be.get("official_website") or "").strip() and any(o["keys"]):
        # (a buyer with no key of its own — 2026-11-13 01:07Z build failed on one with IndexError — is not listed)
        CB_NOSITE.append((sorted(k for k in o["keys"] if k)[0], o["name"], be.get("address") or {}))
    if not (em and acc) and tier in ("A", "B", "L") and (be.get("official_website") or "").strip():
        # 2026-11-12: a buyer under a current contract with no mailbox of its own on file: its own site goes to the mailbox reader
        # (coord/results/ranked/contract_buyers_without_mailbox.csv, read by tools/lead_crawl.py on the mailbox-crawl runners)
        _ws = be["official_website"].strip()
        _wh = registrable(host_of(_ws) or "")
        if _wh and not SHARED_GOV.match(_wh):
            CB_NOMAIL.append((sorted(k for k in o["keys"] if k)[0], o["name"], _ws, o["n"]))
    score = TS[tier] * 10 + g * 6 + (3 if acc else 0) + o["fields"]
    a = v.get("address") or {}
    rows.append({"jurisdiction": gj, "rank_group": ("GOLD" if tier in "AB" and g == 4 and acc else "%s%d" % (tier, g)), "completeness_score": score,
        "buyer": o["name"], "buyer_website": be.get("official_website") or "", "buyer_address": json.dumps(be.get("address") or {}, ensure_ascii=False)[:200],
        "email": em, "email_type": et, "email_check": es, "email_evidence_url": eu, "email_evidence_quote": eq,
        "contract_status": {"A": "active (published end date today or later)", "B": "likely active (" + (("Québec, awarded in the last 3 years, no closing notice" if jur_of_record(r) == "QC" else "source marks it as continuing; awarded in the last 3 years, no end date published") if r["status"] == "ongoing_inferred" and award_date(r) >= CUTOFF3 else "awarded in the last 12 months, no end date published") + ")", "L": "likely active (awarded 12-36 months ago, no end date published; multi-year contracts often still run)", "C": "end date unknown, awarded over 3 years ago"}[tier], "contract_reference": json.dumps(c.get("identifiers") or {}, ensure_ascii=False)[:3000], "contract_title": (c.get("title") or "")[:200], **rec_extra(c), **classify_plus(c, (r.get("source") or {}).get("key") or ""),
        "contract_value": c.get("value") or "", "currency": c.get("currency") or "", "award_date": award_date(r), "start_date": d.get("start") or "", "end_date": d.get("end") or "",
        "contract_link": r.get("link") or "", "source": (r.get("source") or {}).get("name", ""), "vendor": v.get("name") or "", "vendor_legal_name": ve.get("legal_name") or "",
        "vendor_address": ", ".join(x for x in (a.get("line1"), a.get("city"), a.get("region"), a.get("postal_code")) if x), "vendor_country_basis": v.get("country_basis") or "",
        "vendor_bn9": ve.get("business_number_bn9") or "", "vendor_gst_hst_derived": ve.get("gst_hst_account_derived") or "", "vendor_website": ve.get("website") or "",
        "vendor_emails": "; ".join((x.get("email") or x.get("value") or "") if isinstance(x, dict) else str(x) for x in (ve.get("contact_emails_published") or [])), "contracts_with_canadian_suppliers": o["n"], "buyer_keys": len(o["keys"]), "keys": "|".join(sorted(k for k in o["keys"] if k)), "tier": tier, "grade": g, "acc": acc})
    fill_contract(rows[-1], r, o["keys"])
    x = rows[-1]
    if not x.get("end_date") and d.get("end_inferred"):  # downstream §5.3: the pipeline's inferred end (award date + published duration), labelled
        x["end_date"] = "%s (inferred: award date + the duration the source publishes; see contract_status)" % str(d["end_inferred"])[:10]; n_pair["end_date_inferred"] += 1
    if not x.get("start_date") and d.get("signed"):
        x["start_date"] = "%s (contract signature date as published)" % str(d["signed"])[:10]; n_pair["start_from_signed"] += 1
    x["distinct_canadian_vendors"] = str(len(o["vendors"]))
    x["records_last_12_months"] = str(o["n12"])
    x["latest_award_date_any_vendor"] = o["latest"]
    x["total_known_value_canadian_suppliers"] = ("%.2f %s over %d of %d records with a published value" % (o["value"], "/".join(k for k, _ in o["cur"].most_common(2)), o["nval"], o["n"])) if o["nval"] else ""
    x["other_canadian_vendors_sample"] = "; ".join("%s (%d)" % (n, c) for n, c in o["vendors"].most_common(6) if n != x.get("vendor"))[:400]
    x["record_sources"] = "; ".join("%s (%d)" % (n, c) for n, c in o["sources"].most_common(4))[:300]
    _vr = (o.get("vrefs") or {}).get((x.get("vendor") or "").strip(), [])
    x["records_with_this_vendor"] = str(o["vendors"].get((x.get("vendor") or "").strip(), 0))
    x["all_references_with_this_vendor"] = "; ".join(_vr)[:800]
    x["most_recent_record_reference_any_vendor"] = o.get("latest_ref") or ""
    # same-pair fill: a contract fact the proof record lacks, taken from another record of the same buyer-vendor pair (labelled with that record)
    _pb = (o.get("pairbest") or {}).get((x.get("vendor") or "").strip(), {})
    for _k, (_v, _refid, _srcn, _ad, _rid) in _pb.items():
        if _k == "currency" or x.get(_k) or not _v or _rid == r.get("record_id"):
            continue
        # reviewer 2026-11-08: another contract's facts stay in their own columns; the row's contract columns describe the proof record only
        x[_k + "_from_pair"] = "%s (another record of the same buyer-vendor pair: %s, %s%s)" % (_v[:300 if _k == "contract_description" else 200], _refid or "record", _srcn, (", " + _ad) if _ad else "")
        n_pair[_k] += 1
        if _k == "contract_value" and _pb.get("currency"):
            x["contract_value_from_pair"] += " %s" % _pb["currency"][0]
    x["_org"] = o
    x["org_group_key"] = o.get("p") or ""  # the grouping key of the contract records (contracts_export joins on it)
    x["vendor_registry_status"] = x.get("vendor_registry_status") or ve.get("registry_status") or ""
    x["vendor_registry_match_level"] = ve.get("registry_match_level") or ""
    x["vendor_incorporation_date"] = x.get("vendor_incorporation_date") or (ve.get("incorporation_or_registration_date") or "")[:10]
    x["vendor_bn_source"] = ve.get("business_number_source") or ""
print("same-pair fill (facts from another record of the same buyer-vendor pair):", dict(n_pair))
print("buyers under contract: a mailbox the referee holds that is not taken for the row, by reason: %s | examples (buyer | mailbox | site on file | page it was read on): %s"
      % (dict(n_mailrej.most_common()), " ;; ".join(n_mailrej_ex[:60])))
print("contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used):", n_ve_form)
for _o in orgs.values():  # used only while the organisation's row was built
    _o.pop("pairbest", None); _o.pop("vrefs", None); _o["best"] = None
# 4. buyers proven by payment / subaward records or client listings (no contract in the dataset)
leads = {r["buyer_key"]: r for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_buyer_leads.csv", encoding="utf-8", errors="replace"))}
# 2026-11-10: the cloud row factory (tools/cc_clients.py: client pages of .ca vendors read from the Common Crawl archive, vendor's Canadian postal
# address quoted) writes its own file, so the Mac's bridge (which rewrites claude_buyer_leads.csv whole) can never drop a cloud lead
_n_cc = 0
# 2026-11-10 (tools/lead_store.py): the cloud leads are a frozen base file plus append-only shards (lead_shards/: rows added, changed or withdrawn
# by the engines since); the store gives the current state of both the rows and their details
import lead_store as _LS
_cl, _cd = _LS.load()
for _k, r in _cl.items():
    if _k not in leads:
        leads[_k] = r
        _n_cc += 1
# tenant leads accepted by the candidate crawl (stores on Shopify, customer portals) arrive in their own append-only shards (tenant_state/)
_n_ts = 0
for _p in sorted(_g0.glob(ROOT + "/data/incoming/claude/tenant_state/leads_*.gz")):
    with gzip.open(_p, "rt", encoding="utf-8", newline="") as _fh:
        for r in csv.DictReader(_fh):
            if r.get("buyer_key") and r["buyer_key"] not in leads:
                leads[r["buyer_key"]] = r
                _n_ts += 1
print("tenant leads from the shards: %d" % _n_ts)
# websites found later for leads that had none (tools/lead_sites.py: Wikidata official website of an item whose label equals the buyer's name)
_n_lw = 0
if os.path.exists(ROOT + "/data/incoming/claude/claude_lead_websites.csv"):
    for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_lead_websites.csv", encoding="utf-8", errors="replace")):
        _L = leads.get(r.get("buyer_key"))
        if _L is not None and not (_L.get("website") or "").strip() and (r.get("website") or "").startswith("http"):
            _L["website"] = r["website"]; _n_lw += 1
print("leads: %d (%d from the cloud row factory; %d websites from the lead site finder)" % (len(leads), _n_cc, _n_lw))
class PackedRecords:
    """a table of JSON records kept compressed (2026-11-10): 238,266 lead details were 477 MB as dicts — 2 KB each — and the table grows with
    the leads, not with the rows that use them. A record is unpacked when asked for; the last one asked stays unpacked, because the lead loop
    asks for the same key several times. What get() returns is a copy for reading: nothing written to it is kept."""
    __slots__ = ("d", "_k", "_v")
    def __init__(self):
        self.d, self._k, self._v = {}, None, None
    def setdefault(self, k, v):
        if k not in self.d:
            self.d[k] = zlib.compress(json.dumps(v, ensure_ascii=False, separators=(",", ":")).encode("utf-8"), 1)
    def get(self, k, default=None):
        if k is not None and k == self._k:
            return self._v
        b = self.d.get(k)
        if b is None:
            return default
        self._k, self._v = k, json.loads(zlib.decompress(b))
        return self._v
    def __contains__(self, k):
        return k in self.d
    def __len__(self):
        return len(self.d)
LDET = PackedRecords()  # owner 2026-11-03 ("every field"): the lead's own record details (amount, currency, identifiers, dates, vendor address, title)
for _ldp in ("claude_lead_details.jsonl.gz",):
    if os.path.exists(ROOT + "/data/incoming/claude/" + _ldp):
        for _d in jl(ROOT + "/data/incoming/claude/" + _ldp):
            LDET.setdefault(_d.get("key"), _d)
for _k, _d in _cd.items():  # the cloud leads' details: base file, then the shards (the newest record of a key wins: an engine may refresh a licence fee or a date)
    LDET.setdefault(_k, _d)
del _cl, _cd
for _p in sorted(_g0.glob(ROOT + "/data/incoming/claude/tenant_state/details_*.gz"), reverse=True):
    for _d in jl(_p):
        LDET.setdefault(_d.get("key"), _d)
LFACTS = {}  # 2026-11-10: what the cloud mailbox crawl read on the buyer's OWN pages (tools/lead_crawl.py): its name and its postal address, quoted
# 2026-11-13: tools/addr_reread.py reads an address the organisation states in its page's source rather than its text — the schema.org PostalAddress
# of its own JSON-LD, or the place of the Google map its own page embeds — and the cell says which (address_how)
_LF_HOW = {"jsonld": "as its own page states it in its structured data (schema.org PostalAddress)", "map": "the place of the Google map its own page embeds",
           "legal": "as its own privacy / terms / legal page prints it, beside its own name",
           # 2026-11-13 (tools/addr_reread.py --city): printed without a postal code; the city names the distributor (every postal code of it in one territory)
           "street_city": "as its own page prints it, street and city without a postal code",
           "city_contact": "the city its own contact page names (no street address printed)",
           # 2026-11-13 (tools/registry_locate.py): the head office the organisation declares to its business register, matched on its very name and province
           "registry": "as the organisation declares it to its business register (head office / registered office; the name and the province agree)"}
def lf_cell(f, url=""):
    return "%s (%s on %s, read %s)" % (f["address"], _LF_HOW.get(f.get("address_how") or "", "as printed"), f.get("address_url") or url or "", f.get("date") or "")
LFACTS_DOM = {}  # the same facts by website domain: a row made under another key of the same site (a registry lead, a credit lead) uses them too
from ap_crawler import address_from as _addr_from
import lead_crawl as _LCF  # the facts: the single file of before 2026-11-10 plus the append-only shards (site_facts/)
import tech_relationships as _TR
# how vendors bill, in their own words (tools/vendor_billing.py; the vetted vendors' terms read by hand): owner's bar of 2026-11-11, used by lead_strength
# and by the recurring_billing columns
import vendor_billing as _VB
import payee_billing as _PAYEE
import by_location as _BYLOC  # how the bodies behind the register / roster / licence lanes send their bill and take the money (hand-read, quoted)
import relationship_rows as _RR  # the owner's test of a row (how the bill is paid, the fields of its kind, ship ready): one function for this table and for tools/relationship_rows.py
try:
    VBILL = _VB.load()
except Exception as _e:
    VBILL = {}
    print("vendor billing facts not loaded: %s" % _e)
_BILL_CUR, _BILL_CUR_DOM = {}, {}
for _v in _TR.VENDORS.values():
    if _v.get("billing"):
        for _n in (_v.get("legal"), _v.get("name"), "%s dba %s" % (_v.get("legal") or "", _v.get("name") or "")):
            if _n:
                _BILL_CUR.setdefault(norm(_n), _v["billing"])
        _h = registrable(host_of(_v.get("hq_url") or "") or "")
        if _h:
            _BILL_CUR_DOM.setdefault(_h, _v["billing"])
for _h, _b in getattr(_TR, "BILLING_BY_DOMAIN", {}).items():
    _BILL_CUR_DOM.setdefault(_h, _b)
n_name_again = 0
MOVED = {}  # lead key -> (domain name on file, site that answers, final URL, day read): a second name of the organisation (tools/lead_crawl.py moved_site_ok)
for _d in _LCF.facts_records():
    if _d.get("key"):
        if _d.get("moved") and _d.get("asked"):
            MOVED[_d["key"]] = (_d["asked"], _d.get("site") or "", _d["moved"], _d.get("date") or "")
        if not _d.get("site_name") and _d.get("title"):
            # the name is read out of the stored home-page title again with today's rule (2026-11-10: 3,495 sites had a title and no name — the
            # rule of the day they were read did not know initials: "Comox Valley Animal Hospital" on cvah.ca, "Ordre des Géologues du Québec" on ogq.qc.ca)
            _d["site_name"] = _LCF.site_name_for(host_of(_d.get("site") or ""), None, _d["title"], _TR)
            n_name_again += bool(_d["site_name"])
        if _d.get("address_quote") and _d.get("address_how") not in ("jsonld", "map", "street_city", "city_contact", "registry"):  # the address is cut out of the quote again with today's rule (a telephone number or a year in front of it was taken for the street number)
            _d["address"] = _addr_from(_d["address_quote"]) or _d.get("address") or ""
            if not _d["address"] and (_d.get("address_country") or "") != "CA":
                # 2026-11-13 (rule 18, utilities abroad): a U.S. address the cutter does not take whole — the quote up to its ZIP code stands for it
                _mz = _BYLOC.US_ZIP_RX.search(_d["address_quote"])
                if _mz:
                    _d["address"] = re.sub(r"\s+", " ", _d["address_quote"][max(0, _mz.end() - 120):_mz.end()]).strip()
                elif (_d.get("address_country") or "") in ("KY", "BB", "BM"):  # an island a Caribbean utility serves whole (lead_crawl KY/BB/BM_ADDR)
                    _d["address"] = re.sub(r"\s+", " ", _d["address_quote"][-160:]).strip()
        if "?" in (_d.get("address_url") or ""):
            # a visitor or campaign identifier a site adds to its own links (?shpxid=…, utm_…, fbclid) is not part of the page's address
            _d["address_url"] = re.sub(r"[?&]$", "", re.sub(r"(?<=[?&])(?:shpxid|utm_[a-z]+|fbclid|gclid|srsltid|_gl|mc_[a-z]+|ref)=[^&#]*&?", "", _d["address_url"]))
        # only what the rows use is kept (the title and the address quote have been read above): the table grows with the sites, 1.2 KB a site
        # twice over when every field of the record was kept in both tables
        _d = {k_: _d[k_] for k_ in ("key", "site", "date", "site_name", "address", "address_url", "address_country", "address_how") if _d.get(k_)}
        LFACTS[_d["key"]] = _d
        _fd = registrable(host_of(_d.get("site") or ""))
        if _fd and _fd not in LFACTS_DOM:
            LFACTS_DOM[_fd] = _d  # the same record under its site's domain (no copy)
        elif _fd and ((_d.get("site_name") and not LFACTS_DOM[_fd].get("site_name")) or (_d.get("address") and not LFACTS_DOM[_fd].get("address"))):
            LFACTS_DOM[_fd] = dict(LFACTS_DOM[_fd], **_d)
# 2026-11-10 (row audit): the vendor's address of a crawled lead is the quote that ends at its postal code — with the page's words in front
# ("OUR WORK Donate No results found CONNECT BC ALLIANCE FOR ARTS + CULTURE 100-938 Howe Street Vancouver BC V6Z 1N9"), or the labels of the
# page's schema.org block ("streetAddress: …, addressLocality: …"). The address is cut out with the crawler's own rule; the cut is used only
# when it reads as a whole address (a street word in it, none lost in front of it, no clock time). The page it was read on stays in the cell.
_STREET_WORD = re.compile(r"\b(?:street|st|avenue|ave|av|road|rd|boulevard|boul|blvd|rue|chemin|ch|drive|dr|way|lane|court|crt|place|highway|hwy|route|rte|rang|crescent|cres|parkway|pkwy|"
                          r"square|terrace|trail|line|c[ôo]te|mont[ée]e|promenade|circle|gate|row|quai|all[ée]e|impasse|concession|sideroad|po box|p\.o\. box|c\.p\.|case postale)\b\.?", re.I)
_CRAWLED_PF = {"vendor_site_cc", "site_member_cc", "site_credit_cc", "dns_service_cc", "tech_tenant_cc"}
def tidy_vendor_address(va):
    m = re.search(r" \((?:as printed|schema\.org|headquarters)", va or "")
    core, tail = (va[:m.start()], va[m.start():]) if m else (va or "", "")
    if "streetAddress:" in core:
        core = re.sub(r"\b(?:streetAddress|addressLocality|addressRegion|postalCode|addressCountry):\s*", "", core)
        return re.sub(r"\s+,", ",", re.sub(r"\s+", " ", core)).strip(" ,") + tail
    if not _CA_PC0.search(core.upper()):
        return va
    cut = _addr_from(core) or ""
    front = core[:len(core) - len(cut)] if cut and core.endswith(cut) else ""
    if cut and front.strip() and len(cut) >= 15 and _STREET_WORD.search(cut) and not _STREET_WORD.search(front[-40:]) and not re.search(r"\d", front[-8:]) and not re.search(r"\d{1,2}:\d{2}", cut):
        return cut + tail
    return va
_CA_PC0 = re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]\s?\d[ABCEGHJ-NPRSTV-Z]\d\b")
n_lf = collections.Counter()
REG_NAMED = set()  # lead keys whose legal name is the owner of record on a federal register (tools/tm_register.py)
def apply_details(x, k):
    f = LFACTS.get(k) or LFACTS_DOM.get(registrable(host_of(x.get("buyer_website") or "")))
    if f and not LFACTS.get(k) and host_of(f.get("site") or "") != host_of(x.get("buyer_website") or ""):
        f = None; n_lf["facts of another host of the domain not taken"] += 1  # eastridge-emc.churchcenter.com is not lcachurch.churchcenter.com
    if f:
        if f.get("site_name") and (re.fullmatch(r"(?:https?://)?(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}/?", (x.get("buyer") or "").lower()) or x.get("tier") == "R"):
            # the lead only carried the domain (or its address) — or the row is about the site itself (tier R) and its name so far is what a third party
            # wrote next to a link ("Product categories that we currently provide"): the organisation's own home page names it
            x["buyer"] = f["site_name"]; n_lf["buyer_name_from_own_home_page"] += 1
        if f.get("address") and not x.get("buyer_address"):
            x["buyer_address"] = lf_cell(f, x.get("buyer_website") or ""); n_lf["buyer_address_from_own_page"] += 1
    d = LDET.get(k)
    if not d:
        return
    if not d.get("reference") and d.get("platform") in ("dns_service_cc", "site_credit_cc") and x.get("buyer_website"):
        # a hosting / DNS / e-mail service is sold for a domain name, a website is built for one: the domain is the identifier both parties share
        # (no account or order number is published). Same rule as the registry rows, whose reference is the registered name.
        d = dict(d, reference=registrable(host_of(x["buyer_website"])))
    if not d.get("reference") and d.get("platform") == "tech_tenant_cc" and x.get("buyer_website"):
        # 2026-11-11 (owner: every field of an invoice; the store and clinic rows had no reference at all): a platform bills an account, and the
        # account is the store, the clinic or the portal itself. Its address on the vendor's platform (the myshopify.com name the store's own
        # meta.json gives, the portal's host) and its own domain are the identifiers both parties share; no account number is published.
        _own = registrable(host_of(x["buyer_website"]) or "")
        _ms = re.search(r"([a-z0-9][a-z0-9-]*\.myshopify\.com)", d.get("service_seen") or "")
        _ph = host_of(d.get("record_url") or "")
        _acct = _ms.group(1) if _ms else _ph if (_ph and registrable(_ph) != _own) else ""
        d = dict(d, reference=" / ".join(v_ for v_ in (_acct, _own) if v_))
        n_lf["reference: the account's own address on the vendor's platform"] += 1
    if d.get("client_label") and re.fullmatch(r"(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}", (x.get("buyer") or "").lower()):
        # the lead only carried the domain: the name the Canadian vendor wrote next to its link, kept only when it agrees with that domain
        _lab = re.sub(r"\s+", " ", d["client_label"]).strip(" -–—|:·•")
        _lab = re.sub(r"\s+\d{1,6}[A-Za-z]?,?\s+(?:[A-Za-zÀ-ÿ0-9.'’-]+\s+){0,2}(?:Chem\.?|Chemin|Rue|Boul\.?|Boulevard|Av\.?|Avenue|Ave\.?|Route|Rte\.?|Rang|Mont[ée]e|Street|St\.?|Road|Rd\.?|Drive|Dr\.?|Blvd\.?|Highway|Hwy\.?|"
                      r"Way|Lane|Ln\.?|Court|Ct\.?|Crescent|Cres\.?|Place|Pl\.?|C[ôo]te|Principale|Main)(?![A-Za-zÀ-ÿ]).*$", "", _lab).strip(" -–—|:·•,")  # a dealer list prints "Name 1015 Chem. de …": the name only
        _flat = unicodedata.normalize("NFKD", _lab).encode("ascii", "ignore").decode().lower()
        _n, _dl = re.sub(r"[^a-z0-9]", "", _flat), re.sub(r"[^a-z0-9]", "", registrable(host_of(x.get("buyer_website") or x.get("buyer") or "")).split(".")[0])
        _tk = [t for t in re.findall(r"[a-z0-9]{4,}", _flat) if t not in ("home", "accueil", "welcome", "bienvenue", "website", "site", "official", "page", "visit", "www", "http", "https")]
        if 3 <= len(_lab) <= 80 and not re.search(r"https?:|www\.|\.(?:ca|com|org|net)\b|@", _lab, re.I) and _dl and ((len(_dl) >= 4 and _dl in _n) or (len(_n) >= 4 and _n in _dl) or any(t in _dl for t in _tk)):
            x["buyer"] = _lab; n_lf["buyer_name_from_vendor_link_label"] += 1
    if d.get("member_address_quote") and not x.get("buyer_address"):
        # a member page of a chamber / association directory prints the member's own address (a third party's page: labelled as such)
        _m = re.search(r"(?<![\w-])\d{1,6}[A-Za-z]?,?\s+(?:[a-zà-ÿ]+\.?\s+){0,2}[A-ZÀ-Ý0-9]", d["member_address_quote"])
        x["buyer_address"] = "%s (as printed in %s %s, %s)" % ((d["member_address_quote"][_m.start():] if _m else d["member_address_quote"]).strip()[:160], d.get("register_label") or "the member directory of", d.get("vendor") or "the body", d.get("record_url") or "")
        n_lf["buyer_address_from_member_directory"] += 1
    br = d.get("buyer_register")
    if isinstance(br, dict):
        # a public register kept by the body that is paid (2026-11-10: the Régie du bâtiment du Québec's list of active licences) states the payer's legal identity
        _src = " (%s)" % br.get("label", "the body's public register")
        if br.get("legal_name"):
            x["buyer_legal_name_as_published"] = br["legal_name"] + _src; n_lf["buyer_legal_name_from_register"] += 1
            if d.get("platform") in ("tm_register", "pt_register", "authority_register", "exchange_register"):
                # the owner of record on the federal trademarks register IS the legal person (and the site was tied to it by that very name):
                # a name read off the site later does not replace it. The same for a registrant of a regulatory authority: the row is the
                # registrant's relationship, and a site shared with sister companies ("LH (Wasaga) Ltd." on Lancaster Homes' site) states another name
                REG_NAMED.add(k)
        if br.get("trade_names") and not x.get("buyer_trade_name_as_published"):
            x["buyer_trade_name_as_published"] = "; ".join(br["trade_names"]) + _src
        if br.get("registry_id") and not x.get("buyer_registry_id"):
            x["buyer_registry_id"] = br["registry_id"] + _src
        if br.get("legal_form") and not x.get("buyer_legal_form"):
            x["buyer_legal_form"] = br["legal_form"] + _src
        if br.get("phone") and not x.get("buyer_phone"):
            x["buyer_phone"] = br["phone"] + _src
    if d.get("vendor_address") and d.get("platform") in _CRAWLED_PF:
        _tv = tidy_vendor_address(d["vendor_address"])
        if _tv != d["vendor_address"]:
            d = dict(d, vendor_address=_tv); n_lf["vendor_address_cut_out_of_its_quote"] += 1
    if str(d.get("value_field") or "").lower() == "amount" and re.search(r"data\.wa\.gov/resource/(?:9ncw-tqjn|t9je-9qwa)", json.dumps(d, ensure_ascii=False)[:3000] + " " + (x.get("contract_link") or "")):
        # 2026-11-13: Washington L&I's "amount" is the PRIME contract's estimated amount ("Estimated Contract Amount" — Sound Transit's $228 million
        # light-rail contract on the affidavit of Pro-Bel, whose own "contractamount" was $82,557.60); the filer's own amount is another field, which
        # tools/lead_scanner.py now prefers. The prime's amount is never this vendor's value.
        d = dict(d, value="", value_field=""); n_lf["Washington L&I: the prime contract's amount not taken for the filer's value"] += 1
    for col, key in (("contract_value", "value"), ("currency", "currency"), ("contract_reference", "reference"), ("start_date", "start"),
                     ("end_date", "end"), ("vendor_address", "vendor_address"), ("contract_title", "title")):
        if not x.get(col) and d.get(key):
            # value_basis: the amount is the payee's published tariff for this kind of licence, not a payment record (said in the cell)
            x[col] = d[key] if col != "contract_value" or not (d.get("value_field") or d.get("value_basis")) else \
                ("%s (%s)" % (d[key], d["value_basis"])) if d.get("value_basis") else "%s (source field: %s)" % (d[key], d["value_field"])
    if d.get("reference") and not x.get("all_identifiers"):
        try:
            _ids = json.loads(d["reference"]) if str(d["reference"]).startswith("{") else {"reference": d["reference"]}
        except Exception:
            _ids = {"reference": str(d["reference"])}
        x.update(classify_ids(_ids if isinstance(_ids, dict) else {"reference": str(_ids)}, d.get("platform") or "", x.get("instrument_type") or ""))
    if x.get("contract_value") and not x.get("currency"):
        pf = d.get("platform") or ""
        x["currency"] = "USD (derived from the source's government)" if re.search(r"usa|socrata|ckan_us|tx1295|ferc|990|sec|cms", pf) else \
                        "CAD (derived from the source's government)" if re.search(r"bc_sofi|fir|fnfta|ckan|cz_|advd", pf) else ""
seen = {norm(x["buyer"]) for x in rows}
seen_dom = {registrable((urllib.parse.urlparse(x["buyer_website"]).hostname or "").lower().removeprefix("www.")) for x in rows if x.get("buyer_website")}
seen_dom.discard("")
import urllib.parse
REL_PATH = re.compile(r"client|customer|case-stud|casestud|case_stud|temoignage|t%C3%A9moignage|testimonial|success-stor|"
                      r"portfolio|our-work|realisations?\b|r%C3%A9alisations?|nos-realisations|clientele", re.I)  # re.I: the path is lower-cased below, so the %C3%A9 forms never matched before 2026-11-10
_STORY_REL = re.compile(r"client|customer|case-?stud|case_stud|temoignage|t%c3%a9moignage|testimonial|success|etudes?-de-cas|cas-clients?|histoires?-de-succes|reussites?|r%c3%a9ussites?|references?/|projets?/|projects?/|portfolio|realisations?", re.I)
NOT_REL_PATH = re.compile(r"terms|reference|support|service|product|letter|lettre|news|nouvelle|blog|article|press|media|document|conditions|bill|/loi|career|emploi|job|event|evenement|contact|about|a-propos|partner|partenaire")
# 2026-11-10 (owner: "a Canadian entity gets paid … establish that relationship"): pages where a Canada-located organisation lists the parties
# that PAY it — sponsors / exhibitors of an organiser, dealers / retailers / distributors of a supplier (same tests as tools/cc_clients.py)
SPONSOR_PATH = re.compile(r"/[^/]*(sponsors|commanditaires|exhibitors?|exposants|advertisers|annonceurs)([-_.][^/]*)?/?$")
TENANT_PATH = re.compile(r"/[^/]*(our-tenants|tenant-directory|tenant-list|nos-locataires|liste-des-locataires|repertoire-des-locataires|merchants|marchands|commer(c|%c3%a7)ants|store-directory|shop-directory"
                         r"|repertoire-des-(magasins|boutiques|commerces|marchands))([-_.][^/]*)?/?$")
DEALER_PATH = re.compile(r"/[^/]*(dealers?|where-to-buy|ou-acheter|o%c3%b9-acheter|retailers|stockists|d(e|%c3%a9)taillants|revendeurs|points-de-vente)([-_.][^/]*)?/?$")  # not "distributors": wrong direction on a distributor's own site
NOT_PAYER_PATH = re.compile(r"become|devenir|devenez|opportunit|package|forfait|prospectus|application|apply|form|kit|levels|niveaux|sponsorship|commandite|login|log-in|signin|sign-in|account|compte|portal|portail|supplier|fournisseur|brand|marque|manufactur|fabricant|career|emploi|job"
                            r"|blog|news|nouvelle|article|actualit|press|communiqu|regist|casino|blackjack|poker|betting|roulette|slots|/[^/]{37,}/?$")  # the last alternative: an article slug, not a list page
# member directories of a Canada-located body (same tests as tools/cc_clients.py): a one-member page of a GrowthZone / ChamberMaster directory, or a member-list page
MEMBER_ONE_PATH = re.compile(r"^/list/member/[^/]+/?$")
_OURWORK_TOP = re.compile(r"^/(?:(?:en|fr|en-ca|fr-ca)/)?[^/]*our-work")
def rel_path(p):
    """REL_PATH with "our-work" only as the first path part (2026-11-10 row audit: /advocacy/our-work/policy-areas/… is an organisation's programme page; its links are partners)"""
    q = p if _OURWORK_TOP.match(p) else p.replace("our-work", "our-w0rk")
    return any(len(seg) <= 30 and REL_PATH.search(seg) for seg in q.split("/"))  # the word in a short path part; a long slug that merely contains it is an article
INVESTOR = re.compile(r"ventures?\b|venture capital|capital\b|invest|private equity|\bequity\b|\bfunds?\b|\bfonds\b|holdings?\b|incubat|accelerat|\bangels?\b|placements", re.I)
MEMBER_PATH = re.compile(r"/[^/]*(members|membres|member-directory|membership-directory|member-list|directory-of-members|repertoire-des-membres|liste-des-membres)([-_.][^/]*)?/?$")
NOT_MEMBER_PATH = re.compile(r"board|council|committee|comit|conseil|team|equipe|%c3%a9quipe|staff|personnel|faculty|executive|ex%c3%a9cutif|directors|administrat|family|famil|only|area|zone|login|log-in|signin|sign-in"
                             r"|account|compte|portal|portail|become|devenir|devenez|join|adh%c3%a9|adhesion|benefit|avantage|application|apply|form|renew|register|inscription|fees|dues|cotisation|tarif|news|nouvelle"
                             r"|blog|event|evenement|honorary|honoraire|founding|fondateur|past|ancien|crew|band|cast|choir|chorale|caucus|mla|mpp|legislat|parliament|parlement|senat|assembl|elected|elus|%c3%a9lus"
                             r"|student|etudiant|%c3%a9tudiant|alumni|lab|research|recherche|group|groupe|profile|profil|user|forum")
# the text starts with "client listing": contrib/claude/rank_buyers/batches.py files the row with the client listings (P06-P08) by that prefix
PAYER_TEXT = {"sponsor": "client listing on the vendor's own site (undated): sponsor / exhibitor named by the Canada-located organiser — the listed party pays the organiser",
              "dealer": "client listing on the vendor's own site (undated): dealer / retailer named by the Canada-located supplier — the listed party buys from the supplier",
              "tenant": "client listing on the vendor's own site (undated): tenant / merchant named by the Canada-located landlord, market or business association — the listed party pays it rent, fees or a levy",
              "member": "client listing on the vendor's own site (undated): member named in the member directory of the Canada-located body (chamber of commerce, board of trade, association) — members pay it dues"}
# a lead whose own key has no mailbox yet borrows the confirmed mailbox found for the same organisation under another key
# (same registrable website domain, held by ONE organisation only: shared government domains never lend)
mail_dom = collections.defaultdict(dict)
for mk, (ms, mr) in mail.items():
    md = registrable((mr["mailbox"].split("@")[-1] or "").lower())
    if md:
        mail_dom[md][mk] = (ms, mr)
GEN_W = {"city", "town", "county", "district", "university", "college", "municipality", "corporation", "township", "village", "school",
         "board", "society", "association", "national", "foundation", "company", "group", "services", "international", "canada"}
def name_fits(a, b):
    """two names of one body: a bare domain on either side, or a shared distinctive word"""
    if not a or not b or ("." in a and " " not in a.strip()) or ("." in b and " " not in b.strip()):
        return True
    ta = {w for w in re.findall(r"[a-z]{4,}", norm(a)) if w not in GEN_W}
    tb = {w for w in re.findall(r"[a-z]{4,}", norm(b)) if w not in GEN_W}
    return bool(ta & tb) or not ta or not tb
def borrow(L):
    """the confirmed mailbox of the organisation that owns the lead's website domain: one organisation (possibly under
    several keys whose names fit each other), never a domain shared by several bodies"""
    d = registrable(host_of(L.get("website") or ""))
    owners = list((mail_dom.get(d) or {}).values())
    if not owners:
        return None
    names = [norm(mr.get("org_name") or "") for ms, mr in owners]
    same_box = len({mr["mailbox"].lower() for ms, mr in owners}) == 1
    if not same_box and not all(a and b and (a in b or b in a) for a in names for b in names):
        return None  # several bodies share this domain (a county and its library, a government and its ministries)
    ms, mr = max(owners, key=lambda x: x[0])
    return (ms, mr) if name_fits(L.get("buyer_name") or "", mr.get("org_name") or "") else None  # e.g. a person named in a customer story is not the university
borrowed = 0
# 4a. tier R (2026-11-10, owner 2026-11-09 23:41 EST: "some Canadian entity receives money for a service they provided, and that relationship is
# established online"): the holder of a .ca domain name has an agreement in force with the Canadian Internet Registration Authority and pays
# for the registration through a CIRA-certified registrar, which CIRA's rules require to be a Canadian person or corporation. A recorded,
# current relationship for every organisation whose own .ca site publishes its mailbox — until now most of them were delivered with an
# INFERRED relationship only (P13). The domain is proven live by the referee itself: it re-fetched the mailbox page on that domain.
# Weakest lead class: any other relationship of the organisation claims the row first (lead_strength 6).
REG_AGREEMENT = "https://stg-saas.cira.ca/uploads/2023/06/Registrant-Agreement-Version-2.2_0.pdf"
REG_REGISTRARS = "https://stg.cira.ca/uploads/2023/05/cprregistrar_-_en.pdf"
CF_REG = ("registry contract (.ca domain name registration)=cira.ca; CIRA's Registrant Agreement, version 2.2 (%s, read 2026-11-10): “This agreement (the \"Agreement\") is between you "
          "(the \"Registrant\") and the Canadian Internet Registration Authority (\"CIRA\")” … “\"Fees\" means the fees payable to CIRA in connection with this Agreement, including an "
          "application for a Domain Name and/or any renewal” … notice address “CIRA, 979 Bank Street, Suite 400, Ottawa, Ontario K1S 5K5”. Registrar of record: CIRA's Canadian "
          "Presence Requirements For Registrars, version 1.1 (%s): “Only the following persons will be permitted to be certified and to act as a Registrar … A corporation: (i) under "
          "the laws of Canada or any province or territory of Canada; and (ii) which has a place of business in Canada”" % (REG_AGREEMENT, REG_REGISTRARS))
n_reg = 0
try:
    import hashlib as _hl
    from ap_crawler import GENERIC_MAIL as _GEN_MAIL
    for _md, _owners in list(mail_dom.items()):
        if not _md.endswith(".ca") or _md.count(".") > 2 or _GEN_MAIL.search(_md) or _GEN_MAIL.search("x." + _md) or re.search(r"(^|\.)(gc|canada|gouv\.qc|gov\.[a-z]{2})\.ca$", _md):
            continue  # shared mail hosts, and names under a government's own domain (a department is not the registrant of gc.ca)
        _own = [(ms, mr) for ms, mr in _owners.values() if registrable(host_of(mr.get("evidence_url") or "")) == _md]  # the mailbox is printed on a page of that very domain
        if not _own:
            continue
        _ms, _mr = max(_own, key=lambda x: x[0])
        _k = "lead:" + _hl.sha1(("%s|reg:ca" % _md).encode()).hexdigest()[:16]
        if _k in leads:
            continue
        _nm = (_mr.get("org_name") or "").strip()
        if not _nm or re.match(r"(?i)^(https?://|www\.)", _nm):
            _nm = _md  # a row whose "name" is the site's address: the domain, until the site's own name is read
        leads[_k] = {"buyer_key": _k, "buyer_name": _nm, "website": "https://%s/" % _md, "canadian_vendor_rows": "1",
                     "example_vendor": "Canadian Internet Registration Authority (CIRA)", "canada_field_value": CF_REG,
                     "evidence_dataset": "https://dns.google/resolve?name=%s&type=NS" % _md, "latest_record_date": today}
        LDET.setdefault(_k, {"key": _k, "platform": "ca_registry", "title": ".ca domain name registration: %s" % _md, "reference": _md,
                             "vendor_address": "979 Bank Street, Suite 400, Ottawa, Ontario K1S 5K5 (CIRA's notice address in its Registrant Agreement, version 2.2: %s)" % REG_AGREEMENT})
        n_reg += 1
except Exception as _e:
    print("registry leads skipped: %s" % _e)
print("registry leads (.ca domains carrying a confirmed mailbox of their own organisation): %d" % n_reg)
# 4a-bis (2026-11-11). A domain name whose home page answers at the home page of ANOTHER domain is a second name of the organisation that
# runs that site (osfs.ca -> flyos.ca, feuer.ca -> valenciarisk.com): 1 in 7 of the .ca sites that had given no mailbox. The mailbox reader
# now follows such a name (tools/lead_crawl.py moved_site_ok: home page to home page, never a platform, a network, a parking service or a
# provider's own domain) and reads the site that answers; its facts record names both. Here the lead is told where its organisation's
# site is — the row's website, mailbox and name are those of the site that answers; the relationship stays the one of the name on file:
#   - a lead of any lane (a DNS service, a credit, a listing) keeps its record and takes the site that answers as its website;
#   - a .ca name with no lead of its own gets the registry lead (tier R) when the site that answers is not itself a .ca site (that one
#     gets its own registry lead above): the organisation holds a .ca registration, its site lives elsewhere.
# One row per organisation: the lead is keyed by the site that answers like every other lead (seen_dom). A site that more than 30
# different names answer at is a hub (a broker, a franchise network, a domain dealer): nobody's second name is read from it.
n_moved = collections.Counter()
try:
    _hub = collections.Counter(registrable(host_of(_v[1])) for _v in MOVED.values())
    for _k, (_asked, _site, _murl, _mdate) in sorted(MOVED.items()):
        _a, _b, _bh = registrable(host_of(_asked)), registrable(host_of(_site)), host_of(_site)
        if not _a or not _b or _a == _b:
            continue
        if _hub[_b] > 30:
            n_moved["the site answers for more than 30 names (a hub): left out"] += 1
            continue
        _m = mail.get(_k)
        if not _m or registrable(host_of(_m[1].get("evidence_url") or "")) != _b:
            n_moved["no confirmed mailbox on the site that answers (yet)"] += 1
            continue
        if _k in leads:
            if registrable(host_of(leads[_k].get("website") or "")) == _a:
                leads[_k] = dict(leads[_k], website="https://%s/" % _bh, _alias=(_a, _b, _mdate))
                n_moved["lead of another lane: its site is the one that answers"] += 1
            continue
        if not _a.endswith(".ca") or _a.count(".") > 2 or re.search(r"(^|\.)(gc|canada|gouv\.qc|gov\.[a-z]{2})\.ca$", _a):
            continue
        if _b.endswith(".ca"):
            n_moved[".ca name answering at another .ca site (that site has its own registry lead)"] += 1
            continue
        _nm = (_m[1].get("org_name") or "").strip()
        if not _nm or re.match(r"(?i)^(https?://|www\.)", _nm) or registrable(_nm.lower()) == _a:
            _nm = _b  # the name so far is the domain that was asked: the site that answers, until its own name is read
        leads[_k] = {"buyer_key": _k, "buyer_name": _nm, "website": "https://%s/" % _bh, "canadian_vendor_rows": "1",
                     "example_vendor": "Canadian Internet Registration Authority (CIRA)", "canada_field_value": CF_REG,
                     "evidence_dataset": "https://dns.google/resolve?name=%s&type=NS" % _a, "latest_record_date": today, "_alias": (_a, _b, _mdate)}
        LDET.setdefault(_k, {"key": _k, "platform": "ca_registry", "title": ".ca domain name registration: %s (answers at %s)" % (_a, _b), "reference": _a,
                             "vendor_address": "979 Bank Street, Suite 400, Ottawa, Ontario K1S 5K5 (CIRA's notice address in its Registrant Agreement, version 2.2: %s)" % REG_AGREEMENT})
        n_moved["registry lead for a .ca name whose site lives under another ending"] += 1
except Exception as _e:
    print("second names skipped: %s" % _e)
print("organisations' second domain names (the name on file answers at their site under another domain):", len(MOVED), dict(n_moved))
# ---- ranking in parts (2026-11-10) -------------------------------------------------------------------------------------------------------
# RANK_PART="i/N": this process ranks part i of N. Measured: 1.9 GB fixed + ~12 KB a row — a million rows do not fit one 16 GB runner. The
# rows that grow are the leads' and the inferred rows of organisations with a mailbox; the contract rows and P12 are small and stay whole in
# part 0. What the ranker joins must be in one part:
#   - leads of one website domain (one row per site: seen_dom, the upgrades by domain, a borrowed mailbox, the second-mailbox fold);
#   - organisations that hold the same mailbox (one row per mailbox), and an organisation with the site its mailbox was read on: the mailbox's
#     domain joins them (a freemail / access-provider domain joins nobody: there only the same box does);
#   - whoever shares a domain or a mailbox with a row that exists before the leads, or with a buyer of the contract dataset: part 0.
# A group of joined organisations is named by its smallest member and placed by the hash of that name, so it keeps its part from build to
# build. Parts > 0 build the contract rows as every run does (the leads are judged against them) and write only their own rows.
# tools/rank_merge.py puts the parts together. Measured on 76,706 rows in two parts: the same rows but one, the same cells but a provider
# name in 13 carry-over notes. Without RANK_PART nothing here runs.
_PART = (os.environ.get("RANK_PART") or "").strip()
_PI, _PN = (int(_PART.split("/")[0]), int(_PART.split("/")[1])) if _PART else (0, 1)
_part_of, _XLEAD = {}, None
def _lead_label(_l):
    return "%s — %s%s" % (re.sub(r"=.*$", "", _l.get("canada_field_value") or "lead") if "stories" not in (_l.get("canada_field_value") or "") else "customer story published by the vendor",
                          _l.get("example_vendor") or "", (" (%s)" % _l["latest_record_date"][:10]) if _l.get("latest_record_date") else "")
def _lead_tables(_leads):
    """the lead relationships by website domain and by exact name, for the back-reference "also seen in the lead files" """
    _ld, _ln = collections.defaultdict(list), collections.defaultdict(list)
    for _k, _l in _leads.items():
        _d = registrable(host_of(_l.get("website") or "")) if _l.get("website") else ""
        _lab = _lead_label(_l)
        if _d and not SHARED_GOV.match(_d):
            _ld[_d].append(_lab)
        _ln[norm(_l.get("buyer_name") or "")].append(_lab)
    return _ld, _ln
if _PN > 1:
    import hashlib as _hp
    _XLEAD = _lead_tables(leads)  # the back-reference reads every lead, whatever its part
    for x in rows:
        x["_pre"] = "1"  # a row that exists before the leads: written by part 0 only
    def _pdom(u):
        return registrable(host_of(u)) if u else ""
    def _box_node(mr):
        e = (mr.get("mailbox") or "").strip().lower()
        d = registrable(e.split("@")[-1]) if "@" in e else ""
        return ("box:" + e) if (d and FREEMAIL.match(d)) else d
    _up = {}
    def _find(a):
        r = a
        while _up.setdefault(r, r) != r:
            r = _up[r]
        while _up[a] != r:
            _up[a], a = r, _up[a]
        return r
    def _union(a, b):
        ra, rb = _find(a), _find(b)
        if ra != rb:
            _up[max(ra, rb)] = min(ra, rb)  # the smallest name stands for the group
    _core = set()
    for x in rows:
        _core.add(_pdom(x.get("buyer_website") or ""))
        if x.get("email"):
            _core.add(_box_node({"mailbox": x["email"]}))
    _node = {}
    for _mk, (_ms, _mr) in mail.items():  # every organisation with a mailbox: a lead, or a candidate of the inferred rows
        _site = (VEN.get(_mk) or {}).get("website") or (BUY.get(_mk) or {}).get("official_website") or (leads[_mk].get("website") if _mk in leads else "") or ""
        _bn = _box_node(_mr)
        # its site; an organisation without a known site stands under its mailbox's domain — or, with a freemail box, under the host of the page
        # the box was read on (the inferred rows keep one row per such host)
        _sd = _pdom(_site) if _site else (registrable(host_of(_mr.get("evidence_url") or "")) if _bn.startswith("box:") else "")
        _ns = [d for d in (_sd, _bn) if d] or ["key:" + _mk]
        for _d in _ns[1:]:
            _union(_ns[0], _d)
        _find(_ns[0])
        _node[_mk] = _ns[0]
        if _mk in BUY:  # a buyer of the contract dataset: P12 and the contract rows are ranked in part 0
            _core.update(_ns)
    for _k, _L in leads.items():
        _d0 = _pdom(_L.get("website") or "")
        if _k not in _node:
            _node[_k] = _d0 or ("key:" + _k)
            _find(_node[_k])
        elif _d0:
            _union(_node[_k], _d0)
        for _ok, (_os, _or) in (mail_dom.get(_d0) or {}).items() if _d0 else ():
            _union(_node[_k], _node.get(_ok) or _box_node(_or))  # a lead may borrow the mailbox of the organisation that owns its site's domain
    # the same site name under two endings (ventilationgr.ca / ventilationgr.com, thingsengraved.ca / .com) is one organisation more often than
    # not, and the ranker delivers one inferred row per organisation name: such domains stay together (measured: 15 of the 30 rows that two
    # parts delivered beyond a single run were this case)
    for _d in [d for d in list(_up) if "." in d and not d.startswith(("box:", "key:", "sld:"))]:
        _lab = _d.split(".")[0]
        if len(_lab) >= 6:
            _union(_d, "sld:" + _lab)
    _core.discard("")
    _core_roots = {_find(d) for d in _core if d in _up}
    _n_core = 0
    for _k, _n in _node.items():
        _r = _find(_n)
        if _r in _core_roots:
            _part_of[_k] = 0; _n_core += 1
        else:
            _part_of[_k] = int(_hp.sha1(_r.encode()).hexdigest()[:8], 16) % _PN
    _sizes, _nl = collections.Counter(_part_of[k] for k in leads), len(leads)
    leads = {k: v for k, v in leads.items() if _part_of[k] == _PI}
    print("RANK_PART %d/%d: %d of %d leads in this part (leads per part: %s); organisations placed: %d, of which %d stand with a row that exists before the leads or a buyer of the contract dataset (part 0)" % (
        _PI, _PN, len(leads), _nl, dict(sorted(_sizes.items())), len(_part_of), _n_core))
    _free(globals(), "_up", "_node", "_core", "_core_roots")
    # What belongs to the other parts' organisations is not read again by this process: the ranker only joins what the partition keeps
    # together. Measured before this (two parts of 76,913 rows): a part peaked at 2.42 GB against 2.49 GB for one process — every table was
    # still whole. The tables read later (DNS posture, the lanes' row details) are cut to this part's mailboxes where they are loaded.
    _memstat("at the partition", rows, globals())
    _others = {k for k, p in _part_of.items() if p != _PI}
    _n0 = (len(mail), len(LDET), len(LFACTS))
    for _k in _others:
        mail.pop(_k, None); LDET.d.pop(_k, None); LFACTS.pop(_k, None)
    for _d in list(mail_dom):
        _o = mail_dom[_d]
        for _k in [k for k in _o if k in _others]:
            del _o[_k]
        if not _o:
            del mail_dom[_d]
    for _d in [d for d, f in LFACTS_DOM.items() if f.get("key") in _others]:
        del LFACTS_DOM[_d]
    _PART_BOXES = {(m.get("mailbox") or "").strip().lower() for _s, m in mail.values()}  # every mailbox an organisation of this part may end up with
    print("RANK_PART %d/%d: tables cut to this part — mailboxes %d -> %d, lead details %d -> %d, site facts %d -> %d" % (_PI, _PN, _n0[0], len(mail), _n0[1], len(LDET), _n0[2], len(LFACTS)))
    del _others
    _memstat("after the cut", rows, globals())
_SN = int(os.environ.get("RANK_SAMPLE") or 0)  # debug only: a fixed 1-in-N sample of the leads and of the inferred rows, to compare two versions of this script on a small machine
if not _SN and not (_PN > 1):  # the whole table only (a sample or a part would write a partial list)
    os.makedirs(ROOT + "/out/ranked", exist_ok=True)  # tools/ranked_publish.py copies it to coord/results/ranked/ (the mailbox reader's lead list)
    with open(ROOT + "/out/ranked/contract_buyers_without_mailbox.csv", "w", encoding="utf-8", newline="") as _fc:
        _wc = csv.writer(_fc)
        _wc.writerow(["buyer_key", "buyer_name", "website", "canadian_vendor_rows", "example_vendor", "canada_field_value", "evidence_dataset", "latest_record_date"])
        for _k, _n, _w, _c in sorted(CB_NOMAIL, key=lambda t: -t[3]):
            _wc.writerow([_k, _n, _w, _c, "", "buyer under a current contract with a Canada-located vendor (contract dataset)", "", ""])
if not _SN and not (_PN > 1):
    with open(ROOT + "/out/ranked/contract_buyers_without_website.csv", "w", encoding="utf-8", newline="") as _fc:
        _wc = csv.writer(_fc)
        _wc.writerow(["buyer_key", "buyer_name", "postal_code", "region", "country", "address"])
        for _k, _n, _a in CB_NOSITE:
            if isinstance(_a, dict):
                _pc, _rg, _cc = _a.get("postal_code") or "", _a.get("region") or "", _a.get("country") or ""
                _txt = ", ".join(str(v_) for v_ in (_a.get("line1"), _a.get("city"), _rg, _pc, _cc) if v_)
            else:
                _txt = str(_a or ""); _m = re.search(r"\b([A-Z]\d[A-Z])\s?(\d[A-Z]\d)\b", _txt.upper())
                _pc, _rg, _cc = (_m.group(1) + _m.group(2)) if _m else "", "", "CA" if _m else ""
            _wc.writerow([_k, _n, _pc, _rg, _cc, _txt[:200]])
print("buyers under a current contract with no confirmed mailbox of their own, whose own site goes to the mailbox reader:", len(CB_NOMAIL),
      "| with no website on file (written for the places lookup):", len(CB_NOSITE), "| websites from the places lookup:", dict(n_cbsite))
def _in_sample(k):
    import hashlib as _hs
    return not _SN or int(_hs.sha1((k or "").encode()).hexdigest()[:8], 16) % _SN == 0
if _SN:
    leads = {k: v for k, v in leads.items() if _in_sample(k)}
    print("RANK_SAMPLE: 1 lead in %d kept: %d" % (_SN, len(leads)))
# Owner, 2026-11-11 13:09 and 13:58 EST: "it needs to be bank transfers relationship not credit card … Shopify is over saturated in this way … if
# it's not on invoice, by bank transfer then it's no"; asked what to do with the rows billed to a card on file or through a registrar: "Remove
# them". A lead whose vendor charges a card on file — Shopify by its own terms, any other vendor whose published way of being paid names cards
# and no bank payment — makes no row and does not claim its organisation's site: another relationship of that organisation can. A vendor that
# takes a bank payment as well as a card stays (owner, 14:20 EST: an invoice that can be paid by bank transfer is in).
CARD_ROWS = os.environ.get("RANK_CARD_ROWS") == "1"      # 1 = the table as it was before the rule (for a comparison build)
REGISTRY_ROWS = os.environ.get("RANK_REGISTRY_ROWS") == "1"
def _lead_card_only(k, L):
    cfv = L.get("canada_field_value") or ""
    if CARD_ROWS or "(tech)" not in cfv:
        return False
    if (L.get("example_vendor") or "").startswith("Shopify"):
        return True
    d_ = LDET.get(k) or {}
    vd_ = registrable(host_of(d_.get("vendor_site") or "") or "")
    cur_ = _BILL_CUR.get(norm(L.get("example_vendor") or "")) or _BILL_CUR_DOM.get(vd_)
    txt = str(((cur_ or {}).get("bill") or {}).get("payment") or "")
    if not txt and vd_ in VBILL:
        txt = str((_VB.extra_of(VBILL.get(vd_), "paymethod") or {}).get("q") or "")
    return bool(txt) and bool(_RR._CARD.search(txt)) and not _RR._bank_ok(txt)
def lead_strength(kl):
    """dated records first, then services seen on the buyer's site, 12-36 month records, client listings, other links:
    the strongest relationship of an organisation claims its website domain (one row per organisation)"""
    cfv, ld = kl[1].get("canada_field_value") or "", (kl[1].get("latest_record_date") or "")[:10]
    if cfv.startswith("registry contract"):
        return 6
    if "vendor located in Canada" in cfv:
        return 4 if re.search(r"\((wall|stories)\)", cfv) else 5
    if "(tech)" in cfv:
        # owner's bar of 2026-11-11 ("billed for something monthly … systematically by the vendor"): of the services an organisation is seen to use,
        # the one whose vendor says it bills by the month claims the row; then a platform or DNS service priced by the month; a design credit last
        d_ = LDET.get(kl[0]) or {}
        vd_ = registrable(host_of(d_.get("vendor_site") or "") or "")
        cur_ = _BILL_CUR.get(norm(kl[1].get("example_vendor") or "")) or _BILL_CUR_DOM.get(vd_)
        if "credited on the buyer's own site" in cfv and not cur_ and not (d_.get("credit_class") == "P" or re.search(r"host|h[ée]berg|maint|powered|propuls|g[ée]r[ée]|managed", d_.get("credit_phrase") or "", re.I)):
            return 1.9
        c_ = {"monthly": "monthly", "monthly_or_yearly": "monthly_price", "yearly": "yearly"}.get(cur_["cls"], "") if cur_ else (_VB.cycle_of(VBILL.get(vd_))[0] if vd_ in VBILL else "")
        return 1 + {"monthly": 0.0, "quarterly": 0.1, "monthly_price": 0.2, "per_transaction": 0.4, "yearly": 0.5}.get(c_, 0.7)
    if "membership / statutory fee relationship" in cfv:
        return 3.5
    return 0 if CUTOFF <= ld <= today else 2 if CUTOFF3 <= ld else 3
UNNAMED_VENDOR = re.compile(r"redact|withheld|\bPII\b|confidential|not disclosed|undisclosed|anonymi", re.I)
def tech_status(k, L):
    """the service seen on the buyer's own site. 2026-11-10 (tools/credit_scan.py): a credit line on the buyer's own home page ("Website by …",
    "Site web réalisé par …", "Hébergé par …") that links to a vendor whose own site prints its Canadian postal address"""
    d = (L.get("latest_record_date") or "")[:10]
    if "credited on the buyer's own site" in (L.get("canada_field_value") or ""):
        q = re.sub(r"\s+", " ", (LDET.get(k) or {}).get("credit_quote") or "").strip()
        return "active service seen on the buyer's own site (%s): the site credits the Canada-located vendor %s%s" % (d, L["example_vendor"], (" — “%s”" % q[-140:]) if q else "")
    if "seen in the buyer's public DNS" in (L.get("canada_field_value") or ""):
        # 2026-11-10 (tools/dns_services.py): the buyer's own DNS records name the provider that receives its mail (MX), serves its zone (NS)
        # or is authorised to send its mail (SPF); the provider's own site prints its Canadian postal address
        det = LDET.get(k) or {}
        how = {"mx": "its mail is received by %s (MX record)", "ns": "its DNS zone is served by %s (NS record)", "spf": "its SPF record authorises %s to send its mail",
               "cname": "its website address (www) is an alias of %s (CNAME record)",
               "txt": "its DNS carries the vendor's domain-verification record %s (a business account)"}.get(det.get("dns_record_kind") or "", "its DNS records name %s")
        return "active service seen in the buyer's public DNS records (%s): %s — Canada-located provider %s" % (d, how % (det.get("dns_provider_host") or L["example_vendor"]), L["example_vendor"])
    return "active service seen on the buyer's own site (%s): Canada-HQ vendor %s" % (d, L["example_vendor"])
# 2026-11-10 (row audit of 45 random client-page leads of the cloud row factory: about half were not clients — a "Send a File" link on a
# testimonials page, a cookie notice on a portfolio page, a blog post whose address contains "case-study", a funder's logo on "our work").
# A link on a client-type page of a Canada-located vendor is a CLIENT LISTING only when
#   (a) the page is a list or an item page, not an article: no date in its address, the path part that carries the client word has at most three
#       words (a longer slug only when the link's own label names the linked site), no "become a client / client resources / login" words;
#   (b) the link names the organisation it leads to: its label fits the linked site's domain (or is that address), or the page's own last path part
#       does ("/portfolio/acme-plumbing/"), or the label is a plain "visit website" on such a page;
#   (c) an "our work" page counts as a portfolio only as a list page whose labels name the sites, or through (b)'s item address / "visit website"
#       (a charity's "our work / public policy" pages list partners and funders).
# Everything else stays in the file as the weakest package (tier E: a link, not shown to be a client). Applies to the cloud row factory's leads,
# which carry the link's label; the Mac-era leads carry only the page title and are judged by the path as before.
ARTICLE_DATE = re.compile(r"/(?:19|20)\d\d/\d{1,2}(?:/|$)")
NOT_CLIENT_PAGE = re.compile(r"become|devenir|devenez|new-client|nouveaux?-clients?|intake|formulaire|[-/]forms?(?:[-/.]|$)|resource|ressource|login|log-in|signin|sign-in|portal|portail|"
                             r"our-work(?:force|place|shop|out)|workout|workshop|workplace|workforce|client-card|customer-service|service-client|service-a-la-clientele")
WEB_LABEL = re.compile(r"^(?:(?:visit|view|voir|visiter|visitez|launch|see|go to|open|consulter|consultez)\s+(?:the\s+|this\s+|our\s+|their\s+|le\s+|ce\s+)?(?:new\s+|live\s+)?(?:web ?site|site(?: web| internet)?|project|projet)|"
                       r"web ?site|site web|site internet|live (?:site|preview|project))\W*(?:\(.*\))?\W*$", re.I)
URL_LABEL = re.compile(r"^(?:https?://)?(?:www\.)?([a-z0-9-]+(?:\.[a-z0-9-]+)+)(?:/\S*)?$", re.I)
_FILE_EXT = re.compile(r"\.(?:png|jpe?g|gif|svg|webp|pdf|ico|bmp)$", re.I)
def label_names_site(label, dl):
    """does a link's label name the site it leads to? dl = the linked domain's own label, letters and digits only"""
    lab = (label or "").strip()
    if not lab or not dl:
        return False
    m = URL_LABEL.match(lab)
    if m and not _FILE_EXT.search(lab):
        return re.sub(r"[^a-z0-9]", "", registrable(m.group(1).lower()).split(".")[0]) == dl  # an address as the label: it must be the linked site's
    flat = re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", lab).encode("ascii", "ignore").decode().lower())
    if len(dl) >= 4 and dl in flat:
        return True
    if _LCF.name_fit(lab, dl) >= 20:
        return True
    toks = [t for t in re.findall(r"[a-z0-9]{3,}", unicodedata.normalize("NFKD", lab).encode("ascii", "ignore").decode().lower())]
    cover = sum(len(t) if t in dl else 6 if len(t) >= 7 and t[:6] in dl else 0 for t in dict.fromkeys(toks))
    return len(dl) >= 5 and cover >= 0.6 * len(dl)  # "AB Architectural Glazing" -> abglazing, "ZS Metal Fabrication" -> zsmetalfabricating
def client_listing(path, label, bhost, vhost):
    """(True, how) when the link is a client listing by the three tests above, else (False, why not)"""
    dl = re.sub(r"[^a-z0-9]", "", registrable(bhost or "").split(".")[0])
    vl = re.sub(r"[^a-z0-9]", "", registrable(vhost or "").split(".")[0])
    if len(os.path.commonprefix([dl, vl])) >= 10:
        return False, "sister site of the page's owner"
    if ARTICLE_DATE.search(path):
        return False, "dated article"
    if NOT_CLIENT_PAGE.search(path):
        return False, "a page for clients (forms, resources, login), not a list of them"
    q = path if _OURWORK_TOP.match(path) else path.replace("our-work", "our-w0rk")
    segs = [sg for sg in q.split("/") if sg]
    kws = [sg for sg in segs if len(sg) <= 30 and REL_PATH.search(sg)]
    if not kws:
        return False, "no client word in a short path part"
    kw = kws[0]
    n_words = len([w for w in re.split(r"[-_.+%\s]+", re.sub(r"\.(?:html?|php|aspx?)$", "", kw)) if w])
    slug = segs[-1] if segs[-1] != kw else ""
    slug_fit = bool(slug) and label_names_site(urllib.parse.unquote(re.sub(r"\.(?:html?|php|aspx?)$", "", slug)).replace("-", " ").replace("_", " "), dl)
    fit, web = label_names_site(label, dl), bool(WEB_LABEL.match((label or "").strip()))
    if n_words > 3:
        return (True, "label names the site") if fit else (True, "page address names the site") if slug_fit else (False, "article: the client word sits in a slug of %d words" % n_words)
    if "our-work" in kw:
        if slug_fit or web or (fit and not slug):
            return True, "portfolio page"
        return False, "an organisation's 'our work' programme page"
    if fit:
        return True, "label names the site"
    if slug_fit:
        return True, "page address names the site"
    if web:
        return True, "'visit website' on a client page"
    return False, "the link's label does not name the linked site"
def _same_family(a, b):
    wa, wb = re.findall(r"[a-zà-ÿ0-9]+", (a or "").lower()), re.findall(r"[a-zà-ÿ0-9]+", (b or "").lower())
    # a first word that only names a kind of institution proves nothing ("Chambre de commerce de X" and "… de Y" are two chambers, "Bank of …" two banks)
    return (len(wa) >= 3 and len(wb) >= 3 and wa[:2] == wb[:2] and wa != wb and max(len(wa[0]), len(wa[1])) >= 4
            and not re.fullmatch(r"ville|city|town|municipalit[ée]|village|township|county|bank|banque|universit[yé]|coll[eè]ge|church|[ée]glise|[ée]cole|school|h[oô]tel|restaurant|"
                                 r"clini(?:c|que)|centre|center|club|association|chambre|chamber|the|le|la|les", wa[0]))
n_cl = collections.Counter()
if not REGISTRY_ROWS:
    # the holder of a .ca name pays its registrar, by the registrar's own methods (a card for nearly all), and the Canadian registry bills the
    # registrar, not the holder: not "on invoice, by bank transfer". Owner 2026-11-11: "Remove them". The organisations stay on file — their
    # sites, names, addresses and mailboxes are what the register lanes (licences, memberships, agents of record …) are matched against.
    _reg_keys = [_k for _k, _l in leads.items() if (_l.get("canada_field_value") or "").startswith("registry contract")]
    for _k in _reg_keys:
        del leads[_k]
    print("registry leads (.ca registrations) left out by the owner's rule of 2026-11-11 (paid through a registrar, not on invoice by bank transfer): %d" % len(_reg_keys))
REG_DOMS = {registrable(host_of(_l.get("website") or "")) for _l in leads.values() if (_l.get("canada_field_value") or "").startswith("registry contract")} - {""}
for k, L in sorted(leads.items(), key=lead_strength):
    if norm(L["buyer_name"]) in seen or UNNAMED_VENDOR.search(L.get("example_vendor") or "") or not (L.get("example_vendor") or "").strip(): continue  # a relationship needs a named vendor
    if norm(L["buyer_name"]) == norm(L.get("example_vendor") or ""):
        n_cl["the same organisation on both sides (a firm that is its own agent of record): no row"] += 1
        continue
    if _lead_card_only(k, L):
        n_cl["charged to a card on file — Shopify, or a vendor whose published payment methods are cards only (owner 2026-11-11: on invoice, by bank transfer): no row"] += 1
        continue
    if k in mail:
        (acc, g), m = mail[k]
    else:
        b = borrow(L)
        if not b: continue
        (acc, g), m = b
        borrowed += 1
    if BAD_LOCAL.search(m["mailbox"].split("@")[0]): continue
    lsite = L.get("website") or ""
    if lsite and not same_org(m["mailbox"], lsite, L["buyer_name"]):
        continue  # a contractor's, parent government's or other body's mailbox seen on the lead's pages
    if not lsite:
        ph = (urllib.parse.urlparse(m.get("evidence_url") or "").hostname or "").lower().removeprefix("www.")
        if not (ph and same_org(m["mailbox"], "https://" + ph, L["buyer_name"])):
            continue
    if not mail_page_own(m["mailbox"], m.get("evidence_url") or "", lsite or ("https://" + m["mailbox"].split("@")[-1]), L["buyer_name"], m.get("evidence_quote") or ""):
        n_cl["the mailbox was read on another organisation's page (a directory, a regional body's, a partner's), not on its own: no row"] += 1
        continue
    if "consultant without a firm" in (L.get("canada_field_value") or ""):
        # test row of 2026-11-11: a lobbyists' register names a consultant who files without a firm — a natural person as the vendor (15 rows). A person is
        # not a vendor of this table (the register lanes leave natural persons out since 2026-11-10); the consultant's firm, when the register names one, is.
        n_cl["left out: the vendor is a person (a consultant lobbyist registered without a firm)"] += 1
        continue
    ldom = registrable((urllib.parse.urlparse(lsite).hostname or m["mailbox"].split("@")[-1]).lower().removeprefix("www."))
    if ldom in seen_dom:
        continue  # the same organisation already delivered (contract buyer or another lead with the same website)
    seen_dom.add(ldom)
    client = "vendor located in Canada" in L.get("canada_field_value", "")
    payer = ""
    cfv0, ld0 = L.get("canada_field_value", ""), (L.get("latest_record_date") or "")[:10]
    story_dated = "(stories" in cfv0 and CUTOFF <= ld0 <= today and bool(re.search(r"\(stories; (?:contract data|Canada-HQ)", cfv0) or POSTAL.search(cfv0.upper()))
    if story_dated:
        client = False  # a customer story the vendor published in the last 12 months, vendor proven in Canada: a dated record (B)
    elif client and re.search(r"\((wall|stories)", L.get("canada_field_value", "")):
        # a client logo wall on the vendor's home page, or one of its (undated) customer stories: a client listing by construction — when the story's own
        # address says it is one. Test row of 2026-11-11: "And the honorary doctorate goes to" (a university's news story of 2010) stood as a client of the
        # university; United Way, alumni and sustainability "stories" did the same. A story that is not filed under clients, customers, case studies,
        # success stories or testimonials is a link (tier E), with its reason written on the row.
        other_why = ""
        if "(stories" in cfv0 and not _STORY_REL.search(urllib.parse.urlparse(L.get("evidence_dataset") or "").path.lower()):
            client, other_why = "other", "a news or community story on the vendor's site, not filed as a customer story"
            n_cl["not shown to be a client: a news or community story on the vendor's site (not filed as a customer story)"] += 1
    elif client:  # a link on a Canadian vendor's page: a client listing only on a real client / case-study / references page
        path = urllib.parse.urlparse(L.get("evidence_dataset") or "").path.lower()
        _rost = (LDET.get(k) or {}).get("roster") or ""
        if _rost in ("member", "dealer", "tenant", "sponsor", "exhibitor"):
            payer = "sponsor" if _rost == "exhibitor" else _rost  # a roster another lane harvested (tools/roster_ingest.py): its descriptor says what kind of list it is
        elif MEMBER_ONE_PATH.search(path) or (MEMBER_PATH.search(path) and not NOT_MEMBER_PATH.search(path) and len(path.rstrip("/").rsplit("/", 1)[-1]) <= 36 and not (rel_path(path) and not NOT_REL_PATH.search(path))):
            payer = "member"  # a member directory: the listed party pays dues to the Canada-located body (a long slug that merely contains "membres" is an article)
        elif not NOT_PAYER_PATH.search(path) and (DEALER_PATH.search(path) or SPONSOR_PATH.search(path) or TENANT_PATH.search(path)) and not (rel_path(path) and not NOT_REL_PATH.search(path)):
            payer = "dealer" if DEALER_PATH.search(path) else "sponsor" if SPONSOR_PATH.search(path) else "tenant"  # a customer listing by construction: the listed party pays the Canada-located organisation
        elif not rel_path(path) or NOT_REL_PATH.search(path):
            client = "other"  # owner's rule (2026-11-01): kept as the weakest relationship package, never mixed with client listings
        elif "portfolio" in path and INVESTOR.search(((LDET.get(k) or {}).get("page_title") or "") + " " + (L.get("example_vendor") or "")):
            client = "other"  # an investor's portfolio lists the companies it invested in: a link, not a client relationship
        vh = (urllib.parse.urlparse(L.get("evidence_dataset") or "").hostname or "").lower().removeprefix("www.")
        bh = (urllib.parse.urlparse(L.get("website") or "").hostname or L.get("buyer_name") or "").lower().removeprefix("www.")
        if vh and bh and registrable(vh) == registrable(bh):  # the same organisation linking to itself (sister schools, own departments)
            seen_dom.discard(ldom)  # no row from this lead: the domain stays free for another relationship of the organisation
            continue
        other_why = ""
        _ld0 = LDET.get(k) or {}
        if client is True and not payer and _ld0.get("platform") == "vendor_site_cc" and "client_label" in _ld0:
            _ok, _how = client_listing(path, _ld0.get("client_label") or "", bh, vh)
            n_cl[("client listing: " if _ok else "not shown to be a client: ") + _how] += 1
            if not _ok:
                client, other_why = "other", _how
        if client is True and not payer and _same_family(L["buyer_name"], L.get("example_vendor") or ""):
            # test row of 2026-11-11: "Parkinson Society British Columbia" as a client of "Parkinson Society Newfoundland & Labrador" (a link among sister
            # societies on a testimonial page). Two organisations whose names open with the same two words are bodies of one family, not buyer and vendor.
            client, other_why = "other", "the two organisations carry the same name (bodies of one federation or chain)"
            n_cl["not shown to be a client: sister bodies (names open with the same two words)"] += 1
        if client == "other" and ldom in REG_DOMS:
            # a link that is not shown to be a client relationship, on a site that holds a .ca registration: the registration (a paid relationship
            # with a named Canadian body) claims the row; the link stays listed among the row's other relationship sources
            seen_dom.discard(ldom); n_cl["link only, and the site has a .ca registration: the registration takes the row"] += 1
            continue
    recent = (L.get("latest_record_date") or "") >= CUTOFF and not client  # paid / subcontracted in the last 12 months
    announced = bool(re.search(r"release dateline|EDC|own news release|customer story published by the vendor", L.get("canada_field_value", "")))
    src = (L.get("canada_field_value") or "").split("=")[0].strip()[:90]  # the source's Canada field, e.g. "contractor address country (IRS Form 990)"
    likely = not client and not recent and CUTOFF3 <= (L.get("latest_record_date") or "") < CUTOFF  # owner's 12-36 month rule (dated deal or payment)
    irs = "IRS Form" in L.get("canada_field_value", "")
    tech = "(tech)" in L.get("canada_field_value", "")  # buyer's own site shows it uses a Canada-HQ vendor's paid service today
    member = "membership / statutory fee relationship" in L.get("canada_field_value", "")  # current member / regulated payer list of a Canadian body (own package)
    registry = (L.get("canada_field_value") or "").startswith("registry contract")
    tier = "R" if registry else "M" if member else "T" if tech else "E" if client == "other" else "D" if client else "B" if recent else "L" if likely else "C"
    rows.append({"rank_group": ("GOLD" if tier == "B" and g == 4 and acc else "GOLD-T" if tier == "T" and g == 4 and acc else "GOLD-M" if tier == "M" and g == 4 and acc else "%s%d" % (tier, g)), "completeness_score": TS.get(tier, 0) * 10 + g * 6 + (3 if acc else 0),
        "buyer": L["buyer_name"], "buyer_website": L["website"], "award_date": L.get("latest_record_date") or "",
        "email": m["mailbox"], "email_type": LABEL_G.get(g, m["mailbox_type"]), "email_check": "confirmed" if acc else m["check_status"], "email_evidence_url": m["evidence_url"], "email_evidence_quote": m["evidence_quote"],
        "contract_status": ("registration contract in force for the organisation's own .ca domain name %s (live on %s): every .ca name is held under the Registrant Agreement of the Canadian Internet "
                            "Registration Authority and paid for through a CIRA-certified registrar (a Canadian person or corporation under CIRA's rules); the registrant of record is not read here "
                            "(normally the organisation itself, sometimes its web agency)" % (
                                ("%s — a second name of the organisation: its home page answers at the organisation's site %s, redirect followed %s" % L["_alias"]) if L.get("_alias")
                                else registrable(host_of(L.get("website") or "")), today)) if registry else
                           ("member of a Canadian body (stated on the buyer's own site, read %s): %s" % ((L.get("latest_record_date") or "")[:10], L["example_vendor"])) if member and "member badge on the buyer's own site" in L.get("canada_field_value", "") else
                           ("accredited business of a Canadian Better Business Bureau since %s (its BBB profile read %s): %s — accredited businesses pay the BBB dues"
                            % ((LDET.get(k) or {}).get("accredited_since") or "an unstated date", (L.get("latest_record_date") or "")[:10], L["example_vendor"])) if member and "accredited business of the Canadian body" in L.get("canada_field_value", "") else
                           ("registered with a Canadian regulatory authority, registration no. %s: %s — first registered %s, %s (the authority's own public register, the registrant's entry read %s); "
                            "registrants pay the authority its registration and transaction fees"
                            % ((LDET.get(k) or {}).get("reference") or "?", L["example_vendor"], (LDET.get(k) or {}).get("start") or "on an unstated date",
                               ("registration in force up to %s" % (LDET.get(k) or {})["end"]) if (LDET.get(k) or {}).get("end") else "no expiry date on the entry",
                               (L.get("latest_record_date") or "")[:10])) if member and "registrant of the Canadian body" in L.get("canada_field_value", "") else
                           # 2026-11-13 (tools/bc_crown.py): the Province of British Columbia's Harvest Billing System lists each stumpage invoice and the client it is billed to
                           ("billed stumpage by a Canadian public body: %s — %s invoices to this client in the 12 months to %s, the latest no. %s of %s — the Harvest Billing System's public "
                            "Billing Summary report (read %s); stumpage is billed on the Crown timber the client harvests and is due on receipt of the invoice"
                            % (L["example_vendor"], (LDET.get(k) or {}).get("bc_invoices") or "?", (L.get("latest_record_date") or "")[:10], (LDET.get(k) or {}).get("reference") or "?",
                               (L.get("latest_record_date") or "")[:10], ((LDET.get(k) or {}).get("buyer_register") or {}).get("label", "")[-10:] or (L.get("latest_record_date") or "")[:10]))
                           if member and "stumpage invoice of the Canadian body" in L.get("canada_field_value", "") else
                           ("holder of licence no. %s issued by a Canadian public body: %s — first issued %s, %s (the body's own public list of licences in force, read %s); the holder pays the body to keep the licence"
                            % ((LDET.get(k) or {}).get("reference") or "?", L["example_vendor"], (LDET.get(k) or {}).get("start") or "on an unstated date",
                               ("in force / fees paid up to %s" % (LDET.get(k) or {})["end"]) if (LDET.get(k) or {}).get("end") else "no end or cancellation date in the list",
                               (L.get("latest_record_date") or "")[:10])) if member and "licence holder of the Canadian body" in L.get("canada_field_value", "") else
                           # 2026-11-13 (tools/saq_agents.py): the SAQ's own product pages name the producer and its agent promotionnel in Québec
                           ("producer represented in Québec by its promotional agent: %s is the agent promotionnel of the producer at the Société des alcools du Québec for %s "
                            "product(s) on its list (e.g. %s, code SAQ %s) — the SAQ's own product page%s, read %s; the agent represents the producer in Québec and is paid by it"
                            % (L["example_vendor"], (LDET.get(k) or {}).get("saq_products") or "one or more", (LDET.get(k) or {}).get("title") or "?",
                               (LDET.get(k) or {}).get("reference") or "?", "s" if str((LDET.get(k) or {}).get("saq_products") or "1") != "1" else "",
                               (L.get("latest_record_date") or "")[:10])) if member and "promotional agent of record" in L.get("canada_field_value", "") else
                           ("client of a Canadian trademark agent of record: %s acts for the owner before the Canadian Intellectual Property Office on %s of its trademarks in force or pending "
                            "(e.g. %s; first registered %s, latest renewal due %s) — the Office's public register, extract of %s; an owner's agent fees are sometimes billed through its own counsel"
                            % (L["example_vendor"], (LDET.get(k) or {}).get("tm_marks_with_this_agent") or "one or more", (LDET.get(k) or {}).get("reference") or "see the register",
                               (LDET.get(k) or {}).get("tm_first_registered") or "not yet", (LDET.get(k) or {}).get("tm_latest_renewal_due") or "not set",
                               (LDET.get(k) or {}).get("tm_extract") or (L.get("latest_record_date") or "")[:10])) if member and "trademark agent of record" in L.get("canada_field_value", "") else
                           ("client of a Canadian patent agent of record: %s acts for the owner before the Canadian Intellectual Property Office on %s of its Canadian patents and applications "
                            "(e.g. %s; %s in force, %s pending) — the Office's public patent register, extract of %s; the agent prosecutes the applications, pays the yearly maintenance fees "
                            "and bills the owner for both, sometimes through the owner's own counsel"
                            % (L["example_vendor"], (LDET.get(k) or {}).get("pt_with_this_agent") or "one or more", (LDET.get(k) or {}).get("reference") or "see the register",
                               (LDET.get(k) or {}).get("pt_in_force", "?"), (LDET.get(k) or {}).get("pt_pending", "?"),
                               (LDET.get(k) or {}).get("pt_extract") or (L.get("latest_record_date") or "")[:10])) if member and "patent agent of record" in L.get("canada_field_value", "") else
                           ("owner of %s trademark registration(s) in force on the Canadian register (e.g. %s; first registered %s, latest renewal due %s): the owner pays the Canadian Intellectual "
                            "Property Office to register a mark and to renew it every ten years — the Office's public register, extract of %s"
                            % ((LDET.get(k) or {}).get("tm_marks_in_force") or "one or more", (LDET.get(k) or {}).get("reference") or "see the register",
                               (LDET.get(k) or {}).get("tm_first_registered") or "not yet", (LDET.get(k) or {}).get("tm_latest_renewal_due") or "not set",
                               (LDET.get(k) or {}).get("tm_extract") or (L.get("latest_record_date") or "")[:10])) if member and "trademark registration holder of the Canadian body" in L.get("canada_field_value", "") else
                           ("holds the right to sell %s in Canada on Health Canada's public register (%s, read %s): Health Canada invoices the holder every year for the right "
                            "to sell each one" % ((LDET.get(k) or {}).get("hc_what") or "products", (LDET.get(k) or {}).get("register_label") or "Health Canada's register",
                                                  (L.get("latest_record_date") or "")[:10])) if member and "right-to-sell holder of the Canadian body" in L.get("canada_field_value", "") else
                           ("listed issuer on a Canadian stock exchange: %s — symbol %s, listed since %s, on %s (read %s); every listed company pays the exchange %s"
                            % (L["example_vendor"], (LDET.get(k) or {}).get("xc_ticker") or "?", (LDET.get(k) or {}).get("start") or "an unstated date",
                               (LDET.get(k) or {}).get("register_label") or "the exchange's list of listed companies", (L.get("latest_record_date") or "")[:10],
                               (LDET.get(k) or {}).get("xc_fee_words") or "an annual sustaining fee, on the exchange's invoice")) if member and "listed issuer of the Canadian body" in L.get("canada_field_value", "") else
                           ("member / regulated payer of a Canadian body (current list read %s): %s" % ((L.get("latest_record_date") or "")[:10], L["example_vendor"])) if member else
                           tech_status(k, L) if tech else
                           ("likely active (awarded 12-36 months ago; deal announced by the Canada-based vendor: press release / EDC transaction)" if announced else
                            "likely active (awarded 12-36 months ago; paid in a fiscal year ending 12-36 months ago: IRS Form 990 contractor located in Canada)" if irs else
                            "likely active (awarded 12-36 months ago; record dated 12-36 months ago: %s)" % src) if likely else
                           (("link on a client-type page of the Canada-located vendor's site, not shown to be a client relationship (%s)" % other_why) if other_why else
                            "linked from a page of the Canada-located vendor's site (not a client page)") if client == "other" else
                           (PAYER_TEXT[payer] if payer else "client listing on the vendor's own site (undated)") if client else
                           ("likely active (customer story published by the Canada-located vendor in the last 12 months)" if story_dated else
                            "likely active (contract announced by the Canada-based vendor in the last 12 months: press release / EDC transaction)"
                            if re.search(r"release dateline|EDC|own news release", L.get("canada_field_value", "")) else
                            "likely active (paid in a fiscal year ending in the last 12 months: IRS Form 990 contractor located in Canada)" if irs else
                            "likely active (record dated in the last 12 months: %s)" % src) if recent else "payment / subaward record",
        "contract_link": L["evidence_dataset"], "vendor": L["example_vendor"], "vendor_country_basis": L["canada_field_value"],
        "contracts_with_canadian_suppliers": L["canadian_vendor_rows"], "keys": k, "buyer_keys": 1, "tier": tier, "grade": g, "acc": acc})
    x, ev, cfv = rows[-1], (L.get("example_vendor") or "").strip(), (L.get("canada_field_value") or "")
    if L.get("_alias") and not registry:  # the record is about the organisation's other domain name: said in the row
        x["contract_status"] = "%s — the record is about the organisation's domain name %s, whose home page answers at its site %s (redirect followed %s)" % (((x.get("contract_status") or "").rstrip(". "),) + tuple(L["_alias"]))
    dm = re.search(r"=\s*([a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,})(?:[;/\s]|$)", cfv.lower())
    vdom = ev.lower() if re.fullmatch(r"[a-z0-9-]+(\.[a-z0-9-]+)*\.[a-z]{2,}", ev.lower()) else (dm.group(1) if dm else "")
    x.update(vend_fill("", "" if vdom == ev.lower() else ev, vdom))
    apply_details(x, k)
    _dd0 = LDET.get(k) or {}
    if (_dd0.get("platform") == "roster_file" and _dd0.get("list_name") and _dd0.get("record_url")
            and registrable(host_of(_dd0.get("record_url") or "")) != registrable(host_of(_dd0.get("vendor_site") or ""))):
        # 2026-11-13: a roster kept by ANOTHER public body that the biller's own page links (Ontario's cannabis stores on the AGCO's open data, B.C.'s
        # on the province's licence list): not "a client listing on the vendor's own site" — the list, who keeps it, and the biller's own words
        # (the roster's marker words stay first: the give-way rule, the billing period and the fact basis read them)
        _mk = {"dealer": "dealer / retailer named by", "member": "member named in the member directory of", "tenant": "tenant / merchant named by",
               "sponsor": "sponsor / exhibitor named by", "exhibitor": "sponsor / exhibitor named by"}.get(_dd0.get("roster") or "")
        if _mk:
            x["contract_status"] = ("%s %s on %s (%s), a list kept by another public body that the biller's own page links; the biller's own words: “%s”" % (
                _mk, _dd0.get("vendor") or "the Canada-located body", _dd0["list_name"][:200], _dd0["record_url"], (_dd0.get("pays_quote") or "")[:280]))
    if _dd0.get("platform") == "dian_import":
        # tools/dian_cloud.py: Colombia's customs (DIAN) publishes every import declaration line — the importer (with its NIT), the exporter with its
        # address, the exporter's invoice number and date, its FOB value and how the importer pays it (FORMA_PAGO): a public record of the bill
        x["contract_status"] = ("importer of record of goods invoiced by an exporter located in Canada: %s invoiced it on %s (invoice %s, US$%s FOB) — import "
                                "declaration %s of %s published by Colombia's customs (DIAN); %s declaration line%s from exporters in Canada on file from %s to %s, US$%s FOB in all"
                                % (_dd0.get("vendor") or "", _dd0.get("dian_invoice_date") or "an unstated date", _dd0.get("dian_invoice") or "?",
                                   format(float(_dd0.get("dian_fob") or 0), ",.2f"), _dd0.get("dian_declaration") or "?", _dd0.get("dian_declaration_date") or "?",
                                   L.get("canadian_vendor_rows") or "1", "" if str(L.get("canadian_vendor_rows")) == "1" else "s", _dd0.get("dian_first") or "?",
                                   _dd0.get("dian_last") or "?", format(float(_dd0.get("dian_fob_total_buyer") or 0), ",.2f")))
        if _dd0.get("dian_payment_form"):
            x["bill_payment_method_as_published"] = "“%s” (FORMA_PAGO of the import declaration; TIPO_IMPORTACION “%s”)" % (_dd0["dian_payment_form"], _dd0.get("dian_import_type") or "")
        if not x.get("buyer_address") and _dd0.get("dian_importer_address"):
            x["buyer_address"] = "%s (as the import declaration records it: DIRECCION_IMPORTADOR, DEPARTAMENTO_IMPORTADOR)" % _dd0["dian_importer_address"]
    if _dd0.get("platform") == "f5500_plan":
        # tools/f5500_benefits.py: the plan's Form 5500 (US Department of Labor) names the Canadian insurer of its contracts (Schedule A) or a provider
        # in Canada it paid (Schedule C item 2)
        if _dd0.get("f55_insurer"):
            x["contract_status"] = ("insured benefit plan of a Canadian insurer: %s insures the organisation's plan (%s) — policy %s, %s, %s persons covered, policy period "
                                    "to %s; Form 5500 Schedule A of plan year %s (US Department of Labor)" % (
                                        _dd0["f55_insurer"], (_dd0.get("f55_plan_names") or "its benefit plan")[:120], _dd0.get("f55_policy_numbers") or "?",
                                        _dd0.get("f55_benefits") or "group insurance", _dd0.get("f55_persons") or "?", _dd0.get("f55_policy_to") or "?", _dd0.get("f55_plan_year") or "?"))
        else:
            x["contract_status"] = ("service provider in Canada paid by the organisation's benefit plan: %s, paid US$%s in plan year %s (Form 5500 Schedule C, US Department of Labor)"
                                    % (_dd0.get("f55_providers") or _dd0.get("vendor") or "?", format(float(_dd0.get("f55_provider_comp") or 0), ",.0f"), _dd0.get("f55_plan_year") or "?"))
        if not x.get("buyer_address") and _dd0.get("f55_sponsor_address"):
            x["buyer_address"] = "%s (the sponsor's mailing address as the plan's Form 5500 records it)" % _dd0["f55_sponsor_address"]
    if registry:
        x["vendor_website"] = x.get("vendor_website") or "https://www.cira.ca/"
        x["vendor_address"] = (LDET.get(k) or {}).get("vendor_address") or x.get("vendor_address") or ""  # CIRA's address as its own agreement prints it (a dataset record of CIRA said only "Ottawa, ON")
    x["source"] = ("the .ca registry's public delegation of the buyer's domain (DNS) and CIRA's Registrant Agreement" if registry else
                   "the buyer's own website (it states its membership of the Canada-located body, linked)" if member and "member badge on the buyer's own site" in cfv else
                   "the Canadian regulatory authority's own public register (the registrant's own entry)" if member and "registrant of the Canadian body" in cfv else
                   "the Canadian licensing body's own public list of active licences (open data, updated daily)" if member and "licence holder of the Canadian body" in cfv else
                   "the exchange's own list of listed companies (TMX Group's monthly workbook of TSX and TSXV issuers)" if member and "listed issuer of the Canadian body" in cfv else
                   "the Société des alcools du Québec's own product pages (producer and agent promotionnel of each product)" if member and "promotional agent of record" in cfv else
                   "the Canadian trademarks register published by the Canadian Intellectual Property Office (open data; owner of record and agent of record)" if member and "trademark" in cfv and "Canadian Intellectual Property Office" in cfv else
                   "the Canadian body's own current member / participant list" if member else
                   "the buyer's own website (its credit line names the Canada-located vendor that made / hosts the site)" if tech and "credited on the buyer's own site" in cfv else
                   "the buyer's own public DNS records (they name the Canada-located provider of its e-mail, hosting or DNS service)" if tech and "seen in the buyer's public DNS" in cfv else
                   "the buyer's own website or its customer portal on the vendor's platform (service of a Canada-HQ vendor in use)" if tech else
                   "the Canada-located vendor's own website" if client else src or "relationship record")
    if (LDET.get(k) or {}).get("platform") == "dian_import":
        x["source"] = "Colombia's customs (DIAN) import declaration"
    if (LDET.get(k) or {}).get("platform") == "f5500_plan":
        x["source"] = "the plan's Form 5500 filing (US Department of Labor)"
print("lead rows: facts from the buyer's own pages / the vendor's link label:", dict(n_lf), "| sites named again from their stored home-page title:", n_name_again)
print("client-page links judged (cloud row factory):", dict(sorted(n_cl.items(), key=lambda kv: -kv[1])))
for x in rows:
    x.setdefault("_jur", "")
# 4b. a dated record from the last 12 months (lead: payment, auditor's report, filing, release ...) for an organisation
# already delivered with an older or undated relationship (contract 12-36 months / over 3 years old, client listing,
# other link, service seen on its site): the row takes the newer relationship. Only when ONE delivered row has that
# registrable website domain (never guess between bodies sharing a domain).
up, up_t = collections.defaultdict(list), collections.defaultdict(list)
for k, L in leads.items():
    cfv, ld = L.get("canada_field_value") or "", (L.get("latest_record_date") or "")[:10]
    d = registrable(host_of(L.get("website") or ""))
    if "(tech)" in cfv and d and CUTOFF <= ld <= today:
        up_t[d].append((ld, k, L))  # an active service seen on the buyer's own site: upgrades a client-listing / link / old row to T
        continue
    if cfv.startswith("registry contract") or "vendor located in Canada" in cfv or "membership / statutory fee relationship" in cfv or not (CUTOFF <= ld <= today) or UNNAMED_VENDOR.search(L.get("example_vendor") or ""):
        continue  # client listings, member lists and registry contracts are not dated purchase records; the vendor must be named
    if d:
        up[d].append((ld, k, L))
dom_rows = collections.defaultdict(list)
for x in rows:
    d = registrable(host_of(x.get("buyer_website") or ""))
    if d:
        dom_rows[d].append(x)
upgraded = 0
GENERIC_W = ("city", "town", "county", "district", "university", "college", "municipality", "corporation", "township", "village", "school", "board", "society", "association")
named = lambda nm: "." not in nm or " " in nm.strip()  # a real name, not a bare domain
def same_body(L, x):
    lt = {w for w in re.findall(r"[a-z]{4,}", norm(L.get("buyer_name") or "")) if w not in GENERIC_W}
    return not (lt and named(L.get("buyer_name") or "") and named(x["buyer"]) and not lt & set(re.findall(r"[a-z]{4,}", norm(x["buyer"]))))
# 2026-11-10 (row audit): a row that takes a newer relationship kept cells of the old one — the old contract's number as "the reference to quote",
# its description, instrument, bids and identifiers, the old vendor's registry cells — next to the new vendor's name (a credit-line row of a
# municipality quoted a SEAO tender number of another supplier's contract). Every cell that describes the old relationship is emptied first:
# the old record's identifiers, text, amounts and dates, every vendor_* cell, the pair facts. Buyer-level facts stay (its other vendors, its
# record counts, its most recent reference, each labelled as such).
OLD_REL_COLS = {"contract_reference", "contract_title", "contract_value", "currency", "start_date", "end_date", "instrument_type", "procurement_method", "commodity",
                "contract_description", "number_of_bids", "po_number_as_published", "contract_or_agreement_number", "solicitation_or_tender_number", "award_or_notice_id",
                "buyer_vendor_id", "vendor_ids_in_record", "commodity_codes", "buyer_org_codes", "amendment_or_modification", "all_identifiers", "identifier_count",
                "invoice_reference_hint", "records_with_this_vendor", "all_references_with_this_vendor"}
def reset_relationship(x):
    for col in list(x):
        if col in OLD_REL_COLS or col.startswith("vendor_") or col.endswith("_from_pair"):
            x[col] = ""
for d, cands in up.items():
    xs = dom_rows.get(d) or []
    if len(xs) != 1 or xs[0]["tier"] in ("A", "B"):
        continue
    x = xs[0]
    pick = next(((k, L) for ld, k, L in sorted(cands, key=lambda c: c[0], reverse=True) if same_body(L, x)), None)
    if not pick:
        continue  # every dated lead names another body (e.g. a library or board on the same website)
    k, L = pick
    cfv = L.get("canada_field_value") or ""
    g, acc = int(x["grade"] or 0), x["acc"]
    src = cfv.split("=")[0].strip()[:90]
    reset_relationship(x)
    x.update({"tier": "B", "rank_group": "GOLD" if g == 4 and acc else "B%d" % g, "completeness_score": TS["B"] * 10 + g * 6 + (3 if acc else 0),
              "award_date": L["latest_record_date"][:10], "contract_link": L["evidence_dataset"], "vendor": L["example_vendor"],
              "vendor_country_basis": cfv, "contracts_with_canadian_suppliers": L["canadian_vendor_rows"],
              "contract_status": ("likely active (contract announced by the Canada-based vendor in the last 12 months: press release / EDC transaction)"
                                  if re.search(r"release dateline|EDC|own news release", cfv) else
                                  "likely active (paid in a fiscal year ending in the last 12 months: IRS Form 990 contractor located in Canada)" if "IRS Form" in cfv else
                                  "likely active (record dated in the last 12 months: %s)" % src),
              "source": src or "relationship record", "keys": "|".join(sorted(set((x.get("keys") or "").split("|") + [k]) - {""})),
              "buyer_keys": int(x.get("buyer_keys") or 1) + 1})
    for col in ("contract_reference", "contract_title", "contract_value", "currency", "start_date", "end_date", "vendor_legal_name",
                "vendor_address", "vendor_bn9", "vendor_gst_hst_derived", "vendor_website", "vendor_emails"):
        x[col] = ""
    ev = (L.get("example_vendor") or "").strip()
    dm = re.search(r"=\s*([a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,})(?:[;/\s]|$)", cfv.lower())
    vdom = ev.lower() if re.fullmatch(r"[a-z0-9-]+(\.[a-z0-9-]+)*\.[a-z]{2,}", ev.lower()) else (dm.group(1) if dm else "")
    x.update(vend_fill("", "" if vdom == ev.lower() else ev, vdom))
    apply_details(x, k)
    upgraded += 1
upgraded_t = 0
for d, cands in up_t.items():
    xs = dom_rows.get(d) or []
    if len(xs) != 1 or xs[0]["tier"] not in ("C", "D", "E", "L"):
        continue
    x = xs[0]
    pick = next(((k, L) for ld, k, L in sorted(cands, key=lambda c: c[0], reverse=True) if same_body(L, x)), None)
    if not pick:
        continue
    k, L = pick
    g, acc = int(x["grade"] or 0), x["acc"]
    reset_relationship(x)
    x.update({"tier": "T", "rank_group": "GOLD-T" if g == 4 and acc else "T%d" % g, "completeness_score": TS["T"] * 10 + g * 6 + (3 if acc else 0),
              "award_date": L["latest_record_date"][:10], "contract_link": L["evidence_dataset"], "vendor": L["example_vendor"],
              "vendor_country_basis": L.get("canada_field_value") or "", "contracts_with_canadian_suppliers": L["canadian_vendor_rows"],
              "contract_status": tech_status(k, L),
              "source": "the buyer's own website (its credit line names the Canada-located vendor that made / hosts the site)" if "credited on the buyer's own site" in (L.get("canada_field_value") or "") else
                        "the buyer's own public DNS records (they name the Canada-located provider of its e-mail, hosting or DNS service)" if "seen in the buyer's public DNS" in (L.get("canada_field_value") or "") else
                        "the buyer's own website (service of a Canada-HQ vendor in use)",
              "keys": "|".join(sorted(set((x.get("keys") or "").split("|") + [k]) - {""})), "buyer_keys": int(x.get("buyer_keys") or 1) + 1})
    for col in ("contract_reference", "contract_title", "contract_value", "currency", "start_date", "end_date", "vendor_legal_name",
                "vendor_address", "vendor_bn9", "vendor_gst_hst_derived", "vendor_website", "vendor_emails"):
        x[col] = ""
    ev = (L.get("example_vendor") or "").strip()
    if "credited on the buyer's own site" in (L.get("canada_field_value") or "") or "seen in the buyer's public DNS" in (L.get("canada_field_value") or ""):
        _dm = re.search(r"=\s*([a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,})(?:[;/\s]|$)", (L.get("canada_field_value") or "").lower())
        x.update(vend_fill("", "" if _dm and _dm.group(1) == ev.lower() else ev, _dm.group(1) if _dm else ""))
        apply_details(x, k)  # the vendor's address as its own site prints it, the credit line as the service description
    else:
        x.update(vend_fill("", ev, ""))
    upgraded_t += 1
print("leads with a borrowed mailbox: %d | rows upgraded by a newer dated record: %d | rows upgraded to an active service seen on the buyer's site: %d" % (borrowed, upgraded, upgraded_t))
# 5. P12 (owner 2026-11-03, "lowest quality but still AP"): organisations not ranked above, with their own confirmed
# mailbox, whose relationship is weaker: a contract whose vendor is in Canada only through a business-registry match
# (the source has no vendor country; owner's item 2 of 2026-11-01), or a contract that already ended, dated (award /
# start / end) on or after CUT5 (5 years). Labelled "weaker relationship" so it never mixes with P01-P11.
covered_keys = {k for x in rows for k in (x.get("keys") or "").split("|") if k}
covered_dom = {registrable(host_of(x["buyer_website"])) for x in rows if x.get("buyer_website")} - {""}
covered_name = {norm(x["buyer"]) for x in rows} - {""}
covered_mail = {(x.get("email") or "").lower() for x in rows} - {""}
def reg_canada(ve):
    """the vendor is in Canada through a registry match: a confident match whose registered office is in Canada"""
    if ve.get("registry_match_level") not in ("exact", "strong"):
        return ""
    ra = ve.get("registered_address") or {}
    if not (ra.get("country") in ("CA", "CAN", "Canada") or POSTAL.search(addr_text(ra).upper())):
        return ""
    m = next((m for m in ve.get("matches") or [] if m.get("match_confidence") in ("exact", "strong")), {})
    return "registry match only (%s): %s %s '%s', registered office %s (%s); the source publishes no vendor country" % (
        ve.get("registry_match_level"), m.get("registry") or "registry", m.get("id") or "", m.get("legal_name") or ve.get("legal_name") or "",
        addr_text(ra), (m.get("source_url") or "")[:120])
import glob as _glob
orgs12, seen_rec = {}, set()
for kind, paths in ((("ended", sorted(_glob.glob(REL + "ended_*.jsonl.gz"))), ("registry", [REL + "vendor_country_unverified_contracts.jsonl.gz"])) if _PI == 0 else ()):  # ranking in parts: P12 in part 0
    for r in jl(*paths):
        if r.get("record_id") in seen_rec:
            continue
        seen_rec.add(r.get("record_id"))
        clean_ve(r)
        d = r["contract"].get("dates") or {}
        end, ad = str(d.get("end") or "")[:10], award_date(r)
        if ad > today:
            continue
        if kind == "ended":
            basis = (r.get("vendor") or {}).get("country_basis") or ""
            if not basis or not (ad >= CUT5 or CUT5 <= end < today):
                continue
        else:
            basis = reg_canada(r.get("vendor_enrichment") or {})
            if not basis or not (ad >= CUT5 or end >= today):
                continue
        be = r.get("buyer_enrichment") or {}
        key = be.get("buyer_key"); name = be.get("canonical_name") or (r.get("buyer") or {}).get("name") or ""
        p, j, own = parent(name), jur_of_record(r), (r.get("buyer") or {}).get("name") or ""
        po = parent(own)
        if po and len(po.split()) <= 3 and not PLACE.search(po) and j:
            p, name = po + " | " + j, own
        if not p or p in orgs or key in covered_keys or norm(name) in covered_name:
            continue
        s12 = (kind == "ended", max(ad, end if end < today else ad), contract_score(r)[1])
        o = orgs12.setdefault(p, {"keys": set(), "best": None, "bs": None, "n": 0, "name": name, "be": be, "jur": collections.Counter(), "basis": "", "kind": ""})
        o["keys"].add(key); o["n"] += 1; o["jur"][j] += 1
        if o["bs"] is None or s12 > o["bs"]:
            o.update(best=r, bs=s12, basis=basis, kind=kind, fields=s12[2])
n12, skipped12 = 0, collections.Counter()
for p, o in orgs12.items():
    r, be = o["best"], o["be"]
    c, v, ve, d = r["contract"], r.get("vendor") or {}, r.get("vendor_enrichment") or {}, (r["contract"].get("dates") or {})
    gj = o["jur"].most_common(1)[0][0] if o["jur"] else ""
    site = be.get("official_website") or next((BUY[k]["official_website"] for k in o["keys"] if k in BUY and BUY[k].get("official_website")), "")
    em, et, es, eu, eq, g, acc = emailcols(o["keys"], be, gj, o["name"], site)
    if not (em and acc and g >= 1) or em.lower() in covered_mail or (site and registrable(host_of(site)) in covered_dom):
        skipped12["no own confirmed mailbox" if not (em and acc and g >= 1) else "same organisation already in a row"] += 1
        continue  # P12 needs the organisation's own confirmed mailbox and an organisation not delivered above
    end, ad = str(d.get("end") or "")[:10], award_date(r)
    st = ("weaker relationship (within 5 years): contract ended %s (awarded %s); vendor located in Canada per the source" % (end, ad or "date not published")
          if o["kind"] == "ended" else
          "weaker relationship (within 5 years): %s; vendor located in Canada only through a business-registry match" %
          ("active contract (published end date %s)" % end if end >= today else "contract awarded %s" % ad))
    a = v.get("address") or {}
    rows.append({"jurisdiction": gj, "rank_group": "F%d" % g, "completeness_score": (20 if o["kind"] == "ended" else 10) + g * 6 + 3 + o["fields"],
        "buyer": o["name"], "buyer_website": site, "buyer_address": json.dumps(be.get("address") or {}, ensure_ascii=False)[:200],
        "email": em, "email_type": et, "email_check": es, "email_evidence_url": eu, "email_evidence_quote": eq, "contract_status": st,
        "contract_reference": json.dumps(c.get("identifiers") or {}, ensure_ascii=False)[:3000], "contract_title": (c.get("title") or "")[:200], **rec_extra(c), **classify_plus(c, (r.get("source") or {}).get("key") or ""),
        "contract_value": c.get("value") or "", "currency": c.get("currency") or "", "award_date": ad, "start_date": d.get("start") or "", "end_date": end,
        "contract_link": r.get("link") or "", "source": (r.get("source") or {}).get("name", ""), "vendor": v.get("name") or "", "vendor_legal_name": ve.get("legal_name") or "",
        "vendor_address": addr_text(a), "vendor_country_basis": o["basis"] if o["kind"] == "registry" else v.get("country_basis") or "",
        "vendor_bn9": ve.get("business_number_bn9") or "", "vendor_gst_hst_derived": ve.get("gst_hst_account_derived") or "", "vendor_website": ve.get("website") or "",
        "vendor_emails": "; ".join((x.get("email") or x.get("value") or "") if isinstance(x, dict) else str(x) for x in (ve.get("contact_emails_published") or [])),
        "contracts_with_canadian_suppliers": o["n"], "buyer_keys": len(o["keys"]), "keys": "|".join(sorted(k for k in o["keys"] if k)), "tier": "F", "grade": g, "acc": acc})
    fill_contract(rows[-1], r, o["keys"])
    n12 += 1
    covered_keys |= o["keys"]; covered_mail.add(em.lower()); covered_name.add(norm(o["name"]))
    if rows[-1]["buyer_website"]:
        covered_dom.add(registrable(host_of(rows[-1]["buyer_website"])))
# 6. P13 (owner 2026-11-03, "even more inferred"): every other organisation with its own confirmed role mailbox
# (coord/results/org_mailboxes.csv) and no relationship row: the Canada-located vendor it very likely pays, inferred
# from its type and province, with the law or market fact in plain words. Never a record: vendor "inferred: ...",
# contract_status "inferred relationship (no record): ...". Each vendor's location is quoted from its own site
# (pages read 2026-11-03).
INFV = {
    "MPAC": ("Municipal Property Assessment Corporation (MPAC)", "https://www.mpac.ca", "1340 Pickering Parkway, Suite 101, Pickering ON L1V 0C4",
             "https://www.mpac.ca/en/ContactUs", "or by mail to MPAC, 1340 Pickering Parkway, Suite 101, Pickering ON L1V 0C4"),
    "CPC": ("Canada Post Corporation", "https://www.canadapost-postescanada.ca", "2701 Riverside Drive, Ottawa ON K1A 0B1",
            "https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page",
            "Access to Information and Privacy Canada Post Corporation 2701 Riverside Drive, N1160 Ottawa ON K1A 0B1"),
    "HQ": ("Hydro-Québec", "https://www.hydroquebec.com", "75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4",
           "https://www.hydroquebec.com/nous-joindre/", "Siège social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4"),
    "MBH": ("Manitoba Hydro", "https://www.hydro.mb.ca", "360 Portage Avenue, Winnipeg, MB R3C 0G8",
            "https://www.hydro.mb.ca/support/contact/", "Mail Manitoba Hydro 360 Portage Avenue Winnipeg, MB Canada R3C 0G8"),
    "SKP": ("SaskPower", "https://www.saskpower.com", "2025 Victoria Avenue, Regina, SK S4P 0S1", "https://saskpower.com/contact",
            "Send us a letter: SaskPower Corporate Relations and Communications 9th Floor, 2025 Victoria Ave Regina, SK S4P 0S1"),
    "NBP": ("NB Power", "https://www.nbpower.com", "515 King Street, Fredericton, NB E3B 4X1", "https://www.nbpower.com/en/contact-us/",
            "For correspondence NB Power 515 King Street PO Box 2000, STN A Fredericton, NB E3B 4X1"),
    "QEC": ("Qulliq Energy Corporation", "https://www.qec.nu.ca", "3091 6th Street, Baker Lake, NU X0C 0A0", "https://www.qec.nu.ca/contact-us",
            "REGIONAL OFFICES Baker Lake Iqaluit 3091 6th Street Baker Lake, NU X0C 0A0"),
    "BCH": ("BC Hydro", "https://www.bchydro.com", "333 Dunsmuir St., Vancouver, B.C. V6B 5R3", "https://www.bchydro.com/contact.html",
            "Corporate head office 333 Dunsmuir St. Vancouver, B.C. V6B 5R3"),
}
FACT = {
    "MPAC": "MPAC is 'an independent, not-for-profit corporation funded by all Ontario municipalities' (its own site, https://www.mpac.ca/en/AboutUs; "
            "levy under the Municipal Property Assessment Corporation Act, 1997; a lower-tier municipality's share may be paid through its county or region)",
    "CPC": "Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14)",
    "HQ": "Hydro-Québec holds the exclusive right to distribute electricity in Québec outside the 9 municipal networks (Alma, Amos, Baie-Comeau, Coaticook, "
          "Joliette, Magog, Saguenay-Jonquière, Sherbrooke, Westmount) and the Saint-Jean-Baptiste-de-Rouville co-op (Act respecting the Régie de l'énergie)",
    "MBH": "Manitoba Hydro is the only electricity distributor in Manitoba (The Manitoba Hydro Act; it took over Winnipeg Hydro in 2002)",
    "SKP": "SaskPower holds the electricity franchise in Saskatchewan outside the Saskatoon and Swift Current municipal utilities (The Power Corporation Act)",
    "NBP": "NB Power distributes electricity across New Brunswick outside the Saint John, Edmundston and Perth-Andover utilities (Electricity Act)",
    "QEC": "Qulliq Energy Corporation is the only electricity utility in Nunavut, serving all 25 communities (Qulliq Energy Corporation Act)",
    "BCH": "BC Hydro is the electricity utility for most of British Columbia (FortisBC and a few municipal utilities serve parts of the Okanagan and Kootenays)",
}
UTIL = {"QC": ("HQ", r"\b(alma|amos|baie comeau|coaticook|joliette|magog|saguenay|jonquiere|sherbrooke|lennoxville|rock forest|fleurimont|"
                    r"westmount|saint jean baptiste)\b"),
        "MB": ("MBH", r"$^"), "SK": ("SKP", r"\b(saskatoon|swift current)\b"), "NB": ("NBP", r"\b(saint john|edmundston|perth andover)\b"),
        "NU": ("QEC", r"$^"),
        "BC": ("BCH", r"\b(new westminster|nelson|penticton|summerland|grand forks|kelowna|trail|castlegar|rossland|osoyoos|oliver|princeton|creston|"
                      r"peachland|lake country|keremeos|greenwood|midway|fruitvale|montrose|warfield|salmo|kaslo|naramata)\b")}
NOT_MUNI = re.compile(r"librar|biblioth|police|housing|habitation|hydro|museum|musee|arena|chamber|chambre|school|ecole|scolaire|fire|incendie|club|church|"
                      r"eglise|tourism|tourisme|caisse|foundation|fondation|association|society|societe|cooperative|centre|center|festival|golf|marina|"
                      r"hotel|restaurant|\binc\b|\bltd\b|\bltee\b|corporation de developpement|economic development|\bbia\b|business|improvement|plumbing|heating|"
                      r"construction|trades|energy|services|solutions|\bgroup|groupe|realty|immobili|consult|church|parish|diocese|motel|\bclub\b", re.I)
MUNI_NAME = re.compile(r"^(?:the\s+)?(?:corporation of the\s+)?(?:(?:ville|municipalite|cite|canton|cantons unis|paroisse|village|town|city|township|county|"
                       r"comte|united counties|regional municipality|region|rural municipality|resort village|summer village|municipal district|"
                       r"district municipality|municipality|regional district|district|hamlet)\s+(?:of|de|du|des|d)\b|mrc\b|m r c\b|municipalite regionale de comte\b)|"
                       r"\s(?:township|county|municipality)$")
MUNI_DOM = re.compile(r"^(?:ville|town|city|township|municipalite|municipality|canton|paroisse|county|comte|mrc)\.[a-z0-9-]+\.|"
                      r"^(?:villede|townof|cityof|townshipof|countyof|municipalitede|municipalityof|cantonde|paroissede|mrcde)[a-z]{3,}", re.I)
INST = re.compile(r"\b(school|schools|scolaire|cegep|college|universit\w*|hospital|hopital|cisss|ciusss|health|sante|board of education|school district|"
                  r"centre de services scolaire|commission scolaire|conseil scolaire|first nation|premiere nation|government|gouvernement|ministry|ministere)\b")
PROV_DOM = {"qc": "QC", "on": "ON", "bc": "BC", "ab": "AB", "mb": "MB", "sk": "SK", "ns": "NS", "nb": "NB", "nl": "NL", "nf": "NL", "pe": "PE",
            "yk": "YT", "nt": "NT", "nu": "NU"}
PNAME = {"QC": "Québec", "ON": "Ontario", "BC": "British Columbia", "AB": "Alberta", "MB": "Manitoba", "SK": "Saskatchewan", "NS": "Nova Scotia",
         "NB": "New Brunswick", "NL": "Newfoundland and Labrador", "PE": "Prince Edward Island", "YT": "Yukon", "NT": "Northwest Territories", "NU": "Nunavut"}
# Registered addresses from public registries (CRA List of charities, provincial school directories), built by
# org_places.py: key -> province / city. A key listed there is an organisation located in Canada by that registry.
PLACES = {}
if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "org_places.csv.gz")):
    with gzip.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "org_places.csv.gz"), "rt", encoding="utf-8") as _fh:
        for _r in csv.DictReader(_fh):
            if (_r.get("country") or "CA") == "CA":
                PLACES[_r["buyer_key"]] = _r
def place_cell(k):
    """the registered address a public registry gives for the organisation (org_places.csv.gz: the CRA List of charities, the provincial school
    directories), as an address cell that says where it is from; '' when there is none"""
    pl = PLACES.get(k) or {}
    pc = re.sub(r"[^A-Z0-9]", "", (pl.get("postal_code") or "").upper())
    pc = "%s %s" % (pc[:3], pc[3:]) if len(pc) == 6 else (pl.get("postal_code") or "")
    head = ", ".join(v for v in (pl.get("address"), pl.get("city"), " ".join(v_ for v_ in (pl.get("province"), pc) if v_)) if v)
    return ("%s (its registered address in %s)" % (head, pl.get("source") or "a public registry")) if head else ""
def province_of(k, email, site, quote):
    if k in VEN and VEN[k]["region"]:
        return VEN[k]["region"], "its address in the vendor table of the release"
    if k in BUY and region_code(BUY[k].get("address")):
        return region_code(BUY[k].get("address")), "its address in the buyer table of the release"
    if k in PLACES and PLACES[k].get("province") in PNAME:
        return PLACES[k]["province"], "its registered address in %s" % PLACES[k]["source"]
    for dom in (email.split("@")[-1].lower(), host_of(site)):
        m = re.search(r"\.([a-z]{2})\.ca$", dom)
        if m and m.group(1) in PROV_DOM:
            return PROV_DOM[m.group(1)], "its domain %s" % dom
        j = jur_of_mail("x@" + dom)
        if j and j != "FED":
            return j, "its domain %s" % dom
    pcs = {prov_of_postal(m.group(0)) for m in POSTAL.finditer((quote or "").upper())} - {""}
    if len(pcs) == 1:
        return pcs.pop(), "the postal code on its own page (%s)" % POSTAL.search((quote or "").upper()).group(0)
    return "", ""
def infer(name, email, site, prov, fed, place=""):
    """(vendor id, confidence, buyer description, why): near-certain by law / market structure first, generic last"""
    n, dom = norm(name), email.split("@")[-1].lower()
    muni = (bool(MUNI_NAME.search(n)) or bool(MUNI_DOM.search(dom)) or bool(MUNI_DOM.search(host_of(site)))) and not NOT_MUNI.search(n)
    inst = bool(INST.search(n)) and not re.search(r"\b(inc|ltd|ltee|corp|llc|enr)\b", n)  # a company named "... Health Inc." is not an institution
    if fed:
        return "CPC", "high", "a federal department or agency of Canada (mailbox on a Government of Canada domain)", \
               FACT["CPC"] + "; federal bodies mail letters, cheques and notices"
    if prov == "ON" and muni:
        return "MPAC", "high", "an Ontario municipality", FACT["MPAC"]
    if prov in UTIL:
        vid, skip = UTIL[prov]
        local = re.search(skip, n) or re.search(skip, norm(place))  # it may be served by a municipal or co-op utility
        if not local:
            conf = "high" if (muni or inst) and prov != "BC" else "medium" if (muni or inst or prov != "BC") else "low"
            what = "%s in %s" % ("a municipality" if muni else "an institution (school, college, university, health or government body)" if inst else "an organisation", PNAME[prov])
            why = FACT[vid] + ("; it pays electricity for the buildings and street lighting it operates" if muni else
                               "; it pays electricity for the buildings it operates" if inst else
                               "; an organisation with premises there buys its electricity from it, unless its landlord pays it through the lease")
            return vid, conf, what, why
    what = "%s located in Canada%s" % ("a municipality" if muni else "an institution (school, college, university, health or government body)" if inst else "an organisation", " (%s)" % PNAME[prov] if prov else "")
    if muni:
        return "CPC", "medium", what, FACT["CPC"] + "; municipalities mail property-tax and assessment notices"
    if inst:
        return "CPC", "medium", what, FACT["CPC"] + "; such institutions mail letters and notices"
    return "CPC", "low", what, "generic: " + FACT["CPC"] + "; most organisations mail some letters, but not every one does"
# the postal code an organisation's own home page prints (the scan, detector 5: data/incoming/claude/credit_scan/links_<stamp>.gz, 4th column
# "site name|copyright name|legalName|postal code"): the address of an organisation whose lead reader kept none. 377,262 home pages on 2026-11-11.
SCAN_PC = _BYLOC.scan_postal_codes()
print("home pages that print a Canadian postal code (the scan's name facts):", len(SCAN_PC))
# 2026-11-12: how many organisations print the same urban postal code (tools/by_location.py: SHARED_SAY, SHARED_FAIL) — over the home pages the
# scan read and, further down, this build's rows by where the organisation is; by registrable domain. A rural code stands for a whole town.
_PC_DOMS = collections.defaultdict(set)
for _h, (_pc, _day) in SCAN_PC.items():
    if _pc[1] != "0":
        _PC_DOMS[_pc].add(registrable(_h))
def scan_address(md, *sites):
    """'' or the postal code the organisation's own home page prints, as an address cell that says where it was read. The site must be the
    one the organisation's mailbox is on (same registrable domain): a directory page that printed its mailbox is not its home page."""
    if not md or FREEMAIL.match(md):
        return ""
    for h in [re.sub(r"^www\.", "", host_of(u) or "") for u in sites if u] + [md]:
        if h and registrable(h) == registrable(md) and h in SCAN_PC:
            pc, day = SCAN_PC[h]
            return "postal code %s %s (as printed on the organisation's home page https://%s/, read by the home-page scan%s)" % (pc[:3], pc[3:], h, (" of " + day) if day else "")
    return ""
def address_beside_mailbox(pc_text, quote, url):
    """a fuller address than the home page's postal code alone, when the page that prints the organisation's mailbox prints its address with that
    very postal code (test set of 2026-11-11: "postal code V9N 1H3" on a row whose mailbox quote reads "103 – 555 4th Street Courtenay, BC V9N 1H3")"""
    m = _BYLOC.PC.search((pc_text or "").upper())
    if not m or not quote:
        return ""
    pc = re.sub(r"[^A-Z0-9]", "", m.group(0))
    mq = next((q_ for q_ in _BYLOC.PC.finditer(quote.upper()) if re.sub(r"[^A-Z0-9]", "", q_.group(0)) == pc), None)
    if not mq or "<" in quote[:mq.end()][-160:]:
        return ""  # (a quote that is page source, tags and all, is not cut into an address)
    a_ = _addr_from(quote[:mq.end()]) or ""
    return ("%s (as printed beside the organisation's mailbox on %s)" % (a_, url or "its own page")) if (len(a_) >= 18 and _STREET_WORD.search(a_) and re.match(r"\d", a_)) else ""
def address_beside_mailbox_abroad(quote, url):
    """rule 18: the organisation's address abroad as the page that prints its mailbox prints it — the words up to a U.S. ZIP code of the utilities'
    states, or up to an address on an island a Caribbean utility serves whole (the strict patterns of tools/by_location.py) — when its own site's
    facts gave none; "" when the quote is page source or holds no such address"""
    q = re.sub(r"\s+", " ", quote or "")
    if not q:
        return ""
    m = _BYLOC.US_ZIP_RX.search(q)
    if not m:
        m = next((rx.search(q) for _k, rx, _n, _l in _BYLOC._CARIB if rx.search(q)), None)
    if not m or "<" in q[max(0, m.end() - 160):m.end()]:
        return ""
    a_ = re.sub(r"^\S*\s", "", q[max(0, m.end() - 120):m.end()])
    a_ = re.split(r"\S+@\S+|\||•|·|(?i:\b(?:e-?mail|phone|tel|fax)\b\s*:?)", a_)[-1].strip(" ,;:|-")  # what follows the mailbox, a separator or a label
    return ("%s (as printed beside the organisation's mailbox on %s)" % (a_, url or "its own page")) if (len(a_) >= 12 and re.search(r"\d", a_)) else ""
def city_place(texts, url):
    """(distributor, address cell) when no postal code was read and the organisation's own page names a city that one distributor serves whole
    (tools/by_location.py: biller_for_city) — the cell says the city, where it was read and that it is a city, not a street address"""
    t = " ".join(x_ for x_ in texts if x_)
    if not t or _BYLOC.fsa_of(t):
        return None, ""
    r_ = _BYLOC.biller_for_city(t)
    if not r_:
        return None, ""
    return r_[0], "%s (the city the organisation's own page prints beside its mailbox or address: “%s”, %s; no street address or postal code was read)" % (
        r_[1], re.sub(r"\s+", " ", r_[2]).strip()[:160], url or "its own page")
n_city = collections.Counter()
_PROV_OF_PC = {"A": "NL", "B": "NS", "C": "PE", "E": "NB", "G": "QC", "H": "QC", "J": "QC", "K": "ON", "L": "ON", "M": "ON", "N": "ON", "P": "ON", "R": "MB", "S": "SK", "T": "AB", "V": "BC", "Y": "YT"}
# owner 2026-11-11 16:01 EST, second step. A row whose own relationship cannot meet the rule gives way to the one biller its address has by
# law, when its own printed address names one: a service whose vendor's way of being paid is not published (hosting and software are commonly
# charged to a card, so nothing is said "by the kind" there: 13,203 such rows in the sample build of 21:45Z, none of them ship ready), a
# client listing or a link (the vendor's statement, never established), a trademark owner billed by the Office (its page names no notice or
# invoice). The other relationship stays on the row as a note (other_relationship_sources). Decided here, before the row is enriched, so
# that every cell of the row is the distributor's from the start; a service whose vendor publishes a bank payment keeps its row.
# 2026-11-12 (coord/DECISIONS.md, 2026-11-12: the address a public places dataset lists): an organisation whose mailbox the referee re-read and
# whose own pages located nothing — no postal code, no city — may stand on the address an Overture Maps place lists for its website, when all
# the domain's open places print one postal code and the place's name fits the organisation's (tools/by_location.py: directory_addresses,
# directory_cell). Its own pages always come first; every cell that uses such an address says where it comes from.
n_ovt = collections.Counter()
_ovt_need = set()
for _k, ((_acc, _g), _m) in mail.items():
    if _acc and _g >= 1 and "@" in (_m.get("mailbox") or ""):
        _ovt_need.add(registrable((_m.get("mailbox") or "").strip().lower().partition("@")[2]))
for _x in rows:
    for _d in ((_x.get("email") or "").lower().partition("@")[2], host_of(_x.get("buyer_website") or "") if _x.get("buyer_website") else ""):
        if _d:
            _ovt_need.add(registrable(_d))
OVT = _BYLOC.directory_addresses(_ovt_need)
OVT13, PLC13 = {}, {}
print("addresses an Overture Maps place lists for the website of an organisation on file (one postal code for the whole domain): %d domains of %d" % (len(OVT), len(_ovt_need)), flush=True)
del _ovt_need
_URLISH = re.compile(r"(?:https?://)?(?:www\.)?[\w.-]+\.[a-z]{2,}/?", re.I)
def _ovt_fits(name, names, dom):
    """the place's name is the organisation's: the domain's own label in the place's name (or the place's name in the label), or a distinctive
    word both names share"""
    lab = re.sub(r"[^a-z0-9]", "", norm(dom.split(".")[0]))
    ta = set() if (not name or _URLISH.fullmatch(name.strip())) else {w for w in re.findall(r"[a-z]{4,}", norm(name)) if w not in GEN_W}
    for pn in (names or "").split(" | "):
        pp = re.sub(r"[^a-z0-9]", "", norm(pn))
        if len(lab) >= 5 and (lab in pp or (len(pp) >= 5 and pp in lab)):
            return True
        if ta & {w for w in re.findall(r"[a-z]{4,}", norm(pn)) if w not in GEN_W}:
            return True
    return False
def ovt_place(name, md, site):
    """(distributor, address cell) from the address an Overture Maps place lists for the organisation's website, or (None, "")"""
    doms = [registrable(md)] if md and not FREEMAIL.match(md) else []
    if site:
        doms.append(registrable(host_of(site)))
    for d in dict.fromkeys(x_ for x_ in doms if x_):
        o = OVT.get(d)
        if not o:
            continue
        if not _ovt_fits(name, o.get("names") or "", d):
            n_ovt["… a listed address whose place's name does not fit the organisation's: not used"] += 1
            continue
        b = _BYLOC.biller_for(o["postcode"])
        if not b:
            n_ovt["… a listed address with no distributor (Alberta, an edge between two, a territory): not used"] += 1
            continue
        return b, _BYLOC.directory_cell(o)
    return None, ""
# 2026-11-13 (tools/phone_places.py): the address of the Overture Maps place that lists the organisation's own telephone number and bears its name or
# lists its website — the last way to where an organisation is, after its own pages, a registry, the city it names and the address listed for its website
PHP = _BYLOC.phone_addresses()
PHN13 = {}
print("organisations located by the place that lists their telephone number (tools/phone_places.py): %d on file" % len(PHP), flush=True)
def phone_place(k):
    o = PHP.get(k)
    if not o:
        return None, ""
    b = _BYLOC.biller_for(o["postcode"])
    if not b:
        n_ovt["… a telephone-listed address with no distributor (Alberta, an edge between two, a territory): not used"] += 1
        return None, ""
    return b, _BYLOC.phone_cell(o)
SRC_OWN = "the distributor's exclusive territory and the organisation's own printed address (no contract, payment or listing record)"
SRC_DIR = ("the distributor's exclusive territory and the address a public places dataset (Overture Maps) lists for the organisation's website "
           "(no contract, payment or listing record)")
SRC_PHONE = ("the distributor's exclusive territory and the address of the place a public places dataset (Overture Maps) lists for the organisation's own "
             "telephone number (no contract, payment or listing record)")
# 2026-11-13: the same two ways on Foursquare's open places (tools/fsq_places.py), said with their own dataset
SRC_DIR_FSQ = SRC_DIR.replace("(Overture Maps)", "(Foursquare Open Source Places)")
SRC_PHONE_FSQ = SRC_PHONE.replace("(Overture Maps)", "(Foursquare Open Source Places)")
_src_loc = lambda b_addr: (SRC_DIR if _BYLOC.DIRECTORY_MARK in b_addr else SRC_DIR_FSQ if _BYLOC.DIRECTORY_MARK_FSQ in b_addr else SRC_PHONE if _BYLOC.PHONE_MARK in b_addr
                           else SRC_PHONE_FSQ if _BYLOC.PHONE_MARK_FSQ in b_addr else SRC_OWN)
GAVE_WAY = {}
n_gw = collections.Counter()
_ROSTER13 = ("member named in the member directory", "tenant / merchant named by", "dealer / retailer named by", "sponsor / exhibitor named by")
def _svc_pay_text(x, k):
    d_ = LDET.get(k) or {}
    vd_ = registrable(host_of(d_.get("vendor_site") or x.get("vendor_website") or "") or "")
    cur_ = _BILL_CUR.get(norm(x.get("vendor") or "")) or _BILL_CUR_DOM.get(vd_)
    txt = str(((cur_ or {}).get("bill") or {}).get("payment") or "")
    if not txt and vd_ in VBILL:
        txt = str((_VB.extra_of(VBILL.get(vd_), "paymethod") or {}).get("q") or "")
    return txt
for x in rows:
    t = x.get("tier")
    # 2026-11-13: also a contract on file that is not current (awarded more than three years ago, no end date published that is still to come):
    # the owner's rule 11 — it stands no row, so the organisation stands on the distributor of its address (644 located rows were held so in the
    # table of 11:39Z); its keys need not be a lead's
    _old_c = (t == "C" and x.get("acc") and int(x.get("grade") or 0) >= 1 and "|" not in (x.get("keys") or "")
              and (x.get("award_date") or "")[:10] and (x.get("award_date") or "")[:10] < CUTOFF3 and not ((x.get("end_date") or "")[:10] >= today))
    if not _old_c and (t not in ("T", "D", "E", "M") or not x.get("acc") or int(x.get("grade") or 0) < 1 or "|" in (x.get("keys") or "") or not (x.get("keys") or "").startswith("lead:")):
        continue
    k, cs = x["keys"], x.get("contract_status") or ""
    if _old_c:
        why = "the contract on file was awarded more than three years ago and no end date still to come is published (owner's rule 11)"
    elif t == "T":
        if _RR.payment_route({"bill_payment_method_as_published": _svc_pay_text(x, k), "vendor": x.get("vendor") or ""}, "service seen on the buyer's side")[0] in _RR.ROUTE_OK:
            continue
        why = "how that vendor is paid is not published, and a service of this kind is commonly charged to a card"
    elif t == "M":
        _pe = _PAYEE.payee_for(x.get("vendor") or "", (LDET.get(k) or {}).get("vendor_site") or "")
        if "canadian intellectual property office" in (x.get("vendor") or "").lower():
            why = "the Office's own page names the ways of paying and no notice or invoice"
        elif _pe and _pe.get("no_invoice"):
            # 2026-11-13: a body that says in its own words that it sends no invoice (OMVIC: dealers self-report and remit): no row on it — the distributor of the address instead
            why = "the body says in its own words that it sends no invoice"
        elif "agent of record" in cs and _RR.agent_is_a_person({"vendor": x.get("vendor") or ""}):
            why = "the agent of record is a named person, not a firm"
        else:
            continue
    elif t == "D" and any(p_ in cs for p_ in _ROSTER13):
        continue
    else:
        why = "a client listing is the vendor's own statement" if t == "D" else "a link on the vendor's site is not shown to be a client relationship"
    n_gw["rows that cannot meet the rule (%s)" % ("contract not current" if _old_c else {"T": "service, payment not published", "M": "a register's body that bills no invoice, or an agent who is a person", "D": "client listing", "E": "link only"}[t])] += 1
    e = (x.get("email") or "").strip()
    local, _, md = e.lower().partition("@")
    if not md or BAD_LOCAL.search(local) or jur_of_mail(e) == "FED":
        n_gw["… not given: mailbox of a federal body, or not one to write to"] += 1; continue
    _lf = LFACTS.get(k) or {}
    site = x.get("buyer_website") or ""
    _sa = scan_address(md, site, _lf.get("site"))
    loc = _BYLOC.biller_for_all(" ".join([x.get("buyer_address") or "", _lf.get("address") or "", x.get("email_evidence_quote") or "", _sa.split(" (as printed")[0]]))
    _cityaddr = ""
    if not loc:
        loc, _cityaddr = city_place([x.get("buyer_address") or "", _lf.get("address_quote") or _lf.get("address") or "", x.get("email_evidence_quote") or ""], x.get("email_evidence_url") or "")
        if not loc and _lf.get("city_quote"):
            loc, _cityaddr = city_place([_lf["city_quote"]], _lf.get("city_url") or "")
        if loc:
            n_city["rows that give way, to the distributor of the city the organisation's page names"] += 1
    _ovtaddr = ""
    if not loc:
        loc, _ovtaddr = ovt_place(x.get("buyer") or "", md, site)
        if loc:
            n_ovt["rows that give way, to the distributor of the address listed for their website"] += 1
    if not loc:
        loc, _ovtaddr = phone_place(k)
        if loc:
            n_ovt["rows that give way, to the distributor of the place listing their telephone number"] += 1
    _pw_gw = ""
    if not loc and _BYLOC.POINTS:  # rule 18: a place at a territory's edge, by the point of its website's own listing
        loc, _pw_gw = _BYLOC.abroad_point(registrable(host_of(site or _lf.get("site") or "")), " ".join([x.get("buyer_address") or "", _lf.get("address") or ""]))
    if not loc:
        n_gw["… no distributor can be named for where it is (no postal code read, Alberta, or an area another utility serves)"] += 1; continue
    _abr_gw = loc if loc.get("abroad") else None  # rule 18: a utility abroad that a Canadian company owns — its own jurisdiction, where and ownership sentence
    if registrable(host_of(loc["site"])) in (registrable(md), registrable(host_of(site))):
        continue
    b_addr = x.get("buyer_address") or (lf_cell(_lf, site or "") if _lf.get("address") else "") or _sa
    if not _BYLOC.fsa_of(b_addr):
        b_addr = (b_addr + "; " if b_addr else "") + (_sa or _cityaddr or _ovtaddr or "")
    if b_addr.startswith("postal code "):
        b_addr = address_beside_mailbox(b_addr, x.get("email_evidence_quote") or "", x.get("email_evidence_url") or "") or b_addr
    if _abr_gw and not b_addr.strip(" ;"):
        b_addr = address_beside_mailbox_abroad(x.get("email_evidence_quote") or "", x.get("email_evidence_url") or "")
    g = int(x["grade"])
    prov, how = province_of(k, e, site, x.get("email_evidence_quote") or "")
    GAVE_WAY[k] = "%s — %s — is on file for this organisation and is not what the row stands on: %s" % ((x.get("vendor") or "").strip(), re.sub(r"\s+", " ", cs)[:260].rstrip(" .,;:"), why)
    new = {"jurisdiction": "", "_jur": (_abr_gw["jur"] if _abr_gw else None) or prov or _PROV_OF_PC.get((_BYLOC.fsa_of(b_addr) or " ")[0]) or "CA", "rank_group": "I%d" % g, "completeness_score": 3 * 10 + g * 6 + 3,
           "buyer": x.get("buyer") or "", "buyer_website": site, "buyer_address": b_addr,
           "email": e, "email_type": x.get("email_type") or "", "email_check": "confirmed", "email_evidence_url": x.get("email_evidence_url") or "", "email_evidence_quote": x.get("email_evidence_quote") or "",
           "contract_status": (_BYLOC.status(loc, _BYLOC.abroad_where(b_addr)[1] or _BYLOC.abroad_where(x.get("email_evidence_quote") or "")[1] or _pw_gw or "its printed address") if _abr_gw else
                               _BYLOC.status(loc, _BYLOC.fsa_of(b_addr) or _BYLOC.fsa_of(x.get("email_evidence_quote") or "") or ((_BYLOC.biller_for_city(b_addr) or ("", "the city it prints"))[1]))),
           "source": _src_loc(b_addr),
           "vendor": "inferred: " + loc["name"], "vendor_address": loc["address"], "vendor_website": loc["site"],
           "vendor_country_basis": (_BYLOC.ownership_sentence(loc) if _abr_gw else "%s, %s: '%s'" % (loc.get("address_source") or "the vendor's own site", loc["address_url"], loc["address_quote"])),
           "contracts_with_canadian_suppliers": 0, "buyer_keys": 1, "keys": k, "tier": "I", "grade": g, "acc": True}
    x.clear(); x.update(new)
    n_gw["… given to the distributor of the organisation's address: %s" % loc["name"]] += 1
    if _abr_gw:
        n_ovt["rows by where the organisation is abroad — a utility a Canadian company owns (rule 18), given way to: %s" % loc["key"]] += 1
print("rows that give way to the biller their address has by law:", dict(sorted(n_gw.items(), key=lambda kv: -kv[1])))
SPC13 = {}
CITY13 = {}  # 2026-11-12: the city an organisation's own page names, when no postal code was read (rank: P13 by where it is)
PNT13 = {}  # 2026-11-13 (rule 18): a place at a territory's edge located by the point of its website's own listing (tools/by_location.py abroad_point)
cands = []
skipped13 = collections.Counter()
for k, ((acc, g), m) in mail.items():
    if not acc or g < 1 or k in covered_keys or (_SN and not _in_sample(k)):
        continue
    if _PN > 1 and _part_of.get(k, 0) != _PI:
        continue  # ranking in parts: an inferred row is made in the part of its organisation
    # owner 2026-11-11 16:01 EST ("think differently … invoice, bank EFT, email, Canadian vendor … populate those fields as best as you can"):
    # where the organisation is, as its own site prints it, names the one body that bills electricity there (tools/by_location.py)
    _lf13 = LFACTS.get(k) or {}
    _sa13 = scan_address((m.get("mailbox") or "").strip().lower().partition("@")[2], (VEN.get(k) or {}).get("website"), (BUY.get(k) or {}).get("official_website"),
                         leads[k].get("website") if k in leads else "", _lf13.get("site"), m.get("evidence_url"))
    _loc13 = _BYLOC.biller_for_all(" ".join([_lf13.get("address") or "", addr_text((BUY.get(k) or {}).get("address")), (VEN.get(k) or {}).get("address") or "", m.get("evidence_quote") or "",
                                             _sa13.split(" (as printed")[0]]))
    if _sa13 and _loc13:
        SPC13[k] = _sa13
    if not _loc13 and k in PLACES:
        # 2026-11-12: its registered address in a public registry (the CRA List of charities, a provincial school directory) — an entry on a
        # public register, filed by the organisation itself; it was on the row but never used to name the distributor
        _loc13 = _BYLOC.biller_for_all(place_cell(k).split(" (its registered")[0])
        if _loc13:
            PLC13[k] = place_cell(k); n_ovt["inferred rows by the organisation's registered address in a public registry"] += 1
    if not _loc13 and _BYLOC.POINTS:
        _d13 = registrable(host_of(_lf13.get("site") or (leads[k].get("website") if k in leads else "") or ""))
        _pb13, _pw13 = _BYLOC.abroad_point(_d13, " ".join([_lf13.get("address") or "", m.get("evidence_quote") or ""]))
        if _pb13:
            _loc13 = _pb13; PNT13[k] = _pw13
    if not _loc13:
        _loc13, _ca13 = city_place([_lf13.get("address_quote") or _lf13.get("address") or "", addr_text((BUY.get(k) or {}).get("address")), m.get("evidence_quote") or ""], m.get("evidence_url") or "")
        if not _loc13 and _lf13.get("city_quote"):
            _loc13, _ca13 = city_place([_lf13["city_quote"]], _lf13.get("city_url") or "")
        if _loc13:
            CITY13[k] = _ca13
    if not _loc13:
        _nm13 = (VEN.get(k) or {}).get("name") or (BUY.get(k) or {}).get("canonical_name") or (BUY.get(k) or {}).get("name") or \
                (leads[k].get("buyer_name") if k in leads else "") or (m.get("org_name") or "")
        _st13 = (VEN.get(k) or {}).get("website") or (BUY.get(k) or {}).get("official_website") or (leads[k].get("website") if k in leads else "") or _lf13.get("site") or ""
        _loc13, _oa13 = ovt_place(_nm13, (m.get("mailbox") or "").strip().lower().partition("@")[2], _st13)
        if _loc13:
            OVT13[k] = _oa13
    if not _loc13:
        _loc13, _pa13 = phone_place(k)
        if _loc13:
            PHN13[k] = _pa13
    if k.startswith("lead:") and not REGISTRY_ROWS and not _loc13:
        # 2026-11-11: an organisation that came through a lane (its key was minted by a lead engine) and whose lead is withdrawn, or removed by
        # the owner's rule of that day (a .ca registration, a store, a card-billed service), gets no inferred row in its place. Without this
        # the 100,000 organisations of the .ca pool came back as "inferred: Canada Post Corporation" (sample build of 19:15Z: 41,634 inferred
        # rows of 77,953). They stay on file as the pool the register lanes are matched against.
        skipped13["known only through a lead that is withdrawn or removed (owner 2026-11-11: no inferred row in its place)"] += 1; continue
    e = (m.get("mailbox") or "").strip()
    local, _, md = e.lower().partition("@")
    if not md or BAD_LOCAL.search(local):
        skipped13["bad mailbox"] += 1; continue
    found = (m.get("org_name") or "").strip()  # the name the agent wrote next to the mailbox; the key's own name decides identity
    ident = (VEN.get(k) or {}).get("name") or (BUY.get(k) or {}).get("canonical_name") or (BUY.get(k) or {}).get("name") or \
            (leads[k].get("buyer_name") if k in leads else "") or found
    name = found if (re.fullmatch(r"(https?://)?[\w.-]+\.[a-z]{2,}/?", ident.strip(), re.I) and found and not re.match(r"https?://|www\.", found, re.I)) else ident
    eh = host_of(m.get("evidence_url") or "")
    site = (VEN.get(k) or {}).get("website") or (BUY.get(k) or {}).get("official_website") or \
           (leads[k].get("website") if k in leads else "") or ("https://" + eh if eh else "")
    if not same_org(e, site or "https://unknown.invalid", ident):
        skipped13["mailbox not the organisation's own"] += 1; continue
    _real_site = (VEN.get(k) or {}).get("website") or (BUY.get(k) or {}).get("official_website") or (leads[k].get("website") if k in leads else "")
    if not mail_page_own(e, m.get("evidence_url") or "", _real_site or ("https://" + md), ident, m.get("evidence_quote") or ""):
        skipped13["mailbox read on another organisation's page (a directory, a regional body's, a partner's), not on its own"] += 1; continue
    fed = jur_of_mail(e) == "FED" and not k.startswith("v:")
    prov, how = province_of(k, e, site, m.get("evidence_quote") or "")
    country = "CA" if (k.split(":")[0] in ("osm", "wd", "v") or k in PLACES or prov or fed or md.endswith(".ca") or host_of(site).endswith(".ca")
                       or (BUY.get(k) or {}).get("country") == "CA" or _loc13) else ""  # _loc13: its own page prints a Canadian postal code
    if not country:
        skipped13["not located in Canada (no honest inference)"] += 1; continue
    if site and not (VEN.get(k) or {}).get("website") and not (BUY.get(k) or {}).get("official_website") and not (k in leads and leads[k].get("website")) \
            and registrable(host_of(site)) != registrable(md) and not FREEMAIL.match(md):
        site = "https://" + md  # the page was a directory or partner page: the organisation's own domain is its mailbox's
    place = " ".join([(m.get("evidence_quote") or ""), addr_text((BUY.get(k) or {}).get("address")), (VEN.get(k) or {}).get("address") or "",
                      (PLACES.get(k) or {}).get("city") or ""])
    vid, conf, what, why = infer(name, e, site, prov, fed, place)
    if _loc13 and not fed:
        vid, conf, what, why = "LOC:" + _loc13["key"], "high", "an organisation whose own printed address lies in the distributor's territory", _loc13["territory"]
        INFV.setdefault(vid, (_loc13["name"], _loc13["site"], _loc13["address"], _loc13["address_url"], _loc13["address_quote"]))
    elif vid == "CPC" and not fed:
        # a letter carrier is not a body that sends this organisation an invoice: no row is made on it any more (25,785 such rows on 2026-11-11)
        skipped13["no biller can be named for where it is (no postal code on its own page, Alberta, or an area another utility serves)"] += 1; continue
    if registrable(host_of(INFV[vid][1])) in (registrable(md), registrable(host_of(site))):
        skipped13["is the inferred vendor itself"] += 1; continue
    dom = registrable(host_of(site)) if site else ("" if FREEMAIL.match(md) else registrable(md))
    cands.append(({"high": 3, "medium": 2, "low": 1}[conf], g, k, e, name, site, dom, prov, how, vid, conf, what, why, m))
cands.sort(key=lambda c: (-c[0], -c[1], c[2]))
n13 = 0
# 2026-11-10: an organisation the org universe already knew (registry / OSM / Wikidata / places key) that now has a relationship row from a
# lead (cloud row factory: 451 such rows in the first build) keeps the lead's relationship AND takes the organisation's key, so every fact
# held under that key (registered name, BN, postal address, phone …) still attaches to the row. Same registrable website domain, names fit.
lead_row_by_dom = {}
for x in rows:
    if (x.get("keys") or "").startswith("lead:") and "|" not in (x.get("keys") or "") and x.get("buyer_website"):
        _d = registrable(host_of(x["buyer_website"]))
        if _d:
            lead_row_by_dom[_d] = None if _d in lead_row_by_dom else x  # two lead rows on one domain: never guess
n_keyjoin = collections.Counter()
for sc, g, k, e, name, site, dom, prov, how, vid, conf, what, why, m in cands:
    if e.lower() in covered_mail or (dom and dom in covered_dom) or norm(name) in covered_name:
        _lr = lead_row_by_dom.get(dom) if dom else None
        if _lr is not None and not k.startswith("lead:") and k not in _lr["keys"].split("|") and name_fits(_lr.get("buyer") or "", name):
            _lr["keys"] += "|" + k; _lr["buyer_keys"] = int(_lr.get("buyer_keys") or 1) + 1; n_keyjoin["rows"] += 1
            _ba = addr_text((BUY.get(k) or {}).get("address")) or (VEN.get(k) or {}).get("address") or place_cell(k)
            if _ba and not _lr.get("buyer_address"):
                _lr["buyer_address"] = _ba; n_keyjoin["buyer_address"] += 1
            if name and re.fullmatch(r"(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}", (_lr.get("buyer") or "").lower()) and not re.fullmatch(r"(https?://)?[\w.-]+\.[a-z]{2,}/?", name.strip(), re.I):
                _lr["buyer"] = name; n_keyjoin["buyer_name"] += 1  # the lead only carried the domain
        skipped13["same organisation already in a row (domain / mailbox / name)"] += 1
        if not (e.lower() in covered_mail or (dom and dom in covered_dom)):
            skipped13["… of which by the NAME alone (its own mailbox and domain are in no row)"] += 1
        continue
    covered_mail.add(e.lower()); covered_name.add(norm(name)); covered_keys.add(k)
    if dom:
        covered_dom.add(dom)
    vname, vsite, vaddr, vurl, vquote = INFV[vid]
    LABEL = {4: "invoicing/AP", 3: "finance/accounting dept or supplier-payment office", 2: "purchasing", 1: "general"}
    b_addr = addr_text((BUY.get(k) or {}).get("address")) or (VEN.get(k) or {}).get("address") or place_cell(k)
    _lf = LFACTS.get(k) or {}
    if not b_addr and _lf.get("address"):
        b_addr = lf_cell(_lf, site or "")
    if vid.startswith("LOC:") and not _BYLOC.fsa_of(b_addr) and SPC13.get(k):
        b_addr = (b_addr + "; " if b_addr else "") + SPC13[k]  # no postal code in what was read of its address: the one its home page prints
    elif vid.startswith("LOC:") and not _BYLOC.fsa_of(b_addr) and PLC13.get(k):
        b_addr = (b_addr + "; " if b_addr and PLC13[k] not in b_addr else "") + (PLC13[k] if PLC13[k] not in b_addr else b_addr)
    elif vid.startswith("LOC:") and not _BYLOC.fsa_of(b_addr) and CITY13.get(k):
        b_addr = (b_addr + "; " if b_addr else "") + CITY13[k]; n_city["inferred rows by the city the organisation's page names"] += 1
    elif vid.startswith("LOC:") and not _BYLOC.fsa_of(b_addr) and OVT13.get(k):
        b_addr = (b_addr + "; " if b_addr else "") + OVT13[k]; n_ovt["inferred rows by the address listed for the organisation's website"] += 1
    elif vid.startswith("LOC:") and not _BYLOC.fsa_of(b_addr) and PHN13.get(k):
        b_addr = (b_addr + "; " if b_addr else "") + PHN13[k]; n_ovt["inferred rows by the place listing the organisation's telephone number"] += 1
    if b_addr.startswith("postal code "):
        b_addr = address_beside_mailbox(b_addr, m.get("evidence_quote") or "", m.get("evidence_url") or "") or b_addr
    if _lf.get("site_name") and re.fullmatch(r"(?:https?://)?(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}/?", (name or "").strip().lower()):
        name = _lf["site_name"]  # the lead only carried the domain: the organisation's own home page names it (as apply_details does for a lead's row)
    _abr = _BYLOC.BY_KEY.get(vid[4:]) if vid.startswith("LOC:") else None
    _abr = _abr if (_abr or {}).get("abroad") else None  # rule 18: a utility abroad that a Canadian company owns
    if _abr and not b_addr:
        b_addr = address_beside_mailbox_abroad(m.get("evidence_quote") or "", m.get("evidence_url") or "")
    rows.append({"jurisdiction": "", "_jur": (_abr["jur"] if _abr else None) or prov or (_PROV_OF_PC.get((_BYLOC.fsa_of(b_addr) or " ")[0]) if vid.startswith("LOC:") else "") or "CA", "rank_group": "I%d" % g, "completeness_score": sc * 10 + g * 6 + 3,
        "buyer": name, "buyer_website": site, "buyer_address": b_addr,
        "email": e, "email_type": LABEL[g], "email_check": "confirmed", "email_evidence_url": m.get("evidence_url") or "", "email_evidence_quote": m.get("evidence_quote") or "",
        "contract_status": (_BYLOC.status(_abr, _BYLOC.abroad_where(b_addr)[1] or _BYLOC.abroad_where(m.get("evidence_quote") or "")[1] or PNT13.get(k, "")) if _abr else
                            _BYLOC.status(_BYLOC.BY_KEY[vid[4:]], _BYLOC.fsa_of(b_addr) or _BYLOC.fsa_of(m.get("evidence_quote") or "") or ((_BYLOC.biller_for_city(b_addr) or ("", "the city it prints"))[1])) if vid.startswith("LOC:") else
                            "inferred relationship (no record): %s confidence; the buyer is %s%s; %s" % (conf, what, (" (province from %s)" % how) if how else "", why)),
        "source": (_src_loc(b_addr) if vid.startswith("LOC:") else
                   "inference from the buyer's type and province (no contract, payment or listing record)"),
        "vendor": "inferred: " + vname, "vendor_address": vaddr, "vendor_website": vsite,
        "vendor_country_basis": _BYLOC.ownership_sentence(_abr) if _abr else "%s, %s: '%s'" % ((_BYLOC.BY_KEY[vid[4:]].get("address_source") if vid.startswith("LOC:") else "") or "the vendor's own site", vurl, vquote),
        "contracts_with_canadian_suppliers": 0, "buyer_keys": 1, "keys": k, "tier": "I", "grade": g, "acc": True})
    n13 += 1
    if _abr:
        n_ovt["rows by where the organisation is abroad — a utility a Canadian company owns (rule 18): %s" % _abr["key"]] += 1
        if PNT13.get(k):
            n_ovt["… of which located by the point of its website's listing (a ZIP code area at the territory's edge)"] += 1
print("P12 organisations:", len(orgs12), "added:", n12, dict(skipped12), "| P13 added:", n13, "| P13 skipped:", dict(skipped13))
print("by the city the organisation's own page names (no postal code read; tools/by_location.py biller_for_city):", dict(n_city))
print("by the address an Overture Maps place lists for the organisation's website (nothing on its own pages located it; tools/by_location.py directory_cell):",
      dict(n_ovt))
print("lead rows that took the organisation's own key (registry facts attach):", dict(n_keyjoin))
_free(globals(), "VEN", "VEN_NAME", "VEN_DOM", "BUY", "TEAMV", "mail", "MAIL_ALL", "mail_dom", "cands", "orgs12", "up_t", "dom_rows", "lead_row_by_dom",
      "covered_keys", "covered_dom", "covered_name", "covered_mail", "seen_dom", "SCAN_PC", "SPC13", "CITY13", "OVT13", "PLC13", "PHN13", "PNT13")  # last used by the row builders above (OVT: by the last address fill)
# ---- 2026-11-13: Ontario's broader public sector reports its own electricity (tools/bps_energy.py) ----------------------------------------------
# Owner 13:20 EST: "have your estimate as precise and specific to relationship as possible add as much over 5000 as possible". A municipality,
# school board, university, college or public hospital of Ontario reports under O. Reg. 25/23 the electricity each of its facilities bought
# from the grid, and the regulation asks for a facility's report only where the body "is issued the invoices and is responsible for making the
# payments" (s. 6 (1)). The bill of the distributor of those facilities is then a record, and its amount is calculated from the body's own use.
# A row of such a body that stands on where it is takes that record (the distributor with the largest of its bills). A row that stands on
# anything else gives way to it when it carries no published amount of $5,000 or more and the record's bill is $5,000 a month or more (rule
# 15: published $5,000+, then estimated $5,000+); the relationship it stood on is kept in sight (other_relationship_sources).
import bps_energy as _BPSE
BPS = _BPSE.load()
_BPS_IX = _BPSE.index(BPS["orgs"]) if BPS.get("orgs") else None
n_bps = collections.Counter()
_BPS_NUM = re.compile(r"\s*(?:C|CA|US|CAD|USD)?\$?\s?(\d[\d,]*(?:\.\d+)?)")
def _bps_published_5k(x):
    for c_ in ("contract_value", "bill_amount_indicative"):
        m_ = _BPS_NUM.match(str(x.get(c_) or ""))
        if m_:
            try:
                if float(m_.group(1).replace(",", "")) >= 5000:
                    return True
            except ValueError:
                pass
    return False
def _bps_vendor(loc):
    return {"vendor": "inferred: " + loc["name"], "vendor_address": loc["address"], "vendor_website": loc["site"],
            "vendor_country_basis": "%s, %s: '%s'" % (loc.get("address_source") or "the vendor's own site", loc["address_url"], loc["address_quote"])}
def _bps_status(org, gk):
    d_, g_ = BPS["orgs"][org], BPS["orgs"][org]["groups"][gk]
    return ("electricity account of its own facilities — %s reports, under Ontario's O. Reg. 25/23, the electricity bought from the grid by %d of its facilities in the "
            "territory of %s (%s kWh in %s), and the regulation asks for a facility's report only where the body is issued the invoices for its energy"
            % (org, g_["n"], g_["distributor"], format(g_["kwh"], ","), d_["year"]))
def _bps_round(v):
    return format(int(round(v, -3 if v >= 100000 else -2 if v >= 10000 else -1)), ",")
def _bps_cells(x):
    """the cells of a row that stands on a body's own energy report: the record, what is billed, and the bill calculated from the body's own use"""
    org, gk = x["_bps"]
    d_, M = BPS["orgs"][org], BPS["meta"]
    g_ = d_["groups"][gk]
    places = ", ".join(g_["places"][:6]) + (" …" if len(g_["places"]) > 6 else "")
    cityw = {"Toronto": "the lower of the two average prices Hydro-Québec computed for Toronto (Toronto Hydro's city)",
             "Ottawa": "the lower of the two average prices Hydro-Québec computed for Ottawa (Hydro Ottawa's city)"}.get(
                 g_["city"], "the lowest of the four average prices Hydro-Québec computed for Ottawa and Toronto (the two Ontario cities of its comparison)")
    hq = "; ".join("“%s”" % M["hq_lines"][c_] for c_ in (("Toronto",) if g_["city"] == "Toronto" else ("Ottawa",) if g_["city"] == "Ottawa" else ("Ottawa", "Toronto")))
    parts = []
    if g_["n_small"] and g_.get("small_rate"):
        parts.append("the %d using under %s kWh a month at %s's own small-business rates in the Ontario Energy Board's file of current rates (fixed charges $%.2f + %.2f ¢ a kWh; %s)"
                     % (g_["n_small"], format(M["small_kwh"], ","), g_["distributor"], g_["small_rate"][0], g_["small_rate"][1], M["oeb_file"]))
    if g_.get("n_small_hq"):
        parts.append("the %d using under %s kWh a month at %s at its smallest business level (10,000 kWh a month; %s's own small-business rates are not in the "
                     "Ontario Energy Board's file as read)" % (g_["n_small_hq"], format(M["small_kwh"], ","), cityw, g_["distributor"]))
    if g_["n_large"]:
        parts.append("the %d larger at %s at the consumption levels of its table on either side of each one's use "
                     "(%s; ¢ a kWh at 1,000 / 10,000 / 100,000 / 400,000 / 1,170,000 / 3,060,000 / 30,600,000 kWh a month, excluding taxes: %s; %s)" % (g_["n_large"], cityw, M["hq_title"], hq, M["hq_pdf"]))
    lo = d_.get("left_out") or {}
    left = ("; left out of the sum (the report's own figures): %s" % ", ".join("%d %s" % (v_, ("facility" if v_ == 1 else "facilities") + {"use implausible for the floor area": " whose reported use is implausible for its floor area",
                                                                                   "same kilowatt-hours as another of its facilities": " reporting the very same kilowatt-hours as another",
                                                                                   "postal code names no distributor": " whose postal code names no single distributor"}.get(k_, " (" + k_ + ")")) for k_, v_ in sorted(lo.items()))) if lo else ""
    return {
        "relationship_kind": "electricity account of the body's own facilities: the distributor of their addresses bills the body for each of them (its own energy report under Ontario's O. Reg. 25/23)",
        "relationship_fact_basis": ("fact, public record: %s's own energy report for %s (Ontario Broader Public Sector energy reporting, open data of the Ministry of Energy and Mines: %s) lists "
                                    "%d of its facilities in the territory of %s, each by its address, with %s kWh of electricity bought from the grid; a facility's report “%s” "
                                    "(O. Reg. 25/23, s. 6 (1): %s) — the dataset's page: “%s”; it adds: “%s” (%s). The distributor of a facility is the one the Ontario Energy Board "
                                    "licenses for the service area of its postal code" % (org, d_["year"], d_["url"], g_["n"], g_["distributor"], format(g_["kwh"], ","),
                                                                                         M["regulation_quote"], M["regulation"], M["dataset_quote"],
                                                                                         M.get("dataset_quote_voluntary") or "", M["dataset_page"])),
        "contract_title": "Electricity service to %d facilities of %s in the territory of %s (%s)" % (g_["n"], org, g_["distributor"], places),
        "bill_items_as_published": "electricity delivered to the body's %d reported facilities in this distributor's territory (%s)" % (g_["n"], places),
        "bill_amount_calculated": ("estimated — about $%s a month before tax, from the body's own reported use: %s reported %s kWh of electricity bought from the grid in %s by these %d facilities "
                                   "(about %s kWh a month; %s data set: %s); each facility's monthly use is priced — %s; the amount is the sum of what each facility's use comes to in a month%s"
                                   % (_bps_round(g_["month"]), org, format(g_["kwh"], ","), d_["year"], g_["n"], format(int(round(g_["kwh"] / 12.0)), ","), d_["year"], d_["url"], "; ".join(parts), left)),
        "invoice_reference_hint": "the account number of each facility, printed on the distributor's bills (not public)",
        "source": "the body's own energy report, Ontario Broader Public Sector energy reporting under O. Reg. 25/23 (open data, Ministry of Energy and Mines, %s data set)" % d_["year"],
        "how_relationship_was_found": ("tools/bps_energy.py read the Ontario Ministry of Energy and Mines' open data of the broader public sector's energy reports (the %s data set) and named "
                                       "the distributor of each facility's postal code (tools/by_location.py: the Ontario Energy Board's map of service areas); the body's row was matched to "
                                       "its report by name and address" % d_["year"]),
        "contract_status": _bps_status(org, gk)}
if _BPS_IX:
    _bps_of = {}
    for _i, x in enumerate(rows):
        _m = _BPSE.match(_BPS_IX, x.get("buyer") or "", x.get("buyer_address") or "", x.get("_jur") or x.get("jurisdiction") or "", x.get("email") or "")
        if _m:
            _bps_of[_i] = _m[0]
    _org_5k = {o_ for i_, o_ in _bps_of.items() if rows[i_].get("tier") != "I" and _bps_published_5k(rows[i_])}  # a body with a published $5,000+ record keeps it
    for _i, x in enumerate(rows):
        if _i not in _bps_of:
            continue
        _org = _bps_of[_i]
        _dir = BPS["orgs"][_org].get("directory") or {}
        _diraddr = ("%s, %s, ON %s %s (its address in %s)" % (_dir["address"], _dir.get("city") or "", _dir["postal_code"][:3], _dir["postal_code"][3:], _dir.get("source") or "a directory of the Province of Ontario")
                    if _dir.get("address") and len(_dir.get("postal_code") or "") == 6 else "")
        _gs = BPS["orgs"][_org]["groups"]
        _gk = max(_gs, key=lambda k_: _gs[k_]["month"])
        _loc = _BYLOC.BY_KEY.get(_gk)
        if not _loc:
            continue
        n_bps["rows of a body that reports its electricity under O. Reg. 25/23"] += 1
        if x.get("tier") == "I":
            if re.sub(r"^inferred:\s*", "", x.get("vendor") or "") != _loc["name"]:
                x.update(_bps_vendor(_loc)); n_bps["… standing on where it is, moved to the distributor of the largest of its reported bills"] += 1
            x["contract_status"] = _bps_status(_org, _gk)
            x["_bps"] = (_org, _gk)
            if _diraddr and not _BYLOC.code_of(x.get("buyer_address") or ""):
                x["buyer_address"] = _diraddr; n_bps["… its address from the province's directory (none with a postal code on the row)"] += 1
            n_bps["… standing on where it is: now on the record of its own report"] += 1
            continue
        if _bps_published_5k(x):
            n_bps["… kept on its record: it carries a published amount of $5,000 or more"] += 1; continue
        if _org in _org_5k:
            n_bps["… kept on its record: another row of the body carries a published amount of $5,000 or more (one row per buyer)"] += 1; continue
        if _gs[_gk]["month"] < 5000:
            n_bps["… kept on its record: the bill its report gives is under $5,000 a month"] += 1; continue
        _e = (x.get("email") or "").strip()
        _lo, _, _md = _e.lower().partition("@")
        if not x.get("acc") or int(x.get("grade") or 0) < 1 or not _md or BAD_LOCAL.search(_lo) or jur_of_mail(_e) == "FED":
            n_bps["… kept on its record: no mailbox to write to on the row"] += 1; continue
        _was = "%s — %s — is on file for this organisation and is not what the row stands on: it carries no published amount of $5,000 or more, and the body's own energy report gives a larger bill" % (
            (x.get("vendor") or "").strip(), re.sub(r"\s+", " ", x.get("contract_status") or x.get("contract_title") or "a record")[:260].rstrip(" .,;:"))
        for _k in (x.get("keys") or "").split("|"):
            if _k:
                GAVE_WAY[_k] = _was
        _g = int(x.get("grade") or 1)
        _new = {"_jur": "ON", "rank_group": "I%d" % _g, "completeness_score": 3 * 10 + _g * 6 + 3,
                "buyer": x.get("buyer") or "", "buyer_website": x.get("buyer_website") or "", "buyer_address": x.get("buyer_address") or "",
                "email": _e, "email_type": x.get("email_type") or "", "email_check": x.get("email_check") or "confirmed",
                "email_evidence_url": x.get("email_evidence_url") or "", "email_evidence_quote": x.get("email_evidence_quote") or "",
                "contract_status": _bps_status(_org, _gk), "source": "the body's own energy report, Ontario Broader Public Sector energy reporting under O. Reg. 25/23 (open data, Ministry of Energy and Mines)",
                "contracts_with_canadian_suppliers": x.get("contracts_with_canadian_suppliers") or 0, "buyer_keys": x.get("buyer_keys") or 1, "keys": x.get("keys") or "",
                "tier": "I", "grade": _g, "acc": True, "_bps": (_org, _gk)}
        _new.update(_bps_vendor(_loc))
        if _diraddr and not _BYLOC.code_of(_new["buyer_address"]):
            _new["buyer_address"] = _diraddr; n_bps["… its address from the province's directory (none with a postal code on the row)"] += 1
        for _c in list(x.keys()):
            if not _c.startswith("_") and _c not in _new and _c != "jurisdiction":
                x[_c] = ""  # every column stays (the first row names the columns), the record's own cells go
        x.update(_new)
        n_bps["… given way to its own energy report (no published $5,000 or more on the row; the report's bill is $5,000 a month or more)"] += 1
    print("Ontario bodies that report their electricity (tools/bps_energy.py; %d bodies in the reports):" % len(BPS["orgs"]), dict(n_bps))
# 2026-11-13 (owner 13:20 EST: "have your estimate as precise and specific to relationship as possible add as much over 5000 as possible"): a municipality
# outside Ontario that stands on where it is (the distributor of its town hall's address) is billed by that distributor for each of its facilities; its bill
# is estimated from its own residents (Statistics Canada, 2021 Census) and the kWh a resident of the Ontario municipalities of its size report under
# O. Reg. 25/23 (tools/muni_energy.py) — not at a small office's 2,500 kWh. A municipality's record row that carries no published amount of $5,000 or more
# gives way to it when the estimate at the lower quartile is $5,000 a month or more, as a body's row gives way to its own energy report above.
import muni_energy as _MUNI
n_muni = collections.Counter()
if _MUNI.load():
    _MUNI_MAIN = {p_: d_ for p_, (c_, d_) in _MUNI.CITY.items()}
    def _muni_prov(x):
        pc_ = _BYLOC.code_of(x.get("buyer_address") or "")
        if pc_:
            return _BYLOC._PROV_OF_FIRST.get(pc_[0], "")
        j_ = (x.get("_jur") or x.get("jurisdiction") or "")[:2]
        return j_ if j_ in _MUNI_MAIN else ""
    _muni_of = {}
    for _i, x in enumerate(rows):
        if x.get("_bps"):
            continue
        _pv = _muni_prov(x)
        if _pv not in _MUNI_MAIN:
            continue
        _mm = _MUNI.match(x.get("buyer") or "", _pv, x.get("buyer_website") or "")
        if _mm:
            _ee = _MUNI.estimate(_mm["pop"], _pv)
            if _ee:
                _muni_of[_i] = (_mm, _ee, _pv)
    _muni_5k = {m_[0]["code"] for i_, m_ in _muni_of.items() if rows[i_].get("tier") != "I" and _bps_published_5k(rows[i_])}
    for _i, (_mm, _ee, _pv) in _muni_of.items():
        x = rows[_i]
        n_muni["rows of a municipality matched to its census subdivision (outside Ontario)"] += 1
        if x.get("tier") == "I":
            if re.sub(r"^inferred:\s*", "", x.get("vendor") or "") != _MUNI_MAIN[_pv]:
                n_muni["… standing on where it is, but not on the province's main distributor: left as it is"] += 1; continue
            x["_muni"] = (_mm, _ee, _pv)
            n_muni["… standing on where it is: the bill estimated from its residents" + (" ($5,000 a month or more at the lower quartile)" if _ee["p25"] >= 5000 else "")] += 1
            continue
        if _bps_published_5k(x):
            n_muni["… kept on its record: it carries a published amount of $5,000 or more"] += 1; continue
        if _mm["code"] in _muni_5k:
            n_muni["… kept on its record: another row of the municipality carries a published amount of $5,000 or more"] += 1; continue
        if _ee["p25"] < 5000:
            n_muni["… kept on its record: the estimate at the lower quartile is under $5,000 a month"] += 1; continue
        _loc = _BYLOC.biller_for(x.get("buyer_address") or "")
        if not _loc or _loc.get("name") != _MUNI_MAIN[_pv]:
            n_muni["… kept on its record: its printed address names no distributor, or another than the province's main one"] += 1; continue
        _e = (x.get("email") or "").strip()
        _lo, _, _md = _e.lower().partition("@")
        if not x.get("acc") or int(x.get("grade") or 0) < 1 or not _md or BAD_LOCAL.search(_lo) or jur_of_mail(_e) == "FED":
            n_muni["… kept on its record: no mailbox to write to on the row"] += 1; continue
        _was = "%s — %s — is on file for this organisation and is not what the row stands on: it carries no published amount of $5,000 or more, and the municipality's electricity, estimated from its residents, comes to more" % (
            (x.get("vendor") or "").strip(), re.sub(r"\s+", " ", x.get("contract_status") or x.get("contract_title") or "a record")[:260].rstrip(" .,;:"))
        for _k in (x.get("keys") or "").split("|"):
            if _k:
                GAVE_WAY[_k] = _was
        _g = int(x.get("grade") or 1)
        _new = {"_jur": _pv, "rank_group": "I%d" % _g, "completeness_score": 3 * 10 + _g * 6 + 2,
                "buyer": x.get("buyer") or "", "buyer_website": x.get("buyer_website") or "", "buyer_address": x.get("buyer_address") or "",
                "email": _e, "email_type": x.get("email_type") or "", "email_check": x.get("email_check") or "confirmed",
                "email_evidence_url": x.get("email_evidence_url") or "", "email_evidence_quote": x.get("email_evidence_quote") or "",
                "contract_status": _BYLOC.status(_loc, _BYLOC.fsa_of(x.get("buyer_address") or "")),
                "source": "the electricity distributor of the municipality's own address (tools/by_location.py), its bill estimated from its residents (tools/muni_energy.py)",
                "contracts_with_canadian_suppliers": x.get("contracts_with_canadian_suppliers") or 0, "buyer_keys": x.get("buyer_keys") or 1, "keys": x.get("keys") or "",
                "tier": "I", "grade": _g, "acc": True, "_muni": (_mm, _ee, _pv)}
        _new.update(_bps_vendor(_loc))
        for _c in list(x.keys()):
            if not _c.startswith("_") and _c not in _new and _c != "jurisdiction":
                x[_c] = ""
        x.update(_new)
        n_muni["… given way to its electricity (no published $5,000 or more on the row; the estimate at the lower quartile is $5,000 a month or more)"] += 1
print("municipalities outside Ontario, their electricity from their residents (tools/muni_energy.py):", dict(n_muni))
os.makedirs(ROOT + "/out/ranked", exist_ok=True)
cols = [c for c in rows[0].keys() if not c.startswith("_")]
rows.sort(key=lambda x: (x["tier"] in ("F", "I") and not x.get("_bps"), x["tier"] == "I" and not x.get("_bps"), x["rank_group"] != "GOLD", -x["completeness_score"]))  # P12 / P13 never displace a stronger row; a body's own energy report (O. Reg. 25/23) is a record
# one row per body: two spellings of one name ("MRC Charlevoix" / "MRC  de Charlevoix") that share a buyer key within the
# same government are one buyer; the best-ranked row stands for it and carries all its keys
seen, seen_any, merged = {}, {}, []  # seen_any: the first row registered under a key in ANY jurisdiction (2026-11-10: the scan of `seen` for every
for x in rows:                      # row without a jurisdiction was quadratic — 5 minutes at 80,000 rows, hours at a million; same result by a lookup)
    ks = [k for k in (x.get("keys") or "").split("|") if k]
    j = x.get("jurisdiction") or ""
    hit = next((seen.get((k, j)) or seen.get((k, "")) for k in ks if (k, j) in seen or (k, "") in seen), None)
    if hit is None and not x.get("jurisdiction"):
        hit = next((seen_any[k] for k in ks if k in seen_any), None)
    if hit is not None:
        allk = sorted(set((hit.get("keys") or "").split("|")) | set(ks) - {""})
        hit["keys"], hit["buyer_keys"] = "|".join(allk), len(allk)
        continue
    for k in ks:
        seen[(k, x.get("jurisdiction") or "")] = x
        seen_any.setdefault(k, x)
    merged.append(x)
rows = merged
_free(globals(), "seen", "seen_any", "merged")  # they hold every row: a row written at the end could not be released (2026-11-10: +0.9 GB during the last pass)
# owner 2026-11-04 ("each row as populated as possible"): what the lanes read on the SAME page as the verified mailbox —
# AP phone, invoice mailing address, invoicing requirements / payment terms, invoice portal (an extra channel, never the contact)
EXTRA = {}
for f in sorted(_glob.glob(ROOT + "/data/incoming/*/*buyer_ap*results*.csv") + _glob.glob(ROOT + "/data/incoming/*/*_ap_*results*.csv")):
    try:
        for r in csv.DictReader(io.StringIO(open(f, encoding="utf-8", errors="replace").read().replace("\0", ""))):
            e = (r.get("ap_email") or "").strip().lower()
            if not e:
                continue
            d = EXTRA.setdefault(e, {})
            for col in ("ap_phone", "invoice_mailing_address", "invoicing_requirements_summary", "invoice_portal_url"):
                v = re.sub(r"\s+", " ", (r.get(col) or "")).strip()
                if v and v.lower() not in ("not_published", "none", "n/a", "-", "na", "null") and col not in d:
                    d[col] = v[:300]
    except Exception:
        pass
AP_TITLE = re.compile(r"accounts? payable|comptes? (?:à|a) payer|comptes payables|\bAP\b|payables?|finance clerk|accounting clerk|treasurer|tr[ée]sori|comptab|accountant", re.I)
NAME_RX = re.compile(r"\b([A-ZÉÈ][a-zéèêàçï'\-]{2,}(?:\s(?:[A-ZÉÈ]\.?\s)?[A-ZÉÈ][a-zéèêàçï'\-]{2,}){1,2})\b")
NOT_NAME = re.compile(r"accounts|payable|finance|services?|department|office|city|town|village|county|municipal|district|regional|ministry|university|college|school|hospital|health|"
                      r"contact|email|phone|invoice|supplier|vendor|general|public|canada|ontario|quebec|british|columbia|alberta|manitoba|street|avenue|road|box|suite|floor|"
                      r"monday|friday|hours|please|send|submit|questions|inquiries|information|center|centre|main|north|south|east|west|hall|building|bank|credit|union|first|nation",
                      re.I)
try:
    from buyer_pages import FIRST_NAMES as _FIRST
except Exception:
    _FIRST = set()
HONORIFIC = re.compile(r"\b(?:Mme|M\.|Mr\.?|Mrs\.?|Ms\.?|Madame|Monsieur|Dr\.?)\s+$")
ROLE_NEAR = re.compile(r"treasurer|tr[ée]sori|accounts? payable|payables?|comptes? (?:à|a) payer|comptes payables|comptab|accounting|accountant|finance|finances|"
                       r"bookkeeper|contr[ôo]leur|controller|\bAP\b|factur|invoic|commis-comptable|technicienne? (?:en )?comptab", re.I)
NOT_NAME2 = re.compile(r"purchase|order|address|adresse|ville|city|town|code|group|church|services?|management|budget|close|state|technicien|comptable|clerk|office|"
                       r"administrat|contact|courriel|email|t[ée]l[ée]phone|poste|ext\b|fax|department|finance|accounting|invoice|accounts|payable|payroll|visiting|"
                       r"general|inquir|treasurer|secretary|ladies|budget|close|main|navigation|hours|please|questions|vendors?|suppliers?|area|field|hill|hills|park|"
                       r"lake|river|valley|county|region|district|municipal|school|university|college|hospital|centre|center|society|association|foundation|"
                       r"hall|house|building|tower|plaza|campus|library|arena|stadium", re.I)
def ap_contact_name(quote, email, buyer=""):
    """the AP contact the organisation itself prints next to its invoicing mailbox (business contact information published by
    the organisation; never used as a mailbox). Conservative: a 2-3 word proper name within 60 characters of the mailbox whose
    first word is a known given name or that follows an honorific, with an AP / finance role word next to it, and sharing
    no word with the organisation's name."""
    q = quote or ""
    i = q.lower().find(email.lower())
    if i < 0:
        return ""
    win = q[max(0, i - 70):i + len(email) + 70]
    if not AP_TITLE.search(win):
        return ""
    btoks = set(re.findall(r"[a-zà-ÿ]{3,}", (buyer or "").lower()))
    for m in NAME_RX.finditer(win):
        nm = m.group(1)
        toks = nm.split()
        hon = bool(HONORIFIC.search(win[max(0, m.start() - 12):m.start()]))
        if toks[0] in ("Mme", "Madame", "Monsieur", "Mr", "Mrs", "Ms", "Dr"):
            hon, toks = True, toks[1:]
            nm = " ".join(toks)
        if len(toks) == 3 and re.match(r"(?i)manager|comptab|greff|commis|previous|technicien|secr|agent|adjoint|directeur|directrice|tr[ée]sor|clerk|officer|coordinat|supervis|assistant|controller|contr[ôo]leur|bookkeeper|accountant|treasurer|finance|payable", toks[2]):
            toks = toks[:2]; nm = " ".join(toks)
        if NOT_NAME2.search(nm) or len(toks) < 2 or re.search(r"\d", nm) or set(t.lower() for t in toks) & btoks:
            continue
        if not (toks[0].lower() in _FIRST or hon):
            continue
        near = win[max(0, m.start() - 40):m.end() + 40]
        if ROLE_NEAR.search(near) and not re.search(r"secretary|secr[ée]taire|ressources humaines|human resources|\bHR\b|president|pr[ée]sident|director|directeur|directrice|mayor|maire|clerk\b(?!.{0,20}(?:finance|account|comptab))", near, re.I):
            return nm
    return ""
FR = re.compile(r"\b(de la|du|des|les|pour|avec|nous|vous|facture|factures|courriel|téléphone|ville|municipalité|comptes|fournisseurs|paiement|adresse|envoyer|veuillez|service des finances|hôtel de ville|greffe|bureau)\b", re.I)
EN = re.compile(r"\b(the|and|for|with|please|send|invoice|invoices|email|phone|accounts|payable|department|office|hours|contact|submit|payment|address|finance|city hall|town hall)\b", re.I)
def language_hint(x):
    t = " ".join((x.get(c) or "") for c in ("email_evidence_quote", "buyer", "contract_title"))
    fr, en = len(FR.findall(t)), len(EN.findall(t))
    j = (x.get("jurisdiction") or "")
    if fr > en * 1.5 and fr >= 2:
        return "fr"
    if en > fr * 1.5 and en >= 2:
        return "en" if j != "QC" else "en (Québec: fr likely accepted)"
    return "fr/en" if j in ("QC", "NB") or (fr and en) else ("en" if en else ("fr" if fr else ""))
n_x = collections.Counter()
for x in rows:
    for col in ("ap_phone", "invoice_mailing_address", "invoicing_requirements", "invoice_portal_url", "ap_contact_name_as_published", "email_deliverability", "language_hint"):
        x.setdefault(col, "")
    e = (x.get("email") or "").lower()
    if not e:
        continue
    d = EXTRA.get(e) or {}
    if d.get("ap_phone"):
        x["ap_phone"] = d["ap_phone"]; n_x["ap_phone"] += 1
    if d.get("invoice_mailing_address"):
        x["invoice_mailing_address"] = d["invoice_mailing_address"]; n_x["invoice_mailing_address"] += 1
    if d.get("invoicing_requirements_summary"):
        x["invoicing_requirements"] = d["invoicing_requirements_summary"]; n_x["invoicing_requirements"] += 1
    if d.get("invoice_portal_url"):
        x["invoice_portal_url"] = d["invoice_portal_url"] + " (additional channel published by the buyer; the e-mail is the contact)"; n_x["invoice_portal_url"] += 1
    nm = ap_contact_name(x.get("email_evidence_quote") or "", e, x.get("buyer") or "")
    if nm:
        x["ap_contact_name_as_published"] = nm + " (as printed by the organisation next to its invoicing mailbox)"; n_x["ap_contact_name"] += 1
    x["language_hint"] = language_hint(x)
print("extras from the lanes' result rows:", dict(n_x))
OC = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_org_contacts.jsonl.gz"):
    for d in jl(ROOT + "/data/incoming/claude/claude_org_contacts.jsonl.gz"):
        OC[d.get("domain")] = d
N_OTHER_HOST = collections.Counter()
# the member-directory hosts of Canada-located bodies and each body's own domain (tools/member_live.py: "business.ottawabot.ca" is the Ottawa
# Board of Trade's directory, its own site is ottawabot.ca) — the one case where the lane itself says whose another host of a domain is
BODY_DOM = {}
try:
    import member_live as _ML0
    BODY_DOM = {(_h[4:] if _h.startswith("www.") else _h): _v[0] for _h, _v in _ML0.known_hosts().items()}
except Exception as _e:
    print("member-directory hosts not read (%s): a body's own site is not taken for its directory host" % str(_e)[:80])
def own_host_record(rec, h, table, name=""):
    """2026-11-10 (row audit, round 3): a site reader's record was kept under its site's registrable domain and handed to every row on that
    domain — "Texas Department of Insurance" (read on tdi.texas.gov) to five other Texas agencies, one municipality's name and address to the
    sixteen others on ao.ca, one church's address to another church on churchcenter.com, a realtor's logo to the platform it is hosted on. A
    record is a row's own when it was read on the row's own host. Read on another host of the domain, it is still the row's own in two cases
    only: the reader read that host for this very organisation (the name it was given is the row's name: bookstore.upei.ca and upei.ca are both
    "University of Prince Edward Island"), or the row's host is the member directory of the body whose own site was read (BODY_DOM). Anything
    else says nothing about this row; the readers key their records by host since that day, so each host gets its own."""
    if rec is None:
        return None
    rh = host_of(rec.get("website") or "")
    if rh and h and rh != h:
        _sq = lambda t: re.sub(r"^(?:the|la|le|les) ", "", norm(t)).replace(" ", "")  # "University of King's College" = "University of Kings College", "The City of Winnipeg" = "City of Winnipeg"
        rn = _sq(rec.get("name") or "")
        if name and rn and rn == _sq(name) and not DOMAIN_NAME.match((rec.get("name") or "").strip()):
            N_OTHER_HOST[table + ": taken, read on another host for the same organisation (same name)"] += 1
            return rec
        if BODY_DOM.get(h) and rh == BODY_DOM[h]:
            N_OTHER_HOST[table + ": taken, the row's host is the member directory of the body whose own site was read"] += 1
            return rec
        N_OTHER_HOST[table + ": not taken"] += 1
        return None
    return rec
def oc_of(url, name=""):
    """org_contacts record for a site; shared hosts (canada.ca …) are keyed by organisation path since 2026-11-08"""
    h = host_of(url or "")
    if not h:
        return None
    dom = registrable(h)
    pth = urllib.parse.urlparse(url if "//" in url else "https://" + url).path.rstrip("/")
    seg = "/".join(pth.split("/")[:3]) if pth else ""
    return (OC.get(dom + seg) if seg else None) or (OC.get(h + seg) if seg else None) or own_host_record((OC.get(h) if h != dom else None) or OC.get(dom), h, "org_contacts", name)
def flat_q(t):
    return re.sub(r"\s+", " ", t or "").strip()
# where an address is (2026-11-10): every row's vendor is located in Canada by the row's own evidence, so an address that the vendor's website
# prints OUTSIDE Canada is the group's or another office's, never the address of the Canada-located vendor ("CoreFour Inc. (Edsby)" carried
# Cupertino, Okta's Toronto office carried San Francisco). Such an address, and the telephone printed with it, are not taken for the vendor.
_CA_PC = re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]\s?\d[ABCEGHJ-NPRSTV-Z]\d\b")
_CA_WORD = re.compile(r"\bCanada\b|Qu[ée]bec|\bOntario\b|\bAlberta\b|British Columbia|Colombie-Britannique|\bManitoba\b|\bSaskatchewan\b|Nova Scotia|Nouvelle-[ÉE]cosse|New Brunswick"
                      r"|Nouveau-Brunswick|Newfoundland|Terre-Neuve|Prince Edward Island|\bYukon\b|\bNunavut\b|Northwest Territories", re.I)
_CA_PROV = re.compile(r"\b(?:AB|BC|MB|NB|NL|NS|NT|NU|ON|PE|QC|SK|YT)\b")
_US_ZIP = re.compile(r"\b(?:A[LKZR]|C[AOT]|D[EC]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY])\.?,?\s+\d{5}(?:-\d{4})?\b")
def in_canada_text(a):
    return bool(_CA_PC.search((a or "").upper()) or _CA_WORD.search(a or ""))
def site_country(o):
    """where the address a site prints for itself is: "CA", "abroad" or "" (no address read, or a placeholder / unreadable one)"""
    a = flat_q(str((o or {}).get("address") or ""))
    if not a or not re.search(r"\d", a):
        return ""
    cc = ((o or {}).get("address_country") or "").strip()
    if cc.upper() in ("CA", "CAN", "CANADA") or in_canada_text(a):
        return "CA"
    if (cc and re.fullmatch(r"[A-Za-zÀ-ÿ .'-]{2,40}", cc)) or _US_ZIP.search(a):
        return "abroad"
    return ""
SITE_OWNER = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_site_owner_wd.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_site_owner_wd.csv", encoding="utf-8")):
        SITE_OWNER[_r["domain"]] = _r
_CA_SECTION = re.compile(r"/(?:ca|ca-en|ca-fr|en-ca|fr-ca|en_ca|fr_ca|canada)(?:/|$)", re.I)
def in_ca_section(url):
    """a page inside the Canadian section of a group's site (kpmg.com/ca/en/…, ca.brinks.com): the Canadian arm's own page"""
    try:
        u = urllib.parse.urlparse(url or "")
    except ValueError:
        return False
    return bool(_CA_SECTION.search(u.path or "") or re.match(r"(?:ca|canada)\.", (u.hostname or "").lower().removeprefix("www.")))
def site_not_the_vendors_own(website):
    """the website on a vendor's row is a foreign organisation's: Wikidata names its organisation with headquarters abroad, or (Wikidata silent)
    the only address the site prints for itself is outside Canada. What such a site states about itself — its legal name, its trading name, its
    address, its telephone — is the group's, not the Canada-located vendor's ("KPMG International Limited" from kpmg.com's legal page for KPMG LLP,
    "International Business Machines Corporation" for IBM Canada)."""
    h = host_of(website or "")
    if not h or h.endswith(".ca"):
        return False
    v = (SITE_OWNER.get(registrable(h)) or {}).get("verdict")
    return v == "abroad" or (v != "canada" and site_country(oc_of(website)) == "abroad")
# owner 2026-11-04: facts each organisation prints on its own site (tools/org_extras.py): legal name (copyright line), BN / GST-HST /
# charity number, NEQ / QST, logo, language; and the site's status from org_contacts
OX = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_org_extras.jsonl.gz"):
    for d in jl(ROOT + "/data/incoming/claude/claude_org_extras.jsonl.gz"):
        OX[d.get("domain")] = d
def ox_of(url, name=""):
    """org_extras record for a site; on shared hosts (canada.ca, ontario.ca …) org_extras v2 keys one record per organisation path"""
    h = host_of(url or "")
    if not h:
        return None
    dom = registrable(h)
    pth = urllib.parse.urlparse(url if "//" in url else "https://" + url).path.rstrip("/")
    seg = "/".join(pth.split("/")[:3]) if pth else ""
    return (OX.get(dom + seg) if seg else None) or (OX.get(h + seg) if seg else None) or own_host_record((OX.get(h) if h != dom else None) or OX.get(dom), h, "org_extras", name)
TRAIL = re.compile(r"(?:\s+(?:our|the|all|home|about|contact|site|web|privacy|terms|follow|connect|menu|search|login|accessibility|faq|careers|news|events|donate|"
                   r"language|english|french|fran[çc]ais|skip|top|back|rights|reserved|reserves|tous|droits|r[ée]serv[ée]s|powered|by|design|website|sitemap|plan))+$", re.I)
BAD_LEGAL = re.compile(r"copyright act|subject to|proprietary|affiliated|licen[cs]e|rights reserved|droits r[ée]serv|\btheme\b|muffin group|posted by|"
                       r"schoolmessenger|sportsengine|launchit|civicplus|civic plus|granicus|esolutions|blackboard|finalsite|apptegy|edlio|\bwix\b|squarespace|"
                       r"wordpress|shopify|weebly|godaddy|intrado|blackbaud|municipal website|all content|this (?:web)?site|ce site", re.I)
CUT_PREFIX = re.compile(r"\b(?:saint|sainte|st|ste|lac|val|mont|rivi[èe]re|baie|cap|pointe|notre|port|fort|grand|grande|petit|petite|trois|sept|[îi]le|[îi]les|bois|"
                        r"la|le|les|du|de|des|d|l|au|aux|sur|en|et|and|of|the|for|&)$", re.I)
GENERIC_NAME = re.compile(r"^(?:contactez[- ]nous|contact(?:ez)?(?:[- ]us)?|nous joindre|accueil|home(?: page)?|bienvenue|welcome|about(?: us)?|[àa] propos|coordonn[ée]es|"
                          r"page d.accueil|untitled|index|services|joindre|page not found|404|login|connexion)\W*$", re.I)
DOMAIN_NAME = re.compile(r"^(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}$", re.I)
# 2026-11-10 (row audit): what the footer / copyright reader took for a legal name on 3 % of the rows that carry one — a run of menu words
# ("Releases Company Careers About Us …", 89 KPMG rows), the web agency's credit ("Made by Enova Inc", "Designed by DCS TECHNOLOGIES INC"), an
# address or opening hours ("Office Location: NWT Commerce Place, 4th Floor …"), a cookie or consent sentence ("University of Regina We use
# cookies to give you the best"), a mailbox, a fragment cut inside brackets. None of these is a name.
_NAV_STRONG = re.compile(r"\b(?:about us|contact us|[àa] propos|nous joindre|faq|blog|podcast|log ?in|sign ?in|sign[- ]?up|site ?map|newsroom|careers?|carri[èe]res?|privacy|case studies|"
                         r"testimonials|cart|menu|submenu|search|releases|subscribe|newsletter)\b", re.I)
_NAV_WEAK = re.compile(r"\b(?:home|accueil|services|support|news|events|resources|team|portfolio|employment|partners|products|solutions|shop|gallery|investors|company|contact|about|"
                       r"twitter|instagram|facebook|linkedin|youtube)\b", re.I)
_CREDIT_LINE = re.compile(r"\b(?:designed|developed|created|built|made|hosted|powered|maintained|managed|provided|crafted|produced)\s+(?:and\s+\w+\s+)?by\b|"
                          r"\b(?:web ?site|site|web design|design|marketing|d[ée]veloppement)\s+(?:by|par)\b|\b(?:cr[ée]{2}|con[çc]u|r[ée]alis[ée]|propuls[ée]|h[ée]berg[ée]|d[ée]velopp[ée])e?s?\s+par\b|"
                          # 2026-11-10 (round 3): "© WEYMOK Tous droits réservés Réalisation : SIGNÉ FRANÇOIS ROY INC" gave the agency as the legal name of 9 sites
                          r"\b(?:r[ée]alisation|conception|cr[ée]ation|design|d[ée]veloppement|h[ée]bergement|une r[ée]alisation de|un site de|site web)\s*:", re.I)
# a template's placeholder, a degree or a professional title, a programme: printed on a page, never the legal name of the organisation
_PLACEHOLDER = re.compile(r"^(?:your |my |the )?(?:company|business|site|website|store|shop|brand|organi[sz]ation)(?: |')?s? ?(?:name|title)(?: here)?$|^(?:doctor|docteur|master|bachelor|ma[îi]trise|baccalaur[ée]at)\s+(?:of|in|en|[èe]s)\b|"
                          r"^(?:registered|certified|licensed|chartered|accredited)\s+[a-zà-ÿ]+(?:\s+[a-zà-ÿ]+)?\s*(?:therap|technolog|nurse|practition|professional|accountant|planner|engineer|dietitian|hygienist)\w*$", re.I)
_PLACE_NOUN = {"canada", "quebec", "ontario", "alberta", "manitoba", "saskatchewan", "columbia", "scotia", "brunswick", "newfoundland", "labrador", "yukon", "nunavut", "territories",
               "island", "montreal", "toronto", "vancouver", "calgary", "ottawa", "edmonton", "winnipeg", "halifax", "america", "states", "kingdom", "australia", "france", "texas", "california"}
def only_generic_words(n, buyer=""):
    """"University", "Canadian Association", "Municipalité du canton", "Centre", "Community Foundation": a kind of body, not a body. A name that
    carries a place ("Health Canada", "Santé Québec", "Ville de Québec") is complete; so is a run of three such words and more ("First Nations
    Health Authority", "Provincial Health Services Authority"); and the organisation's own name is never refused."""
    t = set(re.findall(r"[a-z]{2,}|\d+", unicodedata.normalize("NFKD", n or "").encode("ascii", "ignore").decode().lower()))
    t -= {"the", "of", "de", "du", "des", "la", "le", "les", "and", "et", "for", "pour", "inc", "ltd"}
    if not t or (t & _PLACE_NOUN) or (t - NAME_STOP - GENERIC_ORG - _NATIONAL) or len(t - NAME_STOP) >= 3:
        return False  # a number is a word of its own: "District 3", "School District 43"
    return re.sub(r"^(?:the|la|le|les|l) ", "", norm(buyer)) != re.sub(r"^(?:the|la|le|les|l) ", "", norm(n))
_NOT_A_NAME = re.compile(r"\d{1,2}:\d{2}|\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]\s?\d[ABCEGHJ-NPRSTV-Z]\d\b|\b(?:floor|[ée]tage|suite\s+\d|c/o|attn|office location|office hours|heures d.ouverture|boul\.|p\.?o\.? box|"
                         r"case postale)\b|\b(?:we (?:use|acknowledge|are|carry|offer|have)|we['’]re|you (?:consent|agree|need|can)|(?:to|for|give|help) you|who we are|what we|this field|should be|shall be|"
                         r"are you|limited time|book an?|click here|read more|learn more|and our|(?:visit|meet|join|contact|call|email|follow|see|find|work with|connect with|stay with) (?:our|us)|"
                         r"based on \d+ reviews?)\b|^\d+\s*,\s|^\d+(?:\s+\d+)+", re.I)
_BARE_GENERIC = re.compile(r"^(?:foundation|fondation|company|group|groupe|association|society|soci[ée]t[ée]|corporation|limited|copyright|inc|media partners|partners|office pro)\.?$", re.I)
def clean_legal(name, buyer=""):
    """the copyright-line name, or "" when it is a sentence fragment, a web platform's own copyright, or a name cut at a hyphen
    (org_extras ≤ 2026-11-04 stopped at the first dash: 'Municipalité de Saint' for Saint-Jean-sur-Richelieu)"""
    n = re.sub(r"[\uf000-\uf8ff\u2000-\u206f\ue000-\uf8ff]", " ", name or "")  # icon-font glyphs glued to footer text
    n = re.sub(r"\s+", " ", n).strip(" .,-–—|:")
    n = re.split(r"\s*(?:-->|<!--)", n)[0].strip(" .,-–—|:")  # "Synergy Foundation --> This": the end of a comment in the page's markup
    # "AND DISCLOSURE Menno S. Martin Contractor Limited": the end of the page's heading ("PRIVACY AND DISCLOSURE") run into the name that follows it
    n = re.sub(r"^(?:(?:AND|OF|&|ET|DE)\s+)?(?:(?:PRIVACY|TERMS|CONDITIONS|DISCLOSURE|DISCLAIMER|POLICY|POLICIES|NOTICE|LEGAL|USE|COOKIES?|CONFIDENTIALIT[ÉE]|POLITIQUE|MENTIONS|L[ÉE]GALES)\s+(?:(?:AND|OF|&|ET|DE)\s+)?)+(?=[A-Z0-9][a-zà-ÿ0-9.])", "", n)
    n = re.sub(r"^(?:tous droits r[ée]serv[ée]s|all rights reserved|copyright|©|\(c\))\s*(?:(?:19|20)\d\d\s*)?", "", n, flags=re.I).strip(" .,-–—|:")
    n = re.sub(r"^(?:19|20)\d\d\s*[/|–—-]*\s*", "", n).strip(" .,-–—|:/")  # "2026 // Coop Audiovisuelle GTS"
    n = re.sub(r"^(?:(?:january|february|march|april|may|june|july|august|september|october|november|december|janvier|f[ée]vrier|mars|avril|mai|juin|juillet|ao[ûu]t|septembre|octobre|novembre|"
               r"d[ée]cembre)\.?\s+(?:\d{1,2},?\s+)?(?:19|20)\d\d|\d{1,2}(?:er)?\s+(?:january|february|march|april|may|june|july|august|september|october|november|december|janvier|f[ée]vrier|mars|avril|mai|juin|"
               r"juillet|ao[ûu]t|septembre|octobre|novembre|d[ée]cembre)\.?\s+(?:19|20)\d\d)\s+", "", n, flags=re.I).strip(" .,-–—|:/")  # "July 16, 2026 City Best Limousine": the page's "last updated" date
    n = re.sub(r"^(?:\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]\d{4}\s+(?=[A-Za-zÀ-ÿ])", "", n)  # "775-8387 Midtown Veterinary Hospital": the end of a telephone number
    n = re.sub(r"^\d{1,2}[.)]\s+(?:introduction|d[ée]finitions?|agreement to (?:the )?terms|acceptance of (?:the )?terms|general(?: terms)?|g[ée]n[ée]ralit[ée]s|pr[ée]ambule|overview|scope|"
               r"who we are|qui sommes-nous|about us|[àa] propos)\s+", "", n, flags=re.I).strip(" .,-–—|:/")  # "1. Introduction Divertissements Oxygames inc"
    if " | " in n and len(n.split(" | ")[0].strip()) >= 3:
        n = n.split(" | ")[0].strip(" .,-–—|:")  # "Canadian College of Traditional Chinese Medicine | CCTCM | …"
    n = re.split(r"\s+(?:connect with us|follow us|stay connected|subscribe|sign up|cricos\b|abn\b|acn\b|registered charity|charitable registration|privacy(?=\s+(?:policy|notice|statement|terms|settings|&|and\s+(?:terms|cookie)|\|)|\s*$)|terms(?=\s+(?:of|and|&|conditions|\|)|\s*$)|all rights|"
                 r"tous droits|site ?map|plan du site|accessibilit|contact us|nous joindre|back to top|retour en haut|pr[ée]f[ée]rences des t[ée]moins|we use cookies|this site uses)\b", n, maxsplit=1, flags=re.I)[0].strip(" .,-–—|:")
    n = TRAIL.sub("", n).strip(" .,-–—|:")
    n = re.sub(r"\s+copyright$", "", n, flags=re.I).strip(" .,-–—|:")  # "Canadian Nurses Association Copyright"
    n = re.sub(r"^(?:[àa] la|au|aux|[àa] l'|the|la|le|les|l')\s+", "", n, flags=re.I).strip() if re.match(r"^(?:[àa] la|au|aux|[àa] l')\s", n, re.I) else n  # "à la Commission scolaire …" (pilot dossier S1-12)
    n = re.sub(r"^à\s+", "", n)  # "à Devimco Immobilier Inc"
    n = re.sub(r"^(?:reserved\s+(?:to|by)|r[ée]serv[ée]s?\s+[àa])\s+", "", n, flags=re.I)  # "(All rights) Reserved to Brooks Building Maintenance inc"
    n = re.sub(r"\s+o/a$", "", n, flags=re.I)  # "… Professional Corporation o/a": the trade name that followed was cut off
    if BAD_LEGAL.search(n) or CUT_PREFIX.search(n) or (re.match(r"^(?:'?s\b|[a-z])", n) and not re.match(r"^[a-z]{1,6}[A-Z0-9][A-Za-z0-9]*\s+\S", n)) or re.search(r"\bno\.?$", n, re.I):
        return ""  # a fragment cut at the front ("s Union Partners"), lowercase start, or ending in "No" (a registration number followed);
        # 2026-11-11: "easyDNS Technologies Inc", "eGrr Services Inc.", "iTrack Fitness Inc" begin with a small letter by design
    if buyer and re.sub(r"\s+", " ", buyer).strip().lower().startswith(n.lower() + "-"):
        return ""
    _ns, _nw = len(_NAV_STRONG.findall(n)), len(_NAV_WEAK.findall(n))
    if _ns >= 2 or (_ns >= 1 and _nw >= 2) or "@" in n or n.count("(") != n.count(")"):
        return ""  # a run of menu words ("Releases Company Careers About Us …"), a mailbox, or a fragment cut inside brackets ("Act)to Company at support@")
    if _CREDIT_LINE.search(n) or _NOT_A_NAME.search(n) or _BARE_GENERIC.match(n) or len(n.split()) > 12 or _PLACEHOLDER.search(n) or only_generic_words(n, buyer):
        return ""  # the web agency's credit, an address / opening hours / consent sentence, a bare generic word, a placeholder, a degree or title
    if re.search(r"\s(?:by|with|and|are|is|of|the|to|for|from|or|as|that|which|par|de|du|des|et|avec|pour|sur|dans|le|la|les|qui|que)$", n, re.I) or re.match(r"(?:by|en)\s+\w+(?:ing|ant)\b", n, re.I) or \
            re.search(r"\b(?:and|et)\s+(?:are|is|sont|est)\b|\b(?:are|is|sont|est)\s+(?:protected|owned|the property|registered|prot[ée]g[ée]e?s?|la propri[ée]t[ée])\b", n, re.I):
        return ""  # a piece of a sentence: "XXL IT Services and are protected by", "By booking a cleaning service with NeatNow"
    return n if 3 <= len(n) <= 90 and re.search(r"[A-Za-zÀ-ÿ]{3}", n) else ""
# the footer of a site built on a government template credits the government ("© Gouvernement du Québec" on every centre de services scolaire's
# site): that is not the legal name of a body that is a legal person in its own right
_OWN_PERSON = re.compile(r"centre de services scolaire|commission scolaire|school (?:board|district|division)|[ée]cole\b|c[ée]gep|coll[èe]ge|college|universit|\bville\b|municipalit|"
                         r"\b(?:city|town|village|township|county) of\b|ciu?sss|hospital|h[ôo]pital|\br[ée]gie\b|office municipal|soci[ée]t[ée] de transport", re.I)
def credit_of_a_government(ln, org):
    return bool(re.match(r"(?:gouvernement|government)\b", ln or "", re.I) and _OWN_PERSON.search(org or "") and not re.search(r"gouvernement|government", org or "", re.I))
def bn_ok(d):
    lab = (d.get("bn_label") or "") + " " + (d.get("bn_quote") or "")
    return not re.search(r"wikidata|https?://|/wiki/|\bQ\d{6,}", lab, re.I)
SITE_STATUS = {"ok": "site answers", "no_contact": "site answers (no contact details found)", "blocked": "site blocks automated readers",
               "robots": "robots.txt disallows reading", "http_0": "site unreachable when read", "not_html": "site served no HTML", "error": "read error"}
TERMS = re.compile(r"\b(net\s?\d{2}\b|\d{2}\s?(?:calendar |business )?days?\b|within\s\d{2}\s?(?:calendar |business )?days|\d{2}\s?jours|dans les \d{2} jours|upon receipt|on receipt|"
                   r"[àa] (?:la )?r[ée]ception|2%\s?\d{2}|net\s?\d{2}\s?days|payment terms?[^.]{0,40})", re.I)
PO_REQ = re.compile(r"(?:purchase order|\bPO\b|P\.O\.|bon de commande|num[ée]ro de (?:bon de )?commande)[^.]{0,80}?(?:required|must|need|doit|obligatoire|requis|include|indiqu|mention|quote|reference|référenc)|"
                    r"(?:required|must|need|doit|obligatoire|requis|include|indiqu|mention|quote|reference|référenc)[^.]{0,80}?(?:purchase order|\bPO\b|P\.O\.|bon de commande|num[ée]ro de (?:bon de )?commande)", re.I)
NAME_STOP = {"the", "and", "inc", "ltd", "city", "town", "ville", "corporation", "limited", "des", "les", "municipality", "county", "canada", "group", "groupe", "ltee", "corp", "company", "of", "de", "du", "la", "le", "services", "service", "international", "solutions", "consulting", "llp", "llc", "co"}
GENERIC_ORG = {"university", "universite", "college", "school", "board", "district", "county", "region", "regional", "municipalite", "municipal", "department", "departement",
               "ministry", "ministere", "hospital", "hopital", "health", "sante", "centre", "center", "authority", "agency", "agence", "office", "bureau", "commission", "council",
               "conseil", "community", "communaute", "public", "national", "federal", "provincial", "state", "government", "gouvernement", "first", "nation", "nations",
               "society", "association", "foundation", "fondation", "institute", "institut", "library", "bibliotheque", "township", "canton", "village", "cite", "city", "town"}
PAGE_NOISE = re.compile(r"\b(faculty and staff|faculty & staff|log ?in|sign ?in|search|disclaimers?|whitepapers?|brochures|data sheets|menu|home ?page|skip to|click here|read more|locations & hours|privacy policy|terms of use|cookie)\b|^(address|contact|about|welcome to)\b", re.I)  # navigation fragments; legitimate names such as "BCIT Student Association" or "ESF Events Ltd" must pass (19:39Z build lost 158 names, 150 junk, ~8 real)


_NATIONAL = {"canadian", "canadien", "canadienne", "national", "nationale", "provincial", "federal", "quebec", "ontario", "alberta"}
_KIND = {"municipality": re.compile(r"\b(?:town|city|village|municipality|township|county|ville|municipalit[ee]|canton|mrc)\b"),
         "hospital": re.compile(r"(?<!\banimal\s)(?<!\bpet\s)(?<!\bveterinary\s)(?<!\bvet\s)\b(?:hospital|hopital(?! veterinaire)|health authority|hospitalier)\b"), "university": re.compile(r"\b(?:university|universite)\b"),
         "college": re.compile(r"\b(?:college|cegep|polytechnic)\b"), "school": re.compile(r"\b(?:school|ecole|school board|commission scolaire)\b"),
         "church": re.compile(r"\b(?:church|eglise|parish|paroisse|diocese)\b"), "bank": re.compile(r"\b(?:bank|banque|credit union|caisse)\b"),
         "ministry": re.compile(r"\b(?:ministry|ministere|government of|gouvernement)\b"), "police": re.compile(r"\bpolice\b"),
         "library": re.compile(r"\b(?:library|bibliotheque)\b"), "museum": re.compile(r"\b(?:museum|musee)\b")}
_KIND_HOST = {"municipality": re.compile(r"town|city|village|ville|municipal|county|township|mrc"), "hospital": re.compile(r"hospital|hopital|health|sante|chu|ciss"),
              "university": re.compile(r"universit|^u[a-z]{2,5}$|uq|\.edu"), "college": re.compile(r"college|cegep|polytech|\.edu"), "school": re.compile(r"school|ecole|scolaire|csd|sd\d|css|\.edu|k12|isd\b"),
              "church": re.compile(r"church|eglise|parish|paroisse|diocese"), "bank": re.compile(r"bank|banque|caisse|credit"), "ministry": re.compile(r"gov|gouv|gc\.ca"),
              "police": re.compile(r"police"), "library": re.compile(r"librar|biblio"), "museum": re.compile(r"museum|musee")}
_INI_STOP = {"de", "du", "des", "la", "le", "les", "l", "d", "of", "the", "and", "et", "for", "a", "au", "aux", "in", "en", "sur"}
def _host_label(website):
    try:
        return re.sub(r"[^a-z0-9]", "", registrable(host_of(website or "") or "").split(".")[0])
    except Exception:
        return ""
_LEAD_SKIP = {"town", "city", "village", "township", "municipality", "county", "district", "ville", "municipalite", "canton", "paroisse", "university", "universite", "college",
              "centre", "center", "hopital", "hospital", "ecole", "school", "corporation", "societe", "association", "ordre", "commission", "regie", "office", "bureau", "institut",
              "institute", "federation", "fondation", "foundation", "groupe", "group", "conseil", "council", "club", "regional", "rural"}
def label_from_words(cand, hl):
    """the site's own label is written with the candidate's words, in their order — whole words, their beginnings, their initials — and every
    letter of the label is accounted for: "usask" = U. of SASKatchewan, "austincc" = AUSTIN C. C., "bmo" = B. of MOntreal, "tol" = T. O. L.,
    "mcgill" = MCGILL (University), "chumontreal" = C. H. de l'U. de MONTREAL, "westspringsvet" = WEST SPRINGS VET. Words may be left out only
    when they are articles / prepositions, or a kind-of-body word in front of the name ("Town of BANFF"); what follows the label does not matter.
    "vernonchamber" is not written with "Vernon Jubilee Hospital", "kitchenermarket" not with "City of Kitchener"."""
    words = re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", (cand or "").replace("&", " and ")).encode("ascii", "ignore").decode().lower())
    n = len(hl)
    if n < 2 or not words or len(words) > 14:
        return False
    memo = {}
    def go(i, j, strong, used):
        if i == n or (used and hl[i:] == "s"):
            return strong or used >= 3  # one whole word or beginning of three letters and more, or at least three initials
        key = (i, j, strong, min(used, 3))
        if key in memo:
            return memo[key]
        ok = False
        for k in range(j, len(words)):
            w = words[k]
            for ln in range(min(len(w), n - i), 0, -1):
                if hl.startswith(w[:ln], i) and go(i + ln, k + 1, strong or ln >= 3, used + 1):
                    ok = True
                    break
            if ok or not (w in _INI_STOP or (not used and w in _LEAD_SKIP)):
                break  # this word may not be left out
        memo[key] = ok
        return ok
    return go(0, 0, False, 0)
def label_begins(cand, hl):
    """the site's label begins with the candidate's own leading words, written whole: "stonechurch|vet" = STONE CHURCH Animal Clinic,
    "northernfire|store" = NORTHERN FIRE, "unitedcanada|inc", "newlife|pt" = NEW LIFE Physiotherapy — over two words and more, or over one word
    that few names carry and that is at least half of the label ("brock|u"). A word further inside the label proves nothing: "smile|dentalcare"
    is not Canadian DENTAL CARE, "lapointe|dental" is not DENTAL Corporation of Canada, "bristol|dental" not the Ontario DENTAL Association."""
    words = re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", (cand or "").replace("&", " and ")).encode("ascii", "ignore").decode().lower())
    i = nw = 0
    first = ""
    for w in words:
        if len(w) >= 2 and hl.startswith(w, i):
            i += len(w); nw += 1; first = first or w
        elif w in _INI_STOP or (nw == 0 and w in _LEAD_SKIP):
            continue
        else:
            break
    return i >= 4 and (nw >= 2 or (nw == 1 and 2 * i >= len(hl) and first not in WORD_COMMON))
def label_of_whole_words(cand, hl):
    """the whole label is two and more of the candidate's words, written whole and in their order, others left out: "qualityhomes" = QUALITY
    (Engineered) HOMES Ltd, "torontodental" = TORONTO DENTAL Clinic Inc. Not "smiledentalcare" for Canadian Dental Care: "smile" is nobody's."""
    words = re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", (cand or "").replace("&", " and ")).encode("ascii", "ignore").decode().lower())[:14]
    memo = {}
    def go(i, j, n):
        if i == len(hl):
            return n >= 2
        if (i, j, min(n, 2)) not in memo:
            memo[(i, j, min(n, 2))] = any(len(words[k]) >= 2 and hl.startswith(words[k], i) and go(i + len(words[k]), k + 1, n + 1) for k in range(j, len(words)))
        return memo[(i, j, min(n, 2))]
    return len(hl) >= 4 and go(0, 0, 0)
_NUMBERED_CO = re.compile(r"\d[\d\s-]*\s+(?:Qu[ée]bec|Canada|Ontario|Alberta|Manitoba|Saskatchewan|B\.?C\.?|Nova Scotia|N\.?B\.?|N\.?S\.?|Yukon|Newfoundland)\s+(?:Inc|Ltd|Lt[ée]e|Corp|Limited|Limit[ée]e|ULC)\b", re.I)
def tight_name(cand, website):
    """the beginning of an accepted name that still writes the site's own label, when what follows is not part of a name: a street address
    ("Criminal Trial Lawyers 480 University" -> "Criminal Trial Lawyers") or a tagline after a dash ("Vision Integrity Engineering Ltd -
    Integrity for a Safer World"). A tail that is itself a name stays: a numbered company ("Noraa 9439-4145 Québec Inc"), a spelled-out name
    or legal entity after the dash ("NBREA - New Brunswick Real Estate Association")."""
    hl = _host_label(website)
    c = cand or ""
    m = re.search(r"\s+[-–—|:]\s+", c)
    if m and not LEGAL_FORMISH.search(c[m.end():]):
        cut = c[:m.start()].strip(" .,-–—|:")
        if len(cut) >= 3 and hl and label_from_words(cut, hl):
            return cut
    m = re.search(r"\s+(?=\d)", c)
    if m and not _NUMBERED_CO.search(c[m.start():]):
        cut = c[:m.start()].strip(" .,-–—|:")
        if len(cut) >= 3 and hl and label_from_words(cut, hl):
            return cut
    return c
def name_overlap(cand, org_name, website=""):
    """a name taken from a page must share a DISTINCTIVE token with the organisation's own name or its host (reviewer 2026-11-08; pilot dossiers
    2026-11-09: "Cambrian College Faculty and staff" and "Pioneer Path University" had passed on the generic words college / university)"""
    if PAGE_NOISE.search(cand or ""):
        return False
    def toks(t):
        return {w for w in re.findall(r"[a-z0-9]{3,}", unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()) if w not in NAME_STOP}
    ct, ot = toks(re.sub(r"\s*\([^()]{1,12}\)\s*$", "", cand or "")), toks(org_name)
    h = unicodedata.normalize("NFKD", host_of(website or "") or "").encode("ascii", "ignore").decode().lower().replace("www.", "").replace("-", "")
    hl = _host_label(website)
    words_all = re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", cand or "").encode("ascii", "ignore").decode().lower())
    words = [w for w in words_all if w not in _INI_STOP]
    ini = "".join(w[0] for w in words)
    # 2026-11-10 (row audit): a name stated on an "about" or "board of directors" page is often ANOTHER body — "Vernon Jubilee Hospital" on the Vernon
    # chamber's board page, "Town of Cochrane" on the Cochrane chamber's, "City of Toronto" on a congress's, all accepted on the shared place name.
    # A candidate that names a kind of institution (a town, a hospital, a university, a bank …) which neither the organisation's own name nor its
    # address carries is another body — unless its initials are the organisation's name or sit in its address ("Centre hospitalier de l'Université
    # de Montréal" for chumontreal.qc.ca), or the address is written with the candidate's own words ("austincc.edu", "unionps.org", "westspringsvet.ca").
    def kinds(text):
        t = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode().lower()
        return {k for k, rx in _KIND.items() if rx.search(t)}
    ck = kinds(cand)
    if ck and not ck <= (kinds(org_name) | {k for k, rx in _KIND_HOST.items() if rx.search(h) or rx.search(hl)}):
        on = re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", org_name or "").encode("ascii", "ignore").decode().lower())
        if not ((len(ini) >= 3 and (ini == on or ini in h)) or (hl and label_from_words(cand, hl))):
            return False
    cd, od = ct - GENERIC_ORG - _NATIONAL, ot - GENERIC_ORG - _NATIONAL
    # 2026-11-10 (round 3): the shared word must be one that few organisations carry. "Canadian Dental Care" (a federal programme) was the legal
    # name of 71 dental clinics on the word "dental", "Doctor of Dental Surgery" of 16 on "surgery", "Canadian Real Estate Association" of 29
    # brokers on "real estate", "Texas Department of Insurance" of five other agencies on "texas". A word carried by more than one name in 2,000
    # (WORD_COMMON, counted on the names of the organisations whose site was read) proves nothing by itself: the names must then be one inside
    # the other. The site's address written with the candidate's own words still proves it ("dentalcorp.ca" = DENTAL CORPoration of Canada).
    shared = (cd & od) if (cd and od) else (ct & ot)  # one side has only generic words (e.g. "Health Authority"): any shared token
    # the candidate, word for word, as a whole part of the organisation's name — between its start or a separator and a separator or its end:
    # "City of Richmond" in "City of Richmond, California — GF-POLI". A piece that stops inside the name is a cut name, not a name: "Town of New"
    # (Tecumseth), "BC Society" (for the Museum of Original Costume), "University of Canada" (First Nations …).
    _cw = re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", re.sub(r"\s*\([^()]{1,12}\)\s*$", "", cand or "")).encode("ascii", "ignore").decode().lower())
    if len(_cw) >= 2:
        _on = unicodedata.normalize("NFKD", re.sub(r"[\u2013\u2014]", "-", org_name or "")).encode("ascii", "ignore").decode().lower()
        if re.search(r"(?:^|[,;:|(/]|\s-)\s*(?:the\s+)?" + r"[\s'.&]+".join(map(re.escape, _cw)) + r"\s*(?:$|[,;:|()/]|-\s)", _on):
            return True
    if shared and (any(t not in WORD_COMMON for t in shared) or ot <= ct or (ct <= ot and len(ct) >= 2)):
        return True  # a word few names carry — or the organisation's whole name inside the candidate ("Desjardins" in "Fédération des caisses
                     # Desjardins du Québec", "Toronto Dental Clinic Inc"), or the candidate a part of it of two words and more
    if h and (hl in ct or label_begins(cand, hl) or label_of_whole_words(cand, hl) or any(t in h for t in (cd or ct) if len(t) >= 4 and t not in WORD_COMMON)):
        return True  # the address is the candidate's own word ("desjardins.com"), begins with or is made of its words, or carries a word few names carry
    if DOMAIN_NAME.match((org_name or "").strip()):  # the organisation is known by a domain only ("centrerecreatifzone15.ca"): that label is its name
        ol = _host_label(org_name.strip())
        if ol and ol != hl and (label_from_words(cand, ol) or label_begins(cand, ol) or label_of_whole_words(cand, ol)):
            return True
    return bool(hl) and label_from_words(cand, hl)  # "ctaontario.ca" = Construction Training & Apprenticeship ONTARIO
LEGAL_FORMISH = re.compile(r"\b(inc|ltd|limited|lt[ée]e|llc|llp|corp|corporation|company|co\.|society|association|foundation|fondation|university|universit[ée]|college|coll[èe]ge|c[ée]gep|city|town|village|municipality|municipalit[ée]|ville|county|district|township|school|scolaire|hospital|h[ôo]pital|health|sant[ée]|authority|board|commission|agency|office|ministry|minist[èe]re|department|government|gouvernement|library|biblioth[èe]que|church|trust|group|groupe|holdings|cooperative|coop[ée]rative|credit union|caisse|soci[ée]t[ée]|centre|center|institute|institut|canada|r[ée]gie|f[ée]d[ée]ration)\b", re.I)
PORTAL_INVOICING = re.compile(r"e-invoicing|supplier payments|supplier onboarding", re.I)
MENTION_STRICT = {"payment_method": re.compile(r"\b(?:direct deposit|d[ée]p[ôo]t direct|electronic funds transfer|EFT|ACH|virement|e-?transfer|Interac(?!t)|paid by cheque|payment by cheque|par ch[èe]que|credit card payments?|P-?card|wire transfer)\b", re.I),
                  "tax_exempt": re.compile(r"\b(?:tax[- ]exempt|exempt from|exon[ée]r|HST rebate|GST rebate|PST exempt|exemption de taxe|municipal rebate)", re.I),
                  "esignature": re.compile(r"\b(?:DocuSign|Adobe ?Sign|electronic signatures?|digital signatures?|signatures? [ée]lectroniques?|signatures? num[ée]riques?|e-?signatures?)\b", re.I),
                  "ap_cycle": re.compile(r"(?:cheque runs?|payment runs?|payments? (?:are|is) (?:issued|processed|made|released)|paiements? (?:sont )?(?:[ée]mis|effectu[ée]s|trait[ée]s)|cycle de paiement|invoices? (?:are|is) paid)", re.I)}
MENTION_CTX = re.compile(r"invoice|factur|supplier|vendor|fournisseur|payable|payment to|paiement|purchase order|bon de commande|accounts payable|comptes [àa] payer|remit|remise|procurement|approvisionnement|purchasing|achats", re.I)
MENTION_NOISE = re.compile(r"copyright|dmca|infring|cookie|newsletter|donat|\bdon\b|tax receipt|re[çc]u|charitable|patient|student|[ée]tudiant|tuition|membership|adh[ée]sion|property tax|taxes fonci|parking|stationnement|utility bill|water bill|facture d['’]eau|compte de taxes|interact", re.I)
def v2_fill(x, d, side):
    """org_extras v2 facts (schema.org JSON-LD, tel: links, portal links, page mentions) into the row's empty cells, each labelled with its page"""
    pre = "buyer_" if side == "buyer" else "vendor_"
    pg = d.get("jsonld_page") or d.get("website") or ""
    if not x.get(pre + "phone") and (d.get("jsonld_phone") or d.get("tel_links")):
        x[pre + "phone"] = "%s (%s)" % ((d.get("jsonld_phone") or d["tel_links"].split(";")[0].strip())[:40], "schema.org JSON-LD telephone on %s" % pg if d.get("jsonld_phone") else "tel: link on %s" % (d.get("tel_links_url") or d.get("website") or "the organisation's site")); n_ox[side + "_phone_v2"] += 1
    acol = "buyer_address" if side == "buyer" else "vendor_address"
    if (not x.get(acol) or x.get(acol) in ("{}", "[]")) and d.get("jsonld_address"):
        _ja = d["jsonld_address"][:160]
        if side == "vendor" and not in_canada_text(_ja) and (_US_ZIP.search(_ja) or re.search(r",\s*(?:US|USA|United States|GB|UK|United Kingdom|FR|France|DE|Germany|AU|Australia|IN|India|NL|IE|CH|SE|FI|JP|CN)\s*$", _ja)):
            n_ox["vendor_address_v2_outside_canada_not_taken"] += 1  # the group's address in its page source, not the Canada-located vendor's (see "where an address is")
        else:
            x[acol] = "%s (schema.org JSON-LD PostalAddress on %s)" % (_ja, pg); n_ox[side + "_address_v2"] += 1
    tid = re.sub(r"\D", "", d.get("jsonld_tax_id") or "")
    bcol = "buyer_bn_as_published" if side == "buyer" else "vendor_bn9"
    if not x.get(bcol) and len(tid) >= 9 and tid[:9] != "000000000" and not re.fullmatch(r"(\d)\1{8}", tid[:9]) and re.search(r"\d{9}\s?(?:RT|RR|RP|RC)?", d.get("jsonld_tax_id") or ""):
        x[bcol] = "%s (schema.org JSON-LD taxID \"%s\" on %s)" % (tid[:9], (d.get("jsonld_tax_id") or "")[:30], pg); n_ox[side + "_bn_jsonld"] += 1
        gcol = "buyer_gst_hst_derived" if side == "buyer" else "vendor_gst_hst_derived"
        if not x.get(gcol):
            x[gcol] = tid[:9] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"
    if d.get("linkedin_url"):
        x[pre + "linkedin_url"] = d["linkedin_url"]
    if side == "vendor":
        if d.get("jsonld_founding_date") and not x.get("vendor_founded"):
            x["vendor_founded"] = "%s (schema.org JSON-LD foundingDate on %s)" % (d["jsonld_founding_date"], pg)
        if d.get("jsonld_employees") and not x.get("vendor_employees"):
            x["vendor_employees"] = "%s (schema.org JSON-LD numberOfEmployees on %s)" % (d["jsonld_employees"], pg)
        if d.get("jsonld_naics"):
            x["vendor_industry_naics"] = "%s (schema.org JSON-LD naics on %s)" % (d["jsonld_naics"], pg)
    else:
        ports = d.get("portals") or []
        if ports:
            x["buyer_supplier_portals_linked"] = "; ".join("%s (%s): %s" % (q["name"], q["kind"], q["url"]) for q in ports)[:600]
            if not x.get("ap_system_hint"):
                x["ap_system_hint"] = "linked from the buyer's site: " + "; ".join("%s (%s)" % (q["name"], q["kind"]) for q in ports)[:220]; n_ox["ap_system_hint_links"] += 1
            inv = next((q for q in ports if PORTAL_INVOICING.search(q["kind"])), None)
            if inv and not x.get("invoice_portal_url"):
                x["invoice_portal_url"] = inv["url"]; x["invoice_portal_kind"] = "%s (%s), linked from %s" % (inv["name"], inv["kind"], inv.get("on_page") or "the buyer's site"); n_ox["invoice_portal_links"] += 1
        for k, col in (("payment_method", "buyer_payment_method_preference"), ("tax_exempt", "buyer_tax_exempt_status"), ("esignature", "buyer_esignature_preference"), ("ap_cycle", "buyer_ap_cycle_published")):
            m = (d.get("mentions") or {}).get(k)
            if m and not x.get(col):
                # reviewer 2026-11-08: "interacting with the Sites", DMCA boilerplate — the mention must be a real term in a payables / supplier context
                ctx = (m.get("quote") or "") + " " + (m.get("text") or "")
                if not MENTION_STRICT[k].search(m.get("text") or "") or not MENTION_CTX.search(ctx) or MENTION_NOISE.search(ctx):
                    n_ox[col + "_mention_rejected"] += 1
                    continue
                x[col] = "%s (mentioned on %s)" % (m["text"][:160], m.get("url") or "the buyer's site"); n_ox[col + "_mention"] += 1
# counted on the names of every organisation whose site was read (the same list whatever part of the table this process ranks), not on the rows
_wdf, _wn = collections.Counter(), {norm(_d.get("name") or "") for _d in OX.values()} - {""}
for _nm in _wn:
    _wdf.update(set(_t for _t in _nm.split() if len(_t) >= 3))
WORD_COMMON = {w for w, c in _wdf.items() if c > max(40, len(_wn) // 2000)}
del _wdf
# a name that the readers found on three or more different sites is a programme, an association, a franchisor, a trademark owner — not the
# legal name of each of those sites (counted on every site read, not only on the rows)
_NAME_SITES, _cl = collections.defaultdict(set), {}
for _d in OX.values():
    _dm = registrable(host_of(_d.get("website") or "")) or _d.get("domain") or ""
    for _k in ("legal_name_stated", "jsonld_legal_name", "jsonld_name", "legal_name", "legal_name_party", "legal_name_operator"):
        _raw = _d.get(_k) or ""
        if _raw:
            if _raw not in _cl:
                _cl[_raw] = norm(clean_legal(_raw))
            if _cl[_raw]:
                _NAME_SITES[_cl[_raw]].add(_dm)
NAME_ON_MANY = {n for n, ds in _NAME_SITES.items() if len(ds) >= 3}
del _NAME_SITES, _cl
_OPERATOR_BEFORE = re.compile(r"(?:(?:(?:owned and )?operated|owned|published)\s+by|a (?:division|subsidiary) of|exploit[ée]e?s?\s+par|d[ée]tenue?s?\s+par|[ée]dit[ée]e?s?\s+par|(?:la |est )propri[ée]t[ée]\s+(?:exclusive\s+)?de|"
                              r"une (?:division|filiale) de)\s*:?\s*(?:the\s+|la\s+|le\s+|l['’]\s*)?[\"“«]?\s*$", re.I)
_WE_AFTER = re.compile(r"\s*[.,]?\s*\((?:hereinafter\s+|ci-apr[èe]s\s+)?[\"“«'‘]?\s*(?:we|us|our|nous|notre|the company|la soci[ée]t[ée]|l['’]entreprise)\b", re.I)
_LEGAL_PERSON = re.compile(r"\b(?:inc|incorporated|incorpor[ée]e|ltd|limited|lt[ée]e|limit[ée]e|llc|llp|l\.?p|corp|corporation|s\.?\s?a|s\.?a\.?r\.?l|s\.?e\.?n\.?c(?:\.?r\.?l)?|enr|ulc|plc|gmbh|"
                           r"society|soci[ée]t[ée]|association|foundation|fondation|coop[ée]rative|co-operative|organization|organisation|university|universit[ée]|college|coll[èe]ge|"
                           r"council|conseil|authority|commission|institute|institut|centre|center|church|[ée]glise|club|federation|f[ée]d[ée]ration|trust|board|bureau|office)\b\.?", re.I)
_PLATFORM_CO = re.compile(r"\b(?:odoo|shopify|wix|squarespace|godaddy|weebly|webflow|lightspeed|bigcommerce|automattic|wordpress|jimdo|duda|square|stripe|paypal|google|meta platforms|facebook|"
                          r"mailchimp|intuit|hubspot|cloudflare|amazon|microsoft|apple|ecwid|wordfence|mindbody|vagaro|jane software|growthzone|chambermaster|wild apricot|personify|"
                          r"civicplus|granicus|esolutions|blackbaud|eventbrite|ticketmaster|vimeo|youtube|linkedin|instagram|tiktok|twitter|yelp|tripadvisor|opentable|doordash|uber)\b", re.I)
_CORP_FORM_END = re.compile(r"(?:\b(?:inc|incorporated|incorpor[ée]e|ltd|limited|lt[ée]e|limit[ée]e|corp|corporation|llp|llc|ulc|plc|gmbh|senc|sencrl)\b\.?|\bL\.L\.P\.?|\bS\.E\.N\.C\.(?:R\.L\.)?)\s*$", re.I)
_LF_WORDS = {"inc", "incorporated", "incorporee", "ltd", "limited", "ltee", "limitee", "corp", "corporation", "llp", "llc", "ulc", "the", "la", "le", "les", "l", "of", "de", "du", "des", "d", "and", "et"}
def same_legal_name(a, b):
    """two printings of one legal name: the same words, legal-form words and articles aside; a register's two-language name ("X / Y") agrees by either half"""
    ta = [t for t in norm(a).split() if t not in _LF_WORDS]
    if not ta:
        return False
    return any(ta == [t for t in norm(part).split() if t not in _LF_WORDS] for part in [b] + re.split(r"\s*/\s*", b or ""))
_PAGE_NAME = re.compile(r"\((?:stated on|printed with its legal form|schema\.org|the copyright line of)")
def register_name_takes(cell, reg_name):
    """a register's name takes an empty cell, and the cell of a name read off the organisation's pages when it is the same name (the register's
    printing, with its source, replaces the page's)"""
    return not cell or bool(_PAGE_NAME.search(cell) and same_legal_name(re.sub(r"\s*\([^()]*(?:\([^()]*\)[^()]*)*\)\s*$", "", cell), reg_name))
# a web agency that runs its clients' sites ("This website is operated by Dr. Marketing Inc." on a dental practice's terms page) is not the practice
_AGENCY_CO = re.compile(r"\b(?:marketing|media|m[ée]dias?|web|design|digital|num[ée]rique|agency|agence|studios?|creative|cr[ée]ati(?:f|ve|on)s?|communications?|hosting|h[ée]bergement|interactive|interactif|seo|"
                        r"advertising|publicit[ée]|branding|graphi\w+|internet|online|software|logiciels?|technolog\w+|consult\w+|solutions?|it)\b", re.I)
def stated_as_operator(raw, quote, page="", site=""):
    """the page says in so many words that this name runs the site: "This website is operated by 9123-4567 Québec inc.", "Acme Holdings Ltd. («we»)".
    Such a statement ties the name to the site by itself — a numbered company shares no word with the name it trades under — when it is made on
    the row's own site, names a legal person (a company, an association: "owned and operated by Darren and his family" names nobody we print)
    and is not a web platform's own terms ("operated by Odoo S.A")."""
    q, r = re.sub(r"\s+", " ", quote or ""), re.sub(r"\s+", " ", raw or "").strip()
    i = q.lower().find(r.lower()) if len(r) >= 4 else -1
    if i < 0 or not (_LEGAL_PERSON.search(r) or _NUMBERED_CO.search(r)) or _PLATFORM_CO.search(r):
        return False
    if page and site and registrable(host_of(page) or "") != registrable(host_of(site) or ""):
        return False  # "Coast Hotels Limited", stated on coasthotels.com, for the hotel it manages
    return bool(_OPERATOR_BEFORE.search(q[max(0, i - 70):i]) or _WE_AFTER.match(q[i + len(r):i + len(r) + 60]))
_DBA = re.compile(r"\s*,?\s+(?:doing business as|operating as|carrying on business as|trading as|faisant affaires? sous(?: le nom(?: de)?)?|o/a|d\.?b\.?a\.?)\s+", re.I)
_DIV_OF = re.compile(r"\s*,?\s+(?:is\s+|est\s+)?(?:a|an|une)\s+(?:division|business unit|subsidiary|filiale|initiative|program(?:me)?|service)\s+(?:of|de|du|de la|d['’])\s*(?:the\s+|la\s+|le\s+)?", re.I)
_PUBLIC_BODY_WORD = re.compile(r"\b(?:municipality|municipalit[ée]|ville|city|town|township|county|district|village|government|gouvernement|minist[èe]re|ministry|hospital|h[ôo]pital|"
                               r"school|[ée]cole|library|biblioth[èe]que|nation|band)\b", re.I)
_GENERIC_CO_WORD = set("technologies technology solutions services service systems enterprises entreprises holdings group groupe consulting management gestion industries international canada global "
                       "media digital communications ventures partners associates properties investments capital company compagnie software networks labs studio studios design marketing "
                       "construction logistics trading development developments resources realty the les and et of de".split())
def generic_only_name(n):
    """ "Technologies Inc.", "Services Ltd.": the tail of a name whose first word the reader did not take ("easyDNS Technologies Inc." — a word that
    begins with a small letter), not a name"""
    w = [t for t in re.findall(r"[a-zà-ÿ0-9]+", _CORP_FORM_END.sub("", n or "").lower())]
    return bool(w) and len(w) <= 3 and all(t in _GENERIC_CO_WORD for t in w)
def legal_and_trade(cand):
    """(legal person, name traded under) when a stated name holds both: "X Ltd doing business as Y", "Y, a division of X"; else None"""
    m = _DBA.search(cand)
    if m:
        legal, trade = cand[:m.start()].strip(" ,"), cand[m.end():].strip(" ,")
    else:
        m = _DIV_OF.search(cand)
        if not m:
            return None
        trade, legal = cand[:m.start()].strip(" ,"), cand[m.end():].strip(" ,")
    if len(legal) >= 4 and len(trade) >= 3 and (_LEGAL_PERSON.search(legal) or _NUMBERED_CO.search(legal) or _PUBLIC_BODY_WORD.search(legal)):
        return legal, trade
    return None
def others_name(cand, x):
    """the candidate is printed on three or more sites, and nothing but common words ties it to this organisation: it is not its own name, nor
    the start of it, nor what its address spells, and the two share no word that few names carry"""
    nc = norm(cand)
    if nc not in NAME_ON_MANY:
        return False
    nb = norm(x.get("buyer") or "")
    if nb == nc or nb.startswith(nc + " ") and not re.match(r"(?:for|of|pour|de|des|du|in|and|et)\b", nb[len(nc) + 1:]):
        return False
    if any(len(t) >= 3 and t not in WORD_COMMON and t not in NAME_STOP and t not in GENERIC_ORG and t not in _NATIONAL for t in set(nc.split()) & set(nb.split())):
        return False
    hl = _host_label(x.get("buyer_website") or "")
    return not (hl and label_from_words(cand, hl))
print("words too common to prove a name (in more than 1 in 2,000 of the %d names of organisations whose site was read): %d; names printed on 3+ sites: %d" % (len(_wn), len(WORD_COMMON), len(NAME_ON_MANY)))
del _wn
_GOV_SITE = re.compile(r"(?:^|\.)(?:gov\.[a-z]{2}\.ca|gc\.ca|canada\.ca|alberta\.ca|ontario\.ca|gouv\.qc\.ca|quebec\.ca|gnb\.ca|novascotia\.ca|saskatchewan\.ca|manitoba\.ca|yukon\.ca|princeedwardisland\.ca|"
                       r"gov\.nl\.ca|gov\.nt\.ca|gov\.nu\.ca|[a-z]{2}\.gov|gov\.[a-z]{2,3}|gov)$")
def own_name_plainly(ln, org, site):
    """a copyright-line name that needs no shared distinctive word: it is the organisation's name itself (name_overlap refuses "Salt Spring Cookie
    Co" for the word cookie), its initials are the organisation's name or its address ("Canadian Association of Farm Advisors" for CAFA), or it
    is the government whose own site this office is on ("Government of British Columbia" for a ministry on www2.gov.bc.ca)"""
    a, b_ = norm(ln), norm(org)
    if a and (a == b_ or (len(a) >= 8 and b_.startswith(a + " ")) or (len(b_) >= 8 and a.startswith(b_ + " "))):
        return True
    words = [w for w in re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", ln or "").encode("ascii", "ignore").decode().lower()) if w not in _INI_STOP]
    ini = "".join(w[0] for w in words)
    if len(ini) >= 3 and ini in (re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", org or "").encode("ascii", "ignore").decode().lower()), _host_label(site) or "-"):
        return True
    return bool(re.match(r"(?:government|gouvernement)\s+(?:of|du|de)\b", ln or "", re.I) and _GOV_SITE.search(host_of(site or "") or "") and not _OWN_PERSON.search(org or ""))
_DBG_NAMES = open(os.environ["RANK_DEBUG_NAMES"], "w", encoding="utf-8") if os.environ.get("RANK_DEBUG_NAMES") else None  # debug only: the names the copyright rule takes and leaves
def _dbg_name(what, org, name, site):
    if _DBG_NAMES:
        _DBG_NAMES.write("%s\t%s\t%s\t%s\n" % (what, (org or "")[:60], (name or "")[:80], (site or "")[:60]))
def copyright_company(n):
    """a copyright line's name that may stand although it shares no word with the site's name: a short company name that ends with its legal
    form, not an agency's, not a platform's, not a name printed on three sites and more, with no sign of the page's own words around it"""
    return bool(n and (_CORP_FORM_END.search(n) or _NUMBERED_CO.search(n)) and len(n.split()) <= 7 and re.match(r"[A-ZÀ-Ý0-9]", n) and not _AGENCY_CO.search(n) and not _PLATFORM_CO.search(n)
                and norm(n) not in NAME_ON_MANY and not re.match(r"[A-Z][A-Za-z .'-]{2,30}, [A-Z]{2} ", n)
                and not re.search(r"[®™:;!?]|\b(?:subsidiary|division|member|part|affiliate|trademark|marque|filiale) (?:of|de|du)\b|\bwebmaster\b|\b(?:home|about|contact|menu|browse|links|disclaimer)\b", n, re.I))
_LEAD_DATE = re.compile(r"^\d{1,2}[./-]\d{1,2}[./-](?:19|20)?\d\d\s+(?=[A-Za-zÀ-ÿ0-9])")
n_ox = collections.Counter()
for x in rows:
    for col in ("buyer_legal_name_as_published", "buyer_bn_as_published", "buyer_gst_hst_derived", "buyer_logo_url", "buyer_website_status",
                "vendor_trading_name", "vendor_neq", "vendor_qst_as_published", "vendor_logo_url", "vendor_website_status", "payment_terms_as_published", "po_required_as_published"):
        x.setdefault(col, "")
    b, bo = ox_of(x.get("buyer_website"), x.get("buyer") or ""), oc_of(x.get("buyer_website"), x.get("buyer") or "")
    if b:
        ln = clean_legal(b.get("legal_name"), x.get("buyer") or "")
        if ln and credit_of_a_government(ln, x.get("buyer") or ""):
            ln = ""; n_ox["buyer_legal_name_government_template_credit"] += 1
        if ln and re.search(r"independently owned|ind[ée]pendamment d[ée]tenu|propri[ée]t[ée] ind[ée]pendante|franchis[ée]e? ind[ée]pendant", b.get("legal_name_quote") or "", re.I) and not name_overlap(ln, x.get("buyer") or "", x.get("buyer_website") or ""):
            ln = ""; n_ox["buyer_legal_name_franchisor_copyright_not_taken"] += 1  # "Each Best Western® branded hotel is independently owned and operated. © Best Western International, Inc."
        # 2026-11-11 (rows read before the owner's test set went out; 37,221 names came from a copyright line, 2,701 of them shared nothing with
        # the organisation's name or address): such a line named the legal person about one time in two ("Soccer World" © HamOnt Sports Limited)
        # — otherwise the site's maker ("Jumptools® Inc", "Ta Gueule Communications inc"), a picture's owner ("Peanuts Worldwide LLC"), a parent,
        # or a run of the page's own words ("Disclaimer Browse Home Municipal Office Services Dep"). That name now waits: what the site states in
        # so many words goes first, and it is taken last, only as a short company name with its legal form, and the cell says what it rests on.
        _cp_last = ""
        if ln and not name_overlap(ln, x.get("buyer") or "", x.get("buyer_website") or "") and not own_name_plainly(ln, x.get("buyer") or "", x.get("buyer_website") or ""):
            if copyright_company(ln) and norm(ln) != norm(x.get("vendor") or "") and registrable(host_of(b.get("legal_name_url") or "") or "") == registrable(host_of(x.get("buyer_website") or "") or "-"):
                _cp_last = ln  # printed on the organisation's own domain: a donation or booking page on a platform's host carries the platform's line
                _dbg_name("buyer kept", x.get("buyer"), ln, x.get("buyer_website"))
            else:
                n_ox["buyer_legal_name_copyright_line_shares_nothing_with_the_name_not_taken"] += 1
                _dbg_name("buyer left", x.get("buyer"), ln, x.get("buyer_website"))
            ln = ""
        basis = "the site's copyright / footer line"
        # v3 (2026-11-10, tools/org_extras.py): the name the site prints WITH its legal form and that its own domain name spells ("Credit Lift Inc." on
        # creditlift.ca, "Autoénergie Canada inc." on autoenergie.com). Measured on 324 sites: where it differed from the name the older readers held
        # (15 times), it was right 14 times — so it goes first, except before a copyright line that itself carries a company form.
        _site = x.get("buyer_website") or ""
        _own = lambda u: bool(u) and registrable(host_of(u) or "") == registrable(host_of(_site) or "")
        _sp = re.sub(r"\s+", " ", b.get("legal_name_spelled") or "").strip() if int(b.get("legal_name_spelled_v") or 0) >= 4 else ""  # the reader's v3 (three hours of 2026-11-11) took 7 % names cut short or run into the page's words; the name says which version took it (a v3 name used to stay in a record v4 had re-read)
        _reg_cell = bool(x.get("buyer_legal_name_as_published"))  # a public register has named the legal person already (apply_details): what the site prints does not replace it
        if _sp and not _reg_cell and not (ln and (_CORP_FORM_END.search(ln) or _LEGAL_PERSON.search(ln))) and not _PLATFORM_CO.search(_sp) and name_overlap(_sp, x.get("buyer") or "", _site):
            ln = _sp
            basis = "printed with its legal form on %s; %s" % (b.get("legal_name_spelled_url") or "the organisation's site", re.sub(r"\s*\(([^()]*)\)", r", \1", b.get("legal_name_spelled_basis") or "its words spell the site's own domain name"))
            n_ox["buyer_legal_name_v3_spelled_by_the_domain"] += 1
        if not ln and not _reg_cell:
            # the legal person a page of the site puts behind the site's own name: "Majid Enterprises Inc., operating as Lawn Lovers", "Solaris (1457570
            # Alberta Ltd.)", "Legal Entity : Sleepera Mattress Wholesale Ltd." — not a name printed on three sites and more (a maker's notice on its
            # dealers' sites, a platform's terms), unless it is this organisation's own
            _pn, _pt, _ph = _LEAD_DATE.sub("", re.sub(r"\s+", " ", b.get("legal_name_party") or "").strip()), (b.get("legal_name_party_trade") or "").strip(), b.get("legal_name_party_how") or ""
            if _pn and not generic_only_name(_pn) and not _PLATFORM_CO.search(_pn) and _own(b.get("legal_name_party_url")) and (not (norm(_pn) in NAME_ON_MANY or _AGENCY_CO.search(_pn)) or name_overlap(_pn, x.get("buyer") or "", _site)) and (
                    name_overlap(_pt, x.get("buyer") or "", _site) if _pt else _ph.startswith(("labelled", "named with its legal form under the label"))):
                ln = _pn
                basis = (("stated on %s: %s “%s”, as the legal person doing business under the site's name" % (b.get("legal_name_party_url"), _ph, _pt)) if _pt else
                         ("stated on %s: %s, as the site's operator" % (b.get("legal_name_party_url"), _ph)) if _ph.startswith("named with its legal form") else
                         ("stated on %s: labelled there as the legal entity, as the site's operator" % b.get("legal_name_party_url")))
                n_ox["buyer_legal_name_v3_legal_person_behind_the_site_name"] += 1
        if not ln and not _reg_cell:
            _on = _LEAD_DATE.sub("", re.sub(r"\s+", " ", b.get("legal_name_operator") or "").strip())
            if _on and not generic_only_name(_on) and (not (norm(_on) in NAME_ON_MANY or _AGENCY_CO.search(_on)) or name_overlap(_on, x.get("buyer") or "", _site)) and stated_as_operator(_on, b.get("legal_name_operator_quote"), b.get("legal_name_operator_url") or "", _site):
                ln, basis = _on, "stated on %s, as the site's operator" % (b.get("legal_name_operator_url") or "the site's legal page")
                n_ox["buyer_legal_name_v3_stated_as_operator"] += 1
        if not ln:  # v2 (2026-11-08): the name the organisation states itself — schema.org JSON-LD legalName, then its Terms / Privacy / Legal page
            for k, lab in (("jsonld_legal_name", "schema.org JSON-LD legalName on %s" % (b.get("jsonld_page") or "the site")), ("legal_name_stated", "stated on %s" % (b.get("legal_name_stated_url") or "the site's legal page")),
                           ("jsonld_name", "schema.org JSON-LD Organization name on %s" % (b.get("jsonld_page") or "the site"))):
                cand = clean_legal(b.get(k) or "", x.get("buyer") or "")
                if cand and others_name(cand, x):
                    n_ox["buyer_legal_name_v2_printed_on_many_sites"] += 1  # "Canadian Dental Care", "Ontario Dental Association", "Canadian Real Estate Association"
                    continue
                _two = legal_and_trade(cand) if cand else None
                if _two and name_overlap(_two[1], x.get("buyer") or "", x.get("buyer_website") or ""):
                    # "Hiwachka Enterprises LTD doing business as Steady Effort Yoga", "MOPC Network, a division of the Municipality of Pictou County":
                    # one of the two names is the site's, the other is its legal person
                    ln, basis = _two[0], lab + ", as the legal person doing business under the site's name"; n_ox["buyer_legal_name_v2_doing_business_as"] += 1
                    break
                if cand and (k != "jsonld_name" or LEGAL_FORMISH.search(cand)) and name_overlap(cand, x.get("buyer") or "", x.get("buyer_website") or ""):
                    ln, basis = tight_name(cand, x.get("buyer_website") or ""), lab; n_ox["buyer_legal_name_v2_" + k] += 1
                    break
                if cand and k.startswith("jsonld") and (_LEGAL_PERSON.search(cand) or _NUMBERED_CO.search(cand)) and b.get("jsonld_url") and host_of(b["jsonld_url"]) == host_of(x.get("buyer_website") or ""):
                    # 2026-11-11: a legal person's name only. Without a word shared with the site's name, the node's own address was all that tied it to
                    # the organisation, and a node of an events page ("Kennetcook District Fire Hall" on a municipality's site) or a person's first
                    # name ("Daryl", "Direction") passed: 373 of 852 such names shared nothing with the row's name.
                    # the site's own structured statement about itself: the node gives this very site as the organisation's address
                    ln, basis = cand, lab + ", which gives this site as the organisation's own"; n_ox["buyer_legal_name_v2_" + k + "_own_site_node"] += 1
                    break
                if cand and k == "legal_name_stated" and stated_as_operator(b.get(k), b.get("legal_name_stated_quote"), b.get("legal_name_stated_url") or "", x.get("buyer_website") or ""):
                    ln, basis = cand, lab + ", as the site's operator"; n_ox["buyer_legal_name_v2_stated_as_operator"] += 1
                    break
                elif cand:
                    n_ox["buyer_legal_name_v2_rejected_no_overlap"] += 1  # reviewer 2026-11-08: "Internet Protocol", "Ville de Granby" on another body's site
        if not ln and _cp_last and not _reg_cell:
            ln, basis = _cp_last, "the copyright line of %s names this company; it shares no word with the site's name: taken as the company behind it on that line alone" % (b.get("legal_name_url") or "the organisation's site")
            n_ox["buyer_legal_name_copyright_line_company_behind_the_site_name"] += 1
        if ln and (x.get("keys") or "").split("|")[0] in REG_NAMED and x.get("buyer_legal_name_as_published"):
            ln = ""; n_ox["buyer_legal_name_kept_from_the_trademarks_register"] += 1
        if ln:
            # 2026-11-12: every name says where it was read — the copyright line's page too (21,752 ready rows carried a bare name)
            x["buyer_legal_name_as_published"] = "%s (%s)" % (ln, ("the copyright line of %s" % (b.get("legal_name_url") or x.get("buyer_website") or "the organisation's site"))
                                                             if basis.startswith("the site's copyright") else basis); n_ox["buyer_legal_name"] += 1
            if (GENERIC_NAME.match(x.get("buyer") or "") or DOMAIN_NAME.match(x.get("buyer") or "")) and not basis.startswith("the copyright line of"):
                x["buyer"] = ln; n_ox["p13_name_from_legal_name"] += 1  # the crawler only had the site's domain or a page title
        v2_fill(x, b, "buyer")
        if b.get("bn") and bn_ok(b):
            x["buyer_bn_as_published"] = "%s %s (as printed: %s; %s)" % (b["bn"], b.get("bn_program") or "", b.get("bn_label") or "", b.get("bn_url") or "")
            x["buyer_gst_hst_derived"] = b["bn"] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"; n_ox["buyer_bn"] += 1
        if b.get("logo_url"):
            x["buyer_logo_url"] = b["logo_url"]; n_ox["buyer_logo"] += 1
        if not x.get("language_hint") and b.get("language"):
            x["language_hint"] = b["language"]
    if bo and bo.get("status"):
        x["buyer_website_status"] = SITE_STATUS.get(bo["status"], bo["status"])
    if x.get("tier") == "I" and GENERIC_NAME.match(x.get("buyer") or ""):  # "Contactez-nous", "Home": the mailbox's domain names the body better
        x["buyer"] = (x.get("email") or "").split("@")[-1] or x["buyer"]; n_ox["p13_name_from_domain"] += 1
    v, vo = ox_of(x.get("vendor_website"), x.get("vendor") or ""), oc_of(x.get("vendor_website"), x.get("vendor") or "")
    _foreign_site = bool(v) and site_not_the_vendors_own(x.get("vendor_website"))
    if _foreign_site:
        n_ox["vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor"] += 1
    if v and not _foreign_site and DOMAIN_NAME.match((x.get("vendor") or "").strip()) and (v.get("og_site_name") or v.get("title")):
        # 2026-11-11: a vendor known by its domain only ("whc.ca", 7,333 rows of the build of 01:51Z; "business.nvchamber.ca") is printed under the name
        # its own home page gives it, when that name agrees with the domain ("Web Hosting Canada"); the domain stays in vendor_website
        _vsn = _LCF.site_name_for(host_of(x.get("vendor_website") or "") or x["vendor"].strip().lower(), v.get("og_site_name"), v.get("title"), _TR)
        if _vsn and not DOMAIN_NAME.match(_vsn) and not GENERIC_NAME.match(_vsn):
            x["vendor"] = _vsn; n_ox["vendor named by its own site's name instead of its domain"] += 1
    elif v and re.search(r"\s(?:l|d|qu|n|s|j|c)$", (x.get("vendor") or "").strip(), re.I):
        # 2026-11-11 (test set: "Chambre de Commerce de l"): a name the lead engine cut at an apostrophe — the value of the site's og:site_name was
        # read up to the first quote of either kind (63 names, 900 leads; the engines are corrected) — is completed from the vendor's own home
        # page when a name there begins with the same words
        _cut = (x.get("vendor") or "").strip()
        for _full in (html.unescape(str(v.get("og_site_name") or "")).strip(), html.unescape(str(v.get("title") or "")).split("|")[0].strip()):
            if len(_full) > len(_cut) + 1 and norm(_full).startswith(norm(_cut)) and _full[len(_cut):len(_cut) + 1] in "'’":
                x["vendor"] = re.split(r"\s+[|–—-]\s+", _full)[0].strip()[:90]; n_ox["vendor name cut at an apostrophe, completed from its own home page"] += 1
                break
    if v and not (x.get("vendor") or "").startswith("inferred"):
        _vcp = "" if x.get("vendor_legal_name") or (_foreign_site and not in_ca_section(v.get("legal_name_url") or "")) else clean_legal(v.get("legal_name"), x.get("vendor") or "")
        _vcp_last = ""
        if _vcp and not name_overlap(_vcp, x.get("vendor") or "", x.get("vendor_website") or "") and not own_name_plainly(_vcp, x.get("vendor") or "", x.get("vendor_website") or ""):  # 2026-11-11: as for the buyer's copyright line above
            if copyright_company(_vcp) and norm(_vcp) != norm(x.get("buyer") or "") and registrable(host_of(v.get("legal_name_url") or "") or "") == registrable(host_of(x.get("vendor_website") or "") or "-"):
                _vcp_last = _vcp  # "SofterWare, Inc" on a charity's donation page hosted by that company is not the charity's legal name
                _dbg_name("vendor kept", x.get("vendor"), _vcp, x.get("vendor_website"))
            else:
                n_ox["vendor_legal_name_copyright_line_shares_nothing_with_the_name_not_taken"] += 1
                _dbg_name("vendor left", x.get("vendor"), _vcp, x.get("vendor_website"))
            _vcp = ""
        if _vcp:
            x["vendor_legal_name"] = _vcp + " (as printed on the vendor's site: %s)" % (v.get("legal_name_url") or ""); n_ox["vendor_legal_name"] += 1
        if v.get("neq"):
            x["vendor_neq"] = "%s (as printed: %s)" % (v["neq"], v.get("neq_url") or ""); n_ox["vendor_neq"] += 1
        if v.get("qst"):
            x["vendor_qst_as_published"] = "%s (as printed: %s)" % (v["qst"], v.get("qst_url") or ""); n_ox["vendor_qst"] += 1
        if not x.get("vendor_bn9") and v.get("bn") and bn_ok(v):
            x["vendor_bn9"] = v["bn"] + " (as printed on the vendor's site: %s)" % (v.get("bn_url") or "")
            x["vendor_gst_hst_derived"] = v["bn"] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"; n_ox["vendor_bn"] += 1
        if v.get("logo_url"):
            x["vendor_logo_url"] = v["logo_url"]; n_ox["vendor_logo"] += 1
        if not x.get("vendor_legal_name"):
            for k, lab in (("jsonld_legal_name", "schema.org JSON-LD legalName"), ("legal_name_stated", "stated on the vendor's legal page")):
                if _foreign_site and not in_ca_section((v.get("jsonld_page") if k.startswith("jsonld") else v.get("legal_name_stated_url")) or ""):
                    continue  # the group's own statement on its worldwide pages; a page of its Canadian section may name the Canadian entity
                cand = clean_legal(v.get(k) or "", x.get("vendor") or "")
                if cand and name_overlap(cand, x.get("vendor") or "", x.get("vendor_website") or ""):
                    x["vendor_legal_name"] = "%s (%s: %s)" % (tight_name(cand, x.get("vendor_website") or ""), lab, v.get("jsonld_page") if k.startswith("jsonld") else v.get("legal_name_stated_url") or ""); n_ox["vendor_legal_name_v2"] += 1
                    break
                if cand and ((k == "jsonld_legal_name" and v.get("jsonld_url") and host_of(v["jsonld_url"]) == host_of(x.get("vendor_website") or "")) or
                             (k == "legal_name_stated" and stated_as_operator(v.get(k), v.get("legal_name_stated_quote"), v.get("legal_name_stated_url") or "", x.get("vendor_website") or ""))):
                    # the vendor's own site says it in so many words: its structured data gives the site as the organisation's own, or a page says who operates it
                    x["vendor_legal_name"] = "%s (%s: %s)" % (cand, lab + (", which gives this site as the organisation's own" if k.startswith("jsonld") else ", as the site's operator"), v.get("jsonld_page") if k.startswith("jsonld") else v.get("legal_name_stated_url") or ""); n_ox["vendor_legal_name_v2_site_says"] += 1
                    break
        if not x.get("vendor_legal_name") and not _foreign_site:
            # 2026-11-11: the reader's v4 names (see the buyer block above), for the vendor's own site — tier T rows of the build of 01:51Z: 52 % with
            # a vendor legal name (7,333 rows of one host, "whc.ca", without one)
            _vsite, _vn = x.get("vendor_website") or "", x.get("vendor") or ""
            _vown = lambda u: bool(u) and registrable(host_of(u) or "") == registrable(host_of(_vsite) or "")
            _vsp = re.sub(r"\s+", " ", v.get("legal_name_spelled") or "").strip() if int(v.get("legal_name_spelled_v") or 0) >= 4 else ""
            _vpn, _vpt, _vph = re.sub(r"\s+", " ", v.get("legal_name_party") or "").strip(), (v.get("legal_name_party_trade") or "").strip(), v.get("legal_name_party_how") or ""
            _von = re.sub(r"\s+", " ", v.get("legal_name_operator") or "").strip()
            if _vsp and not _PLATFORM_CO.search(_vsp) and name_overlap(_vsp, _vn, _vsite):
                x["vendor_legal_name"] = "%s (printed with its legal form on %s; %s)" % (_vsp, v.get("legal_name_spelled_url") or "the vendor's site", re.sub(r"\s*\(([^()]*)\)", r", \1", v.get("legal_name_spelled_basis") or "its words spell the site's own domain name"))
                n_ox["vendor_legal_name_v3_spelled_by_the_domain"] += 1
            elif _vpn and not generic_only_name(_vpn) and not _PLATFORM_CO.search(_vpn) and _vown(v.get("legal_name_party_url")) and (not (norm(_vpn) in NAME_ON_MANY or _AGENCY_CO.search(_vpn)) or name_overlap(_vpn, _vn, _vsite)) and (
                    name_overlap(_vpt, _vn, _vsite) if _vpt else _vph.startswith("labelled")):
                x["vendor_legal_name"] = ("%s (stated on %s: %s “%s”, as the legal person doing business under the site's name)" % (_vpn, v.get("legal_name_party_url"), _vph, _vpt)) if _vpt else (
                    "%s (stated on %s: labelled there as the legal entity, as the site's operator)" % (_vpn, v.get("legal_name_party_url")))
                n_ox["vendor_legal_name_v3_legal_person_behind_the_site_name"] += 1
            elif _von and not generic_only_name(_von) and (not (norm(_von) in NAME_ON_MANY or _AGENCY_CO.search(_von)) or name_overlap(_von, _vn, _vsite)) and stated_as_operator(_von, v.get("legal_name_operator_quote"), v.get("legal_name_operator_url") or "", _vsite):
                x["vendor_legal_name"] = "%s (stated on %s, as the site's operator)" % (_von, v.get("legal_name_operator_url") or "the site's legal page")
                n_ox["vendor_legal_name_v3_stated_as_operator"] += 1
        if not x.get("vendor_legal_name") and _vcp_last:
            x["vendor_legal_name"] = "%s (the copyright line of %s names this company; it shares no word with the vendor's name: taken as the company behind it on that line alone)" % (_vcp_last, v.get("legal_name_url") or "the vendor's site")
            n_ox["vendor_legal_name_copyright_line_company_behind_the_site_name"] += 1
        v2_fill(x, v, "vendor")
        if not x.get("vendor_trading_name") and not _foreign_site:  # 2026-11-08: the name the vendor trades under on its own site when it differs from its legal name (schema.org alternateName / Organization name)
            vl0 = (x.get("vendor_legal_name") or "").split(" (")[0].strip()
            for k, lab in (("jsonld_alternate_name", "schema.org alternateName on the vendor's site"), ("jsonld_name", "schema.org Organization name on the vendor's site")):
                cand = re.sub(r"\s+", " ", str(v.get(k) or "")).strip()
                if cand and vl0 and norm(cand) != norm(vl0) and len(cand) <= 80 and not LEGAL_FORMISH.search(cand) and name_overlap(cand, x.get("vendor") or "", x.get("vendor_website") or ""):
                    x["vendor_trading_name"] = "%s (%s: %s)" % (cand[:120], lab, v.get("jsonld_page") or ""); n_ox["vendor_trading_name_jsonld"] += 1
                    break
    if vo and vo.get("status") and not (x.get("vendor") or "").startswith("inferred"):
        x["vendor_website_status"] = SITE_STATUS.get(vo["status"], vo["status"])
    vl, vn = (x.get("vendor_legal_name") or "").split(" (as printed")[0], x.get("vendor") or ""
    if vl and vn and norm(vl) != norm(vn) and not vn.startswith("inferred"):
        x["vendor_trading_name"] = vn
    txt = " ".join((x.get(c) or "") for c in ("invoicing_requirements", "email_evidence_quote"))
    m = TERMS.search(txt)
    if m:
        x["payment_terms_as_published"] = flat_q(m.group(0))[:80]; n_ox["payment_terms"] += 1
    m = PO_REQ.search(txt)
    if m:
        x["po_required_as_published"] = "yes (as published: %s)" % flat_q(m.group(0))[:120]; n_ox["po_required"] += 1
print("org_extras: %d organisations read; filled %s" % (len(OX), dict(n_ox)))
# a regional mailbox of a multinational (invoices.aunz@, ap.emea@, ptvi.invoice@) is not the entity's own box unless the region is the buyer's
REGION_TOK = {"aunz": {"AU", "NZ"}, "anz": {"AU", "NZ"}, "apac": {"AU", "NZ", "SG", "JP", "IN", "CN", "HK", "MY", "PH"}, "emea": {"UK", "GB", "FR", "DE", "IE", "NL", "BE", "ES", "IT", "CH", "SE", "ZA", "AE"},
              "latam": {"MX", "BR", "AR", "CL", "CO"}, "uk": {"UK", "GB"}, "gb": {"UK", "GB"}, "usa": {"US"}, "us": {"US"}, "india": {"IN"}, "china": {"CN"}, "brasil": {"BR"}, "brazil": {"BR"},
              "mexico": {"MX"}, "france": {"FR"}, "germany": {"DE"}, "japan": {"JP"}, "singapore": {"SG"}, "australia": {"AU"}, "nz": {"NZ"}, "europe": {"UK", "GB", "FR", "DE", "IE", "NL", "BE", "ES", "IT", "CH", "SE"},
              "eu": {"UK", "GB", "FR", "DE", "IE", "NL", "BE", "ES", "IT", "CH", "SE", "EU", "DK", "FI", "NO", "AT", "PT", "PL", "LU"}, "asia": {"SG", "JP", "IN", "CN", "HK", "MY", "PH", "KR", "TH", "ID", "VN"}, "oceania": {"AU", "NZ"},
              "mena": {"AE", "SA", "QA", "EG", "KW", "BH", "OM", "JO", "MA"}, "nordic": {"SE", "NO", "DK", "FI", "IS"}, "nordics": {"SE", "NO", "DK", "FI", "IS"}, "benelux": {"BE", "NL", "LU"}, "canada": {"CA", "FED", "QC", "ON", "BC", "AB", "SK", "MB", "NS", "NB", "PE", "NL", "YT", "NT", "NU"},
              "asia": {"SG", "JP", "IN", "CN", "HK", "MY", "PH"}, "ptvi": {"ID"}, "indonesia": {"ID"}, "africa": {"ZA"}, "canada": {"CA"}, "ca": {"CA"}}
CA_PROV = {"ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "YT", "NT", "NU", "CA"}
n_reg = 0
for x in rows:
    e = (x.get("email") or "").lower()
    if not e:
        continue
    toks = [t for t in re.split(r"[._-]", e.split("@")[0]) if t]
    j = (x.get("jurisdiction") or "").upper()
    jset = {"CA"} if j in CA_PROV else {j}
    for t in toks:
        if t in REGION_TOK and t not in ("ca", "canada", "us", "usa") and not (REGION_TOK[t] & jset):
            for col in ("email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote", "ap_phone", "invoice_mailing_address",
                        "invoicing_requirements", "invoice_portal_url", "ap_contact_name_as_published"):
                x[col] = ""
            x["grade"], x["rank_group"], n_reg = 0, "%s0" % x.get("tier", ""), n_reg + 1
            break
        if t in ("us", "usa") and j in CA_PROV or (t in ("ca", "canada") and j and j not in CA_PROV):
            for col in ("email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote"):
                x[col] = ""
            x["grade"], x["rank_group"], n_reg = 0, "%s0" % x.get("tier", ""), n_reg + 1
            break
print("regional mailboxes of multinationals removed from other-country entities:", n_reg)
# a mailbox whose domain publishes no mail server (tools/mx_check.py, DNS only) cannot receive the survey: the row stays, without it
MX = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_mx_check.tsv"):
    for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_mx_check.tsv", encoding="utf-8"), delimiter="\t"):
        MX[r["domain"]] = r["status"]
FREEMAIL = re.compile(r"^(?:gmail|googlemail|hotmail|outlook|live|msn|yahoo|ymail|rocketmail|aol|icloud|me|mac|protonmail|proton|gmx|mail|yandex|zoho|hush|hushmail|fastmail|tutanota|tuta|pm)\.(?:com|ca|net|org|fr|me|co\.uk|de|ch)$", re.I)
n_mx = n_free = 0
for x in rows:
    e = (x.get("email") or "").lower()
    st = MX.get(e.split("@")[-1]) if e else None
    if e and FREEMAIL.match(e.split("@")[-1]):  # owner 2026-11-04 10:21 ("ironclad"): a webmail address is not an organisational mailbox, whoever publishes it
        for col in ("email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote", "ap_phone", "invoice_mailing_address",
                    "invoicing_requirements", "invoice_portal_url", "ap_contact_name_as_published"):
            x[col] = ""
        x["grade"], x["rank_group"], n_free = 0, "%s0" % x.get("tier", ""), n_free + 1
        continue
    if e and st == "none":
        for col in ("email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote", "ap_phone", "invoice_mailing_address",
                    "invoicing_requirements", "invoice_portal_url", "ap_contact_name_as_published"):
            x[col] = ""
        x["grade"], x["rank_group"], n_mx = 0, "%s0" % x.get("tier", ""), n_mx + 1
    elif e:
        x["email_deliverability"] = {"mx": "domain publishes a mail server (MX)", "a_only": "no MX record; A record only (deliverability uncertain)",
                                     "error": "DNS check failed; re-checked next run"}.get(st, "not checked yet")
print("mx_check: %d domains known; %d mailboxes on domains with no mail server removed; %d webmail (freemail) addresses removed" % (len(MX), n_mx, n_free))
# e-mail security posture of the mailbox's domain (owner 2026-11-04 10:45: DMARC / SPF in every row; tools/dmarc_check.py, DNS only)
MXH = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_mx_check.tsv"):
    for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_mx_check.tsv", encoding="utf-8"), delimiter="\t"):
        MXH[r["domain"]] = r.get("mail_hosts") or ""
DM = {}
_dm_need = None
if _PN > 1:  # ranking in parts: only the domains of this part's mailboxes (the rows' own, and every mailbox one of its organisations may still take)
    _dm_need = {b.split("@")[-1] for b in _PART_BOXES if "@" in b} | {(x.get("email") or "").lower().split("@")[-1] for x in rows if x.get("email")}
for r in _PCSV.rows(ROOT + "/data/incoming/claude/claude_dmarc_check.tsv", delimiter="\t"):  # written in parts (tools/dmarc_check.py)
    if _dm_need is None or r["domain"] in _dm_need:
        DM[r["domain"]] = r
PROVIDER = (("outlook.com|protection.outlook|mail.protection", "Microsoft 365"), ("google.com|googlemail|aspmx", "Google Workspace"), ("pphosted|proofpoint", "Proofpoint"),
            ("mimecast", "Mimecast"), ("barracuda", "Barracuda"), ("messagelabs|symantec|broadcom", "Symantec / Broadcom"), ("fortimail|fortinet", "Fortinet"),
            ("cisco|iphmx|ironport", "Cisco"), ("trendmicro", "Trend Micro"), ("mxlogic|mcafee", "McAfee"), ("secureserver|godaddy", "GoDaddy"), ("zoho", "Zoho"),
            ("mailgun|sendgrid|amazonses|awsapps|amazonaws", "Amazon / transactional"), ("ovh\\.net|ovh\\.ca", "OVH"), ("1and1|ionos|kundenserver", "IONOS"),
            ("emailsrvr|rackspace", "Rackspace"), ("hostinger|titan", "Titan / Hostinger"), ("videotron|bell\\.ca|bellnet|sympatico|telus|shaw\\.ca|rogers|cogeco|eastlink|sasktel|mts\\.net", "ISP mail"),
            ("icloud|me\\.com|yahoodns|yahoo|aol", "consumer webmail"), ("protonmail|proton\\.me", "Proton"), ("hostedemail|opensrs|tucows", "Tucows / OpenSRS"), ("websitewelcome|hostgator", "HostGator"),
            ("bluehost", "Bluehost"), ("dreamhost", "DreamHost"), ("siteground", "SiteGround"), ("cloudflare|mx\\.cloudflare", "Cloudflare"), ("registrar-servers|namecheap|privateemail", "Namecheap"),
            ("qq\\.com|163\\.com|aliyun", "Chinese provider"), ("mailbox\\.org|posteo", "German provider"))
def provider(hosts):
    h = (hosts or "").lower()
    for rx, name in PROVIDER:
        if re.search(rx, h):
            return name
    return ("self-hosted or other (%s)" % h.split(";")[0][:60]) if h and not h.startswith(("A", "AAAA")) else "no MX record" if h.startswith(("A", "AAAA")) else "not checked"
DMARC_LABEL = {"no_record": "no DMARC record", "none": "v=DMARC1; p=none (monitor only, no enforcement)", "quarantine": "p=quarantine", "reject": "p=reject",
               "invalid": "invalid DMARC record", "error": "DNS lookup failed"}
SPF_LABEL = {"hard_fail": "SPF -all (hard fail)", "soft_fail": "SPF ~all (soft fail)", "neutral": "SPF ?all (neutral)", "pass_all": "SPF +all (allows everyone)",
             "no_all": "SPF without an all mechanism", "no_record": "no SPF record", "error": "DNS lookup failed"}
n_dm = collections.Counter()
for x in rows:
    e = (x.get("email") or "").lower()
    d = e.split("@")[-1] if e else ""
    r = DM.get(d) or {}
    for col in ("dmarc_policy", "dmarc_record", "dmarc_record_domain", "spf_policy", "spf_record", "mail_provider", "email_security_posture", "dns_checked_date"):
        x.setdefault(col, "")
    if not e:
        continue
    pol, spfp = r.get("policy") or "", r.get("spf_policy") or ""
    x["dmarc_policy"] = DMARC_LABEL.get(pol, "not checked yet")
    x["dmarc_record"] = r.get("record") or ""
    x["dmarc_record_domain"] = r.get("record_domain") or ("" if pol in ("", "no_record") else d)
    x["spf_policy"] = SPF_LABEL.get(spfp, "not checked yet")
    x["spf_record"] = r.get("spf_record") or ""
    x["mail_provider"] = provider(MXH.get(d))
    x["dns_checked_date"] = r.get("checked_date") or ""
    if pol:
        exposed = pol in ("no_record", "none", "invalid")
        x["email_security_posture"] = ("EXPOSED to sender spoofing: %s" % x["dmarc_policy"] if exposed else "DMARC enforced: %s" % x["dmarc_policy"]) + \
                                      "; %s; mail handled by %s" % (x["spf_policy"], x["mail_provider"])
        n_dm["exposed" if exposed else "enforced"] += 1
print("dmarc/spf: %d domains known; rows %s" % (len(DM), dict(n_dm)))
used_mail = {}  # one delivered row per mailbox: buyers that share one mailbox (branches on a government's central box) are one contact point
def _site_dom(x):
    h = host_of(x.get("buyer_website") or "")
    return registrable(h) if h else ""
drop = set(); n_fold = 0
for i, x in enumerate(rows):
    e = (x.get("email") or "").lower()
    if not e:
        continue
    if e in used_mail:
        holder = used_mail[e]
        # the same organisation under another key or spelling (same website domain as the row that keeps the mailbox): one row, not a
        # mailbox-less duplicate (owner 2026-11-04 10:18 "all distinct buyers?"; e.g. "Township of Leeds and the Thousand Islands" twice)
        if _site_dom(x) and _site_dom(x) == _site_dom(holder) and _site_dom(x) == registrable(e.split("@")[-1]):
            hk = set((holder.get("keys") or "").split("|")); hk |= set((x.get("keys") or "").split("|"))
            holder["keys"] = "|".join(sorted(k for k in hk if k)); holder["buyer_keys"] = len([k for k in hk if k])
            try:
                holder["contracts_with_canadian_suppliers"] = max(int(holder.get("contracts_with_canadian_suppliers") or 0), int(x.get("contracts_with_canadian_suppliers") or 0))
            except (TypeError, ValueError):
                pass
            drop.add(i); n_fold += 1
            continue
        for col in ("email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote"):
            x[col] = ""
        x["grade"], x["rank_group"] = 0, "%s0" % x.get("tier", "")
        continue
    used_mail[e] = x
rows = [x for i, x in enumerate(rows) if i not in drop]
print("same organisation under another key folded into the row that holds its mailbox:", n_fold)
# second pass: two rows of ONE organisation with two different mailboxes (info@ and ap@ of the same body) — same site domain, same
# mail domain, same name family (first two significant words) — keep the better-graded / better-tiered row and carry the keys
STOP_W = {"the", "of", "de", "du", "des", "la", "le", "les", "and", "et", "for", "a", "an", "d", "l", "ville", "city", "town", "municipalite", "municipality", "county", "universite", "university", "college"}
def _fam(x):
    toks = [t for t in re.split(r"[^a-z0-9]+", norm(x.get("buyer") or "")) if t and t not in STOP_W]
    return " ".join(toks[:2])
TIER_RANK = {"A": 0, "B": 1, "T": 2, "M": 3, "C": 4, "D": 5, "L": 6, "E": 7, "R": 7.5, "F": 8, "I": 9}
groups = collections.defaultdict(list)
for x in rows:
    e = (x.get("email") or "").lower(); sd = _site_dom(x)
    if e and sd and sd == registrable(e.split("@")[-1]) and not SHARED_GOV.match(sd):
        groups[(sd, _fam(x))].append(x)
drop2, n_fold2 = set(), 0
for (sd, fam), lst in groups.items():
    if len(lst) < 2 or not fam:
        continue
    lst.sort(key=lambda x: (TIER_RANK.get(x.get("tier") or "I", 9), -int(x.get("grade") or 0), -int(float(x.get("completeness_score") or 0))))
    keep = lst[0]
    for x in lst[1:]:
        hk = set((keep.get("keys") or "").split("|")) | set((x.get("keys") or "").split("|"))
        keep["keys"] = "|".join(sorted(k for k in hk if k)); keep["buyer_keys"] = len([k for k in hk if k])
        drop2.add(id(x)); n_fold2 += 1
rows = [x for x in rows if id(x) not in drop2]
print("second mailbox of the same organisation (same site and mail domain, same name family) folded:", n_fold2)
_free(globals(), "used_mail", "groups", "drop", "drop2", "lst", "keep", "holder")
for x in rows:  # owner 2026-11-03: fill what can be derived (after the merge, which keys on jurisdiction and website)
    if not x.get("jurisdiction"):
        x["jurisdiction"] = x.get("_jur") or ""
    if not x.get("buyer_website") and x.get("email"):
        md, eh = x["email"].split("@")[-1].lower(), host_of(x.get("email_evidence_url") or "")
        x["buyer_website"] = "https://" + (eh if eh and registrable(eh) == registrable(md) else md if not FREEMAIL.match(md) else eh) if (eh or not FREEMAIL.match(md)) else ""
# owner 2026-11-03 ("the address, the headquarters, everything about the buyer and the vendor"): head-office address, phone and
# role mailboxes read from each organisation's own site by tools/org_contacts.py (evidence URL kept), by registrable domain
NA_ADDR = re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z] ?\d[ABCEGHJ-NPRSTV-Z]\d\b|\b\d{5}(?:-\d{4})?\b.*\b(?:USA|United States)|, [A-Z]{2},? \d{5}\b|\b(?:ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|YT|NT|NU)\b")
def phone_fits(phone, address):
    """a foreign-country number on a group site is not the Canadian / US entity's phone"""
    p = (phone or "").strip()
    return not (p.startswith("+") and not re.match(r"\+\s?1\b", p) and NA_ADDR.search(address or ""))
n_oc = collections.Counter()
for x in rows:
    for col in ("buyer_phone", "buyer_contact_evidence_url", "vendor_phone", "vendor_contact_evidence_url"):
        x.setdefault(col, "")
    b = oc_of(x.get("buyer_website"), x.get("buyer") or "")
    if (x.get("buyer_address") or "").strip() in ("CA", "US", "Canada", "CA, CA"):
        x["buyer_address"] = ""  # the release's buyer table had only the country: that is no bill-to address (2026-11-09)
    if b:
        if not x.get("buyer_address") and b.get("address"):
            x["buyer_address"] = b["address"]; n_oc["buyer_address"] += 1
        if b.get("phone") and phone_fits(b["phone"], x.get("buyer_address")):
            x["buyer_phone"] = b["phone"]; n_oc["buyer_phone"] += 1
        x["buyer_contact_evidence_url"] = b.get("address_url") or b.get("phone_url") or ""
    v = oc_of(x.get("vendor_website"), x.get("vendor") or "")
    if v:
        _vab = site_country(v) == "abroad"
        if _vab:
            n_oc["vendor site prints an address outside Canada: address and telephone not taken"] += 1
        if not x.get("vendor_address") and v.get("address") and not _vab:
            x["vendor_address"] = v["address"]; n_oc["vendor_address"] += 1
        if v.get("phone") and not _vab and phone_fits(v["phone"], x.get("vendor_address")):
            x["vendor_phone"] = v["phone"]; n_oc["vendor_phone"] += 1
        if not x.get("vendor_emails") and v.get("emails"):
            x["vendor_emails"] = v["emails"]; n_oc["vendor_emails"] += 1
        x["vendor_contact_evidence_url"] = v.get("address_url") or v.get("emails_url") or v.get("phone_url") or ""
print("org_contacts: %d organisations read; filled %s" % (len(OC), dict(n_oc)))
print("site-reader records read on another host of the row's domain (look-ups):", dict(N_OTHER_HOST))
# 9. owner 2026-11-04 10:50: every row states the nature of the relationship, how it was found, and where every fact comes from
LANE_META = {}  # (key, mailbox) -> (lane, file, retrieved_date, task_id)
_lm_need = {(x.get("email") or "").lower() for x in rows if x.get("email")} if _PN > 1 else None  # ranking in parts: only the mailboxes of this part's rows
for path in _glob.glob(ROOT + "/data/incoming/*/*buyer_ap*results*.csv"):
    lane = os.path.basename(os.path.dirname(path))
    try:
        for r in csv.DictReader(io.StringIO(open(path, encoding="utf-8", errors="replace").read().replace("\0", ""))):
            e = (r.get("ap_email") or "").strip().lower()
            if e and (_lm_need is None or e in _lm_need):
                for k in (r.get("buyer_key") or "").split("|"):
                    LANE_META.setdefault((k.strip(), e), (lane, os.path.basename(path), r.get("retrieved_date") or "", r.get("task_id") or ""))
                LANE_META.setdefault(("", e), (lane, os.path.basename(path), r.get("retrieved_date") or "", r.get("task_id") or ""))
    except Exception:
        pass
INGEST_DATE = ""
try:
    INGEST_DATE = re.search(r"Ingest report — (\S+)", open(ROOT + "/coord/INGEST_REPORT.md", encoding="utf-8").read()).group(1)
except Exception:
    pass
BTYPE = (
    (r"\b(first nation|nation|band council|tribal|m[ée]tis|inuit|conseil de bande|cree|mohawk|anishinabe|innu)\b", "First Nation / Indigenous government"),
    (r"\b(school board|school district|school division|board of education|centre de services scolaire|commission scolaire|cssd|csd|dsb|conseil scolaire|academy trust|independent school district|isd|public schools|k-12)\b", "school board / school district"),
    (r"\b(universit|polytechnic|institute of technology|college|coll[èe]ge|c[ée]gep|cegep|school of|academy|institut universitaire)\b", "university / college"),
    (r"\b(hospital|h[ôo]pital|health (?:authority|region|services|network|centre|center|system)|ciusss|cisss|chu\b|healthcare|sant[ée]|medical cent|clinic|long[- ]term care|nursing home|chsld)\b", "hospital / health authority"),
    (r"\b(ville|city of|town of|village|municipalit|township|canton|county of|comt[ée]|mrc\b|regional municipality|regional district|district of|borough|parish|paroisse|arrondissement|metro vancouver|metropolitan)\b", "municipality / local government"),
    (r"\b(transit|transport|transpo|airport|a[ée]roport|port authority|port of|harbour|ferry|rail|m[ée]tro|r[ée]seau de transport|soci[ée]t[ée] de transport)\b", "transport / transit authority"),
    (r"\b(hydro|power|electric|utilit|water|wastewater|energy|gas|sewer|waterworks|[ée]nergie|r[ée]gie)\b", "utility / public corporation"),
    (r"\b(ministry|minist[èe]re|department of|secr[ée]tariat|government of|gouvernement|province of|state of|commonwealth of|treasury board|legislative|assembly|parliament|service canada|agency|agence|commission|tribunal|board|office of|bureau|crown|authority|administration|service|services)\b", "government ministry / agency"),
    (r"\b(library|biblioth|museum|mus[ée]e|gallery|theatre|theater|arts|festival|zoo|aquarium|orchestra|foundation|fondation|charit|church|[ée]glise|diocese|parish|association|society|soci[ée]t[ée]|federation|f[ée]d[ée]ration|council|conseil|union|syndicat|chamber|chambre|institute|institut|centre|center|club|non-?profit|coop|co-op|credit union|caisse)\b", "non-profit / association / cultural body"),
    (r"\b(inc|ltd|lt[ée]e|llc|llp|corp|corporation|company|co\b|plc|gmbh|sa\b|s\.a\.|bv|ag\b|group|groupe|holdings|industries|enterprises|entreprises|partners|bank|banque|insurance|assurance|trust|capital|realty|construction|technologies|systems|solutions|pharma|mining|resources|oil|petroleum|motors|airlines|shipbuilding|aerospace|laboratories)\b", "company (private sector)"),
)
def buyer_type(name, jur):
    n = (name or "").lower()
    for rx, label in BTYPE:
        if re.search(rx, n, re.I):
            if label == "government ministry / agency" and jur == "US":
                return "US government body (federal, state or local)"
            if label == "municipality / local government" and jur == "US":
                return "US city / county / local government"
            return label
    return "organisation (type not stated in the record)"
KIND = {"A": "public contract / purchase award with a published end date (dated record)", "B": "public contract / purchase award in the last 12 months (dated record)",
        "T": "active paid service of a Canada-HQ vendor seen on the buyer's own site", "M": "member or regulated payer of a Canadian body (current list)",
        "C": "named as a client by the Canada-located vendor (client list / customer story / case study)", "D": "named as a client by the Canada-located vendor (client list / customer story), dated",
        "L": "dated deal or payment 12 to 36 months ago", "E": "linked from the Canada-located vendor's site (weakest listed relationship)", "F": "older contract or payment (more than 36 months, or ended)",
        "R": ".ca domain name registration in force: agreement with the Canadian Internet Registration Authority, fee paid through a CIRA-certified (Canadian) registrar",
        "I": "inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain", "N": "no relationship record"}
HOW_FOUND = {"A": "the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)",
             "B": "same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field",
             "T": "tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read",
             "M": "tools/member_lists.py read the Canadian body's current member / regulated-payer list and matched the buyer by name",
             "C": "tools/client_lists.py / customer_stories.py read the vendor's own client list or customer story naming the buyer",
             "D": "tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer",
             "L": "a dated public record (payment register, subaward, vendor news release or EDC transaction) 12 to 36 months old, harvested by the lead scanners",
             "E": "tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release",
             "F": "an older or ended record in the contract dataset (release tables)",
             "R": "the organisation's own site on its .ca domain publishes the mailbox (re-fetched by the referee, so the domain is registered and live); every .ca registrant is a party to CIRA's Registrant Agreement (quoted in `vendor_country_basis`)",
             "I": "no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)",
             "N": "no relationship record"}
LANE_WORDS = {"claude": "the claude lane's no-AI tools", "chatgpt": "the ChatGPT/Codex agent (lane chatgpt)", "codex": "the Codex agent (lane codex)", "gemini": "the Gemini agent (lane gemini)", "jules": "the Jules agent (lane jules)"}
def mailbox_how(file, lane):
    f = (file or "").lower()
    if "crawl" in f: return "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages)"
    if "search" in f or "deep" in f: return "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI"
    if "apfirst" in f: return "page from the owner's earlier extract, re-read by tools/ap_pages.py without AI"
    if "dsenrich" in f: return "mailbox from the dataset build, re-submitted so the referee re-fetched the page"
    if "federal" in f: return "PSPC / departmental supplier-payment directory read by the claude lane"
    if "manual" in f or "agent" in f: return "researched by a Claude agent that opened the page and quoted it"
    if "peppol" in f: return "Peppol directory lookup by the claude lane"
    if "xverify" in f: return "cross-verification row (a second lane quoting the same page)"
    return "researched by %s (page opened and quoted)" % LANE_WORDS.get(lane, lane or "a lane agent")
# ---- owner 2026-11-06 D-items: evidence-page re-read (terms, PO, portal, phone, address, printed AP contact, buyer GST), Peppol, dataset back-reference, sensitivity, template language ----
AT = {}  # key (mailbox or buyer_key) -> every page read for it; merged field by field below (a buyer's terms, PO rule, phone, address sit on different pages)
try:
    for _p in (ROOT + "/data/incoming/claude/claude_ap_terms.csv", ROOT + "/data/incoming/claude/claude_ap_terms_pages.csv.gz"):  # mailbox pages; walker / search pages (gzipped companion since 2026-11-08)
        if not os.path.exists(_p):
            continue
        with (gzip.open if _p.endswith(".gz") else open)(_p, "rt", encoding="utf-8", errors="replace") as _fh:
            _txt = _fh.read().replace("\0", "")
        for _r in csv.DictReader(io.StringIO(_txt)):
            if _r.get("status") == "ok" and _r.get("email"):
                AT.setdefault(_r["email"].lower(), []).append(_r)
except Exception as _e:
    print("ap_terms file unreadable:", type(_e).__name__, _e); AT = {}
AT_PAGE_RX = re.compile(r"invoice|factur|payable|supplier|vendor|fourniss|payment|paiement|terms|conditions|purchas|procure|achat|approvisionnement|accounts|comptabilit|finance", re.I)
AT_FIELDS = ("payment_terms", "po_required", "portal_name", "portal_url", "ap_phone", "invoice_mailing_address", "ap_contact_name", "invoice_format", "buyer_bn", "bn_quote", "mailbox_context", "payment_method", "ap_cycle", "tax_exempt", "esignature", "ap_system", "setup_url", "setup_quote")
AT_TERM_FIELDS = ("payment_terms", "po_required", "portal_name", "payment_method", "ap_cycle", "tax_exempt", "esignature", "ap_system", "buyer_bn", "invoice_format", "setup_url")


def at_pages(x):
    """the pages read for this row: the mailbox's own evidence page first, then pages found for the buyer (walker / search) that are about invoicing, suppliers or purchasing"""
    e = (x.get("email") or "").lower()
    own = list(AT.get(e) or [])
    found = []
    for k in (x.get("keys") or "").split("|"):
        for r_ in AT.get(k) or []:
            if r_ not in own and (AT_PAGE_RX.search((r_.get("final_url") or r_.get("evidence_url") or "") + " " + (r_.get("payment_terms_quote") or "")) or any(r_.get(f) for f in AT_TERM_FIELDS)):
                found.append(r_)  # a bylaw / policy PDF whose address says nothing counts when a term was read from it
    found.sort(key=lambda r_: (not re.search(r"payable|invoice|factur|supplier|vendor|fourniss", (r_.get("final_url") or "") , re.I), r_.get("final_url") or ""))
    return own + found


def at_merge(pages):
    """first page that carries each field, with that page's own source note"""
    m = {}
    for r_ in pages:
        for f in AT_FIELDS:
            if r_.get(f) and f not in m:
                m[f] = r_[f]; m[f + "_row"] = r_; m[f + "_src"] = " (as printed on %s, re-read %s)" % (r_.get("final_url") or r_.get("evidence_url"), r_.get("retrieved_date"))
    return m


n_at = collections.Counter()
n_at_pages = 0
for x in rows:
    e = (x.get("email") or "").lower()
    pages = at_pages(x)
    if not pages:
        continue
    n_at_pages += len(pages)
    own = AT.get(e) or []
    t = at_merge(pages)
    x["_at"] = set()
    if t.get("payment_terms") and not x.get("payment_terms_as_published"):
        x["payment_terms_as_published"] = t["payment_terms"] + t["payment_terms_src"]; x["_at"].add("payment_terms_as_published"); n_at["payment_terms"] += 1
    if t.get("po_required") and not x.get("po_required_as_published"):
        x["po_required_as_published"] = t["po_required"] + t["po_required_src"]; x["_at"].add("po_required_as_published"); n_at["po_required"] += 1
    if t.get("portal_name") and not x.get("invoice_portal_url"):
        x["invoice_portal_url"] = "%s%s (additional channel named on the buyer's page; the e-mail is the contact)" % (t.get("portal_url") or t["portal_name"], (" — " + t["portal_name"]) if t.get("portal_url") else ""); x["_at"].add("invoice_portal_url"); n_at["portal"] += 1
    _ap_page = int(x.get("grade") or 0) >= 3  # next to an AP / finance mailbox it is the AP phone and address; next to a general mailbox it is the organisation's
    if t.get("ap_phone"):
        src = t["ap_phone_src"]
        if (_ap_page or t["ap_phone_row"] not in own) and not x.get("ap_phone"):
            x["ap_phone"] = t["ap_phone"] + src; x["_at"].add("ap_phone"); n_at["ap_phone"] += 1  # a phone on an AP / supplier / purchasing page is the AP phone even when the row's mailbox is general
        elif not _ap_page and not x.get("buyer_phone"):
            x["buyer_phone"] = t["ap_phone"] + " (printed next to the organisation's mailbox%s)" % src; n_at["buyer_phone_from_page"] += 1
    if t.get("invoice_mailing_address"):
        src = t["invoice_mailing_address_src"]
        if (_ap_page or t["invoice_mailing_address_row"] not in own) and not x.get("invoice_mailing_address"):
            x["invoice_mailing_address"] = t["invoice_mailing_address"] + src; x["_at"].add("invoice_mailing_address"); n_at["address"] += 1
        elif not _ap_page and not x.get("buyer_address"):
            x["buyer_address"] = t["invoice_mailing_address"] + " (printed next to the organisation's mailbox%s)" % src; n_at["buyer_address_from_page"] += 1
    if t.get("ap_contact_name") and not x.get("ap_contact_name_as_published"):
        x["ap_contact_name_as_published"] = t["ap_contact_name"] + " (as printed by the organisation on its own accounts-payable page%s)" % t["ap_contact_name_src"]; x["_at"].add("ap_contact_name_as_published"); n_at["ap_contact_name"] += 1
    if t.get("invoice_format"):
        add = "invoice format as published: %s" % t["invoice_format"]
        if add[:40] not in (x.get("invoicing_requirements") or ""):
            x["invoicing_requirements"] = ((x.get("invoicing_requirements") + " | ") if x.get("invoicing_requirements") else "") + add + t["invoice_format_src"]; x["_at"].add("invoicing_requirements"); n_at["format"] += 1
    if t.get("buyer_bn") and not x.get("buyer_bn_as_published") and re.match(r"^\d{9}RT0001$", t["buyer_bn"]):
        bn_page = t["buyer_bn_row"]
        x["buyer_bn_as_published"] = "%s (GST/HST number as printed on %s: \"%s\")" % (t["buyer_bn"], bn_page.get("final_url") or bn_page.get("evidence_url"), (bn_page.get("bn_quote") or "")[:160])
        x["buyer_gst_hst_derived"] = t["buyer_bn"] + " (printed by the buyer itself; not derived)"; x["_at"].add("buyer_bn_as_published"); n_at["buyer_bn"] += 1
    if own and own[0].get("mailbox_context"):
        x["email_evidence_context"] = "%s (page text around the mailbox, re-read %s)" % (own[0]["mailbox_context"], own[0].get("retrieved_date")); n_at["context"] += 1
    for col, lab in (("payment_method", "buyer_payment_method_preference"), ("ap_cycle", "buyer_ap_cycle_published"), ("tax_exempt", "buyer_tax_exempt_status"), ("esignature", "buyer_esignature_preference")):
        if t.get(col):
            x[lab] = "%s%s" % (t[col], t[col + "_src"]); n_at[col] += 1
    if t.get("portal_name") and not t["portal_name"].startswith("supplier / vendor portal") and not (x.get("ap_system_hint") or "").startswith("named on"):
        x["ap_system_hint"] = ("named on the buyer's page: %s%s" % (t["portal_name"], t["portal_name_src"])) + (("; " + x["ap_system_hint"]) if x.get("ap_system_hint") else ""); n_at["ap_system_portal"] += 1
    if t.get("ap_system") and not (x.get("ap_system_hint") or "").startswith("named on"):
        x["ap_system_hint"] = ("named on the buyer's page: %s%s" % (t["ap_system"], t["ap_system_src"])) + (("; " + x["ap_system_hint"]) if x.get("ap_system_hint") else ""); n_at["ap_system"] += 1
    if t.get("setup_url") and not x.get("supplier_setup_url"):
        x["supplier_setup_url"] = "%s (%s%s)" % (t["setup_url"], (t.get("setup_quote") or "").replace("link text: ", "linked as \"") + ("\"" if t.get("setup_quote") else ""), t["setup_url_src"]); n_at["setup_url"] += 1
    if own and own[0].get("mailbox_still_on_page") == "no":
        x["mailbox_recheck_note"] = "mailbox not seen in the page text when re-read %s (dynamic page, PDF or removed — the referee's own re-fetch decides; check before use)" % own[0].get("retrieved_date"); n_at["mailbox_gone"] += 1
    elif own:
        x["mailbox_recheck_note"] = "mailbox seen again on the page when re-read %s" % own[0].get("retrieved_date")
print("ap_terms (evidence pages re-read): %d keys read, %d pages used across rows; filled %s" % (len(AT), n_at_pages, dict(n_at)))
_free(globals(), "AT", "EXTRA")
# Peppol Directory (D8): every Canadian participant, matched by key / exact name
PEP = []
if os.path.exists(ROOT + "/data/incoming/claude/claude_peppol_participants.csv"):
    PEP = list(csv.DictReader(open(ROOT + "/data/incoming/claude/claude_peppol_participants.csv", encoding="utf-8", errors="replace")))
pep_key, pep_name = {}, {}
for _p in PEP:
    for k in (_p.get("buyer_keys") or "").split("|"):
        if k: pep_key[k] = _p
    for nm in (_p.get("names") or "").split(" | "):
        if norm(nm): pep_name[norm(nm)] = _p
pep_date = PEP[0]["retrieved_date"] if PEP else ""
n_pep = collections.Counter()
for x in rows:
    x["peppol_participant_id"] = x["peppol_registered"] = x["vendor_peppol_id"] = ""
    if not PEP:
        continue
    hit = next((pep_key[k] for k in (x.get("keys") or "").split("|") if k in pep_key), None) or pep_name.get(norm(x.get("buyer") or ""))
    if hit:
        x["peppol_participant_id"] = "%s %s" % (hit.get("participant_scheme") or "", hit.get("participant_id") or "")
        x["peppol_registered"] = "yes — Peppol Directory participant registered %s (%s; %s)" % (hit.get("registration_date") or "date not listed", hit.get("names") or "", hit.get("public_page") or ""); n_pep["buyer"] += 1
    else:
        x["peppol_registered"] = "not listed in the Peppol Directory (country=CA search on %s: %d Canadian participants in total)" % (pep_date, len(PEP))
    vh = pep_name.get(norm((x.get("vendor_legal_name") or "").split(" (as")[0])) or pep_name.get(norm(x.get("vendor") or ""))
    if vh and not (x.get("vendor") or "").startswith("inferred"):
        x["vendor_peppol_id"] = "%s %s (Peppol Directory, registered %s; %s)" % (vh.get("participant_scheme") or "", vh.get("participant_id") or "", vh.get("registration_date") or "n/a", vh.get("public_page") or ""); n_pep["vendor"] += 1
print("peppol: %d Canadian participants; matched buyers %d, vendors %d" % (len(PEP), n_pep["buyer"], n_pep["vendor"]))
def _dom_of(u):
    try:
        return registrable((urllib.parse.urlparse(u if "//" in (u or "") else "https://" + (u or "")).hostname or "").lower().removeprefix("www."))
    except Exception:
        return ""
# D11 / C1 / C2 / H1: provincial municipal directories (tools/municipal_directory.py) — legal name, address, phone, website, tier, population
# 2026-11-10 (row audit, round 3): the directories were looked up by the registrable domain of the row's site, and the first entry of a domain
# won — "Municipalité de Authier" (authier.ao.ca) was the legal name, address and telephone of the sixteen other municipalities hosted on
# ao.ca, "Village de Godbout" of every municipality with a page on municipalites-du-quebec.com. An entry is now a row's own only when the row's
# site is the entry's site: the same host and, when the entry's address goes below the host ("…/godbout"), the same first folder. A site that
# two entries of different names give is a portal and names neither.
_MD_TRIVIAL = re.compile(r"^(?:fr|en|fr-ca|en-ca|fr_ca|en_ca|accueil|home|index\.(?:php|html?|aspx?)|default\.aspx?)?$", re.I)
def _md_site(u):
    """(host, first folder) of a site address; the folder is "" for the root and for a language or home-page folder"""
    try:
        pu = urllib.parse.urlparse(u if "//" in (u or "") else "https://" + (u or ""))
    except Exception:
        return "", ""
    h = (pu.hostname or "").lower()
    h = h[4:] if h.startswith("www.") else h
    seg = (pu.path or "").strip("/").split("/")[0]
    return h, ("" if _MD_TRIVIAL.match(seg) else seg.lower())
MD_DOM, MD_NAME, _md_names = {}, {}, collections.defaultdict(set)
for _mdp in (ROOT + "/data/incoming/claude/claude_municipal_directory.csv", ROOT + "/data/incoming/claude/claude_org_directories.csv"):
    if not os.path.exists(_mdp):
        continue
    for _r in csv.DictReader(open(_mdp, encoding="utf-8", errors="replace")):
        _d = _md_site(_r.get("website") or "") if _r.get("website") else ("", "")
        if _d[0] and not SHARED_GOV.match(registrable(_d[0]) or _d[0]):
            MD_DOM.setdefault(_d, _r); _md_names[_d].add(norm(_r.get("legal_name") or ""))
        for nm in (_r.get("legal_name"), (_r.get("source_quote") or "").split(";")[0]):
            if nm and len(norm(nm)) >= 5:
                MD_NAME.setdefault((_r["province"], norm(nm)), _r)
# the place name without its designation ("Ville de X" / "X" / "Municipalité de X" / "Town of X" all name the same body); an ambiguous core (two bodies in one province) is skipped
DESIG_RX = re.compile(r"^(?:la |le |les |l['’])?(?:ville|municipalit[ée](?: r[ée]gionale de comt[ée])?|mrc|cit[ée]|canton|paroisse|village|township|town|city|county|district|regional district|regional municipality|rural municipality|resort municipality|municipal district|united counties|the corporation of the (?:city|town|township|village|municipality|county|district|regional municipality))\s+(?:of|de|du|des|d['’])?\s*", re.I)
def md_core(nm):
    c = norm(DESIG_RX.sub("", (nm or "").strip()))
    return c if len(c) >= 4 else ""
for _d, _ns in _md_names.items():
    if len(_ns) > 1:
        MD_DOM.pop(_d, None)
print("directories: %d entries reachable by their own site; %d sites given by entries of different names, left out" % (len(MD_DOM), sum(len(v) > 1 for v in _md_names.values())))
del _md_names
MD_CORE, _md_amb = {}, set()
for (_pv, _nm), _r in list(MD_NAME.items()):
    _c = md_core(_nm)
    if not _c:
        continue
    if (_pv, _c) in MD_CORE and MD_CORE[(_pv, _c)] is not _r and MD_CORE[(_pv, _c)].get("legal_name") != _r.get("legal_name"):
        _md_amb.add((_pv, _c))
    MD_CORE.setdefault((_pv, _c), _r)
for _k in _md_amb:
    MD_CORE.pop(_k, None)
n_md = collections.Counter()
for x in rows:
    for c in ("buyer_municipal_tier", "buyer_population", "directory_general_email", "municipal_directory_source"):
        x.setdefault(c, "")
    if not MD_DOM:
        continue
    _d = _md_site(x.get("buyer_website") or "") if x.get("buyer_website") else ("", "")
    prov = x.get("jurisdiction") or ""
    hit = (MD_DOM.get(_d) if _d[0] else None) or MD_NAME.get((prov, norm(x.get("buyer") or ""))) or MD_NAME.get((prov, norm((x.get("buyer_legal_name_as_published") or "").split(" (")[0])))
    if not hit and prov and prov not in ("CA",) and re.search(r"\b(ville|municipalit|mrc|canton|paroisse|village|township|town|city|county|district|municipality)\b", x.get("buyer") or "", re.I):
        hit = MD_CORE.get((prov, md_core(x.get("buyer") or "")))  # "Ville de X" ↔ directory "X" (designation separate); ambiguous cores were dropped
        if hit:
            n_md["matched_by_place_name"] += 1
    if not hit:
        continue
    if hit["province"] != prov and prov not in ("", "CA") and hit["province"] not in ("CA",) and not (hit["province"] == "FED" and prov == "FED"):
        continue
    src = " (provincial municipal directory: %s, %s)" % (hit["source_url"], hit["retrieved_date"])
    n_md["matched"] += 1
    if not x.get("buyer_legal_name_as_published") and hit.get("legal_name"):
        x["buyer_legal_name_as_published"] = hit["legal_name"] + src; n_md["legal_name"] += 1
    if not x.get("buyer_address") and hit.get("address") and re.search(r"[A-Za-zÀ-ÿ]{3}", hit["address"]) and (
            re.search(r"\d", hit["address"]) or re.search(r"(?i)\b(?:building|tower|house|centre|center|street|avenue|road|crescent|place|square|drive|boulevard|rue|chemin|[ée]difice|complexe)\b", hit["address"])):
        # an address has a word and a number, or names a building or a street ("R.G. Casey Building, John McEwen Crescent"): one directory's address
        # column holds mail codes ("CP3-1-130") and body names ("Department of Defence")
        x["buyer_address"] = ", ".join(v for v in (hit["address"], hit.get("postal_code")) if v) + src; n_md["address"] += 1
    if not x.get("buyer_phone") and hit.get("phone"):
        x["buyer_phone"] = hit["phone"] + src; n_md["phone"] += 1
    if not x.get("buyer_website") and hit.get("website"):
        x["buyer_website"] = hit["website"]; x["buyer_website_status"] = (x.get("buyer_website_status") or "") + " (from the provincial municipal directory)"; n_md["website"] += 1
    if hit.get("municipal_tier"):
        x["buyer_municipal_tier"] = "%s (%s%s)" % (hit["municipal_tier"], ("within " + hit["upper_tier_or_mrc"] + "; ") if hit.get("upper_tier_or_mrc") and hit["municipal_tier"].lower().startswith("lower") else "", "Ontario MMAH list") + src
    elif hit["province"] == "QC":
        x["buyer_municipal_tier"] = "local municipality%s (MAMH répertoire)%s" % ((" of MRC " + hit["upper_tier_or_mrc"]) if hit.get("upper_tier_or_mrc") else "", src)
    if hit.get("population"):
        x["buyer_population"] = hit["population"] + src
    if hit.get("general_email"):
        x["directory_general_email"] = hit["general_email"] + " (the municipality's general mailbox as listed in the provincial directory; not the delivered mailbox)"
    x["municipal_directory_source"] = hit["source_url"]
print("municipal / organisation directories:", dict(n_md))
# CRA registered charities → buyers' BN (RR account), legal name, address, fiscal period end (tools/charity_buyers.py)
CHB = {}
_chp = ROOT + "/data/incoming/claude/claude_charity_buyers.csv"
if os.path.exists(_chp):
    for _r in csv.DictReader(open(_chp, encoding="utf-8", errors="replace")):
        CHB.setdefault(_r["buyer_key"], _r)
n_ch = collections.Counter()
for x in rows:
    for c in ("buyer_fiscal_year_end", "buyer_charity_status", "buyer_charity_designation"):
        x.setdefault(c, "")
    h = next((CHB[k] for k in (x.get("keys") or "").split("|") if k in CHB), None)
    if not h:
        continue
    src = " (CRA list of registered charities, %s, %s; matched by %s)" % (h["source_url"], h["retrieved_date"], h["match_basis"])
    n_ch["matched"] += 1
    if not x.get("buyer_bn_as_published") and h.get("bn"):
        x["buyer_bn_as_published"] = h["bn"] + " — charity registration number (RR program account)" + src; n_ch["bn"] += 1
        if not x.get("buyer_gst_hst_derived") and h.get("bn9"):
            x["buyer_gst_hst_derived"] = h["bn9"] + "RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)"
    if h.get("legal_name") and register_name_takes(x.get("buyer_legal_name_as_published") or "", h["legal_name"]):
        x["buyer_legal_name_as_published"] = h["legal_name"] + src; n_ch["legal_name"] += 1
    if not x.get("buyer_address") and (h.get("address") or h.get("city")):
        x["buyer_address"] = ", ".join(v for v in (h.get("address"), h.get("city"), h.get("province"), h.get("postal_code")) if v) + src; n_ch["address"] += 1
    if not x.get("buyer_website") and h.get("website"):
        x["buyer_website"] = h["website"]; n_ch["website"] += 1
    if h.get("fiscal_period_end"):
        x["buyer_fiscal_year_end"] = h["fiscal_period_end"] + src
    x["buyer_charity_status"] = (h.get("charity_status") or "registered") + src
    x["buyer_charity_designation"] = "; ".join(v for v in (h.get("designation"), h.get("category")) if v)
print("charity buyers:", dict(n_ch))
# 2026-11-10: the registration number itself joins a row to the CRA list (tools/charity_buyers.py writes the list in a compact form). 1,167 rows of the
# build of 22:38Z carried a charity registration number — printed on the organisation's own site, or in a federal grants record — that the list holds,
# without the list's name and address: the match above works by name and by web address only, and the number says more than either ("Ronald McDonald
# House Toronto" is TORONTO CHILDREN'S CARE INC., "Charlotte Street Arts Centre" is FREDERICTON ARTS AND LEARNING INCORPORATED). A holder that is a
# foundation or a trust, where the organisation's own name is not one, may be its fundraising body: its name is reported, not taken as the legal name.
CRA, CRA9 = {}, collections.defaultdict(list)
_crp = ROOT + "/data/incoming/claude/claude_cra_charities.csv.gz"
if os.path.exists(_crp):
    with gzip.open(_crp, "rt", encoding="utf-8", newline="") as _f:
        for _r in csv.DictReader(_f):
            CRA[_r["bn"]] = _r; CRA9[_r["bn"][:9]].append(_r)
_FUND_BODY = re.compile(r"\b(?:foundation|fondation|trust|fiducie|fund|fonds|endowment|dotation|friends|amis|auxiliary|auxiliaire|alumni)\b", re.I)
n_cr = collections.Counter()
for x in rows:
    if not CRA or x.get("buyer_charity_status"):
        continue
    _b = x.get("buyer_bn_as_published") or ""
    _m = re.match(r"\s*(\d{9})\s?RR\s?(\d{4})", _b)
    h = CRA.get(_m.group(1) + "RR" + _m.group(2)) if _m else None
    if not h:
        _m9 = re.match(r"\s*(\d{9})\b(?!\s?R[TPCMZ])", _b)
        if _m9 and re.search(r"charit|bienfaisance|registration|enregistrement", _b, re.I) and len(CRA9.get(_m9.group(1), ())) == 1:
            h = CRA9[_m9.group(1)][0]  # the nine digits printed as a charity's registration number, and one registered account under them
    if not h:
        continue
    n_cr["matched"] += 1
    src = " (CRA list of registered charities, %s, %s; found by the registration number %s)" % (h.get("source_url") or "", h.get("retrieved_date") or "", h["bn"])
    _bn = x.get("buyer") or ""
    _same = name_overlap(h.get("legal_name") or "", _bn, x.get("buyer_website") or "") or (h.get("account_name") and name_overlap(h["account_name"], _bn, x.get("buyer_website") or ""))
    _fund = bool(_FUND_BODY.search(h.get("legal_name") or "")) and not _FUND_BODY.search(_bn) and not _same
    x["buyer_charity_status"] = "registered: %s holds the registration %s%s%s" % (h.get("legal_name") or "", h["bn"],
        " — a foundation / trust under another name than the organisation's: it may be its fundraising body, so its name is not taken as the legal name" if _fund else "", src)
    x["buyer_charity_designation"] = "; ".join(v for v in (h.get("designation"), h.get("category")) if v)
    if _fund:
        n_cr["holder is a foundation / trust under another name: reported only"] += 1
        continue
    if h.get("legal_name") and (register_name_takes(x.get("buyer_legal_name_as_published") or "", h["legal_name"]) or "JSON-LD Organization name on" in x["buyer_legal_name_as_published"]):
        # an empty cell, or the name the site's structured data shows (a display name, not a statement of the legal person)
        x["buyer_legal_name_as_published"] = "%s (holder of the charity registration number in buyer_bn_as_published; %s)" % (h["legal_name"], src[2:-1]); n_cr["legal_name"] += 1
    if not x.get("buyer_address") and (h.get("address") or h.get("city")):
        x["buyer_address"] = ", ".join(v for v in (h.get("address"), h.get("city"), h.get("province"), h.get("postal_code")) if v) + src; n_cr["address"] += 1
    if (GENERIC_NAME.match(_bn) or DOMAIN_NAME.match(_bn)) and (h.get("account_name") or h.get("legal_name")):
        x["buyer"] = h.get("account_name") or h["legal_name"]; n_cr["name_from_the_register"] += 1  # the row was known by its domain only
print("charity registration numbers found in the CRA list:", dict(n_cr), "| list:", len(CRA))
# Wikidata, one organisation at a time (tools/wikidata_orgs.py): official names, type, HQ, inception, budget, employees — blank cells only
WDB, WDV = {}, {}
_wdp = ROOT + "/data/incoming/claude/claude_wikidata_orgs.csv"
if os.path.exists(_wdp):
    for _r in csv.DictReader(open(_wdp, encoding="utf-8", errors="replace")):
        if _r.get("status") == "matched":
            (WDB if _r["side"] == "b" else WDV)[_r["key"]] = _r
n_wd = collections.Counter()
for x in rows:
    for c in ("buyer_wikidata", "buyer_founded", "buyer_budget_or_revenue", "buyer_employees", "buyer_legal_form", "vendor_wikidata", "vendor_founded", "vendor_employees"):
        x.setdefault(c, "")
    w = next((WDB[k] for k in (x.get("keys") or "").split("|") if k in WDB), None)
    if w:
        src = " (Wikidata %s, %s; %s)" % (w["qid"], w["match_basis"], w["retrieved_date"])
        n_wd["buyers"] += 1
        nm = (w.get("official_name") or "").split(" | ")[0].split(" [")[0] or w.get("label_en") or w.get("label_fr")
        if not x.get("buyer_legal_name_as_published") and nm:
            x["buyer_legal_name_as_published"] = nm + src.replace("(Wikidata", "(official name per Wikidata" if w.get("official_name") else "(label per Wikidata"); n_wd["buyer_legal_name"] += 1
        if not x.get("buyer_address") and (w.get("street_address") or w.get("headquarters")):
            x["buyer_address"] = (w.get("street_address") or w.get("headquarters")) + src; n_wd["buyer_address"] += 1
        if not x.get("buyer_phone") and w.get("phone"):
            x["buyer_phone"] = w["phone"] + src; n_wd["buyer_phone"] += 1
        if not x.get("buyer_website") and w.get("website"):
            x["buyer_website"] = w["website"].split(";")[0]; n_wd["buyer_website"] += 1
        x["buyer_wikidata"] = w["evidence_url"] + ("; " + w["instance_of"] if w.get("instance_of") else "")
        x["buyer_founded"] = (w.get("inception") or "") and (w["inception"] + src)
        x["buyer_budget_or_revenue"] = (w.get("budget_or_revenue") or "") and (w["budget_or_revenue"].strip() + src)
        x["buyer_employees"] = (w.get("employees") or "") and (w["employees"] + src)
        x["buyer_legal_form"] = (w.get("legal_form") or "") and (w["legal_form"] + src)
    vk = "v:" + norm(((x.get("vendor_legal_name") or "").split(" (")[0]) or (x.get("vendor") or ""))
    v = WDV.get(vk) or WDV.get("v:" + norm(x.get("vendor") or ""))
    if v and not (x.get("vendor") or "").startswith("inferred"):
        src = " (Wikidata %s, %s; %s)" % (v["qid"], v["match_basis"], v["retrieved_date"])
        n_wd["vendors"] += 1
        nm = (v.get("official_name") or "").split(" | ")[0].split(" [")[0]
        if not x.get("vendor_legal_name") and nm:
            x["vendor_legal_name"] = nm + src; n_wd["vendor_legal_name"] += 1
        if not x.get("vendor_address") and (v.get("street_address") or v.get("headquarters")):
            x["vendor_address"] = (v.get("street_address") or v.get("headquarters")) + " (headquarters per Wikidata %s; not the registered address)" % v["qid"]; n_wd["vendor_address"] += 1
        if not x.get("vendor_website") and v.get("website"):
            x["vendor_website"] = v["website"].split(";")[0]; n_wd["vendor_website"] += 1
        if not x.get("vendor_phone") and v.get("phone"):
            x["vendor_phone"] = v["phone"] + src
        if not x.get("vendor_neq") and v.get("neq"):
            x["vendor_neq"] = v["neq"] + src; n_wd["vendor_neq"] += 1
        x["vendor_wikidata"] = v["evidence_url"] + ("; " + v["instance_of"] if v.get("instance_of") else "")
        x["vendor_founded"] = (v.get("inception") or "") and (v["inception"] + src)
        x["vendor_employees"] = (v.get("employees") or "") and (v["employees"] + src)
print("wikidata:", dict(n_wd))
# Crown corporations' own GST/BN numbers (printed on their own pages; data/incoming/claude/claude_crown_bn.csv) → inferred-vendor rows (downstream §8.5)
CROWN = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_crown_bn.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_crown_bn.csv", encoding="utf-8")):
        CROWN[norm(_r["vendor"])] = _r
n_cr = 0
for x in rows:
    c = CROWN.get(norm((x.get("vendor") or "").replace("inferred: ", "")))
    if c and not x.get("vendor_bn9"):
        x["vendor_bn9"] = "%s (GST/HST registration number printed by the organisation itself: %s, %s)" % (c["bn9"], c["url"], c["retrieved_date"])
        x["vendor_gst_hst_derived"] = "%sRT0001 (%s)" % (c["bn9"], c["program_account_as_printed"])
        x["vendor_bn_source"] = x.get("vendor_bn_source") or "printed on the organisation's own page (%s)" % c["url"]; n_cr += 1
print("crown-corporation BNs applied to inferred-vendor rows:", n_cr)
# vendor websites proposed by search and CONFIRMED by reading the site (tools/vendor_sites_check.py → claude_vendor_sites.csv)
VSITE = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_vendor_sites.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_vendor_sites.csv", encoding="utf-8")):
        if _r.get("check_status") == "confirmed" and _r.get("website"):
            VSITE[norm(_r["vendor_key"])] = _r
# 2026-11-11 (build of 01:51Z): 16,993 Shopify rows carried "https://finance.yahoo.com/quote/SHOP/profile/" as the vendor's website, TMX Group
# another quote page, 30 vendors a page of leadiq.com — the search check had "confirmed" any page that prints the vendor's name. (1) A vetted
# software vendor's website is the site of its own terms page (tools/tech_relationships.py hq_url). (2) A site proposed by search is taken only
# when its host carries the vendor's name and is not a directory, a quote page, an app store or a register.
_VETTED_SITE = {}
for _v in _TR.VENDORS.values():
    _h = registrable(host_of(_v.get("hq_url") or "") or "")
    if _h:
        for _n in (_v.get("legal"), _v.get("name"), "%s dba %s" % (_v.get("legal") or "", _v.get("name") or "")):
            if _n:
                _VETTED_SITE.setdefault(norm(_n), ("https://%s/" % _h, _v.get("hq_url")))
_VETTED_SITE.setdefault(norm("TMX Group Limited"), ("https://www.tmx.com/", "https://www.tmx.com/privacy-policy"))  # the exchange-listing lane's vendor (tools/exchange_listing.py TMX_HQ_URL, read 2026-11-03)
_THIRD_PARTY_SITE = re.compile(r"(?:^|\.)(?:yahoo\.com|bloomberg\.com|linkedin\.com|facebook\.com|wikipedia\.org|crunchbase\.com|zoominfo\.com|leadiq\.com|rocketreach\.co|dnb\.com|opencorporates\.com|"
                               r"yellowpages\.ca|pagesjaunes\.ca|canada411\.ca|411\.ca|glassdoor\.[a-z.]+|indeed\.com|twitter\.com|x\.com|instagram\.com|youtube\.com|google\.com|apple\.com|amazon\.[a-z.]+|"
                               r"reuters\.com|marketwatch\.com|sedarplus\.ca|sedar\.com|sec\.gov|canada\.ca|gc\.ca|bbb\.org|yelp\.[a-z.]+|tripadvisor\.[a-z.]+|kijiji\.ca|manta\.com|mapquest\.com|waze\.com|"
                               r"github\.com|medium\.com|linktr\.ee|eventbrite\.[a-z.]+|houzz\.[a-z.]+|homestars\.com|constructconnect\.com|portailconstructo\.com|construction411\.com|highergov\.com|"
                               r"govtribe\.com|merx\.com|biddingo\.com|bidsandtenders\.ca|seao\.ca|buyandsell\.gc\.ca|canadabuys\.canada\.ca|ic\.gc\.ca|ised-isde\.canada\.ca)$", re.I)
_SF_STOP = set("the and inc ltd corp corporation limited llp llc co company group groupe canada canadian services service solutions systems international consulting associates of de du des la le les et".split())
_SF_FORM = set("inc ltd corp corporation limited llp llc co ltee incorporated the of de du des la le les and et".split())
def site_fits_name(name, website):
    """does the site's host carry the vendor's name: a distinctive word of the name ("calgary" in ucalgary.ca), the host's label inside the name,
    or the name's initials (ey.com, mhs.com)?"""
    lab = re.sub(r"[^a-z0-9]", "", (registrable(host_of(website) or "") or "").split(".")[0])
    words = re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower())
    sig = [w for w in words if w not in _SF_STOP]
    if not lab or not words or lab in _SF_STOP:
        return False
    if any(len(w) >= 4 and w in lab for w in sig) or (len(lab) >= 4 and lab in "".join(words)) or (len(lab) >= 2 and lab in sig) or any(len(w) >= 3 and lab.startswith(w) for w in sig):
        return True  # … or the host is a word of the name ("WSP Canada Inc." on wsp.com), or begins with one ("RBR Ltd." on rbr-global.com)
    ini = "".join(w[0] for w in words if w not in _SF_FORM)
    ini_sig = "".join(w[0] for w in sig)
    return (len(lab) >= 2 and lab in (ini, ini_sig)) or (len(ini_sig) >= 3 and lab.startswith(ini_sig))
n_vs, n_vs_no = 0, collections.Counter()
for x in rows:
    vn = x.get("vendor") or ""
    if vn and not x.get("vendor_website") and norm(vn) in _VETTED_SITE:
        x["vendor_website"], x["vendor_website_basis"] = _VETTED_SITE[norm(vn)][0], "the site of the vendor's own terms page (%s)" % _VETTED_SITE[norm(vn)][1]
        n_vs_no["vetted vendor: the site of its own terms page"] += 1
        continue
    v_ = VSITE.get(norm(vn)) if vn and not vn.startswith("inferred") and not x.get("vendor_website") else None
    if v_ and (_THIRD_PARTY_SITE.search(host_of(v_["website"]) or "") or not (name_overlap(vn, "", v_["website"]) or site_fits_name(vn, v_["website"]))):
        n_vs_no["search proposal not taken: a directory / quote page / register, or a host that does not carry the vendor's name"] += 1
        v_ = None
    if v_:
        x["vendor_website"] = v_["website"]
        x["vendor_website_basis"] = "found by a web search, confirmed by reading the site on %s: %s (%s)" % (v_["retrieved_date"], v_["evidence_url"], (v_.get("evidence_quote") or "")[:160]); n_vs += 1
print("vendor websites confirmed from search proposals:", len(VSITE), "applied:", n_vs, dict(n_vs_no))
# inferred vendors' own published phone / address (claude_inferred_vendor_facts.csv: pages opened on the Crown corporation's site, quoted) → P13 rows
IVF = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_inferred_vendor_facts.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_inferred_vendor_facts.csv", encoding="utf-8")):
        IVF[norm(_r["vendor"])] = _r
n_ivf = collections.Counter()
for x in rows:
    vn = x.get("vendor") or ""
    f_ = IVF.get(norm(vn.replace("inferred: ", ""))) if vn.startswith("inferred") else None
    if not f_:
        continue
    if not x.get("vendor_phone") and f_.get("phone"):
        x["vendor_phone"] = "%s (%s; %s)" % (f_["phone"], f_.get("phone_label") or "", f_["phone_url"]); n_ivf["phone"] += 1
        x["vendor_contact_evidence_url"] = x.get("vendor_contact_evidence_url") or f_["phone_url"]
    if not x.get("vendor_address") and f_.get("address"):
        x["vendor_address"] = "%s (%s; %s)" % (f_["address"], f_.get("address_label") or "", f_["address_url"]); n_ivf["address"] += 1
print("inferred vendors' published phone / address applied:", dict(n_ivf))
FORM_CLASS_RX = [(re.compile(r"\b(?:llp|l\.l\.p\.|lp|l\.p\.|senc|sencrl|s\.e\.n\.c\.|s\.e\.c\.|sec|partnership|soci[ée]t[ée] en nom collectif|soci[ée]t[ée] en commandite)\b", re.I), "partnership"),
                 (re.compile(r"\b(?:inc|incorporated|incorpor[ée]e|ltd|limited|lt[ée]e|limit[ée]e|corp|corporation|ulc|llc|plc|s\.a\.|gmbh|ag|company|co|cie|compagnie)\b\.?", re.I), "corporation"),
                 (re.compile(r"\b(?:enr|enrg|enregistr[ée]e|sole proprietor)\b", re.I), "sole proprietorship")]
def form_class(name):
    for rx, cls in FORM_CLASS_RX:
        if rx.search(name or ""):
            return cls
    return ""
# Canada's Business Registries (tools/registry_lookup.py → claude_registry_lookup.csv): BN, registered name, registry id, entity type, status,
# incorporation date, registered office for vendors (and corporation-type buyers) that no other registry matched (downstream §2.1 / §3.2)
CBR = {"vendor": {}, "buyer": {}}
# 2026-11-10 (row audit): 73 rows carried the legal name "CANADA INC." and its NEQ — tools/bulk_registry_match.py had taken the bracketed part of
# Wikidata's batch labels ("Dassault Systèmes (Canada)", "Roche (Canada)") for a name and found a Québec company called "CANADA INC.". The tool no
# longer does; a registered name made only of legal-form and place words is never another organisation's identity, whatever file it comes from.
_REG_PLACE = {"canada", "quebec", "ontario", "alberta", "manitoba", "saskatchewan", "columbia", "british", "international", "global", "america", "north", "nord", "amerique"}
_REG_LEGAL = {"inc", "incorporated", "incorporee", "ltd", "limited", "ltee", "limitee", "corp", "corporation", "co", "company", "cie", "compagnie", "llc", "llp", "lp", "enr", "enrg", "senc",
              "sencrl", "sec", "ulc", "plc", "the", "la", "le", "les", "de", "du", "des", "and", "et", "of"}
def _reg_toks(s):
    return [t for t in re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()) if t not in _REG_LEGAL]
def reg_name_is_generic(matched, own):
    """the registered name says nothing ("CANADA INC.", "Co-Québec inc.", "INTERNATIONAL INC.") and is not the organisation's own name"""
    m = _reg_toks(matched)
    return bool(matched) and all(t in _REG_PLACE for t in m) and m != _reg_toks(own)
n_reg_generic = 0
if os.path.exists(ROOT + "/data/incoming/claude/claude_registry_lookup.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_registry_lookup.csv", encoding="utf-8", errors="replace")):
        if _r.get("status") == "found" and _r.get("juri_id") and reg_name_is_generic(_r.get("matched_name"), _r.get("name")):
            n_reg_generic += 1
        elif _r.get("status") == "found" and _r.get("juri_id"):
            _r["_label"] = "Canada's Business Registries, %s %s" % (_r.get("registry_source") or "", _r.get("juri_id") or "")
            CBR[_r["kind"]][_r["key"] if _r["kind"] == "buyer" else norm(_r["key"])] = _r
n_bulk = 0
if os.path.exists(ROOT + "/data/incoming/claude/claude_registry_bulk.csv"):  # tools/bulk_registry_match.py: REQ open data (NEQ) and Corporations Canada open data (BN); the API rows above win when both exist
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_registry_bulk.csv", encoding="utf-8", errors="replace")):
        if _r.get("status") == "found" and _r.get("juri_id") and reg_name_is_generic(_r.get("matched_name"), _r.get("name")):
            n_reg_generic += 1
        elif _r.get("status") == "found" and _r.get("juri_id"):
            _k = _r["key"] if _r["kind"] == "buyer" else norm(_r["key"])
            _r["_label"] = "%s, %s" % (_r.get("registry_source") or "registry open data", _r.get("juri_id") or "")
            if _k not in CBR[_r["kind"]]:
                CBR[_r["kind"]][_k] = _r; n_bulk += 1
            elif _r["juri_id"].startswith("NEQ") and not (CBR[_r["kind"]][_k].get("juri_id") or "").startswith("NEQ"):
                CBR[_r["kind"]][_k]["_neq"] = _r["juri_id"]; CBR[_r["kind"]][_k]["_neq_src"] = _r.get("registry_source") or ""  # the API row has the BN, the REQ row the NEQ: keep both
            elif (_r.get("bn9") or "").strip() and not (CBR[_r["kind"]][_k].get("bn9") or "").strip():
                # 2026-11-10: the reverse case — the API row is the REQ record (no BN), the open-data row is Corporations Canada (BN). An API run on
                # 2026-11-09 made the REQ row primary for "Dassault Systèmes (Canada)" and 64 rows lost their BN9. Keep the BN with its own source.
                CBR[_r["kind"]][_k]["_bn9_other"] = _r["bn9"].strip(); CBR[_r["kind"]][_k]["_bn9_other_src"] = "%s, %s, %s" % (_r.get("registry_source") or "registry open data", _r.get("juri_id") or "", _r.get("retrieved_date") or "")
print("registry bulk rows added (no API row for the key):", n_bulk, "| registry rows left out, the registered name is only legal-form and place words:", n_reg_generic)
# 2026-11-13 (billers first, tools/vendor_numbers.py): a vendor the lanes name by its brand or by a bilingual pair, looked up under the legal name its
# own site prints or under each half of its name — the register entry of exactly that name, active; used where no other register record was found
n_alias = 0
if os.path.exists(ROOT + "/data/incoming/claude/claude_registry_alias.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_registry_alias.csv", encoding="utf-8", errors="replace")):
        if _r.get("status") == "found" and _r.get("juri_id") and not reg_name_is_generic(_r.get("matched_name"), _r.get("name")) and norm(_r["key"]) not in CBR["vendor"]:
            _r["_label"] = "Canada's Business Registries, %s %s" % (_r.get("registry_source") or "", _r.get("juri_id") or "")
            CBR["vendor"][norm(_r["key"])] = _r; n_alias += 1
print("registry rows of vendors found under the legal name their own site prints or a half of their name (tools/vendor_numbers.py):", n_alias)
# 2026-11-10 (row audit, round 3): a buyer's registry record is kept under the row's key, and the row's name changes — a lead first named
# "Ville de Québec" (a name read off a page of ymcaquebec.org) is "LES YMCA DU QUÉBEC" today, and still carried the City's registered name and
# NEQ; "UNIVERSITÉ DU QUÉBEC" sat on calculquebec.ca the same way (14 rows with those two names alone). A record is left out when the name it
# was looked up under is no longer one of the row's names AND the registered name is of a sort that has to agree with the row and does not:
# it is made of a kind of body, a place and everyday words only ("VILLE DE QUÉBEC", "The Canadian Real Estate Association"), or it names a
# kind of institution (a town, a university, a hospital) that neither the row's names nor its address carry — and it fails the test a name
# read off a page has to pass (name_overlap). "HERITAGE DENTAL CENTRE LTD." stays on heritagedentaledmonton.ca, "CENTRAL LANGLEY PET HOSPITAL
# LTD." on centrallangleyvet.ca. A company's registered name with a word of its own stays — most are numbered companies, matched through
# the name the company trades under, and nothing shows them wrong. The registry tools look a row up again when its name has changed.
_REG_KIND = {"ville", "city", "town", "municipalite", "municipality", "village", "canton", "township", "county", "paroisse", "universite", "university", "college", "cegep", "gouvernement",
             "government", "province", "ministere", "ministry", "association", "societe", "society", "fondation", "foundation", "club", "centre", "center", "groupe", "group", "services",
             "service", "gestion", "holdings", "entreprises", "enterprises"}
_NAME_SRC_CUT = re.compile(r"\s*\((?:as registered|stated on|the copyright line of|printed with its legal form|holder of the charity registration|the name on the organisation's own home page|the organisation's name as the source|"
                           r"schema\.org|provincial municipal directory|recipient legal name|as printed|carried from|CRA |registered charity).*$")
_SITE_SAYS = re.compile(r"as the site's operator\)\s*$|under the site's name\)\s*$|JSON-LD legalName on [^()]*, which gives this site as the organisation's own\)\s*$")
def reg_record_is_rows(b, x):
    names = [x.get("buyer") or "", _NAME_SRC_CUT.sub("", x.get("buyer_legal_name_as_published") or "")]
    q = _reg_toks(b.get("name") or "")
    if q and any(q == _reg_toks(nm) for nm in names):
        return True  # looked up under a name the row still carries
    matched = b.get("matched_name") or ""
    m_all = _reg_toks(matched)
    if m_all and any(m_all == _reg_toks(nm) for nm in names):
        return True
    site = x.get("buyer_website") or ""
    agrees = lambda: any(nm and name_overlap(matched, nm, site) for nm in names)  # the test a name read off a page has to pass
    if not [t for t in m_all if t not in _REG_PLACE and t not in _REG_KIND and t not in WORD_COMMON]:
        return agrees()  # "VILLE DE QUÉBEC", "The Canadian Real Estate Association": a kind of body, a place, everyday words — it has to be the row's
    mk = {k for k, rx in _KIND.items() if rx.search(unicodedata.normalize("NFKD", matched).encode("ascii", "ignore").decode().lower())}
    if mk:  # a town, a university, a hospital … on a row that says it is none
        own = unicodedata.normalize("NFKD", " ".join(names)).encode("ascii", "ignore").decode().lower()
        h = re.sub(r"[^a-z0-9.]", "", host_of(site) or "")
        if not mk <= ({k for k, rx in _KIND.items() if rx.search(own)} | {k for k, rx in _KIND_HOST.items() if rx.search(h)}):
            return agrees()
    return True  # a company's registered name (often a numbered company's): it stays with the row it was matched to
n_cbr = collections.Counter()
_CBR_BUYER_NAME = {}
for _r in CBR["buyer"].values():  # the register's records of buyers, by the name they were looked up under (for a vendor that is also a buyer on file)
    _CBR_BUYER_NAME.setdefault(norm(_r.get("name") or ""), _r)
for x in rows:
    vn = x.get("vendor") or ""
    # 2026-11-11: an inferred vendor ("inferred: Hydro-Québec") is that organisation — the inference is about the relationship, not about who the
    # vendor is: its register entry is looked up under its name, also where the register tool met it as a buyer (18,053 tier-I rows had no vendor legal name)
    _vq = re.sub(r"^inferred:\s*", "", vn)
    c = (CBR["vendor"].get(norm(_vq)) or (_CBR_BUYER_NAME.get(norm(_vq)) if vn.startswith("inferred") else None)) if _vq else None
    if not c and _vq and x.get("vendor_legal_name"):
        # 2026-11-11: a vendor the lead names by its site ("Webnames.ca") whose own site prints its legal name ("Webnames.ca Inc"): the register tool
        # looked that printed name up and found the corporation of exactly that name — the build of 22:11Z left 3,763 such rows without the vendor's
        # number (2,890 of them on one vendor), because the row takes the printed name as its vendor name only later
        _vl = re.sub(r"\s*\((?:as printed|stated on|schema\.org|printed with its legal form|the copyright line|as registered).*$", "", x["vendor_legal_name"]).strip()
        if _vl and norm(_vl) != norm(_vq):
            c = CBR["vendor"].get(norm(_vl))
            if c:
                n_cbr["vendor found under the legal name its own site prints"] += 1
    if c and form_class(vn) and form_class(c.get("matched_name") or "") and form_class(vn) != form_class(c.get("matched_name") or ""):
        n_cbr["vendor_skipped_legal_form"] += 1; c = None  # reviewer 2026-11-08: Smythe LLP is not Smythe Inc.
    if c and vn.startswith("inferred") and _RR._DEAD.search(c.get("status_state") or "") and not _RR._LIVE.search(c.get("status_state") or ""):
        # 2026-11-11: a distributor the regulator licenses today is not the register entry of the same name that is inactive (Orangeville Hydro
        # Limited, ON 1438531: an earlier corporation of that name) — the record is not put on the row, and no warning with it (136 rows failed on it)
        n_cbr["inactive register entry of the same name not taken for a biller a regulator names today"] += 1; c = None
    if c:
        src = "%s, %s" % (c["_label"], c["retrieved_date"])
        if re.search(r"\((?:stated on|schema\.org|as printed on the vendor's site)", x.get("vendor_legal_name") or ""):
            x["vendor_legal_name"] = ""  # the registered name beats a name read off a page
        if c.get("bn9") and not x.get("vendor_bn9"):
            x["vendor_bn9"] = "%s (%s)" % (c["bn9"], src); x["vendor_bn_source"] = x.get("vendor_bn_source") or "registry: " + src; n_cbr["vendor_bn9"] += 1
            if not x.get("vendor_gst_hst_derived"):
                x["vendor_gst_hst_derived"] = c["bn9"] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"
        elif c.get("_bn9_other") and not x.get("vendor_bn9"):  # the BN from the other registry record of the same name (see the loader above)
            x["vendor_bn9"] = "%s (%s)" % (c["_bn9_other"], c["_bn9_other_src"]); x["vendor_bn_source"] = x.get("vendor_bn_source") or "registry: " + c["_bn9_other_src"]; n_cbr["vendor_bn9_other_registry"] += 1
            if not x.get("vendor_gst_hst_derived"):
                x["vendor_gst_hst_derived"] = c["_bn9_other"] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"
        if not x.get("vendor_legal_name") and c.get("matched_name"):
            x["vendor_legal_name"] = "%s (as registered: %s)" % (c["matched_name"], src); n_cbr["vendor_legal_name"] += 1
        if not x.get("vendor_registered_address") and (c.get("reg_office_address") or c.get("reg_office_city") or c.get("reg_office_province")):
            x["vendor_registered_address"] = ("%s (registered address; %s)" % (c["reg_office_address"], src)) if c.get("reg_office_address") else ("%s (registered office city / province; %s)" % (", ".join(v for v in (c.get("reg_office_city"), c.get("reg_office_province")) if v), src)); n_cbr["vendor_registered_address"] += 1
        if (c.get("juri_id") or "").startswith("NEQ") and not x.get("vendor_neq"):
            x["vendor_neq"] = "%s (%s)" % (c["juri_id"].replace("NEQ ", ""), src); n_cbr["vendor_neq"] += 1
        elif c.get("_neq") and not x.get("vendor_neq"):
            x["vendor_neq"] = "%s (%s, %s)" % (c["_neq"].replace("NEQ ", ""), c["_neq_src"], c["retrieved_date"]); n_cbr["vendor_neq"] += 1
        if not x.get("vendor_registry_status") and c.get("status_state"):
            x["vendor_registry_status"] = "%s%s (%s)" % (c["status_state"], (" — " + c["status_notes"]) if c.get("status_notes") and c["status_notes"] != c["status_state"] else "", src); n_cbr["vendor_registry_status"] += 1
        if not x.get("vendor_incorporation_date") and c.get("date_incorporated"):
            x["vendor_incorporation_date"] = c["date_incorporated"]; n_cbr["vendor_incorporation_date"] += 1
        if not x.get("vendor_legal_form") and c.get("entity_type"):
            x["vendor_legal_form"] = "%s (%s)" % (c["entity_type"], src); n_cbr["vendor_legal_form"] += 1
        if not x.get("vendor_trading_name") and c.get("alternate_names"):
            x["vendor_trading_name"] = c["alternate_names"] + " (alternate names in the registry)"; n_cbr["vendor_trading_name"] += 1
        x["vendor_registry_id"] = ((x.get("vendor_registry_id") + "; ") if x.get("vendor_registry_id") else "") + "%s (%s)" % (c["juri_id"], c["registry_source"])
        x["vendor_registry_url"] = x.get("vendor_registry_url") or c.get("ui_url") or ""
    k = next((_k for _k in (x.get("keys") or "").split("|") if _k in CBR["buyer"]), (x.get("keys") or "").split("|")[0])
    b = CBR["buyer"].get(k) if k else None
    if b and not reg_record_is_rows(b, x):
        n_cbr["buyer record looked up under a name the row no longer carries, not taken"] += 1; b = None
    if b and _SITE_SAYS.search(x.get("buyer_legal_name_as_published") or "") and _reg_toks(_NAME_SRC_CUT.sub("", x["buyer_legal_name_as_published"])) != _reg_toks(b.get("matched_name") or ""):
        # the site names its legal person in so many words ("operated by 1688150 Alberta Ltd"); a registry record found under the trading name
        # ("Pegasus Paper") and carrying another name is somebody else's. The registry tools look the stated name up (tools/registry_names.py).
        n_cbr["buyer record of another name than the legal person the site itself states, not taken"] += 1; b = None
    if (b and not re.search(r"\b(?:inc|incorporated|ltd|limited|lt[ée]e|corp|corporation|llc|llp|lp|co|company|cie|enr|senc|ulc)\b\.?", b.get("name") or "", re.I)
            and re.search(r"\(printed with its legal form", x.get("buyer_legal_name_as_published") or "")
            and _reg_toks(_NAME_SRC_CUT.sub("", x["buyer_legal_name_as_published"])) != _reg_toks(b.get("matched_name") or "")):
        # 2026-11-11: plain names are looked up too (tools/registry_lookup.py). A record found under the PLAIN name that carries another name than
        # the one the buyer's own site prints with its legal form is a namesake or a parent (measured: 13 of 105): the site's own words stand.
        n_cbr["buyer record found under a plain name, another name than the site prints with its legal form: not taken"] += 1; b = None
    if b:
        src = "%s, %s" % (b["_label"], b["retrieved_date"])
        if re.search(r"\((?:stated on|printed with its legal form|schema\.org|recipient legal name)", x.get("buyer_legal_name_as_published") or ""):
            x["buyer_legal_name_as_published"] = ""  # the registered name beats a name read off a page or another dataset
        if b.get("bn9") and not x.get("buyer_bn_as_published"):
            x["buyer_bn_as_published"] = "%s (%s)" % (b["bn9"], src); n_cbr["buyer_bn"] += 1
            if not x.get("buyer_gst_hst_derived"):
                x["buyer_gst_hst_derived"] = b["bn9"] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"
        if not x.get("buyer_legal_name_as_published") and b.get("matched_name"):
            x["buyer_legal_name_as_published"] = "%s (as registered: %s)" % (b["matched_name"], src); n_cbr["buyer_legal_name"] += 1
        if not x.get("buyer_legal_form") and b.get("entity_type"):
            x["buyer_legal_form"] = "%s (%s)" % (b["entity_type"], src)
        x["buyer_registry_id"] = "%s (%s; %s)" % (b["juri_id"], b["registry_source"], b.get("ui_url") or "")
        if not x.get("buyer_address") and b.get("reg_office_address"):
            x["buyer_address"] = "%s (registered address; %s)" % (b["reg_office_address"], src); n_cbr["buyer_address"] += 1
        if (b.get("_neq") or (b.get("juri_id") or "").startswith("NEQ")) and "NEQ" not in (x.get("buyer_registry_id") or "") and b.get("_neq"):
            x["buyer_registry_id"] += "; %s (%s)" % (b["_neq"], b["_neq_src"])
print("Canada's Business Registries + registry open data: %d vendors, %d buyers found; filled %s" % (len(CBR["vendor"]), len(CBR["buyer"]), dict(n_cbr)))
# award facts read from the buyer's own award page (tools/award_facts.py → claude_award_facts.csv): value, dates, PO / contract / tender numbers,
# number of bids printed next to the vendor's name, for pairs whose proof record lacks them (owner 2026-11-08 12:47 EST: change the approach, not the goal)
AF = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_award_facts.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_award_facts.csv", encoding="utf-8", errors="replace")):
        if _r.get("status") != "ok" or not _r.get("vendor_seen"):
            continue
        _score = sum(1 for c in ("contract_value", "start_date", "end_date", "po_number", "contract_number", "tender_number", "number_of_bids") if _r.get(c)) + (1 if (_r.get("page_kind") or "").startswith(("council", "bid results", "award notice")) else 0)
        if _score and (_r["row_key"] not in AF or _score > AF[_r["row_key"]][0]):
            AF[_r["row_key"]] = (_score, _r)
n_af = collections.Counter()
for x in rows:
    _k = (x.get("keys") or "").split("|")[0] + "||" + (x.get("vendor") or "").strip()
    _hit = AF.get(_k)
    if not _hit:
        continue
    f = _hit[1]
    src = "as printed in the buyer's own %s: %s, read %s" % (f.get("page_kind") or "award page", f.get("final_url") or f.get("url"), f.get("retrieved_date"))
    if f.get("contract_value") and not x.get("contract_value"):
        x["contract_value"] = "%s (%s: \"%s\")" % (f["contract_value"], src, (f.get("value_quote") or "")[:200]); n_af["contract_value"] += 1
        if f.get("currency") and not x.get("currency"):
            x["currency"] = f["currency"]
    for col, fc in (("start_date", "start_date"), ("end_date", "end_date")):
        if f.get(fc) and not x.get(col):
            x[col] = "%s (%s: \"%s\")" % (f[fc], src, (f.get("dates_quote") or "")[:200]); n_af[col] += 1
    for col, fc in (("po_number_as_published", "po_number"), ("contract_or_agreement_number", "contract_number"), ("solicitation_or_tender_number", "tender_number")):
        if f.get(fc) and not x.get(col):
            x[col] = "%s (%s: \"%s\")" % (f[fc], src, (f.get("numbers_quote") or "")[:200]); n_af[col] += 1
    if f.get("number_of_bids") and not x.get("number_of_bids"):
        x["number_of_bids"] = "%s (%s: \"%s\")" % (f["number_of_bids"], src, (f.get("bids_quote") or "")[:200]); n_af["number_of_bids"] += 1
    if f.get("term") and not x.get("end_date") and not x.get("contract_term_as_published"):
        x["contract_term_as_published"] = "%s (%s: \"%s\")" % (f["term"], src, (f.get("dates_quote") or "")[:200]); n_af["term"] += 1
print("award facts from the buyers' own award pages: %d pairs with a page; filled %s" % (len(AF), dict(n_af)))
# federal grants & contributions disclosure (tools/gc_recipients.py → claude_gc_recipients.csv): recipient_business_number of buyers and vendors
GCR = {"vendor": {}, "buyer": {}}
if os.path.exists(ROOT + "/data/incoming/claude/claude_gc_recipients.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_gc_recipients.csv", encoding="utf-8", errors="replace")):
        _bn = _r.get("bn9") or ""
        if not _bn or _bn in ("999999999", "000000000", "123456789") or re.fullmatch(r"(\d)\1{8}", _bn):
            continue  # placeholder numbers (reviewer 2026-11-08)
        if re.match(r"^[A-Z][A-Za-zÀ-ÿ'’\- ]{1,40},\s*[A-Z][A-Za-zÀ-ÿ'’\-]{1,30}(?:\s+[A-Z]\.?)?$", _r.get("matched_name") or "") or (_r.get("recipient_type") or "").upper() in ("P", "I"):
            continue  # an individual ("Surname, Given"): never an organisation's BN or legal name
        GCR[_r["kind"]][_r["key"] if _r["kind"] == "buyer" else norm(_r["key"])] = _r
n_gcr = collections.Counter()
for x in rows:
    k = next((_k for _k in (x.get("keys") or "").split("|") if _k in GCR["buyer"]), (x.get("keys") or "").split("|")[0])
    g = GCR["buyer"].get(k) if k else None
    if g and x.get("buyer_bn_as_published") and g["bn9"] not in x["buyer_bn_as_published"]:
        # 46 of 873 buyers carry a different BN in the federal G&C disclosure than in the CRA charities list (a related entity, e.g. a library board vs the
        # library's charity, or a keying error by the department): keep the charity / printed BN and record the other one for the reader
        x["buyer_bn_note"] = "the federal grants & contributions disclosure lists recipient_business_number %s for \"%s\" (%s agreement(s)); kept the BN above, which comes from the CRA charities list or the buyer's own page" % (g["bn_as_published"], g.get("matched_name") or "", g.get("agreements") or "?"); n_gcr["buyer_bn_conflict_noted"] += 1
    if g and not x.get("buyer_bn_as_published"):
        x["buyer_bn_as_published"] = "%s (recipient_business_number in the federal grants & contributions disclosure, %s agreement(s), last %s; %s)" % (g["bn_as_published"], g.get("agreements") or "?", g.get("last_agreement_date") or "n/a", g["source_url"]); n_gcr["buyer_bn"] += 1
        if not x.get("buyer_gst_hst_derived"):
            x["buyer_gst_hst_derived"] = g["bn9"] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"
    if g and g.get("matched_name") and g["bn9"] in (x.get("buyer_bn_as_published") or "") and register_name_takes(x.get("buyer_legal_name_as_published") or "", g["matched_name"]):
        # 2026-11-10: the recipient's legal name goes with its number — also on a row that had the number from another source and no name (until
        # this day the name was written only together with the number), and in the place of the same name read off a page
        x["buyer_legal_name_as_published"] = "%s (recipient legal name in the federal grants & contributions disclosure)" % g["matched_name"]; n_gcr["buyer_legal_name"] += 1
    vn = x.get("vendor") or ""
    g = GCR["vendor"].get(norm(vn)) if vn and not vn.startswith("inferred") else None
    if g and not x.get("vendor_bn9"):
        x["vendor_bn9"] = "%s (recipient_business_number in the federal grants & contributions disclosure, last agreement %s; %s)" % (g["bn9"], g.get("last_agreement_date") or "n/a", g["source_url"]); n_gcr["vendor_bn9"] += 1
        x["vendor_bn_source"] = x.get("vendor_bn_source") or "federal grants & contributions disclosure (recipient_business_number)"
        if not x.get("vendor_gst_hst_derived"):
            x["vendor_gst_hst_derived"] = g["bn9"] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"
# 2026-11-11: page furniture around a name read off a page (build of 01:51Z: 455 of 82,018 legal-name cells — "Lambton College Your Cart Check Out
# Continue Shopping", "· Temagami First Nation ·", "Town of Kapuskasing Freedom of Information", "Perfected Coffee and protected by intellectual
# property laws", "Privacy Policy The Redeemed Christian Church of God"); and the legal person a sentence names as the owner ("DIV7 is a Division
# of Naro Building Systems Inc", "HR Property Maintenance · Operated by Haryana Enterprises Ltd"). Names that come from a register are not touched.
_TP_PAGE = re.compile(r"(?:stated on|printed with its legal form|schema\.org|the name on the organisation's own home page|the organisation's name as the source|the copyright line of)")
def cell_split(cell):
    """a cell "NAME (source text)" -> (NAME, " (source text)"); the source is the bracket that ends the cell and begins with a small letter (or
    "CRA …"); a name's own brackets stay in the name ("CHICKPEA FOOD (MAIN STREET) INC. (the City of Vancouver's open data list …)")"""
    c = cell or ""
    if c.endswith(")"):
        depth = 0
        for i in range(len(c) - 1, -1, -1):
            if c[i] == ")":
                depth += 1
            elif c[i] == "(":
                depth -= 1
                if depth == 0:
                    if i > 0 and c[i - 1] == " " and re.match(r"[a-z]|CRA ", c[i + 1:]):
                        return c[:i - 1], c[i - 1:]
                    break
    return c, ""
_TP_LEAD = re.compile(r"^(?:[\s·•┃|+»>*–—-]+|\d{1,4}\s*[·•|]\s*|(?:copyright|©|\(c\))\s*(?:(?:19|20)\d\d)?\s*|(?:privacy (?:policy|notice)(?: (?:for|of))?|privacy office of|terms (?:and|&) conditions(?: introduction in)?|"
                      r"agreement to terms|terms of (?:use|service)|conditions g[ée]n[ée]rales(?: de vente)?|politique de confidentialit[ée]|welcome to|bienvenue (?:chez|[àa]|au|sur le site de)|"
                      r"official (?:web)?site of|site (?:web )?officiel (?:de la|du|de|des)|facebook|instagram|twitter|youtube|linkedin|tiktok|pinterest)\s+)+", re.I)
_TP_TAIL = re.compile(r"\s+(?:and (?:is |are )?protected\b|or its (?:content )?suppliers\b|(?:or|and|and/or) (?:its|their) (?:respective )?(?:owners?|licensors?|licensees?|information providers?|affiliates?|partners?|agents?|subsidiaries|third[- ]party \w+)\b|"
                      r"unless otherwise (?:stated|noted|indicated|specified)\b|for use (?:within|on|in|by)\b|[Tt]hroughout$|[Hh]ereinafter$|[Hh]erein$|[Cc]ollectively$|and will\b|will (?:take|be|not)\b|[Ww]e value\b|[Yy]our [Cc]art\b|[Pp]lease (?:select|note|contact)\b|Non-discrimination Policy\b|"
                      r"(?:Accessibility\s+)?Freedom of Information\b|at such time\b|[Gg]et in touch\b|Scroll to Top\b|Loading\b|Translate\b|Log in\b|E-commerce$|Discover$|and/or its (?:affiliates|subsidiaries)\b|×).*$")
_TP_OWNER = re.compile(r"^(.{0,70}?)(?:\s|^)(?:((?:is )?(?:an?|the) (?:registered trade ?name|trade ?name|registered business name|business name|operating name) of)|"
                       r"(is (?:an?|the) (?:division|subsidiary|product|service|brand) of|(?:is |are )?(?:owned and )?operated by:?|o/o by:?)|"
                       r"((?:is|are) (?:an? |the )?(?:registered )?trade ?marks? (?:of|owned by)))\s+(.{3,80})$", re.I)
_TP_IS = re.compile(r"\s+(?:(is|are|was|were)\s+(?:an?|the|registered|members?|owned|operated|located|committed|proud)\b|(?:IS|is) (?:A|a) (?:registered )?501).*$")
_TP_SEP = re.compile(r"\s*(?:-->|·|»|\s\|\s)\s*")
_TP_FORM = re.compile(r"\b(?:inc|ltd|llc|corp|corporation|limited|incorporated|lt[ée]e|limit[ée]e|llp|plc|gmbh|s\.?e\.?n\.?c\.?(?:r\.?l\.?)?)\b\.?", re.I)
_TP_BARE = re.compile(r"^(?:inc|ltd|llc|corp|limited|incorporated|lt[ée]e|s\.?e\.?n\.?c)\b\.?(?:\s|$|\.|,)", re.I)
_TP_CAMEL = re.compile(r"^[a-z]{1,6}[A-Z0-9][\w&.'’ -]{2,70}$")
def _tp_clean(cand, buyer):
    """clean_legal, plus a name that begins with a small letter by design ("pureBalance Wellness Centre Inc", "eGrr Services Inc.")"""
    cand = cand.strip(" ,-–—|:·•┃»>;")
    out = clean_legal(cand, buyer)
    if not out and _TP_CAMEL.match(cand) and _TP_FORM.search(cand[-14:]) and not BAD_LEGAL.search(cand):
        out = cand
    if not out or _TP_BARE.match(out):
        return ""
    if cand.endswith(".") and _TP_FORM.search(cand[-8:]) and out == cand[:-1]:
        out = cand  # the full stop of "Inc." stays
    return out
def tidy_page_name(cell, buyer="", site=""):
    """-> (cell, what): what = "" (unchanged), "tidied", "owner" (the legal person the text names behind the name) or "fragment" (cell "")"""
    name, src = cell_split(cell)
    if src and not _TP_PAGE.match(src[2:]):
        return cell, ""  # a register's or a list's name
    n0 = re.sub(r"[⠀ \s]+", " ", name).strip()
    d = _TP_OWNER.match(n0)
    if d:
        head, y = d.group(1).strip(" ·;,"), d.group(5).strip()
        if d.group(2) or (d.group(3) and _TP_FORM.search(y)):
            out = _tp_clean(y, buyer)  # "X is the operating name of Y", "X is a division of Y Inc", "X · Operated by Y Ltd": Y is the legal person behind X
            return (out + src, "owner") if out else ("", "fragment")
        if d.group(4) and _TP_FORM.search(y) and name_overlap(y, buyer, site):
            out = _tp_clean(y, buyer)  # a trademark notice names the mark's owner — a parent, a licensor, Apple: taken only when it carries the organisation's own name
            return (out + src, "owner") if out else ("", "fragment")
        return "", "fragment"
    parts = [q for q in _TP_SEP.split(n0) if q.strip()]
    order = ([q for q in parts if _TP_FORM.search(q)] + [parts[0]]) if len(parts) > 1 else [n0]
    for cand in order:
        cand = _TP_LEAD.sub("", cand)
        # 2026-11-11: a page word run into the name ("History Vancouver Poetry House Society" on the About page of Vancouver Poetry House): dropped
        # when what follows begins like the organisation's own name (in a sample of 45 published names "stated on" a page, 8 carried such a word
        # or a clause of the sentence — "… or its licensors", "… unless otherwise stated", "… for use within")
        _w = cand.split()
        if len(_w) >= 3 and _w[0].lower() in ("history", "home", "about", "contact", "menu", "welcome", "overview", "mission", "team", "accueil", "historique") \
                and buyer and re.sub(r"^(?:the|la|le|les)\s+", "", buyer.strip(), flags=re.I).lower().startswith(_w[1].lower()):
            cand = " ".join(_w[1:])
        if cand.startswith("[") and "]" not in cand:
            cand = cand[1:]
        cand = _TP_TAIL.sub("", cand)
        mm = _TP_IS.search(cand)
        if mm:
            head = cand[:mm.start()].strip()
            if (mm.group(1) or "").lower() in ("are", "were") or (len(head.split()) < 2 and not _TP_FORM.search(head)):
                continue  # a sentence about a group or a person ("Kinesiologists are members of …", "Stephen is a board certified …")
            cand = head
        cand = cand.strip(" ,-–—|:·•┃»>;")
        if cand == n0:
            return cell, ""
        w = cand.split()
        if len(w) >= 3 and w[-1].lower() == w[0].lower():
            cand = " ".join(w[:-1])  # "Capita plc Capita (is an …)"
        out = _tp_clean(cand, buyer)
        if out:
            return out + src, "tidied"
    return "", "fragment"
_TP_CLAUSE = re.compile(r"\s+(?:(?:or|and|and/or) (?:its|their) (?:respective )?(?:owners?|licensors?|licensees?|information providers?|affiliates?|partners?|agents?|subsidiaries|(?:content )?suppliers)\b|"
                        r"unless otherwise (?:stated|noted|indicated|specified)\b|for use within\b).*$")
n_tp = collections.Counter()
for x in rows:
    _c = x.get("buyer_legal_name_as_published") or ""
    if _c:
        _new, _what = tidy_page_name(_c, x.get("buyer") or "", x.get("buyer_website") or "")
        if _what:
            n_tp[_what] += 1
            x["buyer_legal_name_as_published"] = _new
            # a row named after that very statement ("ProVision Coaching Network or its information providers") takes the tidied name too
            _old = cell_split(_c)[0].strip()
            if _what == "tidied" and _new and (x.get("buyer") or "").strip() == _old:
                x["buyer"] = cell_split(_new)[0].strip() or x["buyer"]; n_tp["row's own name tidied with it"] += 1
    # the same clauses at the end of a row's own name when no legal-name cell carries it (the name came from the same sentence)
    _b = x.get("buyer") or ""
    if _b and _TP_CLAUSE.search(_b):
        _nb = _TP_CLAUSE.sub("", _b).strip(" ,-–—|:·")
        if len(_nb) >= 3 and _nb != _b:
            x["buyer"] = _nb; n_tp["row's own name: a clause of the sentence cut off"] += 1
print("legal names read off a page, tidied:", dict(n_tp))
_WELCOME = re.compile(r"^(?:welcome to|bienvenue (?:chez|[àa]|au|sur le site de)|official (?:web)?site of)\s+(?=\S+\s+\S)", re.I)
# 2026-11-10: a name that carries its company form ("Kobes Welding Ltd.", "Plumblink Plumbing Inc.") is the legal name as published — by the organisation
# itself when it is the name on its own home page, else by the source of the row's record. Last in the chain: every register and every statement of the
# site goes first, and the registry tools look the name up as before (a register's name then takes the cell). 6,228 rows of the build of 2026-11-10
# 22:38Z had such a name and an empty legal-name cell.
n_lform = 0
for x in rows:
    if x.get("buyer_legal_name_as_published"):
        continue
    _bn0 = re.sub(r"\s+", " ", x.get("buyer") or "").strip()
    _bn = _WELCOME.sub("", _bn0)  # "Welcome to Quantum Internet Solutions Ltd." is the page's title: the name is what follows
    if _CORP_FORM_END.search(_bn) and 5 <= len(_bn) <= 90 and not DOMAIN_NAME.match(_bn) and not _PLATFORM_CO.search(_bn) and not re.search(r"[|/()]| - | – |\. ", _bn):
        _lf = next((LFACTS[_k] for _k in (x.get("keys") or "").split("|") if _k in LFACTS), None)
        if _lf and norm(_lf.get("site_name") or "") in (norm(_bn), norm(_bn0)):
            _wh = "the name on the organisation's own home page, %s, read %s" % (_lf.get("site") or x.get("buyer_website") or "", _lf.get("date") or "")
        else:
            _wh = "the organisation's name as the source of this row's record gives it"
        x["buyer_legal_name_as_published"] = "%s (%s; it carries its legal form; not checked against a company register)" % (_bn, _wh)
        n_lform += 1
print("legal name: the organisation's own name carries its legal form (cells still empty after every register and site statement): %d" % n_lform)
# 2026-11-11: the organisation a certificate authority validated. The Certificate Transparency logs (tools/ct_names.py reads their names tiles)
# carry the subject of every certificate; for an organisation-validated certificate the authority checked that the organisation exists under
# that name at that place (O=, L=, ST=, C=). Kept by the reader: subjects with country CA and the domains the certificate covers. Used here for
# a legal-name cell still EMPTY after every other source (the row's own name with its legal form included), when the row's site is one of
# those domains and the subject carries the organisation's own name — a
# certificate's subject is its subscriber, which can be the host or the CDN that covers its customers' names ("Fastly, Inc." on a
# thousand sites), and a certificate that covers more than a dozen domains is such a one. The cell says where the name was read: the
# names tile (a public, immutable file) and the certificate's own name.
OVC, n_ovc = {}, collections.Counter()
_OV_OTHER = re.compile(r"(?i)\b(?:foundation|fondation|auxiliary|auxiliaire|alumni|dipl[ôo]m[ée]s|students?['’]? (?:union|association|society|council)|association [ée]tudiante|faculty association|"
                       r"staff association|union|syndicat|club|friends of|amis d[eu]|retirees|retrait[ée]s)\b")
try:
    import glob as _gov
    _ov_logs = {}
    try:
        _ov_logs = {k_: (v_.get("url") or "") for k_, v_ in (json.load(open(ROOT + "/data/incoming/claude/ct_names/cursor.json", encoding="utf-8")).get("logs") or {}).items()}
    except Exception:
        pass
    def _ov_tile(n):
        t = "%03d" % n
        while len(t) % 3:
            t = "0" + t
        q = [t[i:i + 3] for i in range(0, len(t), 3)]
        return "/".join(["x" + z for z in q[:-1]] + [q[-1]])
    for _p in sorted(_gov.glob(ROOT + "/data/incoming/claude/ct_names/ov_ca_*.jsonl.gz")):
        with gzip.open(_p, "rt", encoding="utf-8") as _f:
            for _l in _f:
                try:
                    _o = json.loads(_l)
                except ValueError:
                    continue
                _org = "; ".join((_o.get("s") or {}).get("Organization") or []).strip()
                if not _org or not (1 <= len(_o.get("d") or []) <= 12):
                    continue
                for _d in _o["d"]:
                    OVC.setdefault(_d, []).append(_o)
    for x in rows:
        if x.get("buyer_legal_name_as_published") or not x.get("buyer_website"):
            continue
        _d = registrable(host_of(x["buyer_website"]) or "")
        if not _d or SHARED_GOV.match(_d) or not OVC.get(_d):
            continue  # a government's shared domain: the certificate is the government's, the row may be a board or an office of its own
        _bn = re.sub(r"\s+", " ", x.get("buyer") or "").strip()
        for _o in OVC.get(_d) or ():
            _s = _o["s"]
            _org = re.sub(r"\s+", " ", "; ".join(_s.get("Organization") or [])).strip()
            # the subject must be the organisation of THIS row. A row with a name of its own: the two names share a distinctive word ("SaskTel"
            # on a village's page under sasktel.net fits the site and not the village), the row is not another body beside it (a hospital's
            # foundation, a university's student union) and not a company with its own legal form (TELUS Health (Canada) Ltd. is not TELUS
            # Corporation). A row known by its domain only: the subject must fit the site's own name.
            _core = re.sub(r"\s*\([^()]*\)\s*$", "", _bn)
            if DOMAIN_NAME.match(_bn) or not re.search(r"[A-Za-zÀ-ÿ]{4}", _bn):
                _ok = site_fits_name(_org, x["buyer_website"])
            else:
                _ok = (name_fits(_bn, _org) and name_overlap(_org, _bn, x["buyer_website"])
                       and not (_OV_OTHER.search(_bn) and not _OV_OTHER.search(_org))
                       and not ((_CORP_FORM_END.search(_bn) or _CORP_FORM_END.search(_core)) and not (same_legal_name(_bn, _org) or same_legal_name(_core, _org))))
            if generic_only_name(_org) or not _ok:
                n_ovc["subject does not carry the organisation's own name: not taken"] += 1
                continue
            _where = ", ".join(z for z in ("; ".join(_s.get("Locality") or []), "; ".join(_s.get("Province") or []), "CA") if z)
            _url = (_ov_logs.get(_o.get("log") or "") + "tile/names/" + _ov_tile(int(_o["tile"]))) if _ov_logs.get(_o.get("log") or "") and _o.get("tile") is not None else ""
            _day = _tm.strftime("%Y-%m-%d", _tm.gmtime(int(_o["ts"]) / 1000)) if _o.get("ts") else ""
            x["buyer_legal_name_as_published"] = "%s (organisation validated by a certificate authority: subject O=%s, %s of the certificate for %s; Certificate Transparency log %s%s%s)" % (
                _org, _org, _where, _s.get("CommonName") or _d, _o.get("log") or "", (", names tile %s" % _url) if _url else "", (", logged %s" % _day) if _day else "")
            n_ovc["buyer_legal_name"] += 1
            break
except Exception as _e:
    print("validated certificate subjects skipped: %s" % _e)
print("legal names from validated certificate subjects (Certificate Transparency): domains on file %d;" % len(OVC), dict(n_ovc))
# 2026-11-12 (rows read for the owner: "no hallucinations … don't misappropriate … everything exact"): the last look at the buyer's legal-name cell.
# A name read off a page loses a web agency's credit or a page word run onto it ("City of Port Coquitlam Footer", "Municipalité de Val-Morin
# Conception", "Ville de St-Honoré Une réalisation de Devicom", "Tous droits réservés, SPCTE Inc"); a photo credit, a slogan or a headline is
# no name ("Photos courtoisie …", "… the customer always comes first", "30 SCHOOLS IN THE NEWS STORY"); a professional regulator's name read on
# a member's site is not the member's ("Ordre des Arpenteurs-Géomètres" on a surveying firm's). A Wikidata label is kept only when it is the
# organisation's own name or its acronym's expansion — not a translation ("Umeå University"), an old name, or another body ("Public Safety
# Canada" for Québec's Ministère de la Sécurité publique, "European Central Bank" for the European Commission). Register names are untouched.
_LN_JUNK_TAIL = re.compile(r"\s+(footer|header|une r[ée]alisation|r[ée]alisation|conception|t[ée]moins de navigation|apply now|in the news|access to information|"
                           r"acc[eè]s [àa] l.information|contacts? directory|open data|site ?map|plan du site|newsletter)\b.*$", re.I)
_LN_JUNK_HEAD = re.compile(r"^(?:tous droits r[ée]s\w*v[ée]s|all rights reserved|copyright|©)\s*[,.:;–—-]*\s*", re.I)
_LN_NOT_A_NAME = re.compile(r"^(?:photos?|cr[ée]dits?)\b|courtoisie|the customer always|get the credit|\bapply now\b|\bnews story\b|\bin the news\b", re.I)
_LN_REGULATOR = re.compile(r"^(?:ordre|order of|barreau|law society|chambre des notaires|coll[eè]ge des (?:m[ée]decins|pharmaciens|dentistes|naturopathes|enseignants))\b", re.I)
_LN_REGISTER_SRC = re.compile(r"^\s*\((?:as registered|CRA list|holder of the charity registration|organisation validated by a certificate authority|the Canadian trademarks register|"
                              r"the R[ée]gie|the City of [A-Za-z]+'s open data|the [A-Za-z ]+'s list of active licences|recipient legal name|provincial municipal directory)|global LEI register", re.I)
n_lnf = collections.Counter()
def _acr_of(s):
    return "".join(w[0] for w in norm(s).split() if w not in ("of", "the", "and", "de", "du", "des", "la", "le", "les", "et", "for", "a", "l", "d"))
for x in rows:
    _c = x.get("buyer_legal_name_as_published") or ""
    if not _c:
        continue
    _nm, _src = cell_split(_c)
    _b = x.get("buyer") or ""
    _new = _nm.strip()
    if not _LN_REGISTER_SRC.search(_src):
        _h0 = _LN_JUNK_HEAD.sub("", _new)
        if _h0 != _new:
            _new = _h0.strip(" ,-–—|:")
        _mt = _LN_JUNK_TAIL.search(_new)
        if _mt and not re.search(r"(?<![a-zà-ÿ])%s(?![a-zà-ÿ])" % re.escape(_mt.group(1).lower()), _b.lower()):
            _new = _new[:_mt.start()].strip(" ,-–—|:")
            if _new and not name_overlap(_new, _b, x.get("buyer_website") or ""):
                _new = ""  # what is left is someone else's name ("Audet Photo SERVICES Réalisation de projets Construction Mafranc inc")
            n_lnf["a web agency's credit or a page word cut off the end (footer, conception, réalisation …)"] += 1
        if _new and _LN_NOT_A_NAME.search(_new):
            _new = ""; n_lnf["not a name (a photo credit, a slogan, a headline): cell emptied"] += 1
        elif _new and _LN_REGULATOR.search(_new) and not norm(_b).startswith(" ".join(norm(_new).split()[:2])):
            _new = ""; n_lnf["a professional regulator's name read on a member's site: cell emptied"] += 1
    if _new and "Wikidata" in _src:
        _nn, _nb = norm(_new), norm(_b)
        _same = bool(_nn) and bool(_nb) and (_nn == _nb or (" %s " % _nb) in (" %s " % _nn) or (" %s " % _nn) in (" %s " % _nb))
        _acr = bool(re.fullmatch(r"[A-Z0-9&]{2,8}", _b.strip() or "-")) and _acr_of(_new).startswith(_nb.replace(" ", ""))
        _flat_b = _nb.replace(" ", "")
        _shared = bool({w for w in _nn.split() if len(w) >= 4 and w not in GENERIC_TOK} & {w for w in _nb.split() if len(w) >= 4 and w not in GENERIC_TOK}) \
            or any(len(w) >= 6 and w in _flat_b for w in _nn.split() if w not in GENERIC_TOK)
        if "label per Wikidata" in _src and not (_same or _acr):
            _new = ""; n_lnf["a Wikidata label that is not the organisation's own name (a translation, another body, an old name): cell emptied"] += 1
        elif not (_same or _acr or _shared) or re.search(r"dioecesis", _new, re.I) or not _nn:
            _new = ""; n_lnf["a Wikidata official name sharing nothing with the organisation's name: cell emptied"] += 1
    if _new != _nm.strip():
        x["buyer_legal_name_as_published"] = (_new + _src) if _new else ""
print("buyer legal names, last check:", dict(n_lnf))
# 2026-11-12 (rows read for the owner, "don't misappropriate … addresses"): a member directory's page prints the body's own address in its
# footer, and 160 ready rows had taken it as the member's ("102, 150 Edwards Way NW, Airdrie" — the Airdrie chamber's — on every Airdrie
# member's row); a directory whose page title stood where the member's name goes named five Tofino businesses "Tofino Chamber of Commerce".
# The body's own address is not the member's, the body's name is not the member's, and a run of page words with no number, postal code,
# province or comma is no address ("NEWS UPDATES PREMIER PARTNERS … ARBIOS BIOTECH").
_PCX = re.compile(r"\b([A-Z]\d[A-Z])\s?(\d[A-Z]\d)\b")
_PROVX = re.compile(r"\b(?:AB|BC|MB|NB|NL|NS|NT|NU|ON|PE|QC|SK|YT|Alberta|British Columbia|Manitoba|New Brunswick|Newfoundland|Nova Scotia|Ontario|"
                    r"Prince Edward Island|Qu[ée]bec|Saskatchewan|Yukon)\b|\b[A-Z]{2}\s+\d{5}\b", re.I)
n_addr = collections.Counter()
for x in rows:
    _a = x.get("buyer_address") or ""
    _ap = _a.split(" (")[0]
    if _a and "(as printed in " in _a:
        _va = (x.get("vendor_address") or "").split(" (")[0]
        _m1, _m2 = _PCX.search(_ap.upper()), _PCX.search(_va.upper())
        _n1, _n2 = re.findall(r"\d+", _ap.split(",")[0] if "," in _ap else _ap)[:2], re.findall(r"\d+", _va)[:3]
        _core = lambda s_: re.sub(r"[^A-Z0-9]", "", s_.upper())
        if _va and (_core(_ap) == _core(_va) or (_m1 and _m2 and _m1.groups() == _m2.groups() and _n1 and any(n_ in _n2 for n_ in _n1))):
            x["buyer_address"] = ""; n_addr["a directory's own address (the body's) taken as the member's: removed"] += 1
            continue
    if _ap and not re.search(r"\d", _ap) and not _PROVX.search(_ap) and "," not in _ap and not _a.startswith("postal code") and (
            len(_ap.split()) >= 5 or re.search(r"\b(?:news|updates?|newsletter|archive|menu|home|contact|partners?|agreement)\b", _ap, re.I)):
        x["buyer_address"] = ""; n_addr["page words with no number, postal code, province or comma: removed"] += 1
for x in rows:
    _vn = re.sub(r"^[—–-]+\s*", "", re.sub(r"\s*\(.*$", "", x.get("vendor_legal_name") or re.sub(r"^inferred:\s*", "", x.get("vendor") or "")))
    _flat = lambda s_: re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s_ or "").encode("ascii", "ignore").decode().lower())
    if _vn and _flat(x.get("buyer")) and _flat(x.get("buyer")) == _flat(_vn):
        _ln0 = cell_split(x.get("buyer_legal_name_as_published") or "")[0].strip()
        _alt = _ln0 if (_ln0 and _flat(_ln0) != _flat(_vn)) else registrable(host_of(x.get("buyer_website") or "") or "") or (x.get("email") or "").partition("@")[2]
        if _alt:
            x["buyer"] = _alt; n_addr["the vendor's name stood where the buyer's goes: replaced by the buyer's own legal name or domain"] += 1
print("buyer address and name, last check:", dict(n_addr))
print("grants & contributions recipient BNs: %d buyers, %d vendors in file; filled %s" % (len(GCR["buyer"]), len(GCR["vendor"]), dict(n_gcr)))
# 2026-11-11: the vendor's legal name, last links of the chain (build of 01:51Z: 63,216 named-vendor rows without one; one host's 7,333 rows).
# (1) data/incoming/claude/claude_vendor_names_read.csv — the vendor's own terms of service read by hand for the vendors with the most rows whose
#     legal pages the site reader does not reach ("… are operated by WHC Online Solutions Inc", two links below the home page); URL + quote kept.
# (2) a vendor name that itself carries the company form ("Octopusapp Inc. dba Jobber", "TMX Group Limited"), as the buyer side does.
VNR = {}
_vnr = ROOT + "/data/incoming/claude/claude_vendor_names_read.csv"
if os.path.exists(_vnr):
    for _r in csv.DictReader(open(_vnr, encoding="utf-8")):
        if _r.get("domain") and _r.get("legal_name") and _r.get("url") and _r.get("quote"):
            VNR[_r["domain"].strip().lower()] = _r
n_vln = collections.Counter()
for x in rows:
    if x.get("vendor_legal_name"):
        continue
    _inf = (x.get("vendor") or "").startswith("inferred")
    _vd = registrable(host_of(x.get("vendor_website") or "") or "")
    _r = VNR.get(_vd) or VNR.get(re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", re.sub(r"\s*\([^()]*\)\s*$", "", re.sub(r"^inferred:\s*", "", x.get("vendor") or ""))).encode("ascii", "ignore").decode().lower()))
    if not _r and _inf:
        continue  # an inferred vendor's name is ours, not a source's: only a name read on a page (the table above) or a register (below) is printed
    if _r:
        x["vendor_legal_name"] = "%s (stated on %s: “%s”; %s, read %s)" % (_r["legal_name"], _r["url"], re.sub(r"\s+", " ", _r["quote"]).replace("(", "[").replace(")", "]")[:220], _r.get("how") or "read on the vendor's own page", _r.get("read_date") or "")
        if _r.get("trading_name") and not x.get("vendor_trading_name"):
            x["vendor_trading_name"] = "%s (the name the vendor trades under on %s)" % (_r["trading_name"], "https://%s/" % _r["domain"])
        n_vln["the vendor's own terms, read by hand"] += 1
        continue
    _vn = re.sub(r"\s+", " ", x.get("vendor") or "").strip()
    _two = legal_and_trade(_vn)
    _cand = _two[0] if _two else _vn
    if _CORP_FORM_END.search(_cand) and 5 <= len(_cand) <= 90 and not DOMAIN_NAME.match(_cand) and not re.search(r"[|/]| - | – |\. \S", _cand):
        x["vendor_legal_name"] = "%s (the vendor's name as the source of this row's record gives it; it carries its legal form; not checked against a company register)" % _cand
        if _two and not x.get("vendor_trading_name"):
            x["vendor_trading_name"] = "%s (the name it does business as, in the same record)" % _two[1]
        n_vln["the vendor's own name carries its legal form"] += 1
print("vendor legal name, last links of the chain:", dict(n_vln))
# 2026-11-11: the vendor of a row is itself an organisation of this table — the city that issues the business licence, a board of trade, a
# Crown corporation (tier M of the build of 01:51Z: vendor website 6.5 %, telephone 3.4 %, number 1.9 %; "The City of Calgary", 625 rows, with
# none of them while the row "City of Calgary" carries calgary.ca). What that organisation's own row publishes is the same organisation's:
# its website, telephone, legal name and number are carried to the vendor side, each still with its own source. Same name (a leading "The"
# apart) and the same province — "City of Richmond" in British Columbia is not the one in Virginia.
_CA_PROVS = {"AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"}
def _prov_in(text):
    m = _CA_PROV.findall(text or "")
    return m[-1] if m else ""
_AS_BUYER = {}
for y in rows:
    _j = (y.get("jurisdiction") or "").upper()[:2]
    if _j in _CA_PROVS and (y.get("buyer_website") or y.get("buyer_phone")):
        _k = (norm(re.sub(r"^the\s+", "", y.get("buyer") or "", flags=re.I)), _j)
        if len(_k[0]) >= 6 and (_k not in _AS_BUYER or len(y.get("buyer_legal_name_as_published") or "") > len(_AS_BUYER[_k].get("buyer_legal_name_as_published") or "")):
            _AS_BUYER[_k] = y
n_vb = collections.Counter()
for x in rows:
    _vn = re.sub(r"\s*\([^()]*\)\s*$", "", re.sub(r"^inferred:\s*", "", x.get("vendor") or ""))
    _pv = _prov_in((x.get("vendor_address") or "").split(" (")[0]) or _prov_in((x.get("vendor_country_basis") or "")[:260])
    y = _AS_BUYER.get((norm(re.sub(r"^the\s+", "", _vn, flags=re.I)), _pv)) if _vn and _pv else None
    if not y or y is x:
        continue
    _row = "this table's own row “%s”" % (y.get("buyer") or "")
    if not x.get("vendor_website") and y.get("buyer_website"):
        x["vendor_website"], x["vendor_website_basis"] = y["buyer_website"], "the vendor is itself an organisation of this table: its website as %s gives it" % _row
        n_vb["vendor_website"] += 1
    if not x.get("vendor_phone") and y.get("buyer_phone"):
        x["vendor_phone"] = y["buyer_phone"]; n_vb["vendor_phone"] += 1
    if not x.get("vendor_legal_name") and y.get("buyer_legal_name_as_published"):
        x["vendor_legal_name"] = y["buyer_legal_name_as_published"]; n_vb["vendor_legal_name"] += 1
    _bn = re.match(r"\s*(\d{9})\b", y.get("buyer_bn_as_published") or "")
    if not x.get("vendor_bn9") and _bn:
        x["vendor_bn9"] = "%s (the number %s carries: %s)" % (_bn.group(1), _row, re.sub(r"\s+", " ", (y.get("buyer_bn_as_published") or ""))[:160].replace("(", "[").replace(")", "]"))
        x["vendor_bn_source"] = x.get("vendor_bn_source") or "the vendor's own row in this table"
        if not x.get("vendor_gst_hst_derived"):
            x["vendor_gst_hst_derived"] = _bn.group(1) + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"
        n_vb["vendor_bn9"] += 1
print("vendors that are organisations of this table (same name, same province): facts carried from their own row:", dict(n_vb))
# the buyers' own purchase-order / contract open data joined to existing pairs (tools/po_opendata.py → claude_po_records.csv; downstream §1.1)
POD = collections.defaultdict(list)
_pop = ROOT + "/data/incoming/claude/claude_po_records.csv.gz"
if not os.path.exists(_pop) and os.path.exists(_pop[:-3]):
    _pop = _pop[:-3]
# 2026-11-10: only the records of a (buyer, vendor) pair that some row can ask for are kept, and only the six cells the join prints (the file's
# 555,539 records as whole dicts were ~2 GB of memory for a dozen matching pairs)
def _po_keys(x):
    bkeys = {parent(x.get("buyer") or ""), parent((x.get("buyer_legal_name_as_published") or "").split(" (")[0]), (x.get("org_group_key") or "").split(" | ")[0]} - {""}
    vkeys = {norm(x.get("vendor") or ""), parent(x.get("vendor") or ""), norm((x.get("vendor_legal_name") or "").split(" (")[0]), parent((x.get("vendor_legal_name") or "").split(" (")[0])} - {""}
    return bkeys, vkeys
_need_p = set()
for x in rows:
    if not (x.get("vendor") or "").startswith("inferred"):
        _bk, _vk = _po_keys(x)
        _need_p |= {(b, v) for b in _bk for v in _vk}
_need_b = {b for b, _ in _need_p}
_n_po_read = 0
if os.path.exists(_pop):
    for _r in csv.DictReader((gzip.open(_pop, "rt", encoding="utf-8", errors="replace") if _pop.endswith(".gz") else open(_pop, encoding="utf-8", errors="replace"))):
        _n_po_read += 1
        _pb = parent(_r["buyer"])
        if _pb not in _need_b:
            continue
        _t = {"po_number": _r["po_number"], "date": _r["date"], "amount": _r["amount"], "kind": _r["kind"], "source_url": _r["source_url"], "id_label": _r["id_label"]}
        _nv = norm(_r["vendor_name"])
        if (_pb, _nv) in _need_p:
            POD[(_pb, _nv)].append(_t)
        pv = parent(_r["vendor_name"])
        if pv and pv != _nv and (_pb, pv) in _need_p:
            POD[(_pb, pv)].append(_t)
n_po = collections.Counter()
for x in rows:
    for c in ("po_numbers_this_pair_open_data", "po_count_this_pair_open_data", "contract_numbers_this_pair_open_data"):
        x.setdefault(c, "")
    if not POD or (x.get("vendor") or "").startswith("inferred"):
        continue
    bkeys, vkeys = _po_keys(x)
    hits = []
    for b in bkeys:
        for v in vkeys:
            hits += POD.get((b, v), [])
    if not hits:
        continue
    hits = sorted({(h["po_number"], h["date"], h["amount"], h["kind"], h["source_url"], h["id_label"]) for h in hits}, key=lambda t: t[1], reverse=True)
    pos = [h for h in hits if h[3] == "po"]; cons = [h for h in hits if h[3] != "po"]
    n_po["pairs"] += 1
    if pos:
        x["po_numbers_this_pair_open_data"] = "; ".join("%s (%s%s)" % (h[0], h[1] or "undated", (", " + h[2]) if h[2] else "") for h in pos[:8])[:400] + " — %s" % pos[0][5]
        x["po_count_this_pair_open_data"] = str(len(pos))
        if not x.get("po_number_as_published"):
            x["po_number_as_published"] = "%s (%s; the buyer's own open data %s; dated %s%s)" % (pos[0][0], pos[0][5], pos[0][4], pos[0][1] or "n/a", (", " + pos[0][2]) if pos[0][2] else ""); n_po["po_filled"] += 1
        if not x.get("invoice_reference_hint") or x["invoice_reference_hint"].startswith(("no identifier", "only system")):
            x["invoice_reference_hint"] = "most recent purchase-order number for this pair in the buyer's own open data: %s (%s)" % (pos[0][0], pos[0][1] or "undated")
    if cons:
        x["contract_numbers_this_pair_open_data"] = "; ".join("%s (%s%s)" % (h[0], h[1] or "undated", (", " + h[2]) if h[2] else "") for h in cons[:8])[:400] + " — %s" % cons[0][5]
        if not x.get("contract_or_agreement_number"):
            x["contract_or_agreement_number"] = "%s (%s; the buyer's own open data %s; dated %s)" % (cons[0][0], cons[0][5], cons[0][4], cons[0][1] or "n/a"); n_po["contract_filled"] += 1
print("buyers' PO / contract open data joined:", dict(n_po), "| records read:", _n_po_read, "| kept (a row's own buyer-vendor pair):", sum(len(v) for v in POD.values()))
del POD, _need_b, _need_p
# D2 / D12: back-reference between the contract dataset and the lead relationships (same organisation by website domain or exact name)
AGG_DOM, AGG_NAME = {}, {}
for _p, _o in orgs.items():
    _d = _dom_of((_o.get("be") or {}).get("official_website") or "")
    if _d and not SHARED_GOV.match(_d):
        AGG_DOM.setdefault(_d, _o)
    AGG_NAME.setdefault(norm(_o.get("name") or ""), _o)
LEAD_DOM, LEAD_NAME = _XLEAD if _XLEAD is not None else _lead_tables(leads)  # ranking in parts: the tables of every lead, built before the leads were split
n_x2 = collections.Counter()
for x in rows:
    x.setdefault("most_recent_record_reference_any_vendor", ""); x["records_in_contract_dataset"] = ""; x["other_relationship_sources"] = ""
    _d, _n = _dom_of(x.get("buyer_website") or ""), norm(x.get("buyer") or "")
    if x.get("_org") is None and x.get("tier") not in ("A", "B", "L", "C", "D", "F"):
        _o = (AGG_DOM.get(_d) if _d else None) or AGG_NAME.get(_n)
        if not _o:
            x["records_in_contract_dataset"] = "none found for this organisation (matched by website domain and exact name)"
        else:
            x["records_in_contract_dataset"] = "%d records with Canada-located vendors in the contract dataset (%d distinct vendors; latest %s; matched by %s)" % (_o["n"], len(_o["vendors"]), _o.get("latest") or "n/a", "website domain" if _d and AGG_DOM.get(_d) is _o else "exact name")
            if _o.get("latest_ref") and not x.get("most_recent_record_reference_any_vendor"):
                x["most_recent_record_reference_any_vendor"] = _o["latest_ref"]
            if x.get("invoice_reference_hint", "").startswith(("no identifier", "only system")) or not x.get("invoice_reference_hint"):
                x["invoice_reference_hint"] = "no identifier on this relationship; most recent contract-dataset reference for this buyer: %s" % _o["latest_ref"] if _o.get("latest_ref") else x.get("invoice_reference_hint", "")
            n_x2["lead rows with dataset history"] += 1
    else:
        x["records_in_contract_dataset"] = "%s records with Canada-located vendors (this row's organisation)" % x.get("contracts_with_canadian_suppliers") if x.get("contracts_with_canadian_suppliers") else ""
    _o2 = x.get("_org")
    for c in ("typical_contract_value_p50", "typical_contract_value_p75", "typical_contract_value_p90", "average_contract_duration_days", "commodity_distribution_top3", "year_over_year_spend_trend", "typical_cadence_days", "vendor_concentration_top_share", "all_canadian_vendors", "pair_prior_records", "pair_first_or_repeat", "pair_value_trend", "pair_dates_and_values"):
        x.setdefault(c, "" if _o2 else "no dataset record for this pair / buyer")
    if _o2:
        try:
            vals = sorted(_o2.get("vals") or [])
            if vals:
                x["typical_contract_value_p50"] = "%.2f" % vals[len(vals) // 2]; x["typical_contract_value_p75"] = "%.2f" % vals[min(len(vals) - 1, int(len(vals) * 0.75))]
            ds = sorted(set(dd[:10] for dd in (_o2.get("dates") or []) if len(dd) >= 10))
            if len(ds) >= 2:
                x["typical_cadence_days"] = str(round((datetime.date.fromisoformat(ds[-1]) - datetime.date.fromisoformat(ds[0])).days / (len(ds) - 1)))
            top = _o2["vendors"].most_common(1)
            if top and _o2["n"]:
                x["vendor_concentration_top_share"] = "%s: %d%% of %d records" % (top[0][0][:60], 100 * top[0][1] // _o2["n"], _o2["n"])
            x["all_canadian_vendors"] = "; ".join("%s (%d)" % (nn, cc) for nn, cc in _o2["vendors"].most_common())[:2000]
            if vals:
                x["typical_contract_value_p90"] = "%.2f" % vals[min(len(vals) - 1, int(len(vals) * 0.9))]
            if _o2.get("durs"):
                x["average_contract_duration_days"] = str(round(sum(_o2["durs"]) / len(_o2["durs"])))
                x["contract_durations_counted"] = str(len(_o2["durs"]))
            if _o2.get("coms"):
                x["commodity_distribution_top3"] = "; ".join("%s (%d)" % (cc, nn) for cc, nn in _o2["coms"].most_common(3))[:300]
            yv = sorted((y, v) for y, v in (_o2.get("yv") or {}).items() if y.isdigit())
            if len(yv) >= 2:
                x["year_over_year_spend_trend"] = "; ".join("%s: %.0f" % (y, v) for y, v in yv[-6:]) + (" — %s" % ("increasing" if yv[-1][1] > yv[-2][1] * 1.25 else "decreasing" if yv[-1][1] < yv[-2][1] * 0.8 else "stable") + " vs previous year (published values only)")
            vn = (x.get("vendor") or "").strip()
            pl = sorted(pp for pp in ((_o2.get("pairs") or {}).get(vn, [])) if pp[0])
            n_pair = _o2["vendors"].get(vn, 0)
            x["pair_prior_records"] = str(n_pair)
            x["pair_first_or_repeat"] = ("repeat relationship (%d records%s)" % (n_pair, (", %s to %s" % (pl[0][0][:10], pl[-1][0][:10])) if pl else "")) if n_pair > 1 else "single record of this pair in the dataset" if n_pair == 1 else "no record of this pair in the contract dataset"
            pv = [v for dd, v in pl if v > 0]
            if len(pv) >= 3:
                h = len(pv) // 2; a1, b1 = sum(pv[:h]) / h, sum(pv[h:]) / (len(pv) - h)
                x["pair_value_trend"] = "increasing" if b1 > a1 * 1.25 else "decreasing" if b1 < a1 * 0.8 else "stable"
            elif pv:
                x["pair_value_trend"] = "too few dated values (%d)" % len(pv)
            x["pair_dates_and_values"] = "; ".join("%s%s" % (dd[:10], (" %.2f" % v) if v > 0 else "") for dd, v in pl[-12:])[:400]
        except Exception as _e2:
            x["pair_value_trend"] = x.get("pair_value_trend") or ""
    _ls = (LEAD_DOM.get(_d) if _d else None) or LEAD_NAME.get(_n) or []
    if _ls and x.get("tier") in ("A", "B", "L", "C", "D", "F", "E", "M", "I", "R"):
        x["other_relationship_sources"] = "also seen in the lead files: " + "; ".join(sorted(set(_ls))[:6])[:600]; n_x2["dataset rows with lead relationships"] += 1
    _gw = next((GAVE_WAY[k_] for k_ in (x.get("keys") or "").split("|") if k_ in GAVE_WAY), "") if x.get("tier") == "I" else ""
    if _gw:  # the relationship that gave way to the distributor of the organisation's address (decided before P13): kept in sight, in words
        x["other_relationship_sources"] = (_gw + ((" | " + x["other_relationship_sources"]) if x.get("other_relationship_sources") else ""))[:1000]; n_x2["rows that carry the relationship that gave way"] += 1
    x.pop("_org", None)
print("back-references:", dict(n_x2))
_free(globals(), "leads", "LEAD_DOM", "LEAD_NAME", "_XLEAD", "orgs", "AGG_DOM", "AGG_NAME")
# D13: high-sensitivity buyers (downstream suppression), by the organisation's published name / type — a tag, never a removal
SENSITIVE = [("police oversight body", re.compile(r"serious incident response team|special investigations unit|bureau des enqu[êe]tes ind[ée]pendantes|independent investigations? (?:office|unit)|police (?:complaint|review|oversight)|civilian review and complaints|law enforcement review|commissaire [àa] la d[ée]ontologie polici[èe]re|office of the independent police review", re.I)),
             ("police service / police board", re.compile(r"\bpolice\b|\bpolici[èe]re?\b|s[ûu]ret[ée] du qu[ée]bec|\bRCMP\b|\bGRC\b|gendarmerie|\bOPP\b|constabulary|sheriff|law enforcement", re.I)),
             ("corrections / detention", re.compile(r"correctional|corrections\b|d[ée]tention|penitentiar|\bprison\b|\bjail\b|parole|probation|services correctionnels", re.I)),
             ("intelligence / security / defence", re.compile(r"security intelligence|communications security establishment|\bCSIS\b|\bSCRS\b|\bCSE\b|national defence|d[ée]fense nationale|armed forces|forces arm[ée]es|defence research|\bRDDC\b|\bDRDC\b|border services|services frontaliers|\bCBSA\b|\bASFC\b", re.I)),
             ("coroner / medical examiner", re.compile(r"\bcoroner|medical examiner|m[ée]decin l[ée]giste", re.I)),
             ("child / youth protection", re.compile(r"children'?s aid|child(?:ren)? and family services|child protection|protection de la jeunesse|\bDPJ\b|youth protection|child welfare|child and youth advocate|child advocacy", re.I)),
             ("shelter / crisis / sexual-assault service", re.compile(r"\bshelter\b|refuge pour femmes|maison d'h[ée]bergement|transition house|crisis (?:cent|line|servic)|distress cent|sexual assault|agression sexuelle|rape crisis|suicide prevention|women'?s (?:centre|center|resource)|interval house|violence (?:against|conjugale|familiale)", re.I)),
             ("courts / tribunals / legal aid", re.compile(r"\bcourt(?:s|house)?\b|tribunal|legal aid|aide juridique|judicial|magistrat", re.I)),
             ("health: mental health / addiction / sexual health", re.compile(r"mental health|sant[ée] mentale|addiction|toxicomanie|d[ée]pendance|psychiatri|sexual health|sant[ée] sexuelle|planned parenthood|hiv|aids committee|sida", re.I))]
n_sens = collections.Counter()
for x in rows:
    nm = " ".join((x.get(c) or "") for c in ("buyer", "buyer_legal_name_as_published", "buyer_type"))
    tag = next((lab for lab, rx in SENSITIVE if rx.search(nm)), "")
    if tag:
        x["sensitivity_tag"] = "high-sensitivity buyer (%s): suppress from outreach unless reviewed (tag from the organisation's published name / type)" % tag; n_sens[tag] += 1
    else:
        x["sensitivity_tag"] = "none identified from the organisation's name / type"
print("sensitivity tags:", dict(n_sens))
# D15: the template language to use, explicit for Québec
QC_HINT = re.compile(r"\b(qu[ée]bec|montr[ée]al|laval|gatineau|sherbrooke|saguenay|l[ée]vis|trois-rivi[èe]res|longueuil|cisss|ciusss|c[ée]gep|mrc\b|municipalit[ée] (?:de|du|des|d')|ville de|centre de services scolaire|commission scolaire|arrondissement|paroisse|canton de)\b", re.I)
for x in rows:
    j = x.get("jurisdiction") or x.get("_jur") or ""
    site = (x.get("buyer_website") or "").lower()
    addr = x.get("buyer_address") or ""
    qc = j == "QC" or (j in ("", "CA") and (".qc.ca" in site or site.rstrip("/").endswith(".quebec") or re.search(r"\bQC\b|Qu[ée]bec", addr) or re.search(r"\b[GHJ]\d[A-Z] ?\d[A-Z]\d\b", addr) or QC_HINT.search(x.get("buyer") or "")))
    lh = x.get("language_hint") or ""
    if qc:
        x["template_language"] = "fr (Québec buyer; French first%s)" % ("; its invoicing page is in English, English also accepted" if lh.startswith("en") else "")
    elif j == "NB" or (j == "FED") or re.search(r"\.gc\.ca|canada\.ca|gnb\.ca", site):
        x["template_language"] = "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: %s)" % (lh or "not detected")
    elif lh.startswith("fr"):
        x["template_language"] = "fr (invoicing page in French)"
    elif j in ("US", "UK", "AU", "NZ", "IE") or site.endswith((".gov", ".us", ".edu", ".gov.uk", ".gov.au")):
        x["template_language"] = "en"
    else:
        x["template_language"] = "en" if not lh or lh.startswith("en") else lh
# second pass over the site readers' facts: websites found later in the pipeline (Wikidata, vendor_sites_check, search proposals) missed the first
# org_contacts / org_extras join — 95 Gold rows had a vendor phone on file and "not_published" in the row (2026-11-08 19:30 EST)
n_late = collections.Counter()
for x in rows:
    for side in ("buyer", "vendor"):
        o = oc_of(x.get(side + "_website"), x.get(side) or "")
        if o:
            _ab = side == "vendor" and site_country(o) == "abroad"  # see "where an address is" above
            if not x.get(side + "_address") and o.get("address") and not _ab:
                x[side + "_address"] = o["address"]; n_late[side + "_address"] += 1
            if not x.get(side + "_phone") and o.get("phone") and not _ab and phone_fits(o["phone"], x.get(side + "_address")):
                x[side + "_phone"] = o["phone"]; n_late[side + "_phone"] += 1
            if side == "vendor" and not x.get("vendor_emails") and o.get("emails") and not (x.get("vendor") or "").startswith("inferred"):
                x["vendor_emails"] = o["emails"]; n_late["vendor_emails"] += 1
            if not x.get(side + "_contact_evidence_url"):
                x[side + "_contact_evidence_url"] = o.get("address_url") or o.get("phone_url") or o.get("emails_url") or ""
        e = ox_of(x.get(side + "_website"), x.get(side) or "")
        if e and e.get("logo_url") and not x.get(side + "_logo_url"):
            x[side + "_logo_url"] = e["logo_url"]; n_late[side + "_logo"] += 1
print("site readers, second pass (websites found late):", dict(n_late))
# 2026-11-10 (row audit): a client page, a logo wall or a customer story proves a relationship with the CANADA-LOCATED vendor only when the site
# that carries it is that vendor's own. The Mac-era lanes tied a vendor "located in Canada" by Wikidata, OpenStreetMap or a contract record to a
# website, and for a multinational's Canadian arm that website is the group's worldwide site: Okta's San Francisco site (an OpenStreetMap office
# "Okta - Toronto"), ibm.com for "IBM Canada", 3ds.com for "Dassault Systèmes (Canada)", kodak.com, a British rugby club's season page — their
# customers all over the world were delivered as customers of a Canadian vendor. Whose site it is, in the order of the evidence:
#   1. Wikidata (tools/site_owner_wd.py): the best-known organisation that gives the site as its official website, or the same-name parent
#      organisation of the Canadian item, has its headquarters outside Canada -> the group's site, not the Canada-located entity's own.
#      Headquarters in Canada -> its own site, whatever office the site reader happened to pick (Sid Lee's London office, Maplesoft's UK one).
#   2. No word from Wikidata: the address the site itself prints (tools/org_contacts.py). Outside Canada -> not shown to be the Canada-located
#      entity's site, unless a Canadian registry holds a corporation of the site's own name with its registered office in Canada and no
#      "… Canada Inc." national-arm name (eleven-x, Guardly: Canadian companies whose site prints a US office).
#   3. The site prints no address in Canada (or was not read) and the vendor is named as the Canadian arm of a group ("IBM Canada",
#      "DMG EVENTS (CANADA) INC.", "Okta - Toronto") on a site whose name carries no "canada" -> not shown either.
#   0. Before all that: a listing inside the site's Canadian section (kpmg.com/ca/en/…, ca.brinks.com) is the Canadian arm's own page.
# Such a row stays in the file as tier E with the reason. .ca sites are not concerned (a .ca registration requires Canadian presence).
# Measured 2026-11-10 on 3,250 such rows: the reader's single address alone was wrong for 17 of 76 sites that print a foreign address
# (Canadian companies with an office abroad), and Wikidata's "(Canada)" label suffix says nothing — hence the order above.
_ARM_NAME = re.compile(r"(?<!\bof )(?<!\bdu )(?<!\bde )\bcanada\)?,?\s*(?:inc|incorporated|incorpor[ée]e|ltd|lt[ée]e|limited|limit[ée]e|ulc|corp|corporation|co|lp|company|compagnie)?\.?\s*$", re.I)
_ARM_OFFICE = re.compile(r"\s[-–]\s(?:toronto|vancouver|montr[ée]al|ottawa|calgary|edmonton|winnipeg|qu[ée]bec|halifax|mississauga|waterloo)$", re.I)
_FOREIGN_FORM = re.compile(r"\b(?:llc|l\.l\.c\.|gmbh|plc|pty|b\.v\.|s\.a\.s\.?|a\.g\.|oy|ab)\b\.?\s*$", re.I)
def _legal_core(x):
    return re.sub(r"\s*\((?:as registered|stated on|schema\.org|as printed|carried from).*$", "", x.get("vendor_legal_name") or "").strip()
def arm_of_a_group(x, label):
    """the vendor is named as the national arm of a group, on a site whose own name carries no "canada" (Wikidata's "(Canada)" label suffix says nothing)"""
    if "canada" in label:
        return False
    v = re.sub(r"\s*\(canada\)\s*$", "", (x.get("vendor") or "").strip(), flags=re.I)
    for nm in (v, _legal_core(x)):
        if nm and not re.match(r"\W*canad", nm, re.I) and (_ARM_NAME.search(nm) or _ARM_OFFICE.search(nm)):
            return True
    return False
def formed_in_canada_under_the_sites_name(x, label):
    """a Canadian registry holds a corporation of the site's own name, registered office in Canada, not a national arm and not a foreign form"""
    legal, ra = _legal_core(x), (x.get("vendor_registered_address") or "").split(" (registered")[0]  # without the source note ("… Canada's Business Registries")
    if not legal or not x.get("vendor_registry_id") or _FOREIGN_FORM.search(legal) or re.search(r"extra-?provincial", x.get("vendor_legal_form") or "", re.I):
        return False
    if arm_of_a_group(x, label) or not (in_canada_text(ra) or _CA_PROV.search(ra)):
        return False
    return max(_name_fit(legal, label), _name_fit(re.sub(r"\s*\(canada\)\s*$", "", x.get("vendor") or "", flags=re.I), label)) >= 60
# A vendor whose own published terms say which customers its Canadian entity contracts with (tools/tech_relationships.py VENDORS, scope_countries:
# "Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada"): a customer story about a merchant that
# is not shown to be in those countries is a link, not a relationship with the Canada-located entity (53 shopify.com case studies: British,
# German, Australian, Singaporean merchants).
SCOPED = {registrable(host_of(_v["hq_url"])): _v for _v in _TR.VENDORS.values() if _v.get("scope_countries") and _v.get("hq_url")}
def buyer_country(x):
    a, h = x.get("buyer_address") or "", host_of(x.get("buyer_website") or "")
    if in_canada_text(a) or h.endswith(".ca"):
        return "CA"
    if _US_ZIP.search(a) or h.endswith((".us", ".gov", ".edu", ".mil")):
        return "US"
    j = (x.get("jurisdiction") or "").upper()[:2]
    return j if j in ("CA", "US") else ""
n_glob = collections.Counter()
for x in rows:
    if x.get("tier") not in ("D", "B", "L") or not (x.get("vendor_country_basis") or "").startswith("vendor located in Canada ("):
        continue
    _vh = host_of(x.get("contract_link") or "")
    if not _vh or _vh.endswith(".ca"):
        continue
    _dom = registrable(_vh)
    _label = re.sub(r"[^a-z0-9]", "", _dom.split(".")[0])
    _wd, _oc = SITE_OWNER.get(_dom) or {}, oc_of("https://" + _vh)
    _sc, _why = site_country(_oc), ""
    _sv = SCOPED.get(_dom)
    if _sv and buyer_country(x) not in _sv["scope_countries"]:
        _why = "%s's own terms: %s (%s); this buyer is not shown to be in %s" % (_sv.get("name") or _dom, _sv.get("scope") or "", _sv["hq_url"], " or ".join(_sv["scope_countries"]))
        n_glob["the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country"] += 1
    elif in_ca_section(x.get("contract_link") or ""):
        n_glob["kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)"] += 1  # kpmg.com/ca/en/…, ca.brinks.com: the Canadian arm's own pages
    elif _wd.get("verdict") == "abroad":
        _why = "the site that carries the listing, %s, is the site of %s — headquarters %s (%s; %s, read %s)" % (
            _dom, _wd.get("owner_label") or "another organisation", ", ".join(v for v in (_wd.get("owner_hq"), _wd.get("owner_hq_country")) if v) or "outside Canada",
            _wd.get("via") or "Wikidata", _wd.get("evidence_url") or "", _wd.get("retrieved_date") or "")
        n_glob["Wikidata: the site's organisation has its headquarters outside Canada"] += 1
    elif _wd.get("verdict") == "canada":
        n_glob["kept — Wikidata: the site's organisation has its headquarters in Canada"] += 1
        if _sc == "abroad":
            n_glob["kept although the site reader's address is abroad (Wikidata: headquarters in Canada)"] += 1
    elif _sc == "abroad":
        if formed_in_canada_under_the_sites_name(x, _label):
            n_glob["kept — address abroad on the site, but a corporation of the site's name is registered in Canada"] += 1
        else:
            _why = "the site that carries the listing gives its own address outside Canada: %s (%s)" % (flat_q(str(_oc.get("address")))[:90], _oc.get("address_url") or _vh)
            n_glob["the site's own address is outside Canada"] += 1
    elif _sc == "" and arm_of_a_group(x, _label):
        _why = "the listing is on %s; the vendor is named as the Canadian arm of a group (%s) and the site prints no address in Canada (not read, or no address)" % (_dom, (x.get("vendor") or "")[:60])
        n_glob["Canadian arm of a group, site not shown to be its own"] += 1
    else:
        n_glob["kept — the site prints an address in Canada" if _sc == "CA" else "kept — no evidence about whose site it is"] += 1
    if not _why:
        continue
    _g, _acc = int(x.get("grade") or 0), x.get("acc")
    n_glob["from tier " + x["tier"]] += 1
    x["tier"], x["rank_group"], x["completeness_score"] = "E", "E%d" % _g, TS["E"] * 10 + _g * 6 + (3 if _acc else 0)
    x["contract_status"] = "listed on a site that is not shown to be the Canada-located vendor's own — a link, not shown to be a relationship with the Canada-located entity (%s)" % _why
print("listings on a site that is not the Canada-located vendor's own (-> tier E):", dict(n_glob))
_free(globals(), "OX", "OC")
# the same vendor's BN9 / remit-to address read for one row applies to every row of that vendor (same legal entity); carried with its source
# 2026-11-10: the vendor's other identity facts travel with the BN, from the same row (26,082 registry rows carried CIRA's BN and no legal name, no
# registry id and no derived GST/HST number — "vendor GST/HST number" was the most-missing invoice element of the whole package)
CARRY_ID = ("vendor_legal_name", "vendor_registry_id", "vendor_registry_url", "vendor_registered_address", "vendor_legal_form", "vendor_registry_status",
            "vendor_registry_match_level", "vendor_incorporation_date", "vendor_trading_name", "vendor_neq", "vendor_qst_as_published", "vendor_phone", "vendor_emails", "vendor_logo_url")
_vbn, _vad, _vid = {}, {}, {}
for x in rows:
    _vn = norm(re.sub(r"^inferred:\s*", "", x.get("vendor") or ""))
    if not _vn:
        continue
    if re.match(r"^\d{9}", x.get("vendor_bn9") or "") and _vn not in _vbn:
        _vbn[_vn] = (x["vendor_bn9"], x.get("vendor_bn_source") or "", x.get("buyer") or "")
        _vid[_vn] = {c: x[c] for c in CARRY_ID if x.get(c) and x[c] != "not_published"}
        _vid[_vn]["vendor_gst_hst_derived"] = x.get("vendor_gst_hst_derived") or ""
    _ad = x.get("vendor_address") or x.get("vendor_registered_address") or ""
    if _ad and _ad not in ("not_published",) and _vn not in _vad:
        _vad[_vn] = (_ad, x.get("buyer") or "")
n_carry = collections.Counter()
for x in rows:
    _vn = norm(re.sub(r"^inferred:\s*", "", x.get("vendor") or ""))
    if not _vn:
        continue
    if not re.match(r"^\d{9}", x.get("vendor_bn9") or "") and _vn in _vbn:
        x["vendor_bn9"] = _vbn[_vn][0]; x["vendor_bn_source"] = (_vbn[_vn][1] or "see the same vendor's other rows") + " — carried from this vendor's row with %s" % _vbn[_vn][2][:60]; n_carry["bn9"] += 1
        _from = " (carried from this vendor's row with %s)" % _vbn[_vn][2][:60]
        for _c, _v in _vid.get(_vn, {}).items():
            if _c == "vendor_gst_hst_derived" or x.get(_c):
                continue
            x[_c] = _v if _c in ("vendor_phone", "vendor_emails", "vendor_logo_url", "vendor_registry_url", "vendor_incorporation_date", "vendor_registry_match_level") else _v + _from
            n_carry[_c[7:]] += 1
    if re.match(r"^\d{9}", x.get("vendor_bn9") or "") and not x.get("vendor_gst_hst_derived") and _vn in _vbn and x["vendor_bn9"][:9] == _vbn[_vn][0][:9]:
        x["vendor_gst_hst_derived"] = (_vid.get(_vn) or {}).get("vendor_gst_hst_derived") or (x["vendor_bn9"][:9] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)")
        n_carry["gst_hst_derived"] += 1
    if not (x.get("vendor_address") or x.get("vendor_registered_address")) and _vn in _vad:
        x["vendor_registered_address"] = _vad[_vn][0] + " (carried from this vendor's row with %s)" % _vad[_vn][1][:60]; n_carry["address"] += 1
print("same-vendor carry-over (BN9, identity facts and address from the vendor's other rows):", dict(n_carry))
_free(globals(), "_vbn", "_vad", "_vid")
_memstat("before the narrative columns", rows, globals())
# ---- downstream pack (owner 2026-11-06 22:00, the downstream agent's 150 questions: prompts/downstream_150_questions.md). Guarded: a failure here never stops the build.
# construction-work detector for the statutory prompt-payment default (contract text, NAICS 23, UNSPSC 72): conservative word list, contract fields only (never the vendor's name)
CONSTR_RX = re.compile(r"travaux de construction|\bconstruction\b(?! equipment| materials? supply)|general contractor|entrepreneur g[ée]n[ée]ral|\bpaving\b|\bpavage\b|\broofing\b|\btoiture\b|\bdemolition\b|\bexcavation\b|watermain|\bsewer\b|[ée]gout|aqueduc|\bHVAC\b|road (?:work|reconstruction|rehabilitation)|r[ée]fection|bridge (?:rehabilitation|replacement|repair)|building (?:renovation|retrofit|envelope|addition)|\brenovation\b|r[ée]novation|site (?:servicing|works)|civil works|mechanical and electrical|electrical (?:work|contractor|upgrade)|plumbing", re.I)
# statutes read 2026-11-08 (primary pages; quotes ≤ 300 chars); only Acts whose text was read are here — SK / MB / NS / NB / QC / BC prompt-payment rules were not verified today and are not applied
PROMPT_PAY = {
    "FED": "statutory default for construction work (buyer published no terms): the Crown must pay a proper invoice no later than the 28th day after receiving it — Federal Prompt Payment for Construction Work Act, S.C. 2019, c. 29, s. 387, s. 9(2), in force 2023-12-09 (https://laws-lois.justice.gc.ca/eng/acts/F-7.7/FullText.html, read 2026-11-08: \"no later than the 28th day after the day on which the proper invoice is received\"); applies only to construction work for a federal project under that Act",
    "ON": "statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: \"an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor\"); applies only if this contract is an improvement under the Act",
    "AB": "statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Prompt Payment and Construction Lien Act, R.S.A. 2000, c. P-26.4, s. 32.2(1) (current to 2025-04-01) (https://kings-printer.alberta.ca/documents/Acts/P26P4.pdf, read 2026-11-08: \"an owner who owes money under a proper invoice must pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice\"); s. 1.1(1.1): does not apply to Crown public works; applies only if this contract is an improvement under the Act",
}

# GST/HST status of public buyers, derived from CRA GST/HST Memorandum 18-2 "Provincial Governments" (canada.ca, read 2026-11-08 on the Mac engine; quotes ≤ 300 chars).
# Derived = a rule the buyer is subject to by type and province, never a value the buyer published; labelled, in its own column; the invoice card uses it only when nothing is published.
CRA_18_2 = "https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html"
TAX_PAY_REBATE = "pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (%s, read 2026-11-08: \"The governments of all the participating provinces, as well as Quebec, British Columbia and Nunavut, have agreed to use the pay and rebate model. Therefore, their government departments and all of their Crown agents will pay the GST/HST on their purchases\"); derived from buyer type and province, not published by the buyer" % CRA_18_2
TAX_POINT_RELIEF = "provincial government entity in %s: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (" + CRA_18_2 + ", read 2026-11-08: \"Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence\"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified"
TAX_MUNICIPAL = "municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, %s, read 2026-11-08: \"Note: A municipality is not a government for purposes of the GST/HST\"); charge GST/HST; derived from buyer type, not published by the buyer" % CRA_18_2
TAX_RATE = {"ON": "HST 13% (Ontario)", "NB": "HST 15% (New Brunswick)", "NL": "HST 15% (Newfoundland and Labrador)", "NS": "HST 15% (Nova Scotia)", "PE": "HST 15% (Prince Edward Island)"}
TAX_RATE_NOTE = " — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', %s, read 2026-11-08: \"The HST applies in the participating provinces at the following rates: 13%% in Ontario and 15%% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%%\"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here" % CRA_18_2

CITY_TO_PROV = {"toronto": "ON", "ottawa": "ON", "mississauga": "ON", "brampton": "ON", "hamilton": "ON", "london": "ON", "markham": "ON", "vaughan": "ON", "kitchener": "ON", "windsor": "ON", "richmond hill": "ON", "oakville": "ON", "burlington": "ON", "sudbury": "ON", "oshawa": "ON", "barrie": "ON", "st. catharines": "ON", "guelph": "ON", "cambridge": "ON", "whitby": "ON", "kingston": "ON", "thunder bay": "ON", "waterloo": "ON", "brantford": "ON", "pickering": "ON", "niagara falls": "ON", "peterborough": "ON", "sault ste. marie": "ON", "sarnia": "ON", "north bay": "ON", "belleville": "ON", "cornwall": "ON", "timmins": "ON", "orillia": "ON", "stratford": "ON", "owen sound": "ON",
                "montreal": "QC", "quebec": "QC", "laval": "QC", "gatineau": "QC", "longueuil": "QC", "sherbrooke": "QC", "levis": "QC", "saguenay": "QC", "trois-rivieres": "QC", "terrebonne": "QC", "saint-jean-sur-richelieu": "QC", "repentigny": "QC", "brossard": "QC", "drummondville": "QC", "saint-jerome": "QC", "granby": "QC", "blainville": "QC", "saint-hyacinthe": "QC", "shawinigan": "QC", "dollard-des-ormeaux": "QC", "rimouski": "QC", "victoriaville": "QC", "rouyn-noranda": "QC", "boucherville": "QC", "sept-iles": "QC", "val-d'or": "QC", "alma": "QC", "baie-comeau": "QC", "thetford mines": "QC", "joliette": "QC", "sorel-tracy": "QC", "magog": "QC",
                "vancouver": "BC", "surrey": "BC", "burnaby": "BC", "richmond": "BC", "abbotsford": "BC", "coquitlam": "BC", "kelowna": "BC", "langley": "BC", "saanich": "BC", "delta": "BC", "kamloops": "BC", "nanaimo": "BC", "victoria": "BC", "chilliwack": "BC", "prince george": "BC", "vernon": "BC", "courtenay": "BC", "campbell river": "BC", "penticton": "BC", "north vancouver": "BC", "new westminster": "BC", "port coquitlam": "BC", "maple ridge": "BC", "cranbrook": "BC", "fort st. john": "BC",
                "calgary": "AB", "edmonton": "AB", "red deer": "AB", "lethbridge": "AB", "st. albert": "AB", "medicine hat": "AB", "grande prairie": "AB", "airdrie": "AB", "spruce grove": "AB", "leduc": "AB", "fort mcmurray": "AB", "lloydminster": "AB", "okotoks": "AB", "cochrane": "AB", "camrose": "AB", "brooks": "AB",
                "winnipeg": "MB", "brandon": "MB", "steinbach": "MB", "thompson": "MB", "portage la prairie": "MB", "regina": "SK", "saskatoon": "SK", "prince albert": "SK", "moose jaw": "SK", "swift current": "SK", "yorkton": "SK", "north battleford": "SK",
                "halifax": "NS", "dartmouth": "NS", "sydney": "NS", "truro": "NS", "new glasgow": "NS", "kentville": "NS", "moncton": "NB", "saint john": "NB", "fredericton": "NB", "dieppe": "NB", "miramichi": "NB", "bathurst": "NB", "edmundston": "NB", "st. john's": "NL", "mount pearl": "NL", "corner brook": "NL", "gander": "NL", "grand falls-windsor": "NL", "charlottetown": "PE", "summerside": "PE", "whitehorse": "YT", "yellowknife": "NT", "iqaluit": "NU"}
CITY_PROV = re.compile(r"\b(" + "|".join(sorted((re.escape(c) for c in CITY_TO_PROV), key=len, reverse=True)) + r")\b")
PROV_NAMES = {"newfoundland": "NL", "labrador": "NL", "terre-neuve": "NL", "nova scotia": "NS", "nouvelle-ecosse": "NS", "new brunswick": "NB", "nouveau-brunswick": "NB", "prince edward island": "PE", "ile-du-prince-edouard": "PE",
              "quebec": "QC", "ontario": "ON", "manitoba": "MB", "saskatchewan": "SK", "alberta": "AB", "british columbia": "BC", "colombie-britannique": "BC", "yukon": "YT", "northwest territories": "NT", "territoires du nord-ouest": "NT", "nunavut": "NU"}
PROV_NAME = re.compile(r"\b(" + "|".join(sorted((re.escape(c) for c in PROV_NAMES), key=len, reverse=True)) + r")\b")
PACK_COLS = ["pay_on_sight", "pay_on_sight_missing", "channel_tier", "invoice_text", "invoice_card_json", "invoice_readiness", "invoice_missing", "ap_grade", "ap_score", "ap_grade_basis", "ap_gap_to_A", "ap_payability", "supplier_setup_url", "buyer_tax_status_derived", "tax_rate_indicative_derived", "invoice_currency_derived", "contract_term_as_published", "statutory_payees_inferred", "vendor_years_in_business", "mta_sts", "tls_rpt", "bimi", "buyer_payment_method_preference", "buyer_ap_cycle_published", "buyer_tax_exempt_status", "buyer_esignature_preference", "inference_confidence", "mailbox_confidence", "data_quality_score", "ship_ready", "invoice_portal_kind", "invoice_portal_note", "payment_terms_default_policy",
             "instrument_type_normalized", "buyer_bn_program", "vendor_registry_warning", "vendor_registry_note", "sensitivity_flag", "buyer_sector", "evidence_age_days", "reverify_due",
             "facts_provenance_json", "invoicing_requirements_structured", "ap_system_hint", "typical_contract_value_p50", "typical_contract_value_p75", "typical_cadence_days",
             "vendor_concentration_top_share", "all_canadian_vendors", "pair_prior_records", "pair_first_or_repeat", "pair_value_trend", "pair_dates_and_values"]
_PERSON_DESIG = re.compile(r"(?i)\b(?:(?:the )?(?:official )?web ?site of|site (?:web )?(?:officiel )?de|personal real estate corporation|prec\b\*?|realtor|real estate (?:agent|broker|professional)|"
                           r"courti[eè]re? immobili[eè]re?|sales representative|broker of record|cpa|cga|cma|m\.d\.|dds|dmd|ph\.?d\.?|dr\.|esq\.?|notaire|avocate?)(?![A-Za-zÀ-ÿ])|[®™*]")
EXTRA_SENS = [("law enforcement (incl. transit / parks)", re.compile(r"transit (?:police|enforcement|safety)|special constable|conservation officer|by-?law enforcement|peace officer", re.I)),
              ("financial regulator / oversight office", re.compile(r"\bOSFI\b|superintendent of financial institutions|\bFINTRAC\b|\bCANAFE\b|competition bureau|bureau de la concurrence|privacy commissioner|protection de la vie priv[ée]e|auditor general|v[ée]rificat(?:eur|rice) g[ée]n[ée]ral|ombuds|integrity commissioner|elections? (?:canada|ontario|bc|alberta|qu[ée]bec)|[ée]lections qu[ée]bec|securities commission|autorit[ée] des march[ée]s financiers|\bAMF\b", re.I)),
              ("justice / prosecution / law society", re.compile(r"public prosecution|poursuites p[ée]nales|courts administration|judicial council|attorney general|procureur g[ée]n[ée]ral|crown (?:attorney|counsel|prosecut)|law society|barreau du|directeur des poursuites|ministry of (?:the )?attorney|justice (?:canada|qu[ée]bec)|minist[èe]re de la justice|department of justice", re.I)),
              ("major bank", re.compile(r"\bTD\b|toronto-dominion|\bBMO\b|bank of montreal|banque de montr[ée]al|scotiabank|bank of nova scotia|banque scotia|\bRBC\b|royal bank|banque royale|\bCIBC\b|canadian imperial bank|national bank of canada|banque nationale|desjardins", re.I)),
              ("cybersecurity vendor", re.compile(r"crowdstrike|fortinet|palo alto|sentinelone|esentire|\bcisco\b|check ?point software|trend micro|mcafee|sophos|rapid7|tenable|\bokta\b|zscaler|proofpoint|mimecast|bell canada cyber|telus (?:security|cyber)", re.I)),
              ("political party", re.compile(r"conservative party|parti conservateur|liberal party|parti lib[ée]ral|new democratic party|\bNDP\b|\bNPD\b|bloc qu[ée]b[ée]cois|green party|parti vert|parti qu[ée]b[ée]cois|coalition avenir|qu[ée]bec solidaire|people's party|united conservative|saskatchewan party|\bPC party\b|"
                                             # 2026-11-11 (test set, a party shown under its domain name): the parties' own domains
                                             r"//(?:www\.)?(?:plq\.org|pq\.org|liberal\.ca|conservative\.ca|conservateur\.ca|ndp\.ca|npd\.ca|blocquebecois\.org|greenparty\.ca|partivert\.ca|coalitionavenirquebec\.org|"
                                             r"quebecsolidaire\.net|peoplespartyofcanada\.ca|unitedconservative\.ca|saskparty\.com|albertandp\.ca|ontariondp\.ca|ontarioliberal\.ca|ontariopc\.ca|bcndp\.ca)\b", re.I)),
              ("major media organisation", re.compile(r"\bCBC\b|radio-canada|\bCTV\b|global news|corus entertainment|postmedia|torstar|toronto star|globe and mail|qu[ée]becor|\bTVA\b|la presse\b|rogers (?:media|sports)|bell media|cogeco media|le devoir", re.I)),
              ("named exclusion (owner)", re.compile(r"university of toronto|universit[ée] de toronto|\bUofT\b|utoronto\.ca", re.I))]
# 2026-11-09 14:20Z: a portal counts as an INVOICE channel (pay-on-sight tier 1) only when it is an e-invoicing / supplier-invoice network; tender portals
# (SEAO, MERX, bids&tenders, Bonfire …) and generic "supplier portal" mentions never are — 466 "yes" rows had leaned on them (SEAO alone 190).
TENDER_PORTAL = re.compile(r"seao|merx|bids ?& ?tenders|bidsandtenders|bonfire|biddingo|bidnet|demandstar|publicpurchase|ungm|sam\.gov|bcbid|purchasingconnection|canadabuys|buyandsell|achatsetventes|ontariotenders|tenders?\b|appels? d'offres|e-?tender|find-tender|contractsfinder|ted\.europa|marches?-?publics|soumission", re.I)
EINVOICE_PORTAL = re.compile(r"ariba|coupa|jaggaer|sciquest|tungsten|kofax|basware|esker|taulia|tradeshift|transcepta|openinvoice|isupplier|oracle|workday|ghx|pagero|opentext|medius|yooz|zycus|ivalua|gep ?smart|paymentworks|tipalti|avidxchange|bill\.com|e-?invoic|einvoic|invoice|factur", re.I)
PORTAL_ACTIONABLE = re.compile(r"ariba|coupa|jaggaer|sciquest|tungsten|basware|sap business|esker|taulia|tradeshift|isupplier|oracle|workday|bonfire|bidsandtenders|bids ?& ?tenders|merx|seao|transcepta|openinvoice|paymentworks|zycus|ivalua|gep ?smart|medius|yooz|procurify|supplier|vendor|fourniss|portal|portail|invoice|factur", re.I)
AP_SYS = re.compile(r"\b(SAP Ariba|Ariba|Coupa|Jaggaer|Workday|Oracle (?:E-Business|ERP|Fusion|iSupplier)|Oracle|SAP S/4HANA|SAP|PeopleSoft|Esker|Kofax|Tipalti|Bill\.com|AvidXchange|Basware|Tungsten|Taulia|Tradeshift|Unit4|Dynamics 365|Sage Intacct|Sage 300|Munis|Tyler|Yardi|JD Edwards|Infor|Netsuite)\b", re.I)
INSTR = [("standing offer", r"standing offer|offre [àa] commandes|\bSO\b"), ("supply arrangement", r"supply arrangement|arrangement en mati[èe]re"), ("purchase order", r"purchase order|bon de commande|\bPO\b|delivery order|call-?up"),
         ("blanket order", r"blanket"), ("grant or contribution", r"\bgrant|contribution|subvention"), ("lease", r"\blease\b|\bbail\b"), ("amendment", r"amendment|modification|avenant"), ("contract", r"contract|contrat|agreement|entente|award|march[ée]")]
SECTOR = [("government: municipal", r"municipal"), ("government: provincial / federal", r"ministry|agency|government"), ("government: US", r"US government"), ("education: post-secondary", r"university|college"),
          ("education: K-12", r"school"), ("healthcare", r"hospital|health"), ("utility", r"utility"), ("transport / transit", r"transport|transit"), ("Indigenous government", r"First Nation|Indigenous"), ("non-profit", r"non-profit"), ("private sector", r"company")]
TYPE_RULES = [("university / college", r"universit|college|coll[èe]ge|c[ée]gep|polytechni|\.edu\b|\.ac\."), ("hospital / health authority", r"hospital|h[ôo]pital|health (?:authority|services|centre|network)|cisss|ciusss|\bchu\b|clinic|sant[ée]"),
              ("school board / school district", r"school (?:board|district|division)|centre de services scolaire|commission scolaire|\bcsd\b|\bk12\b"), ("municipality / local government", r"city of|town of|village of|township|county|municipalit|ville de|\bmrc\b|borough|district of|regional district|rural municipality"),
              ("government ministry / agency", r"ministry|minist[èe]re|department of|government of|gouvernement|agency|agence|commission|office of|secr[ée]tariat|\.gov\b|gc\.ca|gouv\.qc"), ("utility / public corporation", r"hydro|power|energy|utilit|water (?:district|authority)|\bgas\b"),
              ("transport / transit authority", r"transit|transport|airport|a[ée]roport|port authority|railway"), ("First Nation / Indigenous government", r"first nation|nation\b|band council|tribal|m[ée]tis|inuit|conseil des"), ("religious organisation", r"church|diocese|parish|paroisse|synagogue|mosque|temple|[ée]glise"),
              ("library", r"librar|biblioth"), ("non-profit / association / cultural body", r"foundation|fondation|society|soci[ée]t[ée]|association|club|centre|center|council|museum|mus[ée]e|theatre|festival|charity|coalition|institute|institut"),
              ("company (private sector)", r"\binc\b|\bltd|limited|corp|\bllc\b|lt[ée]e|\bco\b|group|groupe|holdings|enterprises|industries|technologies|services")]
# ---- owner's bar of 2026-11-11 (06:24 EST): "I want to know for a fact that there's a relationship to a point where they would be getting billed
# for something monthly … Or every 3 months, they get billed for something systematically by the vendor." A row says what is PUBLISHED about
# when the vendor bills (recurring_billing) and where that is published (recurring_billing_basis). Nothing is assumed:
#   1 monthly / 1 quarterly   the vendor's own terms say it bills by the month (every 30 days) or the quarter, and its service is seen in use by
#                             the buyer (its platform under the buyer's site, the buyer's DNS records, a "powered by / hosted by" line)
#   2 monthly or yearly       the vendor's own price list is by the month and it also sells a year paid in advance (or does not say which is
#                             billed): which period this buyer pays for is not published
#   3 yearly or longer        a fee for a year or more at a time (a .ca name: 1 to 10 years; a licence, a registration, a membership, an audit)
#   4 per transaction         a fee on each sale / booking / vehicle
#   5 not published           a contract record, a client listing, a design credit, a link, an inference: nothing published says when the vendor bills
BILL_WORDS = {"monthly": "1 monthly", "quarterly": "1 quarterly", "monthly_or_yearly": "2 monthly or yearly", "yearly": "3 yearly or longer", "per_transaction": "4 per transaction"}
_HOSTED_CREDIT = re.compile(r"host|h[ée]berg|maint|powered|propuls|g[ée]r[ée]|managed", re.I)
_REC_TEXT = [("1 monthly", re.compile(r"\b(?:monthly|per month|each month|mensuel(?:le)?s?|par mois|mensuellement)\b", re.I)),
             ("1 quarterly", re.compile(r"\b(?:quarterly|per quarter|trimestriel(?:le)?s?|par trimestre)\b", re.I)),
             ("4 per transaction", re.compile(r"\bper (?:vehicle|transaction|sale|unit)\b|\bpar (?:v[ée]hicule|transaction|vente)\b", re.I)),
             ("3 yearly or longer", re.compile(r"\b(?:annual(?:ly)?|yearly|per year|each year|annuel(?:le)?s?|par an(?:n[ée]e)?|chaque ann[ée]e)\b", re.I))]
_FEE_QUOTE = re.compile(r"“([^”]{10,320})”\s*\((https?://[^)\s]+)\)")
CIRA_TERM = ("CIRA's General Registration Rules, version 3.22 (https://stg.cira.ca/uploads/2023/05/general-registration-rules.pdf, read 2026-11-11), s. 2.4: “An Applicant may select a "
             "registration period of 1 to 10 years for the registration of the Domain Name” and s. 7.3: “upon the expiry of its Registration Period, each Domain Name Registration is automatically "
             "renewed by CIRA for one year”: the fee is paid for one to ten years at a time, through the registrar")
def _vendor_cycle(vd):
    """what tools/vendor_billing.py read on the vendor's own site: (class, quoted statement, longer periods it also sells, sentence when nothing was found)"""
    o = VBILL.get(vd) if vd else None
    if not o:
        return "", "", [], "the vendor's own site has not been read for its billing period yet"
    c, st_, more = _VB.cycle_of(o)
    if not c:
        return "", "", [], (("the vendor's own site (%s) was read on %s, %d pages: no price with its period and no billing statement on them" % (vd, o.get("date"), len(o.get("pages") or [])))
                            if o.get("status") == "ok" else "the vendor's own site (%s) could not be read on %s (%s)" % (vd, o.get("date"), o.get("status")))
    longer = [m for m in more if m in ("yearly", "quarterly")] if c in ("monthly", "monthly_price") else ["yearly"] if c == "quarterly" and "yearly" in more else []
    return c, "“%s” (%s, read %s)" % (st_["q"][:300], st_["u"], o.get("date")), longer, ""
_MEMBER_WORDS = re.compile(r"member|dues|cotis|adh[ée]s|licen[cs]|registr|permit|permis|droits|inscri", re.I)
_BILL_NOUN = r"(?:fees?|payments?|billing|invoic\w+|subscriptions?|rentals?|leases?|maintenance|licen[cs]es?|support|charges?|retainers?|abonnements?|frais|loyers?|location|entretien|versements?|redevances?)"
_REC_PERIOD = [("1 monthly", r"(?:monthly|per month|each month|mensuel(?:le)?s?|par mois|mensuellement)"), ("1 quarterly", r"(?:quarterly|per quarter|trimestriel(?:le)?s?|par trimestre)"),
               ("3 yearly or longer", r"(?:annual(?:ly)?|yearly|per year|annuel(?:le)?s?|par an(?:n[ée]e)?)")]
_REC_RX = [(lab, re.compile(r"\b" + per + r"\W+(?:\w+\W+){0,2}" + _BILL_NOUN + r"\b|\b" + _BILL_NOUN + r"\W+(?:\w+\W+){0,2}" + per + r"\b", re.I)) for lab, per in _REC_PERIOD]
# 2026-11-12 (owner, 09:00 EST: "those contract amounts, the billing cadence, you better have it set. Don't just put the value of the contract,
# but also the billing cadence. So let's say it's monthly. What would that be?"). A public record gives a contract's parties, subject, value and
# dates, not its schedule of payments. What the contract buys says how a contract of that kind is billed: works by progress invoice each month,
# a service over a term each month in arrears, goods at each delivery. The row says it is by the kind of the contract, and from what the kind
# was read (its commodity code, the record's own category, or the words of its title); the amount of one bill is calculated in
# tools/relationship_rows.py (the published value over the published term, or over the buyer's own average term — then an estimate).
_NAT_CONSTR = re.compile(r"\b(?:construction|constructing|reconstruct\w*|rehabilitat\w*|r[ée]habilitation|r[ée]fection|travaux|paving|pavage|resurfac\w*|asphalt(?:ing|age)|"
                         r"bridges?|ponts?|culverts?|ponceaux?|sewers?|[ée]gouts?|watermains?|aqueducs?|roofing|toitures?|renovat\w*|r[ée]novation|demolition|d[ée]molition|"
                         r"excavat\w*|terrassement|earthworks?|agrandissement|r[ée]am[ée]nagement|mise aux normes|road works|roadworks|works contract)\b", re.I)
_NAT_SERV = re.compile(r"\b(?:services?|entretien|d[ée]neigement|snow (?:removal|clearing|plowing|ploughing)|maintenance|collecte|collection|consult\w*|conseils?|"
                       r"ing[ée]nierie|engineering|design|conception|[ée]tudes?|study|studies|inspections?|nettoyage|cleaning|janitorial|conciergerie|gardiennage|"
                       r"security guards?|surveillance|support|audit|v[ée]rification|formation|training|location|rental|leasing|hauling|towing|remorquage|"
                       r"landscap\w*|paysag\w*|tonte|mowing|disposal|[ée]limination|gestion|management|hosting|h[ée]bergement|operation|exploitation)\b", re.I)
_NAT_GOODS = re.compile(r"\b(?:fournitures?|achats?|acquisitions?|purchases?|purchasing|supply(?:\s+and\s+deliver\w*)?|livraison|delivery of|camions?|trucks?|v[ée]hicules?|"
                        r"vehicles?|[ée]quipements?|equipment|mat[ée]riel|materials?|produits?|products?|pi[èe]ces|parts|chlorure|abrasifs?|salt|carburants?|fuel|propane|"
                        r"diesel|enrob[ée]s|uniforms?|v[êe]tements|ordinateurs?|computers?|laptops?|serveurs?|licen[cs]es?|mobilier|furniture|chemicals?|produit chimique)\b", re.I)
def contract_nature(x):
    """("works" | "services" | "goods" | "", from what it was read) for a contract row"""
    codes = " ".join(str(x.get(c_) or "") for c_ in ("commodity_codes", "commodity", "commodity_codes_from_pair"))
    for m in re.finditer(r"(UNSPSC|CPV|NAICS)?\s*(\d{6,8})\b(?:\s*\(?([^);|]{0,60}))?", codes):
        sch, code, label = (m.group(1) or ("UNSPSC" if len(m.group(2)) == 8 else "NAICS")), m.group(2), (m.group(3) or "").strip()
        why = "its commodity code %s %s%s" % (sch, code, (" (%s)" % label) if label else "")
        seg = code[:2]
        if sch == "UNSPSC" and len(code) == 8:
            if code[:4] in ("7211", "7212", "7213", "7214", "7215") or seg == "95":
                return "works", why
            if seg == "72":
                return ("works" if _NAT_CONSTR.search(label) else "services"), why
            if "70" <= seg <= "94":
                return "services", why
            if "10" <= seg <= "60":
                return "goods", why
        if sch == "CPV":
            if seg == "45":
                return "works", why
            if seg <= "44" or seg == "48":
                return "goods", why
            if seg >= "50":
                return "services", why
        if sch == "NAICS":
            if seg == "23":
                return "works", why
            if seg in ("31", "32", "33", "42", "44", "45"):
                return "goods", why
            return "services", why
    pm = (x.get("procurement_method") or x.get("procurement_method_from_pair") or "").strip()
    if re.fullmatch(r"(?i)construction|travaux(?: de construction)?|works", pm):
        return "works", "the record's own category: “%s”" % pm
    if re.fullmatch(r"(?i)services?|services professionnels|services de nature technique", pm):
        return "services", "the record's own category: “%s”" % pm
    if re.fullmatch(r"(?i)goods|biens|approvisionnement|supplies", pm):
        return "goods", "the record's own category: “%s”" % pm
    t = " ".join(str(x.get(c_) or "") for c_ in ("contract_title", "contract_description"))
    t = re.sub(r"\((?:the record's title|first sentence of the record's description)[^)]*\)", " ", t)[:400]
    why = "the words of its title: “%s”" % re.sub(r"\s+", " ", (x.get("contract_title") or x.get("contract_description") or "")[:120]).strip()
    if _NAT_CONSTR.search(t):
        return "works", why
    g, sv = _NAT_GOODS.search(t), _NAT_SERV.search(t)
    if sv:
        return "services", why
    if g:
        return "goods", why
    return "", ""
_ON_MONTHLY = ("in Ontario the Construction Act makes it the rule: “Unless the contract provides otherwise, a proper invoice must be given to the owner on a monthly "
               "basis” (s. 6.3(1), as Goodmans LLP sets it out, https://www.goodmans.ca/insights/article/Prompt_Payment_under_the_Construction_Act__The__Proper_Invoice__and_Strict_Payment_Deadlines, read 2026-11-12)")
def contract_term_days(x):
    try:
        d0 = datetime.date.fromisoformat(str(x.get("start_date") or x.get("award_date") or "")[:10])
        d1 = datetime.date.fromisoformat(str(x.get("end_date") or "")[:10])
        return (d1 - d0).days
    except ValueError:
        return None
def contract_cadence_by_kind(x):
    """(recurring_billing, basis) for a contract whose record says nothing of when the vendor bills: how a contract of its kind is billed, said to be"""
    nat, why = contract_nature(x)
    days = contract_term_days(x)
    tail = "; this contract's own schedule of payments is not published"
    if nat == "works":
        on = (x.get("jurisdiction") or "") == "CA" and re.search(r"\b(?:ON|Ontario)\b", (x.get("buyer_address") or "") + " " + (x.get("buyer_province") or ""))
        return "1 monthly", ("by the kind of relationship: works are billed by progress invoice, month by month as the work goes%s (what the contract buys: works, by %s)%s"
                             % (("; " + _ON_MONTHLY) if on else "", why, tail))
    if nat == "services":
        if days is not None and days < 45:
            return "4 per transaction", "by the kind of relationship: a service of a few weeks is invoiced when it is rendered (what the contract buys: a service, by %s)%s" % (why, tail)
        return "1 monthly", ("by the kind of relationship: a service that runs over a term is invoiced in arrears, for the work of each month (what the contract buys: a service, by %s)%s"
                             % (why, tail))
    if nat == "goods":
        return "4 per transaction", "by the kind of relationship: goods are invoiced at each delivery (what the contract buys: goods, by %s)%s" % (why, tail)
    if days is not None and days >= 60:
        return "1 monthly", ("by the kind of relationship: a contract that runs over a term (%d days) is invoiced as it goes, month by month being the usual period; what it buys "
                             "is not stated in a way read here%s" % (days, tail))
    return "4 per transaction", ("by the kind of relationship: a contract with no term published is invoiced at delivery or at each stage of the work; what it buys is not "
                                 "stated in a way read here%s" % tail)


def billing_of(x, ld):
    """(recurring_billing, recurring_billing_basis): what is published about when the vendor bills this buyer"""
    if ld.get("platform") == "f5500_plan":
        if ld.get("f55_insurer"):
            return "1 monthly", ("by the kind of relationship: a group insurance premium is billed each month for the policy year; the plan's policy %s runs to %s "
                                 "(Form 5500 Schedule A, plan year %s)" % (ld.get("f55_policy_numbers") or "?", ld.get("f55_policy_to") or "?", ld.get("f55_plan_year") or "?"))
        return "5 not published", "the plan's Schedule C records what the provider was paid in the plan year (%s), not how often it bills" % (ld.get("f55_plan_year") or "?")
    if ld.get("platform") == "dian_import":
        return "4 per transaction", ("for each shipment, the exporter's commercial invoice: the import declarations on file cite %s invoice%s of exporters in Canada "
                                     "from %s to %s, the newest %s of %s (Colombia's customs, DIAN)" % (ld.get("dian_invoices") or "1", "" if str(ld.get("dian_invoices")) == "1" else "s",
                                                                                                        ld.get("dian_first") or "?", ld.get("dian_last") or "?", ld.get("dian_invoice") or "?", ld.get("dian_invoice_date") or "?"))
    t = x.get("tier") or "N"
    cfv, cs = x.get("vendor_country_basis") or "", x.get("contract_status") or ""
    vd = registrable(host_of(ld.get("vendor_site") or x.get("vendor_website") or "") or "")
    vname = x.get("vendor") or "the vendor"
    if t == "T":
        credit, dns = "credited on the buyer's own site" in cfv, "seen in the buyer's public DNS" in cfv
        hosted = credit and (ld.get("credit_class") == "P" or bool(_HOSTED_CREDIT.search(ld.get("credit_phrase") or "")))
        seen = ("the service answers in the buyer's own DNS records" if dns else
                ("the buyer's own site says “%s” this vendor" % re.sub(r"\s+", " ", ld.get("credit_phrase") or "powered by").strip()) if credit else
                "the vendor's platform runs under the buyer's own site")
        cur = _BILL_CUR.get(norm(x.get("vendor") or "")) or _BILL_CUR_DOM.get(vd)
        if credit and not hosted and not cur:
            c, q, longer, why = _vendor_cycle(vd)
            return "5 not published", ("a credit line says who made the site (“%s”): whether the vendor still bills the organisation, and how often, is not published%s"
                                       % (re.sub(r"\s+", " ", ld.get("credit_phrase") or "").strip() or "credit", ("; for reference, the vendor's own price list: " + q) if q else ""))
        if cur:
            return BILL_WORDS[cur["cls"]], "%s's own terms: “%s” (%s, read %s)%s; %s" % (vname, cur["quote"], cur["url"], cur["read"], ("; " + cur["more"]) if cur.get("more") else "", seen)
        c, q, longer, why = _vendor_cycle(vd)
        if c == "monthly" and not longer:
            return "1 monthly", "the vendor's own statement: %s; %s" % (q, seen)
        if c == "quarterly" and not longer:
            return "1 quarterly", "the vendor's own statement: %s; %s" % (q, seen)
        if c in ("monthly", "monthly_price", "quarterly"):
            return "2 monthly or yearly", ("the vendor's own price list is by the %s%s: %s; %s; which period this buyer pays for is not published"
                                           % ("quarter" if c == "quarterly" else "month", (" and it also sells by the " + " and the ".join("year" if m == "yearly" else "quarter" for m in longer)) if longer else "", q, seen))
        if c == "yearly":
            return "3 yearly or longer", "the vendor's own price list is by the year: %s; %s" % (q, seen)
        if c == "per_transaction":
            return "4 per transaction", "the vendor's own price list is per transaction: %s; %s" % (q, seen)
        for lab, rx in _REC_RX:  # the row's own subject names the period of what is paid ("annual sustaining listing fee")
            m = rx.search(x.get("contract_title") or "")
            if m:
                return lab, "the subject of the relationship names its period: “%s”; %s" % ((x.get("contract_title") or "")[:200], seen)
        return "5 not published", "%s; %s" % (seen, why)
    if t == "R":
        return "3 yearly or longer", CIRA_TERM
    if t == "M":
        if cs.startswith("listed issuer on a Canadian stock exchange"):
            if ld.get("xc_exchange") == "CSE":  # the Canadian Securities Exchange: a monthly maintenance fee
                return "1 monthly", "the exchange's own fee page: %s" % (ld.get("bill_delivery") or "a monthly maintenance fee")[:420]
            return "3 yearly or longer", "the exchange's own fee schedule: %s" % (ld.get("bill_delivery") or "an annual sustaining fee for each calendar year")[:420]
        if cs.startswith(("client of a Canadian trademark agent of record", "client of a Canadian patent agent of record")):
            return "4 per transaction", ("by the kind of relationship: an agent of record bills its professional fees for each filing, step, renewal or maintenance fee it handles "
                                         "for the owner; no schedule of bills is published")
        m = _FEE_QUOTE.search(cfv) or _FEE_QUOTE.search(cs)
        if m:
            for lab, rx in _REC_TEXT:
                if rx.search(m.group(1)):
                    return lab, "the body's own statement of its fee: “%s” (%s)" % (m.group(1)[:300], m.group(2))
        if x.get("end_date") and (x.get("start_date") or x.get("award_date")):
            return "3 yearly or longer", ("a fee for each licence / registration period: in force since %s, paid up to %s as the public register gives it; not a monthly bill"
                                          % (x.get("start_date") or x.get("award_date"), x["end_date"]))
        c, q, longer, why = _vendor_cycle(vd)
        if c and _MEMBER_WORDS.search(q):  # a statement about the body's own dues or fees, not about a benefit plan it sells
            return ({"monthly": "1 monthly" if not longer else "2 monthly or yearly", "monthly_price": "2 monthly or yearly", "quarterly": "1 quarterly" if not longer else "2 monthly or yearly",
                     "yearly": "3 yearly or longer", "per_transaction": "4 per transaction"}[c],
                    "the body's own site on its fees: %s; the organisation is on the body's current list" % q)
        # rule 13 (2026-11-11 21:30Z) and the owner at 20:14 EST ("populate as much as possible per relationship"): when the body's own sentence is not
        # found, the row says how a bill of that kind comes — by the kind of relationship, and says so
        if re.search(r"system operator|\b(?:IESO|AESO)\b|op[ée]rateur ind[ée]pendant", vname, re.I):
            return "1 monthly", ("by the kind of relationship: an electricity market operator settles its participants' charges every month and sends each its "
                                 "statement; the operator's own sentence was not found (%s)" % why)
        return "3 yearly or longer", ("by the kind of relationship: a body bills its membership dues, and the fee of a licence or registration, for each year or each "
                                      "period of the licence; the body's own sentence on its fee and period was not found (%s)" % why)
    if t == "I":
        return "5 not published", "no record of this relationship: the vendor is inferred from the organisation's type and province"
    if "member named in the member directory" in cs:
        c, q, longer, why = _vendor_cycle(vd)
        if c and _MEMBER_WORDS.search(q):
            return ({"monthly": "1 monthly" if not longer else "2 monthly or yearly", "monthly_price": "2 monthly or yearly", "quarterly": "1 quarterly" if not longer else "2 monthly or yearly",
                     "yearly": "3 yearly or longer", "per_transaction": "4 per transaction"}[c], "the body's own site on its dues: %s; the organisation is in the body's member directory" % q)
        return "3 yearly or longer", ("by the kind of relationship: membership dues are billed by the year; the body's own pages do not give the fee and its period (%s)" % why)
    if "tenant / merchant named by" in cs:
        return "1 monthly", "by the kind of relationship: rent and the charges of a lease are billed by the month; the landlord's own sentence on its bills is not read"
    if "sponsor / exhibitor named by" in cs:
        return "3 yearly or longer", ("by the kind of relationship: a sponsorship or an exhibitor's fee is billed for the event or the season, once a year or less often; "
                                      "the body's own sentence on its bills is not read")
    if "dealer / retailer named by" in cs:
        return "4 per transaction", "by the kind of relationship: a dealer is invoiced for each order of goods it buys for resale; the supplier's own sentence on its bills is not read"
    if "vendor located in Canada" in cfv or t in ("D", "E") or (t == "C" and not x.get("records_in_contract_dataset")):
        c, q, longer, why = _vendor_cycle(vd)
        return "5 not published", ("the vendor names the organisation %s: what it bills, and how often, is not published%s"
                                   % ("as a client" if t != "E" else "on its site (a link, not shown to be a client)", ("; for reference, the vendor's own price list: " + q) if q else ""))
    if (x.get("source") or "").startswith("auditor of record"):
        return "3 yearly or longer", "the audit of each fiscal year: the organisation's own audited financial statements name the auditor (one engagement a year)"
    txt = " ".join(x.get(c_) or "" for c_ in ("contract_title", "contract_description", "contract_term_as_published", "commodity"))
    txt = re.sub(r"\((?:the record's title|first sentence of the record's description)[^)]*\)", " ", txt)
    for lab, rx in _REC_RX:  # the period next to what is paid ("annual maintenance", "monthly rental", "abonnement annuel"), never a schedule of visits or a yearly output
        m = rx.search(txt)
        if m:
            return lab, "the public record's own text: “%s”" % re.sub(r"\s+", " ", txt[max(0, m.start() - 120):m.end() + 120]).strip()
    if x.get("contract_value") or x.get("contract_title") or x.get("contract_description") or x.get("award_date"):
        return contract_cadence_by_kind(x)
    return "5 not published", "the public record gives the parties, the subject, the value and the dates of the contract, not when the vendor bills"
# ---- owner 2026-11-11 07:15 EST: "the data that would go within the invoice … billing cadence, other things like that around that billing and
# invoicing nature of the relationship … know the fields that the Shopify invoice would have … How much does it cost?" and "when do we know for a
# fact? When … something being where it is means that there's a relationship". Each cell quotes the vendor's (or the body's) own page; a cell
# with no published source stays empty.
BILL_COLS = ["bill_amount_indicative", "bill_amount_basis", "bill_items_as_published", "bill_currency_as_published", "bill_delivery_as_published", "bill_payment_method_as_published",
             "bill_tax_rule_as_published", "bill_identifier_format", "service_stops_if_unpaid", "bill_due_terms_as_published", "bill_remit_to_as_published", "relationship_fact_basis",
             "billing_period_calculated", "bill_amount_calculated"]
# owner 2026-11-11 07:15 EST: "inference of inference … becomes a calculated guess … if there's so many inferences pointing to one thing". A billing
# period that is NOT published for this relationship but follows from two published things goes in its own column, always opening with the word
# "calculated", never into recurring_billing: (1) a client the vendor names + the vendor's own price list by the month; (2) construction work for
# an Ontario owner + the Construction Act's default of monthly proper invoices (statute read 2026-11-11).
ON_MONTHLY = ("calculated — monthly: construction work for an owner in Ontario, and the Construction Act, R.S.O. 1990, c. C.30, s. 6.3(1): “Proper invoices shall be given to an owner on a "
              "monthly basis, unless the contract provides otherwise.” (https://www.ontario.ca/laws/statute/90c30, read 2026-11-11); this contract's own terms are not published")
CIRA_LEGAL = "Canadian Internet Registration Authority (as it names itself in its Registrant Agreement, version 2.2: “the Canadian Internet Registration Authority (\"CIRA\")”)"
_DOMAIN_NAME = re.compile(r"(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}")
_LEGAL_NOTE = re.compile(r"\s+\((?:stated on|as printed|printed with|schema\.org|the vendor's name|the name on|carried from|as registered|as it names|official name|as the |its words|the copyright)")
# 2026-11-11, second reading of test rows (a draft of 100 drawn from the whole table): 14 rows had a defect in a name, an address or an amount.
#   a vendor named by its page title ("Buy Domains & Email At Hover.com", "Dedicated Server Web Hosting PCI Compliant Canada » Zenutech");
#   a buyer named by a title with bars ("YYC Detail | Car Auto Detailing | Paint Protection | Ceramic") or by its address with a slash ("cwmc.ca/");
#   an address that begins with the page's words ("today. Call us Message us Contact Info Cameron, MO 64429-2112"), a charity number, a written "\n";
#   a subject that is the word "null".
_ADDR_MARK = re.compile(r"(?:contact\s+info(?:rmation)?|call\s+us(?:\s+now)?|message\s+us|learn\s+more|read\s+more|get\s+directions|(?:mailing\s+|office\s+|our\s+|physical\s+|postal\s+|civic\s+)?add?ress(?:e)?|adresse(?:\s+postale)?|"
                        r"head\s+office|corporate\s+office|main\s+office|headquarters|si[èe]ge\s+social|visit\s+us|find\s+us(?:\s+here)?|our\s+(?:office|location)s?|locations?|coordonn[ée]es|(?:pour\s+)?nous\s+joindre|"
                        r"contact(?:ez)?[- ](?:us|nous)|get\s+in\s+touch|talk\s+to\s+us|reach\s+us|come\s+visit(?:\s+us)?|where\s+to\s+find\s+us|o[ùu]\s+nous\s+trouver)(?:\s+(?:is|est))?\s*:?\s+", re.I)
_ADDR_NOTE = re.compile(r"\s\((?:as printed|CRA |city, province|the |read |per |from |headquarters|official|registered|its |label|schema|stated|printed|provincial|recipient|carried|archive)")
_CIVIC = re.compile(r"(?<![\w#-])(?:\d{1,6}[A-Za-z]?(?:\s?[-–]\s?\d{1,6})?\s*,?\s+(?:[A-Za-zÀ-ÿ0-9'’.-]+\s+){0,4}?(?:rue|street|st\.?|avenue|ave?\.?|road|rd\.?|boul\S*|blvd\.?|drive|dr\.?|chemin|ch\.|route|rang|way|lane|"
                    r"ln\.?|court|ct\.?|crescent|cres\.?|place|pl\.?|highway|hwy\.?|parkway|pkwy\.?|trail|terrace|square|circle|line|sideroad|concession|mont[ée]e|c[ôo]te|all[ée]e|impasse|croissant|promenade|quai)(?![A-Za-zÀ-ÿ])"
                    r"|(?:P\.?\s?O\.?\s?Box|C\.\s?P\.|Case\s+postale|Bo[iî]te\s+postale)\s?\d)", re.I)
def addr_clean(a):
    """the printed address without the page's words in front of it; the note in brackets that follows it stays"""
    a = a or ""
    m = _ADDR_NOTE.search(a)
    body, note = (a[:m.start()], a[m.start():]) if m else (a, "")
    b = re.sub(r"\s*\\[nrt]\s*", " ", body)  # a line break written out as two characters
    b = re.sub(r";\s*vendor_address_missing:\s*(?:False|True)\s*$", "", b)  # a field name of the source left in the cell
    b = re.sub(r"^FIRM_ADDRESS:\s*(?:null\b)?\s*", "", b)
    b = re.split(r"\s*(?:-->|<!--)\s*", b)[-1]  # the end of a comment in the page's markup
    b = re.sub(r"^\d{5}\s?\d{4}\s?RR\s?\d{4}\s+", "", b)  # a charity registration number printed before the address
    last = None
    for mk in _ADDR_MARK.finditer(b):
        if mk.end() < len(b) - 8:
            last = mk
    if last and re.search(r"\d", b[last.end():]):
        head = b[:last.start()]
        if not re.search(r"\d{2,}", head) or re.search(r"[.!?]\s", head):  # what stands before the mark is prose, not the first line of the address
            b = b[last.end():]
    b = re.sub(r"^[a-zà-ÿ][^.!?]{0,60}[.!?]\s+(?=[A-Z0-9])", "", b)  # "today. 123 Main St": the end of a sentence
    cv = _CIVIC.search(b)
    if cv and cv.start() > 0:
        head = b[:cv.start()]
        if len(head.split()) >= 3 and not head.rstrip().endswith(",") and not re.search(r"\d{3,}", head) and not re.search(r"\b(?:suite|unit|bureau|floor|[ée]tage|local|app?t?\.?|c/o|a/s)\b", head, re.I):
            b = b[cv.start():]  # three words or more run into the civic number, none of them a unit or a floor: the page's words or a name; a first line that ends
                                # with a comma ("Licence and Permit Issuing Office, 850 Coxwell Avenue", "Commerce Court North, 25 King Street West") is part of the address
    b = re.sub(r"\s{2,}", " ", b).strip(" ,;:-•·")
    if body.lstrip().startswith("“") and b.endswith("”") and not b.startswith("“"):
        b = "“… " + b  # a quoted line of the page: the cut is shown
    return (b + note) if len(b) >= 6 else (a if not body.startswith("FIRM_ADDRESS") else "")
def name_from_title(name, website):
    """the organisation's name inside a page title used as its name: the part that fits its own address, or the address's own word"""
    lab = re.sub(r"[^a-z0-9]", "", (registrable(host_of(website or "") or "") or "").split(".")[0].lower())
    if len(lab) < 3:
        return ""
    segs = [q.strip(" -–—|:·•»>") for q in re.split(r"\s+[|–—:·•»>]\s+|\s+-\s+|\s*[|»]\s*|(?<=\w):\s+", name) if q.strip(" -–—|:·•»>")]
    if len(segs) > 1:
        fit = sorted(((_LCF.name_fit(q, lab), -i, q) for i, q in enumerate(segs)), reverse=True)
        # the first part of a title when it fits the address at all; a later part only when it nearly spells the address ("… » Zenutech" on zenutech.com, not
        # "Calgary" on calgarybusinesscoach.ca after "Rodina Ventures", nor "Traffic Tickets" after "Criminal Lawyer Toronto")
        if fit[0][0] >= (20 if fit[0][1] == 0 else 75) and 2 <= len(fit[0][2]) <= 60:
            return fit[0][2]
    m = re.search(r"(?<![A-Za-z0-9])(%s)\.[a-z]{2,6}(?![A-Za-z0-9])" % re.escape(lab), name, re.I)
    if m and len(name.split()) >= 3:
        return m.group(1)  # the title carries the site's own address ("Buy Domains & Email At Hover.com"): the word in front of the dot
    return ""
_JUNK_NAME = re.compile(r"^(?:about(?: us)?|home|contact(?: us)?|welcome|accueil|services?|index|untitled|page d'accueil|homepage|menu|blog|shop|store|news|introduction|[àa] propos)$", re.I)
_TITLE_PREFIX = re.compile(r"^(?:welcome to|bienvenue (?:chez|à|au|aux|sur le site d[eu])|introduction)\s+(?:the\s+)?", re.I)
# 2026-11-13 (21Z, owner 13:23 EST "everything accurate no errors"): names that are not names, read on the table of 20:32Z — an image's file name as a
# sponsor's name ("Edmonton Global_web.jpg", "nnsl.png"), the page-title word "Home" beside the name ("Pelagica Books Home", "Viking Self Storage: Home",
# "Home / Constructions DV"), the word "Logo" ("MCAP Logo"), and a town's bare name taken from a business's own site ("Toronto" on merlottoronto.com,
# "Kingston" on bridges-kingston.com): Statistics Canada's census subdivisions (2021 Census, table 98-10-0002-01) give the names of places
_IMG_NAME = re.compile(r"\.(?:jpe?g|png|gif|svg|webp|bmp|tiff?|avif)$|_web\b|[-_]\d{2,4}x\d{2,4}\b|^(?:img|dsc|image|logo)[-_ ]?\d+", re.I)
_HOME_WORD = re.compile(r"^(?:home|accueil)\s*[/|:–—«»·•-]+\s*(?=\S)|\s*(?:[/|:–—«»·•-]+\s*|\.)(?:home|accueil)$|\s(?:home|accueil)$", re.I)  # a leading "Home" only before a separator ("Home Office" is a name)
_HOME_NAME_WORD = set("""funeral nursing care retirement group mobile children childrens smart model show open foster rest senior seniors memorial sweet almost entire
nickel locum your my our the at away dream custom new family forever happy healthy green modular tiny manufactured log timber luxury perfect ideal cozy safe first
comfort mission youth boarding guest lodge heritage maison""".split())  # a trailing "Home" after one of these makes a name with it ("Funeral Home")
def strip_home_word(name):
    m = re.search(r"(\S+)\s(?:home|accueil)$", name, re.I)
    if m and not re.search(r"[/|:–—.-]$", m.group(1)) and re.sub(r"[^a-z]", "", m.group(1).lower()) in _HOME_NAME_WORD:
        return name
    t = _HOME_WORD.sub("", name)
    return t.strip(" -–—|:/.") if t != name else name
_LOGO_WORD = re.compile(r"^(?:le )?logo (?:of (?:our client )?(?:the )?|for (?:the )?|de la |du |des |de l['’]|d['’]|de )|\s*[-–|:]?\s*\blogos?$|^logos?\b\s*[-–|:]?\s*", re.I)
_PLACES = set()
try:
    for _r in csv.DictReader(gzip.open(ROOT + "/tools/data/ca_csd_population.csv.gz", "rt", encoding="utf-8")):
        _PLACES.add(re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", _r["name"]).encode("ascii", "ignore").decode().lower()))
except OSError:
    pass
_PLACES.discard("")
_PLACE_TYPE = {"county", "municipality", "municipalite", "municipal", "district", "township", "city", "town", "village", "ville", "canton", "cantons", "unis", "paroisse",
               "rural", "rm", "regional", "region", "of", "de", "du", "des", "la", "le", "les", "the", "corporation", "summer", "resort", "united", "townships"}
_PLACE_AFFIX = sorted("""cityof townof villageof townshipof municipalityof municipalitede municipalite villede ville rmof rm countyof county cantonde canton paroissede
paroisse summervillageof sv districtof district regionof regionde region mrc mun city town township village municipality twp ca qc on ab bc mb sk ns nb nl pe nt nu yt
online official info gov web site net area alberta quebec ontario manitoba saskatchewan britishcolumbia novascotia newbrunswick newfoundland labrador pei yukon nunavut
canada usa us""".split(), key=len, reverse=True)
def _strip_affixes(t):
    changed = True
    while t and changed:
        changed = False
        for a in _PLACE_AFFIX:
            if t.startswith(a) and len(t) > len(a) - 1:
                t, changed = t[len(a):], True
                break
            if t.endswith(a):
                t, changed = t[:-len(a)], True
                break
    return t
_fold_nos = lambda t: re.sub(r"\bsainte\b", "ste", re.sub(r"\bsaint\b", "st", re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()))).strip()
_PLACE_CORES = {"".join(w for w in _fold_nos(n).split() if w not in _PLACE_TYPE) for n in _PLACES} if _PLACES else set()
def place_name_not_this_org(name, website):
    """a buyer named by a place's bare name (no word of a municipality in it), on a site whose own domain spells that place and something more than a
    municipality's, a province's or a web address's words: a business of the town (merlottoronto.com, bridges-kingston.com, madebykawarthalakes.ca),
    not the town (hiltontownship.ca, villageofempress.com, crossfieldalberta.com); a domain that does not spell the place whole (rdcounty.ca) is left"""
    toks = _fold_nos(name).split()
    if not toks or any(w in _PLACE_TYPE for w in toks):
        return False  # "City of Austin", "Municipalité de Maria", "The Argyle": named with a word of its kind, not by the place alone
    core = "".join(toks)
    f = re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower())
    if len(core) < 3 or not website or not (f in _PLACES or core in _PLACE_CORES):
        return False
    host = (host_of(website) or "").lower()
    reg = registrable(host) or host
    if SHARED_GOV.match(reg):
        return False  # a government-wide site (gov.bc.ca): its domain says nothing of the body
    lab = re.sub(r"[^a-z0-9]", "", _fold_nos(reg.split(".")[0]).replace(" ", ""))
    if core not in lab:
        return False
    a, b = lab.split(core, 1)
    return len(_strip_affixes(a)) + len(_strip_affixes(b)) >= 3
def _premises(a):
    """(civic number, first word of the street) and postal code of a printed address"""
    m = re.search(r"(?<![\w#-])(\d{2,6})[ ,]+(?:(?:rue|boul\S*|av\S*|ch\S*|route|rang)\s+)?([A-Za-zÀ-ÿ'\-]{4,})", a or "", re.I)
    pc = re.search(r"\b([ABCEGHJ-NPRSTVXY]\d[A-Z]) ?(\d[A-Z]\d)\b", (a or "").upper())
    return ((m.group(1), norm(m.group(2))) if m else None), ((pc.group(1) + pc.group(2)) if pc else None)
CIRA_KEEP = ("CIRA's General Registration Rules, version 3.22, s. 7.1: “In order to maintain a Domain Name Registration, the Registration Period must be renewed prior to its expiry.” "
             "(https://stg.cira.ca/uploads/2023/05/general-registration-rules.pdf, read 2026-11-11)")
CIRA_PAY = ("through the registrar of record — CIRA's General Registration Rules, s. 7.2: “To renew the Registration Period of a Registration prior to its expiry, a Registrant must request its "
            "Registrar of Record to submit a renewal request to CIRA.”")
# CIRA's Registrar Agreement, version 1.15 (July 7, 2016), Article 7, opened with the project's reader on 2026-11-11: who CIRA charges for a .ca name, when, and
# that the amounts are on its website (cira.ca answers 403 to the reader, so the amount stays unread; stg.cira.ca serves the agreement itself)
CIRA_REG = "CIRA's Registrar Agreement, version 1.15 (https://stg.cira.ca/uploads/2023/05/registrar-agreement.pdf, read 2026-11-11)"
CIRA_BILL = ("CIRA charges the registrar of record, and the registrar bills the registrant under its own terms — %s, s. 7.1(f): “a fee for each registration of a Domain Name and a fee for the renewal of "
             "a Domain Name Registration”; s. 7.2(b): “Fees arising from Transaction Requests will be charged and are payable at the time the Transaction Request is made.”" % CIRA_REG)
CIRA_TAX = "%s, s. 7.1: “The amount of such fees (collectively the “Fees”) are set forth at CIRA’s website and do not include any applicable taxes.”" % CIRA_REG
CIRA_AMOUNT = ("not read: CIRA's fee for a year of registration is “set forth at CIRA’s website” (%s, s. 7.1), and that website refuses this project's reader (403 on 2026-11-11); "
               "the registrar's own price to the registrant depends on the registrar, which is not looked up (no bulk WHOIS query)" % CIRA_REG)
# A .ca row's amount (owner 2026-11-11: "the amount that would be billed within that billing cadence"; "a calculated value only when several signals
# agree, and labelled as calculated"): what the registrant pays its registrar is not published for any one name. What Canada-located vendors print
# for a .ca name by the year is (tools/vendor_billing.py reads their price pages every day): with five such prices and more, the row carries
# their range in its own column, opening with the word "calculated" — never in bill_amount_indicative.
_CA_PRICES = _VB.ca_name_prices(VBILL)
def _ca_amount_calculated():
    if len(_CA_PRICES) < 5:
        return ""
    _f = lambda v: ("%.2f" % v).rstrip("0").rstrip(".")
    _mid = _CA_PRICES[len(_CA_PRICES) // 2] if len(_CA_PRICES) % 2 else None
    _midv = _mid[0] if _mid else (_CA_PRICES[len(_CA_PRICES) // 2 - 1][0] + _CA_PRICES[len(_CA_PRICES) // 2][0]) / 2
    _ex = "; ".join("“%s” (%s, read %s)" % (re.sub(r"\s+", " ", q).strip()[:150], u, d) for v, dom, q, u, d in (_CA_PRICES[0], _CA_PRICES[len(_CA_PRICES) // 2], _CA_PRICES[-1]))
    return ("calculated — $%s to $%s a year, middle value $%s: the prices that %d Canada-located vendors print for a .ca name by the year (lowest, middle, highest: %s). "
            "The organisation's own registrar and the price it pays are not published" % (_f(_CA_PRICES[0][0]), _f(_CA_PRICES[-1][0]), _f(_midv), len(_CA_PRICES), _ex))
CA_AMOUNT_CALC = _ca_amount_calculated()
print("a .ca name by the year, as printed by the vendors on file: %d prices%s" % (len(_CA_PRICES), (" — " + CA_AMOUNT_CALC[:140]) if CA_AMOUNT_CALC else " (fewer than five: no calculated amount)"))
# 2026-11-12: a member body's dues, as its own membership pages print them. The reader keeps price statements ("$299 per Year") and plan
# statements ("annual memberships starting at $219 for the year"); a member row took only a price statement whose own words said "member" —
# so Vernon's "$299 per Year" on /membership/membership-levels/ and Langley's "$219 for the year" were not taken (204 member rows of 12,435
# carried an amount in the table of 00:14Z). A statement counts when its page is a membership page (by its address) or its words say
# member / dues; a page of advertising, sponsorship, events or news never; the lowest such amount is the floor of a member's dues.
_DUES_PATH = re.compile(r"member|membre|adh[ée]|join|dues|cotis|rates?-|tarif|levels|options|benefits|avantages|investment|investissement", re.I)
_NOT_DUES_PATH = re.compile(r"advertis|publicit|sponsor|commandit|banner|event|[ée]v[ée]nement|ticket|billet|news|nouvelles|blog|article|tariff-business|award|gala|golf", re.I)
# what is not the dues of an organisation: a discount or a rebate, a fee of a person (individual, student, retired …), a fee by head
_NOT_DUES = re.compile(r"non-?members?|non-?membres?|r[ée]duction|discount|rabais|remise|\d\s?%|\bsave\b|[ée]conomi|per\s+capita|par\s+(?:capita|habitant|personne)|individu|student|[ée]tudiant|personal\s+member|youth|jeunes|"
                       r"junior|retir|retrait[ée]|famil|household|lifetime|[àa]\s+vie\b|per\s+(?:person|head)|par\s+t[êe]te|"
                       # 2026-11-13 (21Z, the table of 20:32Z): the price or the value of a member benefit is not the dues — "Members can post up to 5 free job postings
                       # annually ($1050 value)" (Bio Alberta), "Minimum purchase of $1500.00 or 3000 litres per year" (a fuel program, South Shuswap), "Avantage membre :
                       # 108 $/mois au lieu de 120 $/mois" (a partner's service, CCI de la MRC)
                       r"\bvalue\b|valeur|au\s+lieu\s+de|instead\s+of|avantages?\s+membres?|member\s+(?:benefit|perk|price|rate|discount)|minimum\s+purchase|achat\s+minimum|litres?\b|"
                       r"job\s+postings?|free\s+(?:job|listing|ad)|regular(?:ly)?\s+\$|prix\s+r[ée]gulier", re.I)
_AMT_Q = re.compile(r"(?:C|CA|US)?\$\s?(\d+(?:[ ,\u00a0]\d{3})*(?:\.\d{1,2})?)(?!\d)|(?<![\d.,])(\d+(?:[ \u00a0]\d{3})*(?:,\d{1,2})?)\s?\$")
def member_dues(rec, vd=""):
    """(value, currency, 'year' | 'month', statement) — the lowest dues a member body's own membership pages print, or None. The amount is read
    again from the statement's words: the reader's money pattern cut a number of four digits written without a separator ("$1195.00" was 119)."""
    best = None
    for st_ in (rec or {}).get("stmts") or []:
        per = {"price_year": "year", "plan_year": "year", "price_month": "month", "plan_month": "month"}.get(st_.get("c"))
        if not per:
            continue
        q, u = st_.get("q") or "", st_.get("u") or ""
        h_ = (urllib.parse.urlparse(u).hostname or "").lower()
        if vd and registrable(h_[4:] if h_.startswith("www.") else h_) != vd:
            continue  # a page of another site
        path = urllib.parse.urlparse(u).path or ""
        if _NOT_DUES_PATH.search(path) or not (_DUES_PATH.search(path) or _MEMBER_WORDS.search(q)):
            continue
        if len(q.split()) > 16 and not _MEMBER_WORDS.search(q):
            continue  # a long sentence on a membership page that does not speak of membership
        if _NOT_DUES.search(q) or _VB._PROMO.search(q) or _VB._NOT_A_PRICE.search(q) or _VB._ADDON.search(q):
            continue
        v0, cur = _VB.parse_money(st_.get("m") or q)
        if v0 is None:
            v0, cur = _VB.parse_money(q)  # a plan statement's match is its words ("annual memberships"): the amount is in its sentence
        if v0 is None:
            continue
        d0 = ("%.2f" % v0).rstrip("0").rstrip(".").split(".")[0]
        v = None
        for m_ in _AMT_Q.finditer(q):  # the amount of the statement, whole
            t_ = (m_.group(1) or m_.group(2) or "").replace("\u00a0", " ")
            dig = re.sub(r"[ ,]", "", t_.split(".")[0]) if m_.group(1) else re.sub(r"[ ]", "", t_.split(",")[0])
            if dig.startswith(d0):
                try:
                    v = float(re.sub(r"[ ,]", "", t_)) if m_.group(1) else float(re.sub(r" ", "", t_).replace(",", "."))
                except ValueError:
                    v = None
                break
        if v is None or v < 20 or v > 25000:
            continue  # a "$0" plan, a "$1" offer; a figure of an article
        y = v * 12 if per == "month" else v
        if best is None or y < best[0]:
            best = (y, v, cur, per, st_)
    return best[1:] if best else None
def _money_words(v, cur, per):
    return "from %s%s a %s" % ({"CAD": "C$", "USD": "US$"}.get(cur, "$"), ("%.2f" % v).rstrip("0").rstrip("."), per)
def bill_profile(x, ld, cls):
    """the other fields of the vendor's bill and the reason the relationship is a fact, each from a published page"""
    if ld.get("platform") == "f5500_plan":
        _ins, _py = ld.get("f55_insurer") or "", ld.get("f55_plan_year") or "?"
        if _ins:
            _pr, _cm = float(ld.get("f55_premiums") or 0), float(ld.get("f55_commissions") or 0)
            _calc = (("calculated — about US$%s a month: the premiums the insurer received in plan year %s, US$%s (Form 5500 Schedule A, WLFR_PREMIUM_RCVD_AMT), "
                      "spread over 12 monthly bills" % (format(_pr / 12, ",.0f"), _py, format(_pr, ",.0f"))) if _pr > 0 else
                     ("calculated — more than US$%s a month (more than US$%s a year): the insurer paid US$%s in commissions on these contracts in plan year %s "
                      "(Form 5500 Schedule A, INS_BROKER_COMM_TOT_AMT); commissions are paid out of the premium, so the premium is more" % (
                          format(_cm / 12, ",.0f"), format(_cm, ",.0f"), format(_cm, ",.0f"), _py)) if _cm > 0 else "")
            return {"bill_amount_calculated": _calc,
                    "bill_items_as_published": "group %s insurance for %s persons covered, policy %s (Form 5500 Schedule A)" % (ld.get("f55_benefits") or "", ld.get("f55_persons") or "?", ld.get("f55_policy_numbers") or "?"),
                    "bill_currency_as_published": "USD (the plan's Form 5500)",
                    "bill_delivery_as_published": "by the kind of relationship: a premium statement each month for the policy year, the policy running to %s" % (ld.get("f55_policy_to") or "?"),
                    "bill_identifier_format": "the policy (contract) number, as the plan's Schedule A gives it (%s)" % (ld.get("f55_policy_numbers") or "?"),
                    "relationship_fact_basis": ("fact, public record: the plan's Form 5500 Schedule A (US Department of Labor, plan year %s) names %s as the insurer of its contract %s, "
                                                "policy period to %s, %s persons covered (%s; %s)" % (_py, _ins, ld.get("f55_policy_numbers") or "?", ld.get("f55_policy_to") or "?",
                                                                                                    ld.get("f55_persons") or "?", ld.get("record_url") or "", ld.get("dataset_page") or ""))}
        _pc = float(ld.get("f55_provider_comp") or 0)
        return {"bill_amount_indicative": "US$%s paid in plan year %s" % (format(_pc, ",.0f"), _py) if _pc > 0 else "",
                "bill_amount_basis": "the plan's Form 5500 Schedule C, item 2 (direct and indirect compensation of the provider), plan year %s (%s)" % (_py, ld.get("record_url") or ""),
                "bill_items_as_published": "services to the organisation's benefit plan (Form 5500 Schedule C)",
                "bill_currency_as_published": "USD (the plan's Form 5500)",
                "relationship_fact_basis": ("fact, public record: the plan's Form 5500 Schedule C (US Department of Labor, plan year %s) names %s, at %s, as paid US$%s by the plan (%s)"
                                            % (_py, ld.get("f55_providers") or ld.get("vendor") or "?", (ld.get("vendor_address") or "?").split(" (")[0], format(_pc, ",.0f"), ld.get("record_url") or ""))}
    if ld.get("platform") == "dian_import":
        _fob = float(ld.get("dian_fob") or 0)
        return {"bill_amount_indicative": "US$%s FOB for the newest invoice (%s of %s)" % (format(_fob, ",.2f"), ld.get("dian_invoice") or "?", ld.get("dian_invoice_date") or "?"),
                "bill_amount_basis": ("VALOR_FOB_USD of import declaration %s (Colombia's customs, DIAN: %s); with freight US$%s and insurance US$%s the customs value is US$%s CIF; "
                                      "US$%s FOB with this exporter and US$%s with every exporter in Canada on file (%s)" % (
                                          ld.get("dian_declaration") or "?", ld.get("record_url") or "", ld.get("dian_freight") or "0", ld.get("dian_insurance") or "0",
                                          ld.get("dian_cif") or "?", format(float(ld.get("dian_fob_total_pair") or 0), ",.2f"), format(float(ld.get("dian_fob_total_buyer") or 0), ",.2f"),
                                          (ld.get("dian_months") or "").replace(";", ", "))),
                "bill_items_as_published": "%s (tariff heading %s)" % ((ld.get("title") or "")[:260], ld.get("dian_hs") or "?"),
                "bill_currency_as_published": "USD (VALOR_FOB_USD of the declaration)",
                "bill_delivery_as_published": ("the exporter's commercial invoice %s of %s, cited in import declaration %s (NUMERO_FACTURA, FECHA_FACTURA); shipped by %s, cleared at %s"
                                               % (ld.get("dian_invoice") or "?", ld.get("dian_invoice_date") or "?", ld.get("dian_declaration") or "?",
                                                  (ld.get("dian_transport") or "?").lower(), ld.get("dian_customs_office") or "?")),
                "bill_payment_method_as_published": "“%s” (FORMA_PAGO of the import declaration; TIPO_IMPORTACION “%s”)" % (ld.get("dian_payment_form") or "?", ld.get("dian_import_type") or "?"),
                "bill_identifier_format": "the exporter's invoice number, as the declaration cites it (%s)" % (ld.get("dian_invoice") or "?"),
                "relationship_fact_basis": ("fact, public record: Colombia's customs (DIAN) publishes import declaration %s of %s, which names the organisation as the importer "
                                            "(NIT %s) and %s as the exporter, at %s, with the exporter's invoice %s of %s (%s)" % (
                                                ld.get("dian_declaration") or "?", ld.get("dian_declaration_date") or "?", ld.get("dian_nit") or "?", ld.get("vendor") or "?",
                                                (ld.get("vendor_address") or "?").split(" (")[0], ld.get("dian_invoice") or "?", ld.get("dian_invoice_date") or "?", ld.get("record_url") or ""))}
    t = x.get("tier") or "N"
    cfv, cs = x.get("vendor_country_basis") or "", x.get("contract_status") or ""
    vd = registrable(host_of(ld.get("vendor_site") or x.get("vendor_website") or "") or "")
    o, out = {}, {}
    day = (x.get("award_date") or "")[:10] or "the day it was read"
    if t == "T":
        credit, dns = "credited on the buyer's own site" in cfv, "seen in the buyer's public DNS" in cfv
        hosted = credit and (ld.get("credit_class") == "P" or bool(_HOSTED_CREDIT.search(ld.get("credit_phrase") or "")))
        cur = _BILL_CUR.get(norm(x.get("vendor") or "")) or _BILL_CUR_DOM.get(vd)
        rec = VBILL.get(vd) if vd else None
        if cur:
            out["bill_amount_indicative"], out["bill_amount_basis"] = cur.get("amount") or "", cur.get("amount_basis") or ""
            b = cur.get("bill") or {}
            for col, k in (("bill_items_as_published", "items"), ("bill_currency_as_published", "currency"), ("bill_delivery_as_published", "delivery"),
                           ("bill_payment_method_as_published", "payment"), ("bill_tax_rule_as_published", "tax"), ("bill_identifier_format", "identifier"), ("service_stops_if_unpaid", "unpaid"),
                           ("bill_due_terms_as_published", "terms")):  # 2026-11-13: "terms" — the hand-read bills of Vianet and Hosted in Canada carried it, no row took it
                out[col] = b.get(k) or ""
        if not out.get("bill_due_terms_as_published") and vd in getattr(_TR, "DUE_TERMS_BY_DOMAIN", {}):
            out["bill_due_terms_as_published"] = _TR.DUE_TERMS_BY_DOMAIN[vd]  # when the bill is due, in the host's own terms (tools/tech_relationships.py)
        if rec and not (credit and not hosted and not cur):
            _svc = ("mail" if re.search(r"\b(?:MX|SPF|spf1|DKIM|DMARC)\b|v=spf1|authorises|send its mail|mail is handled", (ld.get("dns_record") or "") + " " + cs, re.I) else "dns") if dns else ""
            low = _VB.lowest(rec, _svc)
            if cls.startswith("3"):
                low.pop("month", None)  # a vendor that bills by the year: its yearly price, never a monthly figure it only shows for comparison (Hover)
            if not out.get("bill_amount_indicative") and (low.get("month") or low.get("year")):
                per = "month" if low.get("month") else "year"
                v, c_, st_ = low[per]
                out["bill_amount_indicative"] = _money_words(v, c_, per)
                out["bill_amount_basis"] = ("the vendor's lowest published price by the %s: “%s” (%s, read %s); the buyer's own plan and amount are not published"
                                            % (per, st_["q"][:260], st_["u"], rec.get("date")))
                if c_ and not out.get("bill_currency_as_published"):
                    out["bill_currency_as_published"] = "%s: the vendor's prices are quoted in %s (“%s”, %s)" % (c_, {"CAD": "Canadian dollars", "USD": "U.S. dollars"}[c_], st_["m"].strip()[:60], st_["u"])
            elif not out.get("bill_amount_indicative") and dns and _VB.lowest(rec):
                out["bill_amount_basis"] = ("not taken: the prices read on the vendor's site (%s) are for another of its products than the one seen in the organisation's DNS records "
                                            "(a mailbox price for a zone on its name servers, or a telephone, television or Internet-access price)" % vd)
            for col, k in (("bill_currency_as_published", "currency"), ("bill_payment_method_as_published", "paymethod"), ("service_stops_if_unpaid", "unpaid"),
                           ("bill_delivery_as_published", "delivery"), ("bill_tax_rule_as_published", "tax"),  # the last two: reader version 4 (2026-11-11)
                           ("bill_due_terms_as_published", "terms")):  # reader version 7 (2026-11-13): when the bill is due
                st_ = _VB.extra_of(rec, k)
                if st_ and not out.get(col):
                    out[col] = "“%s” (%s, read %s)" % (st_["q"][:280], st_["u"], rec.get("date"))
        if cur and not out.get("bill_items_as_published"):
            out["bill_items_as_published"] = "the subscription to the vendor's service, in the words of its own terms: “%s” (%s)" % (cur["quote"][:240], cur["url"])
        if re.search(r"/password/?$", x.get("contract_link") or "") and (x.get("vendor") or "").startswith("Shopify"):
            out["bill_amount_basis"] = ((out.get("bill_amount_basis") or "") + "; this store shows its password page (%s): it is on the platform, and it may be closed for a time or not yet open, "
                                        "in which case its fee can differ from an open store's" % x["contract_link"]).lstrip("; ")
            n_billcol["Shopify store behind its password page (noted beside the amount)"] += 1
        unpaid = (" The vendor cuts an unpaid service off: %s" % out["service_stops_if_unpaid"][:240]) if out.get("service_stops_if_unpaid") else ""
        if credit and not hosted and not cur:
            out["relationship_fact_basis"] = "stated by the buyer: its own site names the vendor as the maker of the site (“%s”): work done and paid for at least once; nothing published shows a bill today" % re.sub(r"\s+", " ", ld.get("credit_phrase") or "credit").strip()
        elif dns:
            out["relationship_fact_basis"] = ("fact, seen on the buyer's side: the buyer's own DNS %s (%s, read %s): the service is running.%s "
                                              "The account at the provider is normally the organisation's own; sometimes its web agency holds it and is the one billed."
                                              % ("carries the vendor's account-verification record" if ld.get("dns_record_kind") == "txt" else "records name the vendor's servers",
                                                 (ld.get("dns_record") or "")[:120], day, unpaid))
        elif credit:
            out["relationship_fact_basis"] = "fact, seen on the buyer's side: the buyer's own site says “%s” the vendor (read %s): the site runs on the vendor's service.%s" % (re.sub(r"\s+", " ", ld.get("credit_phrase") or "powered by").strip(), day, unpaid)
        else:
            out["relationship_fact_basis"] = "fact, seen on the buyer's side: the vendor's platform answers under the buyer's own site (%s, read %s): the service is running.%s" % ((x.get("contract_link") or "")[:120], day, unpaid)
    elif t == "R":
        out["bill_items_as_published"] = ".ca domain name registration and its renewals, 1 to 10 years at a time (CIRA's General Registration Rules, s. 2.4 and 7.1)"
        out["bill_payment_method_as_published"] = CIRA_PAY
        out["service_stops_if_unpaid"] = CIRA_KEEP
        out["bill_delivery_as_published"], out["bill_tax_rule_as_published"], out["bill_amount_basis"] = CIRA_BILL, CIRA_TAX, CIRA_AMOUNT
        out["bill_amount_calculated"] = CA_AMOUNT_CALC
        out["relationship_fact_basis"] = "fact, seen on the buyer's side: the organisation's own .ca name answers (read %s), and a .ca name that is not renewed lapses: %s" % (day, CIRA_KEEP)
    elif t == "M":
        m = _FEE_QUOTE.search(cfv) or _FEE_QUOTE.search(cs)
        if m and re.search(r"\$\s?\d|\d\s?\$", m.group(1)):
            v, c_ = _VB.parse_money(m.group(1))
            if v:
                out["bill_amount_indicative"] = "%s%s%s" % ({"CAD": "C$", "USD": "US$"}.get(c_, "$"), ("%.2f" % v).rstrip("0").rstrip("."),
                                                             " per vehicle" if re.search(r"per vehicle", m.group(1), re.I) else " a year" if re.search(r"annual|year|ann[ée]e", m.group(1), re.I) else "")
                out["bill_amount_basis"] = "the body's own statement of its fee: “%s” (%s)" % (m.group(1)[:280], m.group(2))
        if ld.get("platform") in ("hc_register", "radio_register", "exchange_register", "bc_water", "bc_stumpage", "ab_aer", "hc_pmra", "cnsc_licence", "cer_levy"):
            # tools/hc_registers.py / tools/radio_licences.py: the published fee of one product (a drug, a device licence, a radio station) and the year's bill
            # calculated from what the register lists for the organisation today (a radio licensee's: at least, from the lowest fee of each station)
            # lists for the company today; how the invoice comes and when it is due, in Health Canada's own guidance
            for _c, _k in (("bill_amount_indicative", "fee_unit"), ("bill_amount_basis", "fee_unit_basis"), ("bill_amount_calculated", "fee_calculated"),
                           ("bill_delivery_as_published", "bill_delivery"), ("bill_due_terms_as_published", "bill_terms"), ("bill_items_as_published", "bill_items")):
                if ld.get(_k):
                    out[_c] = ld[_k]
        if ld.get("platform") == "rbq_licence" and not out.get("bill_amount_indicative") and not re.search(r"constructeur-propri", (ld.get("title") or "") + " " + (x.get("contract_title") or ""), re.I):
            # (an owner-builder's licence — "constructeur-propriétaire" — has its own fee table, not read yet: no amount is written for it)
            # the Régie's own fee table, read 2026-11-11: what a licence costs to keep for a year, by type of licence (the row's licence names its categories)
            _gen = bool(re.search(r"g[ée]n[ée]ral", (ld.get("title") or "") + " " + (x.get("contract_title") or ""), re.I))
            out["bill_amount_indicative"] = "%s $ a year" % ("989.81" if _gen else "547.53")
            out["bill_amount_basis"] = ("the Régie du bâtiment du Québec's fee table “Maintien d’une licence – 2026” (droits + frais = total): “Général (annexe I) 884,54 $ 105,27 $ 989,81 $”, "
                                        "“Général et spécialisé (annexes I, II et III) 884,54 $ 105,27 $ 989,81 $”, “Spécialisé (annexes II et III) 442,26 $ 105,27 $ 547,53 $” "
                                        "(https://www.rbq.gouv.qc.ca/licence/tarification-et-amendes/tarification-pour-lentrepreneur-de-construction/, read 2026-11-11); this licence is %s"
                                        % ("general or general and specialised" if _gen else "specialised only, as far as its categories on the register say"))
            out["bill_items_as_published"] = "the yearly fee to keep a construction contractor's licence (“Maintien d’une licence”): droits + frais"
        rec = VBILL.get(vd) if vd else None
        if rec and not out.get("bill_amount_indicative"):
            low = _VB.lowest(rec)
            st_ = (low.get("year") or low.get("month") or (None, None, None))[2]
            if st_ and _MEMBER_WORDS.search(st_["q"]):
                per = "year" if low.get("year") else "month"
                out["bill_amount_indicative"] = _money_words(low[per][0], low[per][1], per)
                out["bill_amount_basis"] = "the body's lowest published fee by the %s: “%s” (%s, read %s); the organisation's own fee is not published" % (per, st_["q"][:260], st_["u"], rec.get("date"))
        if cs.startswith("client of a Canadian trademark agent of record"):
            out["relationship_fact_basis"] = ("fact, public record: the Canadian Intellectual Property Office's trademarks register names this firm as the agent of record for the organisation's "
                                              "trademarks (%s)" % (x.get("contract_link") or x.get("source") or "")[:160])
        elif cs.startswith("client of a Canadian patent agent of record"):
            out["relationship_fact_basis"] = ("fact, public record: the Canadian Intellectual Property Office's patent register (CSV extract of 2024-05-22) names this firm as the agent of record "
                                              "for the organisation's patents and applications (%s)" % (x.get("contract_link") or x.get("source") or "")[:160])
        elif cs.startswith("producer represented in Québec by its promotional agent"):
            out["relationship_fact_basis"] = ("fact, public record: the Société des alcools du Québec's own product page names the organisation as the producer and the firm as its "
                                              "agent promotionnel in Québec (%s)" % (x.get("contract_link") or x.get("source") or "")[:160])
        elif cs.startswith("listed issuer on a Canadian stock exchange"):
            out["relationship_fact_basis"] = ("fact, public record: the exchange's own list of listed companies names the organisation as a listed issuer, with its symbol (%s)"
                                              % (x.get("contract_link") or x.get("source") or "")[:160])
        elif cs.startswith("holds the right to sell"):
            # tools/hc_registers.py and the PMRA lane of tools/bc_crown.py: Health Canada's own public registers
            out["relationship_fact_basis"] = ("fact, public record: Health Canada's own public register lists the organisation as holding the right to sell the products "
                                              "it invoices yearly (%s)" % (x.get("contract_link") or x.get("source") or "")[:160])
        elif cs.startswith("billed stumpage by a Canadian public body"):
            out["relationship_fact_basis"] = ("fact, public record: the Province of British Columbia's Harvest Billing System lists the invoices it billed to this client, "
                                              "each with its number, timber mark and value (%s)" % (x.get("contract_link") or x.get("source") or "")[:160])
        elif cs.startswith(("holder of licence", "registered with a Canadian regulatory authority", "owner of ", "accredited business")):
            out["relationship_fact_basis"] = "fact, public record: the body's own public register lists the organisation as licensed / registered / accredited today (%s)" % (x.get("contract_link") or x.get("source") or "")[:160]
        elif cs.startswith("member of a Canadian body (stated on the buyer's own site"):
            out["relationship_fact_basis"] = "stated by the buyer: its own site states its membership of the body and links to it"
        else:
            out["relationship_fact_basis"] = "fact, the biller's own roster: the body's current member list names the organisation (%s)" % (x.get("contract_link") or "")[:160]
    elif t == "I":
        out["relationship_fact_basis"] = "inferred, not a fact: no record of this relationship; the vendor is the one organisations of this type and province normally pay"
    elif "vendor located in Canada" in cfv or t in ("D", "E") or (t == "C" and not x.get("records_in_contract_dataset")):
        what = ("as a member in its member directory" if "member named in the member directory" in cs else "as its tenant or merchant" if "tenant / merchant named by" in cs else
                "as a dealer of its products" if "dealer / retailer named by" in cs else "as a sponsor or exhibitor" if "sponsor / exhibitor named by" in cs else "as a client")
        # 2026-11-11, the owner chose the lanes "members of Canadian chambers and associations" and "dealers, franchisees and commercial tenants of
        # Canadian companies". A member directory, a dealer list, a tenant directory or a sponsor / exhibitor list is the list of who pays, kept
        # and published by the body that is paid, and current by construction (a lapsed member leaves the directory, a closed dealer the
        # locator): the biller's own roster. A client list, a logo wall or a case study is what a vendor says about itself — his rule of
        # 07:15 EST the same day: "a vendor's client list is the vendor's statement" — and stays that.
        _roster = what != "as a client" and t != "E"
        out["relationship_fact_basis"] = ("link only: the organisation is linked from the vendor's site, not shown to be a client" if t == "E" else
                                          "fact, the biller's own roster: the Canadian body's own page names the organisation %s (%s)" % (what, (x.get("contract_link") or "")[:160]) if _roster else
                                          "stated by the vendor: its own page names the organisation %s (%s); not seen from the buyer's side" % (what, (x.get("contract_link") or "")[:160]))
        if what == "as a member in its member directory" and not out.get("bill_amount_indicative"):
            # a member named in the body's own directory pays its dues: the amount is the body's lowest published membership fee, said to be the
            # lowest (a member's own dues are never published; they are that or more) — the same reading as for a register's fee (tier M above)
            rec = VBILL.get(vd) if vd else None
            md_ = member_dues(rec, vd) if rec else None
            if md_:
                v_, cur_, per, st_ = md_
                out["bill_amount_indicative"] = _money_words(v_, cur_, per)
                out["bill_amount_basis"] = "the body's lowest published membership fee by the %s: “%s” (%s, read %s); the member's own dues are not published (they are that or more)" % (per, st_["q"][:260], st_["u"], rec.get("date"))
                n_billcol["member rows that carry the body's lowest published dues"] += 1
        if ld.get("platform") == "roster_file" and ld.get("fee_calculated") and not str(x.get("bill_amount_calculated") or "").strip():
            # 2026-11-13: a roster whose body publishes what all its listed parties pay together and how many they are (OCS Wholesale: its wholesale
            # revenue and its number of Authorized Cannabis Stores): the average bill, labelled as an estimate and saying from what (rule 16)
            out["bill_amount_calculated"] = ld["fee_calculated"]
            n_billcol["roster rows with an estimate calculated from the body's own published figures"] += 1
        if ld.get("platform") == "roster_file" and ld.get("bill_items") and not out.get("bill_items_as_published"):
            out["bill_items_as_published"] = ld["bill_items"]
    else:
        out["relationship_fact_basis"] = _RR.record_basis(x)  # a press release says it is the vendor's own announcement (tools/relationship_rows.py)
    if cls.startswith("5") and t in ("C", "D") and "vendor located in Canada" in cfv and "member named in the member directory" not in cs:
        c_, q_, longer_, why_ = _vendor_cycle(vd)
        if c_ in ("monthly", "monthly_price", "quarterly"):
            out["billing_period_calculated"] = ("calculated — by the %s%s: the vendor names the organisation as a client, and the vendor's own price list is by the %s: %s; "
                                               "what this client buys and how it is billed are not published"
                                               % ("quarter" if c_ == "quarterly" else "month", " or the year" if longer_ else "", "quarter" if c_ == "quarterly" else "month", q_))
    if t in ("T", "C", "D", "E", "M") and not out.get("bill_items_as_published") and not (x.get("contract_title") or "").strip():
        rec = VBILL.get(vd) if vd else None
        if rec and (rec.get("desc") or rec.get("title")):
            # the relationship names no subject (a client listing, a link, a membership): what the vendor says it sells, in its own words
            out["bill_items_as_published"] = "what the vendor says it sells, on its own home page: “%s” (%s, read %s); what it sells to this organisation is not published" % (
                (rec.get("desc") or rec.get("title"))[:260], rec.get("final") or "https://%s/" % vd, rec.get("date"))
    if t != "T":
        # owner 2026-11-11 ("on invoice, by bank transfer … don't forget all invoice details … tailor to each"): how the body behind a licence, a
        # registration, a membership, a dealership or a contract sends its bill and takes the money. First the bodies read by hand
        # (tools/payee_billing.py: a few regulators and cities carry thousands of rows each), then what the vendor reader found on the body's own
        # site (reader version 4: payment methods, how the invoice arrives, what happens when it is not paid).
        if _PAYEE.fill(out, x, x.get("vendor") or "", ld.get("vendor_site") or x.get("vendor_website") or ""):
            n_billcol["bill details from the body's own payment page, read by hand (tools/payee_billing.py)"] += 1
        _rec9 = VBILL.get(vd) if vd else None
        if _rec9:
            for col, k in (("bill_payment_method_as_published", "paymethod"), ("bill_delivery_as_published", "delivery"), ("service_stops_if_unpaid", "unpaid"),
                           ("bill_currency_as_published", "currency"), ("bill_tax_rule_as_published", "tax"), ("bill_due_terms_as_published", "terms")):
                st_ = _VB.extra_of(_rec9, k)
                if st_ and not out.get(col) and not str(x.get(col) or "").strip():
                    out[col] = "“%s” (%s, read %s)" % (st_["q"][:280], st_["u"], _rec9.get("date"))
    if t not in ("R", "I"):
        (sa, pa), (sv, pv) = _premises(x.get("buyer_address")), _premises(x.get("vendor_address"))
        if sa and sa == sv and (pa == pv or not pa or not pv):
            out["relationship_fact_basis"] += " Caution: the buyer and the vendor print the same street address: they may be one organisation, or one may be housed by the other."
            n_billcol["same street address on both sides (caution written)"] += 1
    return out
n_bill, n_bill_shop, n_billcol, n_inv, n_inv_t = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
n_ship, n_ship_miss, n_ship_one, n_ship_level = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
n_mark, n_fill = collections.Counter(), collections.Counter()  # owner 2026-11-11 20:36 EST: every row marked by its amount; 20:04 EST: how full the invoice is
KEY_FIELDS = ["buyer_website", "buyer_address", "buyer_phone", "buyer_legal_name_as_published", "email_evidence_url", "ap_phone", "invoice_mailing_address", "invoicing_requirements", "payment_terms_as_published",
              "po_required_as_published", "contract_title", "contract_value", "award_date", "contract_link", "vendor_address", "vendor_bn9", "vendor_website", "vendor_emails", "vendor_phone", "vendor_legal_name", "invoice_reference_hint", "commodity_codes"]
_today = datetime.date.today()
for after, new in (("buyer_address", ["buyer_phone", "buyer_contact_evidence_url"]), ("vendor_emails", ["vendor_phone", "vendor_contact_evidence_url"]),
                   ("email_evidence_quote", ["mailbox_provenance", "email_deliverability", "email_security_posture", "dmarc_policy", "dmarc_record", "dmarc_record_domain", "spf_policy", "spf_record", "mail_provider", "dns_checked_date",
                                             "ap_contact_name_as_published", "ap_phone", "invoice_mailing_address", "invoicing_requirements", "invoice_portal_url", "language_hint"]),
                   ("contract_status", ["relationship_kind", "relationship_detail", "how_relationship_was_found", "relationship_fact_basis", "recurring_billing", "recurring_billing_basis",
                                       "bill_amount_indicative", "bill_amount_basis", "bill_items_as_published", "bill_currency_as_published", "bill_delivery_as_published",
                                       "bill_payment_method_as_published", "bill_tax_rule_as_published", "bill_identifier_format", "service_stops_if_unpaid", "bill_due_terms_as_published",
                                       "bill_remit_to_as_published", "billing_period_calculated", "bill_amount_calculated", "invoice_fields_present", "invoice_fields_missing"]),
                   ("contract_reference", ["invoice_reference_hint", "po_number_as_published", "contract_or_agreement_number", "solicitation_or_tender_number", "award_or_notice_id",
                                           "buyer_vendor_id", "vendor_ids_in_record", "commodity_codes", "buyer_org_codes", "amendment_or_modification", "all_identifiers", "identifier_count",
                                           "records_with_this_vendor", "all_references_with_this_vendor"]),
                   ("contract_title", ["contract_description", "instrument_type", "procurement_method", "commodity", "number_of_bids"]),
                   ("buyer_contact_evidence_url", ["buyer_legal_name_as_published", "buyer_bn_as_published", "buyer_gst_hst_derived", "buyer_logo_url", "buyer_website_status"]),
                   ("vendor_legal_name", ["vendor_trading_name", "vendor_registry_id", "vendor_registry_url", "vendor_registered_address", "vendor_neq", "vendor_qst_as_published", "vendor_legal_form", "vendor_activity_code", "vendor_employees_quebec", "vendor_establishments_quebec", "vendor_directors_range", "vendor_last_annual_filing"]),
                   ("vendor_contact_evidence_url", ["vendor_logo_url", "vendor_website_status"]),
                   ("invoicing_requirements", ["payment_terms_as_published", "po_required_as_published"]),
                   ("buyer_website_status", ["buyer_type", "buyer_facts_provenance", "distinct_canadian_vendors", "records_last_12_months", "latest_award_date_any_vendor", "total_known_value_canadian_suppliers", "other_canadian_vendors_sample", "record_sources"]),
                   ("vendor_website_status", ["vendor_registry_status", "vendor_registry_match_level", "vendor_incorporation_date", "vendor_bn_source", "vendor_billing_ar_email", "vendor_contacts_found_by", "vendor_peppol_id", "vendor_facts_provenance", "method_notes"]),
                   ("language_hint", ["template_language"]),
                   ("all_references_with_this_vendor", ["most_recent_record_reference_any_vendor", "records_in_contract_dataset", "other_relationship_sources"]),
                   ("buyer_type", ["sensitivity_tag", "sensitivity_flag", "buyer_sector", "peppol_participant_id", "peppol_registered"]),
                   ("completeness_score", ["data_quality_score", "ship_ready", "ship_ready_missing", "amount_mark", "payment_route", "payment_route_basis", "invoice_fields_for_kind", "invoice_fields_missing_for_kind", "vendor_tax_or_registration_number", "ap_mailbox_ready"]), ("email_check", ["mailbox_confidence", "evidence_age_days", "reverify_due"]), ("email_evidence_quote", ["email_evidence_context", "mailbox_recheck_note"]),
                   ("invoice_portal_url", ["invoice_portal_kind", "invoice_portal_note", "ap_system_hint", "invoicing_requirements_structured", "pay_on_sight", "pay_on_sight_missing", "channel_tier", "invoice_text", "invoice_card_json", "invoice_readiness", "invoice_missing", "ap_grade", "ap_score", "ap_grade_basis", "ap_gap_to_A", "ap_payability", "supplier_setup_url"]), ("payment_terms_as_published", ["payment_terms_default_policy"]),
                   ("instrument_type", ["instrument_type_normalized"]), ("contract_status", ["inference_confidence"]), ("buyer_bn_as_published", ["buyer_bn_program", "buyer_trade_name_as_published"]), ("vendor_registry_status", ["vendor_registry_warning", "vendor_registry_note"]),
                   ("other_relationship_sources", ["typical_contract_value_p50", "typical_contract_value_p75", "typical_cadence_days", "vendor_concentration_top_share", "all_canadian_vendors", "pair_prior_records", "pair_first_or_repeat", "pair_value_trend", "pair_dates_and_values"]),
                   ("method_notes", ["facts_provenance_json", "org_group_key"]), ("po_number_as_published", ["po_numbers_this_pair_open_data", "po_count_this_pair_open_data", "contract_numbers_this_pair_open_data"]), ("vendor_incorporation_date", ["vendor_years_in_business"]), ("dns_checked_date", ["mta_sts", "tls_rpt", "bimi"]),
                   ("invoicing_requirements_structured", ["buyer_payment_method_preference", "buyer_ap_cycle_published", "buyer_tax_exempt_status", "buyer_esignature_preference"]), ("buyer_website_status", ["buyer_linkedin_url", "buyer_supplier_portals_linked", "buyer_registry_id", "buyer_bn_note"]),
                   ("all_references_with_this_vendor", ["contract_value_from_pair", "start_date_from_pair", "end_date_from_pair", "contract_title_from_pair", "contract_description_from_pair", "instrument_type_from_pair", "procurement_method_from_pair", "number_of_bids_from_pair", "po_number_as_published_from_pair", "contract_or_agreement_number_from_pair", "solicitation_or_tender_number_from_pair", "award_or_notice_id_from_pair", "buyer_vendor_id_from_pair", "commodity_codes_from_pair", "buyer_org_codes_from_pair"]), ("vendor_website_status", ["vendor_website_basis", "vendor_linkedin_url", "vendor_industry_naics"]), ("peppol_registered", ["statutory_payees_inferred", "buyer_municipal_tier", "buyer_population", "directory_general_email", "municipal_directory_source", "buyer_fiscal_year_end", "buyer_charity_status", "buyer_charity_designation", "buyer_wikidata", "buyer_founded", "buyer_budget_or_revenue", "buyer_employees", "buyer_legal_form"]),
                   ("vendor_years_in_business", ["vendor_wikidata", "vendor_founded", "vendor_employees"]),
                   ("typical_contract_value_p75", ["typical_contract_value_p90", "average_contract_duration_days", "commodity_distribution_top3", "year_over_year_spend_trend"]),
                   ("buyer_tax_exempt_status", ["buyer_tax_status_derived", "tax_rate_indicative_derived", "invoice_currency_derived"]), ("end_date", ["contract_term_as_published"]),
                   ("recurring_billing", ["billing_cadence"]), ("contract_reference", ["po_or_reference_to_quote"]), ("commodity", ["contract_nature"]),
                   ("average_contract_duration_days", ["contract_durations_counted"])):
    if after in cols:
        i = cols.index(after) + 1
        cols[i:i] = [c for c in new if c not in cols]
# 2026-11-10: the last two passes (narrative columns, downstream pack) and the three output files are one pass over the rows: each row is completed,
# written and released. Both passes only read the row itself, and their long texts (provenance, invoice text, the invoice card as JSON …) were about
# half of a row's memory — held for every row at once just to be written a minute later. The row count is meant to grow tenfold on a 16 GB runner.
n9, npk = collections.Counter(), collections.Counter()
_vreg_key = lambda s_: " ".join(w_ for w_ in norm(s_).split() if w_ not in ("lp", "llp", "sec", "s", "e", "c", "srl", "r", "l", "the"))  # LP = S.E.C., LLP = S.R.L.: one partnership
VREG = {}
try:
    for _r in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools", "data", "vendor_registers.json"), encoding="utf-8")):
        for _a in _r.get("aliases") or ():
            VREG[_vreg_key(_a)] = _r
except (OSError, ValueError):
    pass
cnt, _n_rows, _n_mail, _n_contract = collections.Counter(), len(rows), 0, 0
# 2026-11-12 (owner, 08:45 EST: an amount on every row, estimated plausibly where none is published): the lowest yearly dues that the chambers
# of commerce and boards of trade of this build publish on their own pages, one figure a chamber — the basis of the estimate a member row of a
# chamber whose own dues are not read takes (tools/relationship_rows.py: estimate_missing_amount)
_chd = {}
for x in rows:
    if "member named in the member directory" not in (x.get("contract_status") or "") or not re.search(r"chamber of commerce|board of trade|chambre de commerce", x.get("vendor") or "", re.I):
        continue
    _ldc = LDET.get((x.get("keys") or "").split("|")[0]) or {}
    _vdc = registrable(host_of(_ldc.get("vendor_site") or x.get("vendor_website") or "") or "")
    if not _vdc or _vdc in _chd:
        continue
    _mdc = member_dues(VBILL.get(_vdc), _vdc) if VBILL.get(_vdc) else None
    if _mdc and _mdc[2] == "year" and (_mdc[1] or "CAD").upper() in ("CAD", "C$", "$", "") and 25 <= _mdc[0] <= 5000:
        _chd[_vdc] = _mdc[0]
if len(_chd) >= 20:
    _cv = sorted(_chd.values())
    _RR.CHAMBER_DUES = {"median": _cv[len(_cv) // 2], "n": len(_cv), "low": _cv[0], "high": _cv[-1]}
print("chambers of commerce and boards of trade whose lowest yearly dues are read on their own pages: %d%s" % (len(_chd), (" — median $%.0f, from $%.0f to $%.0f" % (
    _RR.CHAMBER_DUES["median"], _RR.CHAMBER_DUES["low"], _RR.CHAMBER_DUES["high"])) if _RR.CHAMBER_DUES else " (fewer than 20: no estimate from them)"))
# 2026-11-10 (disk): the plain CSV is 15 KB a row — 2.6 GB at 170,000 rows, 15 GB at a million; nothing reads it (a runner has 85 GB free).
# Only the compressed table is written now (batches.py and contracts_export.py read it); RANK_PLAIN_CSV=1 still writes the plain file for a local look.
_PLAIN = os.environ.get("RANK_PLAIN_CSV") == "1"
for _old in ("ranked_buyers.csv", "ranked_buyers.csv.gz", "ranked_buyers.jsonl.gz"):
    # removed, not overwritten: a plain table left by an earlier run would be read instead of this build's, and the publisher hard-links the
    # compressed table into coord/results/ranked/ (the "previous build" of the next run) — writing through the old name would empty that copy too
    if os.path.exists(ROOT + "/out/ranked/" + _old):
        os.remove(ROOT + "/out/ranked/" + _old)
_f1 = open(ROOT + "/out/ranked/ranked_buyers.csv", "w", newline="", encoding="utf-8") if _PLAIN else None
_f2 = gzip.open(ROOT + "/out/ranked/ranked_buyers.csv.gz", "wt", newline="", encoding="utf-8", compresslevel=6)  # the published copy
_f3 = gzip.open(ROOT + "/out/ranked/ranked_buyers.jsonl.gz", "wt", encoding="utf-8", compresslevel=6)  # S1.1: the same rows as JSON lines
_w1 = csv.DictWriter(_f1, fieldnames=cols, extrasaction="ignore") if _PLAIN else None
if _PLAIN:
    _w1.writeheader()
_w2 = csv.DictWriter(_f2, fieldnames=cols, extrasaction="ignore"); _w2.writeheader()
# 2026-11-12: the organisations that print the same urban postal code (_PC_DOMS, begun where the scan's codes are loaded): this build's rows added
_loc_rows = []
for x in rows:
    if x.get("tier") == "I":
        _pc = _BYLOC.code_of(x.get("buyer_address") or "") or _BYLOC.code_of(x.get("email_evidence_quote") or "")
        if _pc and _pc[1] != "0":
            _md = registrable((x.get("email") or "").partition("@")[2].lower())
            if _md:
                _PC_DOMS[_pc].add(_md)
            _loc_rows.append((x, _pc))
for x, _pc in _loc_rows:
    x["_pc_orgs"] = len(_PC_DOMS[_pc])
print("rows by where the organisation is, at an urban postal code many organisations print: %d or more (said on the row) %d; %d or more (the landlord's account: not ready) %d — of %d such rows at an urban code"
      % (_BYLOC.SHARED_SAY, sum(1 for x, _ in _loc_rows if x["_pc_orgs"] >= _BYLOC.SHARED_SAY), _BYLOC.SHARED_FAIL, sum(1 for x, _ in _loc_rows if x["_pc_orgs"] >= _BYLOC.SHARED_FAIL), len(_loc_rows)))
del _PC_DOMS, _loc_rows
for _ri, x in enumerate(rows):
    if _PI and x.get("_pre"):
        rows[_ri] = None  # ranking in parts: the rows that exist before the leads are written by part 0
        continue
    for col in ("vendor_billing_ar_email", "vendor_contacts_found_by", "invoice_reference_hint", "po_number_as_published", "contract_or_agreement_number", "solicitation_or_tender_number", "award_or_notice_id", "buyer_vendor_id", "vendor_ids_in_record",
                "commodity_codes", "buyer_org_codes", "amendment_or_modification", "all_identifiers", "identifier_count", "records_with_this_vendor", "all_references_with_this_vendor",
                "relationship_kind", "relationship_detail", "how_relationship_was_found", "recurring_billing", "recurring_billing_basis", "relationship_fact_basis", "bill_amount_indicative", "bill_amount_basis", "bill_items_as_published",
                "bill_currency_as_published", "bill_delivery_as_published", "bill_payment_method_as_published", "bill_tax_rule_as_published", "bill_identifier_format", "service_stops_if_unpaid", "bill_due_terms_as_published", "bill_remit_to_as_published", "billing_period_calculated", "bill_amount_calculated", "invoice_fields_present", "invoice_fields_missing", "buyer_type", "mailbox_provenance", "buyer_facts_provenance", "vendor_facts_provenance", "method_notes",
                "distinct_canadian_vendors", "records_last_12_months", "latest_award_date_any_vendor", "total_known_value_canadian_suppliers", "other_canadian_vendors_sample", "record_sources",
                "vendor_registry_status", "vendor_registry_match_level", "vendor_incorporation_date", "vendor_bn_source"):
        x.setdefault(col, "")
    if not x.get("contract_title") and (x.get("contract_description") or "").strip() and x.get("contract_link"):  # the source publishes a description but no separate title
        x["contract_title"] = re.split(r"(?<=[.!?])\s", x["contract_description"].strip(), maxsplit=1)[0][:150] + " (first sentence of the record's description; the source publishes no separate title)"
        n9["contract_title_from_description"] += 1
    if (x.get("contract_description") or "") in ("", "not_published") and (x.get("contract_title") or "").strip() and "publishes no separate title" not in (x.get("contract_title") or ""):
        x["contract_description"] = x["contract_title"].strip()[:300] + " (the record's title; the source publishes no separate description)"; n9["contract_description_from_title"] += 1
    elif (x.get("contract_description") or "") in ("", "not_published") and (x.get("relationship_detail") or "").strip():
        x["contract_description"] = "relationship record, no contract text: %s" % x["relationship_detail"].strip()[:280]; n9["contract_description_from_relationship"] += 1
    _hint = x.get("invoice_reference_hint") or ""
    if (not _hint or _hint.startswith(("no identifier", "only system"))) and (x.get("po_required_as_published") or "").startswith(("yes", "purchase-order terms published")):
        x["invoice_reference_hint"] = ("the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (%s)" if x["po_required_as_published"].startswith("yes") else
                                       "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (%s)") % x["po_required_as_published"][:200]  # owner 2026-11-08: the reference an AP clerk matches
        n9["invoice_reference_hint_po_rule"] += 1
    if not x.get("records_with_this_vendor") and not (x.get("vendor") or "").startswith("inferred"):  # downstream §1.10: a lead-based row has no contract record, the relationship record itself counts
        x["records_with_this_vendor"] = "1 (relationship record: %s; 0 in the contract dataset)" % ((x.get("how_relationship_was_found") or x.get("source") or "see contract_link")[:160])
        n9["records_with_this_vendor_lead"] += 1
    t = x.get("tier") or "N"
    # seen in the owner's test rows of 2026-11-11: a menu word as the buyer's name (579 "About" from BBB profiles), "Welcome to …" page titles, dates
    # written day-month by a Canadian BBB, the registry's legal name under an odd note, Shopify's Montréal office instead of the office its terms give
    _b = (x.get("buyer") or "").strip()
    if _IMG_NAME.search(_b):
        if x.get("buyer_website"):
            x["buyer"] = registrable(host_of(x["buyer_website"]) or "") or _b; n9["buyer named by an image's file name (a logo on the biller's page): its domain name instead"] += 1
        else:
            x["buyer_name_fault"] = "the name is an image's file name (“%s”), not the organisation's name" % _b[:80]; n9["buyer named by an image's file name, no site of its own: not ready"] += 1
        _b = (x.get("buyer") or "").strip()
    _vm = re.match(r"(?i)visit\s+(.{3,90}?)[’']s\s+(?:web\s?site|site|page)$", _b)
    if _vm:
        x["buyer"] = _b = _vm.group(1).strip(); n9["buyer name: a link's words (Visit …'s website) cut to the name"] += 1
    _hb = strip_home_word(_b)
    if _hb != _b and len(_hb) >= 3 and not re.search(r"home|accueil", re.sub(r"[^a-z]", "", (registrable(host_of(x.get("buyer_website") or "") or "") or "").lower())):
        x["buyer"] = _b = _hb; n9["buyer name: the page-title word Home / Accueil beside it removed"] += 1
    _lb = _LOGO_WORD.sub("", _b)
    _lb = _lb.strip(" -–—|:/.") if _lb != _b else _b
    if _lb != _b and len(_lb) >= 3 and "logo" not in (registrable(host_of(x.get("buyer_website") or "") or "") or "").lower():
        x["buyer"] = _b = _lb; n9["buyer name: the word Logo beside it removed"] += 1
    if place_name_not_this_org(_b, x.get("buyer_website") or ""):
        x["buyer"] = _b = registrable(host_of(x["buyer_website"]) or "") or _b; n9["buyer named by a town's bare name on a site that names more: its domain name instead"] += 1
    if _JUNK_NAME.match(_b) and x.get("buyer_website"):
        x["buyer"] = registrable(host_of(x["buyer_website"]) or "") or _b; n9["buyer named by a menu word (About, Home …): its domain name instead"] += 1
    else:
        _b2 = _TITLE_PREFIX.sub("", _b)
        if _b2 != _b and len(_b2) >= 3:
            x["buyer"] = _b2; n9["buyer name: the page-title opening (Welcome to …) removed"] += 1
    _b = (x.get("buyer") or "").strip()
    if _b.endswith("/") and _DOMAIN_NAME.fullmatch(_b.rstrip("/").lower()):
        x["buyer"] = _b = _b.rstrip("/"); n9["buyer name: the slash after its domain name removed"] += 1
    if (" | " in _b or "|" in _b) and x.get("buyer_website"):
        _b3 = name_from_title(_b, x["buyer_website"]) or _b.split("|")[0].strip(" -–—:")
        if 3 <= len(_b3) < len(_b):
            x["buyer"] = _b3; n9["buyer name: the part of a page title that names it"] += 1
    if "(stories" in (x.get("vendor_country_basis") or "") and x.get("buyer_website") and len(_b.split()) >= 4 and norm(x.get("contract_title") or "").startswith(norm(_b)[:40]) and not _LEGAL_PERSON.search(_b):
        x["buyer"] = _b = registrable(host_of(x["buyer_website"]) or "") or _b; n9["buyer named by the title of the vendor's story: its domain name instead"] += 1
    _v0 = (x.get("vendor") or "").strip()
    if not _v0.startswith("inferred") and x.get("vendor_website") and ("»" in _v0 or "|" in _v0 or " > " in _v0 or len(_v0.split()) >= 5):
        _v1 = name_from_title(_v0, x["vendor_website"]) if ("»" in _v0 or "|" in _v0 or " > " in _v0 or not _LEGAL_PERSON.search(_v0)) else ""
        if _v1 and _v1 != _v0 and len(_v1) < len(_v0):
            if _v1.islower():
                _v1 = _v1.capitalize()
            for _tc in ("contract_status", "relationship_detail", "relationship_fact_basis", "recurring_billing_basis", "contract_description", "bill_amount_basis", "vendor_country_basis"):
                if _v0 in (x.get(_tc) or ""):
                    x[_tc] = x[_tc].replace(_v0, _v1)
            if not (x.get("vendor_trading_name") or "").strip():
                x["vendor_trading_name"] = "%s (the title of the vendor's own home page)" % _v0[:120]
            x["vendor"] = _v1; n9["vendor named by its page title: the part that names it"] += 1
    for _ac in ("buyer_address", "vendor_address"):
        _a0 = x.get(_ac) or ""
        if _a0 and (_ADDR_MARK.search(_a0) or "\\n" in _a0 or "-->" in _a0 or "vendor_address_missing" in _a0 or re.match(r"\d{5}\s?\d{4}\s?RR|[a-zà-ÿ]|FIRM_ADDRESS", _a0) or (_CIVIC.search(_a0) and _CIVIC.search(_a0).start() > 20)):
            _a1 = addr_clean(_a0)
            if _a1 != _a0:
                x[_ac] = _a1; n9["%s: the page's words in front of it removed" % _ac] += 1
    if (x.get("contract_title") or "").strip().lower() in ("null", "none", "n/a", "nan", "undefined"):
        x["contract_title"] = ""; n9["subject that was the word null: emptied"] += 1
    for _dc in ("start_date", "end_date", "award_date"):
        _m = re.match(r"^(\d{4})-(\d\d)-(\d\d)$", x.get(_dc) or "")
        if _m and int(_m.group(2)) > 12 >= int(_m.group(3)):
            x[_dc] = "%s-%s-%s" % (_m.group(1), _m.group(3), _m.group(2)); n9["date written day-month: put in order"] += 1
    if t == "R":
        x["vendor_legal_name"] = CIRA_LEGAL
    # a party still shown under its domain name ("linknow.com", "business.nvchamber.ca": 11,308 vendor cells and 28,800 buyer cells on 2026-11-11) takes
    # the legal name the row already carries for it; the domain stays as the trading name
    for _side, _lcol, _tcol in (("vendor", "vendor_legal_name", "vendor_trading_name"), ("buyer", "buyer_legal_name_as_published", "buyer_trade_name_as_published")):
        _nm0 = (x.get(_side) or "").strip()
        if _DOMAIN_NAME.fullmatch(_nm0.lower()):
            _ln = _LEGAL_NOTE.split((x.get(_lcol) or "").strip())[0].strip(" -")
            if _ln and _ln != "not_published" and "(" not in _ln and 3 <= len(_ln) <= 90 and not _DOMAIN_NAME.fullmatch(_ln.lower()):
                if not (x.get(_tcol) or "").strip():
                    x[_tcol] = "%s (the %s's domain name, under which the relationship was found)" % (_nm0, _side)
                x[_side] = _ln; n9["%s shown under its legal name instead of its domain name" % _side] += 1
    _cvb = _BILL_CUR.get(norm(x.get("vendor") or "")) if t == "T" else None
    if _cvb and _cvb.get("addr"):
        x["vendor_address"] = _cvb["addr"]
    x["buyer_type"] = buyer_type(x.get("buyer"), x.get("jurisdiction") or x.get("_jur") or "")
    x["relationship_kind"] = KIND.get(t, KIND["N"])
    x["how_relationship_was_found"] = HOW_FOUND.get(t, HOW_FOUND["N"])
    if (x.get("contract_status") or "").startswith(("insured benefit plan of a Canadian insurer", "service provider in Canada paid by the organisation's benefit plan")):
        _ld = LDET.get((x.get("keys") or "").split("|")[0]) or {}
        x["relationship_kind"] = ("benefit plan contract: %s" % ("a Canadian insurer bills the employer's group insurance premiums (the plan's Form 5500)" if _ld.get("f55_insurer")
                                                                 else "a provider in Canada is paid by the employer's benefit plan (the plan's Form 5500)"))
        x["how_relationship_was_found"] = ("tools/f5500_benefits.py read the US Department of Labor's Form 5500 open data (Schedule A insurers, Schedule C providers with a foreign "
                                           "address in Canada); the sponsor's own site was kept only because %s; the mailbox comes from that site" % (_ld.get("site_tied_to_holder_by") or "its own pages print its ZIP code")[:420])
    if (x.get("contract_status") or "").startswith("importer of record of goods invoiced by"):
        _ld = LDET.get((x.get("keys") or "").split("|")[0]) or {}
        x["relationship_kind"] = "export sale: an exporter located in Canada invoices the importer for each shipment (Colombia's customs, DIAN, publishes the declaration)"
        x["how_relationship_was_found"] = ("tools/dian_cloud.py read DIAN's monthly declaration-level import microdata (importer, exporter and its address, invoice, value, "
                                           "form of payment); the importer's own site was kept only because %s; the mailbox comes from that site" % (_ld.get("site_tied_to_holder_by") or "its own pages print its NIT")[:420])
    if t == "M":  # tier M has several engines: say which one found this row
        _cs = x.get("contract_status") or ""
        if _cs.startswith("holder of licence"):
            _ld = LDET.get((x.get("keys") or "").split("|")[0]) or {}
            x["relationship_kind"] = "licence in force with a Canadian public body: the holder pays the body to keep it (the body's own public list of licences)"
            x["how_relationship_was_found"] = (("tools/rbq_licences.py read the Régie du bâtiment du Québec's daily open-data list of active licences; the holder's own site was kept only because it shows the "
                                                "holder's licence number, telephone, postal code or name (%s); the mailbox comes from that site") if _ld.get("platform") == "rbq_licence" else
                                               ("tools/biz_licences.py read the body's open-data list of licences in force and tied a licence to this organisation only on %s; several different licensees "
                                                "fitting one organisation are dropped")) % (_ld.get("site_tied_to_holder_by") or "the tests of the tool")
        elif _cs.startswith("registered with a Canadian regulatory authority"):
            _ld = LDET.get((x.get("keys") or "").split("|")[0]) or {}
            x["relationship_kind"] = "registration in force with a Canadian regulatory authority: the registrant pays the authority to be and to stay registered (the authority's own public register)"
            x["how_relationship_was_found"] = ("tools/authority_registers.py read the authority's public register entry by entry; the registrant's site is the one its entry names, kept only because its "
                                               "home page shows %s as the register has it; the mailbox comes from that site") % (_ld.get("site_tied_to_holder_by") or "the registrant's telephone number or postal code")
        elif _cs.startswith(("client of a Canadian trademark agent of record", "owner of ")) and "Canadian Intellectual Property Office" in _cs:
            _ld = LDET.get((x.get("keys") or "").split("|")[0]) or {}
            x["relationship_kind"] = ("professional representation before a Canadian public body: the owner's trademark agent of record, a Canada-located firm named by the register"
                                      if _cs.startswith("client") else
                                      "registration in force with a Canadian public body: the owner pays the Canadian Intellectual Property Office to register and renew its trademarks")
            x["how_relationship_was_found"] = ("tools/tm_register.py read the Canadian Intellectual Property Office's open-data trademarks register (owner of record with its address; agent of record "
                                               "with its address); the owner's own site was kept only on %s (%s); the mailbox comes from that site"
                                               % (_ld.get("site_tied_to_holder_by") or "the tests of the tool", (_ld.get("site_facts_from") or "")[:120]))
        elif _cs.startswith("listed issuer on a Canadian stock exchange"):
            _ld = LDET.get((x.get("keys") or "").split("|")[0]) or {}
            x["relationship_kind"] = ("listing on a Canadian stock exchange: the issuer pays the exchange %s (the exchange's own list and fee schedule)"
                                      % (_ld.get("xc_fee_words") or "an annual sustaining fee, on the exchange's invoice"))
            x["how_relationship_was_found"] = ("tools/exchange_issuers.py read the exchange's own list of listed companies (name, symbol, sector, listing date); the issuer's "
                                               "own site was kept only because %s; the mailbox comes from that site" % (_ld.get("site_tied_to_holder_by") or "the tests of the tool")[:400])
        elif _cs.startswith("client of a Canadian patent agent of record"):
            _ld = LDET.get((x.get("keys") or "").split("|")[0]) or {}
            x["relationship_kind"] = "professional representation before a Canadian public body: the owner's patent agent of record, a Canada-located firm named by the register"
            x["how_relationship_was_found"] = ("tools/pt_register.py read the Canadian Intellectual Property Office's open-data patent register (owner of record with its address; agent of record; "
                                               "the agent firm's address from the same Office's trademarks register); the owner's own site was kept only on %s (%s); the mailbox comes from that site"
                                               % (_ld.get("site_tied_to_holder_by") or "the tests of tools/tm_register.py", (_ld.get("site_facts_from") or "")[:120]))
        elif _cs.startswith("accredited business"):
            x["how_relationship_was_found"] = "tools/bbb_accredited.py read the business's public BBB profile (an archived copy; bbb.org's sitemap of accredited businesses says who is accredited today); the profile gives the business's own website"
        elif _cs.startswith("member of a Canadian body (stated on the buyer's own site"):
            x["how_relationship_was_found"] = "tools/credit_scan.py read the organisation's own home page, which states its membership of the Canada-located body and links to it"
    _ldb = LDET.get((x.get("keys") or "").split("|")[0]) or {}
    _vn0 = (x.get("vendor") or "").strip()
    if re.search(r"\s(?:d|l|qu|n|s|j|c)$", _vn0, re.I) and _ldb.get("page_title"):
        # 1,089 leads carry a vendor name cut at its apostrophe ("Chambre de Commerce et d", "Réseau d"): the page title the lead kept has the rest
        _mt = re.search(re.escape(_vn0) + r"['’]\s?([^|–—:·•]{2,80}?)(?=\s+[|–—:·•]|\s+-\s|$)", _ldb["page_title"])
        if _mt:
            x["vendor"] = "%s’%s" % (_vn0, _mt.group(1).strip()); n9["vendor name cut at an apostrophe: completed from the page title"] += 1
    x["recurring_billing"], x["recurring_billing_basis"] = billing_of(x, _ldb)
    if (x.get("tier") or "") not in ("I", "M", "R", "T", "D", "E") and (x.get("contract_value") or x.get("award_date") or x.get("contract_title")):
        _nat, _nwhy = contract_nature(x)
        if _nat:
            x["contract_nature"] = "%s — by %s" % ({"works": "works (construction)", "services": "a service", "goods": "goods"}[_nat], _nwhy)
    for _c, _v in bill_profile(x, _ldb, x["recurring_billing"]).items():
        if _v:
            x[_c] = _v
    if x.get("tier") == "I":
        # a row that stands on where the organisation is: what its distributor bills, how often, the least amount, how the bill arrives and is paid
        _bl = (_BYLOC.BY_KEY.get(x["_bps"][1]) if x.get("_bps") else None) or _BYLOC.of_row(x)  # a body's own energy report names its distributor (tools/bps_energy.py)
        if _bl:
            # 2026-11-12: a row that gave way to the distributor still went through the bill profile of the lead it came from — 2,600 rows of the
            # table of 00:14Z printed another vendor's tax sentence (a web host's "prix … avant taxes") on an electricity bill. Every bill cell
            # of such a row is the distributor's, or empty.
            if any(x.get(_c) for _c in ("bill_tax_rule_as_published", "bill_identifier_format", "bill_amount_indicative", "bill_payment_method_as_published", "bill_amount_calculated")):
                n_billcol["rows by where the organisation is that carried bill cells of another relationship's vendor: emptied"] += 1
            for _c in BILL_COLS:
                x[_c] = ""
            for _c, _v in _BYLOC.row_cells(_bl, x).items():
                if _v:
                    x[_c] = _v
            n_billcol["rows that stand on where the organisation is (its electricity distributor)"] += 1
            if x.get("_bps"):
                x.update(_bps_cells(x)); n_billcol["… of which on the body's own energy report (O. Reg. 25/23; the bill calculated from its own use)"] += 1
            elif x.get("_muni"):
                x["bill_amount_calculated"] = _MUNI.sentence(*x["_muni"])
                x["contract_title"] = "Electricity service to the municipality's facilities (its town hall's address: %s)" % ((x.get("buyer_address") or "").split(" (")[0][:120])
                n_billcol["… of which a municipality's, the bill estimated from its residents (tools/muni_energy.py)"] += 1
    if not CARD_ROWS:
        # the last check of the owner's rule (2026-11-11: "Remove them"): a row whose bill, as published, goes to a card on file or through a
        # registrar is not written — whatever lane it came from, and before it is counted anywhere below
        _rt0 = _RR.payment_route(x, _RR.kind_of(x))[0]
        if _rt0 in ("card", "registrar"):
            n9["rows not written — %s (owner 2026-11-11: on invoice, by bank transfer)" % _RR.ROUTE_LABEL[_rt0]] += 1
            _n_rows -= 1
            rows[_ri] = None
            continue
    if not str(x.get("vendor_bn9") or "").strip() and not (x.get("vendor") or "").startswith("inferred"):
        # the vendor's own GST/HST registration number as its site prints it (vendor reader, version 4): the first nine digits are its Business Number.
        # A number the vendor prints is published, and the cell says where; a QST number (ten digits) is not a Business Number and is left alone.
        _vd9 = registrable(host_of(x.get("vendor_website") or "") or "")
        _st9 = _VB.extra_of(VBILL.get(_vd9), "taxno") if _vd9 else None
        _m9 = re.search(r"\b(?:GST|HST|TPS|TVH)\b[^0-9]{0,40}(\d{9})(?!\d)(\s?RT\s?\d{4})?", (_st9 or {}).get("m") or "", re.I)
        if _m9 and len(set(_m9.group(1))) > 2 and _m9.group(1) not in ("123456789", "987654321"):
            x["vendor_bn9"] = "%s (the vendor's GST/HST number as its own site prints it: “%s”, %s, read %s)" % (_m9.group(1), _st9["q"][:140], _st9["u"], (VBILL.get(_vd9) or {}).get("date"))
            x["vendor_gst_hst_derived"] = ("%sRT0001 (as printed by the vendor)" % _m9.group(1)) if _m9.group(2) and re.sub(r"\s", "", _m9.group(2)).upper() == "RT0001" else \
                ("%sRT0001 (derived: BN9 + RT0001; the vendor prints its GST/HST number without the account suffix)" % _m9.group(1))
            n_billcol["vendor tax number from the GST/HST number the vendor's own site prints"] += 1
    if x.get("email"):
        n_bill[(x["recurring_billing"], t)] += 1
        for _c in BILL_COLS:
            n_billcol[_c] += bool(x.get(_c))
        # owner 2026-11-11 07:48 EST: "every single aspect within an invoice matters … the amount … the correct address, the vendor": the invoice's
        # fields on this row, one by one (a cell that says not_published is empty)
        _has = lambda c_: str(x.get(c_) or "").strip() not in ("", "not_published")  # contract_value is a number on dataset rows
        _sure = lambda c_: _has(c_) and "on that line alone" not in str(x.get(c_) or "")  # a legal name that rests on a copyright line alone is shown with its note, and not counted
        _inv = {"buyer legal name": _sure("buyer_legal_name_as_published"), "buyer address": _has("buyer_address"), "vendor legal name": _sure("vendor_legal_name"),
                "vendor address": _has("vendor_address") or _has("vendor_registered_address"), "vendor tax number": _has("vendor_bn9"),
                "what is billed": _has("contract_title") or _has("bill_items_as_published"), "amount": _has("contract_value") or _has("bill_amount_indicative"),
                "billing period": x["recurring_billing"][:1] in "1234", "reference": _has("contract_reference") or _has("invoice_reference_hint")}
        for _c, _v in _inv.items():
            n_inv[_c] += _v
        x["invoice_fields_present"] = "%d/9" % sum(_inv.values())
        x["invoice_fields_missing"] = "; ".join(c_ for c_, v_ in _inv.items() if not v_) or "none of the nine"
        n_inv["all nine"] += all(_inv.values())
        n_inv["all but the amount"] += all(v_ for c_, v_ in _inv.items() if c_ != "amount")
        if not _inv["amount"] and _has("bill_amount_calculated"):  # a calculated amount is not a published one: counted on its own line, never among the nine
            n_inv["amount, calculated only"] += 1
            n_inv["all nine with the amount calculated"] += all(v_ for c_, v_ in _inv.items() if c_ != "amount")
            x["invoice_fields_missing"] = x["invoice_fields_missing"].replace("amount", "amount (a calculated one is given)", 1)
        n_inv_t[(t, sum(_inv.values()))] += 1
        if (x.get("vendor") or "").startswith("Shopify"):
            n_bill_shop[(_ldb.get("buyer_country_evidence") or "")[:2].upper() or buyer_country(x) or "country not read"] += 1
    parts = ["%s (%s, %s) — %s: %s" % (x.get("buyer") or "", x["buyer_type"], x.get("jurisdiction") or x.get("_jur") or "jurisdiction not stated", x["relationship_kind"], x.get("vendor") or "vendor not named")]
    if x.get("contract_title"): parts.append("subject: %s" % x["contract_title"][:200])
    if x.get("instrument_type"): parts.append("instrument: %s" % x["instrument_type"])
    if x.get("po_number_as_published"): parts.append("PO / procurement number: %s" % x["po_number_as_published"][:160])
    if x.get("contract_or_agreement_number"): parts.append("contract number: %s" % x["contract_or_agreement_number"][:160])
    if x.get("solicitation_or_tender_number"): parts.append("solicitation: %s" % x["solicitation_or_tender_number"][:120])
    if x.get("contract_reference") and x["contract_reference"] not in ("{}", ""): parts.append("all identifiers: %s" % x["contract_reference"][:300])
    if x.get("contract_value"): parts.append("value: %s %s" % (x["contract_value"], x.get("currency") or ""))
    dates = ", ".join(l for l in (("awarded %s" % x["award_date"]) if x.get("award_date") else "", ("start %s" % x["start_date"]) if x.get("start_date") else "", ("end %s" % x["end_date"]) if x.get("end_date") else "") if l)
    if dates: parts.append(dates)
    if x.get("source"): parts.append("published by: %s" % x["source"])
    if x.get("contract_link"): parts.append("record: %s" % x["contract_link"])
    if x.get("vendor_country_basis"): parts.append("vendor in Canada because: %s" % x["vendor_country_basis"][:220])
    if x.get("contract_status"): parts.append("status rule: %s" % x["contract_status"][:220])
    parts.append("billing period: %s — %s" % (x["recurring_billing"], x["recurring_billing_basis"][:260]))
    if x.get("distinct_canadian_vendors"): parts.append("this buyer has %s records with Canada-located vendors (%s distinct vendors; %s in the last 12 months; latest %s)" % (x.get("contracts_with_canadian_suppliers"), x["distinct_canadian_vendors"], x.get("records_last_12_months") or "0", x.get("latest_award_date_any_vendor") or "n/a"))
    x["relationship_detail"] = " | ".join(parts)
    e = (x.get("email") or "").lower()
    if e:
        meta = next((LANE_META.get((k, e)) for k in (x.get("keys") or "").split("|") if (k, e) in LANE_META), None) or LANE_META.get(("", e))
        lane, file, rdate, task = meta if meta else ("", "", "", "")
        n9["mailbox meta found" if meta else "mailbox meta missing"] += 1
        mp = ["%s (%s)" % (e, x.get("email_type") or "")]
        mp.append(mailbox_how(file, lane) + (" on %s" % rdate if rdate else ""))
        mp.append("page: %s" % (x.get("email_evidence_url") or ""))
        if x.get("email_evidence_quote"): mp.append("quote: \"%s\"" % x["email_evidence_quote"][:160].replace("\n", " "))
        mp.append(("verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report %s)" % INGEST_DATE) if x.get("email_check") == "confirmed" else "verification: %s" % (x.get("email_check") or "pending"))
        if x.get("email_deliverability"): mp.append("DNS: %s" % x["email_deliverability"])
        if x.get("email_security_posture"): mp.append(x["email_security_posture"])
        if lane: mp.append("lane file: %s/%s%s" % (lane, file, (" task %s" % task) if task else ""))
        x["mailbox_provenance"] = " | ".join(mp)
    bp = []
    if x.get("buyer_address") and x.get("buyer_contact_evidence_url"): bp.append("address and phone: the buyer's own site, %s (tools/org_contacts.py: JSON-LD / contact page; no AI)" % x["buyer_contact_evidence_url"])
    elif x.get("buyer_address"): bp.append("address: the buyer's record / buyer table")
    if x.get("buyer_legal_name_as_published"): bp.append("legal name: " + ("the source named in brackets in buyer_legal_name_as_published" if x["buyer_legal_name_as_published"].rstrip().endswith(")") else "the copyright / footer line of the organisation's own site (tools/org_extras.py)"))
    if x.get("buyer_bn_as_published"): bp.append("BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed")
    if x.get("buyer_logo_url"): bp.append("logo: og:image / logo image of the buyer's site")
    if x.get("buyer_website_status"): bp.append("website: %s" % x["buyer_website_status"])
    for col, lab in (("ap_phone", "AP phone"), ("invoice_mailing_address", "invoice mailing address"), ("invoicing_requirements", "invoicing requirements"), ("payment_terms_as_published", "payment terms"), ("po_required_as_published", "PO requirement"), ("invoice_portal_url", "invoice portal"), ("ap_contact_name_as_published", "AP contact name")):
        if x.get(col): bp.append("%s: %s" % (lab, ("the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)" if col in (x.get("_at") or ()) else "the lane's AP page (%s)" % (x.get("email_evidence_url") or "evidence page"))))
    x["buyer_facts_provenance"] = "; ".join(bp) if bp else "no buyer facts beyond the record and the mailbox page"
    vp = []
    if x.get("vendor"): vp.append("name and address: the record's vendor block (%s)" % (x.get("source") or "source"))
    if x.get("vendor_registry_id"): vp.append("registry identity: %s%s (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; %s)" % (x["vendor_registry_id"], (" status %s" % x["vendor_registry_status"]) if x.get("vendor_registry_status") else "", x.get("vendor_registry_match_level") or "match"))
    if x.get("vendor_bn9"): vp.append("BN9: %s; GST/HST %s" % (x.get("vendor_bn_source") or "registry match", "derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated)"))
    if x.get("vendor_incorporation_date"): vp.append("incorporated / registered: %s" % x["vendor_incorporation_date"])
    if x.get("vendor_contact_evidence_url"): vp.append("phone / role e-mails / logo: the vendor's own site, %s (tools/org_contacts.py, org_extras.py)" % x["vendor_contact_evidence_url"])
    if x.get("vendor_contacts_found_by"): vp.append("role / billing mailboxes researched by the %s" % x["vendor_contacts_found_by"][:200])
    if x.get("vendor_website"): vp.append("website: %s%s" % (x["vendor_website"], (" (%s)" % x["vendor_website_status"]) if x.get("vendor_website_status") else ""))
    if x.get("vendor_neq"): vp.append("NEQ: %s" % x["vendor_neq"])
    x["vendor_facts_provenance"] = "; ".join(vp) if vp else "no vendor facts beyond the record"
    x["method_notes"] = "no AI-written values; every fact carries its page in the matching *_evidence_url / *_provenance column; blank = not_published; method and rules: contrib/claude/rank_buyers/README.md, AGENTS.md §2"
    try:  # the downstream pack is guarded: a failure never stops the build (the row is written with what it has)
        for c in PACK_COLS:
            x.setdefault(c, "")
        # 2026-11-10: what the buyer's OWN pages say (tools/lead_crawl.py site facts): its postal address when the row has none, and the name it
        # trades under. An invoice may name the recipient by "the name under which the recipient does business" (Input Tax Credit Information
        # (GST/HST) Regulations, SOR/91-45 s. 3(c)(i)), so a self-published trade name with an address completes the bill-to block.
        _lf = next((LFACTS[_k] for _k in (x.get("keys") or "").split("|") if _k in LFACTS), None)
        x.setdefault("buyer_trade_name_as_published", "")
        if _lf:
            if _lf.get("address") and not (x.get("buyer_address") or "").strip() and not (x.get("invoice_mailing_address") or "").strip():
                x["buyer_address"] = lf_cell(_lf); npk["buyer_address_from_own_page"] += 1
            if _lf.get("site_name") and not x["buyer_trade_name_as_published"]:
                x["buyer_trade_name_as_published"] = "%s (the name on the organisation's own home page, %s, read %s)" % (_lf["site_name"], _lf.get("site") or "", _lf.get("date") or ""); npk["buyer_trade_name_as_published"] += 1
        # 2026-11-12 (billers first): a vendor's number in its home register as the global LEI register records it (tools/data/vendor_registers.json,
        # exact legal names only: Smart & Biggar, KPMG, Gowling WLG), when nothing else gave the row a number
        # 2026-11-13 (owner 13:23 EST, every field): the agent of record as the Office's register names it, with its legal form ("SMART & BIGGAR LP",
        # "MOFFAT & CO.", "RIEL PROFESSIONAL CORPORATION"), is the firm's legal name: 5,139 agent rows had none
        if not str(x.get("vendor_legal_name") or "").strip() and (x.get("contract_status") or "").startswith(("client of a Canadian trademark agent", "client of a Canadian patent agent")) \
                and re.search(r"\b(?:LLP|L\.L\.P\.|LP|L\.P\.|S\.?E\.?N\.?C\.?R\.?L\.?|S\.E\.C\.|INC\.?|INCORPORATED|LTD\.?|LIMITED|LT[ÉE]E|CORP(?:ORATION)?\.?|PROFESSIONAL CORPORATION|& CO\.?|AND COMPANY)\b", x.get("vendor") or "", re.I):
            x["vendor_legal_name"] = "%s (as the Canadian Intellectual Property Office's register names the agent of record, with its legal form)" % re.sub(r"\s+", " ", x["vendor"]).strip()
            npk["vendor legal name: the agent of record as the Office's register names it"] += 1
        if VREG and not any(str(x.get(c_) or "").strip() for c_ in ("vendor_bn9", "vendor_neq", "vendor_registry_id")):
            _vr = VREG.get(_vreg_key(x.get("vendor") or ""))
            if _vr:
                x["vendor_registry_id"] = _vr["registration"]; npk["vendor number from the LEI register (tools/data/vendor_registers.json)"] += 1
        # test set of 2026-11-12: a copyright line taken for the name ("© 2017-2026 ITMBC Enterprises Inc.")
        _bn9 = re.sub(r"^\s*(?:©|\(c\)|copyright)\s*(?:©\s*)?(?:(?:19|20)\d{2}\s*(?:[-–]\s*(?:19|20)\d{2})?)?\s*[,.|:–-]*\s*", "", x.get("buyer") or "", flags=re.I).strip()
        if _bn9 != (x.get("buyer") or "").strip() and len(_bn9) >= 3:
            x["buyer"] = _bn9; npk["buyer name without the copyright sign and years in front of it"] += 1
        # 2026-11-12: nothing on file gives the buyer's address — the address an Overture Maps place lists for its website, when the domain's places
        # print one postal code and the place's name fits the buyer's; the cell says it is a public places dataset's (tools/by_location.py)
        if OVT and not (x.get("buyer_address") or "").strip() and not (x.get("invoice_mailing_address") or "").strip():
            _md9 = (x.get("email") or "").lower().partition("@")[2]
            for _d9 in dict.fromkeys(d_ for d_ in ((registrable(_md9) if _md9 and not FREEMAIL.match(_md9) else ""),
                                                  (registrable(host_of(x["buyer_website"])) if x.get("buyer_website") else "")) if d_):
                _oa9 = OVT.get(_d9)
                if _oa9 and _ovt_fits(x.get("buyer") or "", _oa9.get("names") or "", _d9):
                    x["buyer_address"] = _BYLOC.directory_cell(_oa9); npk["buyer_address_from_a_listed_place (%s)" % ("Foursquare" if _oa9.get("datasets") == "Foursquare" else "Overture Maps")] += 1
                    break
        # 2026-11-13: then the place listing the organisation's own telephone number, under its name or with its website (tools/phone_places.py)
        if PHP and not (x.get("buyer_address") or "").strip() and not (x.get("invoice_mailing_address") or "").strip():
            _po9 = next((PHP[_k9] for _k9 in (x.get("keys") or "").split("|") if _k9 in PHP), None)
            if _po9:
                x["buyer_address"] = _BYLOC.phone_cell(_po9); npk["buyer_address_from_the_place_listing_its_telephone (%s)" % ("Foursquare" if str(_po9.get("release") or "").startswith("Foursquare") else "Overture Maps")] += 1
        t, g, ec = x.get("tier") or "", int(x.get("grade") or 0), x.get("email_check") or ""
        name_site = " ".join((x.get(c) or "") for c in ("buyer", "buyer_legal_name_as_published", "buyer_trade_name_as_published", "buyer_website"))
        # buyer_type fallback (C4.1) and sector (S4.1)
        if (x.get("buyer_type") or "").startswith("organisation (type not stated"):
            for lab, rx in TYPE_RULES:
                if re.search(rx, name_site, re.I):
                    x["buyer_type"] = lab + " (from the organisation's name / web domain)"; npk["buyer_type_from_name"] += 1; break
        x["buyer_sector"] = next((lab for lab, rx in SECTOR if re.search(rx, x.get("buyer_type") or "", re.I)), "not stated")
        # sensitivity (M1/M2)
        if (x.get("sensitivity_tag") or "").startswith("none"):
            for lab, rx in EXTRA_SENS:
                if rx.search(name_site):
                    x["sensitivity_tag"] = "high-sensitivity buyer (%s): suppress from outreach unless reviewed (tag from the organisation's published name / domain)" % lab; npk["sensitivity_extra"] += 1; break
        # 2026-11-11 (a row of the owner's test set: a named professional's own site as the buyer): a buyer that carries one person's name and nothing
        # else — a given name, then one word that few organisations' names carry, no legal form anywhere on the row — may be a person, not an
        # organisation. It is tagged for review like the other sensitive kinds (so it is not "ship ready" and is not drawn into test sets); the
        # row stays. Contract records are left alone: their buyers are organisations by the record itself.
        if (x.get("sensitivity_tag") or "").startswith("none") and t not in ("A", "B", "C", "L", "F"):
            _pb = (x.get("buyer") or "").strip()
            # 2026-11-11 (test set: "Michelle Harrison PREC*", "Website of Quimper-Swiderski, Hannah"): the name is read without the designation a
            # professional adds to it, and "Surname, Given" is turned round
            _pb = re.sub(r"\s+", " ", _PERSON_DESIG.sub(" ", _pb)).strip(" ,.-–|")
            if _pb.count(",") == 1 and all(len(re.findall(r"[A-Za-zÀ-ÿ'’.-]+", h_)) == 1 for h_ in _pb.split(",")):
                _pb = " ".join(h_.strip() for h_ in reversed(_pb.split(",")))
            _pt = re.findall(r"[A-Za-zÀ-ÿ'’.-]+", _pb)
            if len(_pt) == 2 and len(_pb) <= 34 and not re.search(r"\d|[|/@&]", _pb) and _pt[0][:1].isupper() and _pt[1][:1].isupper():
                _f0 = re.split(r"[-.]", unicodedata.normalize("NFKD", _pt[0]).encode("ascii", "ignore").decode().lower())[0]
                _l0 = norm(_pt[1])
                if _f0 in _FIRST and _l0 and _l0 not in WORD_COMMON and _l0 not in GENERIC_ORG and not _LEGAL_PERSON.search(_pb + " " + (x.get("buyer_legal_name_as_published") or "").split(" (")[0]):
                    x["sensitivity_tag"] = "high-sensitivity buyer (one person's name: the site may be a person's own and not an organisation's): suppress from outreach unless reviewed (tag from the buyer's name)"
                    npk["sensitivity_one_persons_name"] += 1
        x["sensitivity_flag"] = "yes" if (x.get("sensitivity_tag") or "").startswith("high") else "no"
        # confidence columns (H4.2 / T4)
        m = re.search(r"\b(high|medium|low) confidence\b", (x.get("contract_status") or "") + " " + (x.get("relationship_detail") or ""), re.I)
        if t == "I":
            conf = (m.group(1).upper() + " (" + {"HIGH": "statutory or sole-provider relationship for this type of organisation", "MEDIUM": "typical supplier for this type of organisation", "LOW": "plausible supplier only"}[m.group(1).upper()] + ")") if m else "not stated in this build"
            if re.search(r"municipal property assessment|\bMPAC\b", x.get("vendor") or "", re.I) and (x.get("buyer_municipal_tier") or "").lower().startswith("lower"):
                conf = "not applicable — lower-tier Ontario municipality: MPAC levies the upper-tier municipality (MPAC Act s. 12(1)); do not use this inference"
            if re.search(r"canada post|postes canada", x.get("vendor") or "", re.I) and re.search(r"non-profit|religious|library", x.get("buyer_type") or "", re.I):
                conf = "LOW (small organisation: mailing volume unknown)"
            # H2: cities served by a municipal electricity distributor, not by the provincial utility at retail
            _city = " ".join((x.get(c) or "") for c in ("buyer", "buyer_address"))
            if re.search(r"hydro-?qu[ée]bec", x.get("vendor") or "", re.I) and re.search(r"\b(Alma|Amos|Baie-Comeau|Coaticook|Joliette|Magog|Saguenay|Chicoutimi|Jonqui[èe]re|Sherbrooke|Westmount|Saint-Jean-Baptiste-de-Rouville)\b", _city, re.I):
                conf = "LOW (this city is served at retail by its municipal electricity distributor; Hydro-Québec supplies it at wholesale)"
            if re.search(r"saskpower", x.get("vendor") or "", re.I) and re.search(r"\b(Saskatoon|Swift Current)\b", _city, re.I):
                conf = "LOW (this city runs its own electricity utility; SaskPower supplies it at wholesale)"
            x["inference_confidence"] = conf
        else:
            x["inference_confidence"] = "n/a (the relationship is a record, not an inference)"
        x["mailbox_confidence"] = ("%s; %s" % ({"confirmed": "verified by the referee (page re-fetched)", "cross_verified": "cross-verified by two lanes", "pending": "pending referee check"}.get(ec.split(";")[0], ec or "no mailbox"),
                                               {4: "invoicing / AP mailbox", 3: "finance mailbox", 2: "purchasing mailbox", 1: "general role mailbox"}.get(g, "no mailbox"))) if x.get("email") else "no mailbox"
        # portal cleanup (D6)
        pu = x.get("invoice_portal_url") or ""
        if pu:
            url_part, _, note = pu.partition(" (")
            x["invoice_portal_url"] = url_part.strip()
            x["invoice_portal_note"] = ("(" + note).strip() if note else ""
            x["invoice_portal_kind"] = "actionable supplier / invoice portal named by the buyer" if PORTAL_ACTIONABLE.search(url_part) else "other page named by the buyer (check before use)"
        # policy default (D4.2)
        if (x.get("jurisdiction") or "") == "FED" or re.search(r"\.gc\.ca|canada\.ca", (x.get("buyer_website") or "") + " " + (x.get("email") or "")):
            x["payment_terms_default_policy"] = "Government of Canada standard: payment within 30 days of receipt of a valid invoice (Treasury Board Directive on Payments) — policy default, not this buyer's published term"
        # statutory prompt-payment default for CONSTRUCTION work (owner 2026-11-08 11:53 EST: derived defaults only where nothing is published, source-cited, last resort):
        # payment_terms_as_published stays empty; payment_terms_default_policy carries the statute the buyer is bound by, with URL, date read and quote.
        if not x.get("payment_terms_default_policy") or (x.get("jurisdiction") or "") == "FED":
            pc_ = re.search(r"\b([A-Z])\d[A-Z]\s?\d[A-Z]\d\b", x.get("buyer_address") or "")
            prov = {"QC": "QC", "ON": "ON", "BC": "BC", "AB": "AB", "SK": "SK", "MB": "MB", "NS": "NS", "NB": "NB", "NL": "NL", "PE": "PE", "YT": "YT", "NT": "NT", "NU": "NU"}.get(x.get("jurisdiction") or "", "")
            if not prov and pc_:
                prov = {"G": "QC", "H": "QC", "J": "QC", "K": "ON", "L": "ON", "M": "ON", "N": "ON", "P": "ON", "V": "BC", "T": "AB", "S": "SK", "R": "MB", "B": "NS", "E": "NB", "A": "NL", "C": "PE", "Y": "YT", "X": "NT"}.get(pc_.group(1), "")
            if not prov:
                md_ = re.search(r"\.(qc|on|bc|ab|sk|mb|ns|nb|nl|pe|yk|nt|nu)\.ca(?:/|$)", (x.get("buyer_website") or "").lower())
                prov = md_.group(1).upper().replace("YK", "YT") if md_ else ""
            bt = x.get("buyer_type") or ""
            ctext = " ".join((x.get(c) or "") for c in ("contract_description", "commodity", "contract_title", "commodity_distribution_top3"))[:600]
            naics = (x.get("vendor_industry_naics") or "").strip()
            is_constr = bool(CONSTR_RX.search(ctext)) or bool(re.match(r"^23\d", naics)) or bool(re.search(r"\b72\d{6}\b", x.get("commodity_codes") or ""))
            if is_constr:
                fed = (x.get("jurisdiction") or "") == "FED" or bool(re.search(r"\.gc\.ca|canada\.ca", (x.get("buyer_website") or "") + " " + (x.get("email") or "")))
                crown_ab = bool(re.search(r"ministry|government|agency|crown", bt, re.I))
                if fed:
                    x["payment_terms_default_policy"] = PROMPT_PAY["FED"]
                elif prov == "ON":
                    x["payment_terms_default_policy"] = PROMPT_PAY["ON"]
                    if (x.get("recurring_billing") or "").startswith("5") and not x.get("billing_period_calculated"):
                        x["billing_period_calculated"] = ON_MONTHLY; n_billcol["billing_period_calculated (Ontario construction)"] += 1
                elif prov == "AB" and not crown_ab:
                    x["payment_terms_default_policy"] = PROMPT_PAY["AB"]
                if x.get("payment_terms_default_policy", "").startswith("statutory"):
                    npk["prompt_payment_default"] += 1
        # instrument normalisation (E4.2)
        it = (x.get("instrument_type") or "") + " " + (x.get("contract_title") or "")[:80]
        x["instrument_type_normalized"] = next((lab for lab, rx in INSTR if re.search(rx, it, re.I)), "other / not stated") if (x.get("instrument_type") or x.get("contract_title")) else ""
        # description cut (E3.2)
        d = x.get("contract_description") or ""
        if len(d) >= 299:
            cut = max(d.rfind(". ", 150), d.rfind("; ", 150))
            x["contract_description"] = (d[:cut + 1] if cut > 0 else d[:d.rfind(" ", 150)]).strip() + " …"
        # currency default (E1.2)
        if x.get("contract_value") and not x.get("currency") and t in ("A", "B", "L", "C", "D", "F") and CUR.get(x.get("jurisdiction") or ""):
            x["currency"] = "%s (default: this source publishes in %s)" % (CUR[x["jurisdiction"]], CUR[x["jurisdiction"]]); npk["currency_default"] += 1
        # BN program (R4.1)
        b = x.get("buyer_bn_as_published") or ""
        if b:
            x["buyer_bn_program"] = "RR (registered charity program account)" if re.search(r"\bRR\s?\d{4}", b) else "RT (GST/HST program account)" if re.search(r"RT\s?\d{4}|GST|HST|TPS|TVH", b) else "program not stated with the number"
        # dissolved vendors (R5.1)
        vs = x.get("vendor_registry_status") or ""
        _segs = [t.strip() for t in vs.split(";") if t.strip()]
        _dead = re.compile(r"dissol|inactive|radi[ée]|cancel|revoked|struck|annul|liquidat|discontinued|amalgamated|historical", re.I)
        _live = re.compile(r"\bactive\b|immatricul|en vigueur|in good standing|registered\b|existing|current", re.I)
        # 2026-11-08 19:55 EST: warn when the vendor's PRIMARY registry record is dead, or when no registry shows it alive — not when an extra-provincial
        # registration lapsed while the home registry says Active (542 Gold rows carried the warning for that and lost grade A)
        # 2026-11-12: a corporation that amalgamated or was continued elsewhere goes on as its successor (GFL Environmental, Evertz, Kinectrics were
        # "Inactive — amalgamated" under an old number while they bill today); and a vendor that a CURRENT record names — a body's roster or
        # register read in the last year, a contract dated in the last twelve months — exists, whatever a namesake's entry says. Those keep a note;
        # the warning (which takes the row out) stays for an end — dissolved, struck off, cancelled, revoked, liquidated, bankrupt — of a vendor
        # no current record names. 972 rows failed on the warning alone in the table of 13:24Z.
        _succ = re.compile(r"amalgamat|continu|fusion", re.I)
        _end = re.compile(r"dissol|radi[ée]|cancel|revoked|struck|annul|liquidat|bankrupt|faillite", re.I)
        _segdead = lambda t_: bool(_dead.search(t_)) and not _live.search(t_) and not _succ.search(t_)
        _current_rec = t == "M" or (t in ("A", "B") and (x.get("award_date") or "")[:10] >= CUTOFF)
        if _segs and (_segdead(_segs[0]) or (not any(_live.search(t_) or _succ.search(t_) for t_ in _segs) and any(_segdead(t_) for t_ in _segs))):
            if _current_rec or not any(_end.search(t_) for t_ in _segs):
                x["vendor_registry_note"] = ("a register lists '%s' for a corporation of this name — %s; the warning is not kept"
                                             % (vs[:80], "the vendor is named in a current record (%s)" % ("the body's own list, read in the last year" if t == "M" else "a contract dated %s" % (x.get("award_date") or "")[:10])
                                                if _current_rec else "an inactive entry with no end (dissolution, striking off, cancellation) stated, often an old number of a living company"))
                npk["registry_note: dead-looking entry, vendor current or no end stated"] += 1
            else:
                x["vendor_registry_warning"] = "WARNING: registry status '%s' — the match may be a namesake or the vendor may no longer exist; verify before use" % vs[:60]; npk["registry_warning"] += 1
        elif _segs and any(_succ.search(t_) for t_ in _segs) and not any(_live.search(t_) for t_ in _segs):
            x["vendor_registry_note"] = "a register lists '%s': the corporation amalgamated or was continued, and goes on as its successor" % vs[:80]; npk["registry_note: amalgamated / continued"] += 1
        elif _segs and any(_dead.search(t) for t in _segs[1:]):
            x["vendor_registry_note"] = "another registry lists a lapsed registration (%s); the primary record is alive" % "; ".join(t[:50] for t in _segs[1:] if _dead.search(t))[:160]; npk["registry_note"] += 1
        # evidence age (O1.3)
        md = re.search(r" on (\d{4}-\d{2}-\d{2})", x.get("mailbox_provenance") or "")
        if md:
            try:
                age = (_today - datetime.date.fromisoformat(md.group(1))).days
                x["evidence_age_days"] = str(age); x["reverify_due"] = "yes (mailbox evidence older than 60 days)" if age > 60 else "no"
            except ValueError:
                pass
        # AP system hint (N1)
        sysn = sorted(set(m2.group(1) for m2 in AP_SYS.finditer(" ".join((x.get(c) or "") for c in ("invoicing_requirements", "invoice_portal_url", "invoice_portal_note", "email_evidence_quote")))))
        if sysn:
            prev = x.get("ap_system_hint") or ""
            x["ap_system_hint"] = ("named on the buyer's page: " + ", ".join(sysn)[:200]) + (("; " + prev) if prev and not prev.startswith("named on") else "")
        # structured requirements (D3.2)
        fmt = re.search(r"invoice format as published: ([^|]+)", x.get("invoicing_requirements") or "")
        x["invoicing_requirements_structured"] = json.dumps({k: v for k, v in (("submission_channel", "e-mail" + (" + portal" if x.get("invoice_portal_url") else "")), ("payment_terms", x.get("payment_terms_as_published") or ""), ("po_required", x.get("po_required_as_published") or ""),
                                                             ("portal_url", x.get("invoice_portal_url") or ""), ("portal_kind", x.get("invoice_portal_kind") or ""), ("invoice_format", fmt.group(1).strip() if fmt else ""), ("ap_phone", x.get("ap_phone") or ""),
                                                             ("mailing_address", x.get("invoice_mailing_address") or ""), ("requirements_text", (x.get("invoicing_requirements") or "")[:300])) if v}, ensure_ascii=False) if x.get("email") else ""
        # owner 2026-11-08 11:21 EST ("invoice grade, invoice framing"): the row read as the header of an invoice this vendor would send this buyer —
        # bill-to, submit-to, references, terms, tax, currency, vendor identity, follow-up — with every element's presence checked
        def _val(c):
            v = x.get(c)
            v = ("" if v is None else str(v)).strip()  # contract_value may still be a float in a few rows
            return "" if (not v or v in ("not_published", "{}", "[]") or re.match(r"^(?:no |none\b|not |0 in the|only system|n/a\b|not applicable|unknown\b|aucun|no dataset|no record|no identifier)", v, re.I)) else v
        # derived GST/HST status and indicative rate (owner 2026-11-08 11:53 EST: plausibility values only where nothing is published, source-derived, labelled)
        x["buyer_tax_status_derived"] = x["tax_rate_indicative_derived"] = x["invoice_currency_derived"] = ""
        _site0 = (x.get("buyer_website") or "").lower().rstrip("/"); _jur0 = (x.get("jurisdiction") or "").upper()
        _cc0 = ({"US": "US", "UK": "GB", "GB": "GB", "AU": "AU", "NZ": "AU", "EU": "EU", "DE": "EU", "FR": "EU", "NL": "EU", "BE": "EU", "IE": "EU", "IT": "EU", "ES": "EU", "AT": "EU", "SE": "EU", "DK": "EU", "FI": "EU", "PL": "EU", "PT": "EU", "CH": "EU", "NO": "EU"}.get(_jur0) or
                ("US" if re.search(r"\.(gov|edu|mil|us)$|\.gov\b", _site0) else "GB" if re.search(r"\.uk$", _site0) else "AU" if re.search(r"\.(au|nz)$", _site0) else "EU" if re.search(r"\.(eu|de|fr|nl|be|ie|it|es|at|se|dk|fi|pl|pt|ch|no)$", _site0) else ""))
        if not _cc0 and _lf and _lf.get("address_country") in ("US", "GB", "AU") and (_lf.get("address") or "") and (_lf["address"][:40] in (x.get("buyer_address") or "")):
            _cc0 = _lf["address_country"]  # the address printed on the buyer's own page is in that country (.com sites carry no country)
        if not _cc0:
            pc2 = re.search(r"\b([A-Z])\d[A-Z]\s?\d[A-Z]\d\b", x.get("buyer_address") or "")
            prov2 = {"QC": "QC", "ON": "ON", "BC": "BC", "AB": "AB", "SK": "SK", "MB": "MB", "NS": "NS", "NB": "NB", "NL": "NL", "PE": "PE", "YT": "YT", "NT": "NT", "NU": "NU"}.get(x.get("jurisdiction") or "", "")
            if not prov2 and pc2:
                prov2 = {"G": "QC", "H": "QC", "J": "QC", "K": "ON", "L": "ON", "M": "ON", "N": "ON", "P": "ON", "V": "BC", "T": "AB", "S": "SK", "R": "MB", "B": "NS", "E": "NB", "A": "NL", "C": "PE", "Y": "YT", "X": "NT"}.get(pc2.group(1), "")
            if not prov2:
                md3 = re.search(r"\.(qc|on|bc|ab|sk|mb|ns|nb|nl|pe|yk|nt|nu)\.ca(?:/|$)", (x.get("buyer_website") or "").lower() + " " + (x.get("email") or "").lower().split("@")[-1] + "/")
                prov2 = md3.group(1).upper().replace("YK", "YT") if md3 else ""
            if not prov2:  # 2026-11-08 20:10 EST (owner: tax treatment on every row an invoice can be built for): the registry place table, then the city named in the address
                for _k in (x.get("keys") or "").split("|"):
                    _pp = (PLACES.get(_k) or {}).get("province") or ""
                    if _pp.upper() in TAX_RATE or _pp.upper() in ("QC", "BC", "AB", "SK", "MB", "YT", "NT", "NU"):
                        prov2 = _pp.upper(); break
            if not prov2:
                _city = CITY_PROV.search(unicodedata.normalize("NFKD", (x.get("buyer_address") or "") + " | " + (x.get("buyer") or "")).encode("ascii", "ignore").decode().lower())
                prov2 = CITY_TO_PROV[_city.group(1)] if _city else ""
            if not prov2:  # the province named in the address ("NS, CA") or in the body's own name ("Efficiency Manitoba", "NLSchools (Newfoundland and Labrador …)")
                _pa = re.search(r"\b(QC|ON|BC|AB|SK|MB|NS|NB|NL|PE|YT|NT|NU)\b(?=[,\s)]|$)", x.get("buyer_address") or "")
                _pn = PROV_NAME.search(unicodedata.normalize("NFKD", (x.get("buyer") or "") + " | " + (x.get("buyer_legal_name_as_published") or "") + " | " + (x.get("buyer_address") or "")).encode("ascii", "ignore").decode().lower())
                prov2 = _pa.group(1) if _pa else (PROV_NAMES[_pn.group(1)] if _pn else "")
            bt2 = (x.get("buyer_type") or "").lower()
            fed2 = (x.get("jurisdiction") or "") == "FED" or bool(re.search(r"\.gc\.ca|canada\.ca", (x.get("buyer_website") or "")))
            if fed2 and not prov2:
                x["buyer_tax_status_derived"] = "DERIVED: federal body — the Government of Canada pays GST/HST on its purchases (since 1991-04-01; federal departments, agencies and Crown corporations); charge the rate of the province where the supply is made (place-of-supply rules), 5 % GST where no HST applies"
            if not fed2 and prov2 and ("ministry" in bt2 or "crown" in bt2 or re.search(r"\bgovernment\b", bt2)) and not re.search(r"municipal|school|hospital|university|college|transit|utility", bt2):
                if prov2 in ("MB", "SK", "AB", "NT", "YT"):
                    x["buyer_tax_status_derived"] = TAX_POINT_RELIEF % {"MB": "Manitoba", "SK": "Saskatchewan", "AB": "Alberta", "NT": "the Northwest Territories", "YT": "Yukon"}[prov2]
                elif prov2 in ("ON", "NB", "NL", "NS", "PE", "QC", "BC", "NU"):
                    x["buyer_tax_status_derived"] = TAX_PAY_REBATE
            elif "municipal" in bt2 and prov2:
                x["buyer_tax_status_derived"] = TAX_MUNICIPAL
            elif re.search(r"first nation|indigenous government|band council|conseil de bande", bt2) and prov2:  # pilot dossier S1-02 (2026-11-09): band councils are relieved, not "taxable presumed"
                x["buyer_tax_status_derived"] = ("DERIVED: Indian band / band-empowered entity — GST/HST relief under CRA Technical Information Bulletin B-039 (goods delivered to a reserve; services acquired for "
                                                 "band management activities or for real property on reserve, on or off reserve) when the band certifies the purchase; otherwise charge the %s place-of-supply rate; "
                                                 "ask the band's finance office for its certificate wording before the first invoice (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/b-039.html)" % prov2)
            elif prov2:  # every other Canadian purchaser (university, hospital, school board, company, non-profit): taxable supply at the place-of-supply rate; any PSB rebate is the buyer's own claim
                x["buyer_tax_status_derived"] = "DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of %s on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs" % prov2
            if prov2 in TAX_RATE:
                x["tax_rate_indicative_derived"] = TAX_RATE[prov2] + TAX_RATE_NOTE
            elif prov2 in ("QC", "BC", "AB", "SK", "MB", "YT", "NT", "NU"):
                x["tax_rate_indicative_derived"] = "GST 5%% (%s)" % prov2 + TAX_RATE_NOTE
            if x["buyer_tax_status_derived"] or x["tax_rate_indicative_derived"]:
                npk["tax_derived"] += 1
            if not _val("currency") and (prov2 or fed2 or (x.get("jurisdiction") or "") == "CA" or (x.get("buyer_website") or "").lower().rstrip("/").endswith(".ca")):
                x["invoice_currency_derived"] = "CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)"
                npk["invoice_currency_derived"] += 1
        else:  # buyer outside Canada: exported supply, local tax is the buyer's; currency from the buyer's country
            _cc = _cc0
            if _cc:
                x["buyer_tax_status_derived"] = "DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); %s" % {"US": "US state sales / use tax is self-assessed by the buyer", "GB": "UK VAT is accounted for by the buyer under the reverse charge where applicable", "AU": "Australian GST is accounted for by the buyer where applicable", "EU": "EU VAT is accounted for by the buyer under the reverse charge where applicable"}[_cc]
                if not _val("currency"):
                    x["invoice_currency_derived"] = {"US": "USD", "GB": "GBP", "AU": "AUD", "EU": "EUR"}[_cc] + " (derived from the buyer's country; CAD if the parties agreed so)"
                    npk["invoice_currency_derived"] += 1
                npk["tax_derived_foreign"] += 1
        card = {
            "bill_to": {"legal_name": _val("buyer_legal_name_as_published") or _val("buyer"), "legal_name_is_published": bool(_val("buyer_legal_name_as_published")), "trade_name": _val("buyer_trade_name_as_published"), "address": _val("invoice_mailing_address") or _val("buyer_address"),
                        "address_is_the_invoice_address": bool(_val("invoice_mailing_address")), "tax_number": _val("buyer_bn_as_published"), "language": _val("template_language") or _val("language_hint")},
            "submit_to": {"email": _val("email"), "email_type": _val("email_type"), "supplier_setup_url": (x.get("supplier_setup_url") or "").split(" (")[0], "portal_url": _val("invoice_portal_url"), "portal_kind": _val("invoice_portal_kind"), "mailing_address": _val("invoice_mailing_address"),
                          "format": (fmt.group(1).strip() if fmt else ""), "system": _val("ap_system_hint"), "e_invoicing_peppol": _val("peppol_participant_id")},
            "references_required": {"po_required": _val("po_required_as_published"), "po_number": _val("po_number_as_published"), "contract_or_agreement_number": _val("contract_or_agreement_number"),
                                    "vendor_id_with_buyer": _val("buyer_vendor_id"), "reference_hint": _val("invoice_reference_hint")},
            "terms": {"payment_terms": _val("payment_terms_as_published") or _val("payment_terms_default_policy"), "payment_method": _val("buyer_payment_method_preference"), "payment_cycle": _val("buyer_ap_cycle_published"), "e_signature": _val("buyer_esignature_preference")},
            "tax": {"buyer_tax_status": _val("buyer_tax_exempt_status") or (("DERIVED: " + x["buyer_tax_status_derived"][:160]) if x.get("buyer_tax_status_derived") else ""), "buyer_tax_status_is_published": bool(_val("buyer_tax_exempt_status")), "indicative_rate": (x.get("tax_rate_indicative_derived") or "").split(" — ")[0], "currency": _val("currency") or (("DERIVED: " + x["invoice_currency_derived"][:40]) if x.get("invoice_currency_derived") else ""), "currency_is_published": bool(_val("currency")), "vendor_gst_hst": _val("vendor_gst_hst_derived"), "vendor_qst": _val("vendor_qst_as_published")},
            "vendor_identity": {"legal_name": _val("vendor_legal_name") or _val("vendor"), "bn9": _val("vendor_bn9"), "neq": _val("vendor_neq"), "remit_address": _val("vendor_registered_address") or _val("vendor_address")},
            "follow_up": {"ap_phone": _val("ap_phone") or _val("buyer_phone"), "ap_contact": _val("ap_contact_name_as_published"), "requirements_text": (x.get("invoicing_requirements") or "")[:300]},
        }
        _pk = x.get("invoice_portal_kind") or ""
        _pn = (x.get("invoice_portal_url") or "") + ("" if _pk.startswith(("actionable", "other page")) else " " + _pk)  # the generic kind text says "invoice" for every portal: judge the name / URL only
        card["submit_to"]["portal_is_invoice_channel"] = bool(_pn.strip()) and not TENDER_PORTAL.search(_pn) and bool(EINVOICE_PORTAL.search(_pn))
        card["submit_to"]["portal_class"] = "" if not _pn.strip() else "e-invoicing portal" if card["submit_to"]["portal_is_invoice_channel"] else "tender portal (not an invoice channel)" if TENDER_PORTAL.search(_pn) else "portal (not confirmed as an invoice channel)"
        x["invoice_card_json"] = json.dumps(card, ensure_ascii=False) if x.get("email") else ""
        elements = [("bill-to legal name (published)", card["bill_to"]["legal_name_is_published"]), ("bill-to address", bool(card["bill_to"]["address"])), ("submission channel (mailbox or portal)", bool(card["submit_to"]["email"] or card["submit_to"]["portal_url"])),
                    ("PO rule", bool(card["references_required"]["po_required"])), ("reference to quote (PO / contract / vendor id)", bool(card["references_required"]["po_number"] or card["references_required"]["contract_or_agreement_number"] or card["references_required"]["vendor_id_with_buyer"])),
                    ("payment terms", bool(card["terms"]["payment_terms"])), ("currency", bool(card["tax"]["currency"])), ("buyer tax status", bool(card["tax"]["buyer_tax_status"])), ("vendor GST/HST number", bool(card["tax"]["vendor_gst_hst"])),
                    ("vendor legal name", bool(_val("vendor_legal_name"))), ("AP phone or contact for follow-up", bool(card["follow_up"]["ap_phone"] or card["follow_up"]["ap_contact"]))]
        have = [n for n, ok in elements if ok]; miss = [n for n, ok in elements if not ok]
        x["invoice_readiness"] = "%d/%d invoice elements present" % (len(have), len(elements)) if x.get("email") else ""
        x["invoice_missing"] = "; ".join(miss) if x.get("email") else ""
        # owner 2026-11-08 11:24 EST ("add AP grade … how stringent, max"): the row's accounts-payable data graded A–E on what an invoice needs
        # and on plausibility signals that the channel is real and current. Mechanical: every criterion is a column already carrying its source.
        if x.get("email"):
            et, ec = (x.get("email_type") or ""), (x.get("email_check") or "")
            bw_reg = registrable(host_of(x.get("buyer_website") or "")) if x.get("buyer_website") else ""
            own_domain = bool(bw_reg) and (bw_reg == registrable((x.get("email") or "").split("@")[-1].lower())
                                           or bw_reg == registrable(host_of(x.get("email_evidence_url") or "")))  # the buyer's second domain (uleth.ca / ulethbridge.ca, vdmt.ca / villedemont-tremblant.qc.ca, ec.gc.ca / canada.ca) counts when the buyer's own site publishes the mailbox
            mx_ok = (x.get("email_deliverability") or "").startswith("domain publishes a mail server")
            crit = [
                ("invoicing / AP mailbox", et.startswith(("invoic", "accounts_payable", "supplier_payment", "ap")), 20),
                ("finance mailbox", et.startswith("finance") and not et.startswith(("invoic", "accounts_payable")), 10),
                ("referee-confirmed mailbox", ec.startswith("confirmed"), 15),
                ("mailbox seen again within 60 days", (x.get("reverify_due") or "") == "no" or (x.get("mailbox_recheck_note") or "").startswith("mailbox seen again"), 8),
                ("mailbox on the buyer's own domain (or published on the buyer's own site)", own_domain, 7),
                ("domain publishes a mail server (MX)", mx_ok, 5),
                ("bill-to legal name published", card["bill_to"]["legal_name_is_published"], 8),
                ("invoice or billing address", bool(card["bill_to"]["address"]), 6),
                ("PO rule published", bool(card["references_required"]["po_required"]), 6),
                ("payment terms published", bool(_val("payment_terms_as_published")), 6),
                ("currency known", bool(card["tax"]["currency"]), 2),
                ("invoice format / requirements published", bool(card["submit_to"]["format"] or _val("invoicing_requirements")), 3),
                ("AP phone or AP contact", bool(_val("ap_phone") or card["follow_up"]["ap_contact"]), 2),
                ("payment cycle or method published (plausibility)", bool(card["terms"]["payment_cycle"] or card["terms"]["payment_method"]), 2),
            ]
            penalties = []
            notes = []
            if (x.get("email_security_posture") or "").startswith("EXPOSED"):
                notes.append("buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)")  # owner 2026-11-08 19:11 EST: the grade measures the invoice data; the buyer's DNS posture is reported, it is not the vendor's invoice gap (it blocked A on 269 Gold rows)
            if x.get("buyer_bn_note"):
                penalties.append(("BN conflict between sources", 2))
            if (x.get("vendor_registry_warning") or ""):
                penalties.append(("vendor registry warning", 2))
            score = sum(w for _, ok, w in crit if ok) - sum(w for _, w in penalties)
            score = max(0, min(100, score))
            ap_mail = crit[0][1]; confirmed = crit[2][1]
            if confirmed and ap_mail and crit[6][1] and crit[7][1] and crit[8][1] and crit[9][1] and crit[4][1] and crit[5][1] and not penalties:
                apg = "A"
            elif confirmed and (ap_mail or crit[1][1]) and crit[6][1] and crit[7][1] and (crit[8][1] or crit[9][1]):
                apg = "B"
            elif confirmed and (ap_mail or crit[1][1] or crit[6][1] or crit[7][1]):
                apg = "C"
            elif confirmed:
                apg = "D"
            else:
                apg = "E"
            x["ap_grade"] = apg  # apg, not g: g is the mailbox grade 1-4 used by data_quality_score / ship_ready below (local test 16:40Z: TypeError str < int skipped the whole pack)
            x["ap_score"] = str(score)
            x["ap_grade_basis"] = "met: %s | missing: %s%s%s" % ("; ".join(n_ for n_, ok, _ in crit if ok) or "none", "; ".join(n_ for n_, ok, _ in crit if not ok) or "none", (" | notes: " + "; ".join(notes)) if notes else "", (" | penalties: " + "; ".join(n_ for n_, _ in penalties)) if penalties else "")
            a_need = [n_ for k_, n_ in ((2, "referee confirmation of the mailbox"), (0, "an invoicing / AP mailbox (not finance / procurement / general)"), (4, "a mailbox on the buyer's own domain or published on its own site"), (5, "MX record for the mailbox domain"), (6, "published bill-to legal name"), (7, "invoice / billing address"), (8, "published PO rule"), (9, "published payment terms")) if not crit[k_][1]]
            a_need += ["clear the penalty: " + n_ for n_, _ in penalties]
            x["ap_gap_to_A"] = "; ".join(a_need) if apg != "A" else "none"
            # AP payability (owner 2026-11-08 14:53 EST: weigh the fields the way an AP team pays, not equally): an invoice is paid when it REACHES the right
            # inbox / portal, is addressed to the right legal entity, carries the reference the buyer insists on, and is taxed right; terms, phone and
            # cycle only change when and how — the PO number itself is handed to the vendor by the buyer and is not a public datum
            chan = confirmed and (ap_mail or crit[1][1])
            billto = card["bill_to"]["legal_name_is_published"] and bool(card["bill_to"]["address"])
            po_known = bool(card["references_required"]["po_required"]) or bool(_val("po_number_as_published")) or bool(_val("contract_or_agreement_number"))
            tax_known = bool(card["tax"]["buyer_tax_status"]) or bool(x.get("tax_rate_indicative_derived"))
            setup_known = bool(x.get("supplier_setup_url")) or bool(card["submit_to"]["portal_url"]) or "registr" in (x.get("invoicing_requirements") or "").lower()
            need = [n_ for ok_, n_ in ((chan, "a confirmed invoicing / AP or finance channel"), (billto, "bill-to legal name and address"), (po_known, "the buyer's PO / reference rule"), (tax_known, "tax treatment"))
                    if not ok_]
            x["ap_payability"] = ("payable today: channel + bill-to + reference rule + tax treatment%s%s" % ("; supplier setup known" if setup_known else "; supplier setup form not found (first payment may need it)", "; terms published" if crit[9][1] else "; terms not published (buyer's default applies)")) if not need else "not yet payable — missing: " + "; ".join(need)
            # pay on sight (owner 2026-11-08 19:55 EST: "you see the invoice, boom, it's paid"): could an invoice be generated from this row and clear AP matching?
            # channel tier 1 = confirmed invoicing / AP mailbox or invoice portal, 2 = confirmed finance mailbox, 3 = confirmed purchasing / general mailbox (routed internally), 0 = unconfirmed
            _portal_ok = card["submit_to"]["portal_is_invoice_channel"]
            tier = 1 if (confirmed and ap_mail) or _portal_ok else 2 if confirmed and crit[1][1] else 3 if confirmed else 0
            x["channel_tier"] = str(tier)
            v_legal = _val("vendor_legal_name") or re.sub(r"^inferred:\s*", "", _val("vendor"))  # an inferred relationship's vendor (Canada Post Corporation, BC Hydro) is a certain identity; only the relationship is inferred
            v_gst = _val("vendor_bn9")
            v_addr = _val("vendor_address") or _val("vendor_registered_address")
            tax_any = bool(card["tax"]["buyer_tax_status"]) or bool(x.get("tax_rate_indicative_derived")) or bool(x.get("buyer_tax_status_derived"))
            cur_any = bool(card["tax"]["currency"]) or bool(x.get("invoice_currency_derived"))
            _public = bool(re.search(r"municipal|government|ministry|agency|utility|public corporat|crown|school|scolaire|health|hospital|universit|college|c[ée]gep|transit|library|police|first nation|band council", (x.get("buyer_type") or "").lower()))
            billto_pos = bool(card["bill_to"]["address"]) and (card["bill_to"]["legal_name_is_published"] or bool(card["bill_to"]["trade_name"]) or (_public and bool(_val("buyer")) and not DOMAIN_NAME.match(_val("buyer")) and not GENERIC_NAME.match(_val("buyer"))))  # a public body bills under the name it publishes itself (Ville de Laval, City of Kelowna); any organisation may be billed under the name it does business under (SOR/91-45 s. 3(c)(i))
            pos_need = [n_ for ok_, n_ in ((tier in (1, 2), "a confirmed invoicing / AP or finance channel" if tier != 3 else "an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)"),
                                           (billto_pos, "bill-to legal name and address" if not card["bill_to"]["address"] else "bill-to legal name"), (bool(v_legal), "the vendor's legal name"), (bool(v_gst), "the vendor's GST/HST number (BN9)"), (bool(v_addr), "the vendor's remit-to address"),
                                           (tax_any, "tax treatment"), (cur_any, "currency")) if not ok_]
            if not pos_need:
                x["pay_on_sight"] = "yes" if po_known else "yes — reference rule not published (quote the buyer's PO / order number when one is issued)"
            elif tier == 3 and all(ok_ for ok_ in (billto_pos, bool(v_legal), bool(v_gst), bool(v_addr), tax_any, cur_any)):
                x["pay_on_sight"] = "routed — complete invoice, but only a purchasing / general inbox is confirmed"
            else:
                x["pay_on_sight"] = "no"
            x["pay_on_sight_missing"] = "; ".join(pos_need + ([] if po_known else ["(reference rule not published)"]))
            npk["pay_on_sight_" + x["pay_on_sight"].split(" ")[0]] += 1
            _terms = _val("payment_terms_as_published") or (x.get("payment_terms_default_policy") or "").split(" (")[0] or "vendor's standard terms (buyer publishes none)"
            _ref = "; ".join(t_ for t_ in (("PO " + _val("po_number_as_published")) if _val("po_number_as_published") else "", ("contract " + _val("contract_or_agreement_number").split(";")[0]) if _val("contract_or_agreement_number") else "", ("tender " + _val("solicitation_or_tender_number").split(";")[0]) if _val("solicitation_or_tender_number") else "") if t_)
            _lines = ["DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)",
                      "BILL TO: %s%s" % ((card["bill_to"]["legal_name"] if card["bill_to"]["legal_name_is_published"] or not card["bill_to"]["trade_name"] else card["bill_to"]["trade_name"].split(" (the name on")[0] + " (name it does business under, from its own site)") or "(legal name not published)",
                                         (" — " + card["bill_to"]["address"]) if card["bill_to"]["address"] else " — (address not published)") + ((" — buyer tax no. " + card["bill_to"]["tax_number"]) if card["bill_to"]["tax_number"] else ""),
                      "SUBMIT TO: %s%s%s%s" % (_val("email") or "(no mailbox)", " (%s mailbox, %s)" % (_val("email_type") or "type unknown", "confirmed by the referee" if confirmed else "not yet confirmed"), ((" | invoice portal: " if _portal_ok else " | " + card["submit_to"]["portal_class"] + ": ") + card["submit_to"]["portal_url"]) if card["submit_to"]["portal_url"] else "", (" | format: " + card["submit_to"]["format"]) if card["submit_to"]["format"] else ""),
                      "REFERENCE: %s%s" % (_ref or "none in the record", (" | PO rule: " + card["references_required"]["po_required"].split(" (as printed")[0][:120]) if card["references_required"]["po_required"] else " | PO rule: not published"),
                      "FROM / REMIT TO: %s%s%s%s" % (v_legal or "(vendor legal name not confirmed)", (" — " + v_addr) if v_addr else " — (remit-to address not published)", (" | GST/HST %sRT0001 (account derived from the BN9)" % v_gst) if v_gst else " | GST/HST number not public", (" | NEQ " + _val("vendor_neq").split(" ")[0]) if _val("vendor_neq") else ""),
                      "TAX: %s | CURRENCY: %s | TERMS: %s" % (re.sub(r"^(?:DERIVED: )+", "DERIVED: ", (card["tax"]["buyer_tax_status"] or x.get("buyer_tax_status_derived") or x.get("tax_rate_indicative_derived") or "treatment unknown"))[:160], (card["tax"]["currency"] or (x.get("invoice_currency_derived") or "").split(" (")[0] or "unknown"), _terms[:100]),
                      "DESCRIPTION: %s%s" % ((_val("contract_title") or _val("contract_description") or _val("relationship_detail") or "(no contract text)")[:140], (" | AMOUNT: %s %s" % (_money(_val("contract_value")), (card["tax"]["currency"] or x.get("invoice_currency_derived") or "").split(" (")[0].replace("DERIVED: ", ""))) if _val("contract_value") else "")]
            x["invoice_text"] = "\n".join(_lines)[:1500]
            npk["ap_payable_today"] += not need
        x["facts_provenance_json"] = json.dumps({"mailbox": [p.strip() for p in (x.get("mailbox_provenance") or "").split(" | ") if p.strip()], "buyer_facts": [p.strip() for p in (x.get("buyer_facts_provenance") or "").split("; ") if p.strip()],
                                                 "vendor_facts": [p.strip() for p in (x.get("vendor_facts_provenance") or "").split("; ") if p.strip()], "relationship": x.get("how_relationship_was_found") or ""}, ensure_ascii=False)[:4000]
        # quality score / ship_ready (S2)
        mq = {4: 40, 3: 30, 2: 20, 1: 12}.get(g, 0) if ec.startswith(("confirmed", "cross")) else (5 if x.get("email") else 0)
        rq = {"A": 30, "B": 30, "T": 26, "M": 22, "L": 18, "C": 14, "D": 14, "F": 12, "R": 11, "E": 10, "I": 6}.get(t, 0)
        fq = 30 * sum(1 for c in KEY_FIELDS if x.get(c)) / len(KEY_FIELDS)
        x["data_quality_score"] = str(int(round(mq + rq + fq)))
        # The owner's test of a row (2026-11-11: 12:31, 13:00, 13:09, 13:58 and 14:20 EST). Until then this column answered the first goal's question —
        # is the mailbox an invoicing / AP one, re-read by the referee, on one of four tiers — and said "no" on 97 of his 100 test rows, 87 of them
        # because the mailbox is a general one ("the old thing is moronic": the general mailbox is where they take things in, and that is fine).
        # That answer is kept under its own name (ap_mailbox_ready: no column is deleted). ship_ready is his test, made by ONE function for this
        # table and for tools/relationship_rows.py (owner_test): the relationship is established and current; the organisation's role mailbox
        # was re-read by the referee; the bill is paid on invoice and bank transfer is a published or inherent way to pay it — never a card on
        # file; the fields of its KIND of relationship are filled ("as populated as that relationship could expect it to be"); nothing flags it.
        x["ap_mailbox_ready"] = ("yes" if (g == 4 and ec.startswith(("confirmed", "cross")) and t in ("A", "B", "T", "M") and x["sensitivity_flag"] == "no" and not x.get("vendor_registry_warning"))
                           else "yes (finance mailbox, not AP)" if (g == 3 and ec.startswith(("confirmed", "cross")) and t in ("A", "B", "T", "M") and x["sensitivity_flag"] == "no")
                           else "no (%s)" % ("sensitive buyer" if x["sensitivity_flag"] == "yes" else "vendor registry warning" if x.get("vendor_registry_warning") else "mailbox not referee-confirmed" if not ec.startswith(("confirmed", "cross")) else "mailbox below finance grade" if g < 3 else "relationship not dated / active"))
        npk["ap_mailbox_ready_yes"] += x["ap_mailbox_ready"] == "yes"
        if (x.get("relationship_fact_basis") or "").startswith("by where it is"):
            x["vendor"] = re.sub(r"^inferred:\s*", "", x.get("vendor") or "")  # the distributor of the address is certain: only the account holder is not published
        if (x.get("source") or "").lower().startswith("auditor of record") and str(x.get("contract_value") or "").strip() \
                and not re.search(r"audit|v[ée]rification|honoraires|remuneration of (?:the )?auditor", str(x.get("contract_value") or ""), re.I):
            # 2026-11-13 (owner 13:23 EST: "everything accurate no errors"): an auditor of record's row had taken a figure of the statements or of the
            # Financial Information Return for the contract's value (City of Kamloops 17,265,535; Township of Brudenell 25,751,298 — a total, not the
            # audit fee): only a value whose quote names the audit fee is kept
            x["contract_value"] = ""; x["contract_value_from_pair"] = ""
            n_x2["auditor of record: a figure of the statements not taken for the audit fee"] += 1
        _k9, _r9, _o9 = _RR.owner_test(x)
        n_ship[(_k9, x["payment_route"], "yes" if not _o9 else "no")] += 1
        if not _o9:
            _sr9 = x["ship_ready"]
            n_ship_level["by where the organisation is (its electricity distributor)" if "by where the organisation is" in _sr9 else
                         "every field of its kind, in the biller's or the record's own words" if _sr9 in ("yes", "yes (the amount is calculated and labelled so)") else
                         "best effort: by the kind of relationship, or a field of its kind not published"] += 1
        n_mark[((x.get("amount_mark") or "5 no amount").split(" (")[0], "yes" if not _o9 else "no")] += 1
        if not _o9:
            _am9 = any(str(x.get(_c) or "").strip() for _c in ("bill_amount_indicative", "contract_value", "bill_amount_calculated"))
            _pe9 = (x.get("recurring_billing") or "")[:1] in ("1", "2", "3", "4")
            n_fill["ship ready"] += 1
            n_fill["with an amount (published or calculated) and a billing period"] += _am9 and _pe9
            n_fill["with amount, period, biller legal name and number, what is billed, how the bill arrives, how it is paid, due terms"] += bool(
                _am9 and _pe9 and all(any(str(x.get(_c) or "").strip() for _c in _cs) for _cs in (("vendor_legal_name",), ("vendor_tax_or_registration_number",), ("bill_items_as_published", "contract_title"),
                                                                                             ("bill_delivery_as_published",), ("bill_payment_method_as_published",), ("bill_due_terms_as_published", "payment_terms_as_published"))))
        for _p9 in _o9:
            n_ship_miss[_p9.split(" (")[0]] += 1
        if len(_o9) == 1:
            n_ship_one[(_k9, _o9[0].split(" (")[0])] += 1
        # statutory payees (downstream list 2 §10): legally mandated payers, one labelled column, never a row or a mailbox
        pc = re.search(r"\b([A-Z])\d[A-Z]\s?\d[A-Z]\d\b", x.get("buyer_address") or "")
        prov = {"QC": "QC", "ON": "ON", "BC": "BC", "AB": "AB", "SK": "SK", "MB": "MB", "NS": "NS", "NB": "NB", "NL": "NL", "PE": "PE", "YT": "YT", "NT": "NT", "NU": "NU"}.get(x.get("jurisdiction") or "", "")
        if not prov and pc:
            prov = {"G": "QC", "H": "QC", "J": "QC", "K": "ON", "L": "ON", "M": "ON", "N": "ON", "P": "ON", "V": "BC", "T": "AB", "S": "SK", "R": "MB", "B": "NS", "E": "NB", "A": "NL", "C": "PE", "Y": "YT", "X": "NT"}.get(pc.group(1), "")
        if not prov:
            md2 = re.search(r"\.(qc|on|bc|ab|sk|mb|ns|nb|nl|pe|yk|nt|nu)\.ca(?:/|$)", (x.get("buyer_website") or "").lower())
            prov = md2.group(1).upper().replace("YK", "YT") if md2 else ""
        bt = x.get("buyer_type") or ""
        public = bool(re.search(r"municipal|ministry|agency|school|hospital|health|university|college|utility|transit|transport|First Nation|US government", bt))
        company = "company" in bt
        board = {"QC": ("CNESST", "LATMP s. 280: every Québec employer must register"), "ON": ("WSIB", "Workplace Safety and Insurance Act: Schedule 1 / Schedule 2 employers (public bodies are Schedule 2; some private industries are not mandatory)"),
                 "BC": ("WorkSafeBC", "Workers Compensation Act: employers with workers must register"), "AB": ("WCB-Alberta", "Workers' Compensation Act: mandatory except exempt industries"), "SK": ("Saskatchewan WCB", "Workers' Compensation Act"),
                 "MB": ("WCB Manitoba", "Workers Compensation Act"), "NS": ("WCB Nova Scotia", "Workers' Compensation Act"), "NB": ("WorkSafeNB", "Workers' Compensation Act"), "NL": ("WorkplaceNL", "Workplace Health, Safety and Compensation Act"),
                 "PE": ("WCB PEI", "Workers Compensation Act"), "YT": ("Yukon WCHSB", "Workers' Safety and Compensation Act"), "NT": ("WSCC", "Workers' Compensation Act (NT/NU)"), "NU": ("WSCC", "Workers' Compensation Act (NT/NU)")}.get(prov)
        sp_ = []
        if board and (public or company or "non-profit" in bt or "religious" in bt or "library" in bt) and (x.get("jurisdiction") or "") != "FED":
            conf = "HIGH" if (prov == "QC" or public) else "MEDIUM (private employer: coverage depends on the industry schedule)"
            sp_.append("%s — employer premiums (%s) — %s" % (board[0], board[1], conf))
        if prov == "QC" and (company or "non-profit" in bt):
            sp_.append("Registraire des entreprises du Québec — annual registration fee (Act respecting the legal publicity of enterprises) — HIGH for registered enterprises")
        if prov == "QC" and (public or company or "non-profit" in bt):
            sp_.append("Revenu Québec — source deductions / QST remittances — HIGH for employers")
        x["statutory_payees_inferred"] = ("; ".join(sp_) + " | inferred from jurisdiction and organisation type; not a supplier contract; no mailbox attached") if sp_ else ("none inferred (province not identified)" if not prov else "none inferred for this organisation type")
        # vendor years in business (mechanical)
        vi = x.get("vendor_incorporation_date") or ""
        if re.match(r"^\d{4}-\d{2}-\d{2}$", vi):
            try:
                x["vendor_years_in_business"] = "%.1f (since %s, registry date)" % ((_today - datetime.date.fromisoformat(vi)).days / 365.25, vi)
            except ValueError:
                pass
        # DNS transport / brand records (dmarc_check: MTA-STS, TLS-RPT, BIMI)
        dd = DM.get((x.get("email") or "").lower().split("@")[-1]) if x.get("email") else None
        if dd is not None:
            for k, lab in (("mta_sts", "MTA-STS"), ("tls_rpt", "TLS-RPT"), ("bimi", "BIMI")):
                v = dd.get(k) or ""
                x[k] = "not checked yet" if not v else ("no %s record" % lab if v == "none" else "yes (%s)" % v[:80])
    except Exception as _e:
        npk["rows where the pack failed"] += 1
        if npk["rows where the pack failed"] <= 3:
            import traceback; traceback.print_exc(); print("downstream pack failed on row %d:" % _ri, type(_e).__name__, _e)
    _w2.writerow(x)
    if _PLAIN:
        _w1.writerow(x)
    _f3.write(json.dumps({c: x.get(c, "") for c in cols}, ensure_ascii=False) + "\n")
    cnt[x["rank_group"]] += 1; _n_mail += 1 if x["email"] else 0; _n_contract += 1 if x["contract_status"] in TIER else 0
    rows[_ri] = None  # written: the row's memory is free for the next one
    if _ri and _ri % 100000 == 0:
        print("rows written: %d of %d" % (_ri, _n_rows))
_f2.close(); _f3.close()
if _PLAIN:
    _f1.close()
print("narrative columns:", dict(n9))
# owner's bar of 2026-11-11: rows with a mailbox by what is published about the billing period, each tier on its own
_bt = collections.Counter()
for (_c, _t), _n in n_bill.items():
    _bt[_c] += _n
print("recurring billing (owner's bar of 2026-11-11: billed monthly or every three months, systematically, by the vendor) — rows with a mailbox:")
for _c in sorted(_bt):
    print("  %-22s %7d   %s" % (_c, _bt[_c], " · ".join("%s %d" % (_t, n_bill[(_c, _t)]) for _t in sorted({t_ for (c_, t_) in n_bill if c_ == _c}))))
print("  rows that meet the bar as published (1 monthly + 1 quarterly): %d of %d rows with a mailbox | Shopify rows by the store's country: %s"
      % (_bt.get("1 monthly", 0) + _bt.get("1 quarterly", 0), sum(_bt.values()), ", ".join("%s %d" % kv for kv in n_bill_shop.most_common())))
print("  the bill's fields, rows with a mailbox that carry each: %s" % ", ".join("%s %d" % (c_, n_billcol[c_]) for c_ in BILL_COLS))
print("  beside them:", {k_: v_ for k_, v_ in n_billcol.items() if k_ not in BILL_COLS})
_nm_ = max(1, sum(_bt.values()))
print("invoice fields (owner 2026-11-11: every aspect within an invoice) — rows with a mailbox that carry each, of %d: %s" % (_nm_, " · ".join("%s %d (%.0f%%)" % (c_, n_inv[c_], 100.0 * n_inv[c_] / _nm_) for c_ in
      ("buyer legal name", "buyer address", "vendor legal name", "vendor address", "vendor tax number", "what is billed", "amount", "billing period", "reference", "all but the amount", "all nine", "amount, calculated only", "all nine with the amount calculated"))))
# the owner's test (2026-11-11), row by row — one row per buyer, no buyer twice
_sy = sum(n_ for (k_, r_, v_), n_ in n_ship.items() if v_ == "yes")
print("SHIP READY (a Canadian biller with a relationship that is current + the organisation's role mailbox re-read by the referee + a bill on invoice, payable by bank transfer — never a card on file + no flag; "
      "owner 2026-11-11 16:01 EST: the fields are populated as well as they can be): %d of %d rows" % (_sy, sum(n_ship.values())))
print("  of which: %s" % " · ".join("%s %d" % kv for kv in n_ship_level.most_common()))
print("  by amount (owner 20:36 EST: every row marked, $5,000 and more first) — ready / all: %s" % " · ".join("%s: %d / %d" % (m_, n_mark[(m_, "yes")], n_mark[(m_, "yes")] + n_mark[(m_, "no")]) for m_ in sorted({m2 for (m2, _v) in n_mark})))
print("  how full the invoice is, over the ready rows: %s" % " · ".join("%s %d" % kv for kv in n_fill.items()))
print("  by kind and by how the bill is paid (ready / all): %s" % " · ".join("%s — %s: %d / %d" % (k_, r_, n_ship[(k_, r_, "yes")], n_ship[(k_, r_, "yes")] + n_ship[(k_, r_, "no")]) for (k_, r_) in sorted({(k2, r2) for (k2, r2, _v) in n_ship}, key=lambda kr: -(n_ship[(kr[0], kr[1], "yes")] + n_ship[(kr[0], kr[1], "no")]))))
print("  what is missing, over the rows that fail: %s" % " · ".join("%s %d" % kv for kv in n_ship_miss.most_common(20)))
print("  one thing away (kind: what is missing): %s" % " · ".join("%s: %s %d" % (k_, m_, n_) for (k_, m_), n_ in n_ship_one.most_common(16)))
print("  rows by number of the nine fields, tier by tier: %s" % " | ".join("%s: %s" % (t_, " ".join("%d×%d" % (k_, n_inv_t[(t_, k_)]) for k_ in range(9, 2, -1) if n_inv_t[(t_, k_)])) for t_ in sorted({t2 for (t2, _k) in n_inv_t})))
print("downstream pack:", dict(npk))
# the change list against the previous build (tools/release_diff.py) is made by tools/rank_tail.sh once this process has ended: it holds two
# tables' compared cells in memory, and as a child process here it stood next to everything the ranker still holds
print("rows", _n_rows); print(sorted(cnt.items(), key=lambda kv: (kv[0] != "GOLD", kv[0])))
print("with any email:", _n_mail, "| contract buyers:", _n_contract)
