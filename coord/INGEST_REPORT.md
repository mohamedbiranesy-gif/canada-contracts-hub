# Ingest report — 2026-11-08T21:28:22Z

- buyers with team findings: 76856 (with at least one verified e-mail/portal: 74551)
- vendors with team findings: 15497
- QA rows: 200
- counters: {'files': 257, 'buyer_findings_verified': 92694, 'buyer_findings_verified_on_archive_copy': 5804, 'buyer_findings_not_found_on_page': 2723, 'buyer_findings_unverified_page_unavailable': 1001, 'buyer_findings_rejected_personal_or_invalid': 69, 'buyer_findings_not_found_on_page_hidden': 403, 'vendor_emails_not_found_on_page': 418, 'vendor_emails_not_found_on_page_hidden': 420, 'vendor_emails_verified': 4411, 'vendor_emails_unverified_page_unavailable': 346, 'buyer_findings_cross_verified': 11, 'verify_tasks_chatgpt': 140, 'verify_tasks_gemini': 435}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1310 | 5 | 0 | 40 | 0 | 43 | 0 |
| claude | 87331 | 0 | 0 | 628 | 12 | 1576 | 68 |
| codex | 17 | 0 | 0 | 0 | 0 | 0 | 0 |
| gemini | 4036 | 6 | 0 | 322 | 391 | 1104 | 1 |
