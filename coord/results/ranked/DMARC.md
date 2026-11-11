# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 113029 | 223 |
| v=DMARC1; p=none (monitor only) | 108660 | 587 |
| p=quarantine | 35041 | 594 |
| p=reject | 17505 | 601 |
| invalid DMARC record | 215 | 1 |
| lookup error | 84 | 0 |

Rows without enforcement (no record / p=none / invalid): **221904**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 205 / 215
- P01M: 27 / 31 / 37 / 31
- P01T: 65 / 143 / 130 / 89
- P02: 57 / 174 / 139 / 101
- P03: 2 / 60 / 83 / 112
- P04: 784 / 1495 / 947 / 627
- P05: 53 / 140 / 131 / 97
- P06: 20 / 88 / 79 / 110
- P06M: 5014 / 4563 / 2386 / 1217
- P06T: 32728 / 36015 / 10820 / 4828
- P07: 187 / 288 / 182 / 145
- P08: 8219 / 10485 / 4479 / 2416
- P09: 56 / 96 / 99 / 42
- P10: 620 / 995 / 577 / 455
- P10R: 50431 / 36827 / 10565 / 4739
- P11: 6403 / 11353 / 1994 / 1188
- P12: 2 / 4 / 0 / 1
- P13: 8336 / 5723 / 2188 / 1092
