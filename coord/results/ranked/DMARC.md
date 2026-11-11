# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 113517 | 223 |
| v=DMARC1; p=none (monitor only) | 109434 | 588 |
| p=quarantine | 35298 | 594 |
| p=reject | 17661 | 603 |
| invalid DMARC record | 215 | 1 |
| lookup error | 83 | 0 |

Rows without enforcement (no record / p=none / invalid): **223166**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 205 / 215
- P01M: 27 / 31 / 34 / 30
- P01T: 65 / 144 / 131 / 91
- P02: 58 / 183 / 142 / 102
- P03: 2 / 63 / 86 / 113
- P04: 832 / 1624 / 979 / 663
- P05: 53 / 140 / 130 / 97
- P06: 21 / 87 / 78 / 109
- P06M: 4980 / 4514 / 2348 / 1169
- P06T: 33370 / 36976 / 11124 / 4998
- P07: 185 / 277 / 179 / 144
- P08: 8162 / 10350 / 4441 / 2397
- P09: 56 / 96 / 99 / 42
- P10: 621 / 990 / 579 / 457
- P10R: 50323 / 36706 / 10549 / 4736
- P11: 6406 / 11355 / 1993 / 1190
- P12: 2 / 4 / 0 / 1
- P13: 8329 / 5714 / 2201 / 1107
