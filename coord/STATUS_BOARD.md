# STATUS BOARD (auto-generated 2026-10-26 15:39 UTC — do not edit by hand)

## Dataset (release `dataset-latest`, reference date 2026-10-26)
| metric | value |
|---|---|
| contracts, vendor verified in Canada | 530,293 |
| contracts, vendor country unverified | 51,346 |
| sources with records / checked without | 73 / 119 |
| status: ongoing (explicit end date) | 82,830 |
| status: ongoing_inferred | 321,550 |
| status: end_date_unknown | 125,913 |
| buyer AP e-mail | 150968 (28%) |
| buyer invoice portal | 6252 (1%) |
| buyer website | 474658 (90%) |
| vendor registry match | 411223 (78%) |
| vendor Business Number (BN9) | 127118 (24%) |
| vendor website | 130635 (25%) |
| vendor any contact | 130635 (25%) |

## Team research progress (rows returned → verified)
| lane | task | rows | found | not_published | blocked | other |
|---|---|---|---|---|---|---|
| chatgpt | chatgpt_buyer_ap_results_batch01.csv | 190 | 32 | 56 | 9 | 93 |
| chatgpt | chatgpt_buyer_ap_results_batch02.csv | 80 | 30 | 14 | 12 | 24 |
| chatgpt | chatgpt_qa_audit_results_batch01.csv | 100 | 0 | 0 | 0 | 100 |
| chatgpt | chatgpt_qa_audit_results_batch02.csv | 100 | 0 | 0 | 0 | 100 |
| gemini | gemini_buyer_ap_results_batch01.csv | 61 | 36 | 25 | 0 | 0 |

**team_buyers**: 203 entities researched, 88 with at least one verified contact.

**team_vendors**: 0 entities researched, 0 with at least one verified contact.

## Source registry (`coord/source_registry.csv`)
| lane | todo | in_progress | done | blocked |
|---|---|---|---|---|
| codex | 15 | 0 | 0 | 0 |
| jules | 9 | 0 | 2 | 0 |

## Last ingest
- buyers with team findings: 203 (with at least one verified e-mail/portal: 88)
- vendors with team findings: 0
- QA rows: 200
- counters: {'files': 5, 'buyer_findings_verified': 135, 'buyer_findings_unverified_page_unavailable': 3, 'buyer_findings_not_found_on_page': 6, 'verify_tasks_gemini': 2, 'verify_tasks_chatgpt': 1}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Where to look
- Next work per lane: `coord/NEXT.md`
- Messages: `coord/inbox/`
- Decisions: `coord/DECISIONS.md`
