"""One row per distinct buyer, ranked by proof quality and completeness (see README.md). Run from anywhere:
    gh release download dataset-latest -D data/release   # once (needs canadian_vendor_contracts; vendors_enriched, buyers_enriched,
                                                          # vendor_country_unverified_contracts and ended_* are optional: P12 + field fill)
    python3 contrib/claude/rank_buyers/rank.py && python3 contrib/claude/rank_buyers/batches.py
"""
import csv, gzip, json, re, io, collections, unicodedata, datetime, sys, os
import builtins as _bi, time as _tm
_T0 = _TL = _tm.time()
def print(*a, **k):
    """every progress line carries the seconds since the start and since the line before: the row count is meant to grow tenfold, and this
    shows which step stops scaling (2026-11-10: a build took 30+ minutes at 69,000 rows)"""
    global _TL
    _now = _tm.time()
    _bi.print("[%5.0fs +%4.0fs]" % (_now - _T0, _now - _TL), *a, **k)
    _TL = _now


def _money(v):
    """contract_value as it should print on an invoice: 2 decimals, thousands separators (the records carry floats such as 416594.66000000003)"""
    try:
        return "{:,.2f}".format(float(str(v).replace(",", "").replace("$", "").strip()))
    except (TypeError, ValueError):
        return str(v)


ROOT = __import__("os").path.abspath(__import__("os").path.join(__import__("os").path.dirname(__file__), "../../.."))
sys.path.insert(0, ROOT + "/tools"); sys.argv = sys.argv[:1]
import urllib.parse
from ap_crawler import same_org, registrable  # the buyer's own mailbox, not a contractor's or partner's named on its pages
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
def mail_entry(r):
    """(accepted, grade) of one referee mailbox row, or None when rank.py never uses it"""
    r["mailbox"] = re.sub(r"^(?:u003e|u003c|>|<)+", "", (r.get("mailbox") or "").strip(), flags=re.I)  # JSON escape debris glued to the address
    acc = r["check_status"] in ("verified", "cross_verified")
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
_vl = ROOT + "/coord/results/verification_log.csv"
if os.path.exists(_vl):
    for r in csv.DictReader(io.StringIO(open(_vl, encoding="utf-8", errors="replace").read().replace("\0", ""))):
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
print("mailboxes taken from the verification log (better than org_mailboxes' single pick):", n_vl)
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
for v in jl(REL + "vendors_enriched.jsonl.gz"):
    s = v.get("summary") or {}
    reg = s.get("registry_match_level") in ("exact", "strong")  # registry facts only from a confident match
    ra = (s.get("registered_address") or {}) if reg else {}
    ca = next((x["value"] for x in v.get("addresses_in_contract_data") or [] if (x.get("value") or {}).get("line1") or (x.get("value") or {}).get("city")), {})
    bn = s.get("business_number_bn9") if reg else None
    rec = {"name": v.get("name") or "", "legal_name": (s.get("legal_name") or "") if reg else "", "bn9": bn or "",
           "gst": (s.get("gst_hst_account_derived") or (bn + "RT0001" if bn else "")) if reg else "",
           "address": addr_text(ca) or addr_text(ra), "region": region_code(ca) or region_code(ra), "website": s.get("website") or "",
           "emails": "; ".join(e if isinstance(e, str) else (e.get("email") or "") for e in s.get("contact_emails_published") or []),
           "registry": next(({"registry": m.get("registry"), "id": m.get("id"), "legal_name": m.get("legal_name"), "url": m.get("source_url")}
                             for m in s.get("matches") or [] if m.get("match_confidence") in ("exact", "strong")), None) if reg else None,
           "reg_address": addr_text(ra), "reg_region": region_code(ra), "full": {}}
    if reg:  # the full registry records behind the confident matches (REQ: NEQ, trade names, legal form, CAE activity, employees; Corporations Canada: BN, act, directors range; OrgBook: entity type)
        for m in v.get("registry_matches_full") or []:
            if m.get("match_confidence") in ("exact", "strong") and m.get("registry") not in rec["full"]:
                rec["full"][m["registry"]] = m
    VEN[v["vendor_key"]] = rec
    for n in {norm(v.get("name")), norm(rec["legal_name"])} - {""}:
        VEN_NAME[n] = v["vendor_key"] if VEN_NAME.get(n, v["vendor_key"]) == v["vendor_key"] else None  # ambiguous name: no lookup
    if rec["website"]:
        VEN_DOM.setdefault(registrable(host_of(rec["website"])), v["vendor_key"])
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
    full = v.get("full") or {}
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
                       r"unsubscribe|no-?reply|donotreply|^events?$|^news$|alumni|scholarship|bourse|^social$|^marketing$|^comms?$|^communications?$", re.I)
def jur_of_record(r):
    s = (r.get("source") or {}).get("name", "")
    return next((j for rx, j in JUR_SRC if re.search(rx, s)), "")
def jur_of_mail(email):
    d = "." + (email or "").split("@")[-1].lower()
    return next((j for rx, j in JUR_DOM if re.search(rx, d)), "")
