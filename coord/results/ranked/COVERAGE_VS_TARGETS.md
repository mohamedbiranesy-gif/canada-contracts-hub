# Coverage vs the downstream team's targets — 2026-11-13

Benchmarks (field × package with a numeric target): **90 of 438 met** (20.5%); 67 within 10 points; 281 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 420, P01T 203, P01_GOLD 653, P02 489, P03 276, P04 4792, P05 429, P06M 30486, P06T 54756, P06 246, P07 775, P08 29228, P09 276, P10R 0, P10 2018, P11 1808, P12 11, P13 204826

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 13.3% | 7 | vendor GST/HST number (398 rows) |
| P01T | 203 | 1.0% | 33.5% | 8 | payment terms (159 rows) |
| P01_GOLD | 653 | 23.3% | 69.2% | 9 | payment terms (245 rows) |
| P02 | 489 | 7.2% | 52.8% | 9 | PO rule (375 rows) |
| P03 | 276 | 14.1% | 54.7% | 9 | PO rule (140 rows) |
| P04 | 4792 | 1.0% | 13.8% | 7 | PO rule (4522 rows) |
| P05 | 429 | 0.9% | 17.0% | 7 | payment terms (358 rows) |
| P06M | 30486 | 0.0% | 3.0% | 7 | PO rule (29694 rows) |
| P06T | 54756 | 0.1% | 13.6% | 7 | PO rule (54403 rows) |
| P06 | 246 | 0.0% | 10.6% | 7 | reference to quote (PO / contract / vendor id) (230 rows) |
| P07 | 775 | 0.0% | 3.6% | 6 | PO rule (737 rows) |
| P08 | 29228 | 0.0% | 1.8% | 6 | PO rule (28906 rows) |
| P09 | 276 | 1.4% | 42.0% | 8 | payment terms (257 rows) |
| P10 | 2018 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2018 rows) |
| P11 | 1808 | 0.1% | 8.0% | 6 | PO rule (1744 rows) |
| P12 | 11 | 0.0% | 36.4% | 8 | PO rule (11 rows) |
| P13 | 204826 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (204826 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 420 | 13 | 118 | 289 | 0 | 0 | 69 |
| P01T | 203 | 26 | 31 | 146 | 0 | 0 | 66 |
| P01_GOLD | 653 | 255 | 177 | 221 | 0 | 0 | 81 |
| P02 | 489 | 0 | 197 | 292 | 0 | 0 | 66 |
| P03 | 276 | 0 | 0 | 265 | 11 | 0 | 57 |
| P04 | 4792 | 0 | 0 | 4155 | 637 | 0 | 46 |
| P05 | 429 | 14 | 29 | 374 | 12 | 0 | 51 |
| P06M | 30486 | 0 | 47 | 30399 | 40 | 0 | 46 |
| P06T | 54756 | 0 | 27 | 38019 | 16710 | 0 | 38 |
| P06 | 246 | 15 | 33 | 198 | 0 | 0 | 67 |
| P07 | 775 | 0 | 22 | 735 | 18 | 0 | 55 |
| P08 | 29228 | 0 | 0 | 26610 | 2618 | 0 | 46 |
| P09 | 276 | 5 | 10 | 260 | 1 | 0 | 53 |
| P10 | 2018 | 2 | 10 | 1367 | 639 | 0 | 41 |
| P11 | 1808 | 7 | 12 | 37 | 0 | 1752 | 24 |
| P12 | 11 | 0 | 0 | 11 | 0 | 0 | 51 |
| P13 | 204826 | 12 | 68 | 204734 | 12 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 420 | 308 | 73.3% | tax treatment (81) |
| P01T | 203 | 123 | 60.6% | bill-to legal name and address (65) |
| P01_GOLD | 653 | 494 | 75.7% | bill-to legal name and address (93) |
| P02 | 489 | 332 | 67.9% | the buyer's PO / reference rule (85) |
| P03 | 276 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (276) |
| P04 | 4792 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4792) |
| P05 | 429 | 45 | 10.5% | a confirmed invoicing / AP or finance channel (341) |
| P06M | 30486 | 337 | 1.1% | a confirmed invoicing / AP or finance channel (30060) |
| P06T | 54756 | 323 | 0.6% | a confirmed invoicing / AP or finance channel (54010) |
| P06 | 246 | 44 | 17.9% | the buyer's PO / reference rule (111) |
| P07 | 775 | 48 | 6.2% | the buyer's PO / reference rule (318) |
| P08 | 29228 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (29228) |
| P09 | 276 | 39 | 14.1% | a confirmed invoicing / AP or finance channel (226) |
| P10 | 2018 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (1945) |
| P11 | 1808 | 19 | 1.1% | a confirmed invoicing / AP or finance channel (1752) |
| P12 | 11 | 2 | 18.2% | a confirmed invoicing / AP or finance channel (9) |
| P13 | 204826 | 45 | 0.0% | a confirmed invoicing / AP or finance channel (202283) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 420 | 9 | 2.1% | 7 | 0 | the vendor's GST/HST number (BN9) (398) |
| P01T | 203 | 82 | 40.4% | 2 | 0 | the vendor's GST/HST number (BN9) (75) |
| P01_GOLD | 653 | 409 | 62.6% | 11 | 0 | the vendor's GST/HST number (BN9) (168) |
| P02 | 489 | 213 | 43.6% | 22 | 0 | the vendor's GST/HST number (BN9) (226) |
| P03 | 276 | 19 | 6.9% | 0 | 132 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (102) |
| P04 | 4792 | 42 | 0.9% | 7 | 907 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3764) |
| P05 | 429 | 21 | 4.9% | 8 | 129 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (203) |
| P06M | 30486 | 11 | 0.0% | 14 | 727 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (29142) |
| P06T | 54756 | 359 | 0.7% | 15 | 18716 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (35210) |
| P06 | 246 | 19 | 7.7% | 47 | 0 | the vendor's GST/HST number (BN9) (118) |
| P07 | 775 | 16 | 2.1% | 135 | 36 | the vendor's GST/HST number (BN9) (385) |
| P08 | 29228 | 5 | 0.0% | 14 | 7274 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (21878) |
| P09 | 276 | 36 | 13.0% | 0 | 107 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (107) |
| P10 | 2018 | 5 | 0.2% | 14 | 280 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1643) |
| P11 | 1808 | 7 | 0.4% | 2 | 0 | a confirmed invoicing / AP or finance channel (1736) |
| P12 | 11 | 1 | 9.1% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 204826 | 23 | 0.0% | 1204 | 80799 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (121299) |
| **all** | 331692 | 1277 | 0.4% | 1502 | 109112 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 407 | 0 | 0 | 0 | 306 | 10 | 0 | 311 | 347 | 0 |
| P01T | 177 | 0 | 0 | 0 | 115 | 61 | 26 | 149 | 160 | 2 |
| P01_GOLD | 398 | 0 | 0 | 0 | 39 | 76 | 29 | 218 | 260 | 2 |
| P02 | 489 | 0 | 489 | 0 | 59 | 57 | 14 | 375 | 304 | 2 |
| P03 | 276 | 0 | 276 | 0 | 27 | 45 | 25 | 140 | 148 | 2 |
| P04 | 4792 | 0 | 4792 | 0 | 2654 | 1475 | 970 | 4522 | 4290 | 32 |
| P05 | 415 | 0 | 362 | 0 | 87 | 100 | 39 | 345 | 360 | 7 |
| P06M | 30486 | 0 | 30486 | 0 | 24112 | 1758 | 127 | 29694 | 29179 | 20 |
| P06T | 54756 | 0 | 54756 | 0 | 49303 | 34150 | 21507 | 54403 | 53853 | 381 |
| P06 | 231 | 0 | 0 | 0 | 129 | 68 | 37 | 179 | 201 | 4 |
| P07 | 775 | 0 | 775 | 0 | 528 | 303 | 93 | 737 | 731 | 5 |
| P08 | 29228 | 0 | 29228 | 0 | 23143 | 12620 | 3995 | 28906 | 28460 | 185 |
| P09 | 271 | 0 | 252 | 0 | 12 | 68 | 1 | 246 | 259 | 7 |
| P10 | 2016 | 0 | 1986 | 0 | 1047 | 1094 | 928 | 1955 | 1918 | 17 |
| P11 | 1801 | 1752 | 1708 | 0 | 931 | 1221 | 509 | 1744 | 1735 | 21 |
| P12 | 11 | 0 | 10 | 0 | 0 | 3 | 0 | 11 | 11 | 2 |
| P13 | 204814 | 0 | 204339 | 0 | 173874 | 124638 | 17 | 204458 | 203532 | 70 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 56.7% | 95% | 78470 |
| buyer_logo_url | P13 | 72.3% | 95% | 46471 |
| buyer_legal_name_as_published | P13 | 39.1% | 60% | 42708 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 40909 |
| ap_system_hint | P13 | 0.3% | 20% | 40322 |
| buyer_bn_as_published | P13 | 10.3% | 30% | 40256 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 30556 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 30518 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 29555 |
| vendor_registered_address | P08 | 31.8% | 70% | 11170 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 10937 |
| ap_system_hint | P06T | 0.6% | 20% | 10602 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8112 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8090 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 7849 |
| buyer_phone | P08 | 70.9% | 95% | 7039 |
| buyer_ap_cycle_published | P06M | 0.1% | 20% | 6080 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5833 |
| ap_system_hint | P06M | 1.3% | 20% | 5697 |
| vendor_emails | P08 | 55.8% | 75% | 5599 |
| ap_system_hint | P08 | 0.9% | 20% | 5575 |
| buyer_legal_name_as_published | P08 | 56.8% | 75% | 5313 |
| vendor_bn9 | P08 | 32.3% | 50% | 5186 |
| vendor_phone | P08 | 67.6% | 85% | 5078 |
| vendor_trading_name | P08 | 33.9% | 50% | 4703 |
| buyer_esignature_preference | P06M | 0.5% | 15% | 4419 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 4331 |
| buyer_tax_exempt_status | P06M | 0.9% | 15% | 4297 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 4268 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 4257 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 4199 |
| invoice_reference_hint | P08 | 12.3% | 25% | 3707 |
| buyer_bn_as_published | P08 | 22.6% | 35% | 3632 |
| average_contract_duration_days | P04 | 14.8% | 90% | 3606 |
| currency | P04 | 21.2% | 95% | 3538 |
| ap_phone | P04 | 15.5% | 85% | 3331 |
| commodity_codes | P04 | 16.7% | 85% | 3276 |
| award_or_notice_id | P04 | 18.6% | 85% | 3181 |
| contract_value | P04 | 20.8% | 85% | 3076 |
| invoice_mailing_address | P04 | 15.2% | 75% | 2864 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 94.5% | 94.5% | +1.3 | 50% | ✅ met |
| P01T | 203 | 95.1% | 95.1% | -0.5 | 50% | ✅ met |
| P01_GOLD | 653 | 92.2% | 94.6% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 489 | 75.7% | 77.1% | +0.7 | 95% | ❌ 19 pts to go |
| P03 | 276 | 83.3% | 86.6% | +1.7 | 95% | ❌ 12 pts to go |
| P04 | 4792 | 44.0% | 45.3% | +12.2 | 90% | ❌ 46 pts to go |
| P05 | 429 | 40.3% | 43.4% | +0.7 | 70% | ❌ 30 pts to go |
| P06M | 30486 | 93.9% | 93.9% | +0.7 | n/a | no target |
| P06T | 54756 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06 | 246 | 31.7% | 31.7% | -3.7 | 30% | ✅ met |
| P07 | 775 | 13.8% | 13.8% | -0.4 | 30% | ❌ 16 pts to go |
| P08 | 29228 | 12.3% | 12.3% | +0.1 | 25% | ❌ 13 pts to go |
| P09 | 276 | 98.9% | 99.6% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2018 | 3.1% | 3.1% | -0.2 | 25% | ❌ 22 pts to go |
| P11 | 1808 | 55.0% | 55.7% | +0.7 | 60% | 🟡 5 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 204826 | 99.6% | 99.6% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 653 | 5.7% | 5.7% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 489 | 5.1% | 5.1% | -1.1 | 50% | ❌ 45 pts to go |
| P03 | 276 | 1.8% | 1.8% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4792 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 429 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 30486 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 92.4% | 92.4% | +2.8 | n/a | no target |
| P01T | 203 | 78.3% | 78.3% | -1.6 | 50% | ✅ met |
| P01_GOLD | 653 | 68.9% | 68.9% | +1.6 | 85% | ❌ 16 pts to go |
| P02 | 489 | 67.1% | 67.1% | +0.9 | 90% | ❌ 23 pts to go |
| P03 | 276 | 62.7% | 62.7% | +2.2 | 85% | ❌ 22 pts to go |
| P04 | 4792 | 41.8% | 41.8% | +12.7 | 85% | ❌ 43 pts to go |
| P05 | 429 | 31.0% | 31.0% | +1.1 | 60% | ❌ 29 pts to go |
| P06M | 30486 | 93.7% | 93.7% | +0.7 | n/a | no target |
| P06T | 54756 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06 | 246 | 6.5% | 6.5% | +0.1 | n/a | no target |
| P07 | 775 | 9.2% | 9.2% | +0.1 | n/a | no target |
| P08 | 29228 | 11.3% | 11.3% | +0.0 | n/a | no target |
| P09 | 276 | 95.7% | 95.7% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 52.3% | 52.3% | +0.8 | 60% | 🟡 8 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 653 | 49.3% | 49.3% | -2.4 | 80% | ❌ 31 pts to go |
| P02 | 489 | 55.4% | 55.4% | -2.7 | 60% | 🟡 5 pts to go |
| P03 | 276 | 48.6% | 48.6% | -1.8 | 80% | ❌ 31 pts to go |
| P04 | 4792 | 17.9% | 17.9% | -6.1 | 50% | ❌ 32 pts to go |
| P05 | 429 | 13.8% | 13.8% | +1.2 | 40% | ❌ 26 pts to go |
| P06M | 30486 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 81.2% | 81.2% | +0.1 | 50% | ✅ met |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 3.3% | 3.3% | +0.0 | 40% | ❌ 37 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 58.5% | 58.5% | -2.4 | 85% | ❌ 26 pts to go |
| P02 | 489 | 55.4% | 55.4% | -2.7 | 90% | ❌ 35 pts to go |
| P03 | 276 | 56.9% | 56.9% | -2.5 | 85% | ❌ 28 pts to go |
| P04 | 4792 | 18.6% | 18.6% | -6.3 | 85% | ❌ 66 pts to go |
| P05 | 429 | 21.4% | 21.4% | +1.0 | 50% | ❌ 29 pts to go |
| P06M | 30486 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 3.7% | 3.7% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 12.3% | 12.3% | -0.3 | 60% | ❌ 48 pts to go |
| P02 | 489 | 6.5% | 6.5% | -0.8 | 50% | ❌ 44 pts to go |
| P03 | 276 | 8.3% | 8.3% | -0.3 | 50% | ❌ 42 pts to go |
| P04 | 4792 | 1.5% | 1.5% | -0.4 | 40% | ❌ 38 pts to go |
| P05 | 429 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 30486 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 3.6% | 3.6% | +0.0 | 50% | ❌ 46 pts to go |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 34.3% | 34.3% | -1.6 | 80% | ❌ 46 pts to go |
| P02 | 489 | 50.1% | 50.1% | -2.9 | 90% | ❌ 40 pts to go |
| P03 | 276 | 32.6% | 32.6% | -1.2 | 80% | ❌ 47 pts to go |
| P04 | 4792 | 16.7% | 16.7% | -5.5 | 85% | ❌ 68 pts to go |
| P05 | 429 | 7.7% | 7.7% | +1.3 | 50% | ❌ 42 pts to go |
| P06M | 30486 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 73.2% | 73.2% | +0.1 | 95% | ❌ 22 pts to go |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 2.7% | 2.7% | +0.1 | 50% | ❌ 47 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 8.0% | 8.0% | -0.1 | 50% | ❌ 42 pts to go |
| P02 | 489 | 4.9% | 4.9% | -1.3 | 50% | ❌ 45 pts to go |
| P03 | 276 | 2.5% | 2.5% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 4792 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 30486 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 489 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4792 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 30486 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 54756 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 246 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 775 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29228 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2018 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1808 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 5.2% | 5.2% | -1.2 | 70% | ❌ 65 pts to go |
| P01T | 203 | 55.2% | 55.2% | -5.1 | 60% | 🟡 5 pts to go |
| P01_GOLD | 653 | 72.1% | 72.1% | -2.7 | 90% | ❌ 18 pts to go |
| P02 | 489 | 51.3% | 51.3% | -3.0 | 85% | ❌ 34 pts to go |
| P03 | 276 | 63.8% | 63.8% | -3.1 | 90% | ❌ 26 pts to go |
| P04 | 4792 | 28.2% | 28.2% | -10.0 | 75% | ❌ 47 pts to go |
| P05 | 429 | 54.8% | 54.8% | +0.1 | 50% | ✅ met |
| P06M | 30486 | 2.9% | 2.9% | +0.0 | n/a | no target |
| P06T | 54756 | 65.2% | 65.2% | +0.7 | n/a | no target |
| P06 | 246 | 41.9% | 41.9% | -0.2 | 40% | ✅ met |
| P07 | 775 | 32.6% | 32.6% | +0.5 | 50% | ❌ 17 pts to go |
| P08 | 29228 | 32.3% | 32.3% | +1.7 | 50% | ❌ 18 pts to go |
| P09 | 276 | 56.5% | 56.5% | -0.2 | 80% | ❌ 24 pts to go |
| P10 | 2018 | 38.8% | 38.8% | +0.0 | 40% | 🟡 1 pts to go |
| P11 | 1808 | 53.7% | 53.7% | -0.9 | 60% | 🟡 6 pts to go |
| P12 | 11 | 54.5% | 54.5% | +9.0 | 85% | ❌ 30 pts to go |
| P13 | 204826 | 44.7% | 44.7% | -0.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 42.1% | 42.1% | -4.5 | n/a | no target |
| P01T | 203 | 55.7% | 55.7% | -4.1 | n/a | no target |
| P01_GOLD | 653 | 74.1% | 74.1% | +1.2 | 95% | ❌ 21 pts to go |
| P02 | 489 | 74.4% | 74.4% | -0.2 | 95% | ❌ 21 pts to go |
| P03 | 276 | 70.7% | 70.7% | +1.2 | 95% | ❌ 24 pts to go |
| P04 | 4792 | 54.1% | 54.1% | +1.0 | 95% | ❌ 41 pts to go |
| P05 | 429 | 58.7% | 58.7% | +0.6 | 70% | ❌ 11 pts to go |
| P06M | 30486 | 38.9% | 38.9% | -2.4 | n/a | no target |
| P06T | 54756 | 68.7% | 68.7% | +1.2 | n/a | no target |
| P06 | 246 | 37.4% | 37.4% | -0.8 | 80% | ❌ 43 pts to go |
| P07 | 775 | 31.6% | 31.6% | +0.6 | 70% | ❌ 38 pts to go |
| P08 | 29228 | 31.8% | 31.8% | +2.1 | 70% | ❌ 38 pts to go |
| P09 | 276 | 86.2% | 86.2% | +0.0 | 100% | ❌ 14 pts to go |
| P10 | 2018 | 39.3% | 39.3% | +0.1 | 70% | ❌ 31 pts to go |
| P11 | 1808 | 58.7% | 58.7% | +0.1 | 75% | ❌ 16 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 40.4% | 40.4% | +0.2 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 22.1% | 22.1% | +0.0 | n/a | no target |
| P01T | 203 | 59.6% | 59.6% | -5.9 | n/a | no target |
| P01_GOLD | 653 | 50.8% | 50.8% | +2.0 | 60% | 🟡 9 pts to go |
| P02 | 489 | 57.9% | 57.9% | +2.1 | 60% | 🟡 2 pts to go |
| P03 | 276 | 54.0% | 54.0% | +1.7 | 60% | 🟡 6 pts to go |
| P04 | 4792 | 54.3% | 54.3% | +11.7 | 55% | 🟡 1 pts to go |
| P05 | 429 | 23.5% | 23.5% | +0.8 | 50% | ❌ 26 pts to go |
| P06M | 30486 | 11.3% | 11.3% | +1.8 | n/a | no target |
| P06T | 54756 | 70.4% | 70.4% | +2.5 | n/a | no target |
| P06 | 246 | 50.0% | 50.0% | +1.4 | n/a | no target |
| P07 | 775 | 39.5% | 39.5% | -0.1 | 55% | ❌ 16 pts to go |
| P08 | 29228 | 33.9% | 33.9% | +0.9 | 50% | ❌ 16 pts to go |
| P09 | 276 | 72.1% | 72.1% | +0.1 | 70% | ✅ met |
| P10 | 2018 | 47.8% | 47.8% | -0.3 | 55% | 🟡 7 pts to go |
| P11 | 1808 | 59.3% | 59.3% | +0.1 | 50% | ✅ met |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 204826 | 2.9% | 2.9% | -0.3 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 24.3% | 24.3% | -9.0 | n/a | no target |
| P01T | 203 | 77.3% | 77.3% | -2.2 | n/a | no target |
| P01_GOLD | 653 | 48.4% | 48.4% | -2.0 | 70% | ❌ 22 pts to go |
| P02 | 489 | 54.8% | 54.8% | -2.0 | 70% | ❌ 15 pts to go |
| P03 | 276 | 48.2% | 48.2% | -2.2 | 70% | ❌ 22 pts to go |
| P04 | 4792 | 49.7% | 49.7% | -5.2 | 65% | ❌ 15 pts to go |
| P05 | 429 | 29.6% | 29.6% | +0.5 | 60% | ❌ 30 pts to go |
| P06M | 30486 | 23.5% | 23.5% | -3.9 | n/a | no target |
| P06T | 54756 | 87.0% | 87.0% | +4.3 | n/a | no target |
| P06 | 246 | 70.7% | 70.7% | +1.4 | 40% | ✅ met |
| P07 | 775 | 66.6% | 66.6% | +1.6 | 85% | ❌ 18 pts to go |
| P08 | 29228 | 67.6% | 67.6% | +3.6 | 85% | ❌ 17 pts to go |
| P09 | 276 | 56.2% | 56.2% | -0.2 | 85% | ❌ 29 pts to go |
| P10 | 2018 | 65.0% | 65.0% | -1.1 | 85% | ❌ 20 pts to go |
| P11 | 1808 | 68.5% | 68.5% | +0.4 | 75% | 🟡 6 pts to go |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 204826 | 90.8% | 90.8% | -1.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 29.0% | 29.0% | -8.8 | n/a | no target |
| P01T | 203 | 98.0% | 98.0% | -0.3 | n/a | no target |
| P01_GOLD | 653 | 75.3% | 75.3% | -3.3 | 90% | ❌ 15 pts to go |
| P02 | 489 | 78.5% | 78.5% | -3.3 | 90% | ❌ 12 pts to go |
| P03 | 276 | 81.2% | 81.2% | -4.1 | 90% | 🟡 9 pts to go |
| P04 | 4792 | 70.9% | 70.9% | -11.9 | 85% | ❌ 14 pts to go |
| P05 | 429 | 44.8% | 44.8% | +0.3 | 70% | ❌ 25 pts to go |
| P06M | 30486 | 29.4% | 29.4% | -3.6 | n/a | no target |
| P06T | 54756 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 246 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 775 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 29228 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 276 | 77.5% | 77.5% | -0.3 | 100% | ❌ 22 pts to go |
| P10 | 2018 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1808 | 97.5% | 97.5% | -0.5 | 100% | 🟡 2 pts to go |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 204826 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 13.6% | 13.6% | -2.5 | n/a | no target |
| P01T | 203 | 54.2% | 54.2% | -5.6 | n/a | no target |
| P01_GOLD | 653 | 41.8% | 41.8% | -1.6 | 70% | ❌ 28 pts to go |
| P02 | 489 | 45.2% | 45.2% | -2.0 | 75% | ❌ 30 pts to go |
| P03 | 276 | 43.5% | 43.5% | -1.2 | 75% | ❌ 32 pts to go |
| P04 | 4792 | 35.2% | 35.2% | -3.5 | 70% | ❌ 35 pts to go |
| P05 | 429 | 21.9% | 21.9% | +0.6 | 55% | ❌ 33 pts to go |
| P06M | 30486 | 6.7% | 6.7% | +0.8 | n/a | no target |
| P06T | 54756 | 41.8% | 41.8% | -5.6 | n/a | no target |
| P06 | 246 | 52.0% | 52.0% | +0.9 | n/a | no target |
| P07 | 775 | 53.7% | 53.7% | +1.0 | 70% | ❌ 16 pts to go |
| P08 | 29228 | 55.8% | 55.8% | +1.0 | 75% | ❌ 19 pts to go |
| P09 | 276 | 46.7% | 46.7% | -0.2 | 85% | ❌ 38 pts to go |
| P10 | 2018 | 44.4% | 44.4% | +0.0 | 80% | ❌ 36 pts to go |
| P11 | 1808 | 51.6% | 51.6% | -1.7 | 70% | ❌ 18 pts to go |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 204826 | 5.9% | 5.9% | +0.4 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 27.6% | 27.6% | -10.2 | n/a | no target |
| P01T | 203 | 96.1% | 96.1% | -0.4 | n/a | no target |
| P01_GOLD | 653 | 69.8% | 69.8% | -3.1 | 90% | ❌ 20 pts to go |
| P02 | 489 | 73.4% | 73.4% | -3.3 | 90% | ❌ 17 pts to go |
| P03 | 276 | 77.9% | 77.9% | -4.1 | 90% | ❌ 12 pts to go |
| P04 | 4792 | 66.7% | 66.7% | -11.0 | 85% | ❌ 18 pts to go |
| P05 | 429 | 43.4% | 43.4% | +0.5 | 75% | ❌ 32 pts to go |
| P06M | 30486 | 28.5% | 28.5% | -4.4 | n/a | no target |
| P06T | 54756 | 97.8% | 97.8% | -0.5 | n/a | no target |
| P06 | 246 | 91.9% | 91.9% | +1.9 | n/a | no target |
| P07 | 775 | 94.3% | 94.3% | +2.6 | 100% | 🟡 6 pts to go |
| P08 | 29228 | 92.8% | 92.8% | +5.5 | 100% | 🟡 7 pts to go |
| P09 | 276 | 66.3% | 66.3% | -0.2 | n/a | no target |
| P10 | 2018 | 89.9% | 89.9% | -0.4 | 100% | ❌ 10 pts to go |
| P11 | 1808 | 90.2% | 90.2% | +0.0 | n/a | no target |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 204826 | 69.4% | 69.4% | -0.4 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 32.4% | 32.4% | -4.5 | n/a | no target · QC vendors: 56 rows, 100.0% filled |
| P01T | 203 | 22.7% | 22.7% | +3.0 | n/a | no target · QC vendors: 34 rows, 88.2% filled |
| P01_GOLD | 653 | 45.5% | 45.5% | +2.0 | 95% | ❌ 50 pts to go · QC vendors: 49 rows, 98.0% filled |
| P02 | 489 | 57.7% | 57.7% | +1.7 | 95% | ❌ 37 pts to go · QC vendors: 112 rows, 100.0% filled |
| P03 | 276 | 44.9% | 44.9% | +2.0 | 95% | ❌ 50 pts to go · QC vendors: 19 rows, 100.0% filled |
| P04 | 4792 | 39.2% | 39.2% | +6.8 | 95% | ❌ 56 pts to go · QC vendors: 587 rows, 98.0% filled |
| P05 | 429 | 14.9% | 14.9% | +0.9 | n/a | no target · QC vendors: 38 rows, 100.0% filled |
| P06M | 30486 | 34.6% | 34.6% | -2.9 | n/a | no target · QC vendors: 7617 rows, 99.9% filled |
| P06T | 54756 | 38.4% | 38.4% | +7.8 | n/a | no target · QC vendors: 21370 rows, 96.2% filled |
| P06 | 246 | 6.5% | 6.5% | -0.6 | n/a | no target · QC vendors: 10 rows, 60.0% filled |
| P07 | 775 | 6.8% | 6.8% | -0.1 | n/a | no target · QC vendors: 44 rows, 79.5% filled |
| P08 | 29228 | 7.1% | 7.1% | +0.1 | n/a | no target · QC vendors: 1767 rows, 92.8% filled |
| P09 | 276 | 73.6% | 73.6% | +0.1 | 95% | ❌ 21 pts to go · QC vendors: 100 rows, 100.0% filled |
| P10 | 2018 | 16.1% | 16.1% | +0.4 | n/a | no target · QC vendors: 200 rows, 92.5% filled |
| P11 | 1808 | 20.7% | 20.7% | +1.1 | n/a | no target · QC vendors: 323 rows, 94.1% filled |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 204826 | 21.9% | 21.9% | -0.3 | n/a | no target · QC vendors: 44871 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 41.7% | 41.7% | -4.5 | n/a | no target · vendors with a registry record: 175 rows, 100.0% filled |
| P01T | 203 | 55.7% | 55.7% | -4.1 | n/a | no target · vendors with a registry record: 113 rows, 100.0% filled |
| P01_GOLD | 653 | 81.8% | 81.8% | +0.9 | 100% | ❌ 18 pts to go · vendors with a registry record: 534 rows, 100.0% filled |
| P02 | 489 | 78.3% | 78.3% | -0.1 | 100% | ❌ 22 pts to go · vendors with a registry record: 383 rows, 100.0% filled |
| P03 | 276 | 79.0% | 79.0% | +0.8 | 100% | ❌ 21 pts to go · vendors with a registry record: 218 rows, 100.0% filled |
| P04 | 4792 | 54.8% | 54.8% | +0.8 | 100% | ❌ 45 pts to go · vendors with a registry record: 2625 rows, 100.0% filled |
| P05 | 429 | 63.2% | 63.2% | +0.4 | n/a | no target · vendors with a registry record: 271 rows, 100.0% filled |
| P06M | 30486 | 38.8% | 38.8% | -2.4 | n/a | no target · vendors with a registry record: 11837 rows, 100.0% filled |
| P06T | 54756 | 68.8% | 68.8% | +1.2 | n/a | no target · vendors with a registry record: 37668 rows, 100.0% filled |
| P06 | 246 | 38.2% | 38.2% | -1.1 | n/a | no target · vendors with a registry record: 94 rows, 100.0% filled |
| P07 | 775 | 32.3% | 32.3% | +0.5 | n/a | no target · vendors with a registry record: 250 rows, 100.0% filled |
| P08 | 29228 | 31.8% | 31.8% | +1.8 | n/a | no target · vendors with a registry record: 9302 rows, 100.0% filled |
| P09 | 276 | 89.5% | 89.5% | +0.0 | n/a | no target · vendors with a registry record: 247 rows, 100.0% filled |
| P10 | 2018 | 40.2% | 40.2% | +0.1 | n/a | no target · vendors with a registry record: 812 rows, 100.0% filled |
| P11 | 1808 | 59.5% | 59.5% | +0.2 | n/a | no target · vendors with a registry record: 1076 rows, 100.0% filled |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P13 | 204826 | 40.4% | 40.4% | +0.2 | n/a | no target · vendors with a registry record: 82806 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 97.6% | 97.6% | +1.2 | 90% | ✅ met |
| P01T | 203 | 70.0% | 70.0% | -0.7 | 90% | ❌ 20 pts to go |
| P01_GOLD | 653 | 88.4% | 88.4% | +1.0 | 95% | 🟡 7 pts to go |
| P02 | 489 | 88.3% | 88.3% | +0.1 | 95% | 🟡 7 pts to go |
| P03 | 276 | 83.7% | 83.7% | +0.6 | 85% | 🟡 1 pts to go |
| P04 | 4792 | 69.2% | 69.2% | +4.7 | 90% | ❌ 21 pts to go |
| P05 | 429 | 76.7% | 76.7% | -1.3 | 75% | ✅ met |
| P06M | 30486 | 94.2% | 94.2% | +0.4 | n/a | no target |
| P06T | 54756 | 37.6% | 37.6% | +0.7 | n/a | no target |
| P06 | 246 | 72.4% | 72.4% | +1.3 | 80% | 🟡 8 pts to go |
| P07 | 775 | 60.9% | 61.0% | +2.7 | 80% | ❌ 19 pts to go |
| P08 | 29228 | 56.8% | 56.8% | +4.9 | 75% | ❌ 18 pts to go |
| P09 | 276 | 75.4% | 75.4% | -0.2 | 95% | ❌ 20 pts to go |
| P10 | 2018 | 45.8% | 45.8% | -1.0 | 70% | ❌ 24 pts to go |
| P11 | 1808 | 32.5% | 32.5% | +0.7 | 65% | ❌ 32 pts to go |
| P12 | 11 | 72.7% | 72.7% | +0.0 | 80% | 🟡 7 pts to go |
| P13 | 204826 | 39.1% | 39.2% | -6.5 | 60% | ❌ 21 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 13.3% | 13.3% | -5.2 | 50% | ❌ 37 pts to go |
| P01T | 203 | 15.8% | 15.8% | -0.4 | n/a | no target |
| P01_GOLD | 653 | 19.1% | 19.1% | -0.7 | 40% | ❌ 21 pts to go |
| P02 | 489 | 19.0% | 19.0% | -0.9 | 40% | ❌ 21 pts to go |
| P03 | 276 | 19.6% | 19.6% | -0.7 | 40% | ❌ 20 pts to go |
| P04 | 4792 | 14.0% | 14.0% | -2.3 | 40% | ❌ 26 pts to go |
| P05 | 429 | 21.0% | 21.0% | +0.1 | 25% | 🟡 4 pts to go |
| P06M | 30486 | 19.1% | 19.1% | -1.3 | n/a | no target |
| P06T | 54756 | 9.9% | 9.9% | +2.4 | n/a | no target |
| P06 | 246 | 20.7% | 20.7% | +3.2 | 35% | ❌ 14 pts to go |
| P07 | 775 | 22.8% | 22.8% | +3.7 | 35% | ❌ 12 pts to go |
| P08 | 29228 | 22.6% | 22.6% | +4.9 | 35% | ❌ 12 pts to go |
| P09 | 276 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P10 | 2018 | 8.9% | 8.9% | +1.8 | 30% | ❌ 21 pts to go |
| P11 | 1808 | 9.6% | 9.6% | +3.1 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 204826 | 10.3% | 10.3% | -2.2 | 30% | ❌ 20 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 85.7% | 85.7% | +0.5 | 100% | ❌ 14 pts to go |
| P01_GOLD | 653 | 91.9% | 91.9% | +0.8 | 100% | 🟡 8 pts to go |
| P02 | 489 | 96.7% | 96.7% | +0.1 | 100% | 🟡 3 pts to go |
| P03 | 276 | 90.2% | 90.2% | +0.7 | 100% | 🟡 10 pts to go |
| P04 | 4792 | 79.3% | 79.3% | +6.8 | 100% | ❌ 21 pts to go |
| P05 | 429 | 90.2% | 90.2% | +0.2 | 100% | 🟡 10 pts to go |
| P06M | 30486 | 99.6% | 99.6% | +0.2 | n/a | no target |
| P06T | 54756 | 60.7% | 60.7% | +2.0 | n/a | no target |
| P06 | 246 | 83.3% | 83.3% | +1.2 | 95% | ❌ 12 pts to go |
| P07 | 775 | 87.7% | 87.7% | +2.3 | 95% | 🟡 7 pts to go |
| P08 | 29228 | 86.3% | 86.3% | +1.8 | 95% | 🟡 9 pts to go |
| P09 | 276 | 96.4% | 96.4% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2018 | 53.9% | 54.0% | -0.7 | 95% | ❌ 41 pts to go |
| P11 | 1808 | 63.7% | 63.7% | +2.8 | 80% | ❌ 16 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 204826 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 65.7% | 65.7% | -5.4 | n/a | no target |
| P01T | 203 | 71.4% | 71.4% | -2.8 | n/a | no target |
| P01_GOLD | 653 | 73.0% | 73.0% | -0.2 | 90% | ❌ 17 pts to go |
| P02 | 489 | 77.5% | 77.5% | -0.9 | 95% | ❌ 18 pts to go |
| P03 | 276 | 74.3% | 74.3% | +0.2 | 95% | ❌ 21 pts to go |
| P04 | 4792 | 69.7% | 69.7% | +0.2 | 95% | ❌ 25 pts to go |
| P05 | 429 | 71.6% | 71.6% | -0.9 | 90% | ❌ 18 pts to go |
| P06M | 30486 | 70.5% | 70.5% | -6.2 | n/a | no target |
| P06T | 54756 | 58.2% | 58.2% | -0.4 | n/a | no target |
| P06 | 246 | 71.1% | 71.1% | +5.7 | 95% | ❌ 24 pts to go |
| P07 | 775 | 68.0% | 68.0% | +8.3 | 90% | ❌ 22 pts to go |
| P08 | 29228 | 70.9% | 70.9% | +12.3 | 95% | ❌ 24 pts to go |
| P09 | 276 | 85.5% | 85.5% | -0.3 | 100% | ❌ 14 pts to go |
| P10 | 2018 | 52.9% | 52.9% | -0.9 | 95% | ❌ 42 pts to go |
| P11 | 1808 | 32.9% | 32.9% | +2.2 | 75% | ❌ 42 pts to go |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target |
| P13 | 204826 | 56.7% | 56.7% | -11.2 | 95% | ❌ 38 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 77.6% | 77.6% | -5.9 | n/a | no target |
| P01T | 203 | 90.1% | 90.1% | -1.6 | 95% | 🟡 5 pts to go |
| P01_GOLD | 653 | 85.1% | 85.1% | +0.1 | 90% | 🟡 5 pts to go |
| P02 | 489 | 90.6% | 90.6% | -0.4 | 95% | 🟡 4 pts to go |
| P03 | 276 | 84.1% | 84.1% | +0.3 | 95% | ❌ 11 pts to go |
| P04 | 4792 | 90.4% | 90.4% | -1.2 | 90% | ✅ met |
| P05 | 429 | 92.5% | 92.5% | +0.1 | 95% | 🟡 2 pts to go |
| P06M | 30486 | 81.9% | 81.9% | -3.4 | n/a | no target |
| P06T | 54756 | 87.2% | 87.2% | +2.6 | n/a | no target |
| P06 | 246 | 92.7% | 92.7% | +7.3 | 100% | 🟡 7 pts to go |
| P07 | 775 | 94.6% | 94.6% | +11.0 | 100% | 🟡 5 pts to go |
| P08 | 29228 | 95.0% | 95.0% | +17.2 | 100% | 🟡 5 pts to go |
| P09 | 276 | 73.9% | 73.9% | -0.3 | n/a | no target |
| P10 | 2018 | 94.2% | 94.2% | -0.2 | 100% | 🟡 6 pts to go |
| P11 | 1808 | 55.4% | 55.4% | +4.3 | 80% | ❌ 25 pts to go |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 204826 | 72.3% | 72.3% | -8.5 | 95% | ❌ 23 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 3.6% | 3.6% | +0.4 | n/a | no target |
| P01T | 203 | 9.4% | 9.4% | +0.7 | n/a | no target |
| P01_GOLD | 653 | 13.8% | 13.8% | -0.2 | 25% | ❌ 11 pts to go |
| P02 | 489 | 24.1% | 24.1% | -0.7 | 40% | ❌ 16 pts to go |
| P03 | 276 | 9.1% | 9.1% | +0.1 | 20% | ❌ 11 pts to go |
| P04 | 4792 | 2.5% | 2.5% | -0.8 | 20% | ❌ 18 pts to go |
| P05 | 429 | 3.0% | 3.0% | -0.3 | 15% | ❌ 12 pts to go |
| P06M | 30486 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 54756 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 246 | 5.3% | 5.3% | -0.1 | n/a | no target |
| P07 | 775 | 8.1% | 8.1% | +0.2 | n/a | no target |
| P08 | 29228 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 276 | 7.2% | 7.2% | -0.4 | n/a | no target |
| P10 | 2018 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1808 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 13.1% | 13.1% | -3.0 | n/a | no target |
| P01T | 203 | 18.7% | 18.7% | -0.5 | 70% | ❌ 51 pts to go |
| P01_GOLD | 653 | 41.0% | 41.0% | -1.1 | 80% | ❌ 39 pts to go |
| P02 | 489 | 55.0% | 55.0% | -2.3 | 90% | ❌ 35 pts to go |
| P03 | 276 | 18.5% | 18.5% | -0.7 | 60% | ❌ 42 pts to go |
| P04 | 4792 | 15.5% | 15.5% | -4.7 | 85% | ❌ 70 pts to go |
| P05 | 429 | 11.0% | 11.0% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 30486 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06T | 54756 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 246 | 13.4% | 13.4% | +0.2 | n/a | no target |
| P07 | 775 | 9.9% | 9.9% | +0.8 | n/a | no target |
| P08 | 29228 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P09 | 276 | 72.1% | 72.1% | +0.1 | 95% | ❌ 23 pts to go |
| P10 | 2018 | 1.5% | 1.5% | -0.1 | n/a | no target |
| P11 | 1808 | 12.7% | 12.7% | -0.3 | n/a | no target |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 204826 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 6.0% | 6.0% | +0.4 | n/a | no target |
| P01T | 203 | 11.8% | 11.8% | +2.6 | n/a | no target |
| P01_GOLD | 653 | 32.8% | 32.8% | -1.0 | 70% | ❌ 37 pts to go |
| P02 | 489 | 37.6% | 37.6% | -1.1 | 75% | ❌ 37 pts to go |
| P03 | 276 | 19.2% | 19.2% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 4792 | 15.2% | 15.2% | -5.0 | 75% | ❌ 60 pts to go |
| P05 | 429 | 10.3% | 10.3% | +0.1 | 50% | ❌ 40 pts to go |
| P06M | 30486 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06T | 54756 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 246 | 6.1% | 6.1% | +0.4 | n/a | no target |
| P07 | 775 | 5.0% | 5.0% | +0.4 | n/a | no target |
| P08 | 29228 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 276 | 68.8% | 68.8% | +0.1 | 95% | ❌ 26 pts to go |
| P10 | 2018 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P11 | 1808 | 12.4% | 12.4% | -0.4 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 204826 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 10.0% | 10.0% | +2.4 | n/a | no target |
| P01T | 203 | 8.4% | 8.4% | -0.3 | n/a | no target |
| P01_GOLD | 653 | 55.3% | 55.4% | -1.8 | 80% | ❌ 25 pts to go |
| P02 | 489 | 43.8% | 44.0% | -1.5 | 75% | ❌ 31 pts to go |
| P03 | 276 | 34.4% | 34.4% | -1.7 | 70% | ❌ 36 pts to go |
| P04 | 4792 | 15.0% | 15.3% | -4.9 | 70% | ❌ 55 pts to go |
| P05 | 429 | 13.8% | 13.8% | -0.2 | 50% | ❌ 36 pts to go |
| P06M | 30486 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P06T | 54756 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 246 | 13.0% | 13.0% | -0.2 | n/a | no target |
| P07 | 775 | 1.3% | 1.3% | +0.2 | n/a | no target |
| P08 | 29228 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 276 | 46.7% | 47.1% | -0.2 | 80% | ❌ 33 pts to go |
| P10 | 2018 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P11 | 1808 | 4.3% | 4.4% | -0.2 | n/a | no target |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 204826 | 0.1% | 0.1% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 17.4% | 17.4% | +2.5 | n/a | no target |
| P01T | 203 | 21.2% | 21.2% | +2.0 | 60% | ❌ 39 pts to go |
| P01_GOLD | 653 | 60.2% | 60.2% | -2.0 | 70% | 🟡 10 pts to go |
| P02 | 489 | 37.8% | 37.8% | -1.7 | 50% | ❌ 12 pts to go |
| P03 | 276 | 46.4% | 46.4% | -1.3 | 55% | 🟡 9 pts to go |
| P04 | 4792 | 10.5% | 10.5% | -2.0 | 40% | ❌ 30 pts to go |
| P05 | 429 | 16.1% | 16.1% | -0.5 | 40% | ❌ 24 pts to go |
| P06M | 30486 | 4.3% | 4.3% | +1.5 | n/a | no target |
| P06T | 54756 | 1.6% | 1.6% | +0.1 | n/a | no target |
| P06 | 246 | 18.3% | 18.3% | +0.1 | n/a | no target |
| P07 | 775 | 5.7% | 5.7% | +0.8 | n/a | no target |
| P08 | 29228 | 2.6% | 2.6% | +0.5 | n/a | no target |
| P09 | 276 | 6.2% | 6.2% | +0.4 | n/a | no target |
| P10 | 2018 | 5.0% | 5.0% | -0.1 | n/a | no target |
| P11 | 1808 | 4.0% | 4.0% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.6% | 0.6% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 26.0% | 26.0% | +4.3 | n/a | no target |
| P01T | 203 | 26.6% | 26.6% | -1.3 | 65% | ❌ 38 pts to go |
| P01_GOLD | 653 | 66.6% | 66.6% | -2.0 | 70% | 🟡 3 pts to go |
| P02 | 489 | 23.3% | 23.3% | -0.4 | 50% | ❌ 27 pts to go |
| P03 | 276 | 49.3% | 49.3% | -1.1 | 60% | ❌ 11 pts to go |
| P04 | 4792 | 5.6% | 5.6% | +0.0 | 40% | ❌ 34 pts to go |
| P05 | 429 | 19.6% | 19.6% | -0.3 | 45% | ❌ 25 pts to go |
| P06M | 30486 | 2.6% | 2.6% | +0.9 | n/a | no target |
| P06T | 54756 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 246 | 27.2% | 27.2% | -2.1 | n/a | no target |
| P07 | 775 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P08 | 29228 | 1.1% | 1.1% | +0.2 | n/a | no target |
| P09 | 276 | 10.9% | 10.9% | +0.0 | n/a | no target |
| P10 | 2018 | 3.1% | 3.1% | -0.2 | n/a | no target |
| P11 | 1808 | 3.5% | 3.5% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 18.1% | 18.1% | +6.1 | n/a | no target |
| P01T | 203 | 13.3% | 13.3% | +0.6 | n/a | no target |
| P01_GOLD | 653 | 49.0% | 49.0% | -1.2 | 50% | 🟡 1 pts to go |
| P02 | 489 | 36.0% | 36.0% | -1.6 | n/a | no target |
| P03 | 276 | 50.7% | 50.7% | -0.1 | 60% | 🟡 9 pts to go |
| P04 | 4792 | 9.9% | 9.9% | -2.9 | n/a | no target |
| P05 | 429 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 30486 | 1.1% | 1.1% | +0.3 | n/a | no target |
| P06T | 54756 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 246 | 18.3% | 18.3% | -2.1 | n/a | no target |
| P07 | 775 | 5.2% | 5.2% | -0.5 | n/a | no target |
| P08 | 29228 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P09 | 276 | 20.7% | 20.7% | +0.0 | n/a | no target |
| P10 | 2018 | 2.3% | 2.3% | -0.2 | n/a | no target |
| P11 | 1808 | 2.4% | 2.4% | -0.3 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 204826 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 8.3% | 8.3% | -0.5 | 15% | 🟡 7 pts to go |
| P01T | 203 | 13.3% | 13.3% | +0.6 | 15% | 🟡 2 pts to go |
| P01_GOLD | 653 | 33.8% | 33.8% | -1.3 | 40% | 🟡 6 pts to go |
| P02 | 489 | 11.5% | 11.7% | -0.7 | 25% | ❌ 14 pts to go |
| P03 | 276 | 15.6% | 15.6% | -0.9 | 25% | 🟡 9 pts to go |
| P04 | 4792 | 2.2% | 2.2% | -0.5 | 15% | ❌ 13 pts to go |
| P05 | 429 | 6.5% | 6.5% | -0.1 | 15% | 🟡 8 pts to go |
| P06M | 30486 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 54756 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 246 | 9.3% | 9.3% | +0.0 | 15% | 🟡 6 pts to go |
| P07 | 775 | 3.5% | 3.5% | +0.1 | 15% | ❌ 12 pts to go |
| P08 | 29228 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 276 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2018 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1808 | 1.3% | 1.3% | +0.1 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 204826 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 8.8% | 8.8% | +3.2 | 15% | 🟡 6 pts to go |
| P01T | 203 | 12.3% | 12.3% | +1.4 | 25% | ❌ 13 pts to go |
| P01_GOLD | 653 | 28.5% | 28.5% | -0.4 | 25% | ✅ met |
| P02 | 489 | 23.9% | 23.9% | -1.5 | 15% | ✅ met |
| P03 | 276 | 21.4% | 21.4% | -0.4 | 15% | ✅ met |
| P04 | 4792 | 3.2% | 3.2% | -0.8 | 15% | ❌ 12 pts to go |
| P05 | 429 | 11.4% | 11.4% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 30486 | 0.9% | 0.9% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 54756 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 246 | 7.7% | 7.7% | +0.6 | 15% | 🟡 7 pts to go |
| P07 | 775 | 1.7% | 1.7% | -0.1 | 15% | ❌ 13 pts to go |
| P08 | 29228 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P09 | 276 | 1.4% | 1.4% | -0.1 | 15% | ❌ 14 pts to go |
| P10 | 2018 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1808 | 1.9% | 1.9% | +0.1 | 15% | ❌ 13 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 204826 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 2.1% | 2.1% | +0.5 | 20% | ❌ 18 pts to go |
| P01T | 203 | 3.4% | 3.4% | +0.3 | 20% | ❌ 17 pts to go |
| P01_GOLD | 653 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 489 | 1.4% | 1.4% | -0.1 | 20% | ❌ 19 pts to go |
| P03 | 276 | 1.4% | 1.4% | -0.5 | 20% | ❌ 19 pts to go |
| P04 | 4792 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P05 | 429 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 30486 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 246 | 1.2% | 1.2% | -0.2 | 20% | ❌ 19 pts to go |
| P07 | 775 | 0.3% | 0.3% | +0.1 | 20% | ❌ 20 pts to go |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 276 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2018 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1808 | 0.2% | 0.2% | +0.1 | 20% | ❌ 20 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 2.4% | 2.4% | +0.8 | 15% | ❌ 13 pts to go |
| P01T | 203 | 2.5% | 2.5% | -0.6 | 15% | ❌ 12 pts to go |
| P01_GOLD | 653 | 11.0% | 11.0% | +0.5 | 15% | 🟡 4 pts to go |
| P02 | 489 | 10.0% | 10.0% | -1.5 | 15% | 🟡 5 pts to go |
| P03 | 276 | 20.3% | 20.3% | -0.4 | 15% | ✅ met |
| P04 | 4792 | 1.9% | 1.9% | -0.5 | 15% | ❌ 13 pts to go |
| P05 | 429 | 3.0% | 3.0% | +0.2 | 15% | ❌ 12 pts to go |
| P06M | 30486 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P06T | 54756 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 246 | 4.1% | 4.1% | +0.2 | 15% | ❌ 11 pts to go |
| P07 | 775 | 1.8% | 1.8% | +0.6 | 15% | ❌ 13 pts to go |
| P08 | 29228 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P09 | 276 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2018 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1808 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 204826 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 18.3% | 18.3% | +5.9 | 20% | 🟡 2 pts to go |
| P01T | 203 | 14.3% | 14.3% | +0.8 | 40% | ❌ 26 pts to go |
| P01_GOLD | 653 | 45.5% | 45.5% | -1.1 | 40% | ✅ met |
| P02 | 489 | 41.5% | 41.5% | -1.7 | 20% | ✅ met |
| P03 | 276 | 49.3% | 49.3% | +0.8 | 35% | ✅ met |
| P04 | 4792 | 11.6% | 11.6% | -3.3 | 20% | 🟡 8 pts to go |
| P05 | 429 | 15.6% | 15.6% | +0.0 | 20% | 🟡 4 pts to go |
| P06M | 30486 | 1.3% | 1.3% | +0.3 | 20% | ❌ 19 pts to go |
| P06T | 54756 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 246 | 18.3% | 18.3% | -2.8 | 20% | 🟡 2 pts to go |
| P07 | 775 | 5.8% | 5.8% | -0.3 | 20% | ❌ 14 pts to go |
| P08 | 29228 | 0.9% | 0.9% | +0.1 | 20% | ❌ 19 pts to go |
| P09 | 276 | 21.0% | 21.0% | -0.1 | 20% | ✅ met |
| P10 | 2018 | 3.7% | 3.7% | -0.1 | 20% | ❌ 16 pts to go |
| P11 | 1808 | 3.0% | 3.0% | -0.2 | 20% | ❌ 17 pts to go |
| P12 | 11 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P13 | 204826 | 0.3% | 0.3% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 11.4% | 11.4% | -6.7 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 68.9% | 68.9% | -2.7 | 95% | ❌ 26 pts to go |
| P02 | 489 | 63.0% | 63.0% | -3.2 | 95% | ❌ 32 pts to go |
| P03 | 276 | 55.4% | 55.4% | -2.5 | 90% | ❌ 35 pts to go |
| P04 | 4792 | 20.8% | 20.8% | -5.7 | 85% | ❌ 64 pts to go |
| P05 | 429 | 39.4% | 39.4% | +0.5 | 75% | ❌ 36 pts to go |
| P06M | 30486 | 22.9% | 22.9% | -5.2 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 3.9% | 3.9% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 11.4% | 11.4% | -6.7 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 70.8% | 70.8% | -2.7 | 100% | ❌ 29 pts to go |
| P02 | 489 | 64.6% | 64.6% | -3.6 | 100% | ❌ 35 pts to go |
| P03 | 276 | 58.0% | 58.0% | -2.5 | n/a | no target |
| P04 | 4792 | 21.2% | 21.2% | -5.8 | 95% | ❌ 74 pts to go |
| P05 | 429 | 35.2% | 35.2% | +0.6 | 80% | ❌ 45 pts to go |
| P06M | 30486 | 22.9% | 22.9% | -5.2 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 91.7% | 91.7% | +0.1 | 100% | 🟡 8 pts to go |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 4.1% | 4.1% | +0.1 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 81.9% | 81.9% | -2.4 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 54.1% | 54.1% | +1.8 | 85% | ❌ 31 pts to go |
| P02 | 489 | 60.5% | 60.5% | +1.3 | 90% | ❌ 30 pts to go |
| P03 | 276 | 46.7% | 46.7% | +2.7 | 85% | ❌ 38 pts to go |
| P04 | 4792 | 37.9% | 37.9% | +8.8 | 90% | ❌ 52 pts to go |
| P05 | 429 | 33.1% | 33.1% | +0.2 | 75% | ❌ 42 pts to go |
| P06M | 30486 | 82.0% | 82.0% | -2.3 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 81.9% | 81.9% | +0.1 | 95% | ❌ 13 pts to go |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 3.8% | 3.8% | +0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 54.5% | 54.5% | -11.4 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 53.8% | 53.8% | +1.8 | 85% | ❌ 31 pts to go |
| P02 | 489 | 54.8% | 54.8% | +1.4 | 90% | ❌ 35 pts to go |
| P03 | 276 | 47.1% | 47.1% | +2.7 | 85% | ❌ 38 pts to go |
| P04 | 4792 | 33.6% | 33.6% | +9.0 | 90% | ❌ 56 pts to go |
| P05 | 429 | 42.0% | 42.0% | -0.7 | 75% | ❌ 33 pts to go |
| P06M | 30486 | 63.0% | 63.0% | -6.2 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.4% | 0.4% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 3.0% | 3.0% | +0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 97.1% | 97.1% | +1.9 | n/a | no target |
| P01T | 203 | 95.6% | 95.6% | -0.5 | n/a | no target |
| P01_GOLD | 653 | 86.1% | 86.2% | +0.6 | 100% | ❌ 14 pts to go |
| P02 | 489 | 77.9% | 77.9% | +0.3 | 100% | ❌ 22 pts to go |
| P03 | 276 | 92.8% | 92.8% | +0.3 | n/a | no target |
| P04 | 4792 | 53.8% | 53.8% | +3.2 | 95% | ❌ 41 pts to go |
| P05 | 429 | 77.6% | 77.6% | +0.3 | 95% | ❌ 17 pts to go |
| P06M | 30486 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 54756 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 246 | 20.3% | 20.3% | -0.1 | n/a | no target |
| P07 | 775 | 10.1% | 10.1% | -0.1 | n/a | no target |
| P08 | 29228 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 276 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2018 | 71.1% | 71.1% | +0.5 | n/a | no target |
| P11 | 1808 | 70.2% | 70.2% | +0.4 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 99.6% | 99.6% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 97.1% | 97.1% | +1.9 | n/a | no target |
| P01T | 203 | 95.6% | 95.6% | -0.5 | n/a | no target |
| P01_GOLD | 653 | 89.1% | 89.3% | +0.4 | 100% | ❌ 11 pts to go |
| P02 | 489 | 79.1% | 79.1% | +0.3 | 100% | ❌ 21 pts to go |
| P03 | 276 | 93.5% | 93.5% | +0.3 | n/a | no target |
| P04 | 4792 | 56.3% | 56.3% | +2.3 | 95% | ❌ 39 pts to go |
| P05 | 429 | 89.7% | 89.7% | +0.4 | 70% | ✅ met |
| P06M | 30486 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 54756 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 246 | 20.3% | 20.3% | -0.1 | n/a | no target |
| P07 | 775 | 10.1% | 10.1% | -0.1 | n/a | no target |
| P08 | 29228 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 276 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2018 | 71.1% | 71.1% | +0.5 | n/a | no target |
| P11 | 1808 | 70.2% | 70.2% | +0.3 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 16.4% | 16.4% | -0.5 | 60% | ❌ 44 pts to go · rows from a source that publishes bids: 368 rows, 29.1% filled |
| P02 | 489 | 9.4% | 9.4% | -1.3 | n/a | no target · rows from a source that publishes bids: 293 rows, 15.7% filled |
| P03 | 276 | 13.4% | 13.4% | -0.5 | n/a | no target · rows from a source that publishes bids: 143 rows, 25.9% filled |
| P04 | 4792 | 1.3% | 1.3% | -0.4 | n/a | no target · rows from a source that publishes bids: 884 rows, 7.0% filled |
| P05 | 429 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 60 rows, 18.3% filled |
| P06M | 30486 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 54756 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 4.3% | 4.3% | -0.1 | n/a | no target · rows from a source that publishes bids: 263 rows, 4.6% filled |
| P10 | 2018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1808 | 0.4% | 0.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 68 rows, 11.8% filled |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 11 rows, 0.0% filled |
| P13 | 204826 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 97.5% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 51.1% | 82.7% | -2.3 | 90% | ❌ 39 pts to go |
| P02 | 489 | 50.5% | 87.5% | -2.9 | 90% | ❌ 40 pts to go |
| P03 | 276 | 44.2% | 80.8% | -1.7 | 90% | ❌ 46 pts to go |
| P04 | 4792 | 14.8% | 94.7% | -4.8 | 90% | ❌ 75 pts to go |
| P05 | 429 | 0.0% | 81.1% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 30486 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 54756 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 2.9% | 4.7% | +0.0 | 90% | ❌ 87 pts to go |
| P10 | 2018 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1808 | 2.2% | 97.6% | +0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 1.0% | 98.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 25.1% | 56.7% | -1.4 | 90% | ❌ 65 pts to go |
| P02 | 489 | 49.7% | 86.7% | -2.7 | n/a | no target |
| P03 | 276 | 24.3% | 60.9% | -0.9 | n/a | no target |
| P04 | 4792 | 15.9% | 95.9% | -5.5 | n/a | no target |
| P05 | 429 | 0.5% | 81.6% | +0.0 | n/a | no target |
| P06M | 30486 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 54756 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 40.6% | 42.4% | +0.2 | n/a | no target |
| P10 | 2018 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1808 | 2.3% | 97.7% | +0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 2.5% | 100.0% | +0.3 | n/a | no target |
| P01_GOLD | 653 | 50.1% | 81.6% | -1.9 | 95% | ❌ 45 pts to go |
| P02 | 489 | 55.4% | 92.4% | -2.7 | n/a | no target |
| P03 | 276 | 48.2% | 84.8% | -2.2 | n/a | no target |
| P04 | 4792 | 16.5% | 96.5% | -5.7 | n/a | no target |
| P05 | 429 | 5.1% | 86.2% | +0.1 | n/a | no target |
| P06M | 30486 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 54756 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 246 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 775 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29228 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 59.8% | 61.6% | -0.6 | n/a | no target |
| P10 | 2018 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1808 | 2.3% | 97.8% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 204826 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 489 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4792 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 30486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 54756 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 246 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 775 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29228 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2018 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1808 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 204826 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 489 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4792 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 30486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 54756 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 246 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 775 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29228 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2018 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1808 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 204826 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 489 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4792 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 30486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 54756 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 246 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 775 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29228 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2018 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1808 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 204826 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

