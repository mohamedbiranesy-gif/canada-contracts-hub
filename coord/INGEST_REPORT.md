# Ingest report — 2026-11-08T06:57:16Z

- buyers with team findings: 76351 (with at least one verified e-mail/portal: 74025)
- vendors with team findings: 15497
- QA rows: 200
- counters: {'files': 239, 'buyer_findings_verified': 89922, 'buyer_findings_verified_on_archive_copy': 5739, 'buyer_findings_not_found_on_page': 2660, 'buyer_findings_unverified_page_unavailable': 888, 'buyer_findings_rejected_personal_or_invalid': 67, 'buyer_findings_not_found_on_page_hidden': 363, 'vendor_emails_not_found_on_page': 418, 'vendor_emails_not_found_on_page_hidden': 420, 'vendor_emails_verified': 4410, 'vendor_emails_unverified_page_unavailable': 347, 'verify_tasks_chatgpt': 224, 'verify_tasks_gemini': 374}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1270 | 0 | 0 | 14 | 0 | 24 | 0 |
| claude | 85029 | 0 | 0 | 565 | 9 | 1558 | 66 |
| gemini | 3623 | 0 | 0 | 309 | 354 | 1078 | 1 |
