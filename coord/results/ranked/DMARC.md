# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 17585 | 88 |
| v=DMARC1; p=none (monitor only) | 20793 | 357 |
| p=quarantine | 9002 | 405 |
| p=reject | 4773 | 447 |
| invalid DMARC record | 44 | 0 |
| lookup error | 6 | 0 |
| not checked | 417 | 2 |

Rows without enforcement (no record / p=none / invalid): **38422**

## By package (no record / p=none / quarantine / reject)
- P01: 23 / 154 / 192 / 195
- P01M: 3 / 2 / 5 / 8
- P01T: 4 / 25 / 37 / 24
- P02: 43 / 114 / 105 / 76
- P03: 0 / 49 / 82 / 95
- P04: 277 / 524 / 485 / 281
- P05: 57 / 126 / 113 / 79
- P06: 2 / 29 / 45 / 84
- P06M: 32 / 60 / 37 / 39
- P06T: 686 / 1133 / 365 / 237
- P07: 17 / 85 / 68 / 75
- P08: 714 / 1185 / 722 / 430
- P09: 86 / 121 / 106 / 49
- P10: 650 / 1087 / 560 / 301
- P11: 46 / 243 / 129 / 86
- P12: 4 / 11 / 4 / 3
- P13: 14941 / 15845 / 5947 / 2711