orgs = {}
for l in gzip.open(ROOT + "/data/release/canadian_vendor_contracts.jsonl.gz", "rt", encoding="utf-8"):
    r = json.loads(l); be = r.get("buyer_enrichment") or {}
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
    if sc > o["bs"] or (sc == o["bs"] and award_date(r) > award_date(o["best"])):
        o["best"], o["bs"], o["fields"] = r, sc, fields
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
def emailcols(keys, be, gj="", name="", site=""):
    def own(e, page="", quote=""):
        if keys & MTL_KEYS and re.search(r"@(ville\.)?montreal\.(ca|qc\.ca)$", e or "", re.I):  # units of the Ville de Montréal (manual01)
            return True
        if "direct-deposit" in page or "depot-direct" in page:  # PSPC's table maps each federal institution to its mailbox
            return True
        md = (e or "").split("@")[-1].lower()
        if SHARED_GOV.match(md) and not shared_gov_page_names_buyer(e, page, quote, name):
            return False  # another agency's mailbox on the same government domain (spot-check 2026-11-04: tn.gov/correction credited to TDOT)
        if gj and gj != "FED" and jur_of_mail(e) == gj and re.search(r"@(gov\.[a-z]{2}\.ca|gnb\.ca|novascotia\.ca|ontario\.ca)$", e or "", re.I):
            return True  # a provincial government's shared mail domain, for a body of that same government
        if not site and page:  # no known website: the page counts as the buyer's own site only if its domain names the buyer
            h = (urllib.parse.urlparse(page).hostname or "").lower()
            if h and same_org("x@" + registrable(h[4:] if h.startswith("www.") else h), "https://unknown.invalid", name):
                return same_org(e, "https://" + h, name)
        return same_org(e, site or "https://unknown.invalid", name)
    fits = lambda e, page="", quote="": (not gj or jur_of_mail(e) in ("", gj)) and not BAD_LOCAL.search((e or "").split("@")[0]) and own(e, page, quote)
    LABEL = {4: "invoicing/AP", 3: "finance/accounting dept or supplier-payment office", 2: "purchasing", 1: "general"}
    opts = []  # (accepted, grade, row) from the referee's mailboxes and from earlier enrichment; the best accepted one wins
    for k in sorted(k for k in keys if k):  # sorted: equal mailboxes are broken the same way on every run (a set's order is random)
        if k in mail and fits(mail[k][1]["mailbox"], mail[k][1].get("evidence_url") or "", mail[k][1].get("evidence_quote") or ""):
            (acc, g), m = mail[k]
            opts.append(((acc, g), (m["mailbox"], LABEL[g], "confirmed" if acc else m["check_status"], m["evidence_url"], m["evidence_quote"], g, acc)))
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
    em, et, es, eu, eq, g, acc = emailcols(o["keys"], be, gj, o["name"], be.get("official_website") or "")
    tier = tier_of(r)
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
# 4. buyers proven by payment / subaward records or client listings (no contract in the dataset)
leads = {r["buyer_key"]: r for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_buyer_leads.csv", encoding="utf-8", errors="replace"))}
# 2026-11-10: the cloud row factory (tools/cc_clients.py: client pages of .ca vendors read from the Common Crawl archive, vendor's Canadian postal
# address quoted) writes its own file, so the Mac's bridge (which rewrites claude_buyer_leads.csv whole) can never drop a cloud lead
_n_cc = 0
if os.path.exists(ROOT + "/data/incoming/claude/claude_buyer_leads_cc.csv"):
    for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_buyer_leads_cc.csv", encoding="utf-8", errors="replace")):
        if r.get("buyer_key") and r["buyer_key"] not in leads:
            leads[r["buyer_key"]] = r
            _n_cc += 1
# 2026-11-10: tenant leads accepted by the candidate crawl (stores on Shopify, customer portals) arrive in append-only shards (tenant_state/)
_n_ts = 0
for _p in sorted(_g0.glob(ROOT + "/data/incoming/claude/tenant_state/leads_*.gz")) + sorted(_g0.glob(ROOT + "/data/incoming/claude/lead_shards/leads_*.gz")):  # lead_shards/: any engine's leads (BBB accredited businesses …)
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
LDET = {}  # owner 2026-11-03 ("every field"): the lead's own record details (amount, currency, identifiers, dates, vendor address, title)
for _ldp in ("claude_lead_details.jsonl.gz", "claude_lead_details_cc.jsonl.gz"):
    if os.path.exists(ROOT + "/data/incoming/claude/" + _ldp):
        for _d in jl(ROOT + "/data/incoming/claude/" + _ldp):
            LDET.setdefault(_d.get("key"), _d)
for _p in sorted(_g0.glob(ROOT + "/data/incoming/claude/tenant_state/details_*.gz")) + sorted(_g0.glob(ROOT + "/data/incoming/claude/lead_shards/details_*.gz")):
    for _d in jl(_p):
        LDET.setdefault(_d.get("key"), _d)
LFACTS = {}  # 2026-11-10: what the cloud mailbox crawl read on the buyer's OWN pages (tools/lead_crawl.py): its name and its postal address, quoted
LFACTS_DOM = {}  # the same facts by website domain: a row made under another key of the same site (a registry lead, a credit lead) uses them too
from ap_crawler import address_from as _addr_from
for _d in jl(ROOT + "/data/incoming/claude/claude_lead_site_facts.jsonl.gz"):
    if _d.get("key"):
        if _d.get("address_quote"):  # the address is cut out of the quote again with today's rule (a telephone number or a year in front of it was taken for the street number)
            _d["address"] = _addr_from(_d["address_quote"]) or _d.get("address") or ""
        LFACTS[_d["key"]] = _d
        _fd = registrable(host_of(_d.get("site") or ""))
        if _fd and (_fd not in LFACTS_DOM or (_d.get("site_name") and not LFACTS_DOM[_fd].get("site_name")) or (_d.get("address") and not LFACTS_DOM[_fd].get("address"))):
            LFACTS_DOM[_fd] = dict(LFACTS_DOM.get(_fd) or {}, **{k_: v_ for k_, v_ in _d.items() if v_})
n_lf = collections.Counter()
def apply_details(x, k):
    f = LFACTS.get(k) or LFACTS_DOM.get(registrable(host_of(x.get("buyer_website") or "")))
    if f:
        if f.get("site_name") and re.fullmatch(r"(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}", (x.get("buyer") or "").lower()):
            x["buyer"] = f["site_name"]; n_lf["buyer_name_from_own_home_page"] += 1  # the lead only carried the domain; the organisation's own home page names it
        if f.get("address") and not x.get("buyer_address"):
            x["buyer_address"] = "%s (as printed on %s, read %s)" % (f["address"], f.get("address_url") or x.get("buyer_website") or "", f.get("date") or ""); n_lf["buyer_address_from_own_page"] += 1
    d = LDET.get(k)
    if not d:
        return
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
        x["buyer_address"] = "%s (as printed in the member directory of %s, %s)" % ((d["member_address_quote"][_m.start():] if _m else d["member_address_quote"]).strip()[:160], d.get("vendor") or "the body", d.get("record_url") or "")
        n_lf["buyer_address_from_member_directory"] += 1
    for col, key in (("contract_value", "value"), ("currency", "currency"), ("contract_reference", "reference"), ("start_date", "start"),
                     ("end_date", "end"), ("vendor_address", "vendor_address"), ("contract_title", "title")):
        if not x.get(col) and d.get(key):
            x[col] = d[key] if col != "contract_value" or not d.get("value_field") else "%s (source field: %s)" % (d[key], d["value_field"])
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
        leads[_k] = {"buyer_key": _k, "buyer_name": (_mr.get("org_name") or "").strip() or _md, "website": "https://%s/" % _md, "canadian_vendor_rows": "1",
                     "example_vendor": "Canadian Internet Registration Authority (CIRA)", "canada_field_value": CF_REG,
                     "evidence_dataset": "https://dns.google/resolve?name=%s&type=NS" % _md, "latest_record_date": today}
        LDET.setdefault(_k, {"key": _k, "platform": "ca_registry", "title": ".ca domain name registration: %s" % _md, "reference": _md,
                             "vendor_address": "979 Bank Street, Suite 400, Ottawa, Ontario K1S 5K5 (CIRA's notice address in its Registrant Agreement, version 2.2: %s)" % REG_AGREEMENT})
        n_reg += 1
except Exception as _e:
    print("registry leads skipped: %s" % _e)
print("registry leads (.ca domains carrying a confirmed mailbox of their own organisation): %d" % n_reg)
def lead_strength(kl):
    """dated records first, then services seen on the buyer's site, 12-36 month records, client listings, other links:
    the strongest relationship of an organisation claims its website domain (one row per organisation)"""
    cfv, ld = kl[1].get("canada_field_value") or "", (kl[1].get("latest_record_date") or "")[:10]
    if cfv.startswith("registry contract"):
        return 6
    if "vendor located in Canada" in cfv:
        return 4 if re.search(r"\((wall|stories)\)", cfv) else 5
    if "(tech)" in cfv:
        return 1
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
               "txt": "its DNS carries the vendor's verification record %s"}.get(det.get("dns_record_kind") or "", "its DNS records name %s")
        return "active service seen in the buyer's public DNS records (%s): %s — Canada-located provider %s" % (d, how % (det.get("dns_provider_host") or L["example_vendor"]), L["example_vendor"])
    return "active service seen on the buyer's own site (%s): Canada-HQ vendor %s" % (d, L["example_vendor"])
