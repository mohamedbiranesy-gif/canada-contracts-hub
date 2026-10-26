# Ongoing contracts with Canada-based vendors — dataset README

Reference date **2026-10-25**. Generated 2026-10-26 02:24 UTC.

Every contract found in published sources worldwide where (1) the **vendor is located in Canada** according to the source's own vendor country/address field (never guessed from the name), (2) the **buyer is a named organisation**, and (3) the contract is **ongoing on 2026-10-25** — or the source publishes the award without any end date (kept and flagged, never dropped).

## Files

| File | Contents |
|---|---|
| `canadian_vendor_contracts.jsonl.gz` | **511,762 records** with a verified Canada-located vendor. One JSON object per line: normalized fields + status/confidence + best link + vendor and buyer enrichment. The bulky verbatim source block (`raw`) is left out here — it is in `full/`. |
| `vendor_country_unverified_contracts.jsonl.gz` | **50,896 records** from sources that do not publish where the vendor is (Nova Scotia, City of Toronto, City of Ottawa, Ontario Vendor of Record, a few others). Probably mostly Canadian vendors, but not verified — kept separate. |
| `parties_not_identified_contracts.jsonl.gz` | **1,831 records** taken out of the two files above because one party is not identifiable in the source: CCC (Canadian Commercial Corporation) transactions whose foreign-government buyer is not disclosed (663), WHO contracts with the supplier's name withheld (547), placeholder vendor names such as "INDIVIDUAL CONSULTANT", "SEE SUPPLIER NOTES", "REDACTED", "Various" (World Bank, MERX, Nova Scotia, Toronto, bids&tenders and others), Mesa AZ rows with no vendor name. Each carries `parties_identifiable_reason`. The per-source `full/` files still contain them. |
| `full/<source>.jsonl.gz` | The same records per source **with `raw`**: every field the source publishes, verbatim — all identifiers, PO / contract / solicitation / reference / procurement numbers, amendment and transaction rows, codes, amounts, dates, addresses, contacts — plus the same enrichment blocks. |
| `vendors_enriched.jsonl.gz` | One line per vendor (119,131): every registry candidate with its full registry row, match confidence and evidence; Business Number and derived GST/HST account; names, addresses and identifiers seen across all contract sources. Join on `vendor_enrichment.vendor_key`. |
| `buyers_enriched.jsonl.gz` | One line per buyer (5,851): official website, accounts-payable / supplier-invoicing mailboxes with evidence URL, invoice portal, invoicing instructions, procurement and general contacts, identifiers, address. Join on `buyer_enrichment.buyer_key`. |
| `summary.json`, `merge_stats.json`, `enrichment_summary.json` | Counts by source, status, confidence, buyer country, value sums; enrichment coverage. |
| `source_notes.md` | The coverage note of every source checked — what was downloaded (URLs, times, row counts), how vendor country and status were decided, how links are built, known gaps — including sources checked and rejected. |

## How sure is "ongoing"? (`status` and `status_confidence`)

_The counts in this and the per-source tables were taken before the 1,831 records without identifiable parties were split out._

| status_confidence | meaning | verified-CA records |
|---|---|---|
| `high` | explicit published end date ≥ 2026-10-25 and start/award ≤ 2026-10-25 | 78,712 |
| `high_flagged_date` | as high, but the end date looks like a placeholder (e.g. 9999-12-31) | 129 |
| `medium` | end computed from a stated duration/term, framework or project period, or the parent award's period (arithmetic in `status_basis`) | 16,503 |
| `low` | Quebec SEAO convention: no closure record published, contract concluded 2023 or later | 80,423 |
| `very_low` | Quebec SEAO convention, contract concluded before 2023 — closure publication is incomplete and late, so many of these have ended | 224,726 |
| `unknown` | award/contract published, nothing about the end date | 112,650 |

For "definitely running" use `high` + `medium` (95,344 records). `status_basis` on every record states the exact fields and comparison used.

Buyer countries (verified-CA records): 127 distinct; top: CA 504,482, US 5,826, unknown 1,388, GB 253, DE 146, AU 109, FR 79, NL 62, RO 55, DK 52, UA 48, IE 42.

## Record layout (every line)

