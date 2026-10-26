# ca_manitoba — Manitoba (data.gov.mb.ca blocked; MERX handled by another worker)

Checked 2026-10-25 17:40 UTC. `https://data.gov.mb.ca/` is refused by the egress proxy (502 CONNECT, host not allowed). Manitoba government and MB public-sector awards are published on MERX (`https://www.merx.com/public/solicitations/awarded?location=361`, 17,801 awarded solicitations; the award tab `/public/solicitations/<id>/abstract/award` carries Supplier Awarded, full address incl. country, Awarded Value, Award Date and Contract Dates). I started a MERX crawl but found that a parallel worker already owns `downloads/ca_merx` + `scripts/ca_merx` (its listing/details crawlers were running), so I stopped mine, deleted my files from that folder, and left MERX to that worker (source_key `ca_merx`). Note for them: MERX's AWS WAF intermittently answers `HTTP 202` with header `x-amzn-waf-action: challenge` and an empty body; a retry after a pause succeeds.

Result: 0 records under `ca_manitoba`.
