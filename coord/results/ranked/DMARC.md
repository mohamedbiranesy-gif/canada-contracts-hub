# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 135278 | 277 |
| v=DMARC1; p=none (monitor only) | 128405 | 666 |
| p=quarantine | 44650 | 655 |
| p=reject | 21469 | 638 |
| invalid DMARC record | 250 | 1 |
| lookup error | 122 | 0 |

Rows without enforcement (no record / p=none / invalid): **263933**

## By package (no record / p=none / quarantine / reject)
- P01: 26 / 194 / 211 / 226
- P01M: 57 / 115 / 124 / 124
- P01T: 35 / 71 / 59 / 41
- P02: 58 / 167 / 150 / 111
- P03: 4 / 72 / 93 / 106
- P04: 979 / 1763 / 1267 / 802
- P05: 53 / 143 / 132 / 100
- P06: 28 / 71 / 59 / 90
- P06M: 9690 / 10798 / 6194 / 3812
- P06T: 22849 / 23495 / 6203 / 2524
- P07: 217 / 279 / 161 / 121
- P08: 10048 / 11918 / 4760 / 2540
- P09: 50 / 91 / 92 / 43
- P10: 484 / 747 / 444 / 375
- P11: 571 / 710 / 310 / 219
- P12: 2 / 7 / 0 / 1
- P13: 90127 / 77764 / 24391 / 10234
