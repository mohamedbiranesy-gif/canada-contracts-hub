#!/usr/bin/env python3
"""Write docs/HANDOFF_ROWS.md from HANDOFF_TEMPLATE.md and the corrected table: every number in it is counted on the table.

  python3 contrib/claude/final_correction/handoff.py OUTDIR [docs/HANDOFF_ROWS.md]
OUTDIR holds ranked_buyers.csv.gz (corrected, sorted, folded), counts.json (correct_table.py), and the logs of priority_sort / fold if saved.
"""
import collections, csv, datetime, gzip, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import relationship_rows as RR  # noqa: E402

csv.field_size_limit(1 << 30)

DESC = {
    "jurisdiction": "the buyer's jurisdiction code (CA, a province, US, a US state, UK, EU …) as the source or the ranker set it",
    "rank_group": "the ranker's group: tier letter + mailbox grade (GOLD = tier A/B with an invoicing/AP mailbox, confirmed); decides the package",
    "completeness_score": "the ranker's sort score inside a tier (tier strength × 10 + mailbox grade × 6 + 3 if confirmed)",
    "data_quality_score": "0–100: mailbox quality + relationship tier + share of key fields filled",
    "ship_ready": "the owner's test: yes · yes (what is by kind / by location / calculated / not published) · no",
    "ship_ready_missing": "every reason a row is not ready (or, for a ready row, empty)",
    "amount_mark": "1 published $5,000+ · 2 estimated $5,000+ · 3 published under $5,000 · 4 estimated under · 5 no amount — with the figure it rests on",
    "payment_route": "how the bill is paid: on invoice, by bank transfer / cheque (in the biller's words, or by the kind of relationship); either; card; registrar …",
    "payment_route_basis": "the sentence that decides the route (the biller's own, quoted, or the kind's statement)",
    "invoice_fields_for_kind": "the kind of relationship and the fields an invoice of that kind carries",
    "invoice_fields_missing_for_kind": "the fields of the kind that nothing published fills (named, not hidden)",
    "vendor_tax_or_registration_number": "the vendor's number for the invoice: BN / GST-HST (derived) or its home register's number, labelled",
    "ap_mailbox_ready": "the old label of the mailbox test, kept under its own name",
    "buyer": "the organisation billed, by its own name (its domain name when the only name found was not a name)",
    "buyer_website": "the organisation's own website",
    "buyer_address": "its printed address (its own page, a register, a directory, or the place listing for its site), with where it was read",
    "buyer_phone": "its published telephone",
    "buyer_contact_evidence_url": "the page the buyer's contact facts were read on",
    "buyer_legal_name_as_published": "its legal name as a register, the CRA charities list, a disclosure or its own page prints it (with the source)",
    "buyer_bn_as_published": "its Business Number as published (with the source)",
    "buyer_bn_program": "the BN program account, when published",
    "buyer_trade_name_as_published": "its trade or other names as published",
    "buyer_gst_hst_derived": "BN9 + RT0001 — derived, labelled; never looked up in the CRA registry",
    "buyer_logo_url": "its logo as its site serves it",
    "buyer_website_status": "whether the site answered, and from where the site came",
    "buyer_linkedin_url": "its LinkedIn page, when linked from its site",
    "buyer_supplier_portals_linked": "supplier or bid portals its site links to",
    "buyer_registry_id": "its register entry (NEQ, corporation number …)",
    "buyer_bn_note": "a conflict between two sources' BN, said",
    "buyer_type": "the kind of organisation (municipality, school board, hospital, university, company, non-profit …) from its name and jurisdiction",
    "sensitivity_tag": "a tag for sensitive buyers (health, shelters, police …), with the reason",
    "sensitivity_flag": "yes when the buyer is sensitive (the row is held: a flag takes it out of the ready set)",
    "buyer_sector": "its sector as published or derived",
    "peppol_participant_id": "its Peppol e-invoicing participant id, when registered",
    "peppol_registered": "whether it is in the Peppol directory",
    "statutory_payees_inferred": "bodies an organisation of that type pays by law (CRA, provincial bodies) — inferred, no mailbox, not a supplier relationship",
    "buyer_municipal_tier": "a municipality's tier (lower, upper, MRC …) from the provincial directory",
    "buyer_population": "a municipality's population from the provincial directory or the census",
    "directory_general_email": "the general mailbox a provincial directory lists (not the delivered mailbox)",
    "municipal_directory_source": "the provincial municipal directory used",
    "buyer_fiscal_year_end": "its fiscal year end, when published",
    "buyer_charity_status": "its CRA registered-charity status",
    "buyer_charity_designation": "its CRA designation (charitable organisation, public / private foundation)",
    "buyer_wikidata": "its Wikidata item",
    "buyer_founded": "its founding year, when published",
    "buyer_budget_or_revenue": "its budget or revenue, when published",
    "buyer_employees": "its employees, when published",
    "buyer_legal_form": "its legal form, when published",
    "buyer_facts_provenance": "where each buyer fact on the row was read",
    "email": "the organisation's own role mailbox (re-read by the referee)",
    "email_type": "its role: invoicing/AP · finance/accounting dept or supplier-payment office · purchasing · general",
    "email_check": "how it was confirmed: confirmed (the referee re-fetched the page) · cross_verified (two lanes) · pending",
    "mailbox_confidence": "the confirmation, in words, with its date",
    "evidence_age_days": "days since the mailbox's page was read",
    "reverify_due": "yes when the evidence is older than 60 days",
    "email_evidence_url": "the page that prints the mailbox",
    "email_evidence_quote": "≤ 300 characters of that page containing the mailbox",
    "email_evidence_context": "what else the page says around it (the role, the department)",
    "mailbox_recheck_note": "a later re-read of the mailbox, when one was made",
    "mailbox_provenance": "who found the mailbox and how (crawler, lane, page)",
    "email_deliverability": "whether the mail domain publishes a mail server (MX), DNS only",
    "email_security_posture": "the mail domain's DMARC / SPF posture in words",
    "dmarc_policy": "DMARC policy (none / quarantine / reject / no record)",
    "dmarc_record": "the DMARC record as published",
    "dmarc_record_domain": "the domain the DMARC record was read on",
    "spf_policy": "the SPF policy",
    "spf_record": "the SPF record as published",
    "mail_provider": "the mail provider by the MX hosts (Microsoft 365, Google, ISP mail …)",
    "dns_checked_date": "when the DNS was read",
    "mta_sts": "MTA-STS policy, when published", "tls_rpt": "TLS-RPT record, when published", "bimi": "BIMI record, when published",
    "ap_contact_name_as_published": "an AP contact's title or name as the organisation prints it on the same page (role first)",
    "ap_phone": "the AP telephone as printed on the mailbox's page",
    "invoice_mailing_address": "where invoices go by post, as printed",
    "invoicing_requirements": "what the organisation asks invoices to carry (PO, format, address …), quoted",
    "payment_terms_as_published": "the buyer's own payment terms, quoted (net 30 …)",
    "payment_terms_default_policy": "a jurisdiction's prompt-payment law or policy when the buyer publishes none (labelled)",
    "po_required_as_published": "whether invoices must carry a PO, as published",
    "invoice_portal_url": "the buyer's invoice or supplier portal",
    "invoice_portal_kind": "what that portal is (e-invoicing, supplier registration, tender portal …)",
    "invoice_portal_note": "a note on the portal",
    "ap_system_hint": "the AP / e-invoicing system the portal reveals (SAP Ariba, Coupa, Jaggaer …)",
    "invoicing_requirements_structured": "the requirements as structured data",
    "buyer_payment_method_preference": "how the buyer pays its suppliers, as published (EFT, cheque …)",
    "buyer_ap_cycle_published": "its payment run, as published",
    "buyer_tax_exempt_status": "a published tax exemption",
    "buyer_tax_status_derived": "DERIVED: what tax an invoice to it carries (the place-of-supply rule, the public-service-body rebate, exports zero-rated …)",
    "tax_rate_indicative_derived": "the GST/HST/QST rate of its province, derived",
    "invoice_currency_derived": "the invoice currency, derived from the buyer's country when no record states one",
    "buyer_esignature_preference": "a published e-signature preference",
    "pay_on_sight": "yes / routed / no: could an invoice made from the row clear AP matching on sight",
    "pay_on_sight_missing": "what it lacks",
    "channel_tier": "1 invoicing/AP mailbox or invoice portal · 2 finance · 3 purchasing/general · 0 unconfirmed",
    "invoice_text": "the draft invoice header (section 7)",
    "invoice_card_json": "the same as structured data (section 7)",
    "invoice_readiness": "n/14 invoice elements present",
    "invoice_missing": "the invoice elements missing",
    "ap_grade": "A–E: how complete and how confirmed the AP data is",
    "ap_score": "0–100 behind the grade",
    "ap_grade_basis": "the criteria met and missing",
    "ap_gap_to_A": "what grade A would need",
    "ap_payability": "payable today or what is missing (channel, bill-to, reference rule, tax)",
    "supplier_setup_url": "the buyer's supplier set-up form or page",
    "language_hint": "the language of the mailbox's page",
    "template_language": "the invoice's language (French first for Québec buyers)",
    "contract_status": "why the relationship is current, in words (the record's dates, the register's state, the service seen …)",
    "inference_confidence": "for a row by location: how certain the distributor is; n/a for a record",
    "relationship_kind": "the kind of relationship, in words",
    "relationship_detail": "the relationship in one paragraph: dates, value, billing period, the buyer's other Canadian vendors",
    "how_relationship_was_found": "the tool and the source that found it",
    "relationship_fact_basis": "why it is a fact (fact, public record · fact, the biller's own roster · fact, seen on the buyer's side · by where it is · stated by …)",
    "recurring_billing": "the billing period: 1 monthly · 2 quarterly · 3 yearly or longer · 4 per order / project · 5 one-off …",
    "billing_cadence": "the cadence in words, with whether it is published or by the kind",
    "recurring_billing_basis": "the sentence or rule the period rests on",
    "bill_amount_indicative": "a published amount of one bill",
    "bill_amount_basis": "where that amount was read (quote, page, day)",
    "bill_items_as_published": "what is billed",
    "bill_currency_as_published": "the bill's currency, as published",
    "bill_delivery_as_published": "how the bill reaches the payer (an invoice by mail, a notice, a portal …), quoted",
    "bill_payment_method_as_published": "how the biller is paid, quoted",
    "bill_tax_rule_as_published": "the tax the biller adds, quoted",
    "bill_identifier_format": "the number a bill carries (invoice, account, licence, policy number)",
    "service_stops_if_unpaid": "what happens when it is not paid, quoted",
    "bill_due_terms_as_published": "when the bill is due, quoted",
    "bill_remit_to_as_published": "where a payment by post goes, quoted",
    "billing_period_calculated": "a period calculated when none is published (labelled)",
    "bill_amount_calculated": "the estimate or calculation (estimated — / calculated —), with every figure it rests on",
    "invoice_fields_present": "n/9 of the nine main invoice fields present",
    "invoice_fields_missing": "the main invoice fields missing",
    "contract_reference": "the record's reference (contract, licence, permit, patent, policy number …)",
    "po_or_reference_to_quote": "the reference an invoice of this relationship should quote, and why",
    "contract_title": "the record's title or what the relationship is for",
    "instrument_type": "the instrument as the source names it (contract, PO, standing offer, grant …)",
    "instrument_type_normalized": "the instrument in a fixed list",
    "procurement_method": "how it was awarded (open, limited, sole source …), as published",
    "commodity": "the commodity as published",
    "contract_nature": "works, a service or goods — and by what",
    "contract_description": "the record's description",
    "number_of_bids": "bids received, as published",
    "po_number_as_published": "the PO number in the record",
    "po_numbers_this_pair_open_data": "other PO numbers of this buyer–vendor pair in open data",
    "po_count_this_pair_open_data": "how many",
    "contract_numbers_this_pair_open_data": "contract numbers of this pair in open data",
    "contract_or_agreement_number": "the contract or agreement number",
    "solicitation_or_tender_number": "the tender or solicitation number",
    "award_or_notice_id": "the award or notice id",
    "buyer_vendor_id": "the vendor's id with the buyer, when published",
    "vendor_ids_in_record": "the vendor ids the record carries",
    "commodity_codes": "commodity codes (UNSPSC, GSIN, NAICS …)",
    "buyer_org_codes": "the buyer's department codes",
    "amendment_or_modification": "an amendment's number or note",
    "all_identifiers": "every identifier of the record, as JSON",
    "identifier_count": "how many",
    "invoice_reference_hint": "what to quote when no PO is published",
    "contract_value": "the record's published value, with its source field",
    "currency": "its currency",
    "award_date": "when it was awarded or dated", "start_date": "when it starts", "end_date": "when it ends (published)",
    "contract_term_as_published": "its term as published",
    "contract_link": "the record's page",
    "source": "the source of the relationship",
    "vendor": "the Canadian biller, by its name (inferred: … for a distributor by location)",
    "vendor_legal_name": "its legal name, with where it was read (register, its own site, the record)",
    "vendor_trading_name": "the name it trades under, when it differs",
    "vendor_registry_id": "its register entry", "vendor_registry_url": "the register's page",
    "vendor_registered_address": "its registered office (register)",
    "vendor_neq": "its Québec NEQ", "vendor_qst_as_published": "its QST number, as printed", "vendor_legal_form": "its legal form",
    "vendor_activity_code": "its activity code (REQ)", "vendor_employees_quebec": "its employees in Québec (REQ range)",
    "vendor_establishments_quebec": "its establishments in Québec (REQ)", "vendor_directors_range": "its number of directors (REQ range)",
    "vendor_last_annual_filing": "its last annual filing", "vendor_address": "its printed address (what puts it in Canada), with the page",
    "vendor_country_basis": "the source field or page that says the vendor is in Canada, quoted",
    "vendor_bn9": "its Business Number, as published", "vendor_gst_hst_derived": "BN9 + RT0001 — derived, labelled",
    "vendor_website": "its website", "vendor_emails": "its role mailboxes, as its site prints them", "vendor_phone": "its telephone",
    "vendor_contact_evidence_url": "where its contacts were read", "vendor_logo_url": "its logo", "vendor_website_status": "whether its site answered",
    "vendor_website_basis": "how its site was tied to it", "vendor_linkedin_url": "its LinkedIn page", "vendor_industry_naics": "its NAICS code",
    "vendor_billing_ar_email": "its billing / receivables mailbox, as printed", "vendor_contacts_found_by": "who found its contacts",
    "vendor_peppol_id": "its Peppol id", "vendor_facts_provenance": "where each vendor fact was read", "method_notes": "notes on how the row was made",
    "facts_provenance_json": "the sources of the mailbox, the buyer's facts, the vendor's facts and the relationship, as JSON",
    "contracts_with_canadian_suppliers": "the buyer's records with Canada-located vendors in the contract dataset",
    "buyer_keys": "how many pipeline keys the buyer has", "keys": "the buyer's pipeline keys (b:…, lead:…)",
    "tier": "A · B · L · F · M · T · C · D · E · R · I · N (section 15)", "grade": "mailbox grade 4 invoicing/AP · 3 finance · 2 purchasing · 1 general",
    "acc": "True when the mailbox is confirmed", "distinct_canadian_vendors": "the buyer's distinct Canada-located vendors",
    "records_last_12_months": "its records of the last 12 months", "latest_award_date_any_vendor": "its latest award with any Canadian vendor",
    "total_known_value_canadian_suppliers": "the total published value of its records with Canadian vendors",
    "other_canadian_vendors_sample": "some of its other Canadian vendors", "record_sources": "the sources of its records",
    "records_with_this_vendor": "its records with this vendor", "all_references_with_this_vendor": "every reference with this vendor",
    "records_in_contract_dataset": "its records in the contract dataset", "other_relationship_sources": "other relationships on file for it (what the row does not stand on)",
    "typical_contract_value_p50": "the median value of its contracts", "typical_contract_value_p75": "the 75th percentile", "typical_contract_value_p90": "the 90th percentile",
    "average_contract_duration_days": "its average contract term", "contract_durations_counted": "how many terms were counted",
    "commodity_distribution_top3": "its top commodities", "year_over_year_spend_trend": "its spend year over year", "typical_cadence_days": "days between its awards",
    "vendor_concentration_top_share": "its top vendor's share", "all_canadian_vendors": "all its Canadian vendors",
    "pair_prior_records": "records of this buyer–vendor pair", "pair_first_or_repeat": "first or repeat relationship", "pair_value_trend": "the pair's value over time",
    "pair_dates_and_values": "the pair's records by date and value", "most_recent_record_reference_any_vendor": "its most recent record's reference",
    "org_group_key": "the grouping key of its contract records", "vendor_registry_status": "the vendor's status in the register",
    "vendor_registry_warning": "a warning from the register (struck off, inactive …): the row is held", "vendor_registry_note": "a note on the register match",
    "vendor_registry_match_level": "how the register match was made", "vendor_incorporation_date": "when it was incorporated",
    "vendor_years_in_business": "its years in business", "vendor_wikidata": "its Wikidata item", "vendor_founded": "its founding year",
    "vendor_employees": "its employees, when published", "vendor_bn_source": "where its BN came from",
}
for _c in ("contract_value", "start_date", "end_date", "contract_title", "contract_description", "instrument_type", "procurement_method", "number_of_bids", "po_number_as_published",
           "contract_or_agreement_number", "solicitation_or_tender_number", "award_or_notice_id", "buyer_vendor_id", "commodity_codes", "buyer_org_codes"):
    DESC[_c + "_from_pair"] = "the same, from another record of the same buyer–vendor pair"

