# Hand-off — building the invoices from the ranked packages (2026-11-09)

For the downstream AI (and anyone generating invoices from `coord/results/ranked/batches/*.csv`). Written by Claude, integrator lane, at the
owner's stop order. Everything below is drawn from the columns that exist on every delivered row; nothing here asks you to invent a value.

## 0. State at hand-off (final build 2026-11-09 13:09Z; the last build of the day re-renders `invoice_text` with formatted amounts)
- 63,628 delivered rows in 17 packages. **Pay on sight = 1,113 rows** (an invoice generated from the row clears AP: confirmed invoicing / AP or finance
  channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known), **+887** that lack
  only a published PO rule, **+22,024 "routed"** (complete invoice, but the organisation publishes one purchasing / general inbox — the invoice is
  forwarded internally, not addressed to AP). Gold (P01): 395 of 624 pay on sight (63 %); Gold at AP grade A: 225; AP payability (the stricter
  "submit today" test incl. the buyer's reference rule): Gold 452 / 624 (72 %), P02 306 / 404 (76 %).
- The 438 downstream benchmarks: 100 met. `COVERAGE_VS_TARGETS.md` carries a ceiling note under every field whose target no honest source can reach.
- Per row you get: `pay_on_sight` (yes / yes — reference rule not published / routed / no), `pay_on_sight_missing`, `channel_tier` (1–3, 0),
  `invoice_text` (a rendered draft header), `invoice_card_json` (the seven blocks, machine-readable), `ap_grade` A–E + `ap_grade_basis` +
  `ap_gap_to_A`, `ap_payability`, `invoice_readiness` / `invoice_missing`, and a provenance string on every fact (`facts_provenance_json`,
  `*_evidence_url`, `*_evidence_quote`, `mailbox_provenance`).

## 1. Which rows to build first (and what to do with the rest)
1. `pay_on_sight = yes` — build and send. 2. `pay_on_sight = yes — reference rule not published` — build; put "PO/order no.: as provided by the buyer"
   on the reference line and send; the buyer will reply with a PO if it needs one. 3. `routed` — build the same invoice; address the e-mail
   "Attention: Accounts Payable / À l'attention des comptes payables" to the general inbox; expect a slower first payment. 4. `no` — do not send; the
   missing element is named in `pay_on_sight_missing`. Within each tier, order by `ap_grade` (A first), then `ship_ready = yes`, then `ap_score`.
   Skip any row with `sensitivity_flag = yes` unless the owner says otherwise (police, corrections, child protection, crisis services).

## 2. Field-by-field: what goes on the invoice and where it comes from
**Header / dates** — invoice number and date are yours. Language: `template_language` (fr / en / fr-en from the buyer's own site; `language_hint`
as fallback). Québec public bodies: French.

**Bill to** — `buyer_legal_name_as_published` (the organisation's own legal name, with its source in brackets) else `buyer` (for public bodies the
published name is the billing name: "Ville de Laval", "City of Kelowna"; `buyer_type` tells you it is a public body). Address: `invoice_mailing_address`
if present (the AP page's own "send invoices to" address — it beats the head office), else `buyer_address`. Buyer's tax number when printed:
`buyer_bn_as_published` (BN + program; `buyer_gst_hst_derived` is BN9 + RT0001 and is labelled derived — do not print it as the buyer's registration).

**Submit to (the channel)** — `email` is the referee-confirmed mailbox; `email_type` says what it is (invoicing/AP, finance, procurement, general);
`channel_tier` 1 = invoicing / AP mailbox or an invoice portal, 2 = finance, 3 = purchasing / general. If `invoice_portal_url` is set and
`invoice_portal_kind` says invoicing (Ariba, Coupa, Tungsten, a supplier portal), the portal is the channel and the mailbox is the contact; a buyer on a
portal usually rejects e-mailed invoices. `supplier_setup_url` / "registr…" in `invoicing_requirements` means the buyer wants the vendor set up
first (W-9-style form, direct-deposit form) — do that before the first invoice. Format rules live in `invoicing_requirements` and
`invoicing_requirements_structured` (PDF only, one invoice per e-mail, size limits, subject-line rules — follow them literally; AP automation
rejects anything else). `peppol_participant_id` / `vendor_peppol_id`: e-invoicing is possible when both exist. `ap_system_hint` tells you the AP
system (Ariba, Coupa, SAP, Workday …) — useful for the expected rejection rules (Ariba: PO number mandatory, line items must match the PO).

**References** — print, in this order, whatever exists: `po_number_as_published` (rare: only buyers with PO-level open data), `contract_or_agreement_number`,
`solicitation_or_tender_number`, `award_or_notice_id`, `buyer_vendor_id` (the buyer's supplier number). `invoice_reference_hint` is the one line to
copy onto the invoice. `po_required_as_published` is the buyer's own rule, with its quote: when it says yes, never send without a PO number — ask the
buyer contact for it (`ap_phone`, `ap_contact_name_as_published`, or the mailbox itself). Never construct a PO number.

**From / remit to (the vendor)** — `vendor_legal_name` (registry or the vendor's own legal page; `vendor_trading_name` when it trades under another
name — print both: "Trading name, a division of Legal Name Inc."), `vendor_registered_address` (registry) or `vendor_address` (the record / the site),
`vendor_bn9` + the GST/HST account `vendor_gst_hst_derived` (BN9 + RT0001 — the standard account suffix; print it as "GST/HST No. 123456789 RT0001"),
`vendor_neq` and `vendor_qst_as_published` for Québec (QST number must appear on Québec invoices when the vendor is QST-registered), `vendor_billing_ar_email`
(the vendor's own AR mailbox for the "questions about this invoice" line), `vendor_phone`, `vendor_website`. If `vendor_bn9` is blank, the invoice is
legally incomplete from $100 (see the legal minimum below) — get the number from the vendor; do not search it.

**Legal minimum for the buyer's input-tax-credit claim** (Input Tax Credit Information (GST/HST) Regulations, SOR/91-45 s. 3, read 2026-11-09 at
https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3-20240620.html): under $100 — supplier name or trade name, invoice date, total;
$100 to $499.99 — plus the supplier's GST/HST registration number and the tax amount (or "tax included"); $500 or more — plus the recipient's name
(or trade name), the payment terms and a description of each supply. Practically every contract here is far above $500, so all three tiers apply:
no invoice leaves without the vendor's registration number, the buyer's name, the terms and a line description. Québec adds the QST number
(Revenu Québec "Preparing invoices"). This is what AP's three-way match and the auditors check first — it is not optional formatting.

**Tax** — `buyer_tax_exempt_status` when the buyer publishes one (rare; quote it); otherwise `buyer_tax_status_derived` + `tax_rate_indicative_derived`
(labelled DERIVED: the rate for the buyer's province under the place-of-supply rules; municipalities / PSBs pay the tax and claim their own rebate;
federal bodies pay GST/HST since 1991; buyers outside Canada: zero-rated export, local tax is theirs). Show tax as a separate line with the rate
and the vendor's registration number; "taxes shown separately" is what the buyers' PO terms ask for most often.

**Currency** — `currency` from the contract record when it exists, else `invoice_currency_derived` (CAD for Canadian buyers; USD / GBP / EUR / AUD by
the buyer's country). State it on the invoice ("All amounts in CAD").

**Terms** — `payment_terms_as_published` (the buyer's own words, quoted) else `payment_terms_default_policy` (the statutory prompt-payment default
for construction, labelled) else the vendor's standard terms (net 30 is the Canadian norm). `buyer_payment_method_preference` (EFT / direct
deposit / cheque) and `buyer_ap_cycle_published` (cheque-run day) belong on the remittance block, not the terms line.

**Description / amount** — `contract_title`, `contract_description`, `contract_value`, `start_date` / `end_date`, `contract_term_as_published`,
`contract_link`. For relationship-proof rows (client lists, lobbying filings, auditor appointments) there is no contract record: the description
is the relationship (`relationship_detail`), the amount is yours.

**Follow-up block** — `ap_phone`, `ap_contact_name_as_published` (named by the organisation itself), `buyer_phone`, `buyer_esignature_preference`
(DocuSign etc. when the buyer wants signed documents), `buyer_supplier_portals_linked`.

## 3. Rules that keep the invoice from bouncing (learned from the buyers' own pages)
- A PO number is the single most common rejection reason at public bodies; the second is sending to the wrong inbox (procurement instead of AP).
- Québec public bodies: French invoice, TPS and TVQ numbers of the vendor, "Numéro de bon de commande" line; CIUSSS / CISSS centralise AP — use the
  centre's "Fournisseurs" address, not the hospital's. Ontario municipalities: HST 13 % shown separately, "Bill to: The Corporation of the …" is
  accepted but the published name is fine. Universities / hospitals / school boards: almost all run Ariba / Coupa / Jaggaer or a PO-matching ERP —
  one invoice per PO, line items in PO order.
- US / UK / AU / EU buyers (P01 contains ~130): zero-rate the Canadian tax, invoice in their currency unless the contract says CAD, add the vendor's
  Canadian GST/HST number anyway (their AP wants a tax id), W-8BEN-E on request for US buyers.
- `email_security_posture` EXPOSED (no DMARC enforcement) is the buyer's own posture, reported for your fraud controls: confirm banking-change requests
  by phone; it does not change the invoice. `mailbox_recheck_note` "not seen when re-read" means the page is dynamic — the referee's own re-fetch
  decided; use the mailbox but expect to confirm it once.
- `evidence_age_days` / `reverify_due`: mailboxes older than 60 days get a courtesy re-check before a first invoice to a buyer you have never billed.

## 4. Ceilings — what the data cannot give you (do not wait for it)
- Vendor GST/HST numbers for ~960 rows (Gold 138, P02 127, P04 693): no public registry exposes them (Québec-only vendors, partnerships, names absent
  from Canada's Business Registries). The vendor has it; ask.
- 22,025 "routed" rows: organisations that publish one inbox. That is their AP channel.
- Bill-to addresses / legal names on sites that block automated readers (~10 % of organisations) and P13 companies absent from registries.
- Contract numbers, values and dates for relationship-proof rows; end dates for P09 (unpublished by definition); PO numbers anywhere the buyer
  publishes no PO-level data.
- P11 (478 rows): mailboxes the referee cannot re-fetch; a second lane's quote confirms them over time.

## 5. What keeps running without anyone (zero cost to the owner) and how to stop it
- GitHub: `rank-buyers.yml` (builds every 6 h + on dispatch), `verify-and-merge.yml` (referee, on every push), `claude-engines.yml` (bulk registry daily).
- The Mac: push loop (15 min), walker-terms loop, site readers (every 2 h), API worker (capped at $170, idle), lane driver (3 h), Gemini's hourly task,
  Codex app automation (30 min, your ChatGPT quota) and a headless `codex exec` loop (`~/cch-crawler-state/codex_exec_loop.sh`, same quota).
  Stop all Mac loops: `pkill -f 'cch-crawler-state/.*_loop' ; pkill -f codex_exec_loop.sh` — the engines are restart-safe (resume files).
- Every result still goes through the referee; nothing lands unverified.

## 6. Levers audited at the stop order (all pushed or ruled out)
Done: AP mailboxes (crawler, walker, deep pages, API search of 7,690 buyers' AP / policy pages, four research lanes, referee + cross-verification);
AP terms (PO rule, payment terms, portals, formats, cadence, payment method, tax instructions, e-signature, AP systems) from 114k pages incl. the
purchasing bylaws / PO terms of 1,195 public bodies; registries (REQ, Corporations Canada, Canada's Business Registries, CRA charities, federal grant
recipients, BC OrgBook, Wikidata, municipal and government directories); vendor sites (legal pages, JSON-LD, logos, phones, role mailboxes, AR mailboxes);
award pages (contract values, dates, numbers, bid counts — 7 % yield); same-vendor carry-over; place-of-supply tax and currency for every row with a
resolvable province or country; public-body billing names; the relationship-record and tender-reference rules.
Ruled out (rules or cost): the CRA GST/HST registry (CAPTCHA), pattern-built mailboxes or numbers, inventing PO / contract numbers or dates, counting
derived defaults as published values, name-variant registry matching without provable precision (expected tens of rows), council-agenda PDF mining
for vendor GST numbers (expected < 20 rows), paying for more API search over pages already read.

## 7. `invoice_card_json` — the machine-readable header (same on every row with a mailbox)
Seven blocks; every value is a copy of the row's column named here, so the provenance is the column's `*_evidence_url` / `facts_provenance_json`:
- `bill_to`: `legal_name` (published legal name else the buyer's name), `legal_name_is_published`, `address` (invoice address else head office),
  `address_is_the_invoice_address`, `tax_number` (buyer's BN as published), `language` (fr / en / fr-en).
- `submit_to`: `email`, `email_type`, `supplier_setup_url`, `portal_url`, `portal_kind`, `mailing_address`, `format` (the "PDF only / one per e-mail" rule),
  `system` (Ariba, Coupa, SAP …), `e_invoicing_peppol`.
- `references_required`: `po_required` (the buyer's own rule, quoted), `po_number`, `contract_or_agreement_number`, `vendor_id_with_buyer`, `reference_hint`.
- `terms`: `payment_terms` (published, else the labelled statutory default), `payment_method`, `payment_cycle`, `e_signature`.
- `tax`: `buyer_tax_status` (published, else "DERIVED: …"), `buyer_tax_status_is_published`, `indicative_rate`, `currency` (published, else "DERIVED: …"),
  `currency_is_published`, `vendor_gst_hst` (BN9 + RT0001, derived), `vendor_qst`.
- `vendor_identity`: `legal_name`, `bn9`, `neq`, `remit_address`.
- `follow_up`: `ap_phone`, `ap_contact` (the person the organisation itself names), `requirements_text`.
Anything prefixed "DERIVED:" is a rule applied to the buyer's province / type, never a published fact: print it, but as the vendor's tax treatment, not
as the buyer's statement. `invoice_text` is the same card rendered as a draft header (BILL TO / SUBMIT TO / REFERENCE / FROM-REMIT TO / TAX |
CURRENCY | TERMS / DESCRIPTION | AMOUNT); the portal is labelled "invoice portal" only when the buyer's page says invoices go there, otherwise
"supplier / tender portal (not an invoice channel)" (SEAO, MERX, bids&tenders are tender portals — never send an invoice to them).

## 8. Two rows as they render (final build) — what "pay on sight" looks like
```
BILL TO: City of Calgary (official name …) — The City of Calgary, Accounts Payable, P.O. Box 2100, Station M, #8041, Calgary, AB T2P 2M5
SUBMIT TO: APInvoices@calgary.ca (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://portal.us.bn.cloud.ariba.com/… — SAP Ariba
  | format: invoices and any backup or supporting documentation in PDF format (as printed on https://www.calgary.ca/our-services/accounts-payable.html)
REFERENCE: contract AB-2026-05492 (apc_reference_number); tender 26-0108 (solicitation_number) | PO rule: yes (as published …)
FROM / REMIT TO: ION UNITED INC. — 1000 888 3rd St. SW, Calgary, AB, T2P 5C5 | GST/HST 894647304RT0001 (account derived from the BN9)
TAX: DERIVED: municipality: GST/HST applies to supplies to it … (GST/HST Memorandum 18-2) | CURRENCY: CAD | TERMS: 10 Business Days after receipt (as printed …)
DESCRIPTION: City of Calgary - Request for Quotes - 26-0108 Infoblox | AMOUNT: 976,500.00 CAD
```
Build it as: a PDF, one invoice, PO number asked from APInvoices@calgary.ca first (rule "yes"), GST 5 % shown separately (Alberta), net 10 business days,
reference line "Contract AB-2026-05492 / RFQ 26-0108 / PO …", sent to the Ariba portal (the mailbox is the fallback the page itself names).
```
BILL TO: Société de transport de Montréal — 1170-800 RUE de La Gauchetière O, Montréal, QC, H5A1J6
SUBMIT TO: facture.comptesapayer@stm.info (invoicing/AP mailbox, confirmed by the referee) | supplier / tender portal (not an invoice channel): SEAO
REFERENCE: contract 20168351|20168352 (ocds_contract_ids); tender 6000041033 (numero) | PO rule: purchase-order terms published (as published: … TVQ et la TPS …)
FROM / REMIT TO: DECASULT INC. — 600 de Maisonneuve Ouest, Suite 3200, Montréal, QC, H3A3J2 | GST/HST 101313286RT0001 (derived from the BN9) | NEQ 1142909408
TAX: DERIVED: taxable purchaser presumed … place-of-supply rate of QC | CURRENCY: CAD | TERMS: net 30 jours (as printed on https://www.stm.info/espace-affaires/fournisseur)
DESCRIPTION: S115 - Services d'experts indépendants en vérification de coûts | AMOUNT: 416,594.66 CAD
```
Build it as: French, "Facture", TPS 5 % and TVQ 9.975 % on separate lines with both registration numbers (the TVQ number is the vendor's — it is not in the
data: ask the vendor; `vendor_qst_as_published` is blank here), "Numéro de contrat 6000041033 / bon de commande …", net 30 days, e-mailed as one PDF to
facture.comptesapayer@stm.info. SEAO is where the tender lived — nothing is sent there.

## 9. Pre-flight checklist before any invoice leaves (all from the row; no lookup needed)
1. `email_check` starts with "confirmed" or "cross" (else the channel is a lead, not a channel). 2. `email_deliverability` says the domain publishes a mail
server. 3. `sensitivity_flag` = no. 4. `vendor_registry_warning` blank (a dissolved vendor cannot bill). 5. `po_required_as_published` yes → PO number in
hand. 6. `invoicing_requirements` obeyed literally (format, one per e-mail, subject line, attachments). 7. Amount ≥ $500 → vendor GST/HST number, buyer
name, terms, description all present (§2 legal minimum). 8. Québec buyer → French + TVQ. 9. Buyer outside Canada → no Canadian tax, their currency unless
the contract says otherwise. 10. `evidence_age_days` > 60 → one courtesy confirmation of the mailbox before a first invoice.

## 10. The e-mail that carries the invoice (what the buyers' own pages ask for, counted over the rows that publish requirements)
PDF required or preferred on 479 rows, "PO number on the invoice" on 284, an attachment size limit on 94 (10–30 MB), a vendor-setup / EFT form on 77,
"one invoice per e-mail" on 27, a prescribed subject line on 11 (typical: "vendor name, PO number, contract number, invoice number"), no paper on 9.
So the default that satisfies every rule at once: one PDF per e-mail (invoice + backup in the same PDF, under 10 MB), nothing in the body that is not
also on the invoice, subject `<Vendor legal name> — Invoice <no.> — PO <no.> — <contract / tender no.>` (French for Québec: `<Fournisseur> — Facture
<no> — Bon de commande <no> — Contrat <no>`), from the vendor's own AR mailbox (`vendor_billing_ar_email`) so replies land with the vendor, and the
buyer's `invoicing_requirements` applied on top where they say something stricter. For `routed` rows the subject starts with "Accounts Payable /
Comptes payables:" so the general inbox forwards it unopened. Never attach a W-9 (Canadian vendor) — a W-8BEN-E goes only when the US buyer asks.
