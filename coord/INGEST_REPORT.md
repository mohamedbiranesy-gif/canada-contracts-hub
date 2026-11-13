# Ingest report — 2026-11-13T20:40:55Z

- buyers with team findings: 683574 (with at least one verified e-mail/portal: 652550)
- vendors with team findings: 15607
- QA rows: 200
- counters: {'files': 704, 'buyer_findings_verified': 698619, 'buyer_findings_verified_on_archive_copy': 14864, 'buyer_findings_not_found_on_page': 3598, 'buyer_findings_unverified_page_unavailable': 29484, 'buyer_findings_not_found_on_page_hidden': 525, 'buyer_findings_rejected_personal_or_invalid': 814, 'vendor_emails_not_found_on_page': 413, 'vendor_emails_not_found_on_page_hidden': 422, 'vendor_emails_verified': 4465, 'vendor_emails_unverified_page_unavailable': 329, 'buyer_findings_cross_verified': 13, 'ledger_verdict_stands_page_not_read_again_not_found_on_page': 3998, 'ledger_verdict_stands_page_not_read_again_not_found_on_page_hidden': 946, 'ledger_verdict_stands_page_not_read_again_unverified_page_unavailable': 29618, 'ledger_verdict_stands_page_not_read_again_verified': 694033, 'verify_tasks_chatgpt': 107, 'verify_tasks_gemini': 29087, 'verify_tasks_jules': 9}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv` (lane claude: `verification_log_claude.csv` and its parts). Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1594 | 5 | 0 | 60 | 1 | 43 | 0 |
| claude | 692225 | 1 | 0 | 29067 | 70 | 2403 | 813 |
| codex | 229 | 0 | 0 | 17 | 0 | 4 | 0 |
| gemini | 4571 | 7 | 0 | 327 | 454 | 1148 | 1 |
