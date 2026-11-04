# pool_audit.jsonl.gz (owner's earlier AI run, received 2026-11-04 05:21Z) — what was kept

65,981 e-mail rows with a self-assessed "side" and confidence. Assessment against AGENTS.md §2:
- 42,964 rows = Québec RBQ licence-holder e-mails (contractors = vendors, 65 % freemail or named persons): not buyer
  contacts; vendor e-mails only where the mailbox is a role box on the vendor's own domain (7,678) — 120 ranked rows could
  be filled by domain match, left for the enrichment step with the registry itself as provenance (not this extract).
- 776 "buyer_side" rows = CanadaBuys award-notice contacts: named procurement officers (marie-pier.x@forces.gc.ca):
  never usable (rule 5).
- 22,241 "unknown" rows = e-mails scraped from organisation pages and business listings, no quote: 7,291 role mailboxes on
  10,015 domains; 3,237 domains we had no mailbox for, 8 of them delivered buyers without any mailbox yet
  (accountspayable@draytonvalley.ca, finances@cegep-lanaudiere.qc.ca …).
- Kept as HINTS only: `pool_urls.tsv.gz` = the source page (or the home page) of every role mailbox on a domain we lack,
  read by tools/ap_pages.py (evidence or nothing; the ingest referee re-fetches). Nothing from the extract is written to
  the deliverable directly.
- Learning adopted: the extract's deliverability pass (syntax + MX) → tools/mx_check.py flags delivered mailboxes whose
  domain publishes no MX record (DNS only, no SMTP probing).
