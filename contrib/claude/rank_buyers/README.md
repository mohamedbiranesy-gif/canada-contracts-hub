# rank_buyers — the ranked deliverable

One row per distinct buyer organisation, ranked by how well its relationship with a Canada-located supplier is proven
and how complete its invoicing contact is. `batches.py` splits it into quality batches:

| batch | meaning |
|---|---|
| 1_GOLD | active contract (published end date today or later; or awarded in the last 12 months; or Québec, awarded in the last 3 years with no closing notice; or a payment / subcontract dated in the last 12 months) + confirmed invoicing / AP mailbox of the buyer itself |
| 1b | same, but the mailbox is the finance / accounting department's (no invoicing mailbox published) |
| 2 | same, purchasing mailbox |
| 3 | same, general mailbox (info@, reception@ ...) |
| 4 | active contract, mailbox found but not yet confirmed by the referee |
| 5 | active contract, no mailbox yet |
| 6 | payment or subaward record (buyer's own spending data, USAspending) + confirmed mailbox |
| 6b | listed on a Canada-located vendor's client / testimonial page (undated, lower confidence) + confirmed mailbox |
| 6c | relationship record, mailbox not yet confirmed |
| 7 / 8 | older contract (no end date, awarded over a year ago), with / without mailbox |

Quality rules applied on top of the referee's checks:
- a mailbox counts only if it belongs to the buyer itself (`tools/ap_crawler.py:same_org`: same domain, a domain or
  mailbox name that spells the buyer's name / acronym, the Québec health network domain, a provincial government's shared
  domain for a body of that government); contractors' and partners' mailboxes named on the buyer's pages are dropped;
- "invoicing / AP" needs an invoicing word in the mailbox name, or the words just before the address sending invoices
  there; person-looking mailboxes (initial + surname) are never used; receivables, HR, complaints, media boxes are dropped;
- ministries with the same short name in different governments ("Justice", "Health", "Education") share a buyer key
  upstream (`scripts/merge/finalize.py: bkey = name + country`); they are split here by the source's government and a
  mailbox only attaches when its domain fits that government. (Upstream fix pending: add the jurisdiction to bkey.)
