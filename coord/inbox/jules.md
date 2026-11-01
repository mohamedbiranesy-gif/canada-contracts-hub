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
