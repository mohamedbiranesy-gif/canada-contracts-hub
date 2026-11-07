# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 17631 | 89 |
| v=DMARC1; p=none (monitor only) | 20846 | 356 |
| p=quarantine | 9013 | 404 |
| p=reject | 4780 | 447 |
| invalid DMARC record | 45 | 0 |
| lookup error | 7 | 0 |
| not checked | 11023 | 45 |

Rows without enforcement (no record / p=none / invalid): **38522**

## By package (no record / p=none / quarantine / reject)
- P01: 24 / 165 / 192 / 197
- P01M: 3 / 2 / 5 / 8
- P01T: 4 / 25 / 37 / 25
- P02: 44 / 133 / 112 / 79
- P03: 0 / 49 / 83 / 95
- P04: 281 / 548 / 504 / 288
- P05: 58 / 125 / 115 / 81
- P06: 2 / 29 / 45 / 84
- P06M: 32 / 60 / 37 / 39
- P06T: 685 / 1134 / 366 / 236
- P07: 17 / 85 / 69 / 75
- P08: 714 / 1180 / 721 / 428
- P09: 88 / 121 / 106 / 51
- P10: 652 / 1088 / 560 / 301
- P11: 42 / 217 / 117 / 82
- P12: 4 / 11 / 4 / 3
- P13: 14981 / 15874 / 5940 / 2708
