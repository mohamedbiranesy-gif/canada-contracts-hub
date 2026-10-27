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

- Research follow-up: after a website migration, follow the live vendor page to current PDF links instead of reusing indexed retired paths (Ottawa Hospital). A local Python CA-store failure can be checked with the system-trust HTTP client while certificate verification stays enabled; access-denied/CAPTCHA responses still stop research.
- PDF text engines may insert artificial intra-word spaces. Independent extraction from the same cached public PDF can confirm a literal organizational role (Mesa Transportation); retain the unmodified body, secondary text and contract dates. Do not construct an address from a partial extraction.

### 2026-10-27 — chatgpt buyer AP batch06 research patterns
- BC Government Directory now displays a public notice that organizational/employee-directory access requires government credentials. Stale indexed phones, addresses or branch contacts do not restore public access; preserve the restriction and use separately public invoice policy only with its actual scope.
- Invoice samples need visual inspection: Muskoka prints a red D2 field marker immediately before the sample email, which text extraction concatenates into the address. Preserve the literal quote, distinguish the marker, and keep illustrative/project-specific destinations unclear until current intake is confirmed.
- Current public vendor instructions can conflict with office contact footers. JMU explicitly directs vendor invoices to ZIP22801 while its AP office/footer gives22807 for the same street/MSC. Retain both cited values and the conflict; do not silently correct one using the other.
- Follow current policy links and compare versions with indexed results. Zorra currently links an11-page2019-effective purchasing policy while search also exposes a13-page March2025 copy. SD43 migrated old administrative-procedure URLs to404 but currently links a public December2020 POterms PDF. Record exact versions and avoid promoting dead-PDF snippets.
- A vendor EFT form supplies enrollment routes, not automatically invoice intake or invoice postal destinations. Canmore publishes a current EFT mailbox/form and older project-specific invoice instructions to the same role; retain the project number/payment clock separately. Read scanned purchasing policies visually when text extraction is empty; Canmore FIN-006 July8,2025 is8 scanned pages.
- Quebec vendor contact research (`gemini_vendor_contacts_batch01`): Many mid-sized Quebec construction, civil engineering, and IT consulting firms publish general role mailboxes (`info@`, `contact@`, `ventes@`, `sales@`, `administration@`) on their `/contact` or `/nous-joindre` pages, whereas national subsidiaries (Waste Connections / Enviro Connexions, WM Québec, Lumen / Sonepar, Chemtrade, Protection Incendie Troy) use web forms (`status=website_only`).
- Numbered Quebec companies (e.g., `9083-0126 QUÉBEC INC.`, `9124-4277 QUÉBEC INC.`, `178001 CANADA INC.`) often operate under trade names (`Creusage R.L.`, `Transport Noël et fils`, `Groupe Nicky`); pairing the numbered legal name or postal code with RBQ/municipal directories (`portailconstructo.com`, municipal business directories) resolves the trade name, official site, and general contact details.
- A public DOCX can independently publish an AP role while the HTML contact email is protected (Rocky View Schools AF5106-C, October2025). Read the literal document text, retain the untouched file and version, and distinguish EFT enrollment from invoice intake. Do not decode the protected HTML.
- Current-linked bilingual EFT forms may publish different AP phone numbers (Saint John English5066582951/French5066582923). Keep the conflict and language labels; an invoice postal route needs separate invoice-specific evidence, even if its address matches the EFT office.
- Shared-services hospital invoice lists identify separate member payers. Mohawk Medbuy's current member-hospital PDF mailboxes and sensitive-invoice addresses do not establish its own corporate AP route after the Plexxus amalgamation. Member/staff Basware technical support is not supplier invoice intake.
- Direct website mailboxes can have different scope from the buyer name: Eastern Health's older EFT form is still linked from its September2026-updated fertility subsidy page. Preserve the current link and form date, limit the role to demonstrated payment-setup use, and avoid extending it across all NL Health Services zones. Client cheque enquiry numbers are not vendor AP numbers.
- BC Parks' general park-information mailbox and reservation call centre are not AP contacts. General ministry invoice-content policy can be retained for composite historical branch names while exact paying unit and invoice destination stay unclear.

