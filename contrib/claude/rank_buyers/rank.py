"""One row per distinct buyer, ranked by proof quality and completeness (see README.md). Run from anywhere:
    gh release download dataset-latest -D data/release   # once (needs canadian_vendor_contracts; vendors_enriched, buyers_enriched,
                                                          # vendor_country_unverified_contracts and ended_* are optional: P12 + field fill)
    python3 contrib/claude/rank_buyers/rank.py && python3 contrib/claude/rank_buyers/batches.py
"""
import csv, gzip, json, re, io, collections, unicodedata, datetime, sys, os
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
GRADE = {"invoice_submission": 4, "accounts_payable": 4, "supplier_payment": 4, "procurement": 2, "general": 1}
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
                     r"customer|care|client|rfp|rfq|procserv|^proc|invsub|inv[._-]sub|guichet|adjoint", re.I)
STRONG_ANY = re.compile(r"(?<!manu)factur|invoic|payable|comptesapayer|accountspayable|comptespayables|apinvoice|invsub", re.I)
def roleish(local, org=""):
    toks = [t for t in re.split(r"[._+-]+", local.lower()) if t]
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
    return g
# 1. best mailbox per buyer key (referee export)
WRONG_ENTITY = {"ptvi.invoice@vale.com": "PT Vale Indonesia's invoicing mailbox (an overseas shipping instruction on vale.com), not Vale Canada's"}
mail = {}
raw = open(ROOT + "/coord/results/org_mailboxes.csv", encoding="utf-8", errors="replace").read().replace("\0", "")
for r in csv.DictReader(io.StringIO(raw)):
    r["mailbox"] = re.sub(r"^(?:u003e|u003c|>|<)+", "", (r.get("mailbox") or "").strip(), flags=re.I)  # JSON escape debris glued to the address
    acc = r["check_status"] in ("verified", "cross_verified")
    g = real_grade(r["mailbox"], r["mailbox_type"], r["evidence_quote"], r.get("org_name") or "")
    if g < 0:
        continue
    if re.search(r"direct-deposit|depot-direct", r.get("evidence_url") or "") and g < 3:
        g = 3  # PSPC's table of each federal institution's supplier-payment office: finance tier, not invoicing
    if r["mailbox"].lower() in WRONG_ENTITY:
        continue  # a mailbox of another entity on the group's shared domain (spot-check 2026-11-04)
    if g >= 3 and re.search(r"property-tax|paying-|pay-your|pay-online|payonline|tax-pay|taxes|utility-bill|utilit|water-bill|billing|fines|tickets|tuition|donat|fees|"
                            r"make-a-payment|payment-method|payment-option|/payments?(?:/|$|\.)|e-?transfer|how-to-pay|ways-to-pay|pay-?bills?|pay-?my",
                            (r.get("evidence_url") or "").lower()) and not re.search(r"payable|supplier|vendor|fourniss|invoice|factur|procure|purchas|finance|accounting",
                                                                                     ((r.get("evidence_url") or "") + " " + (r.get("evidence_quote") or "")).lower()):
        g = 1  # a mailbox published on the page where residents / customers pay the organisation
    s = (acc, g)
    if r["org_key"] not in mail or s > mail[r["org_key"]][0]:
        mail[r["org_key"]] = (s, r)
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
           "reg_address": addr_text(ra), "reg_region": region_code(ra)}
    VEN[v["vendor_key"]] = rec
    for n in {norm(v.get("name")), norm(rec["legal_name"])} - {""}:
        VEN_NAME[n] = v["vendor_key"] if VEN_NAME.get(n, v["vendor_key"]) == v["vendor_key"] else None  # ambiguous name: no lookup
    if rec["website"]:
        VEN_DOM.setdefault(registrable(host_of(rec["website"])), v["vendor_key"])
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
    return {"vendor_legal_name": v.get("legal_name", ""), "vendor_address": v.get("address", ""), "vendor_bn9": v.get("bn9", ""),
            "vendor_gst_hst_derived": v.get("gst", ""), "vendor_website": v.get("website", "") or ("https://" + domain if domain else ""),
            "vendor_emails": v.get("emails", ""),
            "vendor_registry_id": ("%s: %s" % (REGN.get(rg.get("registry"), rg.get("registry")), rg.get("id"))) if rg.get("id") else "",
            "vendor_registry_url": rg.get("url") or "", "vendor_registered_address": v.get("reg_address", "") if v.get("reg_address") and v.get("reg_address") != v.get("address") else ""}
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
TS = {"A": 3, "B": 2, "T": 1.8, "L": 1.5, "M": 1.2, "C": 1, "D": 1, "E": 0.5}
CUTOFF = (datetime.date.today() - datetime.timedelta(days=365)).isoformat()
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
                       r"billing|taxation|^taxe", re.I)
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
    o = orgs.setdefault(p, {"keys": set(), "best": None, "bs": -1, "n": 0, "name": name, "be": be, "jur": collections.Counter()})
    o["keys"].add(key); o["n"] += 1; o["jur"][j] += 1
    if sc > o["bs"] or (sc == o["bs"] and award_date(r) > award_date(o["best"])):
        o["best"], o["bs"], o["fields"] = r, sc, fields
        if len(name) < len(o["name"]) or not o["name"]: o["name"] = name
