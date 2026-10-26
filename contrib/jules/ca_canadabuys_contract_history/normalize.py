#!/usr/bin/env python3
"""Build normalized/canada_federal_legacy.jsonl from the CanadaBuys LEGACY files:
  CHL = "Legacy contract history, 2009-01 to 2023-05 (prior to CanadaBuys)"   (dataset 4fe645a1-...)
  ANL = "Legacy award notices, 2012 to 2022-08 (prior to CanadaBuys)"           (dataset a1acb126-...)
keeping Canadian-located suppliers whose contract is ongoing on 2026-10-25 (or published without an end date), and
dropping anything already present in normalized/canada_federal.jsonl or superseded by newer data in the CanadaBuys
complete files / the proactive-disclosure file.

Usage: python3 -I build.py <legacy_dir> <canada_federal_downloads_dir> <cf_index.jsonl.gz> <out.jsonl> <stats.json>
"""
import sys, os, re, json, gzip, collections, datetime, time
import pandas as pd

REF = "2026-10-25"
REF_DATE = datetime.date(2026, 10, 25)
LD, FD, IDX, OUT, STATS = [a.rstrip("/") for a in sys.argv[1:6]]


def pick(path):
    return path if os.path.exists(path) else path + ".gz"


CHL = pick(LD + "/2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv")
ANL = pick(LD + "/2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv")
CHC = pick(FD + "/contractHistoryComplete-contratsOctroyesComplet.csv")
ANC = pick(FD + "/awardNoticeComplete-avisAttributionComplet.csv")
PDF = pick(FD + "/contracts.csv")

RETRIEVED = {"chl": "2026-10-26T02:59:40Z", "anl": "2026-10-26T02:59:50Z"}  # downloads/canada_federal_legacy/download.log
DATASET = {"chl": "https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4",
           "anl": "https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb"}
RESOURCE = {"chl": "https://canadabuys.canada.ca/opendata/pub/2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv",
            "anl": "https://canadabuys.canada.ca/opendata/pub/2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv"}
RESOURCE_NAME = {"chl": "Legacy contract history, 2009-01 to 2023-05 (prior to CanadaBuys)",
                 "anl": "Legacy award notices, 2012 to 2022-08 (prior to CanadaBuys)"}

LOGF = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", "build.log"), "a", encoding="utf-8")


def log(*a):
    msg = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + " " + " ".join(str(x) for x in a)
    print(msg, file=sys.stderr, flush=True)
    LOGF.write(msg + "\n"); LOGF.flush()


stats = collections.defaultdict(collections.Counter)


# ----------------------------------------------------------------------------- helpers (same rules as canada_federal/build.py)
def norm_id(s):
    return re.sub(r"\s+", "", (s or "").strip().upper())


def alnum(s):
    return re.sub(r"[^A-Z0-9]", "", (s or "").upper())


DEGENERATE_IDS = {"", "NULL", "N/A", "NA", "NONE", "0", "-", "--", "TBD", "UNKNOWN", "ACQUISITIONCARD", "ACQUISITIONCARDS",
                  "VARIOUS", "MULTIPLE", "SEECOMMENTS", "CARD", "NIL", "X", "XX", "XXX", "N.A.", "NOTAPPLICABLE", "NOTAVAILABLE"}


def degenerate(s):
    s = norm_id(s)
    return s in DEGENERATE_IDS or len(alnum(s)) < 4


STRONG_ID_RE = re.compile(r"^(?:[A-Z0-9]{5,6}-[A-Z0-9]{6,}(?:[/:]\d{3}[/:][A-Z0-9]{2,6})?|CW\d{7}|WS\d{10}|[A-Z]{1,3}\d{2,3}[A-Z]{1,2}-\d{2}[A-Z0-9]{4,}(?:[/:]\d{3}[/:][A-Z0-9]{2,6})?)$")


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


CANADA_VALUES = {"CA", "CAN", "CANADA", "CANADA(CA)", "CANADÁ", "CANDA", "CANANDA", "CANANA", "CANAD"}


def is_canada_label(s):
    return re.sub(r"[\s`'\".]", "", (s or "")).upper() in CANADA_VALUES


def name_tokens(s):
    s = (s or "").upper().replace("&", " AND ")
    return {t for t in re.findall(r"[A-Z0-9ÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ]+", s) if len(t) >= 3}


TOKEN_DF = collections.Counter()
CORP_SUFFIX = {"INC", "LTD", "LTEE", "LTÉE", "LIMITED", "LIMITEE", "LIMITÉE", "CORP", "CORPORATION", "CO", "COMPANY", "LLC", "LP", "LLP",
               "ULC", "PLC", "GMBH", "SRL", "SAS", "INCORPORATED", "ENR", "SENC", "SENCRL", "SEC", "THE", "AND", "CANADA"}


def core_tokens(s):
    return {t for t in name_tokens(s) if TOKEN_DF.get(t, 0) <= 40 and t not in CORP_SUFFIX}


def names_agree(a, b):
    if not a or not b:
        return False
    na, nb = alnum(a), alnum(b)
    if na and nb and (na == nb or (min(len(na), len(nb)) >= 8 and (na.startswith(nb) or nb.startswith(na)))):
        return True
    return bool(core_tokens(a) & core_tokens(b))


CANCEL_VENDOR_RE = re.compile(r"cancel|no contract|not awarded|no award|annul", re.I)


def cb_notice_url(kind, ref):
    slug = (ref or "").strip().lower()
    if re.fullmatch(r"(cb-\d+-\d+|mx-\d+|ws\d+-doc\d+|pw-\d{2}-\d{8}(-\d+)?|cw\d+)", slug):
        return f"https://canadabuys.canada.ca/en/tender-opportunities/{kind}/{slug}"
    return None


