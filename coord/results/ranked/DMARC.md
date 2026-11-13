# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 138435 | 282 |
| v=DMARC1; p=none (monitor only) | 131358 | 674 |
| p=quarantine | 45532 | 656 |
| p=reject | 21920 | 641 |
| invalid DMARC record | 252 | 1 |
| lookup error | 130 | 0 |

Rows without enforcement (no record / p=none / invalid): **270045**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 195 / 206 / 219
- P01M: 60 / 117 / 131 / 125
- P01T: 35 / 70 / 57 / 41
- P02: 59 / 162 / 152 / 111
- P03: 4 / 71 / 92 / 107
- P04: 957 / 1748 / 1254 / 798
- P05: 53 / 143 / 131 / 102
- P06: 27 / 71 / 57 / 86
- P06M: 10235 / 11417 / 6505 / 3986
- P06T: 22813 / 23511 / 6213 / 2497
- P07: 210 / 274 / 154 / 118
- P08: 9854 / 11693 / 4640 / 2485
- P09: 8 / 24 / 24 / 15
- P10: 479 / 729 / 431 / 364
- P11: 570 / 708 / 303 / 216
- P12: 2 / 8 / 0 / 1
- P13: 93044 / 80417 / 25182 / 10649
