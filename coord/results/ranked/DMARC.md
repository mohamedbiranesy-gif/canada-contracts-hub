# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 21972 | 102 |
| v=DMARC1; p=none (monitor only) | 25588 | 368 |
| p=quarantine | 10322 | 416 |
| p=reject | 5343 | 454 |
| invalid DMARC record | 57 | 0 |
| lookup error | 11 | 0 |
| not checked | 12 | 0 |

Rows without enforcement (no record / p=none / invalid): **47617**

## By package (no record / p=none / quarantine / reject)
- P01: 24 / 166 / 193 / 197
- P01M: 3 / 2 / 5 / 8
- P01T: 4 / 25 / 37 / 25
- P02: 42 / 129 / 108 / 76
- P03: 0 / 48 / 80 / 93
- P04: 275 / 541 / 499 / 287
- P05: 58 / 125 / 115 / 81
- P06: 2 / 29 / 44 / 84
- P06M: 32 / 62 / 37 / 39
- P06T: 686 / 1132 / 364 / 235
- P07: 17 / 85 / 69 / 75
- P08: 711 / 1174 / 720 / 428
- P09: 86 / 115 / 105 / 50
- P10: 649 / 1085 / 559 / 300
- P11: 59 / 247 / 139 / 93
- P12: 4 / 11 / 3 / 3
- P13: 19320 / 20612 / 7245 / 3269