KIND_TEXT = {
    "utility account by location": (
        "**What it is.** The electricity distributor that, by law, serves the organisation's own printed address bills it every month or two on an "
        "invoice paid through a bank (rule 13, owner 2026-11-11 16:01 EST). Abroad, the same for the utilities a Canadian company owns (rule 18).\n\n"
        "**Depth.** The biller is certain for the address; the account holder is not published (the organisation, its landlord, or both) and every "
        "row says so. Weakest of the kinds; it comes last for a buyer with any record (rule 13: a record or a service seen first).\n\n"
        "**Source and tool.** `tools/by_location.py`: 68 distributors with their postal areas (each one's own territory page and rate page read and "
        "quoted); Ontario by the Ontario Energy Board's map of service areas (`tools/on_ldc_table.py`, postal code by postal code; a code near an edge "
        "or shared by two gets none); towns running their own utility over their whole territory (Westmount, New Westminster, Penticton, Coaticook …); "
        "Alberta left out (retail choice: no distributor's bill). The address is the organisation's own page, a register, or the place listing for its "
        "website (Overture Maps, Foursquare), said on the row. Rule 18 abroad: `tools/abroad_utilities.py` (retail service territories, ZIP codes "
        "wholly inside one territory, the parent's own page quoted for the ownership).\n\n"
        "**Amount.** The distributor's own published rates at 2,500 kWh a month (a small office), estimated; municipalities outside Ontario from "
        "their residents (section 5).\n\n**Caveats.** A tower, campus or business centre (50+ organisations at one postal code) is held; a postal "
        "code printed with another province is held; a city whose utility serves only part of it gets no distributor."),
    "utility account by own report": (
        "**What it is.** An Ontario public body's own energy report under O. Reg. 25/23 lists its facilities, their addresses and the electricity "
        "each bought from the grid; the regulation asks for a facility's report only where the body is issued the invoices for its energy.\n\n"
        "**Depth.** A public record of the relationship and of its size, with the account holder (the body) published.\n\n**Source and tool.** "
        "`tools/bps_energy.py` (Ontario Ministry of Energy and Mines open data), each facility's postal code to its distributor (OEB map).\n\n"
        "**Amount.** Calculated from the body's own reported use (section 5)."),
    "public contract": (
        "**What it is.** A contract, purchase order or award by a public buyer to a vendor whose address in the record is in Canada.\n\n**Depth.** "
        "Strongest: a public record naming both parties, with value, dates and references. Current when the published end date is today or later "
        "(tier A), or the award is less than 12 months old (B; 12–36 months is L, not current alone); an award more than three years old with no "
        "end date is not current (rule 11).\n\n**Source and tool.** The contract dataset: 82+ source pipelines (`scripts/<source>/`, notes in "
        "`notes/`), merged into the release `dataset-latest`; Canadian federal, provincial, municipal, school-board and health-authority disclosures, "
        "US federal (USAspending, subawards), states and cities, UK, EU (TED), Australia, and others; the vendor's Canada location read from the "
        "source's own vendor address or country field (`vendor_country_basis`).\n\n**Amount.** The published value, spread over the term when the "
        "term is published; a framework ceiling is never a bill."),
    "licence or registration": (
        "**What it is.** The organisation holds a licence or registration in force with a Canadian body, which bills it to keep it (yearly, or at "
        "each renewal).\n\n**Depth.** The body's own public register lists the holder today: current by construction.\n\n**Source and tool.** "
        "City business licences (Vancouver, Calgary, Edmonton, Toronto — `tools/biz_licences.py`), the Régie du bâtiment du Québec, the CMEQ and the "
        "CMMTQ (`rbq-licences`), Québec's Office de la protection du consommateur, Health Canada's establishment and product registers "
        "(`tools/hc_registers.py`), ISED's radio licences, the HCRA, the RACJ, provincial resource registers and others (`authority-registers`). "
        "Natural persons and sole proprietors are left out.\n\n**Amount.** The body's own fee table for that kind of licence, or the fee paid in the "
        "open data."),
    "agent of record": (
        "**What it is.** A Canadian patent or trademark agent named by CIPO's register as the agent of record for the organisation's patents or "
        "trademarks; the agent bills the owner for each step and for the official fees it advances.\n\n**Depth.** A public register; the agent's "
        "own fees are not published.\n\n**Source and tool.** CIPO's patent register (CSV extract) and trademark register (`pt-register`, "
        "`tm-register`, `pt-sites`, `tm-sites`); the firm's name with its legal form as the register prints it.\n\n**Amount.** CIPO's official 2026 "
        "fees as a floor (section 5)."),
    "membership": (
        "**What it is.** The organisation is a member of a Canadian chamber, board of trade, association or accreditation body that bills dues each "
        "year.\n\n**Depth.** The body's own current member directory (a lapsed member leaves it): the biller's own roster. BBB accreditation is a "
        "fee too.\n\n**Source and tool.** Member directories read by `member-live` / `tools/member_lists.py` (GrowthZone / ChamberMaster / "
        "MemberClicks and the bodies' own pages), BBB accredited businesses.\n\n**Amount.** The body's lowest published membership fee (the "
        "member's own dues are that or more)."),
    "sponsorship": (
        "**What it is.** A sponsor or exhibitor of a Canadian organisation's event or programme, billed the fee.\n\n**Depth.** The organiser's own "
        "list; current only for this year's or an upcoming event; an in-kind or donors list, a foundation funding the organisation, or a past event "
        "is not a row.\n\n**Amount.** Rarely published (sponsorship tiers are not tied to names)."),
    "dealership": (
        "**What it is.** A dealer or retailer of a Canadian manufacturer or distributor, invoiced for the goods it buys for resale.\n\n**Depth.** The "
        "supplier's own dealer locator; what the dealer buys is never published (no amount).\n\n**Caveats.** A supplier's terms for its online "
        "shop (cards, PayPal, checkout) are a retail customer's, not the dealer's: they are not used."),
    "tenancy": (
        "**What it is.** A commercial tenant of a Canadian landlord (a mall, an office group), billed rent each month.\n\n**Depth.** The landlord's "
        "own tenant directory. A Canadian group's buildings abroad are not rows (rule 19)."),
    "service seen on the buyer's side": (
        "**What it is.** The buyer's own site or DNS runs on a Canada-headquartered vendor's paid service that is billed on invoice (hosting, mail, "
        "DNS, platforms).\n\n**Depth.** Seen today on the buyer's side; the account may be the organisation's or its web agency's. A service "
        "charged to a card on file is not a row (rule 6).\n\n**Source and tool.** `tools/tech_relationships.py`, `tools/tech_portals2.py`, the DNS "
        "sweeps (`dns-services`, `ct-names`), the vendors' own billing pages (`tools/vendor_billing.py`, hand-read ones in `BILLING_BY_DOMAIN`).\n\n"
        "**Amount.** The vendor's lowest published price for the product seen."),
    "benefit plan contract": (
        "**What it is.** A US employer's benefit plan insured by a Canadian insurer (Sun Life Assurance Company of Canada's U.S. branch — the "
        "Canadian legal entity itself) or paying a provider in Canada.\n\n**Depth.** The plan's Form 5500 (US Department of Labor), Schedule A or "
        "C: a public record with the policy number and the year.\n\n**Amount.** Premiums or commissions of the plan year (section 5)."),
    "exchange listing": (
        "**What it is.** A company listed on a Canadian stock exchange (TSX, TSXV, CSE), billed listing fees.\n\n**Depth.** The exchange's own "
        "list of issuers."),
    "export sale": (
        "**What it is.** An importer abroad buying from a Canadian exporter, on the exporter's commercial invoice.\n\n**Depth.** Colombia's customs "
        "(DIAN) import declarations name the importer, the exporter, the exporter's invoice number and date, the FOB value and the payment form."),
    "promotional agency": (
        "**What it is.** A producer represented in Québec by its promotional agent, as the SAQ's own product page names both; the agent bills its "
        "commission.\n\n**Depth.** The SAQ's page (`tools/saq_agents.py`)."),
}
LIMITS = """- **Rows by location are the bulk** (<!--LOC--> of the ready rows): the biller is certain, the account holder is not published, and the amount is a
  small office's estimate unless the organisation reports its own use (Ontario public bodies) or is a municipality outside Ontario.
- **"By the kind of relationship"**: <!--BYKINDN--> ready rows say how a bill of their kind is billed and paid because the biller publishes nothing on
  it; the biggest billers among them (one page read there would fill their rows): <!--TOPBYKIND-->.
- **Amounts**: <!--AMT--> ready rows carry an amount; of those, <!--AMTPUB--> published and <!--AMTEST--> estimated. Member dues are the body's lowest
  published fee, not the member's own; an agent's own fees, a dealer's purchases and a sponsor's tier are not published.
- **Mailboxes**: <!--GEN--> ready rows carry a general mailbox (the organisation publishes no invoicing, finance or purchasing one); the owner ruled it
  fine (rule 9).
- **Rule 19 judgement**: 336 exhibitors and sponsors of Marketplace Events' shows are held as billed by a U.S. LLC ("Marketplace Events LLC", with
  Canadian offices; Investment Canada lists the LLC as a Canadian business in Beechville, NS). If the owner reads it otherwise, they come back by
  removing that one register match (coord/DECISIONS.md, 2026-11-14).
- **Names**: a buyer whose only name found was not a name shows its domain name (zakaccounting.ca); about <!--DOMNAMES--> ready rows are named by a
  domain.
- **Dates move**: the table means "current on 2026-11-13" (`coord/config.json`). Of the ready rows, <!--EXP30--> carry a published end date within
  30 days of it and <!--EXP90--> within 90 days; <!--NODATE--> ready public contracts have no published end date (an award of the last 12 months,
  tier B). Read `end_date` against the day of use.
- **Values are as the source publishes them**: a contract value is the record's own (a group purchase can be published under one member — the
  village of Senneville's road-salt contract of $23.5 million is one of them); the figure is not converted to Canadian dollars (the currency
  follows it in `amount_mark` when it is not the dollar).
- **Mailboxes at an internet provider**: <!--ISP--> ready rows carry the organisation's own mailbox at videotron.ca, bell.net, sympatico.ca, shaw.ca,
  cogeco … — printed by the organisation as its address, kept (decision of 2026-11-04); the webmail rule names the free webmail services.
- **Broken characters**: <!--FFFD--> ready rows carry a replacement character (�) in a name, an address or a title, where a page was read in the
  wrong encoding; it cannot be read back without the page (the buyer's name in such a row was replaced by its domain name).
- **Names**: the corrected copy cleaned thousands of names (section 12), but a few hundred ready rows still carry a page's words rather than the
  organisation's name (a service and a town: "Dentist in Bracebridge", a slogan) — the row's website and mailbox identify it.
- **Nothing here is legal or tax advice**: tax cells marked DERIVED follow the general rules (place of supply, public service bodies, exports) and
  say so."""


