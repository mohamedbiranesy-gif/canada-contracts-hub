# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **94 of 446 met** (21.1%); 62 within 10 points; 290 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 53, P01T 203, P01_GOLD 626, P02 404, P03 212, P04 1639, P05 417, P06M 4248, P06T 19524, P06 342, P07 737, P08 21048, P09 312, P10R 25308, P10 3417, P11 3312, P12 7, P13 10552

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 20.8% | 8 | PO rule (45 rows) |
| P01T | 203 | 0.5% | 22.2% | 6 | reference to quote (PO / contract / vendor id) (195 rows) |
| P01_GOLD | 626 | 24.3% | 71.1% | 10 | payment terms (215 rows) |
| P02 | 404 | 8.9% | 62.6% | 9 | PO rule (299 rows) |
| P03 | 212 | 17.5% | 68.9% | 9 | PO rule (95 rows) |
| P04 | 1639 | 2.8% | 36.8% | 8 | PO rule (1484 rows) |
| P05 | 417 | 1.2% | 17.3% | 7 | payment terms (347 rows) |
| P06M | 4248 | 0.0% | 1.3% | 8 | PO rule (4239 rows) |
| P06T | 19524 | 0.0% | 0.7% | 5 | reference to quote (PO / contract / vendor id) (19459 rows) |
| P06 | 342 | 0.0% | 5.6% | 5 | reference to quote (PO / contract / vendor id) (342 rows) |
| P07 | 737 | 0.0% | 1.9% | 5 | reference to quote (PO / contract / vendor id) (737 rows) |
| P08 | 21048 | 0.0% | 0.1% | 4 | reference to quote (PO / contract / vendor id) (21048 rows) |
| P09 | 312 | 1.3% | 43.6% | 8 | payment terms (291 rows) |
| P10R | 25308 | 0.0% | 0.0% | 6 | vendor GST/HST number (25308 rows) |
| P10 | 3417 | 0.0% | 0.7% | 5 | reference to quote (PO / contract / vendor id) (3414 rows) |
| P11 | 3312 | 0.2% | 1.7% | 6 | PO rule (3280 rows) |
| P12 | 7 | 0.0% | 57.1% | 9 | PO rule (7 rows) |
| P13 | 10552 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (10552 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 53 | 6 | 1 | 46 | 0 | 0 | 73 |
| P01T | 203 | 28 | 44 | 131 | 0 | 0 | 73 |
| P01_GOLD | 626 | 231 | 186 | 209 | 0 | 0 | 82 |
| P02 | 404 | 0 | 183 | 221 | 0 | 0 | 66 |
| P03 | 212 | 0 | 0 | 205 | 7 | 0 | 57 |
| P04 | 1639 | 0 | 0 | 1581 | 58 | 0 | 53 |
| P05 | 417 | 14 | 28 | 351 | 24 | 0 | 51 |
| P06M | 4248 | 0 | 2 | 4232 | 14 | 0 | 51 |
| P06T | 19524 | 0 | 28 | 16293 | 3203 | 0 | 43 |
| P06 | 342 | 21 | 34 | 287 | 0 | 0 | 66 |
| P07 | 737 | 0 | 17 | 678 | 42 | 0 | 48 |
| P08 | 21048 | 0 | 0 | 15856 | 5192 | 0 | 38 |
| P09 | 312 | 4 | 12 | 293 | 3 | 0 | 53 |
| P10R | 25308 | 0 | 7 | 20524 | 4777 | 0 | 43 |
| P10 | 3417 | 3 | 14 | 2390 | 1010 | 0 | 43 |
| P11 | 3312 | 0 | 0 | 0 | 0 | 3312 | 23 |
| P12 | 7 | 0 | 1 | 6 | 0 | 0 | 51 |
| P13 | 10552 | 2 | 8 | 9486 | 1056 | 0 | 51 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 53 | 38 | 71.7% | the buyer's PO / reference rule (9) |
| P01T | 203 | 59 | 29.1% | the buyer's PO / reference rule (68) |
| P01_GOLD | 626 | 464 | 74.1% | bill-to legal name and address (109) |
| P02 | 404 | 305 | 75.5% | the buyer's PO / reference rule (54) |
| P03 | 212 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (212) |
| P04 | 1639 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (1639) |
| P05 | 417 | 45 | 10.8% | a confirmed invoicing / AP or finance channel (331) |
| P06M | 4248 | 31 | 0.7% | a confirmed invoicing / AP or finance channel (4188) |
| P06T | 19524 | 24 | 0.1% | a confirmed invoicing / AP or finance channel (19118) |
| P06 | 342 | 33 | 9.6% | bill-to legal name and address (212) |
| P07 | 737 | 8 | 1.1% | bill-to legal name and address (404) |
| P08 | 21048 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (21048) |
| P09 | 312 | 41 | 13.1% | a confirmed invoicing / AP or finance channel (262) |
| P10R | 25308 | 267 | 1.1% | a confirmed invoicing / AP or finance channel (24747) |
| P10 | 3417 | 9 | 0.3% | a confirmed invoicing / AP or finance channel (3268) |
| P11 | 3312 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3312) |
| P12 | 7 | 2 | 28.6% | a confirmed invoicing / AP or finance channel (5) |
| P13 | 10552 | 3 | 0.0% | a confirmed invoicing / AP or finance channel (10282) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 53 | 6 | 11.3% | 8 | 0 | the vendor's GST/HST number (BN9) (37) |
| P01T | 203 | 42 | 20.7% | 20 | 0 | the vendor's GST/HST number (BN9) (90) |
| P01_GOLD | 626 | 409 | 65.3% | 21 | 0 | the vendor's GST/HST number (BN9) (124) |
| P02 | 404 | 219 | 54.2% | 35 | 0 | the vendor's GST/HST number (BN9) (130) |
| P03 | 212 | 17 | 8.0% | 1 | 131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (52) |
| P04 | 1639 | 43 | 2.6% | 10 | 724 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (824) |
| P05 | 417 | 23 | 5.5% | 9 | 102 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (221) |
| P06M | 4248 | 1 | 0.0% | 14 | 80 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4098) |
| P06T | 19524 | 17 | 0.1% | 62 | 1949 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (17087) |
| P06 | 342 | 14 | 4.1% | 19 | 0 | the vendor's GST/HST number (BN9) (189) |
| P07 | 737 | 7 | 0.9% | 32 | 17 | the vendor's GST/HST number (BN9) (352) |
| P08 | 21048 | 1 | 0.0% | 3 | 1005 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (20010) |
| P09 | 312 | 39 | 12.5% | 1 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (128) |
| P10R | 25308 | 444 | 1.8% | 0 | 17024 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7667) |
| P10 | 3417 | 6 | 0.2% | 23 | 464 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2782) |
| P11 | 3312 | 5 | 0.2% | 0 | 0 | a confirmed invoicing / AP or finance channel (3296) |
| P12 | 7 | 2 | 28.6% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2) |
| P13 | 10552 | 3 | 0.0% | 206 | 7146 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3097) |
| **all** | 92361 | 1298 | 1.4% | 464 | 28770 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 47 | 0 | 0 | 0 | 5 | 5 | 0 | 45 | 46 | 1 |
| P01T | 175 | 0 | 0 | 0 | 33 | 63 | 10 | 130 | 142 | 30 |
| P01_GOLD | 395 | 0 | 0 | 0 | 11 | 94 | 34 | 193 | 228 | 60 |
| P02 | 404 | 0 | 404 | 0 | 5 | 39 | 8 | 299 | 228 | 22 |
| P03 | 212 | 0 | 212 | 0 | 5 | 37 | 11 | 95 | 97 | 25 |
| P04 | 1639 | 0 | 1639 | 0 | 80 | 376 | 103 | 1484 | 1279 | 111 |
| P05 | 403 | 0 | 351 | 0 | 58 | 133 | 52 | 338 | 349 | 58 |
| P06M | 4248 | 0 | 4248 | 0 | 227 | 371 | 43 | 4239 | 4227 | 3 |
| P06T | 19524 | 0 | 19524 | 0 | 8372 | 13327 | 3721 | 19397 | 19177 | 172 |
| P06 | 321 | 0 | 0 | 0 | 105 | 199 | 74 | 251 | 290 | 9 |
| P07 | 737 | 0 | 737 | 0 | 352 | 498 | 148 | 681 | 693 | 17 |
| P08 | 21048 | 0 | 21048 | 0 | 14057 | 17249 | 5565 | 20971 | 20865 | 219 |
| P09 | 308 | 0 | 288 | 0 | 9 | 69 | 4 | 282 | 294 | 45 |
| P10R | 25308 | 0 | 25232 | 0 | 450 | 15046 | 6283 | 25282 | 25235 | 22 |
| P10 | 3414 | 0 | 3356 | 0 | 1192 | 2512 | 1197 | 3368 | 3321 | 136 |
| P11 | 3312 | 3312 | 3259 | 0 | 1965 | 3161 | 857 | 3280 | 3250 | 32 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 6 | 0 |
| P13 | 10550 | 0 | 10462 | 0 | 314 | 3164 | 1521 | 10523 | 10530 | 25 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_logo_url | P08 | 33.4% | 100% | 14012 |
| buyer_phone | P08 | 28.5% | 95% | 13997 |
| vendor_registered_address | P08 | 9.7% | 70% | 12701 |
| buyer_legal_name_as_published | P08 | 18.0% | 75% | 11987 |
| vendor_logo_url | P08 | 46.1% | 100% | 11335 |
| vendor_phone | P08 | 33.6% | 85% | 10818 |
| vendor_bn9 | P08 | 8.3% | 50% | 8770 |
| vendor_emails | P08 | 34.2% | 75% | 8592 |
| vendor_trading_name | P08 | 18.0% | 50% | 6728 |
| buyer_bn_as_published | P08 | 7.6% | 35% | 5760 |
| invoice_reference_hint | P08 | 0.4% | 25% | 5185 |
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 5058 |
| ap_system_hint | P10R | 0.4% | 20% | 4958 |
| buyer_address | P08 | 73.5% | 95% | 4519 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 4205 |
| ap_system_hint | P08 | 0.5% | 20% | 4114 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 3898 |
| buyer_tax_exempt_status | P10R | 0.1% | 15% | 3781 |
| buyer_esignature_preference | P10R | 0.1% | 15% | 3781 |
| ap_system_hint | P06T | 1.0% | 20% | 3708 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 3654 |
| buyer_esignature_preference | P08 | 0.1% | 15% | 3132 |
| buyer_payment_method_preference | P08 | 0.1% | 15% | 3127 |
| buyer_tax_exempt_status | P08 | 0.2% | 15% | 3124 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 2890 |
| buyer_tax_exempt_status | P06T | 0.4% | 15% | 2855 |
| buyer_payment_method_preference | P06T | 0.4% | 15% | 2842 |
| buyer_logo_url | P11 | 10.5% | 80% | 2302 |
| buyer_phone | P11 | 7.9% | 75% | 2223 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 2109 |
| buyer_phone | P13 | 75.1% | 95% | 2099 |
| vendor_phone | P11 | 12.5% | 75% | 2070 |
| buyer_logo_url | P13 | 75.4% | 95% | 2064 |
| ap_system_hint | P13 | 0.9% | 20% | 2019 |
| buyer_legal_name_as_published | P11 | 4.6% | 65% | 2002 |
| vendor_emails | P11 | 10.7% | 70% | 1963 |
| contract_value | P11 | 2.6% | 60% | 1901 |
| award_or_notice_id | P11 | 2.7% | 60% | 1899 |
| commodity_codes | P11 | 1.8% | 50% | 1595 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 1575 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 79.2% | 79.2% | +34.8 | 50% | ✅ met |
| P01T | 203 | 37.9% | 37.9% | -33.8 | 50% | ❌ 12 pts to go |
| P01_GOLD | 626 | 92.3% | 94.6% | -0.2 | 95% | 🟡 3 pts to go |
| P02 | 404 | 83.9% | 85.6% | +0.0 | 95% | ❌ 11 pts to go |
| P03 | 212 | 91.5% | 95.8% | -1.3 | 95% | 🟡 4 pts to go |
| P04 | 1639 | 66.0% | 68.9% | -2.6 | 90% | ❌ 24 pts to go |
| P05 | 417 | 38.1% | 40.8% | -3.0 | 70% | ❌ 32 pts to go |
| P06M | 4248 | 94.1% | 94.1% | +87.0 | n/a | no target |
| P06T | 19524 | 1.0% | 1.0% | -3.4 | n/a | no target |
| P06 | 342 | 26.6% | 26.6% | -21.6 | 30% | 🟡 3 pts to go |
| P07 | 737 | 7.6% | 7.6% | -16.2 | 30% | ❌ 22 pts to go |
| P08 | 21048 | 0.4% | 0.4% | -2.0 | 25% | ❌ 25 pts to go |
| P09 | 312 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 25308 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 3417 | 1.5% | 2.0% | -0.7 | 25% | ❌ 24 pts to go |
| P11 | 3312 | 19.5% | 20.0% | -4.6 | 60% | ❌ 40 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10552 | 0.3% | 0.3% | +0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 626 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 404 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 212 | 1.9% | 1.9% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 1639 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 417 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P06M | 4248 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 0.6% | 0.6% | +0.1 | 50% | ❌ 49 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P11 | 3312 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 66.0% | 66.0% | +66.0 | n/a | no target |
| P01T | 203 | 3.9% | 3.9% | -1.5 | 50% | ❌ 46 pts to go |
| P01_GOLD | 626 | 67.6% | 67.6% | +0.0 | 85% | ❌ 17 pts to go |
| P02 | 404 | 75.5% | 75.5% | +0.0 | 90% | ❌ 14 pts to go |
| P03 | 212 | 74.5% | 74.5% | -1.0 | 85% | ❌ 10 pts to go |
| P04 | 1639 | 63.0% | 63.0% | -2.5 | 85% | ❌ 22 pts to go |
| P05 | 417 | 29.0% | 29.0% | -2.0 | 60% | ❌ 31 pts to go |
| P06M | 4248 | 94.0% | 94.0% | +94.0 | n/a | no target |
| P06T | 19524 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 96.2% | 96.2% | -0.4 | 100% | 🟡 4 pts to go |
| P10R | 25308 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 18.9% | 18.9% | -1.1 | 60% | ❌ 41 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 2.0% | 2.0% | -0.2 | 30% | ❌ 28 pts to go |
| P01_GOLD | 626 | 51.3% | 51.3% | +0.0 | 80% | ❌ 29 pts to go |
| P02 | 404 | 66.6% | 66.6% | -0.2 | 60% | ✅ met |
| P03 | 212 | 62.7% | 62.7% | -1.2 | 80% | ❌ 17 pts to go |
| P04 | 1639 | 52.3% | 52.3% | -2.2 | 50% | ✅ met |
| P05 | 417 | 12.2% | 12.2% | -1.1 | 40% | ❌ 28 pts to go |
| P06M | 4248 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19524 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 84.0% | 84.0% | -2.1 | 50% | ✅ met |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 2.5% | 2.5% | -15.0 | 40% | ❌ 38 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 3.0% | 3.0% | -0.3 | n/a | no target |
| P01_GOLD | 626 | 61.0% | 61.0% | -0.1 | 85% | ❌ 24 pts to go |
| P02 | 404 | 65.6% | 65.6% | -0.2 | 90% | ❌ 24 pts to go |
| P03 | 212 | 73.1% | 73.1% | -1.4 | 85% | ❌ 12 pts to go |
| P04 | 1639 | 54.1% | 54.1% | -2.2 | 85% | ❌ 31 pts to go |
| P05 | 417 | 19.9% | 19.9% | -1.2 | 50% | ❌ 30 pts to go |
| P06M | 4248 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19524 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 2.7% | 2.7% | -16.3 | 60% | ❌ 57 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 1.0% | 1.0% | -1.2 | n/a | no target |
| P01_GOLD | 626 | 12.9% | 12.9% | -0.1 | 60% | ❌ 47 pts to go |
| P02 | 404 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 212 | 10.4% | 10.4% | -0.2 | 50% | ❌ 40 pts to go |
| P04 | 1639 | 4.1% | 4.1% | -0.2 | 40% | ❌ 36 pts to go |
| P05 | 417 | 1.2% | 1.2% | -0.1 | 20% | ❌ 19 pts to go |
| P06M | 4248 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19524 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 2.6% | 2.6% | +0.0 | 50% | ❌ 47 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 0.4% | 0.4% | -2.6 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 1.5% | 1.5% | +1.5 | n/a | no target |
| P01_GOLD | 626 | 35.0% | 35.0% | -0.1 | 80% | ❌ 45 pts to go |
| P02 | 404 | 60.6% | 60.6% | +0.0 | 90% | ❌ 29 pts to go |
| P03 | 212 | 40.6% | 40.6% | -0.7 | 80% | ❌ 39 pts to go |
| P04 | 1639 | 49.2% | 49.2% | -2.1 | 85% | ❌ 36 pts to go |
| P05 | 417 | 5.5% | 5.5% | -0.5 | 50% | ❌ 44 pts to go |
| P06M | 4248 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19524 | 0.2% | 0.2% | +0.2 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 75.6% | 75.6% | -0.3 | 95% | ❌ 19 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 1.8% | 1.8% | -11.3 | 50% | ❌ 48 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | -0.6 | n/a | no target |
| P01_GOLD | 626 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 404 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 212 | 2.4% | 2.4% | +0.0 | 30% | ❌ 28 pts to go |
| P04 | 1639 | 1.0% | 1.0% | -0.1 | 30% | ❌ 29 pts to go |
| P05 | 417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 4248 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 212 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1639 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 417 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 4248 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 19524 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 342 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 737 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21048 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 25308 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 3417 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3312 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 30.2% | 30.2% | -69.8 | 70% | ❌ 40 pts to go |
| P01T | 203 | 39.9% | 39.9% | -40.5 | 60% | ❌ 20 pts to go |
| P01_GOLD | 626 | 77.8% | 77.8% | -0.1 | 90% | ❌ 12 pts to go |
| P02 | 404 | 67.3% | 67.3% | +0.0 | 85% | ❌ 18 pts to go |
| P03 | 212 | 81.6% | 81.6% | -0.6 | 90% | 🟡 8 pts to go |
| P04 | 1639 | 54.4% | 54.4% | -1.0 | 75% | ❌ 21 pts to go |
| P05 | 417 | 51.8% | 51.8% | -0.8 | 50% | ✅ met |
| P06M | 4248 | 2.8% | 2.8% | -71.6 | n/a | no target |
| P06T | 19524 | 12.8% | 12.8% | -47.9 | n/a | no target |
| P06 | 342 | 19.6% | 19.6% | -24.4 | 40% | ❌ 20 pts to go |
| P07 | 737 | 14.1% | 14.1% | -24.0 | 50% | ❌ 36 pts to go |
| P08 | 21048 | 8.3% | 8.3% | -31.9 | 50% | ❌ 42 pts to go |
| P09 | 312 | 57.7% | 57.7% | +3.4 | 80% | ❌ 22 pts to go |
| P10R | 25308 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 3417 | 28.0% | 28.0% | -8.6 | 40% | ❌ 12 pts to go |
| P11 | 3312 | 76.5% | 76.5% | +31.8 | 60% | ✅ met |
| P12 | 7 | 71.4% | 71.4% | +18.8 | 85% | ❌ 14 pts to go |
| P13 | 10552 | 88.9% | 88.9% | -2.8 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 69.8% | 69.8% | +8.7 | n/a | no target |
| P01T | 203 | 38.4% | 38.4% | -24.6 | n/a | no target |
| P01_GOLD | 626 | 74.9% | 74.9% | +0.1 | 95% | ❌ 20 pts to go |
| P02 | 404 | 84.9% | 84.9% | +0.0 | 95% | ❌ 10 pts to go |
| P03 | 212 | 77.4% | 77.4% | -0.5 | 95% | ❌ 18 pts to go |
| P04 | 1639 | 79.1% | 79.1% | -1.6 | 95% | ❌ 16 pts to go |
| P05 | 417 | 55.4% | 55.4% | -0.8 | 70% | ❌ 15 pts to go |
| P06M | 4248 | 55.8% | 55.8% | +35.0 | n/a | no target |
| P06T | 19524 | 28.3% | 28.3% | -49.9 | n/a | no target |
| P06 | 342 | 24.0% | 24.0% | -31.4 | 80% | ❌ 56 pts to go |
| P07 | 737 | 18.5% | 18.5% | -33.5 | 70% | ❌ 52 pts to go |
| P08 | 21048 | 9.7% | 9.7% | -42.7 | 70% | ❌ 60 pts to go |
| P09 | 312 | 87.8% | 87.8% | -0.7 | 100% | ❌ 12 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 31.1% | 31.1% | -11.3 | 70% | ❌ 39 pts to go |
| P11 | 3312 | 63.0% | 63.0% | +7.7 | 75% | ❌ 12 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 20.8% | 20.8% | -29.2 | n/a | no target |
| P01T | 203 | 24.1% | 24.1% | +4.5 | n/a | no target |
| P01_GOLD | 626 | 52.4% | 52.4% | +0.0 | 60% | 🟡 8 pts to go |
| P02 | 404 | 67.1% | 67.1% | -0.2 | 60% | ✅ met |
| P03 | 212 | 63.7% | 63.7% | -1.2 | 60% | ✅ met |
| P04 | 1639 | 54.2% | 54.2% | -1.3 | 55% | 🟡 1 pts to go |
| P05 | 417 | 25.7% | 25.7% | +0.4 | 50% | ❌ 24 pts to go |
| P06M | 4248 | 1.3% | 1.3% | -16.0 | n/a | no target |
| P06T | 19524 | 28.7% | 28.7% | -24.9 | n/a | no target |
| P06 | 342 | 29.8% | 29.8% | -23.2 | n/a | no target |
| P07 | 737 | 25.8% | 25.8% | -20.2 | 55% | ❌ 29 pts to go |
| P08 | 21048 | 18.0% | 18.0% | -29.5 | 50% | ❌ 32 pts to go |
| P09 | 312 | 71.8% | 71.8% | +0.4 | 70% | ✅ met |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 41.4% | 41.4% | -10.5 | 55% | ❌ 14 pts to go |
| P11 | 3312 | 62.6% | 62.6% | +19.6 | 50% | ✅ met |
| P12 | 7 | 85.7% | 85.7% | +1.5 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 24.5% | 24.5% | -36.6 | n/a | no target |
| P01T | 203 | 41.4% | 41.4% | +11.0 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | +0.0 | 70% | ❌ 18 pts to go |
| P02 | 404 | 57.2% | 57.2% | +0.0 | 70% | ❌ 13 pts to go |
| P03 | 212 | 57.1% | 57.1% | -0.1 | 70% | ❌ 13 pts to go |
| P04 | 1639 | 51.4% | 51.4% | -0.6 | 65% | ❌ 14 pts to go |
| P05 | 417 | 34.8% | 34.8% | +0.2 | 60% | ❌ 25 pts to go |
| P06M | 4248 | 2.1% | 2.1% | -28.3 | n/a | no target |
| P06T | 19524 | 25.1% | 25.1% | +21.6 | n/a | no target |
| P06 | 342 | 43.6% | 43.6% | -16.0 | 40% | ✅ met |
| P07 | 737 | 43.0% | 43.0% | -24.9 | 85% | ❌ 42 pts to go |
| P08 | 21048 | 33.6% | 33.6% | -34.5 | 85% | ❌ 51 pts to go |
| P09 | 312 | 52.9% | 52.9% | -2.5 | 85% | ❌ 32 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 54.3% | 54.3% | -12.0 | 85% | ❌ 31 pts to go |
| P11 | 3312 | 12.5% | 12.5% | -42.4 | 75% | ❌ 62 pts to go |
| P12 | 7 | 14.3% | 14.3% | -1.5 | n/a | no target |
| P13 | 10552 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 32.1% | 32.1% | -62.3 | n/a | no target |
| P01T | 203 | 95.6% | 95.6% | +5.4 | n/a | no target |
| P01_GOLD | 626 | 89.5% | 89.5% | +0.1 | 90% | 🟡 0 pts to go |
| P02 | 404 | 87.9% | 87.9% | +0.3 | 90% | 🟡 2 pts to go |
| P03 | 212 | 89.2% | 89.2% | -0.7 | 90% | 🟡 1 pts to go |
| P04 | 1639 | 80.1% | 80.1% | -1.2 | 85% | 🟡 5 pts to go |
| P05 | 417 | 52.0% | 52.0% | +1.0 | 70% | ❌ 18 pts to go |
| P06M | 4248 | 4.6% | 4.6% | -63.3 | n/a | no target |
| P06T | 19524 | 95.9% | 95.9% | +18.0 | n/a | no target |
| P06 | 342 | 98.5% | 98.5% | +1.5 | 50% | ✅ met |
| P07 | 737 | 99.2% | 99.2% | +2.4 | 100% | 🟡 1 pts to go |
| P08 | 21048 | 99.4% | 99.4% | +3.3 | 100% | 🟡 1 pts to go |
| P09 | 312 | 79.8% | 79.8% | +0.0 | 100% | ❌ 20 pts to go |
| P10R | 25308 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 3417 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3312 | 99.0% | 99.0% | +6.0 | 100% | 🟡 1 pts to go |
| P12 | 7 | 28.6% | 28.6% | -13.5 | n/a | no target |
| P13 | 10552 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 20.8% | 20.8% | -29.2 | n/a | no target |
| P01T | 203 | 44.3% | 44.3% | -1.4 | n/a | no target |
| P01_GOLD | 626 | 45.7% | 45.7% | +0.0 | 70% | ❌ 24 pts to go |
| P02 | 404 | 51.7% | 51.7% | +0.2 | 75% | ❌ 23 pts to go |
| P03 | 212 | 51.4% | 51.4% | +0.0 | 75% | ❌ 24 pts to go |
| P04 | 1639 | 41.5% | 41.5% | -1.4 | 70% | ❌ 28 pts to go |
| P05 | 417 | 24.9% | 24.9% | +0.4 | 55% | ❌ 30 pts to go |
| P06M | 4248 | 1.2% | 1.2% | -14.9 | n/a | no target |
| P06T | 19524 | 20.1% | 20.1% | +17.2 | n/a | no target |
| P06 | 342 | 34.2% | 34.2% | -6.8 | n/a | no target |
| P07 | 737 | 34.7% | 34.7% | -2.2 | 70% | ❌ 35 pts to go |
| P08 | 21048 | 34.2% | 34.2% | -14.5 | 75% | ❌ 41 pts to go |
| P09 | 312 | 50.0% | 50.0% | -2.0 | 85% | ❌ 35 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 41.8% | 41.8% | -9.5 | 80% | ❌ 38 pts to go |
| P11 | 3312 | 10.7% | 10.7% | -29.8 | 70% | ❌ 59 pts to go |
| P12 | 7 | 28.6% | 28.6% | -3.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 30.2% | 30.2% | -64.2 | n/a | no target |
| P01T | 203 | 75.4% | 75.4% | -13.7 | n/a | no target |
| P01_GOLD | 626 | 79.9% | 79.9% | +0.1 | 90% | ❌ 10 pts to go |
| P02 | 404 | 77.5% | 77.5% | +0.3 | 90% | ❌ 12 pts to go |
| P03 | 212 | 81.1% | 81.1% | -0.6 | 90% | 🟡 9 pts to go |
| P04 | 1639 | 70.0% | 70.0% | -0.9 | 85% | ❌ 15 pts to go |
| P05 | 417 | 49.4% | 49.4% | +1.0 | 75% | ❌ 26 pts to go |
| P06M | 4248 | 3.6% | 3.6% | -64.3 | n/a | no target |
| P06T | 19524 | 43.2% | 43.2% | -33.9 | n/a | no target |
| P06 | 342 | 63.2% | 63.2% | -25.4 | n/a | no target |
| P07 | 737 | 58.5% | 58.5% | -32.0 | 100% | ❌ 42 pts to go |
| P08 | 21048 | 46.1% | 46.1% | -42.9 | 100% | ❌ 54 pts to go |
| P09 | 312 | 61.2% | 61.2% | -1.3 | n/a | no target |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 72.9% | 72.9% | -16.1 | 100% | ❌ 27 pts to go |
| P11 | 3312 | 70.4% | 70.4% | -4.1 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -8.2 | n/a | no target |
| P13 | 10552 | 75.3% | 75.3% | -7.4 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 41.5% | 41.5% | +41.5 | n/a | no target · QC vendors: 22 rows, 100.0% filled |
| P01T | 203 | 18.2% | 18.2% | -3.5 | n/a | no target · QC vendors: 7 rows, 100.0% filled |
| P01_GOLD | 626 | 48.1% | 48.1% | +0.2 | 95% | ❌ 47 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 404 | 68.3% | 68.3% | -0.3 | 95% | ❌ 27 pts to go · QC vendors: 107 rows, 100.0% filled |
| P03 | 212 | 54.7% | 54.7% | -1.1 | 95% | ❌ 40 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 1639 | 58.3% | 58.3% | -1.9 | 95% | ❌ 37 pts to go · QC vendors: 443 rows, 98.6% filled |
| P05 | 417 | 15.6% | 15.6% | +0.8 | n/a | no target · QC vendors: 37 rows, 94.6% filled |
| P06M | 4248 | 53.9% | 53.9% | +53.9 | n/a | no target · QC vendors: 2290 rows, 100.0% filled |
| P06T | 19524 | 23.9% | 23.9% | -32.0 | n/a | no target · QC vendors: 2293 rows, 100.0% filled |
| P06 | 342 | 12.3% | 12.3% | -14.2 | n/a | no target · QC vendors: 18 rows, 100.0% filled |
| P07 | 737 | 8.1% | 8.1% | -13.3 | n/a | no target · QC vendors: 33 rows, 97.0% filled |
| P08 | 21048 | 5.5% | 5.5% | -23.4 | n/a | no target · QC vendors: 705 rows, 99.3% filled |
| P09 | 312 | 78.8% | 78.8% | -1.3 | 95% | ❌ 16 pts to go · QC vendors: 116 rows, 100.0% filled |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 17.2% | 17.2% | -6.2 | n/a | no target · QC vendors: 397 rows, 97.2% filled |
| P11 | 3312 | 59.1% | 59.1% | +29.8 | n/a | no target · QC vendors: 107 rows, 99.1% filled |
| P12 | 7 | 57.1% | 57.1% | -16.6 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 64.2% | 64.2% | +3.1 | n/a | no target · vendors with a registry record: 34 rows, 100.0% filled |
| P01T | 203 | 38.4% | 38.4% | -24.6 | n/a | no target · vendors with a registry record: 78 rows, 100.0% filled |
| P01_GOLD | 626 | 83.4% | 83.4% | -0.1 | 100% | ❌ 17 pts to go · vendors with a registry record: 522 rows, 100.0% filled |
| P02 | 404 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go · vendors with a registry record: 360 rows, 100.0% filled |
| P03 | 212 | 88.2% | 88.2% | -0.7 | 100% | ❌ 12 pts to go · vendors with a registry record: 187 rows, 100.0% filled |
| P04 | 1639 | 79.7% | 79.7% | -1.7 | 100% | ❌ 20 pts to go · vendors with a registry record: 1306 rows, 100.0% filled |
| P05 | 417 | 60.2% | 60.2% | -1.5 | n/a | no target · vendors with a registry record: 251 rows, 100.0% filled |
| P06M | 4248 | 54.8% | 54.8% | +34.0 | n/a | no target · vendors with a registry record: 2327 rows, 100.0% filled |
| P06T | 19524 | 28.3% | 28.3% | -49.9 | n/a | no target · vendors with a registry record: 5533 rows, 100.0% filled |
| P06 | 342 | 24.9% | 24.9% | -32.9 | n/a | no target · vendors with a registry record: 85 rows, 100.0% filled |
| P07 | 737 | 18.7% | 18.7% | -35.7 | n/a | no target · vendors with a registry record: 138 rows, 100.0% filled |
| P08 | 21048 | 9.8% | 9.8% | -44.5 | n/a | no target · vendors with a registry record: 2053 rows, 100.0% filled |
| P09 | 312 | 91.3% | 91.3% | -0.3 | n/a | no target · vendors with a registry record: 285 rows, 100.0% filled |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 31.9% | 31.9% | -11.8 | n/a | no target · vendors with a registry record: 1090 rows, 100.0% filled |
| P11 | 3312 | 63.4% | 63.4% | +5.2 | n/a | no target · vendors with a registry record: 2100 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 90.6% | 90.6% | -3.8 | 90% | ✅ met |
| P01T | 203 | 69.0% | 69.0% | -25.6 | 90% | ❌ 21 pts to go |
| P01_GOLD | 626 | 85.0% | 85.0% | +0.4 | 95% | 🟡 10 pts to go |
| P02 | 404 | 90.3% | 90.3% | -0.3 | 95% | 🟡 5 pts to go |
| P03 | 212 | 82.5% | 82.5% | -0.7 | 85% | 🟡 2 pts to go |
| P04 | 1639 | 77.1% | 77.1% | -1.7 | 90% | ❌ 13 pts to go |
| P05 | 417 | 68.1% | 68.1% | -7.7 | 75% | 🟡 7 pts to go |
| P06M | 4248 | 91.3% | 91.3% | +2.6 | n/a | no target |
| P06T | 19524 | 31.7% | 31.7% | -32.7 | n/a | no target |
| P06 | 342 | 41.8% | 41.8% | -14.8 | 80% | ❌ 38 pts to go |
| P07 | 737 | 32.4% | 32.4% | -21.2 | 80% | ❌ 48 pts to go |
| P08 | 21048 | 18.0% | 18.0% | -18.8 | 75% | ❌ 57 pts to go |
| P09 | 312 | 77.9% | 77.9% | -2.9 | 95% | ❌ 17 pts to go |
| P10R | 25308 | 40.5% | 40.6% |  | n/a | no target |
| P10 | 3417 | 26.5% | 26.5% | -5.5 | 70% | ❌ 44 pts to go |
| P11 | 3312 | 4.6% | 4.6% | -20.3 | 65% | ❌ 60 pts to go |
| P12 | 7 | 71.4% | 71.4% | -2.3 | 80% | 🟡 9 pts to go |
| P13 | 10552 | 70.0% | 70.0% | +17.5 | 60% | ✅ met |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 22.6% | 22.6% | -16.3 | 50% | ❌ 27 pts to go |
| P01T | 203 | 14.8% | 14.8% | -5.9 | n/a | no target |
| P01_GOLD | 626 | 20.6% | 20.6% | +0.2 | 40% | ❌ 19 pts to go |
| P02 | 404 | 21.5% | 21.5% | -0.3 | 40% | ❌ 18 pts to go |
| P03 | 212 | 26.4% | 26.4% | -0.5 | 40% | ❌ 14 pts to go |
| P04 | 1639 | 26.5% | 26.5% | -1.1 | 40% | ❌ 14 pts to go |
| P05 | 417 | 19.9% | 19.9% | -3.0 | 25% | 🟡 5 pts to go |
| P06M | 4248 | 13.1% | 13.1% | -12.5 | n/a | no target |
| P06T | 19524 | 14.5% | 14.5% | -16.4 | n/a | no target |
| P06 | 342 | 11.7% | 11.7% | +0.9 | 35% | ❌ 23 pts to go |
| P07 | 737 | 8.4% | 8.4% | -1.9 | 35% | ❌ 27 pts to go |
| P08 | 21048 | 7.6% | 7.6% | -3.5 | 35% | ❌ 27 pts to go |
| P09 | 312 | 16.3% | 16.3% | -0.8 | n/a | no target |
| P10R | 25308 | 18.5% | 18.5% |  | n/a | no target |
| P10 | 3417 | 7.1% | 7.1% | -2.5 | 30% | ❌ 23 pts to go |
| P11 | 3312 | 1.3% | 1.3% | -7.1 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +3.8 | n/a | no target |
| P13 | 10552 | 40.9% | 40.9% | +15.0 | 30% | ✅ met |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 203 | 95.1% | 95.1% | +1.6 | 100% | 🟡 5 pts to go |
| P01_GOLD | 626 | 90.3% | 90.3% | +2.6 | 100% | 🟡 10 pts to go |
| P02 | 404 | 97.5% | 97.5% | +0.7 | 100% | 🟡 2 pts to go |
| P03 | 212 | 92.9% | 92.9% | +1.1 | 100% | 🟡 7 pts to go |
| P04 | 1639 | 92.7% | 92.7% | +1.7 | 100% | 🟡 7 pts to go |
| P05 | 417 | 86.6% | 86.6% | +1.7 | 100% | ❌ 13 pts to go |
| P06M | 4248 | 99.0% | 99.0% | +27.0 | n/a | no target |
| P06T | 19524 | 80.8% | 80.8% | +0.6 | n/a | no target |
| P06 | 342 | 76.0% | 76.0% | +7.3 | 95% | ❌ 19 pts to go |
| P07 | 737 | 79.6% | 79.6% | +9.0 | 95% | ❌ 15 pts to go |
| P08 | 21048 | 73.5% | 73.5% | +7.3 | 95% | ❌ 22 pts to go |
| P09 | 312 | 95.5% | 95.5% | +0.0 | 100% | 🟡 4 pts to go |
| P10R | 25308 | 75.1% | 75.1% |  | n/a | no target |
| P10 | 3417 | 64.8% | 64.9% | -0.4 | 95% | ❌ 30 pts to go |
| P11 | 3312 | 66.4% | 66.4% | +32.0 | 80% | ❌ 14 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10552 | 85.5% | 85.5% | +9.4 | 95% | 🟡 10 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 92.5% | 92.5% | +3.6 | n/a | no target |
| P01T | 203 | 69.0% | 69.0% | -11.4 | n/a | no target |
| P01_GOLD | 626 | 70.4% | 70.4% | +0.2 | 90% | ❌ 20 pts to go |
| P02 | 404 | 79.5% | 79.5% | -0.2 | 95% | ❌ 16 pts to go |
| P03 | 212 | 73.6% | 73.6% | +0.0 | 95% | ❌ 21 pts to go |
| P04 | 1639 | 83.3% | 83.3% | -1.6 | 95% | ❌ 12 pts to go |
| P05 | 417 | 70.7% | 70.7% | -4.3 | 90% | ❌ 19 pts to go |
| P06M | 4248 | 95.1% | 95.1% | +11.2 | n/a | no target |
| P06T | 19524 | 48.0% | 48.0% | -29.3 | n/a | no target |
| P06 | 342 | 45.6% | 45.6% | -18.9 | 95% | ❌ 49 pts to go |
| P07 | 737 | 38.3% | 38.3% | -28.0 | 90% | ❌ 52 pts to go |
| P08 | 21048 | 28.5% | 28.5% | -46.2 | 95% | ❌ 66 pts to go |
| P09 | 312 | 86.9% | 86.9% | -2.1 | 100% | ❌ 13 pts to go |
| P10R | 25308 | 76.0% | 76.0% |  | n/a | no target |
| P10 | 3417 | 50.8% | 50.8% | -20.7 | 95% | ❌ 44 pts to go |
| P11 | 3312 | 7.9% | 7.9% | -21.0 | 75% | ❌ 67 pts to go |
| P12 | 7 | 85.7% | 85.7% | -3.8 | n/a | no target |
| P13 | 10552 | 75.1% | 75.1% | -4.2 | 95% | ❌ 20 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 77.4% | 77.4% | -0.4 | n/a | no target |
| P01T | 203 | 77.8% | 77.8% | -13.5 | 95% | ❌ 17 pts to go |
| P01_GOLD | 626 | 82.3% | 82.3% | +0.1 | 90% | 🟡 8 pts to go |
| P02 | 404 | 88.4% | 88.4% | +0.0 | 95% | 🟡 7 pts to go |
| P03 | 212 | 84.0% | 84.0% | -0.6 | 95% | ❌ 11 pts to go |
| P04 | 1639 | 83.9% | 83.9% | -0.3 | 90% | 🟡 6 pts to go |
| P05 | 417 | 87.3% | 87.3% | -2.3 | 95% | 🟡 8 pts to go |
| P06M | 4248 | 68.9% | 68.9% | -16.2 | n/a | no target |
| P06T | 19524 | 53.8% | 53.8% | -40.3 | n/a | no target |
| P06 | 342 | 60.8% | 60.8% | -29.6 | 100% | ❌ 39 pts to go |
| P07 | 737 | 49.9% | 49.9% | -38.2 | 100% | ❌ 50 pts to go |
| P08 | 21048 | 33.4% | 33.4% | -57.3 | 100% | ❌ 67 pts to go |
| P09 | 312 | 69.9% | 69.9% | -4.1 | n/a | no target |
| P10R | 25308 | 83.6% | 83.6% |  | n/a | no target |
| P10 | 3417 | 69.5% | 69.5% | -20.6 | 100% | ❌ 30 pts to go |
| P11 | 3312 | 10.5% | 10.5% | -26.0 | 80% | ❌ 70 pts to go |
| P12 | 7 | 100.0% | 100.0% | +15.8 | n/a | no target |
| P13 | 10552 | 75.4% | 75.4% | -8.8 | 95% | ❌ 20 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 7.5% | 7.5% | -9.2 | n/a | no target |
| P01T | 203 | 12.8% | 12.8% | -11.1 | n/a | no target |
| P01_GOLD | 626 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 404 | 27.7% | 27.7% | +0.0 | 40% | ❌ 12 pts to go |
| P03 | 212 | 10.4% | 10.4% | -0.2 | 20% | 🟡 10 pts to go |
| P04 | 1639 | 7.1% | 7.1% | -0.3 | 20% | ❌ 13 pts to go |
| P05 | 417 | 3.4% | 3.4% | -0.5 | 15% | ❌ 12 pts to go |
| P06M | 4248 | 0.5% | 0.5% | -4.3 | n/a | no target |
| P06T | 19524 | 0.8% | 0.8% | -2.4 | n/a | no target |
| P06 | 342 | 4.7% | 4.7% | -0.7 | n/a | no target |
| P07 | 737 | 6.5% | 6.5% | +0.2 | n/a | no target |
| P08 | 21048 | 0.2% | 0.2% | -0.8 | n/a | no target |
| P09 | 312 | 7.7% | 7.7% | -0.2 | n/a | no target |
| P10R | 25308 | 0.5% | 0.5% |  | n/a | no target |
| P10 | 3417 | 0.8% | 0.8% | -0.5 | n/a | no target |
| P11 | 3312 | 0.4% | 0.4% | -2.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 10552 | 0.8% | 0.8% | +0.2 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 39.6% | 39.6% | +0.7 | n/a | no target |
| P01T | 203 | 31.0% | 31.0% | -3.8 | 70% | ❌ 39 pts to go |
| P01_GOLD | 626 | 43.3% | 43.3% | +0.0 | 80% | ❌ 37 pts to go |
| P02 | 404 | 64.1% | 64.1% | +0.0 | 90% | ❌ 26 pts to go |
| P03 | 212 | 23.1% | 23.1% | +0.0 | 60% | ❌ 37 pts to go |
| P04 | 1639 | 48.4% | 48.4% | -2.1 | 85% | ❌ 37 pts to go |
| P05 | 417 | 12.0% | 12.0% | -1.0 | 50% | ❌ 38 pts to go |
| P06M | 4248 | 0.6% | 0.6% | -5.9 | n/a | no target |
| P06T | 19524 | 1.1% | 1.1% | -1.6 | n/a | no target |
| P06 | 342 | 16.4% | 16.4% | -1.7 | n/a | no target |
| P07 | 737 | 11.3% | 11.3% | -7.7 | n/a | no target |
| P08 | 21048 | 0.1% | 0.1% | -0.5 | n/a | no target |
| P09 | 312 | 78.2% | 78.2% | -2.4 | 95% | ❌ 17 pts to go |
| P10R | 25308 | 0.8% | 0.8% |  | n/a | no target |
| P10 | 3417 | 2.0% | 2.0% | -1.1 | n/a | no target |
| P11 | 3312 | 9.7% | 9.7% | -19.6 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -3.0 | n/a | no target |
| P13 | 10552 | 1.1% | 1.1% | +0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 3.8% | 3.8% | +3.8 | n/a | no target |
| P01T | 203 | 15.8% | 15.8% | -0.5 | n/a | no target |
| P01_GOLD | 626 | 33.9% | 33.9% | -0.1 | 70% | ❌ 36 pts to go |
| P02 | 404 | 44.3% | 44.3% | +0.0 | 75% | ❌ 31 pts to go |
| P03 | 212 | 23.1% | 23.1% | +0.0 | 55% | ❌ 32 pts to go |
| P04 | 1639 | 48.4% | 48.4% | -2.1 | 75% | ❌ 27 pts to go |
| P05 | 417 | 10.6% | 10.6% | -1.1 | 50% | ❌ 39 pts to go |
| P06M | 4248 | 0.2% | 0.2% | -1.6 | n/a | no target |
| P06T | 19524 | 0.8% | 0.8% | -0.7 | n/a | no target |
| P06 | 342 | 9.4% | 9.4% | -0.8 | n/a | no target |
| P07 | 737 | 5.3% | 5.3% | -5.0 | n/a | no target |
| P08 | 21048 | 0.1% | 0.1% | -0.4 | n/a | no target |
| P09 | 312 | 76.0% | 76.0% | -1.7 | 95% | ❌ 19 pts to go |
| P10R | 25308 | 0.6% | 0.6% |  | n/a | no target |
| P10 | 3417 | 1.3% | 1.3% | -0.5 | n/a | no target |
| P11 | 3312 | 9.8% | 9.8% | -19.1 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | -1.5 | n/a | no target |
| P13 | 10552 | 0.7% | 0.7% | +0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 7.5% | 7.5% | -9.2 | n/a | no target |
| P01T | 203 | 12.8% | 12.8% | -6.8 | n/a | no target |
| P01_GOLD | 626 | 57.8% | 58.0% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 404 | 52.2% | 52.5% | +0.0 | 75% | ❌ 23 pts to go |
| P03 | 212 | 44.8% | 44.8% | -0.4 | 70% | ❌ 25 pts to go |
| P04 | 1639 | 46.7% | 47.8% | -2.0 | 70% | ❌ 23 pts to go |
| P05 | 417 | 14.4% | 14.4% | -2.0 | 50% | ❌ 36 pts to go |
| P06M | 4248 | 0.6% | 0.6% | -3.6 | n/a | no target |
| P06T | 19524 | 0.5% | 0.6% | -1.1 | n/a | no target |
| P06 | 342 | 14.0% | 14.0% | -10.1 | n/a | no target |
| P07 | 737 | 2.2% | 2.2% | -3.0 | n/a | no target |
| P08 | 21048 | 0.2% | 0.2% | -0.8 | n/a | no target |
| P09 | 312 | 45.8% | 46.2% | +1.7 | 80% | ❌ 34 pts to go |
| P10R | 25308 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 3417 | 1.0% | 1.1% | -0.5 | n/a | no target |
| P11 | 3312 | 2.8% | 2.8% | -13.9 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -3.0 | n/a | no target |
| P13 | 10552 | 0.4% | 0.4% | +0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 13.2% | 13.2% | -25.7 | n/a | no target |
| P01T | 203 | 30.0% | 30.0% | -26.5 | 60% | ❌ 30 pts to go |
| P01_GOLD | 626 | 63.6% | 63.6% | +0.1 | 70% | 🟡 6 pts to go |
| P02 | 404 | 43.6% | 43.6% | -0.2 | 50% | 🟡 6 pts to go |
| P03 | 212 | 54.2% | 54.2% | -1.1 | 55% | 🟡 1 pts to go |
| P04 | 1639 | 22.0% | 22.0% | -0.9 | 40% | ❌ 18 pts to go |
| P05 | 417 | 16.3% | 16.3% | -1.1 | 40% | ❌ 24 pts to go |
| P06M | 4248 | 0.5% | 0.5% | -16.2 | n/a | no target |
| P06T | 19524 | 1.8% | 1.8% | -10.7 | n/a | no target |
| P06 | 342 | 15.2% | 15.2% | -15.5 | n/a | no target |
| P07 | 737 | 6.0% | 6.0% | -10.3 | n/a | no target |
| P08 | 21048 | 0.9% | 0.9% | -3.8 | n/a | no target |
| P09 | 312 | 5.8% | 5.8% | +0.0 | n/a | no target |
| P10R | 25308 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 3417 | 2.8% | 2.8% | -1.1 | n/a | no target |
| P11 | 3312 | 1.9% | 1.9% | -5.7 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | -1.5 | n/a | no target |
| P13 | 10552 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 15.1% | 15.1% | -29.3 | n/a | no target |
| P01T | 203 | 36.0% | 36.0% | -33.6 | 65% | ❌ 29 pts to go |
| P01_GOLD | 626 | 69.2% | 69.2% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 404 | 26.0% | 26.0% | -0.2 | 50% | ❌ 24 pts to go |
| P03 | 212 | 55.2% | 55.2% | -1.0 | 60% | 🟡 5 pts to go |
| P04 | 1639 | 9.5% | 9.5% | -0.4 | 40% | ❌ 30 pts to go |
| P05 | 417 | 18.9% | 18.9% | -2.5 | 45% | ❌ 26 pts to go |
| P06M | 4248 | 0.2% | 0.2% | -6.9 | n/a | no target |
| P06T | 19524 | 0.7% | 0.7% | -3.6 | n/a | no target |
| P06 | 342 | 26.6% | 26.6% | -21.6 | n/a | no target |
| P07 | 737 | 7.6% | 7.6% | -16.2 | n/a | no target |
| P08 | 21048 | 0.4% | 0.4% | -2.0 | n/a | no target |
| P09 | 312 | 9.6% | 9.6% | +0.9 | n/a | no target |
| P10R | 25308 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 3417 | 1.4% | 1.4% | -0.7 | n/a | no target |
| P11 | 3312 | 1.0% | 1.0% | -5.8 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 10552 | 0.3% | 0.3% | +0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 3.8% | 3.8% | -7.3 | n/a | no target |
| P01T | 203 | 21.2% | 21.2% | -23.4 | n/a | no target |
| P01_GOLD | 626 | 49.7% | 49.7% | -0.1 | 50% | 🟡 0 pts to go |
| P02 | 404 | 42.6% | 42.6% | +0.0 | n/a | no target |
| P03 | 212 | 57.5% | 57.5% | -1.2 | 60% | 🟡 2 pts to go |
| P04 | 1639 | 25.2% | 25.2% | -1.2 | n/a | no target |
| P05 | 417 | 14.6% | 14.6% | -2.1 | n/a | no target |
| P06M | 4248 | 0.4% | 0.4% | -3.8 | n/a | no target |
| P06T | 19524 | 0.8% | 0.8% | -3.2 | n/a | no target |
| P06 | 342 | 19.3% | 19.3% | -16.2 | n/a | no target |
| P07 | 737 | 7.2% | 7.2% | -11.5 | n/a | no target |
| P08 | 21048 | 0.2% | 0.2% | -1.3 | n/a | no target |
| P09 | 312 | 18.3% | 18.3% | -0.6 | n/a | no target |
| P10R | 25308 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 3417 | 1.7% | 1.7% | -0.7 | n/a | no target |
| P11 | 3312 | 1.1% | 1.1% | -6.7 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -21.1 | n/a | no target |
| P13 | 10552 | 0.6% | 0.6% | +0.2 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 7.5% | 7.5% | -20.3 | 15% | 🟡 8 pts to go |
| P01T | 203 | 15.3% | 15.3% | -14.0 | 15% | ✅ met |
| P01_GOLD | 626 | 35.3% | 35.3% | +0.2 | 40% | 🟡 5 pts to go |
| P02 | 404 | 13.6% | 13.9% | -0.3 | 25% | ❌ 11 pts to go |
| P03 | 212 | 21.2% | 21.2% | -0.4 | 25% | 🟡 4 pts to go |
| P04 | 1639 | 4.9% | 4.9% | -0.3 | 15% | ❌ 10 pts to go |
| P05 | 417 | 6.5% | 6.5% | -1.6 | 15% | 🟡 8 pts to go |
| P06M | 4248 | 0.7% | 0.7% | -5.3 | 15% | ❌ 14 pts to go |
| P06T | 19524 | 0.4% | 0.4% | -1.1 | 15% | ❌ 15 pts to go |
| P06 | 342 | 6.4% | 6.4% | -3.8 | 15% | 🟡 9 pts to go |
| P07 | 737 | 2.6% | 2.6% | -4.1 | 15% | ❌ 12 pts to go |
| P08 | 21048 | 0.1% | 0.1% | -0.8 | 15% | ❌ 15 pts to go |
| P09 | 312 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 25308 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P10 | 3417 | 1.1% | 1.1% | -0.3 | 15% | ❌ 14 pts to go |
| P11 | 3312 | 0.2% | 0.2% | -1.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 10552 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 3.8% | 3.8% | -7.3 | 15% | ❌ 11 pts to go |
| P01T | 203 | 16.3% | 16.3% | -16.3 | 25% | 🟡 9 pts to go |
| P01_GOLD | 626 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 404 | 28.0% | 28.0% | +0.0 | 15% | ✅ met |
| P03 | 212 | 25.5% | 25.5% | -0.5 | 15% | ✅ met |
| P04 | 1639 | 7.7% | 7.7% | -0.5 | 15% | 🟡 7 pts to go |
| P05 | 417 | 10.6% | 10.6% | -1.4 | 15% | 🟡 4 pts to go |
| P06M | 4248 | 0.1% | 0.1% | -2.3 | 15% | ❌ 15 pts to go |
| P06T | 19524 | 0.4% | 0.4% | -2.3 | 15% | ❌ 15 pts to go |
| P06 | 342 | 5.8% | 5.8% | -6.2 | 15% | 🟡 9 pts to go |
| P07 | 737 | 2.7% | 2.7% | -4.8 | 15% | ❌ 12 pts to go |
| P08 | 21048 | 0.2% | 0.2% | -0.8 | 15% | ❌ 15 pts to go |
| P09 | 312 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 25308 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 3417 | 0.9% | 0.9% | -0.5 | 15% | ❌ 14 pts to go |
| P11 | 3312 | 0.7% | 0.7% | -4.4 | 15% | ❌ 14 pts to go |
| P12 | 7 | 14.3% | 14.3% | -12.0 | 15% | 🟡 1 pts to go |
| P13 | 10552 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 1.9% | 1.9% | -3.7 | 20% | ❌ 18 pts to go |
| P01T | 203 | 4.9% | 4.9% | -4.9 | 20% | ❌ 15 pts to go |
| P01_GOLD | 626 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 404 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 212 | 1.9% | 1.9% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 1639 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 417 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 4248 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 19524 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P06 | 342 | 1.5% | 1.5% | -2.1 | 20% | ❌ 18 pts to go |
| P07 | 737 | 0.4% | 0.4% | -0.4 | 20% | ❌ 20 pts to go |
| P08 | 21048 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P09 | 312 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 3417 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P11 | 3312 | 0.1% | 0.1% | -0.5 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 1.9% | 1.9% | -3.7 | 15% | ❌ 13 pts to go |
| P01T | 203 | 3.4% | 3.4% | -4.2 | 15% | ❌ 12 pts to go |
| P01_GOLD | 626 | 10.5% | 10.5% | -0.1 | 15% | 🟡 4 pts to go |
| P02 | 404 | 13.4% | 13.4% | +0.0 | 15% | 🟡 2 pts to go |
| P03 | 212 | 23.6% | 23.6% | -0.4 | 15% | ✅ met |
| P04 | 1639 | 4.3% | 4.3% | -0.3 | 15% | ❌ 11 pts to go |
| P05 | 417 | 2.6% | 2.6% | -0.3 | 15% | ❌ 12 pts to go |
| P06M | 4248 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 19524 | 0.2% | 0.2% | -1.2 | 15% | ❌ 15 pts to go |
| P06 | 342 | 3.2% | 3.2% | -2.2 | 15% | ❌ 12 pts to go |
| P07 | 737 | 1.4% | 1.4% | -2.2 | 15% | ❌ 14 pts to go |
| P08 | 21048 | 0.1% | 0.1% | -0.6 | 15% | ❌ 15 pts to go |
| P09 | 312 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 25308 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 3417 | 0.5% | 0.5% | -0.3 | 15% | ❌ 14 pts to go |
| P11 | 3312 | 0.3% | 0.3% | -1.8 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 10552 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 5.7% | 5.7% | -5.4 | 20% | ❌ 14 pts to go |
| P01T | 203 | 20.2% | 20.2% | -21.1 | 40% | ❌ 20 pts to go |
| P01_GOLD | 626 | 45.7% | 45.7% | -0.1 | 40% | ✅ met |
| P02 | 404 | 48.5% | 48.5% | +0.0 | 20% | ✅ met |
| P03 | 212 | 54.7% | 54.7% | -1.1 | 35% | ✅ met |
| P04 | 1639 | 28.9% | 28.9% | -1.4 | 20% | ✅ met |
| P05 | 417 | 14.9% | 14.9% | -1.8 | 20% | 🟡 5 pts to go |
| P06M | 4248 | 0.4% | 0.4% | -3.8 | 20% | ❌ 20 pts to go |
| P06T | 19524 | 1.0% | 1.0% | -3.5 | 20% | ❌ 19 pts to go |
| P06 | 342 | 19.9% | 19.9% | -15.6 | 20% | 🟡 0 pts to go |
| P07 | 737 | 6.4% | 6.4% | -8.3 | 20% | ❌ 14 pts to go |
| P08 | 21048 | 0.5% | 0.5% | -1.8 | 20% | ❌ 20 pts to go |
| P09 | 312 | 18.3% | 18.3% | -3.7 | 20% | 🟡 2 pts to go |
| P10R | 25308 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P10 | 3417 | 1.9% | 1.9% | -0.7 | 20% | ❌ 18 pts to go |
| P11 | 3312 | 1.3% | 1.3% | -6.7 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | -15.8 | 20% | ❌ 20 pts to go |
| P13 | 10552 | 0.9% | 0.9% | +0.3 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 45.3% | 45.3% | +45.3 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | -0.6 | n/a | no target |
| P01_GOLD | 626 | 69.6% | 69.6% | -0.1 | 95% | ❌ 25 pts to go |
| P02 | 404 | 73.0% | 73.0% | -0.3 | 95% | ❌ 22 pts to go |
| P03 | 212 | 66.0% | 66.0% | -1.3 | 90% | ❌ 24 pts to go |
| P04 | 1639 | 56.4% | 56.4% | -2.0 | 85% | ❌ 29 pts to go |
| P05 | 417 | 35.7% | 35.7% | +0.8 | 75% | ❌ 39 pts to go |
| P06M | 4248 | 61.0% | 61.0% | +61.0 | n/a | no target |
| P06T | 19524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 89.7% | 89.7% | -1.1 | 100% | ❌ 10 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 2.6% | 2.6% | -16.2 | 60% | ❌ 57 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 45.3% | 45.3% | +45.3 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 72.8% | 72.8% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 404 | 77.0% | 77.0% | -0.2 | 100% | ❌ 23 pts to go |
| P03 | 212 | 73.1% | 73.1% | -1.4 | n/a | no target |
| P04 | 1639 | 57.9% | 57.9% | -2.1 | 95% | ❌ 37 pts to go |
| P05 | 417 | 32.1% | 32.1% | +0.9 | 80% | ❌ 48 pts to go |
| P06M | 4248 | 61.0% | 61.0% | +61.0 | n/a | no target |
| P06T | 19524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 92.9% | 92.9% | -0.5 | 100% | 🟡 7 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 2.8% | 2.8% | -17.2 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 62.3% | 62.3% | +62.3 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | -0.6 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | -0.1 | 85% | ❌ 33 pts to go |
| P02 | 404 | 66.6% | 66.6% | -0.2 | 90% | ❌ 23 pts to go |
| P03 | 212 | 53.8% | 53.8% | -1.0 | 85% | ❌ 31 pts to go |
| P04 | 1639 | 62.8% | 62.8% | -1.3 | 90% | ❌ 27 pts to go |
| P05 | 417 | 33.8% | 33.8% | -1.4 | 75% | ❌ 41 pts to go |
| P06M | 4248 | 91.8% | 91.8% | +91.8 | n/a | no target |
| P06T | 19524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 85.3% | 85.3% | -0.3 | 95% | 🟡 10 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 2.4% | 2.4% | -14.9 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 64.2% | 64.2% | +64.2 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | -0.6 | n/a | no target |
| P01_GOLD | 626 | 51.9% | 51.9% | -0.2 | 85% | ❌ 33 pts to go |
| P02 | 404 | 60.9% | 60.9% | -0.2 | 90% | ❌ 29 pts to go |
| P03 | 212 | 55.2% | 55.2% | -1.0 | 85% | ❌ 30 pts to go |
| P04 | 1639 | 53.5% | 53.5% | -0.8 | 90% | ❌ 36 pts to go |
| P05 | 417 | 42.2% | 42.2% | +0.5 | 75% | ❌ 33 pts to go |
| P06M | 4248 | 85.4% | 85.4% | +85.4 | n/a | no target |
| P06T | 19524 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 2.0% | 2.0% | -12.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 69.8% | 69.8% | +69.8 | n/a | no target |
| P01T | 203 | 90.6% | 90.6% | +9.1 | n/a | no target |
| P01_GOLD | 626 | 85.6% | 85.6% | -0.1 | 100% | ❌ 14 pts to go |
| P02 | 404 | 81.7% | 81.7% | +0.0 | 100% | ❌ 18 pts to go |
| P03 | 212 | 92.5% | 92.5% | +0.2 | n/a | no target |
| P04 | 1639 | 72.2% | 72.2% | -0.4 | 95% | ❌ 23 pts to go |
| P05 | 417 | 76.7% | 76.7% | +1.2 | 95% | ❌ 18 pts to go |
| P06M | 4248 | 96.2% | 96.2% | +95.6 | n/a | no target |
| P06T | 19524 | 92.5% | 92.5% | +9.1 | n/a | no target |
| P06 | 342 | 36.0% | 36.0% | -39.9 | n/a | no target |
| P07 | 737 | 26.7% | 26.7% | -50.3 | n/a | no target |
| P08 | 21048 | 14.5% | 14.5% | -70.4 | n/a | no target |
| P09 | 312 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 25308 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 3417 | 75.8% | 75.8% | -22.6 | n/a | no target |
| P11 | 3312 | 34.0% | 34.0% | -55.9 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 69.8% | 69.8% | +69.8 | n/a | no target |
| P01T | 203 | 90.6% | 90.6% | +9.1 | n/a | no target |
| P01_GOLD | 626 | 88.8% | 88.8% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 404 | 82.9% | 83.2% | +0.0 | 100% | ❌ 17 pts to go |
| P03 | 212 | 93.9% | 93.9% | +0.1 | n/a | no target |
| P04 | 1639 | 79.4% | 79.4% | +0.4 | 95% | ❌ 16 pts to go |
| P05 | 417 | 90.6% | 90.6% | +0.5 | 70% | ✅ met |
| P06M | 4248 | 96.2% | 96.2% | +95.6 | n/a | no target |
| P06T | 19524 | 92.5% | 92.5% | +9.1 | n/a | no target |
| P06 | 342 | 36.0% | 36.0% | -39.9 | n/a | no target |
| P07 | 737 | 26.7% | 26.7% | -50.3 | n/a | no target |
| P08 | 21048 | 14.5% | 14.5% | -70.4 | n/a | no target |
| P09 | 312 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 25308 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 3417 | 75.8% | 75.8% | -22.6 | n/a | no target |
| P11 | 3312 | 34.1% | 34.1% | -56.2 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | -0.6 | n/a | no target · rows from a source that publishes bids: 6 rows, 16.7% filled |
| P01_GOLD | 626 | 17.3% | 17.3% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 367 rows, 29.4% filled |
| P02 | 404 | 13.1% | 13.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 294 rows, 18.0% filled |
| P03 | 212 | 16.0% | 16.0% | -0.3 | n/a | no target · rows from a source that publishes bids: 140 rows, 24.3% filled |
| P04 | 1639 | 3.5% | 3.5% | -0.2 | n/a | no target · rows from a source that publishes bids: 878 rows, 6.6% filled |
| P05 | 417 | 3.1% | 3.1% | -0.3 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 4248 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 19524 | 0.0% | 0.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 64 rows, 4.7% filled |
| P06 | 342 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 3.2% | 3.2% | +0.1 | n/a | no target · rows from a source that publishes bids: 299 rows, 3.3% filled |
| P10R | 25308 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3312 | 0.4% | 0.4% | -2.3 | n/a | no target · rows from a source that publishes bids: 91 rows, 14.3% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 10552 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.5% | 97.5% | +0.5 | n/a | no target |
| P01_GOLD | 626 | 53.0% | 82.4% | -0.2 | 90% | ❌ 37 pts to go |
| P02 | 404 | 60.9% | 85.6% | -0.2 | 90% | ❌ 29 pts to go |
| P03 | 212 | 55.2% | 75.9% | -1.0 | 90% | ❌ 35 pts to go |
| P04 | 1639 | 43.5% | 86.2% | -1.8 | 90% | ❌ 46 pts to go |
| P05 | 417 | 0.0% | 82.5% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 4248 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 19524 | 0.0% | 99.7% | +0.0 | n/a | no target |
| P06 | 342 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 2.2% | 3.8% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 25308 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3312 | 1.8% | 98.7% | -10.9 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 1.0% | 98.0% | +1.0 | n/a | no target |
| P01_GOLD | 626 | 25.9% | 55.3% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 404 | 59.9% | 84.7% | +0.0 | n/a | no target |
| P03 | 212 | 30.2% | 50.9% | -0.6 | n/a | no target |
| P04 | 1639 | 47.7% | 90.4% | -2.0 | n/a | no target |
| P05 | 417 | 0.5% | 83.0% | +0.0 | n/a | no target |
| P06M | 4248 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 19524 | 0.2% | 99.8% | +0.2 | n/a | no target |
| P06 | 342 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 42.0% | 43.6% | -2.4 | n/a | no target |
| P10R | 25308 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3312 | 1.7% | 98.5% | -9.9 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 2.5% | 99.5% | +0.3 | n/a | no target |
| P01_GOLD | 626 | 51.6% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 404 | 65.6% | 90.3% | +0.0 | n/a | no target |
| P03 | 212 | 58.0% | 78.8% | -1.1 | n/a | no target |
| P04 | 1639 | 48.2% | 90.9% | -2.1 | n/a | no target |
| P05 | 417 | 4.8% | 87.3% | -0.4 | n/a | no target |
| P06M | 4248 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 19524 | 0.2% | 99.9% | +0.2 | n/a | no target |
| P06 | 342 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 737 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21048 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 64.1% | 65.7% | -3.4 | n/a | no target |
| P10R | 25308 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 3417 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3312 | 1.8% | 98.6% | -10.9 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10552 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 212 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1639 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 417 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4248 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 19524 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 342 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 737 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 21048 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 25308 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 3417 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10552 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 212 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1639 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 417 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4248 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 19524 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 342 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 737 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 21048 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 25308 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 3417 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10552 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 53 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 212 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1639 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 417 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4248 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 19524 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 342 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 737 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 21048 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 25308 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 3417 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10552 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

