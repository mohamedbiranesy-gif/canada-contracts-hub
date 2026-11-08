# Enrichment to the brim — Claude's operating prompt (from the downstream spec of 2026-11-08 and the owner's order)

Owner, 2026-11-08 08:26: "all those identifiers for every single package … filled to the brim … live tools, not redundant crawls …
some other database somewhere … do specific company searches … we'll search 60,000 individual companies … find a new thing".
Quality rules stay absolute (AGENTS.md §2): a value exists only with the page it was read from, its date and a quote; role mailboxes
only; no CAPTCHA / login / proxy; nothing derived is labelled as published. Within those rules: every public database that holds a
fact about one of our organisations gets read, organisation by organisation if that is what it takes.

## What moves each field (new sources, in priority order) — and what honestly cannot move it
| Field (spec §) | Lever | Engine |
|---|---|---|
| buyer_legal_name_as_published (§3.1) | official registers of organisations, matched by website domain or exact name: provincial municipal directories (QC, ON done; AB officials export, BC local-government WFS, MB/NL PDFs, SK/NB/NS lists), school-board and hospital lists (ON, QC, AB, BC), IRCC designated-learning-institution list, GC Registry of Applied Titles, GOV.UK organisations API, US Census Government Units Survey, Australian Government Organisations Register; **Wikidata per organisation** (official name P1448, label, type, HQ, inception, budget, employees) | `tools/gov_directories.py`, `tools/wikidata_orgs.py` (Mac) |
| buyer_bn_as_published (§3.2), buyer_fiscal_year_end (§3.9) | **CRA registered-charity list** (universities, hospitals, foundations, religious bodies, arts bodies all carry BN+RR0001 and a fiscal period end); municipalities / ministries: only when printed (ap_terms catches GST numbers on AP pages) | `tools/charity_buyers.py` (Mac) |
| po_number_as_published (§1.1) | the buyers' own **purchase-order open data** (Toronto, Ottawa, Vancouver, Calgary, Edmonton, Winnipeg, Montréal, Québec, Halifax, Hamilton, Mississauga, Surrey, Regina, Saskatoon, universities) joined to the existing buyer–vendor pairs: PO numbers for pairs we already have, never new rows without a vendor-location field | `tools/po_opendata.py` (Mac) after URL discovery by agents |
| vendor_bn9 (§2.1) | ceiling stated: BN is a CRA number published only by Corporations Canada (federal corps, done), the CRA charity list (done), BC OrgBook (BC corps, done) and vendors' own sites (org_extras, done); provincial registries (ON, AB, SK, MB) do not publish BN and are search-only / paid. REQ gives NEQ, matched in bulk | — |
| vendor_* facts (§2.2–2.13) | all-vendor org_contacts/org_extras pass (done 11-07: 8,350 sites read), Wikidata per vendor, SEC EDGAR submissions JSON for public companies (business address, fiscal year end, state of incorporation), Corporations Canada directors (bulk, "vendor_authorized_signatories") | `tools/wikidata_orgs.py`, `tools/edgar_orgs.py`, merge plugin |
| invoicing_requirements / payment_terms / AP contact / portal (§4) | **one search per organisation** ("<buyer>" accounts payable invoice) instead of 10-domain groups: WebSearch waves of 6 agents × 33 searches every 25 minutes while credits last; a paid search API on the Mac (Brave Search API, ~$5 per 1,000 queries) would do all 66k organisations without Claude credits — owner's call | agent waves (`search/pc/`), `tools/company_search.py` when a key exists |
| contract_value / dates / description (§5) | only from the record; Public Accounts give vendor totals, not contract values — not merged into contract fields (stated) | — |
| contracts subfolder (§6) | covers every delivered organisation that has dataset records; the rest have none by definition; per-pair cumulative value / first / last dates added to the rows | rank.py |
| mail checks (§7) | done: MX / SPF / DMARC / MTA-STS / TLS-RPT / BIMI on every delivered domain, daily; history file from 11-07 on | Mac daily loop |
| P13 refinements (§8) | done where data exists (confidence column, Canada Post calibration, municipal electricity distributors, ON tier column); MPAC: 0 rows | rank.py |
| quality score / ship_ready / per-category scores / versioning (§9) | done; per-category scores added | rank.py |

## The loop (every wake-up)
1. Pull; read SUMMARY / VALIDATION / AUDIT / CHANGELOG of the last build; fix any regression first.
2. Mac engines alive? (`launch15.sh`); new result files pushed by push_loop?
3. Launch the next search wave (6 agents, one organisation per search, highest tiers first) and the next Mac job from the table.
4. Merge new result files into rank.py when a new source lands (always: blank cells only, provenance suffix, never overwrite a verified value).
5. Dispatch a build when a source landed; refresh the status table in `prompts/claude_d_items.md`; the Downloads loop ships it.
