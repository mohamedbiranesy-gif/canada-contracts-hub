# Handoff — the final table of Canada Contracts Hub, row by row

*Written by lane `claude` on 2026-11-13, for whoever (human or AI) picks this up next. Generated from the corrected table by
`contrib/claude/final_correction/handoff.py`; the numbers in it are counted on that table, not remembered.*

---

## 0. Read this first

**The project is stopped.** The owner ended it on 2026-11-13 at 20:51 EST ("pull the plug"), after GitHub disabled Actions for the account at
23:39Z. Every workflow timer is commented out and no workflow starts another while `coord/ACTIONS_PAUSED` exists (see that file). Do not restart
anything without the owner's word. If GitHub turns Actions back on and the owner wants one last build, run `rank-buyers` by hand once.

**The deliverable** is one table: one row per organisation (the *buyer*) that a Canadian biller (the *vendor*) bills on invoice, payable by bank
transfer or cheque, with the organisation's own role mailbox. Two copies exist:

| copy | where | what it is |
|---|---|---|
| original | release `ranked-latest` on GitHub (`ranked_buyers.csv.gz`, build 2026-11-13 22:10Z), and on the owner's Mac: `~/Desktop/canada-contracts-hub-final/ranked_buyers_ORIGINAL_2026-11-13_2210Z.csv.gz` | the last table a build made |
| **corrected (use this one)** | the owner's Mac: `~/Desktop/canada-contracts-hub-final/ranked_buyers_CORRECTED_2026-11-14.csv.gz`, with `corrections.csv.gz` (every changed cell, before → after) and `folded_rows.csv` / `duplicate_buyers_dropped.csv` (rows taken out as a second row of one buyer), `counts.json` (every correction counted) and this handoff as `HANDOFF_ROWS.md` | the original with every correction written after the last build applied, row by row (section 12) |

Regenerate the corrected copy from the original at any time (about 25 minutes on two cores; 7 GB of memory is enough):

```
python3 contrib/claude/final_correction/correct_table.py correct ranked_buyers.csv.gz OUT
python3 tools/priority_sort.py OUT
python3 contrib/claude/final_correction/correct_table.py fold OUT
```

**Headline counts of the corrected table** (362,833 rows):

| | ready | all rows |
|---|---:|---:|
| rows | **298,247** | 362,833 |
| amount mark 1 — published $5,000+ | 2,152 | 3,861 |
| amount mark 2 — estimated $5,000+ | 743 | 788 |
| amount mark 3 — published under $5,000 | 238,784 | 270,922 |
| amount mark 4 — estimated under $5,000 | 23,447 | 24,490 |
| amount mark 5 — no amount | 33,121 | 62,772 |

Of the ready rows: 265,143 carry an amount and a billing period; 221,557 carry every main invoice field (amount, period, biller legal name and number, what is billed, how the bill arrives, how it is paid, when it is due); 2,895 are $5,000 or more a bill (published or estimated).

---

## 1. What a row is

A row is a **buyer** — one organisation, never twice (owner, 2026-11-11 20:36 EST: "no buyer twice is hard rule") — and **one current
relationship** in which a **Canadian biller** sends that buyer **a bill on invoice** that can be **paid by bank transfer or cheque**, plus the
buyer's own **role mailbox** where the bill can be sent. Everything else on the row is what an invoice of that relationship carries, populated as
far as anything published allows, each value with the page it was read on.

Four things make a row ready (`ship_ready` starts with `yes`), the owner's rule 13 (2026-11-11 16:01 EST: "invoice bank eft email Canadian vendor"):

1. **A Canadian biller with a relationship that is a fact and current.** The vendor is in Canada by the source's own vendor country or address
   field, never by its name (AGENTS.md §2.1). "A fact" is defined by the owner's rule 1: something whose being there means the relationship
   exists — a contract award, a register entry, a roster the biller publishes, a service seen running on the buyer's side, the distributor that
   by law serves the buyer's address. A vendor's client list is the vendor's statement and does not count alone.
2. **A bill on invoice.** A bill charged to a card on file (a Shopify store, self-serve software, most hosting plans) or paid through a go-between
   (a `.ca` name through its registrar) makes no row (owner's rule 6, 2026-11-11 13:09 EST: "if it's not on invoice, by bank transfer then it's
   no"). These rows were removed from the table.
3. **A bank payment** — bank transfer, cheque, pre-authorised debit, online banking bill payment — published by the biller, or inherent to the
   kind of relationship (section 6).
4. **The organisation's own role mailbox**, printed on its own pages and re-read by the referee (the `verify-and-merge` workflow re-fetched the
   page and found the address on it). Never a named person's mailbox, never webmail, never an address built from a pattern (§2.5). When the
   organisation publishes no invoicing mailbox, its purchasing mailbox, then its general mailbox (info@, reception@, greffe@) is used and labelled
   (owner, 2026-10-28; rule 9).

And two fields must be there: the biller's own printed address (it is what puts the biller in Canada) and, for a row that stands on where the
organisation is, the organisation's own address. Every other field of the row's kind that nothing published fills is **named** on the row
(`invoice_fields_missing_for_kind`) and does not take the row out; the row sorts below complete ones.

`ship_ready` reads:
- `yes` — every field of its kind, in the biller's or the record's own words;
- `yes (…)` — ready, and the bracket says what is by the kind of relationship, by where the organisation is, calculated, or not published;
- `no` — held back; `ship_ready_missing` gives every reason.

**Order of the table** (owner, 2026-11-11 20:36 EST: "mark everything, prioritise over 5000"): ready rows first, then the rest; inside each, by
`amount_mark` 1 to 5 (section 5); inside a class, the ranker's own order (the stronger relationship and the better mailbox first).

---

## 2. Files