for k, L in sorted(leads.items(), key=lead_strength):
    if norm(L["buyer_name"]) in seen or UNNAMED_VENDOR.search(L.get("example_vendor") or "") or not (L.get("example_vendor") or "").strip(): continue  # a relationship needs a named vendor
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
        pass  # a client logo wall on the vendor's home page, or one of its (undated) customer stories: a client listing by construction
    elif client:  # a link on a Canadian vendor's page: a client listing only on a real client / case-study / references page
        path = urllib.parse.urlparse(L.get("evidence_dataset") or "").path.lower()
        if MEMBER_ONE_PATH.search(path) or (MEMBER_PATH.search(path) and not NOT_MEMBER_PATH.search(path) and len(path.rstrip("/").rsplit("/", 1)[-1]) <= 36 and not (rel_path(path) and not NOT_REL_PATH.search(path))):
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
                            "(normally the organisation itself, sometimes its web agency)" % (registrable(host_of(L.get("website") or "")), today)) if registry else
                           ("member of a Canadian body (stated on the buyer's own site, read %s): %s" % ((L.get("latest_record_date") or "")[:10], L["example_vendor"])) if member and "member badge on the buyer's own site" in L.get("canada_field_value", "") else
                           ("accredited business of a Canadian Better Business Bureau since %s (its BBB profile read %s): %s — accredited businesses pay the BBB dues"
                            % ((LDET.get(k) or {}).get("accredited_since") or "an unstated date", (L.get("latest_record_date") or "")[:10], L["example_vendor"])) if member and "accredited business of the Canadian body" in L.get("canada_field_value", "") else
                           ("member / regulated payer of a Canadian body (current list read %s): %s" % ((L.get("latest_record_date") or "")[:10], L["example_vendor"])) if member else
                           tech_status(k, L) if tech else
                           ("likely active (awarded 12-36 months ago; deal announced by the Canada-based vendor: press release / EDC transaction)" if announced else
                            "likely active (awarded 12-36 months ago; paid in a fiscal year ending 12-36 months ago: IRS Form 990 contractor located in Canada)" if irs else
                            "likely active (awarded 12-36 months ago; record dated 12-36 months ago: %s)" % src) if likely else
                           "linked from a page of the Canada-located vendor's site (not a client page)" if client == "other" else
                           (PAYER_TEXT[payer] if payer else "client listing on the vendor's own site (undated)") if client else
                           ("likely active (customer story published by the Canada-located vendor in the last 12 months)" if story_dated else
                            "likely active (contract announced by the Canada-based vendor in the last 12 months: press release / EDC transaction)"
                            if re.search(r"release dateline|EDC|own news release", L.get("canada_field_value", "")) else
                            "likely active (paid in a fiscal year ending in the last 12 months: IRS Form 990 contractor located in Canada)" if irs else
                            "likely active (record dated in the last 12 months: %s)" % src) if recent else "payment / subaward record",
        "contract_link": L["evidence_dataset"], "vendor": L["example_vendor"], "vendor_country_basis": L["canada_field_value"],
        "contracts_with_canadian_suppliers": L["canadian_vendor_rows"], "keys": k, "buyer_keys": 1, "tier": tier, "grade": g, "acc": acc})
    x, ev, cfv = rows[-1], (L.get("example_vendor") or "").strip(), (L.get("canada_field_value") or "")
    dm = re.search(r"=\s*([a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,})(?:[;/\s]|$)", cfv.lower())
    vdom = ev.lower() if re.fullmatch(r"[a-z0-9-]+(\.[a-z0-9-]+)*\.[a-z]{2,}", ev.lower()) else (dm.group(1) if dm else "")
    x.update(vend_fill("", "" if vdom == ev.lower() else ev, vdom))
    apply_details(x, k)
    if registry:
        x["vendor_website"] = x.get("vendor_website") or "https://www.cira.ca/"
        x["vendor_address"] = (LDET.get(k) or {}).get("vendor_address") or x.get("vendor_address") or ""  # CIRA's address as its own agreement prints it (a dataset record of CIRA said only "Ottawa, ON")
    x["source"] = ("the .ca registry's public delegation of the buyer's domain (DNS) and CIRA's Registrant Agreement" if registry else
                   "the buyer's own website (it states its membership of the Canada-located body, linked)" if member and "member badge on the buyer's own site" in cfv else
                   "the Canadian body's own current member / participant list" if member else
                   "the buyer's own website (its credit line names the Canada-located vendor that made / hosts the site)" if tech and "credited on the buyer's own site" in cfv else
                   "the buyer's own public DNS records (they name the Canada-located provider of its e-mail, hosting or DNS service)" if tech and "seen in the buyer's public DNS" in cfv else
                   "the buyer's own website or its customer portal on the vendor's platform (service of a Canada-HQ vendor in use)" if tech else
                   "the Canada-located vendor's own website" if client else src or "relationship record")
print("lead rows: facts from the buyer's own pages / the vendor's link label:", dict(n_lf))
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
for kind, paths in (("ended", sorted(_glob.glob(REL + "ended_*.jsonl.gz"))), ("registry", [REL + "vendor_country_unverified_contracts.jsonl.gz"])):
    for r in jl(*paths):
        if r.get("record_id") in seen_rec:
            continue
        seen_rec.add(r.get("record_id"))
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
cands = []
skipped13 = collections.Counter()
for k, ((acc, g), m) in mail.items():
    if not acc or g < 1 or k in covered_keys:
        continue
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
    fed = jur_of_mail(e) == "FED" and not k.startswith("v:")
    prov, how = province_of(k, e, site, m.get("evidence_quote") or "")
    country = "CA" if (k.split(":")[0] in ("osm", "wd", "v") or k in PLACES or prov or fed or md.endswith(".ca") or host_of(site).endswith(".ca")
                       or (BUY.get(k) or {}).get("country") == "CA") else ""
    if not country:
        skipped13["not located in Canada (no honest inference)"] += 1; continue
    if site and not (VEN.get(k) or {}).get("website") and not (BUY.get(k) or {}).get("official_website") and not (k in leads and leads[k].get("website")) \
            and registrable(host_of(site)) != registrable(md) and not FREEMAIL.match(md):
        site = "https://" + md  # the page was a directory or partner page: the organisation's own domain is its mailbox's
    place = " ".join([(m.get("evidence_quote") or ""), addr_text((BUY.get(k) or {}).get("address")), (VEN.get(k) or {}).get("address") or "",
                      (PLACES.get(k) or {}).get("city") or ""])
    vid, conf, what, why = infer(name, e, site, prov, fed, place)
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
            _ba = addr_text((BUY.get(k) or {}).get("address")) or (VEN.get(k) or {}).get("address") or \
                  ", ".join(v for v in ((PLACES.get(k) or {}).get(f) for f in ("address", "city", "province", "postal_code")) if v)
            if _ba and not _lr.get("buyer_address"):
                _lr["buyer_address"] = _ba; n_keyjoin["buyer_address"] += 1
            if name and re.fullmatch(r"(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}", (_lr.get("buyer") or "").lower()) and not re.fullmatch(r"(https?://)?[\w.-]+\.[a-z]{2,}/?", name.strip(), re.I):
                _lr["buyer"] = name; n_keyjoin["buyer_name"] += 1  # the lead only carried the domain
        skipped13["same organisation already in a row (domain / mailbox / name)"] += 1; continue
    covered_mail.add(e.lower()); covered_name.add(norm(name)); covered_keys.add(k)
    if dom:
        covered_dom.add(dom)
    vname, vsite, vaddr, vurl, vquote = INFV[vid]
    LABEL = {4: "invoicing/AP", 3: "finance/accounting dept or supplier-payment office", 2: "purchasing", 1: "general"}
    b_addr = addr_text((BUY.get(k) or {}).get("address")) or (VEN.get(k) or {}).get("address") or \
             ", ".join(x for x in ((PLACES.get(k) or {}).get(f) for f in ("address", "city", "province", "postal_code")) if x)
    rows.append({"jurisdiction": "", "_jur": prov or "CA", "rank_group": "I%d" % g, "completeness_score": sc * 10 + g * 6 + 3,
        "buyer": name, "buyer_website": site, "buyer_address": b_addr,
        "email": e, "email_type": LABEL[g], "email_check": "confirmed", "email_evidence_url": m.get("evidence_url") or "", "email_evidence_quote": m.get("evidence_quote") or "",
        "contract_status": "inferred relationship (no record): %s confidence; the buyer is %s%s; %s" % (conf, what, (" (province from %s)" % how) if how else "", why),
        "source": "inference from the buyer's type and province (no contract, payment or listing record)",
        "vendor": "inferred: " + vname, "vendor_address": vaddr, "vendor_website": vsite,
        "vendor_country_basis": "the vendor's own site, %s: '%s'" % (vurl, vquote),
        "contracts_with_canadian_suppliers": 0, "buyer_keys": 1, "keys": k, "tier": "I", "grade": g, "acc": True})
    n13 += 1
