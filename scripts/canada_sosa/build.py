#!/usr/bin/env python3
"""Build normalized/canada_sosa.jsonl (+ canada_sosa_unverified_country.jsonl) from PSPC's weekly
"Active Standing Offers and Supply Arrangements (SOSA)" file (open.canada.ca dataset f5c8a5a0-354d-455a-99ab-8276aa38032e).

The SOSA file has no supplier address. Supplier location is taken from the SAME instrument (same agreement / CW number)
in CanadaBuys contract history / award notices (complete + legacy files), which publish supplierAddress*.
Instruments already present in normalized/canada_federal.jsonl or normalized/canada_federal_legacy.jsonl are dropped.

Usage: python3 -I build.py <sosa.csv> <canada_federal_dl_dir> <legacy_dl_dir> <cf_index.jsonl.gz> <legacy.jsonl> <out.jsonl> <out_unverified.jsonl> <stats.json>
"""
import sys, os, re, json, gzip, collections, datetime
import pandas as pd

SOSA, FD, LD, IDX, LEG, OUT, OUTU, STATS = sys.argv[1:9]
REF = "2026-10-25"; REF_DATE = datetime.date(2026, 10, 25)
RETRIEVED = "2026-10-26T03:02:25Z"  # file mtime of the copy fetched by this workstream's earlier run (re-fetch at 03:21:54Z failed TLS verification)
DATASET_URL = "https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e"
RESOURCE_URL = "https://sosa.canadabuys.canada.ca/cds/opendata/tpsgc-pwgsc_ocama-sosa.csv"
stats = collections.defaultdict(collections.Counter)


def alnum(s):
    return re.sub(r"[^A-Z0-9]", "", (s or "").upper())


def parse_date(s):
    s = (s or "").strip()[:10]
    try:
        return datetime.date.fromisoformat(s) if re.match(r"^\d{4}-\d{2}-\d{2}$", s) else None
    except ValueError:
        return None


def to_num(s):
    try:
        return float((s or "").replace(",", "").replace("$", "").strip())
    except ValueError:
        return None


CANADA_VALUES = {"CA", "CAN", "CANADA", "CANADA(CA)", "CANADÁ", "CANDA", "CANANDA", "CANANA", "CANAD"}


def is_canada_label(s):
    return re.sub(r"[\s`'\".]", "", (s or "")).upper() in CANADA_VALUES


PC_RE = re.compile(r"^[A-Za-z]\d[A-Za-z](?:\s?\d[A-Za-z]\d)?$")


def name_tokens(s):
    s = (s or "").upper().replace("&", " AND ")
    return {t for t in re.findall(r"[A-Z0-9ÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ]+", s) if len(t) >= 3}


GENERIC = {"INC", "LTD", "LTEE", "LIMITED", "CORP", "CORPORATION", "COMPANY", "CANADA", "THE", "AND", "SERVICES", "GROUP", "SOLUTIONS",
           "CONSULTING", "TECHNOLOGIES", "SYSTEMS", "INTERNATIONAL", "ULC", "LLC", "LIMITEE", "LTÉE", "LIMITÉE", "ENR"}


def names_agree(a, b):
    na, nb = alnum(a), alnum(b)
    if not na or not nb:
        return False
    if na == nb or (min(len(na), len(nb)) >= 8 and (na.startswith(nb) or nb.startswith(na))):
        return True
    return bool((name_tokens(a) - GENERIC) & (name_tokens(b) - GENERIC))


AGREEMENT_TYPES = {"SA": "Supply Arrangement", "NMSO": "National Master Standing Offer", "RISO": "Regional Individual Standing Offer",
                   "NISO": "National Individual Standing Offer", "DISO": "Departmental Individual Standing Offer",
                   "RMSO": "Regional Master Standing Offer"}

# ----------------------------------------------------------------------------- SOSA rows -> agreements
df = pd.read_csv(SOSA, dtype=str, keep_default_na=False, encoding="utf-8-sig")
stats["sosa"]["rows"] = len(df)
agreements = collections.OrderedDict()
for row in df.to_dict(orient="records"):
    a = row["agreement-number"].strip()
    if not a:
        stats["sosa"]["blank_agreement_number"] += 1
        continue
    agreements.setdefault(a, []).append(row)
stats["sosa"]["agreements"] = len(agreements)


def ids_of(a):
    ids = {alnum(a)}
    m = re.match(r"^(CW\d{7})", a.upper())
    if m:
        ids.add(m.group(1))
    return ids


