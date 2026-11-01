# Ingest report — 2026-11-01T13:46:54Z

- buyers with team findings: 18736 (with at least one verified e-mail/portal: 17804)
- vendors with team findings: 15297
- QA rows: 200
- counters: {'files': 197, 'buyer_findings_verified': 22216, 'buyer_findings_unverified_page_unavailable': 195, 'buyer_findings_not_found_on_page': 1276, 'buyer_findings_not_found_on_page_hidden': 323, 'buyer_findings_rejected_personal_or_invalid': 26, 'buyer_findings_pending_verification': 185, 'vendor_emails_not_found_on_page': 399, 'vendor_emails_not_found_on_page_hidden': 420, 'vendor_emails_verified': 4304, 'vendor_emails_pending_verification': 321, 'buyer_findings_cross_verified': 4, 'verify_tasks_gemini': 638, 'verify_tasks_chatgpt': 15}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 966 | 2 | 0 | 34 | 1 | 22 | 0 |
| claude | 18942 | 2 | 3 | 157 | 5 | 646 | 26 |
| gemini | 2308 | 0 | 182 | 0 | 317 | 608 | 0 |
