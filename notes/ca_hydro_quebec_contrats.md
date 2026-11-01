# Source: Hydro-Québec contracts awarded

- **Source Key:** `ca_hydro_quebec_contrats`
- **Publisher:** Hydro-Québec
- **URL:** [https://www.hydroquebec.com/fournisseurs/soumissionner/attribution-des-contrats.html](https://www.hydroquebec.com/fournisseurs/soumissionner/attribution-des-contrats.html)
- **Dataset CSV:** `https://www.hydroquebec.com/soumissionnez/attribution/attribution.csv`

## Processing Notes
- The CSV file has `;` as a delimiter and uses `latin-1` or `utf-8-sig` encoding.
- Dates are published in `YYYYMMDD` format under `DATE_DE_CONCLUSION_DU_CONTRAT`.
- The dataset does not provide a contract end date. Therefore, the status for all records is `end_date_unknown`.
- `MONTANT` field provides the value when available.
- `PAYS_FOURN` explicitely specifies the country of the vendor (Canada).

## Volume Stats (as of 2026-10-25)
- **Rows seen:** 93
- **Rows Canadian:** 93
- **Rows output:** 93 (all marked as `end_date_unknown`)
