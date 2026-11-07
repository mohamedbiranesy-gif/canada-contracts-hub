# Ingest report — 2026-11-07T11:56:19Z

- buyers with team findings: 76340 (with at least one verified e-mail/portal: 69632)
- vendors with team findings: 15497
- QA rows: 200
- counters: {'files': 238, 'buyer_findings_verified': 84726, 'buyer_findings_verified_on_archive_copy': 657, 'buyer_findings_unverified_page_unavailable': 5729, 'buyer_findings_not_found_on_page': 2654, 'buyer_findings_pending_verification': 76, 'buyer_findings_not_found_on_page_hidden': 524, 'buyer_findings_rejected_personal_or_invalid': 67, 'vendor_emails_not_found_on_page': 418, 'vendor_emails_not_found_on_page_hidden': 421, 'vendor_emails_verified': 4399, 'vendor_emails_unverified_page_unavailable': 356, 'vendor_emails_pending_verification': 1, 'buyer_findings_cross_verified': 240, 'verify_tasks_chatgpt': 281, 'verify_tasks_gemini': 639}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1227 | 22 | 10 | 22 | 3 | 24 | 0 |
| claude | 80117 | 103 | 20 | 5173 | 71 | 1553 | 66 |
| gemini | 3382 | 115 | 46 | 372 | 372 | 1077 | 1 |
