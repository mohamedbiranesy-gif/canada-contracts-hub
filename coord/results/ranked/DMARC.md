# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 69828 | 176 |
| v=DMARC1; p=none (monitor only) | 69938 | 540 |
| p=quarantine | 25336 | 537 |
| p=reject | 12938 | 543 |
| invalid DMARC record | 137 | 1 |
| lookup error | 50 | 0 |

Rows without enforcement (no record / p=none / invalid): **139903**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 206 / 215
- P01M: 28 / 34 / 36 / 31
- P01T: 21 / 76 / 56 / 39
- P02: 56 / 169 / 138 / 103
- P03: 2 / 63 / 86 / 112
- P04: 757 / 1452 / 907 / 602
- P05: 53 / 141 / 130 / 98
- P06: 17 / 81 / 68 / 106
- P06M: 5555 / 5205 / 2581 / 1289
- P06T: 14559 / 15517 / 4436 / 2123
- P07: 168 / 241 / 157 / 129
- P08: 7141 / 8979 / 3794 / 2070
- P09: 60 / 99 / 102 / 44
- P10: 573 / 877 / 517 / 421
- P11: 368 / 606 / 273 / 207
- P12: 4 / 8 / 2 / 1
- P13: 40441 / 36210 / 11847 / 5348
