#!/usr/bin/env python3
"""Profile the CanadaBuys legacy files (streamed). Usage: python3 -I profile.py <csv> <ch|an> <out_json>"""
import sys, re, json, collections
import pandas as pd

path, kind, out = sys.argv[1], sys.argv[2], sys.argv[3]
REF = "2026-10-25"
CANADA = {"CA", "CAN", "CANADA", "CANADA(CA)", "CANADÁ", "CANDA", "CANANDA", "CANANA", "CANAD"}
PC = re.compile(r"^[A-Za-z]\d[A-Za-z](?:\s?\d[A-Za-z]\d)?$")
st_col = "contractStatus-statutContrat-eng" if kind == "ch" else "awardStatus-attributionStatut-eng"
cols = ["referenceNumber-numeroReference", "contractNumber-numeroContrat", "amendmentNumber-numeroModification",
        "contractAwardDate-dateAttributionContrat", "contractStartDate-contratDateDebut", "contractEndDate-dateFinContrat",
        "supplierAddressCountry-fournisseurAdressePays-eng", "supplierAddressPostalCode-fournisseurAdresseCodePostal",
        st_col, "instrumentType-typeInstrument-eng", "amendmentType-typeModification-eng", "publicationDate-datePublication",
        "contractingEntityName-nomEntitContractante-eng", "endUserEntitiesName-nomEntitesUtilisateurFinal-eng"]
S = collections.defaultdict(collections.Counter)
refs = set(); cn = set()
n = 0
for ch in pd.read_csv(path, chunksize=100000, dtype=str, keep_default_na=False, encoding="utf-8-sig", usecols=cols):
    n += len(ch)
    c = ch["supplierAddressCountry-fournisseurAdressePays-eng"].str.strip()
    S["country"].update(c.value_counts().head(60).to_dict())
    isca = c.map(lambda s: re.sub(r"[\s`'\".]", "", s).upper() in CANADA) | ((c == "") & ch["supplierAddressPostalCode-fournisseurAdresseCodePostal"].str.strip().map(lambda s: bool(PC.match(s))))
    e = ch["contractEndDate-dateFinContrat"].str.strip().str[:10]
    eb = e.map(lambda s: "blank" if s == "" else ("future" if s >= REF else "past"))
    S["end_bucket_all"].update(eb.value_counts().to_dict())
    S["end_bucket_CA"].update(eb[isca].value_counts().to_dict())
    S["status_CA_by_end"].update((ch[st_col][isca].str.strip() + " | " + eb[isca]).value_counts().to_dict())
    S["instrument_CA_future_or_blank"].update(ch["instrumentType-typeInstrument-eng"][isca & (eb != "past")].str.strip().value_counts().to_dict())
    S["amendtype"].update(ch["amendmentType-typeModification-eng"].str.strip().value_counts().to_dict())
    S["award_year_CA_blank_end"].update(ch["contractAwardDate-dateAttributionContrat"][isca & (eb == "blank")].str[:4].value_counts().to_dict())
    S["end_year_CA_future"].update(e[isca & (eb == "future")].str[:4].value_counts().to_dict())
    S["pubyear"].update(ch["publicationDate-datePublication"].str[:4].value_counts().to_dict())
    S["contracting_entity_CA_live"].update(ch["contractingEntityName-nomEntitContractante-eng"][isca & (eb != "past")].str.strip().value_counts().head(40).to_dict())
    refs.update(ch["referenceNumber-numeroReference"].tolist())
    cn.update(ch.loc[isca & (eb != "past"), "referenceNumber-numeroReference"].tolist())
    print(n, file=sys.stderr, flush=True)
res = {"rows": n, "distinct_refs": len(refs), "distinct_refs_CA_with_future_or_blank_end_row": len(cn)}
for k, v in S.items():
    res[k] = dict(v.most_common(80))
json.dump(res, open(out, "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: res[k] for k in ["rows", "distinct_refs", "distinct_refs_CA_with_future_or_blank_end_row"]}))
