# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 54312 | 143 |
| v=DMARC1; p=none (monitor only) | 55862 | 489 |
| p=quarantine | 20108 | 512 |
| p=reject | 10254 | 543 |
| invalid DMARC record | 113 | 0 |
| lookup error | 34 | 0 |
| not checked | 27503 | 52 |

Rows without enforcement (no record / p=none / invalid): **110287**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 179 / 206 / 215
- P01M: 12 / 12 / 20 / 15
- P01T: 33 / 75 / 90 / 63
- P02: 52 / 169 / 137 / 98
- P03: 1 / 58 / 85 / 111
- P04: 563 / 1178 / 834 / 551
- P05: 53 / 135 / 129 / 91
- P06: 16 / 83 / 74 / 100
- P06M: 1989 / 1552 / 786 / 376
- P06T: 12679 / 14515 / 4940 / 2168
- P07: 125 / 239 / 152 / 115
- P08: 5635 / 7780 / 3426 / 1852
- P09: 58 / 100 / 101 / 42
- P10: 578 / 956 / 554 / 411
- P10R: 25963 / 21765 / 6116 / 2768
- P11: 1097 / 2531 / 654 / 396
- P12: 2 / 5 / 0 / 1
- P13: 5431 / 4530 / 1804 / 881
