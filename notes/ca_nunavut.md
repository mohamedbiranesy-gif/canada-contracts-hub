# ca_nunavut — Government of Nunavut (REJECTED: no supplier identity/address accessible)

Checked 2026-10-25 17:47–18:20 UTC.
- `https://www.gov.nu.ca/…` (procurement pages, public tenders, contract activity reports) — HTTP 403 Cloudflare "Just a moment…" JS challenge; not bypassed.
- `https://www.nunavuttenders.ca/` (GN Request for Tenders/Proposals site) is reachable. Its `AwardHistoryList.aspx` lists awards (Ref Number, Description, "FOB Point Or Location" = delivery location, Award Date; 20 per page, ASP.NET postback paging) but **does not show the awarded supplier**; the per-tender link (`Default.aspx?op=lnk&ref=…`, and the postback on the award row) redirects to `RegisterBidder.aspx` (vendor registration required). So neither supplier name nor supplier address is obtainable without registering. The "FOB Point" (e.g. "Ottawa, ON") is the delivery point, not the vendor address, and must not be used.
- GN "Contract Activity Reports" (annual PDFs listing contracts with vendor community) sit behind the gov.nu.ca Cloudflare challenge.

Result: 0 records.
