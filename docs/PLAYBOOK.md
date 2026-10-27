# PLAYBOOK — what works (updated by Claude as the team learns)

## A. Where invoicing / AP contacts are published, by organisation type
- **Canadian federal departments**
  - PSPC "Direct deposit for government suppliers" page: a table of each department's *supplier-payment* mailbox (label it `supplier_payment`).
  - The invoicing clause in the department's free CanadaBuys solicitation documents (often names the invoice mailbox).
  - Department "Invoicing instructions" pages (e.g. SSC, NRCan).
- **Québec ministries and agencies**
  - "Fournisseurs" / "Faire affaire avec nous" pages.
  - "Exigences de facturation" PDFs.
  - Supplier registration or direct-deposit forms (they usually name the comptes à payer mailbox).
- **CISSS / CIUSSS / Santé Québec establishments**
  - The "Fournisseurs" section.
  - The PDF "Exigences de facturation" or "Guide du fournisseur".
  - Often one central comptes-à-payer mailbox per establishment.
- **Québec cities and MRCs**
  - "Fournisseurs", "Faire affaire avec la Ville", "Exigences de facturation" PDF (Ville de Montréal publishes one).
  - Otherwise the trésorerie / finances page.
- **Centres de services scolaires, cégeps, universities**
  - "Services des ressources financières" / "Finance — Accounts Payable" pages.
  - Supplier forms; purchase-order terms.
- **Provinces**
  - Some have one central AP mailbox: e.g. Newfoundland and Labrador `gnlinvoices@gov.nl.ca`; NWT `financial_sharedservices@gov.nt.ca`.
  - Others use an e-invoicing portal (e.g. Alberta: 1GX / SAP Ariba).
  - Ministries then inherit that central contact.
- **Municipalities elsewhere in Canada**
  - "Accounts Payable", "Vendor information", "Doing business with the City".
  - "Purchase order terms and conditions" PDF.
  - Example: City of Toronto divisions all use `apinvoice@toronto.ca`.
- **US federal** — Treasury IPP (ipp.gov) for most agencies; DoD WAWF/PIEE; VA Tungsten. Record these as `invoice_portal_url`.
- **US states and cities** — "Accounts Payable" / "Vendor Payments" pages, vendor self-service portals.

## B. Query bank
- **French:**
  - "<organisme>" facturation fournisseurs;
  - "<organisme>" comptes à payer courriel;
  - "<organisme>" exigences de facturation;
  - "<organisme>" guide du fournisseur;
  - "<organisme>" conditions générales d'achat;
  - "<organisme>" dépôt direct fournisseur formulaire;
  - site:<domaine> facture;
  - site:<domaine> filetype:pdf facturation.
- **English:**
  - "<org>" accounts payable email;
  - "<org>" submit invoices;
  - "<org>" invoice submission;
  - "<org>" vendor guide invoice;
  - "<org>" purchase order terms and conditions invoice;
  - "<org>" doing business with us;
  - site:<domain> invoice;
  - site:<domain> filetype:pdf "accounts payable".

## C. Evidence standard (see `DATA/verified_ap_examples.csv` for 25 real accepted findings)
- **GOOD:**
  - `ap_email=comptesapayer@ville.example.qc.ca`;
  - `evidence_url` = the city's "Fournisseurs" page;
  - quote: "Les factures doivent être transmises à comptesapayer@ville.example.qc.ca en indiquant le numéro de bon de commande".
