# Ingest report — 2026-11-06T14:57:56Z

- buyers with team findings: 76303 (with at least one verified e-mail/portal: 73666)
- vendors with team findings: 15387
- QA rows: 200
- counters: {'files': 234, 'buyer_findings_verified': 88950, 'buyer_findings_verified_on_archive_copy': 617, 'buyer_findings_not_found_on_page': 2537, 'buyer_findings_unverified_page_unavailable': 1358, 'buyer_findings_not_found_on_page_hidden': 477, 'buyer_findings_rejected_personal_or_invalid': 88, 'vendor_emails_not_found_on_page': 409, 'vendor_emails_not_found_on_page_hidden': 426, 'vendor_emails_verified': 4391, 'vendor_emails_unverified_page_unavailable': 313, 'buyer_findings_cross_verified': 199, 'verify_tasks_chatgpt': 213, 'verify_tasks_gemini': 343}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 976 | 15 | 0 | 12 | 0 | 22 | 0 |
| claude | 84431 | 88 | 0 | 937 | 8 | 1469 | 87 |
| gemini | 3543 | 96 | 0 | 312 | 367 | 1046 | 1 |
