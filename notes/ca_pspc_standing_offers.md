# `ca_pspc_standing_offers`

- **Endpoint:** `https://sosa.canadabuys.canada.ca/cds/opendata/tpsgc-pwgsc_ocama-sosa.csv`
- **Fields:** `sosa-description_en`, `sosa-description_fr`, `commodity-description_en`, `commodity-description_fr`, `commodity`, `supplier-standardized-name`, `supplier-legal-name`, `supplier-operating-name`, `end-user-entity_en`, `end-user-entity_fr`, `award-date`, `expiry-date`, `delivery-point-code`, `delivery-point_en`, `delivery-point_fr`, `agreement-type_en`, `agreement-type_fr`, `agreement-number`, `date-file-published`
- **Counts:**
  - Total rows seen in SOSA: 6842 rows / 3981 agreements
  - Verified Canadian-vendor ongoing/ended records output: 0 (The script leverages cross-referencing with other CanadaBuys history files to infer vendor locations as the source doesn't provide them, and those cross-references couldn't be loaded in this run).
  - Unverified country records output: 3851
- **Quirks:**
  - Original source dataset lacks vendor address/country fields. The pipeline cross-references `canada_federal` legacy files to obtain the missing address information.
