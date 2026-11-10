# Ingest report — 2026-11-10T02:51:38Z

- buyers with team findings: 78605 (with at least one verified e-mail/portal: 76284)
- vendors with team findings: 15607
- QA rows: 200
- counters: {'files': 274, 'buyer_findings_verified': 96931, 'buyer_findings_verified_on_archive_copy': 5854, 'buyer_findings_not_found_on_page': 2792, 'buyer_findings_unverified_page_unavailable': 1090, 'buyer_findings_not_found_on_page_hidden': 470, 'buyer_findings_rejected_personal_or_invalid': 70, 'vendor_emails_not_found_on_page': 418, 'vendor_emails_not_found_on_page_hidden': 426, 'vendor_emails_verified': 4433, 'vendor_emails_unverified_page_unavailable': 352, 'buyer_findings_cross_verified': 13, 'verify_tasks_chatgpt': 111, 'verify_tasks_gemini': 438, 'verify_tasks_jules': 9}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1592 | 5 | 0 | 61 | 1 | 44 | 0 |
| claude | 90550 | 1 | 0 | 668 | 12 | 1592 | 69 |
| codex | 229 | 0 | 0 | 17 | 0 | 4 | 0 |
| gemini | 4560 | 7 | 0 | 331 | 457 | 1152 | 1 |
