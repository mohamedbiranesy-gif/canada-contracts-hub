# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 21276 | 92 |
| v=DMARC1; p=none (monitor only) | 26431 | 385 |
| p=quarantine | 10438 | 437 |
| p=reject | 5407 | 485 |
| invalid DMARC record | 59 | 0 |
| lookup error | 7 | 0 |

Rows without enforcement (no record / p=none / invalid): **47766**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 178 / 208 / 213
- P01M: 1 / 3 / 5 / 9
- P01T: 3 / 26 / 37 / 26
- P02: 49 / 146 / 120 / 86
- P03: 0 / 46 / 69 / 89
- P04: 247 / 551 / 489 / 270
- P05: 56 / 127 / 119 / 82
- P06: 2 / 29 / 45 / 90
- P06M: 32 / 63 / 37 / 36
- P06T: 676 / 1151 / 372 / 239
- P07: 15 / 88 / 73 / 76
- P08: 690 / 1194 / 720 / 431
- P09: 72 / 135 / 116 / 55
- P10: 628 / 1096 / 565 / 305
- P11: 40 / 231 / 122 / 84
- P12: 4 / 11 / 1 / 3
- P13: 18736 / 21356 / 7340 / 3313
