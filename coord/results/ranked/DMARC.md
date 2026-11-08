# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 21272 | 91 |
| v=DMARC1; p=none (monitor only) | 26434 | 378 |
| p=quarantine | 10433 | 426 |
| p=reject | 5404 | 474 |
| invalid DMARC record | 59 | 0 |
| lookup error | 7 | 0 |

Rows without enforcement (no record / p=none / invalid): **47765**

## By package (no record / p=none / quarantine / reject)
- P01: 24 / 171 / 196 / 206
- P01M: 1 / 3 / 5 / 9
- P01T: 3 / 26 / 37 / 26
- P02: 45 / 148 / 124 / 82
- P03: 0 / 51 / 77 / 95
- P04: 252 / 554 / 490 / 276
- P05: 56 / 125 / 116 / 82
- P06: 2 / 29 / 45 / 89
- P06M: 32 / 63 / 37 / 36
- P06T: 673 / 1153 / 372 / 240
- P07: 15 / 88 / 73 / 76
- P08: 690 / 1194 / 720 / 431
- P09: 71 / 134 / 114 / 53
- P10: 628 / 1096 / 565 / 305
- P11: 41 / 231 / 121 / 82
- P12: 4 / 11 / 3 / 3
- P13: 18735 / 21357 / 7338 / 3313
