# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 131062 | 269 |
| v=DMARC1; p=none (monitor only) | 124713 | 649 |
| p=quarantine | 43432 | 635 |
| p=reject | 20896 | 622 |
| invalid DMARC record | 244 | 1 |
| lookup error | 114 | 0 |

Rows without enforcement (no record / p=none / invalid): **256019**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 196 / 208 / 224
- P01M: 56 / 101 / 109 / 111
- P01T: 35 / 76 / 60 / 40
- P02: 58 / 168 / 152 / 113
- P03: 4 / 72 / 95 / 108
- P04: 995 / 1786 / 1274 / 808
- P05: 53 / 143 / 132 / 101
- P06: 28 / 75 / 63 / 92
- P06M: 9189 / 10209 / 5851 / 3567
- P06T: 22974 / 23607 / 6276 / 2572
- P07: 218 / 284 / 164 / 123
- P08: 10130 / 12029 / 4840 / 2570
- P09: 50 / 90 / 91 / 43
- P10: 498 / 756 / 448 / 376
- P11: 563 / 706 / 306 / 221
- P12: 2 / 8 / 0 / 1
- P13: 86184 / 74407 / 23363 / 9826
