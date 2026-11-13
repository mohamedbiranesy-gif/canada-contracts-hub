# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 112997 | 236 |
| v=DMARC1; p=none (monitor only) | 108813 | 613 |
| p=quarantine | 37852 | 599 |
| p=reject | 18264 | 594 |
| invalid DMARC record | 214 | 1 |
| lookup error | 454 | 10 |

Rows without enforcement (no record / p=none / invalid): **222024**

## By package (no record / p=none / quarantine / reject)
- P01: 24 / 187 / 209 / 222
- P01M: 48 / 75 / 70 / 73
- P01T: 31 / 83 / 68 / 47
- P02: 55 / 164 / 144 / 109
- P03: 3 / 72 / 91 / 105
- P04: 748 / 1479 / 1069 / 689
- P05: 53 / 141 / 130 / 99
- P06: 27 / 78 / 67 / 97
- P06M: 7694 / 8021 / 4521 / 2593
- P06T: 26506 / 25955 / 6593 / 2825
- P07: 221 / 297 / 173 / 130
- P08: 10449 / 12385 / 4995 / 2673
- P09: 50 / 92 / 92 / 43
- P10: 503 / 767 / 455 / 384
- P11: 565 / 723 / 317 / 225
- P12: 2 / 7 / 0 / 1
- P13: 66018 / 58287 / 18858 / 7949
