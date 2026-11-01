# Ingest report — 2026-11-01T17:32:34Z

- buyers with team findings: 21216 (with at least one verified e-mail/portal: 19955)
- vendors with team findings: 15387
- QA rows: 200
- counters: {'files': 203, 'buyer_findings_verified': 25361, 'buyer_findings_unverified_page_unavailable': 683, 'buyer_findings_not_found_on_page': 1529, 'buyer_findings_not_found_on_page_hidden': 334, 'buyer_findings_rejected_personal_or_invalid': 60, 'vendor_emails_not_found_on_page': 404, 'vendor_emails_not_found_on_page_hidden': 420, 'vendor_emails_verified': 4338, 'vendor_emails_unverified_page_unavailable': 318, 'buyer_findings_cross_verified': 70, 'verify_tasks_gemini': 932, 'verify_tasks_chatgpt': 15}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 966 | 17 | 0 | 19 | 1 | 22 | 0 |
| claude | 22039 | 24 | 0 | 432 | 6 | 729 | 60 |
| gemini | 2356 | 29 | 0 | 162 | 327 | 778 | 0 |
