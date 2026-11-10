# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 30735 | 111 |
| v=DMARC1; p=none (monitor only) | 38300 | 456 |
| p=quarantine | 15189 | 495 |
| p=reject | 8045 | 534 |
| invalid DMARC record | 79 | 0 |
| lookup error | 14 | 0 |

Rows without enforcement (no record / p=none / invalid): **69114**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 179 / 206 / 215
- P01M: 12 / 8 / 17 / 16
- P01T: 20 / 55 / 75 / 53
- P02: 50 / 160 / 127 / 92
- P03: 0 / 49 / 76 / 93
- P04: 492 / 1018 / 668 / 406
- P05: 57 / 141 / 129 / 91
- P06: 17 / 96 / 91 / 125
- P06M: 1809 / 1487 / 732 / 363
- P06T: 6780 / 8217 / 3088 / 1402
- P07: 128 / 264 / 174 / 143
- P08: 5777 / 8130 / 3676 / 2037
- P09: 58 / 104 / 105 / 43
- P10: 574 / 938 / 558 / 401
- P10R: 10091 / 11672 / 3322 / 1499
- P11: 671 / 1838 / 516 / 296
- P12: 2 / 5 / 0 / 1
- P13: 4172 / 3939 / 1629 / 769
