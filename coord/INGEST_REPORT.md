# Ingest report — 2026-11-01T11:42:33Z

- buyers with team findings: 15617 (with at least one verified e-mail/portal: 14858)
- vendors with team findings: 15017
- QA rows: 200
- counters: {'files': 194, 'buyer_findings_verified': 18880, 'buyer_findings_pending_verification': 468, 'buyer_findings_not_found_on_page': 821, 'buyer_findings_not_found_on_page_hidden': 309, 'buyer_findings_rejected_personal_or_invalid': 24, 'vendor_emails_not_found_on_page': 390, 'vendor_emails_not_found_on_page_hidden': 410, 'vendor_emails_verified': 4197, 'vendor_emails_pending_verification': 353, 'verify_tasks_chatgpt': 15, 'verify_tasks_gemini': 343}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 966 | 0 | 36 | 0 | 1 | 22 | 0 |
| claude | 15632 | 0 | 162 | 0 | 5 | 434 | 24 |
| gemini | 2282 | 0 | 270 | 0 | 303 | 365 | 0 |