WHY = [
    ("ready -> not ready: relationship: the vendor's own name is a U.S. legal entity", "rule 19 (owner 2026-11-13 11:44 EST): a company abroad is not a Canadian vendor — 336 of them the exhibitors and sponsors of Marketplace Events LLC's shows"),
    ("ready -> not ready: relationship: the vendor is a company abroad", "rule 19: a company abroad that a Canadian company owns (John Hancock)"),
    ("ready -> not ready: relationship: the organisation and the biller are one", "a body does not bill itself (a chapter named by its parent's name, a utility at its own address)"),
    ("ready -> not ready: relationship not established", "a foundation that funds the organisation is not its biller"),
    ("ready -> not ready: field: buyer address", "a row by location whose address was taken out (a platform's, a template's) or whose postal code lies in another province than the one printed: the distributor is not certain"),
    ("ready -> not ready: field: vendor address", "the source prints no address for the vendor (what puts it in Canada), or the address was read on the buyer's own site"),
    ("ready -> not ready", "all the rows the corrections took out of the ready set (the reasons follow)"),
    ("not ready -> ready", "rows that received a mailbox the referee had re-read before Actions stopped"),
    ("buyer name corrected — ", "a page title's words around the name (title_names.py; each rule read against the rows it changes)"),
    ("buyer name corrected", "the organisation's name out of a page's title or text, or its domain name where the only name found was not a name"),
    ("buyer name: not a name", "no name and no site of its own: not ready (AGENTS.md §2.2)"),
    ("buyer's site: a mail provider's domain", "the site was the domain of the organisation's mailbox (videotron.ca, sympatico.ca): removed"),
    ("vendor's site: the buyer's own", "the vendor's site was the buyer's (a municipality's list of local merchants): removed with what was read on it"),
    ("the organisation and the biller are one", "same name or same site: no relationship"),
    ("vendor legal name cleared", "a sentence of a terms page that shares a word with the vendor is not its legal name (\"Voice over Internet Protocol\" for Storm Internet)"),
    ("CMEQ / CMMTQ licence", "the corporation's own yearly dues and the yearly fee to keep the licence, each published, their sum calculated"),
    ("bill details added", "how the body bills and takes payment, each sentence verified on its own page after the build (tools/data/payees)"),
    ("mailbox added", "read on the organisation's own site and re-read by the referee before Actions stopped"),
    ("municipality outside Ontario", "electricity estimated from its residents (tools/muni_energy.py), a floor"),
    ("member dues amount cleared", "a member benefit's price or value is not the dues"),
    ("buyer legal name cleared", "a sole proprietor's own name is not written"),
    ("row with no vendor at all", "no biller: no relationship record (tier N)"),
    ("ready -> not ready: relationship: the address the distributor was named for is a web platform", "a Shopify store's legal notice names Shopify's head office (151 O'Connor Street, Ottawa): the store is not there"),
    ("ready -> not ready: relationship: the address the distributor was named for is a site template", "a site template's sample address (123 Main Street … M1M 1M1) named the distributor"),
    ("ready -> not ready: relationship: the organisation's site and mailbox are another country", "a places listing in Canada that gives a site abroad (a namesake's), or a Canadian office with its parent's mailbox abroad"),
    ("ready -> not ready: mailbox: on another country's domain", "a mailbox of an affiliate abroad or a namesake (Deloitte & Touche LLP of Virginia with deloitte.be)"),
    ("ready -> not ready: site: the organisation's site and mailbox are another country", "a register's address in one country, a namesake's site in another"),
    ("ready -> not ready: no mailbox", "a named person's mailbox taken off, or a namesake's site and mailbox"),
    ("buyer address: a web platform's own address", "Google, Cloudflare, Meta, YouTube, Shopify … named on privacy and legal pages, read as the organisation's address: taken out"),
    ("buyer address: a site template's sample", "\"123 Main Street, New York, NY 10001\", \"Lorem ipsum\" — a template's sample: taken out"),
    ("buyer address: another office's", "the company's legal form and its mailbox are of one country (a GmbH with its .de mailbox): the address of an office elsewhere taken out"),
    ("buyer address: another country's than its own site", "read on its own site of another country: another office's or a third party's — taken out"),
    ("location row on a web platform", "see above: no relationship"),
    ("location row whose site or mailbox", "held: the organisation is not shown to be at the address"),
    ("mailbox of another country", "held: an affiliate's or a namesake's mailbox"),
    ("record's address in one country", "held: a namesake's site"),
    ("mailbox removed: a named person's", "AGENTS.md §2.5: cindy.accounting@…, jen.accounting@… are persons' mailboxes"),
    ("mailbox: its role corrected", "the page says what the mailbox is for (Durham University: invoice queries only, “Do not send invoices to this address”)"),
    ("site and mailbox removed: a namesake's site", "a site matched by name to another organisation (a German firm's for a U.S. exporter)"),
    ("vendor address: the receiving facility", "a U.S. EPA hazardous-waste export notice: the Canadian receiving facility is the vendor; the shipper's address had been put in its place"),
    ("buyer's site: a mail provider's domain", "the site was the domain of the organisation's mailbox (videotron.ca, sympatico.ca): removed"),
]


