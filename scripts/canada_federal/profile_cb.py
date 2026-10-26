#!/usr/bin/env python3
"""Profile CanadaBuys contract history / award notices / tender notices.
Usage: python3 -I profile_cb.py <which: ch|an|tn> <csv path>
"""
import sys, re, collections, json
import pandas as pd

which, path = sys.argv[1], sys.argv[2]
REF = "2026-10-25"
C = collections.Counter
stats = collections.defaultdict(C)
nrows = 0
examples = {}

def vc(col, key=None, top=None, chunk=None, mask=None):
    s = chunk[col] if mask is None else chunk.loc[mask, col]
    stats[key or col].update(s.value_counts().to_dict())

def fmt(s):
    if s == "": return "blank"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s): return "YYYY-MM-DD"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}[T ].*", s): return "YYYY-MM-DD+time"
    return "other:" + s[:12]

for chunk in pd.read_csv(path, chunksize=100000, dtype=str, keep_default_na=False, encoding="utf-8-sig"):
    nrows += len(chunk)
    cols = chunk.columns
    if which in ("ch", "an"):
        vc("supplierAddressCountry-fournisseurAdressePays-eng", chunk=chunk)
        vc("supplierAddressCountry-fournisseurAdressePays-fra", chunk=chunk)
        vc("supplierAddressProvince-fournisseurAdresseProvince-eng", chunk=chunk)
        vc("contractCurrency-contratMonnaie", chunk=chunk)
        vc("instrumentType-typeInstrument-eng", chunk=chunk)
        vc("amendmentType-typeModification-eng", chunk=chunk)
        vc("noticeType-avisType-eng", chunk=chunk)
        vc("procurementMethod-methodeApprovisionnement-eng", chunk=chunk)
        vc("contractingEntityName-nomEntitContractante-eng", chunk=chunk)
        vc("contractingEntityAddressCountry-entiteContractanteAdressePays-eng", chunk=chunk)
        stats["fmt_contractStartDate"].update(chunk["contractStartDate-contratDateDebut"].map(fmt).value_counts().to_dict())
        stats["fmt_contractEndDate"].update(chunk["contractEndDate-dateFinContrat"].map(fmt).value_counts().to_dict())
        stats["fmt_contractAwardDate"].update(chunk["contractAwardDate-dateAttributionContrat"].map(fmt).value_counts().to_dict())
        stats["fmt_publicationDate"].update(chunk["publicationDate-datePublication"].map(fmt).value_counts().to_dict())
        stats["fmt_amendmentDate"].update(chunk["amendmentDate-dateModification"].map(fmt).value_counts().to_dict())
        stats["amendmentNumber"].update(chunk["amendmentNumber-numeroModification"].value_counts().to_dict())
        stats["pubDate_year"].update(chunk["publicationDate-datePublication"].str[:4].value_counts().to_dict())
        ctry = chunk["supplierAddressCountry-fournisseurAdressePays-eng"].str.strip()
        ed = chunk["contractEndDate-dateFinContrat"].str.strip()
        live = ed.str.match(r"^\d{4}-\d{2}-\d{2}") & (ed.str[:10] >= REF)
        stats["live_rows_by_country"].update(ctry[live].value_counts().to_dict())
        stats["blank_end_by_country"].update(ctry[ed == ""].value_counts().to_dict())
        stats["blank_end_pubyear_CA"].update(chunk.loc[(ed == "") & (ctry == "Canada"), "publicationDate-datePublication"].str[:4].value_counts().to_dict())
        statuscol = "contractStatus-statutContrat-eng" if which == "ch" else "awardStatus-attributionStatut-eng"
        vc(statuscol, chunk=chunk)
        stats["status_x_live"].update((chunk[statuscol] + "|live=" + live.map(str)).value_counts().to_dict())
        # identifiers
        stats["ref_blank"]["blank"] += (chunk["referenceNumber-numeroReference"].str.strip() == "").sum()
        stats["sol_blank"]["blank"] += (chunk["solicitationNumber-numeroSollicitation"].str.strip() == "").sum()
        stats["cn_blank"]["blank"] += (chunk["contractNumber-numeroContrat"].str.strip() == "").sum()
        stats["ref_prefix"].update(chunk["referenceNumber-numeroReference"].str.extract(r"^([A-Za-z]+)")[0].fillna("<none>").value_counts().to_dict())
        stats["cn_prefix"].update(chunk["contractNumber-numeroContrat"].str.extract(r"^([A-Za-z]+)")[0].fillna("<none>").value_counts().to_dict())
        if which == "ch":
            vc("numberOfRecords-nombreEnregistrements", chunk=chunk)
            stats["pn_blank"]["blank"] += (chunk["procurementNumber-numeroApprovisionnement"].str.strip() == "").sum()
            stats["pn_prefix"].update(chunk["procurementNumber-numeroApprovisionnement"].str.extract(r"^([A-Za-z]+)")[0].fillna("<none>").value_counts().to_dict())
            stats["ref_dups"].update(chunk["referenceNumber-numeroReference"].value_counts().to_dict())
            stats["cn_dups"].update(chunk["contractNumber-numeroContrat"].value_counts().to_dict())
        else:
            stats["ref_dups"].update(chunk["referenceNumber-numeroReference"].value_counts().to_dict())
            stats["cn_dups"].update(chunk["contractNumber-numeroContrat"].value_counts().to_dict())
        if "ex_live_ca" not in examples:
            sel = chunk[live & (ctry == "Canada")]
            if len(sel):
                examples["ex_live_ca"] = sel.head(2).to_dict(orient="records")
        if "ex_blank_end" not in examples:
            sel = chunk[(ed == "") & (ctry == "Canada")]
            if len(sel):
                examples["ex_blank_end"] = sel.head(2).to_dict(orient="records")
    else:  # tender notices
        vc("tenderStatus-appelOffresStatut-eng", chunk=chunk)
        vc("noticeType-avisType-eng", chunk=chunk)
        vc("contractingEntityName-nomEntitContractante-eng", chunk=chunk)
        stats["fmt_pub"].update(chunk["publicationDate-datePublication"].map(fmt).value_counts().to_dict())
        stats["fmt_close"].update(chunk["tenderClosingDate-appelOffresDateCloture"].map(fmt).value_counts().to_dict())
        stats["sol_blank"]["blank"] += (chunk["solicitationNumber-numeroSollicitation"].str.strip() == "").sum()
        stats["ref_prefix"].update(chunk["referenceNumber-numeroReference"].str.extract(r"^([A-Za-z]+)")[0].fillna("<none>").value_counts().to_dict())
        stats["ref_dups"].update(chunk["referenceNumber-numeroReference"].value_counts().to_dict())
        stats["sol_dups"].update(chunk["solicitationNumber-numeroSollicitation"].str.strip().str.upper().value_counts().to_dict())
        u = chunk["noticeURL-URLavis-eng"].str.strip()
        stats["noticeURL_host"].update(u.str.extract(r"^https?://([^/]+)")[0].fillna("<blank or none>").value_counts().to_dict())
        stats["noticeURL_pattern"].update(u.str.replace(r"\d+", "#", regex=True).str.replace(r"/[A-Za-z0-9_\-]{8,}$", "/<id>", regex=True).value_counts().to_dict())
        if "ex" not in examples:
            examples["ex"] = chunk.head(2).to_dict(orient="records")
            examples["ex_url"] = chunk.loc[u != "", ["referenceNumber-numeroReference", "solicitationNumber-numeroSollicitation", "noticeURL-URLavis-eng", "noticeURL-URLavis-fra"]].head(8).to_dict(orient="records")
            examples["ex_url_cb"] = chunk.loc[u.str.contains("canadabuys", na=False), ["referenceNumber-numeroReference", "solicitationNumber-numeroSollicitation", "noticeURL-URLavis-eng", "noticeURL-URLavis-fra"]].head(8).to_dict(orient="records")
    print(f"{which} rows so far {nrows}", file=sys.stderr, flush=True)

out = {"which": which, "nrows": nrows}
for k, c in stats.items():
    if k.endswith("_dups"):
        out[k] = {"distinct": len(c), "with_multiple_rows": sum(1 for v in c.values() if v > 1), "max_rows": max(c.values()) if c else 0, "top5": c.most_common(5)}
    elif k in ("contractingEntityName-nomEntitContractante-eng",):
        out[k] = {"distinct": len(c), "top40": c.most_common(40)}
    else:
        out[k] = c.most_common(40)
out["examples"] = examples
print(json.dumps(out, indent=1, ensure_ascii=False, default=str))
