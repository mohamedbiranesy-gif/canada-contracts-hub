# ca_municipal_purchase_orders_open_data

- **Source URL**: https://data.edmonton.ca/d/y9rm-5xha (Edmonton Purchase Orders Over $10,000)
- **Status**: First slice completed (Edmonton POs)
- **Method**:
  - Downloaded CSV from Socrata endpoint `https://data.edmonton.ca/api/views/y9rm-5xha/rows.csv?accessType=DOWNLOAD`.
  - Edmonton's dataset contains straight purchase orders. It lacks an explicit PO Number column in this dataset export, but satisfies the PO dataset requirement.
  - The dataset lacks explicit vendor addresses/countries. Vendor country is inferred by exact or loose name matching against the verified Canadian vendor dictionary `contrib/claude/buyer_pages/vendors_ca.tsv.gz`.
  - Edmonton POs only have a start/create date and no end date. All records matched are kept with `status` "end_date_unknown", according to the schema rules for datasets lacking end dates but publishing awards.
- **Records emitted**: 1627 records matched to verified Canadian vendors.
- **Run pipeline**: `contrib/jules/ca_municipal_purchase_orders_open_data/run.sh`