CROWN_RE = re.compile(r"bank of canada|business development bank|farm credit|export development|canada post|deposit insurance|marine atlantic|\bvia\b|canada lands|national capital commission|defence construction|old port|downsview|telefilm|commercial corporation|mortgage and housing|atomic energy|museum|national gallery|film board|pilotage|royal canadian mint|infrastructure bank|dairy commission|freshwater fish|windsor-detroit|jacques cartier|air transport security|development investment|standards council|development research centre|broadcasting corporation|council for the arts|destination canada|race relations|pension investment|ingenium|canadian commercial", re.I)


def buyer_type(name):
    return "crown corporation" if CROWN_RE.search(name or "") else "federal department or agency"


def split_multi(s):
    if not s or not s.strip():
        return None
    parts = [p.strip().lstrip("*").strip() for p in re.split(r"[\n\r]+", s) if p.strip().lstrip("*").strip()]
    return parts or None


def first_nonblank(*vals):
    for v in vals:
        if v is not None and str(v).strip() != "":
            return v
    return None


def amend_key(s):
    s = (s or "").strip()
    return (0, int(s), "") if s.isdigit() else (1, 0, s)


C_REF, C_CN = "referenceNumber-numeroReference", "contractNumber-numeroContrat"
C_AMD, C_PUB = "amendmentNumber-numeroModification", "publicationDate-datePublication"
C_AWD, C_STA, C_END = "contractAwardDate-dateAttributionContrat", "contractStartDate-contratDateDebut", "contractEndDate-dateFinContrat"
C_CTRY, C_CTRYF, C_PC = "supplierAddressCountry-fournisseurAdressePays-eng", "supplierAddressCountry-fournisseurAdressePays-fra", "supplierAddressPostalCode-fournisseurAdresseCodePostal"
C_LEG, C_OPN, C_STD = "supplierLegalName-nomLegalFournisseur-eng", "supplierOperatingName-nomCommercialFournisseur-eng", "supplierStandardizedName-nomNormaliseFournisseur-eng"
C_SOL, C_PROC = "solicitationNumber-numeroSollicitation", "procurementNumber-numeroApprovisionnement"
C_ATYPE, C_ADATE = "amendmentType-typeModification-eng", "amendmentDate-dateModification"
C_CHST, C_ANST = "contractStatus-statutContrat-eng", "awardStatus-attributionStatut-eng"
C_INST = "instrumentType-typeInstrument-eng"


def country_of(row):
    ce, cf = row.get(C_CTRY, ""), row.get(C_CTRYF, "")
    if is_canada_label(ce) or is_canada_label(cf):
        return True, f"{C_CTRY} = {ce.strip() or cf.strip()!r}"
    if ce.strip() == "" and cf.strip() == "" and canadian_postal(row.get(C_PC, "")):
        return True, f"{C_PC} pattern {row.get(C_PC, '').strip()!r} ({C_CTRY} blank)"
    return False, None


def read_csv_chunks(path, usecols=None):
    return pd.read_csv(path, chunksize=50000, dtype=str, keep_default_na=False, encoding="utf-8-sig", usecols=usecols,
                       compression="gzip" if path.endswith(".gz") else None)


# ============================================================================= 1. CHL pass 1: latest row per contract
log("CHL pass 1", CHL)
CHL_COLS1 = [C_REF, C_CN, C_AMD, C_PUB, C_AWD, C_STA, C_END, C_CTRY, C_CTRYF, C_PC, C_LEG, C_OPN, C_STD, C_ATYPE, C_ADATE, C_CHST, C_INST, C_PROC, C_SOL]
chl_last = {}   # ref -> (sortkey, summary dict)
chl_nrows = collections.Counter()
for chunk in read_csv_chunks(CHL, CHL_COLS1):
    for row in chunk.to_dict(orient="records"):
        ref = row[C_REF].strip()
        if not ref:
            stats["chl"]["blank_ref_rows"] += 1
            continue
        chl_nrows[ref] += 1
        k = (amend_key(row[C_AMD]), row[C_PUB])
        cur = chl_last.get(ref)
        if cur is None or k >= cur[0]:
            chl_last[ref] = (k, row)
    stats["chl"]["rows"] += len(chunk)
log("CHL contracts", len(chl_last), "rows", stats["chl"]["rows"])
stats["chl"]["contracts"] = len(chl_last)

# id index for CHL (alnum contract number / reference number -> ref)
chl_by_id = collections.defaultdict(set)
for ref, (k, row) in chl_last.items():
    for v in (ref, row[C_CN]):
        if v and not degenerate(v):
            chl_by_id[alnum(v)].add(ref)


def chl_decide(ref):
    """returns (is_candidate, reason, info dict)"""
    row = chl_last[ref][1]
    ok, basis = country_of(row)
    info = {"country_ok": ok, "country_basis": basis}
    if not ok:
        return False, "vendor_not_canada", info
    if row[C_ATYPE].strip() == "Termination":
        return False, "terminated", info
    if row[C_CHST].strip() == "Cancelled":
        return False, "cancelled", info
    end = parse_date(row[C_END]); start = parse_date(row[C_STA]) or parse_date(row[C_AWD])
    info.update({"end": end, "start": start})
    if end is None:
        # (CHL has an end date on every row; kept for completeness)
        return True, "end_blank", info
    if end < REF_DATE:
        return False, "end_before_ref", info
    if start is not None and start > REF_DATE:
        return False, "future_start", info
    return True, "end_on_or_after_ref", info


chl_cand = {}
for ref in chl_last:
    c, reason, info = chl_decide(ref)
    stats["chl_decision"][reason] += 1
    if c:
        chl_cand[ref] = info
log("CHL candidates", len(chl_cand))

# ============================================================================= 2. ANL pass 1: notice groups
log("ANL pass 1", ANL)
ANL_COLS1 = [C_REF, C_CN, C_AMD, C_PUB, C_AWD, C_STA, C_END, C_CTRY, C_CTRYF, C_PC, C_LEG, C_ATYPE, C_ANST, C_INST, C_SOL,
             "supplierLegalName-nomLegalFournisseur-fra"]
