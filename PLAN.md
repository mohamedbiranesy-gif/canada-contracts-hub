# PLAN.md — route to 1,000,000 (written 2026-11-13 00:41Z; detail and pool sizes: docs/ROUTE_TO_1M.md)
Approach chosen: widen the pools of named organisations tied to a Canadian biller by a public record, and fix the website/mailbox
bottleneck with one shared finder (Overture places + domains proven by a published identifier). Dropped: loosening rule 1/6 without the
owner (would inflate); hand research of single buyers (does not scale).
Tasks (each with a checkable result):
1. dian-imports first run -> leads_dian_* shards > 0 (CHECKS: dian). 2. f5500 first run -> leads_f55_* > 0. 3. next rank build carries the
kinds 'export sale' / 'benefit plan contract' and writes contract_buyers_without_website.csv. 4. hc + xc finders: sites up week over week.
5. CWB certified companies (authority register) -> leads. 6. registry rows built by jules/codex (CER, BC stumpage, CIRO, Accreditation
Canada, PCAOB, DBRS, permits, lobbyists, CSA, industrial designs). 7. read 10 rows per new kind by eye each build.
Pre-mortem (six months on, it failed because): (a) guessed sites tied to the wrong company -> check: identifier printed on the site, sample
50; (b) rows count organisations twice under two domains -> check: one-per-buyer dedupe in rank, sample duplicates; (c) the owner rejects a
kind (US branch, by-location) -> check: each kind is one flag in rank.py and can be withdrawn by a gone shard.
