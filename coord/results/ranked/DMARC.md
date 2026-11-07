# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 20057 | 87 |
| v=DMARC1; p=none (monitor only) | 24342 | 370 |
| p=quarantine | 10031 | 419 |
| p=reject | 5198 | 451 |
| invalid DMARC record | 57 | 0 |
| lookup error | 8 | 0 |
| not checked | 24 | 0 |

Rows without enforcement (no record / p=none / invalid): **44456**

## By package (no record / p=none / quarantine / reject)
- P01: 22 / 164 / 189 / 188
- P01M: 2 / 3 / 5 / 8
- P01T: 3 / 25 / 38 / 25
- P02: 39 / 131 / 106 / 77
- P03: 0 / 51 / 81 / 92
- P04: 252 / 555 / 489 / 278
- P05: 56 / 124 / 110 / 78
- P06: 2 / 28 / 43 / 81
- P06M: 29 / 61 / 36 / 38
- P06T: 658 / 1127 / 359 / 219
- P07: 15 / 79 / 66 / 76
- P08: 679 / 1180 / 708 / 421
- P09: 70 / 125 / 108 / 50
- P10: 618 / 1078 / 547 / 290
- P11: 80 / 324 / 198 / 160
- P12: 4 / 9 / 3 / 3
- P13: 17528 / 19278 / 6945 / 3114
