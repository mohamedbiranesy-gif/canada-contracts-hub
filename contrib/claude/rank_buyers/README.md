# rank_buyers — the ranked deliverable (packages for the owner's survey sampling frame)

`rank.py` builds one row per DISTINCT buyer organisation (a buyer never repeats; a vendor may), with its best proof of a
relationship with a Canada-located vendor and its best own published role mailbox. `batches.py` puts each buyer in the
single best package it qualifies for. Output: `out/ranked/batches/*.csv` (refreshed every 3 h into
`coord/results/ranked/batches/` by the `rank-buyers` workflow; `coord/results/ranked/SUMMARY.md` has the counts).

## Packages (best first; every delivered row carries the buyer's own mailbox)
| package | relationship | mailbox |
|---|---|---|
| P01 GOLD | active: published end date today or later; or awarded / paid / announced / filed in the last 12 months (contract, payment, subaward, import declaration, lobbyist registration, SEC/PCAOB service provider, Form 990 contractor, vendor's own dated news release or customer story ...) | invoicing / AP (confirmed) |
| P01T | active service seen on the buyer's own website today: it uses the paid service of a Canada-headquartered vendor (Shopify Inc. for CA/US stores, eSCRIBE, BiblioCommons, D2L, Edsby, Amilia, Jane with 2+ practitioners, Docebo, Absorb, Coveo, Unbounce, Lightspeed) — kept apart from P01 | invoicing / AP (confirmed) |
| P02 / P03 / P04 | active (as P01) | finance dept / purchasing / general |
| P05 | likely active: contract or dated record 12–36 months old, no end date published | any confirmed |
| P06 / P07 / P08 | listed as a client on the Canada-located vendor's own site (client page, logo wall, undated customer story) | invoicing / finance or purchasing / general |
| P06T | active service seen on the buyer's own website (as P01T) | other confirmed mailbox |
| P09 | older contract or payment record (awarded over 3 years ago / undated) | any confirmed |
| P10 | linked from a page of the Canada-located vendor's site that is not a client page | any confirmed |
| P11 | any relationship above | mailbox found but not yet confirmed by the referee |
| Z | any relationship | no mailbox yet (not delivered) |

## Key columns
`buyer`, `buyer_website`, `email`, `email_type` (invoicing/AP, finance, purchasing, general), `email_check` (confirmed =
the referee re-opened the page and saw the address), `email_evidence_url` + `email_evidence_quote` (≤300 characters
containing the address), `contract_status` (which relationship rule applies, with its source), `award_date`,
`contract_link` (the record), `vendor`, `vendor_country_basis` (the source's own proof that the vendor is located in
Canada), vendor registry fields when known, `keys` (all buyer keys folded into the row).

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