- `record_id`, `source` (key, name, publisher, dataset_url, record_url, retrieved_at), `source_file`
- `status`, `status_basis`, `status_confidence`, `status_confidence_basis`
- `link` + `link_type`: the record's own page when the portal has one, otherwise the closest notice/project page, otherwise the dataset page (then use the identifiers to find it)
- `contract`: identifiers (every id type the source has), title, description, instrument_type, procurement_method, solicitation_procedure, commodity codes (GSIN/UNSPSC/NAICS/PSC/CPV…), value, currency, value_detail, dates (published, signed, start, end, amended_last…), related (notice URLs, parent awards…)
- `buyer` and `vendor` as published (name, country, country_basis, identifiers, address, contact)
- `cross_source_matches`: other records that are probably the same contract in another source (same vendor and buyer plus same value, same dates or a shared identifier) — records are not merged
- `vendor_enrichment`: registry match level, legal name, status, federal corporation number, Quebec NEQ, BC registration number, **Business Number (BN9)** and its source, **derived GST/HST account (BN9+RT0001)**, registered address, incorporation/registration date, governing law, Quebec legal form / employee band / activity, the matches with evidence and source URL
- `buyer_enrichment`: canonical name, official website, identifiers, address, **`ap_contact`** (emails, invoice portal, invoicing requirements, instructions URL, evidence with page URL + retrieval time), procurement contact, general contact

## Enrichment: what it covers and how far to trust it

Coverage on the 513,143 verified-CA records: vendor matched to a business registry (exact/strong) 74%; vendor Business Number 24%; vendor website verified 23%; vendor contact (published in the contract data or on its own site) 24%; buyer official website 89%; buyer accounts-payable mailbox 24%; buyer invoice portal 1%.

Vendor table (119,131 vendors): registry match exact 51,486, strong 6,816; Business Number 13,548; website looked up 45,682, verified website 8,958, published role mailbox 4,420.

**Vendors.** Matched by normalised legal name, using the vendor's city, postal code (or 3-character postal prefix) and province to tell same-named companies apart; NEQs already published in Quebec contract data were matched directly. Registries: Corporations Canada federal corporations open data (corporation number, Business Number, status, registered office; 2026-10-25 extract), Registraire des entreprises du Québec open data (NEQ, legal form, status, names history, domicile address, establishments, activity, employee band; 2026-10-15 extract), BC OrgBook public API (registration number, Business Number, status) for every vendor with a BC address, and for vendors elsewhere still lacking a Business Number, OrgBook's extraprovincial registrations (companies from other provinces registered to do business in BC) — a match counts only when the registration's home jurisdiction equals the vendor's province (this lookup is slow and was still running at assembly time; `vendors_enriched.jsonl.gz` shows which vendors were queried). One-word vendor names are never matched with more than `weak` confidence. Hand check of random samples: federal 30/30 correct; Quebec 25/30 before tightening — name-only matches without any city/postal agreement were then downgraded to `weak` (kept as candidates, never used for identifiers). Most Canadian companies are provincially incorporated outside Quebec/BC (e.g. Ontario, Alberta) and those registries publish no bulk data, which is why many vendors have no Business Number.

**Vendor websites and contacts.** Few sources publish vendor websites, so candidate domains were derived from each vendor's distinctive name words (.ca/.com) and a site was accepted only when its pages show the company name and a location from the contract data or registry (postal code, city or province); robots.txt was honoured. Sites reached only through a redirect to another domain (often a parent or brand) are marked `verified_via_redirect`. From the verified site's homepage and contact pages, organisational role mailboxes on the site's own domain (info@, sales@, accounting@, billing@ …) and main phone numbers were recorded with the page URL; personal-looking addresses were dropped, and protected/obfuscated emails and bot-checked pages were skipped. Vendors were processed in order of contract count; `website_lookup_status` tells whether a vendor was reached before assembly. Contacts that the contract sources themselves publish (e.g. supplier contact e-mail and phone in CanadaBuys or bids&tenders) are in `vendor.contact`.

**GST/HST.** No public source lists GST/HST numbers by company. `gst_hst_account_derived` = BN9 + `RT0001` is the usual first GST/HST account of a registered business, but it is **derived, not published**, and exists only if the business is registered. The CRA GST/HST Registry, which confirms a number, sits behind a CAPTCHA, so nothing was confirmed automatically — confirm there before relying on one.

