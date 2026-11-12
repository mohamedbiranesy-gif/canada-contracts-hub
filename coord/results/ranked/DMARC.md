# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 105607 | 218 |
| v=DMARC1; p=none (monitor only) | 101626 | 588 |
| p=quarantine | 35447 | 576 |
| p=reject | 17182 | 573 |
| invalid DMARC record | 190 | 1 |
| lookup error | 89 | 0 |

Rows without enforcement (no record / p=none / invalid): **207423**

## By package (no record / p=none / quarantine / reject)
- P01: 22 / 184 / 204 / 215
- P01M: 40 / 60 / 58 / 60
- P01T: 19 / 74 / 61 / 43
- P02: 54 / 163 / 143 / 108
- P03: 3 / 66 / 88 / 107
- P04: 705 / 1366 / 900 / 593
- P05: 52 / 140 / 132 / 100
- P06: 20 / 73 / 63 / 94
- P06M: 7009 / 7120 / 3809 / 2140
- P06T: 18013 / 18250 / 4815 / 2408
- P07: 172 / 244 / 147 / 115
- P08: 7473 / 9297 / 3876 / 2112
- P09: 51 / 89 / 91 / 43
- P10: 505 / 774 / 461 / 392
- P11: 471 / 645 / 280 / 214
- P12: 2 / 8 / 0 / 1
- P13: 70996 / 63073 / 20319 / 8437
