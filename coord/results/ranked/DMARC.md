# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 136096 | 278 |
| v=DMARC1; p=none (monitor only) | 128902 | 667 |
| p=quarantine | 44784 | 650 |
| p=reject | 21537 | 637 |
| invalid DMARC record | 251 | 1 |
| lookup error | 122 | 0 |

Rows without enforcement (no record / p=none / invalid): **265249**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 196 / 208 / 224
- P01M: 58 / 113 / 124 / 125
- P01T: 35 / 69 / 59 / 40
- P02: 59 / 165 / 153 / 112
- P03: 4 / 72 / 92 / 108
- P04: 968 / 1760 / 1259 / 800
- P05: 53 / 143 / 132 / 101
- P06: 28 / 72 / 58 / 87
- P06M: 9672 / 10786 / 6191 / 3816
- P06T: 22698 / 23339 / 6145 / 2501
- P07: 216 / 278 / 160 / 119
- P08: 10022 / 11891 / 4745 / 2534
- P09: 50 / 90 / 91 / 43
- P10: 479 / 735 / 434 / 368
- P11: 569 / 710 / 307 / 219
- P12: 2 / 8 / 0 / 1
- P13: 91158 / 78475 / 24626 / 10339
