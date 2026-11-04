# The deliverable, pushed to its maximum — owner's end goal turned into prompts (2026-11-04 00:44 local)

Owner: "perfect in its integrity with all the information I provided by 11 am Wednesday (soft), end of day Wednesday (hard).
An entry is worthless without an AP e-mail: no e-mail or a dead e-mail → remove. Every row as populated as possible,
vendor side and buyer side. Think micro and macro, operational aspects like the DNS test, beyond what I asked."
Hard rules stay: AGENTS.md §2 (evidence or nothing, organisational mailboxes, no fabrication, no getting around blocks).

## A. Integrity gates (every delivered row, enforced in rank.py / batches.py / tools/validate_deliverable.py)
1. **Mailbox present, syntactically valid, on a domain with a mail server** (tools/mx_check.py: MX, else A/AAAA; a negative
   confirmed by two public resolvers before removal). `none` → the row leaves the delivered packages (stays in Z).
2. **Mailbox is the organisation's own role mailbox** (same_org; no named person; no pattern-built address; no freemail
   unless the organisation's own site uses it and the referee saw it there).
3. **Mailbox evidence**: URL + ≤300-char quote containing the address + retrieval date; referee-verified (`confirmed`) for
   every package except P11.
4. **Relationship evidence**: `contract_status` names the rule and the source; `vendor_country_basis` is the source's own
   field or the vendor's own site; date within the package's window.
5. **One row per organisation, one row per mailbox** (merge by key / domain / name; shared central boxes once).
6. **No blank cell** in delivered packages: a value, or the literal `not_published`.
7. **No receivables mailbox graded as invoicing** (payments@/accounting@ on resident-payment pages; FR taxpayer phrases).
8. **Validation report** (coord/results/ranked/VALIDATION.md): counts per gate, zero tolerance on 1–6, sample of rows.

## B. Field completeness — what each row strives to carry, and where it comes from
Vendor side:
| field | column | source |
|---|---|---|
| legal name | vendor_legal_name | registry match (Corporations Canada / REQ / BC OrgBook / provincial), else the record |
| trading name | vendor (as in the record) / vendor_trading_name when it differs | the record |
| registered address | vendor_address | registry match, else the record, else the vendor's own site (org_contacts) |
| CRA BN + RT0001 | vendor_bn9, vendor_gst_hst_derived (always "derived") | registry match; the vendor's own site when it prints its BN (org_extras) |
| QC NEQ | vendor_neq | REQ match (bulk registry); QST number is not published anywhere public → not_published |
| provincial corp number | vendor_provincial_number | BC OrgBook / Alberta / Ontario matches where the enrichment has them |
| phone | vendor_phone | the vendor's own site (org_contacts) |
| website | vendor_website | registry / record / site finder |
| billing / AR e-mail (FROM address) | vendor_emails (role boxes: ar@, billing@, accounts@, info@ …) | the vendor's own site |
| signatory name + title | — | not published; stays not_published |
| logo / letterhead | vendor_logo_url | og:image / logo image on the vendor's own site (org_extras) |
| WSIB clearance | — | WSIB eClearance is a web application; not automated (rule 6); not_published |
| certificate of insurance | — | not public; not_published |
Buyer side:
| legal entity name | buyer, buyer_legal_name_as_published | the record; the site's copyright / footer line (org_extras) |
| billing address | invoice_mailing_address (AP page), buyer_address | lanes' AP rows; buyer table; the buyer's own site |
| AP e-mail | email (+ email_type, email_check, evidence) | referee |
| AP contact name | ap_contact_name_as_published | only as the organisation prints it next to its AP mailbox (business contact information; never a mailbox) |
| phone | ap_phone (AP page), buyer_phone | lanes' AP rows; the buyer's own site |
| buyer GST/HST / BN | buyer_bn_as_published, buyer_gst_hst_derived | the buyer's own site when it prints it (charities print their BN; org_extras) |
| PO / contract reference | contract_reference, contract_title, instrument_type (standing offer / blanket order / contract), procurement_method, commodity, description, number_of_bids | the record |
| payment terms | payment_terms_as_published; invoicing_requirements | AP page text ("Net 30", "within 45 days", "dans les 30 jours") |
| PO required on invoice | po_required_as_published | AP page text |
| cost centre / vote / project code | — | not published; not_published |
| delivery address | — | not published; not_published |
| tax-exempt certificate | — | not published; not_published |
| language | language_hint (fr / en / fr-en) | evidence page language + province |
| deliverability | email_deliverability | mx_check |
| website alive | buyer_website_status / vendor_website_status | org_contacts fetch result |

## C. Engines that fill B (all on the owner's Mac, all resumable; copies in ~/cch-vnews/tools)
- tools/org_contacts.py — address / phone / role mailboxes (buyers and vendors). Round 2 running.
- tools/org_extras.py — legal name from the copyright line, BN / GST-HST / charity number as printed, logo URL, language,
  site status. One fetch of the home page (+ about / legal page) per domain.
- tools/mx_check.py — deliverability (re-run before every rank; `none` confirmed twice).
- tools/buyer_pages.py — dated awards on public bodies' own sites (round 2 running; precision rules in DECISIONS).
- tools/lead_scanner.py --bridge — record details per lead (amount with its source field, identifiers, dates, vendor address).
- Registry enrichment for vendors lacking BN / NEQ (scripts/enrichment_*): Gold-package vendors first.
- Search rounds (200 WebSearch / turn): mailbox-first Q files (Q_13–Q_22 ready), upgrade B files only for A/B/T organisations.

## D. Loop (every ~60 min until the hard deadline)
1. Engines check / restart (by PID). 2. Search round, read with ap_pages / deep_pages. 3. mx_check refresh; rank-buyers
dispatch; validate_deliverable; spot-check 5 new Gold-class rows + 5 newly filled fields. 4. Record decisions.
5. Owner message only with numbers that moved. 6. Before 11:00 local: final re-rank, VALIDATION.md green, README current,
message with totals and file locations. After 11:00: keep improving until end of day; final message at the hard deadline.
