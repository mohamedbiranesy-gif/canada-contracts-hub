# Ingest report — 2026-11-11T13:35:50Z

- buyers with team findings: 330278 (with at least one verified e-mail/portal: 307554)
- vendors with team findings: 15607
- QA rows: 200
- counters: {'files': 288, 'buyer_findings_verified': 338570, 'buyer_findings_verified_on_archive_copy': 13157, 'buyer_findings_not_found_on_page': 3027, 'buyer_findings_unverified_page_unavailable': 21513, 'buyer_findings_not_found_on_page_hidden': 505, 'buyer_findings_rejected_personal_or_invalid': 822, 'vendor_emails_not_found_on_page': 412, 'vendor_emails_not_found_on_page_hidden': 422, 'vendor_emails_verified': 4466, 'vendor_emails_unverified_page_unavailable': 329, 'buyer_findings_cross_verified': 13, 'ledger_verdict_stands_page_not_read_again_not_found_on_page': 3375, 'ledger_verdict_stands_page_not_read_again_not_found_on_page_hidden': 910, 'ledger_verdict_stands_page_not_read_again_unverified_page_unavailable': 18254, 'ledger_verdict_stands_page_not_read_again_verified': 328303, 'verify_tasks_chatgpt': 110, 'verify_tasks_gemini': 20791, 'verify_tasks_jules': 9}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv` (lane claude: `verification_log_claude.csv` and its parts). Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1594 | 5 | 0 | 60 | 1 | 43 | 0 |
| claude | 332176 | 1 | 0 | 21096 | 50 | 1832 | 821 |
| codex | 229 | 0 | 0 | 17 | 0 | 4 | 0 |
| gemini | 4571 | 7 | 0 | 327 | 454 | 1148 | 1 |
