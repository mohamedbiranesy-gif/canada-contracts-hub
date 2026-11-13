# Coverage vs the downstream team's targets — 2026-11-13

Benchmarks (field × package with a numeric target): **88 of 438 met** (20.1%); 67 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 429, P01T 207, P01_GOLD 657, P02 485, P03 274, P04 4772, P05 428, P06M 31427, P06T 55074, P06 243, P07 758, P08 28702, P09 71, P10R 0, P10 2008, P11 1806, P12 10, P13 207861

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 12.8% | 7 | vendor GST/HST number (407 rows) |
| P01T | 207 | 1.0% | 32.9% | 8 | payment terms (162 rows) |
| P01_GOLD | 657 | 23.4% | 69.4% | 9 | payment terms (243 rows) |
| P02 | 485 | 7.4% | 53.2% | 9 | PO rule (372 rows) |
| P03 | 274 | 14.2% | 55.1% | 9 | PO rule (139 rows) |
| P04 | 4772 | 1.0% | 14.0% | 7 | PO rule (4501 rows) |
| P05 | 428 | 0.9% | 16.8% | 7 | payment terms (357 rows) |
| P06M | 31427 | 0.0% | 3.0% | 7 | PO rule (30603 rows) |
| P06T | 55074 | 0.1% | 13.5% | 7 | PO rule (54719 rows) |
| P06 | 243 | 0.0% | 10.7% | 7 | reference to quote (PO / contract / vendor id) (227 rows) |
| P07 | 758 | 0.0% | 3.4% | 6 | PO rule (720 rows) |
| P08 | 28702 | 0.0% | 1.8% | 6 | PO rule (28387 rows) |
| P09 | 71 | 4.2% | 35.2% | 8 | payment terms (62 rows) |
| P10 | 2008 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2008 rows) |
| P11 | 1806 | 0.1% | 8.1% | 6 | PO rule (1742 rows) |
| P12 | 10 | 0.0% | 40.0% | 8 | PO rule (10 rows) |
| P13 | 207861 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (207861 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 429 | 13 | 128 | 288 | 0 | 0 | 70 |
| P01T | 207 | 26 | 33 | 148 | 0 | 0 | 66 |
| P01_GOLD | 657 | 257 | 180 | 220 | 0 | 0 | 81 |
| P02 | 485 | 0 | 195 | 290 | 0 | 0 | 66 |
| P03 | 274 | 0 | 0 | 263 | 11 | 0 | 57 |
| P04 | 4772 | 0 | 0 | 4137 | 635 | 0 | 46 |
| P05 | 428 | 16 | 28 | 372 | 12 | 0 | 51 |
| P06M | 31427 | 0 | 53 | 31335 | 39 | 0 | 46 |
| P06T | 55074 | 0 | 27 | 38370 | 16677 | 0 | 38 |
| P06 | 243 | 15 | 36 | 192 | 0 | 0 | 67 |
| P07 | 758 | 0 | 21 | 719 | 18 | 0 | 55 |
| P08 | 28702 | 0 | 0 | 26101 | 2601 | 0 | 46 |
| P09 | 71 | 3 | 6 | 62 | 0 | 0 | 52 |
| P10 | 2008 | 2 | 10 | 1358 | 638 | 0 | 41 |
| P11 | 1806 | 7 | 11 | 38 | 0 | 1750 | 24 |
| P12 | 10 | 0 | 0 | 10 | 0 | 0 | 54 |
| P13 | 207861 | 14 | 73 | 207717 | 57 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 429 | 316 | 73.7% | tax treatment (83) |
| P01T | 207 | 125 | 60.4% | bill-to legal name and address (67) |
| P01_GOLD | 657 | 496 | 75.5% | bill-to legal name and address (96) |
| P02 | 485 | 329 | 67.8% | the buyer's PO / reference rule (83) |
| P03 | 274 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (274) |
| P04 | 4772 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4772) |
| P05 | 428 | 45 | 10.5% | a confirmed invoicing / AP or finance channel (340) |
| P06M | 31427 | 347 | 1.1% | a confirmed invoicing / AP or finance channel (30982) |
| P06T | 55074 | 326 | 0.6% | a confirmed invoicing / AP or finance channel (54321) |
| P06 | 243 | 45 | 18.5% | the buyer's PO / reference rule (106) |
| P07 | 758 | 46 | 6.1% | the buyer's PO / reference rule (309) |
| P08 | 28702 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (28702) |
| P09 | 71 | 10 | 14.1% | a confirmed invoicing / AP or finance channel (51) |
| P10 | 2008 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (1935) |
| P11 | 1806 | 18 | 1.0% | a confirmed invoicing / AP or finance channel (1750) |
| P12 | 10 | 2 | 20.0% | a confirmed invoicing / AP or finance channel (8) |
| P13 | 207861 | 51 | 0.0% | a confirmed invoicing / AP or finance channel (205262) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 429 | 9 | 2.1% | 7 | 0 | the vendor's GST/HST number (BN9) (406) |
| P01T | 207 | 82 | 39.6% | 2 | 0 | the vendor's GST/HST number (BN9) (77) |
| P01_GOLD | 657 | 413 | 62.9% | 11 | 0 | the vendor's GST/HST number (BN9) (168) |
| P02 | 485 | 213 | 43.9% | 22 | 0 | the vendor's GST/HST number (BN9) (221) |
| P03 | 274 | 18 | 6.6% | 0 | 133 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (101) |
| P04 | 4772 | 42 | 0.9% | 7 | 906 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3747) |
| P05 | 428 | 20 | 4.7% | 8 | 129 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (203) |
| P06M | 31427 | 12 | 0.0% | 14 | 756 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (30031) |
| P06T | 55074 | 361 | 0.7% | 15 | 18774 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (35462) |
| P06 | 243 | 20 | 8.2% | 45 | 0 | the vendor's GST/HST number (BN9) (116) |
| P07 | 758 | 14 | 1.8% | 130 | 36 | the vendor's GST/HST number (BN9) (375) |
| P08 | 28702 | 6 | 0.0% | 14 | 7098 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (21528) |
| P09 | 71 | 14 | 19.7% | 0 | 25 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (21) |
| P10 | 2008 | 5 | 0.2% | 14 | 277 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1637) |
| P11 | 1806 | 7 | 0.4% | 2 | 0 | a confirmed invoicing / AP or finance channel (1734) |
| P12 | 10 | 1 | 10.0% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3) |
| P13 | 207861 | 27 | 0.0% | 1244 | 81334 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (123728) |
| **all** | 335212 | 1264 | 0.4% | 1535 | 109473 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 416 | 0 | 0 | 0 | 315 | 11 | 0 | 310 | 352 | 1 |
| P01T | 181 | 0 | 0 | 0 | 116 | 63 | 26 | 152 | 163 | 2 |
| P01_GOLD | 400 | 0 | 0 | 0 | 39 | 78 | 30 | 215 | 258 | 3 |
| P02 | 485 | 0 | 485 | 0 | 59 | 57 | 14 | 372 | 301 | 2 |
| P03 | 274 | 0 | 274 | 0 | 27 | 45 | 24 | 139 | 148 | 2 |
| P04 | 4772 | 0 | 4772 | 0 | 2642 | 1466 | 964 | 4501 | 4260 | 31 |
| P05 | 412 | 0 | 360 | 0 | 87 | 100 | 39 | 344 | 359 | 7 |
| P06M | 31427 | 0 | 31427 | 0 | 24920 | 2558 | 122 | 30603 | 30077 | 17 |
| P06T | 55074 | 0 | 55074 | 0 | 49622 | 34542 | 21344 | 54719 | 54167 | 383 |
| P06 | 228 | 0 | 0 | 0 | 124 | 68 | 36 | 173 | 198 | 4 |
| P07 | 758 | 0 | 758 | 0 | 514 | 296 | 92 | 720 | 715 | 5 |
| P08 | 28702 | 0 | 28702 | 0 | 22736 | 12448 | 3951 | 28387 | 27947 | 178 |
| P09 | 68 | 0 | 53 | 0 | 9 | 38 | 0 | 49 | 63 | 1 |
| P10 | 2006 | 0 | 1976 | 0 | 1041 | 1095 | 925 | 1944 | 1909 | 17 |
| P11 | 1799 | 1750 | 1705 | 0 | 927 | 1222 | 501 | 1742 | 1733 | 20 |
| P12 | 10 | 0 | 9 | 0 | 0 | 2 | 0 | 10 | 10 | 1 |
| P13 | 207847 | 0 | 207361 | 0 | 176629 | 126480 | 83 | 207472 | 206505 | 79 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 56.3% | 95% | 80451 |
| buyer_logo_url | P13 | 71.8% | 95% | 48200 |
| buyer_legal_name_as_published | P13 | 39.2% | 60% | 43336 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 41515 |
| ap_system_hint | P13 | 0.3% | 20% | 40857 |
| buyer_bn_as_published | P13 | 13.0% | 30% | 35303 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 31008 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 30961 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 29997 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11000 |
| vendor_registered_address | P08 | 32.4% | 70% | 10781 |
| ap_system_hint | P06T | 0.6% | 20% | 10665 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8158 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8137 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 7902 |
| buyer_phone | P08 | 70.6% | 95% | 7002 |
| buyer_ap_cycle_published | P06M | 0.1% | 20% | 6269 |
| ap_system_hint | P06M | 1.3% | 20% | 5873 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5728 |
| ap_system_hint | P08 | 0.9% | 20% | 5476 |
| vendor_emails | P08 | 56.0% | 75% | 5457 |
| buyer_legal_name_as_published | P08 | 56.6% | 75% | 5273 |
| vendor_bn9 | P08 | 32.2% | 50% | 5106 |
| vendor_phone | P08 | 67.5% | 85% | 5014 |
| vendor_trading_name | P08 | 34.0% | 50% | 4588 |
| buyer_esignature_preference | P06M | 0.5% | 15% | 4553 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 4472 |
| buyer_tax_exempt_status | P06M | 0.9% | 15% | 4422 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 4192 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 4181 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 4127 |
| invoice_reference_hint | P08 | 12.3% | 25% | 3634 |
| average_contract_duration_days | P04 | 14.8% | 90% | 3588 |
| currency | P04 | 21.2% | 95% | 3521 |
| ap_phone | P04 | 16.5% | 85% | 3272 |
| commodity_codes | P04 | 16.7% | 85% | 3261 |
| award_or_notice_id | P04 | 18.7% | 85% | 3166 |
| contract_value | P04 | 20.9% | 85% | 3061 |
| invoice_mailing_address | P04 | 16.2% | 75% | 2808 |
| buyer_bn_as_published | P08 | 25.2% | 35% | 2801 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 95.1% | 95.1% | +1.9 | 50% | ✅ met |
| P01T | 207 | 94.7% | 94.7% | -0.9 | 50% | ✅ met |
| P01_GOLD | 657 | 92.2% | 94.5% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 485 | 75.9% | 77.3% | +0.9 | 95% | ❌ 19 pts to go |
| P03 | 274 | 83.2% | 86.5% | +1.6 | 95% | ❌ 12 pts to go |
| P04 | 4772 | 44.2% | 45.5% | +12.4 | 90% | ❌ 46 pts to go |
| P05 | 428 | 40.2% | 43.2% | +0.6 | 70% | ❌ 30 pts to go |
| P06M | 31427 | 94.6% | 94.6% | +1.4 | n/a | no target |
| P06T | 55074 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06 | 243 | 33.3% | 33.3% | -2.1 | 30% | ✅ met |
| P07 | 758 | 13.7% | 13.7% | -0.5 | 30% | ❌ 16 pts to go |
| P08 | 28702 | 12.3% | 12.3% | +0.1 | 25% | ❌ 13 pts to go |
| P09 | 71 | 95.8% | 98.6% | -3.1 | 100% | 🟡 4 pts to go |
| P10 | 2008 | 3.2% | 3.2% | -0.1 | 25% | ❌ 22 pts to go |
| P11 | 1806 | 55.3% | 56.0% | +1.0 | 60% | 🟡 5 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 207861 | 99.4% | 99.4% | -0.2 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 207 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 657 | 5.6% | 5.6% | -0.1 | 50% | ❌ 44 pts to go |
| P02 | 485 | 5.4% | 5.4% | -0.8 | 50% | ❌ 45 pts to go |
| P03 | 274 | 1.8% | 1.8% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4772 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 428 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 31427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | +0.7 | 50% | ❌ 49 pts to go |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 92.5% | 92.5% | +2.9 | n/a | no target |
| P01T | 207 | 77.8% | 77.8% | -2.1 | 50% | ✅ met |
| P01_GOLD | 657 | 68.3% | 68.3% | +1.0 | 85% | ❌ 17 pts to go |
| P02 | 485 | 67.6% | 67.6% | +1.4 | 90% | ❌ 22 pts to go |
| P03 | 274 | 62.8% | 62.8% | +2.3 | 85% | ❌ 22 pts to go |
| P04 | 4772 | 42.0% | 42.0% | +12.9 | 85% | ❌ 43 pts to go |
| P05 | 428 | 30.8% | 30.8% | +0.9 | 60% | ❌ 29 pts to go |
| P06M | 31427 | 94.4% | 94.4% | +1.4 | n/a | no target |
| P06T | 55074 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06 | 243 | 6.6% | 6.6% | +0.2 | n/a | no target |
| P07 | 758 | 9.0% | 9.0% | -0.1 | n/a | no target |
| P08 | 28702 | 11.4% | 11.4% | +0.1 | n/a | no target |
| P09 | 71 | 83.1% | 83.1% | -12.5 | 100% | ❌ 17 pts to go |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 52.6% | 52.6% | +1.1 | 60% | 🟡 7 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 207 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 657 | 49.3% | 49.3% | -2.4 | 80% | ❌ 31 pts to go |
| P02 | 485 | 55.7% | 55.7% | -2.4 | 60% | 🟡 4 pts to go |
| P03 | 274 | 48.5% | 48.5% | -1.9 | 80% | ❌ 32 pts to go |
| P04 | 4772 | 18.0% | 18.0% | -6.0 | 50% | ❌ 32 pts to go |
| P05 | 428 | 13.6% | 13.6% | +1.0 | 40% | ❌ 26 pts to go |
| P06M | 31427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 36.6% | 36.6% | -44.5 | 50% | ❌ 13 pts to go |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 3.3% | 3.3% | +0.0 | 40% | ❌ 37 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 207 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 657 | 58.4% | 58.4% | -2.5 | 85% | ❌ 27 pts to go |
| P02 | 485 | 55.9% | 55.9% | -2.2 | 90% | ❌ 34 pts to go |
| P03 | 274 | 56.9% | 56.9% | -2.5 | 85% | ❌ 28 pts to go |
| P04 | 4772 | 18.7% | 18.7% | -6.2 | 85% | ❌ 66 pts to go |
| P05 | 428 | 21.3% | 21.3% | +0.9 | 50% | ❌ 29 pts to go |
| P06M | 31427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 88.7% | 88.7% | -8.4 | 100% | ❌ 11 pts to go |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 3.7% | 3.7% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 207 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 12.5% | 12.5% | -0.1 | 60% | ❌ 48 pts to go |
| P02 | 485 | 6.6% | 6.6% | -0.7 | 50% | ❌ 43 pts to go |
| P03 | 274 | 8.4% | 8.4% | -0.2 | 50% | ❌ 42 pts to go |
| P04 | 4772 | 1.4% | 1.4% | -0.5 | 40% | ❌ 39 pts to go |
| P05 | 428 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 31427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 5.6% | 5.6% | +2.0 | 50% | ❌ 44 pts to go |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 207 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 34.4% | 34.4% | -1.5 | 80% | ❌ 46 pts to go |
| P02 | 485 | 50.3% | 50.3% | -2.7 | 90% | ❌ 40 pts to go |
| P03 | 274 | 32.8% | 32.8% | -1.0 | 80% | ❌ 47 pts to go |
| P04 | 4772 | 16.7% | 16.7% | -5.5 | 85% | ❌ 68 pts to go |
| P05 | 428 | 7.5% | 7.5% | +1.1 | 50% | ❌ 42 pts to go |
| P06M | 31427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 62.0% | 62.0% | -11.1 | 95% | ❌ 33 pts to go |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 2.7% | 2.7% | +0.1 | 50% | ❌ 47 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 207 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 7.9% | 7.9% | -0.2 | 50% | ❌ 42 pts to go |
| P02 | 485 | 5.4% | 5.4% | -0.8 | 50% | ❌ 45 pts to go |
| P03 | 274 | 2.6% | 2.6% | +0.0 | 30% | ❌ 27 pts to go |
| P04 | 4772 | 0.4% | 0.4% | -0.2 | 30% | ❌ 30 pts to go |
| P05 | 428 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 31427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | +1.0 | n/a | no target |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 207 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 657 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 485 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 274 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4772 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 428 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 31427 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55074 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 243 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 758 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28702 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2008 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1806 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 5.1% | 5.1% | -1.3 | 70% | ❌ 65 pts to go |
| P01T | 207 | 54.6% | 54.6% | -5.7 | 60% | 🟡 5 pts to go |
| P01_GOLD | 657 | 72.3% | 72.3% | -2.5 | 90% | ❌ 18 pts to go |
| P02 | 485 | 52.0% | 52.0% | -2.3 | 85% | ❌ 33 pts to go |
| P03 | 274 | 63.5% | 63.5% | -3.4 | 90% | ❌ 26 pts to go |
| P04 | 4772 | 29.0% | 29.0% | -9.2 | 75% | ❌ 46 pts to go |
| P05 | 428 | 54.7% | 54.7% | +0.0 | 50% | ✅ met |
| P06M | 31427 | 3.0% | 3.0% | +0.1 | n/a | no target |
| P06T | 55074 | 65.7% | 65.7% | +1.2 | n/a | no target |
| P06 | 243 | 42.0% | 42.0% | -0.1 | 40% | ✅ met |
| P07 | 758 | 32.3% | 32.3% | +0.2 | 50% | ❌ 18 pts to go |
| P08 | 28702 | 32.2% | 32.2% | +1.6 | 50% | ❌ 18 pts to go |
| P09 | 71 | 64.8% | 64.8% | +8.1 | 80% | ❌ 15 pts to go |
| P10 | 2008 | 38.7% | 38.7% | -0.1 | 40% | 🟡 1 pts to go |
| P11 | 1806 | 53.9% | 53.9% | -0.7 | 60% | 🟡 6 pts to go |
| P12 | 10 | 60.0% | 60.0% | +14.5 | 85% | ❌ 25 pts to go |
| P13 | 207861 | 44.9% | 44.9% | +0.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 42.0% | 42.0% | -4.6 | n/a | no target |
| P01T | 207 | 53.6% | 53.6% | -6.2 | n/a | no target |
| P01_GOLD | 657 | 74.0% | 74.0% | +1.1 | 95% | ❌ 21 pts to go |
| P02 | 485 | 75.5% | 75.5% | +0.9 | 95% | ❌ 20 pts to go |
| P03 | 274 | 70.4% | 70.4% | +0.9 | 95% | ❌ 25 pts to go |
| P04 | 4772 | 55.2% | 55.2% | +2.1 | 95% | ❌ 40 pts to go |
| P05 | 428 | 58.6% | 58.6% | +0.5 | 70% | ❌ 11 pts to go |
| P06M | 31427 | 38.4% | 38.4% | -2.9 | n/a | no target |
| P06T | 55074 | 65.4% | 65.4% | -2.1 | n/a | no target |
| P06 | 243 | 37.9% | 37.9% | -0.3 | 80% | ❌ 42 pts to go |
| P07 | 758 | 31.8% | 31.8% | +0.8 | 70% | ❌ 38 pts to go |
| P08 | 28702 | 32.4% | 32.4% | +2.7 | 70% | ❌ 38 pts to go |
| P09 | 71 | 60.6% | 60.6% | -25.6 | 100% | ❌ 39 pts to go |
| P10 | 2008 | 39.3% | 39.3% | +0.1 | 70% | ❌ 31 pts to go |
| P11 | 1806 | 58.6% | 58.6% | +0.0 | 75% | ❌ 16 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 40.7% | 40.7% | +0.5 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 22.1% | 22.1% | +0.0 | n/a | no target |
| P01T | 207 | 60.9% | 60.9% | -4.6 | n/a | no target |
| P01_GOLD | 657 | 50.7% | 50.7% | +1.9 | 60% | 🟡 9 pts to go |
| P02 | 485 | 58.6% | 58.6% | +2.8 | 60% | 🟡 1 pts to go |
| P03 | 274 | 54.4% | 54.4% | +2.1 | 60% | 🟡 6 pts to go |
| P04 | 4772 | 54.1% | 54.1% | +11.5 | 55% | 🟡 1 pts to go |
| P05 | 428 | 23.6% | 23.6% | +0.9 | 50% | ❌ 26 pts to go |
| P06M | 31427 | 11.3% | 11.3% | +1.8 | n/a | no target |
| P06T | 55074 | 74.7% | 74.7% | +6.8 | n/a | no target |
| P06 | 243 | 50.6% | 50.6% | +2.0 | n/a | no target |
| P07 | 758 | 39.8% | 39.8% | +0.2 | 55% | ❌ 15 pts to go |
| P08 | 28702 | 34.0% | 34.0% | +1.0 | 50% | ❌ 16 pts to go |
| P09 | 71 | 39.4% | 39.4% | -32.6 | 70% | ❌ 31 pts to go |
| P10 | 2008 | 47.9% | 47.9% | -0.2 | 55% | 🟡 7 pts to go |
| P11 | 1806 | 59.7% | 59.7% | +0.5 | 50% | ✅ met |
| P12 | 10 | 90.0% | 90.0% | -0.9 | n/a | no target |
| P13 | 207861 | 2.9% | 2.9% | -0.3 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 23.8% | 23.8% | -9.5 | n/a | no target |
| P01T | 207 | 77.3% | 77.3% | -2.2 | n/a | no target |
| P01_GOLD | 657 | 48.1% | 48.1% | -2.3 | 70% | ❌ 22 pts to go |
| P02 | 485 | 54.8% | 54.8% | -2.0 | 70% | ❌ 15 pts to go |
| P03 | 274 | 48.2% | 48.2% | -2.2 | 70% | ❌ 22 pts to go |
| P04 | 4772 | 49.4% | 49.4% | -5.5 | 65% | ❌ 16 pts to go |
| P05 | 428 | 29.7% | 29.7% | +0.6 | 60% | ❌ 30 pts to go |
| P06M | 31427 | 23.1% | 23.1% | -4.3 | n/a | no target |
| P06T | 55074 | 87.1% | 87.1% | +4.4 | n/a | no target |
| P06 | 243 | 70.0% | 70.0% | +0.7 | 40% | ✅ met |
| P07 | 758 | 66.4% | 66.4% | +1.4 | 85% | ❌ 19 pts to go |
| P08 | 28702 | 67.5% | 67.5% | +3.5 | 85% | ❌ 18 pts to go |
| P09 | 71 | 31.0% | 31.0% | -25.4 | 85% | ❌ 54 pts to go |
| P10 | 2008 | 64.9% | 64.9% | -1.2 | 85% | ❌ 20 pts to go |
| P11 | 1806 | 68.6% | 68.6% | +0.5 | 75% | 🟡 6 pts to go |
| P12 | 10 | 40.0% | 40.0% | +3.6 | n/a | no target |
| P13 | 207861 | 90.7% | 90.7% | -1.1 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 28.4% | 28.4% | -9.4 | n/a | no target |
| P01T | 207 | 98.1% | 98.1% | -0.2 | n/a | no target |
| P01_GOLD | 657 | 75.3% | 75.3% | -3.3 | 90% | ❌ 15 pts to go |
| P02 | 485 | 78.6% | 78.6% | -3.2 | 90% | ❌ 11 pts to go |
| P03 | 274 | 81.4% | 81.4% | -3.9 | 90% | 🟡 9 pts to go |
| P04 | 4772 | 70.7% | 70.7% | -12.1 | 85% | ❌ 14 pts to go |
| P05 | 428 | 44.9% | 44.9% | +0.4 | 70% | ❌ 25 pts to go |
| P06M | 31427 | 28.9% | 28.9% | -4.1 | n/a | no target |
| P06T | 55074 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 243 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 758 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 28702 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 71 | 45.1% | 45.1% | -32.7 | 100% | ❌ 55 pts to go |
| P10 | 2008 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1806 | 97.5% | 97.5% | -0.5 | 100% | 🟡 2 pts to go |
| P12 | 10 | 60.0% | 60.0% | +5.5 | n/a | no target |
| P13 | 207861 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 13.5% | 13.5% | -2.6 | n/a | no target |
| P01T | 207 | 54.1% | 54.1% | -5.7 | n/a | no target |
| P01_GOLD | 657 | 41.2% | 41.2% | -2.2 | 70% | ❌ 29 pts to go |
| P02 | 485 | 45.6% | 45.6% | -1.6 | 75% | ❌ 29 pts to go |
| P03 | 274 | 43.8% | 43.8% | -0.9 | 75% | ❌ 31 pts to go |
| P04 | 4772 | 35.0% | 35.0% | -3.7 | 70% | ❌ 35 pts to go |
| P05 | 428 | 22.0% | 22.0% | +0.7 | 55% | ❌ 33 pts to go |
| P06M | 31427 | 6.7% | 6.7% | +0.8 | n/a | no target |
| P06T | 55074 | 41.6% | 41.6% | -5.8 | n/a | no target |
| P06 | 243 | 52.3% | 52.3% | +1.2 | n/a | no target |
| P07 | 758 | 53.8% | 53.8% | +1.1 | 70% | ❌ 16 pts to go |
| P08 | 28702 | 56.0% | 56.0% | +1.2 | 75% | ❌ 19 pts to go |
| P09 | 71 | 22.5% | 22.5% | -24.4 | 85% | ❌ 62 pts to go |
| P10 | 2008 | 44.3% | 44.3% | -0.1 | 80% | ❌ 36 pts to go |
| P11 | 1806 | 51.9% | 51.9% | -1.4 | 70% | ❌ 18 pts to go |
| P12 | 10 | 30.0% | 30.0% | +2.7 | n/a | no target |
| P13 | 207861 | 5.9% | 5.9% | +0.4 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 27.0% | 27.0% | -10.8 | n/a | no target |
| P01T | 207 | 96.1% | 96.1% | -0.4 | n/a | no target |
| P01_GOLD | 657 | 69.9% | 69.9% | -3.0 | 90% | ❌ 20 pts to go |
| P02 | 485 | 73.4% | 73.4% | -3.3 | 90% | ❌ 17 pts to go |
| P03 | 274 | 78.1% | 78.1% | -3.9 | 90% | ❌ 12 pts to go |
| P04 | 4772 | 66.4% | 66.4% | -11.3 | 85% | ❌ 19 pts to go |
| P05 | 428 | 43.5% | 43.5% | +0.6 | 75% | ❌ 32 pts to go |
| P06M | 31427 | 28.0% | 28.0% | -4.9 | n/a | no target |
| P06T | 55074 | 97.8% | 97.8% | -0.5 | n/a | no target |
| P06 | 243 | 91.8% | 91.8% | +1.8 | n/a | no target |
| P07 | 758 | 94.2% | 94.2% | +2.5 | 100% | 🟡 6 pts to go |
| P08 | 28702 | 92.8% | 92.8% | +5.5 | 100% | 🟡 7 pts to go |
| P09 | 71 | 35.2% | 35.2% | -31.3 | n/a | no target |
| P10 | 2008 | 89.9% | 89.9% | -0.4 | 100% | ❌ 10 pts to go |
| P11 | 1806 | 90.2% | 90.2% | +0.0 | n/a | no target |
| P12 | 10 | 60.0% | 60.0% | +5.5 | n/a | no target |
| P13 | 207861 | 69.0% | 69.0% | -0.8 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 31.9% | 31.9% | -5.0 | n/a | no target · QC vendors: 56 rows, 100.0% filled |
| P01T | 207 | 22.7% | 22.7% | +3.0 | n/a | no target · QC vendors: 35 rows, 88.6% filled |
| P01_GOLD | 657 | 45.1% | 45.1% | +1.6 | 95% | ❌ 50 pts to go · QC vendors: 48 rows, 97.9% filled |
| P02 | 485 | 58.1% | 58.1% | +2.1 | 95% | ❌ 37 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 274 | 44.9% | 44.9% | +2.0 | 95% | ❌ 50 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 4772 | 39.3% | 39.3% | +6.9 | 95% | ❌ 56 pts to go · QC vendors: 591 rows, 97.3% filled |
| P05 | 428 | 14.7% | 14.7% | +0.7 | n/a | no target · QC vendors: 38 rows, 100.0% filled |
| P06M | 31427 | 34.0% | 34.0% | -3.5 | n/a | no target · QC vendors: 7666 rows, 99.9% filled |
| P06T | 55074 | 38.7% | 38.7% | +8.1 | n/a | no target · QC vendors: 21745 rows, 96.0% filled |
| P06 | 243 | 7.0% | 7.0% | -0.1 | n/a | no target · QC vendors: 10 rows, 60.0% filled |
| P07 | 758 | 7.0% | 7.0% | +0.1 | n/a | no target · QC vendors: 44 rows, 79.5% filled |
| P08 | 28702 | 7.1% | 7.1% | +0.1 | n/a | no target · QC vendors: 1750 rows, 92.9% filled |
| P09 | 71 | 28.2% | 28.2% | -45.3 | 95% | ❌ 67 pts to go · QC vendors: 7 rows, 100.0% filled |
| P10 | 2008 | 16.2% | 16.2% | +0.5 | n/a | no target · QC vendors: 201 rows, 92.5% filled |
| P11 | 1806 | 20.7% | 20.7% | +1.1 | n/a | no target · QC vendors: 322 rows, 94.1% filled |
| P12 | 10 | 80.0% | 80.0% | -1.8 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 207861 | 22.2% | 22.2% | +0.0 | n/a | no target · QC vendors: 46147 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 41.7% | 41.7% | -4.5 | n/a | no target · vendors with a registry record: 179 rows, 100.0% filled |
| P01T | 207 | 53.6% | 53.6% | -6.2 | n/a | no target · vendors with a registry record: 111 rows, 100.0% filled |
| P01_GOLD | 657 | 81.7% | 81.7% | +0.8 | 100% | ❌ 18 pts to go · vendors with a registry record: 537 rows, 100.0% filled |
| P02 | 485 | 79.0% | 79.0% | +0.6 | 100% | ❌ 21 pts to go · vendors with a registry record: 383 rows, 100.0% filled |
| P03 | 274 | 78.8% | 78.8% | +0.6 | 100% | ❌ 21 pts to go · vendors with a registry record: 216 rows, 100.0% filled |
| P04 | 4772 | 55.8% | 55.8% | +1.8 | 100% | ❌ 44 pts to go · vendors with a registry record: 2663 rows, 100.0% filled |
| P05 | 428 | 63.1% | 63.1% | +0.3 | n/a | no target · vendors with a registry record: 270 rows, 100.0% filled |
| P06M | 31427 | 38.3% | 38.3% | -2.9 | n/a | no target · vendors with a registry record: 12052 rows, 100.0% filled |
| P06T | 55074 | 65.4% | 65.4% | -2.2 | n/a | no target · vendors with a registry record: 36018 rows, 100.0% filled |
| P06 | 243 | 39.1% | 39.1% | -0.2 | n/a | no target · vendors with a registry record: 95 rows, 100.0% filled |
| P07 | 758 | 32.5% | 32.5% | +0.7 | n/a | no target · vendors with a registry record: 246 rows, 100.0% filled |
| P08 | 28702 | 32.6% | 32.6% | +2.6 | n/a | no target · vendors with a registry record: 9349 rows, 100.0% filled |
| P09 | 71 | 73.2% | 73.2% | -16.3 | n/a | no target · vendors with a registry record: 52 rows, 100.0% filled |
| P10 | 2008 | 40.2% | 40.2% | +0.1 | n/a | no target · vendors with a registry record: 808 rows, 100.0% filled |
| P11 | 1806 | 59.4% | 59.4% | +0.1 | n/a | no target · vendors with a registry record: 1073 rows, 100.0% filled |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 10 rows, 100.0% filled |
| P13 | 207861 | 40.7% | 40.7% | +0.5 | n/a | no target · vendors with a registry record: 84568 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 97.4% | 97.4% | +1.0 | 90% | ✅ met |
| P01T | 207 | 69.6% | 69.6% | -1.1 | 90% | ❌ 20 pts to go |
| P01_GOLD | 657 | 88.1% | 88.1% | +0.7 | 95% | 🟡 7 pts to go |
| P02 | 485 | 88.2% | 88.2% | +0.0 | 95% | 🟡 7 pts to go |
| P03 | 274 | 83.6% | 83.6% | +0.5 | 85% | 🟡 1 pts to go |
| P04 | 4772 | 69.3% | 69.3% | +4.8 | 90% | ❌ 21 pts to go |
| P05 | 428 | 76.6% | 76.6% | -1.4 | 75% | ✅ met |
| P06M | 31427 | 91.9% | 91.9% | -1.9 | n/a | no target |
| P06T | 55074 | 37.3% | 37.3% | +0.4 | n/a | no target |
| P06 | 243 | 72.0% | 72.0% | +0.9 | 80% | 🟡 8 pts to go |
| P07 | 758 | 60.9% | 61.1% | +2.7 | 80% | ❌ 19 pts to go |
| P08 | 28702 | 56.6% | 56.6% | +4.7 | 75% | ❌ 18 pts to go |
| P09 | 71 | 46.5% | 46.5% | -29.1 | 95% | ❌ 48 pts to go |
| P10 | 2008 | 45.5% | 45.5% | -1.3 | 70% | ❌ 24 pts to go |
| P11 | 1806 | 32.3% | 32.3% | +0.5 | 65% | ❌ 33 pts to go |
| P12 | 10 | 80.0% | 80.0% | +7.3 | 80% | ✅ met |
| P13 | 207861 | 39.2% | 39.2% | -6.4 | 60% | ❌ 21 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 16.6% | 16.6% | -1.9 | 50% | ❌ 33 pts to go |
| P01T | 207 | 16.9% | 16.9% | +0.7 | n/a | no target |
| P01_GOLD | 657 | 19.5% | 19.5% | -0.3 | 40% | ❌ 20 pts to go |
| P02 | 485 | 19.4% | 19.4% | -0.5 | 40% | ❌ 21 pts to go |
| P03 | 274 | 21.2% | 21.2% | +0.9 | 40% | ❌ 19 pts to go |
| P04 | 4772 | 15.2% | 15.2% | -1.1 | 40% | ❌ 25 pts to go |
| P05 | 428 | 21.3% | 21.3% | +0.4 | 25% | 🟡 4 pts to go |
| P06M | 31427 | 20.4% | 20.4% | +0.0 | n/a | no target |
| P06T | 55074 | 10.4% | 10.4% | +2.9 | n/a | no target |
| P06 | 243 | 23.0% | 23.0% | +5.5 | 35% | ❌ 12 pts to go |
| P07 | 758 | 25.9% | 25.9% | +6.8 | 35% | 🟡 9 pts to go |
| P08 | 28702 | 25.2% | 25.2% | +7.5 | 35% | 🟡 10 pts to go |
| P09 | 71 | 8.5% | 8.5% | -8.2 | n/a | no target |
| P10 | 2008 | 8.8% | 8.8% | +1.7 | 30% | ❌ 21 pts to go |
| P11 | 1806 | 10.3% | 10.3% | +3.8 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 207861 | 13.0% | 13.0% | +0.5 | 30% | ❌ 17 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 207 | 86.0% | 86.0% | +0.8 | 100% | ❌ 14 pts to go |
| P01_GOLD | 657 | 91.6% | 91.6% | +0.5 | 100% | 🟡 8 pts to go |
| P02 | 485 | 96.7% | 96.7% | +0.1 | 100% | 🟡 3 pts to go |
| P03 | 274 | 90.1% | 90.1% | +0.6 | 100% | 🟡 10 pts to go |
| P04 | 4772 | 79.4% | 79.4% | +6.9 | 100% | ❌ 21 pts to go |
| P05 | 428 | 90.2% | 90.2% | +0.2 | 100% | 🟡 10 pts to go |
| P06M | 31427 | 99.6% | 99.6% | +0.2 | n/a | no target |
| P06T | 55074 | 61.2% | 61.2% | +2.5 | n/a | no target |
| P06 | 243 | 83.5% | 83.5% | +1.4 | 95% | ❌ 12 pts to go |
| P07 | 758 | 87.6% | 87.6% | +2.2 | 95% | 🟡 7 pts to go |
| P08 | 28702 | 86.2% | 86.2% | +1.7 | 95% | 🟡 9 pts to go |
| P09 | 71 | 94.4% | 94.4% | -2.0 | 100% | 🟡 6 pts to go |
| P10 | 2008 | 53.8% | 53.9% | -0.8 | 95% | ❌ 41 pts to go |
| P11 | 1806 | 63.7% | 63.7% | +2.8 | 80% | ❌ 16 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 207861 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 64.8% | 64.8% | -6.3 | n/a | no target |
| P01T | 207 | 71.5% | 71.5% | -2.7 | n/a | no target |
| P01_GOLD | 657 | 73.2% | 73.2% | +0.0 | 90% | ❌ 17 pts to go |
| P02 | 485 | 77.3% | 77.3% | -1.1 | 95% | ❌ 18 pts to go |
| P03 | 274 | 74.5% | 74.5% | +0.4 | 95% | ❌ 20 pts to go |
| P04 | 4772 | 69.6% | 69.6% | +0.1 | 95% | ❌ 25 pts to go |
| P05 | 428 | 71.5% | 71.5% | -1.0 | 90% | ❌ 18 pts to go |
| P06M | 31427 | 69.7% | 69.7% | -7.0 | n/a | no target |
| P06T | 55074 | 57.6% | 57.6% | -1.0 | n/a | no target |
| P06 | 243 | 71.2% | 71.2% | +5.8 | 95% | ❌ 24 pts to go |
| P07 | 758 | 67.2% | 67.2% | +7.5 | 90% | ❌ 23 pts to go |
| P08 | 28702 | 70.6% | 70.6% | +12.0 | 95% | ❌ 24 pts to go |
| P09 | 71 | 66.2% | 66.2% | -19.6 | 100% | ❌ 34 pts to go |
| P10 | 2008 | 52.8% | 52.8% | -1.0 | 95% | ❌ 42 pts to go |
| P11 | 1806 | 32.7% | 32.7% | +2.0 | 75% | ❌ 42 pts to go |
| P12 | 10 | 80.0% | 80.0% | -1.8 | n/a | no target |
| P13 | 207861 | 56.3% | 56.3% | -11.6 | 95% | ❌ 39 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 76.9% | 76.9% | -6.6 | n/a | no target |
| P01T | 207 | 89.9% | 89.9% | -1.8 | 95% | 🟡 5 pts to go |
| P01_GOLD | 657 | 85.2% | 85.2% | +0.2 | 90% | 🟡 5 pts to go |
| P02 | 485 | 90.3% | 90.3% | -0.7 | 95% | 🟡 5 pts to go |
| P03 | 274 | 84.3% | 84.3% | +0.5 | 95% | ❌ 11 pts to go |
| P04 | 4772 | 90.3% | 90.3% | -1.3 | 90% | ✅ met |
| P05 | 428 | 92.5% | 92.5% | +0.1 | 95% | 🟡 2 pts to go |
| P06M | 31427 | 80.9% | 80.9% | -4.4 | n/a | no target |
| P06T | 55074 | 86.3% | 86.3% | +1.7 | n/a | no target |
| P06 | 243 | 92.6% | 92.6% | +7.2 | 100% | 🟡 7 pts to go |
| P07 | 758 | 94.3% | 94.3% | +10.7 | 100% | 🟡 6 pts to go |
| P08 | 28702 | 94.9% | 94.9% | +17.1 | 100% | 🟡 5 pts to go |
| P09 | 71 | 71.8% | 71.8% | -2.4 | n/a | no target |
| P10 | 2008 | 94.2% | 94.2% | -0.2 | 100% | 🟡 6 pts to go |
| P11 | 1806 | 55.4% | 55.4% | +4.3 | 80% | ❌ 25 pts to go |
| P12 | 10 | 90.0% | 90.0% | -0.9 | n/a | no target |
| P13 | 207861 | 71.8% | 71.8% | -9.0 | 95% | ❌ 23 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 3.5% | 3.5% | +0.3 | n/a | no target |
| P01T | 207 | 9.2% | 9.2% | +0.5 | n/a | no target |
| P01_GOLD | 657 | 13.4% | 13.4% | -0.6 | 25% | ❌ 12 pts to go |
| P02 | 485 | 24.1% | 24.1% | -0.7 | 40% | ❌ 16 pts to go |
| P03 | 274 | 8.8% | 8.8% | -0.2 | 20% | ❌ 11 pts to go |
| P04 | 4772 | 2.8% | 2.8% | -0.5 | 20% | ❌ 17 pts to go |
| P05 | 428 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 31427 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 55074 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 243 | 5.3% | 5.3% | -0.1 | n/a | no target |
| P07 | 758 | 8.2% | 8.2% | +0.3 | n/a | no target |
| P08 | 28702 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | -6.2 | n/a | no target |
| P10 | 2008 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1806 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 13.3% | 13.3% | -2.8 | n/a | no target |
| P01T | 207 | 18.4% | 18.4% | -0.8 | 70% | ❌ 52 pts to go |
| P01_GOLD | 657 | 42.2% | 42.2% | +0.1 | 80% | ❌ 38 pts to go |
| P02 | 485 | 55.3% | 55.3% | -2.0 | 90% | ❌ 35 pts to go |
| P03 | 274 | 19.0% | 19.0% | -0.2 | 60% | ❌ 41 pts to go |
| P04 | 4772 | 16.5% | 16.5% | -3.7 | 85% | ❌ 68 pts to go |
| P05 | 428 | 11.7% | 11.7% | +0.6 | 50% | ❌ 38 pts to go |
| P06M | 31427 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06T | 55074 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 243 | 13.6% | 13.6% | +0.4 | n/a | no target |
| P07 | 758 | 9.9% | 9.9% | +0.8 | n/a | no target |
| P08 | 28702 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 71 | 33.8% | 33.8% | -38.2 | 95% | ❌ 61 pts to go |
| P10 | 2008 | 1.5% | 1.5% | -0.1 | n/a | no target |
| P11 | 1806 | 13.2% | 13.2% | +0.2 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | +2.7 | n/a | no target |
| P13 | 207861 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 5.6% | 5.6% | +0.0 | n/a | no target |
| P01T | 207 | 11.6% | 11.6% | +2.4 | n/a | no target |
| P01_GOLD | 657 | 33.5% | 33.5% | -0.3 | 70% | ❌ 36 pts to go |
| P02 | 485 | 37.7% | 37.7% | -1.0 | 75% | ❌ 37 pts to go |
| P03 | 274 | 20.1% | 20.1% | +0.9 | 55% | ❌ 35 pts to go |
| P04 | 4772 | 16.2% | 16.2% | -4.0 | 75% | ❌ 59 pts to go |
| P05 | 428 | 10.7% | 10.7% | +0.5 | 50% | ❌ 39 pts to go |
| P06M | 31427 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06T | 55074 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 243 | 6.2% | 6.2% | +0.5 | n/a | no target |
| P07 | 758 | 5.1% | 5.1% | +0.5 | n/a | no target |
| P08 | 28702 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 71 | 33.8% | 33.8% | -34.9 | 95% | ❌ 61 pts to go |
| P10 | 2008 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1806 | 13.0% | 13.0% | +0.2 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 207861 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 11.4% | 11.4% | +3.8 | n/a | no target |
| P01T | 207 | 8.2% | 8.2% | -0.5 | n/a | no target |
| P01_GOLD | 657 | 56.2% | 56.3% | -0.9 | 80% | ❌ 24 pts to go |
| P02 | 485 | 43.9% | 44.1% | -1.4 | 75% | ❌ 31 pts to go |
| P03 | 274 | 35.8% | 35.8% | -0.3 | 70% | ❌ 34 pts to go |
| P04 | 4772 | 16.1% | 16.3% | -3.8 | 70% | ❌ 54 pts to go |
| P05 | 428 | 14.3% | 14.3% | +0.3 | 50% | ❌ 36 pts to go |
| P06M | 31427 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P06T | 55074 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 243 | 14.0% | 14.0% | +0.8 | n/a | no target |
| P07 | 758 | 1.5% | 1.5% | +0.4 | n/a | no target |
| P08 | 28702 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P09 | 71 | 45.1% | 45.1% | -1.8 | 80% | ❌ 35 pts to go |
| P10 | 2008 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P11 | 1806 | 4.4% | 4.5% | -0.1 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | -6.4 | n/a | no target |
| P13 | 207861 | 0.1% | 0.1% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 17.9% | 17.9% | +3.0 | n/a | no target |
| P01T | 207 | 21.3% | 21.3% | +2.1 | 60% | ❌ 39 pts to go |
| P01_GOLD | 657 | 60.7% | 60.7% | -1.5 | 70% | 🟡 9 pts to go |
| P02 | 485 | 37.9% | 37.9% | -1.6 | 50% | ❌ 12 pts to go |
| P03 | 274 | 46.0% | 46.0% | -1.7 | 55% | 🟡 9 pts to go |
| P04 | 4772 | 10.7% | 10.7% | -1.8 | 40% | ❌ 29 pts to go |
| P05 | 428 | 16.1% | 16.1% | -0.5 | 40% | ❌ 24 pts to go |
| P06M | 31427 | 4.3% | 4.3% | +1.5 | n/a | no target |
| P06T | 55074 | 1.6% | 1.6% | +0.1 | n/a | no target |
| P06 | 243 | 18.5% | 18.5% | +0.3 | n/a | no target |
| P07 | 758 | 5.7% | 5.7% | +0.8 | n/a | no target |
| P08 | 28702 | 2.6% | 2.6% | +0.5 | n/a | no target |
| P09 | 71 | 11.3% | 11.3% | +5.5 | n/a | no target |
| P10 | 2008 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P11 | 1806 | 4.0% | 4.0% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 27.7% | 27.7% | +6.0 | n/a | no target |
| P01T | 207 | 26.6% | 26.6% | -1.3 | 65% | ❌ 38 pts to go |
| P01_GOLD | 657 | 67.3% | 67.3% | -1.3 | 70% | 🟡 3 pts to go |
| P02 | 485 | 23.3% | 23.3% | -0.4 | 50% | ❌ 27 pts to go |
| P03 | 274 | 49.3% | 49.3% | -1.1 | 60% | ❌ 11 pts to go |
| P04 | 4772 | 5.7% | 5.7% | +0.1 | 40% | ❌ 34 pts to go |
| P05 | 428 | 19.6% | 19.6% | -0.3 | 45% | ❌ 25 pts to go |
| P06M | 31427 | 2.6% | 2.6% | +0.9 | n/a | no target |
| P06T | 55074 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 243 | 28.8% | 28.8% | -0.5 | n/a | no target |
| P07 | 758 | 5.0% | 5.0% | -0.1 | n/a | no target |
| P08 | 28702 | 1.1% | 1.1% | +0.2 | n/a | no target |
| P09 | 71 | 31.0% | 31.0% | +20.1 | n/a | no target |
| P10 | 2008 | 3.2% | 3.2% | -0.1 | n/a | no target |
| P11 | 1806 | 3.5% | 3.5% | -0.1 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 18.9% | 18.9% | +6.9 | n/a | no target |
| P01T | 207 | 13.5% | 13.5% | +0.8 | n/a | no target |
| P01_GOLD | 657 | 48.9% | 48.9% | -1.3 | 50% | 🟡 1 pts to go |
| P02 | 485 | 36.7% | 36.7% | -0.9 | n/a | no target |
| P03 | 274 | 51.1% | 51.1% | +0.3 | 60% | 🟡 9 pts to go |
| P04 | 4772 | 9.9% | 9.9% | -2.9 | n/a | no target |
| P05 | 428 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 31427 | 1.1% | 1.1% | +0.3 | n/a | no target |
| P06T | 55074 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 243 | 18.9% | 18.9% | -1.5 | n/a | no target |
| P07 | 758 | 5.3% | 5.3% | -0.4 | n/a | no target |
| P08 | 28702 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P09 | 71 | 23.9% | 23.9% | +3.2 | n/a | no target |
| P10 | 2008 | 2.3% | 2.3% | -0.2 | n/a | no target |
| P11 | 1806 | 2.4% | 2.4% | -0.3 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 207861 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 9.3% | 9.3% | +0.5 | 15% | 🟡 6 pts to go |
| P01T | 207 | 13.5% | 13.5% | +0.8 | 15% | 🟡 2 pts to go |
| P01_GOLD | 657 | 34.1% | 34.1% | -1.0 | 40% | 🟡 6 pts to go |
| P02 | 485 | 11.5% | 11.8% | -0.7 | 25% | ❌ 14 pts to go |
| P03 | 274 | 15.3% | 15.3% | -1.2 | 25% | 🟡 10 pts to go |
| P04 | 4772 | 2.3% | 2.3% | -0.4 | 15% | ❌ 13 pts to go |
| P05 | 428 | 6.5% | 6.5% | -0.1 | 15% | 🟡 8 pts to go |
| P06M | 31427 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 55074 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 243 | 9.9% | 9.9% | +0.6 | 15% | 🟡 5 pts to go |
| P07 | 758 | 3.6% | 3.6% | +0.2 | 15% | ❌ 11 pts to go |
| P08 | 28702 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 71 | 4.2% | 4.2% | +3.1 | 15% | ❌ 11 pts to go |
| P10 | 2008 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1806 | 1.3% | 1.3% | +0.1 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 207861 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 8.4% | 8.4% | +2.8 | 15% | 🟡 7 pts to go |
| P01T | 207 | 12.1% | 12.1% | +1.2 | 25% | ❌ 13 pts to go |
| P01_GOLD | 657 | 28.2% | 28.2% | -0.7 | 25% | ✅ met |
| P02 | 485 | 24.3% | 24.3% | -1.1 | 15% | ✅ met |
| P03 | 274 | 21.9% | 21.9% | +0.1 | 15% | ✅ met |
| P04 | 4772 | 3.2% | 3.2% | -0.8 | 15% | ❌ 12 pts to go |
| P05 | 428 | 11.4% | 11.4% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 31427 | 0.9% | 0.9% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 55074 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 243 | 7.8% | 7.8% | +0.7 | 15% | 🟡 7 pts to go |
| P07 | 758 | 1.6% | 1.6% | -0.2 | 15% | ❌ 13 pts to go |
| P08 | 28702 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P09 | 71 | 2.8% | 2.8% | +1.3 | 15% | ❌ 12 pts to go |
| P10 | 2008 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1806 | 1.8% | 1.8% | +0.0 | 15% | ❌ 13 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 207861 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 2.6% | 2.6% | +1.0 | 20% | ❌ 17 pts to go |
| P01T | 207 | 3.4% | 3.4% | +0.3 | 20% | ❌ 17 pts to go |
| P01_GOLD | 657 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 485 | 1.4% | 1.4% | -0.1 | 20% | ❌ 19 pts to go |
| P03 | 274 | 1.5% | 1.5% | -0.4 | 20% | ❌ 18 pts to go |
| P04 | 4772 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P05 | 428 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 31427 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 243 | 1.6% | 1.6% | +0.2 | 20% | ❌ 18 pts to go |
| P07 | 758 | 0.3% | 0.3% | +0.1 | 20% | ❌ 20 pts to go |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 71 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2008 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1806 | 0.2% | 0.2% | +0.1 | 20% | ❌ 20 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 2.6% | 2.6% | +1.0 | 15% | ❌ 12 pts to go |
| P01T | 207 | 2.4% | 2.4% | -0.7 | 15% | ❌ 13 pts to go |
| P01_GOLD | 657 | 10.8% | 10.8% | +0.3 | 15% | 🟡 4 pts to go |
| P02 | 485 | 10.5% | 10.5% | -1.0 | 15% | 🟡 4 pts to go |
| P03 | 274 | 20.4% | 20.4% | -0.3 | 15% | ✅ met |
| P04 | 4772 | 1.9% | 1.9% | -0.5 | 15% | ❌ 13 pts to go |
| P05 | 428 | 3.0% | 3.0% | +0.2 | 15% | ❌ 12 pts to go |
| P06M | 31427 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P06T | 55074 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 243 | 4.1% | 4.1% | +0.2 | 15% | ❌ 11 pts to go |
| P07 | 758 | 1.8% | 1.8% | +0.6 | 15% | ❌ 13 pts to go |
| P08 | 28702 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P09 | 71 | 2.8% | 2.8% | +2.1 | 15% | ❌ 12 pts to go |
| P10 | 2008 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1806 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 207861 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 19.1% | 19.1% | +6.7 | 20% | 🟡 1 pts to go |
| P01T | 207 | 14.5% | 14.5% | +1.0 | 40% | ❌ 26 pts to go |
| P01_GOLD | 657 | 45.1% | 45.1% | -1.5 | 40% | ✅ met |
| P02 | 485 | 42.3% | 42.3% | -0.9 | 20% | ✅ met |
| P03 | 274 | 49.3% | 49.3% | +0.8 | 35% | ✅ met |
| P04 | 4772 | 11.6% | 11.6% | -3.3 | 20% | 🟡 8 pts to go |
| P05 | 428 | 15.7% | 15.7% | +0.1 | 20% | 🟡 4 pts to go |
| P06M | 31427 | 1.3% | 1.3% | +0.3 | 20% | ❌ 19 pts to go |
| P06T | 55074 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 243 | 18.5% | 18.5% | -2.6 | 20% | 🟡 2 pts to go |
| P07 | 758 | 6.2% | 6.2% | +0.1 | 20% | ❌ 14 pts to go |
| P08 | 28702 | 0.9% | 0.9% | +0.1 | 20% | ❌ 19 pts to go |
| P09 | 71 | 12.7% | 12.7% | -8.4 | 20% | 🟡 7 pts to go |
| P10 | 2008 | 3.6% | 3.6% | -0.2 | 20% | ❌ 16 pts to go |
| P11 | 1806 | 3.0% | 3.0% | -0.2 | 20% | ❌ 17 pts to go |
| P12 | 10 | 10.0% | 10.0% | +0.9 | 20% | 🟡 10 pts to go |
| P13 | 207861 | 0.3% | 0.3% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 11.0% | 11.0% | -7.1 | n/a | no target |
| P01T | 207 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 657 | 68.9% | 68.9% | -2.7 | 95% | ❌ 26 pts to go |
| P02 | 485 | 63.1% | 63.1% | -3.1 | 95% | ❌ 32 pts to go |
| P03 | 274 | 55.5% | 55.5% | -2.4 | 90% | ❌ 34 pts to go |
| P04 | 4772 | 20.9% | 20.9% | -5.6 | 85% | ❌ 64 pts to go |
| P05 | 428 | 39.3% | 39.3% | +0.4 | 75% | ❌ 36 pts to go |
| P06M | 31427 | 22.3% | 22.3% | -5.8 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 77.5% | 77.5% | -11.6 | 100% | ❌ 22 pts to go |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 4.0% | 4.0% | +0.2 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 11.0% | 11.0% | -7.1 | n/a | no target |
| P01T | 207 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 70.6% | 70.6% | -2.9 | 100% | ❌ 29 pts to go |
| P02 | 485 | 64.9% | 64.9% | -3.3 | 100% | ❌ 35 pts to go |
| P03 | 274 | 58.0% | 58.0% | -2.5 | n/a | no target |
| P04 | 4772 | 21.2% | 21.2% | -5.8 | 95% | ❌ 74 pts to go |
| P05 | 428 | 35.0% | 35.0% | +0.4 | 80% | ❌ 45 pts to go |
| P06M | 31427 | 22.3% | 22.3% | -5.8 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 80.3% | 80.3% | -11.3 | 100% | ❌ 20 pts to go |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 4.2% | 4.2% | +0.2 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 82.5% | 82.5% | -1.8 | n/a | no target |
| P01T | 207 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 657 | 54.2% | 54.2% | +1.9 | 85% | ❌ 31 pts to go |
| P02 | 485 | 60.4% | 60.4% | +1.2 | 90% | ❌ 30 pts to go |
| P03 | 274 | 47.1% | 47.1% | +3.1 | 85% | ❌ 38 pts to go |
| P04 | 4772 | 38.1% | 38.1% | +9.0 | 90% | ❌ 52 pts to go |
| P05 | 428 | 32.9% | 32.9% | +0.0 | 75% | ❌ 42 pts to go |
| P06M | 31427 | 82.8% | 82.8% | -1.5 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 64.8% | 64.8% | -17.0 | 95% | ❌ 30 pts to go |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 3.9% | 3.9% | +0.6 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 52.4% | 52.4% | -13.5 | n/a | no target |
| P01T | 207 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 657 | 53.9% | 53.9% | +1.9 | 85% | ❌ 31 pts to go |
| P02 | 485 | 54.4% | 54.4% | +1.0 | 90% | ❌ 36 pts to go |
| P03 | 274 | 47.1% | 47.1% | +2.7 | 85% | ❌ 38 pts to go |
| P04 | 4772 | 33.8% | 33.8% | +9.2 | 90% | ❌ 56 pts to go |
| P05 | 428 | 42.1% | 42.1% | -0.6 | 75% | ❌ 33 pts to go |
| P06M | 31427 | 59.0% | 59.0% | -10.2 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | +1.0 | 95% | ❌ 94 pts to go |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 3.0% | 3.0% | +0.5 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 97.2% | 97.2% | +2.0 | n/a | no target |
| P01T | 207 | 95.2% | 95.2% | -0.9 | n/a | no target |
| P01_GOLD | 657 | 85.8% | 86.0% | +0.3 | 100% | ❌ 14 pts to go |
| P02 | 485 | 78.4% | 78.4% | +0.8 | 100% | ❌ 22 pts to go |
| P03 | 274 | 92.7% | 92.7% | +0.2 | n/a | no target |
| P04 | 4772 | 53.9% | 53.9% | +3.3 | 95% | ❌ 41 pts to go |
| P05 | 428 | 77.6% | 77.6% | +0.3 | 95% | ❌ 17 pts to go |
| P06M | 31427 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 55074 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 243 | 21.0% | 21.0% | +0.6 | n/a | no target |
| P07 | 758 | 10.3% | 10.3% | +0.1 | n/a | no target |
| P08 | 28702 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 71 | 93.0% | 93.0% | -5.2 | 100% | 🟡 7 pts to go |
| P10 | 2008 | 71.0% | 71.0% | +0.4 | n/a | no target |
| P11 | 1806 | 70.2% | 70.2% | +0.4 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 99.4% | 99.4% | -0.2 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 97.2% | 97.2% | +2.0 | n/a | no target |
| P01T | 207 | 95.2% | 95.2% | -0.9 | n/a | no target |
| P01_GOLD | 657 | 88.9% | 89.0% | +0.2 | 100% | ❌ 11 pts to go |
| P02 | 485 | 79.6% | 79.6% | +0.8 | 100% | ❌ 20 pts to go |
| P03 | 274 | 93.4% | 93.4% | +0.2 | n/a | no target |
| P04 | 4772 | 56.5% | 56.5% | +2.5 | 95% | ❌ 38 pts to go |
| P05 | 428 | 89.7% | 89.7% | +0.4 | 70% | ✅ met |
| P06M | 31427 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 55074 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 243 | 21.0% | 21.0% | +0.6 | n/a | no target |
| P07 | 758 | 10.3% | 10.3% | +0.1 | n/a | no target |
| P08 | 28702 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 71 | 93.0% | 93.0% | -5.2 | 100% | 🟡 7 pts to go |
| P10 | 2008 | 71.0% | 71.0% | +0.4 | n/a | no target |
| P11 | 1806 | 70.3% | 70.3% | +0.4 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 207 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 16.1% | 16.1% | -0.8 | 60% | ❌ 44 pts to go · rows from a source that publishes bids: 368 rows, 28.8% filled |
| P02 | 485 | 9.9% | 9.9% | -0.8 | n/a | no target · rows from a source that publishes bids: 294 rows, 16.3% filled |
| P03 | 274 | 13.1% | 13.1% | -0.8 | n/a | no target · rows from a source that publishes bids: 142 rows, 25.4% filled |
| P04 | 4772 | 1.3% | 1.3% | -0.4 | n/a | no target · rows from a source that publishes bids: 882 rows, 7.0% filled |
| P05 | 428 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 59 rows, 18.6% filled |
| P06M | 31427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55074 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 5.6% | 5.6% | +1.2 | n/a | no target · rows from a source that publishes bids: 63 rows, 6.3% filled |
| P10 | 2008 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1806 | 0.4% | 0.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 69 rows, 11.6% filled |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 10 rows, 0.0% filled |
| P13 | 207861 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 207 | 0.0% | 97.6% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 51.1% | 83.0% | -2.3 | 90% | ❌ 39 pts to go |
| P02 | 485 | 50.3% | 87.0% | -3.1 | 90% | ❌ 40 pts to go |
| P03 | 274 | 44.2% | 80.7% | -1.7 | 90% | ❌ 46 pts to go |
| P04 | 4772 | 14.8% | 94.7% | -4.8 | 90% | ❌ 75 pts to go |
| P05 | 428 | 0.0% | 81.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 31427 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55074 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 11.3% | 18.3% | +8.4 | 90% | ❌ 79 pts to go |
| P10 | 2008 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1806 | 2.2% | 97.6% | +0.1 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 207 | 1.0% | 98.6% | +0.1 | n/a | no target |
| P01_GOLD | 657 | 25.3% | 57.1% | -1.2 | 90% | ❌ 65 pts to go |
| P02 | 485 | 49.7% | 86.4% | -2.7 | n/a | no target |
| P03 | 274 | 24.5% | 60.9% | -0.7 | n/a | no target |
| P04 | 4772 | 16.0% | 95.9% | -5.4 | n/a | no target |
| P05 | 428 | 0.5% | 81.8% | +0.0 | n/a | no target |
| P06M | 31427 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55074 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 2.8% | 9.9% | -37.6 | n/a | no target |
| P10 | 2008 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1806 | 2.3% | 97.7% | +0.1 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 207 | 2.4% | 100.0% | +0.2 | n/a | no target |
| P01_GOLD | 657 | 50.1% | 81.9% | -1.9 | 95% | ❌ 45 pts to go |
| P02 | 485 | 55.3% | 92.0% | -2.8 | n/a | no target |
| P03 | 274 | 48.2% | 84.7% | -2.2 | n/a | no target |
| P04 | 4772 | 16.6% | 96.5% | -5.6 | n/a | no target |
| P05 | 428 | 5.1% | 86.4% | +0.1 | n/a | no target |
| P06M | 31427 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55074 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 243 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28702 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 16.9% | 23.9% | -43.5 | n/a | no target |
| P10 | 2008 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1806 | 2.4% | 97.8% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 207861 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 207 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 657 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 485 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 274 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4772 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 428 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 31427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55074 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 243 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 758 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 28702 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2008 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1806 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 207861 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 207 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 657 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 485 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 274 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4772 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 428 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 31427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55074 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 243 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 758 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 28702 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2008 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1806 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 207861 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 207 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 657 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 485 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 274 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4772 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 428 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 31427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55074 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 243 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 758 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 28702 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2008 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1806 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 207861 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