print("P12 organisations:", len(orgs12), "added:", n12, dict(skipped12), "| P13 added:", n13, "| P13 skipped:", dict(skipped13))
print("lead rows that took the organisation's own key (registry facts attach):", dict(n_keyjoin))
os.makedirs(ROOT + "/out/ranked", exist_ok=True)
cols = [c for c in rows[0].keys() if not c.startswith("_")]
rows.sort(key=lambda x: (x["tier"] in ("F", "I"), x["tier"] == "I", x["rank_group"] != "GOLD", -x["completeness_score"]))  # P12 / P13 never displace a stronger row
# one row per body: two spellings of one name ("MRC Charlevoix" / "MRC  de Charlevoix") that share a buyer key within the
# same government are one buyer; the best-ranked row stands for it and carries all its keys
seen, merged = {}, []
for x in rows:
    ks = [k for k in (x.get("keys") or "").split("|") if k]
    j = x.get("jurisdiction") or ""
    hit = next((seen.get((k, j)) or seen.get((k, "")) for k in ks if (k, j) in seen or (k, "") in seen), None)
    if hit is None and not x.get("jurisdiction"):
        hit = next((v for k in ks for (k2, j), v in seen.items() if k2 == k), None)
    if hit is not None:
        allk = sorted(set((hit.get("keys") or "").split("|")) | set(ks) - {""})
        hit["keys"], hit["buyer_keys"] = "|".join(allk), len(allk)
        continue
    for k in ks:
        seen[(k, x.get("jurisdiction") or "")] = x
    merged.append(x)
rows = merged
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
def oc_of(url):
    """org_contacts record for a site; shared hosts (canada.ca …) are keyed by organisation path since 2026-11-08"""
    h = host_of(url or "")
    if not h:
        return None
    dom = registrable(h)
    pth = urllib.parse.urlparse(url if "//" in url else "https://" + url).path.rstrip("/")
    seg = "/".join(pth.split("/")[:3]) if pth else ""
    return (OC.get(dom + seg) if seg else None) or (OC.get(h + seg) if seg else None) or (OC.get(h) if h != dom else None) or OC.get(dom)
def flat_q(t):
    return re.sub(r"\s+", " ", t or "").strip()
# owner 2026-11-04: facts each organisation prints on its own site (tools/org_extras.py): legal name (copyright line), BN / GST-HST /
# charity number, NEQ / QST, logo, language; and the site's status from org_contacts
OX = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_org_extras.jsonl.gz"):
    for d in jl(ROOT + "/data/incoming/claude/claude_org_extras.jsonl.gz"):
        OX[d.get("domain")] = d
def ox_of(url):
    """org_extras record for a site; on shared hosts (canada.ca, ontario.ca …) org_extras v2 keys one record per organisation path"""
    h = host_of(url or "")
    if not h:
        return None
    dom = registrable(h)
    pth = urllib.parse.urlparse(url if "//" in url else "https://" + url).path.rstrip("/")
    seg = "/".join(pth.split("/")[:3]) if pth else ""
    return (OX.get(dom + seg) if seg else None) or (OX.get(h + seg) if seg else None) or (OX.get(h) if h != dom else None) or OX.get(dom)
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
def clean_legal(name, buyer=""):
    """the copyright-line name, or "" when it is a sentence fragment, a web platform's own copyright, or a name cut at a hyphen
    (org_extras ≤ 2026-11-04 stopped at the first dash: 'Municipalité de Saint' for Saint-Jean-sur-Richelieu)"""
    n = re.sub(r"[\uf000-\uf8ff\u2000-\u206f\ue000-\uf8ff]", " ", name or "")  # icon-font glyphs glued to footer text
    n = re.sub(r"\s+", " ", n).strip(" .,-–—|:")
    n = re.sub(r"^(?:tous droits r[ée]serv[ée]s|all rights reserved|copyright|©|\(c\))\s*(?:(?:19|20)\d\d\s*)?", "", n, flags=re.I).strip(" .,-–—|:")
    n = re.split(r"\s+(?:connect with us|follow us|stay connected|subscribe|sign up|cricos\b|abn\b|acn\b|registered charity|charitable registration|privacy|terms|all rights|"
                 r"tous droits|site ?map|plan du site|accessibilit|contact us|nous joindre|back to top|retour en haut)\b", n, 1, flags=re.I)[0].strip(" .,-–—|:")
    n = TRAIL.sub("", n).strip(" .,-–—|:")
    n = re.sub(r"^(?:[àa] la|au|aux|[àa] l'|the|la|le|les|l')\s+", "", n, flags=re.I).strip() if re.match(r"^(?:[àa] la|au|aux|[àa] l')\s", n, re.I) else n  # "à la Commission scolaire …" (pilot dossier S1-12)
    if BAD_LEGAL.search(n) or CUT_PREFIX.search(n) or re.match(r"^(?:'?s\b|[a-z])", n) or re.search(r"\bno\.?$", n, re.I):
        return ""  # a fragment cut at the front ("s Union Partners"), lowercase start, or ending in "No" (a registration number followed)
    if buyer and re.sub(r"\s+", " ", buyer).strip().lower().startswith(n.lower() + "-"):
        return ""
    return n if 3 <= len(n) <= 90 and re.search(r"[A-Za-zÀ-ÿ]{3}", n) else ""
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


