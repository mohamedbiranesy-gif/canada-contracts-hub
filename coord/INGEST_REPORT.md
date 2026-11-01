# Ingest report — 2026-11-01T10:40:46Z

- buyers with team findings: 15612 (with at least one verified e-mail/portal: 14854)
- vendors with team findings: 14847
- QA rows: 200
- counters: {'files': 192, 'buyer_findings_verified': 18875, 'buyer_findings_pending_verification': 398, 'buyer_findings_not_found_on_page': 660, 'buyer_findings_not_found_on_page_hidden': 309, 'buyer_findings_rejected_personal_or_invalid': 24, 'vendor_emails_not_found_on_page': 387, 'vendor_emails_not_found_on_page_hidden': 407, 'vendor_emails_verified': 4159, 'vendor_emails_pending_verification': 324, 'verify_tasks_chatgpt': 11, 'verify_tasks_gemini': 346}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 966 | 0 | 36 | 0 | 1 | 22 | 0 |
| claude | 15631 | 0 | 163 | 0 | 5 | 434 | 24 |
| gemini | 2278 | 0 | 199 | 0 | 303 | 204 | 0 |