- **GOOD:** `invoice_portal_url=https://www.ipp.gov/`, with evidence that the agency appears on IPP's agency list.
- **BAD:**
  - an address you inferred ("they probably use ap@domain");
  - a named employee's mailbox;
  - an e-mail from a third-party directory page listing *another* organisation's contacts (the e-mail domain must belong to the organisation);
  - a page you didn't open;
  - Cloudflare-hidden e-mails (don't decode them).
- **Label precisely:**
  - `invoice_submission` (where invoices are sent) > `accounts_payable` > `supplier_payment` (direct deposit / payment questions) > `procurement` > `general`.
  - A department's direct-deposit contact is `supplier_payment`, not `invoice_submission`.
- **Units vs parent:** use the parent's central AP for a unit only when the parent's page says so (`applies_to=parent_central_ap`).

## D. Vendor website verification
- Accept a site only if it shows the vendor's name **and** a location match (street, city, postal code, or registry number).
- Same-name companies are common ("Apex Construction" exists in many cities). If unsure, mark `ambiguous`.
- Contacts must be on the vendor's own domain, and role mailboxes only (info@, sales@, accounting@, billing@, ar@, admin@).
- Main phone = the number on the contact page / footer.

## E. Judging "ongoing" (QA audit)
- `high`: the source states an end date ≥ 2026-10-25.
- `medium`: an end computed from a stated term (e.g. awarded 2025-03-01 + "36 months").
- `low` / `very_low`: Quebec records where the only evidence is that no closure notice was published — **be skeptical**; Claude is re-checking these with the SEAO API.
- `unknown`: award published, no end information.
- Say whether the page supports the status, and quote the dates you saw.

## F. Pitfalls we hit
- In US data, the state "CA" is California, not Canada.
- At the IDB, Canada's code is "CD", while "CA" means Central America.
- Organisations change websites. When a site fails, search for the new hostname: e.g. New Brunswick's NBON moved to nbon-rpanb.gnb.ca; Manitoba open data is at geoportal.gov.mb.ca.
- Many big Québec bodies publish no AP mailbox at all. Record `not_published` with your queries — that is useful information.


## Patterns learned (gemini)

## Patterns learned (chatgpt)
- Municipal site migrations can leave indexed /en/... PDFs at 404. Follow the current official purchasing page to its linked Govstack/CDN asset; this recovered Durham's supplier guide and Waterloo's current PO terms. Never adopt a mailbox solely from cached search text.
- PDF extraction can split real addresses with artificial spaces (Timmins accounts.payable; WRDSB finance-ap). Render the actual PDF and copy the visible address. This differs from decoding protected/obfuscated HTML email, which was not done.
- A supplier portal is not automatically an invoice portal: Saskatchewan GEM explicitly keeps invoices on the existing process; York provides the construction invoice-upload URL privately at contract start. Preserve those limitations.
- Canada Post contingency notices can publish supplier invoice and EFT roles (Oxford County and Thunder Bay), but retain the notice date and event scope. NLHS Central Regional Office AP phone is unit-specific; do not generalize legacy Eastern EFT or provincial GNL AP to all NLHS zones.

- Vermont: the Treasurer payment portal is for payment advices/inquiries, while current VTBuys supplier guidance covers registration and W9/ACH changes. Do not turn planned invoice-submission features in the prelaunch2023 FAQ into a confirmed current invoice portal. Contract-specific VTrans invoice mailboxes keep their program scope; the still-linked02/22 ACH form is flagged unclear alongside newer electronic guidance.
- NL Hydro: the February2025 Supply Chain Supplier Information Manual specifies HydroAPInvoices@nlh.nl.ca (PDF invoices only) and HydroAPInquiries@nlh.nl.ca (inquiries/statements). Older2021 Nalcor addresses remain hosted but differ from current instructions; retain source age and possible supersession rather than treating them as interchangeable.
- District of North Vancouver: the new site can return only a JavaScript shell to text fetches. Its rendered2025 Canada Post notice links a July30 2025 vendor/EFT form with ap@dnv.org and604-990-2305; this confirms supplier setup, not general invoice intake. Utility billing contacts on the same notice are receivables.
- StCatharines: the current Vendor and purchasing opportunities page links July2024 PO terms on its Govstack CDN after the old indexed PDF404s. That document gives invoice mailbox/postal route and GC27 requirements; suppliers@stcatharines.ca instead handles supplier registration/EFT updates.

- A public EFT/bank-authorization PDF can independently publish a role mailbox even when the page email is protected: HWCDSB prints eft@hwcdsb.ca in its linked bank-deposit form. Record supplier-payment setup purpose; never treat it as invoice intake or decode protected HTML.
- HealthPRO's pharmacy standard terms explicitly send invoices to participating members, and its FAQ says members buy directly. Group-contracting identity does not make the intermediary the payer. Likewise, consultant/lab invoice contacts embedded in municipal reports (for example WSP in an Orillia report) do not belong to the municipality.
- Inspect the response type and final page, not just HTTP200: former Halton Hills and Grand Erie PDF links now land on soft404 HTML. Do not adopt indexed emails or invoice rules from those dead documents.
- HRCE RFP4276 (September2025 snow/ice maintenance) requires email-only invoices; older RFP4000 permits paper. Keep each contract's date/scope and avoid generalizing older postal routes over newer contract instructions.
- Alberta1GX publicly confirms SAPBusinessNetwork handles orders/invoices/payments across departments, but its quick-start flow begins from the ProcessOrder link in the supplier's PO email. The public SupplierInformationPortal is documentation, not the transaction portal; record supplier-help phone separately and leave an unverified invoice URL blank.

- BC program URL migrations: when an old Autism service-provider URL404s, follow actual links from the official parent landing page. The current provider page is under support-needs/pairs and publishes distinct Disability Benefit invoice, Autism Funding invoice, general-help and older portal-access roles. Preserve each section's purpose, prefix and program scope; MCF and CFD addresses on the same page are not automatically aliases.
- City website migrations can leave indexed Treasury text unavailable on current Finance pages. Follow current navigation to purchasing and its linked by-law/construction documents; a general footer address or customer-service phone is not an AP destination.

- Current WCB Nova Scotia pages supersede legacy billing search results: 2026 Work-Connected Recovery network invoices go to Lifemark via ACMS, while non-network invoices use fax; direct physician non-MSI invoices use Dartmouth200-137VentureRun. Current physician contacts expressly reject emailed invoices; their role mailboxes are support, not submission. Keep the service/date scope.
- Follow the actual current PO-term link after a Govstack migration. RDCO now links August2026 v5f terms while its indexed2022 document404s. DCDSB currently links a30-day document but another accessible official PDF says45; retain the conflict and actual applicability rather than choosing by search rank.
- Embedded laboratory chain-of-custody forms distinguish REPORT INFORMATION from INVOICE INFORMATION. A consultant may receive the report while the public buyer pays the invoice. Verify the invoice Company block visually when text extraction is empty, retain only organizational roles, and preserve the specific order/school scope instead of assuming whole-organization AP.
- A shared bidsandtenders account or cooperative purchasing membership does not establish shared accounts payable. RDCO/WestKelowna bidding access, RMA member job postings and separate county/township finance contacts need entity-specific payment evidence.


- Mohawk Medbuy currently publishes Basware invoice mailboxes and separate AP/onboarding inquiry mailboxes, alongside phased SAP Business Network invitations. Keep onboarding/confirmation conditions and historical/current route uncertainty; CAPsource/MEALsource are MMC services, while member hospital invoice destinations remain hospital-specific. The general vendor contract portal is not proven invoice upload.
- Supplier EFT instructions can appear inside a page otherwise devoted to tax forms (Bracebridge). Read the section: the vendor AP form is separate from customer preauthorized tax payments. An EFT form return address still does not establish an invoice mailing address.
- Sault Ste. Marie explicitly keeps Police Department supplier invoices separate from City invoice intake. Payroll service coverage is not evidence of supplier AP coverage.
- AVRCE migrated old document-library/page links to current /download/ links. Follow the live Procurement page for its current General Terms; do not copy AP email/phone from stale indexed forms that now404. Historical school-board identity/payment continuity can remain unclear.
- Scanned BC FOI contracts can publish real organizational billing contacts (STADD Alliance/Vendor Management Office), but retain the2018-2019 contract scope and status unclear. A PO InvoiceTo block and vendor order BillTo block can even give different floors; retain that distinction. Current PPMB health-professional invoice instructions are a separate program, not ministry-wide AP.


- Saskatchewan Social Services voucher invoices go to the address stamped on the requisition; the December2025 public Vendor Direct Deposit PDF independently publishes an IncomeAssistance EFT role even though the HTML email is protected. Keep voucher/IncomeAssistance scope and first-enrollment invoice condition; no protected-email decoding needed.
- EDC English/French ForSuppliers pages publish distinct AccountsPayable and Comptescrediteurs invoice roles with the same AP postal/fax route. Keep both actual mailboxes; a supplier-registration form is not invoice upload, and the pages historical2010 provincial tax-rate paragraph is not current tax guidance.
- BCs public staff directory now says employee and organizational information require government credentials. Treat that as an access restriction even with HTTP200; do not copy stale indexed staff details or open the internal login route.

- French navigation may expose supplier pages that English link filters miss: CSAP’s Fournisseurs page publishes its payables role and a finance-office emergency AP phone. Read actual supplier links before concluding a French body has no published AP route.
- CBC/Radio-Canada’s browser-rendered Already a Supplier / Déjà fournisseur payment accordions publish distinct English and French invoice mailboxes and a separate EFT onboarding role. Read both languages, keep roles separate, and distinguish the public InvoiceInfo upload form from tender registration. A blank JavaScript shell is not proof that the organization publishes no contacts.
- Windsor Essex CHC distinguishes vendors without VendorCafé registration (email invoices) from invited/registered vendors (portal submission). The public page sends registration invitations by email and does not expose a transaction URL; do not substitute the bids&tenders URL or guess a generic portal address.
- Supplier terms can differ between goods and services: East Hants shares an invoice mailbox but service terms add monthly billing and a WCB clearance letter. Preserve those conditions and do not turn a Payables Administrator addressee into an unverified fixed invoice postal address.
- Quote the literal source when a public AP button contains a plain unprotected mailbox: Camrose publishes a data-emailAddress attribute. HTML parsers may reorder attributes when serializing; retain the actual source substring, and never decode protected addresses.

- New Westminster currently links standalone v4 Standard Terms of Purchase; those independently confirm the invoice postal destination seen in old RFPs. Pair current terms with the alphabetical city-contact PDF for the supplier invoice/payment inquiry phone, and exclude MyCity/customer e-billing.
- SARM Member Purchasing advertises net30 and batched invoices with one payment source, but program pages distinguish SARM-billed purchases from suppliers that invoice members directly. Neither tender-intermediary identity nor an outgoing member invoice proves the intake route for every municipal contract.

- Public provider-specific supplier pages can authorize outsourced processor/payment-enrollment mailboxes (VCU TrustFlow/Paymode/BankOfAmerica). Retain the official authorizing URL and each mailbox purpose; enrollment and portal help are separate from invoice intake. Conditional postal instructions still follow the PO/department.
- Re-open the current linked hospital invoice guide before using an old indexed PDF. SJHH currently links a March2024 SmartPDF guide with a new Basware mailbox and no-registration workflow, superseding its2017 registered-portal address; MMC inquiry and patient-information postal routes remain separate.
- Protected HTML need not be decoded when a separate public PDF plainly publishes the role: BCLDB linked invoice sample/definitions and supplier direct-deposit form expose distinct invoice and AP roles. Dummy vendor contacts in a sample are not buyer contacts. Keep the currentFAQ versus olderPDF bill-to conflict.
- Shared purchasing can retain separate AP: GreyBruce joint tender documents explicitly name each boards invoice mailbox/postal route. SouthShore/TriCounty sharedfinance alone does not resolve a historical combinedbuyer label or prove one centres EFT role covers both.
- Current WBG corporate invoice guidance covers member purchases, including IBRD/IFC defined in its terms, not borrower procurement. AskAccounting handles VendorKiosk access; actual invoice destinations come from the PO/contract. VendorManagementPortal onboarding and old WBGeProcure/VKP banking paths coexist; two public pages differ by one day on the April2026 cutoff, so retain the conflict and do not invent a uniform cutover.

- A current successor financial statement can resolve legacy payer identity: BuildNS2026 notes expressly transfer formerNSLands/DevelopNS liabilities. That supports successor scope, but a procurement mailbox still does not prove the invoice intake route, and current templates do not automatically override legacy contracts.
- A current municipal host may retain PDFs for another entity: ShelburneNS search results include DistrictShelburne MDS tenders while the current task is TownShelburne. Verify the actual purchaser inside each document; do not assign the district’s named contact or postal destination to the town. Follow current2026 town tenders for contract-specific invoicing conditions.

## Patterns learned (jules)

## Patterns learned (codex)

## Patterns learned (claude)

### 2026-10-27 — chatgpt buyer AP batch05 patterns
- An HTTP202 page redirecting to `/.well-known/sgcaptcha/` and HTTP200 Radware “Verifying your browser” are access blocks even when a basic status checker labels them successful; stop without trying alternative access to that resource.
- Public current-linked supplier PDFs can independently publish literal role mailboxes even when contact-page emails are protected. Preserve the PDF quote, document version and exact scope. An outgoing remittance sender, bank-setup mailbox or supplier-registration contact is not automatically an invoice inbox.
- Los Angeles GSD Supply Services explicitly accepts City FMS materials/goods/supplies invoices at its central mailbox, postal route and LAVSS. RAMP handles bids/compliance registration. Preserve the goods-only scope for department buyers; Public Works service-contract payment terms have a separate clock. A hosted cooperative-purchasing attachment can contain another government’s AP address: verify the underlying payer. Seven-digit AP directory voice numbers should remain as published without an inferred area code.
- French and English currently-linked terms may list different legal-notice roles (Marine Atlantic). Record their legal scope and source age; a new upload folder date does not establish a revised policy, and Corporate Counsel is not a demonstrated AP route.
