# ua_prozorro
Endpoint: https://public.api.openprocurement.org/api/2.5/contracts
Status: blocked
The API returns a change feed where the primary list endpoint does not contain supplier data. Fetching the supplier requires fetching the detail endpoint for every single contract ID in the feed. The volume is enormous (millions of contracts) and the API has a rate limit of <=3 req/s.
