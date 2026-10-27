# Ingest report — 2026-10-27T12:18:14Z

- buyers with team findings: 2330 (with at least one verified e-mail/portal: 1554)
- vendors with team findings: 0
- QA rows: 200
- counters: {'files': 25, 'buyer_findings_verified': 1982, 'buyer_findings_unverified_page_unavailable': 121, 'buyer_findings_not_found_on_page': 100, 'buyer_findings_not_found_on_page_hidden': 121, 'buyer_findings_cross_verified': 34, 'verify_tasks_gemini': 22, 'verify_tasks_chatgpt': 247}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|
| chatgpt | 384 | 7 | 12 | 0 | 7 | 0 |
| claude | 722 | 10 | 11 | 0 | 3 | 0 |
| gemini | 876 | 17 | 64 | 121 | 90 | 0 |
