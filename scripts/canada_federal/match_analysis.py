#!/usr/bin/env python3
"""Analyse identifier overlap between proactive disclosure (live CA rows) and CanadaBuys CH/AN/TN.
Usage: python3 -I match_analysis.py <downloads dir>
"""
import sys, re, collections, json
import pandas as pd

D = sys.argv[1].rstrip("/") + "/"
REF = "2026-10-25"

def norm(s):
    return re.sub(r"\s+", "", (s or "").strip().upper())

def alnum(s):
    return re.sub(r"[^A-Z0-9]", "", (s or "").upper())

ch = pd.read_csv(D + "contractHistoryComplete-contratsOctroyesComplet.csv", dtype=str, keep_default_na=False, encoding="utf-8-sig",
                 usecols=["referenceNumber-numeroReference", "procurementNumber-numeroApprovisionnement", "solicitationNumber-numeroSollicitation", "contractNumber-numeroContrat", "contractEndDate-dateFinContrat", "supplierAddressCountry-fournisseurAdressePays-eng", "supplierLegalName-nomLegalFournisseur-eng", "endUserEntitiesName-nomEntitesUtilisateurFinal-eng"])
an = pd.read_csv(D + "awardNoticeComplete-avisAttributionComplet.csv", dtype=str, keep_default_na=False, encoding="utf-8-sig",
                 usecols=["referenceNumber-numeroReference", "solicitationNumber-numeroSollicitation", "contractNumber-numeroContrat", "contractEndDate-dateFinContrat", "supplierAddressCountry-fournisseurAdressePays-eng", "supplierLegalName-nomLegalFournisseur-eng", "contractingEntityName-nomEntitContractante-eng", "endUserEntitiesName-nomEntitesUtilisateurFinal-eng"])
tn = pd.read_csv(D + "tenderNoticeComplete-avisAppelOffresComplet.csv", dtype=str, keep_default_na=False, encoding="utf-8-sig",
                 usecols=["referenceNumber-numeroReference", "solicitationNumber-numeroSollicitation"])

ch_ids = {}
for col in ["contractNumber-numeroContrat", "procurementNumber-numeroApprovisionnement", "solicitationNumber-numeroSollicitation", "referenceNumber-numeroReference"]:
    ch_ids[col] = set(ch[col].map(norm)) - {""}
an_ids = {}
for col in ["contractNumber-numeroContrat", "solicitationNumber-numeroSollicitation", "referenceNumber-numeroReference"]:
    an_ids[col] = set(an[col].map(norm)) - {""}
tn_sol = set(tn["solicitationNumber-numeroSollicitation"].map(norm)) - {""}
tn_ref = set(tn["referenceNumber-numeroReference"].map(norm)) - {""}

ch_alnum = set(ch["contractNumber-numeroContrat"].map(alnum)) - {""}
an_alnum = set(an["contractNumber-numeroContrat"].map(alnum)) | set(an["referenceNumber-numeroReference"].map(alnum))
an_alnum -= {""}
# contract number stems: strip the /NNN/XX suffix -> stem
def stem(s):
    s = norm(s)
    m = re.match(r"^([A-Z0-9]+-[A-Z0-9]+)/\d{3}/[A-Z0-9]{2,3}$", s)
    return m.group(1) if m else None
ch_stems = collections.Counter(x for x in ch["contractNumber-numeroContrat"].map(stem) if isinstance(x, str) and x)
an_stems = collections.Counter(x for x in an["contractNumber-numeroContrat"].map(stem) if isinstance(x, str) and x)
stem_by_alnum = collections.defaultdict(list)
for s in list(ch_stems) + list(an_stems):
    stem_by_alnum[alnum(s)].append(s)

stats = collections.Counter()
examples = collections.defaultdict(list)
org_match = collections.Counter()
org_total = collections.Counter()
pid_shapes = collections.Counter()
so_match = collections.Counter()
live_keys = set()

for chunk in pd.read_csv(D + "contracts.csv", chunksize=100000, dtype=str, keep_default_na=False, encoding="utf-8-sig"):
    c = chunk["country_of_vendor"].str.strip().str.upper()
    dd = chunk["delivery_date"].str.strip()
    live = (c == "CA") & dd.str.match(r"^\d{4}-\d{2}-\d{2}$") & (dd >= REF)
    sel = chunk[live]
    for _, r in sel.iterrows():
        pid = norm(r["procurement_id"]); so = norm(r["standing_offer_number"]); org = r["owner_org"]
        key = (org, pid or "REF:" + r["reference_number"])
        if key in live_keys:
            continue
        live_keys.add(key)
        org_total[org] += 1
        shape = re.sub(r"[A-Z]", "A", re.sub(r"\d", "9", pid))
        pid_shapes[shape] += 1
        hit = False
        for col, ids in ch_ids.items():
            if pid and pid in ids:
                stats["pid in CH." + col] += 1; hit = True
                if len(examples["CH." + col]) < 3: examples["CH." + col].append((org, pid, r["vendor_name"]))
        for col, ids in an_ids.items():
            if pid and pid in ids:
                stats["pid in AN." + col] += 1; hit = True
                if len(examples["AN." + col]) < 3: examples["AN." + col].append((org, pid, r["vendor_name"]))
        if pid and pid in tn_sol:
            stats["pid in TN.solicitationNumber"] += 1
            if len(examples["TN.sol"]) < 3: examples["TN.sol"].append((org, pid, r["vendor_name"]))
        if pid and pid in tn_ref:
            stats["pid in TN.referenceNumber"] += 1
        if so:
            for col, ids in ch_ids.items():
                if so in ids: so_match["SO in CH." + col] += 1
            for col, ids in an_ids.items():
                if so in ids: so_match["SO in AN." + col] += 1
            if so in tn_sol: so_match["SO in TN.sol"] += 1
        if not hit and pid:
            a = alnum(pid)
            if a in ch_alnum or a in an_alnum:
                stats["pid alnum-only match (no exact)"] += 1; hit = True
                if len(examples["alnum"]) < 5: examples["alnum"].append((org, pid, r["vendor_name"]))
            elif len(a) >= 8 and re.search(r"[A-Z]", a):
                # stem match e.g. PD 'W8486088630' vs CH 'W8486-088630/001/BLB'
                cand = stem_by_alnum.get(a, [])
                if cand:
                    stats["pid stem match (no exact)"] += 1; hit = True
                    if len(examples["stem"]) < 8: examples["stem"].append((org, pid, r["vendor_name"], cand[:3]))
        if hit:
            org_match[org] += 1
    print("chunk done", file=sys.stderr, flush=True)

print(json.dumps({
    "live_CA_contract_keys": len(live_keys),
    "match_stats": dict(stats),
    "standing_offer_matches": dict(so_match),
    "org_match_rate_top30": [(o, org_match[o], org_total[o]) for o, _ in org_total.most_common(30)],
    "pid_shapes_top40": pid_shapes.most_common(40),
    "examples": examples,
    "ch_stem_count": len(ch_stems), "an_stem_count": len(an_stems),
    "ch_stem_examples": ch_stems.most_common(5), "an_stem_examples": an_stems.most_common(5),
}, indent=1, ensure_ascii=False, default=str))
