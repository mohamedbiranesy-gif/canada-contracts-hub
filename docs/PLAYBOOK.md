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

## Patterns learned (jules)

## Patterns learned (codex)

## Patterns learned (claude)