anl_rows = {}  # ref -> summary
for chunk in read_csv_chunks(ANL, ANL_COLS1):
    for row in chunk.to_dict(orient="records"):
        ref = row[C_REF].strip()
        if not ref:
            stats["anl"]["blank_ref_rows"] += 1
            continue
        if ref in anl_rows:
            stats["anl"]["duplicate_ref_rows"] += 1
            ref = ref + "#dup" + str(stats["anl"]["duplicate_ref_rows"])
        anl_rows[ref] = row
    stats["anl"]["rows"] += len(chunk)
log("ANL rows", len(anl_rows))


def anl_group_key(row, ref):
    sol = alnum(row[C_SOL]); sup = alnum(row[C_LEG])[:40]; cn = "" if degenerate(row[C_CN]) else alnum(row[C_CN])
    return (sol + "|" + sup + "|" + cn) if (cn and sol) else ("REF|" + ref)


anl_groups = collections.defaultdict(list)
for ref, row in anl_rows.items():
    anl_groups[anl_group_key(row, ref)].append(ref)
for g, refs in anl_groups.items():
    refs.sort(key=lambda r: (anl_rows[r][C_PUB], amend_key(anl_rows[r][C_AMD])))
stats["anl"]["groups"] = len(anl_groups)


def anl_decide(g):
    refs = anl_groups[g]
    row = anl_rows[refs[-1]]
    vendor = row[C_LEG].strip() or row.get("supplierLegalName-nomLegalFournisseur-fra", "").strip()
    ok, basis = country_of(row)
    info = {"country_ok": ok, "country_basis": basis, "vendor": vendor}
    if CANCEL_VENDOR_RE.search(vendor or "") and len(vendor or "") > 25:
        return False, "supplier_field_is_cancellation_note", info
    if not ok:
        return False, "vendor_not_canada", info
    if row[C_ANST].strip() == "Cancelled":
        return False, "cancelled", info
    if row[C_ATYPE].strip() == "Termination":
        return False, "terminated", info
    end = parse_date(row[C_END]); start = parse_date(row[C_STA]) or parse_date(row[C_AWD])
    info.update({"end": end, "start": start})
    if start is not None and start > REF_DATE:
        return False, "future_start", info
    if end is None:
        return True, "end_blank", info
    if end < REF_DATE:
        return False, "end_before_ref", info
    return True, "end_on_or_after_ref", info


# token DF over distinct vendor names (CHL latest rows + ANL)
_names = set()
for ref, (k, row) in chl_last.items():
    _names.add((row[C_LEG] or row[C_OPN] or row[C_STD]).strip().upper())
for ref, row in anl_rows.items():
    _names.add(row[C_LEG].strip().upper())
for line in gzip.open(IDX, "rt", encoding="utf-8"):
    for nm in json.loads(line)["vendors"]:
        _names.add(nm.strip().upper())
for nm in _names:
    if nm:
        TOKEN_DF.update(name_tokens(nm))
stats["name_tokens"]["distinct_vendor_names"] = len(_names)
del _names

# ============================================================================= 3. link ANL groups to CHL contracts
anl_to_chl = {}       # group -> (chl ref, basis)
chl_attached = collections.defaultdict(list)  # chl ref -> [groups]
anl_cand = {}         # group -> info (ANL-only candidates)
for g, refs in anl_groups.items():
    c, reason, info = anl_decide(g)
    stats["anl_decision_own"][reason] += 1
    hit = None
    for r in reversed(refs):
        row = anl_rows[r]
        for v in (row[C_CN], r.split("#dup")[0]):
            if not v or degenerate(v):
                continue
            for cref in chl_by_id.get(alnum(v), ()):
                crow = chl_last[cref][1]
                cvend = (crow[C_LEG] or crow[C_OPN] or crow[C_STD]).strip()
                if strong_id(v) or strong_id(crow[C_CN]) or names_agree(cvend, info.get("vendor") or row[C_LEG]):
                    hit = (cref, f"ANL {('contractNumber' if v == row[C_CN] else 'referenceNumber')} {v!r} = CHL contract {cref!r}" + ("" if names_agree(cvend, info.get('vendor') or row[C_LEG]) else f" (strong id; vendor names differ: {cvend!r} vs {(info.get('vendor') or row[C_LEG])!r})"))
                    break
                else:
                    stats["anl_chl_link"]["rejected_weak_id_vendor_mismatch"] += 1
            if hit:
                break
        if hit:
            break
    if hit:
        cref = hit[0]
        anl_to_chl[g] = hit
        if cref in chl_cand:
            chl_attached[cref].append(g)
            stats["anl_chl_link"]["linked_to_chl_candidate"] += 1
            if c:
                stats["anl_chl_link"]["anl_candidate_merged_into_chl_candidate"] += 1
        else:
            stats["anl_chl_link"]["linked_to_chl_noncandidate"] += 1
            if c:
                c2, reason2, _ = chl_decide(cref)
                stats["anl_resolved_by_chl_excluded"][reason2] += 1
        continue
    if c:
        anl_cand[g] = info
        stats["anl_only_candidates"][reason] += 1
log("ANL linked to CHL", len(anl_to_chl), "ANL-only candidates", len(anl_cand))

# ============================================================================= 4. candidate id sets
cand_units = []  # (kind, key)
unit_ids = {}    # (kind,key) -> {alnum: original}
unit_vendor = {}
for ref in chl_cand:
    row = chl_last[ref][1]
    ids = {}
    for v in (ref, row[C_CN]):
        if v and not degenerate(v):
            ids.setdefault(alnum(v), v)
    for g in chl_attached.get(ref, []):
        for r in anl_groups[g]:
            v = anl_rows[r][C_CN]
            if v and not degenerate(v):
                ids.setdefault(alnum(v), v)
    u = ("chl", ref)
    cand_units.append(u); unit_ids[u] = ids
    unit_vendor[u] = [x for x in {row[C_LEG].strip(), row[C_OPN].strip(), row[C_STD].strip()} if x]
