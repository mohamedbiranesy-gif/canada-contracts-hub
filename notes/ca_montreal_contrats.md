# Ville de Montréal contracts (open data: contrats octroyés)

* **Source Key:** `ca_montreal_contrats`
* **Publisher:** Ville de Montréal
* **Dataset URLs:**
  * [Contrats octroyés par les fonctionnaires](https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d)
  * [Contrats – Comité exécutif](https://donnees.montreal.ca/dataset/72083af8-83f8-41c1-823b-1cae5e76ff9a)
  * [Contrats – Conseils d'arrondissement](https://donnees.montreal.ca/dataset/60b9662a-17c3-42f0-9ff1-c39bc9026df2)
  * [Contrats – Conseil d'agglomération](https://donnees.montreal.ca/dataset/5cf0220b-c149-43c4-ac23-758c55648584)
  * [Contrats – Conseil municipal](https://donnees.montreal.ca/dataset/5cf0220b-c149-43c4-ac23-758c55648584)
* **API Details:** Fetches raw CSV files directly via their stable CDN download links.

## Fields
* The contracts lack vendor addresses.
* Supplier locations (to determine if the vendor is in Canada) are sourced from the separate [Liste des fournisseurs](https://donnees.montreal.ca/dataset/3bda8899-279a-46fc-9ad9-8dee68d05def) dataset. Vendors are matched by name (`FOURNISSEUR` or `NOM DU FOURNISSEUR`) to check if `Lieu_Pays` is `CA`.
* End dates are not published; all matching records are marked as `end_date_unknown`.

## Counts
* **Rows seen:** 327,420
* **Rows missing vendor:** 5
* **Rows vendor not in registry (dropped):** 84,297
* **Rows vendor not CA (dropped):** 2,796
* **Rows Canadian:** 240,322

## Quirks
* Since "Liste des fournisseurs" might not contain one-off or unregistered vendors, approximately ~25% of records are dropped because the vendor country could not be strictly verified. This adheres to the rule not to infer location purely from the vendor name or the buyer's location.
