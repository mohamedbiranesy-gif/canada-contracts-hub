# Ingest report — 2026-11-07T18:23:42Z

- buyers with team findings: 76340 (with at least one verified e-mail/portal: 69699)
- vendors with team findings: 15497
- QA rows: 200
- counters: {'files': 238, 'buyer_findings_verified': 84862, 'buyer_findings_verified_on_archive_copy': 793, 'buyer_findings_not_found_on_page': 2656, 'buyer_findings_unverified_page_unavailable': 5667, 'buyer_findings_not_found_on_page_hidden': 524, 'buyer_findings_rejected_personal_or_invalid': 67, 'vendor_emails_not_found_on_page': 418, 'vendor_emails_not_found_on_page_hidden': 421, 'vendor_emails_verified': 4400, 'vendor_emails_unverified_page_unavailable': 356, 'buyer_findings_cross_verified': 210, 'verify_tasks_chatgpt': 278, 'verify_tasks_gemini': 615}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1236 | 16 | 0 | 29 | 3 | 24 | 0 |
| claude | 80206 | 92 | 0 | 5114 | 71 | 1554 | 66 |
| gemini | 3420 | 102 | 0 | 392 | 372 | 1078 | 1 |
