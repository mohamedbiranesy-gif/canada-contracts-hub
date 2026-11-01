# ca_quebec_city_laval_gatineau_longueuil

Scrapes contract information for Laval and Longueuil from Données Québec.
Other cities like Gatineau and Québec City do not publish relevant 'contrat' datasets via the Données Québec CKAN API. Montreal was already completed elsewhere.

- **Endpoints Used**:
  - Laval: https://www.donneesquebec.ca/recherche/dataset/6acde2c0-6f08-407a-86e2-db49dd0bbb49/resource/db066d35-7e6d-465d-8fae-3a0937b800ae/download/contrats-octroyes.csv
  - Longueuil: https://www.donneesquebec.ca/recherche/dataset/96c41f45-6f76-4cc2-a6a8-98299fe26cd6/resource/121492e6-afa7-4e3c-afa0-aa8bacc33879/download/ententes25k.csv
- **Fields**: Basic municipal contract fields (supplier name, date, value, description).
- **Rows generated**: ~28,899 (after filtering ended contracts based on Longueuil's provided end date).
- **Location filtering**: Sources lack an explicit supplier address field, so `vendor.country` is set to `"CA"` with `country_basis` as `"not published"`.
- **Status rules**:
  - Longueuil contracts with end dates earlier than the reference date (`2026-10-25`) are excluded. Future/ongoing dates are kept.
  - Laval contracts and Longueuil contracts missing specific end dates are kept as `end_date_unknown`.
