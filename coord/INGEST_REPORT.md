# Ingest report — 2026-11-13T10:40:04Z

- buyers with team findings: 627530 (with at least one verified e-mail/portal: 597865)
- vendors with team findings: 15607
- QA rows: 200
- counters: {'files': 696, 'buyer_findings_verified': 641449, 'buyer_findings_verified_on_archive_copy': 14741, 'buyer_findings_not_found_on_page': 3491, 'buyer_findings_unverified_page_unavailable': 28159, 'buyer_findings_not_found_on_page_hidden': 525, 'buyer_findings_rejected_personal_or_invalid': 814, 'vendor_emails_not_found_on_page': 413, 'vendor_emails_not_found_on_page_hidden': 422, 'vendor_emails_verified': 4465, 'vendor_emails_unverified_page_unavailable': 329, 'buyer_findings_cross_verified': 13, 'ledger_verdict_stands_page_not_read_again_not_found_on_page': 3903, 'ledger_verdict_stands_page_not_read_again_not_found_on_page_hidden': 946, 'ledger_verdict_stands_page_not_read_again_unverified_page_unavailable': 28484, 'ledger_verdict_stands_page_not_read_again_verified': 644925, 'verify_tasks_chatgpt': 107, 'verify_tasks_gemini': 27728, 'verify_tasks_jules': 9}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv` (lane claude: `verification_log_claude.csv` and its parts). Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1594 | 5 | 0 | 60 | 1 | 43 | 0 |
| claude | 635055 | 1 | 0 | 27742 | 70 | 2296 | 813 |
| codex | 229 | 0 | 0 | 17 | 0 | 4 | 0 |
| gemini | 4571 | 7 | 0 | 327 | 454 | 1148 | 1 |
