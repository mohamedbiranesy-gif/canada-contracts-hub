# rank_buyers — the ranked deliverable (packages for the owner's survey sampling frame)

`rank.py` builds one row per DISTINCT buyer organisation (a buyer never repeats; a vendor may), with its best proof of a
relationship with a Canada-located vendor and its best own published role mailbox. `batches.py` puts each buyer in the
single best package it qualifies for. Inputs from the release: `canadian_vendor_contracts.jsonl.gz` (required),
`vendors_enriched`, `buyers_enriched`, `vendor_country_unverified_contracts`, `ended_*` (optional: each is skipped when
absent, which only empties P12 and some filled fields). Output: `out/ranked/batches/*.csv` (refreshed every 3 h into
`coord/results/ranked/batches/` by the `rank-buyers` workflow; `coord/results/ranked/SUMMARY.md` has the counts).

## Packages (best first; every delivered row carries the buyer's own mailbox)
| package | relationship | mailbox |
|---|---|---|
| P01 GOLD | active: published end date today or later; or awarded / paid / announced / filed in the last 12 months (contract, payment, subaward, import declaration, lobbyist registration, SEC/PCAOB service provider, Form 990 contractor, the organisation's own audited statements naming its auditor (signature city + province), vendor's own dated news release naming the organisation as its customer, or customer story ...) | invoicing / AP (confirmed) |
| P01T | active service seen on the buyer's own website today: it uses the paid service of a Canada-headquartered vendor (Shopify Inc. for CA/US stores, eSCRIBE, BiblioCommons, D2L, Edsby, Amilia, Jane with 2+ practitioners, Docebo, Absorb, Coveo, Unbounce, Lightspeed; since 2026-11-03 also Benevity, Coconut Software, Möbius / DigitalEd, SchoolCash Online / KEV Group portals; TMX Group when the issuer's own site prints its TSX / TSXV ticker (annual listing fee); a group-benefits carrier, employee-assistance provider or academic tool named as the provider on the buyer's own HR / teaching / library pages — each vendor's Canadian head office quoted from its own site) — kept apart from P01 | invoicing / AP (confirmed) |
| P02 / P03 / P04 | active (as P01) | finance dept / purchasing / general |
| P05 | likely active: contract or dated record 12–36 months old, no end date published | any confirmed |
| P06 / P07 / P08 | listed as a client on the Canada-located vendor's own site (client page, logo wall, undated customer story) | invoicing / finance or purchasing / general |
| P06T | active service seen on the buyer's own website (as P01T) | other confirmed mailbox |
| P09 | older contract or payment record (awarded over 3 years ago / undated) | any confirmed |
| P10 | linked from a page of the Canada-located vendor's site that is not a client page | any confirmed |
| P11 | any relationship above | mailbox found but not yet confirmed by the referee |
| P12 | weaker relationship, dated within the last 5 years (award / start / end on or after today minus 5 years): a contract that already ended (vendor in Canada per the source, `ended_*.jsonl.gz`), or a contract whose vendor is in Canada only through a business-registry match (exact / strong match with a Canadian registered office; the source publishes no vendor country, `vendor_country_unverified_contracts.jsonl.gz`). `contract_status` starts with "weaker relationship" | own mailbox, confirmed |
| P13 | inferred relationship, no record: every other organisation with its own confirmed role mailbox (`coord/results/org_mailboxes.csv`) gets the Canada-located vendor it very likely pays, from its type and province (see below). `vendor` = "inferred: …", `contract_status` = "inferred relationship (no record): <confidence>; <buyer type>; <law or fact>" | own mailbox, confirmed |
| P01M / P06M | member or regulated payer of a Canadian body: the organisation is on the CURRENT member / participant / regulated-institution list the body publishes (IESO and AESO market participants, OSFI-regulated institutions, CDIC members, Payments Canada members, CBA / CLHIA / IBC / Electricity Canada / CCUA / CICan / Alberta Municipalities members) and pays it (premiums, market charges, assessments or dues; the fee basis and the body's head office are quoted). Added 2026-11-03 at the owner's "no door closed"; kept apart from P01 / P01T because the body is a regulator or association, not a supplier chosen by the buyer | P01M invoicing / AP (confirmed); P06M other confirmed mailbox |
| Z | any relationship | no mailbox yet (not delivered) |

### P13 inference rules (first match wins; each vendor's location is quoted from its own site in `vendor_country_basis`)
| buyer | inferred vendor | confidence | basis |
|---|---|---|---|
| federal department / agency (mailbox on gc.ca / canada.ca) | Canada Post Corporation | high | exclusive letter privilege, Canada Post Corporation Act s. 14 |
| Ontario municipality | MPAC | high | "funded by all Ontario municipalities" (mpac.ca), MPAC Act 1997 |
| municipality or institution (school, college, university, health or government body) in QC / MB / SK / NB / NU | Hydro-Québec / Manitoba Hydro / SaskPower / NB Power / Qulliq Energy | high | the province's electricity distribution monopoly (towns with their own utility are excluded) |
| other organisation in QC / MB / SK / NB / NU; municipality or institution in BC | same utilities; BC Hydro | medium | as above; a tenant may pay electricity through its lease; FortisBC / municipal utilities serve parts of BC |
| other organisation in BC | BC Hydro | low | as above |
| other municipality or institution located in Canada | Canada Post Corporation | medium | exclusive letter privilege; they mail tax notices / letters |
| any other organisation located in Canada | Canada Post Corporation | low | generic: exclusive letter privilege; not every organisation mails letters |
Province: the release's vendor / buyer table address, else the registered address in a public registry
(`org_places.csv.gz`, built by `org_places.py`: CRA List of charities `cra:<BN9>`, Ontario private schools `onps:`, Alberta
schools / authorities `abed:`; a key listed there counts as located in Canada), else a provincial domain (.qc.ca, gov.bc.ca …),
else the single postal code on the organisation's own page. Organisations not shown to be located in Canada get no inference (skipped). One row
per organisation: P12 / P13 never repeat an organisation, registrable domain or mailbox already in a row above.

## Key columns
`buyer`, `buyer_website`, `email`, `email_type` (invoicing/AP, finance, purchasing, general), `email_check` (confirmed =
the referee re-opened the page and saw the address), `email_evidence_url` + `email_evidence_quote` (≤300 characters
containing the address), `contract_status` (which relationship rule applies, with its source), `award_date`,
`contract_link` (the record), `vendor`, `vendor_country_basis` (the source's own proof that the vendor is located in
Canada), vendor registry fields when known, `keys` (all buyer keys folded into the row).

## Field completeness (owner, 2026-11-03)
Every cell of a delivered package is filled: from the record (identifiers, value, currency, dates, link), then the
release's vendor table (`vendors_enriched.jsonl.gz`: legal name, BN9, address, website, e-mails, only from an exact /
strong registry match) and buyer table (`buyers_enriched.jsonl.gz`: website, address); `buyer_website` falls back to the
mailbox's domain (or the evidence page's host when it is the same domain); `vendor_gst_hst_derived` = BN9 + RT0001,
always labelled derived; a currency missing from a Canadian / US government source is labelled "derived from the
source's government". A field no source gives is the literal `not_published` (Z: e-mail columns are `not_found_yet`).
`ranked_buyers.csv` keeps blanks (it is the working file batches.py reads).

## Quality rules on top of the referee's checks
- Vendor in Canada only from the source itself (address / country field, release dateline, the vendor's own Canada-HQ
  site); never from a name.
- A mailbox counts only if it belongs to the buyer itself (`tools/ap_crawler.py:same_org`: same registrable domain, a
  domain or mailbox name that spells the buyer's name or acronym; a sibling campus, a contractor, a software or
  e-invoicing provider, or a parent government's shared domain for another body never counts). Lead buyers must match
  their own website (or the evidence page's host when no website is known).
- "Invoicing / AP" needs an invoicing word in the mailbox name or the words just before the address; receivable,
  tuition, billing, donation and customer-payment mailboxes count as general at most; person-looking mailboxes are never
  used; HR, complaints, media, privacy boxes are dropped.
- One row per organisation: two spellings sharing a key, or two rows sharing a registrable website domain, are one buyer.
- Ministries with the same short name in different governments are split by the source's government, and a mailbox only
  attaches when its domain fits that government.
- Spot-check 2026-11-02 (10 P01 + 10 P01T rows) and the fixes it led to: see `coord/DECISIONS.md`.
