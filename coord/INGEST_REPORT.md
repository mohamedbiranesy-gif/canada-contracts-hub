# Ingest report — 2026-10-27T06:04:07Z

- buyers with team findings: 2264 (with at least one verified e-mail/portal: 1512)
- vendors with team findings: 0
- QA rows: 200
- counters: {'files': 24, 'buyer_findings_verified': 1909, 'buyer_findings_unverified_page_unavailable': 111, 'buyer_findings_not_found_on_page': 98, 'buyer_findings_not_found_on_page_hidden': 118, 'buyer_findings_cross_verified': 22, 'verify_tasks_gemini': 18, 'verify_tasks_chatgpt': 241}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|
| chatgpt | 326 | 1 | 8 | 0 | 7 | 0 |
| claude | 722 | 10 | 11 | 0 | 3 | 0 |
| gemini | 861 | 11 | 70 | 118 | 88 | 0 |
