# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **52 of 446 met** (11.7%); 97 within 10 points; 297 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 67, P01T 325, P01_GOLD 626, P02 464, P03 256, P04 3315, P05 419, P06M 6303, P06T 57911, P06 281, P07 690, P08 20898, P09 303, P10R 99903, P10 2665, P11 7106, P12 8, P13 18386

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 22.4% | 8 | PO rule (55 rows) |
| P01T | 325 | 0.9% | 21.5% | 7 | payment terms (250 rows) |
| P01_GOLD | 626 | 23.5% | 67.4% | 9 | payment terms (214 rows) |
| P02 | 464 | 7.5% | 51.9% | 9 | PO rule (353 rows) |
| P03 | 256 | 13.7% | 56.6% | 9 | PO rule (122 rows) |
| P04 | 3315 | 1.4% | 17.6% | 6 | PO rule (3116 rows) |
| P05 | 419 | 1.0% | 16.7% | 7 | payment terms (343 rows) |
| P06M | 6303 | 0.0% | 2.1% | 8 | PO rule (6273 rows) |
| P06T | 57911 | 0.0% | 2.2% | 6 | PO rule (57560 rows) |
| P06 | 281 | 0.0% | 7.1% | 6 | reference to quote (PO / contract / vendor id) (281 rows) |
| P07 | 690 | 0.0% | 1.4% | 6 | reference to quote (PO / contract / vendor id) (690 rows) |
| P08 | 20898 | 0.0% | 0.2% | 5 | reference to quote (PO / contract / vendor id) (20898 rows) |
| P09 | 303 | 1.0% | 43.9% | 8 | payment terms (283 rows) |
| P10R | 99903 | 0.0% | 16.5% | 7 | PO rule (99864 rows) |
| P10 | 2665 | 0.0% | 0.7% | 5 | reference to quote (PO / contract / vendor id) (2665 rows) |
| P11 | 7106 | 0.1% | 2.4% | 6 | PO rule (7011 rows) |
| P12 | 8 | 0.0% | 50.0% | 9 | PO rule (8 rows) |
| P13 | 18386 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (18386 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 67 | 6 | 6 | 55 | 0 | 0 | 71 |
| P01T | 325 | 31 | 55 | 239 | 0 | 0 | 71 |
| P01_GOLD | 626 | 224 | 185 | 217 | 0 | 0 | 81 |
| P02 | 464 | 0 | 187 | 277 | 0 | 0 | 66 |
| P03 | 256 | 0 | 0 | 242 | 14 | 0 | 57 |
| P04 | 3315 | 0 | 0 | 2767 | 548 | 0 | 46 |
| P05 | 419 | 15 | 28 | 354 | 22 | 0 | 51 |
| P06M | 6303 | 0 | 3 | 6230 | 70 | 0 | 51 |
| P06T | 57911 | 0 | 41 | 46628 | 11242 | 0 | 38 |
| P06 | 281 | 19 | 43 | 219 | 0 | 0 | 69 |
| P07 | 690 | 0 | 23 | 642 | 25 | 0 | 53 |
| P08 | 20898 | 0 | 0 | 17678 | 3220 | 0 | 43 |
| P09 | 303 | 3 | 12 | 285 | 3 | 0 | 53 |
| P10R | 99903 | 2 | 10 | 64281 | 35610 | 0 | 38 |
| P10 | 2665 | 2 | 13 | 1946 | 704 | 0 | 43 |
| P11 | 7106 | 6 | 9 | 42 | 0 | 7049 | 23 |
| P12 | 8 | 0 | 1 | 7 | 0 | 0 | 54 |
| P13 | 18386 | 2 | 13 | 14499 | 3872 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 67 | 52 | 77.6% | the buyer's PO / reference rule (7) |
| P01T | 325 | 141 | 43.4% | bill-to legal name and address (146) |
| P01_GOLD | 626 | 456 | 72.8% | bill-to legal name and address (119) |
| P02 | 464 | 306 | 65.9% | the buyer's PO / reference rule (79) |
| P03 | 256 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (256) |
| P04 | 3315 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3315) |
| P05 | 419 | 46 | 11.0% | a confirmed invoicing / AP or finance channel (332) |
| P06M | 6303 | 48 | 0.8% | a confirmed invoicing / AP or finance channel (6222) |
| P06T | 57911 | 293 | 0.5% | a confirmed invoicing / AP or finance channel (57035) |
| P06 | 281 | 43 | 15.3% | bill-to legal name and address (127) |
| P07 | 690 | 10 | 1.4% | bill-to legal name and address (311) |
| P08 | 20898 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (20898) |
| P09 | 303 | 40 | 13.2% | a confirmed invoicing / AP or finance channel (253) |
| P10R | 99903 | 416 | 0.4% | a confirmed invoicing / AP or finance channel (98760) |
| P10 | 2665 | 4 | 0.2% | a confirmed invoicing / AP or finance channel (2569) |
| P11 | 7106 | 10 | 0.1% | a confirmed invoicing / AP or finance channel (7049) |
| P12 | 8 | 3 | 37.5% | a confirmed invoicing / AP or finance channel (5) |
| P13 | 18386 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (18025) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 67 | 6 | 9.0% | 6 | 0 | the vendor's GST/HST number (BN9) (53) |
| P01T | 325 | 65 | 20.0% | 21 | 0 | the vendor's GST/HST number (BN9) (168) |
| P01_GOLD | 626 | 394 | 62.9% | 12 | 0 | the vendor's GST/HST number (BN9) (151) |
| P02 | 464 | 210 | 45.3% | 21 | 0 | the vendor's GST/HST number (BN9) (193) |
| P03 | 256 | 17 | 6.6% | 0 | 130 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89) |
| P04 | 3315 | 42 | 1.3% | 8 | 749 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2457) |
| P05 | 419 | 22 | 5.3% | 8 | 101 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (224) |
| P06M | 6303 | 1 | 0.0% | 10 | 115 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6092) |
| P06T | 57911 | 57 | 0.1% | 91 | 8011 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (48877) |
| P06 | 281 | 15 | 5.3% | 24 | 0 | the vendor's GST/HST number (BN9) (164) |
| P07 | 690 | 5 | 0.7% | 48 | 20 | the vendor's GST/HST number (BN9) (376) |
| P08 | 20898 | 2 | 0.0% | 5 | 1573 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (19260) |
| P09 | 303 | 39 | 12.9% | 1 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (122) |
| P10R | 99903 | 839 | 0.8% | 0 | 52083 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (46611) |
| P10 | 2665 | 4 | 0.2% | 18 | 344 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2195) |
| P11 | 7106 | 11 | 0.2% | 13 | 0 | a confirmed invoicing / AP or finance channel (7017) |
| P12 | 8 | 2 | 25.0% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2) |
| P13 | 18386 | 10 | 0.1% | 259 | 10805 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7180) |
| **all** | 219926 | 1741 | 0.8% | 545 | 74056 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 61 | 0 | 0 | 0 | 16 | 7 | 0 | 55 | 58 | 0 |
| P01T | 294 | 0 | 0 | 0 | 126 | 138 | 24 | 241 | 252 | 30 |
| P01_GOLD | 402 | 0 | 0 | 0 | 11 | 102 | 37 | 194 | 228 | 59 |
| P02 | 464 | 0 | 464 | 0 | 40 | 68 | 20 | 353 | 283 | 21 |
| P03 | 256 | 0 | 256 | 0 | 13 | 54 | 24 | 122 | 128 | 28 |
| P04 | 3315 | 0 | 3315 | 0 | 1306 | 1414 | 732 | 3116 | 2860 | 137 |
| P05 | 404 | 0 | 351 | 0 | 66 | 132 | 50 | 335 | 345 | 53 |
| P06M | 6303 | 0 | 6303 | 0 | 2343 | 662 | 112 | 6273 | 6239 | 4 |
| P06T | 57911 | 0 | 57911 | 0 | 43918 | 40725 | 13019 | 57560 | 56485 | 360 |
| P06 | 262 | 0 | 0 | 0 | 95 | 114 | 51 | 186 | 224 | 5 |
| P07 | 690 | 0 | 690 | 0 | 370 | 353 | 111 | 637 | 640 | 15 |
| P08 | 20898 | 0 | 20898 | 0 | 14581 | 12080 | 4108 | 20631 | 20253 | 210 |
| P09 | 300 | 0 | 279 | 0 | 9 | 69 | 3 | 273 | 285 | 44 |
| P10R | 99901 | 0 | 99726 | 0 | 76036 | 74116 | 40861 | 99864 | 99708 | 20 |
| P10 | 2663 | 0 | 2627 | 0 | 1232 | 1616 | 912 | 2594 | 2543 | 112 |
| P11 | 7100 | 7049 | 6994 | 0 | 5733 | 6194 | 950 | 7011 | 6761 | 38 |
| P12 | 8 | 0 | 7 | 0 | 0 | 2 | 0 | 8 | 7 | 0 |
| P13 | 18384 | 0 | 18275 | 0 | 8630 | 10765 | 4467 | 18349 | 18343 | 22 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 19964 |
| ap_system_hint | P10R | 0.2% | 20% | 19782 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 14965 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 14952 |
| buyer_payment_method_preference | P10R | 0.4% | 15% | 14585 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11563 |
| vendor_registered_address | P08 | 15.0% | 70% | 11490 |
| ap_system_hint | P06T | 0.7% | 20% | 11150 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8550 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 8514 |
| buyer_payment_method_preference | P06T | 0.5% | 15% | 8426 |
| buyer_phone | P13 | 49.6% | 95% | 8355 |
| vendor_bn9 | P08 | 11.7% | 50% | 8014 |
| buyer_logo_url | P13 | 52.9% | 95% | 7745 |
| buyer_legal_name_as_published | P08 | 42.2% | 75% | 6856 |
| buyer_phone | P08 | 62.8% | 95% | 6735 |
| mta_sts | P10R | 94.0% | 100% | 5965 |
| tls_rpt | P10R | 94.0% | 100% | 5965 |
| bimi | P10R | 94.0% | 100% | 5965 |
| vendor_phone | P08 | 58.2% | 85% | 5602 |
| buyer_bn_as_published | P08 | 11.0% | 35% | 5025 |
| vendor_emails | P08 | 51.0% | 75% | 5019 |
| invoice_reference_hint | P08 | 1.3% | 25% | 4958 |
| vendor_phone | P11 | 8.2% | 75% | 4750 |
| vendor_emails | P11 | 6.3% | 70% | 4524 |
| vendor_trading_name | P08 | 28.4% | 50% | 4510 |
| mta_sts | P06T | 92.5% | 100% | 4341 |
| tls_rpt | P06T | 92.5% | 100% | 4341 |
| bimi | P06T | 92.5% | 100% | 4341 |
| buyer_phone | P11 | 14.9% | 75% | 4268 |
| contract_value | P11 | 1.2% | 60% | 4180 |
| award_or_notice_id | P11 | 1.2% | 60% | 4179 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 4172 |
| ap_system_hint | P08 | 1.0% | 20% | 3971 |
| buyer_logo_url | P11 | 25.0% | 80% | 3908 |
| buyer_legal_name_as_published | P11 | 12.8% | 65% | 3707 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 3676 |
| vendor_logo_url | P08 | 82.5% | 100% | 3650 |
| buyer_logo_url | P08 | 82.9% | 100% | 3575 |
| ap_system_hint | P13 | 0.6% | 20% | 3572 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 85.1% | 85.1% | +40.7 | 50% | ✅ met |
| P01T | 325 | 89.2% | 89.2% | +17.5 | 50% | ✅ met |
| P01_GOLD | 626 | 92.2% | 94.4% | -0.3 | 95% | 🟡 3 pts to go |
| P02 | 464 | 73.9% | 75.4% | -10.0 | 95% | ❌ 21 pts to go |
| P03 | 256 | 82.0% | 85.2% | -10.8 | 95% | ❌ 13 pts to go |
| P04 | 3315 | 33.8% | 35.4% | -34.8 | 90% | ❌ 56 pts to go |
| P05 | 419 | 38.9% | 41.8% | -2.2 | 70% | ❌ 31 pts to go |
| P06M | 6303 | 92.1% | 92.1% | +85.0 | n/a | no target |
| P06T | 57911 | 80.5% | 80.5% | +76.1 | n/a | no target |
| P06 | 281 | 33.8% | 33.8% | -14.4 | 30% | ✅ met |
| P07 | 690 | 7.7% | 7.7% | -16.1 | 30% | ❌ 22 pts to go |
| P08 | 20898 | 1.3% | 1.3% | -1.1 | 25% | ❌ 24 pts to go |
| P09 | 303 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 99903 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 2.7% | 2.7% | +0.5 | 25% | ❌ 22 pts to go |
| P11 | 7106 | 18.3% | 18.5% | -5.8 | 60% | ❌ 42 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18386 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 325 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 626 | 6.1% | 6.1% | -0.1 | 50% | ❌ 44 pts to go |
| P02 | 464 | 6.2% | 6.2% | -1.0 | 50% | ❌ 44 pts to go |
| P03 | 256 | 1.6% | 1.6% | -0.3 | 40% | ❌ 38 pts to go |
| P04 | 3315 | 0.5% | 0.5% | -0.6 | 30% | ❌ 30 pts to go |
| P05 | 419 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P06M | 6303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.7% | 0.7% | +0.2 | 50% | ❌ 49 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P11 | 7106 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 74.6% | 74.6% | +74.6 | n/a | no target |
| P01T | 325 | 69.8% | 69.8% | +64.4 | 50% | ✅ met |
| P01_GOLD | 626 | 66.9% | 66.9% | -0.7 | 85% | ❌ 18 pts to go |
| P02 | 464 | 65.1% | 65.1% | -10.4 | 90% | ❌ 25 pts to go |
| P03 | 256 | 61.3% | 61.3% | -14.2 | 85% | ❌ 24 pts to go |
| P04 | 3315 | 31.0% | 31.0% | -34.5 | 85% | ❌ 54 pts to go |
| P05 | 419 | 29.1% | 29.1% | -1.9 | 60% | ❌ 31 pts to go |
| P06M | 6303 | 91.9% | 91.9% | +91.9 | n/a | no target |
| P06T | 57911 | 80.2% | 80.2% | +80.0 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 96.0% | 96.0% | -0.6 | 100% | 🟡 4 pts to go |
| P10R | 99903 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 17.2% | 17.2% | -2.8 | 60% | ❌ 43 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 325 | 0.0% | 0.0% | -2.2 | 30% | ❌ 30 pts to go |
| P01_GOLD | 626 | 50.6% | 50.6% | -0.7 | 80% | ❌ 29 pts to go |
| P02 | 464 | 57.1% | 57.1% | -9.7 | 60% | 🟡 3 pts to go |
| P03 | 256 | 51.6% | 51.6% | -12.3 | 80% | ❌ 28 pts to go |
| P04 | 3315 | 25.7% | 25.7% | -28.8 | 50% | ❌ 24 pts to go |
| P05 | 419 | 12.2% | 12.2% | -1.1 | 40% | ❌ 28 pts to go |
| P06M | 6303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | -0.2 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 83.5% | 83.5% | -2.6 | 50% | ✅ met |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 1.1% | 1.1% | -16.4 | 40% | ❌ 39 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 325 | 0.3% | 0.3% | -3.0 | n/a | no target |
| P01_GOLD | 626 | 60.4% | 60.4% | -0.7 | 85% | ❌ 25 pts to go |
| P02 | 464 | 56.5% | 56.5% | -9.3 | 90% | ❌ 34 pts to go |
| P03 | 256 | 60.2% | 60.2% | -14.3 | 85% | ❌ 25 pts to go |
| P04 | 3315 | 26.5% | 26.5% | -29.8 | 85% | ❌ 58 pts to go |
| P05 | 419 | 20.0% | 20.0% | -1.1 | 50% | ❌ 30 pts to go |
| P06M | 6303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | -0.2 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 97.0% | 97.0% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 1.2% | 1.2% | -17.8 | 60% | ❌ 59 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 325 | 0.0% | 0.0% | -2.2 | n/a | no target |
| P01_GOLD | 626 | 12.9% | 12.9% | -0.1 | 60% | ❌ 47 pts to go |
| P02 | 464 | 6.0% | 6.0% | -1.2 | 50% | ❌ 44 pts to go |
| P03 | 256 | 8.6% | 8.6% | -2.0 | 50% | ❌ 41 pts to go |
| P04 | 3315 | 2.1% | 2.1% | -2.2 | 40% | ❌ 38 pts to go |
| P05 | 419 | 1.0% | 1.0% | -0.3 | 20% | ❌ 19 pts to go |
| P06M | 6303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 2.3% | -0.3 | 50% | ❌ 48 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 0.2% | 0.2% | -2.8 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 325 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 34.8% | 34.8% | -0.3 | 80% | ❌ 45 pts to go |
| P02 | 464 | 52.2% | 52.2% | -8.4 | 90% | ❌ 38 pts to go |
| P03 | 256 | 33.6% | 33.6% | -7.7 | 80% | ❌ 46 pts to go |
| P04 | 3315 | 24.3% | 24.3% | -27.0 | 85% | ❌ 61 pts to go |
| P05 | 419 | 5.5% | 5.5% | -0.5 | 50% | ❌ 44 pts to go |
| P06M | 6303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 75.9% | 75.9% | +0.0 | 95% | ❌ 19 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 0.9% | 0.9% | -12.2 | 50% | ❌ 49 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 325 | 0.0% | 0.0% | -1.1 | n/a | no target |
| P01_GOLD | 626 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 464 | 6.2% | 6.2% | -1.0 | 50% | ❌ 44 pts to go |
| P03 | 256 | 2.0% | 2.0% | -0.4 | 30% | ❌ 28 pts to go |
| P04 | 3315 | 0.5% | 0.5% | -0.6 | 30% | ❌ 30 pts to go |
| P05 | 419 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 6303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 325 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 256 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3315 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 419 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 6303 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 57911 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 281 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 690 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 20898 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99903 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 7106 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 20.9% | 20.9% | -79.1 | 70% | ❌ 49 pts to go |
| P01T | 325 | 34.5% | 34.5% | -45.9 | 60% | ❌ 26 pts to go |
| P01_GOLD | 626 | 73.0% | 73.0% | -4.9 | 90% | ❌ 17 pts to go |
| P02 | 464 | 55.2% | 55.2% | -12.1 | 85% | ❌ 30 pts to go |
| P03 | 256 | 69.9% | 69.9% | -12.3 | 90% | ❌ 20 pts to go |
| P04 | 3315 | 33.2% | 33.2% | -22.2 | 75% | ❌ 42 pts to go |
| P05 | 419 | 50.4% | 50.4% | -2.2 | 50% | ✅ met |
| P06M | 6303 | 2.7% | 2.7% | -71.7 | n/a | no target |
| P06T | 57911 | 16.9% | 16.9% | -43.8 | n/a | no target |
| P06 | 281 | 23.8% | 23.8% | -20.2 | 40% | ❌ 16 pts to go |
| P07 | 690 | 17.5% | 17.5% | -20.6 | 50% | ❌ 32 pts to go |
| P08 | 20898 | 11.7% | 11.7% | -28.5 | 50% | ❌ 38 pts to go |
| P09 | 303 | 57.8% | 57.8% | +3.5 | 80% | ❌ 22 pts to go |
| P10R | 99903 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 28.9% | 28.9% | -7.7 | 40% | ❌ 11 pts to go |
| P11 | 7106 | 89.0% | 89.0% | +44.3 | 60% | ✅ met |
| P12 | 8 | 62.5% | 62.5% | +9.9 | 85% | ❌ 22 pts to go |
| P13 | 18386 | 91.0% | 91.0% | -0.7 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 76.1% | 76.1% | +15.0 | n/a | no target |
| P01T | 325 | 38.5% | 38.5% | -24.5 | n/a | no target |
| P01_GOLD | 626 | 70.4% | 70.4% | -4.4 | 95% | ❌ 25 pts to go |
| P02 | 464 | 73.7% | 73.7% | -11.2 | 95% | ❌ 21 pts to go |
| P03 | 256 | 71.9% | 71.9% | -6.0 | 95% | ❌ 23 pts to go |
| P04 | 3315 | 46.6% | 46.6% | -34.1 | 95% | ❌ 48 pts to go |
| P05 | 419 | 53.7% | 53.7% | -2.5 | 70% | ❌ 16 pts to go |
| P06M | 6303 | 70.2% | 70.2% | +49.4 | n/a | no target |
| P06T | 57911 | 30.1% | 30.1% | -48.1 | n/a | no target |
| P06 | 281 | 26.0% | 26.0% | -29.4 | 80% | ❌ 54 pts to go |
| P07 | 690 | 19.1% | 19.1% | -32.9 | 70% | ❌ 51 pts to go |
| P08 | 20898 | 15.0% | 15.0% | -37.4 | 70% | ❌ 55 pts to go |
| P09 | 303 | 87.5% | 87.5% | -1.0 | 100% | ❌ 12 pts to go |
| P10R | 99903 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 32.8% | 32.8% | -9.6 | 70% | ❌ 37 pts to go |
| P11 | 7106 | 90.4% | 90.4% | +35.1 | 75% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 16.4% | 16.4% | -33.6 | n/a | no target |
| P01T | 325 | 25.5% | 25.5% | +5.9 | n/a | no target |
| P01_GOLD | 626 | 47.9% | 47.9% | -4.5 | 60% | ❌ 12 pts to go |
| P02 | 464 | 55.4% | 55.4% | -11.9 | 60% | 🟡 5 pts to go |
| P03 | 256 | 55.1% | 55.1% | -9.8 | 60% | 🟡 5 pts to go |
| P04 | 3315 | 37.3% | 37.3% | -18.2 | 55% | ❌ 18 pts to go |
| P05 | 419 | 22.4% | 22.4% | -2.9 | 50% | ❌ 28 pts to go |
| P06M | 6303 | 2.5% | 2.5% | -14.8 | n/a | no target |
| P06T | 57911 | 26.6% | 26.6% | -27.0 | n/a | no target |
| P06 | 281 | 35.6% | 35.6% | -17.4 | n/a | no target |
| P07 | 690 | 33.0% | 33.0% | -13.0 | 55% | ❌ 22 pts to go |
| P08 | 20898 | 28.4% | 28.4% | -19.1 | 50% | ❌ 22 pts to go |
| P09 | 303 | 71.0% | 71.0% | -0.4 | 70% | ✅ met |
| P10R | 99903 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 39.9% | 39.9% | -12.0 | 55% | ❌ 15 pts to go |
| P11 | 7106 | 90.1% | 90.1% | +47.1 | 50% | ✅ met |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 20.9% | 20.9% | -40.2 | n/a | no target |
| P01T | 325 | 56.3% | 56.3% | +25.9 | n/a | no target |
| P01_GOLD | 626 | 47.9% | 47.9% | -3.9 | 70% | ❌ 22 pts to go |
| P02 | 464 | 54.1% | 54.1% | -3.1 | 70% | ❌ 16 pts to go |
| P03 | 256 | 49.6% | 49.6% | -7.6 | 70% | ❌ 20 pts to go |
| P04 | 3315 | 47.9% | 47.9% | -4.1 | 65% | ❌ 17 pts to go |
| P05 | 419 | 30.8% | 30.8% | -3.8 | 60% | ❌ 29 pts to go |
| P06M | 6303 | 4.7% | 4.7% | -25.7 | n/a | no target |
| P06T | 57911 | 64.0% | 64.0% | +60.5 | n/a | no target |
| P06 | 281 | 59.1% | 59.1% | -0.5 | 40% | ✅ met |
| P07 | 690 | 58.3% | 58.3% | -9.6 | 85% | ❌ 27 pts to go |
| P08 | 20898 | 58.2% | 58.2% | -9.9 | 85% | ❌ 27 pts to go |
| P09 | 303 | 53.5% | 53.5% | -1.9 | 85% | ❌ 32 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 61.1% | 61.1% | -5.2 | 85% | ❌ 24 pts to go |
| P11 | 7106 | 8.2% | 8.2% | -46.7 | 75% | ❌ 67 pts to go |
| P12 | 8 | 25.0% | 25.0% | +9.2 | n/a | no target |
| P13 | 18386 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 23.9% | 23.9% | -70.5 | n/a | no target |
| P01T | 325 | 96.3% | 96.3% | +6.1 | n/a | no target |
| P01_GOLD | 626 | 89.3% | 89.3% | -0.1 | 90% | 🟡 1 pts to go |
| P02 | 464 | 89.2% | 89.2% | +1.6 | 90% | 🟡 1 pts to go |
| P03 | 256 | 91.0% | 91.0% | +1.1 | 90% | ✅ met |
| P04 | 3315 | 89.9% | 89.9% | +8.6 | 85% | ✅ met |
| P05 | 419 | 51.8% | 51.8% | +0.8 | 70% | ❌ 18 pts to go |
| P06M | 6303 | 7.1% | 7.1% | -60.8 | n/a | no target |
| P06T | 57911 | 91.8% | 91.8% | +13.9 | n/a | no target |
| P06 | 281 | 98.2% | 98.2% | +1.2 | 50% | ✅ met |
| P07 | 690 | 98.8% | 98.8% | +2.0 | 100% | 🟡 1 pts to go |
| P08 | 20898 | 99.4% | 99.4% | +3.3 | 100% | 🟡 1 pts to go |
| P09 | 303 | 80.2% | 80.2% | +0.4 | 100% | ❌ 20 pts to go |
| P10R | 99903 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 7106 | 99.6% | 99.6% | +6.6 | 100% | 🟡 0 pts to go |
| P12 | 8 | 37.5% | 37.5% | -4.6 | n/a | no target |
| P13 | 18386 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 16.4% | 16.4% | -33.6 | n/a | no target |
| P01T | 325 | 49.5% | 49.5% | +3.8 | n/a | no target |
| P01_GOLD | 626 | 45.2% | 45.2% | -0.5 | 70% | ❌ 25 pts to go |
| P02 | 464 | 49.6% | 49.6% | -1.9 | 75% | ❌ 25 pts to go |
| P03 | 256 | 44.5% | 44.5% | -6.9 | 75% | ❌ 30 pts to go |
| P04 | 3315 | 37.9% | 37.9% | -5.0 | 70% | ❌ 32 pts to go |
| P05 | 419 | 25.5% | 25.5% | +1.0 | 55% | ❌ 30 pts to go |
| P06M | 6303 | 3.4% | 3.4% | -12.7 | n/a | no target |
| P06T | 57911 | 39.8% | 39.8% | +36.9 | n/a | no target |
| P06 | 281 | 43.4% | 43.4% | +2.4 | n/a | no target |
| P07 | 690 | 46.5% | 46.5% | +9.6 | 70% | ❌ 24 pts to go |
| P08 | 20898 | 51.0% | 51.0% | +2.3 | 75% | ❌ 24 pts to go |
| P09 | 303 | 49.8% | 49.8% | -2.2 | 85% | ❌ 35 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 43.6% | 43.6% | -7.7 | 80% | ❌ 36 pts to go |
| P11 | 7106 | 6.3% | 6.3% | -34.2 | 70% | ❌ 64 pts to go |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 19.4% | 19.4% | -75.0 | n/a | no target |
| P01T | 325 | 90.2% | 90.2% | +1.1 | n/a | no target |
| P01_GOLD | 626 | 77.5% | 77.5% | -2.3 | 90% | ❌ 12 pts to go |
| P02 | 464 | 77.6% | 77.6% | +0.4 | 90% | ❌ 12 pts to go |
| P03 | 256 | 83.2% | 83.2% | +1.5 | 90% | 🟡 7 pts to go |
| P04 | 3315 | 76.7% | 76.7% | +5.8 | 85% | 🟡 8 pts to go |
| P05 | 419 | 48.2% | 48.2% | -0.2 | 75% | ❌ 27 pts to go |
| P06M | 6303 | 5.3% | 5.3% | -62.6 | n/a | no target |
| P06T | 57911 | 83.1% | 83.1% | +6.0 | n/a | no target |
| P06 | 281 | 81.9% | 81.9% | -6.7 | n/a | no target |
| P07 | 690 | 84.1% | 84.1% | -6.4 | 100% | ❌ 16 pts to go |
| P08 | 20898 | 82.5% | 82.5% | -6.5 | 100% | ❌ 18 pts to go |
| P09 | 303 | 61.4% | 61.4% | -1.1 | n/a | no target |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 84.4% | 84.4% | -4.6 | 100% | ❌ 16 pts to go |
| P11 | 7106 | 84.7% | 84.7% | +10.2 | n/a | no target |
| P12 | 8 | 37.5% | 37.5% | +0.7 | n/a | no target |
| P13 | 18386 | 82.4% | 82.4% | -0.3 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 56.7% | 56.7% | +56.7 | n/a | no target · QC vendors: 38 rows, 100.0% filled |
| P01T | 325 | 17.8% | 17.8% | -3.9 | n/a | no target · QC vendors: 17 rows, 100.0% filled |
| P01_GOLD | 626 | 43.6% | 43.6% | -4.3 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 464 | 55.2% | 55.2% | -13.4 | 95% | ❌ 40 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 256 | 46.5% | 46.5% | -9.3 | 95% | ❌ 48 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3315 | 32.5% | 32.5% | -27.7 | 95% | ❌ 62 pts to go · QC vendors: 495 rows, 98.8% filled |
| P05 | 419 | 14.8% | 14.8% | +0.0 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 6303 | 68.2% | 68.2% | +68.2 | n/a | no target · QC vendors: 4300 rows, 100.0% filled |
| P06T | 57911 | 17.1% | 17.1% | -38.8 | n/a | no target · QC vendors: 3244 rows, 100.0% filled |
| P06 | 281 | 8.9% | 8.9% | -17.6 | n/a | no target · QC vendors: 14 rows, 100.0% filled |
| P07 | 690 | 7.2% | 7.2% | -14.2 | n/a | no target · QC vendors: 35 rows, 97.1% filled |
| P08 | 20898 | 7.1% | 7.1% | -21.8 | n/a | no target · QC vendors: 1175 rows, 99.7% filled |
| P09 | 303 | 78.2% | 78.2% | -1.9 | 95% | ❌ 17 pts to go · QC vendors: 111 rows, 100.0% filled |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 17.8% | 17.8% | -5.6 | n/a | no target · QC vendors: 310 rows, 94.5% filled |
| P11 | 7106 | 75.8% | 75.8% | +46.5 | n/a | no target · QC vendors: 108 rows, 99.1% filled |
| P12 | 8 | 62.5% | 62.5% | -11.2 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 73.1% | 73.1% | +12.0 | n/a | no target · vendors with a registry record: 49 rows, 100.0% filled |
| P01T | 325 | 38.8% | 38.8% | -24.2 | n/a | no target · vendors with a registry record: 126 rows, 100.0% filled |
| P01_GOLD | 626 | 79.4% | 79.4% | -4.1 | 100% | ❌ 21 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 464 | 77.4% | 77.4% | -11.7 | 100% | ❌ 23 pts to go · vendors with a registry record: 359 rows, 100.0% filled |
| P03 | 256 | 81.2% | 81.2% | -7.7 | 100% | ❌ 19 pts to go · vendors with a registry record: 208 rows, 100.0% filled |
| P04 | 3315 | 47.1% | 47.1% | -34.3 | 100% | ❌ 53 pts to go · vendors with a registry record: 1561 rows, 100.0% filled |
| P05 | 419 | 58.5% | 58.5% | -3.2 | n/a | no target · vendors with a registry record: 245 rows, 100.0% filled |
| P06M | 6303 | 69.6% | 69.6% | +48.8 | n/a | no target · vendors with a registry record: 4387 rows, 100.0% filled |
| P06T | 57911 | 30.2% | 30.2% | -48.0 | n/a | no target · vendors with a registry record: 17464 rows, 100.0% filled |
| P06 | 281 | 26.7% | 26.7% | -31.1 | n/a | no target · vendors with a registry record: 75 rows, 100.0% filled |
| P07 | 690 | 19.6% | 19.6% | -34.8 | n/a | no target · vendors with a registry record: 135 rows, 100.0% filled |
| P08 | 20898 | 15.2% | 15.2% | -39.1 | n/a | no target · vendors with a registry record: 3185 rows, 100.0% filled |
| P09 | 303 | 91.1% | 91.1% | -0.5 | n/a | no target · vendors with a registry record: 276 rows, 100.0% filled |
| P10R | 99903 | 100.0% | 100.0% |  | n/a | no target · vendors with a registry record: 99903 rows, 100.0% filled |
| P10 | 2665 | 33.5% | 33.5% | -10.2 | n/a | no target · vendors with a registry record: 892 rows, 100.0% filled |
| P11 | 7106 | 90.6% | 90.6% | +32.4 | n/a | no target · vendors with a registry record: 6440 rows, 100.0% filled |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 8 rows, 100.0% filled |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 89.6% | 89.6% | -4.8 | 90% | 🟡 0 pts to go |
| P01T | 325 | 57.5% | 57.5% | -37.1 | 90% | ❌ 32 pts to go |
| P01_GOLD | 626 | 83.7% | 83.7% | -0.9 | 95% | ❌ 11 pts to go |
| P02 | 464 | 85.3% | 85.3% | -5.3 | 95% | 🟡 10 pts to go |
| P03 | 256 | 78.9% | 78.9% | -4.3 | 85% | 🟡 6 pts to go |
| P04 | 3315 | 57.3% | 57.3% | -21.5 | 90% | ❌ 33 pts to go |
| P05 | 419 | 68.5% | 68.5% | -7.3 | 75% | 🟡 6 pts to go |
| P06M | 6303 | 89.5% | 89.5% | +0.8 | n/a | no target |
| P06T | 57911 | 29.7% | 29.7% | -34.7 | n/a | no target |
| P06 | 281 | 59.4% | 59.4% | +2.8 | 80% | ❌ 21 pts to go |
| P07 | 690 | 48.8% | 49.0% | -4.8 | 80% | ❌ 31 pts to go |
| P08 | 20898 | 42.2% | 42.2% | +5.4 | 75% | ❌ 33 pts to go |
| P09 | 303 | 77.2% | 77.2% | -3.6 | 95% | ❌ 18 pts to go |
| P10R | 99903 | 25.8% | 25.8% |  | n/a | no target |
| P10 | 2665 | 39.4% | 39.4% | +7.4 | 70% | ❌ 31 pts to go |
| P11 | 7106 | 12.8% | 12.8% | -12.1 | 65% | ❌ 52 pts to go |
| P12 | 8 | 75.0% | 75.0% | +1.3 | 80% | 🟡 5 pts to go |
| P13 | 18386 | 41.5% | 41.5% | -11.0 | 60% | ❌ 18 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 20.9% | 20.9% | -18.0 | 50% | ❌ 29 pts to go |
| P01T | 325 | 13.5% | 13.5% | -7.2 | n/a | no target |
| P01_GOLD | 626 | 20.6% | 20.6% | +0.2 | 40% | ❌ 19 pts to go |
| P02 | 464 | 19.0% | 19.0% | -2.8 | 40% | ❌ 21 pts to go |
| P03 | 256 | 22.3% | 22.3% | -4.6 | 40% | ❌ 18 pts to go |
| P04 | 3315 | 16.4% | 16.4% | -11.2 | 40% | ❌ 24 pts to go |
| P05 | 419 | 20.0% | 20.0% | -2.9 | 25% | 🟡 5 pts to go |
| P06M | 6303 | 7.7% | 7.7% | -17.9 | n/a | no target |
| P06T | 57911 | 7.7% | 7.7% | -23.2 | n/a | no target |
| P06 | 281 | 12.8% | 12.8% | +2.0 | 35% | ❌ 22 pts to go |
| P07 | 690 | 10.6% | 10.6% | +0.3 | 35% | ❌ 24 pts to go |
| P08 | 20898 | 11.0% | 11.0% | -0.1 | 35% | ❌ 24 pts to go |
| P09 | 303 | 16.2% | 16.2% | -0.9 | n/a | no target |
| P10R | 99903 | 7.4% | 7.4% |  | n/a | no target |
| P10 | 2665 | 6.9% | 6.9% | -2.7 | 30% | ❌ 23 pts to go |
| P11 | 7106 | 1.7% | 1.7% | -6.7 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 18386 | 22.2% | 22.2% | -3.7 | 30% | 🟡 8 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 325 | 92.0% | 92.0% | -1.5 | 100% | 🟡 8 pts to go |
| P01_GOLD | 626 | 89.5% | 89.5% | +1.8 | 100% | ❌ 10 pts to go |
| P02 | 464 | 95.3% | 95.3% | -1.5 | 100% | 🟡 5 pts to go |
| P03 | 256 | 89.5% | 89.5% | -2.3 | 100% | ❌ 10 pts to go |
| P04 | 3315 | 77.3% | 77.3% | -13.7 | 100% | ❌ 23 pts to go |
| P05 | 419 | 87.1% | 87.1% | +2.2 | 100% | ❌ 13 pts to go |
| P06M | 6303 | 98.2% | 98.2% | +26.2 | n/a | no target |
| P06T | 57911 | 77.5% | 77.5% | -2.7 | n/a | no target |
| P06 | 281 | 80.1% | 80.1% | +11.4 | 95% | ❌ 15 pts to go |
| P07 | 690 | 83.6% | 83.6% | +13.0 | 95% | ❌ 11 pts to go |
| P08 | 20898 | 80.3% | 80.3% | +14.1 | 95% | ❌ 15 pts to go |
| P09 | 303 | 95.7% | 95.7% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 99903 | 59.1% | 59.1% |  | n/a | no target |
| P10 | 2665 | 65.6% | 65.7% | +0.4 | 95% | ❌ 29 pts to go |
| P11 | 7106 | 83.3% | 83.3% | +48.9 | 80% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18386 | 75.7% | 75.7% | -0.4 | 95% | ❌ 19 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 89.6% | 89.6% | +0.7 | n/a | no target |
| P01T | 325 | 64.9% | 64.9% | -15.5 | n/a | no target |
| P01_GOLD | 626 | 69.5% | 69.5% | -0.7 | 90% | ❌ 20 pts to go |
| P02 | 464 | 75.9% | 75.9% | -3.8 | 95% | ❌ 19 pts to go |
| P03 | 256 | 73.8% | 73.8% | +0.2 | 95% | ❌ 21 pts to go |
| P04 | 3315 | 68.0% | 68.0% | -16.9 | 95% | ❌ 27 pts to go |
| P05 | 419 | 70.9% | 70.9% | -4.1 | 90% | ❌ 19 pts to go |
| P06M | 6303 | 93.5% | 93.5% | +9.6 | n/a | no target |
| P06T | 57911 | 49.0% | 49.0% | -28.3 | n/a | no target |
| P06 | 281 | 65.1% | 65.1% | +0.6 | 95% | ❌ 30 pts to go |
| P07 | 690 | 59.6% | 59.6% | -6.7 | 90% | ❌ 30 pts to go |
| P08 | 20898 | 62.8% | 62.8% | -11.9 | 95% | ❌ 32 pts to go |
| P09 | 303 | 86.1% | 86.1% | -2.9 | 100% | ❌ 14 pts to go |
| P10R | 99903 | 46.2% | 46.2% |  | n/a | no target |
| P10 | 2665 | 57.2% | 57.2% | -14.3 | 95% | ❌ 38 pts to go |
| P11 | 7106 | 14.9% | 14.9% | -14.0 | 75% | ❌ 60 pts to go |
| P12 | 8 | 75.0% | 75.0% | -14.5 | n/a | no target |
| P13 | 18386 | 49.6% | 49.6% | -29.7 | 95% | ❌ 45 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 74.6% | 74.6% | -3.2 | n/a | no target |
| P01T | 325 | 75.7% | 75.7% | -15.6 | 95% | ❌ 19 pts to go |
| P01_GOLD | 626 | 80.7% | 80.7% | -1.5 | 90% | 🟡 9 pts to go |
| P02 | 464 | 85.8% | 85.8% | -2.6 | 95% | 🟡 9 pts to go |
| P03 | 256 | 84.0% | 84.0% | -0.6 | 95% | ❌ 11 pts to go |
| P04 | 3315 | 84.7% | 84.7% | +0.5 | 90% | 🟡 5 pts to go |
| P05 | 419 | 88.8% | 88.8% | -0.8 | 95% | 🟡 6 pts to go |
| P06M | 6303 | 67.8% | 67.8% | -17.3 | n/a | no target |
| P06T | 57911 | 62.9% | 62.9% | -31.2 | n/a | no target |
| P06 | 281 | 85.4% | 85.4% | -5.0 | 100% | ❌ 15 pts to go |
| P07 | 690 | 81.7% | 81.7% | -6.4 | 100% | ❌ 18 pts to go |
| P08 | 20898 | 82.9% | 82.9% | -7.8 | 100% | ❌ 17 pts to go |
| P09 | 303 | 68.6% | 68.6% | -5.4 | n/a | no target |
| P10R | 99903 | 61.1% | 61.1% |  | n/a | no target |
| P10 | 2665 | 87.2% | 87.2% | -2.9 | 100% | ❌ 13 pts to go |
| P11 | 7106 | 25.0% | 25.0% | -11.5 | 80% | ❌ 55 pts to go |
| P12 | 8 | 75.0% | 75.0% | -9.2 | n/a | no target |
| P13 | 18386 | 52.9% | 52.9% | -31.3 | 95% | ❌ 42 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 6.0% | 6.0% | -10.7 | n/a | no target |
| P01T | 325 | 8.6% | 8.6% | -15.3 | n/a | no target |
| P01_GOLD | 626 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 464 | 24.6% | 24.6% | -3.1 | 40% | ❌ 15 pts to go |
| P03 | 256 | 9.0% | 9.0% | -1.6 | 20% | ❌ 11 pts to go |
| P04 | 3315 | 3.7% | 3.7% | -3.7 | 20% | ❌ 16 pts to go |
| P05 | 419 | 3.3% | 3.3% | -0.6 | 15% | ❌ 12 pts to go |
| P06M | 6303 | 0.3% | 0.3% | -4.5 | n/a | no target |
| P06T | 57911 | 0.4% | 0.4% | -2.8 | n/a | no target |
| P06 | 281 | 5.7% | 5.7% | +0.3 | n/a | no target |
| P07 | 690 | 7.2% | 7.2% | +0.9 | n/a | no target |
| P08 | 20898 | 0.3% | 0.3% | -0.7 | n/a | no target |
| P09 | 303 | 7.6% | 7.6% | -0.3 | n/a | no target |
| P10R | 99903 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2665 | 1.0% | 1.0% | -0.3 | n/a | no target |
| P11 | 7106 | 0.2% | 0.2% | -2.3 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 18386 | 0.4% | 0.4% | -0.2 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 26.9% | 26.9% | -12.0 | n/a | no target |
| P01T | 325 | 24.6% | 24.6% | -10.2 | 70% | ❌ 45 pts to go |
| P01_GOLD | 626 | 43.3% | 43.3% | +0.0 | 80% | ❌ 37 pts to go |
| P02 | 464 | 56.9% | 56.9% | -7.2 | 90% | ❌ 33 pts to go |
| P03 | 256 | 19.1% | 19.1% | -4.0 | 60% | ❌ 41 pts to go |
| P04 | 3315 | 24.3% | 24.3% | -26.2 | 85% | ❌ 61 pts to go |
| P05 | 419 | 12.2% | 12.2% | -0.8 | 50% | ❌ 38 pts to go |
| P06M | 6303 | 0.6% | 0.6% | -5.9 | n/a | no target |
| P06T | 57911 | 0.6% | 0.6% | -2.1 | n/a | no target |
| P06 | 281 | 17.1% | 17.1% | -1.0 | n/a | no target |
| P07 | 690 | 13.2% | 13.2% | -5.8 | n/a | no target |
| P08 | 20898 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 303 | 77.6% | 77.6% | -3.0 | 95% | ❌ 17 pts to go |
| P10R | 99903 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2665 | 1.8% | 1.8% | -1.3 | n/a | no target |
| P11 | 7106 | 4.8% | 4.8% | -24.5 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 18386 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 4.5% | 4.5% | +4.5 | n/a | no target |
| P01T | 325 | 12.3% | 12.3% | -4.0 | n/a | no target |
| P01_GOLD | 626 | 33.9% | 33.9% | -0.1 | 70% | ❌ 36 pts to go |
| P02 | 464 | 39.0% | 39.0% | -5.3 | 75% | ❌ 36 pts to go |
| P03 | 256 | 19.1% | 19.1% | -4.0 | 55% | ❌ 36 pts to go |
| P04 | 3315 | 24.2% | 24.2% | -26.3 | 75% | ❌ 51 pts to go |
| P05 | 419 | 11.0% | 11.0% | -0.7 | 50% | ❌ 39 pts to go |
| P06M | 6303 | 0.1% | 0.1% | -1.7 | n/a | no target |
| P06T | 57911 | 0.4% | 0.4% | -1.1 | n/a | no target |
| P06 | 281 | 8.9% | 8.9% | -1.3 | n/a | no target |
| P07 | 690 | 6.2% | 6.2% | -4.1 | n/a | no target |
| P08 | 20898 | 0.2% | 0.2% | -0.3 | n/a | no target |
| P09 | 303 | 75.2% | 75.2% | -2.5 | 95% | ❌ 20 pts to go |
| P10R | 99903 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2665 | 1.1% | 1.1% | -0.7 | n/a | no target |
| P11 | 7106 | 4.7% | 4.7% | -24.2 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 18386 | 0.5% | 0.5% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 6.0% | 6.0% | -10.7 | n/a | no target |
| P01T | 325 | 9.5% | 9.5% | -10.1 | n/a | no target |
| P01_GOLD | 626 | 58.0% | 58.1% | +0.1 | 80% | ❌ 22 pts to go |
| P02 | 464 | 45.9% | 46.1% | -6.3 | 75% | ❌ 29 pts to go |
| P03 | 256 | 37.9% | 37.9% | -7.3 | 70% | ❌ 32 pts to go |
| P04 | 3315 | 23.8% | 24.3% | -24.9 | 70% | ❌ 46 pts to go |
| P05 | 419 | 14.6% | 14.6% | -1.8 | 50% | ❌ 35 pts to go |
| P06M | 6303 | 0.6% | 0.6% | -3.6 | n/a | no target |
| P06T | 57911 | 0.3% | 0.3% | -1.3 | n/a | no target |
| P06 | 281 | 14.2% | 14.2% | -9.9 | n/a | no target |
| P07 | 690 | 2.5% | 2.5% | -2.7 | n/a | no target |
| P08 | 20898 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P09 | 303 | 45.9% | 46.2% | +1.8 | 80% | ❌ 34 pts to go |
| P10R | 99903 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2665 | 1.2% | 1.3% | -0.3 | n/a | no target |
| P11 | 7106 | 1.5% | 1.5% | -15.2 | n/a | no target |
| P12 | 8 | 37.5% | 37.5% | +5.9 | n/a | no target |
| P13 | 18386 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 13.4% | 13.4% | -25.5 | n/a | no target |
| P01T | 325 | 22.5% | 22.5% | -34.0 | 60% | ❌ 38 pts to go |
| P01_GOLD | 626 | 63.6% | 63.6% | +0.1 | 70% | 🟡 6 pts to go |
| P02 | 464 | 39.0% | 39.0% | -4.8 | 50% | ❌ 11 pts to go |
| P03 | 256 | 50.0% | 50.0% | -5.3 | 55% | 🟡 5 pts to go |
| P04 | 3315 | 13.7% | 13.7% | -9.2 | 40% | ❌ 26 pts to go |
| P05 | 419 | 17.7% | 17.7% | +0.3 | 40% | ❌ 22 pts to go |
| P06M | 6303 | 1.0% | 1.0% | -15.7 | n/a | no target |
| P06T | 57911 | 2.5% | 2.5% | -10.0 | n/a | no target |
| P06 | 281 | 20.3% | 20.3% | -10.4 | n/a | no target |
| P07 | 690 | 7.2% | 7.2% | -9.1 | n/a | no target |
| P08 | 20898 | 3.1% | 3.1% | -1.6 | n/a | no target |
| P09 | 303 | 5.9% | 5.9% | +0.1 | n/a | no target |
| P10R | 99903 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2665 | 4.6% | 4.6% | +0.7 | n/a | no target |
| P11 | 7106 | 4.9% | 4.9% | -2.7 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 18386 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 17.9% | 17.9% | -26.5 | n/a | no target |
| P01T | 325 | 25.8% | 25.8% | -43.8 | 65% | ❌ 39 pts to go |
| P01_GOLD | 626 | 69.0% | 69.0% | -0.2 | 70% | 🟡 1 pts to go |
| P02 | 464 | 23.9% | 23.9% | -2.3 | 50% | ❌ 26 pts to go |
| P03 | 256 | 52.3% | 52.3% | -3.9 | 60% | 🟡 8 pts to go |
| P04 | 3315 | 6.0% | 6.0% | -3.9 | 40% | ❌ 34 pts to go |
| P05 | 419 | 20.0% | 20.0% | -1.4 | 45% | ❌ 25 pts to go |
| P06M | 6303 | 0.5% | 0.5% | -6.6 | n/a | no target |
| P06T | 57911 | 0.6% | 0.6% | -3.7 | n/a | no target |
| P06 | 281 | 33.8% | 33.8% | -14.4 | n/a | no target |
| P07 | 690 | 7.7% | 7.7% | -16.1 | n/a | no target |
| P08 | 20898 | 1.3% | 1.3% | -1.1 | n/a | no target |
| P09 | 303 | 9.9% | 9.9% | +1.2 | n/a | no target |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 2.7% | 2.7% | +0.6 | n/a | no target |
| P11 | 7106 | 1.3% | 1.3% | -5.5 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 18386 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 4.5% | 4.5% | -6.6 | n/a | no target |
| P01T | 325 | 14.8% | 14.8% | -29.8 | n/a | no target |
| P01_GOLD | 626 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 464 | 37.5% | 37.5% | -5.1 | n/a | no target |
| P03 | 256 | 53.1% | 53.1% | -5.6 | 60% | 🟡 7 pts to go |
| P04 | 3315 | 13.3% | 13.3% | -13.1 | n/a | no target |
| P05 | 419 | 15.5% | 15.5% | -1.2 | n/a | no target |
| P06M | 6303 | 0.3% | 0.3% | -3.9 | n/a | no target |
| P06T | 57911 | 0.5% | 0.5% | -3.5 | n/a | no target |
| P06 | 281 | 23.1% | 23.1% | -12.4 | n/a | no target |
| P07 | 690 | 8.0% | 8.0% | -10.7 | n/a | no target |
| P08 | 20898 | 0.6% | 0.6% | -0.9 | n/a | no target |
| P09 | 303 | 18.2% | 18.2% | -0.7 | n/a | no target |
| P10R | 99903 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2665 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 7106 | 1.1% | 1.1% | -6.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -21.1 | n/a | no target |
| P13 | 18386 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 13.4% | 13.4% | -14.4 | 15% | 🟡 2 pts to go |
| P01T | 325 | 11.4% | 11.4% | -17.9 | 15% | 🟡 4 pts to go |
| P01_GOLD | 626 | 35.3% | 35.3% | +0.2 | 40% | 🟡 5 pts to go |
| P02 | 464 | 12.5% | 12.7% | -1.4 | 25% | ❌ 12 pts to go |
| P03 | 256 | 18.0% | 18.0% | -3.6 | 25% | 🟡 7 pts to go |
| P04 | 3315 | 3.0% | 3.0% | -2.2 | 15% | ❌ 12 pts to go |
| P05 | 419 | 6.9% | 6.9% | -1.2 | 15% | 🟡 8 pts to go |
| P06M | 6303 | 0.6% | 0.6% | -5.4 | 15% | ❌ 14 pts to go |
| P06T | 57911 | 0.5% | 0.5% | -1.0 | 15% | ❌ 14 pts to go |
| P06 | 281 | 9.6% | 9.6% | -0.6 | 15% | 🟡 5 pts to go |
| P07 | 690 | 3.6% | 3.6% | -3.1 | 15% | ❌ 11 pts to go |
| P08 | 20898 | 0.5% | 0.5% | -0.4 | 15% | ❌ 14 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 99903 | 0.4% | 0.4% |  | 15% | ❌ 15 pts to go |
| P10 | 2665 | 1.1% | 1.1% | -0.3 | 15% | ❌ 14 pts to go |
| P11 | 7106 | 0.3% | 0.3% | -1.0 | 15% | ❌ 15 pts to go |
| P12 | 8 | 12.5% | 12.5% | +12.5 | 15% | 🟡 2 pts to go |
| P13 | 18386 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 6.0% | 6.0% | -5.1 | 15% | 🟡 9 pts to go |
| P01T | 325 | 12.3% | 12.3% | -20.3 | 25% | ❌ 13 pts to go |
| P01_GOLD | 626 | 29.2% | 29.2% | +0.0 | 25% | ✅ met |
| P02 | 464 | 25.4% | 25.4% | -2.6 | 15% | ✅ met |
| P03 | 256 | 21.5% | 21.5% | -4.5 | 15% | ✅ met |
| P04 | 3315 | 4.3% | 4.3% | -3.9 | 15% | ❌ 11 pts to go |
| P05 | 419 | 11.0% | 11.0% | -1.0 | 15% | 🟡 4 pts to go |
| P06M | 6303 | 0.3% | 0.3% | -2.1 | 15% | ❌ 15 pts to go |
| P06T | 57911 | 0.3% | 0.3% | -2.4 | 15% | ❌ 15 pts to go |
| P06 | 281 | 7.8% | 7.8% | -4.2 | 15% | 🟡 7 pts to go |
| P07 | 690 | 3.2% | 3.2% | -4.3 | 15% | ❌ 12 pts to go |
| P08 | 20898 | 0.5% | 0.5% | -0.5 | 15% | ❌ 14 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P10 | 2665 | 1.6% | 1.6% | +0.2 | 15% | ❌ 13 pts to go |
| P11 | 7106 | 0.7% | 0.7% | -4.4 | 15% | ❌ 14 pts to go |
| P12 | 8 | 25.0% | 25.0% | -1.3 | 15% | ✅ met |
| P13 | 18386 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 0.0% | -5.6 | 20% | ❌ 20 pts to go |
| P01T | 325 | 4.0% | 4.0% | -5.8 | 20% | ❌ 16 pts to go |
| P01_GOLD | 626 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 464 | 1.3% | 1.3% | -0.2 | 20% | ❌ 19 pts to go |
| P03 | 256 | 1.6% | 1.6% | -0.3 | 20% | ❌ 18 pts to go |
| P04 | 3315 | 0.6% | 0.6% | -0.4 | 20% | ❌ 19 pts to go |
| P05 | 419 | 1.2% | 1.2% | +0.2 | 20% | ❌ 19 pts to go |
| P06M | 6303 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 57911 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P06 | 281 | 1.4% | 1.4% | -2.2 | 20% | ❌ 19 pts to go |
| P07 | 690 | 0.6% | 0.6% | -0.2 | 20% | ❌ 19 pts to go |
| P08 | 20898 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P09 | 303 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2665 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 7106 | 0.1% | 0.1% | -0.5 | 20% | ❌ 20 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 1.5% | 1.5% | -4.1 | 15% | ❌ 14 pts to go |
| P01T | 325 | 2.5% | 2.5% | -5.1 | 15% | ❌ 12 pts to go |
| P01_GOLD | 626 | 10.5% | 10.5% | -0.1 | 15% | 🟡 4 pts to go |
| P02 | 464 | 12.1% | 12.1% | -1.3 | 15% | 🟡 3 pts to go |
| P03 | 256 | 20.7% | 20.7% | -3.3 | 15% | ✅ met |
| P04 | 3315 | 2.5% | 2.5% | -2.1 | 15% | ❌ 12 pts to go |
| P05 | 419 | 3.1% | 3.1% | +0.2 | 15% | ❌ 12 pts to go |
| P06M | 6303 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 57911 | 0.2% | 0.2% | -1.2 | 15% | ❌ 15 pts to go |
| P06 | 281 | 5.7% | 5.7% | +0.3 | 15% | 🟡 9 pts to go |
| P07 | 690 | 1.9% | 1.9% | -1.7 | 15% | ❌ 13 pts to go |
| P08 | 20898 | 0.4% | 0.4% | -0.3 | 15% | ❌ 15 pts to go |
| P09 | 303 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P10 | 2665 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P11 | 7106 | 0.4% | 0.4% | -1.7 | 15% | ❌ 15 pts to go |
| P12 | 8 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 18386 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 6.0% | 6.0% | -5.1 | 20% | ❌ 14 pts to go |
| P01T | 325 | 15.4% | 15.4% | -25.9 | 40% | ❌ 25 pts to go |
| P01_GOLD | 626 | 45.8% | 45.8% | +0.0 | 40% | ✅ met |
| P02 | 464 | 42.9% | 42.9% | -5.6 | 20% | ✅ met |
| P03 | 256 | 48.8% | 48.8% | -7.0 | 35% | ✅ met |
| P04 | 3315 | 15.8% | 15.8% | -14.5 | 20% | 🟡 4 pts to go |
| P05 | 419 | 15.0% | 15.0% | -1.7 | 20% | 🟡 5 pts to go |
| P06M | 6303 | 0.6% | 0.6% | -3.6 | 20% | ❌ 19 pts to go |
| P06T | 57911 | 0.7% | 0.7% | -3.8 | 20% | ❌ 19 pts to go |
| P06 | 281 | 23.5% | 23.5% | -12.0 | 20% | ✅ met |
| P07 | 690 | 7.8% | 7.8% | -6.9 | 20% | ❌ 12 pts to go |
| P08 | 20898 | 1.0% | 1.0% | -1.3 | 20% | ❌ 19 pts to go |
| P09 | 303 | 18.2% | 18.2% | -3.8 | 20% | 🟡 2 pts to go |
| P10R | 99903 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P10 | 2665 | 3.5% | 3.5% | +0.9 | 20% | ❌ 16 pts to go |
| P11 | 7106 | 1.2% | 1.2% | -6.8 | 20% | ❌ 19 pts to go |
| P12 | 8 | 0.0% | 0.0% | -15.8 | 20% | ❌ 20 pts to go |
| P13 | 18386 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 52.2% | 52.2% | +52.2 | n/a | no target |
| P01T | 325 | 0.3% | 0.3% | -0.8 | n/a | no target |
| P01_GOLD | 626 | 69.5% | 69.5% | -0.2 | 95% | ❌ 26 pts to go |
| P02 | 464 | 63.1% | 63.1% | -10.2 | 95% | ❌ 32 pts to go |
| P03 | 256 | 54.7% | 54.7% | -12.6 | 90% | ❌ 35 pts to go |
| P04 | 3315 | 27.9% | 27.9% | -30.5 | 85% | ❌ 57 pts to go |
| P05 | 419 | 36.5% | 36.5% | +1.6 | 75% | ❌ 38 pts to go |
| P06M | 6303 | 63.7% | 63.7% | +63.7 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 89.4% | 89.4% | -1.4 | 100% | ❌ 11 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 1.2% | 1.2% | -17.6 | 60% | ❌ 59 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 52.2% | 52.2% | +52.2 | n/a | no target |
| P01T | 325 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 72.8% | 72.8% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 464 | 66.6% | 66.6% | -10.6 | 100% | ❌ 33 pts to go |
| P03 | 256 | 60.5% | 60.5% | -14.0 | n/a | no target |
| P04 | 3315 | 28.6% | 28.6% | -31.4 | 95% | ❌ 66 pts to go |
| P05 | 419 | 33.2% | 33.2% | +2.0 | 80% | ❌ 47 pts to go |
| P06M | 6303 | 63.7% | 63.7% | +63.7 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 92.7% | 92.7% | -0.7 | 100% | 🟡 7 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 1.3% | 1.3% | -18.7 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 71.6% | 71.6% | +71.6 | n/a | no target |
| P01T | 325 | 0.3% | 0.3% | -0.8 | n/a | no target |
| P01_GOLD | 626 | 51.6% | 51.6% | -0.3 | 85% | ❌ 33 pts to go |
| P02 | 464 | 57.8% | 57.8% | -9.0 | 90% | ❌ 32 pts to go |
| P03 | 256 | 44.1% | 44.1% | -10.7 | 85% | ❌ 41 pts to go |
| P04 | 3315 | 31.3% | 31.3% | -32.8 | 90% | ❌ 59 pts to go |
| P05 | 419 | 32.9% | 32.9% | -2.3 | 75% | ❌ 42 pts to go |
| P06M | 6303 | 90.5% | 90.5% | +90.5 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 85.1% | 85.1% | -0.5 | 95% | 🟡 10 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 1.1% | 1.1% | -16.2 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 71.6% | 71.6% | +71.6 | n/a | no target |
| P01T | 325 | 0.3% | 0.3% | -0.8 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | -0.3 | 85% | ❌ 33 pts to go |
| P02 | 464 | 52.8% | 52.8% | -8.3 | 90% | ❌ 37 pts to go |
| P03 | 256 | 45.3% | 45.3% | -10.9 | 85% | ❌ 40 pts to go |
| P04 | 3315 | 26.7% | 26.7% | -27.6 | 90% | ❌ 63 pts to go |
| P05 | 419 | 43.0% | 43.0% | +1.3 | 75% | ❌ 32 pts to go |
| P06M | 6303 | 83.7% | 83.7% | +83.7 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 0.9% | 0.9% | -13.2 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 79.1% | 79.1% | +79.1 | n/a | no target |
| P01T | 325 | 92.0% | 92.0% | +10.5 | n/a | no target |
| P01_GOLD | 626 | 85.5% | 85.5% | -0.2 | 100% | ❌ 14 pts to go |
| P02 | 464 | 75.6% | 75.6% | -6.1 | 100% | ❌ 24 pts to go |
| P03 | 256 | 92.2% | 92.2% | -0.1 | n/a | no target |
| P04 | 3315 | 52.4% | 52.4% | -20.2 | 95% | ❌ 43 pts to go |
| P05 | 419 | 77.8% | 77.8% | +2.3 | 95% | ❌ 17 pts to go |
| P06M | 6303 | 97.5% | 97.5% | +96.9 | n/a | no target |
| P06T | 57911 | 84.0% | 84.0% | +0.6 | n/a | no target |
| P06 | 281 | 27.8% | 27.8% | -48.1 | n/a | no target |
| P07 | 690 | 20.4% | 20.4% | -56.6 | n/a | no target |
| P08 | 20898 | 12.4% | 12.4% | -72.5 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 99903 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 71.7% | 71.7% | -26.7 | n/a | no target |
| P11 | 7106 | 21.7% | 21.7% | -68.2 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 79.1% | 79.1% | +79.1 | n/a | no target |
| P01T | 325 | 92.0% | 92.0% | +10.5 | n/a | no target |
| P01_GOLD | 626 | 88.7% | 88.7% | -0.2 | 100% | ❌ 11 pts to go |
| P02 | 464 | 76.7% | 76.9% | -6.2 | 100% | ❌ 23 pts to go |
| P03 | 256 | 93.0% | 93.0% | -0.8 | n/a | no target |
| P04 | 3315 | 56.0% | 56.0% | -23.0 | 95% | ❌ 39 pts to go |
| P05 | 419 | 90.5% | 90.5% | +0.4 | 70% | ✅ met |
| P06M | 6303 | 97.5% | 97.5% | +96.9 | n/a | no target |
| P06T | 57911 | 84.0% | 84.0% | +0.6 | n/a | no target |
| P06 | 281 | 27.8% | 27.8% | -48.1 | n/a | no target |
| P07 | 690 | 20.4% | 20.4% | -56.6 | n/a | no target |
| P08 | 20898 | 12.4% | 12.4% | -72.5 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 99903 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 71.7% | 71.7% | -26.7 | n/a | no target |
| P11 | 7106 | 21.7% | 21.7% | -68.6 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 325 | 0.0% | 0.0% | -1.1 | n/a | no target |
| P01_GOLD | 626 | 16.8% | 16.8% | -0.5 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 464 | 11.2% | 11.2% | -1.9 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 256 | 13.3% | 13.3% | -3.0 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3315 | 1.7% | 1.7% | -2.0 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 419 | 3.1% | 3.1% | -0.3 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 6303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 57911 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 281 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 3.0% | 3.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 290 rows, 3.1% filled |
| P10R | 99903 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 7106 | 0.2% | 0.2% | -2.5 | n/a | no target · rows from a source that publishes bids: 87 rows, 12.6% filled |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 8 rows, 0.0% filled |
| P13 | 18386 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 325 | 0.3% | 98.5% | +0.3 | n/a | no target |
| P01_GOLD | 626 | 53.2% | 82.4% | +0.0 | 90% | ❌ 37 pts to go |
| P02 | 464 | 52.6% | 87.5% | -8.5 | 90% | ❌ 37 pts to go |
| P03 | 256 | 45.7% | 80.1% | -10.5 | 90% | ❌ 44 pts to go |
| P04 | 3315 | 21.5% | 93.2% | -23.8 | 90% | ❌ 68 pts to go |
| P05 | 419 | 0.0% | 82.6% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 6303 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 57911 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 281 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 4.0% | +0.2 | 90% | ❌ 88 pts to go |
| P10R | 99903 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 7106 | 0.8% | 99.4% | -11.9 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 325 | 0.6% | 98.8% | +0.6 | n/a | no target |
| P01_GOLD | 626 | 25.9% | 55.1% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 464 | 51.7% | 86.6% | -8.2 | n/a | no target |
| P03 | 256 | 25.0% | 59.4% | -5.8 | n/a | no target |
| P04 | 3315 | 23.6% | 95.2% | -26.1 | n/a | no target |
| P05 | 419 | 0.5% | 83.1% | +0.0 | n/a | no target |
| P06M | 6303 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 57911 | 0.1% | 99.9% | +0.1 | n/a | no target |
| P06 | 281 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 41.9% | 43.6% | -2.5 | n/a | no target |
| P10R | 99903 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 7106 | 0.8% | 99.3% | -10.8 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 325 | 1.5% | 99.7% | -0.7 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 81.0% | +0.2 | 95% | ❌ 43 pts to go |
| P02 | 464 | 56.7% | 91.6% | -8.9 | n/a | no target |
| P03 | 256 | 48.0% | 82.4% | -11.1 | n/a | no target |
| P04 | 3315 | 23.8% | 95.4% | -26.5 | n/a | no target |
| P05 | 419 | 4.8% | 87.4% | -0.4 | n/a | no target |
| P06M | 6303 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 57911 | 0.1% | 100.0% | +0.1 | n/a | no target |
| P06 | 281 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 690 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 20898 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 64.0% | 65.7% | -3.5 | n/a | no target |
| P10R | 99903 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2665 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 7106 | 0.8% | 99.4% | -11.9 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18386 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 95.5% | 95.5% | -4.5 | 100% | 🟡 4 pts to go |
| P01T | 325 | 95.4% | 95.4% | -4.6 | 100% | 🟡 5 pts to go |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P03 | 256 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3315 | 97.8% | 97.8% | -2.2 | 100% | 🟡 2 pts to go |
| P05 | 419 | 99.0% | 99.0% | -1.0 | 100% | 🟡 1 pts to go |
| P06M | 6303 | 94.1% | 94.1% | -5.9 | 100% | 🟡 6 pts to go |
| P06T | 57911 | 92.5% | 92.5% | -7.5 | 100% | 🟡 8 pts to go |
| P06 | 281 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 690 | 97.4% | 97.4% | -2.6 | 100% | 🟡 3 pts to go |
| P08 | 20898 | 97.8% | 97.8% | -2.2 | 100% | 🟡 2 pts to go |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99903 | 94.0% | 94.0% |  | 100% | 🟡 6 pts to go |
| P10 | 2665 | 97.4% | 97.4% | -2.6 | 100% | 🟡 3 pts to go |
| P11 | 7106 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18386 | 96.3% | 96.3% | -3.7 | 100% | 🟡 4 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 95.5% | 95.5% | -4.5 | 100% | 🟡 4 pts to go |
| P01T | 325 | 95.4% | 95.4% | -4.6 | 100% | 🟡 5 pts to go |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P03 | 256 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3315 | 97.8% | 97.8% | -2.2 | 100% | 🟡 2 pts to go |
| P05 | 419 | 99.0% | 99.0% | -1.0 | 100% | 🟡 1 pts to go |
| P06M | 6303 | 94.1% | 94.1% | -5.9 | 100% | 🟡 6 pts to go |
| P06T | 57911 | 92.5% | 92.5% | -7.5 | 100% | 🟡 8 pts to go |
| P06 | 281 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 690 | 97.4% | 97.4% | -2.6 | 100% | 🟡 3 pts to go |
| P08 | 20898 | 97.8% | 97.8% | -2.2 | 100% | 🟡 2 pts to go |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99903 | 94.0% | 94.0% |  | 100% | 🟡 6 pts to go |
| P10 | 2665 | 97.4% | 97.4% | -2.6 | 100% | 🟡 3 pts to go |
| P11 | 7106 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18386 | 96.3% | 96.3% | -3.7 | 100% | 🟡 4 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 67 | 95.5% | 95.5% | -4.5 | 100% | 🟡 4 pts to go |
| P01T | 325 | 95.4% | 95.4% | -4.6 | 100% | 🟡 5 pts to go |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P03 | 256 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3315 | 97.8% | 97.8% | -2.2 | 100% | 🟡 2 pts to go |
| P05 | 419 | 99.0% | 99.0% | -1.0 | 100% | 🟡 1 pts to go |
| P06M | 6303 | 94.1% | 94.1% | -5.9 | 100% | 🟡 6 pts to go |
| P06T | 57911 | 92.5% | 92.5% | -7.5 | 100% | 🟡 8 pts to go |
| P06 | 281 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 690 | 97.4% | 97.4% | -2.6 | 100% | 🟡 3 pts to go |
| P08 | 20898 | 97.8% | 97.8% | -2.2 | 100% | 🟡 2 pts to go |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99903 | 94.0% | 94.0% |  | 100% | 🟡 6 pts to go |
| P10 | 2665 | 97.4% | 97.4% | -2.6 | 100% | 🟡 3 pts to go |
| P11 | 7106 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18386 | 96.3% | 96.3% | -3.7 | 100% | 🟡 4 pts to go |

