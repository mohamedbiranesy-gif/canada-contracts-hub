# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **49 of 438 met** (11.2%); 108 within 10 points; 281 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 146, P01T 185, P01_GOLD 641, P02 471, P03 271, P04 3629, P05 427, P06M 15872, P06T 37219, P06 257, P07 677, P08 21626, P09 314, P10R 0, P10 2168, P11 1512, P12 16, P13 144433

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 17.8% | 8 | vendor GST/HST number (131 rows) |
| P01T | 185 | 1.1% | 36.2% | 8 | payment terms (144 rows) |
| P01_GOLD | 641 | 24.3% | 70.8% | 10 | payment terms (224 rows) |
| P02 | 471 | 7.4% | 55.4% | 9 | PO rule (355 rows) |
| P03 | 271 | 14.8% | 58.3% | 9 | payment terms (133 rows) |
| P04 | 3629 | 1.2% | 17.9% | 6 | PO rule (3431 rows) |
| P05 | 427 | 1.2% | 17.8% | 7 | payment terms (352 rows) |
| P06M | 15872 | 0.0% | 3.0% | 7 | PO rule (15665 rows) |
| P06T | 37219 | 0.1% | 11.5% | 6 | PO rule (36989 rows) |
| P06 | 257 | 0.0% | 11.7% | 6 | reference to quote (PO / contract / vendor id) (257 rows) |
| P07 | 677 | 0.0% | 2.5% | 6 | reference to quote (PO / contract / vendor id) (677 rows) |
| P08 | 21626 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (21626 rows) |
| P09 | 314 | 1.3% | 45.2% | 8 | payment terms (293 rows) |
| P10 | 2168 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2168 rows) |
| P11 | 1512 | 0.2% | 7.5% | 6 | PO rule (1446 rows) |
| P12 | 16 | 0.0% | 50.0% | 9 | PO rule (15 rows) |
| P13 | 144433 | 0.0% | 0.2% | 6 | reference to quote (PO / contract / vendor id) (144433 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 146 | 8 | 30 | 108 | 0 | 0 | 71 |
| P01T | 185 | 23 | 36 | 126 | 0 | 0 | 71 |
| P01_GOLD | 641 | 230 | 207 | 204 | 0 | 0 | 82 |
| P02 | 471 | 0 | 199 | 272 | 0 | 0 | 66 |
| P03 | 271 | 0 | 0 | 258 | 13 | 0 | 57 |
| P04 | 3629 | 0 | 0 | 2988 | 641 | 0 | 46 |
| P05 | 427 | 15 | 30 | 369 | 13 | 0 | 51 |
| P06M | 15872 | 0 | 10 | 15798 | 64 | 0 | 46 |
| P06T | 37219 | 0 | 24 | 25647 | 11548 | 0 | 38 |
| P06 | 257 | 16 | 47 | 194 | 0 | 0 | 70 |
| P07 | 677 | 0 | 21 | 633 | 23 | 0 | 54 |
| P08 | 21626 | 0 | 0 | 19043 | 2583 | 0 | 44 |
| P09 | 314 | 4 | 12 | 297 | 1 | 0 | 53 |
| P10 | 2168 | 3 | 13 | 1472 | 680 | 0 | 41 |
| P11 | 1512 | 7 | 13 | 36 | 0 | 1456 | 25 |
| P12 | 16 | 0 | 0 | 16 | 0 | 0 | 54 |
| P13 | 144433 | 12 | 66 | 144342 | 13 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 146 | 110 | 75.3% | tax treatment (16) |
| P01T | 185 | 117 | 63.2% | bill-to legal name and address (53) |
| P01_GOLD | 641 | 488 | 76.1% | bill-to legal name and address (95) |
| P02 | 471 | 323 | 68.6% | the buyer's PO / reference rule (86) |
| P03 | 271 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (271) |
| P04 | 3629 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3629) |
| P05 | 427 | 47 | 11.0% | a confirmed invoicing / AP or finance channel (340) |
| P06M | 15872 | 165 | 1.0% | a confirmed invoicing / AP or finance channel (15657) |
| P06T | 37219 | 242 | 0.7% | a confirmed invoicing / AP or finance channel (36660) |
| P06 | 257 | 43 | 16.7% | the buyer's PO / reference rule (115) |
| P07 | 677 | 6 | 0.9% | the buyer's PO / reference rule (274) |
| P08 | 21626 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (21626) |
| P09 | 314 | 42 | 13.4% | a confirmed invoicing / AP or finance channel (262) |
| P10 | 2168 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2090) |
| P11 | 1512 | 14 | 0.9% | a confirmed invoicing / AP or finance channel (1456) |
| P12 | 16 | 4 | 25.0% | a confirmed invoicing / AP or finance channel (11) |
| P13 | 144433 | 45 | 0.0% | a confirmed invoicing / AP or finance channel (142242) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 146 | 6 | 4.1% | 7 | 0 | the vendor's GST/HST number (BN9) (129) |
| P01T | 185 | 70 | 37.8% | 4 | 0 | the vendor's GST/HST number (BN9) (69) |
| P01_GOLD | 641 | 407 | 63.5% | 11 | 0 | the vendor's GST/HST number (BN9) (159) |
| P02 | 471 | 214 | 45.4% | 21 | 0 | the vendor's GST/HST number (BN9) (206) |
| P03 | 271 | 17 | 6.3% | 0 | 137 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (98) |
| P04 | 3629 | 43 | 1.2% | 7 | 873 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2648) |
| P05 | 427 | 20 | 4.7% | 8 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (210) |
| P06M | 15872 | 6 | 0.0% | 11 | 415 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (15196) |
| P06T | 37219 | 234 | 0.6% | 15 | 9539 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (27065) |
| P06 | 257 | 25 | 9.7% | 49 | 0 | the vendor's GST/HST number (BN9) (119) |
| P07 | 677 | 6 | 0.9% | 110 | 34 | the vendor's GST/HST number (BN9) (308) |
| P08 | 21626 | 3 | 0.0% | 14 | 5005 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (16565) |
| P09 | 314 | 39 | 12.4% | 1 | 129 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (121) |
| P10 | 2168 | 7 | 0.3% | 14 | 271 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1794) |
| P11 | 1512 | 8 | 0.5% | 3 | 0 | a confirmed invoicing / AP or finance channel (1440) |
| P12 | 16 | 3 | 18.8% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5) |
| P13 | 144433 | 11 | 0.0% | 669 | 37040 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (105013) |
| **all** | 229864 | 1119 | 0.5% | 944 | 53571 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 138 | 0 | 0 | 0 | 80 | 8 | 0 | 115 | 121 | 4 |
| P01T | 162 | 0 | 0 | 0 | 89 | 47 | 23 | 131 | 145 | 7 |
| P01_GOLD | 411 | 0 | 0 | 0 | 13 | 77 | 30 | 204 | 239 | 61 |
| P02 | 471 | 0 | 471 | 0 | 38 | 51 | 15 | 355 | 284 | 24 |
| P03 | 271 | 0 | 271 | 0 | 17 | 43 | 26 | 131 | 141 | 24 |
| P04 | 3629 | 0 | 3629 | 0 | 1525 | 1288 | 969 | 3431 | 3176 | 164 |
| P05 | 412 | 0 | 360 | 0 | 79 | 88 | 38 | 343 | 354 | 53 |
| P06M | 15872 | 0 | 15872 | 0 | 10459 | 1225 | 100 | 15665 | 15545 | 245 |
| P06T | 37219 | 0 | 37219 | 0 | 32850 | 22923 | 14646 | 36989 | 36651 | 872 |
| P06 | 241 | 0 | 0 | 0 | 113 | 66 | 42 | 173 | 204 | 9 |
| P07 | 677 | 0 | 677 | 0 | 434 | 273 | 117 | 632 | 637 | 11 |
| P08 | 21626 | 0 | 21626 | 0 | 16469 | 9730 | 3811 | 21358 | 21015 | 410 |
| P09 | 310 | 0 | 289 | 0 | 13 | 73 | 1 | 283 | 296 | 48 |
| P10 | 2165 | 0 | 2132 | 0 | 1121 | 1180 | 983 | 2101 | 2063 | 113 |
| P11 | 1505 | 1456 | 1409 | 0 | 658 | 1037 | 465 | 1446 | 1448 | 60 |
| P12 | 16 | 0 | 14 | 0 | 1 | 4 | 0 | 15 | 15 | 1 |
| P13 | 144421 | 0 | 143999 | 0 | 111903 | 86680 | 20 | 144067 | 143265 | 38 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 59.4% | 95% | 51392 |
| buyer_logo_url | P13 | 72.9% | 95% | 31923 |
| buyer_bn_as_published | P13 | 9.4% | 30% | 29732 |
| buyer_legal_name_as_published | P13 | 40.0% | 60% | 28907 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 28850 |
| ap_system_hint | P13 | 0.4% | 20% | 28293 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 21530 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 21478 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 20792 |
| mta_sts | P13 | 92.9% | 100% | 10246 |
| tls_rpt | P13 | 92.9% | 100% | 10246 |
| bimi | P13 | 92.9% | 100% | 10246 |
| vendor_registered_address | P08 | 30.1% | 70% | 8620 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 7435 |
| ap_system_hint | P06T | 0.6% | 20% | 7213 |
| buyer_phone | P08 | 68.7% | 95% | 5695 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 5516 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 5505 |
| buyer_payment_method_preference | P06T | 0.5% | 15% | 5380 |
| invoice_reference_hint | P08 | 1.2% | 25% | 5139 |
| buyer_legal_name_as_published | P08 | 55.0% | 75% | 4324 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 4315 |
| buyer_bn_as_published | P08 | 15.3% | 35% | 4257 |
| vendor_bn9 | P08 | 30.6% | 50% | 4199 |
| vendor_phone | P08 | 65.8% | 85% | 4145 |
| ap_system_hint | P08 | 1.0% | 20% | 4111 |
| vendor_emails | P08 | 56.3% | 75% | 4035 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 3169 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3145 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3140 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3111 |
| ap_system_hint | P06M | 0.8% | 20% | 3046 |
| vendor_trading_name | P08 | 36.3% | 50% | 2957 |
| buyer_address | P08 | 82.4% | 95% | 2734 |
| average_contract_duration_days | P04 | 20.3% | 90% | 2529 |
| currency | P04 | 27.6% | 95% | 2446 |
| end_date | P04 | 25.2% | 90% | 2351 |
| buyer_esignature_preference | P06M | 0.3% | 15% | 2329 |
| buyer_tax_exempt_status | P06M | 0.5% | 15% | 2305 |
| ap_phone | P04 | 22.9% | 85% | 2253 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 90.4% | 90.4% | +1.3 | 50% | ✅ met |
| P01T | 185 | 94.1% | 94.1% | +0.3 | 50% | ✅ met |
| P01_GOLD | 641 | 92.4% | 94.5% | +0.2 | 95% | 🟡 3 pts to go |
| P02 | 471 | 74.9% | 76.6% | +0.9 | 95% | ❌ 20 pts to go |
| P03 | 271 | 80.8% | 84.5% | -0.6 | 95% | ❌ 14 pts to go |
| P04 | 3629 | 32.2% | 33.9% | +2.0 | 90% | ❌ 58 pts to go |
| P05 | 427 | 38.9% | 41.7% | +0.3 | 70% | ❌ 31 pts to go |
| P06M | 15872 | 91.8% | 91.8% | +0.0 | n/a | no target |
| P06T | 37219 | 98.8% | 98.8% | +0.2 | n/a | no target |
| P06 | 257 | 32.7% | 32.7% | -1.7 | 30% | ✅ met |
| P07 | 677 | 6.6% | 6.6% | -0.3 | 30% | ❌ 23 pts to go |
| P08 | 21626 | 1.2% | 1.2% | -0.1 | 25% | ❌ 24 pts to go |
| P09 | 314 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2168 | 3.1% | 3.2% | +0.0 | 25% | ❌ 22 pts to go |
| P11 | 1512 | 48.5% | 49.3% | +1.6 | 60% | ❌ 12 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 144433 | 99.5% | 99.5% | -0.2 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 185 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 641 | 5.9% | 5.9% | -0.2 | 50% | ❌ 44 pts to go |
| P02 | 471 | 6.4% | 6.4% | +0.2 | 50% | ❌ 44 pts to go |
| P03 | 271 | 1.5% | 1.5% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3629 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 427 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 15872 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 0.6% | 0.6% | -0.1 | 50% | ❌ 49 pts to go |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 84.2% | 84.2% | +2.0 | n/a | no target |
| P01T | 185 | 74.6% | 74.6% | +0.1 | 50% | ✅ met |
| P01_GOLD | 641 | 67.4% | 67.4% | +0.6 | 85% | ❌ 18 pts to go |
| P02 | 471 | 65.6% | 65.6% | +0.8 | 90% | ❌ 24 pts to go |
| P03 | 271 | 60.5% | 60.5% | +0.8 | 85% | ❌ 24 pts to go |
| P04 | 3629 | 29.7% | 29.7% | +2.1 | 85% | ❌ 55 pts to go |
| P05 | 427 | 29.3% | 29.3% | +0.4 | 60% | ❌ 31 pts to go |
| P06M | 15872 | 91.6% | 91.6% | +0.1 | n/a | no target |
| P06T | 37219 | 98.7% | 98.7% | +0.3 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 96.2% | 96.2% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 45.1% | 45.1% | +1.8 | 60% | ❌ 15 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 185 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 641 | 51.5% | 51.5% | +0.7 | 80% | ❌ 28 pts to go |
| P02 | 471 | 57.5% | 57.5% | +0.6 | 60% | 🟡 2 pts to go |
| P03 | 271 | 50.6% | 50.6% | +0.4 | 80% | ❌ 29 pts to go |
| P04 | 3629 | 24.7% | 24.7% | +1.8 | 50% | ❌ 25 pts to go |
| P05 | 427 | 11.7% | 11.7% | +0.3 | 40% | ❌ 28 pts to go |
| P06M | 15872 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 82.8% | 82.8% | -0.6 | 50% | ✅ met |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 4.5% | 4.5% | -1.1 | 40% | ❌ 36 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 185 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 61.3% | 61.3% | +0.9 | 85% | ❌ 24 pts to go |
| P02 | 471 | 57.1% | 57.1% | +0.9 | 90% | ❌ 33 pts to go |
| P03 | 271 | 59.0% | 59.0% | +0.4 | 85% | ❌ 26 pts to go |
| P04 | 3629 | 25.6% | 25.6% | +2.0 | 85% | ❌ 59 pts to go |
| P05 | 427 | 19.9% | 19.9% | +0.2 | 50% | ❌ 30 pts to go |
| P06M | 15872 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 5.0% | 5.0% | -1.0 | 60% | ❌ 55 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 185 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 13.4% | 13.4% | +0.5 | 60% | ❌ 47 pts to go |
| P02 | 471 | 6.2% | 6.2% | +0.2 | 50% | ❌ 44 pts to go |
| P03 | 271 | 7.7% | 7.7% | -0.7 | 50% | ❌ 42 pts to go |
| P04 | 3629 | 1.9% | 1.9% | +0.1 | 40% | ❌ 38 pts to go |
| P05 | 427 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 15872 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 3.5% | 3.5% | +0.2 | 50% | ❌ 46 pts to go |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 0.7% | 0.7% | -0.2 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 185 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 35.6% | 35.6% | +0.8 | 80% | ❌ 44 pts to go |
| P02 | 471 | 52.4% | 52.4% | +0.5 | 90% | ❌ 38 pts to go |
| P03 | 271 | 33.2% | 33.2% | +0.5 | 80% | ❌ 47 pts to go |
| P04 | 3629 | 23.0% | 23.0% | +1.4 | 85% | ❌ 62 pts to go |
| P05 | 427 | 5.6% | 5.6% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 15872 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 74.5% | 74.5% | +0.2 | 95% | ❌ 20 pts to go |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 3.5% | 3.5% | -0.8 | 50% | ❌ 46 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 185 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 8.4% | 8.4% | -0.1 | 50% | ❌ 42 pts to go |
| P02 | 471 | 6.4% | 6.4% | +0.2 | 50% | ❌ 44 pts to go |
| P03 | 271 | 1.8% | 1.8% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3629 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 15872 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 185 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 641 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 271 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3629 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 15872 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 37219 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 257 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 677 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21626 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2168 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1512 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 10.3% | 10.3% | -1.3 | 70% | ❌ 60 pts to go |
| P01T | 185 | 52.4% | 52.4% | +1.9 | 60% | 🟡 8 pts to go |
| P01_GOLD | 641 | 73.0% | 73.0% | -1.8 | 90% | ❌ 17 pts to go |
| P02 | 471 | 53.5% | 53.5% | -0.1 | 85% | ❌ 32 pts to go |
| P03 | 271 | 67.5% | 67.5% | -2.1 | 90% | ❌ 22 pts to go |
| P04 | 3629 | 35.5% | 35.5% | +0.5 | 75% | ❌ 40 pts to go |
| P05 | 427 | 53.2% | 53.2% | -1.5 | 50% | ✅ met |
| P06M | 15872 | 3.1% | 3.1% | -0.1 | n/a | no target |
| P06T | 37219 | 49.3% | 49.3% | +2.0 | n/a | no target |
| P06 | 257 | 43.2% | 43.2% | -0.8 | 40% | ✅ met |
| P07 | 677 | 32.8% | 32.8% | -0.2 | 50% | ❌ 17 pts to go |
| P08 | 21626 | 30.6% | 30.6% | +0.1 | 50% | ❌ 19 pts to go |
| P09 | 314 | 57.6% | 57.6% | -0.7 | 80% | ❌ 22 pts to go |
| P10 | 2168 | 34.5% | 34.5% | +0.0 | 40% | 🟡 6 pts to go |
| P11 | 1512 | 47.6% | 47.6% | +0.7 | 60% | ❌ 12 pts to go |
| P12 | 16 | 56.2% | 56.2% | -3.8 | 85% | ❌ 29 pts to go |
| P13 | 144433 | 29.0% | 29.0% | -2.7 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 58.2% | 58.2% | -1.5 | n/a | no target |
| P01T | 185 | 53.5% | 53.5% | +2.5 | n/a | no target |
| P01_GOLD | 641 | 71.5% | 71.5% | -1.2 | 95% | ❌ 24 pts to go |
| P02 | 471 | 74.7% | 74.7% | +0.9 | 95% | ❌ 20 pts to go |
| P03 | 271 | 69.4% | 69.4% | -2.5 | 95% | ❌ 26 pts to go |
| P04 | 3629 | 50.5% | 50.5% | +1.3 | 95% | ❌ 44 pts to go |
| P05 | 427 | 57.4% | 57.4% | -0.9 | 70% | ❌ 13 pts to go |
| P06M | 15872 | 45.2% | 45.2% | -0.8 | n/a | no target |
| P06T | 37219 | 58.3% | 58.3% | +2.1 | n/a | no target |
| P06 | 257 | 40.9% | 40.9% | -0.1 | 80% | ❌ 39 pts to go |
| P07 | 677 | 32.2% | 32.2% | +0.3 | 70% | ❌ 38 pts to go |
| P08 | 21626 | 30.1% | 30.1% | -0.2 | 70% | ❌ 40 pts to go |
| P09 | 314 | 86.3% | 86.3% | -0.3 | 100% | ❌ 14 pts to go |
| P10 | 2168 | 35.4% | 35.4% | -0.1 | 70% | ❌ 35 pts to go |
| P11 | 1512 | 53.2% | 53.2% | +0.7 | 75% | ❌ 22 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 24.4% | 24.4% | -2.5 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 20.5% | 20.5% | +3.4 | n/a | no target |
| P01T | 185 | 56.2% | 56.2% | +2.6 | n/a | no target |
| P01_GOLD | 641 | 48.4% | 48.4% | -1.4 | 60% | ❌ 12 pts to go |
| P02 | 471 | 56.3% | 56.3% | +0.1 | 60% | 🟡 4 pts to go |
| P03 | 271 | 55.4% | 55.4% | +0.3 | 60% | 🟡 5 pts to go |
| P04 | 3629 | 43.1% | 43.1% | +1.0 | 55% | ❌ 12 pts to go |
| P05 | 427 | 24.4% | 24.4% | -0.2 | 50% | ❌ 26 pts to go |
| P06M | 15872 | 7.2% | 7.2% | +0.4 | n/a | no target |
| P06T | 37219 | 51.4% | 51.4% | +0.5 | n/a | no target |
| P06 | 257 | 48.2% | 48.2% | +0.6 | n/a | no target |
| P07 | 677 | 41.9% | 41.9% | +1.0 | 55% | ❌ 13 pts to go |
| P08 | 21626 | 36.3% | 36.3% | +0.1 | 50% | ❌ 14 pts to go |
| P09 | 314 | 72.0% | 72.0% | -0.3 | 70% | ✅ met |
| P10 | 2168 | 47.8% | 47.8% | +1.0 | 55% | 🟡 7 pts to go |
| P11 | 1512 | 54.0% | 54.0% | +1.8 | 50% | ✅ met |
| P12 | 16 | 87.5% | 87.5% | +0.8 | n/a | no target |
| P13 | 144433 | 3.2% | 3.2% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 48.6% | 48.6% | -1.8 | n/a | no target |
| P01T | 185 | 75.1% | 75.1% | +0.6 | n/a | no target |
| P01_GOLD | 641 | 49.1% | 49.1% | -1.4 | 70% | ❌ 21 pts to go |
| P02 | 471 | 56.9% | 56.9% | -1.3 | 70% | ❌ 13 pts to go |
| P03 | 271 | 51.3% | 51.3% | +0.0 | 70% | ❌ 19 pts to go |
| P04 | 3629 | 55.2% | 55.2% | +1.1 | 65% | 🟡 10 pts to go |
| P05 | 427 | 28.8% | 28.8% | +0.4 | 60% | ❌ 31 pts to go |
| P06M | 15872 | 35.4% | 35.4% | -1.2 | n/a | no target |
| P06T | 37219 | 77.1% | 77.1% | -2.9 | n/a | no target |
| P06 | 257 | 70.8% | 70.8% | +1.9 | 40% | ✅ met |
| P07 | 677 | 65.6% | 65.6% | +0.7 | 85% | ❌ 19 pts to go |
| P08 | 21626 | 65.8% | 65.8% | +0.5 | 85% | ❌ 19 pts to go |
| P09 | 314 | 57.3% | 57.3% | -2.0 | 85% | ❌ 28 pts to go |
| P10 | 2168 | 66.0% | 66.0% | +2.5 | 85% | ❌ 19 pts to go |
| P11 | 1512 | 63.4% | 63.4% | +1.5 | 75% | ❌ 12 pts to go |
| P12 | 16 | 37.5% | 37.5% | +10.8 | n/a | no target |
| P13 | 144433 | 91.7% | 91.7% | +0.5 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 54.1% | 54.1% | -2.5 | n/a | no target |
| P01T | 185 | 97.8% | 97.8% | +0.4 | n/a | no target |
| P01_GOLD | 641 | 78.5% | 78.5% | -1.1 | 90% | ❌ 12 pts to go |
| P02 | 471 | 82.4% | 82.4% | -1.5 | 90% | 🟡 8 pts to go |
| P03 | 271 | 86.7% | 86.7% | -1.1 | 90% | 🟡 3 pts to go |
| P04 | 3629 | 83.3% | 83.3% | -1.1 | 85% | 🟡 2 pts to go |
| P05 | 427 | 45.0% | 45.0% | +0.2 | 70% | ❌ 25 pts to go |
| P06M | 15872 | 41.8% | 41.8% | -1.8 | n/a | no target |
| P06T | 37219 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 257 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 677 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 21626 | 99.9% | 99.9% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 314 | 78.0% | 78.0% | -1.8 | 100% | ❌ 22 pts to go |
| P10 | 2168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1512 | 97.5% | 97.5% | +0.2 | 100% | 🟡 2 pts to go |
| P12 | 16 | 56.2% | 56.2% | +2.9 | n/a | no target |
| P13 | 144433 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 17.8% | 17.8% | +2.3 | n/a | no target |
| P01T | 185 | 65.9% | 65.9% | +0.8 | n/a | no target |
| P01_GOLD | 641 | 42.1% | 42.1% | -1.4 | 70% | ❌ 28 pts to go |
| P02 | 471 | 48.2% | 48.2% | -0.5 | 75% | ❌ 27 pts to go |
| P03 | 271 | 43.9% | 43.9% | +0.6 | 75% | ❌ 31 pts to go |
| P04 | 3629 | 39.4% | 39.4% | +0.7 | 70% | ❌ 31 pts to go |
| P05 | 427 | 22.0% | 22.0% | +0.0 | 55% | ❌ 33 pts to go |
| P06M | 15872 | 4.9% | 4.9% | +0.1 | n/a | no target |
| P06T | 37219 | 64.1% | 64.1% | +2.0 | n/a | no target |
| P06 | 257 | 51.0% | 51.0% | +4.1 | n/a | no target |
| P07 | 677 | 51.4% | 51.4% | +1.4 | 70% | ❌ 19 pts to go |
| P08 | 21626 | 56.3% | 56.3% | +1.5 | 75% | ❌ 19 pts to go |
| P09 | 314 | 47.8% | 47.8% | -1.4 | 85% | ❌ 37 pts to go |
| P10 | 2168 | 44.2% | 44.2% | +0.6 | 80% | ❌ 36 pts to go |
| P11 | 1512 | 56.5% | 56.5% | +2.2 | 70% | ❌ 14 pts to go |
| P12 | 16 | 37.5% | 37.5% | -2.5 | n/a | no target |
| P13 | 144433 | 5.4% | 5.4% | +0.2 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 54.1% | 54.1% | -2.5 | n/a | no target |
| P01T | 185 | 95.7% | 95.7% | +0.9 | n/a | no target |
| P01_GOLD | 641 | 72.1% | 72.1% | -1.7 | 90% | ❌ 18 pts to go |
| P02 | 471 | 77.3% | 77.3% | -1.7 | 90% | ❌ 13 pts to go |
| P03 | 271 | 83.0% | 83.0% | -0.3 | 90% | 🟡 7 pts to go |
| P04 | 3629 | 78.1% | 78.1% | +1.7 | 85% | 🟡 7 pts to go |
| P05 | 427 | 43.6% | 43.6% | +0.5 | 75% | ❌ 31 pts to go |
| P06M | 15872 | 41.7% | 41.7% | -1.6 | n/a | no target |
| P06T | 37219 | 97.1% | 97.1% | +0.4 | n/a | no target |
| P06 | 257 | 92.2% | 92.2% | +1.7 | n/a | no target |
| P07 | 677 | 93.6% | 93.6% | +1.1 | 100% | 🟡 6 pts to go |
| P08 | 21626 | 92.8% | 92.8% | +2.0 | 100% | 🟡 7 pts to go |
| P09 | 314 | 66.2% | 66.2% | +0.1 | n/a | no target |
| P10 | 2168 | 89.9% | 89.9% | +3.1 | 100% | ❌ 10 pts to go |
| P11 | 1512 | 89.4% | 89.4% | +1.7 | n/a | no target |
| P12 | 16 | 56.2% | 56.2% | +9.5 | n/a | no target |
| P13 | 144433 | 68.0% | 68.0% | +2.8 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 46.6% | 46.6% | +0.1 | n/a | no target · QC vendors: 49 rows, 100.0% filled |
| P01T | 185 | 9.2% | 9.2% | -0.2 | n/a | no target · QC vendors: 4 rows, 75.0% filled |
| P01_GOLD | 641 | 42.9% | 42.9% | -0.9 | 95% | ❌ 52 pts to go · QC vendors: 51 rows, 98.0% filled |
| P02 | 471 | 56.5% | 56.5% | +0.9 | 95% | ❌ 38 pts to go · QC vendors: 113 rows, 100.0% filled |
| P03 | 271 | 46.1% | 46.1% | +0.1 | 95% | ❌ 49 pts to go · QC vendors: 22 rows, 100.0% filled |
| P04 | 3629 | 33.2% | 33.2% | +1.0 | 95% | ❌ 62 pts to go · QC vendors: 618 rows, 98.1% filled |
| P05 | 427 | 13.8% | 13.8% | -0.2 | n/a | no target · QC vendors: 35 rows, 94.3% filled |
| P06M | 15872 | 42.1% | 42.1% | -0.7 | n/a | no target · QC vendors: 5838 rows, 99.8% filled |
| P06T | 37219 | 4.9% | 4.9% | -0.4 | n/a | no target · QC vendors: 1823 rows, 76.9% filled |
| P06 | 257 | 8.2% | 8.2% | -0.2 | n/a | no target · QC vendors: 14 rows, 71.4% filled |
| P07 | 677 | 6.1% | 6.1% | -0.2 | n/a | no target · QC vendors: 35 rows, 74.3% filled |
| P08 | 21626 | 6.3% | 6.3% | -0.3 | n/a | no target · QC vendors: 1211 rows, 92.7% filled |
| P09 | 314 | 76.1% | 76.1% | -0.8 | 95% | ❌ 19 pts to go · QC vendors: 116 rows, 100.0% filled |
| P10 | 2168 | 15.2% | 15.2% | -0.4 | n/a | no target · QC vendors: 198 rows, 89.4% filled |
| P11 | 1512 | 13.8% | 13.8% | -1.0 | n/a | no target · QC vendors: 151 rows, 90.7% filled |
| P12 | 16 | 75.0% | 75.0% | +1.7 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 144433 | 23.9% | 23.9% | -2.3 | n/a | no target · QC vendors: 34492 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 57.5% | 57.5% | -1.4 | n/a | no target · vendors with a registry record: 84 rows, 100.0% filled |
| P01T | 185 | 53.5% | 53.5% | +2.5 | n/a | no target · vendors with a registry record: 99 rows, 100.0% filled |
| P01_GOLD | 641 | 79.7% | 79.7% | -1.8 | 100% | ❌ 20 pts to go · vendors with a registry record: 511 rows, 100.0% filled |
| P02 | 471 | 77.7% | 77.7% | +0.2 | 100% | ❌ 22 pts to go · vendors with a registry record: 366 rows, 100.0% filled |
| P03 | 271 | 78.2% | 78.2% | -2.8 | 100% | ❌ 22 pts to go · vendors with a registry record: 212 rows, 100.0% filled |
| P04 | 3629 | 51.2% | 51.2% | +1.5 | 100% | ❌ 49 pts to go · vendors with a registry record: 1859 rows, 100.0% filled |
| P05 | 427 | 62.1% | 62.1% | -1.2 | n/a | no target · vendors with a registry record: 265 rows, 100.0% filled |
| P06M | 15872 | 45.1% | 45.1% | -0.8 | n/a | no target · vendors with a registry record: 7156 rows, 100.0% filled |
| P06T | 37219 | 58.3% | 58.3% | +2.1 | n/a | no target · vendors with a registry record: 21712 rows, 100.0% filled |
| P06 | 257 | 41.6% | 41.6% | +0.2 | n/a | no target · vendors with a registry record: 107 rows, 100.0% filled |
| P07 | 677 | 32.8% | 32.8% | +0.5 | n/a | no target · vendors with a registry record: 222 rows, 100.0% filled |
| P08 | 21626 | 30.3% | 30.3% | -0.1 | n/a | no target · vendors with a registry record: 6552 rows, 100.0% filled |
| P09 | 314 | 90.1% | 90.1% | -0.5 | n/a | no target · vendors with a registry record: 283 rows, 100.0% filled |
| P10 | 2168 | 36.1% | 36.1% | -0.1 | n/a | no target · vendors with a registry record: 783 rows, 100.0% filled |
| P11 | 1512 | 54.0% | 54.0% | +0.4 | n/a | no target · vendors with a registry record: 817 rows, 100.0% filled |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 16 rows, 100.0% filled |
| P13 | 144433 | 24.4% | 24.4% | -2.5 | n/a | no target · vendors with a registry record: 35256 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 94.5% | 94.5% | +0.7 | 90% | ✅ met |
| P01T | 185 | 74.6% | 74.6% | +2.2 | 90% | ❌ 15 pts to go |
| P01_GOLD | 641 | 88.0% | 88.0% | +0.3 | 95% | 🟡 7 pts to go |
| P02 | 471 | 89.2% | 89.2% | +1.4 | 95% | 🟡 6 pts to go |
| P03 | 271 | 84.1% | 84.1% | -0.3 | 85% | 🟡 1 pts to go |
| P04 | 3629 | 64.5% | 64.5% | +1.5 | 90% | ❌ 26 pts to go |
| P05 | 427 | 79.4% | 79.4% | +0.3 | 75% | ✅ met |
| P06M | 15872 | 92.3% | 92.3% | +0.7 | n/a | no target |
| P06T | 37219 | 38.4% | 38.4% | +1.1 | n/a | no target |
| P06 | 257 | 74.3% | 74.3% | +0.7 | 80% | 🟡 6 pts to go |
| P07 | 677 | 59.7% | 59.8% | -0.1 | 80% | ❌ 20 pts to go |
| P08 | 21626 | 55.0% | 55.0% | +0.6 | 75% | ❌ 20 pts to go |
| P09 | 314 | 76.8% | 76.8% | -0.1 | 95% | ❌ 18 pts to go |
| P10 | 2168 | 45.6% | 45.6% | -1.1 | 70% | ❌ 24 pts to go |
| P11 | 1512 | 31.4% | 31.4% | +0.1 | 65% | ❌ 34 pts to go |
| P12 | 16 | 75.0% | 75.0% | -5.0 | 80% | 🟡 5 pts to go |
| P13 | 144433 | 40.0% | 40.0% | -7.5 | 60% | ❌ 20 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 17.8% | 17.8% | -2.4 | 50% | ❌ 32 pts to go |
| P01T | 185 | 14.6% | 14.6% | -1.5 | n/a | no target |
| P01_GOLD | 641 | 19.0% | 19.0% | -0.5 | 40% | ❌ 21 pts to go |
| P02 | 471 | 19.1% | 19.1% | +0.0 | 40% | ❌ 21 pts to go |
| P03 | 271 | 21.8% | 21.8% | +0.5 | 40% | ❌ 18 pts to go |
| P04 | 3629 | 14.9% | 14.9% | -0.3 | 40% | ❌ 25 pts to go |
| P05 | 427 | 17.6% | 17.6% | +0.1 | 25% | 🟡 7 pts to go |
| P06M | 15872 | 10.7% | 10.7% | -0.9 | n/a | no target |
| P06T | 37219 | 5.8% | 5.8% | -1.1 | n/a | no target |
| P06 | 257 | 12.1% | 12.1% | -0.7 | 35% | ❌ 23 pts to go |
| P07 | 677 | 14.2% | 14.2% | +0.1 | 35% | ❌ 21 pts to go |
| P08 | 21626 | 15.3% | 15.3% | -0.1 | 35% | ❌ 20 pts to go |
| P09 | 314 | 16.6% | 16.6% | +0.3 | n/a | no target |
| P10 | 2168 | 5.7% | 5.7% | -1.0 | 30% | ❌ 24 pts to go |
| P11 | 1512 | 6.9% | 6.9% | -0.5 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 144433 | 9.4% | 9.4% | -2.9 | 30% | ❌ 21 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 185 | 86.5% | 86.5% | +2.1 | 100% | ❌ 14 pts to go |
| P01_GOLD | 641 | 91.0% | 91.0% | +0.3 | 100% | 🟡 9 pts to go |
| P02 | 471 | 96.4% | 96.4% | +0.9 | 100% | 🟡 4 pts to go |
| P03 | 271 | 89.3% | 89.3% | -0.1 | 100% | ❌ 11 pts to go |
| P04 | 3629 | 72.7% | 72.7% | +1.3 | 100% | ❌ 27 pts to go |
| P05 | 427 | 90.4% | 90.4% | +1.1 | 100% | 🟡 10 pts to go |
| P06M | 15872 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06T | 37219 | 60.6% | 60.6% | +1.3 | n/a | no target |
| P06 | 257 | 82.1% | 82.1% | +3.3 | 95% | ❌ 13 pts to go |
| P07 | 677 | 82.4% | 82.4% | +1.2 | 95% | ❌ 13 pts to go |
| P08 | 21626 | 82.4% | 82.4% | +4.1 | 95% | ❌ 13 pts to go |
| P09 | 314 | 96.5% | 96.5% | +0.4 | 100% | 🟡 4 pts to go |
| P10 | 2168 | 54.6% | 54.6% | +0.2 | 95% | ❌ 40 pts to go |
| P11 | 1512 | 59.1% | 59.1% | +9.7 | 80% | ❌ 21 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 144433 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 80.8% | 80.8% | -5.2 | n/a | no target |
| P01T | 185 | 74.1% | 74.1% | +5.9 | n/a | no target |
| P01_GOLD | 641 | 72.9% | 72.9% | -0.1 | 90% | ❌ 17 pts to go |
| P02 | 471 | 77.7% | 77.7% | -0.2 | 95% | ❌ 17 pts to go |
| P03 | 271 | 73.8% | 73.8% | -1.1 | 95% | ❌ 21 pts to go |
| P04 | 3629 | 69.3% | 69.3% | +0.4 | 95% | ❌ 26 pts to go |
| P05 | 427 | 72.6% | 72.6% | -0.9 | 90% | ❌ 17 pts to go |
| P06M | 15872 | 84.5% | 84.5% | -2.4 | n/a | no target |
| P06T | 37219 | 59.9% | 59.9% | +2.7 | n/a | no target |
| P06 | 257 | 70.8% | 70.8% | +2.3 | 95% | ❌ 24 pts to go |
| P07 | 677 | 66.2% | 66.2% | +1.4 | 90% | ❌ 24 pts to go |
| P08 | 21626 | 68.7% | 68.7% | +0.9 | 95% | ❌ 26 pts to go |
| P09 | 314 | 86.6% | 86.6% | -0.4 | 100% | ❌ 13 pts to go |
| P10 | 2168 | 53.5% | 53.5% | -1.8 | 95% | ❌ 42 pts to go |
| P11 | 1512 | 30.9% | 30.9% | +2.0 | 75% | ❌ 44 pts to go |
| P12 | 16 | 87.5% | 87.5% | -5.8 | n/a | no target |
| P13 | 144433 | 59.4% | 59.4% | -11.4 | 95% | ❌ 36 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 88.4% | 88.4% | +0.8 | n/a | no target |
| P01T | 185 | 89.7% | 89.7% | +6.4 | 95% | 🟡 5 pts to go |
| P01_GOLD | 641 | 84.6% | 84.6% | -0.2 | 90% | 🟡 5 pts to go |
| P02 | 471 | 90.4% | 90.4% | -0.2 | 95% | 🟡 5 pts to go |
| P03 | 271 | 83.4% | 83.4% | -2.2 | 95% | ❌ 12 pts to go |
| P04 | 3629 | 90.2% | 90.2% | +1.0 | 90% | ✅ met |
| P05 | 427 | 92.3% | 92.3% | -0.8 | 95% | 🟡 3 pts to go |
| P06M | 15872 | 90.3% | 90.3% | -2.9 | n/a | no target |
| P06T | 37219 | 81.7% | 81.7% | +6.8 | n/a | no target |
| P06 | 257 | 93.0% | 93.0% | +0.7 | 100% | 🟡 7 pts to go |
| P07 | 677 | 92.6% | 92.6% | +0.4 | 100% | 🟡 7 pts to go |
| P08 | 21626 | 94.2% | 94.2% | +1.9 | 100% | 🟡 6 pts to go |
| P09 | 314 | 73.6% | 73.6% | +0.6 | n/a | no target |
| P10 | 2168 | 92.9% | 92.9% | +1.6 | 100% | 🟡 7 pts to go |
| P11 | 1512 | 49.3% | 49.3% | +7.4 | 80% | ❌ 31 pts to go |
| P12 | 16 | 93.8% | 93.8% | -6.2 | n/a | no target |
| P13 | 144433 | 72.9% | 72.9% | -10.8 | 95% | ❌ 22 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 2.7% | 2.7% | -0.4 | n/a | no target |
| P01T | 185 | 9.2% | 9.2% | -0.2 | n/a | no target |
| P01_GOLD | 641 | 13.9% | 13.9% | -0.3 | 25% | ❌ 11 pts to go |
| P02 | 471 | 25.1% | 25.1% | -0.2 | 40% | ❌ 15 pts to go |
| P03 | 271 | 8.9% | 8.9% | -0.2 | 20% | ❌ 11 pts to go |
| P04 | 3629 | 3.6% | 3.6% | +0.1 | 20% | ❌ 16 pts to go |
| P05 | 427 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 15872 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 37219 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 257 | 5.4% | 5.4% | +0.3 | n/a | no target |
| P07 | 677 | 8.6% | 8.6% | +0.1 | n/a | no target |
| P08 | 21626 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 314 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P10 | 2168 | 0.9% | 0.9% | +0.1 | n/a | no target |
| P11 | 1512 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 144433 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 16.4% | 16.4% | -2.2 | n/a | no target |
| P01T | 185 | 21.6% | 21.6% | -0.8 | 70% | ❌ 48 pts to go |
| P01_GOLD | 641 | 42.9% | 42.9% | -0.6 | 80% | ❌ 37 pts to go |
| P02 | 471 | 57.7% | 57.7% | +0.4 | 90% | ❌ 32 pts to go |
| P03 | 271 | 18.8% | 18.8% | +0.2 | 60% | ❌ 41 pts to go |
| P04 | 3629 | 22.9% | 22.9% | +1.3 | 85% | ❌ 62 pts to go |
| P05 | 427 | 11.9% | 11.9% | +0.3 | 50% | ❌ 38 pts to go |
| P06M | 15872 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 37219 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 257 | 16.0% | 16.0% | +0.6 | n/a | no target |
| P07 | 677 | 10.0% | 10.0% | -0.5 | n/a | no target |
| P08 | 21626 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 314 | 77.1% | 77.1% | -0.8 | 95% | ❌ 18 pts to go |
| P10 | 2168 | 1.6% | 1.6% | -0.1 | n/a | no target |
| P11 | 1512 | 15.7% | 15.7% | -1.0 | n/a | no target |
| P12 | 16 | 25.0% | 25.0% | -1.7 | n/a | no target |
| P13 | 144433 | 0.4% | 0.4% | -0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 5.5% | 5.5% | -0.7 | n/a | no target |
| P01T | 185 | 10.3% | 10.3% | -0.1 | n/a | no target |
| P01_GOLD | 641 | 34.0% | 34.0% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 471 | 39.5% | 39.5% | +0.4 | 75% | ❌ 36 pts to go |
| P03 | 271 | 18.8% | 18.8% | +0.2 | 55% | ❌ 36 pts to go |
| P04 | 3629 | 22.9% | 22.9% | +1.3 | 75% | ❌ 52 pts to go |
| P05 | 427 | 11.0% | 11.0% | +0.3 | 50% | ❌ 39 pts to go |
| P06M | 15872 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 37219 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 257 | 6.2% | 6.2% | +0.3 | n/a | no target |
| P07 | 677 | 5.0% | 5.0% | -0.2 | n/a | no target |
| P08 | 21626 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 314 | 74.5% | 74.5% | -0.7 | 95% | ❌ 20 pts to go |
| P10 | 2168 | 0.7% | 0.7% | -0.2 | n/a | no target |
| P11 | 1512 | 15.4% | 15.4% | -1.0 | n/a | no target |
| P12 | 16 | 18.8% | 18.8% | -1.2 | n/a | no target |
| P13 | 144433 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 6.8% | 6.8% | -1.0 | n/a | no target |
| P01T | 185 | 8.6% | 8.6% | +0.3 | n/a | no target |
| P01_GOLD | 641 | 57.9% | 58.0% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 471 | 45.9% | 46.1% | +0.2 | 75% | ❌ 29 pts to go |
| P03 | 271 | 37.6% | 37.6% | +0.3 | 70% | ❌ 32 pts to go |
| P04 | 3629 | 22.4% | 22.9% | +1.3 | 70% | ❌ 48 pts to go |
| P05 | 427 | 14.8% | 14.8% | +0.6 | 50% | ❌ 35 pts to go |
| P06M | 15872 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 37219 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 257 | 15.6% | 15.6% | -0.9 | n/a | no target |
| P07 | 677 | 1.8% | 1.8% | -0.2 | n/a | no target |
| P08 | 21626 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 314 | 47.1% | 47.1% | +0.5 | 80% | ❌ 33 pts to go |
| P10 | 2168 | 1.1% | 1.2% | -0.1 | n/a | no target |
| P11 | 1512 | 6.0% | 6.1% | -0.8 | n/a | no target |
| P12 | 16 | 37.5% | 37.5% | -2.5 | n/a | no target |
| P13 | 144433 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 17.1% | 17.1% | -1.5 | n/a | no target |
| P01T | 185 | 21.6% | 21.6% | +0.2 | 60% | ❌ 38 pts to go |
| P01_GOLD | 641 | 62.7% | 62.7% | -0.7 | 70% | 🟡 7 pts to go |
| P02 | 471 | 39.7% | 39.7% | +0.0 | 50% | ❌ 10 pts to go |
| P03 | 271 | 48.0% | 48.0% | -0.3 | 55% | 🟡 7 pts to go |
| P04 | 3629 | 12.5% | 12.5% | +0.3 | 40% | ❌ 28 pts to go |
| P05 | 427 | 17.1% | 17.1% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 15872 | 2.1% | 2.1% | -0.1 | n/a | no target |
| P06T | 37219 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P06 | 257 | 20.6% | 20.6% | -1.4 | n/a | no target |
| P07 | 677 | 5.9% | 5.9% | -0.7 | n/a | no target |
| P08 | 21626 | 2.8% | 2.8% | -0.1 | n/a | no target |
| P09 | 314 | 5.7% | 5.7% | -0.2 | n/a | no target |
| P10 | 2168 | 4.8% | 4.8% | +0.2 | n/a | no target |
| P11 | 1512 | 4.2% | 4.2% | -1.0 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 144433 | 0.8% | 0.8% | -0.2 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 21.2% | 21.2% | -0.5 | n/a | no target |
| P01T | 185 | 29.2% | 29.2% | +0.6 | 65% | ❌ 36 pts to go |
| P01_GOLD | 641 | 68.2% | 68.2% | -0.8 | 70% | 🟡 2 pts to go |
| P02 | 471 | 24.6% | 24.6% | +0.4 | 50% | ❌ 25 pts to go |
| P03 | 271 | 51.7% | 51.7% | -0.8 | 60% | 🟡 8 pts to go |
| P04 | 3629 | 5.5% | 5.5% | +0.1 | 40% | ❌ 34 pts to go |
| P05 | 427 | 19.7% | 19.7% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 15872 | 1.3% | 1.3% | -0.1 | n/a | no target |
| P06T | 37219 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 257 | 32.7% | 32.7% | -1.7 | n/a | no target |
| P07 | 677 | 6.6% | 6.6% | -0.3 | n/a | no target |
| P08 | 21626 | 1.2% | 1.2% | -0.1 | n/a | no target |
| P09 | 314 | 9.9% | 9.9% | +0.1 | n/a | no target |
| P10 | 2168 | 3.1% | 3.1% | +0.0 | n/a | no target |
| P11 | 1512 | 4.4% | 4.4% | -0.7 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 144433 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 12.3% | 12.3% | -0.1 | n/a | no target |
| P01T | 185 | 14.1% | 14.1% | +0.6 | n/a | no target |
| P01_GOLD | 641 | 49.1% | 49.1% | -0.7 | 50% | 🟡 1 pts to go |
| P02 | 471 | 37.6% | 37.6% | +0.3 | n/a | no target |
| P03 | 271 | 50.9% | 50.9% | -1.2 | 60% | 🟡 9 pts to go |
| P04 | 3629 | 12.2% | 12.2% | +0.3 | n/a | no target |
| P05 | 427 | 15.0% | 15.0% | -0.2 | n/a | no target |
| P06M | 15872 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06T | 37219 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 257 | 24.1% | 24.1% | -1.5 | n/a | no target |
| P07 | 677 | 7.5% | 7.5% | -0.8 | n/a | no target |
| P08 | 21626 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 314 | 18.5% | 18.5% | +0.9 | n/a | no target |
| P10 | 2168 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 1512 | 3.5% | 3.5% | -1.2 | n/a | no target |
| P12 | 16 | 12.5% | 12.5% | -0.8 | n/a | no target |
| P13 | 144433 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 11.0% | 11.0% | -0.6 | 15% | 🟡 4 pts to go |
| P01T | 185 | 13.0% | 13.0% | +0.5 | 15% | 🟡 2 pts to go |
| P01_GOLD | 641 | 34.8% | 34.8% | -0.5 | 40% | 🟡 5 pts to go |
| P02 | 471 | 12.7% | 13.0% | -0.2 | 25% | ❌ 12 pts to go |
| P03 | 271 | 17.0% | 17.0% | -0.5 | 25% | 🟡 8 pts to go |
| P04 | 3629 | 2.7% | 2.7% | +0.0 | 15% | ❌ 12 pts to go |
| P05 | 427 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 15872 | 0.8% | 0.8% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 37219 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 257 | 10.9% | 10.9% | +0.3 | 15% | 🟡 4 pts to go |
| P07 | 677 | 4.1% | 4.1% | -0.2 | 15% | ❌ 11 pts to go |
| P08 | 21626 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 314 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2168 | 1.2% | 1.2% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1512 | 1.5% | 1.5% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 144433 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 4.8% | 4.8% | -0.6 | 15% | ❌ 10 pts to go |
| P01T | 185 | 11.9% | 11.9% | +0.4 | 25% | ❌ 13 pts to go |
| P01_GOLD | 641 | 28.5% | 28.5% | -0.7 | 25% | ✅ met |
| P02 | 471 | 25.3% | 25.3% | +0.0 | 15% | ✅ met |
| P03 | 271 | 22.5% | 22.5% | +0.4 | 15% | ✅ met |
| P04 | 3629 | 4.1% | 4.1% | +0.1 | 15% | ❌ 11 pts to go |
| P05 | 427 | 11.2% | 11.2% | +0.1 | 15% | 🟡 4 pts to go |
| P06M | 15872 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 37219 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 257 | 8.9% | 8.9% | +0.5 | 15% | 🟡 6 pts to go |
| P07 | 677 | 2.7% | 2.7% | -0.2 | 15% | ❌ 12 pts to go |
| P08 | 21626 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 314 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2168 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1512 | 2.2% | 2.2% | -0.5 | 15% | ❌ 13 pts to go |
| P12 | 16 | 18.8% | 18.8% | -1.2 | 15% | ✅ met |
| P13 | 144433 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 2.1% | 2.1% | -0.2 | 20% | ❌ 18 pts to go |
| P01T | 185 | 4.3% | 4.3% | +0.1 | 20% | ❌ 16 pts to go |
| P01_GOLD | 641 | 4.4% | 4.4% | -0.1 | 20% | ❌ 16 pts to go |
| P02 | 471 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 271 | 1.8% | 1.8% | +0.3 | 20% | ❌ 18 pts to go |
| P04 | 3629 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |
| P05 | 427 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 15872 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 257 | 1.6% | 1.6% | +0.1 | 20% | ❌ 18 pts to go |
| P07 | 677 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 21626 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P09 | 314 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2168 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1512 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 1.4% | 1.4% | -0.2 | 15% | ❌ 14 pts to go |
| P01T | 185 | 3.2% | 3.2% | +0.1 | 15% | ❌ 12 pts to go |
| P01_GOLD | 641 | 10.1% | 10.1% | -0.3 | 15% | 🟡 5 pts to go |
| P02 | 471 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P03 | 271 | 20.3% | 20.3% | +0.1 | 15% | ✅ met |
| P04 | 3629 | 2.3% | 2.3% | +0.0 | 15% | ❌ 13 pts to go |
| P05 | 427 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 15872 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 37219 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 257 | 5.1% | 5.1% | +0.0 | 15% | 🟡 10 pts to go |
| P07 | 677 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P08 | 21626 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 314 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |
| P10 | 2168 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1512 | 1.0% | 1.0% | -0.2 | 15% | ❌ 14 pts to go |
| P12 | 16 | 6.2% | 6.2% | -0.5 | 15% | 🟡 9 pts to go |
| P13 | 144433 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 13.7% | 13.7% | -0.3 | 20% | 🟡 6 pts to go |
| P01T | 185 | 14.6% | 14.6% | +0.5 | 40% | ❌ 25 pts to go |
| P01_GOLD | 641 | 45.6% | 45.6% | -0.6 | 40% | ✅ met |
| P02 | 471 | 43.1% | 43.1% | +0.2 | 20% | ✅ met |
| P03 | 271 | 48.0% | 48.0% | -1.0 | 35% | ✅ met |
| P04 | 3629 | 14.6% | 14.6% | +0.4 | 20% | 🟡 5 pts to go |
| P05 | 427 | 15.5% | 15.5% | +0.1 | 20% | 🟡 4 pts to go |
| P06M | 15872 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P06T | 37219 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 257 | 24.1% | 24.1% | -1.2 | 20% | ✅ met |
| P07 | 677 | 8.1% | 8.1% | -0.5 | 20% | ❌ 12 pts to go |
| P08 | 21626 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 314 | 18.5% | 18.5% | +0.3 | 20% | 🟡 2 pts to go |
| P10 | 2168 | 3.8% | 3.8% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 1512 | 3.8% | 3.8% | -1.0 | 20% | ❌ 16 pts to go |
| P12 | 16 | 6.2% | 6.2% | -0.5 | 20% | ❌ 14 pts to go |
| P13 | 144433 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 30.1% | 30.1% | -3.2 | n/a | no target |
| P01T | 185 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 71.9% | 71.9% | +2.4 | 95% | ❌ 23 pts to go |
| P02 | 471 | 65.2% | 65.2% | +2.3 | 95% | ❌ 30 pts to go |
| P03 | 271 | 57.6% | 57.6% | +4.4 | 90% | ❌ 32 pts to go |
| P04 | 3629 | 27.2% | 27.2% | +2.4 | 85% | ❌ 58 pts to go |
| P05 | 427 | 38.4% | 38.4% | +0.7 | 75% | ❌ 37 pts to go |
| P06M | 15872 | 35.5% | 35.5% | -0.6 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 90.1% | 90.1% | +1.8 | 100% | 🟡 10 pts to go |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 5.2% | 5.2% | -0.8 | 60% | ❌ 55 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 30.1% | 30.1% | -3.2 | n/a | no target |
| P01T | 185 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 73.6% | 73.6% | +0.8 | 100% | ❌ 26 pts to go |
| P02 | 471 | 67.3% | 67.3% | +1.0 | 100% | ❌ 33 pts to go |
| P03 | 271 | 60.1% | 60.1% | +1.2 | n/a | no target |
| P04 | 3629 | 27.6% | 27.6% | +2.1 | 95% | ❌ 67 pts to go |
| P05 | 427 | 34.2% | 34.2% | +0.8 | 80% | ❌ 46 pts to go |
| P06M | 15872 | 35.5% | 35.5% | -0.6 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 92.0% | 92.0% | +0.5 | 100% | 🟡 8 pts to go |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 5.4% | 5.4% | -1.0 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 82.2% | 82.2% | +2.4 | n/a | no target |
| P01T | 185 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 52.3% | 52.3% | +0.7 | 85% | ❌ 33 pts to go |
| P02 | 471 | 58.4% | 58.4% | +0.9 | 90% | ❌ 32 pts to go |
| P03 | 271 | 43.5% | 43.5% | +0.9 | 85% | ❌ 42 pts to go |
| P04 | 3629 | 29.7% | 29.7% | +1.8 | 90% | ❌ 60 pts to go |
| P05 | 427 | 32.3% | 32.3% | -0.4 | 75% | ❌ 43 pts to go |
| P06M | 15872 | 86.2% | 86.2% | -0.9 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 82.5% | 82.5% | -0.9 | 95% | ❌ 12 pts to go |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 4.6% | 4.6% | -0.8 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 80.8% | 80.8% | +2.5 | n/a | no target |
| P01T | 185 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 52.6% | 52.6% | +0.8 | 85% | ❌ 32 pts to go |
| P02 | 471 | 53.1% | 53.1% | +0.5 | 90% | ❌ 37 pts to go |
| P03 | 271 | 43.5% | 43.5% | -0.2 | 85% | ❌ 42 pts to go |
| P04 | 3629 | 25.2% | 25.2% | +1.4 | 90% | ❌ 65 pts to go |
| P05 | 427 | 42.6% | 42.6% | -0.8 | 75% | ❌ 32 pts to go |
| P06M | 15872 | 76.9% | 76.9% | -0.9 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 3.6% | 3.6% | -0.9 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 91.1% | 91.1% | +1.2 | n/a | no target |
| P01T | 185 | 94.6% | 94.6% | +0.3 | n/a | no target |
| P01_GOLD | 641 | 85.5% | 85.5% | +0.2 | 100% | ❌ 14 pts to go |
| P02 | 471 | 77.3% | 77.3% | +0.9 | 100% | ❌ 23 pts to go |
| P03 | 271 | 91.5% | 91.5% | +0.2 | n/a | no target |
| P04 | 3629 | 51.0% | 51.0% | +2.2 | 95% | ❌ 44 pts to go |
| P05 | 427 | 77.5% | 77.5% | +0.0 | 95% | ❌ 18 pts to go |
| P06M | 15872 | 99.0% | 99.0% | +0.1 | n/a | no target |
| P06T | 37219 | 91.3% | 91.3% | +0.7 | n/a | no target |
| P06 | 257 | 22.2% | 22.2% | -0.9 | n/a | no target |
| P07 | 677 | 12.7% | 12.7% | -1.1 | n/a | no target |
| P08 | 21626 | 6.5% | 6.5% | -0.6 | n/a | no target |
| P09 | 314 | 98.4% | 98.4% | -0.3 | 100% | 🟡 2 pts to go |
| P10 | 2168 | 70.6% | 70.6% | -0.4 | n/a | no target |
| P11 | 1512 | 68.9% | 68.9% | +0.8 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 99.5% | 99.5% | -0.2 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 91.1% | 91.1% | +1.2 | n/a | no target |
| P01T | 185 | 94.6% | 94.6% | +0.3 | n/a | no target |
| P01_GOLD | 641 | 88.6% | 88.6% | +0.1 | 100% | ❌ 11 pts to go |
| P02 | 471 | 78.3% | 78.6% | +0.8 | 100% | ❌ 22 pts to go |
| P03 | 271 | 92.3% | 92.3% | +0.3 | n/a | no target |
| P04 | 3629 | 54.2% | 54.2% | +2.3 | 95% | ❌ 41 pts to go |
| P05 | 427 | 89.5% | 89.5% | -0.1 | 70% | ✅ met |
| P06M | 15872 | 99.0% | 99.0% | +0.1 | n/a | no target |
| P06T | 37219 | 91.3% | 91.3% | +0.7 | n/a | no target |
| P06 | 257 | 22.2% | 22.2% | -0.9 | n/a | no target |
| P07 | 677 | 12.7% | 12.7% | -1.1 | n/a | no target |
| P08 | 21626 | 6.5% | 6.5% | -0.6 | n/a | no target |
| P09 | 314 | 98.4% | 98.4% | -0.3 | 100% | 🟡 2 pts to go |
| P10 | 2168 | 70.6% | 70.6% | -0.4 | n/a | no target |
| P11 | 1512 | 69.0% | 69.0% | +0.8 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 185 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 16.7% | 16.7% | -0.1 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 376 rows, 28.5% filled |
| P02 | 471 | 11.0% | 11.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 298 rows, 17.4% filled |
| P03 | 271 | 14.4% | 14.4% | +1.5 | n/a | no target · rows from a source that publishes bids: 144 rows, 27.1% filled |
| P04 | 3629 | 1.6% | 1.6% | +0.1 | n/a | no target · rows from a source that publishes bids: 920 rows, 6.3% filled |
| P05 | 427 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 52 rows, 21.2% filled |
| P06M | 15872 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37219 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 4.5% | 4.5% | +0.3 | n/a | no target · rows from a source that publishes bids: 300 rows, 4.7% filled |
| P10 | 2168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1512 | 0.7% | 0.7% | -0.2 | n/a | no target · rows from a source that publishes bids: 77 rows, 13.0% filled |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 16 rows, 0.0% filled |
| P13 | 144433 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 185 | 0.0% | 97.8% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 53.7% | 82.4% | +0.5 | 90% | ❌ 36 pts to go |
| P02 | 471 | 53.1% | 87.3% | +0.7 | 90% | ❌ 37 pts to go |
| P03 | 271 | 45.4% | 80.1% | +0.9 | 90% | ❌ 45 pts to go |
| P04 | 3629 | 20.3% | 93.0% | +1.2 | 90% | ❌ 70 pts to go |
| P05 | 427 | 0.0% | 82.9% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 15872 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 37219 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 2.5% | 4.1% | +0.2 | 90% | ❌ 88 pts to go |
| P10 | 2168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1512 | 3.1% | 97.1% | -1.0 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 185 | 0.5% | 98.4% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 26.4% | 55.1% | +0.5 | 90% | ❌ 64 pts to go |
| P02 | 471 | 51.8% | 86.0% | +0.3 | n/a | no target |
| P03 | 271 | 24.7% | 59.4% | +0.4 | n/a | no target |
| P04 | 3629 | 22.3% | 94.9% | +1.3 | n/a | no target |
| P05 | 427 | 0.5% | 83.4% | +0.0 | n/a | no target |
| P06M | 15872 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 37219 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 40.8% | 42.4% | -0.2 | n/a | no target |
| P10 | 2168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1512 | 3.0% | 97.0% | -0.7 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 185 | 2.2% | 100.0% | +0.1 | n/a | no target |
| P01_GOLD | 641 | 52.3% | 81.0% | +0.5 | 95% | ❌ 43 pts to go |
| P02 | 471 | 57.3% | 91.5% | +0.9 | n/a | no target |
| P03 | 271 | 48.3% | 83.0% | +1.5 | n/a | no target |
| P04 | 3629 | 23.0% | 95.6% | +1.8 | n/a | no target |
| P05 | 427 | 4.7% | 87.6% | +0.2 | n/a | no target |
| P06M | 15872 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 37219 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 257 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21626 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 61.8% | 63.4% | -0.7 | n/a | no target |
| P10 | 2168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1512 | 3.2% | 97.2% | -0.9 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 144433 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P01T | 185 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 641 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 471 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 271 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P04 | 3629 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P05 | 427 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P06M | 15872 | 98.1% | 98.1% | -1.9 | 100% | 🟡 2 pts to go |
| P06T | 37219 | 98.2% | 98.2% | -1.8 | 100% | 🟡 2 pts to go |
| P06 | 257 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P07 | 677 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P08 | 21626 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2168 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P11 | 1512 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 144433 | 92.9% | 92.9% | -7.1 | 100% | 🟡 7 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P01T | 185 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 641 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 471 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 271 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P04 | 3629 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P05 | 427 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P06M | 15872 | 98.1% | 98.1% | -1.9 | 100% | 🟡 2 pts to go |
| P06T | 37219 | 98.2% | 98.2% | -1.8 | 100% | 🟡 2 pts to go |
| P06 | 257 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P07 | 677 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P08 | 21626 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2168 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P11 | 1512 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 144433 | 92.9% | 92.9% | -7.1 | 100% | 🟡 7 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 146 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P01T | 185 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 641 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 471 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 271 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P04 | 3629 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P05 | 427 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P06M | 15872 | 98.1% | 98.1% | -1.9 | 100% | 🟡 2 pts to go |
| P06T | 37219 | 98.2% | 98.2% | -1.8 | 100% | 🟡 2 pts to go |
| P06 | 257 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P07 | 677 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P08 | 21626 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2168 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P11 | 1512 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 144433 | 92.9% | 92.9% | -7.1 | 100% | 🟡 7 pts to go |

