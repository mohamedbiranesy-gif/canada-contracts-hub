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
`buyer_bn_program`, `vendor_registry_warning`, `sensitivity_flag`, `buyer_sector`, `evidence_age_days`, `reverify_due`,
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
`coord/results/ranked/batches/<package>.csv` — one CSV per package; a package over ~45 MB is delivered in numbered part files
(`P13_…_part1_of_4.csv` …, same columns, split only by size). `coord/results/ranked/ranked_buyers.csv.gz` — every row incl. Z, gzipped
(GitHub refuses files over 100 MB). `SUMMARY.md`, `VALIDATION.md`, `AUDIT.md` + `audit_flags.csv`, `DMARC.md` + `dmarc_no_enforcement.csv` next to them;
`contracts/` holds every contract record of the delivered buyers with all identifiers (gzipped part files).

## Mailbox rules
Webmail addresses (gmail, hotmail, outlook, yahoo, icloud, proton…) are never delivered, whoever publishes them: a webmail account is
not an organisational mailbox. ISP-hosted mailboxes that a small municipality publishes as its official contact (videotron.ca, bellnet.ca…)
are kept and labelled `mail_provider = ISP mail`.

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
