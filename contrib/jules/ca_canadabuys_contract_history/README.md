# ca_canadabuys_contract_history

To build this source, fetch the dummy files or full files to downloads directory:

`bash contrib/jules/ca_canadabuys_contract_history/fetch.sh`

Create a dummy index since we don't have access to canada_federal index right now:
`echo "" | gzip > dummy_idx.jsonl.gz`
`mkdir -p downloads/canada_federal`
`echo "contractNumber-numeroContrat,solicitationNumber-numeroSollicitation,referenceNumber-numeroReference,contractEndDate-dateFinContrat,amendmentNumber-numeroModification,contractStatus-statutContrat-eng,publicationDate-datePublication,supplierLegalName-nomLegalFournisseur-eng,supplierAddressCountry-fournisseurAdressePays-eng" > downloads/canada_federal/contractHistoryComplete-contratsOctroyesComplet.csv`
`echo "contractNumber-numeroContrat,solicitationNumber-numeroSollicitation,referenceNumber-numeroReference,contractEndDate-dateFinContrat,amendmentNumber-numeroModification,publicationDate-datePublication,supplierLegalName-nomLegalFournisseur-eng,supplierAddressCountry-fournisseurAdressePays-eng,contractStatus-statutContrat-eng,awardStatus-attributionStatut-eng" > downloads/canada_federal/awardNoticeComplete-avisAttributionComplet.csv`
`echo "contract_number,solicitation_number,reference_number,procurement_id,delivery_date,amendment_number,vendor_name,country_of_vendor,contract_date,owner_org,contract_value,contract_period_start,instrument_type,reporting_period,owner_org_title" > downloads/canada_federal/contracts.csv`

Then run the build script:

`mkdir -p data/incoming/jules/`
`mkdir -p contrib/jules/ca_canadabuys_contract_history/logs`
`python3 contrib/jules/ca_canadabuys_contract_history/normalize.py downloads/ca_canadabuys_contract_history/ downloads/canada_federal/ dummy_idx.jsonl.gz data/incoming/jules/records_ca_canadabuys_contract_history.jsonl data/incoming/jules/stats_ca_canadabuys_contract_history.json`
`gzip -f data/incoming/jules/records_ca_canadabuys_contract_history.jsonl`

To validate:
`python3 tools/validate_records.py data/incoming/jules/records_ca_canadabuys_contract_history.jsonl.gz`
