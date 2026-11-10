# Ingest report — 2026-11-10T17:37:09Z

- buyers with team findings: 246612 (with at least one verified e-mail/portal: 235250)
- vendors with team findings: 15607
- QA rows: 200
- counters: {'files': 282, 'buyer_findings_verified': 262766, 'buyer_findings_verified_on_archive_copy': 11786, 'buyer_findings_not_found_on_page': 2903, 'buyer_findings_pending_verification': 6966, 'buyer_findings_unverified_page_unavailable': 3196, 'buyer_findings_not_found_on_page_hidden': 474, 'buyer_findings_rejected_personal_or_invalid': 822, 'vendor_emails_not_found_on_page': 421, 'vendor_emails_not_found_on_page_hidden': 426, 'vendor_emails_verified': 4450, 'vendor_emails_unverified_page_unavailable': 331, 'vendor_emails_pending_verification': 1, 'buyer_findings_cross_verified': 13, 'verify_tasks_chatgpt': 112, 'verify_tasks_gemini': 2686, 'verify_tasks_jules': 7}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv` (lane claude: `verification_log_claude.csv` and its parts). Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 1592 | 5 | 19 | 42 | 1 | 44 | 0 |
| claude | 256384 | 1 | 6902 | 2842 | 15 | 1701 | 821 |
| codex | 229 | 0 | 4 | 13 | 0 | 4 | 0 |
| gemini | 4561 | 7 | 41 | 286 | 458 | 1154 | 1 |
