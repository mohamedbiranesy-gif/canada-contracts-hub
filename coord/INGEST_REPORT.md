# Ingest report — 2026-11-11T04:15:56Z

- buyers with team findings: 277480 (with at least one verified e-mail/portal: 263297)
- vendors with team findings: 15607
- QA rows: 200
- counters: {'files': 286, 'buyer_findings_verified': 291968, 'buyer_findings_verified_on_archive_copy': 12133, 'buyer_findings_not_found_on_page': 2924, 'buyer_findings_unverified_page_unavailable': 12987, 'buyer_findings_not_found_on_page_hidden': 469, 'buyer_findings_rejected_personal_or_invalid': 822, 'vendor_emails_not_found_on_page': 412, 'vendor_emails_not_found_on_page_hidden': 422, 'vendor_emails_verified': 4466, 'vendor_emails_unverified_page_unavailable': 329, 'buyer_findings_cross_verified': 13, 'ledger_verdict_stands_page_not_read_again_not_found_on_page': 3336, 'ledger_verdict_stands_page_not_read_again_not_found_on_page_hidden': 890, 'ledger_verdict_stands_page_not_read_again_unverified_page_unavailable': 13314, 'ledger_verdict_stands_page_not_read_again_verified': 296430, 'verify_tasks_chatgpt': 110, 'verify_tasks_gemini': 12249, 'verify_tasks_jules': 9}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv` (lane claude: `verification_log_claude.csv` and its parts). Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1594 | 5 | 0 | 60 | 1 | 43 | 0 |
| claude | 285574 | 1 | 0 | 12570 | 14 | 1729 | 821 |
| codex | 229 | 0 | 0 | 17 | 0 | 4 | 0 |
| gemini | 4571 | 7 | 0 | 327 | 454 | 1148 | 1 |
