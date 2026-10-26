#!/usr/bin/env python3
"""Build normalized/canada_federal.jsonl from:
  1. Proactive Publication - Contracts over $10,000 (contracts.csv)            [PD]
  2. CanadaBuys contract history, 2023-06 onward                              [CH]
  3. CanadaBuys award notices, 2022-08 onward                                 [AN]
  4. CanadaBuys tender notices (enrichment only)                              [TN]

Usage: python3 -I build.py <downloads_dir> <out_jsonl> <stats_json> [--limit-chunks N]
"""
import sys, os, re, json, csv, collections, datetime, time, traceback
import pandas as pd

REF = "2026-10-25"
REF_DATE = datetime.date(2026, 10, 25)
D = sys.argv[1].rstrip("/") + "/"
OUT = sys.argv[2]
STATS = sys.argv[3]
LIMIT_CHUNKS = None
if "--limit-chunks" in sys.argv:
    LIMIT_CHUNKS = int(sys.argv[sys.argv.index("--limit-chunks") + 1])

PD_CSV = D + "contracts.csv"
CH_CSV = D + "contractHistoryComplete-contratsOctroyesComplet.csv"
AN_CSV = D + "awardNoticeComplete-avisAttributionComplet.csv"
TN_CSV = D + "tenderNoticeComplete-avisAppelOffresComplet.csv"

RETRIEVED = {  # from logs/download.log (UTC)
    "pd": "2026-10-25T12:07:44Z",
    "ch": "2026-10-25T12:06:48Z",
    "an": "2026-10-25T12:06:52Z",
    "tn": "2026-10-25T12:06:55Z",
}
DATASET_URL = {
    "pd": "https://open.canada.ca/data/en/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b",
    "ch": "https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4",
    "an": "https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb",
    "tn": "https://open.canada.ca/data/en/dataset/6abd20d4-7a1c-4b38-baa2-9525d0bb2fd2",
}
RESOURCE_URL = {
    "pd": "https://open.canada.ca/data/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b/resource/fac950c0-00d5-4ec1-a4d3-9cbebf98a305/download/contracts.csv",
    "ch": "https://canadabuys.canada.ca/opendata/pub/contractHistoryComplete-contratsOctroyesComplet.csv",
    "an": "https://canadabuys.canada.ca/opendata/pub/awardNoticeComplete-avisAttributionComplet.csv",
    "tn": "https://canadabuys.canada.ca/opendata/pub/tenderNoticeComplete-avisAppelOffresComplet.csv",
}

LOG = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", "build.log"), "a", encoding="utf-8")
def log(*a):
    msg = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + " " + " ".join(str(x) for x in a)
    print(msg, file=sys.stderr, flush=True)
    LOG.write(msg + "\n"); LOG.flush()

stats = collections.defaultdict(collections.Counter)

# ----------------------------------------------------------------------------- helpers
def norm_id(s):
    return re.sub(r"\s+", "", (s or "").strip().upper())

def alnum(s):
    return re.sub(r"[^A-Z0-9]", "", (s or "").upper())

DEGENERATE_IDS = {"", "NULL", "N/A", "NA", "NONE", "0", "-", "--", "TBD", "UNKNOWN", "ACQUISITIONCARD", "ACQUISITIONCARDS",
                  "VARIOUS", "MULTIPLE", "SEECOMMENTS", "CARD", "NIL", "X", "XX", "XXX", "N.A.", "NOTAPPLICABLE", "NOTAVAILABLE"}
def degenerate(pid_norm):
    return pid_norm in DEGENERATE_IDS or len(pid_norm) < 3

STRONG_ID_RE = re.compile(r"^(?:[A-Z0-9]{5,6}-[A-Z0-9]{6,}(?:/\d{3}/[A-Z0-9]{2,3})?|CW\d{7}|WS\d{10}|[A-Z]{1,3}\d{2,3}[A-Z]{1,2}-\d{2}[A-Z0-9]{4,}(?:/\d{3}/[A-Z0-9]{2,3})?)$")
def strong_id(s):
    return bool(STRONG_ID_RE.match(norm_id(s)))

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
def parse_date(s):
    s = (s or "").strip()[:10]
    if not DATE_RE.match(s):
        return None
    try:
        return datetime.date.fromisoformat(s)
    except ValueError:
        return None

def iso(d):
    return d.isoformat() if d else None

def to_num(s):
    s = (s or "").strip().replace(",", "").replace("$", "")
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None

PC_RE = re.compile(r"^[A-Za-z]\d[A-Za-z](?:\s?\d[A-Za-z]\d)?$")
def canadian_postal(s):
    return bool(PC_RE.match((s or "").strip()))

# Spellings of Canada observed in CanadaBuys supplierAddressCountry (free text): CA, Canada, CANADA, canada, Ca, CAN,
# 'Canada.', and typos Canda / Cananda / Canana / Canad.
CANADA_VALUES = {"CA", "CAN", "CANADA", "CANADA(CA)", "CANADÁ", "CANDA", "CANANDA", "CANANA", "CANAD"}
def is_canada_label(s):
    t = re.sub(r"[\s`'\".]", "", (s or "")).upper()
    return t in CANADA_VALUES

def name_tokens(s):
    s = (s or "").upper().replace("&", " AND ")
    return {t for t in re.findall(r"[A-Z0-9ÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ]+", s) if len(t) >= 3}

# document frequency of name tokens over all distinct vendor names seen (filled after nodes are built);
# a token is "distinctive" when it occurs in few distinct vendor names, so generic words (INC, SERVICES,
# CONSULTING, AUDIO, VISUAL, ...) never count as evidence that two names denote the same vendor.
TOKEN_DF = collections.Counter()
DISTINCTIVE_MAX_DF = 40
CORP_SUFFIX = {"INC", "LTD", "LTEE", "LTÉE", "LIMITED", "LIMITEE", "LIMITÉE", "CORP", "CORPORATION", "CO", "COMPANY", "LLC", "LP", "LLP",
               "ULC", "PLC", "GMBH", "SRL", "SAS", "INCORPORATED", "ENR", "SENC", "SENCRL", "SEC"}

def core_tokens(s):
    return {t for t in name_tokens(s) if TOKEN_DF.get(t, 0) <= DISTINCTIVE_MAX_DF and t not in CORP_SUFFIX}

