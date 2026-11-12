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

## Columns (116, in file order)
`jurisdiction`, `rank_group`, `completeness_score`, `buyer`, `buyer_website`, `buyer_address`, `buyer_phone`,
`buyer_contact_evidence_url`, `buyer_legal_name_as_published` (copyright / footer line of the buyer's site),
`buyer_bn_as_published` (BN / charity number as printed, with the page), `buyer_gst_hst_derived` (BN9 + RT0001, labelled
derived, registration not confirmed), `buyer_logo_url`, `buyer_website_status`, `email`, `email_type`, `email_check`,
`email_evidence_url`, `email_evidence_quote`, `email_deliverability` (tools/mx_check.py), `email_security_posture` (one line: EXPOSED to
sender spoofing / DMARC enforced, SPF result, mail provider), `dmarc_policy` (no DMARC record · v=DMARC1; p=none · p=quarantine · p=reject ·
invalid), `dmarc_record` (raw TXT), `dmarc_record_domain` (where it was found; the organizational domain when the mailbox is on a subdomain),
`spf_policy` (-all hard fail · ~all soft fail · ?all neutral · +all · no all · no SPF record), `spf_record`, `mail_provider` (from the MX hosts:
Microsoft 365, Google Workspace, Proofpoint, Mimecast, ISP mail, self-hosted…), `dns_checked_date` (tools/dmarc_check.py, DNS only, negatives
re-confirmed through 8.8.8.8), `ap_contact_name_as_published`
(only as the organisation prints it next to its AP mailbox: business contact information, never a mailbox), `ap_phone`,
`invoice_mailing_address`, `invoicing_requirements`, `payment_terms_as_published`, `po_required_as_published`,
`invoice_portal_url` (an additional channel the buyer publishes; the e-mail is the contact), `language_hint`, `template_language` (D15: fr for every Québec buyer — jurisdiction, .qc.ca site, QC address or French municipal name — en-fr for federal / New Brunswick bodies, else the language of the invoicing page),
`contract_status`, `contract_reference`, `contract_title`, `contract_description`, `instrument_type` (contract / standing
offer / blanket order / supply arrangement as the source names it), `procurement_method`, `commodity`, `number_of_bids`,
`contract_value` (lead rows name the source field), `currency`, `award_date`, `start_date`, `end_date`, `contract_link`,
`source`, `vendor`, `vendor_legal_name`, `vendor_trading_name`, `vendor_registry_id` (NEQ / corporation number / BC
registration from the registry match), `vendor_registry_url`, `vendor_registered_address`, `vendor_neq`,
`vendor_qst_as_published`, `vendor_address`, `vendor_country_basis`, `vendor_bn9`, `vendor_gst_hst_derived`,
`vendor_website`, `vendor_emails` (role boxes on the vendor's own domain: billing / AR / info), `vendor_phone`,
`vendor_contact_evidence_url`, `vendor_logo_url`, `vendor_website_status`, `vendor_peppol_id` (D8: the vendor's Peppol Directory participant id when its exact name is listed), `contracts_with_canadian_suppliers`,
`buyer_keys`, `keys`, `tier`, `grade`, `acc`.
Fields no public source gives (signatory name and title, WSIB clearance number, certificate of insurance, QST number
unless printed, buyer cost centre / vote / project code, delivery address, tax-exempt certificate) are `not_published`.

Added 2026-11-06 (owner's D-items): `most_recent_record_reference_any_vendor` (D2: the organisation's most recent dataset reference — PO / contract /
solicitation / award id — with vendor, source and date; lead rows get it when the same organisation, by website domain or exact name, has
dataset records), `records_in_contract_dataset`, `other_relationship_sources` (D12: lead relationships — customer stories, auditor-of-record
statements, lobbyist registries, SEC ADV, FERC, Form 990 — seen for a dataset buyer), `sensitivity_tag` (D13: police oversight bodies such
as ASIRT / SIU / BEI / IIO, police services, corrections, intelligence / defence / border, coroners, child protection, shelters and crisis
services, courts, mental-health / addiction / sexual-health bodies → "high-sensitivity buyer: suppress unless reviewed"; a tag from the
published name / type, never a removal), `peppol_participant_id` / `peppol_registered` (D8: the Peppol Directory lists 77 Canadian
participants in all, nearly all suppliers; every row says whether the buyer is one), `commodity_codes` now also carries the record's own
commodity block (D14: UNSPSC, GSIN, NAICS, CPV, PSC, economic object codes with their descriptions). `payment_terms_as_published`,
`po_required_as_published`, `invoice_portal_url`, `ap_phone`, `invoice_mailing_address`, `ap_contact_name_as_published`,
`invoicing_requirements` (invoice format) and `buyer_bn_as_published` are also filled from a full re-read of each mailbox's evidence page
(tools/ap_terms.py, D4 / D5 / D6 / D11: regex on the page's own text, URL and date in the cell, no AI, no inference).

Added 2026-11-08 (the downstream agent's per-package asks; every value carries its source in the cell): `org_group_key` (the
grouping of the contract records; the contracts subfolder joins on it), `po_numbers_this_pair_open_data` / `po_count_this_pair_open_data` /
`contract_numbers_this_pair_open_data` (the buyer's own purchase-order / contract open data — Montréal, Laval, Toronto to start — joined to
the pair; `po_number_as_published` and `contract_or_agreement_number` take the most recent one when the record had none),
`vendor_neq`, `vendor_trading_name`, `vendor_legal_form`, `vendor_activity_code` (REQ CAE), `vendor_employees_quebec`,
`vendor_establishments_quebec`, `vendor_directors_range`, `vendor_last_annual_filing` (the full REQ / Corporations Canada / OrgBook
records behind the confident registry matches), `buyer_fiscal_year_end` / `buyer_charity_status` / `buyer_charity_designation` and
charity BNs (CRA list of registered charities, matched by domain + name or exact name + province), `buyer_municipal_tier` /
`buyer_population` / `directory_general_email` / `municipal_directory_source` (provincial municipal and organisation directories:
QC MAMH, ON MMAH, ON school boards, BC school districts, QC collèges and MSSS M02 establishments, IRCC designated learning
institutions, GC Registry of Applied Titles, GOV.UK organisations, Australian Government Organisations Register),
`buyer_wikidata` / `buyer_founded` / `buyer_budget_or_revenue` / `buyer_employees` / `buyer_legal_form` and `vendor_wikidata` /
`vendor_founded` / `vendor_employees` (Wikidata, one organisation at a time, domain + name or exact name + country), Crown
corporations' own GST numbers on inferred-vendor rows (`vendor_bn9`, read and re-verified on their pages), `email_evidence_context`,
`mailbox_recheck_note`, `buyer_payment_method_preference`, `buyer_ap_cycle_published`, `buyer_tax_exempt_status`,
`buyer_esignature_preference`, `mta_sts` / `tls_rpt` / `bimi`, `statutory_payees_inferred`, `vendor_years_in_business`,
`typical_contract_value_p90`, `average_contract_duration_days`, `commodity_distribution_top3`, `year_over_year_spend_trend`,
`inference_confidence` (HIGH / MEDIUM / LOW with the reason; "not applicable" for MPAC on lower-tier Ontario municipalities),
`mailbox_confidence`, `data_quality_score`, `ship_ready`, `invoice_portal_kind` / `invoice_portal_note`, `ap_system_hint`,
`invoicing_requirements_structured`, `facts_provenance_json`, `payment_terms_default_policy`, `instrument_type_normalized`,
`buyer_bn_program`, `vendor_registry_warning` (primary registry record dead, or no registry shows the vendor alive), `vendor_registry_note` (an extra-provincial registration lapsed while the primary record is alive — no penalty), `sensitivity_flag`, `buyer_sector`, `evidence_age_days`, `reverify_due`,
`most_recent_record_reference_any_vendor`, `records_in_contract_dataset`, `other_relationship_sources`, pair columns
(`pair_prior_records`, `pair_first_or_repeat`, `pair_value_trend`, `pair_dates_and_values`), `template_language`, `sensitivity_tag`,
`peppol_participant_id` / `peppol_registered` / `vendor_peppol_id`. `CHANGELOG.md` + `rows_changed.csv` (row- and field-level) ship with
every build; `verified_ledger.csv` keeps the referee's sightings so a mailbox never loses its verdict to a transient fetch failure.

Added 2026-11-08 (second pass, the downstream team's coverage targets): `COVERAGE_VS_TARGETS.md` + `coverage_vs_targets.json` in every
build (tools/coverage_targets.py: every field × package against the targets of 2026-11-08, with Δ since the previous build from
`coord/results/coverage_history.csv`); contract facts a proof record lacks are taken from another record of the SAME buyer–vendor pair and
say so in the cell ("from another record of the same buyer-vendor pair: <reference>, <source>, <date>"); `end_date` carries the pipeline's
inferred end ("inferred: award date + the duration the source publishes") when no end is published, `start_date` the signature date when no
start is published, both labelled; `records_with_this_vendor` names the relationship record for lead-based rows; contract values of
bids&tenders awards come from the awarded bidder's own submitted price when no award value was published (`value_detail.value_basis` in the
dataset, 9,213 records) and `number_of_bids` from the portals' submission lists (58,304 records); `buyer_legal_name_as_published` and
`vendor_legal_name` also come from schema.org JSON-LD `legalName` and from the name a Terms / Privacy / Legal page states ("operated by X
Inc.", "X Inc. ("we")", "The Corporation of the City of X"), each labelled with the page; `buyer_linkedin_url` / `vendor_linkedin_url`,
`buyer_supplier_portals_linked` (e-tendering / e-invoicing / e-signature portals the buyer's own site links to; `ap_system_hint` and
`invoice_portal_url` take them when empty), `vendor_industry_naics` (JSON-LD), `buyer_registry_id`, `vendor_website_basis` (a site proposed
by a web search is used only after tools/vendor_sites_check.py read it and found the company's name on it; the quote is in the cell);
Canada's Business Registries (ISED's public multi-jurisdictional search, tools/registry_lookup.py): `vendor_bn9`, registered name, registered
office city / province, status, incorporation date, entity type, alternate names for vendors, and BN / registered name for corporation-type
buyers — exact registered name, home-jurisdiction record first, province decides ties, ambiguous names skipped; federal grants & contributions
disclosure (tools/gc_recipients.py): `buyer_bn_as_published` / `vendor_bn9` from `recipient_business_number`, exact name + province; the
inferred vendors' own published phone and address (Canada Post Credit Management Group, NB Power, Qulliq Energy) on P13 rows.

## Files
Since 2026-11-10 the build's bulky files are **assets of the release `ranked-latest`** (https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest),
replaced in place by every build — committing them grew the repository by gigabytes a day:
`ranked_batches.zip` — one CSV per package (a package over ~95 MB in numbered part files, `P13_…_part1_of_4.csv` …, same columns, split only by
size); `ranked_buyers.csv.gz` — every row incl. Z; `ranked_contracts.zip` — every contract record of the delivered buyers with all identifiers;
`ranked_extras.zip` — `audit_flags.csv`, `dmarc_no_enforcement.csv`, `rows_changed.csv`; `BUILD.json` — build id, counts, size and SHA-256 of each file.
In git, `coord/results/ranked/`: `WHERE.md` (links and package counts), `BUILD.json`, `SUMMARY.md`, `VALIDATION.md`, `AUDIT.md`, `DMARC.md`,
`CHANGELOG.md`, `COVERAGE_VS_TARGETS.md`, `CONTRACTS.md`, and `batches_head/<package>.csv` (the first 10 rows of each package).
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not hold the current build).

## Mailbox rules
Webmail addresses (gmail, hotmail, outlook, yahoo, icloud, proton…) are never delivered, whoever publishes them: a webmail account is
not an organisational mailbox. ISP-hosted mailboxes that a small municipality publishes as its official contact (videotron.ca, bellnet.ca…)
are kept and labelled `mail_provider = ISP mail`.

Whose mailbox it is (2026-11-12, `rank.py: mail_page_own`, `tools/ap_crawler.py: same_org`; coord/DECISIONS.md 13:40Z):
- read on a directory or roster (211, CIOC, a chamber's or association's member list, a tourism site, Wikivoyage, the PEPPOL directory): not used;
- on the organisation's own domain, read on another site or file of its own: used;
- on another domain: only when read on the organisation's own pages, on a domain whose name spells it, on its files at a hosting service,
  or on a government page that names it; a government portal page (gov.uk/…, canada.ca/…, quebec.ca/…) vouches for no mailbox by itself;
  the Québec health network's @ssss.gouv.qc.ca counts for a body of the network or a mailbox named after the buyer;
- never a mailbox for something else (press, complaints, quality of service, access to information, registers, funding programmes,
  stakeholder engagement, recruiting, receivables).
One row per organisation: `tools/priority_sort.py` joins rows of one organisation that came in under two keys (same name and postal code,
mail domain or website; or same unshared mail domain and postal code) and keeps its best row; `duplicate_buyers_dropped.csv` lists the others.

## Identifier columns (owner 2026-11-06: "PO matters — all identifiers possible")
Right after `contract_reference` (which now holds the record's complete identifier block, no longer truncated): `invoice_reference_hint`
(the one reference to quote: PO / procurement number first, else contract number, else solicitation number, else award id — with the
source field name), `po_number_as_published` (purchase-order / procurement numbers: `pd_procurement_id` of the federal proactive
disclosure, `piid` of US purchase and delivery orders, `order_number` / `po_id` of state purchase-order ledgers, bons de commande),
`contract_or_agreement_number`, `solicitation_or_tender_number`, `award_or_notice_id` (OCDS ocid, SEAO, MERX, bids&tenders ids),
`buyer_vendor_id` (the supplier's id in the buyer's own system), `vendor_ids_in_record` (UEI / DUNS / CAGE / BN as the source prints
them), `commodity_codes` (UNSPSC / GSIN / NAICS / CPV), `buyer_org_codes`, `amendment_or_modification`, `all_identifiers` (every
identifier verbatim, `key=value`), `identifier_count`, `records_with_this_vendor` and `all_references_with_this_vendor` (up to 12
references across every record of this buyer with this vendor). Every record behind a delivered buyer — not only the one shown in
the row — is in `coord/results/ranked/contracts/contracts_of_delivered_buyers_part*.csv.gz` (CONTRACTS.md gives the counts).

## Narrative and provenance columns (owner 2026-11-04 10:50: every row states the relationship and how it was found)
`buyer_type` (derived from the name: municipality, school board, university, hospital/health authority, ministry/agency, utility, First
Nation, non-profit, company…), `relationship_kind` (contract award with end date · award in the last 12 months · active paid service seen
on the buyer's site · member/regulated payer · named as a client by the vendor · dated deal/payment 12–36 months · linked from the
vendor's site · older record · inferred), `relationship_detail` (one line with buyer, vendor, subject, instrument, reference, value,
dates, publishing source, record link, the Canada proof and the status rule, plus the buyer's record counts),
`how_relationship_was_found` (the pipeline step and tool that produced the record), `mailbox_provenance` (who located the mailbox and
how — crawler / web search + no-AI page read / lane agent —, the page, the quote, the referee verification, DNS and security posture,
the lane file and task id), `buyer_facts_provenance` and `vendor_facts_provenance` (the page or table behind every buyer / vendor
fact), `distinct_canadian_vendors`, `records_last_12_months`, `latest_award_date_any_vendor`, `total_known_value_canadian_suppliers`,
`other_canadian_vendors_sample`, `record_sources` (the buyer's whole history with Canada-located vendors in the dataset),
`vendor_registry_status`, `vendor_registry_match_level`, `vendor_incorporation_date`, `vendor_bn_source`, `vendor_billing_ar_email` and
`vendor_contacts_found_by` (the team's referee-verified vendor contacts — lane gemini researched 15,427 vendors, 8,670 with a verified role
mailbox or website, 171 with a billing / AR mailbox — merged into `vendor_emails`), `method_notes`.

## Billing period (owner 2026-11-11: "billed for something monthly … or every 3 months … systematically by the vendor")
`recurring_billing` says what is published about when the vendor bills this buyer; `recurring_billing_basis` quotes the source.

| value | what it means | where it comes from |
|---|---|---|
| `1 monthly`, `1 quarterly` | the vendor's own terms or price page say it bills by the month (every 30 days) or the quarter, and its service is seen in use by the buyer | the vetted vendors' terms read by hand (`tools/tech_relationships.py` BILLING: Shopify "billed … every 30 days", Jane "charged monthly in advance" …); for every other vendor a billing statement found by `tools/vendor_billing.py` on the vendor's own site, with no longer period on the pages read; a public record whose own text says "monthly" |
| `2 monthly or yearly` | the vendor's price list is by the month and it also sells a year paid in advance, or does not say which is billed: the buyer's own period is not published | the same reader (a price with its period, "$4.99/mo") |
| `3 yearly or longer` | a fee for a year or more at a time | `.ca` names (CIRA's rules: 1 to 10 years), licences and registrations with their published expiry date, annual membership dues, the audit of each fiscal year |
| `4 per transaction` | a fee on each sale / booking / vehicle | the vendor's or the body's own statement |
| `5 not published` | nothing published says when the vendor bills | contract records without an invoicing schedule, client listings, design credits ("Website by …"), links, inferred rows |

**The bill's other fields** (owner 2026-11-11 07:15: "the data that would go within the invoice … the fields that the Shopify invoice would
have … how much does it cost?"). Each cell quotes the vendor's or the body's own page; nothing is filled without one.
`bill_amount_indicative` + `bill_amount_basis` (the vendor's price: Shopify "from US$29 a month" with its four plan prices; for other
vendors the lowest price by the month or the year that `tools/vendor_billing.py` found, as a floor — the buyer's own plan is never
published; a body's fee: HCRA $715 a year, OMVIC $22 per vehicle), `bill_items_as_published` (what the bill is made of: Shopify's
subscription, transaction and additional fees; a `.ca` registration and its renewals), `bill_currency_as_published`,
`bill_delivery_as_published` (how the bill reaches the customer), `bill_payment_method_as_published`, `bill_tax_rule_as_published`,
`bill_identifier_format` (Shopify: a nine-digit bill number, "SHOPIFY* 123456789" on a bank statement), `service_stops_if_unpaid`
(the vendor's own rule that an unpaid service is cut off — the reason a service seen running is a service being paid for),
`bill_due_terms_as_published` (when the bill is due: "Payment is due 30 days from the date of the invoice") and
`bill_remit_to_as_published` (where a payment by mail goes, the biller's own printed address). For a licence of Toronto, Calgary or
Edmonton the amount is the city's own (`tools/payee_fees.py`): the open invoice the City of Toronto lists for that licence number
(`bill_identifier_format` then carries its invoice number), the renewal fee of that kind of licence, the line of the fee schedule; a
licence of several types gets the amount the schedule's own rule gives, in `bill_amount_calculated`.

**The owner's test of a row (2026-11-11 afternoon; AGENTS.md §1, rules 6 to 12).** One function decides, `tools/relationship_rows.py:
owner_test`, and every row says what it found: `payment_route` (on invoice, by bank transfer / cheque · on invoice; bank payment or card ·
not published · payable by bank, but no invoice or notice is published · no invoice is sent) with `payment_route_basis` (the biller's or the
buyer's own words); `invoice_fields_for_kind` (the fields a relationship of that kind can carry) and `invoice_fields_missing_for_kind`;
`vendor_tax_or_registration_number` (the GST/HST number derived from a published Business Number, else the number in the vendor's home
register, said to be that); `ship_ready` ("yes", "yes (the amount is calculated and labelled so)" or "no") and `ship_ready_missing`
(everything that keeps the row from "yes"). A row whose bill is charged to a card on file, or goes through a registrar, is not written
at all. The earlier label that looked only at the kind of mailbox is kept as `ap_mailbox_ready`.

**Since 2026-11-11 16:01 EST (AGENTS.md §1, rule 13).** Four things make a row: a Canadian biller with a relationship, a bill on invoice,
a bank payment, the organisation's mailbox. `ship_ready` reads "yes" when every field of the row's kind is filled in the biller's or the
record's own words; "yes (…)" when something is said by the kind of relationship (`payment_route` then ends "by the kind of
relationship"), when a field is not published (named after "not published:"), or when the row stands on where the organisation is; "no"
with the reason in `ship_ready_missing`. A row that stands on where the organisation is (`tools/by_location.py`): `relationship_fact_basis`
begins "by where it is:", the vendor is the electricity distributor of the organisation's own printed address, `recurring_billing`,
`bill_amount_indicative` (the least the distributor bills a business in a month), `bill_delivery_as_published`,
`bill_payment_method_as_published`, `bill_due_terms_as_published` and `bill_remit_to_as_published` are the distributor's own sentences.
The distributor is certain for the address; whose name is on the account is not published, and the row says so.

**Since 2026-11-11 20:36 EST (AGENTS.md §1, rules 14 to 17).** One row per buyer, no buyer twice; a vendor may stand on many rows. $5,000 is
a mark and an order, not a test. `amount_mark` puts every row in one of five classes: "1 published, $5,000 or more" (the value of the
contract as the public record gives it, or the biller's own published fee or price) · "2 estimated, $5,000 or more" · "3 published, under
$5,000" (a price "from $15.43 a month" is $15.43) · "4 estimated, under $5,000" · "5 no amount" — each with the figure it rests on. The
table is written in that order, the rows that meet the test first (`tools/priority_sort.py`, run by `tools/rank_tail.sh`); inside a class
the ranker's order is kept. A buyer under contract carries, among the records of its best tier, one whose published value is $5,000 or
more. An estimate is a calculation from published figures and stands in `bill_amount_calculated`, opening with "estimated —" or
"calculated —": for a row by where the organisation is, what the distributor's own published rate comes to at 2,500 kWh a month (the use
at which the Ontario Energy Board's small-business bill calculator opens), before tax; for a contract, its published value by the year of
its published term. Never in `bill_amount_indicative`, which holds published amounts only. A row by where the organisation is also
carries the distributor's legal name (`vendor_legal_name`), its number in its regulator's register where it has one
(`vendor_registry_id`: an Ontario distributor's licence number), and its tax rule; in Ontario the billing period, the due terms and the
ways of paying are the regulator's own code for every distributor (`tools/on_ldc_table.py`). When ten or more organisations print the same
urban postal code the row says so; from fifty it does not meet the test (a tower, a campus, a business centre or a mail service: the
landlord's account). A "postal code" that is a colour code or a form's placeholder is not one (`tools/by_location.py: usable`).
Where the organisation is, in this order (2026-11-12): the address its own pages print (beside its mailbox, on its contact page, the postal
code its home page prints); its registered address in a public registry (`org_places.csv.gz`: the CRA List of charities, provincial school
directories — "(its registered address in …)"); the city its own page names, when one distributor serves the whole city; and, when none of
these located it, the address an Overture Maps place lists for its website — only when all the domain's open places in Canada print one
postal code and the place's name fits the organisation's. Such a cell ends "(the address an Overture Maps place lists for its website …:
“place name”, place id, from datasets; Overture Maps Foundation open data, release … — a public places dataset, not the organisation's own
pages)", the relationship sentence and `source` say so, and `ship_ready` adds "the organisation's address is the one a public places
dataset (Overture Maps) lists for its website, not read on its own pages". The same listed address fills the buyer's address on a row of
another kind that has none. The file (`overture_addresses.csv.gz`, one address per domain, monthly) is in the release `harvest-state`
(`tools/credit_scan.py overture`, `credit-scan.yml` job overture); a build without it is as before.
`relationship_fact_basis` says in one sentence why the relationship is a fact, or that it is not one: "fact, seen on the buyer's side"
(a running service, a `.ca` name) · "fact, public record" (an award, a register) · "stated by the buyer" (a credit line, a membership
badge) · "stated by the vendor" (a client list) · "link only" · "inferred, not a fact".

`invoice_fields_present` ("7/9") and `invoice_fields_missing` count nine fields on the row: buyer legal name, buyer address, vendor legal
name, vendor address, vendor tax number, what is billed, amount, billing period, reference. The build log prints the fill of each.

`billing_period_calculated` holds a period that is not published for the relationship but follows from two published things, and always
opens with the word "calculated": a client the vendor names + the vendor's price list by the month; construction work for an Ontario owner
+ the Construction Act's default ("Proper invoices shall be given to an owner on a monthly basis, unless the contract provides otherwise").
It never feeds `recurring_billing`.

`bill_amount_calculated` is the same idea for the amount, and also always opens with the word "calculated". Today it is filled on `.ca`
registration rows: the registrant's own registrar and price are not published for any one name (CIRA's fee is on a site that refuses the
reader, and WHOIS is not queried in bulk), but Canada-located vendors print what they charge for a `.ca` name by the year, and
`tools/vendor_billing.py` reads those pages daily. With five such prices or more the cell gives their range, the middle value and three
quoted examples. It never feeds `bill_amount_indicative`, and the nine-field count treats the amount as missing: the log has its own lines
("amount, calculated only", "all nine with the amount calculated").

A legal name taken from a site's copyright line must share a word with the organisation's own name or address. One that shares nothing is
taken last, only when it is a short company name ending with its legal form and not an agency's or a name printed on many sites, and the
cell then says "the copyright line of … names this company; it shares no word with the site's name". A schema.org node that only gives
the site as its own address counts when it names a legal person (Inc., Ltd., LLC, a numbered company), not otherwise.

Only the first line of the table meets the owner's bar of 06:24 as stated. The build log (SUMMARY.md) gives the rows of each value, tier by tier, and the Shopify
rows by the store's country (section 13 of Shopify's terms names two contracting parties for stores in the United States or Canada).
Among the services an organisation is seen to use, the one whose vendor bills by the month claims the row (`lead_strength`).

## Key columns
`buyer`, `buyer_website`, `email`, `email_type` (invoicing/AP, finance, purchasing, general), `email_check` (confirmed =
the referee re-opened the page and saw the address; since 2026-11-04 every package except P11 contains only `confirmed`
mailboxes — the dataset build's own mailboxes were re-submitted to the referee as `claude_buyer_ap_results_dsenrich01.csv`
and a row whose mailbox the referee has not yet seen waits in P11; every mailbox the referee verified for an organisation is considered, not only the one `org_mailboxes.csv` keeps per key), `email_evidence_url` + `email_evidence_quote` (≤300 characters
containing the address), `contract_status` (which relationship rule applies, with its source), `award_date`,
`contract_link` (the record), `vendor`, `vendor_country_basis` (the source's own proof that the vendor is located in
Canada), vendor registry fields when known, `buyer_phone` / `vendor_phone` / `vendor_emails` and the two
`*_contact_evidence_url` columns (the organisation's own site, see below), `keys` (all buyer keys folded into the row).

## Field completeness (owner, 2026-11-03)
Every cell of a delivered package is filled: from the record (identifiers, value, currency, dates, link), then the
release's vendor table (`vendors_enriched.jsonl.gz`: legal name, BN9, address, website, e-mails, only from an exact /
strong registry match) and buyer table (`buyers_enriched.jsonl.gz`: website, address); `buyer_website` falls back to the
mailbox's domain (or the evidence page's host when it is the same domain); `vendor_gst_hst_derived` = BN9 + RT0001,
always labelled derived; a currency missing from a Canadian / US government source is labelled "derived from the
source's government". A field no source gives is the literal `not_published` (Z: e-mail columns are `not_found_yet`).
`ranked_buyers.csv` keeps blanks (it is the working file batches.py reads).

Since 2026-11-04 two more fillers run before the packages are cut:
- **the lead's own record** (`data/incoming/claude/claude_lead_details.jsonl.gz`, written by the bridge in
  tools/lead_scanner.py): for buyers proven by a payment / subaward / filing record rather than a contract in the dataset,
  the record's amount (`contract_value`, suffixed with the source field's name, e.g. "313560 (source field:
  contractamount)"; a fund's or body's asset / budget figure is never taken), identifiers (`contract_reference`, a JSON of
  the record's id-like fields: PO, contract number, award id, filing id), start / end dates, the vendor's address fields
  and the record's title / description;
- **each organisation's own website** (`data/incoming/claude/claude_org_contacts.jsonl.gz`, written by tools/org_contacts.py):
  head-office address (schema.org PostalAddress, an `<address>` element, or a street address pattern with province +
  postal code / state + ZIP / UK postcode / Australian state + postcode; the head-office / city-hall labelled one when a
  page lists several), phone (tel: link or a number next to "Tel" / "Phone" / "Téléphone", never a fax) and role mailboxes
  (info@, contact@, sales@ ... on the organisation's own domain, never a named person). Fills `buyer_address` when the
  buyer table has none, `buyer_phone`, `vendor_address` when the record has none, `vendor_phone`, `vendor_emails` when the
  registry match has none; `buyer_contact_evidence_url` / `vendor_contact_evidence_url` name the page read, the date is
  in the JSONL (`date`), and the quote (≤300 characters around the address) in `address_quote`.

## Quality rules on top of the referee's checks
- A mailbox whose domain publishes no mail server (no MX, A or AAAA record; `data/incoming/claude/claude_mx_check.tsv`,
  tools/mx_check.py, DNS only — never an SMTP probe) is not delivered: the row stays in Z without it.
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

## Invoice-grade columns and AP grade (owner 2026-11-08; all appended, nothing renamed)
- `invoice_card_json`: the row as an invoice header — bill-to (legal name, address, tax number, language), submit-to (mailbox / portal /
  format / AP system; `portal_is_invoice_channel` is true only for an e-invoicing / supplier-invoice network — Ariba, Coupa, Tungsten,
  Basware, GHX, Jaggaer, Workday, Oracle iSupplier … — and `portal_class` names tender portals such as SEAO / MERX / bids&tenders, which
  are never an invoice channel and never count toward pay-on-sight tier 1), references the invoice must quote (PO rule, PO / contract / vendor id), terms (published terms, else the
  labelled default policy; method; cycle), tax (published status, else `DERIVED: …`; indicative rate; currency; vendor GST/HST and QST),
  vendor identity, follow-up. `invoice_readiness` = "n/11 invoice elements present"; `invoice_missing` lists the elements no source gave.
- `ap_grade` A–E, `ap_score` 0–100, `ap_grade_basis` (criteria met / missing / penalties) and `ap_gap_to_A` (what the row still lacks for A).
  A = referee-confirmed invoicing / AP mailbox on the buyer's own domain (or published on the buyer's own site) with MX, published legal
  name, invoice / billing address, PO rule and payment terms, no penalties (DMARC not enforced, BN conflict, vendor registry warning).
  Grade A is the standard every row is worked towards; `COVERAGE_VS_TARGETS.md` prints the A–E distribution and what blocks A per package.
- `payment_terms_default_policy`: a labelled default only — the Government of Canada 30-day directive for federal buyers, or the
  statutory prompt-payment rule for CONSTRUCTION contracts (federal Act s. 9(2), Ontario Construction Act s. 6.4(1), Alberta PPCLA
  s. 32.2(1): 28 days), each with the statute's URL, the date it was read and a quote. `payment_terms_as_published` is never filled
  from it.
- `buyer_tax_status_derived` / `tax_rate_indicative_derived`: GST/HST rules the buyer is subject to by type and province (CRA GST/HST
  Memorandum 18-2: provincial pay-and-rebate vs point-of-purchase relief; a municipality is not a government; HST 13 % / 15 % or
  GST 5 % by province), with URL, date read and quote. Derived, labelled, never written into `buyer_tax_exempt_status`.
