# Data (GitHub Release assets)

Download everything:
```
gh release download dataset-latest -D data/release
```
Or click **Releases → dataset-latest** on GitHub.

| Asset | What |
|---|---|
| `canadian_vendor_contracts.jsonl.gz` | Every contract with the vendor verified in Canada. One JSON per line, schema in `docs/SCHEMA.md`, enrichment attached (`vendor_enrichment`, `buyer_enrichment`) |
| `vendor_country_unverified_contracts.jsonl.gz` | Source has no vendor-country field; likely Canadian vendors, kept separately |
| `parties_not_identified_contracts.jsonl.gz` | Buyer or vendor withheld by the source (kept, never mixed in) |
| `vendors_enriched.jsonl.gz` | One line per vendor: registry matches, BN, derived GST/HST, addresses, website, role e-mails, phones |
| `buyers_enriched.jsonl.gz` | One line per buyer: website, address, AP/invoicing contact with evidence, procurement contact |
| `full_<source>.jsonl.gz` | Per-source files with the complete verbatim `raw` source record |
| `DATASET_README.md`, `summary.json` | Fill rates and field documentation |

`harvest-state` holds the harvesters' progress files:
- `seao_api_notices.jsonl.gz`
- `vendors_web_progress.jsonl.gz`
- compact todo lists to continue from

Put downloads in `data/release/`. It is git-ignored.