| path | what |
|---|---|
| release `ranked-latest` | `ranked_buyers.csv.gz` (the table), `ranked_buyers.jsonl.gz` (the same rows as JSON lines), the packages (`P01…P15`, one row per buyer in the best package it qualifies for, by mailbox type and relationship), `BUILD.json` |
| release `dataset-latest` | the contract dataset behind the public-contract rows (`canadian_vendor_contracts.jsonl.gz`), vendors and buyers enriched |
| `coord/results/ranked/` | the build's reports: `SUMMARY.md` (counters of every rule), `AUDIT.md` (28 checks), `VALIDATION.md`, `CHANGELOG.md`, `COVERAGE_VS_TARGETS.md` |
| `contrib/claude/rank_buyers/rank.py` | the ranker: every row is made here (≈7,300 lines; read the comments, they carry the reasons and the owner's words) |
| `tools/relationship_rows.py` | the owner's test (`owner_test`), the kinds (`kind_of`, `FIELDS`, `BY_KIND`), payment route, amount marks, estimates |
| `tools/by_location.py`, `tools/bps_energy.py`, `tools/muni_energy.py`, `tools/abroad_utilities.py` | the electricity distributors by address; Ontario public bodies' own energy reports; municipalities' bills from their residents; utilities abroad owned by Canadian companies (rule 18) |
| `tools/payee_billing.py` + `tools/data/payees/*.json` | how the bodies behind registers, rosters and licences bill and take payment, each sentence read on their own page (verified by `payee_billing.py verify`) |
| `tools/tech_relationships.py`, `tools/vendor_billing.py` | service rows: what is seen on the buyer's side; the vendors' own price and terms pages |
| `tools/replay_owner_test.py` | measure a change to the owner's test on a built table before any build uses it |
| `contrib/claude/final_correction/` | the final correction (this handoff's table) and this handoff's generator |
| `AGENTS.md` | the contract every agent follows: the mission, the owner's rules 1–20, the hard rules §2 — read it whole |
| `STATE.md`, `coord/DECISIONS.md`, `CHECKS.json`, `docs/OWNER_GUIDE.md`, `docs/ROUTE_TO_1M.md` | state, decisions with reasons, checks, the owner's plain-language guide, the route to the goal |

---

## 3. Every column

The table has 253 columns. Fill = share of the ready rows of the corrected table where the column is not empty (and not `not_published`).

| column | what it holds | fill (ready) | example |
|---|---|---:|---|
| `jurisdiction` | the buyer's jurisdiction code (CA, a province, US, a US state, UK, EU …) as the source or the ranker set it | 71% | AB |
| `rank_group` | the ranker's group: tier letter + mailbox grade (GOLD = tier A/B with an invoicing/AP mailbox, confirmed); decides the package | 100% | GOLD |
| `completeness_score` | the ranker's sort score inside a tier (tier strength × 10 + mailbox grade × 6 + 3 if confirmed) | 100% | 67 |
| `data_quality_score` | 0–100: mailbox quality + relationship tier + share of key fields filled | 100% | 93 |
| `ship_ready` | the owner's test: yes · yes (what is by kind / by location / calculated / not published) · no | 100% | yes (when it is billed is by the kind of the contract (its own schedule of payments is not published)) |
| `ship_ready_missing` | every reason a row is not ready (or, for a ready row, empty) | 0% |  |
| `amount_mark` | 1 published $5,000+ · 2 estimated $5,000+ · 3 published under $5,000 · 4 estimated under · 5 no amount — with the figure it rests on | 100% | 1 published, $5,000 or more a bill (the contract's value 998,392: about 20,802 a month over its term, calculat |
| `payment_route` | how the bill is paid: on invoice, by bank transfer / cheque (in the biller's words, or by the kind of relationship); either; card; registrar … | 100% | on invoice, by bank transfer / cheque |
| `payment_route_basis` | the sentence that decides the route (the biller's own, quoted, or the kind's statement) | 100% | invoice under a public contract award, paid by the buyer's accounts payable (by the kind of relationship: the  |
| `invoice_fields_for_kind` | the kind of relationship and the fields an invoice of that kind carries | 100% | public contract: buyer address, vendor address, vendor tax or registration number, what is billed, amount, ref |
| `invoice_fields_missing_for_kind` | the fields of the kind that nothing published fills (named, not hidden) | 100% | none |
| `vendor_tax_or_registration_number` | the vendor's number for the invoice: BN / GST-HST (derived) or its home register's number, labelled | 85% | 130521958RT0001 — Business Number 130521958 |
| `ap_mailbox_ready` | the old label of the mailbox test, kept under its own name | 100% | yes |
| `buyer` | the organisation billed, by its own name (its domain name when the only name found was not a name) | 100% | Alberta Gaming, Liquor and Cannabis Commission (AGLC) |
| `buyer_website` | the organisation's own website | 100% | https://aglc.ca |
| `buyer_address` | its printed address (its own page, a register, a directory, or the place listing for its site), with where it was read | 95% | 50 Corriveau Ave, St. Albert, T8N 3T5, CA |
| `buyer_phone` | its published telephone | 55% |  |
| `buyer_contact_evidence_url` | the page the buyer's contact facts were read on | 73% | https://aglc.ca/contact-us |
| `buyer_legal_name_as_published` | its legal name as a register, the CRA charities list, a disclosure or its own page prints it (with the source) | 47% | City of Calgary (official name per Wikidata Q36312, official website on the organisation's domain (https://www |
| `buyer_bn_as_published` | its Business Number as published (with the source) | 16% | 897610002 (Canada's Business Registries, AB 209590090, 2026-11-12) |
| `buyer_bn_program` | the BN program account, when published | 16% | RT (GST/HST program account) |
| `buyer_trade_name_as_published` | its trade or other names as published | 76% | AGLC (the name on the organisation's own home page, https://aglc.ca/, read 2026-11-10) |
| `buyer_gst_hst_derived` | BN9 + RT0001 — derived, labelled; never looked up in the CRA registry | 16% | 124072513RT0001 (printed by the buyer itself; not derived) |
| `buyer_logo_url` | its logo as its site serves it | 71% | https://aglc.ca/themes/aglc/images/aglc-refresh-footer-logo.svg |
| `buyer_website_status` | whether the site answered, and from where the site came | 73% | site answers |
| `buyer_linkedin_url` | its LinkedIn page, when linked from its site | 16% | https://www.linkedin.com/company/aglc |
| `buyer_supplier_portals_linked` | supplier or bid portals its site links to | 0% | Workday (e-procurement / supplier portal): https://wd3.myworkday.com/mcgill/d/home.htmld |
| `buyer_registry_id` | its register entry (NEQ, corporation number …) | 21% | 208855536 (AB; https://ised-isde.canada.ca/cbr-rec/en/search?q=Beaumont%20Limitee) |
| `buyer_bn_note` | a conflict between two sources' BN, said | 0% |  |
| `buyer_type` | the kind of organisation (municipality, school board, hospital, university, company, non-profit …) from its name and jurisdiction | 100% | government ministry / agency |
| `sensitivity_tag` | a tag for sensitive buyers (health, shelters, police …), with the reason | 100% | none identified from the organisation's name / type |
| `sensitivity_flag` | yes when the buyer is sensitive (the row is held: a flag takes it out of the ready set) | 100% | no |
| `buyer_sector` | its sector as published or derived | 100% | government: provincial / federal |
| `peppol_participant_id` | its Peppol e-invoicing participant id, when registered | 0% | iso6523-actorid-upis 0060:824251540 |
| `peppol_registered` | whether it is in the Peppol directory | 100% | not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total) |
| `statutory_payees_inferred` | bodies an organisation of that type pays by law (CRA, provincial bodies) — inferred, no mailbox, not a supplier relationship | 100% | none inferred for this organisation type |
| `buyer_municipal_tier` | a municipality's tier (lower, upper, MRC …) from the provincial directory | 0% | local municipality (MAMH répertoire) (provincial municipal directory: https://donneesouvertes.affmunqc.net/rep |
| `buyer_population` | a municipality's population from the provincial directory or the census | 0% | 305437 (provincial municipal directory: https://donneesouvertes.affmunqc.net/repertoire/MUN.csv, 2026-11-08) |
| `directory_general_email` | the general mailbox a provincial directory lists (not the delivered mailbox) | 0% |  |
| `municipal_directory_source` | the provincial municipal directory used | 0% | https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963 |
| `buyer_fiscal_year_end` | its fiscal year end, when published | 0% |  |
| `buyer_charity_status` | its CRA registered-charity status | 3% |  |
| `buyer_charity_designation` | its CRA designation (charitable organisation, public / private foundation) | 3% | C; 0200 |
| `buyer_wikidata` | its Wikidata item | 1% | https://www.wikidata.org/wiki/Q36312; city; city in Alberta; big city |
| `buyer_founded` | its founding year, when published | 1% | 1875-00-00; 1884-11-07 (Wikidata Q36312, official website on the organisation's domain (https://www.calgary.ca |
| `buyer_budget_or_revenue` | its budget or revenue, when published | 0% | budget 40600000000 Q4917 (Wikidata Q11231, official website on the organisation's domain (http://www.dhs.gov)  |
| `buyer_employees` | its employees, when published | 0% | 670 (Wikidata Q212227, official website on the organisation's domain (https://asc-csa.gc.ca) + name; 2026-11-0 |
| `buyer_legal_form` | its legal form, when published | 21% | Alberta Business Corporation (Canada's Business Registries, AB 208855536, 2026-11-11) |
| `buyer_facts_provenance` | where each buyer fact on the row was read | 100% | address: the buyer's record / buyer table |
| `email` | the organisation's own role mailbox (re-read by the referee) | 100% |  |
| `email_type` | its role: invoicing/AP · finance/accounting dept or supplier-payment office · purchasing · general | 100% | invoicing/AP |
| `email_check` | how it was confirmed: confirmed (the referee re-fetched the page) · cross_verified (two lanes) · pending | 100% | confirmed |
| `mailbox_confidence` | the confirmation, in words, with its date | 100% | verified by the referee (page re-fetched); invoicing / AP mailbox |
| `evidence_age_days` | days since the mailbox's page was read | 100% | 5 |
| `reverify_due` | yes when the evidence is older than 60 days | 100% | no |
| `email_evidence_url` | the page that prints the mailbox | 100% | https://aglc.ca/sites/aglc.ca/files/forms/Cannabis_Licensed_Producer_Operations_Manual_20240619.pdf |
| `email_evidence_quote` | ≤ 300 characters of that page containing the mailbox | 100% |  |
| `email_evidence_context` | what else the page says around it (the role, the department) | 11% | invoice queries only — the page: “Invoice queries should be sent to ap.paymentsteam@durham.ac.uk . Do not send |
| `mailbox_recheck_note` | a later re-read of the mailbox, when one was made | 13% | mailbox seen again on the page when re-read 2026-11-08 |
| `mailbox_provenance` | who found the mailbox and how (crawler, lane, page) | 100% |  |
| `email_deliverability` | whether the mail domain publishes a mail server (MX), DNS only | 100% | domain publishes a mail server (MX) |
| `email_security_posture` | the mail domain's DMARC / SPF posture in words | 100% | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Proofpoint |
| `dmarc_policy` | DMARC policy (none / quarantine / reject / no record) | 100% | p=quarantine |
| `dmarc_record` | the DMARC record as published | 100% |  |
| `dmarc_record_domain` | the domain the DMARC record was read on | 58% | aglc.ca |
| `spf_policy` | the SPF policy | 100% | SPF ~all (soft fail) |
| `spf_record` | the SPF record as published | 88% |  |
| `mail_provider` | the mail provider by the MX hosts (Microsoft 365, Google, ISP mail …) | 100% | Proofpoint |
| `dns_checked_date` | when the DNS was read | 100% | 2026-11-06 |
| `mta_sts` | MTA-STS policy, when published | 100% | no MTA-STS record |
| `tls_rpt` | TLS-RPT record, when published | 100% | no TLS-RPT record |
| `bimi` | BIMI record, when published | 100% | no BIMI record |
| `ap_contact_name_as_published` | an AP contact's title or name as the organisation prints it on the same page (role first) | 0% |  |
| `ap_phone` | the AP telephone as printed on the mailbox's page | 1% |  |
| `invoice_mailing_address` | where invoices go by post, as printed | 1% | The City of Calgary, Accounts Payable, P.O. Box 2100, Station M, #8041, Calgary, AB T2P 2M5 |
| `invoicing_requirements` | what the organisation asks invoices to carry (PO, format, address …), quoted | 1% | Federal supplier-payment / direct-deposit contact listed by PSPC for this institution. |
| `payment_terms_as_published` | the buyer's own payment terms, quoted (net 30 …) | 2% | 30 days of receipt (as printed on https://aglc.ca/sites/aglc.ca/files/2017-11/17-11-29%20GM%20Handbook_1.pdf,  |
| `payment_terms_default_policy` | a jurisdiction's prompt-payment law or policy when the buyer publishes none (labelled) | 1% |  |
| `po_required_as_published` | whether invoices must carry a PO, as published | 1% | yes (as published: PO number or required) |
| `invoice_portal_url` | the buyer's invoice or supplier portal | 1% | https://portal.us.bn.cloud.ariba.com/discovery/public/leads/search — SAP Ariba |
| `invoice_portal_kind` | what that portal is (e-invoicing, supplier registration, tender portal …) | 1% | actionable supplier / invoice portal named by the buyer |
| `invoice_portal_note` | a note on the portal | 1% | (additional channel named on the buyer's page; the e-mail is the contact) |
| `ap_system_hint` | the AP / e-invoicing system the portal reveals (SAP Ariba, Coupa, Jaggaer …) | 1% | named on the buyer's page: SAP Ariba, ariba |
| `invoicing_requirements_structured` | the requirements as structured data | 100% | {"submission_channel": "e-mail + portal", "portal_url": "Coupa", "portal_kind": "actionable supplier / invoice |
| `buyer_payment_method_preference` | how the buyer pays its suppliers, as published (EFT, cheque …) | 1% | EFT is the preferred (as printed on https://stalbert.ca/dev/purchasing/invoicing/, re-read 2026-11-08) |
| `buyer_ap_cycle_published` | its payment run, as published | 0% | payments are processed weekly (as printed on https://stalbert.ca/dev/purchasing/invoicing/, re-read 2026-11-08 |
| `buyer_tax_exempt_status` | a published tax exemption | 0% | GST exemption number is #R124072513 (as printed on https://www.wcb.ab.ca/about-wcb/bid-and-vendor-information. |
| `buyer_tax_status_derived` | DERIVED: what tax an invoice to it carries (the place-of-supply rule, the public-service-body rebate, exports zero-rated …) | 94% |  |
| `tax_rate_indicative_derived` | the GST/HST/QST rate of its province, derived | 86% |  |
| `invoice_currency_derived` | the invoice currency, derived from the buyer's country when no record states one | 93% | EUR (derived from the buyer's country; CAD if the parties agreed so) |
| `buyer_esignature_preference` | a published e-signature preference | 0% | Notarius Inc (as printed on https://www.lloydminster.ca/media/0nhiqvhn/2026-01-lloydminster-accounts-payable-r |
| `pay_on_sight` | yes / routed / no: could an invoice made from the row clear AP matching on sight | 100% | yes |
| `pay_on_sight_missing` | what it lacks | 100% | bill-to legal name |
| `channel_tier` | 1 invoicing/AP mailbox or invoice portal · 2 finance · 3 purchasing/general · 0 unconfirmed | 100% | 1 |
| `invoice_text` | the draft invoice header (section 7) | 100% |  |
| `invoice_card_json` | the same as structured data (section 7) | 100% |  |
| `invoice_readiness` | n/14 invoice elements present | 100% | 11/11 invoice elements present |
| `invoice_missing` | the invoice elements missing | 100% | PO rule |
| `ap_grade` | A–E: how complete and how confirmed the AP data is | 100% | A |
| `ap_score` | 0–100 behind the grade | 100% | 85 |
| `ap_grade_basis` | the criteria met and missing | 100% |  |
| `ap_gap_to_A` | what grade A would need | 100% | none |
| `ap_payability` | payable today or what is missing (channel, bill-to, reference rule, tax) | 100% | payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first paymen |
| `supplier_setup_url` | the buyer's supplier set-up form or page | 0% | https://rogersgroupincint.com/become-a-vendor/ (linked as "Become a Vendor" (as printed on https://rogersgroup |
| `language_hint` | the language of the mailbox's page | 98% | en |
| `template_language` | the invoice's language (French first for Québec buyers) | 100% | en |
| `contract_status` | why the relationship is current, in words (the record's dates, the register's state, the service seen …) | 100% | active (published end date today or later) |
| `inference_confidence` | for a row by location: how certain the distributor is; n/a for a record | 100% | n/a (the relationship is a record, not an inference) |
| `relationship_kind` | the kind of relationship, in words | 100% | public contract / purchase award with a published end date (dated record) |
| `relationship_detail` | the relationship in one paragraph: dates, value, billing period, the buyer's other Canadian vendors | 100% |  |
| `how_relationship_was_found` | the tool and the source that found it | 100% | same as above: a dated award record from the public source in `source`, vendor located in Canada per the sourc |
| `relationship_fact_basis` | why it is a fact (fact, public record · fact, the biller's own roster · fact, seen on the buyer's side · by where it is · stated by …) | 100% | fact, public record: CanadaBuys award notices names the vendor and the contract (https://canadabuys.canada.ca/ |
| `recurring_billing` | the billing period: 1 monthly · 2 quarterly · 3 yearly or longer · 4 per order / project · 5 one-off … | 100% | 1 monthly |
| `billing_cadence` | the cadence in words, with whether it is published or by the kind | 100% | monthly (by the kind of relationship); about $20,802 a month (calculated: the published value over the publish |
| `recurring_billing_basis` | the sentence or rule the period rests on | 100% | the public record's own text: “Explorance MLY subscription Explorance MLY annual subscription until Feb 2027” |
| `bill_amount_indicative` | a published amount of one bill | 80% | US$67,277.44 FOB for the newest invoice (103568 of 2026-07-23) |
| `bill_amount_basis` | where that amount was read (quote, page, day) | 81% | the vendor's lowest published price by the month: “$ 80 Monthly” (https://incentre.net/, read 2026-11-13); the |
| `bill_items_as_published` | what is billed | 90% | DO 32615411 PEDIDO TRAMITE: C102211 DECLARACION(1-1) SE EXCLUYE DE RETIE SEGuN LA RESOLUCION 40117 DE ABRIL 02 |
| `bill_currency_as_published` | the bill's currency, as published | 77% | “All fees are in Canadian dollars.” (https://umanitoba.ca/explore/student-experience/tuition-and-financial-sup |
| `bill_delivery_as_published` | how the bill reaches the payer (an invoice by mail, a notice, a portal …), quoted | 81% | “SickKids will send you a bill about a month after your child is discharged.” (https://www.sickkids.ca/en/pati |
| `bill_payment_method_as_published` | how the biller is paid, quoted | 84% | “We accept Visa, Mastercard, and American Express.” (https://www.tritoncanada.ca/faqs/, read 2026-11-13) |
| `bill_tax_rule_as_published` | the tax the biller adds, quoted | 47% | “HST is applied to all consumption and fees.” (https://www.cornwallelectric.com/commercial/electricity-rates,  |
| `bill_identifier_format` | the number a bill carries (invoice, account, licence, policy number) | 0% | the exporter's invoice number, as the declaration cites it (103568) |
| `service_stops_if_unpaid` | what happens when it is not paid, quoted | 25% | “A late payment charge will be added to your account.” (https://app.bchydro.com/accounts-billing/bill-payment/ |
| `bill_due_terms_as_published` | when the bill is due, quoted | 79% | “Statements are dated the 1st of the month. The due date for the balance owing is the 10th of the month.” (bil |
| `bill_remit_to_as_published` | where a payment by post goes, quoted | 35% | “Alectra Utilities PO Box 3700, Concord, ON L4K 5N2” (https://alectrautilities.com/contact-us) (read 2026-11-1 |
| `billing_period_calculated` | a period calculated when none is published (labelled) | 0% |  |
| `bill_amount_calculated` | the estimate or calculation (estimated — / calculated —), with every figure it rests on | 77% | calculated — the whole value falls within one year (about 1,774,451 a month): the contract runs 2026-04-14 to  |
| `invoice_fields_present` | n/9 of the nine main invoice fields present | 100% | 9/9 |
| `invoice_fields_missing` | the main invoice fields missing | 100% | none of the nine |
| `contract_reference` | the record's reference (contract, licence, permit, patent, policy number …) | 22% | {"merx_id": "3961774765", "merx_reference_number": "0000322216", "contract_number": null, "awardee_index": 1} |
| `po_or_reference_to_quote` | the reference an invoice of this relationship should quote, and why | 100% | no PO number published; the contract number AB-2024-07911 (apc_reference_number) (published in the record) is  |
| `contract_title` | the record's title or what the relationship is for | 91% | Alberta Gaming, Liquor and Cannabis Commission - Negotiated Request for Proposal - Consulting Services for Off |
| `instrument_type` | the instrument as the source names it (contract, PO, standing offer, grant …) | 1% | contract award (OPEN-COMPETITIVE) |
| `instrument_type_normalized` | the instrument in a fixed list | 91% | contract |
| `procurement_method` | how it was awarded (open, limited, sole source …), as published | 1% | OPEN-COMPETITIVE |
| `commodity` | the commodity as published | 0% | 43000000, 43000000, 43000000, 43000000 Information Technology Broadcasting and Telecommunications > Data Voice |
| `contract_nature` | works, a service or goods — and by what | 1% | goods — by its commodity code UNSPSC 43000000 (Information Technology Broadcasting and Telecommunications >) |
| `contract_description` | the record's description | 21% | The City of Calgary (“The City”) is seeking interested Infoblox partners or resellers to provide annual mainte |
| `number_of_bids` | bids received, as published | 0% | 1 |
| `po_number_as_published` | the PO number in the record | 0% | 27-0035 (pd_procurement_id) |
| `po_numbers_this_pair_open_data` | other PO numbers of this buyer–vendor pair in open data | 0% | 2512934 (2020-04-27, 291250); SP-28822 (2016-06-09, 1884910,13) — No-reference (tender call or purchase-order  |
| `po_count_this_pair_open_data` | how many | 0% | 40 |
| `contract_numbers_this_pair_open_data` | contract numbers of this pair in open data | 0% |  |
| `contract_or_agreement_number` | the contract or agreement number | 22% | AB-2023-05732 (apc_reference_number) |
| `solicitation_or_tender_number` | the tender or solicitation number | 1% | 2023-022 (solicitation_number); 89c3f150-43b4-0465-2314-39c2ed480000 (opportunity_id) |
| `award_or_notice_id` | the award or notice id | 1% | f8cf354c-73ad-a665-1ec8-39c2ed480000 (award_id) |
| `buyer_vendor_id` | the vendor's id with the buyer, when published | 0% | d723ece1-f691-4111-87de-be6de7f88ddb (supplier_id) |
| `vendor_ids_in_record` | the vendor ids the record carries | 0% |  |
| `commodity_codes` | commodity codes (UNSPSC, GSIN, NAICS …) | 0% | UNSPSC 43000000 (Information Technology Broadcasting and Telecommunications > Data Voice or Multi); GSIN N5820 |
| `buyer_org_codes` | the buyer's department codes | 0% | crtc (pd_owner_org) |
| `amendment_or_modification` | an amendment's number or note | 0% | 0/P00001 (modification_numbers); P00001 (latest_modification_number) |
| `all_identifiers` | every identifier of the record, as JSON | 22% | merx_id=3961774765; merx_reference_number=0000322216; awardee_index=1 |
| `identifier_count` | how many | 22% | 4 |
| `invoice_reference_hint` | what to quote when no PO is published | 92% | contract or agreement number: AB-2023-05732 (apc_reference_number) — source ca_alberta_apc |
| `contract_value` | the record's published value, with its source field | 3% | 998392.15 |
| `currency` | its currency | 3% | CAD |
| `award_date` | when it was awarded or dated | 25% | 2024-01-15 |
| `start_date` | when it starts | 10% | 2023-12-15 |
| `end_date` | when it ends (published) | 7% | 2027-12-15 |
| `contract_term_as_published` | its term as published | 0% |  |
| `contract_link` | the record's page | 30% | https://purchasing.alberta.ca/posting/AB-2023-05732 |
| `source` | the source of the relationship | 100% | Alberta Purchasing Connection (APC) - awarded opportunities |
| `vendor` | the Canadian biller, by its name (inferred: … for a distributor by location) | 100% | Stantec |
| `vendor_legal_name` | its legal name, with where it was read (register, its own site, the record) | 88% | Stantec Inc. |
| `vendor_trading_name` | the name it trades under, when it differs | 15% | Stantec |
| `vendor_registry_id` | its register entry | 81% | Corporations Canada (corporation number): 3018784; corporation number 3018784 (Corporations Canada (open data) |
| `vendor_registry_url` | the register's page | 45% | https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=3018784 |
| `vendor_registered_address` | its registered office (register) | 45% | Suite 300, 10220 103 Avenue Northwest, Edmonton, AB, T5J 0K4, CA |
| `vendor_neq` | its Québec NEQ | 26% | 1170241336 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/datase |
| `vendor_qst_as_published` | its QST number, as printed | 0% | 1226940720 TQ0001 (as printed: https://floemtea.com/fr/policies/terms-of-service) |
| `vendor_legal_form` | its legal form | 45% | Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44 |
| `vendor_activity_code` | its activity code (REQ) | 4% | CAE 7799 — Engineering and environmental consulting |
| `vendor_employees_quebec` | its employees in Québec (REQ range) | 4% | De 1000 à 2499 |
| `vendor_establishments_quebec` | its establishments in Québec (REQ) | 3% | APPLIED ÉLECTRONIQUE: #100-5200 RUE Saint-Patrick, Montréal (Québec), H4E4N9 |
| `vendor_directors_range` | its number of directors (REQ range) | 0% | 3 to 20 directors (Corporations Canada) |
| `vendor_last_annual_filing` | its last annual filing | 2% | REQ annual declaration 2025; Corporations Canada anniversary 1994-03-30 |
| `vendor_address` | its printed address (what puts it in Canada), with the page | 100% | 200, 325 25th Street SE, Calgary, Alberta, T2A 7H8 |
| `vendor_country_basis` | the source field or page that says the vendor is in Canada, quoted | 100% | awards[].address.country == 'Canada' (stateProvince 'Alberta') |
| `vendor_bn9` | its Business Number, as published | 43% | 130521958 |
| `vendor_gst_hst_derived` | BN9 + RT0001 — derived, labelled | 43% | 130521958RT0001 |
| `vendor_website` | its website | 92% | https://www.stantec.com/ |
| `vendor_emails` | its role mailboxes, as its site prints them | 13% |  |
| `vendor_phone` | its telephone | 78% |  |
| `vendor_contact_evidence_url` | where its contacts were read | 82% | https://ionunited.com/contact-us |
| `vendor_logo_url` | its logo | 68% | https://www.stantec.com/static/img/favicon/apple-touch-icon.png |
| `vendor_website_status` | whether its site answered | 18% | site answers |
| `vendor_website_basis` | how its site was tied to it | 2% | the vendor is itself an organisation of this table: its website as this table's own row “BLDG Sci Advisory Inc |
| `vendor_linkedin_url` | its LinkedIn page | 14% | https://www.linkedin.com/company/ionunited |
| `vendor_industry_naics` | its NAICS code | 0% | 518 (schema.org JSON-LD naics on https://www.dayforce.com/) |
| `vendor_billing_ar_email` | its billing / receivables mailbox, as printed | 0% |  |
| `vendor_contacts_found_by` | who found its contacts | 0% | gemini lane, referee-verified on https://www.researchoninvestment.com/contact-us |
| `vendor_peppol_id` | its Peppol id | 0% |  |
| `vendor_facts_provenance` | where each vendor fact was read | 100% | name and address: the record's vendor block (AusTender Contract Notices (OCDS API)) |
| `method_notes` | notes on how the row was made | 100% |  |
| `facts_provenance_json` | the sources of the mailbox, the buyer's facts, the vendor's facts and the relationship, as JSON | 100% |  |
| `contracts_with_canadian_suppliers` | the buyer's records with Canada-located vendors in the contract dataset | 100% | 89 |
| `buyer_keys` | how many pipeline keys the buyer has | 100% | 1 |
| `keys` | the buyer's pipeline keys (b:…, lead:…) | 100% | b:c9cb2b15624c46b7 |
| `tier` | A · B · L · F · M · T · C · D · E · R · I · N (section 15) | 100% | A |
| `grade` | mailbox grade 4 invoicing/AP · 3 finance · 2 purchasing · 1 general | 100% | 4 |
| `acc` | True when the mailbox is confirmed | 100% | True |
| `distinct_canadian_vendors` | the buyer's distinct Canada-located vendors | 1% | 76 |
| `records_last_12_months` | its records of the last 12 months | 1% | 9 |
| `latest_award_date_any_vendor` | its latest award with any Canadian vendor | 1% | 2027-01-01 |
| `total_known_value_canadian_suppliers` | the total published value of its records with Canadian vendors | 1% | 589926191.03 CAD over 83 of 89 records with a published value |
| `other_canadian_vendors_sample` | some of its other Canadian vendors | 1% | Optiv Canada Inc. (2); M&A IT Tech Inc. (2); Staples Canada ULC (1); Connex Telecommunications Inc. (1); PC Co |
| `record_sources` | the sources of its records | 1% | Alberta Purchasing Connection (APC) - awarded opportunities (89) |
| `records_with_this_vendor` | its records with this vendor | 30% | 2 |
| `all_references_with_this_vendor` | every reference with this vendor | 1% | AB-2022-03632 (apc_reference_number) [2022-09-08] 170000.00 CAD; AB-2023-05732 (apc_reference_number) [2024-01 |
| `contract_value_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `start_date_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `end_date_from_pair` | the same, from another record of the same buyer–vendor pair | 0% | 2026-08-28 (another record of the same buyer-vendor pair: us_city_baton_rouge_expenditures:5598-0000025445-1-5 |
| `contract_title_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `contract_description_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `instrument_type_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `procurement_method_from_pair` | the same, from another record of the same buyer–vendor pair | 0% | limited (another record of the same buyer-vendor pair: 061833-2025-1 (contract_ids), Find a Tender Service (UK |
| `number_of_bids_from_pair` | the same, from another record of the same buyer–vendor pair | 0% | 1 (another record of the same buyer-vendor pair: 3535251855 (pd_procurement_id), Proactive Publication – Contr |
| `po_number_as_published_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `contract_or_agreement_number_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `solicitation_or_tender_number_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `award_or_notice_id_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `buyer_vendor_id_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `commodity_codes_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `buyer_org_codes_from_pair` | the same, from another record of the same buyer–vendor pair | 0% |  |
| `records_in_contract_dataset` | its records in the contract dataset | 100% | 89 records with Canada-located vendors (this row's organisation) |
| `other_relationship_sources` | other relationships on file for it (what the row does not stand on) | 40% | also seen in the lead files: contact_address/contact_country_name (FERC EQR seller identity, 2026q2) — CP Ener |
| `typical_contract_value_p50` | the median value of its contracts | 100% | 1150000.00 |
| `typical_contract_value_p75` | the 75th percentile | 100% | 5000000.00 |
| `typical_contract_value_p90` | the 90th percentile | 100% | 12000000.00 |
| `average_contract_duration_days` | its average contract term | 100% | 1668 |
| `contract_durations_counted` | how many terms were counted | 0% | 38 |
| `commodity_distribution_top3` | its top commodities | 100% | License/Maintenance fees for client software related to Dist (11); Data and database access services (10); Man |
| `year_over_year_spend_trend` | its spend year over year | 100% | 2022: 39673846; 2023: 30209627; 2024: 212463925; 2025: 3256127; 2026: 141219879; 2027: 400000 — decreasing vs  |
| `typical_cadence_days` | days between its awards | 100% | 148 |
| `vendor_concentration_top_share` | its top vendor's share | 100% | ESTI Consulting Services: 4% of 89 records |
| `all_canadian_vendors` | all its Canadian vendors | 100% | Explorance Inc (1); Justin Jagosh (1) |
| `pair_prior_records` | records of this buyer–vendor pair | 100% | 2 |
| `pair_first_or_repeat` | first or repeat relationship | 100% | repeat relationship (2 records, 2022-09-08 to 2024-01-15) |
| `pair_value_trend` | the pair's value over time | 100% | too few dated values (2) |
| `pair_dates_and_values` | the pair's records by date and value | 100% | 2022-09-08 170000.00; 2024-01-15 998392.15 |
| `most_recent_record_reference_any_vendor` | its most recent record's reference | 1% | AB-2026-00725 (apc_reference_number) — Green Shield Canada Insurance — Alberta Purchasing Connection (APC) - a |
| `org_group_key` | the grouping key of its contract records | 1% | alberta gaming liquor and cannabis commission |
| `vendor_registry_status` | the vendor's status in the register | 45% | Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (2014-07-28) |
| `vendor_registry_warning` | a warning from the register (struck off, inactive …): the row is held | 0% |  |
| `vendor_registry_note` | a note on the register match | 1% | another registry lists a lapsed registration (Corporations Canada (corporation number): Dissolve); the primary |
| `vendor_registry_match_level` | how the register match was made | 1% | exact |
| `vendor_incorporation_date` | when it was incorporated | 45% | 2014-01-01 |
| `vendor_years_in_business` | its years in business | 45% | 12.9 (since 2014-01-01, registry date) |
| `vendor_wikidata` | its Wikidata item | 0% | https://www.wikidata.org/wiki/Q2331913; business; public company |
| `vendor_founded` | its founding year | 1% | 1954-01-01 (Wikidata Q2331913, official website on the organisation's domain (https://www.stantec.com/) + name |
| `vendor_employees` | its employees, when published | 0% | 22000 (Wikidata Q2331913, official website on the organisation's domain (https://www.stantec.com/) + name; 202 |
| `vendor_bn_source` | where its BN came from | 43% | corporations_canada 3018784 (exact match) |

---

## 4. The kinds of relationship — what each row stands on, how deep it is, where it comes from

`invoice_fields_for_kind` names the kind and the fields an invoice of that kind carries; `relationship_kind` says it in words,
`relationship_fact_basis` says why it is a fact (or that it is not), `how_relationship_was_found` names the tool and the source, `contract_status`
says why it is current, `contract_link` / `source` point to the record.

**Depth, from strongest to weakest:**
1. **A record of the relationship itself, dated and current** — a public contract with a published end date (tier A) or awarded in the last 12
   months (B), an Ontario public body's own energy report (own report), an import declaration with the exporter's invoice number (export sale), a
   Form 5500 schedule naming the insurer and the policy (benefit plan).
2. **The biller's own current list** — a register of licences or registrations, the patent and trademark registers naming the agent of record, a
   stock exchange's list of issuers, a chamber's or association's member directory, a sponsor or exhibitor list, a dealer locator, a tenant
   directory (tier M and the rosters): current by construction (a lapsed member leaves the directory), but the amount billed to this buyer is not
   published.
3. **Seen on the buyer's side** — the buyer's own DNS records or site run on the vendor's service (tier T): the service is running today; who holds
   the account is normally the organisation, sometimes its web agency.
4. **By where the organisation is** — the distributor that by law bills electricity at the organisation's own printed address (tier I, rule 13
   since 2026-11-11 16:01 EST): the biller is certain for the address; whose name is on the account is not published, and every such row says so.

### utility account by location — 208,644 ready of 228,028 rows

**What it is.** The electricity distributor that, by law, serves the organisation's own printed address bills it every month or two on an invoice paid through a bank (rule 13, owner 2026-11-11 16:01 EST). Abroad, the same for the utilities a Canadian company owns (rule 18).

**Depth.** The biller is certain for the address; the account holder is not published (the organisation, its landlord, or both) and every row says so. Weakest of the kinds; it comes last for a buyer with any record (rule 13: a record or a service seen first).

**Source and tool.** `tools/by_location.py`: 68 distributors with their postal areas (each one's own territory page and rate page read and quoted); Ontario by the Ontario Energy Board's map of service areas (`tools/on_ldc_table.py`, postal code by postal code; a code near an edge or shared by two gets none); towns running their own utility over their whole territory (Westmount, New Westminster, Penticton, Coaticook …); Alberta left out (retail choice: no distributor's bill). The address is the organisation's own page, a register, or the place listing for its website (Overture Maps, Foursquare), said on the row. Rule 18 abroad: `tools/abroad_utilities.py` (retail service territories, ZIP codes wholly inside one territory, the parent's own page quoted for the ownership).

**Amount.** The distributor's own published rates at 2,500 kWh a month (a small office), estimated; municipalities outside Ontario from their residents (section 5).

**Caveats.** A tower, campus or business centre (50+ organisations at one postal code) is held; a postal code printed with another province is held; a city whose utility serves only part of it gets no distributor.

Invoice fields of the kind: buyer address, vendor address, what is billed, amount, billing period.

Ready rows by amount mark: estimated $5,000+ 20 · published under $5,000 201,681 · estimated under $5,000 1,796 · no amount 5,147.
How they are paid: on invoice; bank payment or card (the biller takes both) 138,977 · on invoice, by bank transfer / cheque 64,558 · by the kind of relationship (the biller's own words were not 5,109.
Biggest billers: Hydro-Québec (44,811) · BC Hydro (36,066) · Alectra Utilities Corporation (27,270) · Toronto Hydro (26,548) · Hydro One Networks Inc. (12,578) · Hydro Ottawa (7,419).

A ready row, as written (mailbox shown by its type only):

```
buyer:                             Fredericton
vendor:                            NB Power
relationship_fact_basis:           by where it is: the organisation's own address (E3B) lies in the exclusive territory of NB Power — NB Power distributes electricity across New Brunswick outside the municipal utilities of Saint John, Edmundston and Perth-Andover (Electricity Act); the postal areas of those three are left out. A fact
contract_status:                   billed by the electricity distributor of its address — by where the organisation is (postal area E3B), not by a record: NB Power distributes electricity across New Brunswick outside the municipal utilities of Saint John, Edmundston and Perth-Andover (Electricity Act); the postal areas of those three
contract_title:                    Electricity service to the municipality's facilities (its town hall's address: 397 Queen Street Fredericton, NB, Canada E3B 1B5)
recurring_billing:                 1 monthly
bill_amount_indicative:            from $30.87 a billing period
bill_amount_calculated:            estimated — about $112,000 a month before tax for the electricity of the municipality's own facilities (about $160,000 at the median), each billed on its account by this distributor: Fredericton had 63,116 residents (Statistics Canada, 2021 Census, table 98-10-0002-01, census subdivision 1310032: ht
amount_mark:                       2 estimated, $5,000 or more (112,000, calculated — see bill_amount_calculated; published: 30.87)
bill_delivery_as_published:        a bill: “All bills for service are due when rendered and are subject to a late payment charge when payments are received after the date specified on the bill.” (https://www.nbpower.com/en/accounts-billing/understanding-your-bill/rate-schedules-and-policies/f-billing-and-payments) (read 2026-11-11)
bill_payment_method_as_published:  through a bank or by automatic withdrawal from a bank account; a credit card with a fee: “Add NB Power as a payee for options to pay your bill in person, online or over the phone .” … “Never miss your bill due date with automatic payments from your bank account.” … “Easily make a secure, one-time pa
bill_due_terms_as_published:       “All bills for service are due when rendered and are subject to a late payment charge when payments are received after the date specified on the bill.” (https://www.nbpower.com/en/accounts-billing/understanding-your-bill/rate-schedules-and-policies/f-billing-and-payments) (read 2026-11-11)
payment_route:                     on invoice; bank payment or card (the biller takes both)
email_type:                        invoicing/AP
vendor_tax_or_registration_number: number 022248 in the New Brunswick Corporate Registry (Service New Brunswick), and LEI 549300MOGUBVU8NGZP02, as the global LEI register reco — this register entry carries no Business Number
ship_ready:                        yes (by where the organisation is: the biller is certain for the address, the account holder is not published)
```

### service seen on the buyer's side — 28,626 ready of 55,390 rows

**What it is.** The buyer's own site or DNS runs on a Canada-headquartered vendor's paid service that is billed on invoice (hosting, mail, DNS, platforms).

**Depth.** Seen today on the buyer's side; the account may be the organisation's or its web agency's. A service charged to a card on file is not a row (rule 6).

**Source and tool.** `tools/tech_relationships.py`, `tools/tech_portals2.py`, the DNS sweeps (`dns-services`, `ct-names`), the vendors' own billing pages (`tools/vendor_billing.py`, hand-read ones in `BILLING_BY_DOMAIN`).

**Amount.** The vendor's lowest published price for the product seen.

Invoice fields of the kind: buyer address, vendor legal name, vendor address, vendor tax or registration number, what is billed, amount, billing period.

Ready rows by amount mark: published under $5,000 21,612 · no amount 7,014.
How they are paid: on invoice; bank payment or card (the biller takes both) 26,064 · on invoice, by bank transfer / cheque 2,562.
Biggest billers: Web Hosting Canada (17,668) · doteasy (2,304) · APLUS CORPORATION (2,236) · Canadian Web Hosting (1,439) · Likuid.com (933) · Astral Internet Canada (550).

A ready row, as written (mailbox shown by its type only):

```
buyer:                             Paroisse de Notre-Dame-du-Sacré-Coeur-d'Issoudun
vendor:                            Web Hosting Canada
relationship_fact_basis:           fact, seen on the buyer's side: the buyer's own DNS records name the vendor's servers (, read 2026-11-10): the service is running. The vendor cuts an unpaid service off: “Services not paid on their due date risk being suspended, and may be terminated permanently shortly after, at WHC’s sole discreti
contract_status:                   active service seen in the buyer's public DNS records (2026-11-10): its DNS zone is served by ns2.whc.ca (NS record) — Canada-located provider whc.ca
contract_reference:                issoudun.qc.ca
contract_title:                    DNS / web hosting by whc.ca — its DNS zone is served by ns2.whc.ca (NS record): “issoudun.qc.ca NS ns2.whc.ca”
recurring_billing:                 2 monthly or yearly
bill_amount_indicative:            from C$2.79 a month
amount_mark:                       3 published, under $5,000 (the biller's published amount: 2.79)
bill_delivery_as_published:        “When we generate a new invoice, we'll send you an email with a copy of the invoice and will also make the invoice available in your Client Area” (terms of service)
bill_payment_method_as_published:  on its payment page: “Complete our online order form to generate an invoice and select Wire Transfer / Interac / Deposit as the payment method.” “North American Wire transfers or direct deposits at a CIBC branch (in North America) Please note: we do not accept wire transfers or direct deposits for a
bill_due_terms_as_published:       each invoice is due on the service's expiration date, the renewal invoice issued at least 15 days before: “A first payment is required prior to the activation of a service, and all following invoices must be paid in full prior to their due date.” … “WHC will generate renewal invoices automatically f
payment_route:                     on invoice; bank payment or card (the biller takes both)
email_type:                        invoicing/AP
vendor_tax_or_registration_number: 830136297RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed) — Business Number 830136297 (Canada's Business Registries, CC 7081936, 2026-11-11)
ship_ready:                        yes
```

### membership — 20,608 ready of 21,382 rows

**What it is.** The organisation is a member of a Canadian chamber, board of trade, association or accreditation body that bills dues each year.

**Depth.** The body's own current member directory (a lapsed member leaves it): the biller's own roster. BBB accreditation is a fee too.

**Source and tool.** Member directories read by `member-live` / `tools/member_lists.py` (GrowthZone / ChamberMaster / MemberClicks and the bodies' own pages), BBB accredited businesses.

**Amount.** The body's lowest published membership fee (the member's own dues are that or more).

Invoice fields of the kind: buyer address, vendor address, vendor tax or registration number, amount, billing period.

Ready rows by amount mark: published under $5,000 1,957 · estimated under $5,000 7,793 · no amount 10,858.
How they are paid: by the kind of relationship (the biller's own words were not 20,419 · on invoice; bank payment or card (the biller takes both) 116 · on invoice, by bank transfer / cheque 73.
Biggest billers: BBB Alberta and East Kootenay (763) · BBB Serving Central Ontario (477) · SWRBOT (434) · BBB serving Mainland British Columbia (375) · Greater Langley Chamber of Commerce (246) · Landscape Ontario Horticultural Trades Association (Landscap (241).

A ready row, as written (mailbox shown by its type only):

```
buyer:                             Beairsto Elementary School
vendor:                            Greater Vernon Chamber of Commerce
relationship_fact_basis:           fact, the biller's own roster: the Canadian body's own page names the organisation as a member in its member directory (https://business.vernonchamber.ca/list/member/school-district-vernon-no-22-546.htm)
contract_status:                   client listing on the vendor's own site (undated): member named in the member directory of the Canada-located body (chamber of commerce, board of trade, association) — members pay it dues
recurring_billing:                 3 yearly or longer
bill_amount_indicative:            from $299 a year
amount_mark:                       3 published, under $5,000 (the biller's published amount: 299)
bill_delivery_as_published:        “You receive a full year of membership and a renewal notice will be sent on the anniversary of the month you joined.” (https://www.vernonchamber.ca/faq/, read 2026-11-13)
payment_route:                     on invoice, by bank transfer / cheque — by the kind of relationship (the biller's own words were not found)
email_type:                        invoicing/AP
vendor_tax_or_registration_number: 123482044RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed) — Business Number 123482044 (Corporations Canada (open data), corporation number 10235, 2026-11-13)
ship_ready:                        yes (how it is billed and paid is by the kind of relationship, not yet in the biller's own words)
```

### licence or registration — 15,259 ready of 16,203 rows

**What it is.** The organisation holds a licence or registration in force with a Canadian body, which bills it to keep it (yearly, or at each renewal).

**Depth.** The body's own public register lists the holder today: current by construction.

**Source and tool.** City business licences (Vancouver, Calgary, Edmonton, Toronto — `tools/biz_licences.py`), the Régie du bâtiment du Québec, the CMEQ and the CMMTQ (`rbq-licences`), Québec's Office de la protection du consommateur, Health Canada's establishment and product registers (`tools/hc_registers.py`), ISED's radio licences, the HCRA, the RACJ, provincial resource registers and others (`authority-registers`). Natural persons and sole proprietors are left out.

**Amount.** The body's own fee table for that kind of licence, or the fee paid in the open data.

Invoice fields of the kind: buyer address, vendor address, what is billed, amount, billing period, reference.

Ready rows by amount mark: published $5,000+ 420 · estimated $5,000+ 159 · published under $5,000 13,202 · estimated under $5,000 435 · no amount 1,043.
How they are paid: on invoice, by bank transfer / cheque 8,528 · by the kind of relationship (the biller's own words were not 3,442 · on invoice; bank payment or card (the biller takes both) 3,289.
Biggest billers: Régie du bâtiment du Québec (5,019) · City of Vancouver (1,471) · The City of Calgary (1,281) · Innovation, Science and Economic Development Canada (1,233) · City of Edmonton (1,218) · City of Toronto (1,062).

A ready row, as written (mailbox shown by its type only):

```
buyer:                             Braemed Ltd.
vendor:                            Health Canada
relationship_fact_basis:           fact, public record: the body's own public register lists the organisation as licensed / registered / accredited today (https://health-products.canada.ca/mdel-leim/)
contract_status:                   holder of licence no. MDEL 1064 issued by a Canadian public body: Health Canada — first issued on an unstated date, no end or cancellation date in the list (the body's own public list of licences in force, read 2026-11-12); the holder pays the body to keep the licence
contract_reference:                MDEL 1064
contract_title:                    Medical device establishment licence 1064 (Health Canada, MDEL listing: Distribute, Import)
recurring_billing:                 3 yearly or longer
bill_amount_indicative:            C$5,519 a year for each medical device establishment licence (as of April 1, 2026)
amount_mark:                       1 published, $5,000 or more (the biller's published amount: 5,519)
bill_delivery_as_published:        an invoice from Health Canada at each yearly licence review: “We will issue an invoice after we receive and screen your ALR application for completeness.” (https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/establishment-licences/medical-devices-compliance-b
bill_payment_method_as_published:  through a Canadian financial institution's bill payment, direct deposit, wire transfer, cheque, bank draft or money order, or a card: “Payments can be made by applying an existing credit, payment through a Canadian Financial Institution (via Bill Payment Service - BPS), direct deposit, wire transfer
bill_due_terms_as_published:       “Payment is due upon issuance of the invoice.” “Interest on overdue accounts begins to accrue 30 days from the date of invoice issuance.” (https://www.canada.ca/en/health-canada/services/drugs-health-products/funding-fees/review-medical-device-establishment-licence.html, read 2026-11-12)
payment_route:                     on invoice; bank payment or card (the biller takes both)
email_type:                        invoicing/AP
ship_ready:                        yes
```

### agent of record — 12,818 ready of 13,586 rows

**What it is.** A Canadian patent or trademark agent named by CIPO's register as the agent of record for the organisation's patents or trademarks; the agent bills the owner for each step and for the official fees it advances.

**Depth.** A public register; the agent's own fees are not published.

**Source and tool.** CIPO's patent register (CSV extract) and trademark register (`pt-register`, `tm-register`, `pt-sites`, `tm-sites`); the firm's name with its legal form as the register prints it.

**Amount.** CIPO's official 2026 fees as a floor (section 5).

Invoice fields of the kind: buyer address, vendor address, vendor tax or registration number, what is billed, reference.

Ready rows by amount mark: estimated under $5,000 12,818.
How they are paid: by the kind of relationship (the biller's own words were not 10,726 · on invoice, by bank transfer / cheque 2,092.
Biggest billers: SMART & BIGGAR LP (1,838) · GOWLING WLG (CANADA) LLP (1,745) · BORDEN LADNER GERVAIS LLP (716) · MARKS & CLERK (516) · ROBIC AGENCE PI S.E.C./ ROBIC IP AGENCY LP (386) · OSLER, HOSKIN & HARCOURT LLP (354).

### not established — 0 ready of 11,894 rows

### sponsorship — 4,818 ready of 5,952 rows

**What it is.** A sponsor or exhibitor of a Canadian organisation's event or programme, billed the fee.

**Depth.** The organiser's own list; current only for this year's or an upcoming event; an in-kind or donors list, a foundation funding the organisation, or a past event is not a row.

**Amount.** Rarely published (sponsorship tiers are not tied to names).

Invoice fields of the kind: buyer address, vendor address, vendor tax or registration number.

Ready rows by amount mark: no amount 4,818.
How they are paid: by the kind of relationship (the biller's own words were not 4,816 · on invoice; bank payment or card (the biller takes both) 1 · on invoice, by bank transfer / cheque 1.
Biggest billers: Prospectors & Developers Association of Canada (PDAC) (220) · Newcom Media Inc. (Truck World) (89) · Manitoba Ag Days (65) · Canadian Greenhouse Conference (CGC) (48) · Interior Design Show (IDS Vancouver), Informa Connect (43) · JGS Events Inc. (dba Pacific Agriculture Show) (38).

### public contract — 3,056 ready of 5,788 rows

**What it is.** A contract, purchase order or award by a public buyer to a vendor whose address in the record is in Canada.

**Depth.** Strongest: a public record naming both parties, with value, dates and references. Current when the published end date is today or later (tier A), or the award is less than 12 months old (B; 12–36 months is L, not current alone); an award more than three years old with no end date is not current (rule 11).

**Source and tool.** The contract dataset: 82+ source pipelines (`scripts/<source>/`, notes in `notes/`), merged into the release `dataset-latest`; Canadian federal, provincial, municipal, school-board and health-authority disclosures, US federal (USAspending, subawards), states and cities, UK, EU (TED), Australia, and others; the vendor's Canada location read from the source's own vendor address or country field (`vendor_country_basis`).

**Amount.** The published value, spread over the term when the term is published; a framework ceiling is never a bill.

Invoice fields of the kind: buyer address, vendor address, vendor tax or registration number, what is billed, amount, reference.

Ready rows by amount mark: published $5,000+ 1,558 · estimated $5,000+ 35 · published under $5,000 309 · estimated under $5,000 26 · no amount 1,128.
How they are paid: on invoice, by bank transfer / cheque 3,056.
Biggest billers: KPMG LLP (70) · MNP LLP (42) · BDO Canada LLP (33) · Doane Grant Thornton LLP (32) · COR - Kashruth Council of Canada (19) · Bousfields Inc. (19).

A ready row, as written (mailbox shown by its type only):

```
buyer:                             Export Development Canada
vendor:                            TRITON Canada Inc.
relationship_fact_basis:           fact, public record: MERX public Awarded Solicitations (award notices) names the vendor and the contract (https://www.merx.com/exportdevelopmentcanadaedc/solicitations/Pre-employment-and-Exit-Interview-Services/0000320458?origin=0)
contract_status:                   active (published end date today or later)
contract_reference:                {"merx_id": "3930399870", "merx_reference_number": "0000320458", "contract_number": "080905", "awardee_index": 1, "solicitation_number": "26-005", "source_id": "PU.CC.Ont..1117844.C3479501"}
contract_title:                    Pre-employment and Exit Interview Services
recurring_billing:                 1 monthly
bill_amount_calculated:            calculated — the whole value falls within one year (about 5,687 a month): the contract runs 2026-10-01 to 2027-09-30 (364 days)
contract_value:                    68000.0
amount_mark:                       1 published, $5,000 or more a bill (the contract's value 68,000: about 5,687 a month over its term, calculated)
bill_payment_method_as_published:  “We accept Visa, Mastercard, and American Express.” (https://www.tritoncanada.ca/faqs/, read 2026-11-13)
payment_route:                     on invoice, by bank transfer / cheque
email_type:                        invoicing/AP
vendor_tax_or_registration_number: 821604451RT0001 — Business Number 821604451
ship_ready:                        yes (when it is billed is by the kind of the contract (its own schedule of payments is not published); not published: the purchase-order number the buyer requires on invoices (the vendor holds it))
```

### dealership — 2,728 ready of 2,878 rows

**What it is.** A dealer or retailer of a Canadian manufacturer or distributor, invoiced for the goods it buys for resale.

**Depth.** The supplier's own dealer locator; what the dealer buys is never published (no amount).

**Caveats.** A supplier's terms for its online shop (cards, PayPal, checkout) are a retail customer's, not the dealer's: they are not used.

Invoice fields of the kind: buyer address, vendor address, vendor tax or registration number.

Ready rows by amount mark: estimated $5,000+ 117 · no amount 2,611.
How they are paid: by the kind of relationship (the biller's own words were not 2,598 · on invoice, by bank transfer / cheque 130.
Biggest billers: Miles Industries (Valor Fireplaces) (161) · Paradigm Electronics Inc. (130) · Sabian Ltd. (121) · Ontario Cannabis Store (OCS Wholesale) (117) · Sherwood Industries Ltd. (Enviro) (76) · Royal Canadian Mint (69).

A ready row, as written (mailbox shown by its type only):

```
buyer:                             Pakalolo
vendor:                            Ontario Cannabis Store (OCS Wholesale)
relationship_fact_basis:           fact, the biller's own roster: the Canadian body's own page names the organisation as a dealer of its products (https://www.agco.ca/sites/default/files/opendata/AGCOWebSiteCRSANewProcessMapData.csv)
contract_status:                   dealer / retailer named by Ontario Cannabis Store (OCS Wholesale) on the Alcohol and Gaming Commission of Ontario's open-data list of authorized cannabis retail stores (status Authorized to Open, licence active), which every store buys from OCS Wholesale (https://www.agco.ca/sites/default/files/open
contract_reference:                CRSA1185461
recurring_billing:                 4 per transaction
bill_amount_calculated:            estimated — about C$421,500 a month for its 5 stores on the list (about C$84,300 a month per store on average: OCS Wholesale's wholesale revenue of $1,733.8 million in 2024–25 over the 1,709 to 1,719 Authorized Cannabis Stores of that year (1,714 on average), spread over 12 months; what this store b
amount_mark:                       2 estimated, $5,000 or more (421,500, calculated — see bill_amount_calculated)
bill_delivery_as_published:        an invoice for each order: “Separate invoices will be generated for Flow-Through orders and regular replenishment orders.” (https://learn.ocswholesale.ca/wp-content/uploads/2026/02/OCS-Wholesale-Authorized-Cannabis-Retailers-Handbook-February2026.pdf, read 2026-11-13)
bill_payment_method_as_published:  by pre-authorized debit from the retailer's bank account: “As part of your onboarding process, you must complete a PAD agreement to pay for your orders.” … “Once the PAD process is set up, you will not be required to initiate any payments for your orders, as we will retrieve the necessary funds dire
payment_route:                     on invoice, by bank transfer / cheque
email_type:                        general
ship_ready:                        yes (not published: vendor tax or registration number)
```

### benefit plan contract — 780 ready of 793 rows

**What it is.** A US employer's benefit plan insured by a Canadian insurer (Sun Life Assurance Company of Canada's U.S. branch — the Canadian legal entity itself) or paying a provider in Canada.

**Depth.** The plan's Form 5500 (US Department of Labor), Schedule A or C: a public record with the policy number and the year.

**Amount.** Premiums or commissions of the plan year (section 5).

Invoice fields of the kind: buyer address, vendor address, what is billed, amount, reference.

Ready rows by amount mark: published $5,000+ 1 · estimated $5,000+ 103 · estimated under $5,000 579 · no amount 97.
How they are paid: by the kind of relationship (the biller's own words were not 780.
Biggest billers: Sun Life Assurance Company of Canada (779) · HEALTH GAUGE (1).

A ready row, as written (mailbox shown by its type only):

```
buyer:                             CYRUSONE LLC
vendor:                            Sun Life Assurance Company of Canada
relationship_fact_basis:           fact, public record: the plan's Form 5500 Schedule A (US Department of Labor, plan year 2025-01-01 to 2025-12-31) names Sun Life Assurance Company of Canada as the insurer of its contract 920175, policy period to 2025-12-31, 581 persons covered (https://askebsa.dol.gov/FOIA%20Files/2025/All/F_SCH_A_
contract_status:                   insured benefit plan of a Canadian insurer: Sun Life Assurance Company of Canada insures the organisation's plan (CYRUSONE LLC EMPLOYEE WELFARE BENEFIT PLAN) — policy 920175, dental, life insurance, long-term disability, other, short-term disability, vision, 581 persons covered, policy period to 202
contract_reference:                920175
contract_title:                    group dental, life insurance, long-term disability, other, short-term disability, vision insurance (Form 5500 Schedule A)
recurring_billing:                 1 monthly
bill_amount_calculated:            calculated — more than US$8,444 a month (more than US$101,334 a year): the insurer paid US$101,334 in commissions on these contracts in plan year 2025-01-01 to 2025-12-31 (Form 5500 Schedule A, INS_BROKER_COMM_TOT_AMT); commissions are paid out of the premium, so the premium is more
amount_mark:                       2 estimated, $5,000 or more (8,444, calculated — see bill_amount_calculated)
bill_delivery_as_published:        by the kind of relationship: a premium statement each month for the policy year, the policy running to 2025-12-31
payment_route:                     on invoice, by bank transfer / cheque — by the kind of relationship (the biller's own words were not found)
email_type:                        invoicing/AP
vendor_tax_or_registration_number: NEQ 1143517614 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; re — the Québec register publishes the enterprise number, not the Business Number
ship_ready:                        yes (how it is billed and paid is by the kind of relationship, not yet in the biller's own words; the amount is calculated and labelled so)
```

### tenancy — 405 ready of 422 rows

**What it is.** A commercial tenant of a Canadian landlord (a mall, an office group), billed rent each month.

**Depth.** The landlord's own tenant directory. A Canadian group's buildings abroad are not rows (rule 19).

Invoice fields of the kind: buyer address, vendor address, vendor tax or registration number, billing period.

Ready rows by amount mark: no amount 405.
How they are paid: by the kind of relationship (the biller's own words were not 405.
Biggest billers: The Cadillac Fairview Corporation Limited (106) · Oxford Properties Group (50) · Primaris Management Inc. (34) · Morguard Investments Limited (28) · Simply Office (23) · Fonds de placement immobilier Cominar (23).

### exchange listing — 349 ready of 355 rows

**What it is.** A company listed on a Canadian stock exchange (TSX, TSXV, CSE), billed listing fees.

**Depth.** The exchange's own list of issuers.

Invoice fields of the kind: buyer address, vendor address, what is billed, amount, billing period, reference.

Ready rows by amount mark: published $5,000+ 143 · estimated $5,000+ 206.
How they are paid: by the kind of relationship (the biller's own words were not 206 · on invoice; bank payment or card (the biller takes both) 143.
Biggest billers: Canadian Securities Exchange (CNSX Markets Inc.) (206) · TSX Venture Exchange (TMX Group) (124) · Toronto Stock Exchange (TSX Inc., TMX Group) (19).

A ready row, as written (mailbox shown by its type only):

```
buyer:                             Keyera Corp.
vendor:                            Toronto Stock Exchange (TSX Inc., TMX Group)
relationship_fact_basis:           fact, public record: the exchange's own list of listed companies names the organisation as a listed issuer, with its symbol (https://www.tsx.com/en/listings/current-market-statistics)
contract_status:                   listed issuer on a Canadian stock exchange: Toronto Stock Exchange (TSX Inc., TMX Group) — symbol KEY, listed since 2003-05-29, on the exchange's list of listed companies (September 2026, https://www.tsx.com/en/listings/current-market-statistics) (read 2026-11-12); every listed company pays the exch
contract_reference:                symbol KEY (TSX)
contract_title:                    Listing on Toronto Stock Exchange, symbol KEY — Utilities & Pipelines, head office AB, Canada
recurring_billing:                 3 yearly or longer
bill_amount_indicative:            C$12,000 a year at the least (the exchange's published minimum: the base fee of its first tier)
bill_amount_calculated:            calculated — about C$150,000 a year: the exchange's published annual sustaining fee applied to the issuer's market capitalization of C$15,068,214,555 on September 2026 as the exchange's own list gives it (https://www.tsx.com/en/resource/571); the fee is calculated on the market capitalization of the
amount_mark:                       1 published, $5,000 or more (the biller's published amount: 12,000)
bill_delivery_as_published:        an invoice from the exchange every year: “The annual sustaining fee is invoiced in February of each year and calculated on the basis of the Market Capitalization of all TSX listed securities that are issued and outstanding on the Closing Price of such securities as at the last trading day of the pre
bill_payment_method_as_published:  by wire transfer, direct deposit or online banking bill payment with the customer number printed on the invoice, or by credit card: “Credit Card Select Wire Transfer Select Direct Deposit Select Bank Bill Pay Select” … “Online banking bill payment is available at most Canadian financial institutions
payment_route:                     on invoice; bank payment or card (the biller takes both)
email_type:                        invoicing/AP
vendor_tax_or_registration_number: 105255327RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed) — Business Number 105255327 (Canada's Business Registries, ON 11740, 2026-11-13)
ship_ready:                        yes
```

### utility account by own report — 109 ready of 112 rows

**What it is.** An Ontario public body's own energy report under O. Reg. 25/23 lists its facilities, their addresses and the electricity each bought from the grid; the regulation asks for a facility's report only where the body is issued the invoices for its energy.

**Depth.** A public record of the relationship and of its size, with the account holder (the body) published.

**Source and tool.** `tools/bps_energy.py` (Ontario Ministry of Energy and Mines open data), each facility's postal code to its distributor (OEB map).

**Amount.** Calculated from the body's own reported use (section 5).

Invoice fields of the kind: buyer address, vendor address, what is billed, amount, billing period.

Ready rows by amount mark: estimated $5,000+ 103 · published under $5,000 6.
How they are paid: on invoice; bank payment or card (the biller takes both) 106 · on invoice, by bank transfer / cheque 3.
Biggest billers: Hydro One Networks Inc. (56) · Alectra Utilities Corporation (7) · Enova Power Corp. (4) · GrandBridge Energy Inc. (3) · Toronto Hydro (3) · Synergy North Corporation (3).

A ready row, as written (mailbox shown by its type only):

```
buyer:                             District Municipality of Muskoka
vendor:                            inferred: Lakeland Power Distribution Ltd.
relationship_fact_basis:           fact, public record: District of Muskoka's own energy report for 2024 (Ontario Broader Public Sector energy reporting, open data of the Ministry of Energy and Mines: https://data.ontario.ca/dataset/5e976319-9769-4f77-aab9-d170e0131efe/resource/b6b569cf-5d3a-4b96-9972-ea428c316278/download/2024_final
contract_status:                   electricity account of its own facilities — District of Muskoka reports, under Ontario's O. Reg. 25/23, the electricity bought from the grid by 10 of its facilities in the territory of Lakeland Power Distribution Ltd. (5,399,534 kWh in 2024), and the regulation asks for a facility's report only wher
contract_title:                    Electricity service to 10 facilities of District of Muskoka in the territory of Lakeland Power Distribution Ltd. (Bracebridge, Baysville, Huntsville, Mactier, Port Carling)
recurring_billing:                 1 monthly
bill_amount_indicative:            from $47.07 a month
bill_amount_calculated:            estimated — about $67,400 a month before tax, from the body's own reported use: District of Muskoka reported 5,399,534 kWh of electricity bought from the grid in 2024 by these 10 facilities (about 449,961 kWh a month; 2024 data set: https://data.ontario.ca/dataset/5e976319-9769-4f77-aab9-d170e0131ef
amount_mark:                       2 estimated, $5,000 or more (67,400, calculated — see bill_amount_calculated; published: 47.07)
bill_delivery_as_published:        a bill, by mail or made available on line: the Ontario Energy Board's Distribution System Code, which binds every licensed distributor says how — “a bill will be deemed to have been issued to a customer: (a) if sent by mail, on the third day after the date on which the bill was printed by the distri
bill_payment_method_as_published:  by mail, at a financial institution or electronically; by credit card where the distributor takes one — the ways the Ontario Energy Board's Distribution System Code, which binds every licensed distributor counts a payment: “(a) if paid by mail, three days prior to the date on which the distributor r
bill_due_terms_as_published:       at least 20 days from the day the bill is issued: “the minimum payment period shall be 20 days from the date on which the bill was issued to the customer.” (s. 2.6.3 of the Ontario Energy Board's Distribution System Code, which binds every licensed distributor; https://www.oeb.ca/sites/default/files
payment_route:                     on invoice; bank payment or card (the biller takes both)
email_type:                        invoicing/AP
vendor_tax_or_registration_number: Ontario Energy Board electricity distribution licence ED-2002-0540 (its number in the regulator's public register of licensed distributors) — this register entry carries no Business Number
ship_ready:                        yes (the organisation's own energy report under Ontario's O. Reg. 25/23 names the facilities, and the regulation reports only those it is issued the invoices for; the amount is calculated from its reported use)
```

### export sale — 47 ready of 50 rows

**What it is.** An importer abroad buying from a Canadian exporter, on the exporter's commercial invoice.

**Depth.** Colombia's customs (DIAN) import declarations name the importer, the exporter, the exporter's invoice number and date, the FOB value and the payment form.

Invoice fields of the kind: buyer address, vendor address, what is billed, amount, reference.

Ready rows by amount mark: published $5,000+ 30 · published under $5,000 17.
How they are paid: on invoice, by bank transfer / cheque 47.
Biggest billers: TLC PHARMACEUTICAL STANDARDS (2) · VIZIMAX INC. (1) · ANDERSON WATTS LTD. (1) · CALKO CANADA/GREEN MOUNTAIN KNITTING (1) · EDDYFI CANADA INC (1) · 11919296 CANADA INC. O/A QUANTUMPAK (1).

A ready row, as written (mailbox shown by its type only):

```
buyer:                             HMV INGENIEROS LTDA
vendor:                            VIZIMAX INC.
relationship_fact_basis:           fact, public record: Colombia's customs (DIAN) publishes import declaration 32026001142881 of 2026-08-04, which names the organisation as the importer (NIT 860000656) and VIZIMAX INC. as the exporter, at 2284 DE LA PROVINCE STREET, LONGUEU, QUEBEC, Canadá, with the exporter's invoice 103568 of 2026-
contract_status:                   importer of record of goods invoiced by an exporter located in Canada: VIZIMAX INC. invoiced it on 2026-07-23 (invoice 103568, US$67,277.44 FOB) — import declaration 32026001142881 of 2026-08-04 published by Colombia's customs (DIAN); 1 declaration line from exporters in Canada on file from 2026-08-
contract_reference:                103568
contract_title:                    DO 32615411 PEDIDO TRAMITE: C102211 DECLARACION(1-1) SE EXCLUYE DE RETIE SEGuN LA RESOLUCION 40117 DE ABRIL 02 DEL 2024
recurring_billing:                 4 per transaction
bill_amount_indicative:            US$67,277.44 FOB for the newest invoice (103568 of 2026-07-23)
contract_value:                    67277.44 (VALOR_FOB_USD of the newest declaration: the exporter's invoice 103568 of 2026-07-23)
amount_mark:                       1 published, $5,000 or more (the contract's value: 67,277.44 USD)
bill_delivery_as_published:        the exporter's commercial invoice 103568 of 2026-07-23, cited in import declaration 32026001142881 (NUMERO_FACTURA, FECHA_FACTURA); shipped by aéreo, cleared at Aduanas de Bogotá -  Aeropuerto El Dorado
bill_payment_method_as_published:  “Mecanismo de compensación o cuenta de compensación en el exterior” (FORMA_PAGO of the import declaration; TIPO_IMPORTACION “Reembolsable”)
payment_route:                     on invoice, by bank transfer / cheque
email_type:                        invoicing/AP
vendor_tax_or_registration_number: 119469716RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed) — Business Number 119469716 (Canada's Business Registries, AB 2026498572, 2026-11-13)
ship_ready:                        yes
```


---

## 5. Amounts — published first, estimates labelled

Owner's rules 3 and 16: a published amount first; a calculated value only from published figures, saying so and saying from what
(`bill_amount_calculated` starts with `estimated —` or `calculated —`); never an estimate in a published cell; where nothing published supports
one, the cell says not published.

| column | holds |
|---|---|
| `contract_value` | the record's published value (a contract's total, a licence's fee paid, an import's FOB value), with its source field |
| `bill_amount_indicative` | a published amount of one bill (a fee in the biller's own table, a price list's lowest plan, the dues the body prints) |
| `bill_amount_basis` | the sentence or table line it was read in, the page and the day |
| `bill_amount_calculated` | the estimate or the calculation, labelled, with every figure it rests on |
| `amount_mark` | the class of the row's amount, and the figure it rests on: **1** published, $5,000 or more a bill · **2** estimated, $5,000 or more · **3** published, under $5,000 · **4** estimated, under $5,000 · **5** no amount (owner, 2026-11-11 20:36 EST: $5,000 a bill is a priority, not a wall) |

How each estimate is made (the code is the reference; these are its rules):

| kind | method |
|---|---|
| public contract | the contract's value spread over its own term (start to end) when both are published (`calculated —`); otherwise over the buyer's average contract term in the dataset, only when the buyer has at least 5 contracts and a plausible median (≤ $2 million) (`estimated —`); a framework, standing offer or multiple-award ceiling is never a bill (`5 no amount`) |
| utility account by location | the distributor's own published rates (fixed charge + energy price, read on its rate page) at a small office's use, 2,500 kWh a month — a floor for most organisations (`estimated —`) |
| municipality outside Ontario (by location) | its residents (Statistics Canada 2021 Census, table 98-10-0002-01) × the kWh a resident a year that Ontario municipalities of its size report under O. Reg. 25/23 (lower quartile for the mark, median beside it) × Hydro-Québec's 2025 price comparison for the province's city, the lower of its 10,000 and 100,000 kWh prices (`tools/muni_energy.py`); street lighting is not in the reports, so it is a floor |
| utility account by own report | each facility's reported grid electricity (Ontario BPS energy reports, O. Reg. 25/23) priced at its distributor's small-business rates (OEB file of current rates) or Hydro-Québec's comparison at its consumption level, summed by month |
| licence or registration | the body's own fee table for the licence's kind (RBQ, RACJ, CIPO, ISED spectrum, Health Canada …) or the fee the open data says was paid (Vancouver `feepaid`); a register with several types takes the schedule's own rule (`tools/payee_fees.py`) |
| agent of record | CIPO's official 2026 fees the agent advances and bills: at least $595.06 per trademark renewal (first class), at least $60.26 per patent maintenance fee (small entity) — the agent's own fee comes on top and is not published |
| membership | the body's lowest published membership fee (the member's own dues are that or more); a benefit's price or value, a discount, an individual's fee is not the dues |
| benefit plan contract | Form 5500 Schedule A: premiums received ÷ 12, or more than the commissions paid out of the premium ÷ 12 |
| export sale | Colombia's DIAN import declaration: the FOB value of the newest invoice, and the totals with this exporter |
| CMEQ / CMMTQ licences | the corporation's own yearly dues and the yearly fee to keep the licence, each published; their sum in `bill_amount_calculated` |
| service seen on the buyer's side | the vendor's lowest published price by the month or the year for the product seen (never a mailbox price for a DNS zone) |

---

## 6. How the bill comes and how it is paid

`payment_route` (and `payment_route_basis`, which quotes):
- `on invoice, by bank transfer / cheque` — the biller's own words name a bank payment;
- `on invoice; bank payment or card (the biller takes both)` — in; a card accepted beside a bank payment does not take the row out (owner, 13:58 EST: "In");
- `on invoice, by bank transfer / cheque — by the kind of relationship (the biller's own words were not found)` — the biller publishes nothing on
  it; the row says how a bill of that kind is billed and paid (below) and that it is by the kind (rule 13);
- `card on file, charged by the vendor`, `through the registrar of record`, `no invoice is sent …` — never ready (those rows were removed).

By the kind of relationship (`tools/relationship_rows.py BY_KIND`), used only where the biller's own sentence was not found:

| kind | how a bill of that kind is billed and paid |
|---|---|
| licence or registration | a public body's fee for a licence or a registration: a notice or an invoice by mail, paid by cheque or through a financial institution |
| membership | an association's dues: an invoice for each membership year, paid by cheque or bank transfer |
| dealership | a supplier's sales to its dealer: an invoice with each delivery, on terms, paid by cheque or bank transfer |
| tenancy | rent under a commercial lease: due each month, paid by cheque or pre-authorised debit |
| sponsorship | a sponsorship or an exhibitor's fee: an invoice from the organiser, paid by cheque or bank transfer |
| agent of record | an agent's professional fees and the official fees it advances: an invoice for each step, paid by cheque or wire transfer |
| promotional agency | a promotional agent's commission on the producer's sales in Québec: an invoice to the producer it represents, paid by bank (wire) transfer |
| exchange listing | a stock exchange's listing fee: billed by the exchange for each year or each month of listing, paid by wire transfer, pre-authorised debit or cheque |
| utility account by location | an electricity bill: issued every month or every two months, paid through a financial institution, by pre-authorised debit or by cheque |
| utility account by own report | an electricity bill: issued every month or every two months, paid through a financial institution, by pre-authorised debit or by cheque |
| benefit plan contract | an insurer's group premium or a plan provider's fee: a premium statement or an invoice, paid by ACH, wire transfer or cheque |

A biller's own sentence always wins: "card only" takes the row out, "we send no invoice" fails it. Never used for hosting or software, where the
common way is a card on file. The bodies with thousands of rows (the Régie du bâtiment du Québec, the cities of Calgary, Edmonton, Toronto, CIPO,
chambers …) were read by hand: `tools/payee_billing.py` and `tools/data/payees/*.json`, every sentence quoted with its page and day, and an entry is
used only after `payee_billing.py verify` found every quote on the page.

Bill columns: `bill_delivery_as_published` (how the bill reaches the payer), `bill_payment_method_as_published`, `bill_due_terms_as_published`
(when it is due), `service_stops_if_unpaid`, `bill_remit_to_as_published` (where a cheque goes), `bill_tax_rule_as_published`,
`bill_currency_as_published`, `bill_identifier_format` (the number an invoice carries), `bill_items_as_published` (what is billed),
`recurring_billing` (1 monthly · 2 quarterly · 3 yearly or longer · 4 per project / per order …) with `recurring_billing_basis` and `billing_cadence`.

---

## 7. The invoice a vendor could send

Each row with a mailbox carries a draft invoice header (`invoice_text`) and the same as structured data (`invoice_card_json`):

```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: <buyer legal name, or its name> — <address> — buyer tax no. <BN if published>
SUBMIT TO: <mailbox> (<type> mailbox, confirmed by the referee) | portal …
REFERENCE: <PO / contract / tender / vendor id> | PO rule: …
FROM / REMIT TO: <vendor legal name> — <remit address> | GST/HST <BN9>RT0001 (derived) …
TAX: <buyer's tax status, derived and labelled> | CURRENCY: … | TERMS: …
DESCRIPTION: <what is billed> | AMOUNT: …
```

`invoice_card_json` keys: `bill_to` (legal_name, legal_name_is_published, trade_name, address, tax_number, language), `submit_to` (email,
email_type, supplier_setup_url, portal_url, format, system, e_invoicing_peppol, portal_is_invoice_channel, portal_class), `references_required`
(po_required, po_number, contract_or_agreement_number, vendor_id_with_buyer, reference_hint), `terms`, `tax`, `vendor_identity` (legal_name, bn9,
neq, remit_address …), `follow_up`. Around them: `invoice_readiness` (n/14 elements present) and `invoice_missing`, `pay_on_sight` (could an
invoice made from the row clear AP matching), `channel_tier` (1 invoicing/AP mailbox or invoice portal · 2 finance · 3 purchasing/general · 0
unconfirmed), `ap_grade` A–E with `ap_score`, `ap_grade_basis`, `ap_gap_to_A`, `ap_payability`.

The fields an invoice of each kind carries (`tools/relationship_rows.py FIELDS`):

| kind | fields |
|---|---|
| public contract | buyer address, vendor address, vendor tax or registration number, what is billed, amount, reference |
| licence or registration | buyer address, vendor address, what is billed, amount, billing period, reference |
| exchange listing | buyer address, vendor address, what is billed, amount, billing period, reference |
| export sale | buyer address, vendor address, what is billed, amount, reference |
| benefit plan contract | buyer address, vendor address, what is billed, amount, reference |
| membership | buyer address, vendor address, vendor tax or registration number, amount, billing period |
| dealership | buyer address, vendor address, vendor tax or registration number |
| tenancy | buyer address, vendor address, vendor tax or registration number, billing period |
| sponsorship | buyer address, vendor address, vendor tax or registration number |
| agent of record | buyer address, vendor address, vendor tax or registration number, what is billed, reference |
| promotional agency | buyer address, vendor address, vendor tax or registration number, what is billed, reference |
| service seen on the buyer's side | buyer address, vendor legal name, vendor address, vendor tax or registration number, what is billed, amount, billing period |
| utility account by location | buyer address, vendor address, what is billed, amount, billing period |
| utility account by own report | buyer address, vendor address, what is billed, amount, billing period |
| .ca registration | buyer address, vendor legal name, vendor address, vendor tax or registration number, what is billed, amount, billing period |
| not established | buyer address, vendor legal name, vendor address, vendor tax or registration number, what is billed, amount, billing period |

---

## 8. Identifiers

| identifier | columns | rule |
|---|---|---|
| Business Number (9 digits) | `vendor_bn9`, `buyer_bn_as_published` | as published (registry, the CRA charities list, the federal grants disclosure, the organisation's own page) |
| GST/HST number | `vendor_gst_hst_derived`, `buyer_gst_hst_derived` | **derived**: BN9 + `RT0001`, always labelled derived — never published as such, never looked up in the CRA registry (CAPTCHA, §2.6) |
| Québec NEQ / QST | `vendor_neq`, `vendor_qst_as_published` | the Registraire des entreprises; QST only as printed |
| register entries | `vendor_registry_id`, `vendor_registry_url`, `vendor_registered_address`, `vendor_legal_form`, `vendor_incorporation_date`, `vendor_registry_status`, `buyer_registry_id` | Canada's Business Registries, Corporations Canada, REQ, BC OrgBook — matched by name; a partnership and a corporation of the same name are never matched |
| when the GST/HST is not public | `vendor_tax_or_registration_number` | the home register's number (NEQ, corporation number) fills the vendor's number, labelled as such (rule 11) |
| relationship references | `contract_reference`, `po_number_as_published`, `contract_or_agreement_number`, `solicitation_or_tender_number`, `award_or_notice_id`, `buyer_vendor_id`, `all_identifiers`, `po_or_reference_to_quote`, `invoice_reference_hint` | the record's own numbers; a licence, patent, trademark or policy number for the other kinds |
| others | `peppol_participant_id`, `vendor_peppol_id`, `buyer_wikidata`, `vendor_wikidata`, `org_group_key`, `keys` | `keys` are the buyer's keys in the pipeline (b:…, lead:…) |

---

## 9. Mailboxes

`email` is the organisation's own role mailbox; `email_type` its role (invoicing/AP · finance/accounting dept or supplier-payment office ·
purchasing · general); `email_check` how it was confirmed (`confirmed` = the referee re-fetched the page and found it; `cross_verified` = two
lanes quoted it from the same page); `email_evidence_url` and `email_evidence_quote` (≤ 300 characters containing the address) are the proof;
`mailbox_provenance` says who found it and how. Rules that keep a mailbox off the row: a named person's, webmail (gmail, outlook …), a hidden
form field only, a regional office's mailbox of a multinational on a body elsewhere, a mail domain that is not the buyer's own when the page does
not name the body, a recruitment / privacy / donations / media box. `email_deliverability`, `email_security_posture`, `dmarc_policy`,
`spf_policy`, `mail_provider`, `mta_sts`, `tls_rpt`, `bimi` describe the mail domain (DNS only). ISP-hosted municipal mailboxes (videotron.ca,
bellnet.ca) stay, labelled `mail_provider = ISP mail` (decision of 2026-11-04).

The corrected copy also takes off (section 12): the mailboxes of named persons that reached the table (`cindy.accounting@…`, `jen.accounting@…`);
a mailbox on another country's domain than both the organisation's site and its address (an affiliate's abroad — Deloitte & Touche LLP of Virginia
with `deloitte.be`, Hertz in Toronto with `hertz.nl` — or a namesake's); the site and mailbox of a namesake matched by name. A mailbox whose own page
says it is for queries only keeps its place under its true role (Durham University's AP mailbox: "Do not send invoices to this address").

**Addresses.** `buyer_address` may hold several parts (`; ` between them), each with where it was read. Read on the organisation's own pages, an
address can be someone else's: privacy and legal pages name the services a site uses — "Google LLC, 1600 Amphitheatre Parkway", "Cloudflare, Inc.,
101 Townsend St.", and every Shopify store's legal notice "Shopify Inc., 151 O'Connor Street, Ottawa". The corrected copy takes those parts out
(`address_checks.py` lists 31 such addresses), and a site template's sample address ("123 Main Street, New York, NY 10001", "Lorem ipsum"); a row
that stood on where the organisation is and was located by such an address has no relationship and is held (a Belgian store "in Ottawa" billed by
Hydro Ottawa). An address of another country than the organisation's own site and mailbox, read on that site, is another office's (taken out); a
register's address in one country with a site and mailbox of another is a namesake's site (held).

---

## 10. Evidence and provenance

Every researched value carries the page it was read on, the day, and a quote of at most 300 characters containing it (§2.4). The cells named
`*_as_published` quote; derived cells say `DERIVED` or `derived`; estimates say `estimated —` / `calculated —`; values by the kind of relationship
say so. `facts_provenance_json` gathers the sources of the mailbox, the buyer's facts, the vendor's facts and the relationship;
`buyer_facts_provenance`, `vendor_facts_provenance`, `method_notes` and `how_relationship_was_found` say how each was found.

---

## 11. The rules that never bend

The owner's rules are in AGENTS.md §1 (rules 1–20, each with his words and the date). The hard rules (§2) — a contribution that breaks one is
rejected: vendor in Canada by the source's own field, never by name; buyer named; ongoing = start ≤ today ≤ published end date (no end date:
kept and flagged); evidence or nothing (URL, date, quote ≤ 300 characters); organisational contacts only (never a person's mailbox, never a
pattern); no getting around blocks (CAPTCHA, login, bot check → `blocked`); no fabrication (`not_published` with the queries tried is an answer);
GST/HST derived, never published; at most 2 requests a second per host, identified user agent, cache.

Owner rules that shape every row: 6 (on invoice, by bank transfer — or no row), 8/14 (one row per buyer), 13 (four things; populate the rest;
say how), 15 ($5,000 a bill first, mark everything), 16 (every invoice field; estimates labelled), 18 (a utility abroad that a Canadian company
owns is a Canadian vendor: Tampa Electric, TEP, UNS Electric, Central Hudson, Green Mountain Power, Versant Power, Liberty's utilities, the
Caribbean utilities of Fortis, Emera and Algonquin — electricity only, never households), 19 (no other company abroad, even Canadian-owned), 20 (no
utility held jointly by several Canadian pension funds).

---

## 12. What the corrected copy changed, and why

Every changed cell is in `corrections.csv.gz` (row key, buyer, field, before, after).

| correction | rows | why |
|---|---:|---|
| CMEQ / CMMTQ licence: the corporation's own dues and fee | 1,011 | the corporation's own yearly dues and the yearly fee to keep the licence, each published, their sum calculated |
| a domain on Web Hosting Canada's parking nameservers (no hosting): no relationship | 2,304 | no hosting is billed: no relationship |
| bill details added from a body's own page (payee entries verified after the build) | 1,497 | how the body bills and takes payment, each sentence verified on its own page after the build (tools/data/payees) |
| buyer address: a site template's sample address taken out | 55 | "123 Main Street, New York, NY 10001", "Lorem ipsum" — a template's sample: taken out |
| buyer address: a site template's sample words taken out | 29 | "123 Main Street, New York, NY 10001", "Lorem ipsum" — a template's sample: taken out |
| buyer address: a web platform's own address taken out (Amazon) | 3 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Apple) | 1 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Automattic) | 5 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Cloudflare) | 26 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (GoDaddy) | 4 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Google) | 277 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (HubSpot) | 7 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (LinkedIn) | 7 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Mailchimp) | 22 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Meta) | 154 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Microsoft) | 18 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Salesforce) | 6 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Shopify) | 10 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Squarespace) | 1 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Stripe) | 3 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Wix) | 2 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (X / Twitter) | 25 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (YouTube) | 45 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: a web platform's own address taken out (Zoom) | 3 | Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out |
| buyer address: another country's than its own site and mailbox, read on that site (another office or a third party), taken out | 56 | read on its own site of another country: another office's or a third party's — taken out |
| buyer address: another office's (the company's legal form and its mailbox are of AT), taken out | 9 | the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out |
| buyer address: another office's (the company's legal form and its mailbox are of AU), taken out | 7 | the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out |
| buyer address: another office's (the company's legal form and its mailbox are of CH), taken out | 19 | the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out |
| buyer address: another office's (the company's legal form and its mailbox are of DE), taken out | 100 | the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out |
| buyer address: another office's (the company's legal form and its mailbox are of DK), taken out | 3 | the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out |
| buyer address: another office's (the company's legal form and its mailbox are of ES), taken out | 1 | the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out |
| buyer address: another office's (the company's legal form and its mailbox are of IT), taken out | 11 | the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out |
| buyer address: another office's (the company's legal form and its mailbox are of NL), taken out | 3 | the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out |
| buyer address: another office's (the company's legal form and its mailbox are of NO), taken out | 2 | the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out |
| buyer address: another office's (the company's legal form and its mailbox are of SE), taken out | 9 | the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out |
| buyer legal name cleared (a sole proprietor's own name) | 14 | a sole proprietor's own name is not written |
| buyer name corrected | 4,466 | the organisation's name out of a page's title or text, or its domain name where the only name found was not a name |
| buyer name corrected — HTML tags around the name removed | 1 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — UTF-8 read as Latin-1, read back | 4 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a breadcrumb (A > B): the organisation's part | 5 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a contact word after the name removed (Contact us at, Call now …) | 2 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a copyright line removed | 12 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a description after a comma, removed | 245 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a host name written as the name (www. …): the domain name | 211 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a line after a dot separator (address, trade-name note) removed | 3 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a mailbox or a social handle written as the name: the domain name | 28 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a menu's words after the name removed | 1 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a multilingual plug-in's tags ([:en] … [:fr] …): the first language's name | 1 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a placeholder page's words (under construction, coming soon) removed | 43 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a placeholder page's words (under construction, coming soon): the domain name | 1 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a quoted slogan after the name removed | 5 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a separator left at either end removed | 8 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a slogan or a line after the site's brand, removed | 48 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a social handle after the name removed | 3 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a street address after the name removed | 28 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a telephone number or a mailbox beside the name, removed | 68 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a telephone number or a mailbox written as the name: the domain name | 3 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a town and province after the name removed | 404 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — a year before the name removed | 3 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — an address written as the name: the domain name | 107 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — decorative dots and colons around the name removed | 89 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — double spaces collapsed | 160 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — the brackets around the name removed | 16 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — the page-title word Home / Accueil before the name removed | 59 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — the pavilion or group it is part of, after the name, removed | 44 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — the quotation marks of the name removed | 8 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — the words Home page / Page d'accueil removed | 153 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — the words Official site / Site officiel removed | 51 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — the words Welcome / Bienvenue removed | 37 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — what follows the legal form after a comma, removed | 67 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — where it is located, after the name, removed | 6 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name corrected — who operates it or whose division it is, after the name, removed | 43 | a page title's words around the name (title_names.py; each rule read against the rows it changes) |
| buyer name: not a name and no site of its own (the row is not ready) | 6 | no name and no site of its own: not ready (AGENTS.md §2.2) |
| buyer's site: a mail provider's domain, removed | 4 | the site was the domain of the organisation's mailbox (videotron.ca, sympatico.ca): removed |
| location row on a web platform's address: no relationship | 24 | see above: no relationship |
| location row whose site or mailbox is another country's: held | 175 | held: the organisation is not shown to be at the address |
| mailbox added (re-read by the referee before Actions stopped) | 26 | read on the organisation's own site and re-read by the referee before Actions stopped |
| mailbox of another country than the site and the address: held | 190 | held: an affiliate's or a namesake's mailbox |
| mailbox removed: a named person's | 5 | AGENTS.md §2.5: cindy.accounting@…, jen.accounting@… are persons' mailboxes |
| mailbox: its role corrected from its own page | 1 | the page says what the mailbox is for (Durham University: invoice queries only, “Do not send invoices to this address”) |
| member dues amount cleared (a benefit's price or value, not the dues) | 60 | a member benefit's price or value is not the dues |
| municipality outside Ontario: electricity estimated from its residents | 256 | electricity estimated from its residents (tools/muni_energy.py), a floor |
| municipality outside Ontario: electricity estimated from its residents ($5,000 a month or more) | 23 | electricity estimated from its residents (tools/muni_energy.py), a floor |
| not ready -> ready | 19 | rows that received a mailbox the referee had re-read before Actions stopped |
| ready -> not ready | 2,944 | all the rows the corrections took out of the ready set (the reasons follow) |
| ready -> not ready: field: buyer address | 81 | a row by location whose address was taken out (a platform's, a template's) or whose postal code lies in another province than the one printed: the distributor is not certain |
| ready -> not ready: field: vendor address | 8 | the source prints no address for the vendor (what puts it in Canada), or the address was read on the buyer's own site |
| ready -> not ready: mailbox: on another country's domain | 140 | a mailbox of an affiliate abroad or a namesake (Deloitte & Touche LLP of Virginia with deloitte.be) |
| ready -> not ready: no mailbox | 6 | a named person's mailbox taken off, or a namesake's site and mailbox |
| ready -> not ready: relationship not established | 36 | a foundation that funds the organisation is not its biller |
| ready -> not ready: relationship: the address the distributor was named for is a site template's sample addres | 19 | a site template's sample address (123 Main Street … M1M 1M1) named the distributor |
| ready -> not ready: relationship: the address the distributor was named for is a web platform's own | 24 | a Shopify store's legal notice names Shopify's head office (151 O'Connor Street, Ottawa): the store is not there |
| ready -> not ready: relationship: the organisation and the biller are one | 4 | a body does not bill itself (a chapter named by its parent's name, a utility at its own address) |
| ready -> not ready: relationship: the organisation's domain is on Web Hosting Canada's parking nameservers, wh | 2,131 | WHC's own help page: its parking nameservers serve “All domain names without hosting” — a registration, not a hosting bill (owner's rule: no row) |
| ready -> not ready: relationship: the organisation's site and mailbox are another country's | 144 | a places listing in Canada that gives a site abroad (a namesake's), or a Canadian office with its parent's mailbox abroad |
| ready -> not ready: relationship: the vendor is a company abroad that a Canadian company owns, not a Canadian  | 1 | rule 19: a company abroad that a Canadian company owns (John Hancock) |
| ready -> not ready: relationship: the vendor's own name is a U.S. legal entity's | 382 | rule 19 (owner 2026-11-13 11:44 EST): a company abroad is not a Canadian vendor — 336 of them the exhibitors and sponsors of Marketplace Events LLC's shows |
| ready -> not ready: relationship: the vendor's printed address is in the United States | 1 | O'Reilly Media of Santa Rosa, CA: the record's "Canada" was read from California's code |
| ready -> not ready: site: the organisation's site and mailbox are another country's | 7 | a register's address in one country, a namesake's site in another |
| ready -> not ready: site: the record's buyer is CA's | 1 | the record's government is one country, the site and mailbox another's (the U.S. Treasury given the Australian Treasury's) |
| ready -> not ready: site: the record's buyer is US's | 1 | the record's government is one country, the site and mailbox another's (the U.S. Treasury given the Australian Treasury's) |
| record's address in one country, site and mailbox of another: held (a namesake's site) | 18 | held: a namesake's site |
| record's buyer of one country, site and mailbox of another: held (a namesake's) | 2 | held: a namesake's site and mailbox |
| row with no vendor at all: no relationship record | 66 | no biller: no relationship record (tier N) |
| site and mailbox removed: a namesake's site | 1 | a site matched by name to another organisation (a German firm's for a U.S. exporter) |
| the organisation and the biller are one: no relationship | 35 | same name or same site: a body does not bill itself |
| vendor address: the receiving facility of an EPA export notice (the shipper's address was in its place) | 2 | a U.S. EPA hazardous-waste export notice: the Canadian receiving facility is the vendor; the shipper's address had been put in its place |
| vendor legal name cleared (a sentence of a legal page, no legal form, not the vendor's name) | 920 | a sentence of a terms page that shares a word with the vendor is not its legal name ("Voice over Internet Protocol" for Storm Internet) |
| vendor's address in the United States read as Canada: no relationship | 1 | no relationship: not a Canadian vendor |
| vendor's site: the buyer's own, removed with what was read on it | 4 | the vendor's site was the buyer's (a municipality's list of local merchants): removed with what was read on it |

Cells changed, by column: `amount_mark` 2,375 · `bill_amount_basis` 1,071 · `bill_amount_calculated` 1,290 · `bill_amount_indicative` 1,071 · `bill_delivery_as_published` 1,395 · `bill_due_terms_as_published` 485 · `bill_items_as_published` 1,011 · `bill_payment_method_as_published` 406 · `buyer` 4,466 · `buyer_address` 948 · `buyer_legal_name_as_published` 14 · `buyer_website` 5 · `contract_title` 279 · `email` 32 · `email_type` 32 · `invoice_fields_missing_for_kind` 1,418 · `payment_route_basis` 142 · `relationship_kind` 66 · `service_stops_if_unpaid` 117 · `ship_ready` 3,806 · `ship_ready_missing` 3,511 · `tier` 66 · `vendor_address` 2 · `vendor_legal_name` 920 · `vendor_website` 4.

Then one row per organisation (`tools/priority_sort.py`) and one row per website and name (the fold):

```
one row per organisation: rows of an organisation that has a better row, left out (it keeps the best class, then the stronger relationship and the better mailbox): 20 — {('joined through another row', 'ready'): 3, ('mail domain+postal', 'ready'): 1, ('name+mail domain', 'not ready'): 1, ('name+mail domain', 'ready'): 3, ('name+postal', 'not ready'): 9, ('name+postal', 'ready'): 2, ('name+site', 'not ready'): 1} (out/ranked/duplicate_buyers_dropped.csv lists each)
priority order (rows that meet the test first, then by amount): ready, published, $5,000 or more: 2153 · ready, estimated, $5,000 or more: 743 · ready, published, under $5,000: 240918 · ready, estimated, under $5,000: 23448 · ready, no amount: 33122 · not ready, published, $5,000 or more: 1709 · not ready, estimated, $5,000 or more: 45 · not ready, published, under $5,000: 30016 · not ready, estimated, under $5,000: 1043 · not ready, no amount: 29658 — 362855 rows in 301 s
after the late rules (3 rows held), sorted again: one row per organisation: rows of an organisation that has a better row, left out (it keeps the best class, then the stronger relationship and the better mailbox): 0 — {} (out/ranked/duplicate_buyers_dropped.csv lists each) priority order (rows that meet the test first, then by amount): ready, published, $5,000 or more: 2152 · ready, estimated, $5,000 or more: 743 · ready, published, under $5,000: 240915 · ready, estimated, under $5,000: 23447 · ready, no amount: 33121 · not ready, published, $5,000 or more: 1709 · not ready, estimated, $5,000 or more: 45 · not ready, published, under $5,000: 30007 · not ready, estimated, under $5,000: 1043 · not ready, no amount: 29651 — 362833 rows in 291 s 
after the parked-domain rule (2,131 rows held), sorted again: one row per organisation: rows of an organisation that has a better row, left out (it keeps the best class, then the stronger relationship and the better mailbox): 0 — {} (out/ranked/duplicate_buyers_dropped.csv lists each) priority order (rows that meet the test first, then by amount): ready, published, $5,000 or more: 2152 · ready, estimated, $5,000 or more: 743 · ready, published, under $5,000: 238784 · ready, estimated, under $5,000: 23447 · ready, no amount: 33121 · not ready, published, $5,000 or more: 1709 · not ready, estimated, $5,000 or more: 45 · not ready, published, under $5,000: 32138 · not ready, estimated, under $5,000: 1043 · not ready, no amount: 29651 — 362833 rows in 292 s
one row per website and name: {'rows': 362833, 'folded (ready)': 3, 'folded (not ready)': 19}
after the late rules: one row per website and name: {'rows': 362833}
after the parked-domain rule: one row per website and name: {'rows': 362833}
```

How the corrections were made: each rule was written, run over every row, and its changes read before it was kept — the name rules
(`title_names.py`) were rewritten four times after reading their 2,000-odd changes (they had cut "Drivers On Call" to "Drivers On", "Ministère de
l'Environnement, de la Lutte contre les changements climatiques …" at its first comma, "Phoenix Contact" to "Phoenix"); the address rules
(`address_checks.py`) three times (a Canadian postal code typed with the letter O read as a British postcode; a German GmbH's own `.de` mailbox
held instead of its U.S. office's address being taken out; an embassy's mailbox on its government's domain). A person-name test for buyers was
tried and left out: it took "Tim Hortons" and "Paul Davis" for persons.

What the corrected copy could **not** apply (it needs a build's inputs): a municipality's record row giving way to its estimated electricity, a
legal name from another source where a junk one was cleared (the cell is left empty and the field shows as not published), mailboxes the
referee had not re-read when Actions stopped, the draft invoice header of the rows that received a mailbox in the correction (left empty), and the
packages (`P01…P15`) and JSON-lines copy (the release still holds the 22:10Z ones).

---

## 13. Known limits — said plainly

- **Rows by location are the bulk** (208,644 (70%) of the ready rows): the biller is certain, the account holder is not published, and the amount is a
  small office's estimate unless the organisation reports its own use (Ontario public bodies) or is a municipality outside Ontario.
- **"By the kind of relationship"**: 48,501 ready rows say how a bill of their kind is billed and paid because the biller publishes nothing on
  it; the biggest billers among them (one page read there would fill their rows): GOWLING WLG (CANADA) LLP (1,745); Central Hudson Gas & Electric Corporation (1,492); Tucson Electric Power Company (1,483); City of Vancouver (1,471); Green Mountain Power Corporation (1,232); Sun Life Assurance Company of Canada (779); BBB Alberta and East Kootenay (763); BORDEN LADNER GERVAIS LLP (716); Home Construction Regulatory Authority (HCRA) (533); Corporation des maîtres électriciens du Québec (CM (524); MARKS & CLERK (516); BBB Serving Central Ontario (477).
- **Amounts**: 265,144 ready rows carry an amount; of those, 241,492 published and 23,652 estimated. Member dues are the body's lowest
  published fee, not the member's own; an agent's own fees, a dealer's purchases and a sponsor's tier are not published.
- **Mailboxes**: 291,664 ready rows carry a general mailbox (the organisation publishes no invoicing, finance or purchasing one); the owner ruled it
  fine (rule 9).
- **Rule 19 judgement**: 336 exhibitors and sponsors of Marketplace Events' shows are held as billed by a U.S. LLC ("Marketplace Events LLC", with
  Canadian offices; Investment Canada lists the LLC as a Canadian business in Beechville, NS). If the owner reads it otherwise, they come back by
  removing that one register match (coord/DECISIONS.md, 2026-11-14).
- **Names**: a buyer whose only name found was not a name shows its domain name (zakaccounting.ca); about 31,942 ready rows are named by a
  domain.
- **Dates move**: the table means "current on 2026-11-13" (`coord/config.json`). Of the ready rows, 1,551 carry a published end date within
  30 days of it and 4,459 within 90 days; 1,388 ready public contracts have no published end date (an award of the last 12 months,
  tier B). Read `end_date` against the day of use.
- **Values are as the source publishes them**: a contract value is the record's own (a group purchase can be published under one member — the
  village of Senneville's road-salt contract of $23.5 million is one of them); the figure is not converted to Canadian dollars (the currency
  follows it in `amount_mark` when it is not the dollar).
- **Mailboxes at an internet provider**: 51 ready rows carry the organisation's own mailbox at videotron.ca, bell.net, sympatico.ca, shaw.ca,
  cogeco … — printed by the organisation as its address, kept (decision of 2026-11-04); the webmail rule names the free webmail services.
- **Broken characters**: 96 ready rows carry a replacement character (U+FFFD) in a name, an address or a title, where a page was read in the
  wrong encoding; it cannot be read back without the page (the buyer's name in such a row was replaced by its domain name).
- **Names**: the corrected copy cleaned thousands of names (section 12), but a few hundred ready rows still carry a page's words rather than the
  organisation's name (a service and a town: "Dentist in Bracebridge", a slogan) — the row's website and mailbox identify it.
- **Service rows**: a row that stands on the DNS servers of a hosting company is held when the company's own words say those servers carry no
  hosting (Web Hosting Canada's parking nameservers: "All domain names without hosting"); other companies' domain-only servers (a registrar's DNS,
  a free plan) were not re-examined one by one, and a site's account can be its web agency's rather than the organisation's.
- **Nothing here is legal or tax advice**: tax cells marked DERIVED follow the general rules (place of supply, public service bodies, exports) and
  say so.

---

## 14. If the project resumes

1. Read AGENTS.md, then `coord/ACTIONS_PAUSED`, `STATE.md` (top), `coord/DECISIONS.md` (bottom), this file.
2. Only with the owner's word: revert the commit that added `coord/ACTIONS_PAUSED`, then bring the crawlers back far slower than before (in the 24
   hours before GitHub's block the repository ran 583 workflow runs, 253 hours of run time, most of them crawls that restarted themselves; GitHub's
   terms bar a disproportionate burden and, on GitHub-hosted runners, activity unrelated to the software project).
3. Before any build uses a change to the owner's test, measure it: `python3 tools/replay_owner_test.py ranked_buyers.csv.gz` (it caught two errors
   on 2026-11-14 that would have shipped). A change to rank.py is checked with `python3 -m pyflakes` (a sample run, `RANK_SAMPLE=50`, needs more
   than 7 GB of memory).
4. Work billers first: one page read at a biller fills thousands of rows (rule 16). The billers with the most ready rows still billed "by the kind"
   are listed in section 13.
5. Never: a person's mailbox, a guessed address, webmail, a CAPTCHA or login worked around, the CRA GST/HST registry automated, an estimate in a
   published cell, a company abroad as a Canadian vendor (except rule 18's utilities), a buyer twice.
6. After any new build, run the final correction over its table (the three commands of section 0) — until its rules are moved into the build:
   the name rules (`title_names.py`), the address checks (`address_checks.py`), the site checks, the mailbox lists (`REVIEWED_OUT`,
   `PERSON_MAILBOX`, `WRONG_SITE`, `TYPE_OVERRIDE`) and the EPA export fix of `correct_table.py`. Two of its rules already are in rank.py (legal-page
   names, separators at a name's ends). Its lists are by address, not by row: a new build keeps them right.
7. What would add most, in order: (a) read the billing pages of the billers still "by the kind" (section 13 lists the largest — Gowling WLG,
   Central Hudson, Tucson Electric Power, the City of Vancouver, Green Mountain Power, Sun Life …): one page fills thousands of rows' payment and
   delivery fields in the biller's own words; (b) re-read by the referee the mailboxes found after Actions stopped
   (`data/incoming/claude/claude_buyer_ap_results_c5k*.csv` whose rows have no `verified` outcome); (c) the $5,000+ rows held for no mailbox
   (`contrib/claude/c5k_sites.py`, `c5k_mailboxes.py --sites`); (d) the organisations abroad tied to a Canadian biller by a record (the second half
   of the route to a million, `docs/ROUTE_TO_1M.md`).

---

## 15. Words used

**buyer** — the organisation billed. **vendor / biller** — the Canadian organisation that sends the bill. **referee** — the `verify-and-merge`
workflow (`tools/ingest_results.py`) that re-fetches every evidence page and keeps only values it finds on it. **tier** — A contract with a
published end date ≥ today · B awarded in the last 12 months · L 12–36 months ago · F older or ended · M register / roster of a Canadian body ·
T service seen on the buyer's side · C/D named as a client by the vendor (dated D) · E linked from the vendor's site · R `.ca` registration ·
I by where the organisation is · N no relationship record. **kind** — the relationship's kind (section 4). **lane** — an agent's share of the work
(claude, chatgpt, codex, gemini, jules).
