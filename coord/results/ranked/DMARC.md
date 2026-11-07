# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 21141 | 90 |
| v=DMARC1; p=none (monitor only) | 26287 | 375 |
| p=quarantine | 10406 | 421 |
| p=reject | 5379 | 455 |
| invalid DMARC record | 58 | 0 |
| lookup error | 12 | 0 |
| not checked | 12 | 0 |

Rows without enforcement (no record / p=none / invalid): **47486**

## By package (no record / p=none / quarantine / reject)
- P01: 22 / 167 / 195 / 197
- P01M: 2 / 3 / 5 / 8
- P01T: 3 / 25 / 38 / 25
- P02: 38 / 131 / 109 / 77
- P03: 0 / 48 / 81 / 92
- P04: 256 / 559 / 496 / 288
- P05: 56 / 125 / 117 / 81
- P06: 2 / 28 / 44 / 85
- P06M: 31 / 63 / 37 / 39
- P06T: 667 / 1144 / 368 / 238
- P07: 15 / 85 / 69 / 77
- P08: 689 / 1195 / 720 / 430
- P09: 71 / 125 / 109 / 51
- P10: 628 / 1106 / 557 / 299
- P11: 48 / 255 / 142 / 94
- P12: 4 / 9 / 3 / 3
- P13: 18609 / 21219 / 7316 / 3295
