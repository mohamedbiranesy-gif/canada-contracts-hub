# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 85690 | 178 |
| v=DMARC1; p=none (monitor only) | 78634 | 525 |
| p=quarantine | 26738 | 533 |
| p=reject | 13225 | 554 |
| invalid DMARC record | 156 | 0 |
| lookup error | 59 | 1 |
| not checked | 8534 | 13 |

Rows without enforcement (no record / p=none / invalid): **164480**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 179 / 206 / 215
- P01M: 14 / 14 / 20 / 16
- P01T: 43 / 95 / 98 / 66
- P02: 53 / 171 / 137 / 98
- P03: 1 / 58 / 85 / 111
- P04: 596 / 1220 / 850 / 562
- P05: 53 / 136 / 129 / 92
- P06: 18 / 85 / 74 / 101
- P06M: 2518 / 1974 / 959 / 438
- P06T: 20029 / 21751 / 6901 / 2998
- P07: 136 / 252 / 160 / 122
- P08: 6171 / 8452 / 3710 / 1996
- P09: 58 / 100 / 101 / 42
- P10: 596 / 991 / 566 / 431
- P10R: 44719 / 33213 / 9404 / 4221
- P11: 2872 / 3960 / 990 / 544
- P12: 2 / 5 / 0 / 1
- P13: 7786 / 5978 / 2348 / 1171
