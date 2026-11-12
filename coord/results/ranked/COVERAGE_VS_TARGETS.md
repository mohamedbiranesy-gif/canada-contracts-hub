# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **91 of 438 met** (20.8%); 61 within 10 points; 286 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 218, P01T 197, P01_GOLD 625, P02 468, P03 264, P04 3568, P05 424, P06M 20094, P06T 43524, P06 251, P07 679, P08 22779, P09 276, P10R 0, P10 2134, P11 1612, P12 11, P13 163017

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 13.8% | 7 | vendor GST/HST number (203 rows) |
| P01T | 197 | 1.0% | 34.5% | 8 | payment terms (154 rows) |
| P01_GOLD | 625 | 24.0% | 71.0% | 10 | payment terms (221 rows) |
| P02 | 468 | 7.5% | 54.9% | 9 | PO rule (355 rows) |
| P03 | 264 | 14.8% | 54.9% | 9 | PO rule (131 rows) |
| P04 | 3568 | 1.3% | 16.9% | 6 | PO rule (3367 rows) |
| P05 | 424 | 0.9% | 17.2% | 7 | payment terms (352 rows) |
| P06M | 20094 | 0.0% | 2.5% | 7 | PO rule (19715 rows) |
| P06T | 43524 | 0.1% | 9.5% | 6 | PO rule (43178 rows) |
| P06 | 251 | 0.0% | 11.2% | 6 | reference to quote (PO / contract / vendor id) (248 rows) |
| P07 | 679 | 0.0% | 2.5% | 6 | reference to quote (PO / contract / vendor id) (667 rows) |
| P08 | 22779 | 0.0% | 0.5% | 6 | reference to quote (PO / contract / vendor id) (22523 rows) |
| P09 | 276 | 1.4% | 41.7% | 8 | payment terms (258 rows) |
| P10 | 2134 | 0.0% | 1.3% | 5 | reference to quote (PO / contract / vendor id) (2134 rows) |
| P11 | 1612 | 0.1% | 7.0% | 6 | PO rule (1546 rows) |
| P12 | 11 | 0.0% | 36.4% | 8 | PO rule (11 rows) |
| P13 | 163017 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (163017 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 218 | 9 | 54 | 155 | 0 | 0 | 71 |
| P01T | 197 | 26 | 34 | 137 | 0 | 0 | 68 |
| P01_GOLD | 625 | 254 | 164 | 207 | 0 | 0 | 82 |
| P02 | 468 | 0 | 191 | 277 | 0 | 0 | 66 |
| P03 | 264 | 0 | 0 | 251 | 13 | 0 | 57 |
| P04 | 3568 | 0 | 0 | 2930 | 638 | 0 | 46 |
| P05 | 424 | 13 | 29 | 369 | 13 | 0 | 51 |
| P06M | 20094 | 0 | 17 | 20013 | 64 | 0 | 46 |
| P06T | 43524 | 0 | 25 | 28286 | 15213 | 0 | 38 |
| P06 | 251 | 18 | 40 | 193 | 0 | 0 | 69 |
| P07 | 679 | 0 | 21 | 635 | 23 | 0 | 54 |
| P08 | 22779 | 0 | 0 | 19996 | 2783 | 0 | 43 |
| P09 | 276 | 5 | 10 | 260 | 1 | 0 | 53 |
| P10 | 2134 | 3 | 13 | 1446 | 672 | 0 | 41 |
| P11 | 1612 | 7 | 13 | 34 | 0 | 1558 | 23 |
| P12 | 11 | 0 | 0 | 11 | 0 | 0 | 49 |
| P13 | 163017 | 12 | 63 | 162930 | 12 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 218 | 167 | 76.6% | tax treatment (27) |
| P01T | 197 | 115 | 58.4% | bill-to legal name and address (68) |
| P01_GOLD | 625 | 471 | 75.4% | bill-to legal name and address (97) |
| P02 | 468 | 316 | 67.5% | the buyer's PO / reference rule (86) |
| P03 | 264 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (264) |
| P04 | 3568 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3568) |
| P05 | 424 | 44 | 10.4% | a confirmed invoicing / AP or finance channel (337) |
| P06M | 20094 | 222 | 1.1% | a confirmed invoicing / AP or finance channel (19807) |
| P06T | 43524 | 233 | 0.5% | a confirmed invoicing / AP or finance channel (42904) |
| P06 | 251 | 41 | 16.3% | the buyer's PO / reference rule (108) |
| P07 | 679 | 8 | 1.2% | the buyer's PO / reference rule (270) |
| P08 | 22779 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (22779) |
| P09 | 276 | 40 | 14.5% | a confirmed invoicing / AP or finance channel (225) |
| P10 | 2134 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2056) |
| P11 | 1612 | 14 | 0.9% | a confirmed invoicing / AP or finance channel (1558) |
| P12 | 11 | 2 | 18.2% | a confirmed invoicing / AP or finance channel (9) |
| P13 | 163017 | 41 | 0.0% | a confirmed invoicing / AP or finance channel (160714) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 218 | 5 | 2.3% | 7 | 0 | the vendor's GST/HST number (BN9) (203) |
| P01T | 197 | 78 | 39.6% | 3 | 0 | the vendor's GST/HST number (BN9) (71) |
| P01_GOLD | 625 | 401 | 64.2% | 11 | 0 | the vendor's GST/HST number (BN9) (145) |
| P02 | 468 | 214 | 45.7% | 22 | 0 | the vendor's GST/HST number (BN9) (203) |
| P03 | 264 | 17 | 6.4% | 0 | 131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (96) |
| P04 | 3568 | 43 | 1.2% | 7 | 896 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2562) |
| P05 | 424 | 21 | 5.0% | 8 | 123 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (205) |
| P06M | 20094 | 7 | 0.0% | 12 | 486 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (19231) |
| P06T | 43524 | 250 | 0.6% | 14 | 10586 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (32251) |
| P06 | 251 | 24 | 9.6% | 48 | 0 | the vendor's GST/HST number (BN9) (111) |
| P07 | 679 | 6 | 0.9% | 107 | 32 | the vendor's GST/HST number (BN9) (321) |
| P08 | 22779 | 4 | 0.0% | 12 | 5134 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (17584) |
| P09 | 276 | 36 | 13.0% | 0 | 105 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (108) |
| P10 | 2134 | 7 | 0.3% | 15 | 302 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1730) |
| P11 | 1612 | 7 | 0.4% | 2 | 0 | a confirmed invoicing / AP or finance channel (1542) |
| P12 | 11 | 1 | 9.1% | 0 | 4 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5) |
| P13 | 163017 | 22 | 0.0% | 1115 | 65554 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (94971) |
| **all** | 260141 | 1143 | 0.4% | 1383 | 83353 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 209 | 0 | 0 | 0 | 138 | 9 | 0 | 167 | 180 | 0 |
| P01T | 171 | 0 | 0 | 0 | 102 | 62 | 27 | 137 | 155 | 4 |
| P01_GOLD | 371 | 0 | 0 | 0 | 13 | 79 | 30 | 202 | 236 | 2 |
| P02 | 468 | 0 | 468 | 0 | 37 | 56 | 15 | 355 | 284 | 2 |
| P03 | 264 | 0 | 264 | 0 | 17 | 45 | 29 | 131 | 138 | 2 |
| P04 | 3568 | 0 | 3568 | 0 | 1528 | 1290 | 964 | 3367 | 3127 | 33 |
| P05 | 411 | 0 | 358 | 0 | 83 | 96 | 38 | 340 | 354 | 7 |
| P06M | 20094 | 0 | 20094 | 0 | 14279 | 1566 | 108 | 19715 | 19466 | 10 |
| P06T | 43524 | 0 | 43524 | 0 | 39228 | 28970 | 18503 | 43178 | 42773 | 380 |
| P06 | 233 | 0 | 0 | 0 | 117 | 69 | 44 | 172 | 201 | 4 |
| P07 | 679 | 0 | 679 | 0 | 437 | 285 | 117 | 636 | 638 | 5 |
| P08 | 22779 | 0 | 22779 | 0 | 17472 | 10402 | 4167 | 22510 | 22166 | 160 |
| P09 | 271 | 0 | 252 | 0 | 12 | 70 | 2 | 246 | 260 | 7 |
| P10 | 2131 | 0 | 2098 | 0 | 1106 | 1159 | 973 | 2063 | 2025 | 16 |
| P11 | 1605 | 1558 | 1510 | 0 | 766 | 1142 | 493 | 1546 | 1542 | 19 |
| P12 | 11 | 0 | 10 | 0 | 0 | 4 | 0 | 11 | 11 | 2 |
| P13 | 163005 | 0 | 162581 | 0 | 131102 | 105162 | 19 | 162660 | 161816 | 36 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 51.9% | 95% | 70248 |
| buyer_logo_url | P13 | 63.8% | 95% | 50925 |
| buyer_legal_name_as_published | P13 | 35.5% | 60% | 39956 |
| buyer_bn_as_published | P13 | 8.2% | 30% | 35551 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 32566 |
| ap_system_hint | P13 | 0.4% | 20% | 32001 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 24321 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 24268 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 23591 |
| vendor_registered_address | P08 | 30.2% | 70% | 9076 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 8693 |
| ap_system_hint | P06T | 0.6% | 20% | 8435 |
| buyer_phone | P08 | 66.1% | 95% | 6578 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 6438 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 6429 |
| buyer_payment_method_preference | P06T | 0.5% | 15% | 6316 |
| invoice_reference_hint | P08 | 2.3% | 25% | 5171 |
| buyer_legal_name_as_published | P08 | 54.3% | 75% | 4708 |
| vendor_phone | P08 | 64.5% | 85% | 4665 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 4545 |
| vendor_bn9 | P08 | 30.4% | 50% | 4463 |
| vendor_emails | P08 | 55.8% | 75% | 4372 |
| ap_system_hint | P08 | 1.0% | 20% | 4338 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 4011 |
| ap_system_hint | P06M | 1.0% | 20% | 3811 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 3316 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 3315 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3280 |
| vendor_trading_name | P08 | 35.7% | 50% | 3260 |
| buyer_address | P08 | 81.7% | 95% | 3036 |
| buyer_bn_as_published | P08 | 21.7% | 35% | 3027 |
| buyer_esignature_preference | P06M | 0.5% | 15% | 2919 |
| buyer_tax_exempt_status | P06M | 0.7% | 15% | 2878 |
| buyer_payment_method_preference | P06M | 0.7% | 15% | 2870 |
| average_contract_duration_days | P04 | 19.5% | 90% | 2518 |
| currency | P04 | 26.8% | 95% | 2434 |
| end_date | P04 | 24.4% | 90% | 2341 |
| ap_phone | P04 | 20.2% | 85% | 2311 |
| commodity_codes | P04 | 22.1% | 85% | 2246 |
| vendor_neq | P04 | 32.2% | 95% | 2241 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 92.2% | 92.2% | +3.1 | 50% | ✅ met |
| P01T | 197 | 94.9% | 94.9% | +1.1 | 50% | ✅ met |
| P01_GOLD | 625 | 92.0% | 94.6% | -0.2 | 95% | 🟡 3 pts to go |
| P02 | 468 | 75.0% | 76.5% | +1.0 | 95% | ❌ 20 pts to go |
| P03 | 264 | 81.1% | 84.5% | -0.3 | 95% | ❌ 14 pts to go |
| P04 | 3568 | 31.6% | 33.3% | +1.4 | 90% | ❌ 58 pts to go |
| P05 | 424 | 39.6% | 42.5% | +1.0 | 70% | ❌ 30 pts to go |
| P06M | 20094 | 92.3% | 92.3% | +0.5 | n/a | no target |
| P06T | 43524 | 99.0% | 99.0% | +0.4 | n/a | no target |
| P06 | 251 | 32.7% | 32.7% | -1.7 | 30% | ✅ met |
| P07 | 679 | 8.1% | 8.1% | +1.2 | 30% | ❌ 22 pts to go |
| P08 | 22779 | 2.3% | 2.3% | +1.0 | 25% | ❌ 23 pts to go |
| P09 | 276 | 98.9% | 99.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10 | 2134 | 3.3% | 3.3% | +0.2 | 25% | ❌ 22 pts to go |
| P11 | 1612 | 51.4% | 52.2% | +4.5 | 60% | 🟡 9 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163017 | 99.6% | 99.6% | -0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 197 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 5.9% | 5.9% | -0.2 | 50% | ❌ 44 pts to go |
| P02 | 468 | 5.8% | 5.8% | -0.4 | 50% | ❌ 44 pts to go |
| P03 | 264 | 1.9% | 1.9% | +0.4 | 40% | ❌ 38 pts to go |
| P04 | 3568 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 424 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 20094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 88.1% | 88.1% | +5.9 | n/a | no target |
| P01T | 197 | 77.2% | 77.2% | +2.7 | 50% | ✅ met |
| P01_GOLD | 625 | 67.7% | 67.7% | +0.9 | 85% | ❌ 17 pts to go |
| P02 | 468 | 65.6% | 65.6% | +0.8 | 90% | ❌ 24 pts to go |
| P03 | 264 | 59.8% | 59.8% | +0.1 | 85% | ❌ 25 pts to go |
| P04 | 3568 | 28.8% | 28.8% | +1.2 | 85% | ❌ 56 pts to go |
| P05 | 424 | 30.0% | 30.0% | +1.1 | 60% | ❌ 30 pts to go |
| P06M | 20094 | 92.0% | 92.0% | +0.5 | n/a | no target |
| P06T | 43524 | 98.9% | 98.9% | +0.5 | n/a | no target |
| P06 | 251 | 1.2% | 1.2% | +1.2 | n/a | no target |
| P07 | 679 | 1.8% | 1.8% | +1.8 | n/a | no target |
| P08 | 22779 | 1.1% | 1.1% | +1.1 | n/a | no target |
| P09 | 276 | 95.7% | 95.7% | -0.4 | 100% | 🟡 4 pts to go |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 48.3% | 48.3% | +5.0 | 60% | ❌ 12 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 197 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 51.5% | 51.5% | +0.7 | 80% | ❌ 28 pts to go |
| P02 | 468 | 57.7% | 57.7% | +0.8 | 60% | 🟡 2 pts to go |
| P03 | 264 | 50.0% | 50.0% | -0.2 | 80% | ❌ 30 pts to go |
| P04 | 3568 | 23.8% | 23.8% | +0.9 | 50% | ❌ 26 pts to go |
| P05 | 424 | 12.7% | 12.7% | +1.3 | 40% | ❌ 27 pts to go |
| P06M | 20094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 81.2% | 81.2% | -2.2 | 50% | ✅ met |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 4.0% | 4.0% | -1.6 | 40% | ❌ 36 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 197 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 61.1% | 61.1% | +0.7 | 85% | ❌ 24 pts to go |
| P02 | 468 | 57.9% | 57.9% | +1.7 | 90% | ❌ 32 pts to go |
| P03 | 264 | 58.7% | 58.7% | +0.1 | 85% | ❌ 26 pts to go |
| P04 | 3568 | 24.7% | 24.7% | +1.1 | 85% | ❌ 60 pts to go |
| P05 | 424 | 20.5% | 20.5% | +0.8 | 50% | ❌ 30 pts to go |
| P06M | 20094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 4.4% | 4.4% | -1.6 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 197 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 12.8% | 12.8% | -0.1 | 60% | ❌ 47 pts to go |
| P02 | 468 | 6.8% | 6.8% | +0.8 | 50% | ❌ 43 pts to go |
| P03 | 264 | 8.3% | 8.3% | -0.1 | 50% | ❌ 42 pts to go |
| P04 | 3568 | 2.0% | 2.0% | +0.2 | 40% | ❌ 38 pts to go |
| P05 | 424 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 20094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 3.6% | 3.6% | +0.3 | 50% | ❌ 46 pts to go |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 0.6% | 0.6% | -0.3 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 197 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 35.8% | 35.8% | +1.0 | 80% | ❌ 44 pts to go |
| P02 | 468 | 52.4% | 52.4% | +0.5 | 90% | ❌ 38 pts to go |
| P03 | 264 | 33.7% | 33.7% | +1.0 | 80% | ❌ 46 pts to go |
| P04 | 3568 | 22.1% | 22.1% | +0.5 | 85% | ❌ 63 pts to go |
| P05 | 424 | 6.6% | 6.6% | +1.1 | 50% | ❌ 43 pts to go |
| P06M | 20094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 73.2% | 73.2% | -1.1 | 95% | ❌ 22 pts to go |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 3.2% | 3.2% | -1.1 | 50% | ❌ 47 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 197 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.3% | 8.3% | -0.2 | 50% | ❌ 42 pts to go |
| P02 | 468 | 5.6% | 5.6% | -0.6 | 50% | ❌ 44 pts to go |
| P03 | 264 | 2.7% | 2.7% | +0.8 | 30% | ❌ 27 pts to go |
| P04 | 3568 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 424 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 20094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 197 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 468 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3568 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 20094 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43524 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 251 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 679 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22779 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2134 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1612 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 6.9% | 6.9% | -4.7 | 70% | ❌ 63 pts to go |
| P01T | 197 | 55.3% | 55.3% | +4.8 | 60% | 🟡 5 pts to go |
| P01_GOLD | 625 | 74.6% | 74.6% | -0.2 | 90% | ❌ 15 pts to go |
| P02 | 468 | 53.8% | 53.8% | +0.2 | 85% | ❌ 31 pts to go |
| P03 | 264 | 67.4% | 67.4% | -2.2 | 90% | ❌ 23 pts to go |
| P04 | 3568 | 38.0% | 38.0% | +3.0 | 75% | ❌ 37 pts to go |
| P05 | 424 | 54.2% | 54.2% | -0.5 | 50% | ✅ met |
| P06M | 20094 | 2.9% | 2.9% | -0.3 | n/a | no target |
| P06T | 43524 | 51.0% | 51.0% | +3.7 | n/a | no target |
| P06 | 251 | 43.0% | 43.0% | -1.0 | 40% | ✅ met |
| P07 | 679 | 31.2% | 31.2% | -1.8 | 50% | ❌ 19 pts to go |
| P08 | 22779 | 30.4% | 30.4% | -0.1 | 50% | ❌ 20 pts to go |
| P09 | 276 | 56.5% | 56.5% | -1.8 | 80% | ❌ 24 pts to go |
| P10 | 2134 | 37.7% | 37.7% | +3.2 | 40% | 🟡 2 pts to go |
| P11 | 1612 | 51.4% | 51.4% | +4.5 | 60% | 🟡 9 pts to go |
| P12 | 11 | 45.5% | 45.5% | -14.5 | 85% | ❌ 40 pts to go |
| P13 | 163017 | 45.5% | 45.5% | +13.8 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 50.9% | 50.9% | -8.8 | n/a | no target |
| P01T | 197 | 55.3% | 55.3% | +4.3 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.1 | 95% | ❌ 22 pts to go |
| P02 | 468 | 73.9% | 73.9% | +0.1 | 95% | ❌ 21 pts to go |
| P03 | 264 | 69.3% | 69.3% | -2.6 | 95% | ❌ 26 pts to go |
| P04 | 3568 | 53.1% | 53.1% | +3.9 | 95% | ❌ 42 pts to go |
| P05 | 424 | 58.3% | 58.3% | +0.0 | 70% | ❌ 12 pts to go |
| P06M | 20094 | 39.9% | 39.9% | -6.1 | n/a | no target |
| P06T | 43524 | 55.2% | 55.2% | -1.0 | n/a | no target |
| P06 | 251 | 39.8% | 39.8% | -1.2 | 80% | ❌ 40 pts to go |
| P07 | 679 | 31.2% | 31.2% | -0.7 | 70% | ❌ 39 pts to go |
| P08 | 22779 | 30.2% | 30.2% | -0.1 | 70% | ❌ 40 pts to go |
| P09 | 276 | 86.2% | 86.2% | -0.4 | 100% | ❌ 14 pts to go |
| P10 | 2134 | 38.4% | 38.4% | +2.9 | 70% | ❌ 32 pts to go |
| P11 | 1612 | 56.1% | 56.1% | +3.6 | 75% | ❌ 19 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 41.0% | 41.0% | +14.1 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 22.0% | 22.0% | +4.9 | n/a | no target |
| P01T | 197 | 60.9% | 60.9% | +7.3 | n/a | no target |
| P01_GOLD | 625 | 48.6% | 48.6% | -1.2 | 60% | ❌ 11 pts to go |
| P02 | 468 | 55.6% | 55.6% | -0.6 | 60% | 🟡 4 pts to go |
| P03 | 264 | 51.5% | 51.5% | -3.6 | 60% | 🟡 8 pts to go |
| P04 | 3568 | 42.6% | 42.6% | +0.5 | 55% | ❌ 12 pts to go |
| P05 | 424 | 23.3% | 23.3% | -1.3 | 50% | ❌ 27 pts to go |
| P06M | 20094 | 8.5% | 8.5% | +1.7 | n/a | no target |
| P06T | 43524 | 55.2% | 55.2% | +4.3 | n/a | no target |
| P06 | 251 | 49.4% | 49.4% | +1.8 | n/a | no target |
| P07 | 679 | 42.3% | 42.3% | +1.4 | 55% | ❌ 13 pts to go |
| P08 | 22779 | 35.7% | 35.7% | -0.5 | 50% | ❌ 14 pts to go |
| P09 | 276 | 71.7% | 71.7% | -0.6 | 70% | ✅ met |
| P10 | 2134 | 47.8% | 47.8% | +1.0 | 55% | 🟡 7 pts to go |
| P11 | 1612 | 56.7% | 56.7% | +4.5 | 50% | ✅ met |
| P12 | 11 | 90.9% | 90.9% | +4.2 | n/a | no target |
| P13 | 163017 | 3.1% | 3.1% | -0.3 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 37.2% | 37.2% | -13.2 | n/a | no target |
| P01T | 197 | 76.6% | 76.6% | +2.1 | n/a | no target |
| P01_GOLD | 625 | 49.9% | 49.9% | -0.6 | 70% | ❌ 20 pts to go |
| P02 | 468 | 56.4% | 56.4% | -1.8 | 70% | ❌ 14 pts to go |
| P03 | 264 | 50.4% | 50.4% | -0.9 | 70% | ❌ 20 pts to go |
| P04 | 3568 | 54.8% | 54.8% | +0.7 | 65% | ❌ 10 pts to go |
| P05 | 424 | 28.8% | 28.8% | +0.4 | 60% | ❌ 31 pts to go |
| P06M | 20094 | 29.5% | 29.5% | -7.1 | n/a | no target |
| P06T | 43524 | 75.7% | 75.7% | -4.3 | n/a | no target |
| P06 | 251 | 70.9% | 70.9% | +2.0 | 40% | ✅ met |
| P07 | 679 | 65.1% | 65.1% | +0.2 | 85% | ❌ 20 pts to go |
| P08 | 22779 | 64.5% | 64.5% | -0.8 | 85% | ❌ 20 pts to go |
| P09 | 276 | 56.2% | 56.2% | -3.1 | 85% | ❌ 29 pts to go |
| P10 | 2134 | 66.0% | 66.0% | +2.5 | 85% | ❌ 19 pts to go |
| P11 | 1612 | 64.8% | 64.8% | +2.9 | 75% | ❌ 10 pts to go |
| P12 | 11 | 36.4% | 36.4% | +9.7 | n/a | no target |
| P13 | 163017 | 91.9% | 91.9% | +0.7 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 41.7% | 41.7% | -14.9 | n/a | no target |
| P01T | 197 | 98.0% | 98.0% | +0.6 | n/a | no target |
| P01_GOLD | 625 | 78.6% | 78.6% | -1.0 | 90% | ❌ 11 pts to go |
| P02 | 468 | 82.1% | 82.1% | -1.8 | 90% | 🟡 8 pts to go |
| P03 | 264 | 85.2% | 85.2% | -2.6 | 90% | 🟡 5 pts to go |
| P04 | 3568 | 83.0% | 83.0% | -1.4 | 85% | 🟡 2 pts to go |
| P05 | 424 | 44.8% | 44.8% | +0.0 | 70% | ❌ 25 pts to go |
| P06M | 20094 | 35.6% | 35.6% | -8.0 | n/a | no target |
| P06T | 43524 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 251 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 679 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 22779 | 99.9% | 99.9% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 276 | 77.9% | 77.9% | -1.9 | 100% | ❌ 22 pts to go |
| P10 | 2134 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1612 | 97.6% | 97.6% | +0.3 | 100% | 🟡 2 pts to go |
| P12 | 11 | 54.5% | 54.5% | +1.2 | n/a | no target |
| P13 | 163017 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 16.1% | 16.1% | +0.6 | n/a | no target |
| P01T | 197 | 67.0% | 67.0% | +1.9 | n/a | no target |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.2 | 70% | ❌ 26 pts to go |
| P02 | 468 | 46.8% | 46.8% | -1.9 | 75% | ❌ 28 pts to go |
| P03 | 264 | 43.9% | 43.9% | +0.6 | 75% | ❌ 31 pts to go |
| P04 | 3568 | 38.6% | 38.6% | -0.1 | 70% | ❌ 31 pts to go |
| P05 | 424 | 21.7% | 21.7% | -0.3 | 55% | ❌ 33 pts to go |
| P06M | 20094 | 5.6% | 5.6% | +0.8 | n/a | no target |
| P06T | 43524 | 65.0% | 65.0% | +2.9 | n/a | no target |
| P06 | 251 | 53.8% | 53.8% | +6.9 | n/a | no target |
| P07 | 679 | 53.2% | 53.2% | +3.2 | 70% | ❌ 17 pts to go |
| P08 | 22779 | 55.8% | 55.8% | +1.0 | 75% | ❌ 19 pts to go |
| P09 | 276 | 47.1% | 47.1% | -2.1 | 85% | ❌ 38 pts to go |
| P10 | 2134 | 44.3% | 44.3% | +0.7 | 80% | ❌ 36 pts to go |
| P11 | 1612 | 57.4% | 57.4% | +3.1 | 70% | ❌ 13 pts to go |
| P12 | 11 | 27.3% | 27.3% | -12.7 | n/a | no target |
| P13 | 163017 | 5.4% | 5.4% | +0.2 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 41.7% | 41.7% | -14.9 | n/a | no target |
| P01T | 197 | 95.9% | 95.9% | +1.1 | n/a | no target |
| P01_GOLD | 625 | 72.0% | 72.0% | -1.8 | 90% | ❌ 18 pts to go |
| P02 | 468 | 76.5% | 76.5% | -2.5 | 90% | ❌ 14 pts to go |
| P03 | 264 | 81.8% | 81.8% | -1.5 | 90% | 🟡 8 pts to go |
| P04 | 3568 | 77.7% | 77.7% | +1.3 | 85% | 🟡 7 pts to go |
| P05 | 424 | 42.9% | 42.9% | -0.2 | 75% | ❌ 32 pts to go |
| P06M | 20094 | 35.5% | 35.5% | -7.8 | n/a | no target |
| P06T | 43524 | 97.1% | 97.1% | +0.4 | n/a | no target |
| P06 | 251 | 92.0% | 92.0% | +1.5 | n/a | no target |
| P07 | 679 | 93.7% | 93.7% | +1.2 | 100% | 🟡 6 pts to go |
| P08 | 22779 | 91.3% | 91.3% | +0.5 | 100% | 🟡 9 pts to go |
| P09 | 276 | 66.3% | 66.3% | +0.2 | n/a | no target |
| P10 | 2134 | 89.9% | 89.9% | +3.1 | 100% | ❌ 10 pts to go |
| P11 | 1612 | 89.1% | 89.1% | +1.4 | n/a | no target |
| P12 | 11 | 54.5% | 54.5% | +7.8 | n/a | no target |
| P13 | 163017 | 68.6% | 68.6% | +3.4 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 40.8% | 40.8% | -5.7 | n/a | no target · QC vendors: 51 rows, 100.0% filled |
| P01T | 197 | 9.1% | 9.1% | -0.3 | n/a | no target · QC vendors: 7 rows, 42.9% filled |
| P01_GOLD | 625 | 43.2% | 43.2% | -0.6 | 95% | ❌ 52 pts to go · QC vendors: 49 rows, 98.0% filled |
| P02 | 468 | 55.8% | 55.8% | +0.2 | 95% | ❌ 39 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 264 | 42.4% | 42.4% | -3.6 | 95% | ❌ 53 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3568 | 32.2% | 32.2% | +0.0 | 95% | ❌ 63 pts to go · QC vendors: 595 rows, 97.0% filled |
| P05 | 424 | 13.4% | 13.4% | -0.6 | n/a | no target · QC vendors: 36 rows, 91.7% filled |
| P06M | 20094 | 36.5% | 36.5% | -6.3 | n/a | no target · QC vendors: 5952 rows, 99.8% filled |
| P06T | 43524 | 4.4% | 4.4% | -0.9 | n/a | no target · QC vendors: 2223 rows, 63.0% filled |
| P06 | 251 | 7.6% | 7.6% | -0.8 | n/a | no target · QC vendors: 13 rows, 69.2% filled |
| P07 | 679 | 6.2% | 6.2% | -0.1 | n/a | no target · QC vendors: 35 rows, 71.4% filled |
| P08 | 22779 | 6.4% | 6.4% | -0.2 | n/a | no target · QC vendors: 1192 rows, 92.4% filled |
| P09 | 276 | 73.6% | 73.6% | -3.3 | 95% | ❌ 21 pts to go · QC vendors: 99 rows, 100.0% filled |
| P10 | 2134 | 15.2% | 15.2% | -0.4 | n/a | no target · QC vendors: 194 rows, 91.2% filled |
| P11 | 1612 | 13.3% | 13.3% | -1.5 | n/a | no target · QC vendors: 154 rows, 90.3% filled |
| P12 | 11 | 81.8% | 81.8% | +8.5 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 163017 | 23.5% | 23.5% | -2.7 | n/a | no target · QC vendors: 38310 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 50.0% | 50.0% | -8.9 | n/a | no target · vendors with a registry record: 109 rows, 100.0% filled |
| P01T | 197 | 55.3% | 55.3% | +4.3 | n/a | no target · vendors with a registry record: 109 rows, 100.0% filled |
| P01_GOLD | 625 | 80.8% | 80.8% | -0.7 | 100% | ❌ 19 pts to go · vendors with a registry record: 505 rows, 100.0% filled |
| P02 | 468 | 77.8% | 77.8% | +0.3 | 100% | ❌ 22 pts to go · vendors with a registry record: 364 rows, 100.0% filled |
| P03 | 264 | 78.0% | 78.0% | -3.0 | 100% | ❌ 22 pts to go · vendors with a registry record: 206 rows, 100.0% filled |
| P04 | 3568 | 53.9% | 53.9% | +4.2 | 100% | ❌ 46 pts to go · vendors with a registry record: 1922 rows, 100.0% filled |
| P05 | 424 | 63.0% | 63.0% | -0.3 | n/a | no target · vendors with a registry record: 267 rows, 100.0% filled |
| P06M | 20094 | 39.9% | 39.9% | -6.0 | n/a | no target · vendors with a registry record: 8010 rows, 100.0% filled |
| P06T | 43524 | 55.3% | 55.3% | -0.9 | n/a | no target · vendors with a registry record: 24074 rows, 100.0% filled |
| P06 | 251 | 40.6% | 40.6% | -0.8 | n/a | no target · vendors with a registry record: 102 rows, 100.0% filled |
| P07 | 679 | 31.7% | 31.7% | -0.6 | n/a | no target · vendors with a registry record: 215 rows, 100.0% filled |
| P08 | 22779 | 30.3% | 30.3% | -0.1 | n/a | no target · vendors with a registry record: 6903 rows, 100.0% filled |
| P09 | 276 | 89.5% | 89.5% | -1.1 | n/a | no target · vendors with a registry record: 247 rows, 100.0% filled |
| P10 | 2134 | 39.3% | 39.3% | +3.1 | n/a | no target · vendors with a registry record: 838 rows, 100.0% filled |
| P11 | 1612 | 56.9% | 56.9% | +3.3 | n/a | no target · vendors with a registry record: 918 rows, 100.0% filled |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P13 | 163017 | 41.0% | 41.0% | +14.1 | n/a | no target · vendors with a registry record: 66902 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 95.9% | 95.9% | +2.1 | 90% | ✅ met |
| P01T | 197 | 68.5% | 68.5% | -3.9 | 90% | ❌ 22 pts to go |
| P01_GOLD | 625 | 87.4% | 87.4% | -0.3 | 95% | 🟡 8 pts to go |
| P02 | 468 | 88.0% | 88.0% | +0.2 | 95% | 🟡 7 pts to go |
| P03 | 264 | 83.0% | 83.0% | -1.4 | 85% | 🟡 2 pts to go |
| P04 | 3568 | 63.8% | 63.8% | +0.8 | 90% | ❌ 26 pts to go |
| P05 | 424 | 77.4% | 77.4% | -1.7 | 75% | ✅ met |
| P06M | 20094 | 92.2% | 92.2% | +0.6 | n/a | no target |
| P06T | 43524 | 33.4% | 33.4% | -3.9 | n/a | no target |
| P06 | 251 | 72.5% | 72.5% | -1.1 | 80% | 🟡 8 pts to go |
| P07 | 679 | 58.0% | 58.2% | -1.8 | 80% | ❌ 22 pts to go |
| P08 | 22779 | 54.3% | 54.4% | -0.1 | 75% | ❌ 21 pts to go |
| P09 | 276 | 74.6% | 74.6% | -2.3 | 95% | ❌ 20 pts to go |
| P10 | 2134 | 45.7% | 45.7% | -1.0 | 70% | ❌ 24 pts to go |
| P11 | 1612 | 29.2% | 29.2% | -2.1 | 65% | ❌ 36 pts to go |
| P12 | 11 | 63.6% | 63.6% | -16.4 | 80% | ❌ 16 pts to go |
| P13 | 163017 | 35.5% | 35.5% | -12.0 | 60% | ❌ 24 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 17.4% | 17.4% | -2.8 | 50% | ❌ 33 pts to go |
| P01T | 197 | 15.7% | 15.7% | -0.4 | n/a | no target |
| P01_GOLD | 625 | 19.8% | 19.8% | +0.3 | 40% | ❌ 20 pts to go |
| P02 | 468 | 19.4% | 19.4% | +0.3 | 40% | ❌ 21 pts to go |
| P03 | 264 | 21.6% | 21.6% | +0.3 | 40% | ❌ 18 pts to go |
| P04 | 3568 | 15.5% | 15.5% | +0.3 | 40% | ❌ 24 pts to go |
| P05 | 424 | 20.3% | 20.3% | +2.8 | 25% | 🟡 5 pts to go |
| P06M | 20094 | 20.1% | 20.1% | +8.5 | n/a | no target |
| P06T | 43524 | 8.6% | 8.6% | +1.7 | n/a | no target |
| P06 | 251 | 20.3% | 20.3% | +7.5 | 35% | ❌ 15 pts to go |
| P07 | 679 | 21.2% | 21.2% | +7.1 | 35% | ❌ 14 pts to go |
| P08 | 22779 | 21.7% | 21.7% | +6.3 | 35% | ❌ 13 pts to go |
| P09 | 276 | 16.3% | 16.3% | +0.0 | n/a | no target |
| P10 | 2134 | 5.5% | 5.5% | -1.2 | 30% | ❌ 24 pts to go |
| P11 | 1612 | 6.0% | 6.0% | -1.4 | n/a | no target |
| P12 | 11 | 9.1% | 9.1% | +2.4 | n/a | no target |
| P13 | 163017 | 8.2% | 8.2% | -4.1 | 30% | ❌ 22 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 197 | 85.3% | 85.3% | +0.9 | 100% | ❌ 15 pts to go |
| P01_GOLD | 625 | 90.9% | 90.9% | +0.2 | 100% | 🟡 9 pts to go |
| P02 | 468 | 96.4% | 96.4% | +0.9 | 100% | 🟡 4 pts to go |
| P03 | 264 | 88.3% | 88.3% | -1.1 | 100% | ❌ 12 pts to go |
| P04 | 3568 | 72.4% | 72.4% | +1.0 | 100% | ❌ 28 pts to go |
| P05 | 424 | 90.3% | 90.3% | +1.0 | 100% | 🟡 10 pts to go |
| P06M | 20094 | 99.5% | 99.5% | +0.3 | n/a | no target |
| P06T | 43524 | 57.5% | 57.5% | -1.8 | n/a | no target |
| P06 | 251 | 80.9% | 80.9% | +2.1 | 95% | ❌ 14 pts to go |
| P07 | 679 | 82.5% | 82.5% | +1.3 | 95% | ❌ 12 pts to go |
| P08 | 22779 | 81.7% | 81.7% | +3.4 | 95% | ❌ 13 pts to go |
| P09 | 276 | 95.7% | 95.7% | -0.4 | 100% | 🟡 4 pts to go |
| P10 | 2134 | 54.3% | 54.3% | -0.1 | 95% | ❌ 41 pts to go |
| P11 | 1612 | 60.5% | 60.5% | +11.1 | 80% | ❌ 20 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163017 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 63.3% | 63.3% | -22.7 | n/a | no target |
| P01T | 197 | 69.5% | 69.5% | +1.3 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | -0.2 | 90% | ❌ 17 pts to go |
| P02 | 468 | 78.4% | 78.4% | +0.5 | 95% | ❌ 17 pts to go |
| P03 | 264 | 73.5% | 73.5% | -1.4 | 95% | ❌ 22 pts to go |
| P04 | 3568 | 69.0% | 69.0% | +0.1 | 95% | ❌ 26 pts to go |
| P05 | 424 | 72.2% | 72.2% | -1.3 | 90% | ❌ 18 pts to go |
| P06M | 20094 | 72.0% | 72.0% | -14.9 | n/a | no target |
| P06T | 43524 | 50.9% | 50.9% | -6.3 | n/a | no target |
| P06 | 251 | 68.1% | 68.1% | -0.4 | 95% | ❌ 27 pts to go |
| P07 | 679 | 63.5% | 63.5% | -1.3 | 90% | ❌ 26 pts to go |
| P08 | 22779 | 66.1% | 66.1% | -1.7 | 95% | ❌ 29 pts to go |
| P09 | 276 | 85.5% | 85.5% | -1.5 | 100% | ❌ 14 pts to go |
| P10 | 2134 | 53.4% | 53.4% | -1.9 | 95% | ❌ 42 pts to go |
| P11 | 1612 | 28.4% | 28.4% | -0.5 | 75% | ❌ 47 pts to go |
| P12 | 11 | 81.8% | 81.8% | -11.5 | n/a | no target |
| P13 | 163017 | 51.9% | 51.9% | -18.9 | 95% | ❌ 43 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 69.7% | 69.7% | -17.9 | n/a | no target |
| P01T | 197 | 83.8% | 83.8% | +0.5 | 95% | ❌ 11 pts to go |
| P01_GOLD | 625 | 84.3% | 84.3% | -0.5 | 90% | 🟡 6 pts to go |
| P02 | 468 | 90.6% | 90.6% | +0.0 | 95% | 🟡 4 pts to go |
| P03 | 264 | 82.6% | 82.6% | -3.0 | 95% | ❌ 12 pts to go |
| P04 | 3568 | 90.6% | 90.6% | +1.4 | 90% | ✅ met |
| P05 | 424 | 91.7% | 91.7% | -1.4 | 95% | 🟡 3 pts to go |
| P06M | 20094 | 75.8% | 75.8% | -17.4 | n/a | no target |
| P06T | 43524 | 69.4% | 69.4% | -5.5 | n/a | no target |
| P06 | 251 | 90.0% | 90.0% | -2.3 | 100% | 🟡 10 pts to go |
| P07 | 679 | 89.8% | 89.8% | -2.4 | 100% | ❌ 10 pts to go |
| P08 | 22779 | 90.5% | 90.5% | -1.8 | 100% | 🟡 10 pts to go |
| P09 | 276 | 73.2% | 73.2% | +0.2 | n/a | no target |
| P10 | 2134 | 93.0% | 93.0% | +1.7 | 100% | 🟡 7 pts to go |
| P11 | 1612 | 45.3% | 45.3% | +3.4 | 80% | ❌ 35 pts to go |
| P12 | 11 | 90.9% | 90.9% | -9.1 | n/a | no target |
| P13 | 163017 | 63.8% | 63.8% | -19.9 | 95% | ❌ 31 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 3.7% | 3.7% | +0.6 | n/a | no target |
| P01T | 197 | 9.1% | 9.1% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 468 | 24.8% | 24.8% | -0.5 | 40% | ❌ 15 pts to go |
| P03 | 264 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P04 | 3568 | 3.3% | 3.3% | -0.2 | 20% | ❌ 17 pts to go |
| P05 | 424 | 3.1% | 3.1% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 20094 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 43524 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 251 | 5.2% | 5.2% | +0.1 | n/a | no target |
| P07 | 679 | 8.2% | 8.2% | -0.3 | n/a | no target |
| P08 | 22779 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 276 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P10 | 2134 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1612 | 0.8% | 0.8% | -0.2 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 163017 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 16.5% | 16.5% | -2.1 | n/a | no target |
| P01T | 197 | 20.3% | 20.3% | -2.1 | 70% | ❌ 50 pts to go |
| P01_GOLD | 625 | 42.4% | 42.4% | -1.1 | 80% | ❌ 38 pts to go |
| P02 | 468 | 57.3% | 57.3% | +0.0 | 90% | ❌ 33 pts to go |
| P03 | 264 | 18.9% | 18.9% | +0.3 | 60% | ❌ 41 pts to go |
| P04 | 3568 | 20.2% | 20.2% | -1.4 | 85% | ❌ 65 pts to go |
| P05 | 424 | 10.8% | 10.8% | -0.8 | 50% | ❌ 39 pts to go |
| P06M | 20094 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06T | 43524 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 251 | 14.7% | 14.7% | -0.7 | n/a | no target |
| P07 | 679 | 9.6% | 9.6% | -0.9 | n/a | no target |
| P08 | 22779 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 276 | 72.5% | 72.5% | -5.4 | 95% | ❌ 22 pts to go |
| P10 | 2134 | 1.6% | 1.6% | -0.1 | n/a | no target |
| P11 | 1612 | 14.1% | 14.1% | -2.6 | n/a | no target |
| P12 | 11 | 27.3% | 27.3% | +0.6 | n/a | no target |
| P13 | 163017 | 0.3% | 0.3% | -0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 6.9% | 6.9% | +0.7 | n/a | no target |
| P01T | 197 | 9.6% | 9.6% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | -0.1 | 70% | ❌ 36 pts to go |
| P02 | 468 | 39.1% | 39.1% | +0.0 | 75% | ❌ 36 pts to go |
| P03 | 264 | 18.9% | 18.9% | +0.3 | 55% | ❌ 36 pts to go |
| P04 | 3568 | 20.3% | 20.3% | -1.3 | 75% | ❌ 55 pts to go |
| P05 | 424 | 10.1% | 10.1% | -0.6 | 50% | ❌ 40 pts to go |
| P06M | 20094 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 43524 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 251 | 6.4% | 6.4% | +0.5 | n/a | no target |
| P07 | 679 | 4.7% | 4.7% | -0.5 | n/a | no target |
| P08 | 22779 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 276 | 69.2% | 69.2% | -6.0 | 95% | ❌ 26 pts to go |
| P10 | 2134 | 0.8% | 0.8% | -0.1 | n/a | no target |
| P11 | 1612 | 13.6% | 13.6% | -2.8 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | -1.8 | n/a | no target |
| P13 | 163017 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 8.7% | 8.7% | +0.9 | n/a | no target |
| P01T | 197 | 8.1% | 8.1% | -0.2 | n/a | no target |
| P01_GOLD | 625 | 57.1% | 57.3% | -0.9 | 80% | ❌ 23 pts to go |
| P02 | 468 | 45.3% | 45.5% | -0.4 | 75% | ❌ 30 pts to go |
| P03 | 264 | 35.6% | 35.6% | -1.7 | 70% | ❌ 34 pts to go |
| P04 | 3568 | 20.0% | 20.4% | -1.1 | 70% | ❌ 50 pts to go |
| P05 | 424 | 13.9% | 13.9% | -0.3 | 50% | ❌ 36 pts to go |
| P06M | 20094 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P06T | 43524 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 251 | 14.3% | 14.3% | -2.2 | n/a | no target |
| P07 | 679 | 1.5% | 1.5% | -0.5 | n/a | no target |
| P08 | 22779 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 276 | 47.5% | 47.5% | +0.9 | 80% | ❌ 32 pts to go |
| P10 | 2134 | 1.1% | 1.2% | -0.1 | n/a | no target |
| P11 | 1612 | 5.3% | 5.3% | -1.5 | n/a | no target |
| P12 | 11 | 36.4% | 36.4% | -3.6 | n/a | no target |
| P13 | 163017 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 17.4% | 17.4% | -1.2 | n/a | no target |
| P01T | 197 | 21.3% | 21.3% | -0.1 | 60% | ❌ 39 pts to go |
| P01_GOLD | 625 | 62.2% | 62.2% | -1.2 | 70% | 🟡 8 pts to go |
| P02 | 468 | 39.3% | 39.3% | -0.4 | 50% | ❌ 11 pts to go |
| P03 | 264 | 47.7% | 47.7% | -0.6 | 55% | 🟡 7 pts to go |
| P04 | 3568 | 12.4% | 12.4% | +0.2 | 40% | ❌ 28 pts to go |
| P05 | 424 | 16.5% | 16.5% | -0.6 | 40% | ❌ 24 pts to go |
| P06M | 20094 | 3.1% | 3.1% | +0.9 | n/a | no target |
| P06T | 43524 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P06 | 251 | 19.9% | 19.9% | -2.1 | n/a | no target |
| P07 | 679 | 6.0% | 6.0% | -0.6 | n/a | no target |
| P08 | 22779 | 2.7% | 2.7% | -0.2 | n/a | no target |
| P09 | 276 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10 | 2134 | 5.1% | 5.1% | +0.5 | n/a | no target |
| P11 | 1612 | 4.3% | 4.3% | -0.9 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 163017 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 23.4% | 23.4% | +1.7 | n/a | no target |
| P01T | 197 | 30.5% | 30.5% | +1.9 | 65% | ❌ 34 pts to go |
| P01_GOLD | 625 | 67.7% | 67.7% | -1.3 | 70% | 🟡 2 pts to go |
| P02 | 468 | 24.1% | 24.1% | -0.1 | 50% | ❌ 26 pts to go |
| P03 | 264 | 50.4% | 50.4% | -2.1 | 60% | 🟡 10 pts to go |
| P04 | 3568 | 5.6% | 5.6% | +0.2 | 40% | ❌ 34 pts to go |
| P05 | 424 | 19.8% | 19.8% | +0.1 | 45% | ❌ 25 pts to go |
| P06M | 20094 | 1.9% | 1.9% | +0.5 | n/a | no target |
| P06T | 43524 | 0.8% | 0.8% | +0.1 | n/a | no target |
| P06 | 251 | 31.5% | 31.5% | -2.9 | n/a | no target |
| P07 | 679 | 6.3% | 6.3% | -0.6 | n/a | no target |
| P08 | 22779 | 1.2% | 1.2% | -0.1 | n/a | no target |
| P09 | 276 | 10.9% | 10.9% | +1.1 | n/a | no target |
| P10 | 2134 | 3.3% | 3.3% | +0.2 | n/a | no target |
| P11 | 1612 | 4.1% | 4.1% | -1.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 163017 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 13.3% | 13.3% | +0.9 | n/a | no target |
| P01T | 197 | 13.7% | 13.7% | +0.2 | n/a | no target |
| P01_GOLD | 625 | 49.9% | 49.9% | +0.1 | 50% | 🟡 0 pts to go |
| P02 | 468 | 37.6% | 37.6% | +0.3 | n/a | no target |
| P03 | 264 | 50.8% | 50.8% | -1.3 | 60% | 🟡 9 pts to go |
| P04 | 3568 | 12.7% | 12.7% | +0.8 | n/a | no target |
| P05 | 424 | 15.1% | 15.1% | -0.1 | n/a | no target |
| P06M | 20094 | 0.8% | 0.8% | +0.3 | n/a | no target |
| P06T | 43524 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 251 | 23.1% | 23.1% | -2.5 | n/a | no target |
| P07 | 679 | 7.1% | 7.1% | -1.2 | n/a | no target |
| P08 | 22779 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 276 | 20.7% | 20.7% | +3.1 | n/a | no target |
| P10 | 2134 | 2.5% | 2.5% | +0.1 | n/a | no target |
| P11 | 1612 | 3.1% | 3.1% | -1.6 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +4.9 | n/a | no target |
| P13 | 163017 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 10.1% | 10.1% | -1.5 | 15% | 🟡 5 pts to go |
| P01T | 197 | 12.2% | 12.2% | -0.3 | 15% | 🟡 3 pts to go |
| P01_GOLD | 625 | 34.7% | 34.7% | -0.6 | 40% | 🟡 5 pts to go |
| P02 | 468 | 12.2% | 12.4% | -0.7 | 25% | ❌ 13 pts to go |
| P03 | 264 | 16.3% | 16.3% | -1.2 | 25% | 🟡 9 pts to go |
| P04 | 3568 | 2.7% | 2.7% | +0.0 | 15% | ❌ 12 pts to go |
| P05 | 424 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 20094 | 0.7% | 0.7% | -0.2 | 15% | ❌ 14 pts to go |
| P06T | 43524 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 251 | 10.0% | 10.0% | -0.6 | 15% | 🟡 5 pts to go |
| P07 | 679 | 3.8% | 3.8% | -0.5 | 15% | ❌ 11 pts to go |
| P08 | 22779 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 276 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P10 | 2134 | 1.3% | 1.3% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1612 | 1.3% | 1.3% | -0.2 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 163017 | 0.5% | 0.5% | -0.2 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 6.9% | 6.9% | +1.5 | 15% | 🟡 8 pts to go |
| P01T | 197 | 12.7% | 12.7% | +1.2 | 25% | ❌ 12 pts to go |
| P01_GOLD | 625 | 29.3% | 29.3% | +0.1 | 25% | ✅ met |
| P02 | 468 | 25.4% | 25.4% | +0.1 | 15% | ✅ met |
| P03 | 264 | 21.6% | 21.6% | -0.5 | 15% | ✅ met |
| P04 | 3568 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 424 | 11.3% | 11.3% | +0.2 | 15% | 🟡 4 pts to go |
| P06M | 20094 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P06T | 43524 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 251 | 8.4% | 8.4% | +0.0 | 15% | 🟡 7 pts to go |
| P07 | 679 | 2.2% | 2.2% | -0.7 | 15% | ❌ 13 pts to go |
| P08 | 22779 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P09 | 276 | 1.4% | 1.4% | +0.4 | 15% | ❌ 14 pts to go |
| P10 | 2134 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1612 | 2.0% | 2.0% | -0.7 | 15% | ❌ 13 pts to go |
| P12 | 11 | 0.0% | 0.0% | -20.0 | 15% | ❌ 15 pts to go |
| P13 | 163017 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 1.4% | 1.4% | -0.9 | 20% | ❌ 19 pts to go |
| P01T | 197 | 3.6% | 3.6% | -0.6 | 20% | ❌ 16 pts to go |
| P01_GOLD | 625 | 4.3% | 4.3% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 468 | 1.7% | 1.7% | +0.2 | 20% | ❌ 18 pts to go |
| P03 | 264 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3568 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |
| P05 | 424 | 0.9% | 0.9% | -0.3 | 20% | ❌ 19 pts to go |
| P06M | 20094 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 251 | 1.2% | 1.2% | -0.3 | 20% | ❌ 19 pts to go |
| P07 | 679 | 0.3% | 0.3% | -0.1 | 20% | ❌ 20 pts to go |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 276 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2134 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1612 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 1.8% | 1.8% | +0.2 | 15% | ❌ 13 pts to go |
| P01T | 197 | 3.6% | 3.6% | +0.5 | 15% | ❌ 11 pts to go |
| P01_GOLD | 625 | 10.7% | 10.7% | +0.3 | 15% | 🟡 4 pts to go |
| P02 | 468 | 10.9% | 10.9% | -1.1 | 15% | 🟡 4 pts to go |
| P03 | 264 | 20.8% | 20.8% | +0.6 | 15% | ✅ met |
| P04 | 3568 | 2.3% | 2.3% | +0.0 | 15% | ❌ 13 pts to go |
| P05 | 424 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 20094 | 0.5% | 0.5% | +0.2 | 15% | ❌ 14 pts to go |
| P06T | 43524 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 251 | 4.8% | 4.8% | -0.3 | 15% | ❌ 10 pts to go |
| P07 | 679 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P08 | 22779 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P09 | 276 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2134 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1612 | 0.9% | 0.9% | -0.3 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | -6.7 | 15% | ❌ 15 pts to go |
| P13 | 163017 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 13.8% | 13.8% | -0.2 | 20% | 🟡 6 pts to go |
| P01T | 197 | 14.2% | 14.2% | +0.1 | 40% | ❌ 26 pts to go |
| P01_GOLD | 625 | 46.6% | 46.6% | +0.4 | 40% | ✅ met |
| P02 | 468 | 43.2% | 43.2% | +0.3 | 20% | ✅ met |
| P03 | 264 | 47.7% | 47.7% | -1.3 | 35% | ✅ met |
| P04 | 3568 | 14.9% | 14.9% | +0.7 | 20% | 🟡 5 pts to go |
| P05 | 424 | 15.6% | 15.6% | +0.2 | 20% | 🟡 4 pts to go |
| P06M | 20094 | 1.0% | 1.0% | +0.2 | 20% | ❌ 19 pts to go |
| P06T | 43524 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 251 | 23.9% | 23.9% | -1.4 | 20% | ✅ met |
| P07 | 679 | 7.7% | 7.7% | -0.9 | 20% | ❌ 12 pts to go |
| P08 | 22779 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 276 | 20.7% | 20.7% | +2.5 | 20% | ✅ met |
| P10 | 2134 | 3.8% | 3.8% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 1612 | 3.5% | 3.5% | -1.3 | 20% | ❌ 16 pts to go |
| P12 | 11 | 9.1% | 9.1% | +2.4 | 20% | ❌ 11 pts to go |
| P13 | 163017 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 21.6% | 21.6% | -11.7 | n/a | no target |
| P01T | 197 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.0% | 72.0% | +2.5 | 95% | ❌ 23 pts to go |
| P02 | 468 | 65.8% | 65.8% | +2.9 | 95% | ❌ 29 pts to go |
| P03 | 264 | 57.6% | 57.6% | +4.4 | 90% | ❌ 32 pts to go |
| P04 | 3568 | 26.3% | 26.3% | +1.5 | 85% | ❌ 59 pts to go |
| P05 | 424 | 38.9% | 38.9% | +1.2 | 75% | ❌ 36 pts to go |
| P06M | 20094 | 31.0% | 31.0% | -5.1 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 89.1% | 89.1% | +0.8 | 100% | ❌ 11 pts to go |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 4.7% | 4.7% | -1.3 | 60% | ❌ 55 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 21.6% | 21.6% | -11.7 | n/a | no target |
| P01T | 197 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 73.9% | 73.9% | +1.1 | 100% | ❌ 26 pts to go |
| P02 | 468 | 67.7% | 67.7% | +1.4 | 100% | ❌ 32 pts to go |
| P03 | 264 | 60.2% | 60.2% | +1.3 | n/a | no target |
| P04 | 3568 | 26.8% | 26.8% | +1.3 | 95% | ❌ 68 pts to go |
| P05 | 424 | 34.7% | 34.7% | +1.3 | 80% | ❌ 45 pts to go |
| P06M | 20094 | 31.0% | 31.0% | -5.1 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 91.7% | 91.7% | +0.2 | 100% | 🟡 8 pts to go |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 4.8% | 4.8% | -1.6 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 85.3% | 85.3% | +5.5 | n/a | no target |
| P01T | 197 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 52.2% | 52.2% | +0.6 | 85% | ❌ 33 pts to go |
| P02 | 468 | 58.8% | 58.8% | +1.3 | 90% | ❌ 31 pts to go |
| P03 | 264 | 43.6% | 43.6% | +1.0 | 85% | ❌ 41 pts to go |
| P04 | 3568 | 28.8% | 28.8% | +0.9 | 90% | ❌ 61 pts to go |
| P05 | 424 | 33.0% | 33.0% | +0.3 | 75% | ❌ 42 pts to go |
| P06M | 20094 | 86.5% | 86.5% | -0.6 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 81.9% | 81.9% | -1.5 | 95% | ❌ 13 pts to go |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 4.1% | 4.1% | -1.3 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 74.3% | 74.3% | -4.0 | n/a | no target |
| P01T | 197 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 52.0% | 52.0% | +0.2 | 85% | ❌ 33 pts to go |
| P02 | 468 | 53.2% | 53.2% | +0.6 | 90% | ❌ 37 pts to go |
| P03 | 264 | 43.9% | 43.9% | +0.2 | 85% | ❌ 41 pts to go |
| P04 | 3568 | 24.4% | 24.4% | +0.6 | 90% | ❌ 66 pts to go |
| P05 | 424 | 42.5% | 42.5% | -0.9 | 75% | ❌ 32 pts to go |
| P06M | 20094 | 75.5% | 75.5% | -2.3 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.4% | 0.4% | +0.1 | 95% | ❌ 95 pts to go |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 3.2% | 3.2% | -1.3 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 94.5% | 94.5% | +4.6 | n/a | no target |
| P01T | 197 | 95.4% | 95.4% | +1.1 | n/a | no target |
| P01_GOLD | 625 | 85.8% | 85.9% | +0.5 | 100% | ❌ 14 pts to go |
| P02 | 468 | 77.1% | 77.1% | +0.7 | 100% | ❌ 23 pts to go |
| P03 | 264 | 92.0% | 92.0% | +0.7 | n/a | no target |
| P04 | 3568 | 50.5% | 50.5% | +1.7 | 95% | ❌ 44 pts to go |
| P05 | 424 | 77.4% | 77.4% | -0.1 | 95% | ❌ 18 pts to go |
| P06M | 20094 | 99.2% | 99.2% | +0.3 | n/a | no target |
| P06T | 43524 | 92.6% | 92.6% | +2.0 | n/a | no target |
| P06 | 251 | 22.3% | 22.3% | -0.8 | n/a | no target |
| P07 | 679 | 12.8% | 12.8% | -1.0 | n/a | no target |
| P08 | 22779 | 6.1% | 6.1% | -1.0 | n/a | no target |
| P09 | 276 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2134 | 70.7% | 70.7% | -0.3 | n/a | no target |
| P11 | 1612 | 70.6% | 70.6% | +2.5 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 99.6% | 99.6% | -0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 94.5% | 94.5% | +4.6 | n/a | no target |
| P01T | 197 | 95.4% | 95.4% | +1.1 | n/a | no target |
| P01_GOLD | 625 | 89.0% | 89.1% | +0.5 | 100% | ❌ 11 pts to go |
| P02 | 468 | 78.4% | 78.4% | +0.9 | 100% | ❌ 22 pts to go |
| P03 | 264 | 92.8% | 92.8% | +0.8 | n/a | no target |
| P04 | 3568 | 53.8% | 53.8% | +1.9 | 95% | ❌ 41 pts to go |
| P05 | 424 | 89.4% | 89.4% | -0.2 | 70% | ✅ met |
| P06M | 20094 | 99.2% | 99.2% | +0.3 | n/a | no target |
| P06T | 43524 | 92.6% | 92.6% | +2.0 | n/a | no target |
| P06 | 251 | 22.3% | 22.3% | -0.8 | n/a | no target |
| P07 | 679 | 12.8% | 12.8% | -1.0 | n/a | no target |
| P08 | 22779 | 6.1% | 6.1% | -1.0 | n/a | no target |
| P09 | 276 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2134 | 70.7% | 70.7% | -0.3 | n/a | no target |
| P11 | 1612 | 70.7% | 70.7% | +2.5 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 197 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 17.1% | 17.1% | +0.3 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 368 rows, 29.1% filled |
| P02 | 468 | 10.0% | 10.0% | -1.2 | n/a | no target · rows from a source that publishes bids: 294 rows, 16.0% filled |
| P03 | 264 | 13.6% | 13.6% | +0.7 | n/a | no target · rows from a source that publishes bids: 141 rows, 25.5% filled |
| P04 | 3568 | 1.7% | 1.7% | +0.2 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.9% filled |
| P05 | 424 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 56 rows, 19.6% filled |
| P06M | 20094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 4.3% | 4.3% | +0.1 | n/a | no target · rows from a source that publishes bids: 263 rows, 4.6% filled |
| P10 | 2134 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1612 | 0.6% | 0.6% | -0.3 | n/a | no target · rows from a source that publishes bids: 74 rows, 13.5% filled |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 11 rows, 0.0% filled |
| P13 | 163017 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 197 | 0.0% | 98.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 53.4% | 81.9% | +0.2 | 90% | ❌ 37 pts to go |
| P02 | 468 | 53.2% | 87.2% | +0.8 | 90% | ❌ 37 pts to go |
| P03 | 264 | 45.5% | 79.9% | +1.0 | 90% | ❌ 44 pts to go |
| P04 | 3568 | 19.5% | 92.9% | +0.4 | 90% | ❌ 70 pts to go |
| P05 | 424 | 0.0% | 82.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 20094 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43524 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 2.9% | 4.7% | +0.6 | 90% | ❌ 87 pts to go |
| P10 | 2134 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1612 | 2.7% | 97.3% | -1.4 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 197 | 0.5% | 98.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 26.2% | 54.7% | +0.3 | 90% | ❌ 64 pts to go |
| P02 | 468 | 51.9% | 85.9% | +0.4 | n/a | no target |
| P03 | 264 | 25.0% | 59.5% | +0.7 | n/a | no target |
| P04 | 3568 | 21.2% | 94.7% | +0.2 | n/a | no target |
| P05 | 424 | 0.5% | 82.8% | +0.0 | n/a | no target |
| P06M | 20094 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43524 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 40.2% | 42.0% | -0.8 | n/a | no target |
| P10 | 2134 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1612 | 2.7% | 97.3% | -1.0 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 197 | 2.0% | 100.0% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 52.3% | 80.8% | +0.5 | 95% | ❌ 43 pts to go |
| P02 | 468 | 57.9% | 91.9% | +1.5 | n/a | no target |
| P03 | 264 | 49.6% | 84.1% | +2.8 | n/a | no target |
| P04 | 3568 | 22.0% | 95.4% | +0.8 | n/a | no target |
| P05 | 424 | 5.0% | 87.3% | +0.5 | n/a | no target |
| P06M | 20094 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43524 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 679 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22779 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 60.5% | 62.3% | -2.0 | n/a | no target |
| P10 | 2134 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1612 | 2.9% | 97.4% | -1.2 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163017 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 197 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 468 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3568 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 20094 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 43524 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 251 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 679 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 22779 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2134 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1612 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163017 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 197 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 468 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3568 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 20094 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 43524 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 251 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 679 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 22779 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2134 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1612 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163017 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 218 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 197 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 468 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3568 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 20094 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 43524 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 251 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 679 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 22779 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2134 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1612 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163017 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

