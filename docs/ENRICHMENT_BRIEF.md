# Enrichment brief (read with WORKER_BRIEF.md for environment rules)

Goal: attach to every vendor and every buyer in the contract dataset everything that public sources publish about them — registry identifiers, tax identifiers, addresses, websites, role mailboxes for supplier invoicing (accounts payable), procurement contacts — so each contract record can carry it. Reference date 2026-10-25.

Inputs (already built, sorted so the organisations with the most high/medium-confidence ongoing contracts come first — work top-down):
- `enrichment/vendor_master_input.jsonl` — 78,042 vendors. Fields: vendor_key, stem, name, name_variants, countries, country_basis, addresses (seen in the data), identifiers (neq, uei, duns, cage, business numbers … as published), contacts, sources, record_count, record_count_high_or_medium, example_record_ids. 22,297 vendors have high/medium-confidence ongoing contracts: do those first.
- `enrichment/buyer_master_input.jsonl` — 3,692 buyers (name, country, types, identifiers, addresses, contacts seen in the data, record counts). 2,031 have high/medium-confidence contracts: do those first.

Outputs (progressive — append as you go, flush often; one JSON object per line, keyed so the merge step can join):
- `enrichment/vendors_enriched.jsonl` — one line per vendor_key you processed:
```json
{"vendor_key": "...", "name": "...",
 "registry_matches": [{"registry": "corporations_canada | quebec_req | bc_orgbook | canada_business_registries | other", "match_confidence": "exact | strong | weak",
    "match_basis": "how the name/address matched", "legal_name": "", "corporation_number": "", "business_number_bn9": "", "jurisdiction": "",
    "status": "", "incorporation_date": "", "registered_office": {}, "naics_or_activity": "", "other_identifiers": {}, "source_url": "", "retrieved_at": "", "raw": {}}],
 "tax": {"bn9": "", "gst_hst_account_derived": "<BN9>RT0001 or null", "cra_registry_check": {"result": "registered | not_registered | not_found | not_checked", "checked_at": "", "name_used": "", "raw": {}}},
 "contacts": {"website": "", "general_email": "", "phone": "", "source_url": "", "retrieved_at": ""},
 "extras": {"anything else public and useful: employee count, year founded, description, other registrations, parent company"},
 "notes": "free text: conflicts, ambiguities (e.g. several corporations share the name)"}
```
- `enrichment/buyers_enriched.jsonl` — one line per buyer_key you processed:
```json
{"buyer_key": "...", "name": "...", "country": "",
 "official_website": "", "canonical_name": "", "organisation_type": "",
 "identifiers": {"registry/agency codes you can find: owner_org, NEQ, agency code, municipal code, ..."},
 "address": {"line1": "", "city": "", "region": "", "postal_code": "", "country": ""},
 "ap_contact": {"emails": [], "phone": "", "fax": "", "mailing_address": "", "invoice_portal": "", "invoicing_requirements": "", "instructions_url": "", "evidence_snippet": "", "retrieved_at": ""},
 "procurement_contact": {"emails": [], "phone": "", "url": ""},
 "general_contact": {"emails": [], "phone": ""},
 "extras": {}, "notes": ""}
```
- `notes/enrichment_vendors.md` and `notes/enrichment_buyers.md` — sources used (exact URLs, retrieval times, sizes, row counts), matching rules and their precision checks (sample 30 matches by hand, report how many are right), coverage counts (how many of the inputs got each field), known gaps.

Rules:
- Only published, organisational information. Role mailboxes that organisations publish for suppliers/invoicing/procurement (e.g. an "invoices@…" or "accountspayable@…" address on a "doing business with us" page) are in scope; personal mailboxes of individuals are out of scope — do not collect or infer them. Do not guess email patterns; every email must be copied from a page, with its URL as evidence.
- Never invent identifiers. A GST/HST account may be *derived* from a published BN9 (BN9 + "RT0001") only when labelled as derived, and should then be checked in the CRA GST/HST Registry (it confirms a number + name + date; ≤ 1 request/second; record the result verbatim). If the registry disagrees, keep both facts.
- Name matching: normalise accents/case/punctuation/legal suffixes; use province/city/postal code from the dataset to disambiguate; label every match's confidence and basis; when several registry entities share a name and nothing disambiguates, record them all as "weak" rather than choosing.
- Respect sites: ≤ 2–3 requests/second per host, descriptive User-Agent, no bot-check or CAPTCHA circumvention (if a site challenges you, note it and skip).
- Time budget about 3 hours; check `date -u`; leave 20 minutes to finish the notes. Breadth first: cover the top of each input list well before going deep on anyone.
- Reply at the end with a ≤ 25-line summary: sources used, counts of vendors/buyers enriched per field, blockers.