def name_overlap(cand, org_name, website=""):
    """a name taken from a page must share a DISTINCTIVE token with the organisation's own name or its host (reviewer 2026-11-08; pilot dossiers
    2026-11-09: "Cambrian College Faculty and staff" and "Pioneer Path University" had passed on the generic words college / university)"""
    if PAGE_NOISE.search(cand or ""):
        return False
    def toks(t):
        return {w for w in re.findall(r"[a-z0-9]{3,}", unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()) if w not in NAME_STOP}
    ct, ot = toks(cand), toks(org_name)
    cd, od = ct - GENERIC_ORG, ot - GENERIC_ORG
    if cd and od:
        if cd & od:
            return True
    elif ct & ot:  # one side has only generic words (e.g. "Health Authority"): fall back to any shared token
        return True
    h = unicodedata.normalize("NFKD", host_of(website or "") or "").encode("ascii", "ignore").decode().lower().replace("www.", "").replace("-", "")
    return bool(h) and any(t in h for t in (cd or ct) if len(t) >= 4)
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
        x[acol] = "%s (schema.org JSON-LD PostalAddress on %s)" % (d["jsonld_address"][:160], pg); n_ox[side + "_address_v2"] += 1
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
n_ox = collections.Counter()
for x in rows:
    for col in ("buyer_legal_name_as_published", "buyer_bn_as_published", "buyer_gst_hst_derived", "buyer_logo_url", "buyer_website_status",
                "vendor_trading_name", "vendor_neq", "vendor_qst_as_published", "vendor_logo_url", "vendor_website_status", "payment_terms_as_published", "po_required_as_published"):
        x.setdefault(col, "")
    b, bo = ox_of(x.get("buyer_website")), oc_of(x.get("buyer_website"))
    if b:
        ln = clean_legal(b.get("legal_name"), x.get("buyer") or "")
        basis = "the site's copyright / footer line"
        if not ln:  # v2 (2026-11-08): the name the organisation states itself — schema.org JSON-LD legalName, then its Terms / Privacy / Legal page
            for k, lab in (("jsonld_legal_name", "schema.org JSON-LD legalName on %s" % (b.get("jsonld_page") or "the site")), ("legal_name_stated", "stated on %s" % (b.get("legal_name_stated_url") or "the site's legal page")),
                           ("jsonld_name", "schema.org JSON-LD Organization name on %s" % (b.get("jsonld_page") or "the site"))):
                cand = clean_legal(b.get(k) or "", x.get("buyer") or "")
                if cand and (k != "jsonld_name" or LEGAL_FORMISH.search(cand)) and name_overlap(cand, x.get("buyer") or "", x.get("buyer_website") or ""):
                    ln, basis = cand, lab; n_ox["buyer_legal_name_v2_" + k] += 1
                    break
                elif cand:
                    n_ox["buyer_legal_name_v2_rejected_no_overlap"] += 1  # reviewer 2026-11-08: "Internet Protocol", "Ville de Granby" on another body's site
        if ln:
            x["buyer_legal_name_as_published"] = ln if basis.startswith("the site's copyright") else "%s (%s)" % (ln, basis); n_ox["buyer_legal_name"] += 1
            if GENERIC_NAME.match(x.get("buyer") or "") or DOMAIN_NAME.match(x.get("buyer") or ""):
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
    v, vo = ox_of(x.get("vendor_website")), oc_of(x.get("vendor_website"))
    if v and not (x.get("vendor") or "").startswith("inferred"):
        if not x.get("vendor_legal_name") and clean_legal(v.get("legal_name"), x.get("vendor") or ""):
            x["vendor_legal_name"] = clean_legal(v["legal_name"], x.get("vendor") or "") + " (as printed on the vendor's site: %s)" % (v.get("legal_name_url") or ""); n_ox["vendor_legal_name"] += 1
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
                cand = clean_legal(v.get(k) or "", x.get("vendor") or "")
                if cand and name_overlap(cand, x.get("vendor") or "", x.get("vendor_website") or ""):
                    x["vendor_legal_name"] = "%s (%s: %s)" % (cand, lab, v.get("jsonld_page") if k.startswith("jsonld") else v.get("legal_name_stated_url") or ""); n_ox["vendor_legal_name_v2"] += 1
                    break
        v2_fill(x, v, "vendor")
        if not x.get("vendor_trading_name"):  # 2026-11-08: the name the vendor trades under on its own site when it differs from its legal name (schema.org alternateName / Organization name)
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
if os.path.exists(ROOT + "/data/incoming/claude/claude_dmarc_check.tsv"):
    for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_dmarc_check.tsv", encoding="utf-8"), delimiter="\t"):
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
    b = oc_of(x.get("buyer_website"))
    if (x.get("buyer_address") or "").strip() in ("CA", "US", "Canada", "CA, CA"):
        x["buyer_address"] = ""  # the release's buyer table had only the country: that is no bill-to address (2026-11-09)
    if b:
        if not x.get("buyer_address") and b.get("address"):
            x["buyer_address"] = b["address"]; n_oc["buyer_address"] += 1
        if b.get("phone") and phone_fits(b["phone"], x.get("buyer_address")):
            x["buyer_phone"] = b["phone"]; n_oc["buyer_phone"] += 1
        x["buyer_contact_evidence_url"] = b.get("address_url") or b.get("phone_url") or ""
    v = oc_of(x.get("vendor_website"))
    if v:
        if not x.get("vendor_address") and v.get("address"):
            x["vendor_address"] = v["address"]; n_oc["vendor_address"] += 1
        if v.get("phone") and phone_fits(v["phone"], x.get("vendor_address")):
            x["vendor_phone"] = v["phone"]; n_oc["vendor_phone"] += 1
        if not x.get("vendor_emails") and v.get("emails"):
            x["vendor_emails"] = v["emails"]; n_oc["vendor_emails"] += 1
        x["vendor_contact_evidence_url"] = v.get("address_url") or v.get("emails_url") or v.get("phone_url") or ""
print("org_contacts: %d organisations read; filled %s" % (len(OC), dict(n_oc)))
# 9. owner 2026-11-04 10:50: every row states the nature of the relationship, how it was found, and where every fact comes from
LANE_META = {}  # (key, mailbox) -> (lane, file, retrieved_date, task_id)
for path in _glob.glob(ROOT + "/data/incoming/*/*buyer_ap*results*.csv"):
    lane = os.path.basename(os.path.dirname(path))
    try:
        for r in csv.DictReader(io.StringIO(open(path, encoding="utf-8", errors="replace").read().replace("\0", ""))):
            e = (r.get("ap_email") or "").strip().lower()
            if e:
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
MD_DOM, MD_NAME = {}, {}
for _mdp in (ROOT + "/data/incoming/claude/claude_municipal_directory.csv", ROOT + "/data/incoming/claude/claude_org_directories.csv"):
    if not os.path.exists(_mdp):
        continue
    for _r in csv.DictReader(open(_mdp, encoding="utf-8", errors="replace")):
        _d = _dom_of(_r.get("website") or "") if _r.get("website") else ""
        if _d and not SHARED_GOV.match(_d):
            MD_DOM.setdefault(_d, _r)
        for nm in (_r.get("legal_name"), (_r.get("source_quote") or "").split(";")[0]):
            if nm and len(norm(nm)) >= 5:
                MD_NAME.setdefault((_r["province"], norm(nm)), _r)
# the place name without its designation ("Ville de X" / "X" / "Municipalité de X" / "Town of X" all name the same body); an ambiguous core (two bodies in one province) is skipped
DESIG_RX = re.compile(r"^(?:la |le |les |l['’])?(?:ville|municipalit[ée](?: r[ée]gionale de comt[ée])?|mrc|cit[ée]|canton|paroisse|village|township|town|city|county|district|regional district|regional municipality|rural municipality|resort municipality|municipal district|united counties|the corporation of the (?:city|town|township|village|municipality|county|district|regional municipality))\s+(?:of|de|du|des|d['’])?\s*", re.I)
def md_core(nm):
    c = norm(DESIG_RX.sub("", (nm or "").strip()))
    return c if len(c) >= 4 else ""
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
    _d = _dom_of(x.get("buyer_website") or "") if x.get("buyer_website") else ""
    prov = x.get("jurisdiction") or ""
    hit = (MD_DOM.get(_d) if _d else None) or MD_NAME.get((prov, norm(x.get("buyer") or ""))) or MD_NAME.get((prov, norm((x.get("buyer_legal_name_as_published") or "").split(" (")[0])))
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
    if not x.get("buyer_address") and hit.get("address"):
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
    if not x.get("buyer_legal_name_as_published") and h.get("legal_name"):
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
n_vs = 0
for x in rows:
    vn = x.get("vendor") or ""
    v_ = VSITE.get(norm(vn)) if vn and not vn.startswith("inferred") and not x.get("vendor_website") else None
    if v_:
        x["vendor_website"] = v_["website"]
        x["vendor_website_basis"] = "found by a web search, confirmed by reading the site on %s: %s (%s)" % (v_["retrieved_date"], v_["evidence_url"], (v_.get("evidence_quote") or "")[:160]); n_vs += 1