for g, info in anl_cand.items():
    ids = {}
    for r in anl_groups[g]:
        row = anl_rows[r]
        for v in (row[C_CN], r.split("#dup")[0]):
            if v and not degenerate(v):
                ids.setdefault(alnum(v), v)
    u = ("anl", g)
    cand_units.append(u); unit_ids[u] = ids
    unit_vendor[u] = [info["vendor"]] if info.get("vendor") else []
all_ids = collections.defaultdict(list)
for u, ids in unit_ids.items():
    for a in ids:
        all_ids[a].append(u)
log("candidate units", len(cand_units), "distinct ids", len(all_ids))


def vendor_ok(u, names, idval):
    if strong_id(idval):
        return True, "strong id"
    for a in unit_vendor[u]:
        for b in names:
            if names_agree(a, b):
                return True, f"vendor names agree ({a!r} ~ {b!r})"
    return False, None


# ============================================================================= 5a. existing canada_federal records
dup = {}  # unit -> basis
for line in gzip.open(IDX, "rt", encoding="utf-8"):
    r = json.loads(line)
    for a in r["ids"]:
        for u in all_ids.get(a, ()):
            if u in dup:
                continue
            ok, why = vendor_ok(u, r["vendors"], unit_ids[u][a])
            if ok:
                dup[u] = {"record_id": r["record_id"], "id": unit_ids[u][a], "cf_id_value": r["ids_orig"].get(a), "why": why}
            else:
                stats["dedupe_cf"]["id_match_rejected_vendor_mismatch"] += 1
stats["dedupe_cf"]["duplicates"] = len(dup)
stats["dedupe_cf"]["duplicates_chl"] = sum(1 for u in dup if u[0] == "chl")
stats["dedupe_cf"]["duplicates_anl"] = sum(1 for u in dup if u[0] == "anl")
log("duplicates of canada_federal", len(dup))

# ============================================================================= 5b. CanadaBuys complete files (newer data)
superseded = {}
for kind, path, stcol in (("ch_complete", CHC, C_CHST), ("an_complete", ANC, C_ANST)):
    cols = [C_REF, C_CN, C_LEG, C_CTRY, C_END, stcol, C_AMD, C_PUB]
    for chunk in read_csv_chunks(path, cols):
        for row in chunk.to_dict(orient="records"):
            for v in (row[C_CN], row[C_REF]):
                if not v or degenerate(v):
                    continue
                for u in all_ids.get(alnum(v), ()):
                    if u in dup or u in superseded:
                        continue
                    ok, why = vendor_ok(u, [row[C_LEG]], v)
                    if ok:
                        superseded[u] = {"file": kind, "reference": row[C_REF], "contract_number": row[C_CN], "end": row[C_END],
                                         "status": row[stcol], "supplier": row[C_LEG], "country": row[C_CTRY], "why": why}
stats["superseded_by_complete"]["units"] = len(superseded)
log("superseded by complete files", len(superseded))

# ============================================================================= 5c. proactive disclosure
pd_hits = collections.defaultdict(list)  # unit -> rows (subset of columns)
PD_COLS = ["owner_org", "owner_org_title", "reference_number", "procurement_id", "vendor_name", "country_of_vendor", "delivery_date",
           "contract_date", "contract_period_start", "reporting_period", "contract_value", "instrument_type"]
PERIOD_RE = re.compile(r"(\d{4})-(\d{4})-Q([1-4])")


def pd_period_end(row):
    m = PERIOD_RE.search(row["reporting_period"]) or PERIOD_RE.search(row["reference_number"])
    if not m:
        return None
    fy1, q = int(m.group(1)), int(m.group(3))
    return datetime.date.fromisoformat({1: f"{fy1}-06-30", 2: f"{fy1}-09-30", 3: f"{fy1}-12-31", 4: f"{fy1 + 1}-03-31"}[q])


ALL_ID_SET = set(all_ids)
for chunk in read_csv_chunks(PDF, PD_COLS):
    a = chunk["procurement_id"].map(alnum)
    m = a.isin(ALL_ID_SET)
    for aid, row in zip(a[m], chunk[m].to_dict(orient="records")):
        for u in all_ids[aid]:
            if u in dup or u in superseded:
                continue
            ok, why = vendor_ok(u, [row["vendor_name"]], row["procurement_id"])
            if ok:
                pd_hits[u].append(row)
            else:
                stats["pd_match"]["rejected_vendor_mismatch_rows"] += 1
log("units with PD matches", len(pd_hits))

