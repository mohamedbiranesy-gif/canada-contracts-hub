# The downstream agent's 150 questions (2026-11-06) — answers, what runs now, what cannot be done honestly

Written 2026-11-06 22:00 EST with the owner at 2% credits: everything marked **RUNS** is in motion without any Claude credits (Mac
engines, GitHub Actions, the Gemini app); **CODE** landed in rank.py / the workflow tonight and appears from the next 3-hourly build;
**RESET** waits for the search agents (wake-ups at 00:20 / 01:00 on Nov 8); **NO** = not possible under the quality rules (no
fabrication, evidence or nothing, no CAPTCHA/ToS circumvention) — with the reason. Fill rates quoted by the question are from the
11-04/11-06 Gold package.

## A — identifiers
- A1.1/A1.2/A1.3 **CODE**: `most_recent_record_reference_any_vendor` + `records_in_contract_dataset` on every row; lead rows (P06/P06T/P07/P08) get the organisation's latest dataset reference when the same organisation (website domain / exact name) has records; `invoice_reference_hint` says so. A1.4 (P10, vendor-site links): the linked page is a client logo/listing, it carries no reference — **NO** (would be invented). A1.5 synthetic references for P13: **NO** — a made-up customer number is fabrication; the rows say "no identifier".
- A2.1 **RUNS**: `contracts_of_delivered_buyers/CONTRACTS.md` counts PO numbers per delivered buyer each build (11,637 PO records; Gold cap raised to 5,000 records/buyer, D7/F1.3). A2.2/A2.3/G1.x new PO-ledger and council-agenda sources: registered in `coord/source_registry.csv` for Jules/Codex (pipelines, not credit-free from here; Codex is out). A2.4: FIR Schedule 02 carries no PO numbers (auditor fees only). A2.5: `pd_procurement_id` is PSPC's procurement id (the contract/PO reference the department quotes); coverage is what Proactive Disclosure publishes (29,616 records) — complete for the records in the pool, not every federal PO.
- A3.1–A3.3 **partly CODE/NO**: the references come from the records themselves; a "second-pass harvest" of the same sources adds nothing new; Peppol carries no award ids (A3.3 **NO**). A3.4 **CODE** (since 11-06): the classifier labels every key; the same number under two keys is listed once per key, deliberately (verbatim).
- A4.1–A4.3 **RESET/NO**: buyer vendor ids appear only where a source publishes them (eVA, USAspending recipient ids …); supplier portals need a vendor login — not scraped.
- A5.1 vendor_ids_in_record: 0% on Gold because Canadian sources publish none (DUNS/UEI are US). A5.2 **CODE** (D14): UNSPSC/GSIN/NAICS/economic-object codes from the record's own commodity block; text→UNSPSC machine mapping is inference — **NO**. A5.3: org codes only where the source gives them.
- A6.1/A6.2: amendments are separate records in the sources; `amendment_or_modification` shows the ones a record carries; per-row modification history **RESET** (an export of all modifications per contract id from the release — cheap code later).
- A7.1 **CODE**: `other_relationship_sources` (D12). A7.2 **CODE**: `all_references_with_this_vendor` now carries date and value per reference; plus F3 pair columns below.

## B — vendor identity
- B1.1 **NO/partly**: BN9 is a CRA number; provincial registries do not publish it (REQ gives NEQ, not BN). Coverage comes from Corporations Canada (bulk, done), the CRA charities list (done) and the vendor's own printed GST number (**RUNS**: org_extras round 4 + a full vendor-domain pass launched tonight, see J1). ON OnBis / AB / SK / MB / NS registries: search-only, no bulk file, AB paid — **NO** for automation. B1.2 **NO** (CRA registry is CAPTCHA-protected; rule 6). B1.3: Corporations Canada's bulk file carries the BN for federal corporations — already used (`vendor_bn_source`).
- B2.1 **RUNS**: vendor-site addresses via org_contacts (round 4 + the all-vendor pass). B2.2 SEDAR+ **NO** (blocks automated readers).
- B3.1 **done** in the merge (REQ bulk match by legal name). B3.2 **NO**: the QST number is not NEQ+TQ0001 (it is a Revenu Québec number: 10 digits + TQ0001); never derived; captured only when printed (`vendor_qst_as_published`).
- B4.1–B4.3 **RUNS**: the all-vendor pass (org_contacts + org_extras: role mailboxes, phone, address, legal name, logo via og:image/logo image, printed BN/NEQ/QST). J1.2 ceiling: only vendors with a known website can be read (see the build log for the count).
- B5.1 **RUNS** (legal name vs record name → `vendor_trading_name`). B6.1/B6.2 **RESET** (registry re-match heuristics; status refresh is in the merge pipeline, not daily). B7.1: `vendor_bn_source` values are "Corporations Canada", "CRA charities list", "printed on the vendor's site" (with URL), "registry match (REQ)".

