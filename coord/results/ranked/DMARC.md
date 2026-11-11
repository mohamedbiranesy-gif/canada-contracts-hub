# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 98546 | 207 |
| v=DMARC1; p=none (monitor only) | 91822 | 555 |
| p=quarantine | 30489 | 565 |
| p=reject | 15094 | 577 |
| invalid DMARC record | 182 | 1 |
| lookup error | 103 | 0 |

Rows without enforcement (no record / p=none / invalid): **190550**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 205 / 215
- P01M: 25 / 23 / 30 / 22
- P01T: 52 / 106 / 106 / 70
- P02: 56 / 178 / 139 / 100
- P03: 1 / 59 / 85 / 112
- P04: 760 / 1489 / 949 / 630
- P05: 53 / 143 / 134 / 97
- P06: 22 / 94 / 85 / 111
- P06M: 4074 / 3577 / 1761 / 854
- P06T: 23309 / 25369 / 7870 / 3431
- P07: 198 / 306 / 186 / 150
- P08: 8504 / 11103 / 4697 / 2503
- P09: 58 / 100 / 101 / 42
- P10: 640 / 1039 / 608 / 462
- P10R: 48934 / 35661 / 10021 / 4468
- P11: 3427 / 6291 / 1148 / 697
- P12: 2 / 5 / 0 / 0
- P13: 8406 / 6099 / 2364 / 1130
