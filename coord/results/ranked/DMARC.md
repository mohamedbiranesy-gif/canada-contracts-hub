# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 133907 | 273 |
| v=DMARC1; p=none (monitor only) | 127225 | 655 |
| p=quarantine | 44159 | 643 |
| p=reject | 21209 | 628 |
| invalid DMARC record | 250 | 1 |
| lookup error | 118 | 0 |

Rows without enforcement (no record / p=none / invalid): **261382**

## By package (no record / p=none / quarantine / reject)
- P01: 24 / 194 / 210 / 226
- P01M: 57 / 104 / 114 / 116
- P01T: 35 / 71 / 59 / 41
- P02: 59 / 169 / 151 / 111
- P03: 4 / 73 / 93 / 107
- P04: 984 / 1769 / 1271 / 803
- P05: 53 / 142 / 132 / 100
- P06: 28 / 72 / 59 / 91
- P06M: 9494 / 10491 / 5976 / 3646
- P06T: 22953 / 23586 / 6231 / 2534
- P07: 218 / 281 / 160 / 121
- P08: 10075 / 11954 / 4783 / 2547
- P09: 50 / 91 / 90 / 43
- P10: 484 / 750 / 444 / 375
- P11: 569 / 710 / 309 / 221
- P12: 2 / 8 / 0 / 1
- P13: 88818 / 76760 / 24077 / 10126
