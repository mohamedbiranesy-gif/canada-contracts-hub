# Ingest report — 2026-11-01T19:21:49Z

- buyers with team findings: 21236 (with at least one verified e-mail/portal: 20189)
- vendors with team findings: 15387
- QA rows: 200
- counters: {'files': 205, 'buyer_findings_verified': 25919, 'buyer_findings_unverified_page_unavailable': 500, 'buyer_findings_verified_on_archive_copy': 243, 'buyer_findings_not_found_on_page': 1689, 'buyer_findings_not_found_on_page_hidden': 360, 'buyer_findings_rejected_personal_or_invalid': 60, 'vendor_emails_not_found_on_page': 404, 'vendor_emails_not_found_on_page_hidden': 420, 'vendor_emails_verified': 4339, 'vendor_emails_unverified_page_unavailable': 317, 'buyer_findings_cross_verified': 159, 'verify_tasks_gemini': 115, 'verify_tasks_chatgpt': 10}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 970 | 15 | 0 | 17 | 1 | 22 | 0 |
| claude | 22533 | 68 | 0 | 190 | 5 | 735 | 60 |
| gemini | 2416 | 76 | 0 | 180 | 308 | 932 | 0 |
