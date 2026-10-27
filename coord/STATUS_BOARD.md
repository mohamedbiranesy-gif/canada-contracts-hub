# STATUS BOARD (auto-generated 2026-10-27 16:15 UTC — do not edit by hand)

## Dataset (release `dataset-latest`, reference date 2026-10-27)
| metric | value |
|---|---|
| contracts, vendor verified in Canada | 770,539 |
| contracts, vendor country unverified | 51,346 |
| sources with records / checked without | 74 / 119 |
| status: ongoing (explicit end date) | 82,788 |
| status: ongoing_inferred | 321,516 |
| status: end_date_unknown | 366,235 |
| buyer AP e-mail | 580548 (75%) |
| buyer invoice portal | 16715 (2%) |
| buyer website | 714908 (93%) |
| vendor registry match | 411523 (53%) |
| vendor Business Number (BN9) | 127166 (17%) |
| vendor website | 132125 (17%) |
| vendor any contact | 132125 (17%) |

## Team research progress (rows returned → verified)
| lane | task | rows | found | not_published | blocked | other |
|---|---|---|---|---|---|---|
| chatgpt | chatgpt_buyer_ap_results_batch01.csv | 190 | 32 | 56 | 9 | 93 |
| chatgpt | chatgpt_buyer_ap_results_batch02.csv | 142 | 48 | 29 | 16 | 49 |
| chatgpt | chatgpt_buyer_ap_results_batch03.csv | 111 | 36 | 37 | 6 | 32 |
| chatgpt | chatgpt_buyer_ap_results_batch04.csv | 124 | 58 | 20 | 6 | 40 |
| chatgpt | chatgpt_buyer_ap_results_batch05.csv | 114 | 50 | 15 | 3 | 46 |
| chatgpt | chatgpt_buyer_ap_results_batch06.csv | 110 | 38 | 25 | 11 | 36 |
| chatgpt | chatgpt_buyer_ap_results_batch07.csv | 63 | 11 | 15 | 11 | 26 |
| chatgpt | chatgpt_qa_audit_results_batch01.csv | 100 | 0 | 0 | 0 | 100 |
| chatgpt | chatgpt_qa_audit_results_batch02.csv | 100 | 0 | 0 | 0 | 100 |
| claude | claude_buyer_ap_results_crawl01.csv | 746 | 746 | 0 | 0 | 0 |
| gemini | gemini_buyer_ap_results_batch01.csv | 107 | 70 | 35 | 0 | 2 |
| gemini | gemini_buyer_ap_results_batch02.csv | 108 | 65 | 37 | 0 | 6 |
| gemini | gemini_buyer_ap_results_batch03.csv | 128 | 90 | 34 | 0 | 4 |
| gemini | gemini_buyer_ap_results_batch04.csv | 100 | 59 | 40 | 0 | 1 |
| gemini | gemini_buyer_ap_results_batch05.csv | 100 | 78 | 21 | 0 | 1 |
| gemini | gemini_buyer_ap_results_batch06.csv | 100 | 76 | 23 | 0 | 1 |
| gemini | gemini_buyer_ap_results_batch07.csv | 100 | 78 | 22 | 0 | 0 |
| gemini | gemini_buyer_ap_results_batch08.csv | 100 | 73 | 25 | 1 | 1 |
| gemini | gemini_buyer_ap_results_batch09.csv | 100 | 82 | 14 | 1 | 3 |
| gemini | gemini_buyer_ap_results_batch10.csv | 100 | 86 | 9 | 2 | 3 |
| gemini | gemini_buyer_ap_results_batch11.csv | 100 | 80 | 19 | 0 | 1 |
| gemini | gemini_buyer_ap_results_batch12.csv | 100 | 68 | 29 | 0 | 3 |
| gemini | gemini_buyer_ap_results_batch13.csv | 100 | 73 | 22 | 0 | 5 |
| gemini | gemini_buyer_ap_results_batch14.csv | 100 | 76 | 22 | 0 | 2 |
| gemini | gemini_buyer_ap_results_batch15.csv | 100 | 90 | 5 | 0 | 5 |
| gemini | gemini_buyer_ap_results_batch16.csv | 100 | 75 | 19 | 0 | 6 |
| gemini | gemini_buyer_ap_results_batch17.csv | 100 | 87 | 10 | 0 | 3 |
| gemini | gemini_buyer_ap_results_batch18.csv | 100 | 84 | 10 | 0 | 6 |
| gemini | gemini_buyer_ap_results_batch19.csv | 100 | 67 | 25 | 0 | 8 |
| gemini | gemini_buyer_ap_results_batch20.csv | 100 | 61 | 36 | 0 | 3 |
| gemini | gemini_buyer_ap_results_batch21.csv | 97 | 54 | 39 | 0 | 4 |
| gemini | gemini_vendor_contacts_results_batch01.csv | 100 | 85 | 15 | 0 | 0 |
| gemini | gemini_vendor_contacts_results_batch02.csv | 100 | 81 | 19 | 0 | 0 |
| gemini | gemini_vendor_contacts_results_batch03.csv | 100 | 73 | 25 | 2 | 0 |
| gemini | gemini_vendor_contacts_results_batch04.csv | 30 | 11 | 17 | 2 | 0 |
| gemini | gemini_verify_buyer_ap_results_batch01.csv | 28 | 25 | 1 | 2 | 0 |

**team_buyers**: 3050 entities researched, 1964 with at least one verified contact.

**team_vendors**: 330 entities researched, 115 with at least one verified contact.

## Source registry (`coord/source_registry.csv`)
| lane | todo | in_progress | done | blocked |
|---|---|---|---|---|
| codex | 15 | 0 | 0 | 0 |
| jules | 8 | 0 | 3 | 0 |

## Last ingest
- buyers with team findings: 3050 (with at least one verified e-mail/portal: 1955)
- vendors with team findings: 330
- QA rows: 200
- counters: {'files': 36, 'buyer_findings_verified': 2409, 'buyer_findings_unverified_page_unavailable': 137, 'buyer_findings_not_found_on_page': 128, 'buyer_findings_not_found_on_page_hidden': 182, 'vendor_emails_unverified_page_unavailable': 11, 'vendor_emails_not_found_on_page': 5, 'vendor_emails_not_found_on_page_hidden': 14, 'vendor_emails_verified': 119, 'buyer_findings_cross_verified': 34, 'verify_tasks_gemini': 25, 'verify_tasks_chatgpt': 349}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|
| chatgpt | 442 | 7 | 14 | 0 | 8 | 0 |
| claude | 722 | 10 | 11 | 0 | 3 | 0 |
| gemini | 1245 | 17 | 78 | 182 | 117 | 0 |

## Where to look
- Next work per lane: `coord/NEXT.md`
- Messages: `coord/inbox/`
- Decisions: `coord/DECISIONS.md`
