# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 17617 | 88 |
| v=DMARC1; p=none (monitor only) | 20820 | 357 |
| p=quarantine | 9010 | 404 |
| p=reject | 4777 | 447 |
| invalid DMARC record | 45 | 0 |
| lookup error | 6 | 0 |
| not checked | 3639 | 11 |

Rows without enforcement (no record / p=none / invalid): **38482**

## By package (no record / p=none / quarantine / reject)
- P01: 23 / 165 / 194 / 197
- P01M: 3 / 2 / 5 / 8
- P01T: 4 / 25 / 37 / 24
- P02: 44 / 132 / 110 / 80
- P03: 0 / 49 / 81 / 95
- P04: 277 / 521 / 488 / 282
- P05: 57 / 126 / 113 / 79
- P06: 2 / 29 / 45 / 84
- P06M: 32 / 60 / 37 / 39
- P06T: 686 / 1134 / 365 / 236
- P07: 17 / 85 / 68 / 75
- P08: 714 / 1187 / 722 / 431
- P09: 86 / 121 / 106 / 49
- P10: 652 / 1088 / 561 / 301
- P11: 43 / 212 / 121 / 81
- P12: 4 / 11 / 4 / 3
- P13: 14973 / 15873 / 5953 / 2713
