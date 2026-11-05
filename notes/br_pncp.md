# br_pncp
Endpoint: https://pncp.gov.br/api/consulta/v1/contratos
Status: blocked
The API has over 1 million records for a single year (2024), but no server-side filter for the vendor country (`codigoPaisFornecedor` is ignored in the query string). It would require fetching gigabytes of JSON sequentially page by page to find a Canadian vendor. Marking as blocked due to lack of server-side filtering combined with rate limit constraints on such massive data.
