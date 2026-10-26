# Buyer enrichment v2 (buyers_enriched_v2.jsonl) — 2,055 buyers added later

Generated 2026-10-25T22:58:38Z by `scripts/enrichment_buyers_v2/notes.py` (re-run after each assemble). Output: `enrichment/v2/buyers_enriched_v2.jsonl`, one line for **every** one of the 2055 buyers in `enrichment/v2/buyers_new_input.jsonl` (input order; the 651 buyers with high/medium-confidence contracts come first), keyed by `buyer_key`, same record layout as `enrichment/buyers_enriched.jsonl` (see `notes/enrichment_buyers.md`). Buyers with nothing found still get a line whose `notes` says so. Pipeline = copy of `scripts/enrichment_buyers/` adapted in `scripts/enrichment_buyers_v2/` (originals and `enrichment/buyers_enriched.jsonl` untouched); work files in `enrichment/work_buyers_v2/`, new downloads in `downloads/enrichment_buyers_v2/`.

## Coverage (all 2055 buyers / 651 high-medium buyers)

| field | all buyers | high/medium buyers |
|---|---|---|
| official_website (directory, parent organisation's site, or known official domain; `extras.website_check` = crawl status) | 1502 | 562 |
| directory identifiers (Wikidata QID, Ontario board number, …; dataset identifiers are in `identifiers.from_dataset`) | 520 | 277 |
| address (directory, else buyer address as published in the notices, some partial) | 402 | 306 |
| ap_contact.emails (supplier-invoicing / accounts-payable role mailboxes, own or parent organisation's) | 302 | 111 |
| ap_contact.invoice_portal (SAP Business Network/1GX, Ontario Vendor Portal, Ariba …) | 188 | 44 |
| ap_contact.invoicing_requirements (curated text or page excerpt) | 393 | 151 |
| procurement_contact.emails (role mailboxes) | 372 | 160 |
| procurement_contact.url | 409 | 195 |
| general_contact.emails | 387 | 224 |

Of the 150 distinct organisations with the most high/medium contract records (divisions/ministries joined to their parent): website 145, AP mailbox 40, AP mailbox or invoice portal or invoicing instructions 58, procurement mailbox or page 94.

By source group of the buyer (first source; n / high-medium / website / AP e-mail / AP e-mail-or-portal-or-instructions):

| source | buyers | h/m | website | AP e-mail | AP any |
|---|---|---|---|---|---|
| ca_bidsandtenders | 292 | 183 | 253 | 36 | 60 |
| ca_bc_ministry_awards | 238 | 0 | 224 | 1 | 2 |
| ca_alberta_apc | 226 | 223 | 185 | 15 | 32 |
| ca_nova_scotia | 222 | 8 | 106 | 2 | 29 |
| ca_saskatchewan | 187 | 4 | 74 | 4 | 6 |
| ca_newfoundland | 135 | 37 | 102 | 49 | 50 |
| ca_city_toronto | 132 | 11 | 132 | 132 | 132 |
| ca_merx | 126 | 56 | 71 | 16 | 20 |
| ca_biddingo | 68 | 19 | 46 | 4 | 6 |
| us_state_virginia | 59 | 0 | 15 | 0 | 0 |
| undp | 40 | 0 | 40 | 0 | 0 |
| us_state_texas_lbb | 34 | 30 | 27 | 4 | 8 |
| ca_city_ottawa | 21 | 16 | 21 | 21 | 21 |
| us_state_massachusetts | 21 | 0 | 21 | 0 | 21 |
| us_state_ny_abo | 16 | 3 | 2 | 0 | 1 |
| us_state_vermont | 16 | 0 | 16 | 0 | 0 |
| ca_alberta_sole_source | 15 | 15 | 15 | 0 | 15 |
| us_state_alaska | 12 | 0 | 12 | 0 | 0 |
| ca_nwt | 11 | 11 | 9 | 9 | 9 |
| no_opentender | 11 | 0 | 9 | 0 | 0 |
| us_state_oregon | 10 | 6 | 3 | 0 | 0 |
| nl_tenderned | 10 | 2 | 7 | 0 | 0 |
| us_county_montgomery_md_spending | 9 | 1 | 9 | 0 | 0 |
| eu_institutions_opentender | 9 | 0 | 9 | 0 | 0 |
| us_county_miami_dade | 8 | 0 | 8 | 0 | 0 |
| pe_oece | 7 | 3 | 3 | 0 | 0 |
| es_placsp | 7 | 7 | 0 | 0 | 0 |
| cdb | 7 | 2 | 1 | 0 | 0 |
| who | 7 | 0 | 7 | 0 | 0 |
| us_city_mesa_az | 7 | 0 | 7 | 0 | 0 |
| se_opentender | 7 | 0 | 4 | 0 | 0 |
| us_county_fulton_ga | 7 | 0 | 7 | 7 | 7 |
| us_city_la | 6 | 0 | 6 | 0 | 0 |
| cl_mercado_publico | 6 | 0 | 0 | 0 | 0 |
| ch_opentender | 6 | 0 | 3 | 0 | 0 |
| dk_opentender | 6 | 0 | 6 | 0 | 0 |
| us_city_mesquite_tx | 6 | 0 | 6 | 0 | 0 |
| au_wa | 4 | 4 | 3 | 0 | 0 |
| us_city_baton_rouge | 4 | 0 | 4 | 0 | 4 |
| us_city_corona_ca | 4 | 0 | 4 | 0 | 0 |
| fi_opentender | 4 | 0 | 3 | 0 | 0 |
| us_county_montgomery_md | 3 | 3 | 3 | 0 | 0 |
| us_city_indio_ca | 3 | 0 | 3 | 0 | 0 |
| us_city_richmond_ca | 3 | 0 | 3 | 0 | 0 |
| us_city_nyc | 2 | 1 | 2 | 0 | 0 |
| si_mju | 2 | 0 | 0 | 0 | 0 |
| us_city_providence | 2 | 0 | 1 | 0 | 0 |
| hr_eojn | 2 | 0 | 1 | 0 | 0 |
| rw_umucyo | 2 | 0 | 0 | 0 | 0 |
| us_state_oklahoma | 2 | 0 | 2 | 0 | 0 |
| ca_ontario_vor | 1 | 1 | 1 | 1 | 1 |
| us_ny_mta | 1 | 1 | 1 | 1 | 1 |
| us_state_delaware | 1 | 1 | 1 | 0 | 0 |
| fao | 1 | 1 | 1 | 0 | 0 |
| ec_sercop | 1 | 1 | 0 | 0 | 0 |
| us_state_texas_dir | 1 | 1 | 1 | 0 | 0 |
| us_city_austin | 1 | 0 | 1 | 0 | 0 |
| is_opentender | 1 | 0 | 0 | 0 | 0 |
| co_secop | 1 | 0 | 0 | 0 | 0 |
| py_dncp | 1 | 0 | 0 | 0 | 0 |
| zm_zppa | 1 | 0 | 1 | 0 | 0 |

Record additions vs v1 layout: `extras.parent_organisation` (name, key, jurisdiction, basis, website) for divisions and provincial/state government units — the AP/invoicing facts of the parent apply to them (e.g. every "City of Toronto – <division>" gets the City's accounts-payable requirements; every GNL department gets the central GNL invoice mailbox); `extras.jurisdiction_candidates` for 8 buyer keys whose bare name ("Infrastructure", "Finance", "Justice", "Education", "Municipal Affairs", "Executive Council", "Public Service Commission", "Legislative Assembly", "Advanced Education", "Agriculture"…) is used by departments of several governments in the merged data — no single organisation is asserted, instead one entry per government with that government's central AP facts (pick by the record's source); `identifiers.wikidata_qid`; `extras.website_check.reused_from_v1`.

Parent organisations assigned (747 buyer keys): Government of British Columbia 212, City of Toronto 132, Government of Newfoundland and Labrador 51, United Nations Development Programme (UNDP) 40, Newfoundland and Labrador Health Services 38, Government of Saskatchewan 33, Government of Alberta 28, Government of Nova Scotia 27, City of Ottawa 22, Commonwealth of Massachusetts 21, State of Vermont 16, Montgomery County, Maryland 12, State of Alaska 12, Government of the Northwest Territories 8, Miami-Dade County 8, World Health Organization (WHO) 7, City of Mesa, Arizona 7, Fulton County, Georgia 7, City of Los Angeles 6, European Commission 6, City of Mesquite, Texas 6, University of Toronto 5, City of Baton Rouge / Parish of East Baton Rouge 4, City of Corona, California 4, Ministerie van Defensie (Netherlands) 4, City of San José, California 3, City of Indio, California 3, City of Richmond, California 3, Government of Manitoba 2, City of New York 2, Toronto Transit Commission 2, Geological Survey of Norway (NGU) 2, ETH Zürich 2, State of Oklahoma 2, Government of Ontario 1, Government of Yukon 1, State of Delaware 1, Government of Saint Kitts and Nevis 1, Government of The Bahamas 1, Government of Saint Vincent and the Grenadines 1, Government of Antigua and Barbuda 1, Government of Saint Lucia 1, Government of Belize 1, EPFL 1

## Sources (fetched 2026-10-25 unless stated)

Directory / website sources:
| source | match confidence | buyers |
|---|---|---|
| parent-organisation rule | strong | 747 |
| Wikidata | strong | 433 |
| alias rule | strong | 265 |
| Wikidata | weak | 48 |
| Ontario Ministry of Education, School board and school autho | exact | 39 |
| website field of the buyer contact block in the contract not | strong | 13 |

- Parent-organisation rules (`classify.py`): name patterns for divisions ("City of Toronto - …", "City of Ottawa - …", "Commonwealth of Massachusetts - …", "State of Vermont — …", "UNDP - …", "NL Health Services - …", …) and provincial/territorial government units: buyers published by a provincial government's own award source (BC ministry awards, Alberta sole-source disclosure, Alberta APC ministries list, Nova Scotia / Saskatchewan / Newfoundland / NWT sources) whose names are department-like (no municipal designation, no university/board/authority/corporation/… words) → that government. Official sites of the parents are listed in `bulk_v2.py` (PARENT_SITE); government portals were not crawled (their central AP pages were researched directly).
- Wikidata SPARQL (https://query.wikidata.org/sparql, 25 batches 2026-10-25T22:18:25Z – 2026-10-25T22:19:20Z, raw JSON in `downloads/enrichment_buyers_v2/dir/wikidata/`): exact label/alias (en, fr) lookup of name variants (full name, designation-stripped core, "X County"/"County of X"/"Regional Municipality of X" …) → items with official website P856, country P17, class P31 and the province/state reached through P131*. Accepted only when the item is in the buyer's country and province/state (province from the source, notice address, MERX location, or the bids&tenders portal time zone), with municipal class preferred for designated names and full-name labels preferred over core labels; ties with different websites are left unresolved (noted). 'strong' = province verified; 'weak' = unique match without province evidence.
- Ontario Ministry of Education "School board and school authority contact information" (data.ontario.ca, September 2026 CSV, `dir/on_school_board_contact_list_september2026_en.csv`, 85 boards: board number, address, phone, fax, website) — exact normalized board name.
- Alias table (`bulk_v2.py` ALIAS): official domains of well-known organisations (universities, colleges, crowns, utilities, police services, school divisions, Texas/Virginia institutions, EU agencies) — every such site was fetched by the crawler (status in `extras.website_check`).
- Website fields published in the notice's buyer contact block (e.g. PROMPERU, Peruvian/Chilean/EU notices).
- Checked and not usable: CivicInfo BC directory (https://www.civicinfo.bc.ca/directories → Cloudflare "Just a moment" challenge, 403; skipped), Alberta "Find a municipal official" (https://www.alberta.ca/find-a-municipal-official, interactive page behind reCAPTCHA; skipped), Ontario "List of Ontario municipalities" page (no website links). Saskatchewan / Nova Scotia / Newfoundland municipal directories were not reached in the time budget — Wikidata covered most of those municipalities.

Crawler (`crawl.py`, unchanged politeness: UA `contracts-research/1.0 (public-procurement dataset enrichment; polite crawler)`, robots.txt honoured, 0.7 s spacing per host ≈ 1.4 req/s, homepage + ≤ 13 same-site pages chosen by invoice/supplier/procurement/contact keywords); sitemap pass (`deep.py`) for high-priority sites still lacking an AP mailbox; PDF pass (`pdfpass.py`, now honouring robots.txt) over linked supplier/direct-deposit/invoice PDFs. Sites already crawled by the v1 run were reused from `enrichment/work_buyers/` instead of re-fetched (4 sites: http://www.rvo.nl, https://www.brabantwater.nl, https://danskespil.dk, https://www.dtu.dk). Run statistics (pass status: sites): crawl blocked_or_challenged: 46, crawl http_404: 10, crawl http_409: 1, crawl ok: 612, crawl partially_blocked: 8, crawl unreachable: 26, crawl_2 ok: 4, crawl_3 blocked_or_challenged: 2, crawl_3 ok: 25, crawl_3 unreachable: 3, crawl_4 ok: 3, crawl_5 blocked_or_challenged: 2, crawl_5 ok: 8, crawl_6 blocked_or_challenged: 1, crawl_6 ok: 36, crawl_6 partially_blocked: 1, crawl_6 unreachable: 5, crawl_wide ok: 110, deep no_sitemap: 29, deep ok: 121, deep2 no_sitemap: 41, deep2 ok: 119, pdf ok: 220; HTML/PDF pages fetched in v2: 6295.

Targeted research (WebSearch to locate candidate pages, then the page itself fetched with `probe.py` — robots.txt checked, bot-challenge/403 pages logged and skipped, raw copy under `downloads/enrichment_buyers_v2/pages/`, 115 fetches logged in `enrichment/work_buyers_v2/probe_log.jsonl`). `add_manual.py` refuses an e-mail unless it appears in the fetched copy of the cited URL. 52 curated findings in `enrichment/work_buyers_v2/manual_ap.jsonl`:
- `city_of_toronto` — https://www.toronto.ca/business-economy/doing-business-with-the-city/follow-up-on-city-contracts/accounts-payable-requirements/ (retrieved 2026-10-25T22:19:20Z): AP apinvoice@toronto.ca, directdeposit@toronto.ca; portal: SAP Business Network (SAP Ariba) for Ariba-enabled suppliers; procurement: supplychain@toronto.ca
- `gov_NL` — https://www.gov.nl.ca/exec/tbs/supplier-information/ (retrieved 2026-10-25T22:19:21Z): AP gnlinvoices@gov.nl.ca, cspayables@gov.nl.ca
- `gov_NT` — https://www.fin.gov.nt.ca/en/services/new-submitting-invoices (retrieved 2026-10-25T22:23:06Z): AP financial_sharedservices@gov.nt.ca
- `^(nwt health and social services authority|housing nwt|nwt housing corporation)$` — https://www.fin.gov.nt.ca/en/services/new-submitting-invoices (retrieved 2026-10-25T22:23:06Z): AP financial_sharedservices@gov.nt.ca
- `^nova scotia health authority$` — https://www.nshealth.ca/accounts-payable (retrieved 2026-10-25T22:23:08Z): AP financeaccountspayable.av@nshealth.ca
- `^york university$` — https://www.yorku.ca/procurement/?p=7854 (retrieved 2026-10-25T22:19:25Z): AP vendorinvoices@yorku.ca
- `^toronto metropolitan university$` — https://www.torontomu.ca/financial-services/purchasing-payment/vendor-guidance.html (retrieved 2026-10-25T22:19:30Z): AP poinvoices@torontomu.ca, invoices@torontomu.ca
- `^city of saskatoon$` — https://saskatoon.ca/business-development/doing-business-city/payment-and-purchasing-guidelines (retrieved 2026-10-25T22:23:10Z): AP —; procurement: purchasingadmin@saskatoon.ca
- `^toronto district school board$` — https://www.tdsb.on.ca/About-Us/Business-Services/Purchasing/Invoicing (retrieved 2026-10-25T22:19:24Z): AP —
- `city_of_ottawa` — https://documents.ottawa.ca/sites/default/files/Request%20for%20Vendor%20Payment%20by%20Direct%20Deposit%20%28EFT%29-AODA.pdf (retrieved 2026-10-25T22:24:43Z): AP vendormaster@ottawa.ca
- `^region of peel$` — https://peelregion.ca/finance/accounts-payable.asp (retrieved 2026-10-25T22:25:16Z): AP vendors@peelregion.ca
- `gov_ON` — https://ontario.ca/page/doing-business-government-ontario (retrieved 2026-10-25T22:26:40Z): AP opssc@ontario.ca; portal: Ontario Vendor Portal (self-registration; look up invoices, payments and purchase orders)
- `^metropolitan transportation authority$` — https://www.mta.info/doing-business-with-us/vendor-resources (retrieved 2026-10-25T22:26:43Z): AP invoice@mtabsc.org
- `gov_AB` — https://www.alberta.ca/1gx (retrieved 2026-10-25T22:26:47Z): AP —; portal: SAP Business Network (SAP Ariba) via 1GX, Government of Alberta
- `gov_MB` — https://gov.mb.ca/finance/direct.html (retrieved 2026-10-25T22:26:15Z): AP —
- `^city of mississauga$` — https://www.mississauga.ca/services-and-programs/business/doing-business-with-the-city/invoices-and-payments/ (retrieved 2026-10-25T22:31:36Z): AP cityofmississauga_invoicecapture@concursolutions.com, ap.central@mississauga.ca; procurement: purchasing@mississauga.ca
- `^city of edmonton$` — https://www.edmonton.ca/business_economy/selling_to_the_city/corporate-accounts-payable (retrieved 2026-10-25T22:31:38Z): AP apinquiries@edmonton.ca, vendormaintenance@edmonton.ca; portal: SAP Business Network (Ariba portal)
- `^city of brampton$` — https://brampton.ca/EN/residents/Roads-and-Traffic/Maintenance-Programs/Snow-Clearing-Operations/Documents/Accounts Payable Direct Deposit Form Vendor.pdf (retrieved 2026-10-25T22:32:22Z): AP accountspayable@brampton.ca
- `^metro vancouver$` — https://metrovancouver.org/filming/Documents/EFTTransferAuthorizationAgreement.pdf (retrieved 2026-10-25T22:32:24Z): AP accountspayable@metrovancouver.org
- `^university of toronto scarborough$` — https://utsc.utoronto.ca/financial/vendors (retrieved 2026-10-25T22:33:33Z): AP fsd.utsc@utoronto.ca
- `^york region$` — https://www.york.ca/business/information-suppliers (retrieved 2026-10-25T22:34:32Z): AP —
- `^city of red deer$` — https://reddeer.ca/city-government/accounts-payable-inquiries/ (retrieved 2026-10-25T22:35:02Z): AP accountspayable@reddeer.ca
- `^nlschools$` — https://www.nlschools.ca/business/includes/doc/NLSchoolsAccountsPayableInvoiceReq.pdf (retrieved 2026-10-25T22:35:21Z): AP accountspayable@nlschools.ca
- `^regional municipality of wood buffalo$` — https://www.rmwb.ca/programs-and-services/financial-services/accounts-payable/ (retrieved 2026-10-25T22:35:37Z): AP apinvoices@rmwb.ca, masterdata@rmwb.ca
- `^city of st albert$` — https://stalbert.ca/dev/purchasing/invoicing/ (retrieved 2026-10-25T22:35:52Z): AP accountspayable@stalbert.ca
- `^city of london$` — https://london.ca/postalstoppage (retrieved 2026-10-25T22:35:53Z): AP corporateaccountspayable@london.ca
- `^university of calgary$` — https://www.ucalgary.ca/finance/expenses-reimbursement/submit-invoice (retrieved 2026-10-25T22:36:29Z): AP invoices@ucalgary.ca, finance@ucalgary.ca
- `^city of leduc$` — https://www.leduc.ca/wp-content/uploads/2025/03/Leduc-Electronic-Payment-Request-Form.pdf (retrieved 2026-10-25T22:36:30Z): AP accountspayable@leduc.ca
- `^dalhousie university$` — https://www.dal.ca/dept/financial-services/contact-us/fs-department-contacts.html (retrieved 2026-10-25T22:36:31Z): AP apinvoice@dal.ca, finpay@dal.ca; procurement: procurement@dal.ca
- `^bruce power$` — https://www.brucepower.com/become-a-supplier/accounts-payable/ (retrieved 2026-10-25T22:37:02Z): AP bnpdacctspayableinquiriesonly@brucepower.com, bpariba@brucepower.com; portal: SAP Business Network (Ariba) – vendors send their ANID to BPAriba@brucepower.com
- `^greater toronto airports authority$` — https://author.torontopearson.com/-/media/project/pearson/content/corporate/suppliers/electronic-invoicing-requirements.pdf (retrieved 2026-10-25T22:37:04Z): AP ap@gtaa.com, accounts.payable@gtaa.com
- `^ontario tech university$` — https://shared.ontariotechu.ca/shared/department/finance/documents/vendor-eft-direct-deposit-form.pdf (retrieved 2026-10-25T22:37:57Z): AP uoitaccountspayable@uoit.ca
- `^halton district school board$` — https://www.hdsb.ca/our-board/departments/business-services/accounts-payable/ (retrieved 2026-10-25T22:38:21Z): AP ap@hdsb.ca
- `^norquest college$` — https://www.norquest.ca/getmedia/9634ee6a-03b6-4bc9-a0d2-eb99e18e358f/EFT-vendor-form.pdf (retrieved 2026-10-25T22:38:19Z): AP —; procurement: procurementandcontracts@norquest.ca
- `gov_NS` — https://www.novascotia.ca/get-started-supplier-government-step-step (retrieved 2026-10-25T22:39:11Z): AP —
- `state_ma` — https://massfinance.state.ma.us/VendorWeb/VendorInstruction.asp (retrieved 2026-10-25T22:39:12Z): AP —; portal: VendorWeb (Office of the Comptroller) — payment look-up for Commonwealth vendors
- `^mcmaster university$` — https://financial-affairs.mcmaster.ca/services/procurement/supplier-resources/ (retrieved 2026-10-25T22:40:44Z): AP appoinvo@mcmaster.ca
- `^liquor control board of ontario` — https://dev.doingbusinesswithlcbo.com/content/dbwl/en/basepage/home/new-supplier-agent/accounts-payable.html (retrieved 2026-10-25T22:41:02Z): AP accounts.payable@lcbo.com
- `^town of oakville$` — https://www.Oakville.Ca/getmedia/6f634b79-665f-4581-a119-a4f7de3ba632/business-purchasing-supplier-invoice-requirements.pdf (retrieved 2026-10-25T22:47:46Z): AP accountspayable@oakville.ca, ap_inquiries@oakville.ca; procurement: purchasing@oakville.ca
- `^city of kitchener$` — https://www.kitchener.ca/business-in-kitchener/procurement/vendor-invoices-and-payments/ (retrieved 2026-10-25T22:47:47Z): AP accountspayable@kitchener.ca
- `^carleton university$` — https://carleton.ca/financialservices/business-operations/accounts-payable/ (retrieved 2026-10-25T22:48:48Z): AP accounts.payable@carleton.ca
- `^mount royal university$` — https://www.mtroyal.ca/CampusServices/CampusResources/SupplyChainServices/Purchasing/MRU-Invoicing-Procedures_2022Jun08-1.pdf (retrieved 2026-10-25T22:48:50Z): AP accountspayable@mtroyal.ca; procurement: purchasing@mtroyal.ca
- `^university of guelph$` — https://www.uoguelph.ca/finance/departments-services/procurement-and-payables/payments-reimbursements (retrieved 2026-10-25T22:49:25Z): AP acctspay@uoguelph.ca
- `^southern alberta institute of technology$` — https://sait.ca/about-sait/contact-us/doing-business-with-sait (retrieved 2026-10-25T22:49:27Z): AP a.p.invoices@sait.ca; procurement: purchasing@sait.ca, vendor.admin@sait.ca
- `^university of lethbridge$` — https://ulethbridge.ca/node/36478 (retrieved 2026-10-25T22:49:55Z): AP finance.ap@uleth.ca
- `^lakehead university$` — https://www.lakeheadu.ca/faculty-and-staff/departments/services/finance/accounts-payable/ap-contact (retrieved 2026-10-25T22:49:57Z): AP acctspayable@lakeheadu.ca
- `^department of criminal justice$` — https://www.tdcj.texas.gov/divisions/bfd/acct_accts_pay.html (retrieved 2026-10-25T22:50:23Z): AP tdcj.ap.invsvs@tdcj.texas.gov
- `^town of vermilion$` — https://www.vermilion.ca/news/posts/in-the-event-of-a-canada-post-work-stoppage/ (retrieved 2026-10-25T22:51:15Z): AP arap@vermilion.ca
- `^town of greater napanee$` — https://www.greaternapanee.com/media/qbadu22f/fn-2026-02-accounts-payable-policy.pdf (retrieved 2026-10-25T22:51:16Z): AP accountspayable@greaternapanee.com
- `^haldimand county$` — https://www.haldimandcounty.ca/news/posts/canada-post-labour-disruption-impacts/ (retrieved 2026-10-25T22:51:50Z): AP aphelpdesk@haldimandcounty.on.ca
- `^city of richmond$` — https://richmond.ca/city-hall/news/2024/canadapoststrike2024.htm (retrieved 2026-10-25T22:57:44Z): AP treasury@richmond.ca
- `^city of maple ridge$` — https://www.mapleridge.ca/node/4248 (retrieved 2026-10-25T22:58:07Z): AP accounts.payable@mapleridge.ca

## Matching / e-mail rules
- Same e-mail rules as v1 (precision over recall): only addresses copied from the organisation's own pages/documents (or the notice's own contact field for procurement role boxes), each with page URL + retrieval time + snippet in `*.evidence`; personal-looking local parts dropped (first.last, initial+surname, name+digits without role word — e.g. the bids&tenders "purchasing representatives" and APC contact persons in the input are never copied); no address constructed from a pattern; a Cloudflare-obfuscated address (TDSB invoice box) was NOT decoded.
- v2 classifier fix: receivable/customer-billing boxes (water billing, utility billing, tax, AR tokens) are no longer classed as accounts payable (found in the first crawl results: waterbilling…@peelregion.ca, finance-ar@ornge.ca).
- Parent facts are attached to units: the City of Toronto AP requirements apply to all Toronto divisions; GNL's central gnlinvoices@gov.nl.ca applies to provincial departments only (the GNL page says it does not apply to NL Health Services or crown corporations — those keep their own facts); GNWT FESS mailbox applies to GNWT departments, Housing NWT and NTHSSA (stated on the GNWT page).

## Precision checks
- Directory/website matches (2026-10-25, by hand): 30 random buyers with an asserted website (Wikidata strong/weak, Ontario school-board CSV, alias table) checked against the crawled home-page title / known official domain: 30/30 point to the right organisation (3 sites answer with a JS redirect page but are the organisations' official domains). Wikidata/alias websites that did not load (404/unreachable, e.g. outdated Wikidata URLs such as county.middlesex.on.ca, edson.ca) are NOT asserted; they are kept in `extras.website_candidates`.
- AP mailboxes, first pass: a 36-sample of crawler + targeted AP e-mails contained 5 errors — 4 accounts-payable addresses of local businesses listed in municipal business directories (Crossfield, Crowsnest Pass, Penhold) and 1 ambiguous receivable/payable box on a customer-billing page. Fixes: crawler e-mails must be on the organisation's own domain (same registrable domain as its website or the page it was published on, a jurisdiction-consistent government domain, or a domain carrying a distinctive token of the organisation name), business-directory pages are ignored (699 third-party/directory addresses dropped), receivable/billing/tax/water boxes are never AP; a provincial government domain is accepted only for buyers of that province (a gov.bc.ca box published in a Saskatchewan notice was dropped).
- AP mailboxes, final output: 35 random AP e-mails re-checked after the fixes: 35/35 are the organisation's own supplier-payment role mailboxes; 31 are invoice-submission / accounts-payable boxes and 4 are vendor-master / EFT / vendor-assistance boxes (vendormaster@ottawa.ca, masterdata@rmwb.ca, ap.central@mississauga.ca for EFT, opssc@ontario.ca) — those are labelled as such in `notes` / `invoicing_requirements`.
- Parent-organisation rules: the list of buyers assigned to each provincial government was reviewed by hand; crown corporations, legislative offices, municipal bodies and associations that looked like departments (Halifax Water, Kinetic GPO, Innovacorp, NLC, Muskrat Falls, WorkplaceNL, House of Assembly, PHSA, BC Housing, WorkSafeBC, 3sHealth, Sask Gaming …) were excluded (NOT_DEPT list in classify.py) and get their own website/AP facts instead; a classifier bug (`\buniversit\b` never matching "university") that had put Dalhousie / U of Regina under their province was fixed.

## Top organisations (by high/medium contract records, parents joined)

| # | organisation | h/m records | website | AP |
|---|---|---|---|---|
| 1 | Government of Alberta | 2072 | yes | portal/instructions |
| 2 | Government of Ontario | 1818 | yes | e-mail |
| 3 | Government of Yukon | 656 | yes |  |
| 4 | Region of Peel | 576 | yes | e-mail |
| 5 | Infrastructure | 563 |  |  |
| 6 | York Region | 517 | yes | portal/instructions |
| 7 | Halifax Regional Municipality | 425 | yes |  |
| 8 | Region of Halton | 372 | yes | e-mail |
| 9 | City of Saskatoon | 370 | yes | portal/instructions |
| 10 | City of Medicine Hat | 318 | yes |  |
| 11 | Region of Durham | 298 | yes |  |
| 12 | City of Hamilton | 296 | yes | portal/instructions |
| 13 | City of Lethbridge | 284 | yes |  |
| 14 | City of Ottawa | 281 | yes | e-mail |
| 15 | City of Brampton | 277 | yes | e-mail |
| 16 | City of Mississauga | 259 | yes | e-mail |
| 17 | City of Grande Prairie | 231 | yes | portal/instructions |
| 18 | City of Barrie | 230 | yes |  |
| 19 | City of Red Deer | 220 | yes | e-mail |
| 20 | Metro Vancouver | 211 | yes | e-mail |
| 21 | City of Edmonton | 211 | yes | e-mail |
| 22 | City of Richmond Hill | 200 | yes | portal/instructions |
| 23 | City of Maple Ridge | 196 | yes | e-mail |
| 24 | Niagara Region | 188 | yes | portal/instructions |
| 25 | Newfoundland and Labrador Health Services | 184 | yes |  |
| 26 | Manitoba Hydro | 183 | yes | portal/instructions |
| 27 | City of St. Albert | 181 | yes | e-mail |
| 28 | Government of the Northwest Territories | 180 | yes | e-mail |
| 29 | City of Niagara Falls | 172 | yes | e-mail |
| 30 | Government of Newfoundland and Labrador | 164 | yes | e-mail |
| 31 | City of St. John's | 163 | yes | e-mail |
| 32 | Toronto District School Board | 160 | yes | portal/instructions |
| 33 | Northwest Territories Health and Social Services Authority | 157 | yes | e-mail |
| 34 | City of Vaughan | 153 | yes |  |
| 35 | EPCOR | 150 | yes |  |
| 36 | Edmonton Catholic Schools | 144 | yes |  |
| 37 | Rural Municipalities of Alberta | 135 | yes |  |
| 38 | City of Greater Sudbury | 135 | yes | e-mail |
| 39 | Town of Oakville | 128 | yes | e-mail |
| 40 | University of Toronto | 127 | yes | e-mail |
| 41 | Toronto and Region Conservation Authority | 125 | yes |  |
| 42 | City of Airdrie | 124 | yes | e-mail |
| 43 | City of London | 119 | yes | e-mail |
| 44 | Waterloo Region District School Board | 115 | yes |  |
| 45 | Town of Okotoks | 115 | yes |  |
| 46 | Dufferin-Peel Catholic District School Board | 114 | yes | portal/instructions |
| 47 | City of Richmond | 114 | yes | e-mail |
| 48 | City of Oshawa | 106 | yes |  |
| 49 | Finance | 104 |  |  |
| 50 | York University | 102 | yes | e-mail |
| 51 | City of Leduc | 100 | yes | e-mail |
| 52 | Canoe Procurement Group of Canada | 99 | yes |  |
| 53 | City of Brantford | 96 | yes | e-mail |
| 54 | City Of Peterborough | 92 | yes |  |
| 55 | Town of Newmarket | 89 | yes |  |
| 56 | York Catholic District School Board | 89 | yes |  |
| 57 | City of Nanaimo | 89 | yes | e-mail |
| 58 | Provincial Health Shared Services Supply Chain (NL Health Services) | 88 | yes |  |
| 59 | University of Calgary | 87 | yes | e-mail |
| 60 | Norfolk County | 87 | yes | portal/instructions |

## Known gaps / blockers
- Sites answering 403/503 or a bot challenge were skipped and never retried around the block (60 crawl sites): http://cityofelliotlake.com, http://www.brighton.ca, http://www.city.stratford.on.ca, http://www.county.pictou.ns.ca, http://www.dsbn.org, http://www.haldimandcounty.on.ca, http://www.hastingscounty.com, http://www.hopitalmontfort.com, http://www.jernbaneverket.no, http://www.kincardine.net, http://www.leedsandgrenville.ca, http://www.ponokacounty.com, http://www.pvnccdsb.on.ca, http://www.rainbowschools.ca, http://www.scdsb.edu.on.ca, http://www.swiftcurrent.ca, http://www.taber.ca, http://www.timmins.ca, http://www.town.windsor.ns.ca, http://www.townofmahonebay.ca, http://www.tyendinagatownship.com, https://brocku.ca, https://canoeprocurement.ca, https://carling.ca, https://civida.ca, https://dir.texas.gov, https://efficiencymb.ca, https://exploreedmonton.com, https://guelph.ca, https://humber.ca, https://islandstrust.bc.ca, https://kelowna.ca, https://library.novascotia.ca, https://moosejaw.ca, https://ottawa.ca/en, https://quintewest.ca, https://squamish.ca, https://um.fi, https://utilitieskingston.com, https://workplacenl.ca, https://www.burlington.ca, https://www.cssd.ab.ca, https://www.easthants.ca, https://www.enmax.com, https://www.indio.org, https://www.lacaja.com.pe, https://www.londonpubliclibrary.ca, https://www.mynslc.com, https://www.npolar.no, https://www.royalroads.ca, https://www.sanjoseca.gov, https://www.tamuct.edu, https://www.tennet.eu/nl/home, https://www.thorhildcounty.com, https://www.tps.ca, https://www.trs.texas.gov, https://www.ualberta.ca, https://www.uwinnipeg.ca, https://www.vaughan.ca, https://www.wbhadc.ca.
- Targeted pages that were blocked / disallowed (skipped): https://abbotsford.ca/node/10610, https://brocku.ca/vendors/accounts-payable/, https://cdn.halifax.ca/node/1298554, https://hamilton.ca/alert/canada-post-labour-disruption, https://humber.ca/purchasing/invoicing, https://ottawa.ca/en/business/doing-business-city/accounts-payable, https://saskatoon.ca/services-residents/connect-your-city/canada-post-service-disruption, https://www.mass.gov/how-to/mcb-payment-and-financial-information, https://yukon.ca/en/invoice-government, https://yukon.ca/node/24320.
- Provincial governments without a central supplier-invoice mailbox on their own pages: Government of Alberta (1GX / SAP Business Network only), Government of Ontario (invoice to the ministry client; OPS Service Centre for vendor assistance), Manitoba (paying department), BC, Nova Scotia and Saskatchewan (no central AP page found in the time budget — BC's invoice.pss.gov.bc.ca mailbox is for PSS customers' receivables and was not used). Yukon's invoice pages (yukon.ca/en/invoice-government, Departmental Accounts Payable contact list) answered 403 and were skipped.
- City of Ottawa's AP page (ottawa.ca) answered with a bot challenge; the Accounts Payable vendor-master mailbox from the City's EFT form (documents.ottawa.ca) is recorded instead.
- Multi-government buyer keys (`extras.jurisdiction_candidates`) are not resolved to one organisation by design.
- Non-North-American buyers (UNDP offices, EU institutions, Nordic/Dutch/Spanish/Latin American bodies) received websites from the notice/alias/Wikidata and crawler results only.
- Text excerpts in `invoicing_requirements` that start with "[page excerpt]" are raw page text around the first invoice mention; curated entries are written summaries of the cited page.
