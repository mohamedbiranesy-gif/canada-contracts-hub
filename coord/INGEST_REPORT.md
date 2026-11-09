# Ingest report — 2026-11-09T05:01:12Z

- buyers with team findings: 77234 (with at least one verified e-mail/portal: 74918)
- vendors with team findings: 15497
- QA rows: 200
- counters: {'files': 264, 'buyer_findings_verified': 94964, 'buyer_findings_verified_on_archive_copy': 5820, 'buyer_findings_not_found_on_page': 2750, 'buyer_findings_unverified_page_unavailable': 1069, 'buyer_findings_not_found_on_page_hidden': 430, 'buyer_findings_rejected_personal_or_invalid': 70, 'vendor_emails_not_found_on_page': 418, 'vendor_emails_not_found_on_page_hidden': 420, 'vendor_emails_verified': 4411, 'vendor_emails_unverified_page_unavailable': 346, 'buyer_findings_cross_verified': 11, 'verify_tasks_chatgpt': 120, 'verify_tasks_gemini': 428, 'verify_tasks_jules': 4}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1485 | 5 | 0 | 56 | 1 | 43 | 0 |
| claude | 89143 | 0 | 0 | 669 | 12 | 1578 | 69 |
| codex | 98 | 0 | 0 | 7 | 0 | 1 | 0 |
| gemini | 4238 | 6 | 0 | 326 | 417 | 1128 | 1 |