want = {}
for a in agreements:
    for i in ids_of(a):
        want.setdefault(i, set()).add(a)

# ----------------------------------------------------------------------------- existing records
dup = {}
for line in gzip.open(IDX, "rt", encoding="utf-8"):
    r = json.loads(line)
    for i in r["ids"]:
        for a in want.get(i, ()):
            sup = agreements[a][0]["supplier-legal-name"]
            if a in dup:
                continue
            if any(names_agree(sup, v) for v in r["vendors"]) or len(ids_of(a)) == 1:
                dup[a] = {"file": "canada_federal.jsonl", "record_id": r["record_id"], "id": r["ids_orig"].get(i)}
            else:
                stats["dedupe"]["cf_id_match_vendor_mismatch"] += 1
if os.path.exists(LEG):
    for line in open(LEG, encoding="utf-8"):
        r = json.loads(line)
        ci = r["contract"]["identifiers"]
        vals = [ci.get("ch_reference_number"), ci.get("ch_contract_number"), ci.get("an_contract_number")] + list(ci.get("an_reference_numbers") or [])
        for v in vals:
            for a in want.get(alnum(v), ()):
                if a not in dup:
                    dup[a] = {"file": "canada_federal_legacy.jsonl", "record_id": r["record_id"], "id": v}
stats["dedupe"]["duplicates"] = len(dup)

# ----------------------------------------------------------------------------- supplier address from CanadaBuys rows of the same instrument
C_REF, C_CN = "referenceNumber-numeroReference", "contractNumber-numeroContrat"
addr_rows = collections.defaultdict(list)


def pick(p):
    return p if os.path.exists(p) else p + ".gz"


files = [("canadabuys_contract_history_complete", pick(FD + "/contractHistoryComplete-contratsOctroyesComplet.csv")),
         ("canadabuys_award_notices_complete", pick(FD + "/awardNoticeComplete-avisAttributionComplet.csv")),
         ("canadabuys_legacy_contract_history", pick(LD + "/2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv")),
         ("canadabuys_legacy_award_notices", pick(LD + "/2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv"))]
for kind, path in files:
    for chunk in pd.read_csv(path, chunksize=50000, dtype=str, keep_default_na=False, encoding="utf-8-sig",
                             compression="gzip" if path.endswith(".gz") else None):
        ka = chunk[C_REF].map(alnum); kc = chunk[C_CN].map(alnum)
        m = ka.isin(want.keys()) | kc.isin(want.keys())
        for row in chunk[m].to_dict(orient="records"):
            for k in {alnum(row[C_REF]), alnum(row[C_CN])}:
                for a in want.get(k, ()):
                    addr_rows[a].append((kind, row))
stats["address_join"]["agreements_with_canadabuys_rows"] = len(addr_rows)


def best_address(a):
    sup = agreements[a][0]["supplier-legal-name"] or agreements[a][0]["supplier-standardized-name"]
    cands = []
    for kind, row in addr_rows.get(a, []):
        nm = row.get("supplierLegalName-nomLegalFournisseur-eng", "") or row.get("supplierStandardizedName-nomNormaliseFournisseur-eng", "")
        if not names_agree(sup, nm) and not names_agree(agreements[a][0]["supplier-standardized-name"], row.get("supplierStandardizedName-nomNormaliseFournisseur-eng", "")):
            stats["address_join"]["row_vendor_mismatch"] += 1
            continue
        c = row.get("supplierAddressCountry-fournisseurAdressePays-eng", "")
        pc = row.get("supplierAddressPostalCode-fournisseurAdresseCodePostal", "")
        if not c.strip() and not pc.strip():
            continue
        cands.append((row.get("publicationDate-datePublication", ""), row.get("amendmentNumber-numeroModification", ""), kind, row))
    if not cands:
        return None
    cands.sort(key=lambda x: (x[0], x[1]))
    return cands[-1]


# ----------------------------------------------------------------------------- tier 2: same supplier elsewhere in CanadaBuys
# For agreements with no CanadaBuys row of their own, look for the SAME supplier (exact, case-insensitive match of the PSPC
# supplier-standardized-name or supplier legal name) in any CanadaBuys row; accepted only when every matched row carries
# a Canadian supplier address (W1e-style registry match, labelled in vendor.country_basis).
def nkey(s):
    return re.sub(r"\s+", " ", (s or "").strip().upper())


