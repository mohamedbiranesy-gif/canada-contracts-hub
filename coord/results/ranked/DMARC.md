# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 71740 | 184 |
| v=DMARC1; p=none (monitor only) | 71557 | 546 |
| p=quarantine | 25900 | 546 |
| p=reject | 13138 | 548 |
| invalid DMARC record | 143 | 1 |
| lookup error | 433 | 0 |
| not checked | 24074 | 46 |

Rows without enforcement (no record / p=none / invalid): **143440**

## By package (no record / p=none / quarantine / reject)
- P01: 26 / 184 / 208 / 217
- P01M: 28 / 34 / 36 / 31
- P01T: 21 / 75 / 55 / 40
- P02: 56 / 167 / 139 / 103
- P03: 2 / 63 / 86 / 112
- P04: 747 / 1432 / 906 / 599
- P05: 53 / 141 / 129 / 98
- P06: 17 / 79 / 67 / 106
- P06M: 5610 / 5254 / 2621 / 1297
- P06T: 14306 / 15329 / 4375 / 2104
- P07: 166 / 240 / 155 / 127
- P08: 7103 / 8934 / 3762 / 2063
- P09: 60 / 99 / 102 / 44
- P10: 560 / 856 / 505 / 419
- P11: 372 / 607 / 268 / 209
- P12: 4 / 8 / 2 / 1
- P13: 42609 / 38055 / 12484 / 5568
