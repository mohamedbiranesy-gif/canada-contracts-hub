# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **92 of 438 met** (21.0%); 65 within 10 points; 281 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 190, P01T 202, P01_GOLD 624, P02 464, P03 262, P04 3556, P05 419, P06M 18956, P06T 43465, P06 253, P07 660, P08 21363, P09 278, P10R 0, P10 2137, P11 1596, P12 16, P13 164579

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 15.3% | 8 | vendor GST/HST number (175 rows) |
| P01T | 202 | 1.0% | 34.2% | 8 | payment terms (158 rows) |
| P01_GOLD | 624 | 24.4% | 71.3% | 10 | payment terms (216 rows) |
| P02 | 464 | 7.5% | 55.2% | 9 | PO rule (354 rows) |
| P03 | 262 | 15.3% | 55.3% | 9 | payment terms (130 rows) |
| P04 | 3556 | 1.3% | 17.0% | 6 | PO rule (3355 rows) |
| P05 | 419 | 1.0% | 17.2% | 7 | payment terms (347 rows) |
| P06M | 18956 | 0.0% | 2.7% | 7 | PO rule (18577 rows) |
| P06T | 43465 | 0.1% | 9.5% | 6 | PO rule (43121 rows) |
| P06 | 253 | 0.0% | 11.9% | 6 | reference to quote (PO / contract / vendor id) (253 rows) |
| P07 | 660 | 0.0% | 2.6% | 6 | reference to quote (PO / contract / vendor id) (660 rows) |
| P08 | 21363 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (21363 rows) |
| P09 | 278 | 1.4% | 41.4% | 8 | payment terms (260 rows) |
| P10 | 2137 | 0.0% | 1.3% | 5 | reference to quote (PO / contract / vendor id) (2137 rows) |
| P11 | 1596 | 0.1% | 7.1% | 6 | PO rule (1529 rows) |
| P12 | 16 | 0.0% | 50.0% | 9 | PO rule (15 rows) |
| P13 | 164579 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (164579 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 190 | 8 | 53 | 129 | 0 | 0 | 71 |
| P01T | 202 | 23 | 39 | 140 | 0 | 0 | 68 |
| P01_GOLD | 624 | 236 | 185 | 203 | 0 | 0 | 82 |
| P02 | 464 | 0 | 188 | 276 | 0 | 0 | 66 |
| P03 | 262 | 0 | 0 | 249 | 13 | 0 | 57 |
| P04 | 3556 | 0 | 0 | 2917 | 639 | 0 | 46 |
| P05 | 419 | 14 | 29 | 363 | 13 | 0 | 51 |
| P06M | 18956 | 0 | 17 | 18875 | 64 | 0 | 46 |
| P06T | 43465 | 0 | 26 | 28230 | 15209 | 0 | 38 |
| P06 | 253 | 16 | 47 | 190 | 0 | 0 | 70 |
| P07 | 660 | 0 | 21 | 616 | 23 | 0 | 54 |
| P08 | 21363 | 0 | 0 | 18711 | 2652 | 0 | 44 |
| P09 | 278 | 4 | 11 | 262 | 1 | 0 | 53 |
| P10 | 2137 | 3 | 13 | 1448 | 673 | 0 | 41 |
| P11 | 1596 | 7 | 13 | 36 | 0 | 1540 | 23 |
| P12 | 16 | 0 | 0 | 16 | 0 | 0 | 54 |
| P13 | 164579 | 12 | 63 | 164491 | 13 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 190 | 139 | 73.2% | tax treatment (27) |
| P01T | 202 | 119 | 58.9% | bill-to legal name and address (69) |
| P01_GOLD | 624 | 471 | 75.5% | bill-to legal name and address (99) |
| P02 | 464 | 313 | 67.5% | the buyer's PO / reference rule (85) |
| P03 | 262 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (262) |
| P04 | 3556 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3556) |
| P05 | 419 | 44 | 10.5% | a confirmed invoicing / AP or finance channel (332) |
| P06M | 18956 | 189 | 1.0% | a confirmed invoicing / AP or finance channel (18702) |
| P06T | 43465 | 234 | 0.5% | a confirmed invoicing / AP or finance channel (42846) |
| P06 | 253 | 43 | 17.0% | the buyer's PO / reference rule (111) |
| P07 | 660 | 6 | 0.9% | the buyer's PO / reference rule (266) |
| P08 | 21363 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (21363) |
| P09 | 278 | 40 | 14.4% | a confirmed invoicing / AP or finance channel (227) |
| P10 | 2137 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2059) |
| P11 | 1596 | 14 | 0.9% | a confirmed invoicing / AP or finance channel (1540) |
| P12 | 16 | 4 | 25.0% | a confirmed invoicing / AP or finance channel (11) |
| P13 | 164579 | 41 | 0.0% | a confirmed invoicing / AP or finance channel (162227) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 190 | 5 | 2.6% | 7 | 0 | the vendor's GST/HST number (BN9) (175) |
| P01T | 202 | 80 | 39.6% | 3 | 0 | the vendor's GST/HST number (BN9) (74) |
| P01_GOLD | 624 | 403 | 64.6% | 10 | 0 | the vendor's GST/HST number (BN9) (145) |
| P02 | 464 | 213 | 45.9% | 22 | 0 | the vendor's GST/HST number (BN9) (199) |
| P03 | 262 | 17 | 6.5% | 0 | 133 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (94) |
| P04 | 3556 | 43 | 1.2% | 7 | 886 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2562) |
| P05 | 419 | 20 | 4.8% | 8 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (202) |
| P06M | 18956 | 7 | 0.0% | 12 | 479 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (18135) |
| P06T | 43465 | 250 | 0.6% | 14 | 10556 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (32222) |
| P06 | 253 | 26 | 10.3% | 48 | 0 | the vendor's GST/HST number (BN9) (116) |
| P07 | 660 | 6 | 0.9% | 106 | 33 | the vendor's GST/HST number (BN9) (309) |
| P08 | 21363 | 4 | 0.0% | 12 | 4951 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (16356) |
| P09 | 278 | 36 | 12.9% | 0 | 106 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (109) |
| P10 | 2137 | 7 | 0.3% | 16 | 303 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1731) |
| P11 | 1596 | 7 | 0.4% | 3 | 0 | a confirmed invoicing / AP or finance channel (1524) |
| P12 | 16 | 3 | 18.8% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5) |
| P13 | 164579 | 20 | 0.0% | 1149 | 66214 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (95821) |
| **all** | 259020 | 1147 | 0.4% | 1417 | 83789 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 182 | 0 | 0 | 0 | 126 | 9 | 0 | 140 | 154 | 13 |
| P01T | 179 | 0 | 0 | 0 | 104 | 63 | 27 | 141 | 159 | 9 |
| P01_GOLD | 388 | 0 | 0 | 0 | 12 | 81 | 30 | 195 | 231 | 37 |
| P02 | 464 | 0 | 464 | 0 | 38 | 55 | 15 | 354 | 283 | 11 |
| P03 | 262 | 0 | 262 | 0 | 17 | 45 | 27 | 129 | 138 | 9 |
| P04 | 3556 | 0 | 3556 | 0 | 1526 | 1290 | 965 | 3355 | 3107 | 156 |
| P05 | 405 | 0 | 352 | 0 | 80 | 94 | 38 | 335 | 349 | 50 |
| P06M | 18956 | 0 | 18956 | 0 | 13446 | 1565 | 108 | 18577 | 18331 | 456 |
| P06T | 43465 | 0 | 43465 | 0 | 39187 | 28940 | 18494 | 43121 | 42716 | 941 |
| P06 | 237 | 0 | 0 | 0 | 113 | 66 | 42 | 169 | 200 | 9 |
| P07 | 660 | 0 | 660 | 0 | 418 | 267 | 115 | 616 | 619 | 12 |
| P08 | 21363 | 0 | 21363 | 0 | 16283 | 9615 | 3962 | 21089 | 20740 | 427 |
| P09 | 274 | 0 | 254 | 0 | 12 | 71 | 1 | 248 | 262 | 17 |
| P10 | 2134 | 0 | 2101 | 0 | 1107 | 1161 | 974 | 2066 | 2028 | 119 |
| P11 | 1589 | 1540 | 1492 | 0 | 757 | 1130 | 487 | 1529 | 1526 | 56 |
| P12 | 16 | 0 | 14 | 0 | 1 | 4 | 0 | 15 | 15 | 1 |
| P13 | 164567 | 0 | 164129 | 0 | 132187 | 105913 | 20 | 164222 | 163366 | 36 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 52.0% | 95% | 70727 |
| buyer_logo_url | P13 | 63.9% | 95% | 51244 |
| buyer_legal_name_as_published | P13 | 35.6% | 60% | 40082 |
| buyer_bn_as_published | P13 | 8.2% | 30% | 35814 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 32879 |
| ap_system_hint | P13 | 0.4% | 20% | 32308 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 24554 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 24500 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 23817 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 8681 |
| ap_system_hint | P06T | 0.6% | 20% | 8423 |
| vendor_registered_address | P08 | 30.6% | 70% | 8408 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 6430 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 6420 |
| buyer_payment_method_preference | P06T | 0.5% | 15% | 6309 |
| buyer_phone | P08 | 68.5% | 95% | 5662 |
| invoice_reference_hint | P08 | 1.3% | 25% | 5067 |
| buyer_legal_name_as_published | P08 | 55.0% | 75% | 4275 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 4262 |
| vendor_phone | P08 | 65.4% | 85% | 4177 |
| vendor_emails | P08 | 55.9% | 75% | 4089 |
| vendor_bn9 | P08 | 31.0% | 50% | 4063 |
| ap_system_hint | P08 | 1.0% | 20% | 4060 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 3785 |
| ap_system_hint | P06M | 1.1% | 20% | 3591 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3106 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3101 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3071 |
| buyer_address | P08 | 81.4% | 95% | 2900 |
| vendor_trading_name | P08 | 36.5% | 50% | 2879 |
| buyer_esignature_preference | P06M | 0.5% | 15% | 2749 |
| buyer_tax_exempt_status | P06M | 0.7% | 15% | 2710 |
| buyer_payment_method_preference | P06M | 0.7% | 15% | 2702 |
| average_contract_duration_days | P04 | 19.3% | 90% | 2515 |
| buyer_bn_as_published | P08 | 23.3% | 35% | 2490 |
| currency | P04 | 26.5% | 95% | 2436 |
| end_date | P04 | 24.2% | 90% | 2339 |
| ap_phone | P04 | 21.3% | 85% | 2265 |
| commodity_codes | P04 | 21.8% | 85% | 2249 |
| vendor_neq | P04 | 32.1% | 95% | 2238 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 91.1% | 91.1% | +2.0 | 50% | ✅ met |
| P01T | 202 | 95.0% | 95.0% | +1.2 | 50% | ✅ met |
| P01_GOLD | 624 | 92.5% | 94.7% | +0.3 | 95% | 🟡 2 pts to go |
| P02 | 464 | 75.0% | 76.5% | +1.0 | 95% | ❌ 20 pts to go |
| P03 | 262 | 80.9% | 84.4% | -0.5 | 95% | ❌ 14 pts to go |
| P04 | 3556 | 31.3% | 33.0% | +1.1 | 90% | ❌ 59 pts to go |
| P05 | 419 | 38.9% | 41.8% | +0.3 | 70% | ❌ 31 pts to go |
| P06M | 18956 | 91.9% | 91.9% | +0.1 | n/a | no target |
| P06T | 43465 | 99.0% | 99.0% | +0.4 | n/a | no target |
| P06 | 253 | 33.2% | 33.2% | -1.2 | 30% | ✅ met |
| P07 | 660 | 6.7% | 6.7% | -0.2 | 30% | ❌ 23 pts to go |
| P08 | 21363 | 1.3% | 1.3% | +0.0 | 25% | ❌ 24 pts to go |
| P09 | 278 | 98.9% | 99.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10 | 2137 | 3.3% | 3.3% | +0.2 | 25% | ❌ 22 pts to go |
| P11 | 1596 | 51.9% | 52.7% | +5.0 | 60% | 🟡 8 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164579 | 99.6% | 99.6% | -0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 202 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 624 | 5.9% | 5.9% | -0.2 | 50% | ❌ 44 pts to go |
| P02 | 464 | 5.8% | 5.8% | -0.4 | 50% | ❌ 44 pts to go |
| P03 | 262 | 1.5% | 1.5% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3556 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 419 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 18956 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 86.3% | 86.3% | +4.1 | n/a | no target |
| P01T | 202 | 77.2% | 77.2% | +2.7 | 50% | ✅ met |
| P01_GOLD | 624 | 67.3% | 67.3% | +0.5 | 85% | ❌ 18 pts to go |
| P02 | 464 | 65.9% | 65.9% | +1.1 | 90% | ❌ 24 pts to go |
| P03 | 262 | 60.3% | 60.3% | +0.6 | 85% | ❌ 25 pts to go |
| P04 | 3556 | 28.6% | 28.6% | +1.0 | 85% | ❌ 56 pts to go |
| P05 | 419 | 29.1% | 29.1% | +0.2 | 60% | ❌ 31 pts to go |
| P06M | 18956 | 91.6% | 91.6% | +0.1 | n/a | no target |
| P06T | 43465 | 98.9% | 98.9% | +0.5 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 95.7% | 95.7% | -0.4 | 100% | 🟡 4 pts to go |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 48.7% | 48.7% | +5.4 | 60% | ❌ 11 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 202 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 624 | 51.6% | 51.6% | +0.8 | 80% | ❌ 28 pts to go |
| P02 | 464 | 58.2% | 58.2% | +1.3 | 60% | 🟡 2 pts to go |
| P03 | 262 | 50.0% | 50.0% | -0.2 | 80% | ❌ 30 pts to go |
| P04 | 3556 | 23.6% | 23.6% | +0.7 | 50% | ❌ 26 pts to go |
| P05 | 419 | 11.7% | 11.7% | +0.3 | 40% | ❌ 28 pts to go |
| P06M | 18956 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 81.3% | 81.3% | -2.1 | 50% | ✅ met |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 4.1% | 4.1% | -1.5 | 40% | ❌ 36 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 202 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 61.2% | 61.2% | +0.8 | 85% | ❌ 24 pts to go |
| P02 | 464 | 58.2% | 58.2% | +2.0 | 90% | ❌ 32 pts to go |
| P03 | 262 | 58.8% | 58.8% | +0.2 | 85% | ❌ 26 pts to go |
| P04 | 3556 | 24.4% | 24.4% | +0.8 | 85% | ❌ 61 pts to go |
| P05 | 419 | 19.6% | 19.6% | -0.1 | 50% | ❌ 30 pts to go |
| P06M | 18956 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 4.5% | 4.5% | -1.5 | 60% | ❌ 56 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 202 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 464 | 6.9% | 6.9% | +0.9 | 50% | ❌ 43 pts to go |
| P03 | 262 | 8.0% | 8.0% | -0.4 | 50% | ❌ 42 pts to go |
| P04 | 3556 | 1.9% | 1.9% | +0.1 | 40% | ❌ 38 pts to go |
| P05 | 419 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 18956 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 3.2% | 3.2% | -0.1 | 50% | ❌ 47 pts to go |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 0.6% | 0.6% | -0.3 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 202 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 36.2% | 36.2% | +1.4 | 80% | ❌ 44 pts to go |
| P02 | 464 | 52.6% | 52.6% | +0.7 | 90% | ❌ 37 pts to go |
| P03 | 262 | 33.6% | 33.6% | +0.9 | 80% | ❌ 46 pts to go |
| P04 | 3556 | 21.8% | 21.8% | +0.2 | 85% | ❌ 63 pts to go |
| P05 | 419 | 5.7% | 5.7% | +0.2 | 50% | ❌ 44 pts to go |
| P06M | 18956 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 73.7% | 73.7% | -0.6 | 95% | ❌ 21 pts to go |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 3.3% | 3.3% | -1.0 | 50% | ❌ 47 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 202 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 8.3% | 8.3% | -0.2 | 50% | ❌ 42 pts to go |
| P02 | 464 | 5.8% | 5.8% | -0.4 | 50% | ❌ 44 pts to go |
| P03 | 262 | 2.3% | 2.3% | +0.4 | 30% | ❌ 28 pts to go |
| P04 | 3556 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 419 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 18956 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 202 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 262 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3556 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 419 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 18956 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43465 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 253 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 660 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21363 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2137 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1596 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 7.9% | 7.9% | -3.7 | 70% | ❌ 62 pts to go |
| P01T | 202 | 55.0% | 55.0% | +4.5 | 60% | 🟡 5 pts to go |
| P01_GOLD | 624 | 74.5% | 74.5% | -0.3 | 90% | ❌ 16 pts to go |
| P02 | 464 | 54.3% | 54.3% | +0.7 | 85% | ❌ 31 pts to go |
| P03 | 262 | 67.6% | 67.6% | -2.0 | 90% | ❌ 22 pts to go |
| P04 | 3556 | 37.9% | 37.9% | +2.9 | 75% | ❌ 37 pts to go |
| P05 | 419 | 54.4% | 54.4% | -0.3 | 50% | ✅ met |
| P06M | 18956 | 3.0% | 3.0% | -0.2 | n/a | no target |
| P06T | 43465 | 51.0% | 51.0% | +3.7 | n/a | no target |
| P06 | 253 | 43.5% | 43.5% | -0.5 | 40% | ✅ met |
| P07 | 660 | 32.1% | 32.1% | -0.9 | 50% | ❌ 18 pts to go |
| P08 | 21363 | 31.0% | 31.0% | +0.5 | 50% | ❌ 19 pts to go |
| P09 | 278 | 56.5% | 56.5% | -1.8 | 80% | ❌ 24 pts to go |
| P10 | 2137 | 37.7% | 37.7% | +3.2 | 40% | 🟡 2 pts to go |
| P11 | 1596 | 51.4% | 51.4% | +4.5 | 60% | 🟡 9 pts to go |
| P12 | 16 | 56.2% | 56.2% | -3.8 | 85% | ❌ 29 pts to go |
| P13 | 164579 | 45.5% | 45.5% | +13.8 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 57.9% | 57.9% | -1.8 | n/a | no target |
| P01T | 202 | 55.0% | 55.0% | +4.0 | n/a | no target |
| P01_GOLD | 624 | 72.4% | 72.4% | -0.3 | 95% | ❌ 23 pts to go |
| P02 | 464 | 74.8% | 74.8% | +1.0 | 95% | ❌ 20 pts to go |
| P03 | 262 | 69.1% | 69.1% | -2.8 | 95% | ❌ 26 pts to go |
| P04 | 3556 | 53.0% | 53.0% | +3.8 | 95% | ❌ 42 pts to go |
| P05 | 419 | 58.5% | 58.5% | +0.2 | 70% | ❌ 12 pts to go |
| P06M | 18956 | 42.5% | 42.5% | -3.5 | n/a | no target |
| P06T | 43465 | 55.2% | 55.2% | -1.0 | n/a | no target |
| P06 | 253 | 40.7% | 40.7% | -0.3 | 80% | ❌ 39 pts to go |
| P07 | 660 | 32.1% | 32.1% | +0.2 | 70% | ❌ 38 pts to go |
| P08 | 21363 | 30.6% | 30.6% | +0.3 | 70% | ❌ 39 pts to go |
| P09 | 278 | 86.7% | 86.7% | +0.1 | 100% | ❌ 13 pts to go |
| P10 | 2137 | 38.5% | 38.5% | +3.0 | 70% | ❌ 32 pts to go |
| P11 | 1596 | 56.1% | 56.1% | +3.6 | 75% | ❌ 19 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 41.0% | 41.0% | +14.1 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 25.8% | 25.8% | +8.7 | n/a | no target |
| P01T | 202 | 60.9% | 60.9% | +7.3 | n/a | no target |
| P01_GOLD | 624 | 48.4% | 48.4% | -1.4 | 60% | ❌ 12 pts to go |
| P02 | 464 | 55.8% | 55.8% | -0.4 | 60% | 🟡 4 pts to go |
| P03 | 262 | 51.9% | 51.9% | -3.2 | 60% | 🟡 8 pts to go |
| P04 | 3556 | 42.5% | 42.5% | +0.4 | 55% | ❌ 12 pts to go |
| P05 | 419 | 23.4% | 23.4% | -1.2 | 50% | ❌ 27 pts to go |
| P06M | 18956 | 9.0% | 9.0% | +2.2 | n/a | no target |
| P06T | 43465 | 55.2% | 55.2% | +4.3 | n/a | no target |
| P06 | 253 | 48.6% | 48.6% | +1.0 | n/a | no target |
| P07 | 660 | 42.1% | 42.1% | +1.2 | 55% | ❌ 13 pts to go |
| P08 | 21363 | 36.5% | 36.5% | +0.3 | 50% | ❌ 14 pts to go |
| P09 | 278 | 72.3% | 72.3% | +0.0 | 70% | ✅ met |
| P10 | 2137 | 47.8% | 47.8% | +1.0 | 55% | 🟡 7 pts to go |
| P11 | 1596 | 57.1% | 57.1% | +4.9 | 50% | ✅ met |
| P12 | 16 | 87.5% | 87.5% | +0.8 | n/a | no target |
| P13 | 164579 | 3.2% | 3.2% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 42.6% | 42.6% | -7.8 | n/a | no target |
| P01T | 202 | 76.7% | 76.7% | +2.2 | n/a | no target |
| P01_GOLD | 624 | 49.8% | 49.8% | -0.7 | 70% | ❌ 20 pts to go |
| P02 | 464 | 56.5% | 56.5% | -1.7 | 70% | ❌ 14 pts to go |
| P03 | 262 | 50.8% | 50.8% | -0.5 | 70% | ❌ 19 pts to go |
| P04 | 3556 | 54.8% | 54.8% | +0.7 | 65% | ❌ 10 pts to go |
| P05 | 419 | 28.6% | 28.6% | +0.2 | 60% | ❌ 31 pts to go |
| P06M | 18956 | 31.5% | 31.5% | -5.1 | n/a | no target |
| P06T | 43465 | 75.7% | 75.7% | -4.3 | n/a | no target |
| P06 | 253 | 71.1% | 71.1% | +2.2 | 40% | ✅ met |
| P07 | 660 | 65.3% | 65.3% | +0.4 | 85% | ❌ 20 pts to go |
| P08 | 21363 | 65.4% | 65.4% | +0.1 | 85% | ❌ 20 pts to go |
| P09 | 278 | 56.8% | 56.8% | -2.5 | 85% | ❌ 28 pts to go |
| P10 | 2137 | 66.0% | 66.0% | +2.5 | 85% | ❌ 19 pts to go |
| P11 | 1596 | 64.9% | 64.9% | +3.0 | 75% | ❌ 10 pts to go |
| P12 | 16 | 37.5% | 37.5% | +10.8 | n/a | no target |
| P13 | 164579 | 91.9% | 91.9% | +0.7 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 47.9% | 47.9% | -8.7 | n/a | no target |
| P01T | 202 | 98.0% | 98.0% | +0.6 | n/a | no target |
| P01_GOLD | 624 | 78.5% | 78.5% | -1.1 | 90% | ❌ 12 pts to go |
| P02 | 464 | 82.1% | 82.1% | -1.8 | 90% | 🟡 8 pts to go |
| P03 | 262 | 85.9% | 85.9% | -1.9 | 90% | 🟡 4 pts to go |
| P04 | 3556 | 82.9% | 82.9% | -1.5 | 85% | 🟡 2 pts to go |
| P05 | 419 | 44.9% | 44.9% | +0.1 | 70% | ❌ 25 pts to go |
| P06M | 18956 | 37.9% | 37.9% | -5.7 | n/a | no target |
| P06T | 43465 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 253 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 660 | 99.8% | 99.8% | -0.1 | 100% | 🟡 0 pts to go |
| P08 | 21363 | 99.9% | 99.9% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 278 | 78.8% | 78.8% | -1.0 | 100% | ❌ 21 pts to go |
| P10 | 2137 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1596 | 97.6% | 97.6% | +0.3 | 100% | 🟡 2 pts to go |
| P12 | 16 | 56.2% | 56.2% | +2.9 | n/a | no target |
| P13 | 164579 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 18.9% | 18.9% | +3.4 | n/a | no target |
| P01T | 202 | 66.3% | 66.3% | +1.2 | n/a | no target |
| P01_GOLD | 624 | 43.1% | 43.1% | -0.4 | 70% | ❌ 27 pts to go |
| P02 | 464 | 47.2% | 47.2% | -1.5 | 75% | ❌ 28 pts to go |
| P03 | 262 | 44.7% | 44.7% | +1.4 | 75% | ❌ 30 pts to go |
| P04 | 3556 | 38.7% | 38.7% | +0.0 | 70% | ❌ 31 pts to go |
| P05 | 419 | 21.7% | 21.7% | -0.3 | 55% | ❌ 33 pts to go |
| P06M | 18956 | 5.9% | 5.9% | +1.1 | n/a | no target |
| P06T | 43465 | 65.1% | 65.1% | +3.0 | n/a | no target |
| P06 | 253 | 52.2% | 52.2% | +5.3 | n/a | no target |
| P07 | 660 | 51.7% | 51.7% | +1.7 | 70% | ❌ 18 pts to go |
| P08 | 21363 | 55.9% | 55.9% | +1.1 | 75% | ❌ 19 pts to go |
| P09 | 278 | 48.2% | 48.2% | -1.0 | 85% | ❌ 37 pts to go |
| P10 | 2137 | 44.3% | 44.3% | +0.7 | 80% | ❌ 36 pts to go |
| P11 | 1596 | 57.5% | 57.5% | +3.2 | 70% | ❌ 12 pts to go |
| P12 | 16 | 37.5% | 37.5% | -2.5 | n/a | no target |
| P13 | 164579 | 5.4% | 5.4% | +0.2 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 47.9% | 47.9% | -8.7 | n/a | no target |
| P01T | 202 | 96.0% | 96.0% | +1.2 | n/a | no target |
| P01_GOLD | 624 | 72.0% | 72.0% | -1.8 | 90% | ❌ 18 pts to go |
| P02 | 464 | 76.5% | 76.5% | -2.5 | 90% | ❌ 14 pts to go |
| P03 | 262 | 82.4% | 82.4% | -0.9 | 90% | 🟡 8 pts to go |
| P04 | 3556 | 77.7% | 77.7% | +1.3 | 85% | 🟡 7 pts to go |
| P05 | 419 | 43.0% | 43.0% | -0.1 | 75% | ❌ 32 pts to go |
| P06M | 18956 | 37.8% | 37.8% | -5.5 | n/a | no target |
| P06T | 43465 | 97.1% | 97.1% | +0.4 | n/a | no target |
| P06 | 253 | 92.1% | 92.1% | +1.6 | n/a | no target |
| P07 | 660 | 93.8% | 93.8% | +1.3 | 100% | 🟡 6 pts to go |
| P08 | 21363 | 92.8% | 92.8% | +2.0 | 100% | 🟡 7 pts to go |
| P09 | 278 | 66.9% | 66.9% | +0.8 | n/a | no target |
| P10 | 2137 | 89.9% | 89.9% | +3.1 | 100% | ❌ 10 pts to go |
| P11 | 1596 | 89.4% | 89.4% | +1.7 | n/a | no target |
| P12 | 16 | 56.2% | 56.2% | +9.5 | n/a | no target |
| P13 | 164579 | 68.6% | 68.6% | +3.4 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 46.3% | 46.3% | -0.2 | n/a | no target · QC vendors: 50 rows, 100.0% filled |
| P01T | 202 | 8.9% | 8.9% | -0.5 | n/a | no target · QC vendors: 7 rows, 42.9% filled |
| P01_GOLD | 624 | 42.9% | 42.9% | -0.9 | 95% | ❌ 52 pts to go · QC vendors: 49 rows, 98.0% filled |
| P02 | 464 | 56.2% | 56.2% | +0.6 | 95% | ❌ 39 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 262 | 42.0% | 42.0% | -4.0 | 95% | ❌ 53 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 3556 | 32.1% | 32.1% | -0.1 | 95% | ❌ 63 pts to go · QC vendors: 591 rows, 97.0% filled |
| P05 | 419 | 13.4% | 13.4% | -0.6 | n/a | no target · QC vendors: 35 rows, 91.4% filled |
| P06M | 18956 | 38.8% | 38.8% | -4.0 | n/a | no target · QC vendors: 5994 rows, 99.8% filled |
| P06T | 43465 | 4.3% | 4.3% | -1.0 | n/a | no target · QC vendors: 2180 rows, 62.3% filled |
| P06 | 253 | 7.9% | 7.9% | -0.5 | n/a | no target · QC vendors: 13 rows, 69.2% filled |
| P07 | 660 | 6.1% | 6.1% | -0.2 | n/a | no target · QC vendors: 35 rows, 71.4% filled |
| P08 | 21363 | 6.4% | 6.4% | -0.2 | n/a | no target · QC vendors: 1194 rows, 92.5% filled |
| P09 | 278 | 74.1% | 74.1% | -2.8 | 95% | ❌ 21 pts to go · QC vendors: 101 rows, 100.0% filled |
| P10 | 2137 | 15.3% | 15.3% | -0.3 | n/a | no target · QC vendors: 195 rows, 91.3% filled |
| P11 | 1596 | 13.2% | 13.2% | -1.6 | n/a | no target · QC vendors: 154 rows, 90.3% filled |
| P12 | 16 | 75.0% | 75.0% | +1.7 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 164579 | 23.5% | 23.5% | -2.7 | n/a | no target · QC vendors: 38676 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 57.4% | 57.4% | -1.5 | n/a | no target · vendors with a registry record: 109 rows, 100.0% filled |
| P01T | 202 | 55.0% | 55.0% | +4.0 | n/a | no target · vendors with a registry record: 111 rows, 100.0% filled |
| P01_GOLD | 624 | 80.6% | 80.6% | -0.9 | 100% | ❌ 19 pts to go · vendors with a registry record: 503 rows, 100.0% filled |
| P02 | 464 | 78.2% | 78.2% | +0.7 | 100% | ❌ 22 pts to go · vendors with a registry record: 363 rows, 100.0% filled |
| P03 | 262 | 77.9% | 77.9% | -3.1 | 100% | ❌ 22 pts to go · vendors with a registry record: 204 rows, 100.0% filled |
| P04 | 3556 | 53.7% | 53.7% | +4.0 | 100% | ❌ 46 pts to go · vendors with a registry record: 1911 rows, 100.0% filled |
| P05 | 419 | 63.2% | 63.2% | -0.1 | n/a | no target · vendors with a registry record: 265 rows, 100.0% filled |
| P06M | 18956 | 42.4% | 42.4% | -3.5 | n/a | no target · vendors with a registry record: 8037 rows, 100.0% filled |
| P06T | 43465 | 55.3% | 55.3% | -0.9 | n/a | no target · vendors with a registry record: 24026 rows, 100.0% filled |
| P06 | 253 | 41.5% | 41.5% | +0.1 | n/a | no target · vendors with a registry record: 105 rows, 100.0% filled |
| P07 | 660 | 32.7% | 32.7% | +0.4 | n/a | no target · vendors with a registry record: 216 rows, 100.0% filled |
| P08 | 21363 | 30.8% | 30.8% | +0.4 | n/a | no target · vendors with a registry record: 6580 rows, 100.0% filled |
| P09 | 278 | 89.9% | 89.9% | -0.7 | n/a | no target · vendors with a registry record: 250 rows, 100.0% filled |
| P10 | 2137 | 39.4% | 39.4% | +3.2 | n/a | no target · vendors with a registry record: 841 rows, 100.0% filled |
| P11 | 1596 | 57.0% | 57.0% | +3.4 | n/a | no target · vendors with a registry record: 909 rows, 100.0% filled |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 16 rows, 100.0% filled |
| P13 | 164579 | 41.0% | 41.0% | +14.1 | n/a | no target · vendors with a registry record: 67503 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 95.3% | 95.3% | +1.5 | 90% | ✅ met |
| P01T | 202 | 68.8% | 68.8% | -3.6 | 90% | ❌ 21 pts to go |
| P01_GOLD | 624 | 87.0% | 87.0% | -0.7 | 95% | 🟡 8 pts to go |
| P02 | 464 | 88.1% | 88.1% | +0.3 | 95% | 🟡 7 pts to go |
| P03 | 262 | 82.8% | 82.8% | -1.6 | 85% | 🟡 2 pts to go |
| P04 | 3556 | 63.7% | 63.7% | +0.7 | 90% | ❌ 26 pts to go |
| P05 | 419 | 77.6% | 77.6% | -1.5 | 75% | ✅ met |
| P06M | 18956 | 91.7% | 91.8% | +0.1 | n/a | no target |
| P06T | 43465 | 33.4% | 33.4% | -3.9 | n/a | no target |
| P06 | 253 | 73.9% | 73.9% | +0.3 | 80% | 🟡 6 pts to go |
| P07 | 660 | 59.5% | 59.7% | -0.3 | 80% | ❌ 20 pts to go |
| P08 | 21363 | 55.0% | 55.0% | +0.6 | 75% | ❌ 20 pts to go |
| P09 | 278 | 74.5% | 74.5% | -2.4 | 95% | ❌ 20 pts to go |
| P10 | 2137 | 45.7% | 45.7% | -1.0 | 70% | ❌ 24 pts to go |
| P11 | 1596 | 29.2% | 29.2% | -2.1 | 65% | ❌ 36 pts to go |
| P12 | 16 | 75.0% | 75.0% | -5.0 | 80% | 🟡 5 pts to go |
| P13 | 164579 | 35.6% | 35.7% | -11.9 | 60% | ❌ 24 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 18.9% | 18.9% | -1.3 | 50% | ❌ 31 pts to go |
| P01T | 202 | 16.8% | 16.8% | +0.7 | n/a | no target |
| P01_GOLD | 624 | 19.7% | 19.7% | +0.2 | 40% | ❌ 20 pts to go |
| P02 | 464 | 19.8% | 19.8% | +0.7 | 40% | ❌ 20 pts to go |
| P03 | 262 | 21.8% | 21.8% | +0.5 | 40% | ❌ 18 pts to go |
| P04 | 3556 | 15.4% | 15.4% | +0.2 | 40% | ❌ 25 pts to go |
| P05 | 419 | 20.5% | 20.5% | +3.0 | 25% | 🟡 4 pts to go |
| P06M | 18956 | 21.1% | 21.1% | +9.5 | n/a | no target |
| P06T | 43465 | 8.6% | 8.6% | +1.7 | n/a | no target |
| P06 | 253 | 21.7% | 21.7% | +8.9 | 35% | ❌ 13 pts to go |
| P07 | 660 | 22.0% | 22.0% | +7.9 | 35% | ❌ 13 pts to go |
| P08 | 21363 | 23.3% | 23.3% | +7.9 | 35% | ❌ 12 pts to go |
| P09 | 278 | 16.9% | 16.9% | +0.6 | n/a | no target |
| P10 | 2137 | 5.6% | 5.6% | -1.1 | 30% | ❌ 24 pts to go |
| P11 | 1596 | 6.2% | 6.2% | -1.2 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 164579 | 8.2% | 8.2% | -4.1 | 30% | ❌ 22 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 202 | 85.6% | 85.6% | +1.2 | 100% | ❌ 14 pts to go |
| P01_GOLD | 624 | 90.7% | 90.7% | +0.0 | 100% | 🟡 9 pts to go |
| P02 | 464 | 96.3% | 96.3% | +0.8 | 100% | 🟡 4 pts to go |
| P03 | 262 | 88.5% | 88.5% | -0.9 | 100% | ❌ 12 pts to go |
| P04 | 3556 | 72.3% | 72.3% | +0.9 | 100% | ❌ 28 pts to go |
| P05 | 419 | 90.2% | 90.2% | +0.9 | 100% | 🟡 10 pts to go |
| P06M | 18956 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06T | 43465 | 57.4% | 57.4% | -1.9 | n/a | no target |
| P06 | 253 | 81.8% | 81.8% | +3.0 | 95% | ❌ 13 pts to go |
| P07 | 660 | 82.3% | 82.3% | +1.1 | 95% | ❌ 13 pts to go |
| P08 | 21363 | 81.4% | 81.4% | +3.1 | 95% | ❌ 14 pts to go |
| P09 | 278 | 96.0% | 96.0% | -0.1 | 100% | 🟡 4 pts to go |
| P10 | 2137 | 54.3% | 54.3% | -0.1 | 95% | ❌ 41 pts to go |
| P11 | 1596 | 60.1% | 60.1% | +10.7 | 80% | ❌ 20 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164579 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 59.5% | 59.5% | -26.5 | n/a | no target |
| P01T | 202 | 70.3% | 70.3% | +2.1 | n/a | no target |
| P01_GOLD | 624 | 73.1% | 73.1% | +0.1 | 90% | ❌ 17 pts to go |
| P02 | 464 | 78.2% | 78.2% | +0.3 | 95% | ❌ 17 pts to go |
| P03 | 262 | 74.0% | 74.0% | -0.9 | 95% | ❌ 21 pts to go |
| P04 | 3556 | 69.0% | 69.0% | +0.1 | 95% | ❌ 26 pts to go |
| P05 | 419 | 72.1% | 72.1% | -1.4 | 90% | ❌ 18 pts to go |
| P06M | 18956 | 71.0% | 71.0% | -15.9 | n/a | no target |
| P06T | 43465 | 50.9% | 50.9% | -6.3 | n/a | no target |
| P06 | 253 | 70.4% | 70.4% | +1.9 | 95% | ❌ 25 pts to go |
| P07 | 660 | 66.2% | 66.2% | +1.4 | 90% | ❌ 24 pts to go |
| P08 | 21363 | 68.5% | 68.5% | +0.7 | 95% | ❌ 26 pts to go |
| P09 | 278 | 86.0% | 86.0% | -1.0 | 100% | ❌ 14 pts to go |
| P10 | 2137 | 53.4% | 53.4% | -1.9 | 95% | ❌ 42 pts to go |
| P11 | 1596 | 28.7% | 28.7% | -0.2 | 75% | ❌ 46 pts to go |
| P12 | 16 | 87.5% | 87.5% | -5.8 | n/a | no target |
| P13 | 164579 | 52.0% | 52.0% | -18.8 | 95% | ❌ 43 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 65.8% | 65.8% | -21.8 | n/a | no target |
| P01T | 202 | 84.2% | 84.2% | +0.9 | 95% | ❌ 11 pts to go |
| P01_GOLD | 624 | 84.6% | 84.6% | -0.2 | 90% | 🟡 5 pts to go |
| P02 | 464 | 90.3% | 90.3% | -0.3 | 95% | 🟡 5 pts to go |
| P03 | 262 | 83.2% | 83.2% | -2.4 | 95% | ❌ 12 pts to go |
| P04 | 3556 | 90.7% | 90.7% | +1.5 | 90% | ✅ met |
| P05 | 419 | 91.9% | 91.9% | -1.2 | 95% | 🟡 3 pts to go |
| P06M | 18956 | 75.8% | 75.8% | -17.4 | n/a | no target |
| P06T | 43465 | 69.4% | 69.4% | -5.5 | n/a | no target |
| P06 | 253 | 92.5% | 92.5% | +0.2 | 100% | 🟡 8 pts to go |
| P07 | 660 | 92.7% | 92.7% | +0.5 | 100% | 🟡 7 pts to go |
| P08 | 21363 | 94.0% | 94.0% | +1.7 | 100% | 🟡 6 pts to go |
| P09 | 278 | 73.4% | 73.4% | +0.4 | n/a | no target |
| P10 | 2137 | 93.0% | 93.0% | +1.7 | 100% | 🟡 7 pts to go |
| P11 | 1596 | 45.8% | 45.8% | +3.9 | 80% | ❌ 34 pts to go |
| P12 | 16 | 93.8% | 93.8% | -6.2 | n/a | no target |
| P13 | 164579 | 63.9% | 63.9% | -19.8 | 95% | ❌ 31 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 2.6% | 2.6% | -0.5 | n/a | no target |
| P01T | 202 | 8.9% | 8.9% | -0.5 | n/a | no target |
| P01_GOLD | 624 | 13.9% | 13.9% | -0.3 | 25% | ❌ 11 pts to go |
| P02 | 464 | 25.0% | 25.0% | -0.3 | 40% | ❌ 15 pts to go |
| P03 | 262 | 8.8% | 8.8% | -0.3 | 20% | ❌ 11 pts to go |
| P04 | 3556 | 3.7% | 3.7% | +0.2 | 20% | ❌ 16 pts to go |
| P05 | 419 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 18956 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 43465 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 253 | 5.5% | 5.5% | +0.4 | n/a | no target |
| P07 | 660 | 8.5% | 8.5% | +0.0 | n/a | no target |
| P08 | 21363 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 278 | 8.3% | 8.3% | +0.5 | n/a | no target |
| P10 | 2137 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1596 | 0.8% | 0.8% | -0.2 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 164579 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 14.7% | 14.7% | -3.9 | n/a | no target |
| P01T | 202 | 20.3% | 20.3% | -2.1 | 70% | ❌ 50 pts to go |
| P01_GOLD | 624 | 43.6% | 43.6% | +0.1 | 80% | ❌ 36 pts to go |
| P02 | 464 | 57.5% | 57.5% | +0.2 | 90% | ❌ 32 pts to go |
| P03 | 262 | 19.1% | 19.1% | +0.5 | 60% | ❌ 41 pts to go |
| P04 | 3556 | 21.3% | 21.3% | -0.3 | 85% | ❌ 64 pts to go |
| P05 | 419 | 11.7% | 11.7% | +0.1 | 50% | ❌ 38 pts to go |
| P06M | 18956 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06T | 43465 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 253 | 15.4% | 15.4% | +0.0 | n/a | no target |
| P07 | 660 | 10.0% | 10.0% | -0.5 | n/a | no target |
| P08 | 21363 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 278 | 74.8% | 74.8% | -3.1 | 95% | ❌ 20 pts to go |
| P10 | 2137 | 1.6% | 1.6% | -0.1 | n/a | no target |
| P11 | 1596 | 14.5% | 14.5% | -2.2 | n/a | no target |
| P12 | 16 | 31.2% | 31.2% | +4.5 | n/a | no target |
| P13 | 164579 | 0.3% | 0.3% | -0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 5.3% | 5.3% | -0.9 | n/a | no target |
| P01T | 202 | 9.4% | 9.4% | -1.0 | n/a | no target |
| P01_GOLD | 624 | 34.8% | 34.8% | +0.8 | 70% | ❌ 35 pts to go |
| P02 | 464 | 39.2% | 39.2% | +0.1 | 75% | ❌ 36 pts to go |
| P03 | 262 | 19.5% | 19.5% | +0.9 | 55% | ❌ 36 pts to go |
| P04 | 3556 | 21.3% | 21.3% | -0.3 | 75% | ❌ 54 pts to go |
| P05 | 419 | 10.7% | 10.7% | +0.0 | 50% | ❌ 39 pts to go |
| P06M | 18956 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 43465 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 253 | 6.3% | 6.3% | +0.4 | n/a | no target |
| P07 | 660 | 5.0% | 5.0% | -0.2 | n/a | no target |
| P08 | 21363 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 278 | 71.6% | 71.6% | -3.6 | 95% | ❌ 23 pts to go |
| P10 | 2137 | 0.8% | 0.8% | -0.1 | n/a | no target |
| P11 | 1596 | 14.1% | 14.1% | -2.3 | n/a | no target |
| P12 | 16 | 18.8% | 18.8% | -1.2 | n/a | no target |
| P13 | 164579 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 9.5% | 9.5% | +1.7 | n/a | no target |
| P01T | 202 | 8.4% | 8.4% | +0.1 | n/a | no target |
| P01_GOLD | 624 | 58.0% | 58.2% | +0.0 | 80% | ❌ 22 pts to go |
| P02 | 464 | 45.5% | 45.7% | -0.2 | 75% | ❌ 30 pts to go |
| P03 | 262 | 36.6% | 36.6% | -0.7 | 70% | ❌ 33 pts to go |
| P04 | 3556 | 21.2% | 21.7% | +0.1 | 70% | ❌ 49 pts to go |
| P05 | 419 | 14.6% | 14.6% | +0.4 | 50% | ❌ 35 pts to go |
| P06M | 18956 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P06T | 43465 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 253 | 15.4% | 15.4% | -1.1 | n/a | no target |
| P07 | 660 | 1.8% | 1.8% | -0.2 | n/a | no target |
| P08 | 21363 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 278 | 48.9% | 48.9% | +2.3 | 80% | ❌ 31 pts to go |
| P10 | 2137 | 1.1% | 1.2% | -0.1 | n/a | no target |
| P11 | 1596 | 5.5% | 5.5% | -1.3 | n/a | no target |
| P12 | 16 | 37.5% | 37.5% | -2.5 | n/a | no target |
| P13 | 164579 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 18.9% | 18.9% | +0.3 | n/a | no target |
| P01T | 202 | 21.3% | 21.3% | -0.1 | 60% | ❌ 39 pts to go |
| P01_GOLD | 624 | 63.0% | 63.0% | -0.4 | 70% | 🟡 7 pts to go |
| P02 | 464 | 39.0% | 39.0% | -0.7 | 50% | ❌ 11 pts to go |
| P03 | 262 | 47.3% | 47.3% | -1.0 | 55% | 🟡 8 pts to go |
| P04 | 3556 | 12.6% | 12.6% | +0.4 | 40% | ❌ 27 pts to go |
| P05 | 419 | 16.7% | 16.7% | -0.4 | 40% | ❌ 23 pts to go |
| P06M | 18956 | 3.3% | 3.3% | +1.1 | n/a | no target |
| P06T | 43465 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P06 | 253 | 20.9% | 20.9% | -1.1 | n/a | no target |
| P07 | 660 | 6.2% | 6.2% | -0.4 | n/a | no target |
| P08 | 21363 | 2.9% | 2.9% | +0.0 | n/a | no target |
| P09 | 278 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10 | 2137 | 5.1% | 5.1% | +0.5 | n/a | no target |
| P11 | 1596 | 4.4% | 4.4% | -0.8 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 164579 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 26.3% | 26.3% | +4.6 | n/a | no target |
| P01T | 202 | 30.2% | 30.2% | +1.6 | 65% | ❌ 35 pts to go |
| P01_GOLD | 624 | 68.8% | 68.8% | -0.2 | 70% | 🟡 1 pts to go |
| P02 | 464 | 23.7% | 23.7% | -0.5 | 50% | ❌ 26 pts to go |
| P03 | 262 | 50.8% | 50.8% | -1.7 | 60% | 🟡 9 pts to go |
| P04 | 3556 | 5.7% | 5.7% | +0.3 | 40% | ❌ 34 pts to go |
| P05 | 419 | 20.0% | 20.0% | +0.3 | 45% | ❌ 25 pts to go |
| P06M | 18956 | 2.0% | 2.0% | +0.6 | n/a | no target |
| P06T | 43465 | 0.8% | 0.8% | +0.1 | n/a | no target |
| P06 | 253 | 33.2% | 33.2% | -1.2 | n/a | no target |
| P07 | 660 | 6.7% | 6.7% | -0.2 | n/a | no target |
| P08 | 21363 | 1.3% | 1.3% | +0.0 | n/a | no target |
| P09 | 278 | 10.8% | 10.8% | +1.0 | n/a | no target |
| P10 | 2137 | 3.3% | 3.3% | +0.2 | n/a | no target |
| P11 | 1596 | 4.2% | 4.2% | -0.9 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 164579 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 15.3% | 15.3% | +2.9 | n/a | no target |
| P01T | 202 | 13.9% | 13.9% | +0.4 | n/a | no target |
| P01_GOLD | 624 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 464 | 38.1% | 38.1% | +0.8 | n/a | no target |
| P03 | 262 | 51.5% | 51.5% | -0.6 | 60% | 🟡 8 pts to go |
| P04 | 3556 | 12.6% | 12.6% | +0.7 | n/a | no target |
| P05 | 419 | 15.3% | 15.3% | +0.1 | n/a | no target |
| P06M | 18956 | 0.8% | 0.8% | +0.3 | n/a | no target |
| P06T | 43465 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 253 | 24.1% | 24.1% | -1.5 | n/a | no target |
| P07 | 660 | 7.9% | 7.9% | -0.4 | n/a | no target |
| P08 | 21363 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 278 | 20.9% | 20.9% | +3.3 | n/a | no target |
| P10 | 2137 | 2.5% | 2.5% | +0.1 | n/a | no target |
| P11 | 1596 | 3.3% | 3.3% | -1.4 | n/a | no target |
| P12 | 16 | 25.0% | 25.0% | +11.7 | n/a | no target |
| P13 | 164579 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 10.5% | 10.5% | -1.1 | 15% | 🟡 4 pts to go |
| P01T | 202 | 12.9% | 12.9% | +0.4 | 15% | 🟡 2 pts to go |
| P01_GOLD | 624 | 35.1% | 35.1% | -0.2 | 40% | 🟡 5 pts to go |
| P02 | 464 | 12.1% | 12.3% | -0.8 | 25% | ❌ 13 pts to go |
| P03 | 262 | 16.4% | 16.4% | -1.1 | 25% | 🟡 9 pts to go |
| P04 | 3556 | 2.8% | 2.8% | +0.1 | 15% | ❌ 12 pts to go |
| P05 | 419 | 6.7% | 6.7% | +0.1 | 15% | 🟡 8 pts to go |
| P06M | 18956 | 0.7% | 0.7% | -0.2 | 15% | ❌ 14 pts to go |
| P06T | 43465 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 253 | 11.1% | 11.1% | +0.5 | 15% | 🟡 4 pts to go |
| P07 | 660 | 4.1% | 4.1% | -0.2 | 15% | ❌ 11 pts to go |
| P08 | 21363 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 278 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P10 | 2137 | 1.3% | 1.3% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1596 | 1.3% | 1.3% | -0.2 | 15% | ❌ 14 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 164579 | 0.5% | 0.5% | -0.2 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 7.4% | 7.4% | +2.0 | 15% | 🟡 8 pts to go |
| P01T | 202 | 12.4% | 12.4% | +0.9 | 25% | ❌ 13 pts to go |
| P01_GOLD | 624 | 29.0% | 29.0% | -0.2 | 25% | ✅ met |
| P02 | 464 | 25.4% | 25.4% | +0.1 | 15% | ✅ met |
| P03 | 262 | 22.5% | 22.5% | +0.4 | 15% | ✅ met |
| P04 | 3556 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 419 | 11.5% | 11.5% | +0.4 | 15% | 🟡 4 pts to go |
| P06M | 18956 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P06T | 43465 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 253 | 9.1% | 9.1% | +0.7 | 15% | 🟡 6 pts to go |
| P07 | 660 | 2.4% | 2.4% | -0.5 | 15% | ❌ 13 pts to go |
| P08 | 21363 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 278 | 1.4% | 1.4% | +0.4 | 15% | ❌ 14 pts to go |
| P10 | 2137 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1596 | 2.1% | 2.1% | -0.6 | 15% | ❌ 13 pts to go |
| P12 | 16 | 18.8% | 18.8% | -1.2 | 15% | ✅ met |
| P13 | 164579 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 2.1% | 2.1% | -0.2 | 20% | ❌ 18 pts to go |
| P01T | 202 | 3.5% | 3.5% | -0.7 | 20% | ❌ 16 pts to go |
| P01_GOLD | 624 | 4.3% | 4.3% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 464 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 262 | 1.9% | 1.9% | +0.4 | 20% | ❌ 18 pts to go |
| P04 | 3556 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |
| P05 | 419 | 1.0% | 1.0% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 18956 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 253 | 1.6% | 1.6% | +0.1 | 20% | ❌ 18 pts to go |
| P07 | 660 | 0.5% | 0.5% | +0.1 | 20% | ❌ 20 pts to go |
| P08 | 21363 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P09 | 278 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2137 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1596 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 2.1% | 2.1% | +0.5 | 15% | ❌ 13 pts to go |
| P01T | 202 | 3.5% | 3.5% | +0.4 | 15% | ❌ 12 pts to go |
| P01_GOLD | 624 | 10.6% | 10.6% | +0.2 | 15% | 🟡 4 pts to go |
| P02 | 464 | 11.2% | 11.2% | -0.8 | 15% | 🟡 4 pts to go |
| P03 | 262 | 21.0% | 21.0% | +0.8 | 15% | ✅ met |
| P04 | 3556 | 2.3% | 2.3% | +0.0 | 15% | ❌ 13 pts to go |
| P05 | 419 | 2.9% | 2.9% | +0.1 | 15% | ❌ 12 pts to go |
| P06M | 18956 | 0.5% | 0.5% | +0.2 | 15% | ❌ 14 pts to go |
| P06T | 43465 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 253 | 4.7% | 4.7% | -0.4 | 15% | ❌ 10 pts to go |
| P07 | 660 | 1.7% | 1.7% | +0.1 | 15% | ❌ 13 pts to go |
| P08 | 21363 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 278 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2137 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1596 | 0.9% | 0.9% | -0.3 | 15% | ❌ 14 pts to go |
| P12 | 16 | 6.2% | 6.2% | -0.5 | 15% | 🟡 9 pts to go |
| P13 | 164579 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 15.8% | 15.8% | +1.8 | 20% | 🟡 4 pts to go |
| P01T | 202 | 14.4% | 14.4% | +0.3 | 40% | ❌ 26 pts to go |
| P01_GOLD | 624 | 46.2% | 46.2% | +0.0 | 40% | ✅ met |
| P02 | 464 | 43.8% | 43.8% | +0.9 | 20% | ✅ met |
| P03 | 262 | 48.1% | 48.1% | -0.9 | 35% | ✅ met |
| P04 | 3556 | 14.7% | 14.7% | +0.5 | 20% | 🟡 5 pts to go |
| P05 | 419 | 15.8% | 15.8% | +0.4 | 20% | 🟡 4 pts to go |
| P06M | 18956 | 1.1% | 1.1% | +0.3 | 20% | ❌ 19 pts to go |
| P06T | 43465 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 253 | 24.5% | 24.5% | -0.8 | 20% | ✅ met |
| P07 | 660 | 8.3% | 8.3% | -0.3 | 20% | ❌ 12 pts to go |
| P08 | 21363 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 278 | 20.9% | 20.9% | +2.7 | 20% | ✅ met |
| P10 | 2137 | 3.8% | 3.8% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 1596 | 3.6% | 3.6% | -1.2 | 20% | ❌ 16 pts to go |
| P12 | 16 | 18.8% | 18.8% | +12.1 | 20% | 🟡 1 pts to go |
| P13 | 164579 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 23.2% | 23.2% | -10.1 | n/a | no target |
| P01T | 202 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 72.3% | 72.3% | +2.8 | 95% | ❌ 23 pts to go |
| P02 | 464 | 65.7% | 65.7% | +2.8 | 95% | ❌ 29 pts to go |
| P03 | 262 | 57.6% | 57.6% | +4.4 | 90% | ❌ 32 pts to go |
| P04 | 3556 | 26.1% | 26.1% | +1.3 | 85% | ❌ 59 pts to go |
| P05 | 419 | 38.7% | 38.7% | +1.0 | 75% | ❌ 36 pts to go |
| P06M | 18956 | 30.6% | 30.6% | -5.5 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 89.6% | 89.6% | +1.3 | 100% | ❌ 10 pts to go |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 4.8% | 4.8% | -1.2 | 60% | ❌ 55 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 23.2% | 23.2% | -10.1 | n/a | no target |
| P01T | 202 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 74.0% | 74.0% | +1.2 | 100% | ❌ 26 pts to go |
| P02 | 464 | 67.9% | 67.9% | +1.6 | 100% | ❌ 32 pts to go |
| P03 | 262 | 60.3% | 60.3% | +1.4 | n/a | no target |
| P04 | 3556 | 26.5% | 26.5% | +1.0 | 95% | ❌ 68 pts to go |
| P05 | 419 | 34.1% | 34.1% | +0.7 | 80% | ❌ 46 pts to go |
| P06M | 18956 | 30.6% | 30.6% | -5.5 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 92.1% | 92.1% | +0.6 | 100% | 🟡 8 pts to go |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 4.9% | 4.9% | -1.5 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 84.2% | 84.2% | +4.4 | n/a | no target |
| P01T | 202 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 52.7% | 52.7% | +1.1 | 85% | ❌ 32 pts to go |
| P02 | 464 | 58.6% | 58.6% | +1.1 | 90% | ❌ 31 pts to go |
| P03 | 262 | 43.5% | 43.5% | +0.9 | 85% | ❌ 42 pts to go |
| P04 | 3556 | 28.4% | 28.4% | +0.5 | 90% | ❌ 62 pts to go |
| P05 | 419 | 32.9% | 32.9% | +0.2 | 75% | ❌ 42 pts to go |
| P06M | 18956 | 86.2% | 86.2% | -0.9 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 82.4% | 82.4% | -1.0 | 95% | ❌ 13 pts to go |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 4.2% | 4.2% | -1.2 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 83.2% | 83.2% | +4.9 | n/a | no target |
| P01T | 202 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 52.4% | 52.4% | +0.6 | 85% | ❌ 33 pts to go |
| P02 | 464 | 52.8% | 52.8% | +0.2 | 90% | ❌ 37 pts to go |
| P03 | 262 | 43.9% | 43.9% | +0.2 | 85% | ❌ 41 pts to go |
| P04 | 3556 | 24.2% | 24.2% | +0.4 | 90% | ❌ 66 pts to go |
| P05 | 419 | 43.0% | 43.0% | -0.4 | 75% | ❌ 32 pts to go |
| P06M | 18956 | 77.6% | 77.6% | -0.2 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 0.4% | 0.4% | +0.1 | 95% | ❌ 95 pts to go |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 3.3% | 3.3% | -1.2 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 93.7% | 93.7% | +3.8 | n/a | no target |
| P01T | 202 | 95.5% | 95.5% | +1.2 | n/a | no target |
| P01_GOLD | 624 | 85.6% | 85.7% | +0.3 | 100% | ❌ 14 pts to go |
| P02 | 464 | 77.4% | 77.4% | +1.0 | 100% | ❌ 23 pts to go |
| P03 | 262 | 92.0% | 92.0% | +0.7 | n/a | no target |
| P04 | 3556 | 50.3% | 50.3% | +1.5 | 95% | ❌ 45 pts to go |
| P05 | 419 | 77.1% | 77.1% | -0.4 | 95% | ❌ 18 pts to go |
| P06M | 18956 | 99.2% | 99.2% | +0.3 | n/a | no target |
| P06T | 43465 | 92.6% | 92.6% | +2.0 | n/a | no target |
| P06 | 253 | 22.5% | 22.5% | -0.6 | n/a | no target |
| P07 | 660 | 13.0% | 13.0% | -0.8 | n/a | no target |
| P08 | 21363 | 6.5% | 6.5% | -0.6 | n/a | no target |
| P09 | 278 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2137 | 70.7% | 70.7% | -0.3 | n/a | no target |
| P11 | 1596 | 71.2% | 71.2% | +3.1 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 99.6% | 99.6% | -0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 93.7% | 93.7% | +3.8 | n/a | no target |
| P01T | 202 | 95.5% | 95.5% | +1.2 | n/a | no target |
| P01_GOLD | 624 | 88.8% | 88.9% | +0.3 | 100% | ❌ 11 pts to go |
| P02 | 464 | 78.7% | 78.7% | +1.2 | 100% | ❌ 21 pts to go |
| P03 | 262 | 92.7% | 92.7% | +0.7 | n/a | no target |
| P04 | 3556 | 53.6% | 53.6% | +1.7 | 95% | ❌ 41 pts to go |
| P05 | 419 | 89.3% | 89.3% | -0.3 | 70% | ✅ met |
| P06M | 18956 | 99.2% | 99.2% | +0.3 | n/a | no target |
| P06T | 43465 | 92.6% | 92.6% | +2.0 | n/a | no target |
| P06 | 253 | 22.5% | 22.5% | -0.6 | n/a | no target |
| P07 | 660 | 13.0% | 13.0% | -0.8 | n/a | no target |
| P08 | 21363 | 6.5% | 6.5% | -0.6 | n/a | no target |
| P09 | 278 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2137 | 70.7% | 70.7% | -0.3 | n/a | no target |
| P11 | 1596 | 71.3% | 71.3% | +3.1 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 202 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 16.7% | 16.7% | -0.1 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 366 rows, 28.4% filled |
| P02 | 464 | 10.6% | 10.6% | -0.6 | n/a | no target · rows from a source that publishes bids: 295 rows, 16.6% filled |
| P03 | 262 | 13.4% | 13.4% | +0.5 | n/a | no target · rows from a source that publishes bids: 139 rows, 25.2% filled |
| P04 | 3556 | 1.7% | 1.7% | +0.2 | n/a | no target · rows from a source that publishes bids: 861 rows, 7.0% filled |
| P05 | 419 | 2.4% | 2.4% | -0.2 | n/a | no target · rows from a source that publishes bids: 51 rows, 19.6% filled |
| P06M | 18956 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43465 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 4.0% | 4.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 265 rows, 4.2% filled |
| P10 | 2137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1596 | 0.6% | 0.6% | -0.3 | n/a | no target · rows from a source that publishes bids: 75 rows, 13.3% filled |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 16 rows, 0.0% filled |
| P13 | 164579 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 202 | 0.0% | 98.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 53.8% | 82.5% | +0.6 | 90% | ❌ 36 pts to go |
| P02 | 464 | 53.0% | 86.9% | +0.6 | 90% | ❌ 37 pts to go |
| P03 | 262 | 45.4% | 79.8% | +0.9 | 90% | ❌ 45 pts to go |
| P04 | 3556 | 19.3% | 93.0% | +0.2 | 90% | ❌ 71 pts to go |
| P05 | 419 | 0.0% | 83.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 18956 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43465 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 2.9% | 4.7% | +0.6 | 90% | ❌ 87 pts to go |
| P10 | 2137 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1596 | 2.8% | 97.2% | -1.3 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 202 | 0.5% | 98.5% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 26.6% | 55.3% | +0.7 | 90% | ❌ 63 pts to go |
| P02 | 464 | 51.9% | 85.8% | +0.4 | n/a | no target |
| P03 | 262 | 25.2% | 59.5% | +0.9 | n/a | no target |
| P04 | 3556 | 21.0% | 94.8% | +0.0 | n/a | no target |
| P05 | 419 | 0.5% | 83.8% | +0.0 | n/a | no target |
| P06M | 18956 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43465 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 40.6% | 42.4% | -0.4 | n/a | no target |
| P10 | 2137 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1596 | 2.8% | 97.2% | -0.9 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 202 | 2.0% | 100.0% | -0.1 | n/a | no target |
| P01_GOLD | 624 | 52.6% | 81.2% | +0.8 | 95% | ❌ 42 pts to go |
| P02 | 464 | 57.5% | 91.4% | +1.1 | n/a | no target |
| P03 | 262 | 49.6% | 84.0% | +2.8 | n/a | no target |
| P04 | 3556 | 21.8% | 95.6% | +0.6 | n/a | no target |
| P05 | 419 | 4.8% | 88.1% | +0.3 | n/a | no target |
| P06M | 18956 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43465 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 253 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 660 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21363 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 61.2% | 62.9% | -1.3 | n/a | no target |
| P10 | 2137 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1596 | 2.9% | 97.4% | -1.2 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164579 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 202 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 262 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3556 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 419 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 18956 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 43465 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 253 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 660 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 21363 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2137 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1596 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164579 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 202 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 262 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3556 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 419 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 18956 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 43465 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 253 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 660 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 21363 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2137 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1596 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164579 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 190 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 202 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 262 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3556 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 419 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 18956 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 43465 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 253 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 660 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 21363 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2137 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1596 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164579 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