# ============================================================================= 6. decide survivors
survivors = {}
drop_reasons = collections.Counter()
for u in cand_units:
    if u in dup:
        drop_reasons["duplicate_of_canada_federal"] += 1
        continue
    if u in superseded:
        drop_reasons["superseded_by_canadabuys_complete_file_" + superseded[u]["file"]] += 1
        continue
    note = None
    if u in pd_hits:
        rows = pd_hits[u]
        rows.sort(key=lambda r: (pd_period_end(r) or datetime.date.min, r["contract_date"], r["reference_number"]))
        last = rows[-1]
        pend = parse_date(last["delivery_date"]); pq = pd_period_end(last)
        pctry = last["country_of_vendor"].strip().upper()
        if u[0] == "chl":
            crow = chl_last[u[1]][1]
            cdate = max([d for d in (parse_date(crow[C_ADATE]), parse_date(crow[C_PUB]), parse_date(crow[C_AWD])) if d] or [datetime.date.min])
            mine_end = chl_cand[u[1]].get("end")
        else:
            lrow = anl_rows[anl_groups[u[1]][-1]]
            cdate = max([d for d in (parse_date(lrow[C_PUB]), parse_date(lrow[C_AWD])) if d] or [datetime.date.min])
            mine_end = anl_cand[u[1]].get("end")
        if pend is not None and pend < REF_DATE:
            if mine_end is not None and pq is not None and cdate > pq:
                note = f"proactive disclosure ({last['owner_org']} {last['reference_number']}, reporting period {last['reporting_period'] or pq}) reports delivery_date {last['delivery_date']}, but the CanadaBuys legacy row ({cdate}) is newer than that report and gives end {mine_end}; legacy end date kept"
                stats["pd_match"]["kept_legacy_newer_than_pd"] += 1
            else:
                drop_reasons["proactive_disclosure_reports_ended"] += 1
                continue
        elif pctry and pctry != "CA":
            drop_reasons["proactive_disclosure_reports_non_canadian_vendor"] += 1
            continue
        elif pend is not None and pend >= REF_DATE:
            # live in PD but not found in canada_federal.jsonl (e.g. future start there); avoid duplicate
            drop_reasons["proactive_disclosure_live_not_in_canada_federal"] += 1
            continue
        else:
            note = f"proactive disclosure ({last['owner_org']} {last['reference_number']}) matched on procurement_id {last['procurement_id']!r}; its delivery_date is blank"
            stats["pd_match"]["pd_blank_delivery"] += 1
    survivors[u] = note
log("survivors", len(survivors), dict(drop_reasons))
stats["drop_reasons"] = drop_reasons

# ============================================================================= 7. pass 2: full rows
need_chl = {u[1] for u in survivors if u[0] == "chl"}
need_anl_refs = set()
for u in survivors:
    if u[0] == "chl":
        for g in chl_attached.get(u[1], []):
            need_anl_refs.update(r.split("#dup")[0] for r in anl_groups[g])
    else:
        need_anl_refs.update(r.split("#dup")[0] for r in anl_groups[u[1]])
log("pass 2: CHL contracts", len(need_chl), "ANL refs", len(need_anl_refs))
chl_full = collections.defaultdict(list)
for chunk in read_csv_chunks(CHL):
    m = chunk[C_REF].str.strip().isin(need_chl)
    for row in chunk[m].to_dict(orient="records"):
        chl_full[row[C_REF].strip()].append(row)
for ref in chl_full:
    chl_full[ref].sort(key=lambda r: (amend_key(r[C_AMD]), r[C_PUB]))
anl_full = collections.defaultdict(list)
for chunk in read_csv_chunks(ANL):
    m = chunk[C_REF].str.strip().isin(need_anl_refs)
    for row in chunk[m].to_dict(orient="records"):
        anl_full[row[C_REF].strip()].append(row)
log("pass 2 done")


# ============================================================================= 8. build records
def mk_contract_fields(row, src):
    """common contract fields from a CanadaBuys row"""
    it = row.get(C_INST, "").strip()
    inst = {"Contract": "contract", "Contract against SA": "contract against supply arrangement", "Standing Offer": "standing offer",
            "Supply Arrangement": "supply arrangement", "Task Authorization Based Contract": "task authorization based contract"}.get(it, it or None)
    return {
        "instrument_type": inst, "canadabuys_instrument_type": it or None,
        "procurement_method": row.get("procurementMethod-methodeApprovisionnement-eng", "").strip() or None,
        "solicitation_procedure": row.get("procurementMethod-methodeApprovisionnement-eng", "").strip() or None,
        "selection_criteria": row.get("selectionCriteria-criteresSelection-eng", "").strip() or None,
        "limited_tendering_reason": split_multi(row.get("limitedTenderingReason-raisonAppelOffresLimite-eng", "")),
        "trade_agreements": split_multi(row.get("tradeAgreements-accordsCommerciaux-eng", "")),
        "notice_type": row.get("noticeType-avisType-eng", "").strip() or None,
        "commodity": {
            "gsin": (split_multi(row.get("gsin-nibs", "")) or [None])[0],
            "gsin_all": " | ".join(split_multi(row.get("gsin-nibs", "")) or []) or None,
            "gsin_description": " | ".join(split_multi(row.get("gsinDescription-nibsDescription-eng", "")) or []) or None,
            "unspsc": " | ".join(split_multi(row.get("unspsc", "")) or []) or None,
            "unspsc_description": " | ".join(split_multi(row.get("unspscDescription-eng", "")) or []) or None,
            "procurement_category": " | ".join(split_multi(row.get("procurementCategory-categorieApprovisionnement", "")) or []) or None,
        },
    }


PERSON_RE = re.compile(r"^[A-Z][a-zé]+(?: [A-Z]\.)? [A-Z][a-zé]+(?:-[A-Z][a-z]+)?$")
ORGWORD_RE = re.compile(r"canada|defence|defense|parks|health|transport|heritage|statistics|infrastructure|environment|elections|industry|telefilm|marine|atlantic|agency|department|commission|board|council|service|office|bank|corporation|authority|institute|centre|center|museum|library|school|college|university|secretariat|tribunal|program|bureau|general|headquarters", re.I)


LASTFIRST_RE = re.compile(r"^[A-Z][A-Za-zÀ-ÿ'\-]+, [A-Z][A-Za-zÀ-ÿ'\-]+(?: [A-Z][A-Za-zÀ-ÿ'\-]+)?$")
EMAIL_ORG = {"cdic.ca": "Canada Deposit Insurance Corporation"}


def looks_person(x):
    x = (x or "").strip()
    return bool(x) and (bool(PERSON_RE.match(x)) or bool(LASTFIRST_RE.match(x))) and not ORGWORD_RE.search(x)