**Buyers / AP emails.** Only role mailboxes that the organisation itself publishes for suppliers (invoicing, accounts payable, procurement), each copied from a page whose URL and retrieval time are recorded; personal mailboxes were excluded and no address was ever constructed from a pattern. Some federal entries come from PSPC's table of departmental supplier-payment contacts — these handle payment/direct-deposit questions and are labelled as such; contract-specific invoicing instructions in the contract itself take precedence. Divisions inherit their parent organisation's invoicing contact (e.g. City of Toronto divisions, provincial ministries). Hand checks: websites 30/30, AP mailboxes 35/35 in the final samples. About 260 buyer websites refused automated access (403/bot checks) and were skipped.

## Records by source

| source | bucket | records | high | medium | low+very low | unknown |
|---|---|---|---|---|---|---|
| seao_quebec | verified CA | 331,410 | 26,261 | 0 | 305,149 | 0 |
| ca_bidsandtenders | verified CA | 69,975 | 0 | 14,845 | 0 | 55,130 |
| canada_federal | verified CA | 42,193 | 39,862 | 0 | 0 | 2,331 |
| ca_saskatchewan | verified CA | 18,776 | 0 | 0 | 0 | 18,776 |
| ca_bc_ministry_awards | verified CA | 12,871 | 0 | 0 | 0 | 12,871 |
| ca_merx | verified CA | 12,863 | 3,054 | 0 | 0 | 9,809 |
| ca_alberta_apc | verified CA | 6,484 | 5,617 | 0 | 0 | 867 |
| ca_biddingo | verified CA | 4,522 | 14 | 114 | 0 | 4,394 |
| ca_newfoundland | verified CA | 4,500 | 3 | 314 | 0 | 4,183 |
| usaspending | verified CA | 2,715 | 1,809 | 899 | 0 | 7 |
| ca_alberta_sole_source | verified CA | 949 | 949 | 0 | 0 | 0 |
| who | verified CA | 816 | 0 | 0 | 0 | 816 |
| ca_nwt | verified CA | 797 | 795 | 0 | 0 | 2 |
| us_state_virginia | verified CA | 709 | 0 | 0 | 0 | 709 |
| ccc_canada | verified CA | 663 | 0 | 0 | 0 | 663 |
| ted_eu | verified CA | 584 | 28 | 103 | 0 | 453 |
| us_state_vermont | verified CA | 355 | 0 | 0 | 0 | 355 |
| worldbank | verified CA | 310 | 0 | 112 | 0 | 198 |
| ungm | verified CA | 287 | 0 | 0 | 0 | 287 |
| private_press | verified CA | 216 | 27 | 58 | 0 | 131 |
| uk_find_a_tender | verified CA | 136 | 63 | 19 | 0 | 54 |
| austender | verified CA | 97 | 97 | 0 | 0 | 0 |
| us_state_ny_abo | verified CA | 74 | 44 | 0 | 0 | 30 |
| us_state_oregon | verified CA | 74 | 12 | 0 | 0 | 62 |
| uk_contracts_finder | verified CA | 63 | 63 | 0 | 0 | 0 |
| us_state_texas_lbb | verified CA | 62 | 51 | 0 | 0 | 11 |
| us_city_la | verified CA | 58 | 0 | 0 | 0 | 58 |
| us_state_massachusetts | verified CA | 58 | 0 | 0 | 0 | 58 |
| us_city_mesa_az | verified CA | 56 | 0 | 0 | 0 | 56 |
| us_ny_mta | verified CA | 52 | 45 | 0 | 0 | 7 |
| undp | verified CA | 51 | 0 | 0 | 0 | 51 |
| de_bmi_oeffentlichevergabe | verified CA | 32 | 6 | 3 | 0 | 23 |
| sec_edgar | verified CA | 28 | 6 | 16 | 0 | 6 |
| nl_tenderned | verified CA | 27 | 2 | 4 | 0 | 21 |
| no_opentender | verified CA | 22 | 0 | 0 | 0 | 22 |
| cl_mercado_publico | verified CA | 17 | 0 | 0 | 0 | 17 |
| us_state_alaska | verified CA | 17 | 0 | 0 | 0 | 17 |
| us_county_montgomery_md_spending | verified CA | 16 | 1 | 0 | 0 | 15 |
| fao | verified CA | 12 | 0 | 1 | 0 | 11 |
| es_placsp | verified CA | 11 | 4 | 7 | 0 | 0 |
| other_igo | verified CA | 11 | 5 | 5 | 0 | 1 |
| pe_oece | verified CA | 11 | 5 | 0 | 0 | 6 |
| eu_institutions_opentender | verified CA | 10 | 0 | 0 | 0 | 10 |
| si_mju | verified CA | 10 | 0 | 0 | 0 | 10 |
| us_city_baton_rouge | verified CA | 10 | 0 | 0 | 0 | 10 |
| us_city_corona_ca | verified CA | 10 | 0 | 0 | 0 | 10 |
| us_county_miami_dade | verified CA | 10 | 0 | 0 | 0 | 10 |
| dk_opentender | verified CA | 9 | 0 | 0 | 0 | 9 |
| us_city_austin | verified CA | 9 | 0 | 0 | 0 | 9 |
| ch_opentender | verified CA | 8 | 0 | 0 | 0 | 8 |
| se_opentender | verified CA | 8 | 0 | 0 | 0 | 8 |
| cdb | verified CA | 7 | 0 | 2 | 0 | 5 |
| us_county_fulton_ga | verified CA | 7 | 0 | 0 | 0 | 7 |
| hr_eojn | verified CA | 6 | 0 | 0 | 0 | 6 |
| us_city_mesquite_tx | verified CA | 6 | 0 | 0 | 0 | 6 |
| us_city_providence | verified CA | 6 | 0 | 0 | 0 | 6 |
| tw_pcc | verified CA | 5 | 5 | 0 | 0 | 0 |
| au_wa | verified CA | 4 | 4 | 0 | 0 | 0 |
| fi_opentender | verified CA | 4 | 0 | 0 | 0 | 4 |
| nz_gets | verified CA | 4 | 0 | 0 | 0 | 4 |
| us_city_indio_ca | verified CA | 4 | 0 | 0 | 0 | 4 |
| us_state_delaware | verified CA | 4 | 4 | 0 | 0 | 0 |
| rw_umucyo | verified CA | 3 | 0 | 0 | 0 | 3 |
| us_city_richmond_ca | verified CA | 3 | 0 | 0 | 0 | 3 |
| us_county_montgomery_md | verified CA | 3 | 3 | 0 | 0 | 0 |
| ch_simap | verified CA | 2 | 0 | 0 | 0 | 2 |
| is_opentender | verified CA | 2 | 0 | 0 | 0 | 2 |
| us_city_nyc | verified CA | 2 | 0 | 1 | 0 | 1 |
| us_state_oklahoma | verified CA | 2 | 0 | 0 | 0 | 2 |
| co_secop | verified CA | 1 | 0 | 0 | 0 | 1 |
| ec_sercop | verified CA | 1 | 1 | 0 | 0 | 0 |
| py_dncp | verified CA | 1 | 0 | 0 | 0 | 1 |
| us_state_texas_dir | verified CA | 1 | 1 | 0 | 0 | 0 |
| zm_zppa | verified CA | 1 | 0 | 0 | 0 | 1 |
| ca_nova_scotia_unverified_country | vendor location not published | 33,257 | 0 | 1 | 0 | 33,256 |
| ca_city_toronto_unverified_country | vendor location not published | 10,728 | 2 | 46 | 0 | 10,680 |
| ca_city_ottawa_unverified_country | vendor location not published | 5,220 | 0 | 240 | 0 | 4,980 |
| ca_ontario_vor_unverified_country | vendor location not published | 1,818 | 1,818 | 0 | 0 | 0 |
| ca_merx_unverified_country | vendor location not published | 260 | 19 | 0 | 0 | 241 |
| ca_biddingo_unverified_country | vendor location not published | 35 | 0 | 2 | 0 | 33 |
| ca_city_edmonton_unverified_country | vendor location not published | 16 | 16 | 0 | 0 | 0 |
| ca_bidsandtenders_unverified_country | vendor location not published | 12 | 0 | 0 | 0 | 12 |

