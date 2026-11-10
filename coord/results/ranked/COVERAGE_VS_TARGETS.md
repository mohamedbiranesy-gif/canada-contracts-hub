# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **95 of 446 met** (21.3%); 54 within 10 points; 297 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 53, P01T 203, P01_GOLD 625, P02 429, P03 218, P04 2588, P05 418, P06M 4395, P06T 19508, P06 329, P07 710, P08 19644, P09 312, P10R 26614, P10 2472, P11 3321, P12 8, P13 10515

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 20.8% | 8 | PO rule (45 rows) |
| P01T | 203 | 0.5% | 22.2% | 6 | reference to quote (PO / contract / vendor id) (195 rows) |
| P01_GOLD | 625 | 24.5% | 68.6% | 9 | payment terms (214 rows) |
| P02 | 429 | 8.2% | 57.1% | 9 | PO rule (324 rows) |
| P03 | 218 | 17.0% | 65.1% | 9 | PO rule (101 rows) |
| P04 | 2588 | 1.8% | 22.6% | 6 | PO rule (2433 rows) |
| P05 | 418 | 1.0% | 17.0% | 7 | payment terms (347 rows) |
| P06M | 4395 | 0.0% | 1.3% | 8 | PO rule (4386 rows) |
| P06T | 19508 | 0.0% | 0.7% | 5 | reference to quote (PO / contract / vendor id) (19443 rows) |
| P06 | 329 | 0.0% | 5.8% | 5 | reference to quote (PO / contract / vendor id) (329 rows) |
| P07 | 710 | 0.0% | 2.0% | 5 | reference to quote (PO / contract / vendor id) (710 rows) |
| P08 | 19644 | 0.0% | 0.1% | 4 | reference to quote (PO / contract / vendor id) (19644 rows) |
| P09 | 312 | 1.3% | 43.6% | 8 | payment terms (291 rows) |
| P10R | 26614 | 0.0% | 29.2% | 8 | PO rule (26586 rows) |
| P10 | 2472 | 0.0% | 0.4% | 4 | reference to quote (PO / contract / vendor id) (2471 rows) |
| P11 | 3321 | 0.2% | 1.9% | 6 | PO rule (3288 rows) |
| P12 | 8 | 0.0% | 50.0% | 9 | PO rule (8 rows) |
| P13 | 10515 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (10515 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 53 | 6 | 1 | 46 | 0 | 0 | 73 |
| P01T | 203 | 28 | 44 | 131 | 0 | 0 | 73 |
| P01_GOLD | 625 | 231 | 185 | 209 | 0 | 0 | 82 |
| P02 | 429 | 0 | 183 | 246 | 0 | 0 | 66 |
| P03 | 218 | 0 | 0 | 209 | 9 | 0 | 57 |
| P04 | 2588 | 0 | 0 | 2065 | 523 | 0 | 48 |
| P05 | 418 | 14 | 29 | 351 | 24 | 0 | 51 |
| P06M | 4395 | 0 | 2 | 4379 | 14 | 0 | 51 |
| P06T | 19508 | 0 | 28 | 16278 | 3202 | 0 | 43 |
| P06 | 329 | 21 | 34 | 274 | 0 | 0 | 67 |
| P07 | 710 | 0 | 17 | 653 | 40 | 0 | 48 |
| P08 | 19644 | 0 | 0 | 15063 | 4581 | 0 | 38 |
| P09 | 312 | 4 | 12 | 293 | 3 | 0 | 53 |
| P10R | 26614 | 1 | 7 | 21489 | 5117 | 0 | 43 |
| P10 | 2472 | 2 | 7 | 1650 | 813 | 0 | 38 |
| P11 | 3321 | 0 | 1 | 9 | 0 | 3311 | 23 |
| P12 | 8 | 0 | 1 | 7 | 0 | 0 | 54 |
| P13 | 10515 | 2 | 12 | 9446 | 1055 | 0 | 51 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 53 | 38 | 71.7% | the buyer's PO / reference rule (9) |
| P01T | 203 | 59 | 29.1% | the buyer's PO / reference rule (68) |
| P01_GOLD | 625 | 463 | 74.1% | bill-to legal name and address (109) |
| P02 | 429 | 305 | 71.1% | bill-to legal name and address (65) |
| P03 | 218 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (218) |
| P04 | 2588 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (2588) |
| P05 | 418 | 46 | 11.0% | a confirmed invoicing / AP or finance channel (331) |
| P06M | 4395 | 31 | 0.7% | a confirmed invoicing / AP or finance channel (4335) |
| P06T | 19508 | 24 | 0.1% | a confirmed invoicing / AP or finance channel (19103) |
| P06 | 329 | 34 | 10.3% | bill-to legal name and address (201) |
| P07 | 710 | 8 | 1.1% | bill-to legal name and address (385) |
| P08 | 19644 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (19644) |
| P09 | 312 | 41 | 13.1% | a confirmed invoicing / AP or finance channel (262) |
| P10R | 26614 | 284 | 1.1% | a confirmed invoicing / AP or finance channel (26011) |
| P10 | 2472 | 3 | 0.1% | a confirmed invoicing / AP or finance channel (2377) |
| P11 | 3321 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3311) |
| P12 | 8 | 3 | 37.5% | a confirmed invoicing / AP or finance channel (5) |
| P13 | 10515 | 6 | 0.1% | a confirmed invoicing / AP or finance channel (10233) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 53 | 6 | 11.3% | 8 | 0 | the vendor's GST/HST number (BN9) (37) |
| P01T | 203 | 42 | 20.7% | 20 | 0 | the vendor's GST/HST number (BN9) (90) |
| P01_GOLD | 625 | 391 | 62.6% | 13 | 0 | the vendor's GST/HST number (BN9) (150) |
| P02 | 429 | 210 | 49.0% | 19 | 0 | the vendor's GST/HST number (BN9) (167) |
| P03 | 218 | 17 | 7.8% | 0 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (64) |
| P04 | 2588 | 42 | 1.6% | 5 | 638 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1859) |
| P05 | 418 | 22 | 5.3% | 9 | 101 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (222) |
| P06M | 4395 | 1 | 0.0% | 14 | 80 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4244) |
| P06T | 19508 | 17 | 0.1% | 61 | 1949 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (17072) |
| P06 | 329 | 14 | 4.3% | 19 | 0 | the vendor's GST/HST number (BN9) (182) |
| P07 | 710 | 7 | 1.0% | 31 | 17 | the vendor's GST/HST number (BN9) (344) |
| P08 | 19644 | 1 | 0.0% | 3 | 980 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (18632) |
| P09 | 312 | 39 | 12.5% | 1 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (128) |
| P10R | 26614 | 466 | 1.8% | 0 | 17394 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (8560) |
| P10 | 2472 | 2 | 0.1% | 16 | 327 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2030) |
| P11 | 3321 | 5 | 0.2% | 0 | 0 | a confirmed invoicing / AP or finance channel (3295) |
| P12 | 8 | 2 | 25.0% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2) |
| P13 | 10515 | 6 | 0.1% | 210 | 7099 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3096) |
| **all** | 92362 | 1290 | 1.4% | 429 | 28838 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 47 | 0 | 0 | 0 | 5 | 5 | 0 | 45 | 46 | 1 |
| P01T | 175 | 0 | 0 | 0 | 33 | 63 | 10 | 130 | 142 | 30 |
| P01_GOLD | 394 | 0 | 0 | 0 | 11 | 94 | 34 | 193 | 228 | 59 |
| P02 | 429 | 0 | 429 | 0 | 23 | 60 | 20 | 324 | 253 | 22 |
| P03 | 218 | 0 | 218 | 0 | 6 | 39 | 14 | 101 | 103 | 25 |
| P04 | 2588 | 0 | 2588 | 0 | 912 | 1239 | 572 | 2433 | 2225 | 113 |
| P05 | 404 | 0 | 351 | 0 | 58 | 133 | 52 | 339 | 349 | 58 |
| P06M | 4395 | 0 | 4395 | 0 | 242 | 371 | 43 | 4386 | 4374 | 3 |
| P06T | 19508 | 0 | 19508 | 0 | 8371 | 13316 | 3720 | 19382 | 19162 | 172 |
| P06 | 308 | 0 | 0 | 0 | 98 | 187 | 69 | 239 | 277 | 8 |
| P07 | 710 | 0 | 710 | 0 | 331 | 476 | 134 | 654 | 666 | 18 |
| P08 | 19644 | 0 | 19644 | 0 | 12970 | 16036 | 4945 | 19567 | 19464 | 215 |
| P09 | 308 | 0 | 288 | 0 | 9 | 69 | 4 | 282 | 294 | 46 |
| P10R | 26613 | 0 | 26518 | 0 | 898 | 16002 | 6678 | 26586 | 26538 | 24 |
| P10 | 2470 | 0 | 2431 | 0 | 985 | 1867 | 955 | 2435 | 2405 | 112 |
| P11 | 3321 | 3311 | 3258 | 0 | 1972 | 3169 | 863 | 3288 | 3259 | 31 |
| P12 | 8 | 0 | 7 | 0 | 0 | 2 | 0 | 8 | 7 | 0 |
| P13 | 10513 | 0 | 10421 | 0 | 313 | 3168 | 1517 | 10481 | 10488 | 25 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P08 | 29.2% | 95% | 12928 |
| buyer_logo_url | P08 | 34.3% | 100% | 12902 |
| vendor_registered_address | P08 | 10.2% | 70% | 11739 |
| buyer_legal_name_as_published | P08 | 18.4% | 75% | 11125 |
| vendor_logo_url | P08 | 47.8% | 100% | 10263 |
| vendor_phone | P08 | 34.7% | 85% | 9882 |
| vendor_bn9 | P08 | 8.7% | 50% | 8106 |
| vendor_emails | P08 | 35.2% | 75% | 7809 |
| vendor_trading_name | P08 | 18.7% | 50% | 6146 |
| buyer_bn_as_published | P08 | 7.7% | 35% | 5371 |
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 5318 |
| ap_system_hint | P10R | 0.4% | 20% | 5213 |
| invoice_reference_hint | P08 | 0.4% | 25% | 4834 |
| buyer_esignature_preference | P10R | 0.1% | 15% | 3977 |
| buyer_tax_exempt_status | P10R | 0.1% | 15% | 3976 |
| buyer_address | P08 | 74.8% | 95% | 3968 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 3924 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 3895 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 3838 |
| ap_system_hint | P08 | 0.5% | 20% | 3837 |
| ap_system_hint | P06T | 1.0% | 20% | 3706 |
| buyer_esignature_preference | P08 | 0.1% | 15% | 2921 |
| buyer_payment_method_preference | P08 | 0.2% | 15% | 2917 |
| buyer_tax_exempt_status | P08 | 0.2% | 15% | 2913 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 2888 |
| buyer_tax_exempt_status | P06T | 0.4% | 15% | 2853 |
| buyer_payment_method_preference | P06T | 0.4% | 15% | 2841 |
| buyer_logo_url | P11 | 10.5% | 80% | 2308 |
| buyer_phone | P11 | 7.9% | 75% | 2229 |
| vendor_phone | P11 | 11.6% | 75% | 2105 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 2101 |
| buyer_phone | P13 | 75.0% | 95% | 2099 |
| buyer_logo_url | P13 | 75.5% | 95% | 2052 |
| buyer_legal_name_as_published | P11 | 4.6% | 65% | 2007 |
| ap_system_hint | P13 | 0.9% | 20% | 2006 |
| vendor_emails | P11 | 10.0% | 70% | 1993 |
| contract_value | P11 | 2.6% | 60% | 1906 |
| award_or_notice_id | P11 | 2.7% | 60% | 1904 |
| average_contract_duration_days | P04 | 27.6% | 90% | 1617 |
| commodity_codes | P11 | 1.8% | 50% | 1600 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 79.2% | 79.2% | +34.8 | 50% | ✅ met |
| P01T | 203 | 37.9% | 37.9% | -33.8 | 50% | ❌ 12 pts to go |
| P01_GOLD | 625 | 92.3% | 94.6% | -0.2 | 95% | 🟡 3 pts to go |
| P02 | 429 | 79.0% | 80.7% | -4.9 | 95% | ❌ 16 pts to go |
| P03 | 218 | 89.0% | 93.1% | -3.8 | 95% | 🟡 6 pts to go |
| P04 | 2588 | 41.8% | 43.7% | -26.8 | 90% | ❌ 48 pts to go |
| P05 | 418 | 38.3% | 40.9% | -2.8 | 70% | ❌ 32 pts to go |
| P06M | 4395 | 94.3% | 94.3% | +87.2 | n/a | no target |
| P06T | 19508 | 1.0% | 1.0% | -3.4 | n/a | no target |
| P06 | 329 | 27.4% | 27.4% | -20.8 | 30% | 🟡 3 pts to go |
| P07 | 710 | 7.9% | 7.9% | -15.9 | 30% | ❌ 22 pts to go |
| P08 | 19644 | 0.4% | 0.4% | -2.0 | 25% | ❌ 25 pts to go |
| P09 | 312 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 26614 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 1.5% | 1.9% | -0.7 | 25% | ❌ 24 pts to go |
| P11 | 3321 | 21.3% | 21.7% | -2.8 | 60% | ❌ 39 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10515 | 0.3% | 0.4% | +0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 429 | 6.8% | 6.8% | -0.4 | 50% | ❌ 43 pts to go |
| P03 | 218 | 1.8% | 1.8% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 2588 | 0.7% | 0.7% | -0.4 | 30% | ❌ 29 pts to go |
| P05 | 418 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P06M | 4395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19508 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 0.6% | 0.6% | +0.1 | 50% | ❌ 49 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P11 | 3321 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 66.0% | 66.0% | +66.0 | n/a | no target |
| P01T | 203 | 3.9% | 3.9% | -1.5 | 50% | ❌ 46 pts to go |
| P01_GOLD | 625 | 67.7% | 67.7% | +0.1 | 85% | ❌ 17 pts to go |
| P02 | 429 | 71.1% | 71.1% | -4.4 | 90% | ❌ 19 pts to go |
| P03 | 218 | 72.5% | 72.5% | -3.0 | 85% | ❌ 12 pts to go |
| P04 | 2588 | 40.0% | 40.0% | -25.5 | 85% | ❌ 45 pts to go |
| P05 | 418 | 29.2% | 29.2% | -1.8 | 60% | ❌ 31 pts to go |
| P06M | 4395 | 94.2% | 94.2% | +94.2 | n/a | no target |
| P06T | 19508 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 96.2% | 96.2% | -0.4 | 100% | 🟡 4 pts to go |
| P10R | 26614 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 20.7% | 20.7% | +0.7 | 60% | ❌ 39 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 2.0% | 2.0% | -0.2 | 30% | ❌ 28 pts to go |
| P01_GOLD | 625 | 51.2% | 51.2% | -0.1 | 80% | ❌ 29 pts to go |
| P02 | 429 | 62.7% | 62.7% | -4.1 | 60% | ✅ met |
| P03 | 218 | 61.0% | 61.0% | -2.9 | 80% | ❌ 19 pts to go |
| P04 | 2588 | 33.1% | 33.1% | -21.4 | 50% | ❌ 17 pts to go |
| P05 | 418 | 12.4% | 12.4% | -0.9 | 40% | ❌ 28 pts to go |
| P06M | 4395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19508 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 84.0% | 84.0% | -2.1 | 50% | ✅ met |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 2.5% | 2.5% | -15.0 | 40% | ❌ 38 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 3.0% | 3.0% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 61.1% | 61.1% | +0.0 | 85% | ❌ 24 pts to go |
| P02 | 429 | 61.8% | 61.8% | -4.0 | 90% | ❌ 28 pts to go |
| P03 | 218 | 71.1% | 71.1% | -3.4 | 85% | ❌ 14 pts to go |
| P04 | 2588 | 34.2% | 34.2% | -22.1 | 85% | ❌ 51 pts to go |
| P05 | 418 | 20.1% | 20.1% | -1.0 | 50% | ❌ 30 pts to go |
| P06M | 4395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19508 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 2.7% | 2.7% | -16.3 | 60% | ❌ 57 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 1.0% | 1.0% | -1.2 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 429 | 6.8% | 6.8% | -0.4 | 50% | ❌ 43 pts to go |
| P03 | 218 | 10.1% | 10.1% | -0.5 | 50% | ❌ 40 pts to go |
| P04 | 2588 | 2.6% | 2.6% | -1.7 | 40% | ❌ 37 pts to go |
| P05 | 418 | 1.2% | 1.2% | -0.1 | 20% | ❌ 19 pts to go |
| P06M | 4395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19508 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 2.6% | 2.6% | +0.0 | 50% | ❌ 47 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 0.4% | 0.4% | -2.6 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 1.5% | 1.5% | +1.5 | n/a | no target |
| P01_GOLD | 625 | 35.0% | 35.0% | -0.1 | 80% | ❌ 45 pts to go |
| P02 | 429 | 57.1% | 57.1% | -3.5 | 90% | ❌ 33 pts to go |
| P03 | 218 | 39.4% | 39.4% | -1.9 | 80% | ❌ 41 pts to go |
| P04 | 2588 | 31.1% | 31.1% | -20.2 | 85% | ❌ 54 pts to go |
| P05 | 418 | 5.5% | 5.5% | -0.5 | 50% | ❌ 44 pts to go |
| P06M | 4395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19508 | 0.2% | 0.2% | +0.2 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 75.6% | 75.6% | -0.3 | 95% | ❌ 19 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 1.8% | 1.8% | -11.3 | 50% | ❌ 48 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | -0.6 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 429 | 6.8% | 6.8% | -0.4 | 50% | ❌ 43 pts to go |
| P03 | 218 | 2.3% | 2.3% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 2588 | 0.7% | 0.7% | -0.4 | 30% | ❌ 29 pts to go |
| P05 | 418 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 4395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19508 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 218 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 2588 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 418 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 4395 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 19508 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 329 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 710 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19644 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 26614 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3321 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 30.2% | 30.2% | -69.8 | 70% | ❌ 40 pts to go |
| P01T | 203 | 39.9% | 39.9% | -40.5 | 60% | ❌ 20 pts to go |
| P01_GOLD | 625 | 73.1% | 73.1% | -4.8 | 90% | ❌ 17 pts to go |
| P02 | 429 | 57.3% | 57.3% | -10.0 | 85% | ❌ 28 pts to go |
| P03 | 218 | 76.1% | 76.1% | -6.1 | 90% | ❌ 14 pts to go |
| P04 | 2588 | 30.9% | 30.9% | -24.5 | 75% | ❌ 44 pts to go |
| P05 | 418 | 51.2% | 51.2% | -1.4 | 50% | ✅ met |
| P06M | 4395 | 2.7% | 2.7% | -71.7 | n/a | no target |
| P06T | 19508 | 12.8% | 12.8% | -47.9 | n/a | no target |
| P06 | 329 | 20.4% | 20.4% | -23.6 | 40% | ❌ 20 pts to go |
| P07 | 710 | 14.6% | 14.6% | -23.5 | 50% | ❌ 35 pts to go |
| P08 | 19644 | 8.7% | 8.7% | -31.5 | 50% | ❌ 41 pts to go |
| P09 | 312 | 57.7% | 57.7% | +3.4 | 80% | ❌ 22 pts to go |
| P10R | 26614 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 29.2% | 29.2% | -7.4 | 40% | ❌ 11 pts to go |
| P11 | 3321 | 77.6% | 77.6% | +32.9 | 60% | ✅ met |
| P12 | 8 | 62.5% | 62.5% | +9.9 | 85% | ❌ 22 pts to go |
| P13 | 10515 | 88.9% | 88.9% | -2.8 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 69.8% | 69.8% | +8.7 | n/a | no target |
| P01T | 203 | 38.4% | 38.4% | -24.6 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | -4.2 | 95% | ❌ 24 pts to go |
| P02 | 429 | 74.8% | 74.8% | -10.1 | 95% | ❌ 20 pts to go |
| P03 | 218 | 72.5% | 72.5% | -5.4 | 95% | ❌ 22 pts to go |
| P04 | 2588 | 46.9% | 46.9% | -33.8 | 95% | ❌ 48 pts to go |
| P05 | 418 | 55.0% | 55.0% | -1.2 | 70% | ❌ 15 pts to go |
| P06M | 4395 | 56.7% | 56.7% | +35.9 | n/a | no target |
| P06T | 19508 | 28.3% | 28.3% | -49.9 | n/a | no target |
| P06 | 329 | 24.9% | 24.9% | -30.5 | 80% | ❌ 55 pts to go |
| P07 | 710 | 19.6% | 19.6% | -32.4 | 70% | ❌ 50 pts to go |
| P08 | 19644 | 10.2% | 10.2% | -42.2 | 70% | ❌ 60 pts to go |
| P09 | 312 | 87.8% | 87.8% | -0.7 | 100% | ❌ 12 pts to go |
| P10R | 26614 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 32.3% | 32.3% | -10.1 | 70% | ❌ 38 pts to go |
| P11 | 3321 | 80.0% | 80.0% | +24.7 | 75% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 20.8% | 20.8% | -29.2 | n/a | no target |
| P01T | 203 | 24.1% | 24.1% | +4.5 | n/a | no target |
| P01_GOLD | 625 | 50.9% | 50.9% | -1.5 | 60% | 🟡 9 pts to go |
| P02 | 429 | 62.5% | 62.5% | -4.8 | 60% | ✅ met |
| P03 | 218 | 60.1% | 60.1% | -4.8 | 60% | ✅ met |
| P04 | 2588 | 35.7% | 35.7% | -19.8 | 55% | ❌ 19 pts to go |
| P05 | 418 | 25.4% | 25.4% | +0.1 | 50% | ❌ 25 pts to go |
| P06M | 4395 | 1.3% | 1.3% | -16.0 | n/a | no target |
| P06T | 19508 | 28.7% | 28.7% | -24.9 | n/a | no target |
| P06 | 329 | 31.0% | 31.0% | -22.0 | n/a | no target |
| P07 | 710 | 26.8% | 26.8% | -19.2 | 55% | ❌ 28 pts to go |
| P08 | 19644 | 18.7% | 18.7% | -28.8 | 50% | ❌ 31 pts to go |
| P09 | 312 | 71.5% | 71.5% | +0.1 | 70% | ✅ met |
| P10R | 26614 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 41.4% | 41.4% | -10.5 | 55% | ❌ 14 pts to go |
| P11 | 3321 | 79.6% | 79.6% | +36.6 | 50% | ✅ met |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 24.5% | 24.5% | -36.6 | n/a | no target |
| P01T | 203 | 41.4% | 41.4% | +11.0 | n/a | no target |
| P01_GOLD | 625 | 52.5% | 52.5% | +0.7 | 70% | ❌ 18 pts to go |
| P02 | 429 | 56.2% | 56.2% | -1.0 | 70% | ❌ 14 pts to go |
| P03 | 218 | 55.5% | 55.5% | -1.7 | 70% | ❌ 14 pts to go |
| P04 | 2588 | 39.5% | 39.5% | -12.5 | 65% | ❌ 26 pts to go |
| P05 | 418 | 34.4% | 34.4% | -0.2 | 60% | ❌ 26 pts to go |
| P06M | 4395 | 2.0% | 2.0% | -28.4 | n/a | no target |
| P06T | 19508 | 25.1% | 25.1% | +21.6 | n/a | no target |
| P06 | 329 | 45.0% | 45.0% | -14.6 | 40% | ✅ met |
| P07 | 710 | 43.9% | 43.9% | -24.0 | 85% | ❌ 41 pts to go |
| P08 | 19644 | 34.7% | 34.7% | -33.4 | 85% | ❌ 50 pts to go |
| P09 | 312 | 52.6% | 52.6% | -2.8 | 85% | ❌ 32 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 54.8% | 54.8% | -11.5 | 85% | ❌ 30 pts to go |
| P11 | 3321 | 11.6% | 11.6% | -43.3 | 75% | ❌ 63 pts to go |
| P12 | 8 | 25.0% | 25.0% | +9.2 | n/a | no target |
| P13 | 10515 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 32.1% | 32.1% | -62.3 | n/a | no target |
| P01T | 203 | 95.6% | 95.6% | +5.4 | n/a | no target |
| P01_GOLD | 625 | 89.4% | 89.4% | +0.0 | 90% | 🟡 1 pts to go |
| P02 | 429 | 88.6% | 88.6% | +1.0 | 90% | 🟡 1 pts to go |
| P03 | 218 | 89.4% | 89.4% | -0.5 | 90% | 🟡 1 pts to go |
| P04 | 2588 | 87.4% | 87.4% | +6.1 | 85% | ✅ met |
| P05 | 418 | 51.9% | 51.9% | +0.9 | 70% | ❌ 18 pts to go |
| P06M | 4395 | 4.5% | 4.5% | -63.4 | n/a | no target |
| P06T | 19508 | 95.9% | 95.9% | +18.0 | n/a | no target |
| P06 | 329 | 98.5% | 98.5% | +1.5 | 50% | ✅ met |
| P07 | 710 | 98.9% | 98.9% | +2.1 | 100% | 🟡 1 pts to go |
| P08 | 19644 | 99.4% | 99.4% | +3.3 | 100% | 🟡 1 pts to go |
| P09 | 312 | 79.8% | 79.8% | +0.0 | 100% | ❌ 20 pts to go |
| P10R | 26614 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3321 | 99.0% | 99.0% | +6.0 | 100% | 🟡 1 pts to go |
| P12 | 8 | 37.5% | 37.5% | -4.6 | n/a | no target |
| P13 | 10515 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 20.8% | 20.8% | -29.2 | n/a | no target |
| P01T | 203 | 44.3% | 44.3% | -1.4 | n/a | no target |
| P01_GOLD | 625 | 46.2% | 46.2% | +0.5 | 70% | ❌ 24 pts to go |
| P02 | 429 | 50.8% | 50.8% | -0.7 | 75% | ❌ 24 pts to go |
| P03 | 218 | 50.0% | 50.0% | -1.4 | 75% | ❌ 25 pts to go |
| P04 | 2588 | 33.3% | 33.3% | -9.6 | 70% | ❌ 37 pts to go |
| P05 | 418 | 25.1% | 25.1% | +0.6 | 55% | ❌ 30 pts to go |
| P06M | 4395 | 1.2% | 1.2% | -14.9 | n/a | no target |
| P06T | 19508 | 20.1% | 20.1% | +17.2 | n/a | no target |
| P06 | 329 | 35.3% | 35.3% | -5.7 | n/a | no target |
| P07 | 710 | 35.2% | 35.2% | -1.7 | 70% | ❌ 35 pts to go |
| P08 | 19644 | 35.2% | 35.2% | -13.5 | 75% | ❌ 40 pts to go |
| P09 | 312 | 50.0% | 50.0% | -2.0 | 85% | ❌ 35 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 40.1% | 40.1% | -11.2 | 80% | ❌ 40 pts to go |
| P11 | 3321 | 10.0% | 10.0% | -30.5 | 70% | ❌ 60 pts to go |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 30.2% | 30.2% | -64.2 | n/a | no target |
| P01T | 203 | 75.4% | 75.4% | -13.7 | n/a | no target |
| P01_GOLD | 625 | 79.8% | 79.8% | +0.0 | 90% | ❌ 10 pts to go |
| P02 | 429 | 74.8% | 74.8% | -2.4 | 90% | ❌ 15 pts to go |
| P03 | 218 | 78.9% | 78.9% | -2.8 | 90% | ❌ 11 pts to go |
| P04 | 2588 | 53.1% | 53.1% | -17.8 | 85% | ❌ 32 pts to go |
| P05 | 418 | 49.3% | 49.3% | +0.9 | 75% | ❌ 26 pts to go |
| P06M | 4395 | 3.5% | 3.5% | -64.4 | n/a | no target |
| P06T | 19508 | 43.2% | 43.2% | -33.9 | n/a | no target |
| P06 | 329 | 65.0% | 65.0% | -23.6 | n/a | no target |
| P07 | 710 | 60.3% | 60.3% | -30.2 | 100% | ❌ 40 pts to go |
| P08 | 19644 | 47.8% | 47.8% | -41.2 | 100% | ❌ 52 pts to go |
| P09 | 312 | 60.6% | 60.6% | -1.9 | n/a | no target |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 72.7% | 72.7% | -16.3 | 100% | ❌ 27 pts to go |
| P11 | 3321 | 69.1% | 69.1% | -5.4 | n/a | no target |
| P12 | 8 | 37.5% | 37.5% | +0.7 | n/a | no target |
| P13 | 10515 | 75.8% | 75.8% | -6.9 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 41.5% | 41.5% | +41.5 | n/a | no target · QC vendors: 22 rows, 100.0% filled |
| P01T | 203 | 18.2% | 18.2% | -3.5 | n/a | no target · QC vendors: 7 rows, 100.0% filled |
| P01_GOLD | 625 | 43.8% | 43.8% | -4.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 429 | 58.7% | 58.7% | -9.9 | 95% | ❌ 36 pts to go · QC vendors: 107 rows, 100.0% filled |
| P03 | 218 | 50.0% | 50.0% | -5.8 | 95% | ❌ 45 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 2588 | 33.7% | 33.7% | -26.5 | 95% | ❌ 61 pts to go · QC vendors: 449 rows, 98.7% filled |
| P05 | 418 | 15.3% | 15.3% | +0.5 | n/a | no target · QC vendors: 37 rows, 94.6% filled |
| P06M | 4395 | 54.8% | 54.8% | +54.8 | n/a | no target · QC vendors: 2409 rows, 100.0% filled |
| P06T | 19508 | 23.9% | 23.9% | -32.0 | n/a | no target · QC vendors: 2289 rows, 100.0% filled |
| P06 | 329 | 12.8% | 12.8% | -13.7 | n/a | no target · QC vendors: 18 rows, 100.0% filled |
| P07 | 710 | 8.5% | 8.5% | -12.9 | n/a | no target · QC vendors: 33 rows, 97.0% filled |
| P08 | 19644 | 5.8% | 5.8% | -23.1 | n/a | no target · QC vendors: 691 rows, 99.3% filled |
| P09 | 312 | 78.5% | 78.5% | -1.6 | 95% | ❌ 16 pts to go · QC vendors: 116 rows, 100.0% filled |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 17.8% | 17.8% | -5.6 | n/a | no target · QC vendors: 270 rows, 97.0% filled |
| P11 | 3321 | 58.6% | 58.6% | +29.3 | n/a | no target · QC vendors: 96 rows, 99.0% filled |
| P12 | 8 | 62.5% | 62.5% | -11.2 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 64.2% | 64.2% | +3.1 | n/a | no target · vendors with a registry record: 34 rows, 100.0% filled |
| P01T | 203 | 38.4% | 38.4% | -24.6 | n/a | no target · vendors with a registry record: 78 rows, 100.0% filled |
| P01_GOLD | 625 | 79.4% | 79.4% | -4.1 | 100% | ❌ 21 pts to go · vendors with a registry record: 496 rows, 100.0% filled |
| P02 | 429 | 79.0% | 79.0% | -10.1 | 100% | ❌ 21 pts to go · vendors with a registry record: 339 rows, 100.0% filled |
| P03 | 218 | 83.0% | 83.0% | -5.9 | 100% | ❌ 17 pts to go · vendors with a registry record: 181 rows, 100.0% filled |
| P04 | 2588 | 47.3% | 47.3% | -34.1 | 100% | ❌ 53 pts to go · vendors with a registry record: 1224 rows, 100.0% filled |
| P05 | 418 | 59.8% | 59.8% | -1.9 | n/a | no target · vendors with a registry record: 250 rows, 100.0% filled |
| P06M | 4395 | 55.7% | 55.7% | +34.9 | n/a | no target · vendors with a registry record: 2446 rows, 100.0% filled |
| P06T | 19508 | 28.3% | 28.3% | -49.9 | n/a | no target · vendors with a registry record: 5527 rows, 100.0% filled |
| P06 | 329 | 25.8% | 25.8% | -32.0 | n/a | no target · vendors with a registry record: 85 rows, 100.0% filled |
| P07 | 710 | 19.9% | 19.9% | -34.5 | n/a | no target · vendors with a registry record: 141 rows, 100.0% filled |
| P08 | 19644 | 10.3% | 10.3% | -44.0 | n/a | no target · vendors with a registry record: 2029 rows, 100.0% filled |
| P09 | 312 | 91.3% | 91.3% | -0.3 | n/a | no target · vendors with a registry record: 285 rows, 100.0% filled |
| P10R | 26614 | 100.0% | 100.0% |  | n/a | no target · vendors with a registry record: 26614 rows, 100.0% filled |
| P10 | 2472 | 33.2% | 33.2% | -10.5 | n/a | no target · vendors with a registry record: 820 rows, 100.0% filled |
| P11 | 3321 | 80.4% | 80.4% | +22.2 | n/a | no target · vendors with a registry record: 2670 rows, 100.0% filled |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 8 rows, 100.0% filled |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 90.6% | 90.6% | -3.8 | 90% | ✅ met |
| P01T | 203 | 69.0% | 69.0% | -25.6 | 90% | ❌ 21 pts to go |
| P01_GOLD | 625 | 85.0% | 85.0% | +0.4 | 95% | 🟡 10 pts to go |
| P02 | 429 | 86.0% | 86.0% | -4.6 | 95% | 🟡 9 pts to go |
| P03 | 218 | 82.1% | 82.1% | -1.1 | 85% | 🟡 3 pts to go |
| P04 | 2588 | 52.1% | 52.1% | -26.7 | 90% | ❌ 38 pts to go |
| P05 | 418 | 68.2% | 68.2% | -7.6 | 75% | 🟡 7 pts to go |
| P06M | 4395 | 91.6% | 91.6% | +2.9 | n/a | no target |
| P06T | 19508 | 31.7% | 31.7% | -32.7 | n/a | no target |
| P06 | 329 | 43.2% | 43.2% | -13.4 | 80% | ❌ 37 pts to go |
| P07 | 710 | 33.0% | 33.0% | -20.6 | 80% | ❌ 47 pts to go |
| P08 | 19644 | 18.4% | 18.4% | -18.4 | 75% | ❌ 57 pts to go |
| P09 | 312 | 77.9% | 77.9% | -2.9 | 95% | ❌ 17 pts to go |
| P10R | 26614 | 39.9% | 39.9% |  | n/a | no target |
| P10 | 2472 | 24.5% | 24.5% | -7.5 | 70% | ❌ 46 pts to go |
| P11 | 3321 | 4.6% | 4.6% | -20.3 | 65% | ❌ 60 pts to go |
| P12 | 8 | 75.0% | 75.0% | +1.3 | 80% | 🟡 5 pts to go |
| P13 | 10515 | 69.9% | 69.9% | +17.4 | 60% | ✅ met |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 22.6% | 22.6% | -16.3 | 50% | ❌ 27 pts to go |
| P01T | 203 | 14.8% | 14.8% | -5.9 | n/a | no target |
| P01_GOLD | 625 | 20.5% | 20.5% | +0.1 | 40% | ❌ 20 pts to go |
| P02 | 429 | 20.7% | 20.7% | -1.1 | 40% | ❌ 19 pts to go |
| P03 | 218 | 25.7% | 25.7% | -1.2 | 40% | ❌ 14 pts to go |
| P04 | 2588 | 18.5% | 18.5% | -9.1 | 40% | ❌ 22 pts to go |
| P05 | 418 | 20.1% | 20.1% | -2.8 | 25% | 🟡 5 pts to go |
| P06M | 4395 | 13.0% | 13.0% | -12.6 | n/a | no target |
| P06T | 19508 | 14.5% | 14.5% | -16.4 | n/a | no target |
| P06 | 329 | 12.2% | 12.2% | +1.4 | 35% | ❌ 23 pts to go |
| P07 | 710 | 8.6% | 8.6% | -1.7 | 35% | ❌ 26 pts to go |
| P08 | 19644 | 7.7% | 7.7% | -3.4 | 35% | ❌ 27 pts to go |
| P09 | 312 | 16.3% | 16.3% | -0.8 | n/a | no target |
| P10R | 26614 | 18.0% | 18.0% |  | n/a | no target |
| P10 | 2472 | 5.3% | 5.3% | -4.3 | 30% | ❌ 25 pts to go |
| P11 | 3321 | 1.3% | 1.3% | -7.1 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 10515 | 41.1% | 41.1% | +15.2 | 30% | ✅ met |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 203 | 95.1% | 95.1% | +1.6 | 100% | 🟡 5 pts to go |
| P01_GOLD | 625 | 90.2% | 90.2% | +2.5 | 100% | 🟡 10 pts to go |
| P02 | 429 | 94.9% | 94.9% | -1.9 | 100% | 🟡 5 pts to go |
| P03 | 218 | 91.7% | 91.7% | -0.1 | 100% | 🟡 8 pts to go |
| P04 | 2588 | 77.2% | 77.2% | -13.8 | 100% | ❌ 23 pts to go |
| P05 | 418 | 86.6% | 86.6% | +1.7 | 100% | ❌ 13 pts to go |
| P06M | 4395 | 99.0% | 99.0% | +27.0 | n/a | no target |
| P06T | 19508 | 80.8% | 80.8% | +0.6 | n/a | no target |
| P06 | 329 | 76.9% | 76.9% | +8.2 | 95% | ❌ 18 pts to go |
| P07 | 710 | 80.8% | 80.8% | +10.2 | 95% | ❌ 14 pts to go |
| P08 | 19644 | 74.8% | 74.8% | +8.6 | 95% | ❌ 20 pts to go |
| P09 | 312 | 95.5% | 95.5% | +0.0 | 100% | 🟡 4 pts to go |
| P10R | 26614 | 74.9% | 74.9% |  | n/a | no target |
| P10 | 2472 | 61.2% | 61.2% | -4.0 | 95% | ❌ 34 pts to go |
| P11 | 3321 | 66.3% | 66.3% | +31.9 | 80% | ❌ 14 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10515 | 85.5% | 85.5% | +9.4 | 95% | 🟡 10 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 92.5% | 92.5% | +3.6 | n/a | no target |
| P01T | 203 | 69.0% | 69.0% | -11.4 | n/a | no target |
| P01_GOLD | 625 | 70.4% | 70.4% | +0.2 | 90% | ❌ 20 pts to go |
| P02 | 429 | 75.5% | 75.5% | -4.2 | 95% | ❌ 20 pts to go |
| P03 | 218 | 72.5% | 72.5% | -1.1 | 95% | ❌ 22 pts to go |
| P04 | 2588 | 56.4% | 56.4% | -28.5 | 95% | ❌ 39 pts to go |
| P05 | 418 | 70.8% | 70.8% | -4.2 | 90% | ❌ 19 pts to go |
| P06M | 4395 | 95.2% | 95.2% | +11.3 | n/a | no target |
| P06T | 19508 | 47.9% | 47.9% | -29.4 | n/a | no target |
| P06 | 329 | 46.5% | 46.5% | -18.0 | 95% | ❌ 48 pts to go |
| P07 | 710 | 39.6% | 39.6% | -26.7 | 90% | ❌ 50 pts to go |
| P08 | 19644 | 29.2% | 29.2% | -45.5 | 95% | ❌ 66 pts to go |
| P09 | 312 | 86.9% | 86.9% | -2.1 | 100% | ❌ 13 pts to go |
| P10R | 26614 | 74.8% | 74.8% |  | n/a | no target |
| P10 | 2472 | 46.5% | 46.5% | -25.0 | 95% | ❌ 48 pts to go |
| P11 | 3321 | 7.9% | 7.9% | -21.0 | 75% | ❌ 67 pts to go |
| P12 | 8 | 75.0% | 75.0% | -14.5 | n/a | no target |
| P13 | 10515 | 75.0% | 75.0% | -4.3 | 95% | ❌ 20 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 77.4% | 77.4% | -0.4 | n/a | no target |
| P01T | 203 | 77.8% | 77.8% | -13.5 | 95% | ❌ 17 pts to go |
| P01_GOLD | 625 | 82.2% | 82.2% | +0.0 | 90% | 🟡 8 pts to go |
| P02 | 429 | 84.1% | 84.1% | -4.3 | 95% | ❌ 11 pts to go |
| P03 | 218 | 83.0% | 83.0% | -1.6 | 95% | ❌ 12 pts to go |
| P04 | 2588 | 57.3% | 57.3% | -26.9 | 90% | ❌ 33 pts to go |
| P05 | 418 | 87.3% | 87.3% | -2.3 | 95% | 🟡 8 pts to go |
| P06M | 4395 | 69.1% | 69.1% | -16.0 | n/a | no target |
| P06T | 19508 | 53.8% | 53.8% | -40.3 | n/a | no target |
| P06 | 329 | 62.0% | 62.0% | -28.4 | 100% | ❌ 38 pts to go |
| P07 | 710 | 51.7% | 51.7% | -36.4 | 100% | ❌ 48 pts to go |
| P08 | 19644 | 34.3% | 34.3% | -56.4 | 100% | ❌ 66 pts to go |
| P09 | 312 | 69.9% | 69.9% | -4.1 | n/a | no target |
| P10R | 26614 | 82.7% | 82.7% |  | n/a | no target |
| P10 | 2472 | 66.3% | 66.3% | -23.8 | 100% | ❌ 34 pts to go |
| P11 | 3321 | 10.5% | 10.5% | -26.0 | 80% | ❌ 70 pts to go |
| P12 | 8 | 100.0% | 100.0% | +15.8 | n/a | no target |
| P13 | 10515 | 75.5% | 75.5% | -8.7 | 95% | ❌ 20 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 7.5% | 7.5% | -9.2 | n/a | no target |
| P01T | 203 | 12.8% | 12.8% | -11.1 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 429 | 26.3% | 26.3% | -1.4 | 40% | ❌ 14 pts to go |
| P03 | 218 | 10.1% | 10.1% | -0.5 | 20% | 🟡 10 pts to go |
| P04 | 2588 | 4.5% | 4.5% | -2.9 | 20% | ❌ 16 pts to go |
| P05 | 418 | 3.3% | 3.3% | -0.6 | 15% | ❌ 12 pts to go |
| P06M | 4395 | 0.5% | 0.5% | -4.3 | n/a | no target |
| P06T | 19508 | 0.8% | 0.8% | -2.4 | n/a | no target |
| P06 | 329 | 4.9% | 4.9% | -0.5 | n/a | no target |
| P07 | 710 | 6.8% | 6.8% | +0.5 | n/a | no target |
| P08 | 19644 | 0.2% | 0.2% | -0.8 | n/a | no target |
| P09 | 312 | 7.7% | 7.7% | -0.2 | n/a | no target |
| P10R | 26614 | 0.5% | 0.5% |  | n/a | no target |
| P10 | 2472 | 0.8% | 0.8% | -0.5 | n/a | no target |
| P11 | 3321 | 0.4% | 0.4% | -2.1 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 10515 | 0.8% | 0.8% | +0.2 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 39.6% | 39.6% | +0.7 | n/a | no target |
| P01T | 203 | 31.0% | 31.0% | -3.8 | 70% | ❌ 39 pts to go |
| P01_GOLD | 625 | 43.2% | 43.2% | -0.1 | 80% | ❌ 37 pts to go |
| P02 | 429 | 60.6% | 60.6% | -3.5 | 90% | ❌ 29 pts to go |
| P03 | 218 | 22.5% | 22.5% | -0.6 | 60% | ❌ 38 pts to go |
| P04 | 2588 | 30.7% | 30.7% | -19.8 | 85% | ❌ 54 pts to go |
| P05 | 418 | 12.2% | 12.2% | -0.8 | 50% | ❌ 38 pts to go |
| P06M | 4395 | 0.6% | 0.6% | -5.9 | n/a | no target |
| P06T | 19508 | 1.1% | 1.1% | -1.6 | n/a | no target |
| P06 | 329 | 17.0% | 17.0% | -1.1 | n/a | no target |
| P07 | 710 | 11.5% | 11.5% | -7.5 | n/a | no target |
| P08 | 19644 | 0.1% | 0.1% | -0.5 | n/a | no target |
| P09 | 312 | 78.2% | 78.2% | -2.4 | 95% | ❌ 17 pts to go |
| P10R | 26614 | 0.8% | 0.8% |  | n/a | no target |
| P10 | 2472 | 1.7% | 1.7% | -1.4 | n/a | no target |
| P11 | 3321 | 9.7% | 9.7% | -19.6 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 10515 | 1.2% | 1.2% | +0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 3.8% | 3.8% | +3.8 | n/a | no target |
| P01T | 203 | 15.8% | 15.8% | -0.5 | n/a | no target |
| P01_GOLD | 625 | 33.8% | 33.8% | -0.2 | 70% | ❌ 36 pts to go |
| P02 | 429 | 41.7% | 41.7% | -2.6 | 75% | ❌ 33 pts to go |
| P03 | 218 | 22.5% | 22.5% | -0.6 | 55% | ❌ 32 pts to go |
| P04 | 2588 | 30.7% | 30.7% | -19.8 | 75% | ❌ 44 pts to go |
| P05 | 418 | 10.8% | 10.8% | -0.9 | 50% | ❌ 39 pts to go |
| P06M | 4395 | 0.2% | 0.2% | -1.6 | n/a | no target |
| P06T | 19508 | 0.8% | 0.8% | -0.7 | n/a | no target |
| P06 | 329 | 9.4% | 9.4% | -0.8 | n/a | no target |
| P07 | 710 | 5.4% | 5.4% | -4.9 | n/a | no target |
| P08 | 19644 | 0.1% | 0.1% | -0.4 | n/a | no target |
| P09 | 312 | 76.0% | 76.0% | -1.7 | 95% | ❌ 19 pts to go |
| P10R | 26614 | 0.7% | 0.7% |  | n/a | no target |
| P10 | 2472 | 1.1% | 1.1% | -0.7 | n/a | no target |
| P11 | 3321 | 9.7% | 9.7% | -19.2 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 10515 | 0.8% | 0.8% | +0.2 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 7.5% | 7.5% | -9.2 | n/a | no target |
| P01T | 203 | 12.8% | 12.8% | -6.8 | n/a | no target |
| P01_GOLD | 625 | 57.8% | 57.9% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 429 | 49.2% | 49.4% | -3.0 | 75% | ❌ 26 pts to go |
| P03 | 218 | 43.6% | 43.6% | -1.6 | 70% | ❌ 26 pts to go |
| P04 | 2588 | 29.6% | 30.3% | -19.1 | 70% | ❌ 40 pts to go |
| P05 | 418 | 14.6% | 14.6% | -1.8 | 50% | ❌ 35 pts to go |
| P06M | 4395 | 0.6% | 0.6% | -3.6 | n/a | no target |
| P06T | 19508 | 0.5% | 0.6% | -1.1 | n/a | no target |
| P06 | 329 | 14.0% | 14.0% | -10.1 | n/a | no target |
| P07 | 710 | 2.3% | 2.3% | -2.9 | n/a | no target |
| P08 | 19644 | 0.2% | 0.2% | -0.8 | n/a | no target |
| P09 | 312 | 45.8% | 46.2% | +1.7 | 80% | ❌ 34 pts to go |
| P10R | 26614 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2472 | 1.1% | 1.1% | -0.4 | n/a | no target |
| P11 | 3321 | 2.8% | 2.8% | -13.9 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 10515 | 0.5% | 0.5% | +0.2 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 13.2% | 13.2% | -25.7 | n/a | no target |
| P01T | 203 | 30.0% | 30.0% | -26.5 | 60% | ❌ 30 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | +0.0 | 70% | 🟡 6 pts to go |
| P02 | 429 | 41.0% | 41.0% | -2.8 | 50% | 🟡 9 pts to go |
| P03 | 218 | 52.8% | 52.8% | -2.5 | 55% | 🟡 2 pts to go |
| P04 | 2588 | 14.0% | 14.0% | -8.9 | 40% | ❌ 26 pts to go |
| P05 | 418 | 16.5% | 16.5% | -0.9 | 40% | ❌ 24 pts to go |
| P06M | 4395 | 0.5% | 0.5% | -16.2 | n/a | no target |
| P06T | 19508 | 1.8% | 1.8% | -10.7 | n/a | no target |
| P06 | 329 | 15.8% | 15.8% | -14.9 | n/a | no target |
| P07 | 710 | 6.2% | 6.2% | -10.1 | n/a | no target |
| P08 | 19644 | 0.9% | 0.9% | -3.8 | n/a | no target |
| P09 | 312 | 5.8% | 5.8% | +0.0 | n/a | no target |
| P10R | 26614 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2472 | 2.7% | 2.7% | -1.2 | n/a | no target |
| P11 | 3321 | 1.9% | 1.9% | -5.7 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 10515 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 15.1% | 15.1% | -29.3 | n/a | no target |
| P01T | 203 | 36.0% | 36.0% | -33.6 | 65% | ❌ 29 pts to go |
| P01_GOLD | 625 | 69.1% | 69.1% | -0.1 | 70% | 🟡 1 pts to go |
| P02 | 429 | 24.5% | 24.5% | -1.7 | 50% | ❌ 26 pts to go |
| P03 | 218 | 53.7% | 53.7% | -2.5 | 60% | 🟡 6 pts to go |
| P04 | 2588 | 6.0% | 6.0% | -3.9 | 40% | ❌ 34 pts to go |
| P05 | 418 | 18.9% | 18.9% | -2.5 | 45% | ❌ 26 pts to go |
| P06M | 4395 | 0.2% | 0.2% | -6.9 | n/a | no target |
| P06T | 19508 | 0.6% | 0.6% | -3.7 | n/a | no target |
| P06 | 329 | 27.4% | 27.4% | -20.8 | n/a | no target |
| P07 | 710 | 7.9% | 7.9% | -15.9 | n/a | no target |
| P08 | 19644 | 0.4% | 0.4% | -2.0 | n/a | no target |
| P09 | 312 | 9.6% | 9.6% | +0.9 | n/a | no target |
| P10R | 26614 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2472 | 1.5% | 1.5% | -0.6 | n/a | no target |
| P11 | 3321 | 1.0% | 1.0% | -5.8 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 10515 | 0.3% | 0.3% | +0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 3.8% | 3.8% | -7.3 | n/a | no target |
| P01T | 203 | 21.2% | 21.2% | -23.4 | n/a | no target |
| P01_GOLD | 625 | 49.6% | 49.6% | -0.2 | 50% | 🟡 0 pts to go |
| P02 | 429 | 40.1% | 40.1% | -2.5 | n/a | no target |
| P03 | 218 | 56.4% | 56.4% | -2.3 | 60% | 🟡 4 pts to go |
| P04 | 2588 | 16.0% | 16.0% | -10.4 | n/a | no target |
| P05 | 418 | 14.6% | 14.6% | -2.1 | n/a | no target |
| P06M | 4395 | 0.4% | 0.4% | -3.8 | n/a | no target |
| P06T | 19508 | 0.8% | 0.8% | -3.2 | n/a | no target |
| P06 | 329 | 19.8% | 19.8% | -15.7 | n/a | no target |
| P07 | 710 | 7.5% | 7.5% | -11.2 | n/a | no target |
| P08 | 19644 | 0.3% | 0.3% | -1.2 | n/a | no target |
| P09 | 312 | 18.3% | 18.3% | -0.6 | n/a | no target |
| P10R | 26614 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2472 | 1.9% | 1.9% | -0.5 | n/a | no target |
| P11 | 3321 | 1.1% | 1.1% | -6.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -21.1 | n/a | no target |
| P13 | 10515 | 0.7% | 0.7% | +0.3 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 7.5% | 7.5% | -20.3 | 15% | 🟡 8 pts to go |
| P01T | 203 | 15.3% | 15.3% | -14.0 | 15% | ✅ met |
| P01_GOLD | 625 | 35.2% | 35.2% | +0.1 | 40% | 🟡 5 pts to go |
| P02 | 429 | 12.8% | 13.1% | -1.1 | 25% | ❌ 12 pts to go |
| P03 | 218 | 20.6% | 20.6% | -1.0 | 25% | 🟡 4 pts to go |
| P04 | 2588 | 3.2% | 3.2% | -2.0 | 15% | ❌ 12 pts to go |
| P05 | 418 | 6.5% | 6.5% | -1.6 | 15% | 🟡 8 pts to go |
| P06M | 4395 | 0.7% | 0.7% | -5.3 | 15% | ❌ 14 pts to go |
| P06T | 19508 | 0.4% | 0.4% | -1.1 | 15% | ❌ 15 pts to go |
| P06 | 329 | 6.4% | 6.4% | -3.8 | 15% | 🟡 9 pts to go |
| P07 | 710 | 2.7% | 2.7% | -4.0 | 15% | ❌ 12 pts to go |
| P08 | 19644 | 0.2% | 0.2% | -0.7 | 15% | ❌ 15 pts to go |
| P09 | 312 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 26614 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P10 | 2472 | 0.6% | 0.6% | -0.8 | 15% | ❌ 14 pts to go |
| P11 | 3321 | 0.2% | 0.2% | -1.1 | 15% | ❌ 15 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 10515 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 3.8% | 3.8% | -7.3 | 15% | ❌ 11 pts to go |
| P01T | 203 | 16.3% | 16.3% | -16.3 | 25% | 🟡 9 pts to go |
| P01_GOLD | 625 | 29.0% | 29.0% | -0.2 | 25% | ✅ met |
| P02 | 429 | 26.3% | 26.3% | -1.7 | 15% | ✅ met |
| P03 | 218 | 24.8% | 24.8% | -1.2 | 15% | ✅ met |
| P04 | 2588 | 4.9% | 4.9% | -3.3 | 15% | ❌ 10 pts to go |
| P05 | 418 | 10.5% | 10.5% | -1.5 | 15% | 🟡 4 pts to go |
| P06M | 4395 | 0.1% | 0.1% | -2.3 | 15% | ❌ 15 pts to go |
| P06T | 19508 | 0.4% | 0.4% | -2.3 | 15% | ❌ 15 pts to go |
| P06 | 329 | 6.1% | 6.1% | -5.9 | 15% | 🟡 9 pts to go |
| P07 | 710 | 2.8% | 2.8% | -4.7 | 15% | ❌ 12 pts to go |
| P08 | 19644 | 0.2% | 0.2% | -0.8 | 15% | ❌ 15 pts to go |
| P09 | 312 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 26614 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 2472 | 1.1% | 1.1% | -0.3 | 15% | ❌ 14 pts to go |
| P11 | 3321 | 0.7% | 0.7% | -4.4 | 15% | ❌ 14 pts to go |
| P12 | 8 | 12.5% | 12.5% | -13.8 | 15% | 🟡 2 pts to go |
| P13 | 10515 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 1.9% | 1.9% | -3.7 | 20% | ❌ 18 pts to go |
| P01T | 203 | 4.9% | 4.9% | -4.9 | 20% | ❌ 15 pts to go |
| P01_GOLD | 625 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 429 | 1.4% | 1.4% | -0.1 | 20% | ❌ 19 pts to go |
| P03 | 218 | 1.8% | 1.8% | -0.1 | 20% | ❌ 18 pts to go |
| P04 | 2588 | 0.6% | 0.6% | -0.4 | 20% | ❌ 19 pts to go |
| P05 | 418 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 4395 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 19508 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P06 | 329 | 1.5% | 1.5% | -2.1 | 20% | ❌ 18 pts to go |
| P07 | 710 | 0.4% | 0.4% | -0.4 | 20% | ❌ 20 pts to go |
| P08 | 19644 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P09 | 312 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2472 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P11 | 3321 | 0.1% | 0.1% | -0.5 | 20% | ❌ 20 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 1.9% | 1.9% | -3.7 | 15% | ❌ 13 pts to go |
| P01T | 203 | 3.4% | 3.4% | -4.2 | 15% | ❌ 12 pts to go |
| P01_GOLD | 625 | 10.6% | 10.6% | +0.0 | 15% | 🟡 4 pts to go |
| P02 | 429 | 12.6% | 12.6% | -0.8 | 15% | 🟡 2 pts to go |
| P03 | 218 | 22.9% | 22.9% | -1.1 | 15% | ✅ met |
| P04 | 2588 | 2.7% | 2.7% | -1.9 | 15% | ❌ 12 pts to go |
| P05 | 418 | 2.6% | 2.6% | -0.3 | 15% | ❌ 12 pts to go |
| P06M | 4395 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 19508 | 0.2% | 0.2% | -1.2 | 15% | ❌ 15 pts to go |
| P06 | 329 | 3.3% | 3.3% | -2.1 | 15% | ❌ 12 pts to go |
| P07 | 710 | 1.4% | 1.4% | -2.2 | 15% | ❌ 14 pts to go |
| P08 | 19644 | 0.1% | 0.1% | -0.6 | 15% | ❌ 15 pts to go |
| P09 | 312 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 26614 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 2472 | 0.6% | 0.6% | -0.2 | 15% | ❌ 14 pts to go |
| P11 | 3321 | 0.3% | 0.3% | -1.8 | 15% | ❌ 15 pts to go |
| P12 | 8 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 10515 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 5.7% | 5.7% | -5.4 | 20% | ❌ 14 pts to go |
| P01T | 203 | 20.2% | 20.2% | -21.1 | 40% | ❌ 20 pts to go |
| P01_GOLD | 625 | 45.6% | 45.6% | -0.2 | 40% | ✅ met |
| P02 | 429 | 45.7% | 45.7% | -2.8 | 20% | ✅ met |
| P03 | 218 | 53.2% | 53.2% | -2.6 | 35% | ✅ met |
| P04 | 2588 | 18.4% | 18.4% | -11.9 | 20% | 🟡 2 pts to go |
| P05 | 418 | 14.8% | 14.8% | -1.9 | 20% | 🟡 5 pts to go |
| P06M | 4395 | 0.5% | 0.5% | -3.7 | 20% | ❌ 20 pts to go |
| P06T | 19508 | 1.0% | 1.0% | -3.5 | 20% | ❌ 19 pts to go |
| P06 | 329 | 20.7% | 20.7% | -14.8 | 20% | ✅ met |
| P07 | 710 | 6.8% | 6.8% | -7.9 | 20% | ❌ 13 pts to go |
| P08 | 19644 | 0.5% | 0.5% | -1.8 | 20% | ❌ 20 pts to go |
| P09 | 312 | 18.3% | 18.3% | -3.7 | 20% | 🟡 2 pts to go |
| P10R | 26614 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P10 | 2472 | 2.0% | 2.0% | -0.6 | 20% | ❌ 18 pts to go |
| P11 | 3321 | 1.3% | 1.3% | -6.7 | 20% | ❌ 19 pts to go |
| P12 | 8 | 0.0% | 0.0% | -15.8 | 20% | ❌ 20 pts to go |
| P13 | 10515 | 0.9% | 0.9% | +0.3 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 45.3% | 45.3% | +45.3 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | -0.6 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.3 | 95% | ❌ 26 pts to go |
| P02 | 429 | 68.5% | 68.5% | -4.8 | 95% | ❌ 26 pts to go |
| P03 | 218 | 64.2% | 64.2% | -3.1 | 90% | ❌ 26 pts to go |
| P04 | 2588 | 35.7% | 35.7% | -22.7 | 85% | ❌ 49 pts to go |
| P05 | 418 | 35.6% | 35.6% | +0.7 | 75% | ❌ 39 pts to go |
| P06M | 4395 | 61.6% | 61.6% | +61.6 | n/a | no target |
| P06T | 19508 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 89.4% | 89.4% | -1.4 | 100% | ❌ 11 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 2.6% | 2.6% | -16.2 | 60% | ❌ 57 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 45.3% | 45.3% | +45.3 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 429 | 72.5% | 72.5% | -4.7 | 100% | ❌ 28 pts to go |
| P03 | 218 | 71.1% | 71.1% | -3.4 | n/a | no target |
| P04 | 2588 | 36.7% | 36.7% | -23.3 | 95% | ❌ 58 pts to go |
| P05 | 418 | 32.3% | 32.3% | +1.1 | 80% | ❌ 48 pts to go |
| P06M | 4395 | 61.6% | 61.6% | +61.6 | n/a | no target |
| P06T | 19508 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 92.6% | 92.6% | -0.8 | 100% | 🟡 7 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 2.8% | 2.8% | -17.2 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 62.3% | 62.3% | +62.3 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | -0.6 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | -0.2 | 85% | ❌ 33 pts to go |
| P02 | 429 | 62.7% | 62.7% | -4.1 | 90% | ❌ 27 pts to go |
| P03 | 218 | 52.3% | 52.3% | -2.5 | 85% | ❌ 33 pts to go |
| P04 | 2588 | 39.8% | 39.8% | -24.3 | 90% | ❌ 50 pts to go |
| P05 | 418 | 33.7% | 33.7% | -1.5 | 75% | ❌ 41 pts to go |
| P06M | 4395 | 92.1% | 92.1% | +92.1 | n/a | no target |
| P06T | 19508 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 85.3% | 85.3% | -0.3 | 95% | 🟡 10 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 2.4% | 2.4% | -14.9 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 64.2% | 64.2% | +64.2 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | -0.6 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | -0.4 | 85% | ❌ 33 pts to go |
| P02 | 429 | 57.3% | 57.3% | -3.8 | 90% | ❌ 33 pts to go |
| P03 | 218 | 53.7% | 53.7% | -2.5 | 85% | ❌ 31 pts to go |
| P04 | 2588 | 33.8% | 33.8% | -20.5 | 90% | ❌ 56 pts to go |
| P05 | 418 | 42.1% | 42.1% | +0.4 | 75% | ❌ 33 pts to go |
| P06M | 4395 | 85.9% | 85.9% | +85.9 | n/a | no target |
| P06T | 19508 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 2.0% | 2.0% | -12.1 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 69.8% | 69.8% | +69.8 | n/a | no target |
| P01T | 203 | 90.6% | 90.6% | +9.1 | n/a | no target |
| P01_GOLD | 625 | 85.8% | 85.8% | +0.1 | 100% | ❌ 14 pts to go |
| P02 | 429 | 76.9% | 76.9% | -4.8 | 100% | ❌ 23 pts to go |
| P03 | 218 | 89.9% | 89.9% | -2.4 | n/a | no target |
| P04 | 2588 | 45.7% | 45.7% | -26.9 | 95% | ❌ 49 pts to go |
| P05 | 418 | 76.8% | 76.8% | +1.3 | 95% | ❌ 18 pts to go |
| P06M | 4395 | 96.3% | 96.3% | +95.7 | n/a | no target |
| P06T | 19508 | 92.5% | 92.5% | +9.1 | n/a | no target |
| P06 | 329 | 37.4% | 37.4% | -38.5 | n/a | no target |
| P07 | 710 | 28.7% | 28.7% | -48.3 | n/a | no target |
| P08 | 19644 | 15.5% | 15.5% | -69.4 | n/a | no target |
| P09 | 312 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 26614 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 75.4% | 75.4% | -23.0 | n/a | no target |
| P11 | 3321 | 34.2% | 34.2% | -55.7 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 69.8% | 69.8% | +69.8 | n/a | no target |
| P01T | 203 | 90.6% | 90.6% | +9.1 | n/a | no target |
| P01_GOLD | 625 | 89.0% | 89.0% | +0.1 | 100% | ❌ 11 pts to go |
| P02 | 429 | 78.1% | 78.3% | -4.8 | 100% | ❌ 22 pts to go |
| P03 | 218 | 91.3% | 91.3% | -2.5 | n/a | no target |
| P04 | 2588 | 50.3% | 50.3% | -28.7 | 95% | ❌ 45 pts to go |
| P05 | 418 | 90.7% | 90.7% | +0.6 | 70% | ✅ met |
| P06M | 4395 | 96.3% | 96.3% | +95.7 | n/a | no target |
| P06T | 19508 | 92.5% | 92.5% | +9.1 | n/a | no target |
| P06 | 329 | 37.4% | 37.4% | -38.5 | n/a | no target |
| P07 | 710 | 28.7% | 28.7% | -48.3 | n/a | no target |
| P08 | 19644 | 15.5% | 15.5% | -69.4 | n/a | no target |
| P09 | 312 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 26614 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 75.4% | 75.4% | -23.0 | n/a | no target |
| P11 | 3321 | 34.3% | 34.3% | -56.0 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | -0.6 | n/a | no target · rows from a source that publishes bids: 6 rows, 16.7% filled |
| P01_GOLD | 625 | 17.1% | 17.1% | -0.2 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 367 rows, 29.2% filled |
| P02 | 429 | 12.4% | 12.4% | -0.7 | n/a | no target · rows from a source that publishes bids: 294 rows, 18.0% filled |
| P03 | 218 | 15.6% | 15.6% | -0.7 | n/a | no target · rows from a source that publishes bids: 140 rows, 24.3% filled |
| P04 | 2588 | 2.2% | 2.2% | -1.5 | n/a | no target · rows from a source that publishes bids: 878 rows, 6.6% filled |
| P05 | 418 | 3.3% | 3.3% | -0.1 | n/a | no target · rows from a source that publishes bids: 54 rows, 25.9% filled |
| P06M | 4395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19508 | 0.0% | 0.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 64 rows, 4.7% filled |
| P06 | 329 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 3.2% | 3.2% | +0.1 | n/a | no target · rows from a source that publishes bids: 299 rows, 3.3% filled |
| P10R | 26614 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3321 | 0.4% | 0.4% | -2.3 | n/a | no target · rows from a source that publishes bids: 91 rows, 14.3% filled |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 8 rows, 0.0% filled |
| P13 | 10515 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.5% | 97.5% | +0.5 | n/a | no target |
| P01_GOLD | 625 | 53.1% | 82.4% | -0.1 | 90% | ❌ 37 pts to go |
| P02 | 429 | 57.3% | 86.5% | -3.8 | 90% | ❌ 33 pts to go |
| P03 | 218 | 53.7% | 76.6% | -2.5 | 90% | ❌ 36 pts to go |
| P04 | 2588 | 27.6% | 91.3% | -17.7 | 90% | ❌ 62 pts to go |
| P05 | 418 | 0.0% | 82.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 4395 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 19508 | 0.0% | 99.7% | +0.0 | n/a | no target |
| P06 | 329 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 2.2% | 3.8% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 26614 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3321 | 1.8% | 98.7% | -10.9 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 1.0% | 98.0% | +1.0 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.2% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 429 | 56.4% | 85.5% | -3.5 | n/a | no target |
| P03 | 218 | 29.4% | 52.3% | -1.4 | n/a | no target |
| P04 | 2588 | 30.2% | 93.9% | -19.5 | n/a | no target |
| P05 | 418 | 0.5% | 82.8% | +0.0 | n/a | no target |
| P06M | 4395 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 19508 | 0.2% | 99.8% | +0.2 | n/a | no target |
| P06 | 329 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 42.0% | 43.6% | -2.4 | n/a | no target |
| P10R | 26614 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3321 | 1.7% | 98.5% | -9.9 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 2.5% | 99.5% | +0.3 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 81.0% | +0.1 | 95% | ❌ 43 pts to go |
| P02 | 429 | 61.8% | 90.9% | -3.8 | n/a | no target |
| P03 | 218 | 56.4% | 79.4% | -2.7 | n/a | no target |
| P04 | 2588 | 30.5% | 94.2% | -19.8 | n/a | no target |
| P05 | 418 | 4.8% | 87.1% | -0.4 | n/a | no target |
| P06M | 4395 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 19508 | 0.2% | 99.9% | +0.2 | n/a | no target |
| P06 | 329 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 710 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19644 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 64.1% | 65.7% | -3.4 | n/a | no target |
| P10R | 26614 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2472 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3321 | 1.8% | 98.6% | -10.9 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10515 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 218 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 2588 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 418 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4395 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 19508 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 329 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 710 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 19644 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 26614 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2472 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3321 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10515 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 218 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 2588 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 418 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4395 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 19508 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 329 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 710 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 19644 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 26614 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2472 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3321 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10515 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 218 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 2588 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 418 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4395 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 19508 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 329 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 710 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 19644 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 26614 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2472 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3321 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10515 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

