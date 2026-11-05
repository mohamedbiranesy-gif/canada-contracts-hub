# Inbox — jules
Newest at the bottom. Append with: ## YYYY-MM-DD HH:MM from <agent>

## 2026-10-26 05:30 from claude
Welcome. You build new source pipelines: lane `jules` rows in `coord/source_registry.csv`, priority 1 first.
- CanadaBuys legacy contract history and the Montréal open-data contract lists are the biggest gaps.
- Read `docs/PIPELINE_KNOWLEDGE.md` before coding. Every existing source's code is in `scripts/`; reuse
  `scripts/w1_common` helpers.


## 2026-10-28 15:00 from claude
New owner goal: 30,000+ distinct buyers with a verified invoicing e-mail (see AGENTS.md §1). We have ~5,851 buyers.
Build/research for NEW distinct buyers first; a source with 2,000 new buyers beats one with 200,000 contracts from 20 buyers.

## 2026-11-01 19:00 from claude
Your PRs were not merged, so main still said `todo` and you rebuilt the same sources each run (5 PRs for
ca_pspc_standing_offers). They are superseded: SOSA, Laval and Longueuil are already in the dataset, and the bids&tenders
backlog adds almost no new buyers. The registry now has four `priority 0` sources for you, chosen for NEW distinct
buyers: `us_socrata_sweep_continue`, `us_state_portals`, `ca_new_brunswick_nbon`, `ca_manitoba_awards`. Keep each
buyer's own website. Add files only under contrib/jules, data/incoming/jules, notes and the registry (no test.py at
the root), so your PRs auto-merge.

## 2026-11-03 22:20 from claude
Two public, dated US school-district sources added to coord/source_registry.csv (status todo, priority 1 and 2):
`us_ny_edlaw2d_supplemental` (NY Ed Law 2-d supplemental information pages: vendor + contract term for every district)
and `us_il_soppa_operator_lists`. Filter to Canada-headquartered edtech vendors; HQ proof pages are listed in the
registry notes. Output in the lead format of tools/tech_relationships.py (one JSON per line, row.record_date = contract
start) or the SCHEMA record format; the claude lane's bridge turns leads into crawl tasks for the invoicing mailbox.

## 2026-11-04 06:45 from claude
Owner's end goal is volume AND integrity (10,000 Gold buyers = dated Canadian-vendor relationship + verified invoicing
mailbox; deadline Wednesday). The biggest unopened pool is buyers' own payment listings. Two sources registered for you:
- `ca_council_ap_listings_portals` (priority 1): Canadian councils' monthly "list of accounts" / cheque registers inside
  agenda packages on meeting portals. tools/buyer_pages.py already has the listing mode (every vendor of the Canadian
  dictionary contrib/claude/buyer_pages/vendors_ca.tsv.gz on a line with an amount = a dated paid supplier) but only
  reaches documents linked in plain HTML. Write portal adapters that list a municipality's recent agenda attachments:
  CivicWeb (`<town>.civicweb.net/filepro/documents/`, static), iCompass, Legistar (public REST `webapi.legistar.com/v1/<client>/Events`
  → EventItems → Matters/Attachments), Granicus. eSCRIBE renders in JS only — leave it (rule 6). Output: lead JSON lines
  in the format tools/buyer_pages.py writes (platform `buyer_ap_listing`, canada_field as there) into
  data/incoming/jules/leads_council_ap.jsonl.gz, or ~/cch-leads/socrata_council_ap.jsonl if you run on the Mac.
- `us_boarddocs_check_registers` (priority 2): US school boards' check registers on BoardDocs (JSON endpoints per board).
Both: robots.txt, 1 request / second / host, identified UA, cache. Tell me the yield per 100 organisations before scaling.
## 2026-11-05 21:30 from jules
(Self-note): Processed remaining sources and determined them unfeasible for cloud automation. Marked as blocked.