## C — buyer facts
- C1.1 **RUNS** (round 4 legal names) + **RESET** (municipal directories). C1.2 **RUNS** (`ap_terms` captures the buyer's own GST number printed on AP pages; 11-06: rare). C1.3 **CODE**: `buyer_bn_program` labels RR (charity) vs RT (GST/HST) when the printed number says so.
- C2.1 **RUNS** (round 4: 22,764 new domains). C2.2 **NO** honestly from one crawl (city-hall vs service address cannot be told apart without reading); the JSON-LD/contact address is what is used.
- C3.1 **RUNS** (round 4 logos). C4.1 **CODE**: `buyer_type` fallback reduced with domain/keyword rules (no NLP guessing). C5.1 **CODE**: `facts_provenance_json` — a JSON object {column: source note} beside the free text.

## D — AP specifics
- D1.1/D1.2 **RUNS** (ap_terms: printed AP contact next to the mailbox, conservative rule) + lanes (Gemini batches 44–55) + **RESET** (staff-directory agents). Honest ceiling: most buyers publish a mailbox, not a person.
- D2.1 **RUNS** (ap_terms pass 1: ~3,600 AP/finance/purchasing pages; pass 2: general pages). D3.1 **RESET**. D3.2 **CODE**: `invoicing_requirements_structured` (JSON: terms, po_required, portal, format, phone, address — only what was found).
- D4.1 **RUNS** (ap_terms) + **RESET**. D4.2 **CODE**: `payment_terms_default_policy` for federal buyers = "30 days from receipt of a valid invoice (Treasury Board Directive on Payments)" — labelled a policy default, never written into `payment_terms_as_published` (the 20-business-day figure in the question is not the policy).
- D5.1 **CODE/RUNS** (PO_REQ regex over requirements + evidence + ap_terms "no PO no pay").
- D6.1/D6.2 **CODE**: `invoice_portal_url` is now the bare URL/name, `invoice_portal_kind` = actionable supplier portal / informational page, `invoice_portal_note` holds the sentence.
- D7.1/D7.2 **CODE** (D15): `template_language` fr for every Québec buyer, en-fr for federal / NB bodies.

## E — contract metadata
- E1.1 **NO** (Public Accounts give totals per vendor, not per contract; mixing them would mislabel values). E1.2 **CODE**: `currency` defaults to the source's currency convention, labelled "(default: <source> publishes in CAD)".
- E2.1/E2.2 **NO** — derived start/end dates are fabrication; the rows keep `ongoing_no_end_date` semantics. E3.1 **NO** (same record). E3.2 **CODE** (clean sentence cut). E4.1 **NO** (UNSPSC from title text is guessing; codes only from the record, D14). E4.2 **CODE**: `instrument_type_normalized` (contract / standing offer / supply arrangement / purchase order / blanket order / grant or contribution / other, from the source wording).

## F — contracts subfolder and aggregates
- F1.1/F1.2: the subfolder lists every delivered organisation that has dataset records (tiers A/B/L/C/D/F); P06–P13 rows have no dataset records by definition — their relationship evidence is on the row. F1.3 **CODE** (Gold 5,000).
- F2.1 **CODE**: `typical_contract_value_p50`, `typical_contract_value_p75`, `typical_cadence_days`, `vendor_concentration_top_share` per buyer (from the dataset records; no payment-term pattern — not published). F2.2 **CODE**: `all_canadian_vendors` (full list, capped at 2,000 characters; the complete list is the contracts subfolder).
- F3.1/F3.2 **CODE**: `pair_prior_records`, `pair_first_or_repeat`, `pair_value_trend` (increasing / decreasing / stable from dated values), `pair_dates_and_values`.

## G — coverage
- G1.1 priority: Texas comptroller payments and Massachusetts CTHR first (bulk CSV, vendor state field), then Illinois ledger, Kansas KanView, NJ, Indiana, PennWATCH, municipal POs. G1.2–G1.4: pipelines (Jules/Codex queue). G2.1: P13 growth came from the Mac crawlers' lead buyers (131k sites read) and the org_extras names; ~1–2k new organisations/day while the crawler queue lasts. G2.2: P02/P04 growth = lanes' and crawler finds + verification-log merge. G2.3 **RUNS** (lanes) + **RESET**.
- G3.1 **done tonight** (DNS refresh +11,183 domains). G3.2: the referee runs on every push (every 15 min); P11 rows stay pending only when the page blocks GitHub's runner — those need a second lane's read (verify tasks exist). G3.3 **RUNS** (round 4 names).

## H — P13 inference
- H1.1/H1.2: the 11-06 build carries no MPAC rows (0 of 201 member/regulated-payer rows); the levy file was not received in the repo; if MPAC returns, the upper/lower-tier rule in `prompts/claude_d_items.md` applies. H2.1/H2.2 **RESET**: municipal utilities (Longueuil, Westmount, Sherbrooke, Saguenay, Joliette, Magog, Baie-Comeau, Alma, Amos, Coaticook — Québec's 9 municipal distributors; Saskatoon Light & Power, Swift Current; Winnipeg Hydro is Manitoba Hydro since 2002) are known lists; P13 Hydro rows in those cities get re-pointed in code after the reset. H3.1 **CODE**: Canada Post inference confidence lowered for small non-profits / religious bodies / libraries. H3.2 **NO** (mailing volume by buyer type is a guess). H2.1 **CODE** now for the known municipal distributors (Alma, Amos, Baie-Comeau, Coaticook, Joliette, Magog, Saguenay, Sherbrooke, Westmount, Saint-Jean-Baptiste-de-Rouville; Saskatoon, Swift Current): `inference_confidence` LOW with the reason. H4.1 **RESET** (re-tiering the P13 rules needs a reviewed change). H4.2 **CODE**: `inference_confidence` explicit column. H5.1/H5.2 **NO** for now: regulators and telecoms are not "vendors with a dated relationship"; WSIB/CNESST/WorkSafeBC premiums are statutory, not invoiced supplies — the owner's rule was contracts, not statutory payments.

## I — mail security / deliverability
- I1.1 **done tonight**; I1.2 **RESET** (a history file of DMARC policies per check date starts with the daily DNS loop launched tonight). I2.1 **RUNS**: a daily Mac loop re-runs mx_check + dmarc_check on the current delivered mailboxes. I2.2 SMTP probing **NO** (unsolicited RCPT probing is abuse-adjacent; rule 9 spirit). I3.1 **RUNS** (mail_provider from MX each build). I3.2/I4.x **NO** (no sends have been made; catch-all/greylist signals need SMTP probing).

## J — vendor side
- J1.1/J1.2 **RUNS**: the all-vendor domain pass launched tonight (every vendor website in the release, not only ranked rows). J2.1/J2.2 **NO** (NAICS classification and size estimates would be guesses; LinkedIn/D&B scraping breaks ToS). J3.1 **RUNS** (vendor sites are read; `vendor_country_basis` keeps the quote).

## K — French
- K1.1/K1.2 **CODE** (D15). K2.1/K2.2: values are kept as printed (French when the buyer prints French); no translation.

## L — Peppol / e-invoicing
- L1.1 **done**: the whole Peppol Directory for Canada = 77 participants, nearly all suppliers; 2 ranked buyers, 35 vendors matched; every row states it. L1.2 **RESET** (AU/NZ/SG/EU participants for the non-Canadian buyers in the pool — same tool, other countries). L1.3: no Canadian authority on Peppol yet. L2.1–L2.3 **partly CODE**: `invoice_portal_kind` names Ariba/Coupa/Oracle when the buyer's page says so; network membership lists are not public.

## M — sensitivity
- M1.1/M1.2/M2.1/M2.2 **CODE**: `sensitivity_tag` extended (law enforcement, corrections, border, intelligence, financial regulators, justice, major banks, cybersecurity vendors, political parties, major media, University of Toronto named exclusion) + `sensitivity_flag` yes/no.

## N — tech stack
- N1.1/N1.2 **partly**: `invoice_portal_kind` / `ap_system_hint` from the buyer's own pages (Ariba, Coupa, Workday, Oracle, SAP, Esker, Kofax, Tipalti, Bill.com, AvidXchange named on the page); BuiltWith/job-posting inference **NO**. N2.x **NO** (not published).

## O — audit trail
- O1.1 **CODE** (`facts_provenance_json`). O1.2 **RUNS/CODE**: `email_evidence_context` — 500 characters of the page's own text around the mailbox, captured by ap_terms (pass 3 tonight re-reads every delivered page for it); the 300-character quote stays the referee-verified value. O1.3 **CODE**: `evidence_age_days` + `reverify_due` (>60 days) from the retrieval/verification dates. O2.1/O2.2 **CODE**: `tools/release_diff.py` writes `CHANGELOG.md` + `rows_changed.csv` per build (rows added / removed / mailbox changed, per package).

## P / Q — value, cadence, payment history
- P1.x, P2.x, P3.1, Q1.x, Q2.1 **NO/partly**: no payment-lag, dispute or invoice-amount data is public; `typical_contract_value_p50/p75` and `typical_cadence_days` (F2) are the honest proxies.

## R — edge cases
- R1.1 **CODE/audit**: the SHARED_GOV rule is enforced each build; `audit_deliverable.py` reports cross-agency leaks (0 hard fails on 11-06). R2.1 **CODE**: REGION_TOK extended (eu, asia, oceania, mena, nordic, benelux, ca-only tokens, 2-letter country codes as whole tokens). R3.1: the sibling-campus rule applies to every mailbox (same_org); hospital networks and school boards share one domain legitimately. R4.1 **CODE** (`buyer_bn_program`). R5.1 **CODE**: `vendor_registry_warning` for dissolved / inactive matches (a flag; the match itself may be a namesake, so no removal).

## S / T — structure, methodology
- S1.1 **CODE**: `ranked_buyers.jsonl.gz` beside the CSV. S2.1/S2.2 **CODE**: `data_quality_score` (/100) + `ship_ready`. S3.1/S3.2 **CODE** (`CHANGELOG.md`, build id = commit). S4.1/S4.2 **partly CODE**: `buyer_sector` from buyer_type; size **NO**.
- T1.1: the referee re-fetches the evidence URL and requires the mailbox string in the page text (HTML or PDF), case-insensitive; a value hidden behind scripts counts only when two lanes quote it (cross_verified). T2.1: `same_org` is token-based (domain tokens vs organisation name tokens, abbreviations), not fuzzy-scored; it is the same for every tier. T3.1 **CODE**: `audit_deliverable.py` already fails on duplicate organisation / domain / mailbox; count printed in AUDIT.md. T4.1/T4.2 **CODE** (`inference_confidence`, `mailbox_confidence`).

## U / V / W / X
- U1–U4 **RESET/NO** (Common Crawl stays off; LinkedIn **NO**). V1–V4: sector pools are filters over the same rows (`buyer_sector`, `instrument_type_normalized`); standing-offer draws (V4.1) are separate records where the source publishes them. W1.1 top 10 for the invoice use case: ap_terms fills (terms/PO/portal/phone/address), lanes' AP mailboxes (Gold growth), template_language, sensitivity_flag, pair repeat/first, quality score + ship_ready, portal cleanup, Gold contracts 5,000, CHANGELOG, Peppol answer. W1.2: everything above is in the 3-hourly rebuild (no hot-patching of shipped files). W2.1: a field lift = next build (≤3 h) once the engine has run; a reference file = one build; a new category = one build. W3.1: write findings as rows in `data/incoming/<lane>/` (`docs/RETURN_FORMATS.md`) — the referee verifies them like any lane's. W3.2: `tools/validate_deliverable.py` + `audit_deliverable.py` run before every publish; header width is checked. X1.1: 419 newer domains → DNS done; T6_004–009 → RESET; 20,113 no-name P13 → round 4 running; Gold ceiling → stated in DECISIONS. X2.1 **NO** (inferred spend/cadence = fabrication). X3.1 **NO** (no public register of "under investigation"). X4.1: the GitHub repo is the API — `coord/results/ranked/` changes every 3 h; `CHANGELOG.md` + `rows_changed.csv` are the delta.
