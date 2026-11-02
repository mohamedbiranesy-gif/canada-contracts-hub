"""One row per distinct buyer, ranked by proof quality and completeness (see README.md). Run from anywhere:
    gh release download dataset-latest -D data/release   # once
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
STRONG = re.compile(r"^cap$|[._-]cap$|factur|invoic|invsub|inv[._-]sub|payable|payables|compt\w*pay|comptesapayer|^ap$|^ap[._-]|[._-]ap$|[._-]ap[._-]|accounts?[._-]?pay|fournisseur|supplier|vendor|paiement|payment|paymt|apinvoice", re.I)
QUOTE_AP = re.compile(r"factur|invoice|payable|comptes? (à|a) payer|accounts payable|paiement des fournisseurs|supplier payment", re.I)
ROLEISH = re.compile(r"factur|invoic|bill|payable|compt|account|financ|tresor|treasur|fourniss|supplier|vendor|approv|achat|purchas|procure|"
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
STRONG_ANY = re.compile(r"factur|invoic|payable|comptesapayer|accountspayable|comptespayables|apinvoice|invsub", re.I)
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
    if g == 4 and not (STRONG.search(local) or invoice_near(email, quote)):
        g = 2 if re.search(r"procure|purchas|achat|approv", email, re.I) else 1   # labelled AP but nothing says invoicing
    if g < 3 and FIN.search(local) and not re.search(r"procure|purchas|achat|approv|aid|bourse|scholar|tuition|student|etudiant|soutien|financement|funding|grant|subvention|invest|sustainab|bank|loan|pret|credit|client", local, re.I):
        g = 3
    return g
# 1. best mailbox per buyer key (referee export)
mail = {}
raw = open(ROOT + "/coord/results/org_mailboxes.csv", encoding="utf-8", errors="replace").read().replace("\0", "")
for r in csv.DictReader(io.StringIO(raw)):
    acc = r["check_status"] in ("verified", "cross_verified")
    g = real_grade(r["mailbox"], r["mailbox_type"], r["evidence_quote"], r.get("org_name") or "")
    if g < 0:
        continue
    if re.search(r"direct-deposit|depot-direct", r.get("evidence_url") or "") and g < 3:
        g = 3  # PSPC's table of each federal institution's supplier-payment office: finance tier, not invoicing
    s = (acc, g)
    if r["org_key"] not in mail or s > mail[r["org_key"]][0]:
        mail[r["org_key"]] = (s, r)
# 2. contracts: best proof record per parent organisation
TIER = {"ongoing": "A", "ongoing_inferred": "B", "end_date_unknown": "C"}
TS = {"A": 3, "B": 2, "L": 1.5, "C": 1, "D": 1, "E": 0.5}
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
JUR_DOM = [(r"(\.gc\.ca|canada\.ca|\.forces\.ca)$", "FED"), (r"(gov\.ab\.ca|alberta\.ca)$", "AB"), (r"gov\.nt\.ca$", "NT"), (r"gov\.nl\.ca$", "NL"),
           (r"gov\.sk\.ca$", "SK"), (r"(gouv\.qc\.ca|quebec\.ca)$", "QC"), (r"novascotia\.ca$", "NS"), (r"gnb\.ca$", "NB"), (r"gov\.mb\.ca$", "MB"),
           (r"ontario\.ca$", "ON"), (r"gov\.bc\.ca$", "BC"), (r"(gov\.yk\.ca|yukon\.ca)$", "YT"), (r"gov\.nu\.ca$", "NU"), (r"gov\.pe\.ca$", "PE")]
PLACE = re.compile(r"canada|quebec|alberta|ontario|saskatchewan|manitoba|scotia|brunswick|newfoundland|labrador|yukon|northwest|nunavut|"
                   r"british columbia|prince edward|county|city|ville|town|municipal|college|cegep|universit|hydro|\b(bc|nl|ns|nb|pei)\b")
BAD_LOCAL = re.compile(r"recrut|recruit|emploi|career|carriere|job|plainte|complaint|frais|accessoire|patient|usager|media|presse|press|"
                       r"privacy|confidential|aiprp|atip|benevol|volunteer|fondation|foundation|donat|webmaster|^rh$|^hr$|recevable|receivable|revenue|revenu|"
                       r"billing|taxation|^taxe", re.I)
def jur_of_record(r):
    s = (r.get("source") or {}).get("name", "")
    return next((j for rx, j in JUR_SRC if re.search(rx, s)), "")
def jur_of_mail(email):
    d = (email or "").split("@")[-1].lower()
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
    for k in keys:
        if k in mail and fits(mail[k][1]["mailbox"], mail[k][1].get("evidence_url") or ""):
            (acc, g), m = mail[k]
            opts.append(((acc, g), (m["mailbox"], LABEL[g], "confirmed" if acc else m["check_status"], m["evidence_url"], m["evidence_quote"], g, acc)))
    for kind in ("ap_contact", "procurement_contact", "general_contact"):  # earlier enrichment, evidence kept
        c = be.get(kind) or {}
        if c.get("emails") and fits(c["emails"][0]) and roleish(c["emails"][0].split("@")[0], name):
            ev = (c.get("evidence") or [{}])[0] if isinstance(c.get("evidence"), list) else {}
            g = real_grade(c["emails"][0], {"ap_contact": "accounts_payable", "procurement_contact": "procurement", "general_contact": "general"}[kind], (ev.get("quote") or ""), name)
            if g >= 1:
                opts.append(((True, g), (c["emails"][0], LABEL[g], "from dataset enrichment", ev.get("page_url", ""), (ev.get("quote") or "")[:300], g, True)))
    if opts:
        return max(opts, key=lambda x: x[0])[1]
    return "", "", "", "", "", 0, False
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
        "contract_status": {"A": "active (published end date today or later)", "B": "likely active (" + ("Québec, awarded in the last 3 years, no closing notice" if r["status"] == "ongoing_inferred" and award_date(r) >= CUTOFF3 else "awarded in the last 12 months, no end date published") + ")", "L": "likely active (awarded 12-36 months ago, no end date published; multi-year contracts often still run)", "C": "end date unknown, awarded over 3 years ago"}[tier], "contract_reference": json.dumps(c.get("identifiers") or {}, ensure_ascii=False)[:200], "contract_title": (c.get("title") or "")[:200],
        "contract_value": c.get("value") or "", "currency": c.get("currency") or "", "award_date": award_date(r), "start_date": d.get("start") or "", "end_date": d.get("end") or "",
        "contract_link": r.get("link") or "", "source": (r.get("source") or {}).get("name", ""), "vendor": v.get("name") or "", "vendor_legal_name": ve.get("legal_name") or "",
        "vendor_address": ", ".join(x for x in (a.get("line1"), a.get("city"), a.get("region"), a.get("postal_code")) if x), "vendor_country_basis": v.get("country_basis") or "",
        "vendor_bn9": ve.get("business_number_bn9") or "", "vendor_gst_hst_derived": ve.get("gst_hst_account_derived") or "", "vendor_website": ve.get("website") or "",
        "vendor_emails": "; ".join((x.get("email") or x.get("value") or "") if isinstance(x, dict) else str(x) for x in (ve.get("contact_emails_published") or [])), "contracts_with_canadian_suppliers": o["n"], "buyer_keys": len(o["keys"]), "keys": "|".join(sorted(k for k in o["keys"] if k)), "tier": tier, "grade": g, "acc": acc})
# 4. buyers proven by payment / subaward records or client listings (no contract in the dataset)
leads = {r["buyer_key"]: r for r in csv.DictReader(open(ROOT + "/data/incoming/claude/claude_buyer_leads.csv", encoding="utf-8", errors="replace"))}
seen = {norm(x["buyer"]) for x in rows}
import urllib.parse
REL_PATH = re.compile(r"client|customer|case-stud|casestud|case_stud|temoignage|t%C3%A9moignage|testimonial|success-stor|"
                      r"portfolio|our-work|realisations?\b|r%C3%A9alisations?|nos-realisations|clientele")
NOT_REL_PATH = re.compile(r"terms|reference|support|service|product|letter|lettre|news|nouvelle|blog|article|press|media|document|conditions|bill|/loi|career|emploi|job|event|evenement|contact|about|a-propos|partner|partenaire")
for k, L in leads.items():
    if k not in mail or norm(L["buyer_name"]) in seen: continue
    (acc, g), m = mail[k]
    if BAD_LOCAL.search(m["mailbox"].split("@")[0]): continue
    client = "vendor located in Canada" in L.get("canada_field_value", "")
    if client and re.search(r"\((wall|stories)\)", L.get("canada_field_value", "")):
        pass  # a client logo wall on the vendor's home page, or one of its customer stories: a client listing by construction
    elif client:  # a link on a Canadian vendor's page: a client listing only on a real client / case-study / references page
        path = urllib.parse.urlparse(L.get("evidence_dataset") or "").path.lower()
        if not REL_PATH.search(path) or NOT_REL_PATH.search(path):
            client = "other"  # owner's rule (2026-11-01): kept as the weakest relationship package, never mixed with client listings
        vh = (urllib.parse.urlparse(L.get("evidence_dataset") or "").hostname or "").lower().removeprefix("www.")
        bh = (urllib.parse.urlparse(L.get("website") or "").hostname or L.get("buyer_name") or "").lower().removeprefix("www.")
        if vh and bh and registrable(vh) == registrable(bh):  # the same organisation linking to itself (sister schools, own departments)
            continue
    recent = (L.get("latest_record_date") or "") >= CUTOFF and not client  # paid / subcontracted in the last 12 months
    announced = bool(re.search(r"release dateline|EDC|own news release", L.get("canada_field_value", "")))
    likely = announced and not client and not recent and CUTOFF3 <= (L.get("latest_record_date") or "") < CUTOFF  # owner's 12-36 month rule
    tier = "E" if client == "other" else "D" if client else "B" if recent else "L" if likely else "C"
    rows.append({"rank_group": ("GOLD" if tier == "B" and g == 4 and acc else "%s%d" % (tier, g)), "completeness_score": TS.get(tier, 0) * 10 + g * 6 + (3 if acc else 0),
        "buyer": L["buyer_name"], "buyer_website": L["website"], "award_date": L.get("latest_record_date") or "",
        "email": m["mailbox"], "email_type": m["mailbox_type"], "email_check": "confirmed" if acc else m["check_status"], "email_evidence_url": m["evidence_url"], "email_evidence_quote": m["evidence_quote"],
        "contract_status": "likely active (awarded 12-36 months ago; deal announced by the Canada-based vendor: press release / EDC transaction)" if likely else
                           "linked from a page of the Canada-located vendor's site (not a client page)" if client == "other" else
                           "client listing on the vendor's own site (undated)" if client else
                           ("likely active (contract announced by the Canada-based vendor in the last 12 months: press release / EDC transaction)"
                            if re.search(r"release dateline|EDC|own news release", L.get("canada_field_value", "")) else
                            "likely active (payment / subcontract record dated in the last 12 months)") if recent else "payment / subaward record",
        "contract_link": L["evidence_dataset"], "vendor": L["example_vendor"], "vendor_country_basis": L["canada_field_value"],
        "contracts_with_canadian_suppliers": L["canadian_vendor_rows"], "keys": k, "buyer_keys": 1, "tier": tier, "grade": g, "acc": acc})
os.makedirs(ROOT + "/out/ranked", exist_ok=True)
cols = list(rows[0].keys())
rows.sort(key=lambda x: (x["rank_group"] != "GOLD", -x["completeness_score"]))
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
with open(ROOT + "/out/ranked/ranked_buyers.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
cnt = collections.Counter(x["rank_group"] for x in rows)
print("rows", len(rows)); print(sorted(cnt.items(), key=lambda kv: (kv[0] != "GOLD", kv[0])))
print("with any email:", sum(1 for x in rows if x["email"]), "| contract buyers:", sum(1 for x in rows if x["contract_status"] in TIER))
