# Ingest report — 2026-11-05T03:47:29Z

- buyers with team findings: 69534 (with at least one verified e-mail/portal: 66968)
- vendors with team findings: 15387
- QA rows: 200
- counters: {'files': 234, 'buyer_findings_verified': 81999, 'buyer_findings_verified_on_archive_copy': 635, 'buyer_findings_not_found_on_page': 2480, 'buyer_findings_unverified_page_unavailable': 1351, 'buyer_findings_not_found_on_page_hidden': 474, 'buyer_findings_rejected_personal_or_invalid': 83, 'vendor_emails_not_found_on_page': 405, 'vendor_emails_not_found_on_page_hidden': 423, 'vendor_emails_verified': 4347, 'vendor_emails_unverified_page_unavailable': 305, 'buyer_findings_cross_verified': 198, 'verify_tasks_chatgpt': 215, 'verify_tasks_gemini': 340}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 976 | 15 | 0 | 12 | 0 | 22 | 0 |
| claude | 77492 | 88 | 0 | 923 | 7 | 1416 | 82 |
| gemini | 3531 | 95 | 0 | 319 | 366 | 1042 | 1 |