# 3. one row per organisation
rows = []
MTL_KEYS = {r["buyer_key"] for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_buyer_ap_results_manual01.csv", encoding="utf-8"))}
def emailcols(keys, be, gj="", name="", site=""):
    def own(e, page=""):
        if keys & MTL_KEYS and re.search(r"@(ville\.)?montreal\.(ca|qc\.ca)$", e or "", re.I):  # units of the Ville de Montréal (manual01)
            return True
        if "direct-deposit" in page or "depot-direct" in page:  # PSPC's table maps each federal institution to its mailbox
            return True
        if gj and gj != "FED" and jur_of_mail(e) == gj and re.search(r"@(gov\.[a-z]{2}\.ca|gnb\.ca|novascotia\.ca|ontario\.ca)$", e or "", re.I):
            return True  # a provincial government's shared mail domain, for a body of that same government
        if not site and page:  # no known website: the page counts as the buyer's own site only if its domain names the buyer
            h = (urllib.parse.urlparse(page).hostname or "").lower()
            if h and same_org("x@" + registrable(h[4:] if h.startswith("www.") else h), "https://unknown.invalid", name):
                return same_org(e, "https://" + h, name)
        return same_org(e, site or "https://unknown.invalid", name)
    fits = lambda e, page="": (not gj or jur_of_mail(e) in ("", gj)) and not BAD_LOCAL.search((e or "").split("@")[0]) and own(e, page)
    LABEL = {4: "invoicing/AP", 3: "finance/accounting dept or supplier-payment office", 2: "purchasing", 1: "general"}
    opts = []  # (accepted, grade, row) from the referee's mailboxes and from earlier enrichment; the best accepted one wins
    for k in sorted(k for k in keys if k):  # sorted: equal mailboxes are broken the same way on every run (a set's order is random)
        if k in mail and fits(mail[k][1]["mailbox"], mail[k][1].get("evidence_url") or ""):
            (acc, g), m = mail[k]
            opts.append(((acc, g), (m["mailbox"], LABEL[g], "confirmed" if acc else m["check_status"], m["evidence_url"], m["evidence_quote"], g, acc)))
    for kind in ("ap_contact", "procurement_contact", "general_contact"):  # earlier enrichment, evidence kept
        c = be.get(kind) or {}
        if c.get("emails") and fits(c["emails"][0]) and roleish(c["emails"][0].split("@")[0], name):
            ev = (c.get("evidence") or [{}])[0] if isinstance(c.get("evidence"), list) else {}
            if not ev.get("page_url"):
                continue  # evidence or nothing: an enrichment contact without the page it was read on is not delivered
            g = real_grade(c["emails"][0], {"ap_contact": "accounts_payable", "procurement_contact": "procurement", "general_contact": "general"}[kind], (ev.get("quote") or ev.get("snippet") or ""), name)
            if g >= 1:
                opts.append(((True, g), (c["emails"][0], LABEL[g], "from dataset enrichment", ev.get("page_url", ""), (ev.get("quote") or ev.get("snippet") or "")[:300], g, True)))
    if opts:
        return max(opts, key=lambda x: x[0])[1]
    return "", "", "", "", "", 0, False
CUR = {"FED": "CAD", "AB": "CAD", "NT": "CAD", "NL": "CAD", "SK": "CAD", "QC": "CAD", "NS": "CAD", "NB": "CAD", "MB": "CAD", "ON": "CAD", "BC": "CAD",
       "YT": "CAD", "NU": "CAD", "PE": "CAD", "US": "USD", "AU": "AUD", "UK": "GBP"}
def fill_contract(x, r, keys):
    """owner 2026-11-03: every field the record or the release tables give is filled (the rest becomes not_published in batches.py)"""
    v, ve, src = r.get("vendor") or {}, r.get("vendor_enrichment") or {}, r.get("source") or {}
    x["buyer_address"] = addr_text(json.loads(x["buyer_address"]) if x["buyer_address"].startswith("{") and x["buyer_address"].endswith("}") else {}) \
        or addr_text((r.get("buyer") or {}).get("address")) or next((addr_text(BUY[k].get("address")) for k in keys if k in BUY and BUY[k].get("address")), "")
    if not x["buyer_website"]:
        x["buyer_website"] = next((BUY[k]["official_website"] for k in keys if k in BUY and BUY[k].get("official_website")), "")
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
        "contract_status": {"A": "active (published end date today or later)", "B": "likely active (" + (("Québec, awarded in the last 3 years, no closing notice" if jur_of_record(r) == "QC" else "source marks it as continuing; awarded in the last 3 years, no end date published") if r["status"] == "ongoing_inferred" and award_date(r) >= CUTOFF3 else "awarded in the last 12 months, no end date published") + ")", "L": "likely active (awarded 12-36 months ago, no end date published; multi-year contracts often still run)", "C": "end date unknown, awarded over 3 years ago"}[tier], "contract_reference": json.dumps(c.get("identifiers") or {}, ensure_ascii=False)[:200], "contract_title": (c.get("title") or "")[:200], **rec_extra(c),
        "contract_value": c.get("value") or "", "currency": c.get("currency") or "", "award_date": award_date(r), "start_date": d.get("start") or "", "end_date": d.get("end") or "",
        "contract_link": r.get("link") or "", "source": (r.get("source") or {}).get("name", ""), "vendor": v.get("name") or "", "vendor_legal_name": ve.get("legal_name") or "",
        "vendor_address": ", ".join(x for x in (a.get("line1"), a.get("city"), a.get("region"), a.get("postal_code")) if x), "vendor_country_basis": v.get("country_basis") or "",
        "vendor_bn9": ve.get("business_number_bn9") or "", "vendor_gst_hst_derived": ve.get("gst_hst_account_derived") or "", "vendor_website": ve.get("website") or "",
        "vendor_emails": "; ".join((x.get("email") or x.get("value") or "") if isinstance(x, dict) else str(x) for x in (ve.get("contact_emails_published") or [])), "contracts_with_canadian_suppliers": o["n"], "buyer_keys": len(o["keys"]), "keys": "|".join(sorted(k for k in o["keys"] if k)), "tier": tier, "grade": g, "acc": acc})
    fill_contract(rows[-1], r, o["keys"])