unresolved = [a for a in agreements if a not in dup and a not in addr_rows]
want_names = {}
for a in unresolved:
    r0 = agreements[a][0]
    for nm in (r0["supplier-standardized-name"], r0["supplier-legal-name"]):
        k = nkey(nm)
        if len(k) >= 6:
            want_names.setdefault(k, set()).add(a)
name_rows = collections.defaultdict(list)
for kind, path in files:
    for chunk in pd.read_csv(path, chunksize=50000, dtype=str, keep_default_na=False, encoding="utf-8-sig",
                             compression="gzip" if path.endswith(".gz") else None):
        cols = [c for c in ("supplierStandardizedName-nomNormaliseFournisseur-eng", "supplierLegalName-nomLegalFournisseur-eng") if c in chunk.columns]
        for c in cols:
            kk = chunk[c].map(nkey)
            m = kk.isin(want_names.keys())
            for k, row in zip(kk[m], chunk[m].to_dict(orient="records")):
                name_rows[k].append((kind, c, row))
stats["tier2"]["unresolved_agreements"] = len(unresolved)
stats["tier2"]["names_with_rows"] = len(name_rows)


def tier2(a):
    r0 = agreements[a][0]
    rows = []
    for nm in (r0["supplier-standardized-name"], r0["supplier-legal-name"]):
        rows += name_rows.get(nkey(nm), [])
    seen = set(); ev = []
    for kind, col, row in rows:
        key = (kind, row.get(C_REF), row.get("amendmentNumber-numeroModification"))
        if key in seen:
            continue
        seen.add(key)
        c = row.get("supplierAddressCountry-fournisseurAdressePays-eng", "").strip(); pc = row.get("supplierAddressPostalCode-fournisseurAdresseCodePostal", "").strip()
        if not c and not pc:
            continue
        ev.append((is_canada_label(c) or (not c and bool(PC_RE.match(pc))), kind, col, row))
    if not ev:
        return None, "no_rows"
    if not all(x[0] for x in ev):
        return None, "conflicting_or_foreign_country"
    ev.sort(key=lambda x: (x[3].get("publicationDate-datePublication", ""), x[3].get("amendmentNumber-numeroModification", "")))
    return ev, "ok"


