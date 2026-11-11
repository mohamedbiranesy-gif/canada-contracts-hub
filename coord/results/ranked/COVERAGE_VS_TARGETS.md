# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **91 of 438 met** (20.8%); 67 within 10 points; 280 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 132, P01T 334, P01_GOLD 626, P02 488, P03 264, P04 4694, P05 422, P06M 14527, P06T 60669, P06 295, P07 774, P08 25137, P09 298, P10R 0, P10 3662, P11 1461, P12 15, P13 33504

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 19.7% | 8 | vendor GST/HST number (117 rows) |
| P01T | 334 | 0.3% | 27.8% | 8 | payment terms (279 rows) |
| P01_GOLD | 626 | 25.1% | 71.6% | 10 | payment terms (214 rows) |
| P02 | 488 | 7.0% | 52.7% | 9 | PO rule (375 rows) |
| P03 | 264 | 14.8% | 57.2% | 9 | payment terms (131 rows) |
| P04 | 4694 | 1.0% | 13.4% | 6 | PO rule (4484 rows) |
| P05 | 422 | 1.2% | 17.5% | 7 | payment terms (348 rows) |
| P06M | 14527 | 0.0% | 3.2% | 8 | PO rule (14320 rows) |
| P06T | 60669 | 0.0% | 10.8% | 7 | PO rule (60304 rows) |
| P06 | 295 | 0.0% | 11.9% | 7 | reference to quote (PO / contract / vendor id) (295 rows) |
| P07 | 774 | 0.0% | 2.8% | 6 | reference to quote (PO / contract / vendor id) (774 rows) |
| P08 | 25137 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (25137 rows) |
| P09 | 298 | 1.0% | 46.0% | 8 | payment terms (278 rows) |
| P10 | 3662 | 0.0% | 1.1% | 6 | reference to quote (PO / contract / vendor id) (3662 rows) |
| P11 | 1461 | 0.4% | 7.0% | 5 | PO rule (1385 rows) |
| P12 | 15 | 0.0% | 53.3% | 9 | PO rule (14 rows) |
| P13 | 33504 | 0.0% | 0.5% | 7 | reference to quote (PO / contract / vendor id) (33504 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 132 | 8 | 26 | 98 | 0 | 0 | 71 |
| P01T | 334 | 28 | 50 | 256 | 0 | 0 | 68 |
| P01_GOLD | 626 | 227 | 200 | 199 | 0 | 0 | 82 |
| P02 | 488 | 0 | 196 | 292 | 0 | 0 | 66 |
| P03 | 264 | 0 | 0 | 252 | 12 | 0 | 57 |
| P04 | 4694 | 0 | 0 | 3968 | 726 | 0 | 46 |
| P05 | 422 | 15 | 30 | 365 | 12 | 0 | 51 |
| P06M | 14527 | 0 | 10 | 14448 | 69 | 0 | 46 |
| P06T | 60669 | 0 | 36 | 48469 | 12164 | 0 | 38 |
| P06 | 295 | 22 | 57 | 216 | 0 | 0 | 71 |
| P07 | 774 | 0 | 31 | 723 | 20 | 0 | 54 |
| P08 | 25137 | 0 | 0 | 21854 | 3283 | 0 | 44 |
| P09 | 298 | 3 | 12 | 281 | 2 | 0 | 53 |
| P10 | 3662 | 3 | 22 | 2838 | 799 | 0 | 43 |
| P11 | 1461 | 7 | 16 | 47 | 0 | 1391 | 23 |
| P12 | 15 | 0 | 0 | 15 | 0 | 0 | 54 |
| P13 | 33504 | 0 | 21 | 28533 | 4950 | 0 | 45 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 132 | 109 | 82.6% | the buyer's PO / reference rule (12) |
| P01T | 334 | 207 | 62.0% | bill-to legal name and address (106) |
| P01_GOLD | 626 | 473 | 75.6% | bill-to legal name and address (97) |
| P02 | 488 | 313 | 64.1% | the buyer's PO / reference rule (99) |
| P03 | 264 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (264) |
| P04 | 4694 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4694) |
| P05 | 422 | 47 | 11.1% | a confirmed invoicing / AP or finance channel (336) |
| P06M | 14527 | 149 | 1.0% | a confirmed invoicing / AP or finance channel (14335) |
| P06T | 60669 | 440 | 0.7% | a confirmed invoicing / AP or finance channel (59729) |
| P06 | 295 | 55 | 18.6% | the buyer's PO / reference rule (130) |
| P07 | 774 | 13 | 1.7% | the buyer's PO / reference rule (301) |
| P08 | 25137 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (25137) |
| P09 | 298 | 41 | 13.8% | a confirmed invoicing / AP or finance channel (247) |
| P10 | 3662 | 11 | 0.3% | a confirmed invoicing / AP or finance channel (3518) |
| P11 | 1461 | 14 | 1.0% | a confirmed invoicing / AP or finance channel (1391) |
| P12 | 15 | 4 | 26.7% | a confirmed invoicing / AP or finance channel (10) |
| P13 | 33504 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (32736) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 132 | 6 | 4.5% | 7 | 0 | the vendor's GST/HST number (BN9) (117) |
| P01T | 334 | 100 | 29.9% | 9 | 0 | the vendor's GST/HST number (BN9) (169) |
| P01_GOLD | 626 | 408 | 65.2% | 11 | 0 | the vendor's GST/HST number (BN9) (144) |
| P02 | 488 | 211 | 43.2% | 33 | 0 | the vendor's GST/HST number (BN9) (208) |
| P03 | 264 | 16 | 6.1% | 0 | 137 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89) |
| P04 | 4694 | 42 | 0.9% | 7 | 1048 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3535) |
| P05 | 422 | 20 | 4.7% | 8 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (206) |
| P06M | 14527 | 6 | 0.0% | 11 | 387 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (13901) |
| P06T | 60669 | 305 | 0.5% | 24 | 14298 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (45313) |
| P06 | 295 | 32 | 10.8% | 51 | 0 | the vendor's GST/HST number (BN9) (137) |
| P07 | 774 | 10 | 1.3% | 114 | 36 | the vendor's GST/HST number (BN9) (365) |
| P08 | 25137 | 3 | 0.0% | 14 | 5232 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (19830) |
| P09 | 298 | 39 | 13.1% | 1 | 123 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (115) |
| P10 | 3662 | 9 | 0.2% | 36 | 597 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2888) |
| P11 | 1461 | 10 | 0.7% | 6 | 0 | a confirmed invoicing / AP or finance channel (1373) |
| P12 | 15 | 3 | 20.0% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 33504 | 8 | 0.0% | 548 | 20119 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (12525) |
| **all** | 147302 | 1228 | 0.8% | 880 | 42105 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 124 | 0 | 0 | 0 | 68 | 8 | 0 | 104 | 108 | 4 |
| P01T | 306 | 0 | 0 | 0 | 160 | 98 | 31 | 261 | 280 | 13 |
| P01_GOLD | 399 | 0 | 0 | 0 | 11 | 78 | 31 | 194 | 228 | 60 |
| P02 | 488 | 0 | 488 | 0 | 51 | 64 | 19 | 375 | 302 | 23 |
| P03 | 264 | 0 | 264 | 0 | 16 | 41 | 25 | 126 | 137 | 26 |
| P04 | 4694 | 0 | 4694 | 0 | 2303 | 1837 | 1088 | 4484 | 4206 | 191 |
| P05 | 407 | 0 | 356 | 0 | 76 | 88 | 42 | 339 | 350 | 53 |
| P06M | 14527 | 0 | 14527 | 0 | 9374 | 1143 | 122 | 14320 | 14186 | 218 |
| P06T | 60669 | 0 | 60669 | 0 | 49698 | 34485 | 15473 | 60304 | 59677 | 1428 |
| P06 | 273 | 0 | 0 | 0 | 120 | 71 | 50 | 196 | 233 | 10 |
| P07 | 774 | 0 | 774 | 0 | 472 | 310 | 123 | 717 | 719 | 17 |
| P08 | 25137 | 0 | 25137 | 0 | 18607 | 11227 | 4791 | 24817 | 24420 | 558 |
| P09 | 295 | 0 | 274 | 0 | 9 | 69 | 2 | 269 | 281 | 46 |
| P10 | 3659 | 0 | 3608 | 0 | 1608 | 1883 | 1149 | 3578 | 3507 | 162 |
| P11 | 1454 | 1391 | 1345 | 0 | 583 | 1007 | 580 | 1385 | 1385 | 59 |
| P12 | 15 | 0 | 13 | 0 | 1 | 3 | 0 | 14 | 14 | 1 |
| P13 | 33504 | 0 | 33351 | 0 | 436 | 16176 | 7472 | 33452 | 33410 | 18 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 12119 |
| ap_system_hint | P06T | 0.7% | 20% | 11732 |
| vendor_registered_address | P08 | 29.0% | 70% | 10311 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8982 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8961 |
| buyer_payment_method_preference | P06T | 0.6% | 15% | 8745 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 6693 |
| ap_system_hint | P13 | 0.6% | 20% | 6510 |
| buyer_phone | P08 | 69.1% | 95% | 6502 |
| buyer_phone | P13 | 76.7% | 95% | 6131 |
| invoice_reference_hint | P08 | 1.3% | 25% | 5965 |
| buyer_address | P13 | 77.6% | 95% | 5817 |
| vendor_bn9 | P08 | 27.8% | 50% | 5573 |
| vendor_emails | P08 | 55.0% | 75% | 5022 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 5015 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 4999 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 4998 |
| buyer_legal_name_as_published | P08 | 55.3% | 75% | 4943 |
| buyer_payment_method_preference | P13 | 0.8% | 15% | 4761 |
| ap_system_hint | P08 | 1.1% | 20% | 4757 |
| buyer_bn_as_published | P08 | 16.2% | 35% | 4728 |
| vendor_phone | P08 | 66.5% | 85% | 4660 |
| buyer_bn_as_published | P13 | 17.7% | 30% | 4134 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3657 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3637 |
| buyer_payment_method_preference | P08 | 0.7% | 15% | 3605 |
| buyer_address | P08 | 80.9% | 95% | 3540 |
| average_contract_duration_days | P04 | 15.2% | 90% | 3513 |
| currency | P04 | 20.2% | 95% | 3510 |
| end_date | P04 | 18.9% | 90% | 3337 |
| vendor_trading_name | P08 | 37.0% | 50% | 3269 |
| start_date | P04 | 22.1% | 90% | 3187 |
| commodity_codes | P04 | 17.1% | 85% | 3186 |
| ap_phone | P04 | 17.3% | 85% | 3177 |
| vendor_neq | P04 | 27.4% | 95% | 3175 |
| award_or_notice_id | P04 | 18.7% | 85% | 3110 |
| invoice_reference_hint | P04 | 24.1% | 90% | 3092 |
| contract_value | P04 | 19.7% | 85% | 3064 |
| contract_or_agreement_number | P04 | 21.9% | 85% | 2962 |
| buyer_ap_cycle_published | P06M | 0.1% | 20% | 2898 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 89.4% | 89.4% | +0.7 | 50% | ✅ met |
| P01T | 334 | 94.3% | 94.3% | +4.8 | 50% | ✅ met |
| P01_GOLD | 626 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 488 | 70.7% | 72.1% | -3.1 | 95% | ❌ 24 pts to go |
| P03 | 264 | 81.1% | 84.1% | -0.9 | 95% | ❌ 14 pts to go |
| P04 | 4694 | 24.1% | 25.4% | -8.7 | 90% | ❌ 66 pts to go |
| P05 | 422 | 38.6% | 41.5% | +0.0 | 70% | ❌ 31 pts to go |
| P06M | 14527 | 91.7% | 91.7% | -0.9 | n/a | no target |
| P06T | 60669 | 98.1% | 98.1% | +17.8 | n/a | no target |
| P06 | 295 | 33.6% | 33.6% | +1.9 | 30% | ✅ met |
| P07 | 774 | 7.4% | 7.4% | +0.5 | 30% | ❌ 23 pts to go |
| P08 | 25137 | 1.3% | 1.3% | +0.2 | 25% | ❌ 24 pts to go |
| P09 | 298 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 3662 | 2.3% | 2.4% | -0.3 | 25% | ❌ 23 pts to go |
| P11 | 1461 | 46.8% | 47.7% | +33.2 | 60% | ❌ 13 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 33504 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 626 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 488 | 5.9% | 5.9% | -0.3 | 50% | ❌ 44 pts to go |
| P03 | 264 | 1.5% | 1.5% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4694 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 422 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 14527 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 0.3% | 0.3% | +0.3 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 82.6% | 82.6% | +1.2 | n/a | no target |
| P01T | 334 | 80.8% | 80.8% | +10.3 | 50% | ✅ met |
| P01_GOLD | 626 | 66.8% | 66.8% | -0.1 | 85% | ❌ 18 pts to go |
| P02 | 488 | 61.9% | 61.9% | -3.0 | 90% | ❌ 28 pts to go |
| P03 | 264 | 59.5% | 59.5% | -1.8 | 85% | ❌ 26 pts to go |
| P04 | 4694 | 21.9% | 21.9% | -8.2 | 85% | ❌ 63 pts to go |
| P05 | 422 | 28.9% | 28.9% | -0.1 | 60% | ❌ 31 pts to go |
| P06M | 14527 | 91.4% | 91.4% | -1.0 | n/a | no target |
| P06T | 60669 | 98.0% | 98.0% | +18.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 96.0% | 96.0% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 43.1% | 43.1% | +30.4 | 60% | ❌ 17 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 626 | 50.8% | 50.8% | +0.2 | 80% | ❌ 29 pts to go |
| P02 | 488 | 54.3% | 54.3% | -2.7 | 60% | 🟡 6 pts to go |
| P03 | 264 | 50.0% | 50.0% | -1.6 | 80% | ❌ 30 pts to go |
| P04 | 4694 | 18.2% | 18.2% | -6.8 | 50% | ❌ 32 pts to go |
| P05 | 422 | 11.4% | 11.4% | -0.5 | 40% | ❌ 29 pts to go |
| P06M | 14527 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 83.2% | 83.2% | -0.3 | 50% | ✅ met |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 5.5% | 5.5% | +4.7 | 40% | ❌ 34 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 60.4% | 60.4% | +0.0 | 85% | ❌ 25 pts to go |
| P02 | 488 | 53.7% | 53.7% | -2.6 | 90% | ❌ 36 pts to go |
| P03 | 264 | 58.3% | 58.3% | -1.9 | 85% | ❌ 27 pts to go |
| P04 | 4694 | 18.7% | 18.7% | -7.1 | 85% | ❌ 66 pts to go |
| P05 | 422 | 19.7% | 19.7% | -0.2 | 50% | ❌ 30 pts to go |
| P06M | 14527 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 97.0% | 97.0% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 6.0% | 6.0% | +5.1 | 60% | ❌ 54 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 12.9% | 12.9% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 488 | 5.7% | 5.7% | -0.3 | 50% | ❌ 44 pts to go |
| P03 | 264 | 8.3% | 8.3% | -0.3 | 50% | ❌ 42 pts to go |
| P04 | 4694 | 1.4% | 1.4% | -0.6 | 40% | ❌ 39 pts to go |
| P05 | 422 | 0.7% | 0.7% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 14527 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 2.7% | 2.7% | +0.4 | 50% | ❌ 47 pts to go |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 0.9% | 0.9% | +0.8 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 34.8% | 34.8% | +0.0 | 80% | ❌ 45 pts to go |
| P02 | 488 | 49.6% | 49.6% | -2.4 | 90% | ❌ 40 pts to go |
| P03 | 264 | 32.6% | 32.6% | -1.0 | 80% | ❌ 47 pts to go |
| P04 | 4694 | 17.1% | 17.1% | -6.5 | 85% | ❌ 68 pts to go |
| P05 | 422 | 5.5% | 5.5% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 14527 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 75.2% | 75.2% | -0.7 | 95% | ❌ 20 pts to go |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 4.2% | 4.2% | +3.6 | 50% | ❌ 46 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 488 | 5.9% | 5.9% | -0.3 | 50% | ❌ 44 pts to go |
| P03 | 264 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 4694 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 422 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 14527 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 0.3% | 0.3% | +0.3 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 488 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4694 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 14527 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60669 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 774 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25137 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 298 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 3662 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1461 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 11.4% | 11.4% | -3.0 | 70% | ❌ 59 pts to go |
| P01T | 334 | 40.7% | 40.7% | +7.0 | 60% | ❌ 19 pts to go |
| P01_GOLD | 626 | 74.6% | 74.6% | +1.6 | 90% | ❌ 15 pts to go |
| P02 | 488 | 53.5% | 53.5% | -1.6 | 85% | ❌ 32 pts to go |
| P03 | 264 | 69.3% | 69.3% | -0.6 | 90% | ❌ 21 pts to go |
| P04 | 4694 | 32.0% | 32.0% | -0.5 | 75% | ❌ 43 pts to go |
| P05 | 422 | 54.5% | 54.5% | +4.6 | 50% | ✅ met |
| P06M | 14527 | 3.2% | 3.2% | +1.4 | n/a | no target |
| P06T | 60669 | 37.5% | 37.5% | +20.2 | n/a | no target |
| P06 | 295 | 41.7% | 41.7% | +18.9 | 40% | ✅ met |
| P07 | 774 | 30.5% | 30.5% | +14.1 | 50% | ❌ 20 pts to go |
| P08 | 25137 | 27.8% | 27.8% | +16.9 | 50% | ❌ 22 pts to go |
| P09 | 298 | 59.1% | 59.1% | +1.3 | 80% | ❌ 21 pts to go |
| P10 | 3662 | 32.2% | 32.2% | +3.5 | 40% | 🟡 8 pts to go |
| P11 | 1461 | 43.7% | 43.7% | -47.4 | 60% | ❌ 16 pts to go |
| P12 | 15 | 60.0% | 60.0% | -2.5 | 85% | ❌ 25 pts to go |
| P13 | 33504 | 92.1% | 92.1% | +1.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 58.3% | 58.3% | -8.7 | n/a | no target |
| P01T | 334 | 43.4% | 43.4% | +5.4 | n/a | no target |
| P01_GOLD | 626 | 72.4% | 72.4% | +2.0 | 95% | ❌ 23 pts to go |
| P02 | 488 | 72.5% | 72.5% | -1.3 | 95% | ❌ 22 pts to go |
| P03 | 264 | 71.6% | 71.6% | -0.3 | 95% | ❌ 23 pts to go |
| P04 | 4694 | 43.5% | 43.5% | -2.1 | 95% | ❌ 52 pts to go |
| P05 | 422 | 58.1% | 58.1% | +4.7 | 70% | ❌ 12 pts to go |
| P06M | 14527 | 46.2% | 46.2% | -8.4 | n/a | no target |
| P06T | 60669 | 50.3% | 50.3% | +20.0 | n/a | no target |
| P06 | 295 | 39.7% | 39.7% | +14.9 | 80% | ❌ 40 pts to go |
| P07 | 774 | 30.7% | 30.7% | +12.7 | 70% | ❌ 39 pts to go |
| P08 | 25137 | 29.0% | 29.0% | +14.9 | 70% | ❌ 41 pts to go |
| P09 | 298 | 87.6% | 87.6% | +0.1 | 100% | ❌ 12 pts to go |
| P10 | 3662 | 34.4% | 34.4% | +1.9 | 70% | ❌ 36 pts to go |
| P11 | 1461 | 49.3% | 49.3% | -42.9 | 75% | ❌ 26 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 13.6% | 13.6% | +13.6 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 16.7% | 16.7% | +0.2 | n/a | no target |
| P01T | 334 | 53.6% | 53.6% | +27.7 | n/a | no target |
| P01_GOLD | 626 | 49.8% | 49.8% | +1.9 | 60% | ❌ 10 pts to go |
| P02 | 488 | 55.3% | 55.3% | +0.0 | 60% | 🟡 5 pts to go |
| P03 | 264 | 55.3% | 55.3% | +0.2 | 60% | 🟡 5 pts to go |
| P04 | 4694 | 40.6% | 40.6% | +3.9 | 55% | ❌ 14 pts to go |
| P05 | 422 | 24.6% | 24.6% | +2.4 | 50% | ❌ 25 pts to go |
| P06M | 14527 | 6.9% | 6.9% | +3.3 | n/a | no target |
| P06T | 60669 | 48.1% | 48.1% | +21.1 | n/a | no target |
| P06 | 295 | 47.8% | 47.8% | +12.6 | n/a | no target |
| P07 | 774 | 41.1% | 41.1% | +7.9 | 55% | ❌ 14 pts to go |
| P08 | 25137 | 37.0% | 37.0% | +10.1 | 50% | ❌ 13 pts to go |
| P09 | 298 | 72.8% | 72.8% | +1.8 | 70% | ✅ met |
| P10 | 3662 | 46.0% | 46.0% | +6.5 | 55% | 🟡 9 pts to go |
| P11 | 1461 | 51.7% | 51.7% | -40.3 | 50% | ✅ met |
| P12 | 15 | 86.7% | 86.7% | -0.8 | n/a | no target |
| P13 | 33504 | 77.9% | 77.9% | +77.9 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 49.2% | 49.2% | +34.8 | n/a | no target |
| P01T | 334 | 79.3% | 79.3% | +23.0 | n/a | no target |
| P01_GOLD | 626 | 50.3% | 50.3% | +2.4 | 70% | ❌ 20 pts to go |
| P02 | 488 | 59.0% | 59.0% | +5.0 | 70% | ❌ 11 pts to go |
| P03 | 264 | 51.1% | 51.1% | +1.5 | 70% | ❌ 19 pts to go |
| P04 | 4694 | 56.3% | 56.3% | +9.2 | 65% | 🟡 9 pts to go |
| P05 | 422 | 28.0% | 28.0% | -2.7 | 60% | ❌ 32 pts to go |
| P06M | 14527 | 36.8% | 36.8% | +33.3 | n/a | no target |
| P06T | 60669 | 83.5% | 83.5% | +19.7 | n/a | no target |
| P06 | 295 | 69.2% | 69.2% | +11.6 | 40% | ✅ met |
| P07 | 774 | 65.6% | 65.6% | +8.6 | 85% | ❌ 19 pts to go |
| P08 | 25137 | 66.5% | 66.5% | +9.6 | 85% | ❌ 18 pts to go |
| P09 | 298 | 60.1% | 60.1% | +6.6 | 85% | ❌ 25 pts to go |
| P10 | 3662 | 63.7% | 63.7% | +2.7 | 85% | ❌ 21 pts to go |
| P11 | 1461 | 61.7% | 61.7% | +55.3 | 75% | ❌ 13 pts to go |
| P12 | 15 | 26.7% | 26.7% | +1.7 | n/a | no target |
| P13 | 33504 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 55.3% | 55.3% | +35.7 | n/a | no target |
| P01T | 334 | 97.9% | 97.9% | +1.5 | n/a | no target |
| P01_GOLD | 626 | 79.6% | 79.6% | -9.7 | 90% | ❌ 10 pts to go |
| P02 | 488 | 84.0% | 84.0% | -5.2 | 90% | 🟡 6 pts to go |
| P03 | 264 | 87.9% | 87.9% | -3.1 | 90% | 🟡 2 pts to go |
| P04 | 4694 | 86.7% | 86.7% | -3.5 | 85% | ✅ met |
| P05 | 422 | 44.3% | 44.3% | -7.9 | 70% | ❌ 26 pts to go |
| P06M | 14527 | 43.1% | 43.1% | +36.9 | n/a | no target |
| P06T | 60669 | 99.9% | 99.9% | +7.9 | n/a | no target |
| P06 | 295 | 99.3% | 99.3% | +1.0 | 50% | ✅ met |
| P07 | 774 | 99.9% | 99.9% | +0.8 | 100% | 🟡 0 pts to go |
| P08 | 25137 | 99.7% | 99.7% | +0.3 | 100% | 🟡 0 pts to go |
| P09 | 298 | 79.9% | 79.9% | -0.3 | 100% | ❌ 20 pts to go |
| P10 | 3662 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1461 | 97.2% | 97.2% | -2.5 | 100% | 🟡 3 pts to go |
| P12 | 15 | 53.3% | 53.3% | +15.8 | n/a | no target |
| P13 | 33504 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 15.2% | 15.2% | +0.8 | n/a | no target |
| P01T | 334 | 62.0% | 62.0% | +12.9 | n/a | no target |
| P01_GOLD | 626 | 43.5% | 43.5% | -1.7 | 70% | ❌ 26 pts to go |
| P02 | 488 | 49.0% | 49.0% | -0.5 | 75% | ❌ 26 pts to go |
| P03 | 264 | 43.2% | 43.2% | -1.3 | 75% | ❌ 32 pts to go |
| P04 | 4694 | 40.0% | 40.0% | +2.6 | 70% | ❌ 30 pts to go |
| P05 | 422 | 21.6% | 21.6% | -3.9 | 55% | ❌ 33 pts to go |
| P06M | 14527 | 4.6% | 4.6% | +1.3 | n/a | no target |
| P06T | 60669 | 61.0% | 61.0% | +21.4 | n/a | no target |
| P06 | 295 | 47.8% | 47.8% | +5.0 | n/a | no target |
| P07 | 774 | 51.0% | 51.0% | +5.1 | 70% | ❌ 19 pts to go |
| P08 | 25137 | 55.0% | 55.0% | +5.1 | 75% | ❌ 20 pts to go |
| P09 | 298 | 50.0% | 50.0% | +0.2 | 85% | ❌ 35 pts to go |
| P10 | 3662 | 46.7% | 46.7% | +3.2 | 80% | ❌ 33 pts to go |
| P11 | 1461 | 54.3% | 54.3% | +49.3 | 70% | ❌ 16 pts to go |
| P12 | 15 | 40.0% | 40.0% | +15.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 55.3% | 55.3% | +41.9 | n/a | no target |
| P01T | 334 | 95.8% | 95.8% | +6.0 | n/a | no target |
| P01_GOLD | 626 | 73.8% | 73.8% | -3.7 | 90% | ❌ 16 pts to go |
| P02 | 488 | 79.3% | 79.3% | +1.7 | 90% | ❌ 11 pts to go |
| P03 | 264 | 83.3% | 83.3% | +0.1 | 90% | 🟡 7 pts to go |
| P04 | 4694 | 77.2% | 77.2% | +1.6 | 85% | 🟡 8 pts to go |
| P05 | 422 | 42.7% | 42.7% | -6.0 | 75% | ❌ 32 pts to go |
| P06M | 14527 | 42.8% | 42.8% | +38.7 | n/a | no target |
| P06T | 60669 | 96.7% | 96.7% | +13.5 | n/a | no target |
| P06 | 295 | 91.2% | 91.2% | +11.9 | n/a | no target |
| P07 | 774 | 92.1% | 92.1% | +10.5 | 100% | 🟡 8 pts to go |
| P08 | 25137 | 91.0% | 91.0% | +12.1 | 100% | 🟡 9 pts to go |
| P09 | 298 | 66.4% | 66.4% | +5.0 | n/a | no target |
| P10 | 3662 | 86.5% | 86.5% | +2.3 | 100% | ❌ 14 pts to go |
| P11 | 1461 | 87.7% | 87.7% | -0.7 | n/a | no target |
| P12 | 15 | 46.7% | 46.7% | +9.2 | n/a | no target |
| P13 | 33504 | 86.4% | 86.4% | +3.2 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 45.5% | 45.5% | -8.1 | n/a | no target · QC vendors: 49 rows, 100.0% filled |
| P01T | 334 | 11.7% | 11.7% | -6.1 | n/a | no target · QC vendors: 24 rows, 79.2% filled |
| P01_GOLD | 626 | 43.6% | 43.6% | +0.0 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 488 | 53.9% | 53.9% | -1.2 | 95% | ❌ 41 pts to go · QC vendors: 116 rows, 100.0% filled |
| P03 | 264 | 45.8% | 45.8% | -0.7 | 95% | ❌ 49 pts to go · QC vendors: 21 rows, 100.0% filled |
| P04 | 4694 | 27.4% | 27.4% | -4.5 | 95% | ❌ 68 pts to go · QC vendors: 702 rows, 96.9% filled |
| P05 | 422 | 14.0% | 14.0% | -0.8 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 14527 | 43.0% | 43.0% | -10.3 | n/a | no target · QC vendors: 5532 rows, 99.8% filled |
| P06T | 60669 | 8.0% | 8.0% | -9.5 | n/a | no target · QC vendors: 5262 rows, 80.1% filled |
| P06 | 295 | 8.8% | 8.8% | +0.5 | n/a | no target · QC vendors: 20 rows, 70.0% filled |
| P07 | 774 | 6.7% | 6.7% | -0.1 | n/a | no target · QC vendors: 48 rows, 77.1% filled |
| P08 | 25137 | 8.0% | 8.0% | +1.5 | n/a | no target · QC vendors: 1835 rows, 92.6% filled |
| P09 | 298 | 77.5% | 77.5% | -0.7 | 95% | ❌ 18 pts to go · QC vendors: 108 rows, 100.0% filled |
| P10 | 3662 | 16.7% | 16.7% | -0.9 | n/a | no target · QC vendors: 444 rows, 90.5% filled |
| P11 | 1461 | 14.8% | 14.8% | -66.7 | n/a | no target · QC vendors: 154 rows, 91.6% filled |
| P12 | 15 | 73.3% | 73.3% | +10.8 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 33504 | 13.6% | 13.6% | +13.6 | n/a | no target · QC vendors: 4569 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 57.6% | 57.6% | -7.3 | n/a | no target · vendors with a registry record: 76 rows, 100.0% filled |
| P01T | 334 | 43.4% | 43.4% | +5.1 | n/a | no target · vendors with a registry record: 145 rows, 100.0% filled |
| P01_GOLD | 626 | 81.3% | 81.3% | +1.9 | 100% | ❌ 19 pts to go · vendors with a registry record: 509 rows, 100.0% filled |
| P02 | 488 | 76.2% | 76.2% | -1.2 | 100% | ❌ 24 pts to go · vendors with a registry record: 372 rows, 100.0% filled |
| P03 | 264 | 80.3% | 80.3% | -0.9 | 100% | ❌ 20 pts to go · vendors with a registry record: 212 rows, 100.0% filled |
| P04 | 4694 | 43.8% | 43.8% | -2.3 | 100% | ❌ 56 pts to go · vendors with a registry record: 2055 rows, 100.0% filled |
| P05 | 422 | 62.8% | 62.8% | +4.5 | n/a | no target · vendors with a registry record: 265 rows, 100.0% filled |
| P06M | 14527 | 46.0% | 46.0% | -8.3 | n/a | no target · vendors with a registry record: 6688 rows, 100.0% filled |
| P06T | 60669 | 50.4% | 50.4% | +20.0 | n/a | no target · vendors with a registry record: 30587 rows, 100.0% filled |
| P06 | 295 | 40.7% | 40.7% | +15.2 | n/a | no target · vendors with a registry record: 120 rows, 100.0% filled |
| P07 | 774 | 31.1% | 31.1% | +12.7 | n/a | no target · vendors with a registry record: 241 rows, 100.0% filled |
| P08 | 25137 | 29.2% | 29.2% | +14.9 | n/a | no target · vendors with a registry record: 7339 rows, 100.0% filled |
| P09 | 298 | 91.3% | 91.3% | +0.2 | n/a | no target · vendors with a registry record: 272 rows, 100.0% filled |
| P10 | 3662 | 34.8% | 34.8% | +1.6 | n/a | no target · vendors with a registry record: 1274 rows, 100.0% filled |
| P11 | 1461 | 50.3% | 50.3% | -42.0 | n/a | no target · vendors with a registry record: 735 rows, 100.0% filled |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 15 rows, 100.0% filled |
| P13 | 33504 | 13.6% | 13.6% | +13.6 | n/a | no target · vendors with a registry record: 4569 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 93.9% | 93.9% | +5.2 | 90% | ✅ met |
| P01T | 334 | 70.7% | 70.7% | +14.4 | 90% | ❌ 19 pts to go |
| P01_GOLD | 626 | 87.5% | 87.5% | +3.8 | 95% | 🟡 8 pts to go |
| P02 | 488 | 86.9% | 86.9% | +1.7 | 95% | 🟡 8 pts to go |
| P03 | 264 | 84.5% | 84.5% | +5.6 | 85% | 🟡 0 pts to go |
| P04 | 4694 | 60.9% | 60.9% | +4.5 | 90% | ❌ 29 pts to go |
| P05 | 422 | 79.1% | 79.1% | +11.4 | 75% | ✅ met |
| P06M | 14527 | 92.1% | 92.1% | +5.0 | n/a | no target |
| P06T | 60669 | 43.2% | 43.2% | +14.2 | n/a | no target |
| P06 | 295 | 75.9% | 75.9% | +19.0 | 80% | 🟡 4 pts to go |
| P07 | 774 | 59.9% | 60.1% | +13.7 | 80% | ❌ 20 pts to go |
| P08 | 25137 | 55.3% | 55.4% | +16.8 | 75% | ❌ 20 pts to go |
| P09 | 298 | 76.8% | 76.8% | -0.4 | 95% | ❌ 18 pts to go |
| P10 | 3662 | 48.6% | 48.6% | +9.6 | 70% | ❌ 21 pts to go |
| P11 | 1461 | 31.1% | 31.1% | +21.5 | 65% | ❌ 34 pts to go |
| P12 | 15 | 80.0% | 80.0% | +5.0 | 80% | ✅ met |
| P13 | 33504 | 51.7% | 51.7% | +12.5 | 60% | 🟡 8 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 25.8% | 25.8% | +6.2 | 50% | ❌ 24 pts to go |
| P01T | 334 | 21.3% | 21.3% | +8.0 | n/a | no target |
| P01_GOLD | 626 | 19.5% | 19.5% | -1.1 | 40% | ❌ 20 pts to go |
| P02 | 488 | 19.9% | 19.9% | +1.0 | 40% | ❌ 20 pts to go |
| P03 | 264 | 21.2% | 21.2% | -1.1 | 40% | ❌ 19 pts to go |
| P04 | 4694 | 15.2% | 15.2% | -1.1 | 40% | ❌ 25 pts to go |
| P05 | 422 | 17.5% | 17.5% | -2.2 | 25% | 🟡 8 pts to go |
| P06M | 14527 | 13.5% | 13.5% | +4.7 | n/a | no target |
| P06T | 60669 | 9.4% | 9.4% | +1.9 | n/a | no target |
| P06 | 295 | 15.6% | 15.6% | +2.8 | 35% | ❌ 19 pts to go |
| P07 | 774 | 14.9% | 14.9% | +3.4 | 35% | ❌ 20 pts to go |
| P08 | 25137 | 16.2% | 16.2% | +5.8 | 35% | ❌ 19 pts to go |
| P09 | 298 | 16.1% | 16.1% | -0.1 | n/a | no target |
| P10 | 3662 | 11.0% | 11.0% | +4.5 | 30% | ❌ 19 pts to go |
| P11 | 1461 | 7.4% | 7.4% | +6.2 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | -5.8 | n/a | no target |
| P13 | 33504 | 17.7% | 17.7% | -3.3 | 30% | ❌ 12 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 90.1% | 90.1% | -1.8 | 100% | 🟡 10 pts to go |
| P01_GOLD | 626 | 90.7% | 90.7% | +1.2 | 100% | 🟡 9 pts to go |
| P02 | 488 | 95.7% | 95.7% | +0.4 | 100% | 🟡 4 pts to go |
| P03 | 264 | 89.4% | 89.4% | -0.1 | 100% | ❌ 11 pts to go |
| P04 | 4694 | 76.4% | 76.4% | +0.5 | 100% | ❌ 24 pts to go |
| P05 | 422 | 89.3% | 89.3% | +1.9 | 100% | ❌ 11 pts to go |
| P06M | 14527 | 99.2% | 99.2% | +0.4 | n/a | no target |
| P06T | 60669 | 74.5% | 74.5% | -2.9 | n/a | no target |
| P06 | 295 | 81.7% | 81.7% | +0.7 | 95% | ❌ 13 pts to go |
| P07 | 774 | 83.9% | 83.9% | +0.3 | 95% | ❌ 11 pts to go |
| P08 | 25137 | 80.9% | 80.9% | +0.7 | 95% | ❌ 14 pts to go |
| P09 | 298 | 96.3% | 96.3% | +0.6 | 100% | 🟡 4 pts to go |
| P10 | 3662 | 68.5% | 68.5% | +3.4 | 95% | ❌ 26 pts to go |
| P11 | 1461 | 49.9% | 49.9% | -37.3 | 80% | ❌ 30 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 33504 | 77.6% | 77.6% | +2.4 | 95% | ❌ 17 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 86.4% | 86.4% | +0.8 | n/a | no target |
| P01T | 334 | 75.4% | 75.4% | +11.8 | n/a | no target |
| P01_GOLD | 626 | 73.0% | 73.0% | +3.5 | 90% | ❌ 17 pts to go |
| P02 | 488 | 77.3% | 77.3% | +1.6 | 95% | ❌ 18 pts to go |
| P03 | 264 | 75.0% | 75.0% | +1.2 | 95% | ❌ 20 pts to go |
| P04 | 4694 | 69.4% | 69.4% | +2.8 | 95% | ❌ 26 pts to go |
| P05 | 422 | 73.5% | 73.5% | +3.0 | 90% | ❌ 16 pts to go |
| P06M | 14527 | 87.1% | 87.1% | +0.7 | n/a | no target |
| P06T | 60669 | 65.5% | 65.5% | +17.6 | n/a | no target |
| P06 | 295 | 70.5% | 70.5% | +7.4 | 95% | ❌ 24 pts to go |
| P07 | 774 | 66.3% | 66.3% | +11.3 | 90% | ❌ 24 pts to go |
| P08 | 25137 | 69.1% | 69.1% | +10.3 | 95% | ❌ 26 pts to go |
| P09 | 298 | 86.9% | 86.9% | +0.8 | 100% | ❌ 13 pts to go |
| P10 | 3662 | 62.5% | 62.5% | +6.0 | 95% | ❌ 32 pts to go |
| P11 | 1461 | 29.2% | 29.2% | +18.0 | 75% | ❌ 46 pts to go |
| P12 | 15 | 93.3% | 93.3% | +18.3 | n/a | no target |
| P13 | 33504 | 76.7% | 76.7% | +29.1 | 95% | ❌ 18 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 87.9% | 87.9% | +16.8 | n/a | no target |
| P01T | 334 | 87.1% | 87.1% | +13.0 | 95% | 🟡 8 pts to go |
| P01_GOLD | 626 | 84.8% | 84.8% | +4.1 | 90% | 🟡 5 pts to go |
| P02 | 488 | 91.0% | 91.0% | +5.2 | 95% | 🟡 4 pts to go |
| P03 | 264 | 85.6% | 85.6% | +1.6 | 95% | 🟡 9 pts to go |
| P04 | 4694 | 89.2% | 89.2% | +5.9 | 90% | 🟡 1 pts to go |
| P05 | 422 | 93.1% | 93.1% | +4.6 | 95% | 🟡 2 pts to go |
| P06M | 14527 | 94.3% | 94.3% | +27.6 | n/a | no target |
| P06T | 60669 | 80.7% | 80.7% | +19.2 | n/a | no target |
| P06 | 295 | 92.9% | 92.9% | +10.8 | 100% | 🟡 7 pts to go |
| P07 | 774 | 92.5% | 92.5% | +15.3 | 100% | 🟡 8 pts to go |
| P08 | 25137 | 92.7% | 92.7% | +15.6 | 100% | 🟡 7 pts to go |
| P09 | 298 | 73.5% | 73.5% | +4.9 | n/a | no target |
| P10 | 3662 | 91.7% | 91.7% | +4.9 | 100% | 🟡 8 pts to go |
| P11 | 1461 | 42.3% | 42.3% | +23.5 | 80% | ❌ 38 pts to go |
| P12 | 15 | 100.0% | 100.0% | +25.0 | n/a | no target |
| P13 | 33504 | 86.8% | 86.8% | +35.8 | 95% | 🟡 8 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 3.0% | 3.0% | -1.1 | n/a | no target |
| P01T | 334 | 8.1% | 8.1% | -0.3 | n/a | no target |
| P01_GOLD | 626 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 488 | 23.6% | 23.6% | -0.9 | 40% | ❌ 16 pts to go |
| P03 | 264 | 9.1% | 9.1% | +0.1 | 20% | ❌ 11 pts to go |
| P04 | 4694 | 2.8% | 2.8% | -0.8 | 20% | ❌ 17 pts to go |
| P05 | 422 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 14527 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 60669 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 295 | 5.8% | 5.8% | -0.4 | n/a | no target |
| P07 | 774 | 7.6% | 7.6% | +0.3 | n/a | no target |
| P08 | 25137 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 298 | 7.7% | 7.7% | +0.1 | n/a | no target |
| P10 | 3662 | 0.8% | 0.8% | -0.2 | n/a | no target |
| P11 | 1461 | 1.0% | 1.0% | +0.8 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +6.7 | n/a | no target |
| P13 | 33504 | 0.6% | 0.6% | +0.2 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 18.9% | 18.9% | -7.9 | n/a | no target |
| P01T | 334 | 23.1% | 23.1% | -1.0 | 70% | ❌ 47 pts to go |
| P01_GOLD | 626 | 43.5% | 43.5% | +0.2 | 80% | ❌ 36 pts to go |
| P02 | 488 | 55.7% | 55.7% | -1.1 | 90% | ❌ 34 pts to go |
| P03 | 264 | 18.6% | 18.6% | -0.5 | 60% | ❌ 41 pts to go |
| P04 | 4694 | 17.3% | 17.3% | -6.4 | 85% | ❌ 68 pts to go |
| P05 | 422 | 11.6% | 11.6% | -0.3 | 50% | ❌ 38 pts to go |
| P06M | 14527 | 0.7% | 0.7% | +0.3 | n/a | no target |
| P06T | 60669 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06 | 295 | 15.9% | 15.9% | -0.3 | n/a | no target |
| P07 | 774 | 11.2% | 11.2% | -1.8 | n/a | no target |
| P08 | 25137 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 298 | 77.5% | 77.5% | -0.1 | 95% | ❌ 18 pts to go |
| P10 | 3662 | 1.9% | 1.9% | +0.2 | n/a | no target |
| P11 | 1461 | 16.7% | 16.7% | +13.1 | n/a | no target |
| P12 | 15 | 26.7% | 26.7% | +1.7 | n/a | no target |
| P13 | 33504 | 0.9% | 0.9% | +0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 6.8% | 6.8% | -0.4 | n/a | no target |
| P01T | 334 | 11.4% | 11.4% | -0.6 | n/a | no target |
| P01_GOLD | 626 | 34.0% | 34.0% | +0.1 | 70% | ❌ 36 pts to go |
| P02 | 488 | 37.9% | 37.9% | -1.0 | 75% | ❌ 37 pts to go |
| P03 | 264 | 18.6% | 18.6% | -0.5 | 55% | ❌ 36 pts to go |
| P04 | 4694 | 17.2% | 17.2% | -6.4 | 75% | ❌ 58 pts to go |
| P05 | 422 | 10.7% | 10.7% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 14527 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 60669 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 295 | 7.5% | 7.5% | -0.8 | n/a | no target |
| P07 | 774 | 5.3% | 5.3% | -1.1 | n/a | no target |
| P08 | 25137 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 298 | 75.2% | 75.2% | +0.0 | 95% | ❌ 20 pts to go |
| P10 | 3662 | 1.1% | 1.1% | +0.1 | n/a | no target |
| P11 | 1461 | 16.4% | 16.4% | +12.8 | n/a | no target |
| P12 | 15 | 20.0% | 20.0% | +7.5 | n/a | no target |
| P13 | 33504 | 0.6% | 0.6% | +0.2 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 8.3% | 8.3% | +2.1 | n/a | no target |
| P01T | 334 | 6.6% | 6.6% | -2.7 | n/a | no target |
| P01_GOLD | 626 | 58.0% | 58.1% | +0.0 | 80% | ❌ 22 pts to go |
| P02 | 488 | 43.6% | 43.9% | -2.2 | 75% | ❌ 31 pts to go |
| P03 | 264 | 37.5% | 37.5% | -0.4 | 70% | ❌ 32 pts to go |
| P04 | 4694 | 16.9% | 17.3% | -6.2 | 70% | ❌ 53 pts to go |
| P05 | 422 | 14.2% | 14.2% | -0.1 | 50% | ❌ 36 pts to go |
| P06M | 14527 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 60669 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 295 | 15.6% | 15.6% | +2.2 | n/a | no target |
| P07 | 774 | 2.1% | 2.1% | +0.1 | n/a | no target |
| P08 | 25137 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 298 | 46.3% | 46.6% | +0.4 | 80% | ❌ 34 pts to go |
| P10 | 3662 | 1.0% | 1.0% | -0.2 | n/a | no target |
| P11 | 1461 | 6.9% | 7.0% | +5.8 | n/a | no target |
| P12 | 15 | 40.0% | 40.0% | +2.5 | n/a | no target |
| P13 | 33504 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 18.2% | 18.2% | +6.9 | n/a | no target |
| P01T | 334 | 16.2% | 16.2% | -5.8 | 60% | ❌ 44 pts to go |
| P01_GOLD | 626 | 63.6% | 63.6% | +0.0 | 70% | 🟡 6 pts to go |
| P02 | 488 | 38.1% | 38.1% | -0.8 | 50% | ❌ 12 pts to go |
| P03 | 264 | 48.1% | 48.1% | -1.9 | 55% | 🟡 7 pts to go |
| P04 | 4694 | 10.4% | 10.4% | -2.9 | 40% | ❌ 30 pts to go |
| P05 | 422 | 17.1% | 17.1% | -0.2 | 40% | ❌ 23 pts to go |
| P06M | 14527 | 2.3% | 2.3% | +1.6 | n/a | no target |
| P06T | 60669 | 1.6% | 1.6% | -0.8 | n/a | no target |
| P06 | 295 | 21.0% | 21.0% | +1.3 | n/a | no target |
| P07 | 774 | 7.1% | 7.1% | +0.4 | n/a | no target |
| P08 | 25137 | 2.9% | 2.9% | +0.3 | n/a | no target |
| P09 | 298 | 5.7% | 5.7% | -0.2 | n/a | no target |
| P10 | 3662 | 4.2% | 4.2% | -0.3 | n/a | no target |
| P11 | 1461 | 5.2% | 5.2% | +0.9 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | -5.8 | n/a | no target |
| P13 | 33504 | 0.3% | 0.3% | +0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 21.2% | 21.2% | +4.7 | n/a | no target |
| P01T | 334 | 21.9% | 21.9% | -3.4 | 65% | ❌ 43 pts to go |
| P01_GOLD | 626 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 488 | 23.2% | 23.2% | -0.7 | 50% | ❌ 27 pts to go |
| P03 | 264 | 52.3% | 52.3% | +0.0 | 60% | 🟡 8 pts to go |
| P04 | 4694 | 4.5% | 4.5% | -1.3 | 40% | ❌ 36 pts to go |
| P05 | 422 | 19.7% | 19.7% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 14527 | 1.4% | 1.4% | +1.1 | n/a | no target |
| P06T | 60669 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 295 | 33.6% | 33.6% | +1.9 | n/a | no target |
| P07 | 774 | 7.4% | 7.4% | +0.5 | n/a | no target |
| P08 | 25137 | 1.3% | 1.3% | +0.2 | n/a | no target |
| P09 | 298 | 9.7% | 9.7% | -0.2 | n/a | no target |
| P10 | 3662 | 2.3% | 2.3% | -0.3 | n/a | no target |
| P11 | 1461 | 5.2% | 5.2% | +4.2 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +6.7 | n/a | no target |
| P13 | 33504 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 12.9% | 12.9% | +6.7 | n/a | no target |
| P01T | 334 | 11.4% | 11.4% | -3.1 | n/a | no target |
| P01_GOLD | 626 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 488 | 35.7% | 35.7% | -1.7 | n/a | no target |
| P03 | 264 | 52.3% | 52.3% | -0.8 | 60% | 🟡 8 pts to go |
| P04 | 4694 | 9.5% | 9.5% | -3.4 | n/a | no target |
| P05 | 422 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 14527 | 0.5% | 0.5% | +0.2 | n/a | no target |
| P06T | 60669 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06 | 295 | 24.7% | 24.7% | +3.0 | n/a | no target |
| P07 | 774 | 7.6% | 7.6% | +0.4 | n/a | no target |
| P08 | 25137 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 298 | 18.1% | 18.1% | -0.1 | n/a | no target |
| P10 | 3662 | 2.0% | 2.0% | -0.3 | n/a | no target |
| P11 | 1461 | 4.7% | 4.7% | +3.9 | n/a | no target |
| P12 | 15 | 13.3% | 13.3% | +13.3 | n/a | no target |
| P13 | 33504 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 11.4% | 11.4% | +0.1 | 15% | 🟡 4 pts to go |
| P01T | 334 | 10.2% | 10.2% | -0.9 | 15% | 🟡 5 pts to go |
| P01_GOLD | 626 | 35.5% | 35.5% | +0.2 | 40% | 🟡 4 pts to go |
| P02 | 488 | 12.7% | 12.9% | +0.2 | 25% | ❌ 12 pts to go |
| P03 | 264 | 17.4% | 17.4% | -0.6 | 25% | 🟡 8 pts to go |
| P04 | 4694 | 2.2% | 2.2% | -0.6 | 15% | ❌ 13 pts to go |
| P05 | 422 | 6.6% | 6.6% | -0.2 | 15% | 🟡 8 pts to go |
| P06M | 14527 | 0.9% | 0.9% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 60669 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 295 | 10.2% | 10.2% | +0.9 | 15% | 🟡 5 pts to go |
| P07 | 774 | 4.3% | 4.3% | +1.1 | 15% | ❌ 11 pts to go |
| P08 | 25137 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |
| P09 | 298 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 3662 | 1.4% | 1.4% | +0.4 | 15% | ❌ 14 pts to go |
| P11 | 1461 | 1.6% | 1.6% | +1.4 | 15% | ❌ 13 pts to go |
| P12 | 15 | 0.0% | 0.0% | -12.5 | 15% | ❌ 15 pts to go |
| P13 | 33504 | 0.8% | 0.8% | +0.4 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 5.3% | 5.3% | -0.9 | 15% | 🟡 10 pts to go |
| P01T | 334 | 8.4% | 8.4% | -3.6 | 25% | ❌ 17 pts to go |
| P01_GOLD | 626 | 29.2% | 29.2% | +0.0 | 25% | ✅ met |
| P02 | 488 | 24.2% | 24.2% | -1.2 | 15% | ✅ met |
| P03 | 264 | 22.0% | 22.0% | +0.5 | 15% | ✅ met |
| P04 | 4694 | 3.2% | 3.2% | -0.9 | 15% | ❌ 12 pts to go |
| P05 | 422 | 11.1% | 11.1% | +0.3 | 15% | 🟡 4 pts to go |
| P06M | 14527 | 0.5% | 0.5% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 60669 | 0.2% | 0.2% | -0.1 | 15% | ❌ 15 pts to go |
| P06 | 295 | 8.1% | 8.1% | +0.5 | 15% | 🟡 7 pts to go |
| P07 | 774 | 2.7% | 2.7% | -0.4 | 15% | ❌ 12 pts to go |
| P08 | 25137 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 298 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 3662 | 1.3% | 1.3% | -0.3 | 15% | ❌ 14 pts to go |
| P11 | 1461 | 2.7% | 2.7% | +2.2 | 15% | ❌ 12 pts to go |
| P12 | 15 | 20.0% | 20.0% | -5.0 | 15% | ✅ met |
| P13 | 33504 | 0.1% | 0.1% | +0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 2.3% | 2.3% | +2.3 | 20% | ❌ 18 pts to go |
| P01T | 334 | 3.6% | 3.6% | -0.3 | 20% | ❌ 16 pts to go |
| P01_GOLD | 626 | 4.5% | 4.5% | +0.2 | 20% | ❌ 16 pts to go |
| P02 | 488 | 1.4% | 1.4% | +0.1 | 20% | ❌ 19 pts to go |
| P03 | 264 | 1.5% | 1.5% | -0.1 | 20% | ❌ 18 pts to go |
| P04 | 4694 | 0.5% | 0.5% | -0.1 | 20% | ❌ 20 pts to go |
| P05 | 422 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 14527 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 295 | 1.4% | 1.4% | +0.0 | 20% | ❌ 19 pts to go |
| P07 | 774 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 25137 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P09 | 298 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 3662 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1461 | 0.3% | 0.3% | +0.3 | 20% | ❌ 20 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 1.5% | 1.5% | +0.5 | 15% | ❌ 14 pts to go |
| P01T | 334 | 2.1% | 2.1% | -0.3 | 15% | ❌ 13 pts to go |
| P01_GOLD | 626 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 488 | 11.5% | 11.5% | -0.5 | 15% | 🟡 4 pts to go |
| P03 | 264 | 20.1% | 20.1% | -0.6 | 15% | ✅ met |
| P04 | 4694 | 1.9% | 1.9% | -0.5 | 15% | ❌ 13 pts to go |
| P05 | 422 | 2.8% | 2.8% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 14527 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P06T | 60669 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 295 | 5.1% | 5.1% | -0.1 | 15% | 🟡 10 pts to go |
| P07 | 774 | 1.7% | 1.7% | +0.0 | 15% | ❌ 13 pts to go |
| P08 | 25137 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 298 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 3662 | 0.7% | 0.7% | -0.2 | 15% | ❌ 14 pts to go |
| P11 | 1461 | 1.2% | 1.2% | +0.9 | 15% | ❌ 14 pts to go |
| P12 | 15 | 6.7% | 6.7% | +6.7 | 15% | 🟡 8 pts to go |
| P13 | 33504 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 15.2% | 15.2% | +8.0 | 20% | 🟡 5 pts to go |
| P01T | 334 | 12.0% | 12.0% | -3.1 | 40% | ❌ 28 pts to go |
| P01_GOLD | 626 | 46.2% | 46.2% | +0.4 | 40% | ✅ met |
| P02 | 488 | 41.0% | 41.0% | -1.8 | 20% | ✅ met |
| P03 | 264 | 49.2% | 49.2% | +0.4 | 35% | ✅ met |
| P04 | 4694 | 11.4% | 11.4% | -4.0 | 20% | 🟡 9 pts to go |
| P05 | 422 | 15.4% | 15.4% | +0.6 | 20% | 🟡 5 pts to go |
| P06M | 14527 | 0.9% | 0.9% | +0.4 | 20% | ❌ 19 pts to go |
| P06T | 60669 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 295 | 24.4% | 24.4% | +2.3 | 20% | ✅ met |
| P07 | 774 | 7.9% | 7.9% | +0.8 | 20% | ❌ 12 pts to go |
| P08 | 25137 | 1.1% | 1.1% | +0.2 | 20% | ❌ 19 pts to go |
| P09 | 298 | 18.8% | 18.8% | +0.6 | 20% | 🟡 1 pts to go |
| P10 | 3662 | 3.0% | 3.0% | -0.4 | 20% | ❌ 17 pts to go |
| P11 | 1461 | 4.9% | 4.9% | +3.9 | 20% | ❌ 15 pts to go |
| P12 | 15 | 6.7% | 6.7% | +6.7 | 20% | ❌ 13 pts to go |
| P13 | 33504 | 0.6% | 0.6% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 32.6% | 32.6% | -11.7 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 69.5% | 69.5% | +0.0 | 95% | ❌ 26 pts to go |
| P02 | 488 | 60.0% | 60.0% | -3.0 | 95% | ❌ 35 pts to go |
| P03 | 264 | 53.0% | 53.0% | -1.7 | 90% | ❌ 37 pts to go |
| P04 | 4694 | 19.7% | 19.7% | -7.4 | 85% | ❌ 65 pts to go |
| P05 | 422 | 37.7% | 37.7% | +1.2 | 75% | ❌ 37 pts to go |
| P06M | 14527 | 35.8% | 35.8% | -14.3 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 88.9% | 88.9% | -0.5 | 100% | ❌ 11 pts to go |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 6.0% | 6.0% | +5.1 | 60% | ❌ 54 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 32.6% | 32.6% | -11.7 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 488 | 63.3% | 63.3% | -3.2 | 100% | ❌ 37 pts to go |
| P03 | 264 | 58.7% | 58.7% | -1.8 | n/a | no target |
| P04 | 4694 | 20.2% | 20.2% | -7.6 | 95% | ❌ 75 pts to go |
| P05 | 422 | 33.4% | 33.4% | +0.4 | 80% | ❌ 47 pts to go |
| P06M | 14527 | 35.8% | 35.8% | -14.3 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 92.3% | 92.3% | -0.4 | 100% | 🟡 8 pts to go |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 6.4% | 6.4% | +5.4 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 81.1% | 81.1% | +2.7 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 51.6% | 51.6% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 488 | 54.9% | 54.9% | -2.7 | 90% | ❌ 35 pts to go |
| P03 | 264 | 42.4% | 42.4% | -1.7 | 85% | ❌ 43 pts to go |
| P04 | 4694 | 22.1% | 22.1% | -8.3 | 90% | ❌ 68 pts to go |
| P05 | 422 | 32.7% | 32.7% | -0.1 | 75% | ❌ 42 pts to go |
| P06M | 14527 | 89.8% | 89.8% | -0.6 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 84.6% | 84.6% | -0.5 | 95% | ❌ 10 pts to go |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 5.4% | 5.4% | +4.6 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 79.5% | 79.5% | +0.1 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 488 | 50.2% | 50.2% | -2.5 | 90% | ❌ 40 pts to go |
| P03 | 264 | 43.6% | 43.6% | -1.7 | 85% | ❌ 41 pts to go |
| P04 | 4694 | 18.9% | 18.9% | -7.1 | 90% | ❌ 71 pts to go |
| P05 | 422 | 43.4% | 43.4% | +0.5 | 75% | ❌ 32 pts to go |
| P06M | 14527 | 80.8% | 80.8% | -2.9 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 4.4% | 4.4% | +3.7 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 90.2% | 90.2% | +4.6 | n/a | no target |
| P01T | 334 | 94.6% | 94.6% | +2.4 | n/a | no target |
| P01_GOLD | 626 | 85.3% | 85.3% | -0.2 | 100% | ❌ 15 pts to go |
| P02 | 488 | 74.4% | 74.4% | -1.3 | 100% | ❌ 26 pts to go |
| P03 | 264 | 90.9% | 90.9% | -1.3 | n/a | no target |
| P04 | 4694 | 40.7% | 40.7% | -10.8 | 95% | ❌ 54 pts to go |
| P05 | 422 | 77.5% | 77.5% | -0.3 | 95% | ❌ 18 pts to go |
| P06M | 14527 | 98.9% | 98.9% | +0.6 | n/a | no target |
| P06T | 60669 | 89.8% | 89.8% | +6.1 | n/a | no target |
| P06 | 295 | 24.7% | 24.7% | -1.5 | n/a | no target |
| P07 | 774 | 14.7% | 14.7% | -4.4 | n/a | no target |
| P08 | 25137 | 8.9% | 8.9% | -2.1 | n/a | no target |
| P09 | 298 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 3662 | 72.2% | 72.2% | +0.5 | n/a | no target |
| P11 | 1461 | 67.9% | 67.9% | +51.8 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 90.2% | 90.2% | +4.6 | n/a | no target |
| P01T | 334 | 94.6% | 94.6% | +2.4 | n/a | no target |
| P01_GOLD | 626 | 88.5% | 88.5% | -0.2 | 100% | ❌ 12 pts to go |
| P02 | 488 | 75.4% | 75.6% | -1.4 | 100% | ❌ 25 pts to go |
| P03 | 264 | 91.7% | 91.7% | -1.3 | n/a | no target |
| P04 | 4694 | 43.2% | 43.2% | -11.9 | 95% | ❌ 52 pts to go |
| P05 | 422 | 89.6% | 89.6% | -0.6 | 70% | ✅ met |
| P06M | 14527 | 98.9% | 98.9% | +0.6 | n/a | no target |
| P06T | 60669 | 89.8% | 89.8% | +6.1 | n/a | no target |
| P06 | 295 | 24.7% | 24.7% | -1.5 | n/a | no target |
| P07 | 774 | 14.7% | 14.7% | -4.4 | n/a | no target |
| P08 | 25137 | 8.9% | 8.9% | -2.1 | n/a | no target |
| P09 | 298 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 3662 | 72.2% | 72.2% | +0.5 | n/a | no target |
| P11 | 1461 | 68.0% | 68.0% | +51.9 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 488 | 10.7% | 10.7% | -0.5 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 264 | 12.9% | 12.9% | -0.4 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 4694 | 1.2% | 1.2% | -0.4 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 422 | 2.6% | 2.6% | -0.4 | n/a | no target · rows from a source that publishes bids: 50 rows, 22.0% filled |
| P06M | 14527 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60669 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 298 | 3.4% | 3.4% | +0.4 | n/a | no target · rows from a source that publishes bids: 285 rows, 3.5% filled |
| P10 | 3662 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1461 | 0.9% | 0.9% | +0.8 | n/a | no target · rows from a source that publishes bids: 90 rows, 14.4% filled |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 15 rows, 0.0% filled |
| P13 | 33504 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 98.8% | -0.3 | n/a | no target |
| P01_GOLD | 626 | 53.2% | 82.4% | +0.0 | 90% | ❌ 37 pts to go |
| P02 | 488 | 50.0% | 88.1% | -2.5 | 90% | ❌ 40 pts to go |
| P03 | 264 | 44.3% | 80.7% | -1.4 | 90% | ❌ 46 pts to go |
| P04 | 4694 | 15.2% | 95.1% | -5.7 | 90% | ❌ 75 pts to go |
| P05 | 422 | 0.0% | 83.4% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 14527 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60669 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 298 | 2.3% | 4.0% | +0.0 | 90% | ❌ 88 pts to go |
| P10 | 3662 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1461 | 4.0% | 96.9% | +3.4 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.3% | 99.1% | -0.3 | n/a | no target |
| P01_GOLD | 626 | 25.9% | 55.1% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 488 | 49.2% | 87.3% | -2.4 | n/a | no target |
| P03 | 264 | 24.2% | 60.6% | -0.8 | n/a | no target |
| P04 | 4694 | 16.6% | 96.6% | -6.3 | n/a | no target |
| P05 | 422 | 0.5% | 83.9% | +0.0 | n/a | no target |
| P06M | 14527 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60669 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 298 | 40.9% | 42.6% | -1.0 | n/a | no target |
| P10 | 3662 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1461 | 3.7% | 96.6% | +3.1 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 1.2% | 100.0% | -0.3 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 488 | 53.9% | 92.0% | -2.7 | n/a | no target |
| P03 | 264 | 46.6% | 83.0% | -1.4 | n/a | no target |
| P04 | 4694 | 16.8% | 96.8% | -6.3 | n/a | no target |
| P05 | 422 | 4.5% | 87.9% | -0.2 | n/a | no target |
| P06M | 14527 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60669 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 774 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25137 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 298 | 63.1% | 64.8% | -0.9 | n/a | no target |
| P10 | 3662 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1461 | 4.1% | 97.0% | +3.5 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 33504 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 488 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4694 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 14527 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 60669 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 774 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25137 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 298 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 3662 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1461 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 33504 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 488 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4694 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 14527 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 60669 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 774 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25137 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 298 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 3662 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1461 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 33504 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 132 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 488 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4694 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 14527 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 60669 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 774 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25137 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 298 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 3662 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1461 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 33504 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

