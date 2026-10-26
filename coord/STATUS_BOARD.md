# STATUS BOARD (auto-generated 2026-10-26 22:03 UTC — do not edit by hand)

## Dataset (release `dataset-latest`, reference date 2026-10-26)
| metric | value |
|---|---|
| contracts, vendor verified in Canada | 770,613 |
| contracts, vendor country unverified | 51,346 |
| sources with records / checked without | 74 / 119 |
| status: ongoing (explicit end date) | 82,862 |
| status: ongoing_inferred | 321,516 |
| status: end_date_unknown | 366,235 |
| buyer AP e-mail | 500470 (65%) |
| buyer invoice portal | 6482 (1%) |
| buyer website | 714979 (93%) |
| vendor registry match | 411573 (53%) |
| vendor Business Number (BN9) | 127190 (17%) |
| vendor website | 132141 (17%) |
| vendor any contact | 132141 (17%) |

## Team research progress (rows returned → verified)
| lane | task | rows | found | not_published | blocked | other |
|---|---|---|---|---|---|---|
| chatgpt | chatgpt_buyer_ap_results_batch01.csv | 190 | 32 | 56 | 9 | 93 |
| chatgpt | chatgpt_buyer_ap_results_batch02.csv | 142 | 48 | 29 | 16 | 49 |
| chatgpt | chatgpt_buyer_ap_results_batch03.csv | 65 | 22 | 21 | 2 | 20 |
| chatgpt | chatgpt_qa_audit_results_batch01.csv | 100 | 0 | 0 | 0 | 100 |
| chatgpt | chatgpt_qa_audit_results_batch02.csv | 100 | 0 | 0 | 0 | 100 |
| claude | claude_buyer_ap_results_crawl01.csv | 745 | 745 | 0 | 0 | 0 |
| gemini | gemini_buyer_ap_results_batch01.csv | 61 | 36 | 25 | 0 | 0 |

**team_buyers**: 816 entities researched, 684 with at least one verified contact.

**team_vendors**: 0 entities researched, 0 with at least one verified contact.

## Source registry (`coord/source_registry.csv`)
| lane | todo | in_progress | done | blocked |
|---|---|---|---|---|
| codex | 15 | 0 | 0 | 0 |
| jules | 8 | 0 | 3 | 0 |

## Last ingest
- buyers with team findings: 816 (with at least one verified e-mail/portal: 683)
- vendors with team findings: 0
- QA rows: 200
- counters: {'files': 7, 'buyer_findings_verified': 920, 'buyer_findings_unverified_page_unavailable': 25, 'buyer_findings_not_found_on_page': 5, 'buyer_findings_not_found_on_page_hidden': 6, 'buyer_findings_cross_verified': 2, 'verify_tasks_gemini': 20, 'verify_tasks_chatgpt': 5}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|
| chatgpt | 170 | 1 | 2 | 0 | 2 | 0 |
| claude | 721 | 1 | 20 | 0 | 3 | 0 |
| gemini | 29 | 0 | 1 | 6 | 0 | 0 |

## Where to look
- Next work per lane: `coord/NEXT.md`
- Messages: `coord/inbox/`
- Decisions: `coord/DECISIONS.md`