def mk_buyer(row):
    end_user = row.get("endUserEntitiesName-nomEntitesUtilisateurFinal-eng", "").strip()
    ce = row.get("contractingEntityName-nomEntitContractante-eng", "").strip()
    note = None
    name = end_user or ce or None
    if not end_user and ce and looks_person(ce):
        alt = row.get("contactInfoName-informationsContactNom", "").strip()
        if alt and not looks_person(alt):
            name = alt; note = f"contractingEntityName {ce!r} looks like a person's name; buyer.name taken from contactInfoName"
        else:
            name = None; note = f"contractingEntityName {ce!r} looks like a person's name; no organization name in the record"
    if name is None and not end_user and not ce:
        alt = row.get("contactInfoName-informationsContactNom", "").strip()
        dom = (re.search(r"@([a-z0-9.-]+)", row.get("contactInfoEmail-informationsContactCourriel", "").strip().lower()) or [None, None])[1]
        if alt and not looks_person(alt):
            name = alt; note = "contractingEntityName and endUserEntitiesName blank; buyer.name taken from contactInfoName"
        elif dom in EMAIL_ORG:
            name = EMAIL_ORG[dom]; note = f"contractingEntityName and endUserEntitiesName blank; buyer identified from contact e-mail domain {dom}"
        else:
            note = "contractingEntityName and endUserEntitiesName blank; contactInfoName is a person and no organization can be read from the record"
    b = {"name": name, "country": "CA", "type": buyer_type(name), "identifiers": {
            "canadabuys_contracting_entity": ce or None, "canadabuys_end_user_entity": end_user or None,
            "canadabuys_end_user_office": row.get("endUserEntitiesOfficeName-bureauNomEntitesUtilisateurFinal-eng", "").strip() or None},
         "address": {"line1": row.get("contractingEntityAddressLine-ligneAdresseEntiteContractante-eng", "").strip() or None,
                     "city": row.get("contractingEntityAddressCity-entiteContractanteAdresseVille-eng", "").strip() or None,
                     "region": row.get("contractingEntityAddressProvince-entiteContractanteAdresseProvince-eng", "").strip() or None,
                     "postal_code": row.get("contractingEntityAddressPostalCode-entiteContractanteAdresseCodePostal", "").strip() or None,
                     "country": row.get("contractingEntityAddressCountry-entiteContractanteAdressePays-eng", "").strip() or None,
                     "end_user_address": row.get("endUserEntitiesAddress-adresseEntitesUtilisateurFinal-eng", "").strip() or None},
         "contact": {"name": row.get("contactInfoName-informationsContactNom", "").strip() or None,
                     "email": row.get("contactInfoEmail-informationsContactCourriel", "").strip() or None,
                     "phone": row.get("contactInfoPhone-contactInfoTelephone", "").strip() or None,
                     "fax": row.get("contactInfoFax", "").strip() or None,
                     "address": " ".join(x for x in [row.get("contactInfoAddressLine-contactInfoAdresseLigne-eng", "").strip(), row.get("contactInfoCity-contacterInfoVille-eng", "").strip(), row.get("contactInfoProvince-contacterInfoProvince-eng", "").strip(), row.get("contactInfoPostalcode", "").strip(), row.get("contactInfoCountry-contactInfoPays-eng", "").strip()] if x) or None}}
    if note:
        b["name_note"] = note
    return b


def mk_vendor(row, basis, chl=True):
    v = {"name": (row.get(C_LEG, "").strip() or row.get(C_OPN, "").strip() or row.get(C_STD, "").strip() or row.get("supplierLegalName-nomLegalFournisseur-fra", "").strip() or None),
         "country": "CA", "country_basis": basis,
         "identifiers": {"canadabuys_legal_name": row.get(C_LEG, "").strip() or None},
         "address": {"line1": (row.get("supplierAddressLine-ligneAdresseFournisseur-eng", "").replace("<br>", ", ").strip() or None),
                     "city": row.get("supplierAddressCity-fournisseurAdresseVille-eng", "").strip() or None,
                     "region": row.get("supplierAddressProvince-fournisseurAdresseProvince-eng", "").strip() or None,
                     "postal_code": row.get(C_PC, "").strip() or None,
                     "country": row.get(C_CTRY, "").strip() or None},
         "contact": {}}
    if chl:
        v["identifiers"]["canadabuys_operating_name"] = row.get(C_OPN, "").strip() or None
        v["identifiers"]["canadabuys_standardized_name"] = row.get(C_STD, "").strip() or None
        v["employee_count"] = row.get("supplierEmployeeCount-fournisseurNombreEmployes-eng", "").strip() or None
    return v


def placeholder_end(d):
    return d is not None and d.year >= 2100


