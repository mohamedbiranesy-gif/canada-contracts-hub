# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 87739 | 194 |
| v=DMARC1; p=none (monitor only) | 85307 | 562 |
| p=quarantine | 29902 | 556 |
| p=reject | 14877 | 560 |
| invalid DMARC record | 166 | 1 |
| lookup error | 467 | 0 |
| not checked | 11406 | 23 |

Rows without enforcement (no record / p=none / invalid): **173212**

## By package (no record / p=none / quarantine / reject)
- P01: 26 / 185 / 209 / 220
- P01M: 28 / 39 / 38 / 40
- P01T: 20 / 70 / 55 / 40
- P02: 55 / 169 / 139 / 107
- P03: 2 / 68 / 90 / 110
- P04: 715 / 1379 / 921 / 595
- P05: 53 / 142 / 132 / 99
- P06: 16 / 77 / 65 / 96
- P06M: 5823 / 5495 / 2799 / 1430
- P06T: 14719 / 15450 / 4231 / 2085
- P07: 169 / 237 / 149 / 119
- P08: 6993 / 8781 / 3681 / 2011
- P09: 61 / 103 / 102 / 46
- P10: 509 / 777 / 464 / 393
- P11: 406 / 622 / 269 / 203
- P12: 4 / 9 / 2 / 1
- P13: 58140 / 51704 / 16556 / 7282
