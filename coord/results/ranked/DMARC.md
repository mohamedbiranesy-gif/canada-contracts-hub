# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 102712 | 213 |
| v=DMARC1; p=none (monitor only) | 96581 | 563 |
| p=quarantine | 31983 | 583 |
| p=reject | 15909 | 586 |
| invalid DMARC record | 195 | 1 |
| lookup error | 75 | 0 |

Rows without enforcement (no record / p=none / invalid): **199488**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 205 / 215
- P01M: 26 / 31 / 37 / 32
- P01T: 56 / 117 / 119 / 78
- P02: 57 / 174 / 139 / 101
- P03: 2 / 59 / 84 / 112
- P04: 772 / 1491 / 941 / 629
- P05: 53 / 142 / 132 / 97
- P06: 21 / 88 / 80 / 107
- P06M: 4842 / 4535 / 2372 / 1241
- P06T: 25982 / 28336 / 8864 / 3786
- P07: 189 / 288 / 182 / 140
- P08: 8175 / 10571 / 4465 / 2389
- P09: 56 / 96 / 99 / 42
- P10: 630 / 1017 / 583 / 454
- P10R: 48827 / 35284 / 9925 / 4464
- P11: 4504 / 8143 / 1436 / 880
- P12: 2 / 4 / 0 / 1
- P13: 8493 / 6025 / 2320 / 1141
