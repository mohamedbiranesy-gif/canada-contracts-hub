# ca_municipal_purchase_orders_open_data

Status: blocked

## Reason for block

The task required finding and processing purchase order open data portals for 20-40 Canadian cities. The only known Socrata open data portal providing purchase orders was `data.edmonton.ca`. However, Edmonton's historic purchase order dataset (`y9rm-5xha`, covering 2012-2019) is already frozen, and current Edmonton outline agreements (`ydv5-y4pu`) and hired equipment (`gnse-cass`) are already processed by the existing `ca_city_edmonton` pipeline.

Extensive automated search using the Socrata Discovery API across `.ca` domains, ArcGIS Hub search on `opendata-surrey.hub.arcgis.com`, and Opendatasoft search on `opendata.vancouver.ca` yielded no new "purchase order" datasets for Canadian cities (including the listed cities: Calgary, Ottawa, Winnipeg, Surrey, Halifax).

Without unified APIs offering these datasets, finding and writing scrapers for 20-40 heterogeneous CMS/portal implementations is out of scope for a single automated script in the sandbox. Thus, this source is blocked.