print("vendor websites confirmed from search proposals:", len(VSITE), "applied:", n_vs)
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
if os.path.exists(ROOT + "/data/incoming/claude/claude_registry_lookup.csv"):
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_registry_lookup.csv", encoding="utf-8", errors="replace")):
        if _r.get("status") == "found" and _r.get("juri_id"):
            _r["_label"] = "Canada's Business Registries, %s %s" % (_r.get("registry_source") or "", _r.get("juri_id") or "")
            CBR[_r["kind"]][_r["key"] if _r["kind"] == "buyer" else norm(_r["key"])] = _r
n_bulk = 0
if os.path.exists(ROOT + "/data/incoming/claude/claude_registry_bulk.csv"):  # tools/bulk_registry_match.py: REQ open data (NEQ) and Corporations Canada open data (BN); the API rows above win when both exist
    for _r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_registry_bulk.csv", encoding="utf-8", errors="replace")):
        if _r.get("status") == "found" and _r.get("juri_id"):
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
print("registry bulk rows added (no API row for the key):", n_bulk)
n_cbr = collections.Counter()
for x in rows:
    vn = x.get("vendor") or ""
    c = CBR["vendor"].get(norm(vn)) if vn and not vn.startswith("inferred") else None
    if c and form_class(vn) and form_class(c.get("matched_name") or "") and form_class(vn) != form_class(c.get("matched_name") or ""):
        n_cbr["vendor_skipped_legal_form"] += 1; c = None  # reviewer 2026-11-08: Smythe LLP is not Smythe Inc.
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
    if b:
        src = "%s, %s" % (b["_label"], b["retrieved_date"])
        if re.search(r"\((?:stated on|schema\.org|recipient legal name)", x.get("buyer_legal_name_as_published") or ""):
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
        if not x.get("buyer_legal_name_as_published") and g.get("matched_name"):
            x["buyer_legal_name_as_published"] = "%s (recipient legal name in the federal grants & contributions disclosure)" % g["matched_name"]; n_gcr["buyer_legal_name"] += 1
    vn = x.get("vendor") or ""
    g = GCR["vendor"].get(norm(vn)) if vn and not vn.startswith("inferred") else None
    if g and not x.get("vendor_bn9"):
        x["vendor_bn9"] = "%s (recipient_business_number in the federal grants & contributions disclosure, last agreement %s; %s)" % (g["bn9"], g.get("last_agreement_date") or "n/a", g["source_url"]); n_gcr["vendor_bn9"] += 1
        x["vendor_bn_source"] = x.get("vendor_bn_source") or "federal grants & contributions disclosure (recipient_business_number)"
        if not x.get("vendor_gst_hst_derived"):
            x["vendor_gst_hst_derived"] = g["bn9"] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"
print("grants & contributions recipient BNs: %d buyers, %d vendors in file; filled %s" % (len(GCR["buyer"]), len(GCR["vendor"]), dict(n_gcr)))
# the buyers' own purchase-order / contract open data joined to existing pairs (tools/po_opendata.py → claude_po_records.csv; downstream §1.1)
POD = collections.defaultdict(list)
_pop = ROOT + "/data/incoming/claude/claude_po_records.csv.gz"
if not os.path.exists(_pop) and os.path.exists(_pop[:-3]):
    _pop = _pop[:-3]
if os.path.exists(_pop):
    for _r in csv.DictReader((gzip.open(_pop, "rt", encoding="utf-8", errors="replace") if _pop.endswith(".gz") else open(_pop, encoding="utf-8", errors="replace"))):
        POD[(parent(_r["buyer"]), norm(_r["vendor_name"]))].append(_r)
        pv = parent(_r["vendor_name"])
        if pv and pv != norm(_r["vendor_name"]):
            POD[(parent(_r["buyer"]), pv)].append(_r)
n_po = collections.Counter()
for x in rows:
    for c in ("po_numbers_this_pair_open_data", "po_count_this_pair_open_data", "contract_numbers_this_pair_open_data"):
        x.setdefault(c, "")
    if not POD or (x.get("vendor") or "").startswith("inferred"):
        continue
    bkeys = {parent(x.get("buyer") or ""), parent((x.get("buyer_legal_name_as_published") or "").split(" (")[0]), (x.get("org_group_key") or "").split(" | ")[0]} - {""}
    vkeys = {norm(x.get("vendor") or ""), parent(x.get("vendor") or ""), norm((x.get("vendor_legal_name") or "").split(" (")[0]), parent((x.get("vendor_legal_name") or "").split(" (")[0])} - {""}
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
print("buyers' PO / contract open data joined:", dict(n_po), "| records:", sum(len(v) for v in POD.values()))
# D2 / D12: back-reference between the contract dataset and the lead relationships (same organisation by website domain or exact name)
AGG_DOM, AGG_NAME = {}, {}
for _p, _o in orgs.items():
    _d = _dom_of((_o.get("be") or {}).get("official_website") or "")
    if _d and not SHARED_GOV.match(_d):
        AGG_DOM.setdefault(_d, _o)
    AGG_NAME.setdefault(norm(_o.get("name") or ""), _o)
LEAD_DOM, LEAD_NAME = collections.defaultdict(list), collections.defaultdict(list)
for _k, _l in leads.items():
    _d = _dom_of(_l.get("website") or "")
    _lab = "%s — %s%s" % (re.sub(r"=.*$", "", _l.get("canada_field_value") or "lead") if "stories" not in (_l.get("canada_field_value") or "") else "customer story published by the vendor", _l.get("example_vendor") or "", (" (%s)" % _l["latest_record_date"][:10]) if _l.get("latest_record_date") else "")
    if _d and not SHARED_GOV.match(_d):
        LEAD_DOM[_d].append(_lab)
    LEAD_NAME[norm(_l.get("buyer_name") or "")].append(_lab)
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
            if _o2.get("coms"):
                x["commodity_distribution_top3"] = "; ".join("%s (%d)" % (cc, nn) for cc, nn in _o2["coms"].most_common(3))[:300]
            yv = sorted((y, v) for y, v in (_o2.get("yv") or {}).items() if y.isdigit())
            if len(yv) >= 2:
                x["year_over_year_spend_trend"] = "; ".join("%s: %.0f" % (y, v) for y, v in yv[-6:]) + (" — %s" % ("increasing" if yv[-1][1] > yv[-2][1] * 1.25 else "decreasing" if yv[-1][1] < yv[-2][1] * 0.8 else "stable") + " vs previous year (published values only)")
            vn = (x.get("vendor") or "").strip()
            pl = sorted(pp for pp in ((_o2.get("pairs") or {}).get(vn, [])) if pp[0])
            n_pair = _o2["vendors"].get(vn, 0)
            x["pair_prior_records"] = str(n_pair)
            x["pair_first_or_repeat"] = ("repeat relationship (%d records%s)" % (n_pair, (", %s to %s" % (pl[0][0][:10], pl[-1][0][:10])) if pl else "")) if n_pair > 1 else "single record of this pair in the dataset"
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
    x.pop("_org", None)