def names_prefix_match(a, b, n=10):
    na, nb = alnum(a), alnum(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    m = min(len(na), len(nb))
    return m >= n and (na.startswith(nb) or nb.startswith(na))

def names_agree(a, b):
    """loose: same vendor is plausible (prefix match or any shared distinctive token). Used only together with a
    contract-level identifier match."""
    if not a or not b:
        return False
    return names_prefix_match(a, b) or bool(core_tokens(a) & core_tokens(b))

def names_agree_strict(a, b):
    """strict: prefix match, or the distinctive 'core' token sets are equal / one contains the other.
    'Branch Audio Visual' vs 'Hybrid Audio Visual Inc.' -> {BRANCH,AUDIO,VISUAL} vs {HYBRID,AUDIO,VISUAL} -> no."""
    if not a or not b:
        return False
    if names_prefix_match(a, b):
        return True
    ca, cb = core_tokens(a), core_tokens(b)
    if not ca or not cb:
        return False
    return ca <= cb or cb <= ca

CANCEL_VENDOR_RE = re.compile(r"cancel|no contract|not awarded|no award|annul", re.I)

def cb_notice_url(kind, ref):
    """CanadaBuys notice page URL; only for slug families verified to resolve."""
    slug = (ref or "").strip().lower()
    if re.fullmatch(r"(cb-\d+-\d+|mx-\d+|ws\d+-doc\d+|pw-\d{2}-\d{8}(-\d+)?|cw\d+)", slug):
        return f"https://canadabuys.canada.ca/en/tender-opportunities/{kind}/{slug}"
    return None

def pd_record_url(owner_org, reference_number):
    from urllib.parse import quote
    return f"https://search.open.canada.ca/contracts/record/{quote(owner_org, safe='')},{quote(reference_number, safe='')}"

CROWN_RE = re.compile(r"bank of canada|business development bank|farm credit|export development|canada post|deposit insurance|marine atlantic|\bvia\b|canada lands|national capital commission|defence construction|old port|downsview|telefilm|commercial corporation|mortgage and housing|atomic energy|museum|national gallery|film board|pilotage|royal canadian mint|infrastructure bank|dairy commission|freshwater fish|windsor-detroit|jacques cartier|air transport security|development investment|standards council|development research centre|broadcasting corporation|council for the arts|destination canada|race relations|pension investment|ingenium|canadian commercial|\bncc\b|\bbdc\b|\bedc\b|\bfcc\b|\bcdic\b|\bclc\b", re.I)
def buyer_type(name):
    return "crown corporation" if CROWN_RE.search(name or "") else "federal department or agency"

ORG_ALIASES = {
    "dnd-mdn": ["DND", "MDN", "NATIONAL DEFENCE", "NATIONAL DEFENSE", "DEFENCE", "DEFENSE", "CANADIAN FORCES", "CFB", "DRDC"],
    "ic": ["ISED", "INDUSTRY", "INNOVATION"], "dfatd-maecd": ["GAC", "DFATD", "FOREIGN AFFAIRS", "GLOBAL AFFAIRS"],
    "aandc-aadnc": ["CIRNAC", "INDIGENOUS", "CROWN-INDIGENOUS", "NORTHERN AFFAIRS", "AANDC"], "cic": ["IRCC", "IMMIGRATION", "CITIZENSHIP"],
    "ec": ["ECCC", "ENVIRONMENT"], "pc": ["PARKS"], "jus": ["JUSTICE"], "fin": ["FINANCE"], "tc": ["TRANSPORT"], "pch": ["HERITAGE"],
    "wd-deo": ["WD", "WESTERN ECONOMIC", "PRAIRIES"], "infc": ["INFRASTRUCTURE", "HOUSING"], "isc-sac": ["ISC", "INDIGENOUS SERVICES"],
    "esdc-edsc": ["ESDC", "EMPLOYMENT"], "hc-sc": ["HEALTH CANADA", "DEPARTMENT OF HEALTH", "HEALTH (HC)"], "ssc-spc": ["SSC", "SHARED SERVICES"],
    "pwgsc-tpsgc": ["PSPC", "PWGSC", "PUBLIC WORKS", "PUBLIC SERVICES AND PROCUREMENT"], "csc-scc": ["CSC", "CORRECTIONAL", "CORRECTIONNAL", "CORRECTIONS"],
    "rcmp-grc": ["RCMP", "MOUNTED POLICE"], "dfo-mpo": ["DFO", "FISHERIES", "COAST GUARD"], "nrcan-rncan": ["NRCAN", "NATURAL RESOURCES"],
    "nrc-cnrc": ["NRC", "RESEARCH COUNCIL"], "aafc-aac": ["AAFC", "AGRICULTURE"], "cbsa-asfc": ["CBSA", "BORDER"], "cra-arc": ["CRA", "REVENUE"],
    "statcan": ["STATCAN", "STATISTICS"], "phac-aspc": ["PHAC", "PUBLIC HEALTH"], "csa-asc": ["CSA", "SPACE AGENCY"], "lac-bac": ["LAC", "LIBRARY AND ARCHIVES"],
    "vac-acc": ["VAC", "VETERANS"], "elections": ["ELECTIONS", "CHIEF ELECTORAL"], "ps-sp": ["PUBLIC SAFETY"], "tbs-sct": ["TBS", "TREASURY"],
    "pco-bcp": ["PCO", "PRIVY"], "cfia-acia": ["CFIA", "FOOD INSPECTION"], "cihr-irsc": ["CIHR", "HEALTH RESEARCH"], "nserc-crsng": ["NSERC"],
    "sshrc-crsh": ["SSHRC"], "oag-bvg": ["OAG", "AUDITOR"], "opc-cpvp": ["PRIVACY"], "oic-ci": ["INFORMATION COMMISSIONER"],
    "irb-cisr": ["IRB", "REFUGEE"], "cnsc-ccsn": ["CNSC", "NUCLEAR"], "cer-rec": ["CER", "ENERGY REGULATOR"], "casdo-ocena": ["ACCESSIBILITY STANDARDS"],
    "wage": ["WAGE", "WOMEN AND GENDER"], "ced-dec": ["CED", "QUEBEC REGIONS", "REGIONS OF QUEBEC"], "acoa-apeca": ["ACOA", "ATLANTIC CANADA OPPORTUNITIES"],
    "feddevontario": ["FEDDEV"], "fednor": ["FEDNOR"], "cannor": ["CANNOR", "NORTHERN ECONOMIC"], "pacifican": ["PACIFICAN", "PACIFIC ECONOMIC"],
    "prairiescan": ["PRAIRIESCAN", "PRAIRIES ECONOMIC"], "polar-polaire": ["POLAR"], "iaac-aeic": ["IAAC", "IMPACT ASSESSMENT"],
    "cta-otc": ["TRANSPORTATION AGENCY"], "tsb-bst": ["TSB", "SAFETY BOARD"], "crtc": ["CRTC"], "osfi-bsif": ["OSFI", "SUPERINTENDENT"],
    "fcac-acfc": ["FCAC", "CONSUMER AGENCY"], "fintrac-canafe": ["FINTRAC"], "psc-cfp": ["PUBLIC SERVICE COMMISSION", "(PSC)"],
    "csps-efpc": ["CSPS", "SCHOOL OF PUBLIC SERVICE"], "cas-satj": ["COURTS ADMINISTRATION"], "ppsc-sppc": ["PPSC", "PROSECUTION"],
    "atssc-scdata": ["ATSSC", "TRIBUNALS"], "chrc-ccdp": ["CHRC", "HUMAN RIGHTS"], "nfb-onf": ["NFB", "FILM BOARD"], "ngc-mbac": ["GALLERY"],
    "nbc-ccbn": ["BATTLEFIELDS"], "cgc-ccg": ["GRAIN"], "ccohs-cchst": ["CCOHS", "OCCUPATIONAL HEALTH"], "pbc-clcc": ["PAROLE"],
    "mpcc-cppm": ["MILITARY POLICE"], "ocol-clo": ["OFFICIAL LANGUAGES"], "ijc-cmi": ["JOINT COMMISSION"], "iic-iac": ["INVEST IN CANADA"],
    "cics-scic": ["INTERGOVERNMENTAL CONFERENCE"], "pmprb-cepmb": ["PATENTED MEDICINE"], "fja-cmf": ["JUDICIAL AFFAIRS"], "osgg-bsgg": ["GOVERNOR GENERAL"],
    "swc-cfc": ["STATUS OF WOMEN"], "pptc": ["PASSPORT"], "cpc-cpp": ["CIVILIAN REVIEW"], "erc-cee": ["EXTERNAL REVIEW"], "mgerc-ceegm": ["GRIEVANCES"],
    "oci-bec": ["CORRECTIONAL INVESTIGATOR"], "ocl-cal": ["LOBBYING"], "oto-boc": ["TAXPAYERS"], "psic-ispc": ["INTEGRITY"], "nsira-ossnr": ["NSIRA"],
    "ocsec-bccst": ["INTELLIGENCE COMMISSIONER"], "snsicp-scpssnr": ["NSICOP", "PARLIAMENTARIANS"], "sirc-csars": ["SIRC"], "vrab-tacra": ["VRAB", "VETERANS REVIEW"],
    "fpcc-cpac": ["FARM PRODUCTS"], "cwa-aec": ["WATER AGENCY"], "org231": ["LAW COMMISSION"], "ocol": ["OFFICIAL LANGUAGES"],
}
BUYER_STOP = {"CANADA", "CANADIAN", "DEPARTMENT", "AGENCY", "OFFICE", "SERVICE", "SERVICES", "COMMISSION", "BOARD", "NATIONAL", "GOVERNMENT",
              "ROYAL", "AFFAIRS", "DEVELOPMENT", "OF", "THE", "AND", "FOR", "SECRETARIAT", "COUNCIL", "CENTRE", "CENTER", "BUREAU", "MINISTÈRE",
              "ECONOMIC", "REGIONAL", "HEADQUARTERS", "REGION"}
def en_title(t):
    return (t or "").split("|")[0].strip()

def buyer_agrees(owner_org, owner_title_en, *cb_names):
    hay = " ".join(n or "" for n in cb_names).upper()
    if not hay.strip():
        return False
    for a in ORG_ALIASES.get(owner_org, []):
        if a in hay:
            return True
    toks = {t for t in re.findall(r"[A-Z]{4,}", (owner_title_en or "").upper()) if t not in BUYER_STOP}
    return any(t in hay for t in toks)

# ----------------------------------------------------------------------------- code labels (from recombinant schema)
SCHEMA = json.load(open(D + "contracts_schema.json", encoding="utf-8"))
CHOICES = {}
for f in SCHEMA["resources"][0]["fields"]:
    ch = f.get("choices")
    if isinstance(ch, dict):
        CHOICES[f["id"]] = {k: (v.get("en") if isinstance(v, dict) else v) for k, v in ch.items()}
def label(field, code):
    code = (code or "").strip()
    if code == "":
        return None
    return CHOICES.get(field, {}).get(code, code)
def labels_multi(field, codes):
    codes = [c.strip() for c in (codes or "").split(",") if c.strip()]
    return [label(field, c) for c in codes] or None

# ----------------------------------------------------------------------------- load CanadaBuys CH
log("loading CH")
ch_df = pd.read_csv(CH_CSV, dtype=str, keep_default_na=False, encoding="utf-8-sig")
ch_df["_amend_sort"] = ch_df["amendmentNumber-numeroModification"].map(lambda s: (0, int(s)) if s.isdigit() else (1, s))
ch_df = ch_df.sort_values(["referenceNumber-numeroReference", "_amend_sort", "publicationDate-datePublication"], kind="stable")
ch_groups = {}  # ref -> dict
_recs = ch_df.drop(columns=["_amend_sort"]).to_dict(orient="records")
for row in _recs:
    ref = row["referenceNumber-numeroReference"]
    g = ch_groups.get(ref)
    if g is None:
        ch_groups[ref] = {"ref": ref, "rows": [row], "last": row, "first": row}
    else:
        g["rows"].append(row); g["last"] = row
del _recs
stats["ch"]["rows"] = len(ch_df); stats["ch"]["groups"] = len(ch_groups)
del ch_df
log("CH groups", len(ch_groups))

# ----------------------------------------------------------------------------- load CanadaBuys AN
log("loading AN")
an_df = pd.read_csv(AN_CSV, dtype=str, keep_default_na=False, encoding="utf-8-sig")
# The award-notice file is essentially one row per award notice (referenceNumber is unique); amendmentNumber is a
# counter carried on the notice, not a separate row per amendment. We therefore keep one node per row, except that rows
# sharing (solicitation, supplier, non-degenerate contractNumber) are treated as versions of the same award.
an_df["_sol"] = an_df["solicitationNumber-numeroSollicitation"].map(alnum)
an_df["_sup"] = an_df["supplierLegalName-nomLegalFournisseur-eng"].map(lambda s: alnum(s)[:40])
an_df["_cn"] = an_df["contractNumber-numeroContrat"].map(lambda s: "" if degenerate(norm_id(s)) else alnum(s))
an_df["_grp"] = an_df.apply(lambda r: (r["_sol"] + "|" + r["_sup"] + "|" + r["_cn"]) if (r["_cn"] and r["_sol"]) else ("REF|" + r["referenceNumber-numeroReference"]), axis=1)
an_df["_amend_sort"] = an_df["amendmentNumber-numeroModification"].map(lambda s: (0, int(s)) if s.isdigit() else (1, s))
an_df = an_df.sort_values(["_grp", "publicationDate-datePublication", "_amend_sort"], kind="stable")
an_groups = {}
_grps = an_df["_grp"].tolist()
_recs = an_df.drop(columns=["_sol", "_sup", "_cn", "_grp", "_amend_sort"]).to_dict(orient="records")
_tmp = {}
for grp, row in zip(_grps, _recs):
    g = _tmp.get(grp)
    if g is None:
        _tmp[grp] = {"rows": [row], "first": row, "last": row}
    else:
        g["rows"].append(row); g["last"] = row
for grp, g in _tmp.items():
    key = g["last"]["referenceNumber-numeroReference"]
    an_groups[key] = {"ref": key, "rows": g["rows"], "last": g["last"], "first": g["first"]}
del _grps, _recs, _tmp
stats["an"]["rows"] = len(an_df); stats["an"]["groups"] = len(an_groups)
del an_df
log("AN groups", len(an_groups))

# ----------------------------------------------------------------------------- PD pass 1: candidate keys
def pd_keys(chunk):
    pidn = chunk["procurement_id"].str.strip().str.upper().str.replace(r"\s+", "", regex=True)
    deg = pidn.map(degenerate)
    key = pidn.where(~deg, "REF:" + chunk["reference_number"].str.strip())
    key = key.where(deg, "PID:" + pidn)
    return chunk["owner_org"] + "|" + key

log("PD pass 1")
cand = set()
nrows = 0
for i, chunk in enumerate(pd.read_csv(PD_CSV, chunksize=100000, dtype=str, keep_default_na=False, encoding="utf-8-sig")):
    if LIMIT_CHUNKS and i >= LIMIT_CHUNKS:
        break
    nrows += len(chunk)
    c = chunk["country_of_vendor"].str.strip().str.upper()
    stats["pd_country_values"].update(c.value_counts().to_dict())
    dd = chunk["delivery_date"].str.strip()
    live_or_blank = (dd == "") | (dd.str.match(r"^\d{4}-\d{2}-\d{2}$") & (dd >= REF))
    ca = (c == "CA") | ((c == "") & chunk["vendor_postal_code"].map(canadian_postal))
    keys = pd_keys(chunk)
    cand.update(keys[live_or_blank & ca].tolist())
    log(f"  pass1 rows {nrows} candidates {len(cand)}")
stats["pd"]["rows_total"] = nrows
stats["pd"]["candidate_groups"] = len(cand)

# ----------------------------------------------------------------------------- PD pass 2: collect all rows of candidate groups
log("PD pass 2")
pd_rows = collections.defaultdict(list)
for i, chunk in enumerate(pd.read_csv(PD_CSV, chunksize=100000, dtype=str, keep_default_na=False, encoding="utf-8-sig")):
    if LIMIT_CHUNKS and i >= LIMIT_CHUNKS:
        break
    keys = pd_keys(chunk)
    m = keys.isin(cand)
    sub = chunk[m]
    for k, row in zip(keys[m], sub.to_dict(orient="records")):
        pd_rows[k].append(row)
log("PD groups collected", len(pd_rows), "rows", sum(len(v) for v in pd_rows.values()))

PERIOD_RE = re.compile(r"(\d{4}-\d{4}-Q[1-4])")
def pd_period(row):
    rp = row["reporting_period"].strip()
    if re.fullmatch(r"\d{4}-\d{4}-Q[1-4]", rp):
        return rp
    m = PERIOD_RE.search(row["reference_number"])
    return m.group(1) if m else ""

def pd_sort_key(row):
    return (pd_period(row), row["contract_date"].strip(), row["reference_number"].strip())

# ----------------------------------------------------------------------------- build source nodes
class Node:
    __slots__ = ("src", "key", "rows", "last", "first", "ids", "vendor", "country_ok", "country_basis", "buyer_org", "buyer_title",
                 "end", "end_raw", "start", "start_raw", "cancelled", "cancel_reason", "sols")
    def __init__(self, src, key):
        self.src, self.key = src, key
        self.ids = {}  # alnum id -> (field, original)
        self.sols = set()
        self.cancelled = False; self.cancel_reason = None

nodes = []

# PD nodes
for k, rows in pd_rows.items():
    rows.sort(key=pd_sort_key)
    last = rows[-1]
    n = Node("pd", k); n.rows = rows; n.last = last; n.first = rows[0]
    org = last["owner_org"]
    n.buyer_org = org; n.buyer_title = last["owner_org_title"]
    pidn = norm_id(last["procurement_id"])
    if not degenerate(pidn):
        n.ids[alnum(pidn)] = ("procurement_id", last["procurement_id"].strip())
        n.sols.add(alnum(pidn))
    for r in rows:  # other procurement_id spellings across rows (should be identical by construction)
        p = norm_id(r["procurement_id"])
        if not degenerate(p):
            n.ids.setdefault(alnum(p), ("procurement_id", r["procurement_id"].strip()))
    n.vendor = last["vendor_name"].strip() or next((r["vendor_name"].strip() for r in reversed(rows) if r["vendor_name"].strip()), "")
    # vendor country: latest non-blank country_of_vendor
    cvals = [r["country_of_vendor"].strip().upper() for r in rows]
    nonblank = [c for c in cvals if c]
    latest_country = next((c for c in reversed(cvals) if c), "")
    if latest_country == "CA":
        n.country_ok = True; n.country_basis = f"country_of_vendor = 'CA' (latest row {last['reference_number']})"
    elif latest_country == "":
        pcs = [r["vendor_postal_code"].strip() for r in rows if canadian_postal(r["vendor_postal_code"])]
        if pcs:
            n.country_ok = True; n.country_basis = "vendor_postal_code pattern (country_of_vendor blank)"
        else:
            n.country_ok = False; n.country_basis = None
    else:
        n.country_ok = False; n.country_basis = None
    if n.country_ok and len(set(nonblank)) > 1:
        n.country_basis += f"; note other rows report {sorted(set(nonblank) - {'CA'})}"
    n.end_raw = last["delivery_date"].strip(); n.end = parse_date(n.end_raw)
    if n.end is None and n.end_raw == "":
        # fall back to latest non-blank delivery_date in the group
        for r in reversed(rows):
            if r["delivery_date"].strip():
                n.end = parse_date(r["delivery_date"]); n.end_raw = r["delivery_date"].strip() + f" (from earlier row {r['reference_number']}; latest row blank)"
                break
    n.start_raw = last["contract_period_start"].strip() or last["contract_date"].strip()
    n.start = parse_date(n.start_raw)
    nodes.append(n)
stats["pd"]["nodes"] = sum(1 for n in nodes if n.src == "pd")

# CH nodes
for ref, g in ch_groups.items():
    last = g["last"]; rows = g["rows"]
    n = Node("ch", ref); n.rows = rows; n.last = last; n.first = rows[0]
    for fld in ["contractNumber-numeroContrat", "referenceNumber-numeroReference", "procurementNumber-numeroApprovisionnement", "solicitationNumber-numeroSollicitation"]:
        v = last[fld].strip()
        if v and not degenerate(norm_id(v)):
            n.ids.setdefault(alnum(v), (fld, v))
    for fld in ["solicitationNumber-numeroSollicitation", "procurementNumber-numeroApprovisionnement"]:
        v = last[fld].strip()
        if v:
            n.sols.add(alnum(v))
    n.vendor = last["supplierLegalName-nomLegalFournisseur-eng"].strip() or last["supplierOperatingName-nomCommercialFournisseur-eng"].strip() or last["supplierStandardizedName-nomNormaliseFournisseur-eng"].strip()
    ce, cf = last["supplierAddressCountry-fournisseurAdressePays-eng"], last["supplierAddressCountry-fournisseurAdressePays-fra"]
    stats["ch_country_values"][ce.strip()] += 1
    if is_canada_label(ce) or is_canada_label(cf):
        n.country_ok = True; n.country_basis = f"supplierAddressCountry-fournisseurAdressePays-eng = {ce.strip()!r}"
    elif ce.strip() == "" and canadian_postal(last["supplierAddressPostalCode-fournisseurAdresseCodePostal"]):
        n.country_ok = True; n.country_basis = "supplierAddressPostalCode pattern (supplierAddressCountry blank)"
    else:
        n.country_ok = False; n.country_basis = None
    n.buyer_org = None; n.buyer_title = last["endUserEntitiesName-nomEntitesUtilisateurFinal-eng"] or last["contractingEntityName-nomEntitContractante-eng"]
    n.end_raw = last["contractEndDate-dateFinContrat"].strip(); n.end = parse_date(n.end_raw)
    n.start_raw = last["contractStartDate-contratDateDebut"].strip() or last["contractAwardDate-dateAttributionContrat"].strip()
    n.start = parse_date(n.start_raw)
    if last["amendmentType-typeModification-eng"].strip() == "Termination":
        n.cancelled = True; n.cancel_reason = f"CanadaBuys contract history latest row (amendment {last['amendmentNumber-numeroModification']}) amendmentType = Termination"
    st = last["contractStatus-statutContrat-eng"].strip()
    if st == "Cancelled":
        n.cancelled = True; n.cancel_reason = "CanadaBuys contract history contractStatus = Cancelled"
    nodes.append(n)
stats["ch"]["nodes"] = len(ch_groups)

# AN nodes
for ref, g in an_groups.items():
    last = g["last"]; rows = g["rows"]
    n = Node("an", ref); n.rows = rows; n.last = last; n.first = rows[0]
    for r in rows:
        for fld in ["contractNumber-numeroContrat", "referenceNumber-numeroReference", "solicitationNumber-numeroSollicitation"]:
            v = r[fld].strip()
            if v and not degenerate(norm_id(v)):
                n.ids.setdefault(alnum(v), (fld, v))
        v = r["solicitationNumber-numeroSollicitation"].strip()
        if v:
            n.sols.add(alnum(v))
    n.vendor = last["supplierLegalName-nomLegalFournisseur-eng"].strip() or last["supplierLegalName-nomLegalFournisseur-fra"].strip()
    ce, cf = last["supplierAddressCountry-fournisseurAdressePays-eng"], last["supplierAddressCountry-fournisseurAdressePays-fra"]
    stats["an_country_values"][ce.strip()] += 1
    if is_canada_label(ce) or is_canada_label(cf):
        n.country_ok = True; n.country_basis = f"supplierAddressCountry-fournisseurAdressePays-eng = {ce.strip()!r}"
    elif ce.strip() == "" and canadian_postal(last["supplierAddressPostalCode-fournisseurAdresseCodePostal"]):
        n.country_ok = True; n.country_basis = "supplierAddressPostalCode pattern (supplierAddressCountry blank)"
    else:
        n.country_ok = False; n.country_basis = None
    n.buyer_org = None; n.buyer_title = last["endUserEntitiesName-nomEntitesUtilisateurFinal-eng"] or last["contractingEntityName-nomEntitContractante-eng"]
    n.end_raw = last["contractEndDate-dateFinContrat"].strip(); n.end = parse_date(n.end_raw)
    n.start_raw = last["contractStartDate-contratDateDebut"].strip() or last["contractAwardDate-dateAttributionContrat"].strip()
    n.start = parse_date(n.start_raw)
    st = last["awardStatus-attributionStatut-eng"].strip()
    if st == "Cancelled":
        n.cancelled = True; n.cancel_reason = f"CanadaBuys award notice {last['referenceNumber-numeroReference']} awardStatus = Cancelled"
    if CANCEL_VENDOR_RE.search(n.vendor or "") and len(n.vendor or "") > 25:
        n.cancelled = True; n.cancel_reason = f"CanadaBuys award notice supplier field reads as a cancellation note: {n.vendor[:80]!r}"
        n.country_ok = False
    nodes.append(n)
stats["an"]["nodes"] = len(an_groups)
log("nodes", len(nodes))

# token document frequencies over distinct vendor names
_seen_names = set()
for n in nodes:
    nm = (n.vendor or "").strip().upper()
    if nm and nm not in _seen_names:
        _seen_names.add(nm)
        TOKEN_DF.update(name_tokens(nm))
stats["name_tokens"] = {"distinct_vendor_names": len(_seen_names), "distinct_tokens": len(TOKEN_DF),
                        "top_generic_tokens": TOKEN_DF.most_common(40)}
del _seen_names

# ----------------------------------------------------------------------------- union-find merge across sources
parent = list(range(len(nodes)))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra

index = collections.defaultdict(list)  # alnum id -> [node idx]
for i, n in enumerate(nodes):
    for a in n.ids:
        index[a].append(i)

merge_log = collections.Counter()
merge_pairs = {}  # (i,j) -> basis
CONTRACT_FIELDS = {"procurement_id", "contractNumber-numeroContrat", "referenceNumber-numeroReference"}
SOL_RE = re.compile(r"^WS\d{10}$")

def is_solicitation_level(field_i, field_j, value):
    return bool(SOL_RE.match(norm_id(value))) or field_i.startswith(("solicitation", "procurementNumber")) or field_j.startswith(("solicitation", "procurementNumber"))

# Pass 1: contract-level identifiers (PD procurement_id, CanadaBuys contractNumber / CW reference number).
contract_edges = set()
for a, idxs in index.items():
    if len(idxs) < 2:
        continue
    if len(idxs) > 400:
        merge_log["skipped_ids_with_>400_nodes"] += 1
        continue
    for x in range(len(idxs)):
        for y in range(x + 1, len(idxs)):
            i, j = idxs[x], idxs[y]
            ni, nj = nodes[i], nodes[j]
            if ni.src == nj.src:
                continue
            fi, fj = ni.ids[a][0], nj.ids[a][0]
            vi, vj = ni.ids[a][1], nj.ids[a][1]
            if not (fi in CONTRACT_FIELDS and fj in CONTRACT_FIELDS) or is_solicitation_level(fi, fj, vi):
                continue
            strong = strong_id(vi) and strong_id(vj)
            if names_agree(ni.vendor, nj.vendor):
                ok, why = True, "contract id + vendor names agree"
            elif strong:
                ok, why = True, "strong contract id (vendor names differ)"
            elif ni.src == "pd" or nj.src == "pd":
                # weak PD procurement ids (PO numbers like 4500123456) collide across departments: require buyer agreement too
                pdn, other = (ni, nj) if ni.src == "pd" else (nj, ni)
                o = other.last
                ok = buyer_agrees(pdn.buyer_org, en_title(pdn.buyer_title), o.get("contractingEntityName-nomEntitContractante-eng"), o.get("endUserEntitiesName-nomEntitesUtilisateurFinal-eng"))
                why = "weak contract id + buyer agrees (vendor names differ)" if ok else "rejected: weak contract id, vendor names and buyer differ"
            else:
                ok, why = False, "rejected: weak contract id, vendor names differ"
            if ok:
                union(i, j); contract_edges.add(i); contract_edges.add(j)
                merge_pairs.setdefault((min(i, j), max(i, j)), f"{ni.src}.{fi} = {nj.src}.{fj} = {vi!r}: {why}")
            merge_log[f"{ni.src}-{nj.src}: {why}"] += 1

# Pass 2: solicitation-level identifiers (WS…, solicitationNumber, procurementNumber, PD procurement_id used as a
# solicitation number). A solicitation is shared by every award under it (standing offers, supply arrangements,
# multi-award RFPs), so we only use it for nodes that found no contract-level match, require strict vendor-name
# agreement, and require the match to be unique (exactly one counterpart of each other source).
sol_index = collections.defaultdict(lambda: collections.defaultdict(list))  # alnum sol -> src -> [idx]
for i, n in enumerate(nodes):
    if i in contract_edges:
        continue
    for a, (fld, val) in n.ids.items():
        if fld.startswith(("solicitation", "procurementNumber")) or SOL_RE.match(norm_id(val)):
            sol_index[a][n.src].append(i)
    if n.src == "pd":
        for a in n.sols:
            sol_index[a]["pd"].append(i)
for a, by_src in sol_index.items():
    srcs = list(by_src)
    if len(srcs) < 2:
        continue
    for x in range(len(srcs)):
        for y in range(x + 1, len(srcs)):
            li, lj = by_src[srcs[x]], by_src[srcs[y]]
            for i in li:
                cands = [j for j in lj if names_agree_strict(nodes[i].vendor, nodes[j].vendor)]
                if len(cands) == 1:
                    j = cands[0]
                    back = [k for k in li if names_agree_strict(nodes[j].vendor, nodes[k].vendor)]
                    if len(back) == 1:
                        ni, nj = nodes[i], nodes[j]
                        union(i, j)
                        merge_pairs.setdefault((min(i, j), max(i, j)), f"{ni.src} / {nj.src} share solicitation-level id {a!r}: strict vendor-name agreement, unique counterpart on both sides")
                        merge_log[f"{ni.src}-{nj.src}: solicitation id + strict names + unique"] += 1
                    else:
                        merge_log[f"{nodes[i].src}-{nodes[j].src}: rejected: solicitation id, counterpart ambiguous"] += 1
                elif len(cands) > 1:
                    merge_log[f"{nodes[i].src}-{srcs[y]}: rejected: solicitation id, several same-vendor candidates"] += 1
                else:
                    merge_log[f"{nodes[i].src}-{srcs[y]}: rejected: solicitation id, vendor names differ"] += 1
stats["merge"] = dict(merge_log)
log("merge decisions", dict(merge_log))

raw_clusters = collections.defaultdict(list)
for i in range(len(nodes)):
    raw_clusters[find(i)].append(i)
log("raw clusters", len(raw_clusters))

clusters = {}
multi_contract = 0
for root, cl in raw_clusters.items():
    clusters[root] = cl
    cns = {alnum(nodes[i].last["contractNumber-numeroContrat"]) for i in cl if nodes[i].src == "ch"}
    if len(cns) > 1:
        multi_contract += 1
stats["merge"]["clusters_with_multiple_ch_contract_numbers"] = multi_contract
log("clusters", len(clusters), "with multiple CH contract numbers", multi_contract)

# ----------------------------------------------------------------------------- TN index (only needed solicitation numbers)
log("loading TN")
needed_sols = set()
for n in nodes:
    needed_sols |= n.sols
tn_by_sol = collections.defaultdict(list)
tn_rows_total = 0
for chunk in pd.read_csv(TN_CSV, chunksize=20000, dtype=str, keep_default_na=False, encoding="utf-8-sig"):
    tn_rows_total += len(chunk)
    s = chunk["solicitationNumber-numeroSollicitation"].map(alnum)
    sub = chunk[s.isin(needed_sols)]
    for a, row in zip(s[s.isin(needed_sols)], sub.to_dict(orient="records")):
        tn_by_sol[a].append(row)
for a in tn_by_sol:
    tn_by_sol[a].sort(key=lambda r: (r["publicationDate-datePublication"], r["amendmentNumber-numeroModification"]))
stats["tn"]["rows_total"] = tn_rows_total; stats["tn"]["solicitations_indexed"] = len(tn_by_sol)
log("TN indexed solicitations", len(tn_by_sol))

# ----------------------------------------------------------------------------- record building
def first_nonblank(*vals):
    for v in vals:
        if v is not None and str(v).strip() != "":
            return v
    return None

def split_multi(s):
    """CanadaBuys multi-valued cells look like '*GD\\n*SRV'."""
    if not s or not s.strip():
        return None
    parts = [p.strip().lstrip("*").strip() for p in re.split(r"[\n\r]+", s) if p.strip().lstrip("*").strip()]
    return parts or None

out = open(OUT, "w", encoding="utf-8")
written = 0
record_ids = collections.Counter()
excluded = collections.Counter()
by_status = collections.Counter()
by_combo = collections.Counter()
samples = []
tn_guard = collections.Counter()
pd_multi_in_cluster = 0
implausible_end = 0

def build_record(cl):
    global pd_multi_in_cluster, implausible_end
    ns = [nodes[i] for i in cl]
    pds = sorted([n for n in ns if n.src == "pd"], key=lambda n: (-len(n.rows), n.key))
    chs = sorted([n for n in ns if n.src == "ch"], key=lambda n: (-len(n.rows), n.key))
    ans = sorted([n for n in ns if n.src == "an"], key=lambda n: (n.last["publicationDate-datePublication"], n.key), reverse=True)
    primary = (pds or chs or ans)[0]
    # vendor country (primary source decides; other sources noted)
    if not primary.country_ok:
        excluded["vendor_not_canada:" + primary.src] += 1
        return None
    country_notes = []
    for n in ns:
        if n is not primary and n.country_ok is False:
            cv = n.last.get("country_of_vendor") if n.src == "pd" else n.last.get("supplierAddressCountry-fournisseurAdressePays-eng")
            country_notes.append(f"{n.src} reports {cv!r}")
    # cancellation
    for n in chs:
        if n.cancelled:
            excluded["terminated_or_cancelled:ch"] += 1
            return None
    ans_all = list(ans)
    if ans and all(n.cancelled for n in ans):
        if not pds and not chs:
            excluded["cancelled:an_only"] += 1
            return None
        cancel_note = "; ".join(n.cancel_reason for n in ans if n.cancel_reason)
    else:
        cancel_note = None
        if any(n.cancelled for n in ans):
            # drop cancelled award rows from the normalized picture, keep them in raw
            ans = [n for n in ans if not n.cancelled] or ans
    # dates: priority PD > CH > AN (latest row of each)
    end_src = next((n for n in (pds + chs + ans) if n.end is not None), None)
    start_src = next((n for n in (pds + chs + ans) if n.start is not None), None)
    end = end_src.end if end_src else None
    start = start_src.start if start_src else None
    src_name = {"pd": "proactive disclosure", "ch": "CanadaBuys contract history", "an": "CanadaBuys award notice"}
    if end is not None:
        if end < REF_DATE:
            excluded["end_before_ref:" + end_src.src] += 1
            return None
        if start is not None and start > REF_DATE:
            excluded["future_start:" + start_src.src] += 1
            return None
        status = "ongoing"
        lastref = primary.last["reference_number"] if primary.src == "pd" else primary.last["referenceNumber-numeroReference"]
        endfield = {"pd": "delivery_date", "ch": "contractEndDate", "an": "contractEndDate"}[end_src.src]
        startfield = {"pd": "contract_period_start (else contract_date)", "ch": "contractStartDate (else contractAwardDate)", "an": "contractStartDate (else contractAwardDate)"}[start_src.src] if start_src else "n/a"
        basis = f"ongoing: {src_name[end_src.src]} latest row {endfield} {end_src.end_raw} >= {REF}"
        if start_src:
            basis += f" and {src_name[start_src.src]} {startfield} {start_src.start_raw} <= {REF}"
        else:
            basis += "; no parseable start date in any source (status rests on end date alone)"
        if end.year > 2100:
            basis += "; NOTE end date year > 2100 looks like a data-entry error"
            implausible_end += 1
        if primary.src == "ch":
            basis += f"; contractStatus {primary.last['contractStatus-statutContrat-eng'] or 'blank'}"
        if primary.src == "an":
            basis += f"; awardStatus {primary.last['awardStatus-attributionStatut-eng']}"
        if end_src is not primary:
            basis += f" (end date taken from {src_name[end_src.src]}; {src_name[primary.src]} has none)"
    else:
        status = "end_date_unknown"
        if primary.src == "pd":
            basis = f"end_date_unknown: proactive disclosure delivery_date blank/unparseable in all {len(primary.rows)} row(s) (latest {primary.last['reference_number']}, contract_date {primary.last['contract_date']})"
        elif primary.src == "ch":
            basis = f"end_date_unknown: CanadaBuys contract history contractEndDate blank/unparseable ({primary.end_raw!r})"
        else:
            basis = f"end_date_unknown: CanadaBuys award notice {primary.last['referenceNumber-numeroReference']} has blank contractEndDate; awardStatus {primary.last['awardStatus-attributionStatut-eng']}; award date {primary.last['contractAwardDate-dateAttributionContrat']}"
        if len(ns) > 1:
            basis += "; no matched source provides an end date"
    if cancel_note:
        basis += f"; NOTE matched award notice(s) cancelled: {cancel_note}"
    if len(pds) > 1:
        pd_multi_in_cluster += 1

    # ---------------- identifiers
    ids = {}
    if pds:
        p = pds[0]
        ids["pd_owner_org"] = p.buyer_org
        ids["pd_procurement_id"] = p.last["procurement_id"].strip() or None
        ids["pd_reference_number_latest"] = p.last["reference_number"]
        ids["pd_reference_numbers"] = [r["reference_number"] for r in p.rows]
        so = p.last["standing_offer_number"].strip()
        ids["pd_standing_offer_number"] = so if so and so.upper() not in ("NA", "N/A") else None
        if len(pds) > 1:
            ids["pd_additional_groups"] = [{"owner_org": q.buyer_org, "procurement_id": q.last["procurement_id"], "reference_numbers": [r["reference_number"] for r in q.rows]} for q in pds[1:]]
    if chs:
        c = chs[0].last
        ids["ch_reference_number"] = c["referenceNumber-numeroReference"]
        ids["ch_contract_number"] = c["contractNumber-numeroContrat"] or None
        ids["ch_procurement_number"] = c["procurementNumber-numeroApprovisionnement"] or None
        ids["ch_solicitation_number"] = c["solicitationNumber-numeroSollicitation"] or None
        if len(chs) > 1:
            ids["ch_additional_reference_numbers"] = [q.key for q in chs[1:]]
    if ans:
        a = ans[0].last
        ids["an_reference_number_latest"] = a["referenceNumber-numeroReference"]
        ids["an_reference_numbers"] = sorted({r["referenceNumber-numeroReference"] for n in ans for r in n.rows})
        ids["an_contract_number"] = a["contractNumber-numeroContrat"] or None
        ids["an_solicitation_number"] = a["solicitationNumber-numeroSollicitation"] or None

    # ---------------- tender notice enrichment
    tn_row = None; tn_rows = None; tn_basis = None
    tn_candidates = []
    for n in chs + ans:
        for s in n.sols:
            tn_candidates.append((s, n.src, True))
    for n in pds:
        for s in n.sols:
            tn_candidates.append((s, n.src, False))
    for s, src, direct in tn_candidates:
        rows = tn_by_sol.get(s)
        if not rows:
            continue
        if not direct:
            # PD procurement_id matched a tender solicitation number: guard weak ids by buyer agreement
            r = rows[-1]
            pdn = pds[0]
            if not strong_id(pdn.ids.get(s, ("", ""))[1]) and not buyer_agrees(pdn.buyer_org, en_title(pdn.buyer_title), r["contractingEntityName-nomEntitContractante-eng"], r["endUserEntitiesName-nomEntitesUtilisateurFinal-eng"]):
                tn_guard["rejected_weak_id_buyer_mismatch"] += 1
                continue
            tn_guard["accepted_via_pd_" + ("strong_id" if strong_id(pdn.ids.get(s, ("", ""))[1]) else "buyer_agrees")] += 1
            tn_basis = f"proactive disclosure procurement_id matches tender solicitationNumber {rows[-1]['solicitationNumber-numeroSollicitation']!r}"
        else:
            tn_guard["accepted_via_" + src] += 1
            tn_basis = f"CanadaBuys {src} solicitation/procurement number matches tender solicitationNumber {rows[-1]['solicitationNumber-numeroSollicitation']!r}"
        tn_row = rows[-1]; tn_rows = rows
        break
    if tn_row:
        ids["tn_reference_number"] = tn_row["referenceNumber-numeroReference"]
        ids["tn_solicitation_number"] = tn_row["solicitationNumber-numeroSollicitation"]
        if tn_rows and len(tn_rows) > 1:
            ids["tn_reference_numbers_all"] = [r["referenceNumber-numeroReference"] for r in tn_rows]

    # ---------------- contract fields
    contract = {"identifiers": ids}
    related = {}
    if pds:
        p = pds[0]; l = p.last
        contract["title"] = l["description_en"].strip() or None
        desc_parts = [l["comments_en"].strip(), l["additional_comments_en"].strip()]
        contract["description"] = " ".join(x for x in desc_parts if x) or None
        has_sosa = any(r["instrument_type"].strip() == "SOSA" for r in p.rows)
        if has_sosa:
            contract["instrument_type"] = "standing offer / supply arrangement agreement"
        elif ids.get("pd_standing_offer_number") or l["contracting_entity"].strip() in ("DSOSA", "PWSOSA", "SSCSOSA"):
            contract["instrument_type"] = "call-up / contract against standing offer or supply arrangement"
        else:
            contract["instrument_type"] = "contract"
        contract["instrument_type_source_code"] = label("instrument_type", l["instrument_type"])
        contract["solicitation_procedure"] = label("solicitation_procedure", l["solicitation_procedure"])
        contract["procurement_method"] = contract["solicitation_procedure"]
        contract["limited_tendering_reason"] = labels_multi("limited_tendering_reason", l["limited_tendering_reason"])
        contract["award_criteria"] = label("award_criteria", l["award_criteria"])
        contract["number_of_bids"] = int(l["number_of_bids"]) if l["number_of_bids"].strip().isdigit() else None
        contract["trade_agreements"] = labels_multi("trade_agreement", l["trade_agreement"]) or ([label("agreement_type_code", l["agreement_type_code"])] if l["agreement_type_code"].strip() else None)
        contract["commodity"] = {
            "gsin": l["commodity_code"].strip() or None,
            "commodity_type": label("commodity_type", l["commodity_type"]),
            "economic_object_code": l["economic_object_code"].strip() or None,
            "economic_object_description": l["description_en"].strip() or None,
        }
        v = to_num(l["contract_value"])
        contract["value"] = v
        contract["currency"] = "CAD"
        vd = {"pd_total_contract_value": v, "pd_original_value": to_num(l["original_value"]), "pd_latest_amendment_value": to_num(l["amendment_value"]),
              "pd_sum_of_amendment_values_in_rows": round(sum(to_num(r["amendment_value"]) or 0 for r in p.rows), 2),
              "value_source": "proactive disclosure contract_value (latest row)"}
        contract["value_detail"] = vd
        amend_rows = [r for r in p.rows if r["instrument_type"].strip() == "A" or (to_num(r["amendment_value"]) or 0) != 0]
        amended_last = None
        if amend_rows:
            # the proactive-disclosure file has no amendment date; the amendment row's contract_date is usually the original
            # award date, so the reporting quarter is the most reliable indicator -> use the quarter's last day
            q = pd_period(amend_rows[-1])
            m = re.match(r"^(\d{4})-(\d{4})-Q([1-4])$", q)
            if m:
                fy1 = int(m.group(1)); qn = int(m.group(3))
                amended_last = {1: f"{fy1}-06-30", 2: f"{fy1}-09-30", 3: f"{fy1}-12-31", 4: f"{fy1 + 1}-03-31"}[qn]
        contract["dates"] = {
            "published": None,
            "signed": iso(parse_date(p.first["contract_date"])) or iso(parse_date(l["contract_date"])),
            "start": iso(parse_date(l["contract_period_start"])) or iso(parse_date(l["contract_date"])),
            "end": iso(parse_date(l["delivery_date"])) if parse_date(l["delivery_date"]) else (iso(end) if end else None),
            "amended_last": amended_last,
            "amended_last_basis": "last day of the reporting quarter of the latest amendment row (proactive disclosure has no amendment date field)" if amended_last else None,
            "last_reported_period": pd_period(l) or None,
            "first_reported_period": pd_period(p.first) or None,
        }
        if ids.get("pd_standing_offer_number"):
            related["parent_idv_id"] = ids["pd_standing_offer_number"]
        related["proactive_disclosure_record_url"] = pd_record_url(p.buyer_org, l["reference_number"])
    if chs:
        c = chs[0]; l = c.last
        contract.setdefault("title", l["title-titre-eng"].strip() or None)
        if not contract.get("title"):
            contract["title"] = l["title-titre-eng"].strip() or None
        contract["description"] = first_nonblank(contract.get("description"), l["tenderDescription-descriptionAppelOffres-eng"].strip())
        it = l["instrumentType-typeInstrument-eng"].strip()
        if not pds:
            contract["instrument_type"] = {"Contract": "contract", "Contract against SA": "contract against supply arrangement", "Standing Offer": "standing offer",
                                           "Supply Arrangement": "supply arrangement", "Task Authorization Based Contract": "task authorization based contract"}.get(it, it or None)
        contract["canadabuys_instrument_type"] = it or None
        contract["procurement_method"] = first_nonblank(l["procurementMethod-methodeApprovisionnement-eng"].strip(), contract.get("procurement_method"))
        contract.setdefault("solicitation_procedure", l["procurementMethod-methodeApprovisionnement-eng"].strip() or None)
        contract["selection_criteria"] = l["selectionCriteria-criteresSelection-eng"].strip() or None
        contract.setdefault("limited_tendering_reason", split_multi(l["limitedTenderingReason-raisonAppelOffresLimite-eng"]))
        contract.setdefault("trade_agreements", split_multi(l["tradeAgreements-accordsCommerciaux-eng"]))
        com = contract.setdefault("commodity", {})
        com.setdefault("gsin", (split_multi(l["gsin-nibs"]) or [None])[0])
        com["gsin_description"] = " | ".join(split_multi(l["gsinDescription-nibsDescription-eng"]) or []) or None
        com["unspsc"] = " | ".join(split_multi(l["unspsc"]) or []) or None
        com["unspsc_description"] = " | ".join(split_multi(l["unspscDescription-eng"]) or []) or None
        com["procurement_category"] = " | ".join(split_multi(l["procurementCategory-categorieApprovisionnement"]) or []) or None
        tot = to_num(l["totalContractValue-valeurTotaleContrat"]); amt = to_num(l["contractAmount-montantContrat"])
        orig = to_num(c.first["contractAmount-montantContrat"])
        vd = contract.setdefault("value_detail", {})
        vd.update({"ch_total_contract_value": tot, "ch_latest_row_contract_amount": amt, "ch_original_contract_amount": orig,
                   "ch_currency": l["contractCurrency-contratMonnaie"] or None, "ch_number_of_records": l["numberOfRecords-nombreEnregistrements"] or None})
        if contract.get("value") is None:
            contract["value"] = tot if (tot not in (None, 0)) else amt
            contract["currency"] = l["contractCurrency-contratMonnaie"] or None
            vd["value_source"] = "CanadaBuys contract history totalContractValue (latest row)" if (tot not in (None, 0)) else "CanadaBuys contract history contractAmount (latest row)"
        d = contract.setdefault("dates", {})
        d["published"] = first_nonblank(d.get("published"), iso(parse_date(c.first["publicationDate-datePublication"])))
        d["signed"] = first_nonblank(d.get("signed"), iso(parse_date(l["contractAwardDate-dateAttributionContrat"])))
        d["start"] = first_nonblank(d.get("start"), iso(parse_date(l["contractStartDate-contratDateDebut"])), iso(parse_date(l["contractAwardDate-dateAttributionContrat"])))
        d["end"] = first_nonblank(d.get("end"), iso(parse_date(l["contractEndDate-dateFinContrat"])))
        am = [parse_date(r["amendmentDate-dateModification"]) for r in c.rows if parse_date(r["amendmentDate-dateModification"])]
        d["amended_last"] = first_nonblank(d.get("amended_last"), iso(max(am)) if am else None)
        d["ch_end_date"] = iso(parse_date(l["contractEndDate-dateFinContrat"]))
        related["regions_of_delivery"] = split_multi(l["regionsOfDelivery-regionsLivraison-eng"])
    if ans:
        a = ans[0]; l = a.last
        if not contract.get("title"):
            contract["title"] = l["title-titre-eng"].strip() or None
        contract["description"] = first_nonblank(contract.get("description"), l["awardDescription-descriptionAttribution-eng"].strip())
        it = l["instrumentType-typeInstrument-eng"].strip()
        if not pds and not chs:
            contract["instrument_type"] = {"Contract": "contract", "Contract against SA": "contract against supply arrangement", "Standing Offer": "standing offer",
                                           "Supply Arrangement": "supply arrangement", "Task Authorization Based Contract": "task authorization based contract"}.get(it, it or None)
        contract.setdefault("canadabuys_instrument_type", it or None)
        contract["procurement_method"] = first_nonblank(contract.get("procurement_method"), l["procurementMethod-methodeApprovisionnement-eng"].strip())
        contract.setdefault("solicitation_procedure", l["procurementMethod-methodeApprovisionnement-eng"].strip() or None)
        contract.setdefault("selection_criteria", l["selectionCriteria-criteresSelection-eng"].strip() or None)
        contract.setdefault("limited_tendering_reason", split_multi(l["limitedTenderingReason-raisonAppelOffresLimite-eng"]))
        contract.setdefault("trade_agreements", split_multi(l["tradeAgreements-accordsCommerciaux-eng"]))
        contract["notice_type"] = l["noticeType-avisType-eng"].strip() or None
        com = contract.setdefault("commodity", {})
        com.setdefault("gsin", (split_multi(l["gsin-nibs"]) or [None])[0])
        com.setdefault("gsin_description", " | ".join(split_multi(l["gsinDescription-nibsDescription-eng"]) or []) or None)
        com.setdefault("unspsc", " | ".join(split_multi(l["unspsc"]) or []) or None)
        com.setdefault("unspsc_description", " | ".join(split_multi(l["unspscDescription-eng"]) or []) or None)
        com.setdefault("procurement_category", " | ".join(split_multi(l["procurementCategory-categorieApprovisionnement"]) or []) or None)
        tot = to_num(l["totalContractValue-valeurTotaleContrat"]); amt = to_num(l["contractAmount-montantContrat"])
        vd = contract.setdefault("value_detail", {})
        vd.update({"an_total_contract_value": tot, "an_contract_amount": amt, "an_currency": l["contractCurrency-contratMonnaie"] or None})
        if contract.get("value") is None:
            contract["value"] = tot if (tot not in (None, 0)) else amt
            contract["currency"] = l["contractCurrency-contratMonnaie"] or None
            vd["value_source"] = "CanadaBuys award notice totalContractValue" if (tot not in (None, 0)) else "CanadaBuys award notice contractAmount"
        d = contract.setdefault("dates", {})
        d["published"] = first_nonblank(d.get("published"), iso(parse_date(a.first["publicationDate-datePublication"])))
        d["signed"] = first_nonblank(d.get("signed"), iso(parse_date(l["contractAwardDate-dateAttributionContrat"])))
        d["start"] = first_nonblank(d.get("start"), iso(parse_date(l["contractStartDate-contratDateDebut"])), iso(parse_date(l["contractAwardDate-dateAttributionContrat"])))
        d["end"] = first_nonblank(d.get("end"), iso(parse_date(l["contractEndDate-dateFinContrat"])))
        am = [parse_date(r["amendmentDate-dateModification"]) for r in a.rows if parse_date(r["amendmentDate-dateModification"])]
        d["amended_last"] = first_nonblank(d.get("amended_last"), iso(max(am)) if am else None)
        d["an_end_date"] = iso(parse_date(l["contractEndDate-dateFinContrat"]))
        related["award_notice_url"] = cb_notice_url("award-notice", l["referenceNumber-numeroReference"])
        related.setdefault("regions_of_delivery", split_multi(l["regionsOfDelivery-regionsLivraison-eng"]))
    if tn_row:
        related["tender_notice_url"] = cb_notice_url("tender-notice", tn_row["referenceNumber-numeroReference"])
        related["tender_notice_external_url"] = tn_row["noticeURL-URLavis-eng"].strip() or None
        related["tender_notice_match_basis"] = tn_basis
        related["tender_notice_status"] = tn_row["tenderStatus-appelOffresStatut-eng"] or None
        related["tender_notice_closing_date"] = tn_row["tenderClosingDate-appelOffresDateCloture"] or None
    contract["related"] = {k: v for k, v in related.items() if v is not None}
    for k in ["title", "description", "instrument_type", "procurement_method", "solicitation_procedure", "value", "currency"]:
        contract.setdefault(k, None)
    contract.setdefault("commodity", {}); contract.setdefault("value_detail", {}); contract.setdefault("dates", {})

    # ---------------- buyer
    buyer = {}
    if pds:
        p = pds[0]; l = p.last
        buyer["name"] = en_title(l["owner_org_title"])
        buyer["country"] = "CA"
        buyer["type"] = buyer_type(buyer["name"])
        buyer["identifiers"] = {"owner_org": p.buyer_org, "owner_org_title": l["owner_org_title"],
                                "contracting_entity_code": l["contracting_entity"].strip() or None,
                                "contracting_entity": label("contracting_entity", l["contracting_entity"]),
                                "ministers_office": label("ministers_office", l["ministers_office"])}
        buyer["address"] = {}
        bn = l["buyer_name"].strip()
        buyer["contact"] = {"contracting_authority_name": bn if bn and bn.upper() not in ("NA", "N/A") else None}
        if chs or ans:
            l2 = (chs or ans)[0].last
            buyer["identifiers"]["canadabuys_contracting_entity"] = l2["contractingEntityName-nomEntitContractante-eng"] or None
            buyer["identifiers"]["canadabuys_end_user_entity"] = l2["endUserEntitiesName-nomEntitesUtilisateurFinal-eng"] or None
    else:
        l = (chs or ans)[0].last
        end_user = l["endUserEntitiesName-nomEntitesUtilisateurFinal-eng"].strip()
        ce = l["contractingEntityName-nomEntitContractante-eng"].strip()
        # CanadaBuys contractingEntityName is sometimes a person (the contracting officer typed into the organization
        # field, e.g. 'Sylvie Gallant'); fall back to the end-user entity or the contact organisation in that case.
        PERSON_RE = re.compile(r"^[A-Z][a-zé]+(?: [A-Z]\.)? [A-Z][a-zé]+(?:-[A-Z][a-z]+)?$")
        ORGWORD_RE = re.compile(r"canada|defence|defense|parks|health|transport|heritage|statistics|infrastructure|environment|elections|industry|telefilm|marine|atlantic|recruitment|agency|department|commission|board|council|service|office|bank|corporation|authority|institute|centre|center|museum|library|school|college|university|secretariat|tribunal|program|bureau|general|headquarters", re.I)
        def looks_person(x):
            return bool(x) and bool(PERSON_RE.match(x)) and not ORGWORD_RE.search(x)
        name_note = None
        if looks_person(ce) and not end_user:
            alt = l["contactInfoName-informationsContactNom"].strip()
            email_dom = re.search(r"@([a-z0-9.-]+)", l["contactInfoEmail-informationsContactCourriel"].strip().lower())
            if alt and not looks_person(alt):
                name_note = f"contractingEntityName {ce!r} looks like a person's name; buyer.name taken from contactInfoName"
                ce = alt
            elif email_dom and email_dom.group(1).endswith(".gc.ca") and email_dom.group(1) not in ("gc.ca", "canada.ca"):
                dom = email_dom.group(1)
                name_note = f"contractingEntityName {ce!r} looks like a person's name; buyer identified only by contact e-mail domain {dom}"
                ce = f"Government of Canada organization (contact e-mail domain {dom})"
            else:
                name_note = f"contractingEntityName {ce!r} looks like a person's name (contracting officer); no organization name available in the record"
                ce = f"Government of Canada organization (contracting officer {ce})"
        buyer["name"] = end_user or ce or None
        buyer["country"] = "CA"
        buyer["type"] = buyer_type(buyer["name"])
        if name_note:
            buyer["name_note"] = name_note
        buyer["identifiers"] = {"canadabuys_contracting_entity": l["contractingEntityName-nomEntitContractante-eng"].strip() or None, "canadabuys_end_user_entity": end_user or None,
                                "canadabuys_end_user_office": (l.get("endUserEntitiesOfficeName-bureauNomEntitesUtilisateurFinal-eng") or "").strip() or None}
        buyer["address"] = {"line1": l["contractingEntityAddressLine-ligneAdresseEntiteContractante-eng"].strip() or None,
                            "city": l["contractingEntityAddressCity-entiteContractanteAdresseVille-eng"].strip() or None,
                            "region": l["contractingEntityAddressProvince-entiteContractanteAdresseProvince-eng"].strip() or None,
                            "postal_code": l["contractingEntityAddressPostalCode-entiteContractanteAdresseCodePostal"].strip() or None,
                            "country": l["contractingEntityAddressCountry-entiteContractanteAdressePays-eng"].strip() or None,
                            "end_user_address": l["endUserEntitiesAddress-adresseEntitesUtilisateurFinal-eng"].strip() or None}
        buyer["contact"] = {"name": l["contactInfoName-informationsContactNom"].strip() or None, "email": l["contactInfoEmail-informationsContactCourriel"].strip() or None,
                            "phone": l["contactInfoPhone-contactInfoTelephone"].strip() or None, "fax": l["contactInfoFax"].strip() or None,
                            "address": " ".join(x for x in [l["contactInfoAddressLine-contactInfoAdresseLigne-eng"].strip(), l["contactInfoCity-contacterInfoVille-eng"].strip(), l["contactInfoProvince-contacterInfoProvince-eng"].strip(), l["contactInfoPostalcode"].strip(), l["contactInfoCountry-contactInfoPays-eng"].strip()] if x) or None}
        if l["contractingEntityAddressCountry-entiteContractanteAdressePays-eng"].strip() and not is_canada_label(l["contractingEntityAddressCountry-entiteContractanteAdressePays-eng"]):
            buyer["country"] = l["contractingEntityAddressCountry-entiteContractanteAdressePays-eng"].strip()

    # ---------------- vendor
    vendor = {"name": primary.vendor or None, "country": "CA", "country_basis": primary.country_basis + ("; " + "; ".join(country_notes) if country_notes else ""),
              "identifiers": {}, "address": {}, "contact": {}}
    if pds:
        l = pds[0].last
        vendor["identifiers"]["pd_vendor_name_latest"] = l["vendor_name"].strip() or None
        variants = sorted({r["vendor_name"].strip() for r in pds[0].rows if r["vendor_name"].strip()})
        if len(variants) > 1:
            vendor["identifiers"]["pd_vendor_name_variants"] = variants
        vendor["address"]["postal_code_fsa"] = l["vendor_postal_code"].strip() if l["vendor_postal_code"].strip().upper() not in ("", "NA") else None
        vendor["identifiers"]["pd_former_public_servant"] = label("former_public_servant", l["former_public_servant"])
        vendor["identifiers"]["pd_indigenous_business"] = label("indigenous_business", l["indigenous_business"])
        vendor["identifiers"]["pd_indigenous_business_excluding_psib"] = label("indigenous_business_excluding_psib", l["indigenous_business_excluding_psib"])
    if chs or ans:
        l = (chs or ans)[0].last
        vendor["identifiers"]["canadabuys_legal_name"] = l["supplierLegalName-nomLegalFournisseur-eng"].strip() or None
        if chs:
            vendor["identifiers"]["canadabuys_operating_name"] = l["supplierOperatingName-nomCommercialFournisseur-eng"].strip() or None
            vendor["identifiers"]["canadabuys_standardized_name"] = l["supplierStandardizedName-nomNormaliseFournisseur-eng"].strip() or None
            vendor["employee_count"] = l["supplierEmployeeCount-fournisseurNombreEmployes-eng"].strip() or None
        vendor["address"].update({"line1": l["supplierAddressLine-ligneAdresseFournisseur-eng"].strip() or None,
                                  "city": l["supplierAddressCity-fournisseurAdresseVille-eng"].strip() or None,
                                  "region": l["supplierAddressProvince-fournisseurAdresseProvince-eng"].strip() or None,
                                  "postal_code": l["supplierAddressPostalCode-fournisseurAdresseCodePostal"].strip() or None,
                                  "country": l["supplierAddressCountry-fournisseurAdressePays-eng"].strip() or None})
        if not pds and names_agree(chs[0].vendor if chs else "", ans[0].vendor if ans else "") is False and chs and ans:
            vendor["identifiers"]["an_legal_name"] = ans[0].vendor
    if not vendor["address"].get("country"):
        vendor["address"]["country"] = "CA"

    # ---------------- raw
    raw = {}
    if pds:
        p = pds[0]
        raw["proactive_disclosure"] = {
            "owner_org": p.buyer_org, "group_key": p.key, "n_rows": len(p.rows), "rows": p.rows,
            "row_urls": [pd_record_url(r["owner_org"], r["reference_number"]) for r in p.rows],
            "resource_url": RESOURCE_URL["pd"], "retrieved_at": RETRIEVED["pd"],
        }
        if len(pds) > 1:
            raw["proactive_disclosure"]["additional_groups"] = [{"owner_org": q.buyer_org, "group_key": q.key, "rows": q.rows, "row_urls": [pd_record_url(r["owner_org"], r["reference_number"]) for r in q.rows]} for q in pds[1:]]
    if chs:
        raw["canadabuys_contract_history"] = {"reference_number": chs[0].key, "n_rows": len(chs[0].rows), "rows": chs[0].rows, "resource_url": RESOURCE_URL["ch"], "retrieved_at": RETRIEVED["ch"]}
        if len(chs) > 1:
            raw["canadabuys_contract_history"]["additional_groups"] = [{"reference_number": q.key, "rows": q.rows} for q in chs[1:]]
    if ans:
        raw["canadabuys_award_notice"] = {"group_key_solicitation_supplier": ans[0].key, "n_rows": sum(len(n.rows) for n in ans_all), "rows": [r for n in ans_all for r in n.rows], "resource_url": RESOURCE_URL["an"], "retrieved_at": RETRIEVED["an"]}
        if len(ans_all) > len(ans):
            raw["canadabuys_award_notice"]["cancelled_award_reference_numbers"] = [n.key for n in ans_all if n.cancelled]
    if tn_row:
        raw["related_tender_notice"] = tn_row
        if tn_rows and len(tn_rows) > 1:
            raw["related_tender_notice_rows"] = tn_rows
        raw["related_tender_notice_meta"] = {"resource_url": RESOURCE_URL["tn"], "retrieved_at": RETRIEVED["tn"], "match_basis": tn_basis}
    if len(ns) > 1:
        bases = []
        for i in cl:
            for j in cl:
                if i < j and (i, j) in merge_pairs:
                    bases.append(merge_pairs[(i, j)])
        raw["merge"] = {"sources": sorted({n.src for n in ns}), "basis": bases}

    # ---------------- record id / source
    if pds:
        p = pds[0]
        pidn = norm_id(p.last["procurement_id"])
        rid = f"canada_federal:{p.buyer_org}:{pidn if not degenerate(pidn) else p.last['reference_number'].strip()}"
        record_url = pd_record_url(p.buyer_org, p.last["reference_number"])
    elif chs:
        rid = f"canada_federal:cb:{chs[0].key}"
        record_url = related.get("award_notice_url")
    else:
        rid = f"canada_federal:cb:{ans[0].key}"
        record_url = related.get("award_notice_url")
    srcs = []
    if pds: srcs.append("pd")
    if chs: srcs.append("ch")
    if ans: srcs.append("an")
    names = {"pd": "Proactive Publication – Contracts over $10,000", "ch": "CanadaBuys contract history", "an": "CanadaBuys award notices"}
    pubs = {"pd": "Treasury Board of Canada Secretariat / reporting federal organizations (open.canada.ca)", "ch": "Public Services and Procurement Canada (CanadaBuys)", "an": "Public Services and Procurement Canada (CanadaBuys)"}
    source = {
        "key": "canada_federal",
        "name": " + ".join(names[s] for s in srcs) + (" (+ CanadaBuys tender notice)" if tn_row else ""),
        "publisher": "; ".join(dict.fromkeys(pubs[s] for s in srcs)),
        "dataset_url": DATASET_URL[srcs[0]],
        "dataset_urls": {s: DATASET_URL[s] for s in srcs + (["tn"] if tn_row else [])},
        "record_url": record_url,
        "retrieved_at": max(RETRIEVED[s] for s in srcs),
    }
    combo = "+".join(srcs) + ("+tn" if tn_row else "")
    rec = {"record_id": rid, "source": source, "status": status, "status_basis": basis, "contract": contract, "buyer": buyer, "vendor": vendor, "raw": raw}
    return rec, combo

log("writing records")
n_err = 0
for ci, (root, cl) in enumerate(clusters.items()):
    try:
        res = build_record(cl)
    except Exception as e:
        n_err += 1
        log("ERROR cluster", [nodes[i].key for i in cl], repr(e)); log(traceback.format_exc()[-1500:])
        continue
    if res is None:
        continue
    rec, combo = res
    rid = rec["record_id"]
    record_ids[rid] += 1
    if record_ids[rid] > 1:
        rec["record_id"] = f"{rid}#{record_ids[rid]}"
        stats["record_id_collisions"][rid] += 1
    out.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
    written += 1
    by_status[rec["status"]] += 1
    by_combo[combo] += 1
    if len(samples) < 5 and combo not in {s["_combo"] for s in samples} and (combo != "pd" or rec["status"] == "ongoing"):
        s = {k: v for k, v in rec.items() if k != "raw"}
        s["_combo"] = combo
        s["raw_keys"] = {k: (len(v["rows"]) if isinstance(v, dict) and "rows" in v else "present") for k, v in rec["raw"].items()}
        samples.append(s)
    if written % 5000 == 0:
        out.flush(); log(f"  written {written}")
out.close()

stats["output"] = {"records_written": written, "by_status": dict(by_status), "by_source_combination": dict(by_combo), "excluded_clusters": dict(excluded),
                   "clusters_total": len(clusters), "build_errors": n_err, "tn_guard": dict(tn_guard), "clusters_with_multiple_pd_groups": pd_multi_in_cluster,
                   "implausible_end_dates_kept": implausible_end}
stats["samples"] = samples
json.dump({k: (dict(v) if isinstance(v, collections.Counter) else v) for k, v in stats.items()}, open(STATS, "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=str)
log("DONE written", written, "by_status", dict(by_status))
