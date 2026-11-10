# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 24231 | 97 |
| v=DMARC1; p=none (monitor only) | 31072 | 414 |
| p=quarantine | 11944 | 456 |
| p=reject | 6192 | 501 |
| invalid DMARC record | 65 | 0 |
| lookup error | 11 | 0 |

Rows without enforcement (no record / p=none / invalid): **55368**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 179 / 207 / 215
- P01M: 10 / 7 / 16 / 11
- P01T: 9 / 39 / 54 / 37
- P02: 49 / 148 / 120 / 86
- P03: 0 / 47 / 71 / 91
- P04: 246 / 554 / 492 / 275
- P05: 54 / 126 / 115 / 82
- P06: 15 / 73 / 75 / 113
- P06M: 1749 / 1489 / 723 / 349
- P06T: 3124 / 4247 / 1472 / 704
- P07: 68 / 207 / 131 / 122
- P08: 2967 / 4759 / 2157 / 1155
- P09: 68 / 119 / 109 / 50
- P10: 602 / 1075 / 576 / 325
- P10R: 10217 / 11916 / 3374 / 1469
- P11: 621 / 1783 / 490 / 274
- P12: 2 / 4 / 0 / 2
- P13: 4405 / 4300 / 1762 / 832
