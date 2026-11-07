# Ingest report — 2026-11-07T02:59:22Z

- buyers with team findings: 76340 (with at least one verified e-mail/portal: 73747)
- vendors with team findings: 15497
- QA rows: 200
- counters: {'files': 238, 'buyer_findings_verified': 89300, 'buyer_findings_verified_on_archive_copy': 873, 'buyer_findings_not_found_on_page': 2537, 'buyer_findings_unverified_page_unavailable': 1313, 'buyer_findings_not_found_on_page_hidden': 477, 'buyer_findings_rejected_personal_or_invalid': 66, 'vendor_emails_not_found_on_page': 410, 'vendor_emails_not_found_on_page_hidden': 429, 'vendor_emails_verified': 4441, 'vendor_emails_unverified_page_unavailable': 315, 'buyer_findings_cross_verified': 199, 'verify_tasks_chatgpt': 213, 'verify_tasks_gemini': 342}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1259 | 15 | 0 | 12 | 0 | 22 | 0 |
| claude | 84498 | 88 | 0 | 892 | 8 | 1469 | 65 |
| gemini | 3543 | 96 | 0 | 312 | 367 | 1046 | 1 |
