# DMARC posture of the delivered mailboxes — Ranked buyers — 2026-11-04T15:12Z

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; rows without enforcement: `dmarc_no_enforcement.csv` in this folder.

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 16479 | 91 |
| v=DMARC1; p=none (monitor only) | 19611 | 377 |
| p=quarantine | 8631 | 408 |
| p=reject | 4596 | 445 |
| invalid DMARC record | 41 | 0 |
| lookup error | 7 | 0 |

## By package (no record / p=none / quarantine / reject)
- P01: 23 / 157 / 192 / 193
- P01M: 3 / 2 / 5 / 8
- P01T: 5 / 25 / 36 / 23
- P02: 43 / 113 / 101 / 76
- P03: 1 / 48 / 84 / 97
- P04: 280 / 528 / 494 / 291
- P05: 57 / 127 / 116 / 80
- P06: 2 / 31 / 46 / 85
- P06M: 32 / 59 / 36 / 40
- P06T: 683 / 1134 / 368 / 238
- P07: 17 / 84 / 67 / 74
- P08: 715 / 1191 / 721 / 430
- P09: 87 / 126 / 105 / 51
- P10: 649 / 1092 / 562 / 300
- P11: 47 / 247 / 134 / 89
- P12: 4 / 12 / 4 / 3
- P13: 13831 / 14635 / 5560 / 2518