def money_n(s):
    m = re.search(r"\d[\d,]*(?:\.\d+)?", s or "")
    return float(m.group(0).replace(",", "")) if m else None


def main(outdir, dest):
    t = os.path.join(outdir, "ranked_buyers.csv.gz")
    fill, nready, nrows = collections.Counter(), 0, 0
    ex = {}
    k_all, k_ready, k_route, k_mark, k_vendor, k_src, k_ex = (collections.Counter(), collections.Counter(), collections.defaultdict(collections.Counter),
                                                              collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter),
                                                              collections.defaultdict(collections.Counter), {})
    marks_ready, marks_all = collections.Counter(), collections.Counter()
    full = amtper = big = gen = domnames = amt = amtpub = amtest = 0
    isp = fffd = exp30 = exp90 = nodate = 0
    ISP = re.compile(r"@(?:videotron\.(?:ca|com|net)|bell\.net|bellnet\.ca|sympatico\.ca|shaw\.ca|rogers\.com|cogeco\.(?:ca|net)|telus\.net|eastlink\.ca|"
                     r"globetrotter\.net|xplornet\.(?:ca|com)|tbaytel\.net|mts\.net|sasktel\.net|nbnet\.nb\.ca)$", re.I)
    REF = datetime.date(2026, 11, 13)
    bykind_vendor = collections.Counter()
    with gzip.open(t, "rt", encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f)
        head = rd.fieldnames
        for x in rd:
            nrows += 1
            ready = (x.get("ship_ready") or "").startswith("yes")
            kind = (x.get("invoice_fields_for_kind") or "").split(":")[0] or "(none)"
            mk = (x.get("amount_mark") or "5")[:1]
            k_all[kind] += 1
            marks_all[mk] += 1
            if not ready:
                continue
            nready += 1
            k_ready[kind] += 1
            marks_ready[mk] += 1
            k_route[kind][(x.get("payment_route") or "").split(" — ")[-1][:60] if "by the kind" in (x.get("payment_route") or "") else (x.get("payment_route") or "")[:60]] += 1
            k_mark[kind][mk] += 1
            k_vendor[kind][re.sub(r"^inferred:\s*", "", x.get("vendor") or "")[:60]] += 1
            k_src[kind][(x.get("how_relationship_was_found") or "")[:90]] += 1
            if kind not in k_ex and mk in "123" and (x.get("bill_payment_method_as_published") or x.get("bill_delivery_as_published")):
                k_ex[kind] = {c: (x.get(c) or "") for c in ("buyer", "vendor", "relationship_fact_basis", "contract_status", "contract_reference", "contract_title",
                                                             "recurring_billing", "bill_amount_indicative", "bill_amount_calculated", "contract_value", "amount_mark",
                                                             "bill_delivery_as_published", "bill_payment_method_as_published", "bill_due_terms_as_published",
                                                             "payment_route", "email_type", "vendor_tax_or_registration_number", "ship_ready")}
            for c in head:
                v = (x.get(c) or "").strip()
                if v and v != "not_published":
                    fill[c] += 1
                    if c not in ex and len(v) < 160 and c not in ("email", "email_evidence_quote", "ap_phone", "buyer_phone", "vendor_phone", "vendor_emails",
                                                                   "ap_contact_name_as_published", "directory_general_email", "vendor_billing_ar_email", "dmarc_record", "spf_record"):
                        ex[c] = v
            a = any((x.get(c) or "").strip() for c in ("bill_amount_indicative", "contract_value", "bill_amount_calculated"))
            per = (x.get("recurring_billing") or "")[:1] in "1234" and bool((x.get("recurring_billing") or "")[:1])
            amtper += a and per
            amt += a
            if (x.get("contract_value") or x.get("bill_amount_indicative") or "").strip():
                amtpub += 1
            elif (x.get("bill_amount_calculated") or "").strip():
                amtest += 1
            full += bool(a and per and all(any((x.get(c) or "").strip() for c in cs) for cs in (("vendor_legal_name",), ("vendor_tax_or_registration_number",),
                                                                                                   ("bill_items_as_published", "contract_title"),
                                                                                                   ("bill_delivery_as_published",), ("bill_payment_method_as_published", "payment_route_basis"),
                                                                                                   ("bill_due_terms_as_published", "payment_terms_as_published"))))
            big += mk in "12"
            gen += (x.get("email_type") or "") == "general"
            domnames += bool(re.fullmatch(r"(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}", (x.get("buyer") or "").strip().lower()))
            if "by the kind" in (x.get("payment_route") or ""):
                bykind_vendor[re.sub(r"^inferred:\s*", "", x.get("vendor") or "")[:50]] += 1
            isp += bool(ISP.search((x.get("email") or "").strip()))
            fffd += any("\ufffd" in (x.get(c) or "") for c in ("buyer", "buyer_address", "vendor", "vendor_legal_name", "vendor_address", "contract_title"))
            m_ = re.match(r"(\d{4})-(\d{2})-(\d{2})", x.get("end_date") or "")
            if m_:
                try:
                    dd = (datetime.date(int(m_.group(1)), int(m_.group(2)), int(m_.group(3))) - REF).days
                except ValueError:
                    dd = None
                if dd is not None:
                    exp30 += dd <= 30
                    exp90 += dd <= 90
            elif kind == "public contract":
                nodate += 1
    counts = json.load(open(os.path.join(outdir, "counts.json"), encoding="utf-8")).get("counts", {}) if os.path.exists(os.path.join(outdir, "counts.json")) else {}
    s = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "HANDOFF_TEMPLATE.md"), encoding="utf-8").read()
    s = s.replace("<!--DATE-->", datetime.date.today().isoformat()).replace("<!--ROWS-->", format(nrows, ",")).replace("<!--NCOLS-->", str(len(head)))
    mname = {"1": "published $5,000+", "2": "estimated $5,000+", "3": "published under $5,000", "4": "estimated under $5,000", "5": "no amount"}
    s = s.replace("<!--HEADLINE-->", "\n".join([
        "| | ready | all rows |", "|---|---:|---:|", "| rows | **%s** | %s |" % (format(nready, ","), format(nrows, ","))] +
        ["| amount mark %s — %s | %s | %s |" % (k, mname[k], format(marks_ready[k], ","), format(marks_all[k], ",")) for k in "12345"] +
        ["", "Of the ready rows: %s carry an amount and a billing period; %s carry every main invoice field (amount, period, biller legal name and number, "
         "what is billed, how the bill arrives, how it is paid, when it is due); %s are $5,000 or more a bill (published or estimated)." % (
             format(amtper, ","), format(full, ","), format(big, ","))]))
    # columns
    lines = ["| column | what it holds | fill (ready) | example |", "|---|---|---:|---|"]
    for c in head:
        e = (ex.get(c) or "").replace("|", "/").replace("\n", " ")
        lines.append("| `%s` | %s | %s | %s |" % (c, DESC.get(c, "(see the example)").replace("|", "/"), "%.0f%%" % (100.0 * fill[c] / max(1, nready)), e[:110]))
    s = s.replace("<!--COLUMNS-->", "\n".join(lines))
    # kinds
    out = []
    for kind, n in k_all.most_common():
        out.append("### %s — %s ready of %s rows" % (kind, format(k_ready[kind], ","), format(n, ",")))
        out.append("")
        if kind in KIND_TEXT:
            out.append(KIND_TEXT[kind]); out.append("")
        if k_ready[kind]:
            out.append("Invoice fields of the kind: %s." % ", ".join(RR.FIELDS.get(kind, [])) if kind in RR.FIELDS else "")
            out.append("")
            out.append("Ready rows by amount mark: %s." % " · ".join("%s %s" % (mname[m], format(k_mark[kind][m], ",")) for m in "12345" if k_mark[kind][m]))
            out.append("How they are paid: %s." % " · ".join("%s %s" % (r or "(none)", format(c, ",")) for r, c in k_route[kind].most_common(4)))
            out.append("Biggest billers: %s." % " · ".join("%s (%s)" % (v, format(c, ",")) for v, c in k_vendor[kind].most_common(6)))
            out.append("")
            e = k_ex.get(kind)
            if e:
                out.append("A ready row, as written (mailbox shown by its type only):")
                out.append("")
                out.append("```")
                for c, v in e.items():
                    if v:
                        out.append("%-34s %s" % (c + ":", v.replace("\n", " ")[:300]))
                out.append("```")
                out.append("")
    s = s.replace("<!--KINDS-->", "\n".join(out))
    s = s.replace("<!--BYKIND-->", "\n".join(["| kind | how a bill of that kind is billed and paid |", "|---|---|"] +
                                             ["| %s | %s |" % (k, v) for k, v in RR.BY_KIND.items()]))
    s = s.replace("<!--FIELDS-->", "\n".join(["| kind | fields |", "|---|---|"] + ["| %s | %s |" % (k, ", ".join(v)) for k, v in RR.FIELDS.items()]))
    def why(k):  # the longest matching prefix wins
        best = max(((pre, w) for pre, w in WHY if k.startswith(pre)), key=lambda t: len(t[0]), default=("", ""))
        return best[1]
    corr = ["| correction | rows | why |", "|---|---:|---|"] + ["| %s | %s | %s |" % (k.replace("|", "/"), format(v, ","), why(k).replace("|", "/"))
                                                             for k, v in sorted(counts.items()) if not k.startswith("cells changed") and k not in ("rows", "ready after")]
    corr += ["", "Cells changed, by column: " + " · ".join("%s %s" % (k.replace("cells changed: ", "`") + "`", format(v, ","))
                                                      for k, v in sorted(counts.items()) if k.startswith("cells changed")) + "."]
    logs = ""
    for fn in ("priority_sort.log", "fold.log"):
        p = os.path.join(outdir, fn)
        if os.path.exists(p):
            logs += "\n" + open(p, encoding="utf-8").read().strip()
    s = s.replace("<!--CORRECTIONS-->", "Every changed cell is in `corrections.csv.gz` (row key, buyer, field, before, after).\n\n" + "\n".join(corr) +
                  ("\n\nThen one row per organisation (`tools/priority_sort.py`) and one row per website and name (the fold):\n\n```" + logs + "\n```" if logs else ""))
    loc = k_ready["utility account by location"]
    lim = LIMITS.replace("<!--LOC-->", "%s (%.0f%%)" % (format(loc, ","), 100.0 * loc / max(1, nready))).replace("<!--BYKINDN-->", format(sum(bykind_vendor.values()), ","))
    lim = lim.replace("<!--TOPBYKIND-->", "; ".join("%s (%s)" % (v, format(c, ",")) for v, c in bykind_vendor.most_common(12)))
    lim = lim.replace("<!--AMT-->", format(amt, ",")).replace("<!--AMTPUB-->", format(amtpub, ",")).replace("<!--AMTEST-->", format(amtest, ","))
    lim = lim.replace("<!--GEN-->", format(gen, ",")).replace("<!--DOMNAMES-->", format(domnames, ","))
    lim = lim.replace("<!--EXP30-->", format(exp30, ",")).replace("<!--EXP90-->", format(exp90, ",")).replace("<!--NODATE-->", format(nodate, ","))
    lim = lim.replace("<!--ISP-->", format(isp, ",")).replace("<!--FFFD-->", format(fffd, ","))
    s = s.replace("<!--LIMITS-->", lim)
    open(dest, "w", encoding="utf-8").write(s)
    print("written", dest, len(s), "characters; ready", nready, "of", nrows)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "docs/HANDOFF_ROWS.md"))
