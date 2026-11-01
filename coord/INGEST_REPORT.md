# Ingest report — 2026-11-01T15:56:48Z

- buyers with team findings: 19374 (with at least one verified e-mail/portal: 18058)
- vendors with team findings: 15297
- QA rows: 200
- counters: {'files': 199, 'buyer_findings_verified': 22580, 'buyer_findings_pending_verification': 835, 'buyer_findings_not_found_on_page': 1275, 'buyer_findings_not_found_on_page_hidden': 323, 'buyer_findings_rejected_personal_or_invalid': 56, 'vendor_emails_not_found_on_page': 402, 'vendor_emails_not_found_on_page_hidden': 420, 'vendor_emails_verified': 4305, 'vendor_emails_pending_verification': 317, 'verify_tasks_chatgpt': 16, 'verify_tasks_gemini': 515}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 966 | 0 | 36 | 0 | 1 | 22 | 0 |
| claude | 19306 | 0 | 617 | 0 | 5 | 645 | 56 |
| gemini | 2308 | 0 | 182 | 0 | 317 | 608 | 0 |