Sources checked that produced no records (no supplier location, no award data, blocked, or nothing ongoing) — details in `source_notes.md`: adb — Asian Development Bank contract awards — BLOCKED / not reachable; afdb — African Development Bank contract awards — BLOCKED; al_ppc — Albania – Public Procurement Commission (PPC) OCDS; ar_caba — Argentina – Ciudad de Buenos Aires (DGCyC) OCDS (2022); ar_mendoza — Argentina – Mendoza province COMPR.AR OCDS; au_act — ACT Government contracts register — REJECTED/BLOCKED; au_nsw — Australia – New South Wales eTendering (NSW Treasury) OCDS; au_nt — Northern Territory Quotations and Tenders Online — NOT CRAWLED (no bulk export); au_qld — Queensland Government contract disclosure reports (data.qld.gov.au) — BLOCKED; au_sa — South Australia — REJECTED (no open contract-award dataset); au_vic — Victoria (Buying for Victoria / tenders.vic.gov.au) contracts — BLOCKED; bo_agetic — Bolivia – AGETIC procurement OCDS (2019–2020); br_compras_gov — Brazil – Compras.gov.br (federal) OCDS; ca_bc_bid — BC Bid portal (REJECTED: reCAPTCHA browser check) — see ca_bc_ministry_awards for the usable BC source; ca_bonfire — Bonfire (GTY/Euna) public portals of Canadian public bodies (REJECTED: Cloudflare challenge on award pages); ca_city_brampton — City of Brampton open data (REJECTED: no contract-award dataset); ca_city_calgary — City of Calgary open data (REJECTED: no contract-award dataset); ca_city_halifax — Halifax Regional Municipality open data (REJECTED: no contract-award dataset); ca_city_hamilton — City of Hamilton open data (REJECTED: no contract-award dataset); ca_city_london — City of London (ON) open data (REJECTED: no contract-award dataset); ca_city_mississauga — City of Mississauga open data (REJECTED: no contract-award dataset); ca_city_vancouver — City of Vancouver open data (NOT CHECKED: connection reset); ca_city_waterloo — City/Region of Waterloo open data (REJECTED: no contract-award dataset); ca_city_winnipeg — City of Winnipeg open data (REJECTED: no awardee published); ca_crown_corps — Provincial Crown corporations checked for their own award disclosures (REJECTED / covered elsewhere); ca_manitoba — Manitoba (data.gov.mb.ca blocked; MERX handled by another worker); ca_new_brunswick — New Brunswick (BLOCKED: hosts not reachable through the session proxy); ca_nunavut — Government of Nunavut (REJECTED: no supplier identity/address accessible); ca_ontario_otp — Ontario Tenders Portal / Supply Ontario / data.ontario.ca (REJECTED); ca_pei — Prince Edward Island (BLOCKED: 403); ca_yukon — Yukon Government Public Contract Registry (BLOCKED: Cloudflare JS challenge); co_cce — Colombia – Colombia Compra Eficiente (SECOP I/II) OCDS; commonwealth — Commonwealth Secretariat contracts awarded — REJECTED (no supplier country); cr_poder_judicial — Costa Rica – Poder Judicial procurement OCDS; do_dgcp — Dominican Republic – DGCP OCDS; eib — European Investment Bank procurement awards — REJECTED (covered by TED); es_zaragoza — Spain – Ayuntamiento de Zaragoza OCDS; esa — European Space Agency contracts awarded — REJECTED (no reachable award data); fr_dinum — France – DECP données essentielles (DINUM) OCDS; ge_spa — Georgia – State Procurement Agency (SPA) OCDS (2010–2019); gh_ppa — Ghana – PPA OCDS; gr_diavgis — Greece – Diavgeia (Diavgis) OCDS; gt_guatecompras — Guatemala – Guatecompras OCDS; hn_oncae — Honduras – ONCAE HonduCompras OCDS; hn_sefin — Honduras – SEFIN (SIAFI) OCDS; icao — ICAO procurement / contracts awarded — BLOCKED; igo_portals — international organisations' own award portals: index of what was checked; ireland_etenders — Ireland eTenders / OGP open data (SKIPPED: no supplier-country field); it_anac — Italy – ANAC BDNCP OCDS; it_mit — Italy – Ministry of Infrastructure and Transport OCDS (2022–2024); ke_makueni — Kenya – Makueni County OCDS (2021–2022); ke_ppip — Kenya – PPIP OCDS; lr_ppcc — Liberia – PPCC OCDS; md_mtender — Moldova – MTender (Ministry of Finance) OCDS; mx_compranet — Mexico federal CompraNet / ComprasMX contracts — NOT REACHABLE; mx_inai — Mexico – INAI (federal transparency institute) contracting OCDS; mx_nuevo_leon — Mexico – Nuevo León state OCDS; nato_ncia — NATO Communications and Information Agency procurement — BLOCKED; nato_nspa — NATO Support and Procurement Agency contract awards — BLOCKED; ng_bpp — Nigeria – BPP NOCOPO OCDS; no_doffin — Norway Doffin — REJECTED (API key required); partial coverage via OpenTender; ocp_registry — shared pipeline note (not a source); pa_dgcp — Panama – DGCP PanamaCompra OCDS; pe_perucompras — Peru – Central de Compras Públicas Perú Compras OCDS (2021–2023); pt_base — Portugal BASE (Portal dos Contratos Públicos) — REJECTED; sedar_plus — SEDAR+ (Canadian Securities Administrators filings portal) — REJECTED (bot check); sg_gebiz — Singapore Government Procurement via GeBIZ (data.gov.sg) — REJECTED; tz_nest — Tanzania – NeST OCDS; ua_prozorro — Ukraine Prozorro — NOT FEASIBLE in time box; ug_ppda — Uganda – PPDA GPP OCDS; un_secretariat — UN Secretariat Procurement Division contract awards — BLOCKED; unicef — UNICEF Supply Division contract awards — REJECTED (no supplier country); unops — UNOPS own award data — covered via UNGM; own portal not usable; us_city_boston — City of Boston "Contract Award" open data (data.boston.gov): checked, rejected; us_city_chicago — City of Chicago Contracts (data.cityofchicago.org rsxa-ify5): checked, pulled in full, 0 ongoing Canadian-vendor contracts; us_city_denver — City and County of Denver Checkbook (data.colorado.gov wnau-xrqi): checked, rejected; us_city_detroit — City of Detroit "OCP Procurement Agreements" (ArcGIS): checked, 0 Canadian-vendor records; us_city_houston — City of Houston (data.houstontx.gov CKAN): checked, rejected; us_city_las_vegas — City of Las Vegas checkbook with vendor addresses (ArcGIS): checked, 0 records; us_city_philadelphia — Philadelphia contracts (contracts.phila.gov, OpenDataPhilly): checked, rejected; us_city_phoenix — City of Phoenix (phoenixopendata.com CKAN): checked, rejected; us_city_sf — San Francisco "Supplier Contracts" (data.sf.gov cqi5-hm2d): checked, rejected; us_city_urbana_il — City of Urbana, IL "Open Expenditures - Payment Details" (illinois-edp.data.socrata.com p34w-i7rn): checked, 0 records; us_county_cook_il — Cook County (IL) "Procurement - Awarded Contracts & Amendments" (datacatalog.cookcountyil.gov qh8j-6k63): checked, rejected; us_county_king_wa — King County (WA) "Procurement Contracts" (data.kingcounty.gov dqit-zt74): checked, rejected; us_dc — District of Columbia contracts: checked, 0 Canadian-vendor records; us_misc_portals_checked — smaller US local portals checked on resume (2026-10-25, ≈19:28–19:55 UTC) and rejected; us_ny_nyserda — NYSERDA "Supported Clean Energy Research and Development Projects: Beginning 1991" (data.ny.gov 7xzk-zyk5): checked, 0 records; us_state_arizona — Arizona (APP/ProcureAZ app.az.gov, OpenBooks openbooks.az.gov): checked, blocked; us_state_california — California (data.ca.gov / Cal eProcure): checked, rejected; us_state_colorado — Colorado (data.colorado.gov / Transparency Online / COMPASS): checked, rejected; us_state_connecticut — Connecticut (data.ct.gov Open Checkbook / Open Expenditures): checked, rejected; us_state_florida — Florida FACTS (facts.fldfs.com) / MyFloridaMarketPlace: checked, rejected; us_state_georgia — Georgia Procurement Registry (ssl.doas.state.ga.us/gpr): checked, blocked; us_state_hawaii — Hawaii HIePRO (hiepro.ehawaii.gov): checked, blocked; us_state_illinois — Illinois Comptroller contracts / data.illinois.gov: checked, rejected; us_state_indiana — Indiana IDOA Public Contract Search (secure.in.gov/apps/idoa/contractsearch): checked, rejected; us_state_kentucky — Kentucky Transparency (transparency.ky.gov) contract search: checked, rejected; us_state_maine — Maine Office of the State Controller "Vendor Data File" / Open Checkbook: blocked; us_state_maryland — Maryland eMMA / opendata.maryland.gov: checked, rejected (county-level source used instead); us_state_michigan — Michigan SIGMA / Contract Connect / data.michigan.gov: checked, rejected; us_state_minnesota — Minnesota contract search: checked, rejected; us_state_missouri — MissouriBUYS (missouribuys.mo.gov): checked, rejected; us_state_nevada — Nevada (nevadaepro.com / data.nevada.gov): checked, rejected; us_state_new_jersey — New Jersey (NJSTART / YourMoney NJ): checked, rejected; us_state_north_carolina — NC eProcurement / IPS (ips.state.nc.us): checked, blocked; us_state_ny_osc_openbook — NYS Office of the State Comptroller Open Book New York contract search (wwe2.osc.state.ny.us/transparency/contracts): checked, rejected; us_state_ohio — Ohio (OhioCheckbook checkbook.ohio.gov, OhioBuys): checked, blocked; us_state_pennsylvania — Pennsylvania (data.pa.gov, PA Treasury e-Library, eMarketplace): checked, rejected; us_state_tennessee — Tennessee CPO statewide contracts (tn.gov): checked, blocked; us_state_utah — Utah Transparency (transparent.utah.gov): checked, rejected; us_state_washington — Washington State (data.wa.gov Agency Contracts FY2014–FY2025; fiscal.wa.gov): checked, rejected; us_state_wisconsin — Wisconsin VendorNet/WisBuy (wwwcfprd.doa.state.wi.us): checked, blocked; us_transit_agencies — CTA, WMATA, LA Metro, SEPTA procurement pages: checked, rejected; us_universities — UC, CSU, SUNY, Texas A&M system procurement: checked, rejected; uy_arce — Uruguay – ARCE (Agencia Reguladora de Compras Estatales) OCDS API; wfp — World Food Programme contract awards — REJECTED (no public award list); xk_pprc — Kosovo – PPRC e-procurement OCDS; za_etenders — South Africa – eTenders OCDS.

