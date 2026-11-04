# Ingest report — 2026-11-04T18:03:45Z

- buyers with team findings: 63913 (with at least one verified e-mail/portal: 61119)
- vendors with team findings: 15387
- QA rows: 200
- counters: {'files': 234, 'buyer_findings_verified': 75730, 'buyer_findings_verified_on_archive_copy': 377, 'buyer_findings_unverified_page_unavailable': 1683, 'buyer_findings_not_found_on_page': 2472, 'buyer_findings_not_found_on_page_hidden': 474, 'buyer_findings_rejected_personal_or_invalid': 83, 'vendor_emails_not_found_on_page': 405, 'vendor_emails_not_found_on_page_hidden': 423, 'vendor_emails_verified': 4347, 'vendor_emails_unverified_page_unavailable': 305, 'buyer_findings_cross_verified': 217, 'verify_tasks_chatgpt': 216, 'verify_tasks_gemini': 547}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 974 | 16 | 0 | 13 | 0 | 22 | 0 |
| claude | 71236 | 97 | 0 | 1232 | 7 | 1409 | 82 |
| gemini | 3520 | 104 | 0 | 322 | 366 | 1041 | 1 |
