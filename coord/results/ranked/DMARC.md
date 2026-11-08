# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 20071 | 87 |
| v=DMARC1; p=none (monitor only) | 24367 | 370 |
| p=quarantine | 10046 | 418 |
| p=reject | 5204 | 452 |
| invalid DMARC record | 57 | 0 |
| lookup error | 6 | 0 |

Rows without enforcement (no record / p=none / invalid): **44495**

## By package (no record / p=none / quarantine / reject)
- P01: 22 / 165 / 189 / 189
- P01M: 2 / 3 / 5 / 8
- P01T: 3 / 25 / 38 / 25
- P02: 41 / 136 / 111 / 80
- P03: 0 / 50 / 82 / 95
- P04: 255 / 557 / 492 / 279
- P05: 56 / 125 / 110 / 80
- P06: 2 / 28 / 44 / 83
- P06M: 30 / 62 / 37 / 38
- P06T: 660 / 1138 / 362 / 231
- P07: 15 / 84 / 69 / 75
- P08: 685 / 1189 / 712 / 427
- P09: 70 / 127 / 109 / 51
- P10: 624 / 1092 / 559 / 295
- P11: 63 / 278 / 168 / 126
- P12: 4 / 11 / 3 / 3
- P13: 17539 / 19297 / 6956 / 3119
