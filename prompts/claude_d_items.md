# The owner's D1–D15 programme (2026-11-06) — plan, status, and what each run must do

Owner, 2026-11-06 evening: "credits reset tomorrow … set max god mode in motion to address these" and "if there's anything you can
run on my Mac do it … go max, I can't waste a day because credits are down". So: everything that costs no credits (Mac engines,
lane task batches, rank.py code) runs tonight; everything that needs web-search agents waits for the reset (a scheduled wake-up).
Rules unchanged (AGENTS.md §2): evidence or nothing, role mailboxes only, no getting around blocks, no fabrication, 1–2 req/s.

| # | Ask | Status (2026-11-07 03:00Z) | How / where |
|---|---|---|---|
| D1 | Expand P02/P03/P04 pool with the staff-directory search method | **in motion, credit-free**: 2,400 research tasks pushed for the two Mac lanes (`chatgpt_buyer_ap_batch50–61`, `gemini_buyer_ap_batch44–55`; 3,548 more candidates ready in `contrib/claude/lane_tasks/make_lane_batches.py`); **after reset**: agent passes on the same orgs (INSTRUCTIONS_A6 method) + T6_004–009 | tasks: every A/B/T/L org without a confirmed AP mailbox, never-researched first; inbox notes carry the method |
| D2 | `invoice_reference_hint` back-reference for P06/P06T/P07/P08 | **done in rank.py** (`most_recent_record_reference_any_vendor`, `records_in_contract_dataset`; lead rows matched to dataset orgs by website domain / exact name) | next rank run |
| D3 | `vendor_bn9` on P02–P04 via provincial registries | **partly**: the registry match already runs in the merge (Corporations Canada / REQ / BC OrgBook); the remaining vendors are mostly sole proprietors / trade names with no public BN. **after reset**: ON OnBis / AB registry lookups are search-only (no bulk file, CAPTCHA on AB) → honest ceiling | report the ceiling in the next status |
| D4 | `payment_terms_as_published` > 8.6% | **running on the Mac**: `tools/ap_terms.py` re-reads every evidence page (3,694 pages at grade ≥ purchasing); first 1,400 pages → 119 terms, 225 PO rules, 209 portals, 447 AP phones, 154 addresses, 51 printed AP contacts. Lanes also asked to record terms. **after reset**: targeted "supplier guide / payment terms" search pass for Gold buyers still blank | rank merges `claude_ap_terms.csv` |
| D5 | `invoice_portal_url` coverage | same tool (portal names: Ariba, Coupa, Jaggaer, Tungsten, Basware, SAP BN, Esker, Taulia, Bonfire, bids&tenders, SEAO, …) + lanes | same |
| D6 | `ap_contact_name` > 10% | same tool with rank's conservative rule (printed name within 70 chars of the mailbox, AP/finance title, known given name or honorific). Expect a few hundred, not 10%: most buyers publish a mailbox, not a person — the honest ceiling | same |
| D7 | `contracts_of_delivered_buyers` ceiling | **done in code**: Gold buyers capped at 5,000 records (was 500), others 500; CONTRACTS.md now prints the ceiling (all records of delivered orgs) | next rank run |
| D8 | All Canadian Peppol participants | **done**: `tools/peppol_directory.py` read the whole directory — 77 Canadian participants exist, nearly all suppliers; 2 match ranked buyers (both private companies). Every row now says whether the buyer / vendor is listed. Canada's public bodies are not on Peppol | `claude_peppol_participants.csv` |
| D9 | MPAC lower/upper-tier audit | **nothing to audit**: the 11-06 build has 0 MPAC-inferred rows (the 201 member / regulated-payer rows are Alberta Municipalities, CCUA, CICan, IESO, IBC, AESO, CBA, Electricity Canada). If MPAC rows return, apply: upper-tier = County / Regional Municipality / United Counties / Muskoka; single-tier cities; lower-tier rows lose the relationship | — |
| D10 | DMARC re-run on 11-06 data | **done tonight**: mx_check 69,534 domains (+11,183), dmarc_check 69,530 domains (+11,183: 4,836 p=none, 4,423 no record, 1,324 quarantine, 573 reject); pushed; DMARC.md regenerates with the next rank | — |
| D11 | `buyer_legal_name_as_published` > 24.6% on Gold | **running on the Mac**: org_contacts + org_extras round 4 (22,764 new domains); ap_terms also catches the buyer's own GST number. **after reset**: municipal directories (QC Répertoire des municipalités, AB Municipal Contact Information, ON directory, BC CivicInfo) → legal names / addresses / phones for municipalities | round-4 results merge automatically |
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