out = open(OUT, "w", encoding="utf-8"); outu = open(OUTU, "w", encoding="utf-8")
by_status = collections.Counter(); by_status_u = collections.Counter()
for a, rows in agreements.items():
    if a in dup:
        stats["excluded"]["duplicate_" + dup[a]["file"]] += 1
        continue
    r0 = rows[0]
    awards = sorted({parse_date(r["award-date"]) for r in rows if parse_date(r["award-date"])})
    exps = sorted({parse_date(r["expiry-date"]) for r in rows if parse_date(r["expiry-date"])})
    start = awards[0] if awards else None
    end = exps[-1] if exps else None
    if end is None:
        status, basis = "end_date_unknown", "end_date_unknown: SOSA expiry-date blank"
    elif end < REF_DATE:
        stats["excluded"]["expiry_before_ref"] += 1
        continue
    elif start and start > REF_DATE:
        stats["excluded"]["future_award_date"] += 1
        continue
    elif end.year >= 2100:
        status = "ongoing_inferred"
        basis = (f"ongoing_inferred: listed in PSPC's weekly 'Active Standing Offers and Supply Arrangements' file (date-file-published {r0['date-file-published']}), "
                 f"which lists only currently active instruments; expiry-date {end.isoformat()} is a placeholder (year >= 2100); award-date {start} <= {REF}")
    else:
        status = "ongoing"
        basis = f"ongoing: SOSA award-date {start} <= {REF} and expiry-date {end.isoformat()} >= {REF} (listed in the weekly active-SOSA file, date-file-published {r0['date-file-published']})"
    if len(exps) > 1:
        basis += f"; rows carry several expiry dates {[d.isoformat() for d in exps]}, latest used"
    ba = best_address(a)
    vendor = {"name": r0["supplier-legal-name"].strip() or r0["supplier-standardized-name"].strip() or r0["supplier-operating-name"].strip() or None,
              "country": None, "country_basis": None,
              "identifiers": {"sosa_supplier_legal_name": r0["supplier-legal-name"].strip() or None,
                              "sosa_supplier_standardized_name": r0["supplier-standardized-name"].strip() or None,
                              "sosa_supplier_operating_name": r0["supplier-operating-name"].strip() or None},
              "address": {}, "contact": {}}
    addr_src = None
    if ba:
        pub, amd, kind, row = ba
        c = row.get("supplierAddressCountry-fournisseurAdressePays-eng", "").strip()
        pc = row.get("supplierAddressPostalCode-fournisseurAdresseCodePostal", "").strip()
        vendor["address"] = {"line1": row.get("supplierAddressLine-ligneAdresseFournisseur-eng", "").replace("<br>", ", ").strip() or None,
                             "city": row.get("supplierAddressCity-fournisseurAdresseVille-eng", "").strip() or None,
                             "region": row.get("supplierAddressProvince-fournisseurAdresseProvince-eng", "").strip() or None,
                             "postal_code": pc or None, "country": c or None}
        addr_src = {"file": kind, "referenceNumber": row.get(C_REF), "contractNumber": row.get(C_CN), "amendmentNumber": amd, "publicationDate": pub}
        if is_canada_label(c) or (not c and PC_RE.match(pc)):
            vendor["country"] = "CA"
            vendor["country_basis"] = (f"supplierAddressCountry {c!r}" if c else f"supplierAddressPostalCode pattern {pc!r}") + \
                f" of the same instrument ({kind} row {row.get(C_REF)}, amendment {amd}; joined on agreement number {a})"
        else:
            stats["excluded"]["vendor_not_canada"] += 1
            stats["vendor_country_values_excluded"][c] += 1
            continue
    commodities = []
    for r in rows:
        cd = r["commodity"].strip().strip('"')
        if cd and cd not in [x["code"] for x in commodities]:
            commodities.append({"code": cd, "description_en": r["commodity-description_en"].strip().strip('"'), "description_fr": r["commodity-description_fr"].strip().strip('"')})
    regions = []
    for r in rows:
        x = (r["delivery-point-code"].strip(), r["delivery-point_en"].strip())
        if x not in regions:
            regions.append(x)
    at = r0["agreement-type_en"].strip()
    contract = {"identifiers": {"sosa_agreement_number": a, "cw_number": (re.match(r"^(CW\d{7})", a.upper()).group(1) if re.match(r"^(CW\d{7})", a.upper()) else None)},
                "title": r0["sosa-description_en"].strip() or None, "title_fr": r0["sosa-description_fr"].strip() or None,
                "description": "; ".join(f"{c['code']} - {c['description_en']}" for c in commodities) or None,
                "instrument_type": "supply arrangement" if at == "SA" else ("standing offer" if at else None),
                "agreement_type": (f"{AGREEMENT_TYPES.get(at, at)} ({at})" if at else None),
                "procurement_method": None, "solicitation_procedure": None,
                "commodity": {"unspsc": " | ".join(c["code"] for c in commodities) or None,
                              "unspsc_description": " | ".join(c["description_en"] for c in commodities) or None},
                "value": None, "currency": None, "value_detail": {},
                "dates": {"published": (r0["date-file-published"] or "")[:10] or None, "signed": start.isoformat() if start else None,
                          "start": start.isoformat() if start else None, "end": end.isoformat() if (end and end.year < 2100) else None,
                          "amended_last": None},
                "related": {"regions_of_delivery": [f"{c} {n}".strip() for c, n in regions]}}
    if end and end.year >= 2100:
        contract["dates"]["end_as_published"] = end.isoformat()
    if ba:
        row = ba[3]
        tot = to_num(row.get("totalContractValue-valeurTotaleContrat")); amt = to_num(row.get("contractAmount-montantContrat"))
        if tot or amt:
            contract["value_detail"] = {"canadabuys_total_contract_value": tot, "canadabuys_contract_amount": amt,
                                        "value_source": f"{ba[2]} row {row.get(C_REF)} (same instrument); SOSA file itself has no value"}
            contract["value"] = tot if tot else amt
            contract["currency"] = row.get("contractCurrency-contratMonnaie") or "CAD"
        contract["identifiers"]["canadabuys_reference_number"] = row.get(C_REF)
        contract["identifiers"]["canadabuys_solicitation_number"] = row.get("solicitationNumber-numeroSollicitation") or None
        contract["procurement_method"] = row.get("procurementMethod-methodeApprovisionnement-eng") or None
        contract["solicitation_procedure"] = contract["procurement_method"]
        ce = parse_date(row.get("contractEndDate-dateFinContrat"))
        if ce and end and ce != end:
            contract["dates"]["canadabuys_end_date_same_instrument"] = ce.isoformat()
            basis += f"; note: {ba[2]} row {row.get(C_REF)} (publicationDate {ba[0] or 'n/a'}) gives contractEndDate {ce.isoformat()}"
    eu = r0["end-user-entity_en"].strip()
    buyer = {"name": eu or None, "country": "CA",
             "type": "federal department or agency" if eu else None,
             "identifiers": {"sosa_end_user_entity_en": eu or None, "sosa_end_user_entity_fr": r0["end-user-entity_fr"].strip() or None,
                             "issuing_authority": "Public Services and Procurement Canada"},
             "address": {}, "contact": {}}
    if eu == "Public Works and Government Services Canada":
        buyer["name_note"] = "PSPC/PWGSC as end user = government-wide instrument put in place by PSPC for use by federal organizations"
    raw = {"sosa_rows": rows, "resource_url": RESOURCE_URL, "retrieved_at": RETRIEVED}
    if addr_src:
        raw["supplier_address_source"] = addr_src
        raw["supplier_address_source_row"] = ba[3]
    rec = {"record_id": f"canada_sosa:{a}",
           "source": {"key": "canada_sosa", "name": "Standing Offers and Supply Arrangements (SOSA) - Active Standing Offers and Supply Arrangements",
                      "publisher": "Public Services and Procurement Canada", "dataset_url": DATASET_URL, "record_url": None, "retrieved_at": RETRIEVED},
           "status": status, "status_basis": basis, "contract": contract, "buyer": buyer, "vendor": vendor, "raw": raw}
    if vendor["country"] is None and not ba:
        ev, why = tier2(a)
        stats["tier2"][why] += 1
        if ev:
            last = ev[-1][3]
            vendor["country"] = "CA"
            vendor["country_basis_type"] = "registry_match"
            vendor["country_basis"] = (f"same supplier elsewhere in CanadaBuys: exact match of SOSA supplier name ({ev[-1][2].split('-')[0]}) to {len(ev)} CanadaBuys row(s), "
                                       f"all with a Canadian supplierAddressCountry/postal code (latest: {ev[-1][1]} row {last.get(C_REF)}); the SOSA agreement itself has no address")
            vendor["address"] = {"line1": last.get("supplierAddressLine-ligneAdresseFournisseur-eng", "").replace("<br>", ", ").strip() or None,
                                 "city": last.get("supplierAddressCity-fournisseurAdresseVille-eng", "").strip() or None,
                                 "region": last.get("supplierAddressProvince-fournisseurAdresseProvince-eng", "").strip() or None,
                                 "postal_code": last.get("supplierAddressPostalCode-fournisseurAdresseCodePostal", "").strip() or None,
                                 "country": last.get("supplierAddressCountry-fournisseurAdressePays-eng", "").strip() or None,
                                 "address_source": f"{ev[-1][1]} row {last.get(C_REF)} (same supplier, other instrument)"}
            raw["supplier_address_evidence_same_supplier"] = [{"file": k, "matched_column": col, "referenceNumber": r.get(C_REF), "contractNumber": r.get(C_CN),
                                                              "publicationDate": r.get("publicationDate-datePublication"),
                                                              "supplierLegalName": r.get("supplierLegalName-nomLegalFournisseur-eng"),
                                                              "supplierAddressCity": r.get("supplierAddressCity-fournisseurAdresseVille-eng"),
                                                              "supplierAddressProvince": r.get("supplierAddressProvince-fournisseurAdresseProvince-eng"),
                                                              "supplierAddressPostalCode": r.get("supplierAddressPostalCode-fournisseurAdresseCodePostal"),
                                                              "supplierAddressCountry": r.get("supplierAddressCountry-fournisseurAdressePays-eng")} for ok, k, col, r in ev[-10:]]
    if vendor["country"] == "CA":
        out.write(json.dumps(rec, ensure_ascii=False) + "\n"); by_status[status] += 1
    else:
        vendor["country_basis"] = "not published: SOSA file has no supplier address and no CanadaBuys row for this agreement number carries one"
        outu.write(json.dumps(rec, ensure_ascii=False) + "\n"); by_status_u[status] += 1
out.close(); outu.close()
res = {"by_status": by_status, "by_status_unverified": by_status_u}
res.update({k: dict(v) for k, v in stats.items()})
json.dump(res, open(STATS, "w"), indent=1, default=str)
print(json.dumps(res, default=str)[:3000])