## Known limits

- **Private-sector contracts** are only those publicly announced (press releases, SEC filings): a few hundred, a sample rather than a census. Most business-to-business contracts are never published.
- **Blocked or unavailable** (not bypassed): SEDAR+ (bot check), BC Bid contract awards tab (reCAPTCHA; BC's open-data ministry awards were used instead), Yukon contract registry and Nunavut (Cloudflare), PEI (403), New Brunswick NBON and Manitoba open data (not reachable from this environment), New Zealand MBIE GETS files (bot check), Ontario Tenders Portal awards (no public award listing), CRA GST/HST Registry (CAPTCHA).
- **Quebec SEAO `low`/`very_low` records** rest only on the absence of a published closure record; treat them as candidates.
- **Values** are as published — often ceilings, framework maxima or IDV ceilings, not spend. Don't sum across records without care.
- **Duplicates across sources** (e.g. UK Contracts Finder vs Find a Tender, federal proactive disclosure vs CanadaBuys) are flagged in `cross_source_matches`, not merged.
- **"Located in Canada"** follows the address in the contract: Canadian subsidiaries of foreign groups count; foreign subsidiaries of Canadian firms don't.
- bids&tenders and MERX award pages were crawled newest first; very old awards (mostly finished) may not all be included — see their notes.

