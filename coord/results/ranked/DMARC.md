# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 106502 | 218 |
| v=DMARC1; p=none (monitor only) | 101858 | 576 |
| p=quarantine | 33382 | 588 |
| p=reject | 16632 | 592 |
| invalid DMARC record | 202 | 1 |
| lookup error | 85 | 0 |

Rows without enforcement (no record / p=none / invalid): **208562**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 205 / 215
- P01M: 27 / 31 / 36 / 31
- P01T: 61 / 130 / 124 / 83
- P02: 57 / 174 / 139 / 101
- P03: 2 / 60 / 83 / 112
- P04: 773 / 1485 / 944 / 625
- P05: 53 / 140 / 132 / 97
- P06: 20 / 87 / 80 / 107
- P06M: 4928 / 4549 / 2361 / 1235
- P06T: 28257 / 31799 / 9789 / 4288
- P07: 190 / 286 / 183 / 140
- P08: 8176 / 10490 / 4458 / 2385
- P09: 56 / 96 / 99 / 42
- P10: 626 / 994 / 573 / 448
- P10R: 49539 / 36047 / 10272 / 4603
- P11: 5286 / 9429 / 1667 / 1009
- P12: 2 / 4 / 0 / 1
- P13: 8424 / 5877 / 2237 / 1110
