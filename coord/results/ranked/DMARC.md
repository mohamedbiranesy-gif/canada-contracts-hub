# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 91432 | 198 |
| v=DMARC1; p=none (monitor only) | 89056 | 574 |
| p=quarantine | 31314 | 563 |
| p=reject | 15419 | 568 |
| invalid DMARC record | 177 | 1 |
| lookup error | 546 | 0 |
| not checked | 30653 | 76 |

Rows without enforcement (no record / p=none / invalid): **180665**

## By package (no record / p=none / quarantine / reject)
- P01: 26 / 186 / 210 / 221
- P01M: 29 / 47 / 42 / 46
- P01T: 20 / 71 / 57 / 40
- P02: 55 / 169 / 139 / 108
- P03: 2 / 68 / 90 / 110
- P04: 716 / 1381 / 926 / 596
- P05: 53 / 139 / 132 / 100
- P06: 16 / 77 / 65 / 95
- P06M: 5947 / 5838 / 3055 / 1640
- P06T: 15313 / 16025 / 4349 / 2145
- P07: 169 / 238 / 149 / 118
- P08: 6993 / 8782 / 3675 / 2010
- P09: 61 / 103 / 102 / 46
- P10: 508 / 773 / 462 / 392
- P11: 420 / 626 / 274 / 205
- P12: 4 / 9 / 2 / 1
- P13: 61100 / 54524 / 17585 / 7546
