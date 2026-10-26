# ca_bonfire — Bonfire (GTY/Euna) public portals of Canadian public bodies (REJECTED: Cloudflare challenge on award pages)

Checked 2026-10-25T19:30Z. `<org>.bonfirehub.ca/portal/?tab=pastOpportunities` loads for some orgs (ubc, ualberta,
mcmaster: HTTP 200) and the JSON `PublicPortal/getPastPublicOpportunitiesSectionData` lists past projects (UBC: 1,635,
745 with `IsPublicAward: true`) but carries no awardee. The per-opportunity page holding the public award
(`https://ubc.bonfirehub.ca/opportunities/109251`) returns a Cloudflare "Just a moment… Enable JavaScript and cookies"
managed challenge; `PublicPortal/getPublicContractsSectionData` returns a non-JSON challenge body. Several org hosts
(edmonton, calgary, halifax, surrey, regina .bonfirehub.ca) fail at the egress proxy (CONNECT 502). Not bypassed. Result: 0 records.