### 2026-10-27 — chatgpt buyer AP batch07 checkpoint patterns
- Live staff directories override stale search snippets. Port Hawkesbury's search index labels phone7898 Accounts Payable, while the opened current directory identifies that staff member as Recreation/Active Living; current AP is phone7896. Never promote the indexed role without opening its page.
- Efficiency Manitoba's Supplier Network page links `suppliers@efficiencyMB.ca` specifically for direct-deposit enrollment by suppliers/vendors/contractors receiving payments. Its MERX procurement page and program-registration portal have different purposes. Literal public mailto attributes are evidence; generic form-library CAPTCHA code on a page without a form or challenge is not itself an access block.
- WCB Alberta explicitly supports invoice submission/payment tracking at its Ivalua supplier portal for non-claim suppliers and excludes healthcare providers. Its corporate AP role and separate Claims Authorization & Processing EFT role must retain their distinct scopes; employer premium remittance postal addresses are receivables.
- Penetanguishene's current Finance page makes EFT mandatory from2024, while its currently linked vendor form still describes EFT as an option. Preserve the discrepancy and use the form's literal payment-enrollment mailbox; form-header general phone/address does not establish AP or invoice-mail scope.
- Legacy municipal domains can fail certificate hostname checks while an independently identified current official domain works (District Digby moved research from digbydistrict.ca to digbymun.ca). Keep certificate verification enabled, confirm the new entity/site independently, and distinguish District/Municipality of Digby from Town of Digby. Actual403/bot blocks still end access attempts.
- Federal financial support agreements can be time-limited. ECCC2024–25 statements disclose CWA finance/procurement support under MOU and an administration transition throughApril1,2026; this is not evidence that an ECCC supplier mailbox receives CWA invoices inOctober2026. Preserve unresolved current payer scope.
- CHEO's migrated site leaves its indexed legacy POterms PDF at404. Follow current Reporting & Statistics to the file named `purchase-order-terms-and-conditions-20260910.pdf`, which explicitly directs vendor invoices to `payables@cheo.on.ca`. Current terms retain PO-number/net30 requirements; its Privacy Office role/phone and legal notices are not AP contacts.
- Public Laserfiche DocView can initially show only Loading/No preview while its browser viewer exposes the linked electronic PDF. Read the public viewer and use its displayed document URL; do not infer or access hidden/private endpoints. Chester POterms specify PO# on invoices and net30 subject to verification; the separate vendor EFT form is enrollment only and requires business/remittance details, bank evidence and authorization. Read without completing/submitting it.
- A scanned-looking or text-collapsed policy can yield clean literal text with an independent public-PDF parser. Olds College F22 pypdf text collapsed inter-word spaces while PyMuPDF preserved them. Keep original PDF bytes and both extractions; current policy index still links the2015 procedure, so preserve source age instead of treating its processing schedule as a newly confirmed service promise.
- Town and District/Municipality of Shelburne are separate buyers. A District2024 covered-bin RFP hosted by the Town's government site explicitly gives a District invoice postal route; retain the tender scope/date and omit the named-person mailbox. Current District AP page separately publishes vendor EFT enrollment at its Finance role; setup mailing address alone is not general invoice-mail evidence.
- Do not silently infer province from adjacent generic Executive Council rows. NL OCIO/Intergovernmental Affairs have plausible official name matches, while Saskatchewan Communications Services is separately identified by its own current registration material. Preserve unresolved jurisdiction as unclear and keep NL central invoice/AP candidates in notes until contract or PO Bill To confirms coverage. SaskBuilds Corporation and Ministry of SaskBuilds and Procurement are distinct entities in the official ministry description.

