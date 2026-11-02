# Ingest report — 2026-11-02T04:18:54Z

- buyers with team findings: 29701 (with at least one verified e-mail/portal: 27619)
- vendors with team findings: 15387
- QA rows: 200
- counters: {'files': 218, 'buyer_findings_verified': 42077, 'buyer_findings_verified_on_archive_copy': 265, 'buyer_findings_unverified_page_unavailable': 1299, 'buyer_findings_not_found_on_page': 2687, 'buyer_findings_not_found_on_page_hidden': 425, 'buyer_findings_rejected_personal_or_invalid': 75, 'vendor_emails_not_found_on_page': 404, 'vendor_emails_not_found_on_page_hidden': 420, 'vendor_emails_verified': 4339, 'vendor_emails_unverified_page_unavailable': 317, 'buyer_findings_cross_verified': 206, 'verify_tasks_chatgpt': 112, 'verify_tasks_gemini': 451}
- QA tallies: {'buyer_match=yes': 181, 'vendor_match=yes': 173, 'title_match=yes': 181, 'value_match=yes': 120, 'dates_match=yes': 83, 'status_supported=yes': 89, 'dates_match=not_shown': 109, 'buyer_match=not_shown': 14, 'vendor_match=not_shown': 27, 'title_match=not_shown': 13, 'value_match=not_shown': 77, 'status_supported=unclear': 100, 'dates_match=no': 8, 'title_match=no': 6, 'buyer_match=no': 5, 'value_match=no': 3, 'status_supported=no': 11}

## Outcome of each lane's buyer findings
Every row's outcome is in `coord/results/verification_log.csv`. Look up your own rows there.

| lane | verified | cross_verified | waiting to be checked | page unavailable | e-mails hidden from verifier | not on page | rejected |
|---|---|---|---|---|---|---|---|
| chatgpt | 973 | 16 | 0 | 14 | 0 | 22 | 0 |
| claude | 38231 | 92 | 0 | 926 | 7 | 1681 | 74 |
| gemini | 2873 | 98 | 0 | 251 | 320 | 984 | 1 |