print("back-references:", dict(n_x2))
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
        o = oc_of(x.get(side + "_website"))
        if o:
            if not x.get(side + "_address") and o.get("address"):
                x[side + "_address"] = o["address"]; n_late[side + "_address"] += 1
            if not x.get(side + "_phone") and o.get("phone") and phone_fits(o["phone"], x.get(side + "_address")):
                x[side + "_phone"] = o["phone"]; n_late[side + "_phone"] += 1
            if side == "vendor" and not x.get("vendor_emails") and o.get("emails") and not (x.get("vendor") or "").startswith("inferred"):
                x["vendor_emails"] = o["emails"]; n_late["vendor_emails"] += 1
            if not x.get(side + "_contact_evidence_url"):
                x[side + "_contact_evidence_url"] = o.get("address_url") or o.get("phone_url") or o.get("emails_url") or ""
        e = ox_of(x.get(side + "_website"))
        if e and e.get("logo_url") and not x.get(side + "_logo_url"):
            x[side + "_logo_url"] = e["logo_url"]; n_late[side + "_logo"] += 1
print("site readers, second pass (websites found late):", dict(n_late))
# the same vendor's BN9 / remit-to address read for one row applies to every row of that vendor (same legal entity); carried with its source
_vbn, _vad = {}, {}
for x in rows:
    _vn = norm(re.sub(r"^inferred:\s*", "", x.get("vendor") or ""))
    if not _vn:
        continue
    if re.match(r"^\d{9}", x.get("vendor_bn9") or "") and _vn not in _vbn:
        _vbn[_vn] = (x["vendor_bn9"], x.get("vendor_bn_source") or "", x.get("buyer") or "")
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
    if not (x.get("vendor_address") or x.get("vendor_registered_address")) and _vn in _vad:
        x["vendor_registered_address"] = _vad[_vn][0] + " (carried from this vendor's row with %s)" % _vad[_vn][1][:60]; n_carry["address"] += 1