- Bell moved supplier documents from old /-/media URLs (404) to current-linked website-files CDN. March2026 terms distinguish BTI invoices (APBell@textron.com / PO77090) and BTCL (APBellMirabel@textron.com / PO77036), both Textron shared finance FortWorth; never mix subsidiary scope. PayUponReceipt exception and small-business net30 differ from standard net60. Supplier-login link alone does not prove invoice upload.
- Current ATB VendorResources page uses Ivalua for contract/vendor management and vendor-requested onboarding. buyers@atb.com is procurement and ivaluasupport@atb.com technical support; automated no-reply sender is not a contact. Supplier travel April2026 policy has45-day invoice deadline/receipts; retail billpay products are not corporateAP.
- BCWS VendorPortal public page explicitly supports contracts/resources/electronic daily time reports. Capture public loginhref and supplier-support roles without entering BCeID; do not infer general invoice upload. Body BCWS.CWSContracts and footer CWSContracts spellings differ; retain exact variants. Repo personal-email heuristic rejects ResourceManager/CWSContracts dotted roles; preserve evidence pending integrator correction.
- CHRC public contact/financialstatement pages place substantial content outside the HTML main element; extract full visible HTML when main contains only the header. Federal supplier DDdirectory prints contractingandpurchasing./contratsetacquisitions@chrc-ccdp.gc.ca as one mailto; never truncate at slash into a guessed suffix. Current validator cannot store slashlocals, so retain exact evidence/notes for review.
- Canada GoodSamaritan buyer has taskwebsite good-sam.com (USorganization); independently published Canadian gss.org contact gives gssap@gss.org under Invoices and Billing. Keep source-entity ambiguity when taskcontract context is missing. A Python CA-chain failure may be retried using normal system-trust curl with TLSverification enabled; never disablecertificatechecks.
- Current NorthDumfries and PerthSouth directories identify APclerks with dedicatedextensions but individualmailboxes; retain phones and exclude those emails. NewMinas lists both namedfinanceofficer email and accountspayable role on same entry: crop evidence to avoid retaining personalmailbox. DeSalaberry EnglishStaff and FrenchPersonnel confirm accounts@ as APclerk, while finance@ is broader FinancialOfficer.
- Current LondonPublicLibrary site is lpl.ca; old knownwebsite may timeout. AboutLibrary links2025standardterms and bidportal; contactform has actualreCAPTCHA. Terms mention conditionalnonresidentwithholding, not generalinvoiceemail. Flagstaff old domain redirectsflagstaff.ca and FinancialRecords paymentinstructions concern customerspayingCounty, not supplierAP.

- University of Manitoba Finance/Suppliers has separate invoice intake (SPSInvoices@umanitoba.ca, a no-reply processing inbox), backup invoice/payment help (Ask-SPS@umanitoba.ca), Ariba invoice assistance (supplier.enablement@umanitoba.ca), and Canadian EFT enrollment (EFTPayments@umanitoba.ca in its linked PDF). A valid PO or contract number is mandatory; send invoices once by email OR mail, prefer PDF attachment named company+invoice#. Ask-SPS is a published role rejected by the current personal-email heuristic; preserve evidence for review. Purchasing phone is explicitly for non-invoice matters.
- PHSA AP landing links January30,2026 invoice/statement and May14,2026 inquiry/escalation PDF tables. PHSA corporate invoice=PHSA_Invoices@pdf.basware.com, Burnaby1795Willingdon; statements/inquiries=PHSAAccountsPayable@phsa.ca,6042979267. Langley inventory invoice/statements=PHSAInventory_APInvoices@hssbc.ca, POBox4001StationLocation1; inquiry=FHA_APInquiries@phsa.ca,6044551304x741487. Visually check table columns; never substitute another health authority's row. Current invoice sheet permits physical or PDF email attachments despite older generic guideline wording to mail.
- MMC corporate buyer is explicitly listed on its AP contacts page as MSS@pdf.basware.com and mssap@mohawkmedbuy.ca, phone2893910151; these differ from member hospitals. Sensitive-invoice-only corporate postal row has the apparent typo “Mohawk Mohawk Corporation”; preserve that uncertainty when retaining POBox20010Thistletown/900AlbionRoadEtobicoke. Never put personal/health information through the electronic invoice process.
- ODU vendor Invoice Requirements/Payments directs central invoices to invoice@odu.edu and FinanceOffice/RollinsHallRoom2005/NorfolkVA23529-0047; Facilities work ALSO copies facilitiesinv@odu.edu. accountspayable@odu.edu on Vendor Payment Methods is Virtual Payables enrollment. Paymode-X public enrollment link is a payment service, not invoice upload. Missing proper-invoice elements are returned and corrected receipt starts a new due date; contract terms control net30 default.
- A current 2026-hosted BC FIN312 direct-deposit PDF opens with revision2025/10/28 even when search snippets call it2018. Use opened bytes, retain retrieval date and distinguish EFT application mailing routes from supplier invoice mailing. Its EnergyMinesPetroleumResources/CSNR row still uses legacy ministry names; do not resolve current organizational payer solely from that table.
- NorthBattleford2024–2026 sidewalk RFP has role AP invoice email plus named-manager copy and a subject line saying2023. Retain the literal year conflict, project scope and role instruction; exclude named-person address. MetroNet's public French contact lists MetroRichelieu supporting-document postal/fax routes by supplier category; these are not automatically invoice intake, and fax numbers are not AP phone numbers.