out = open(OUT, "w", encoding="utf-8")
OUT_UNID = OUT.replace(".jsonl", "_buyer_unidentified.jsonl")
out_unid = open(OUT_UNID, "w", encoding="utf-8")
by_status = collections.Counter(); written = 0; samples = []; rid_seen = set()
for u, pd_note in survivors.items():
    try:
        if u[0] == "chl":
            ref = u[1]
            rows = chl_full.get(ref) or []
            if not rows:
                stats["build"]["chl_rows_missing_in_pass2"] += 1
                continue
            last, first = rows[-1], rows[0]
            info = chl_cand[ref]
            groups = chl_attached.get(ref, [])
            an_rows = []
            for g in groups:
                for r in anl_groups[g]:
                    an_rows.extend(anl_full.get(r.split("#dup")[0], []))
            an_last = max(an_rows, key=lambda r: (r[C_PUB], amend_key(r[C_AMD]))) if an_rows else None
            end, start = info.get("end"), info.get("start")
            dates_end = iso(end)
            if end is None:
                status = "end_date_unknown"; basis = f"end_date_unknown: CanadaBuys legacy contract history latest row (amendment {last[C_AMD]}) has blank contractEndDate"
            elif placeholder_end(end):
                status = "end_date_unknown"
                basis = (f"end_date_unknown: CanadaBuys legacy contract history latest row (amendment {last[C_AMD]}) contractEndDate {last[C_END]} is a placeholder value "
                         f"(year >= 2100, used for open-ended instruments), not a usable end date; contractStatus {last[C_CHST] or 'blank'}; instrumentType {last[C_INST] or 'blank'}")
                dates_end = None
            else:
                status = "ongoing"
                basis = (f"ongoing: CanadaBuys legacy contract history latest row (amendment {last[C_AMD]}) contractEndDate {last[C_END]} >= {REF} and "
                         f"contractStartDate (else contractAwardDate) {last[C_STA] or last[C_AWD] or 'n/a'} <= {REF}; contractStatus {last[C_CHST] or 'blank'}")
            if pd_note:
                basis += "; " + pd_note
            ids = {"ch_reference_number": ref, "ch_contract_number": last[C_CN] or None, "ch_procurement_number": last[C_PROC] or None,
                   "ch_solicitation_number": last[C_SOL] or None, "ch_amendment_numbers": [r[C_AMD] for r in rows]}
            if an_rows:
                ids["an_reference_numbers"] = sorted({r[C_REF] for r in an_rows})
                ids["an_contract_number"] = an_last[C_CN] or None
                ids["an_solicitation_number"] = an_last[C_SOL] or None
            contract = {"identifiers": ids,
                        "title": last["title-titre-eng"].strip() or (an_last["title-titre-eng"].strip() if an_last else None) or None,
                        "description": first_nonblank(last.get("tenderDescription-descriptionAppelOffres-eng", "").strip(), an_last["awardDescription-descriptionAttribution-eng"].strip() if an_last else None)}
            contract.update(mk_contract_fields(last, "chl"))
            if not contract.get("notice_type") and an_last:
                contract["notice_type"] = an_last.get("noticeType-avisType-eng", "").strip() or None
            tot = to_num(last["totalContractValue-valeurTotaleContrat"]); amt = to_num(last["contractAmount-montantContrat"])
            contract["value"] = tot if tot not in (None, 0) else amt
            contract["currency"] = last["contractCurrency-contratMonnaie"].strip() or ("CAD" if contract["value"] is not None else None)
            contract["value_detail"] = {"ch_total_contract_value": tot, "ch_latest_row_contract_amount": amt,
                                        "ch_original_contract_amount": to_num(first["contractAmount-montantContrat"]),
                                        "ch_number_of_records": last["numberOfRecords-nombreEnregistrements"] or None,
                                        "value_source": "CanadaBuys legacy contract history totalContractValue (latest row)" if tot not in (None, 0) else "CanadaBuys legacy contract history contractAmount (latest row)"}
            if an_last:
                contract["value_detail"]["an_contract_amount"] = to_num(an_last["contractAmount-montantContrat"])
                contract["value_detail"]["an_total_contract_value"] = to_num(an_last["totalContractValue-valeurTotaleContrat"])
            am = [parse_date(r[C_ADATE]) for r in rows if parse_date(r[C_ADATE])]
            contract["dates"] = {"published": first_nonblank(iso(parse_date(first[C_PUB])), iso(parse_date(an_rows[0][C_PUB])) if an_rows else None),
                                 "signed": iso(parse_date(last[C_AWD])) or iso(parse_date(first[C_AWD])),
                                 "start": iso(parse_date(last[C_STA])) or iso(parse_date(last[C_AWD])),
                                 "end": dates_end, "amended_last": iso(max(am)) if am else None}
            if placeholder_end(end):
                contract["dates"]["end_as_published"] = iso(end)
            related = {"regions_of_delivery": split_multi(last.get("regionsOfDelivery-regionsLivraison-eng", ""))}
            if an_last:
                related["award_notice_url"] = cb_notice_url("award-notice", an_last[C_REF])
                related["anl_chl_link_basis"] = [anl_to_chl[g][1] for g in groups]
            contract["related"] = {k: v for k, v in related.items() if v}
            buyer = mk_buyer(last)
            vendor = mk_vendor(last, info["country_basis"] + f" (CanadaBuys legacy contract history latest row, amendment {last[C_AMD]})")
            record_url = cb_notice_url("award-notice", an_last[C_REF]) if an_last else None
            src_name = "CanadaBuys legacy contract history 2009-01 to 2023-05" + (" + legacy award notices 2012-2022" if an_rows else "")
            raw = {"canadabuys_legacy_contract_history": {"reference_number": ref, "n_rows": len(rows), "rows": rows, "resource_url": RESOURCE["chl"], "retrieved_at": RETRIEVED["chl"]}}
            if an_rows:
                raw["canadabuys_legacy_award_notice"] = {"n_rows": len(an_rows), "rows": an_rows, "resource_url": RESOURCE["anl"], "retrieved_at": RETRIEVED["anl"]}
            rid = f"canada_federal_legacy:{ref}"
            dataset_url = DATASET["chl"]; retrieved = RETRIEVED["chl"]
        else:
            g = u[1]
            refs = [r.split("#dup")[0] for r in anl_groups[g]]
            an_rows = []
            for r in refs:
                for row in anl_full.get(r, []):
                    if row not in an_rows:
                        an_rows.append(row)
            if not an_rows:
                stats["build"]["anl_rows_missing_in_pass2"] += 1
                continue
            an_rows.sort(key=lambda r: (r[C_PUB], amend_key(r[C_AMD])))
            last, first = an_rows[-1], an_rows[0]
            info = anl_cand[g]
            end = info.get("end")
            dates_end = iso(end)
            if end is None:
                status = "end_date_unknown"
                basis = (f"end_date_unknown: CanadaBuys legacy award notice {last[C_REF]} has blank contractEndDate (award date {last[C_AWD] or 'n/a'}; awardStatus {last[C_ANST] or 'blank'}, "
                         f"not maintained for legacy notices); contract number {last[C_CN]!r} not found in legacy contract history, CanadaBuys complete files or proactive disclosure")
            elif placeholder_end(end):
                status = "end_date_unknown"; dates_end = None
                basis = f"end_date_unknown: CanadaBuys legacy award notice {last[C_REF]} contractEndDate {last[C_END]} is a placeholder value (year >= 2100); awardStatus {last[C_ANST] or 'blank'}"
            else:
                status = "ongoing"
                basis = (f"ongoing: CanadaBuys legacy award notice {last[C_REF]} contractEndDate {last[C_END]} >= {REF} and contractStartDate (else contractAwardDate) "
                         f"{last[C_STA] or last[C_AWD] or 'n/a'} <= {REF}; awardStatus {last[C_ANST] or 'blank'}")
            if pd_note:
                basis += "; " + pd_note
            ids = {"an_reference_number_latest": last[C_REF], "an_reference_numbers": sorted({r[C_REF] for r in an_rows}),
                   "an_contract_number": last[C_CN] or None, "an_solicitation_number": last[C_SOL] or None}
            contract = {"identifiers": ids, "title": last["title-titre-eng"].strip() or None,
                        "description": last["awardDescription-descriptionAttribution-eng"].strip() or None}
            contract.update(mk_contract_fields(last, "anl"))
            tot = to_num(last["totalContractValue-valeurTotaleContrat"]); amt = to_num(last["contractAmount-montantContrat"])
            contract["value"] = tot if tot not in (None, 0) else amt
            contract["currency"] = last["contractCurrency-contratMonnaie"].strip() or ("CAD" if contract["value"] is not None else None)
            contract["value_detail"] = {"an_total_contract_value": tot, "an_contract_amount": amt,
                                        "value_source": "CanadaBuys legacy award notice totalContractValue" if tot not in (None, 0) else "CanadaBuys legacy award notice contractAmount"}
            am = [parse_date(r[C_ADATE]) for r in an_rows if parse_date(r[C_ADATE])]
            contract["dates"] = {"published": iso(parse_date(first[C_PUB])), "signed": iso(parse_date(last[C_AWD])),
                                 "start": iso(parse_date(last[C_STA])) or iso(parse_date(last[C_AWD])), "end": dates_end,
                                 "amended_last": iso(max(am)) if am else None}
            if placeholder_end(end):
                contract["dates"]["end_as_published"] = iso(end)
            related = {"award_notice_url": cb_notice_url("award-notice", last[C_REF]),
                       "regions_of_delivery": split_multi(last.get("regionsOfDelivery-regionsLivraison-eng", ""))}
            contract["related"] = {k: v for k, v in related.items() if v}
            buyer = mk_buyer(last)
            vendor = mk_vendor(last, info["country_basis"] + f" (CanadaBuys legacy award notice {last[C_REF]})", chl=False)
            vendor["identifiers"]["canadabuys_legal_name_fr"] = last.get("supplierLegalName-nomLegalFournisseur-fra", "").strip() or None
            record_url = cb_notice_url("award-notice", last[C_REF])
            src_name = "CanadaBuys legacy award notices 2012-2022"
            raw = {"canadabuys_legacy_award_notice": {"n_rows": len(an_rows), "rows": an_rows, "resource_url": RESOURCE["anl"], "retrieved_at": RETRIEVED["anl"]}}
            rid = f"canada_federal_legacy:an:{last[C_REF]}"
            dataset_url = DATASET["anl"]; retrieved = RETRIEVED["anl"]
        if rid in rid_seen:
            stats["build"]["record_id_collision"] += 1
            rid = rid + "#" + str(stats["build"]["record_id_collision"])
        rid_seen.add(rid)
        for k in ["title", "description", "instrument_type", "procurement_method", "solicitation_procedure", "value", "currency"]:
            contract.setdefault(k, None)
        if u in pd_hits:
            raw["proactive_disclosure_matches"] = pd_hits[u]
        raw["dedupe_checks"] = {"canada_federal_jsonl": "no contract-level identifier match", "canadabuys_complete_files": "no match",
                                "proactive_disclosure": ("matched; see proactive_disclosure_matches" if u in pd_hits else "no procurement_id match"),
                                "identifiers_checked": sorted(unit_ids[u].values())}
        rec = {"record_id": rid.replace("canada_federal_legacy", "ca_canadabuys_contract_history"),
               "source": {"key": "ca_canadabuys_contract_history", "name": src_name,
                          "publisher": "Public Services and Procurement Canada (CanadaBuys open data, legacy files)",
                          "dataset_url": dataset_url, "record_url": record_url, "retrieved_at": retrieved,
                          "resource_names": [RESOURCE_NAME["chl"]] * (u[0] == "chl") + [RESOURCE_NAME["anl"]] * ("canadabuys_legacy_award_notice" in raw)},
               "status": status, "status_basis": basis, "link": record_url or dataset_url, "contract": contract, "buyer": buyer, "vendor": vendor, "raw": raw}
        if not buyer.get("name"):
            out_unid.write(json.dumps(rec, ensure_ascii=False) + "\n")
            stats["build"]["buyer_unidentified_records"] += 1
            continue
        out.write(json.dumps(rec, ensure_ascii=False) + "\n")
        written += 1; by_status[status] += 1
        stats["buyers"][buyer["name"]] += 1
        if written % 5000 == 0:
            out.flush(); log("written", written)
        if len(samples) < 5 and (written % 997 == 1):
            samples.append(rec["record_id"])
    except Exception as e:
        stats["build"]["errors"] += 1
        log("ERROR", u, repr(e))
out.close(); out_unid.close()
log("DONE written", written, dict(by_status))
res = {"written": written, "by_status": by_status, "samples": samples}
for k, v in stats.items():
    res[k] = dict(v.most_common(60)) if k == "buyers" else dict(v)
json.dump(res, open(STATS, "w"), indent=1, ensure_ascii=False, default=str)