# 4. buyers proven by payment / subaward records or client listings (no contract in the dataset)
leads = {r["buyer_key"]: r for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_buyer_leads.csv", encoding="utf-8", errors="replace"))}
LDET = {}  # owner 2026-11-03 ("every field"): the lead's own record details (amount, currency, identifiers, dates, vendor address, title)
if os.path.exists(ROOT + "/data/incoming/claude/claude_lead_details.jsonl.gz"):
    for _d in jl(ROOT + "/data/incoming/claude/claude_lead_details.jsonl.gz"):
        LDET[_d.get("key")] = _d
def apply_details(x, k):
    d = LDET.get(k)
    if not d:
        return
    for col, key in (("contract_value", "value"), ("currency", "currency"), ("contract_reference", "reference"), ("start_date", "start"),
                     ("end_date", "end"), ("vendor_address", "vendor_address"), ("contract_title", "title")):
        if not x.get(col) and d.get(key):
            x[col] = d[key] if col != "contract_value" or not d.get("value_field") else "%s (source field: %s)" % (d[key], d["value_field"])
    if x.get("contract_value") and not x.get("currency"):
        pf = d.get("platform") or ""
        x["currency"] = "USD (derived from the source's government)" if re.search(r"usa|socrata|ckan_us|tx1295|ferc|990|sec|cms", pf) else \
                        "CAD (derived from the source's government)" if re.search(r"bc_sofi|fir|fnfta|ckan|cz_|advd", pf) else ""
seen = {norm(x["buyer"]) for x in rows}
seen_dom = {registrable((urllib.parse.urlparse(x["buyer_website"]).hostname or "").lower().removeprefix("www.")) for x in rows if x.get("buyer_website")}
seen_dom.discard("")
import urllib.parse
REL_PATH = re.compile(r"client|customer|case-stud|casestud|case_stud|temoignage|t%C3%A9moignage|testimonial|success-stor|"
                      r"portfolio|our-work|realisations?\b|r%C3%A9alisations?|nos-realisations|clientele")
NOT_REL_PATH = re.compile(r"terms|reference|support|service|product|letter|lettre|news|nouvelle|blog|article|press|media|document|conditions|bill|/loi|career|emploi|job|event|evenement|contact|about|a-propos|partner|partenaire")
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
def lead_strength(kl):
    """dated records first, then services seen on the buyer's site, 12-36 month records, client listings, other links:
    the strongest relationship of an organisation claims its website domain (one row per organisation)"""
    cfv, ld = kl[1].get("canada_field_value") or "", (kl[1].get("latest_record_date") or "")[:10]
    if "vendor located in Canada" in cfv:
        return 4 if re.search(r"\((wall|stories)\)", cfv) else 5
    if "(tech)" in cfv:
        return 1
    if "membership / statutory fee relationship" in cfv:
        return 3.5
    return 0 if CUTOFF <= ld <= today else 2 if CUTOFF3 <= ld else 3
UNNAMED_VENDOR = re.compile(r"redact|withheld|\bPII\b|confidential|not disclosed|undisclosed|anonymi", re.I)
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
    cfv0, ld0 = L.get("canada_field_value", ""), (L.get("latest_record_date") or "")[:10]
    story_dated = "(stories" in cfv0 and CUTOFF <= ld0 <= today and bool(re.search(r"\(stories; (?:contract data|Canada-HQ)", cfv0) or POSTAL.search(cfv0.upper()))
    if story_dated:
        client = False  # a customer story the vendor published in the last 12 months, vendor proven in Canada: a dated record (B)
    elif client and re.search(r"\((wall|stories)", L.get("canada_field_value", "")):
        pass  # a client logo wall on the vendor's home page, or one of its (undated) customer stories: a client listing by construction
    elif client:  # a link on a Canadian vendor's page: a client listing only on a real client / case-study / references page
        path = urllib.parse.urlparse(L.get("evidence_dataset") or "").path.lower()
        if not REL_PATH.search(path) or NOT_REL_PATH.search(path):
            client = "other"  # owner's rule (2026-11-01): kept as the weakest relationship package, never mixed with client listings
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
    tier = "M" if member else "T" if tech else "E" if client == "other" else "D" if client else "B" if recent else "L" if likely else "C"
    rows.append({"rank_group": ("GOLD" if tier == "B" and g == 4 and acc else "GOLD-T" if tier == "T" and g == 4 and acc else "GOLD-M" if tier == "M" and g == 4 and acc else "%s%d" % (tier, g)), "completeness_score": TS.get(tier, 0) * 10 + g * 6 + (3 if acc else 0),
        "buyer": L["buyer_name"], "buyer_website": L["website"], "award_date": L.get("latest_record_date") or "",
        "email": m["mailbox"], "email_type": m["mailbox_type"], "email_check": "confirmed" if acc else m["check_status"], "email_evidence_url": m["evidence_url"], "email_evidence_quote": m["evidence_quote"],
        "contract_status": ("member / regulated payer of a Canadian body (current list read %s): %s" % ((L.get("latest_record_date") or "")[:10], L["example_vendor"])) if member else
                           ("active service seen on the buyer's own site (%s): Canada-HQ vendor %s" % ((L.get("latest_record_date") or "")[:10], L["example_vendor"])) if tech else
                           ("likely active (awarded 12-36 months ago; deal announced by the Canada-based vendor: press release / EDC transaction)" if announced else
                            "likely active (awarded 12-36 months ago; paid in a fiscal year ending 12-36 months ago: IRS Form 990 contractor located in Canada)" if irs else
                            "likely active (awarded 12-36 months ago; record dated 12-36 months ago: %s)" % src) if likely else
                           "linked from a page of the Canada-located vendor's site (not a client page)" if client == "other" else
                           "client listing on the vendor's own site (undated)" if client else
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
    x["source"] = ("the Canadian body's own current member / participant list" if member else "the buyer's own website (service of a Canada-HQ vendor in use)" if tech else
                   "the Canada-located vendor's own website" if client else src or "relationship record")
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
    if "vendor located in Canada" in cfv or "membership / statutory fee relationship" in cfv or not (CUTOFF <= ld <= today) or UNNAMED_VENDOR.search(L.get("example_vendor") or ""):
        continue  # client listings and member lists are not dated purchase records; the vendor must be named
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
              "contract_status": "active service seen on the buyer's own site (%s): Canada-HQ vendor %s" % (L["latest_record_date"][:10], L["example_vendor"]),
              "source": "the buyer's own website (service of a Canada-HQ vendor in use)",
              "keys": "|".join(sorted(set((x.get("keys") or "").split("|") + [k]) - {""})), "buyer_keys": int(x.get("buyer_keys") or 1) + 1})
    for col in ("contract_reference", "contract_title", "contract_value", "currency", "start_date", "end_date", "vendor_legal_name",
                "vendor_address", "vendor_bn9", "vendor_gst_hst_derived", "vendor_website", "vendor_emails"):
        x[col] = ""
    ev = (L.get("example_vendor") or "").strip()
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
        "contract_reference": json.dumps(c.get("identifiers") or {}, ensure_ascii=False)[:200], "contract_title": (c.get("title") or "")[:200], **rec_extra(c),
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
for sc, g, k, e, name, site, dom, prov, how, vid, conf, what, why, m in cands:
    if e.lower() in covered_mail or (dom and dom in covered_dom) or norm(name) in covered_name:
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
    h = host_of(url or "")
    return OC.get(registrable(h)) if h else None
def flat_q(t):
    return re.sub(r"\s+", " ", t or "").strip()
# owner 2026-11-04: facts each organisation prints on its own site (tools/org_extras.py): legal name (copyright line), BN / GST-HST /
# charity number, NEQ / QST, logo, language; and the site's status from org_contacts
OX = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_org_extras.jsonl.gz"):
    for d in jl(ROOT + "/data/incoming/claude/claude_org_extras.jsonl.gz"):
        OX[d.get("domain")] = d
def ox_of(url):
    h = host_of(url or "")
    return OX.get(registrable(h)) if h else None
TRAIL = re.compile(r"(?:\s+(?:our|the|all|home|about|contact|site|web|privacy|terms|follow|connect|menu|search|login|accessibility|faq|careers|news|events|donate|"
                   r"language|english|french|fran[çc]ais|skip|top|back|rights|reserved|reserves|tous|droits|r[ée]serv[ée]s|powered|by|design|website|sitemap|plan))+$", re.I)
def clean_legal(name):
    n = re.sub(r"\s+", " ", name or "").strip(" .,-–—|:")
    n = TRAIL.sub("", n).strip(" .,-–—|:")
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
n_ox = collections.Counter()
for x in rows:
    for col in ("buyer_legal_name_as_published", "buyer_bn_as_published", "buyer_gst_hst_derived", "buyer_logo_url", "buyer_website_status",
                "vendor_trading_name", "vendor_neq", "vendor_qst_as_published", "vendor_logo_url", "vendor_website_status", "payment_terms_as_published", "po_required_as_published"):
        x.setdefault(col, "")
    b, bo = ox_of(x.get("buyer_website")), oc_of(x.get("buyer_website"))
    if b:
        ln = clean_legal(b.get("legal_name"))
        if ln:
            x["buyer_legal_name_as_published"] = ln; n_ox["buyer_legal_name"] += 1
        if b.get("bn") and bn_ok(b):
            x["buyer_bn_as_published"] = "%s %s (as printed: %s; %s)" % (b["bn"], b.get("bn_program") or "", b.get("bn_label") or "", b.get("bn_url") or "")
            x["buyer_gst_hst_derived"] = b["bn"] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"; n_ox["buyer_bn"] += 1
        if b.get("logo_url"):
            x["buyer_logo_url"] = b["logo_url"]; n_ox["buyer_logo"] += 1
        if not x.get("language_hint") and b.get("language"):
            x["language_hint"] = b["language"]
    if bo and bo.get("status"):
        x["buyer_website_status"] = SITE_STATUS.get(bo["status"], bo["status"])
    v, vo = ox_of(x.get("vendor_website")), oc_of(x.get("vendor_website"))
    if v and not (x.get("vendor") or "").startswith("inferred"):
        if not x.get("vendor_legal_name") and clean_legal(v.get("legal_name")):
            x["vendor_legal_name"] = clean_legal(v["legal_name"]) + " (as printed on the vendor's site: %s)" % (v.get("legal_name_url") or ""); n_ox["vendor_legal_name"] += 1
        if v.get("neq"):
            x["vendor_neq"] = "%s (as printed: %s)" % (v["neq"], v.get("neq_url") or ""); n_ox["vendor_neq"] += 1
        if v.get("qst"):
            x["vendor_qst_as_published"] = "%s (as printed: %s)" % (v["qst"], v.get("qst_url") or ""); n_ox["vendor_qst"] += 1
        if not x.get("vendor_bn9") and v.get("bn") and bn_ok(v):
            x["vendor_bn9"] = v["bn"] + " (as printed on the vendor's site: %s)" % (v.get("bn_url") or "")
            x["vendor_gst_hst_derived"] = v["bn"] + "RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)"; n_ox["vendor_bn"] += 1
        if v.get("logo_url"):
            x["vendor_logo_url"] = v["logo_url"]; n_ox["vendor_logo"] += 1
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
# a mailbox whose domain publishes no mail server (tools/mx_check.py, DNS only) cannot receive the survey: the row stays, without it
MX = {}
if os.path.exists(ROOT + "/data/incoming/claude/claude_mx_check.tsv"):
    for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_mx_check.tsv", encoding="utf-8"), delimiter="\t"):
        MX[r["domain"]] = r["status"]
n_mx = 0
for x in rows:
    e = (x.get("email") or "").lower()
    st = MX.get(e.split("@")[-1]) if e else None
    if e and st == "none":
        for col in ("email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote", "ap_phone", "invoice_mailing_address",
                    "invoicing_requirements", "invoice_portal_url", "ap_contact_name_as_published"):
            x[col] = ""
        x["grade"], x["rank_group"], n_mx = 0, "%s0" % x.get("tier", ""), n_mx + 1
    elif e:
        x["email_deliverability"] = {"mx": "domain publishes a mail server (MX)", "a_only": "no MX record; A record only (deliverability uncertain)",
                                     "error": "DNS check failed; re-checked next run"}.get(st, "not checked yet")
print("mx_check: %d domains known; %d mailboxes on domains with no mail server removed" % (len(MX), n_mx))
used_mail = set()  # one delivered row per mailbox: buyers that share one mailbox (branches on a government's central box) are one contact point
for x in rows:
    e = (x.get("email") or "").lower()
    if not e:
        continue
    if e in used_mail:
        for col in ("email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote"):
            x[col] = ""
        x["grade"], x["rank_group"] = 0, "%s0" % x.get("tier", "")
    used_mail.add(e)
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
for after, new in (("buyer_address", ["buyer_phone", "buyer_contact_evidence_url"]), ("vendor_emails", ["vendor_phone", "vendor_contact_evidence_url"]),
                   ("email_evidence_quote", ["email_deliverability", "ap_contact_name_as_published", "ap_phone", "invoice_mailing_address", "invoicing_requirements", "invoice_portal_url", "language_hint"]),
                   ("contract_title", ["contract_description", "instrument_type", "procurement_method", "commodity", "number_of_bids"]),
                   ("buyer_contact_evidence_url", ["buyer_legal_name_as_published", "buyer_bn_as_published", "buyer_gst_hst_derived", "buyer_logo_url", "buyer_website_status"]),
                   ("vendor_legal_name", ["vendor_trading_name", "vendor_registry_id", "vendor_registry_url", "vendor_registered_address", "vendor_neq", "vendor_qst_as_published"]),
                   ("vendor_contact_evidence_url", ["vendor_logo_url", "vendor_website_status"]),
                   ("invoicing_requirements", ["payment_terms_as_published", "po_required_as_published"])):
    if after in cols:
        i = cols.index(after) + 1
        cols[i:i] = [c for c in new if c not in cols]
with open(ROOT + "/out/ranked/ranked_buyers.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
cnt = collections.Counter(x["rank_group"] for x in rows)
print("rows", len(rows)); print(sorted(cnt.items(), key=lambda kv: (kv[0] != "GOLD", kv[0])))
print("with any email:", sum(1 for x in rows if x["email"]), "| contract buyers:", sum(1 for x in rows if x["contract_status"] in TIER))
