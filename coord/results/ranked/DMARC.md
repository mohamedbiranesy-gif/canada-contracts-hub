# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 30731 | 111 |
| v=DMARC1; p=none (monitor only) | 38285 | 455 |
| p=quarantine | 15181 | 495 |
| p=reject | 8041 | 534 |
| invalid DMARC record | 79 | 0 |
| lookup error | 44 | 0 |

Rows without enforcement (no record / p=none / invalid): **69095**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 179 / 207 / 215
- P01M: 12 / 8 / 17 / 16
- P01T: 20 / 55 / 75 / 53
- P02: 49 / 148 / 121 / 86
- P03: 0 / 48 / 72 / 92
- P04: 255 / 577 / 508 / 296
- P05: 57 / 141 / 128 / 91
- P06: 18 / 99 / 96 / 129
- P06M: 1748 / 1439 / 704 / 353
- P06T: 6780 / 8224 / 3088 / 1401
- P07: 129 / 272 / 184 / 150
- P08: 6144 / 8763 / 3915 / 2183
- P09: 58 / 104 / 105 / 43
- P10: 805 / 1358 / 759 / 490
- P10R: 9749 / 11085 / 3070 / 1377
- P11: 671 / 1836 / 513 / 292
- P12: 2 / 4 / 0 / 1
- P13: 4209 / 3945 / 1619 / 773
