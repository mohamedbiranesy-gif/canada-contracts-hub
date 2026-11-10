# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 24255 | 98 |
| v=DMARC1; p=none (monitor only) | 31107 | 414 |
| p=quarantine | 11962 | 456 |
| p=reject | 6201 | 502 |
| invalid DMARC record | 65 | 0 |
| lookup error | 11 | 0 |

Rows without enforcement (no record / p=none / invalid): **55427**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 179 / 207 / 215
- P01M: 11 / 7 / 17 / 12
- P01T: 12 / 45 / 66 / 50
- P02: 49 / 148 / 120 / 86
- P03: 0 / 47 / 71 / 91
- P04: 246 / 554 / 491 / 275
- P05: 54 / 123 / 109 / 79
- P06: 15 / 71 / 70 / 107
- P06M: 1718 / 1383 / 667 / 331
- P06T: 3969 / 5842 / 2151 / 973
- P07: 68 / 190 / 123 / 119
- P08: 2817 / 4450 / 1994 / 1062
- P09: 58 / 104 / 105 / 43
- P10: 575 / 989 / 533 / 307
- P10R: 9784 / 11193 / 3100 / 1393
- P11: 624 / 1791 / 494 / 278
- P12: 2 / 4 / 0 / 1
- P13: 4228 / 3987 / 1644 / 779
