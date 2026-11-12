# Ingest report — 2026-11-12T00:50:28Z

- buyers with team findings: 401431 (with at least one verified e-mail/portal: 374255)
- vendors with team findings: 15607
- QA rows: 200
- counters: {'files': 290, 'buyer_findings_verified': 408077, 'buyer_findings_verified_on_archive_copy': 13663, 'buyer_findings_not_found_on_page': 3164, 'buyer_findings_unverified_page_unavailable': 25897, 'buyer_findings_not_found_on_page_hidden': 512, 'buyer_findings_rejected_personal_or_invalid': 822, 'vendor_emails_not_found_on_page': 412, 'vendor_emails_not_found_on_page_hidden': 422, 'vendor_emails_verified': 4466, 'vendor_emails_unverified_page_unavailable': 329, 'buyer_findings_cross_verified': 13, 'ledger_verdict_stands_page_not_read_again_not_found_on_page': 3576, 'ledger_verdict_stands_page_not_read_again_not_found_on_page_hidden': 933, 'ledger_verdict_stands_page_not_read_again_unverified_page_unavailable': 26224, 'ledger_verdict_stands_page_not_read_again_verified': 412539, 'verify_tasks_chatgpt': 110, 'verify_tasks_gemini': 25243, 'verify_tasks_jules': 9}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv` (lane claude: `verification_log_claude.csv` and its parts). Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1594 | 5 | 0 | 60 | 1 | 43 | 0 |
| claude | 401683 | 1 | 0 | 25480 | 57 | 1969 | 821 |
| codex | 229 | 0 | 0 | 17 | 0 | 4 | 0 |
| gemini | 4571 | 7 | 0 | 327 | 454 | 1148 | 1 |
