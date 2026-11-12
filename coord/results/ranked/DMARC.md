# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 71421 | 183 |
| v=DMARC1; p=none (monitor only) | 71240 | 542 |
| p=quarantine | 25785 | 543 |
| p=reject | 13092 | 544 |
| invalid DMARC record | 142 | 1 |
| lookup error | 404 | 1 |
| not checked | 24801 | 46 |

Rows without enforcement (no record / p=none / invalid): **142803**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 206 / 215
- P01M: 28 / 34 / 36 / 31
- P01T: 21 / 75 / 55 / 40
- P02: 56 / 167 / 139 / 103
- P03: 2 / 63 / 86 / 112
- P04: 747 / 1431 / 904 / 598
- P05: 53 / 141 / 129 / 98
- P06: 17 / 80 / 67 / 105
- P06M: 5598 / 5243 / 2616 / 1297
- P06T: 14274 / 15303 / 4365 / 2097
- P07: 166 / 240 / 155 / 127
- P08: 7102 / 8926 / 3761 / 2063
- P09: 60 / 99 / 102 / 44
- P10: 559 / 854 / 505 / 418
- P11: 372 / 608 / 269 / 208
- P12: 4 / 8 / 2 / 1
- P13: 42337 / 37788 / 12388 / 5535
