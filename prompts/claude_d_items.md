# The owner's D1–D15 programme (2026-11-06) — plan, status, and what each run must do

Owner, 2026-11-06 evening: "credits reset tomorrow … set max god mode in motion to address these" and "if there's anything you can
run on my Mac do it … go max, I can't waste a day because credits are down". So: everything that costs no credits (Mac engines,
lane task batches, rank.py code) runs tonight; everything that needs web-search agents waits for the reset (a scheduled wake-up).
Rules unchanged (AGENTS.md §2): evidence or nothing, role mailboxes only, no getting around blocks, no fabrication, 1–2 req/s.

| # | Ask | Status (2026-11-08 07:20Z) | How / where |
|---|---|---|---|
| D1 | Expand P02/P03/P04 pool with the staff-directory search method | **done + continuing**: 2,400 lane tasks (Gemini/ChatGPT apps idle since 11-06 evening — their own limits); agent passes run 11-08: T6_004–009 (T/M staff directories, 53 pages), V7_001–007 (A/B plain accounts-payable pass, 244+ pages / 175+ orgs) → deep_pages p53/p55/p56/p57 on the Mac; verified ledger restored 16 Gold rows the referee had flapped out (565 → 581) | `contrib/claude/lane_tasks/`, scratchpad search/v7, search/t6 |
| D2 | `invoice_reference_hint` back-reference for P06/P06T/P07/P08 | **done in rank.py** (`most_recent_record_reference_any_vendor`, `records_in_contract_dataset`; lead rows matched to dataset orgs by website domain / exact name) | next rank run |
| D3 | `vendor_bn9` on P02–P04 via provincial registries | **partly**: the registry match already runs in the merge (Corporations Canada / REQ / BC OrgBook); the remaining vendors are mostly sole proprietors / trade names with no public BN. **after reset**: ON OnBis / AB registry lookups are search-only (no bulk file, CAPTCHA on AB) → honest ceiling | report the ceiling in the next status |
| D4 | `payment_terms_as_published` > 8.6% | **done as far as the pages go**: ap_terms read 56,985 mailboxes' pages (3 passes) + 64 search-found terms pages (p54): 209 payment terms, 336 PO rules, 609 portals, 828 AP phones (AP-grade pages), 437 mailing addresses, 354 payment-method preferences, 161 tax-exempt notes, 46,046 evidence contexts; honest ceiling: most public bodies do not publish terms on a web page — terms live in PO T&Cs PDFs (read when linked) or are not published | rank merges `claude_ap_terms.csv` |
| D5 | `invoice_portal_url` coverage | same tool (portal names: Ariba, Coupa, Jaggaer, Tungsten, Basware, SAP BN, Esker, Taulia, Bonfire, bids&tenders, SEAO, …) + lanes | same |
| D6 | `ap_contact_name` > 10% | same tool with rank's conservative rule (printed name within 70 chars of the mailbox, AP/finance title, known given name or honorific). Expect a few hundred, not 10%: most buyers publish a mailbox, not a person — the honest ceiling | same |
| D7 | `contracts_of_delivered_buyers` ceiling | **done in code**: Gold buyers capped at 5,000 records (was 500), others 500; CONTRACTS.md now prints the ceiling (all records of delivered orgs) | next rank run |
| D8 | All Canadian Peppol participants | **done**: `tools/peppol_directory.py` read the whole directory — 77 Canadian participants exist, nearly all suppliers; 2 match ranked buyers (both private companies). Every row now says whether the buyer / vendor is listed. Canada's public bodies are not on Peppol | `claude_peppol_participants.csv` |
| D9 | MPAC lower/upper-tier audit | **data now available**: `buyer_municipal_tier` carries the official ON tier (Lower / Upper / Single Tier) for every Ontario municipality in the pool; still 0 MPAC rows in the build, so nothing to demote | — |
| D10 | DMARC re-run on 11-06 data | **done**: 69,555 domains incl. MTA-STS / TLS-RPT / BIMI; daily re-check loop on the Mac | — |
| D11 | `buyer_legal_name_as_published` > 24.6% on Gold | **done for QC + ON municipalities**: official MAMH répertoire (1,281) + ON MMAH list (444) → 1,398 ranked organisations matched, 1,247 legal names, 318 phones, tier (ON) and population (QC) columns; round 4 org_extras added 6,998 legal names; other provinces: MB / NL PDFs fetched (parse later), BC/SK/NB/NS/PE have no official download | `tools/municipal_directory.py` |
| D12 | Cross-reference non-dataset relationships | **done in rank.py** (`other_relationship_sources`: lead relationships seen for a dataset buyer; `records_in_contract_dataset` the other way) | next rank run |
| D13 | Tag ASIRT / SIU / BEI / IIO etc. | **done in rank.py** (`sensitivity_tag`, nine categories, a tag never a removal) | next rank run |
| D14 | `commodity_codes` from UNSPSC etc. | **done in rank.py + contracts export** (`classify_plus`: the record's own commodity block — UNSPSC, GSIN, NAICS, CPV, PSC, economic object) | next rank run |
| D15 | French detection for QC buyers | **done in rank.py** (`template_language`: fr for every Québec buyer by jurisdiction, .qc.ca, QC address or French municipal name; en-fr federal / NB) | next rank run |

## Tonight's Mac deployments (all credit-free; logs in `~/cch-crawler-state/`)
- The Mac rebooted at 06:05 EST and every engine had died: `launch15.sh` restarted push_loop (v3), sync_loop (mac_sync for the
  Gemini / ChatGPT apps), lead_scanner --bridge, ap_crawler, site_finder.
- `ap_terms1.log` (tools/ap_terms.py, 3,635 pages, 24 workers), `org_contacts_r4.log` → `org_extras_r4.log` (round 4, 32 workers),
  `peppol.log` (done), `mx_check11.log` / `dmarc_check6.log` (done).
- The ChatGPT app (automation every 30 min) and the Gemini app (Task mode) are open and working their new batches; mac_sync uploads.

## After the credit reset (scheduled wake-up, Saturday 2026-11-07 ~14:30Z)
1. Pull; check `coord/results/ranked/SUMMARY.md` (the 3-hourly rank picks up ap_terms, peppol, round 4, the lanes' new rows);
   VALIDATION 7/7, AUDIT hard checks PASS; refresh `~/Downloads/canada-contracts-gold-2026-11-07/`.
2. Agent search passes (≤33 searches per agent, one message, sonnet): D1 staff-directory pass on P02–P04 A/B orgs the lanes have
   not reached (`search/a6` method), T6_004–009; D4 "payment terms / supplier guide" pass on Gold buyers still blank; D11 municipal
   directory URLs (4–6 searches) then a Mac fetch; D3 honest ceiling note.
3. Merge → `coord/tasks/claude/claude_search_urls_p53+.csv` → Mac `tools/deep_pages.py --urls` → push → rank → status message.