print("same-vendor carry-over (BN9 / address from the vendor's other rows):", dict(n_carry))
n9 = collections.Counter()
for x in rows:
    for col in ("vendor_billing_ar_email", "vendor_contacts_found_by", "invoice_reference_hint", "po_number_as_published", "contract_or_agreement_number", "solicitation_or_tender_number", "award_or_notice_id", "buyer_vendor_id", "vendor_ids_in_record",
                "commodity_codes", "buyer_org_codes", "amendment_or_modification", "all_identifiers", "identifier_count", "records_with_this_vendor", "all_references_with_this_vendor",
                "relationship_kind", "relationship_detail", "how_relationship_was_found", "buyer_type", "mailbox_provenance", "buyer_facts_provenance", "vendor_facts_provenance", "method_notes",
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
    x["buyer_type"] = buyer_type(x.get("buyer"), x.get("jurisdiction") or x.get("_jur") or "")
    x["relationship_kind"] = KIND.get(t, KIND["N"])
    x["how_relationship_was_found"] = HOW_FOUND.get(t, HOW_FOUND["N"])
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
    if x.get("buyer_legal_name_as_published"): bp.append("legal name: the site's copyright / footer line (tools/org_extras.py)")
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
print("narrative columns:", dict(n9))
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
EXTRA_SENS = [("law enforcement (incl. transit / parks)", re.compile(r"transit (?:police|enforcement|safety)|special constable|conservation officer|by-?law enforcement|peace officer", re.I)),
              ("financial regulator / oversight office", re.compile(r"\bOSFI\b|superintendent of financial institutions|\bFINTRAC\b|\bCANAFE\b|competition bureau|bureau de la concurrence|privacy commissioner|protection de la vie priv[ée]e|auditor general|v[ée]rificat(?:eur|rice) g[ée]n[ée]ral|ombuds|integrity commissioner|elections? (?:canada|ontario|bc|alberta|qu[ée]bec)|[ée]lections qu[ée]bec|securities commission|autorit[ée] des march[ée]s financiers|\bAMF\b", re.I)),
              ("justice / prosecution / law society", re.compile(r"public prosecution|poursuites p[ée]nales|courts administration|judicial council|attorney general|procureur g[ée]n[ée]ral|crown (?:attorney|counsel|prosecut)|law society|barreau du|directeur des poursuites|ministry of (?:the )?attorney|justice (?:canada|qu[ée]bec)|minist[èe]re de la justice|department of justice", re.I)),
              ("major bank", re.compile(r"\bTD\b|toronto-dominion|\bBMO\b|bank of montreal|banque de montr[ée]al|scotiabank|bank of nova scotia|banque scotia|\bRBC\b|royal bank|banque royale|\bCIBC\b|canadian imperial bank|national bank of canada|banque nationale|desjardins", re.I)),
              ("cybersecurity vendor", re.compile(r"crowdstrike|fortinet|palo alto|sentinelone|esentire|\bcisco\b|check ?point software|trend micro|mcafee|sophos|rapid7|tenable|\bokta\b|zscaler|proofpoint|mimecast|bell canada cyber|telus (?:security|cyber)", re.I)),
              ("political party", re.compile(r"conservative party|parti conservateur|liberal party|parti lib[ée]ral|new democratic party|\bNDP\b|\bNPD\b|bloc qu[ée]b[ée]cois|green party|parti vert|parti qu[ée]b[ée]cois|coalition avenir|qu[ée]bec solidaire|people's party|united conservative|saskatchewan party|\bPC party\b", re.I)),
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
KEY_FIELDS = ["buyer_website", "buyer_address", "buyer_phone", "buyer_legal_name_as_published", "email_evidence_url", "ap_phone", "invoice_mailing_address", "invoicing_requirements", "payment_terms_as_published",
              "po_required_as_published", "contract_title", "contract_value", "award_date", "contract_link", "vendor_address", "vendor_bn9", "vendor_website", "vendor_emails", "vendor_phone", "vendor_legal_name", "invoice_reference_hint", "commodity_codes"]
_today = datetime.date.today()
try:
    npk = collections.Counter()
    for x in rows:
        for c in PACK_COLS:
            x.setdefault(c, "")
        # 2026-11-10: what the buyer's OWN pages say (tools/lead_crawl.py site facts): its postal address when the row has none, and the name it
        # trades under. An invoice may name the recipient by "the name under which the recipient does business" (Input Tax Credit Information
        # (GST/HST) Regulations, SOR/91-45 s. 3(c)(i)), so a self-published trade name with an address completes the bill-to block.
        _lf = next((LFACTS[_k] for _k in (x.get("keys") or "").split("|") if _k in LFACTS), None)
        x.setdefault("buyer_trade_name_as_published", "")
        if _lf:
            if _lf.get("address") and not (x.get("buyer_address") or "").strip() and not (x.get("invoice_mailing_address") or "").strip():
                x["buyer_address"] = "%s (as printed on %s, read %s)" % (_lf["address"], _lf.get("address_url") or "", _lf.get("date") or ""); npk["buyer_address_from_own_page"] += 1
            if _lf.get("site_name") and not x["buyer_trade_name_as_published"]:
                x["buyer_trade_name_as_published"] = "%s (the name on the organisation's own home page, %s, read %s)" % (_lf["site_name"], _lf.get("site") or "", _lf.get("date") or ""); npk["buyer_trade_name_as_published"] += 1
        t, g, ec = x.get("tier") or "", int(x.get("grade") or 0), x.get("email_check") or ""
        name_site = " ".join((x.get(c) or "") for c in ("buyer", "buyer_legal_name_as_published", "buyer_website"))
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
        if _segs and (_dead.search(_segs[0]) and not _live.search(_segs[0]) or (not any(_live.search(t) for t in _segs) and any(_dead.search(t) for t in _segs))):
            x["vendor_registry_warning"] = "WARNING: registry status '%s' — the match may be a namesake or the vendor may no longer exist; verify before use" % vs[:60]; npk["registry_warning"] += 1
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
        x["ship_ready"] = ("yes" if (g == 4 and ec.startswith(("confirmed", "cross")) and t in ("A", "B", "T", "M") and x["sensitivity_flag"] == "no" and not x.get("vendor_registry_warning"))
                           else "yes (finance mailbox, not AP)" if (g == 3 and ec.startswith(("confirmed", "cross")) and t in ("A", "B", "T", "M") and x["sensitivity_flag"] == "no")
                           else "no (%s)" % ("sensitive buyer" if x["sensitivity_flag"] == "yes" else "vendor registry warning" if x.get("vendor_registry_warning") else "mailbox not referee-confirmed" if not ec.startswith(("confirmed", "cross")) else "mailbox below finance grade" if g < 3 else "relationship not dated / active"))
        npk["ship_ready_yes"] += x["ship_ready"] == "yes"
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
    print("downstream pack:", dict(npk))
except Exception as _e:
    import traceback; traceback.print_exc(); print("downstream pack skipped:", type(_e).__name__, _e)
for after, new in (("buyer_address", ["buyer_phone", "buyer_contact_evidence_url"]), ("vendor_emails", ["vendor_phone", "vendor_contact_evidence_url"]),
                   ("email_evidence_quote", ["mailbox_provenance", "email_deliverability", "email_security_posture", "dmarc_policy", "dmarc_record", "dmarc_record_domain", "spf_policy", "spf_record", "mail_provider", "dns_checked_date",
                                             "ap_contact_name_as_published", "ap_phone", "invoice_mailing_address", "invoicing_requirements", "invoice_portal_url", "language_hint"]),
                   ("contract_status", ["relationship_kind", "relationship_detail", "how_relationship_was_found"]),
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
                   ("completeness_score", ["data_quality_score", "ship_ready"]), ("email_check", ["mailbox_confidence", "evidence_age_days", "reverify_due"]), ("email_evidence_quote", ["email_evidence_context", "mailbox_recheck_note"]),
                   ("invoice_portal_url", ["invoice_portal_kind", "invoice_portal_note", "ap_system_hint", "invoicing_requirements_structured", "pay_on_sight", "pay_on_sight_missing", "channel_tier", "invoice_text", "invoice_card_json", "invoice_readiness", "invoice_missing", "ap_grade", "ap_score", "ap_grade_basis", "ap_gap_to_A", "ap_payability", "supplier_setup_url"]), ("payment_terms_as_published", ["payment_terms_default_policy"]),
                   ("instrument_type", ["instrument_type_normalized"]), ("contract_status", ["inference_confidence"]), ("buyer_bn_as_published", ["buyer_bn_program", "buyer_trade_name_as_published"]), ("vendor_registry_status", ["vendor_registry_warning", "vendor_registry_note"]),
                   ("other_relationship_sources", ["typical_contract_value_p50", "typical_contract_value_p75", "typical_cadence_days", "vendor_concentration_top_share", "all_canadian_vendors", "pair_prior_records", "pair_first_or_repeat", "pair_value_trend", "pair_dates_and_values"]),
                   ("method_notes", ["facts_provenance_json", "org_group_key"]), ("po_number_as_published", ["po_numbers_this_pair_open_data", "po_count_this_pair_open_data", "contract_numbers_this_pair_open_data"]), ("vendor_incorporation_date", ["vendor_years_in_business"]), ("dns_checked_date", ["mta_sts", "tls_rpt", "bimi"]),
                   ("invoicing_requirements_structured", ["buyer_payment_method_preference", "buyer_ap_cycle_published", "buyer_tax_exempt_status", "buyer_esignature_preference"]), ("buyer_website_status", ["buyer_linkedin_url", "buyer_supplier_portals_linked", "buyer_registry_id", "buyer_bn_note"]),
                   ("all_references_with_this_vendor", ["contract_value_from_pair", "start_date_from_pair", "end_date_from_pair", "contract_title_from_pair", "contract_description_from_pair", "instrument_type_from_pair", "procurement_method_from_pair", "number_of_bids_from_pair", "po_number_as_published_from_pair", "contract_or_agreement_number_from_pair", "solicitation_or_tender_number_from_pair", "award_or_notice_id_from_pair", "buyer_vendor_id_from_pair", "commodity_codes_from_pair", "buyer_org_codes_from_pair"]), ("vendor_website_status", ["vendor_website_basis", "vendor_linkedin_url", "vendor_industry_naics"]), ("peppol_registered", ["statutory_payees_inferred", "buyer_municipal_tier", "buyer_population", "directory_general_email", "municipal_directory_source", "buyer_fiscal_year_end", "buyer_charity_status", "buyer_charity_designation", "buyer_wikidata", "buyer_founded", "buyer_budget_or_revenue", "buyer_employees", "buyer_legal_form"]),
                   ("vendor_years_in_business", ["vendor_wikidata", "vendor_founded", "vendor_employees"]),
                   ("typical_contract_value_p75", ["typical_contract_value_p90", "average_contract_duration_days", "commodity_distribution_top3", "year_over_year_spend_trend"]),
                   ("buyer_tax_exempt_status", ["buyer_tax_status_derived", "tax_rate_indicative_derived", "invoice_currency_derived"]), ("end_date", ["contract_term_as_published"])):
    if after in cols:
        i = cols.index(after) + 1
        cols[i:i] = [c for c in new if c not in cols]
with open(ROOT + "/out/ranked/ranked_buyers.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
with gzip.open(ROOT + "/out/ranked/ranked_buyers.csv.gz", "wt", newline="", encoding="utf-8", compresslevel=6) as f:  # the committed copy (GitHub's 100 MB limit)
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
with gzip.open(ROOT + "/out/ranked/ranked_buyers.jsonl.gz", "wt", encoding="utf-8", compresslevel=6) as f:  # S1.1: the same rows as JSON lines
    for x in rows:
        f.write(json.dumps({c: x.get(c, "") for c in cols}, ensure_ascii=False) + "\n")
try:
    import subprocess
    subprocess.run([sys.executable, ROOT + "/tools/release_diff.py", ROOT + "/coord/results/ranked/ranked_buyers.csv.gz", ROOT + "/out/ranked/ranked_buyers.csv.gz", ROOT + "/out/ranked"], timeout=1500)
except Exception as _e:
    print("release_diff skipped:", _e)
cnt = collections.Counter(x["rank_group"] for x in rows)
print("rows", len(rows)); print(sorted(cnt.items(), key=lambda kv: (kv[0] != "GOLD", kv[0])))
print("with any email:", sum(1 for x in rows if x["email"]), "| contract buyers:", sum(1 for x in rows if x["contract_status"] in TIER))
