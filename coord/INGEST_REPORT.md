# Ingest report — 2026-10-26T20:32:40Z

- buyers with team findings: 803 (with at least one verified e-mail/portal: 671)
- vendors with team findings: 0
- QA rows: 200
- counters: {'files': 7, 'buyer_findings_verified': 904, 'buyer_findings_unverified_page_unavailable': 24, 'buyer_findings_not_found_on_page': 5, 'buyer_findings_not_found_on_page_hidden': 6, 'buyer_findings_cross_verified': 2, 'verify_tasks_gemini': 19, 'verify_tasks_chatgpt': 5}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|
| chatgpt | 170 | 1 | 2 | 0 | 2 | 0 |
| claude | 705 | 1 | 19 | 0 | 3 | 0 |
| gemini | 29 | 0 | 1 | 6 | 0 | 0 |
