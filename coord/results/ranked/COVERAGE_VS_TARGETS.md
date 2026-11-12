# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **93 of 438 met** (21.2%); 62 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 223, P01T 228, P01_GOLD 630, P02 464, P03 265, P04 3568, P05 423, P06M 20378, P06T 59777, P06 269, P07 757, P08 27027, P09 277, P10R 0, P10 2128, P11 1776, P12 10, P13 153569

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 16.1% | 8 | vendor GST/HST number (207 rows) |
| P01T | 228 | 1.3% | 37.7% | 8 | payment terms (182 rows) |
| P01_GOLD | 630 | 24.3% | 71.6% | 10 | payment terms (220 rows) |
| P02 | 464 | 7.8% | 55.4% | 9 | PO rule (354 rows) |
| P03 | 265 | 14.7% | 56.2% | 9 | PO rule (132 rows) |
| P04 | 3568 | 1.3% | 17.2% | 6 | PO rule (3368 rows) |
| P05 | 423 | 0.9% | 17.0% | 7 | payment terms (351 rows) |
| P06M | 20378 | 0.0% | 3.1% | 7 | PO rule (19999 rows) |
| P06T | 59777 | 0.1% | 13.0% | 7 | PO rule (59397 rows) |
| P06 | 269 | 0.0% | 10.4% | 6 | reference to quote (PO / contract / vendor id) (257 rows) |
| P07 | 757 | 0.0% | 2.5% | 6 | payment terms (716 rows) |
| P08 | 27027 | 0.0% | 1.0% | 6 | PO rule (26759 rows) |
| P09 | 277 | 1.4% | 41.9% | 8 | payment terms (259 rows) |
| P10 | 2128 | 0.0% | 1.3% | 5 | reference to quote (PO / contract / vendor id) (2128 rows) |
| P11 | 1776 | 0.1% | 8.1% | 6 | PO rule (1709 rows) |
| P12 | 10 | 0.0% | 40.0% | 8 | PO rule (10 rows) |
| P13 | 153569 | 0.0% | 0.3% | 7 | reference to quote (PO / contract / vendor id) (153569 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 223 | 9 | 54 | 160 | 0 | 0 | 71 |
| P01T | 228 | 27 | 37 | 164 | 0 | 0 | 68 |
| P01_GOLD | 630 | 257 | 169 | 204 | 0 | 0 | 82 |
| P02 | 464 | 0 | 189 | 275 | 0 | 0 | 66 |
| P03 | 265 | 0 | 0 | 253 | 12 | 0 | 57 |
| P04 | 3568 | 0 | 0 | 2941 | 627 | 0 | 46 |
| P05 | 423 | 15 | 28 | 367 | 13 | 0 | 51 |
| P06M | 20378 | 0 | 17 | 20306 | 55 | 0 | 46 |
| P06T | 59777 | 0 | 28 | 40209 | 19540 | 0 | 38 |
| P06 | 269 | 18 | 43 | 208 | 0 | 0 | 68 |
| P07 | 757 | 0 | 21 | 714 | 22 | 0 | 54 |
| P08 | 27027 | 0 | 0 | 23997 | 3030 | 0 | 43 |
| P09 | 277 | 5 | 10 | 261 | 1 | 0 | 53 |
| P10 | 2128 | 3 | 13 | 1447 | 665 | 0 | 41 |
| P11 | 1776 | 7 | 13 | 36 | 0 | 1720 | 23 |
| P12 | 10 | 0 | 0 | 10 | 0 | 0 | 54 |
| P13 | 153569 | 14 | 65 | 153478 | 12 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 223 | 168 | 75.3% | tax treatment (32) |
| P01T | 228 | 139 | 61.0% | bill-to legal name and address (75) |
| P01_GOLD | 630 | 477 | 75.7% | bill-to legal name and address (97) |
| P02 | 464 | 314 | 67.7% | the buyer's PO / reference rule (85) |
| P03 | 265 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (265) |
| P04 | 3568 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3568) |
| P05 | 423 | 44 | 10.4% | a confirmed invoicing / AP or finance channel (336) |
| P06M | 20378 | 223 | 1.1% | a confirmed invoicing / AP or finance channel (20092) |
| P06T | 59777 | 331 | 0.6% | a confirmed invoicing / AP or finance channel (58975) |
| P06 | 269 | 49 | 18.2% | the buyer's PO / reference rule (112) |
| P07 | 757 | 29 | 3.8% | bill-to legal name and address (299) |
| P08 | 27027 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (27027) |
| P09 | 277 | 40 | 14.4% | a confirmed invoicing / AP or finance channel (226) |
| P10 | 2128 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2050) |
| P11 | 1776 | 14 | 0.8% | a confirmed invoicing / AP or finance channel (1720) |
| P12 | 10 | 2 | 20.0% | a confirmed invoicing / AP or finance channel (8) |
| P13 | 153569 | 44 | 0.0% | a confirmed invoicing / AP or finance channel (151409) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 223 | 6 | 2.7% | 7 | 0 | the vendor's GST/HST number (BN9) (207) |
| P01T | 228 | 100 | 43.9% | 3 | 0 | the vendor's GST/HST number (BN9) (74) |
| P01_GOLD | 630 | 409 | 64.9% | 11 | 0 | the vendor's GST/HST number (BN9) (144) |
| P02 | 464 | 214 | 46.1% | 22 | 0 | the vendor's GST/HST number (BN9) (200) |
| P03 | 265 | 18 | 6.8% | 0 | 133 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (96) |
| P04 | 3568 | 42 | 1.2% | 7 | 903 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2558) |
| P05 | 423 | 20 | 4.7% | 8 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (203) |
| P06M | 20378 | 7 | 0.0% | 12 | 492 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (19507) |
| P06T | 59777 | 384 | 0.6% | 14 | 18653 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (40237) |
| P06 | 269 | 25 | 9.3% | 54 | 0 | the vendor's GST/HST number (BN9) (123) |
| P07 | 757 | 13 | 1.7% | 129 | 36 | the vendor's GST/HST number (BN9) (348) |
| P08 | 27027 | 5 | 0.0% | 13 | 6760 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (20206) |
| P09 | 277 | 37 | 13.4% | 0 | 108 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (106) |
| P10 | 2128 | 7 | 0.3% | 15 | 305 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1721) |
| P11 | 1776 | 7 | 0.4% | 3 | 0 | a confirmed invoicing / AP or finance channel (1704) |
| P12 | 10 | 1 | 10.0% | 0 | 4 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 153569 | 21 | 0.0% | 1065 | 61547 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89675) |
| **all** | 271769 | 1316 | 0.5% | 1363 | 89066 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 214 | 0 | 0 | 0 | 142 | 8 | 0 | 171 | 186 | 1 |
| P01T | 201 | 0 | 0 | 0 | 122 | 67 | 31 | 166 | 184 | 4 |
| P01_GOLD | 373 | 0 | 0 | 0 | 13 | 79 | 30 | 199 | 235 | 3 |
| P02 | 464 | 0 | 464 | 0 | 37 | 55 | 14 | 354 | 283 | 2 |
| P03 | 265 | 0 | 265 | 0 | 17 | 46 | 26 | 132 | 140 | 2 |
| P04 | 3568 | 0 | 3568 | 0 | 1521 | 1266 | 959 | 3368 | 3115 | 33 |
| P05 | 408 | 0 | 356 | 0 | 83 | 94 | 39 | 339 | 353 | 7 |
| P06M | 20378 | 0 | 20378 | 0 | 14658 | 1337 | 111 | 19999 | 19753 | 19 |
| P06T | 59777 | 0 | 59777 | 0 | 53614 | 37745 | 24718 | 59397 | 58872 | 375 |
| P06 | 251 | 0 | 0 | 0 | 131 | 74 | 45 | 187 | 219 | 4 |
| P07 | 757 | 0 | 757 | 0 | 509 | 313 | 118 | 714 | 716 | 5 |
| P08 | 27027 | 0 | 27027 | 0 | 21190 | 12639 | 4534 | 26759 | 26403 | 161 |
| P09 | 272 | 0 | 253 | 0 | 12 | 69 | 1 | 247 | 261 | 7 |
| P10 | 2125 | 0 | 2092 | 0 | 1101 | 1132 | 963 | 2057 | 2019 | 16 |
| P11 | 1769 | 1720 | 1672 | 0 | 896 | 1212 | 545 | 1709 | 1703 | 20 |
| P12 | 10 | 0 | 9 | 0 | 0 | 2 | 0 | 10 | 10 | 1 |
| P13 | 153555 | 0 | 153156 | 0 | 123212 | 83342 | 18 | 153231 | 152446 | 61 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 68.0% | 95% | 41503 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 30665 |
| ap_system_hint | P13 | 0.4% | 20% | 30116 |
| buyer_bn_as_published | P13 | 12.6% | 30% | 26784 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 22895 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 22851 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 22056 |
| buyer_legal_name_as_published | P13 | 45.7% | 60% | 21915 |
| buyer_logo_url | P13 | 80.8% | 95% | 21754 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11940 |
| ap_system_hint | P06T | 0.6% | 20% | 11609 |
| vendor_registered_address | P08 | 31.8% | 70% | 10327 |
| buyer_phone | P08 | 61.8% | 95% | 8960 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8861 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8848 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 8569 |
| buyer_legal_name_as_published | P08 | 53.2% | 75% | 5883 |
| vendor_phone | P08 | 64.5% | 85% | 5535 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5394 |
| vendor_emails | P08 | 55.4% | 75% | 5304 |
| ap_system_hint | P08 | 0.8% | 20% | 5181 |
| vendor_bn9 | P08 | 32.7% | 50% | 4675 |
| buyer_logo_url | P08 | 83.2% | 100% | 4532 |
| vendor_trading_name | P08 | 33.9% | 50% | 4340 |
| buyer_bn_as_published | P08 | 19.5% | 35% | 4192 |
| buyer_ap_cycle_published | P06M | 0.1% | 20% | 4065 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 3954 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 3953 |
| invoice_reference_hint | P08 | 10.4% | 25% | 3937 |
| buyer_payment_method_preference | P08 | 0.5% | 15% | 3909 |
| ap_system_hint | P06M | 1.1% | 20% | 3849 |
| vendor_logo_url | P08 | 88.1% | 100% | 3227 |
| buyer_address | P08 | 83.2% | 95% | 3189 |
| buyer_esignature_preference | P06M | 0.5% | 15% | 2960 |
| buyer_tax_exempt_status | P06M | 0.7% | 15% | 2914 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 2885 |
| average_contract_duration_days | P04 | 19.7% | 90% | 2508 |
| currency | P04 | 27.0% | 95% | 2426 |
| end_date | P04 | 24.7% | 90% | 2332 |
| ap_phone | P04 | 21.5% | 85% | 2265 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 92.4% | 92.4% | +3.3 | 50% | ✅ met |
| P01T | 228 | 95.6% | 95.6% | +1.8 | 50% | ✅ met |
| P01_GOLD | 630 | 92.1% | 94.4% | -0.1 | 95% | 🟡 3 pts to go |
| P02 | 464 | 75.0% | 76.5% | +1.0 | 95% | ❌ 20 pts to go |
| P03 | 265 | 81.1% | 84.5% | -0.3 | 95% | ❌ 14 pts to go |
| P04 | 3568 | 31.8% | 33.5% | +1.6 | 90% | ❌ 58 pts to go |
| P05 | 423 | 39.5% | 42.3% | +0.9 | 70% | ❌ 30 pts to go |
| P06M | 20378 | 92.6% | 92.6% | +0.8 | n/a | no target |
| P06T | 59777 | 99.3% | 99.3% | +0.7 | n/a | no target |
| P06 | 269 | 34.9% | 34.9% | +0.5 | 30% | ✅ met |
| P07 | 757 | 12.2% | 12.2% | +5.3 | 30% | ❌ 18 pts to go |
| P08 | 27027 | 10.4% | 10.4% | +9.1 | 25% | ❌ 15 pts to go |
| P09 | 277 | 98.9% | 99.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10 | 2128 | 3.3% | 3.3% | +0.2 | 25% | ❌ 22 pts to go |
| P11 | 1776 | 55.2% | 55.9% | +8.3 | 60% | 🟡 5 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 153569 | 99.6% | 99.6% | -0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 630 | 5.9% | 5.9% | -0.2 | 50% | ❌ 44 pts to go |
| P02 | 464 | 5.6% | 5.6% | -0.6 | 50% | ❌ 44 pts to go |
| P03 | 265 | 1.9% | 1.9% | +0.4 | 40% | ❌ 38 pts to go |
| P04 | 3568 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 423 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 20378 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 88.3% | 88.3% | +6.1 | n/a | no target |
| P01T | 228 | 79.8% | 79.8% | +5.3 | 50% | ✅ met |
| P01_GOLD | 630 | 67.1% | 67.1% | +0.3 | 85% | ❌ 18 pts to go |
| P02 | 464 | 66.2% | 66.2% | +1.4 | 90% | ❌ 24 pts to go |
| P03 | 265 | 60.4% | 60.4% | +0.7 | 85% | ❌ 25 pts to go |
| P04 | 3568 | 29.0% | 29.0% | +1.4 | 85% | ❌ 56 pts to go |
| P05 | 423 | 29.8% | 29.8% | +0.9 | 60% | ❌ 30 pts to go |
| P06M | 20378 | 92.3% | 92.3% | +0.8 | n/a | no target |
| P06T | 59777 | 99.2% | 99.2% | +0.8 | n/a | no target |
| P06 | 269 | 4.5% | 4.5% | +4.5 | n/a | no target |
| P07 | 757 | 6.5% | 6.5% | +6.5 | n/a | no target |
| P08 | 27027 | 9.4% | 9.4% | +9.4 | n/a | no target |
| P09 | 277 | 95.7% | 95.7% | -0.4 | 100% | 🟡 4 pts to go |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 52.3% | 52.3% | +9.0 | 60% | 🟡 8 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 630 | 51.4% | 51.4% | +0.6 | 80% | ❌ 29 pts to go |
| P02 | 464 | 58.4% | 58.4% | +1.5 | 60% | 🟡 2 pts to go |
| P03 | 265 | 50.2% | 50.2% | +0.0 | 80% | ❌ 30 pts to go |
| P04 | 3568 | 24.0% | 24.0% | +1.1 | 50% | ❌ 26 pts to go |
| P05 | 423 | 12.5% | 12.5% | +1.1 | 40% | ❌ 28 pts to go |
| P06M | 20378 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 81.2% | 81.2% | -2.2 | 50% | ✅ met |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 3.4% | 3.4% | -2.2 | 40% | ❌ 37 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 630 | 61.0% | 61.0% | +0.6 | 85% | ❌ 24 pts to go |
| P02 | 464 | 58.6% | 58.6% | +2.4 | 90% | ❌ 31 pts to go |
| P03 | 265 | 58.9% | 58.9% | +0.3 | 85% | ❌ 26 pts to go |
| P04 | 3568 | 24.9% | 24.9% | +1.3 | 85% | ❌ 60 pts to go |
| P05 | 423 | 20.3% | 20.3% | +0.6 | 50% | ❌ 30 pts to go |
| P06M | 20378 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 3.8% | 3.8% | -2.2 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 464 | 6.9% | 6.9% | +0.9 | 50% | ❌ 43 pts to go |
| P03 | 265 | 8.7% | 8.7% | +0.3 | 50% | ❌ 41 pts to go |
| P04 | 3568 | 1.9% | 1.9% | +0.1 | 40% | ❌ 38 pts to go |
| P05 | 423 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 20378 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 3.2% | 3.2% | -0.1 | 50% | ❌ 47 pts to go |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 0.5% | 0.5% | -0.4 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 35.9% | 35.9% | +1.1 | 80% | ❌ 44 pts to go |
| P02 | 464 | 52.6% | 52.6% | +0.7 | 90% | ❌ 37 pts to go |
| P03 | 265 | 34.0% | 34.0% | +1.3 | 80% | ❌ 46 pts to go |
| P04 | 3568 | 22.2% | 22.2% | +0.6 | 85% | ❌ 63 pts to go |
| P05 | 423 | 6.4% | 6.4% | +0.9 | 50% | ❌ 44 pts to go |
| P06M | 20378 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 73.6% | 73.6% | -0.7 | 95% | ❌ 21 pts to go |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 2.8% | 2.8% | -1.5 | 50% | ❌ 47 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 8.3% | 8.3% | -0.2 | 50% | ❌ 42 pts to go |
| P02 | 464 | 5.6% | 5.6% | -0.6 | 50% | ❌ 44 pts to go |
| P03 | 265 | 2.6% | 2.6% | +0.7 | 30% | ❌ 27 pts to go |
| P04 | 3568 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 423 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 20378 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 228 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3568 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 20378 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59777 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 269 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 757 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 27027 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2128 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1776 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 7.2% | 7.2% | -4.4 | 70% | ❌ 63 pts to go |
| P01T | 228 | 60.1% | 60.1% | +9.6 | 60% | ✅ met |
| P01_GOLD | 630 | 74.9% | 74.9% | +0.1 | 90% | ❌ 15 pts to go |
| P02 | 464 | 54.3% | 54.3% | +0.7 | 85% | ❌ 31 pts to go |
| P03 | 265 | 66.8% | 66.8% | -2.8 | 90% | ❌ 23 pts to go |
| P04 | 3568 | 38.2% | 38.2% | +3.2 | 75% | ❌ 37 pts to go |
| P05 | 423 | 54.6% | 54.6% | -0.1 | 50% | ✅ met |
| P06M | 20378 | 2.9% | 2.9% | -0.3 | n/a | no target |
| P06T | 59777 | 64.5% | 64.5% | +17.2 | n/a | no target |
| P06 | 269 | 43.5% | 43.5% | -0.5 | 40% | ✅ met |
| P07 | 757 | 34.2% | 34.2% | +1.2 | 50% | ❌ 16 pts to go |
| P08 | 27027 | 32.7% | 32.7% | +2.2 | 50% | ❌ 17 pts to go |
| P09 | 277 | 57.0% | 57.0% | -1.3 | 80% | ❌ 23 pts to go |
| P10 | 2128 | 38.8% | 38.8% | +4.3 | 40% | 🟡 1 pts to go |
| P11 | 1776 | 55.7% | 55.7% | +8.8 | 60% | 🟡 4 pts to go |
| P12 | 10 | 50.0% | 50.0% | -10.0 | 85% | ❌ 35 pts to go |
| P13 | 153569 | 44.9% | 44.9% | +13.2 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 49.8% | 49.8% | -9.9 | n/a | no target |
| P01T | 228 | 59.6% | 59.6% | +8.6 | n/a | no target |
| P01_GOLD | 630 | 72.7% | 72.7% | +0.0 | 95% | ❌ 22 pts to go |
| P02 | 464 | 74.8% | 74.8% | +1.0 | 95% | ❌ 20 pts to go |
| P03 | 265 | 69.4% | 69.4% | -2.5 | 95% | ❌ 26 pts to go |
| P04 | 3568 | 53.2% | 53.2% | +4.0 | 95% | ❌ 42 pts to go |
| P05 | 423 | 58.2% | 58.2% | -0.1 | 70% | ❌ 12 pts to go |
| P06M | 20378 | 42.0% | 42.0% | -4.0 | n/a | no target |
| P06T | 59777 | 67.5% | 67.5% | +11.3 | n/a | no target |
| P06 | 269 | 39.8% | 39.8% | -1.2 | 80% | ❌ 40 pts to go |
| P07 | 757 | 33.0% | 33.0% | +1.1 | 70% | ❌ 37 pts to go |
| P08 | 27027 | 31.8% | 31.8% | +1.5 | 70% | ❌ 38 pts to go |
| P09 | 277 | 86.6% | 86.6% | +0.0 | 100% | ❌ 13 pts to go |
| P10 | 2128 | 39.2% | 39.2% | +3.7 | 70% | ❌ 31 pts to go |
| P11 | 1776 | 59.7% | 59.7% | +7.2 | 75% | ❌ 15 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 40.4% | 40.4% | +13.5 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 22.4% | 22.4% | +5.3 | n/a | no target |
| P01T | 228 | 65.4% | 65.4% | +11.8 | n/a | no target |
| P01_GOLD | 630 | 48.7% | 48.7% | -1.1 | 60% | ❌ 11 pts to go |
| P02 | 464 | 56.2% | 56.2% | +0.0 | 60% | 🟡 4 pts to go |
| P03 | 265 | 52.1% | 52.1% | -3.0 | 60% | 🟡 8 pts to go |
| P04 | 3568 | 42.6% | 42.6% | +0.5 | 55% | ❌ 12 pts to go |
| P05 | 423 | 22.9% | 22.9% | -1.7 | 50% | ❌ 27 pts to go |
| P06M | 20378 | 8.5% | 8.5% | +1.7 | n/a | no target |
| P06T | 59777 | 67.9% | 67.9% | +17.0 | n/a | no target |
| P06 | 269 | 48.3% | 48.3% | +0.7 | n/a | no target |
| P07 | 757 | 40.4% | 40.4% | -0.5 | 55% | ❌ 15 pts to go |
| P08 | 27027 | 33.9% | 33.9% | -2.3 | 50% | ❌ 16 pts to go |
| P09 | 277 | 72.6% | 72.6% | +0.3 | 70% | ✅ met |
| P10 | 2128 | 48.2% | 48.2% | +1.4 | 55% | 🟡 7 pts to go |
| P11 | 1776 | 59.7% | 59.7% | +7.5 | 50% | ✅ met |
| P12 | 10 | 90.0% | 90.0% | +3.3 | n/a | no target |
| P13 | 153569 | 3.2% | 3.2% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 35.4% | 35.4% | -15.0 | n/a | no target |
| P01T | 228 | 79.4% | 79.4% | +4.9 | n/a | no target |
| P01_GOLD | 630 | 50.3% | 50.3% | -0.2 | 70% | ❌ 20 pts to go |
| P02 | 464 | 57.1% | 57.1% | -1.1 | 70% | ❌ 13 pts to go |
| P03 | 265 | 50.2% | 50.2% | -1.1 | 70% | ❌ 20 pts to go |
| P04 | 3568 | 54.9% | 54.9% | +0.8 | 65% | ❌ 10 pts to go |
| P05 | 423 | 29.1% | 29.1% | +0.7 | 60% | ❌ 31 pts to go |
| P06M | 20378 | 29.0% | 29.0% | -7.6 | n/a | no target |
| P06T | 59777 | 82.7% | 82.7% | +2.7 | n/a | no target |
| P06 | 269 | 69.9% | 69.9% | +1.0 | 40% | ✅ met |
| P07 | 757 | 65.4% | 65.4% | +0.5 | 85% | ❌ 20 pts to go |
| P08 | 27027 | 64.5% | 64.5% | -0.8 | 85% | ❌ 20 pts to go |
| P09 | 277 | 56.7% | 56.7% | -2.6 | 85% | ❌ 28 pts to go |
| P10 | 2128 | 66.1% | 66.1% | +2.6 | 85% | ❌ 19 pts to go |
| P11 | 1776 | 68.5% | 68.5% | +6.6 | 75% | 🟡 6 pts to go |
| P12 | 10 | 40.0% | 40.0% | +13.3 | n/a | no target |
| P13 | 153569 | 91.8% | 91.8% | +0.6 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 39.9% | 39.9% | -16.7 | n/a | no target |
| P01T | 228 | 98.2% | 98.2% | +0.8 | n/a | no target |
| P01_GOLD | 630 | 78.6% | 78.6% | -1.0 | 90% | ❌ 11 pts to go |
| P02 | 464 | 82.1% | 82.1% | -1.8 | 90% | 🟡 8 pts to go |
| P03 | 265 | 85.3% | 85.3% | -2.5 | 90% | 🟡 5 pts to go |
| P04 | 3568 | 82.8% | 82.8% | -1.6 | 85% | 🟡 2 pts to go |
| P05 | 423 | 44.7% | 44.7% | -0.1 | 70% | ❌ 25 pts to go |
| P06M | 20378 | 34.8% | 34.8% | -8.8 | n/a | no target |
| P06T | 59777 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 269 | 99.3% | 99.3% | +0.0 | 50% | ✅ met |
| P07 | 757 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 27027 | 99.9% | 99.9% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 277 | 78.3% | 78.3% | -1.5 | 100% | ❌ 22 pts to go |
| P10 | 2128 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1776 | 97.9% | 97.9% | +0.6 | 100% | 🟡 2 pts to go |
| P12 | 10 | 60.0% | 60.0% | +6.7 | n/a | no target |
| P13 | 153569 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 16.1% | 16.1% | +0.6 | n/a | no target |
| P01T | 228 | 59.6% | 59.6% | -5.5 | n/a | no target |
| P01_GOLD | 630 | 43.2% | 43.2% | -0.3 | 70% | ❌ 27 pts to go |
| P02 | 464 | 47.4% | 47.4% | -1.3 | 75% | ❌ 28 pts to go |
| P03 | 265 | 44.5% | 44.5% | +1.2 | 75% | ❌ 30 pts to go |
| P04 | 3568 | 38.8% | 38.8% | +0.1 | 70% | ❌ 31 pts to go |
| P05 | 423 | 21.5% | 21.5% | -0.5 | 55% | ❌ 34 pts to go |
| P06M | 20378 | 5.5% | 5.5% | +0.7 | n/a | no target |
| P06T | 59777 | 47.4% | 47.4% | -14.7 | n/a | no target |
| P06 | 269 | 52.8% | 52.8% | +5.9 | n/a | no target |
| P07 | 757 | 51.9% | 51.9% | +1.9 | 70% | ❌ 18 pts to go |
| P08 | 27027 | 55.4% | 55.4% | +0.6 | 75% | ❌ 20 pts to go |
| P09 | 277 | 47.7% | 47.7% | -1.5 | 85% | ❌ 37 pts to go |
| P10 | 2128 | 44.4% | 44.4% | +0.8 | 80% | ❌ 36 pts to go |
| P11 | 1776 | 53.5% | 53.5% | -0.8 | 70% | ❌ 16 pts to go |
| P12 | 10 | 30.0% | 30.0% | -10.0 | n/a | no target |
| P13 | 153569 | 5.4% | 5.4% | +0.2 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 39.9% | 39.9% | -16.7 | n/a | no target |
| P01T | 228 | 96.5% | 96.5% | +1.7 | n/a | no target |
| P01_GOLD | 630 | 72.9% | 72.9% | -0.9 | 90% | ❌ 17 pts to go |
| P02 | 464 | 76.9% | 76.9% | -2.1 | 90% | ❌ 13 pts to go |
| P03 | 265 | 81.9% | 81.9% | -1.4 | 90% | 🟡 8 pts to go |
| P04 | 3568 | 77.8% | 77.8% | +1.4 | 85% | 🟡 7 pts to go |
| P05 | 423 | 43.0% | 43.0% | -0.1 | 75% | ❌ 32 pts to go |
| P06M | 20378 | 34.7% | 34.7% | -8.6 | n/a | no target |
| P06T | 59777 | 98.3% | 98.3% | +1.6 | n/a | no target |
| P06 | 269 | 91.1% | 91.1% | +0.6 | n/a | no target |
| P07 | 757 | 91.9% | 91.9% | -0.6 | 100% | 🟡 8 pts to go |
| P08 | 27027 | 88.1% | 88.1% | -2.7 | 100% | ❌ 12 pts to go |
| P09 | 277 | 66.8% | 66.8% | +0.7 | n/a | no target |
| P10 | 2128 | 90.3% | 90.3% | +3.5 | 100% | 🟡 10 pts to go |
| P11 | 1776 | 90.4% | 90.4% | +2.7 | n/a | no target |
| P12 | 10 | 60.0% | 60.0% | +13.3 | n/a | no target |
| P13 | 153569 | 69.6% | 69.6% | +4.4 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 39.0% | 39.0% | -7.5 | n/a | no target · QC vendors: 48 rows, 100.0% filled |
| P01T | 228 | 19.3% | 19.3% | +9.9 | n/a | no target · QC vendors: 33 rows, 87.9% filled |
| P01_GOLD | 630 | 43.0% | 43.0% | -0.8 | 95% | ❌ 52 pts to go · QC vendors: 49 rows, 98.0% filled |
| P02 | 464 | 56.5% | 56.5% | +0.9 | 95% | ❌ 38 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 265 | 42.3% | 42.3% | -3.7 | 95% | ❌ 53 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3568 | 32.5% | 32.5% | +0.3 | 95% | ❌ 62 pts to go · QC vendors: 600 rows, 98.0% filled |
| P05 | 423 | 14.2% | 14.2% | +0.2 | n/a | no target · QC vendors: 36 rows, 100.0% filled |
| P06M | 20378 | 38.6% | 38.6% | -4.2 | n/a | no target · QC vendors: 6453 rows, 99.9% filled |
| P06T | 59777 | 30.6% | 30.6% | +25.3 | n/a | no target · QC vendors: 18592 rows, 95.7% filled |
| P06 | 269 | 7.4% | 7.4% | -1.0 | n/a | no target · QC vendors: 13 rows, 69.2% filled |
| P07 | 757 | 7.0% | 7.0% | +0.7 | n/a | no target · QC vendors: 48 rows, 79.2% filled |
| P08 | 27027 | 6.9% | 6.9% | +0.3 | n/a | no target · QC vendors: 1680 rows, 94.7% filled |
| P09 | 277 | 74.0% | 74.0% | -2.9 | 95% | ❌ 21 pts to go · QC vendors: 100 rows, 100.0% filled |
| P10 | 2128 | 15.7% | 15.7% | +0.1 | n/a | no target · QC vendors: 202 rows, 92.6% filled |
| P11 | 1776 | 19.7% | 19.7% | +4.9 | n/a | no target · QC vendors: 298 rows, 94.6% filled |
| P12 | 10 | 80.0% | 80.0% | +6.7 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 153569 | 22.4% | 22.4% | -3.8 | n/a | no target · QC vendors: 34398 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 49.3% | 49.3% | -9.6 | n/a | no target · vendors with a registry record: 110 rows, 100.0% filled |
| P01T | 228 | 59.6% | 59.6% | +8.6 | n/a | no target · vendors with a registry record: 136 rows, 100.0% filled |
| P01_GOLD | 630 | 80.8% | 80.8% | -0.7 | 100% | ❌ 19 pts to go · vendors with a registry record: 509 rows, 100.0% filled |
| P02 | 464 | 78.4% | 78.4% | +0.9 | 100% | ❌ 22 pts to go · vendors with a registry record: 364 rows, 100.0% filled |
| P03 | 265 | 78.1% | 78.1% | -2.9 | 100% | ❌ 22 pts to go · vendors with a registry record: 207 rows, 100.0% filled |
| P04 | 3568 | 54.1% | 54.1% | +4.4 | 100% | ❌ 46 pts to go · vendors with a registry record: 1929 rows, 100.0% filled |
| P05 | 423 | 62.9% | 62.9% | -0.4 | n/a | no target · vendors with a registry record: 266 rows, 100.0% filled |
| P06M | 20378 | 41.9% | 41.9% | -4.0 | n/a | no target · vendors with a registry record: 8541 rows, 100.0% filled |
| P06T | 59777 | 67.6% | 67.6% | +11.4 | n/a | no target · vendors with a registry record: 40383 rows, 100.0% filled |
| P06 | 269 | 41.3% | 41.3% | -0.1 | n/a | no target · vendors with a registry record: 111 rows, 100.0% filled |
| P07 | 757 | 33.8% | 33.8% | +1.5 | n/a | no target · vendors with a registry record: 256 rows, 100.0% filled |
| P08 | 27027 | 32.1% | 32.1% | +1.7 | n/a | no target · vendors with a registry record: 8679 rows, 100.0% filled |
| P09 | 277 | 89.9% | 89.9% | -0.7 | n/a | no target · vendors with a registry record: 249 rows, 100.0% filled |
| P10 | 2128 | 40.1% | 40.1% | +3.9 | n/a | no target · vendors with a registry record: 854 rows, 100.0% filled |
| P11 | 1776 | 60.5% | 60.5% | +6.9 | n/a | no target · vendors with a registry record: 1074 rows, 100.0% filled |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 10 rows, 100.0% filled |
| P13 | 153569 | 40.4% | 40.4% | +13.5 | n/a | no target · vendors with a registry record: 62008 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 96.4% | 96.4% | +2.6 | 90% | ✅ met |
| P01T | 228 | 70.6% | 70.6% | -1.8 | 90% | ❌ 19 pts to go |
| P01_GOLD | 630 | 87.5% | 87.5% | -0.2 | 95% | 🟡 8 pts to go |
| P02 | 464 | 88.1% | 88.1% | +0.3 | 95% | 🟡 7 pts to go |
| P03 | 265 | 82.6% | 82.6% | -1.8 | 85% | 🟡 2 pts to go |
| P04 | 3568 | 64.5% | 64.5% | +1.5 | 90% | ❌ 26 pts to go |
| P05 | 423 | 77.8% | 77.8% | -1.3 | 75% | ✅ met |
| P06M | 20378 | 93.4% | 93.4% | +1.8 | n/a | no target |
| P06T | 59777 | 36.9% | 36.9% | -0.4 | n/a | no target |
| P06 | 269 | 72.5% | 72.5% | -1.1 | 80% | 🟡 8 pts to go |
| P07 | 757 | 58.7% | 58.8% | -1.1 | 80% | ❌ 21 pts to go |
| P08 | 27027 | 53.2% | 53.3% | -1.2 | 75% | ❌ 22 pts to go |
| P09 | 277 | 75.1% | 75.1% | -1.8 | 95% | ❌ 20 pts to go |
| P10 | 2128 | 46.8% | 46.9% | +0.1 | 70% | ❌ 23 pts to go |
| P11 | 1776 | 31.8% | 31.8% | +0.5 | 65% | ❌ 33 pts to go |
| P12 | 10 | 80.0% | 80.0% | +0.0 | 80% | ✅ met |
| P13 | 153569 | 45.7% | 45.7% | -1.8 | 60% | ❌ 14 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 20.2% | 20.2% | +0.0 | 50% | ❌ 30 pts to go |
| P01T | 228 | 15.8% | 15.8% | -0.3 | n/a | no target |
| P01_GOLD | 630 | 19.4% | 19.4% | -0.1 | 40% | ❌ 21 pts to go |
| P02 | 464 | 20.3% | 20.3% | +1.2 | 40% | ❌ 20 pts to go |
| P03 | 265 | 20.4% | 20.4% | -0.9 | 40% | ❌ 20 pts to go |
| P04 | 3568 | 16.2% | 16.2% | +1.0 | 40% | ❌ 24 pts to go |
| P05 | 423 | 20.8% | 20.8% | +3.3 | 25% | 🟡 4 pts to go |
| P06M | 20378 | 22.3% | 22.3% | +10.7 | n/a | no target |
| P06T | 59777 | 7.5% | 7.5% | +0.6 | n/a | no target |
| P06 | 269 | 19.3% | 19.3% | +6.5 | 35% | ❌ 16 pts to go |
| P07 | 757 | 19.9% | 19.9% | +5.8 | 35% | ❌ 15 pts to go |
| P08 | 27027 | 19.5% | 19.5% | +4.1 | 35% | ❌ 16 pts to go |
| P09 | 277 | 16.6% | 16.6% | +0.3 | n/a | no target |
| P10 | 2128 | 7.1% | 7.1% | +0.4 | 30% | ❌ 23 pts to go |
| P11 | 1776 | 6.6% | 6.6% | -0.8 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +13.3 | n/a | no target |
| P13 | 153569 | 12.6% | 12.6% | +0.3 | 30% | ❌ 17 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 228 | 85.1% | 85.1% | +0.7 | 100% | ❌ 15 pts to go |
| P01_GOLD | 630 | 90.8% | 90.8% | +0.1 | 100% | 🟡 9 pts to go |
| P02 | 464 | 96.6% | 96.6% | +1.1 | 100% | 🟡 3 pts to go |
| P03 | 265 | 89.1% | 89.1% | -0.3 | 100% | ❌ 11 pts to go |
| P04 | 3568 | 72.6% | 72.6% | +1.2 | 100% | ❌ 27 pts to go |
| P05 | 423 | 90.1% | 90.1% | +0.8 | 100% | 🟡 10 pts to go |
| P06M | 20378 | 99.5% | 99.5% | +0.3 | n/a | no target |
| P06T | 59777 | 58.6% | 58.6% | -0.7 | n/a | no target |
| P06 | 269 | 81.8% | 81.8% | +3.0 | 95% | ❌ 13 pts to go |
| P07 | 757 | 84.1% | 84.1% | +2.9 | 95% | ❌ 11 pts to go |
| P08 | 27027 | 83.2% | 83.2% | +4.9 | 95% | ❌ 12 pts to go |
| P09 | 277 | 96.4% | 96.4% | +0.3 | 100% | 🟡 4 pts to go |
| P10 | 2128 | 54.7% | 54.7% | +0.3 | 95% | ❌ 40 pts to go |
| P11 | 1776 | 60.6% | 60.6% | +11.2 | 80% | ❌ 19 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 153569 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 76.7% | 76.7% | -9.3 | n/a | no target |
| P01T | 228 | 75.0% | 75.0% | +6.8 | n/a | no target |
| P01_GOLD | 630 | 73.2% | 73.2% | +0.2 | 90% | ❌ 17 pts to go |
| P02 | 464 | 79.1% | 79.1% | +1.2 | 95% | ❌ 16 pts to go |
| P03 | 265 | 74.0% | 74.0% | -0.9 | 95% | ❌ 21 pts to go |
| P04 | 3568 | 69.7% | 69.7% | +0.8 | 95% | ❌ 25 pts to go |
| P05 | 423 | 72.6% | 72.6% | -0.9 | 90% | ❌ 17 pts to go |
| P06M | 20378 | 83.3% | 83.3% | -3.6 | n/a | no target |
| P06T | 59777 | 58.6% | 58.6% | +1.4 | n/a | no target |
| P06 | 269 | 67.3% | 67.3% | -1.2 | 95% | ❌ 28 pts to go |
| P07 | 757 | 61.3% | 61.3% | -3.5 | 90% | ❌ 29 pts to go |
| P08 | 27027 | 61.8% | 61.8% | -6.0 | 95% | ❌ 33 pts to go |
| P09 | 277 | 85.9% | 85.9% | -1.1 | 100% | ❌ 14 pts to go |
| P10 | 2128 | 53.8% | 53.8% | -1.5 | 95% | ❌ 41 pts to go |
| P11 | 1776 | 31.0% | 31.0% | +2.1 | 75% | ❌ 44 pts to go |
| P12 | 10 | 80.0% | 80.0% | -13.3 | n/a | no target |
| P13 | 153569 | 68.0% | 68.0% | -2.8 | 95% | ❌ 27 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 90.6% | 90.6% | +3.0 | n/a | no target |
| P01T | 228 | 91.2% | 91.2% | +7.9 | 95% | 🟡 4 pts to go |
| P01_GOLD | 630 | 84.9% | 84.9% | +0.1 | 90% | 🟡 5 pts to go |
| P02 | 464 | 90.9% | 90.9% | +0.3 | 95% | 🟡 4 pts to go |
| P03 | 265 | 83.4% | 83.4% | -2.2 | 95% | ❌ 12 pts to go |
| P04 | 3568 | 91.8% | 91.8% | +2.6 | 90% | ✅ met |
| P05 | 423 | 92.4% | 92.4% | -0.7 | 95% | 🟡 3 pts to go |
| P06M | 20378 | 92.8% | 92.8% | -0.4 | n/a | no target |
| P06T | 59777 | 84.7% | 84.7% | +9.8 | n/a | no target |
| P06 | 269 | 88.5% | 88.5% | -3.8 | 100% | ❌ 12 pts to go |
| P07 | 757 | 86.5% | 86.5% | -5.7 | 100% | ❌ 14 pts to go |
| P08 | 27027 | 83.2% | 83.2% | -9.1 | 100% | ❌ 17 pts to go |
| P09 | 277 | 74.0% | 74.0% | +1.0 | n/a | no target |
| P10 | 2128 | 94.4% | 94.4% | +3.1 | 100% | 🟡 6 pts to go |
| P11 | 1776 | 51.6% | 51.6% | +9.7 | 80% | ❌ 28 pts to go |
| P12 | 10 | 90.0% | 90.0% | -10.0 | n/a | no target |
| P13 | 153569 | 80.8% | 80.8% | -2.9 | 95% | ❌ 14 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 3.1% | 3.1% | +0.0 | n/a | no target |
| P01T | 228 | 8.8% | 8.8% | -0.6 | n/a | no target |
| P01_GOLD | 630 | 13.8% | 13.8% | -0.4 | 25% | ❌ 11 pts to go |
| P02 | 464 | 25.0% | 25.0% | -0.3 | 40% | ❌ 15 pts to go |
| P03 | 265 | 8.7% | 8.7% | -0.4 | 20% | ❌ 11 pts to go |
| P04 | 3568 | 3.7% | 3.7% | +0.2 | 20% | ❌ 16 pts to go |
| P05 | 423 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 20378 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 59777 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 269 | 5.2% | 5.2% | +0.1 | n/a | no target |
| P07 | 757 | 7.9% | 7.9% | -0.6 | n/a | no target |
| P08 | 27027 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 277 | 8.3% | 8.3% | +0.5 | n/a | no target |
| P10 | 2128 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1776 | 0.7% | 0.7% | -0.3 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 153569 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 17.0% | 17.0% | -1.6 | n/a | no target |
| P01T | 228 | 19.7% | 19.7% | -2.7 | 70% | ❌ 50 pts to go |
| P01_GOLD | 630 | 43.7% | 43.7% | +0.2 | 80% | ❌ 36 pts to go |
| P02 | 464 | 57.8% | 57.8% | +0.5 | 90% | ❌ 32 pts to go |
| P03 | 265 | 19.2% | 19.2% | +0.6 | 60% | ❌ 41 pts to go |
| P04 | 3568 | 21.5% | 21.5% | -0.1 | 85% | ❌ 64 pts to go |
| P05 | 423 | 11.6% | 11.6% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 20378 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06T | 59777 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P06 | 269 | 13.8% | 13.8% | -1.6 | n/a | no target |
| P07 | 757 | 9.0% | 9.0% | -1.5 | n/a | no target |
| P08 | 27027 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 277 | 74.7% | 74.7% | -3.2 | 95% | ❌ 20 pts to go |
| P10 | 2128 | 1.6% | 1.6% | -0.1 | n/a | no target |
| P11 | 1776 | 13.4% | 13.4% | -3.3 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | +3.3 | n/a | no target |
| P13 | 153569 | 0.3% | 0.3% | -0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 6.3% | 6.3% | +0.1 | n/a | no target |
| P01T | 228 | 9.6% | 9.6% | -0.8 | n/a | no target |
| P01_GOLD | 630 | 34.6% | 34.6% | +0.6 | 70% | ❌ 35 pts to go |
| P02 | 464 | 39.4% | 39.4% | +0.3 | 75% | ❌ 36 pts to go |
| P03 | 265 | 19.6% | 19.6% | +1.0 | 55% | ❌ 35 pts to go |
| P04 | 3568 | 21.5% | 21.5% | -0.1 | 75% | ❌ 54 pts to go |
| P05 | 423 | 10.6% | 10.6% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 20378 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 59777 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 269 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P07 | 757 | 4.6% | 4.6% | -0.6 | n/a | no target |
| P08 | 27027 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 277 | 71.5% | 71.5% | -3.7 | 95% | ❌ 24 pts to go |
| P10 | 2128 | 0.8% | 0.8% | -0.1 | n/a | no target |
| P11 | 1776 | 13.2% | 13.2% | -3.2 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 8.5% | 8.5% | +0.7 | n/a | no target |
| P01T | 228 | 8.3% | 8.3% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 464 | 45.5% | 45.7% | -0.2 | 75% | ❌ 30 pts to go |
| P03 | 265 | 37.0% | 37.0% | -0.3 | 70% | ❌ 33 pts to go |
| P04 | 3568 | 21.4% | 21.8% | +0.3 | 70% | ❌ 49 pts to go |
| P05 | 423 | 14.4% | 14.4% | +0.2 | 50% | ❌ 36 pts to go |
| P06M | 20378 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 59777 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 269 | 14.1% | 14.1% | -2.4 | n/a | no target |
| P07 | 757 | 1.3% | 1.3% | -0.7 | n/a | no target |
| P08 | 27027 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 277 | 48.7% | 48.7% | +2.1 | 80% | ❌ 31 pts to go |
| P10 | 2128 | 1.1% | 1.2% | -0.1 | n/a | no target |
| P11 | 1776 | 4.8% | 4.8% | -2.0 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | -10.0 | n/a | no target |
| P13 | 153569 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 16.6% | 16.6% | -2.0 | n/a | no target |
| P01T | 228 | 19.3% | 19.3% | -2.1 | 60% | ❌ 41 pts to go |
| P01_GOLD | 630 | 62.7% | 62.7% | -0.7 | 70% | 🟡 7 pts to go |
| P02 | 464 | 39.0% | 39.0% | -0.7 | 50% | ❌ 11 pts to go |
| P03 | 265 | 47.2% | 47.2% | -1.1 | 55% | 🟡 8 pts to go |
| P04 | 3568 | 12.7% | 12.7% | +0.5 | 40% | ❌ 27 pts to go |
| P05 | 423 | 16.5% | 16.5% | -0.6 | 40% | ❌ 24 pts to go |
| P06M | 20378 | 3.1% | 3.1% | +0.9 | n/a | no target |
| P06T | 59777 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P06 | 269 | 18.6% | 18.6% | -3.4 | n/a | no target |
| P07 | 757 | 5.4% | 5.4% | -1.2 | n/a | no target |
| P08 | 27027 | 2.3% | 2.3% | -0.6 | n/a | no target |
| P09 | 277 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10 | 2128 | 5.1% | 5.1% | +0.5 | n/a | no target |
| P11 | 1776 | 4.1% | 4.1% | -1.1 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 153569 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 23.3% | 23.3% | +1.6 | n/a | no target |
| P01T | 228 | 27.2% | 27.2% | -1.4 | 65% | ❌ 38 pts to go |
| P01_GOLD | 630 | 68.4% | 68.4% | -0.6 | 70% | 🟡 2 pts to go |
| P02 | 464 | 23.7% | 23.7% | -0.5 | 50% | ❌ 26 pts to go |
| P03 | 265 | 50.2% | 50.2% | -2.3 | 60% | 🟡 10 pts to go |
| P04 | 3568 | 5.6% | 5.6% | +0.2 | 40% | ❌ 34 pts to go |
| P05 | 423 | 19.9% | 19.9% | +0.2 | 45% | ❌ 25 pts to go |
| P06M | 20378 | 1.9% | 1.9% | +0.5 | n/a | no target |
| P06T | 59777 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 269 | 30.5% | 30.5% | -3.9 | n/a | no target |
| P07 | 757 | 5.7% | 5.7% | -1.2 | n/a | no target |
| P08 | 27027 | 1.0% | 1.0% | -0.3 | n/a | no target |
| P09 | 277 | 10.8% | 10.8% | +1.0 | n/a | no target |
| P10 | 2128 | 3.3% | 3.3% | +0.2 | n/a | no target |
| P11 | 1776 | 3.8% | 3.8% | -1.3 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 153569 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 13.0% | 13.0% | +0.6 | n/a | no target |
| P01T | 228 | 12.3% | 12.3% | -1.2 | n/a | no target |
| P01_GOLD | 630 | 49.7% | 49.7% | -0.1 | 50% | 🟡 0 pts to go |
| P02 | 464 | 38.4% | 38.4% | +1.1 | n/a | no target |
| P03 | 265 | 51.3% | 51.3% | -0.8 | 60% | 🟡 9 pts to go |
| P04 | 3568 | 12.8% | 12.8% | +0.9 | n/a | no target |
| P05 | 423 | 15.1% | 15.1% | -0.1 | n/a | no target |
| P06M | 20378 | 0.8% | 0.8% | +0.3 | n/a | no target |
| P06T | 59777 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 269 | 21.9% | 21.9% | -3.7 | n/a | no target |
| P07 | 757 | 6.5% | 6.5% | -1.8 | n/a | no target |
| P08 | 27027 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 277 | 20.9% | 20.9% | +3.3 | n/a | no target |
| P10 | 2128 | 2.5% | 2.5% | +0.1 | n/a | no target |
| P11 | 1776 | 2.8% | 2.8% | -1.9 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +6.7 | n/a | no target |
| P13 | 153569 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 9.9% | 9.9% | -1.7 | 15% | 🟡 5 pts to go |
| P01T | 228 | 12.7% | 12.7% | +0.2 | 15% | 🟡 2 pts to go |
| P01_GOLD | 630 | 35.1% | 35.1% | -0.2 | 40% | 🟡 5 pts to go |
| P02 | 464 | 12.1% | 12.3% | -0.8 | 25% | ❌ 13 pts to go |
| P03 | 265 | 15.8% | 15.8% | -1.7 | 25% | 🟡 9 pts to go |
| P04 | 3568 | 2.8% | 2.8% | +0.1 | 15% | ❌ 12 pts to go |
| P05 | 423 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 20378 | 0.8% | 0.8% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 59777 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 269 | 9.7% | 9.7% | -0.9 | 15% | 🟡 5 pts to go |
| P07 | 757 | 3.6% | 3.6% | -0.7 | 15% | ❌ 11 pts to go |
| P08 | 27027 | 0.5% | 0.5% | -0.1 | 15% | ❌ 14 pts to go |
| P09 | 277 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P10 | 2128 | 1.4% | 1.4% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1776 | 1.3% | 1.3% | -0.2 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 153569 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 6.3% | 6.3% | +0.9 | 15% | 🟡 9 pts to go |
| P01T | 228 | 11.0% | 11.0% | -0.5 | 25% | ❌ 14 pts to go |
| P01_GOLD | 630 | 28.9% | 28.9% | -0.3 | 25% | ✅ met |
| P02 | 464 | 25.4% | 25.4% | +0.1 | 15% | ✅ met |
| P03 | 265 | 22.3% | 22.3% | +0.2 | 15% | ✅ met |
| P04 | 3568 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 423 | 11.3% | 11.3% | +0.2 | 15% | 🟡 4 pts to go |
| P06M | 20378 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P06T | 59777 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 269 | 7.8% | 7.8% | -0.6 | 15% | 🟡 7 pts to go |
| P07 | 757 | 2.0% | 2.0% | -0.9 | 15% | ❌ 13 pts to go |
| P08 | 27027 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P09 | 277 | 1.4% | 1.4% | +0.4 | 15% | ❌ 14 pts to go |
| P10 | 2128 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1776 | 1.9% | 1.9% | -0.8 | 15% | ❌ 13 pts to go |
| P12 | 10 | 0.0% | 0.0% | -20.0 | 15% | ❌ 15 pts to go |
| P13 | 153569 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 1.8% | 1.8% | -0.5 | 20% | ❌ 18 pts to go |
| P01T | 228 | 3.1% | 3.1% | -1.1 | 20% | ❌ 17 pts to go |
| P01_GOLD | 630 | 4.3% | 4.3% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 464 | 1.7% | 1.7% | +0.2 | 20% | ❌ 18 pts to go |
| P03 | 265 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3568 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |
| P05 | 423 | 0.9% | 0.9% | -0.3 | 20% | ❌ 19 pts to go |
| P06M | 20378 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 269 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P07 | 757 | 0.3% | 0.3% | -0.1 | 20% | ❌ 20 pts to go |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 277 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2128 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1776 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 1.8% | 1.8% | +0.2 | 15% | ❌ 13 pts to go |
| P01T | 228 | 3.1% | 3.1% | +0.0 | 15% | ❌ 12 pts to go |
| P01_GOLD | 630 | 10.5% | 10.5% | +0.1 | 15% | 🟡 4 pts to go |
| P02 | 464 | 11.0% | 11.0% | -1.0 | 15% | 🟡 4 pts to go |
| P03 | 265 | 21.1% | 21.1% | +0.9 | 15% | ✅ met |
| P04 | 3568 | 2.4% | 2.4% | +0.1 | 15% | ❌ 13 pts to go |
| P05 | 423 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 20378 | 0.5% | 0.5% | +0.2 | 15% | ❌ 14 pts to go |
| P06T | 59777 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 269 | 4.5% | 4.5% | -0.6 | 15% | ❌ 10 pts to go |
| P07 | 757 | 1.3% | 1.3% | -0.3 | 15% | ❌ 14 pts to go |
| P08 | 27027 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P09 | 277 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2128 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1776 | 0.8% | 0.8% | -0.4 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | -6.7 | 15% | ❌ 15 pts to go |
| P13 | 153569 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 13.9% | 13.9% | -0.1 | 20% | 🟡 6 pts to go |
| P01T | 228 | 13.2% | 13.2% | -0.9 | 40% | ❌ 27 pts to go |
| P01_GOLD | 630 | 46.0% | 46.0% | -0.2 | 40% | ✅ met |
| P02 | 464 | 44.0% | 44.0% | +1.1 | 20% | ✅ met |
| P03 | 265 | 48.3% | 48.3% | -0.7 | 35% | ✅ met |
| P04 | 3568 | 14.9% | 14.9% | +0.7 | 20% | 🟡 5 pts to go |
| P05 | 423 | 15.6% | 15.6% | +0.2 | 20% | 🟡 4 pts to go |
| P06M | 20378 | 1.1% | 1.1% | +0.3 | 20% | ❌ 19 pts to go |
| P06T | 59777 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 269 | 22.7% | 22.7% | -2.6 | 20% | ✅ met |
| P07 | 757 | 7.0% | 7.0% | -1.6 | 20% | ❌ 13 pts to go |
| P08 | 27027 | 0.8% | 0.8% | -0.2 | 20% | ❌ 19 pts to go |
| P09 | 277 | 20.9% | 20.9% | +2.7 | 20% | ✅ met |
| P10 | 2128 | 3.8% | 3.8% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 1776 | 3.3% | 3.3% | -1.5 | 20% | ❌ 17 pts to go |
| P12 | 10 | 10.0% | 10.0% | +3.3 | 20% | 🟡 10 pts to go |
| P13 | 153569 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 19.7% | 19.7% | -13.6 | n/a | no target |
| P01T | 228 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 630 | 71.9% | 71.9% | +2.4 | 95% | ❌ 23 pts to go |
| P02 | 464 | 65.9% | 65.9% | +3.0 | 95% | ❌ 29 pts to go |
| P03 | 265 | 57.4% | 57.4% | +4.2 | 90% | ❌ 33 pts to go |
| P04 | 3568 | 26.5% | 26.5% | +1.7 | 85% | ❌ 58 pts to go |
| P05 | 423 | 38.8% | 38.8% | +1.1 | 75% | ❌ 36 pts to go |
| P06M | 20378 | 30.6% | 30.6% | -5.5 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 89.5% | 89.5% | +1.2 | 100% | ❌ 10 pts to go |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 4.0% | 4.0% | -2.0 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 19.7% | 19.7% | -13.6 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 73.7% | 73.7% | +0.9 | 100% | ❌ 26 pts to go |
| P02 | 464 | 68.1% | 68.1% | +1.8 | 100% | ❌ 32 pts to go |
| P03 | 265 | 60.0% | 60.0% | +1.1 | n/a | no target |
| P04 | 3568 | 27.0% | 27.0% | +1.5 | 95% | ❌ 68 pts to go |
| P05 | 423 | 34.5% | 34.5% | +1.1 | 80% | ❌ 46 pts to go |
| P06M | 20378 | 30.6% | 30.6% | -5.5 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 92.1% | 92.1% | +0.6 | 100% | 🟡 8 pts to go |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 4.2% | 4.2% | -2.2 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 85.7% | 85.7% | +5.9 | n/a | no target |
| P01T | 228 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 630 | 52.2% | 52.2% | +0.6 | 85% | ❌ 33 pts to go |
| P02 | 464 | 58.6% | 58.6% | +1.1 | 90% | ❌ 31 pts to go |
| P03 | 265 | 44.2% | 44.2% | +1.6 | 85% | ❌ 41 pts to go |
| P04 | 3568 | 29.0% | 29.0% | +1.1 | 90% | ❌ 61 pts to go |
| P05 | 423 | 32.9% | 32.9% | +0.2 | 75% | ❌ 42 pts to go |
| P06M | 20378 | 86.6% | 86.6% | -0.5 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 82.3% | 82.3% | -1.1 | 95% | ❌ 13 pts to go |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 3.4% | 3.4% | -2.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 70.9% | 70.9% | -7.4 | n/a | no target |
| P01T | 228 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 630 | 52.1% | 52.1% | +0.3 | 85% | ❌ 33 pts to go |
| P02 | 464 | 52.6% | 52.6% | +0.0 | 90% | ❌ 37 pts to go |
| P03 | 265 | 44.2% | 44.2% | +0.5 | 85% | ❌ 41 pts to go |
| P04 | 3568 | 24.7% | 24.7% | +0.9 | 90% | ❌ 65 pts to go |
| P05 | 423 | 42.6% | 42.6% | -0.8 | 75% | ❌ 32 pts to go |
| P06M | 20378 | 73.9% | 73.9% | -3.9 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 0.4% | 0.4% | +0.1 | 95% | ❌ 95 pts to go |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 2.6% | 2.6% | -1.9 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 94.6% | 94.6% | +4.7 | n/a | no target |
| P01T | 228 | 96.1% | 96.1% | +1.8 | n/a | no target |
| P01_GOLD | 630 | 85.4% | 85.6% | +0.1 | 100% | ❌ 15 pts to go |
| P02 | 464 | 77.6% | 77.6% | +1.2 | 100% | ❌ 22 pts to go |
| P03 | 265 | 91.7% | 91.7% | +0.4 | n/a | no target |
| P04 | 3568 | 50.7% | 50.7% | +1.9 | 95% | ❌ 44 pts to go |
| P05 | 423 | 77.3% | 77.3% | -0.2 | 95% | ❌ 18 pts to go |
| P06M | 20378 | 99.2% | 99.2% | +0.3 | n/a | no target |
| P06T | 59777 | 94.5% | 94.5% | +3.9 | n/a | no target |
| P06 | 269 | 21.2% | 21.2% | -1.9 | n/a | no target |
| P07 | 757 | 11.4% | 11.4% | -2.4 | n/a | no target |
| P08 | 27027 | 5.1% | 5.1% | -2.0 | n/a | no target |
| P09 | 277 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2128 | 70.7% | 70.7% | -0.3 | n/a | no target |
| P11 | 1776 | 71.3% | 71.3% | +3.2 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 99.6% | 99.6% | -0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 94.6% | 94.6% | +4.7 | n/a | no target |
| P01T | 228 | 96.1% | 96.1% | +1.8 | n/a | no target |
| P01_GOLD | 630 | 88.6% | 88.7% | +0.1 | 100% | ❌ 11 pts to go |
| P02 | 464 | 78.9% | 78.9% | +1.4 | 100% | ❌ 21 pts to go |
| P03 | 265 | 92.5% | 92.5% | +0.5 | n/a | no target |
| P04 | 3568 | 54.1% | 54.1% | +2.2 | 95% | ❌ 41 pts to go |
| P05 | 423 | 89.4% | 89.4% | -0.2 | 70% | ✅ met |
| P06M | 20378 | 99.2% | 99.2% | +0.3 | n/a | no target |
| P06T | 59777 | 94.5% | 94.5% | +3.9 | n/a | no target |
| P06 | 269 | 21.2% | 21.2% | -1.9 | n/a | no target |
| P07 | 757 | 11.4% | 11.4% | -2.4 | n/a | no target |
| P08 | 27027 | 5.1% | 5.1% | -2.0 | n/a | no target |
| P09 | 277 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2128 | 70.7% | 70.7% | -0.3 | n/a | no target |
| P11 | 1776 | 71.3% | 71.3% | +3.1 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 368 rows, 28.8% filled |
| P02 | 464 | 10.3% | 10.3% | -0.9 | n/a | no target · rows from a source that publishes bids: 295 rows, 16.3% filled |
| P03 | 265 | 13.6% | 13.6% | +0.7 | n/a | no target · rows from a source that publishes bids: 142 rows, 25.4% filled |
| P04 | 3568 | 1.7% | 1.7% | +0.2 | n/a | no target · rows from a source that publishes bids: 880 rows, 7.0% filled |
| P05 | 423 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 55 rows, 20.0% filled |
| P06M | 20378 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59777 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 4.0% | 4.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 264 rows, 4.2% filled |
| P10 | 2128 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1776 | 0.5% | 0.5% | -0.4 | n/a | no target · rows from a source that publishes bids: 69 rows, 11.6% filled |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 10 rows, 0.0% filled |
| P13 | 153569 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 97.8% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 53.3% | 82.2% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 464 | 52.8% | 86.4% | +0.4 | 90% | ❌ 37 pts to go |
| P03 | 265 | 45.7% | 80.0% | +1.2 | 90% | ❌ 44 pts to go |
| P04 | 3568 | 19.7% | 92.9% | +0.6 | 90% | ❌ 70 pts to go |
| P05 | 423 | 0.0% | 82.5% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 20378 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59777 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 277 | 2.9% | 4.7% | +0.6 | 90% | ❌ 87 pts to go |
| P10 | 2128 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1776 | 2.3% | 97.6% | -1.8 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.9% | 98.7% | +0.4 | n/a | no target |
| P01_GOLD | 630 | 26.3% | 55.2% | +0.4 | 90% | ❌ 64 pts to go |
| P02 | 464 | 51.9% | 85.6% | +0.4 | n/a | no target |
| P03 | 265 | 25.3% | 59.6% | +1.0 | n/a | no target |
| P04 | 3568 | 21.4% | 94.6% | +0.4 | n/a | no target |
| P05 | 423 | 0.5% | 83.0% | +0.0 | n/a | no target |
| P06M | 20378 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59777 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 277 | 40.4% | 42.2% | -0.6 | n/a | no target |
| P10 | 2128 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1776 | 2.4% | 97.7% | -1.3 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 228 | 2.2% | 100.0% | +0.1 | n/a | no target |
| P01_GOLD | 630 | 52.2% | 81.1% | +0.4 | 95% | ❌ 43 pts to go |
| P02 | 464 | 57.8% | 91.4% | +1.4 | n/a | no target |
| P03 | 265 | 49.8% | 84.2% | +3.0 | n/a | no target |
| P04 | 3568 | 22.2% | 95.4% | +1.0 | n/a | no target |
| P05 | 423 | 5.0% | 87.5% | +0.5 | n/a | no target |
| P06M | 20378 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59777 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 269 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 757 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 27027 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 277 | 61.0% | 62.8% | -1.5 | n/a | no target |
| P10 | 2128 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1776 | 2.4% | 97.7% | -1.7 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 153569 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 228 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3568 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 20378 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59777 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 269 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 757 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 27027 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2128 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1776 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 153569 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 228 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3568 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 20378 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59777 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 269 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 757 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 27027 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2128 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1776 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 153569 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 223 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 228 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3568 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 20378 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59777 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 269 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 757 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 27027 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2128 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1776 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 153569 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

