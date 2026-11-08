# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 20057 | 87 |
| v=DMARC1; p=none (monitor only) | 24343 | 371 |
| p=quarantine | 10031 | 419 |
| p=reject | 5197 | 451 |
| invalid DMARC record | 57 | 0 |
| lookup error | 8 | 0 |
| not checked | 25 | 0 |

Rows without enforcement (no record / p=none / invalid): **44457**

## By package (no record / p=none / quarantine / reject)
- P01: 22 / 165 / 189 / 188
- P01M: 2 / 3 / 5 / 8
- P01T: 3 / 25 / 38 / 25
- P02: 39 / 131 / 106 / 77
- P03: 0 / 50 / 81 / 92
- P04: 252 / 554 / 489 / 279
- P05: 56 / 125 / 110 / 80
- P06: 2 / 28 / 43 / 82
- P06M: 29 / 61 / 36 / 38
- P06T: 658 / 1127 / 359 / 220
- P07: 15 / 79 / 66 / 75
- P08: 682 / 1185 / 710 / 426
- P09: 70 / 126 / 108 / 50
- P10: 623 / 1091 / 555 / 295
- P11: 72 / 306 / 188 / 145
- P12: 4 / 9 / 3 / 3
- P13: 17528 / 19278 / 6945 / 3114
