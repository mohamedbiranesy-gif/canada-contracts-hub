# Coverage vs the downstream team's targets — 2026-11-13

Benchmarks (field × package with a numeric target): **86 of 438 met** (19.6%); 64 within 10 points; 288 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 435, P01T 201, P01_GOLD 629, P02 474, P03 275, P04 4816, P05 443, P06M 32303, P06T 53176, P06 242, P07 759, P08 28712, P09 71, P10R 0, P10 2004, P11 1809, P12 11, P13 229919

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 14.7% | 7 | vendor GST/HST number (408 rows) |
| P01T | 201 | 1.0% | 33.3% | 8 | payment terms (157 rows) |
| P01_GOLD | 629 | 22.4% | 69.2% | 9 | payment terms (242 rows) |
| P02 | 474 | 6.8% | 52.7% | 9 | PO rule (366 rows) |
| P03 | 275 | 13.5% | 52.7% | 9 | payment terms (142 rows) |
| P04 | 4816 | 0.9% | 13.6% | 7 | PO rule (4550 rows) |
| P05 | 443 | 0.9% | 17.6% | 7 | payment terms (366 rows) |
| P06M | 32303 | 0.0% | 3.7% | 7 | PO rule (31483 rows) |
| P06T | 53176 | 0.1% | 15.2% | 7 | PO rule (52826 rows) |
| P06 | 242 | 0.4% | 11.6% | 7 | reference to quote (PO / contract / vendor id) (225 rows) |
| P07 | 759 | 0.0% | 5.3% | 6 | PO rule (721 rows) |
| P08 | 28712 | 0.0% | 3.6% | 6 | PO rule (28399 rows) |
| P09 | 71 | 4.2% | 35.2% | 8 | payment terms (62 rows) |
| P10 | 2004 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2004 rows) |
| P11 | 1809 | 0.1% | 8.2% | 6 | PO rule (1746 rows) |
| P12 | 11 | 0.0% | 36.4% | 8 | PO rule (11 rows) |
| P13 | 229919 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (229919 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 435 | 13 | 130 | 292 | 0 | 0 | 69 |
| P01T | 201 | 27 | 30 | 144 | 0 | 0 | 66 |
| P01_GOLD | 629 | 243 | 172 | 214 | 0 | 0 | 81 |
| P02 | 474 | 0 | 185 | 289 | 0 | 0 | 66 |
| P03 | 275 | 0 | 0 | 264 | 11 | 0 | 57 |
| P04 | 4816 | 0 | 0 | 4178 | 638 | 0 | 46 |
| P05 | 443 | 14 | 31 | 384 | 14 | 0 | 51 |
| P06M | 32303 | 0 | 52 | 32210 | 41 | 0 | 46 |
| P06T | 53176 | 0 | 25 | 36436 | 16715 | 0 | 38 |
| P06 | 242 | 15 | 33 | 194 | 0 | 0 | 67 |
| P07 | 759 | 0 | 21 | 720 | 18 | 0 | 56 |
| P08 | 28712 | 0 | 0 | 26109 | 2603 | 0 | 46 |
| P09 | 71 | 3 | 6 | 62 | 0 | 0 | 52 |
| P10 | 2004 | 2 | 10 | 1352 | 640 | 0 | 41 |
| P11 | 1809 | 7 | 11 | 37 | 0 | 1754 | 25 |
| P12 | 11 | 0 | 0 | 11 | 0 | 0 | 51 |
| P13 | 229919 | 27 | 95 | 229770 | 27 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 435 | 317 | 72.9% | tax treatment (86) |
| P01T | 201 | 120 | 59.7% | bill-to legal name and address (66) |
| P01_GOLD | 629 | 482 | 76.6% | bill-to legal name and address (87) |
| P02 | 474 | 324 | 68.4% | the buyer's PO / reference rule (80) |
| P03 | 275 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (275) |
| P04 | 4816 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4816) |
| P05 | 443 | 48 | 10.8% | a confirmed invoicing / AP or finance channel (347) |
| P06M | 32303 | 351 | 1.1% | a confirmed invoicing / AP or finance channel (31843) |
| P06T | 53176 | 340 | 0.6% | a confirmed invoicing / AP or finance channel (52427) |
| P06 | 242 | 43 | 17.8% | the buyer's PO / reference rule (108) |
| P07 | 759 | 52 | 6.9% | the buyer's PO / reference rule (318) |
| P08 | 28712 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (28712) |
| P09 | 71 | 10 | 14.1% | a confirmed invoicing / AP or finance channel (51) |
| P10 | 2004 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (1931) |
| P11 | 1809 | 18 | 1.0% | a confirmed invoicing / AP or finance channel (1754) |
| P12 | 11 | 2 | 18.2% | a confirmed invoicing / AP or finance channel (9) |
| P13 | 229919 | 76 | 0.0% | a confirmed invoicing / AP or finance channel (226958) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 435 | 13 | 3.0% | 7 | 0 | the vendor's GST/HST number (BN9) (407) |
| P01T | 201 | 82 | 40.8% | 2 | 0 | the vendor's GST/HST number (BN9) (72) |
| P01_GOLD | 629 | 396 | 63.0% | 9 | 0 | the vendor's GST/HST number (BN9) (160) |
| P02 | 474 | 205 | 43.2% | 20 | 0 | the vendor's GST/HST number (BN9) (222) |
| P03 | 275 | 19 | 6.9% | 0 | 127 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (105) |
| P04 | 4816 | 42 | 0.9% | 6 | 928 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3768) |
| P05 | 443 | 22 | 5.0% | 8 | 129 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (209) |
| P06M | 32303 | 14 | 0.0% | 14 | 994 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (30655) |
| P06T | 53176 | 362 | 0.7% | 16 | 19185 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (33157) |
| P06 | 242 | 25 | 10.3% | 47 | 0 | the vendor's GST/HST number (BN9) (107) |
| P07 | 759 | 38 | 5.0% | 142 | 40 | the vendor's GST/HST number (BN9) (342) |
| P08 | 28712 | 7 | 0.0% | 16 | 8446 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (20190) |
| P09 | 71 | 14 | 19.7% | 0 | 25 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (21) |
| P10 | 2004 | 5 | 0.2% | 14 | 276 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1634) |
| P11 | 1809 | 7 | 0.4% | 1 | 0 | a confirmed invoicing / AP or finance channel (1738) |
| P12 | 11 | 1 | 9.1% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 229919 | 42 | 0.0% | 1297 | 84971 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (141787) |
| **all** | 356279 | 1294 | 0.4% | 1599 | 115126 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 422 | 0 | 0 | 0 | 321 | 12 | 0 | 316 | 356 | 1 |
| P01T | 174 | 0 | 0 | 0 | 114 | 61 | 26 | 147 | 158 | 2 |
| P01_GOLD | 386 | 0 | 0 | 0 | 39 | 71 | 28 | 214 | 257 | 2 |
| P02 | 474 | 0 | 474 | 0 | 56 | 56 | 13 | 366 | 300 | 0 |
| P03 | 275 | 0 | 275 | 0 | 31 | 47 | 26 | 140 | 150 | 2 |
| P04 | 4816 | 0 | 4816 | 0 | 2689 | 1469 | 966 | 4550 | 4318 | 30 |
| P05 | 429 | 0 | 371 | 0 | 91 | 108 | 41 | 355 | 368 | 7 |
| P06M | 32303 | 0 | 32303 | 0 | 25834 | 2811 | 122 | 31483 | 30953 | 25 |
| P06T | 53176 | 0 | 53176 | 0 | 47739 | 32862 | 21201 | 52826 | 52270 | 390 |
| P06 | 227 | 0 | 0 | 0 | 127 | 67 | 37 | 176 | 197 | 5 |
| P07 | 759 | 0 | 759 | 0 | 515 | 282 | 91 | 721 | 716 | 5 |
| P08 | 28712 | 0 | 28712 | 0 | 22747 | 11914 | 3950 | 28399 | 27960 | 183 |
| P09 | 68 | 0 | 53 | 0 | 9 | 38 | 0 | 49 | 63 | 1 |
| P10 | 2002 | 0 | 1973 | 0 | 1042 | 1093 | 926 | 1941 | 1906 | 16 |
| P11 | 1802 | 1754 | 1710 | 0 | 940 | 1200 | 503 | 1746 | 1736 | 19 |
| P12 | 11 | 0 | 10 | 0 | 0 | 3 | 0 | 11 | 11 | 2 |
| P13 | 229892 | 0 | 229326 | 0 | 198560 | 140667 | 37 | 229482 | 228458 | 91 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 51.1% | 95% | 100883 |
| buyer_logo_url | P13 | 65.2% | 95% | 68589 |
| buyer_legal_name_as_published | P13 | 38.8% | 60% | 48700 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 45924 |
| ap_system_hint | P13 | 0.4% | 20% | 45143 |
| buyer_bn_as_published | P13 | 13.7% | 30% | 37398 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 34311 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 34263 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 33287 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 10621 |
| ap_system_hint | P06T | 0.7% | 20% | 10287 |
| vendor_registered_address | P08 | 39.5% | 70% | 8768 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 7874 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 7851 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 7620 |
| buyer_phone | P08 | 70.5% | 95% | 7030 |
| buyer_ap_cycle_published | P06M | 0.1% | 20% | 6443 |
| ap_system_hint | P06M | 1.3% | 20% | 6047 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5730 |
| ap_system_hint | P08 | 0.9% | 20% | 5480 |
| vendor_emails | P08 | 56.0% | 75% | 5462 |
| vendor_phone | P08 | 67.5% | 85% | 5021 |
| buyer_legal_name_as_published | P08 | 58.5% | 75% | 4736 |
| buyer_esignature_preference | P06M | 0.5% | 15% | 4683 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 4602 |
| vendor_trading_name | P08 | 34.0% | 50% | 4583 |
| buyer_tax_exempt_status | P06M | 0.9% | 15% | 4557 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 4192 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 4182 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 4128 |
| vendor_bn9 | P08 | 37.3% | 50% | 3657 |
| invoice_reference_hint | P08 | 12.3% | 25% | 3636 |
| average_contract_duration_days | P04 | 14.8% | 90% | 3622 |
| currency | P04 | 21.2% | 95% | 3557 |
| ap_phone | P04 | 15.6% | 85% | 3345 |
| commodity_codes | P04 | 16.8% | 85% | 3287 |
| award_or_notice_id | P04 | 18.6% | 85% | 3199 |
| contract_value | P04 | 20.7% | 85% | 3098 |
| invoice_mailing_address | P04 | 15.3% | 75% | 2876 |
| end_date | P04 | 33.5% | 90% | 2723 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 94.9% | 94.9% | +1.7 | 50% | ✅ met |
| P01T | 201 | 95.0% | 95.0% | -0.6 | 50% | ✅ met |
| P01_GOLD | 629 | 92.5% | 94.9% | +0.3 | 95% | 🟡 2 pts to go |
| P02 | 474 | 76.2% | 77.6% | +1.2 | 95% | ❌ 19 pts to go |
| P03 | 275 | 82.2% | 85.5% | +0.6 | 95% | ❌ 13 pts to go |
| P04 | 4816 | 43.9% | 45.2% | +12.1 | 90% | ❌ 46 pts to go |
| P05 | 443 | 41.5% | 44.5% | +1.9 | 70% | ❌ 28 pts to go |
| P06M | 32303 | 94.6% | 94.6% | +1.4 | n/a | no target |
| P06T | 53176 | 99.4% | 99.4% | +0.1 | n/a | no target |
| P06 | 242 | 32.2% | 32.2% | -3.2 | 30% | ✅ met |
| P07 | 759 | 13.8% | 13.8% | -0.4 | 30% | ❌ 16 pts to go |
| P08 | 28712 | 12.3% | 12.3% | +0.1 | 25% | ❌ 13 pts to go |
| P09 | 71 | 95.8% | 98.6% | -3.1 | 100% | 🟡 4 pts to go |
| P10 | 2004 | 3.1% | 3.1% | -0.2 | 25% | ❌ 22 pts to go |
| P11 | 1809 | 55.5% | 56.2% | +1.2 | 60% | 🟡 4 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 229919 | 98.4% | 98.4% | -1.2 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 201 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 629 | 6.0% | 6.0% | +0.3 | 50% | ❌ 44 pts to go |
| P02 | 474 | 5.3% | 5.3% | -0.9 | 50% | ❌ 45 pts to go |
| P03 | 275 | 1.8% | 1.8% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4816 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 443 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 32303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | +0.7 | 50% | ❌ 49 pts to go |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 92.4% | 92.4% | +2.8 | n/a | no target |
| P01T | 201 | 77.6% | 77.6% | -2.3 | 50% | ✅ met |
| P01_GOLD | 629 | 69.0% | 69.0% | +1.7 | 85% | ❌ 16 pts to go |
| P02 | 474 | 67.9% | 67.9% | +1.7 | 90% | ❌ 22 pts to go |
| P03 | 275 | 60.4% | 60.4% | -0.1 | 85% | ❌ 25 pts to go |
| P04 | 4816 | 41.7% | 41.7% | +12.6 | 85% | ❌ 43 pts to go |
| P05 | 443 | 32.3% | 32.3% | +2.4 | 60% | ❌ 28 pts to go |
| P06M | 32303 | 94.4% | 94.4% | +1.4 | n/a | no target |
| P06T | 53176 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06 | 242 | 7.0% | 7.0% | +0.6 | n/a | no target |
| P07 | 759 | 9.1% | 9.1% | +0.0 | n/a | no target |
| P08 | 28712 | 11.4% | 11.4% | +0.1 | n/a | no target |
| P09 | 71 | 83.1% | 83.1% | -12.5 | 100% | ❌ 17 pts to go |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 52.9% | 52.9% | +1.4 | 60% | 🟡 7 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 201 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 629 | 48.5% | 48.5% | -3.2 | 80% | ❌ 32 pts to go |
| P02 | 474 | 56.3% | 56.3% | -1.8 | 60% | 🟡 4 pts to go |
| P03 | 275 | 46.2% | 46.2% | -4.2 | 80% | ❌ 34 pts to go |
| P04 | 4816 | 17.9% | 17.9% | -6.1 | 50% | ❌ 32 pts to go |
| P05 | 443 | 14.9% | 14.9% | +2.3 | 40% | ❌ 25 pts to go |
| P06M | 32303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 36.6% | 36.6% | -44.5 | 50% | ❌ 13 pts to go |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 3.3% | 3.3% | +0.0 | 40% | ❌ 37 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 201 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 629 | 58.2% | 58.2% | -2.7 | 85% | ❌ 27 pts to go |
| P02 | 474 | 55.9% | 55.9% | -2.2 | 90% | ❌ 34 pts to go |
| P03 | 275 | 54.5% | 54.5% | -4.9 | 85% | ❌ 30 pts to go |
| P04 | 4816 | 18.6% | 18.6% | -6.3 | 85% | ❌ 66 pts to go |
| P05 | 443 | 23.0% | 23.0% | +2.6 | 50% | ❌ 27 pts to go |
| P06M | 32303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 88.7% | 88.7% | -8.4 | 100% | ❌ 11 pts to go |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 3.6% | 3.6% | +0.0 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 629 | 12.1% | 12.1% | -0.5 | 60% | ❌ 48 pts to go |
| P02 | 474 | 6.5% | 6.5% | -0.8 | 50% | ❌ 44 pts to go |
| P03 | 275 | 7.3% | 7.3% | -1.3 | 50% | ❌ 43 pts to go |
| P04 | 4816 | 1.4% | 1.4% | -0.5 | 40% | ❌ 39 pts to go |
| P05 | 443 | 0.9% | 0.9% | +0.2 | 20% | ❌ 19 pts to go |
| P06M | 32303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 5.6% | 5.6% | +2.0 | 50% | ❌ 44 pts to go |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 629 | 35.8% | 35.8% | -0.1 | 80% | ❌ 44 pts to go |
| P02 | 474 | 52.1% | 52.1% | -0.9 | 90% | ❌ 38 pts to go |
| P03 | 275 | 32.7% | 32.7% | -1.1 | 80% | ❌ 47 pts to go |
| P04 | 4816 | 16.8% | 16.8% | -5.4 | 85% | ❌ 68 pts to go |
| P05 | 443 | 7.9% | 7.9% | +1.5 | 50% | ❌ 42 pts to go |
| P06M | 32303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 62.0% | 62.0% | -11.1 | 95% | ❌ 33 pts to go |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 2.7% | 2.7% | +0.1 | 50% | ❌ 47 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 629 | 8.3% | 8.3% | +0.2 | 50% | ❌ 42 pts to go |
| P02 | 474 | 5.1% | 5.1% | -1.1 | 50% | ❌ 45 pts to go |
| P03 | 275 | 2.5% | 2.5% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 4816 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 32303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | +1.0 | n/a | no target |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 201 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 629 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 474 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4816 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 443 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 32303 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 53176 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 242 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 759 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28712 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2004 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1809 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 6.2% | 6.2% | -0.2 | 70% | ❌ 64 pts to go |
| P01T | 201 | 56.2% | 56.2% | -4.1 | 60% | 🟡 4 pts to go |
| P01_GOLD | 629 | 72.0% | 72.0% | -2.8 | 90% | ❌ 18 pts to go |
| P02 | 474 | 50.6% | 50.6% | -3.7 | 85% | ❌ 34 pts to go |
| P03 | 275 | 62.2% | 62.2% | -4.7 | 90% | ❌ 28 pts to go |
| P04 | 4816 | 29.1% | 29.1% | -9.1 | 75% | ❌ 46 pts to go |
| P05 | 443 | 53.5% | 53.5% | -1.2 | 50% | ✅ met |
| P06M | 32303 | 3.8% | 3.8% | +0.9 | n/a | no target |
| P06T | 53176 | 68.5% | 68.5% | +4.0 | n/a | no target |
| P06 | 242 | 45.0% | 45.0% | +2.9 | 40% | ✅ met |
| P07 | 759 | 37.4% | 37.4% | +5.3 | 50% | ❌ 13 pts to go |
| P08 | 28712 | 37.3% | 37.3% | +6.7 | 50% | ❌ 13 pts to go |
| P09 | 71 | 64.8% | 64.8% | +8.1 | 80% | ❌ 15 pts to go |
| P10 | 2004 | 38.8% | 38.8% | +0.0 | 40% | 🟡 1 pts to go |
| P11 | 1809 | 54.9% | 54.9% | +0.3 | 60% | 🟡 5 pts to go |
| P12 | 11 | 54.5% | 54.5% | +9.0 | 85% | ❌ 30 pts to go |
| P13 | 229919 | 42.5% | 42.5% | -2.3 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 46.2% | 46.2% | -0.4 | n/a | no target |
| P01T | 201 | 57.2% | 57.2% | -2.6 | n/a | no target |
| P01_GOLD | 629 | 73.8% | 73.8% | +0.9 | 95% | ❌ 21 pts to go |
| P02 | 474 | 75.1% | 75.1% | +0.5 | 95% | ❌ 20 pts to go |
| P03 | 275 | 69.8% | 69.8% | +0.3 | 95% | ❌ 25 pts to go |
| P04 | 4816 | 59.5% | 59.5% | +6.4 | 95% | ❌ 36 pts to go |
| P05 | 443 | 58.5% | 58.5% | +0.4 | 70% | ❌ 12 pts to go |
| P06M | 32303 | 40.3% | 40.3% | -1.0 | n/a | no target |
| P06T | 53176 | 72.4% | 72.4% | +4.9 | n/a | no target |
| P06 | 242 | 40.1% | 40.1% | +1.9 | 80% | ❌ 40 pts to go |
| P07 | 759 | 37.7% | 37.7% | +6.7 | 70% | ❌ 32 pts to go |
| P08 | 28712 | 39.5% | 39.5% | +9.8 | 70% | ❌ 30 pts to go |
| P09 | 71 | 60.6% | 60.6% | -25.6 | 100% | ❌ 39 pts to go |
| P10 | 2004 | 39.2% | 39.2% | +0.0 | 70% | ❌ 31 pts to go |
| P11 | 1809 | 60.1% | 60.1% | +1.5 | 75% | ❌ 15 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 38.7% | 38.7% | -1.5 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 21.8% | 21.8% | -0.3 | n/a | no target |
| P01T | 201 | 59.7% | 59.7% | -5.8 | n/a | no target |
| P01_GOLD | 629 | 50.9% | 50.9% | +2.1 | 60% | 🟡 9 pts to go |
| P02 | 474 | 59.3% | 59.3% | +3.5 | 60% | 🟡 1 pts to go |
| P03 | 275 | 52.7% | 52.7% | +0.4 | 60% | 🟡 7 pts to go |
| P04 | 4816 | 53.8% | 53.8% | +11.2 | 55% | 🟡 1 pts to go |
| P05 | 443 | 23.3% | 23.3% | +0.6 | 50% | ❌ 27 pts to go |
| P06M | 32303 | 11.9% | 11.9% | +2.4 | n/a | no target |
| P06T | 53176 | 73.2% | 73.2% | +5.3 | n/a | no target |
| P06 | 242 | 50.8% | 50.8% | +2.2 | n/a | no target |
| P07 | 759 | 39.9% | 39.9% | +0.3 | 55% | ❌ 15 pts to go |
| P08 | 28712 | 34.0% | 34.0% | +1.0 | 50% | ❌ 16 pts to go |
| P09 | 71 | 39.4% | 39.4% | -32.6 | 70% | ❌ 31 pts to go |
| P10 | 2004 | 47.6% | 47.6% | -0.5 | 55% | 🟡 7 pts to go |
| P11 | 1809 | 59.1% | 59.1% | -0.1 | 50% | ✅ met |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 229919 | 2.7% | 2.7% | -0.5 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 22.8% | 22.8% | -10.5 | n/a | no target |
| P01T | 201 | 77.6% | 77.6% | -1.9 | n/a | no target |
| P01_GOLD | 629 | 47.4% | 47.4% | -3.0 | 70% | ❌ 23 pts to go |
| P02 | 474 | 54.9% | 54.9% | -1.9 | 70% | ❌ 15 pts to go |
| P03 | 275 | 46.9% | 46.9% | -3.5 | 70% | ❌ 23 pts to go |
| P04 | 4816 | 48.8% | 48.8% | -6.1 | 65% | ❌ 16 pts to go |
| P05 | 443 | 30.0% | 30.0% | +0.9 | 60% | ❌ 30 pts to go |
| P06M | 32303 | 22.6% | 22.6% | -4.8 | n/a | no target |
| P06T | 53176 | 86.4% | 86.4% | +3.7 | n/a | no target |
| P06 | 242 | 70.2% | 70.2% | +0.9 | 40% | ✅ met |
| P07 | 759 | 66.4% | 66.4% | +1.4 | 85% | ❌ 19 pts to go |
| P08 | 28712 | 67.5% | 67.5% | +3.5 | 85% | ❌ 18 pts to go |
| P09 | 71 | 29.6% | 29.6% | -26.8 | 85% | ❌ 55 pts to go |
| P10 | 2004 | 65.0% | 65.0% | -1.1 | 85% | ❌ 20 pts to go |
| P11 | 1809 | 68.4% | 68.4% | +0.3 | 75% | 🟡 7 pts to go |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 229919 | 85.8% | 85.8% | -6.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 27.4% | 27.4% | -10.4 | n/a | no target |
| P01T | 201 | 98.5% | 98.5% | +0.2 | n/a | no target |
| P01_GOLD | 629 | 74.2% | 74.2% | -4.4 | 90% | ❌ 16 pts to go |
| P02 | 474 | 78.5% | 78.5% | -3.3 | 90% | ❌ 12 pts to go |
| P03 | 275 | 79.3% | 79.3% | -6.0 | 90% | ❌ 11 pts to go |
| P04 | 4816 | 70.0% | 70.0% | -12.8 | 85% | ❌ 15 pts to go |
| P05 | 443 | 44.9% | 44.9% | +0.4 | 70% | ❌ 25 pts to go |
| P06M | 32303 | 28.3% | 28.3% | -4.7 | n/a | no target |
| P06T | 53176 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 242 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 759 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 28712 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 71 | 43.7% | 43.7% | -34.1 | 100% | ❌ 56 pts to go |
| P10 | 2004 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1809 | 97.5% | 97.5% | -0.5 | 100% | 🟡 2 pts to go |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 229919 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 12.6% | 12.6% | -3.5 | n/a | no target |
| P01T | 201 | 54.2% | 54.2% | -5.6 | n/a | no target |
| P01_GOLD | 629 | 41.8% | 41.8% | -1.6 | 70% | ❌ 28 pts to go |
| P02 | 474 | 46.2% | 46.2% | -1.0 | 75% | ❌ 29 pts to go |
| P03 | 275 | 42.9% | 42.9% | -1.8 | 75% | ❌ 32 pts to go |
| P04 | 4816 | 34.6% | 34.6% | -4.1 | 70% | ❌ 35 pts to go |
| P05 | 443 | 22.3% | 22.3% | +1.0 | 55% | ❌ 33 pts to go |
| P06M | 32303 | 6.8% | 6.8% | +0.9 | n/a | no target |
| P06T | 53176 | 43.3% | 43.3% | -4.1 | n/a | no target |
| P06 | 242 | 52.1% | 52.1% | +1.0 | n/a | no target |
| P07 | 759 | 53.8% | 53.8% | +1.1 | 70% | ❌ 16 pts to go |
| P08 | 28712 | 56.0% | 56.0% | +1.2 | 75% | ❌ 19 pts to go |
| P09 | 71 | 21.1% | 21.1% | -25.8 | 85% | ❌ 64 pts to go |
| P10 | 2004 | 44.4% | 44.4% | +0.0 | 80% | ❌ 36 pts to go |
| P11 | 1809 | 51.8% | 51.8% | -1.5 | 70% | ❌ 18 pts to go |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 229919 | 5.5% | 5.5% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 26.0% | 26.0% | -11.8 | n/a | no target |
| P01T | 201 | 96.5% | 96.5% | +0.0 | n/a | no target |
| P01_GOLD | 629 | 68.4% | 68.4% | -4.5 | 90% | ❌ 22 pts to go |
| P02 | 474 | 72.8% | 72.8% | -3.9 | 90% | ❌ 17 pts to go |
| P03 | 275 | 76.0% | 76.0% | -6.0 | 90% | ❌ 14 pts to go |
| P04 | 4816 | 65.7% | 65.7% | -12.0 | 85% | ❌ 19 pts to go |
| P05 | 443 | 43.6% | 43.6% | +0.7 | 75% | ❌ 31 pts to go |
| P06M | 32303 | 27.4% | 27.4% | -5.5 | n/a | no target |
| P06T | 53176 | 97.6% | 97.6% | -0.7 | n/a | no target |
| P06 | 242 | 91.7% | 91.7% | +1.7 | n/a | no target |
| P07 | 759 | 94.2% | 94.2% | +2.5 | 100% | 🟡 6 pts to go |
| P08 | 28712 | 92.8% | 92.8% | +5.5 | 100% | 🟡 7 pts to go |
| P09 | 71 | 33.8% | 33.8% | -32.7 | n/a | no target |
| P10 | 2004 | 89.9% | 89.9% | -0.4 | 100% | ❌ 10 pts to go |
| P11 | 1809 | 90.0% | 90.0% | -0.2 | n/a | no target |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 229919 | 67.3% | 67.3% | -2.5 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 34.9% | 34.9% | -2.0 | n/a | no target · QC vendors: 70 rows, 100.0% filled |
| P01T | 201 | 23.9% | 23.9% | +4.2 | n/a | no target · QC vendors: 36 rows, 91.7% filled |
| P01_GOLD | 629 | 45.8% | 45.8% | +2.3 | 95% | ❌ 49 pts to go · QC vendors: 47 rows, 95.7% filled |
| P02 | 474 | 58.9% | 58.9% | +2.9 | 95% | ❌ 36 pts to go · QC vendors: 114 rows, 100.0% filled |
| P03 | 275 | 44.4% | 44.4% | +1.5 | 95% | ❌ 51 pts to go · QC vendors: 20 rows, 100.0% filled |
| P04 | 4816 | 40.3% | 40.3% | +7.9 | 95% | ❌ 55 pts to go · QC vendors: 647 rows, 98.3% filled |
| P05 | 443 | 14.7% | 14.7% | +0.7 | n/a | no target · QC vendors: 40 rows, 100.0% filled |
| P06M | 32303 | 34.8% | 34.8% | -2.7 | n/a | no target · QC vendors: 8073 rows, 100.0% filled |
| P06T | 53176 | 40.5% | 40.5% | +9.9 | n/a | no target · QC vendors: 21773 rows, 96.8% filled |
| P06 | 242 | 7.4% | 7.4% | +0.3 | n/a | no target · QC vendors: 10 rows, 60.0% filled |
| P07 | 759 | 8.2% | 8.2% | +1.3 | n/a | no target · QC vendors: 53 rows, 83.0% filled |
| P08 | 28712 | 9.0% | 9.0% | +2.0 | n/a | no target · QC vendors: 2226 rows, 96.3% filled |
| P09 | 71 | 28.2% | 28.2% | -45.3 | 95% | ❌ 67 pts to go · QC vendors: 6 rows, 100.0% filled |
| P10 | 2004 | 15.9% | 15.9% | +0.2 | n/a | no target · QC vendors: 196 rows, 92.3% filled |
| P11 | 1809 | 21.3% | 21.3% | +1.7 | n/a | no target · QC vendors: 329 rows, 95.1% filled |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 229919 | 21.2% | 21.2% | -1.0 | n/a | no target · QC vendors: 48717 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 45.5% | 45.5% | -0.7 | n/a | no target · vendors with a registry record: 198 rows, 100.0% filled |
| P01T | 201 | 57.2% | 57.2% | -2.6 | n/a | no target · vendors with a registry record: 115 rows, 100.0% filled |
| P01_GOLD | 629 | 81.6% | 81.6% | +0.7 | 100% | ❌ 18 pts to go · vendors with a registry record: 513 rows, 100.0% filled |
| P02 | 474 | 79.1% | 79.1% | +0.7 | 100% | ❌ 21 pts to go · vendors with a registry record: 375 rows, 100.0% filled |
| P03 | 275 | 77.8% | 77.8% | -0.4 | 100% | ❌ 22 pts to go · vendors with a registry record: 214 rows, 100.0% filled |
| P04 | 4816 | 60.2% | 60.2% | +6.2 | 100% | ❌ 40 pts to go · vendors with a registry record: 2898 rows, 100.0% filled |
| P05 | 443 | 62.5% | 62.5% | -0.3 | n/a | no target · vendors with a registry record: 277 rows, 100.0% filled |
| P06M | 32303 | 40.3% | 40.3% | -0.9 | n/a | no target · vendors with a registry record: 13028 rows, 100.0% filled |
| P06T | 53176 | 72.4% | 72.4% | +4.8 | n/a | no target · vendors with a registry record: 38508 rows, 100.0% filled |
| P06 | 242 | 41.3% | 41.3% | +2.0 | n/a | no target · vendors with a registry record: 100 rows, 100.0% filled |
| P07 | 759 | 38.3% | 38.3% | +6.5 | n/a | no target · vendors with a registry record: 291 rows, 100.0% filled |
| P08 | 28712 | 39.6% | 39.6% | +9.6 | n/a | no target · vendors with a registry record: 11383 rows, 100.0% filled |
| P09 | 71 | 73.2% | 73.2% | -16.3 | n/a | no target · vendors with a registry record: 52 rows, 100.0% filled |
| P10 | 2004 | 40.1% | 40.1% | +0.0 | n/a | no target · vendors with a registry record: 804 rows, 100.0% filled |
| P11 | 1809 | 61.0% | 61.0% | +1.7 | n/a | no target · vendors with a registry record: 1103 rows, 100.0% filled |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P13 | 229919 | 38.7% | 38.7% | -1.5 | n/a | no target · vendors with a registry record: 88883 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 97.2% | 97.2% | +0.8 | 90% | ✅ met |
| P01T | 201 | 69.7% | 69.7% | -1.0 | 90% | ❌ 20 pts to go |
| P01_GOLD | 629 | 88.7% | 88.7% | +1.3 | 95% | 🟡 6 pts to go |
| P02 | 474 | 88.2% | 88.2% | +0.0 | 95% | 🟡 7 pts to go |
| P03 | 275 | 82.9% | 82.9% | -0.2 | 85% | 🟡 2 pts to go |
| P04 | 4816 | 69.5% | 69.5% | +5.0 | 90% | ❌ 20 pts to go |
| P05 | 443 | 75.6% | 75.6% | -2.4 | 75% | ✅ met |
| P06M | 32303 | 91.3% | 91.3% | -2.5 | n/a | no target |
| P06T | 53176 | 38.2% | 38.2% | +1.3 | n/a | no target |
| P06 | 242 | 72.3% | 72.3% | +1.2 | 80% | 🟡 8 pts to go |
| P07 | 759 | 62.8% | 63.0% | +4.6 | 80% | ❌ 17 pts to go |
| P08 | 28712 | 58.5% | 58.5% | +6.6 | 75% | ❌ 16 pts to go |
| P09 | 71 | 46.5% | 46.5% | -29.1 | 95% | ❌ 48 pts to go |
| P10 | 2004 | 45.5% | 45.5% | -1.3 | 70% | ❌ 24 pts to go |
| P11 | 1809 | 33.7% | 33.7% | +1.9 | 65% | ❌ 31 pts to go |
| P12 | 11 | 72.7% | 72.7% | +0.0 | 80% | 🟡 7 pts to go |
| P13 | 229919 | 38.8% | 38.8% | -6.8 | 60% | ❌ 21 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 17.7% | 17.7% | -0.8 | 50% | ❌ 32 pts to go |
| P01T | 201 | 15.4% | 15.4% | -0.8 | n/a | no target |
| P01_GOLD | 629 | 19.9% | 19.9% | +0.1 | 40% | ❌ 20 pts to go |
| P02 | 474 | 19.0% | 19.0% | -0.9 | 40% | ❌ 21 pts to go |
| P03 | 275 | 20.7% | 20.7% | +0.4 | 40% | ❌ 19 pts to go |
| P04 | 4816 | 15.8% | 15.8% | -0.5 | 40% | ❌ 24 pts to go |
| P05 | 443 | 20.8% | 20.8% | -0.1 | 25% | 🟡 4 pts to go |
| P06M | 32303 | 21.8% | 21.8% | +1.4 | n/a | no target |
| P06T | 53176 | 11.9% | 11.9% | +4.4 | n/a | no target |
| P06 | 242 | 22.3% | 22.3% | +4.8 | 35% | ❌ 13 pts to go |
| P07 | 759 | 27.9% | 27.9% | +8.8 | 35% | 🟡 7 pts to go |
| P08 | 28712 | 27.0% | 27.0% | +9.3 | 35% | 🟡 8 pts to go |
| P09 | 71 | 8.5% | 8.5% | -8.2 | n/a | no target |
| P10 | 2004 | 8.7% | 8.7% | +1.6 | 30% | ❌ 21 pts to go |
| P11 | 1809 | 11.3% | 11.3% | +4.8 | n/a | no target |
| P12 | 11 | 9.1% | 9.1% | -9.1 | n/a | no target |
| P13 | 229919 | 13.7% | 13.7% | +1.2 | 30% | ❌ 16 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 201 | 85.6% | 85.6% | +0.4 | 100% | ❌ 14 pts to go |
| P01_GOLD | 629 | 91.9% | 91.9% | +0.8 | 100% | 🟡 8 pts to go |
| P02 | 474 | 96.8% | 96.8% | +0.2 | 100% | 🟡 3 pts to go |
| P03 | 275 | 89.8% | 89.8% | +0.3 | 100% | ❌ 10 pts to go |
| P04 | 4816 | 79.5% | 79.5% | +7.0 | 100% | ❌ 20 pts to go |
| P05 | 443 | 89.8% | 89.8% | -0.2 | 100% | ❌ 10 pts to go |
| P06M | 32303 | 99.6% | 99.6% | +0.2 | n/a | no target |
| P06T | 53176 | 60.1% | 60.1% | +1.4 | n/a | no target |
| P06 | 242 | 83.1% | 83.1% | +1.0 | 95% | ❌ 12 pts to go |
| P07 | 759 | 87.7% | 87.7% | +2.3 | 95% | 🟡 7 pts to go |
| P08 | 28712 | 86.2% | 86.2% | +1.7 | 95% | 🟡 9 pts to go |
| P09 | 71 | 94.4% | 94.4% | -2.0 | 100% | 🟡 6 pts to go |
| P10 | 2004 | 53.7% | 53.7% | -0.9 | 95% | ❌ 41 pts to go |
| P11 | 1809 | 64.2% | 64.2% | +3.3 | 80% | ❌ 16 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 229919 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 63.9% | 63.9% | -7.2 | n/a | no target |
| P01T | 201 | 70.6% | 70.6% | -3.6 | n/a | no target |
| P01_GOLD | 629 | 72.3% | 72.3% | -0.9 | 90% | ❌ 18 pts to go |
| P02 | 474 | 77.4% | 77.4% | -1.0 | 95% | ❌ 18 pts to go |
| P03 | 275 | 72.7% | 72.7% | -1.4 | 95% | ❌ 22 pts to go |
| P04 | 4816 | 69.1% | 69.1% | -0.4 | 95% | ❌ 26 pts to go |
| P05 | 443 | 70.9% | 70.9% | -1.6 | 90% | ❌ 19 pts to go |
| P06M | 32303 | 67.8% | 67.8% | -8.9 | n/a | no target |
| P06T | 53176 | 55.8% | 55.8% | -2.8 | n/a | no target |
| P06 | 242 | 71.1% | 71.1% | +5.7 | 95% | ❌ 24 pts to go |
| P07 | 759 | 67.1% | 67.1% | +7.4 | 90% | ❌ 23 pts to go |
| P08 | 28712 | 70.5% | 70.5% | +11.9 | 95% | ❌ 24 pts to go |
| P09 | 71 | 66.2% | 66.2% | -19.6 | 100% | ❌ 34 pts to go |
| P10 | 2004 | 52.7% | 52.7% | -1.1 | 95% | ❌ 42 pts to go |
| P11 | 1809 | 32.5% | 32.5% | +1.8 | 75% | ❌ 42 pts to go |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target |
| P13 | 229919 | 51.1% | 51.1% | -16.8 | 95% | ❌ 44 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 75.6% | 75.6% | -7.9 | n/a | no target |
| P01T | 201 | 89.1% | 89.1% | -2.6 | 95% | 🟡 6 pts to go |
| P01_GOLD | 629 | 85.5% | 85.5% | +0.5 | 90% | 🟡 4 pts to go |
| P02 | 474 | 90.5% | 90.5% | -0.5 | 95% | 🟡 4 pts to go |
| P03 | 275 | 82.9% | 82.9% | -0.9 | 95% | ❌ 12 pts to go |
| P04 | 4816 | 89.7% | 89.7% | -1.9 | 90% | 🟡 0 pts to go |
| P05 | 443 | 91.4% | 91.4% | -1.0 | 95% | 🟡 4 pts to go |
| P06M | 32303 | 78.7% | 78.7% | -6.6 | n/a | no target |
| P06T | 53176 | 85.4% | 85.4% | +0.8 | n/a | no target |
| P06 | 242 | 92.1% | 92.1% | +6.7 | 100% | 🟡 8 pts to go |
| P07 | 759 | 94.2% | 94.2% | +10.6 | 100% | 🟡 6 pts to go |
| P08 | 28712 | 94.8% | 94.8% | +17.0 | 100% | 🟡 5 pts to go |
| P09 | 71 | 71.8% | 71.8% | -2.4 | n/a | no target |
| P10 | 2004 | 94.2% | 94.2% | -0.2 | 100% | 🟡 6 pts to go |
| P11 | 1809 | 55.1% | 55.1% | +4.0 | 80% | ❌ 25 pts to go |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 229919 | 65.2% | 65.2% | -15.6 | 95% | ❌ 30 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 3.2% | 3.2% | +0.0 | n/a | no target |
| P01T | 201 | 10.0% | 10.0% | +1.3 | n/a | no target |
| P01_GOLD | 629 | 13.5% | 13.5% | -0.5 | 25% | ❌ 12 pts to go |
| P02 | 474 | 24.5% | 24.5% | -0.3 | 40% | ❌ 16 pts to go |
| P03 | 275 | 9.1% | 9.1% | +0.1 | 20% | ❌ 11 pts to go |
| P04 | 4816 | 2.5% | 2.5% | -0.8 | 20% | ❌ 18 pts to go |
| P05 | 443 | 2.9% | 2.9% | -0.4 | 15% | ❌ 12 pts to go |
| P06M | 32303 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 53176 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 242 | 5.8% | 5.8% | +0.4 | n/a | no target |
| P07 | 759 | 8.2% | 8.2% | +0.3 | n/a | no target |
| P08 | 28712 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | -6.2 | n/a | no target |
| P10 | 2004 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1809 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 13.6% | 13.6% | -2.5 | n/a | no target |
| P01T | 201 | 17.9% | 17.9% | -1.3 | 70% | ❌ 52 pts to go |
| P01_GOLD | 629 | 41.3% | 41.3% | -0.8 | 80% | ❌ 39 pts to go |
| P02 | 474 | 55.7% | 55.7% | -1.6 | 90% | ❌ 34 pts to go |
| P03 | 275 | 18.5% | 18.5% | -0.7 | 60% | ❌ 42 pts to go |
| P04 | 4816 | 15.6% | 15.6% | -4.6 | 85% | ❌ 69 pts to go |
| P05 | 443 | 11.5% | 11.5% | +0.4 | 50% | ❌ 38 pts to go |
| P06M | 32303 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06T | 53176 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 242 | 13.2% | 13.2% | +0.0 | n/a | no target |
| P07 | 759 | 9.9% | 9.9% | +0.8 | n/a | no target |
| P08 | 28712 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 71 | 33.8% | 33.8% | -38.2 | 95% | ❌ 61 pts to go |
| P10 | 2004 | 1.4% | 1.4% | -0.2 | n/a | no target |
| P11 | 1809 | 12.5% | 12.5% | -0.5 | n/a | no target |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 229919 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 5.5% | 5.5% | -0.1 | n/a | no target |
| P01T | 201 | 11.4% | 11.4% | +2.2 | n/a | no target |
| P01_GOLD | 629 | 33.2% | 33.2% | -0.6 | 70% | ❌ 37 pts to go |
| P02 | 474 | 38.8% | 38.8% | +0.1 | 75% | ❌ 36 pts to go |
| P03 | 275 | 19.3% | 19.3% | +0.1 | 55% | ❌ 36 pts to go |
| P04 | 4816 | 15.3% | 15.3% | -4.9 | 75% | ❌ 60 pts to go |
| P05 | 443 | 10.6% | 10.6% | +0.4 | 50% | ❌ 39 pts to go |
| P06M | 32303 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06T | 53176 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 242 | 6.2% | 6.2% | +0.5 | n/a | no target |
| P07 | 759 | 5.1% | 5.1% | +0.5 | n/a | no target |
| P08 | 28712 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 71 | 33.8% | 33.8% | -34.9 | 95% | ❌ 61 pts to go |
| P10 | 2004 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P11 | 1809 | 12.3% | 12.3% | -0.5 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 229919 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 11.0% | 11.0% | +3.4 | n/a | no target |
| P01T | 201 | 8.5% | 8.5% | -0.2 | n/a | no target |
| P01_GOLD | 629 | 55.2% | 55.3% | -1.9 | 80% | ❌ 25 pts to go |
| P02 | 474 | 44.5% | 44.7% | -0.8 | 75% | ❌ 30 pts to go |
| P03 | 275 | 33.8% | 33.8% | -2.3 | 70% | ❌ 36 pts to go |
| P04 | 4816 | 15.0% | 15.3% | -4.9 | 70% | ❌ 55 pts to go |
| P05 | 443 | 14.2% | 14.2% | +0.2 | 50% | ❌ 36 pts to go |
| P06M | 32303 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P06T | 53176 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 242 | 13.6% | 13.6% | +0.4 | n/a | no target |
| P07 | 759 | 1.4% | 1.4% | +0.3 | n/a | no target |
| P08 | 28712 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P09 | 71 | 45.1% | 45.1% | -1.8 | 80% | ❌ 35 pts to go |
| P10 | 2004 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P11 | 1809 | 4.3% | 4.3% | -0.2 | n/a | no target |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 229919 | 0.1% | 0.1% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 18.2% | 18.2% | +3.3 | n/a | no target |
| P01T | 201 | 21.4% | 21.4% | +2.2 | 60% | ❌ 39 pts to go |
| P01_GOLD | 629 | 59.1% | 59.1% | -3.1 | 70% | ❌ 11 pts to go |
| P02 | 474 | 36.7% | 36.7% | -2.8 | 50% | ❌ 13 pts to go |
| P03 | 275 | 45.5% | 45.5% | -2.2 | 55% | 🟡 10 pts to go |
| P04 | 4816 | 10.3% | 10.3% | -2.2 | 40% | ❌ 30 pts to go |
| P05 | 443 | 16.9% | 16.9% | +0.3 | 40% | ❌ 23 pts to go |
| P06M | 32303 | 4.2% | 4.2% | +1.4 | n/a | no target |
| P06T | 53176 | 1.7% | 1.7% | +0.2 | n/a | no target |
| P06 | 242 | 18.6% | 18.6% | +0.4 | n/a | no target |
| P07 | 759 | 5.7% | 5.7% | +0.8 | n/a | no target |
| P08 | 28712 | 2.6% | 2.6% | +0.5 | n/a | no target |
| P09 | 71 | 11.3% | 11.3% | +5.5 | n/a | no target |
| P10 | 2004 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P11 | 1809 | 4.0% | 4.0% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.6% | 0.6% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 27.4% | 27.4% | +5.7 | n/a | no target |
| P01T | 201 | 26.9% | 26.9% | -1.0 | 65% | ❌ 38 pts to go |
| P01_GOLD | 629 | 66.0% | 66.0% | -2.6 | 70% | 🟡 4 pts to go |
| P02 | 474 | 22.8% | 22.8% | -0.9 | 50% | ❌ 27 pts to go |
| P03 | 275 | 49.1% | 49.1% | -1.3 | 60% | ❌ 11 pts to go |
| P04 | 4816 | 5.5% | 5.5% | -0.1 | 40% | ❌ 34 pts to go |
| P05 | 443 | 19.9% | 19.9% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 32303 | 2.5% | 2.5% | +0.8 | n/a | no target |
| P06T | 53176 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06 | 242 | 27.3% | 27.3% | -2.0 | n/a | no target |
| P07 | 759 | 5.0% | 5.0% | -0.1 | n/a | no target |
| P08 | 28712 | 1.1% | 1.1% | +0.2 | n/a | no target |
| P09 | 71 | 31.0% | 31.0% | +20.1 | n/a | no target |
| P10 | 2004 | 3.1% | 3.1% | -0.2 | n/a | no target |
| P11 | 1809 | 3.5% | 3.5% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 18.4% | 18.4% | +6.4 | n/a | no target |
| P01T | 201 | 12.9% | 12.9% | +0.2 | n/a | no target |
| P01_GOLD | 629 | 48.3% | 48.3% | -1.9 | 50% | 🟡 2 pts to go |
| P02 | 474 | 35.7% | 35.7% | -1.9 | n/a | no target |
| P03 | 275 | 50.5% | 50.5% | -0.3 | 60% | 🟡 10 pts to go |
| P04 | 4816 | 9.6% | 9.6% | -3.2 | n/a | no target |
| P05 | 443 | 16.0% | 16.0% | +0.8 | n/a | no target |
| P06M | 32303 | 1.1% | 1.1% | +0.3 | n/a | no target |
| P06T | 53176 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 242 | 18.2% | 18.2% | -2.2 | n/a | no target |
| P07 | 759 | 5.3% | 5.3% | -0.4 | n/a | no target |
| P08 | 28712 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P09 | 71 | 23.9% | 23.9% | +3.2 | n/a | no target |
| P10 | 2004 | 2.3% | 2.3% | -0.2 | n/a | no target |
| P11 | 1809 | 2.3% | 2.3% | -0.4 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 229919 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 9.0% | 9.0% | +0.2 | 15% | 🟡 6 pts to go |
| P01T | 201 | 13.4% | 13.4% | +0.7 | 15% | 🟡 2 pts to go |
| P01_GOLD | 629 | 32.9% | 32.9% | -2.2 | 40% | 🟡 7 pts to go |
| P02 | 474 | 11.0% | 11.2% | -1.2 | 25% | ❌ 14 pts to go |
| P03 | 275 | 15.3% | 15.3% | -1.2 | 25% | 🟡 10 pts to go |
| P04 | 4816 | 2.2% | 2.2% | -0.5 | 15% | ❌ 13 pts to go |
| P05 | 443 | 7.2% | 7.2% | +0.6 | 15% | 🟡 8 pts to go |
| P06M | 32303 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 53176 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 242 | 9.9% | 9.9% | +0.6 | 15% | 🟡 5 pts to go |
| P07 | 759 | 3.6% | 3.6% | +0.2 | 15% | ❌ 11 pts to go |
| P08 | 28712 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 71 | 4.2% | 4.2% | +3.1 | 15% | ❌ 11 pts to go |
| P10 | 2004 | 1.2% | 1.2% | -0.2 | 15% | ❌ 14 pts to go |
| P11 | 1809 | 1.3% | 1.3% | +0.1 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 229919 | 0.5% | 0.5% | -0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 8.7% | 8.7% | +3.1 | 15% | 🟡 6 pts to go |
| P01T | 201 | 12.9% | 12.9% | +2.0 | 25% | ❌ 12 pts to go |
| P01_GOLD | 629 | 28.9% | 28.9% | +0.0 | 25% | ✅ met |
| P02 | 474 | 23.8% | 23.8% | -1.6 | 15% | ✅ met |
| P03 | 275 | 21.5% | 21.5% | -0.3 | 15% | ✅ met |
| P04 | 4816 | 3.1% | 3.1% | -0.9 | 15% | ❌ 12 pts to go |
| P05 | 443 | 11.7% | 11.7% | +0.3 | 15% | 🟡 3 pts to go |
| P06M | 32303 | 0.9% | 0.9% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 53176 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 242 | 7.4% | 7.4% | +0.3 | 15% | 🟡 8 pts to go |
| P07 | 759 | 1.6% | 1.6% | -0.2 | 15% | ❌ 13 pts to go |
| P08 | 28712 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P09 | 71 | 2.8% | 2.8% | +1.3 | 15% | ❌ 12 pts to go |
| P10 | 2004 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1809 | 1.8% | 1.8% | +0.0 | 15% | ❌ 13 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 229919 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 2.3% | 2.3% | +0.7 | 20% | ❌ 18 pts to go |
| P01T | 201 | 3.0% | 3.0% | -0.1 | 20% | ❌ 17 pts to go |
| P01_GOLD | 629 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 474 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 275 | 1.5% | 1.5% | -0.4 | 20% | ❌ 18 pts to go |
| P04 | 4816 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P05 | 443 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 32303 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 242 | 1.7% | 1.7% | +0.3 | 20% | ❌ 18 pts to go |
| P07 | 759 | 0.3% | 0.3% | +0.1 | 20% | ❌ 20 pts to go |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 71 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2004 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1809 | 0.2% | 0.2% | +0.1 | 20% | ❌ 20 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 2.5% | 2.5% | +0.9 | 15% | ❌ 12 pts to go |
| P01T | 201 | 2.5% | 2.5% | -0.6 | 15% | ❌ 12 pts to go |
| P01_GOLD | 629 | 11.0% | 11.0% | +0.5 | 15% | 🟡 4 pts to go |
| P02 | 474 | 10.1% | 10.1% | -1.4 | 15% | 🟡 5 pts to go |
| P03 | 275 | 20.0% | 20.0% | -0.7 | 15% | ✅ met |
| P04 | 4816 | 1.9% | 1.9% | -0.5 | 15% | ❌ 13 pts to go |
| P05 | 443 | 2.9% | 2.9% | +0.1 | 15% | ❌ 12 pts to go |
| P06M | 32303 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P06T | 53176 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 242 | 4.1% | 4.1% | +0.2 | 15% | ❌ 11 pts to go |
| P07 | 759 | 1.8% | 1.8% | +0.6 | 15% | ❌ 13 pts to go |
| P08 | 28712 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P09 | 71 | 2.8% | 2.8% | +2.1 | 15% | ❌ 12 pts to go |
| P10 | 2004 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1809 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 229919 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 18.4% | 18.4% | +6.0 | 20% | 🟡 2 pts to go |
| P01T | 201 | 13.4% | 13.4% | -0.1 | 40% | ❌ 27 pts to go |
| P01_GOLD | 629 | 45.2% | 45.2% | -1.4 | 40% | ✅ met |
| P02 | 474 | 41.4% | 41.4% | -1.8 | 20% | ✅ met |
| P03 | 275 | 49.1% | 49.1% | +0.6 | 35% | ✅ met |
| P04 | 4816 | 11.4% | 11.4% | -3.5 | 20% | 🟡 9 pts to go |
| P05 | 443 | 15.3% | 15.3% | -0.3 | 20% | 🟡 5 pts to go |
| P06M | 32303 | 1.3% | 1.3% | +0.3 | 20% | ❌ 19 pts to go |
| P06T | 53176 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |
| P06 | 242 | 17.8% | 17.8% | -3.3 | 20% | 🟡 2 pts to go |
| P07 | 759 | 6.2% | 6.2% | +0.1 | 20% | ❌ 14 pts to go |
| P08 | 28712 | 0.9% | 0.9% | +0.1 | 20% | ❌ 19 pts to go |
| P09 | 71 | 12.7% | 12.7% | -8.4 | 20% | 🟡 7 pts to go |
| P10 | 2004 | 3.6% | 3.6% | -0.2 | 20% | ❌ 16 pts to go |
| P11 | 1809 | 3.0% | 3.0% | -0.2 | 20% | ❌ 17 pts to go |
| P12 | 11 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P13 | 229919 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 10.8% | 10.8% | -7.3 | n/a | no target |
| P01T | 201 | 0.0% | 0.0% | -0.4 | n/a | no target |
| P01_GOLD | 629 | 69.0% | 69.0% | -2.6 | 95% | ❌ 26 pts to go |
| P02 | 474 | 64.1% | 64.1% | -2.1 | 95% | ❌ 31 pts to go |
| P03 | 275 | 54.5% | 54.5% | -3.4 | 90% | ❌ 36 pts to go |
| P04 | 4816 | 20.7% | 20.7% | -5.8 | 85% | ❌ 64 pts to go |
| P05 | 443 | 38.8% | 38.8% | -0.1 | 75% | ❌ 36 pts to go |
| P06M | 32303 | 21.6% | 21.6% | -6.5 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 76.1% | 76.1% | -13.0 | 100% | ❌ 24 pts to go |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 3.9% | 3.9% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 10.8% | 10.8% | -7.3 | n/a | no target |
| P01T | 201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 629 | 71.7% | 71.7% | -1.8 | 100% | ❌ 28 pts to go |
| P02 | 474 | 66.2% | 66.2% | -2.0 | 100% | ❌ 34 pts to go |
| P03 | 275 | 56.0% | 56.0% | -4.5 | n/a | no target |
| P04 | 4816 | 21.2% | 21.2% | -5.8 | 95% | ❌ 74 pts to go |
| P05 | 443 | 36.6% | 36.6% | +2.0 | 80% | ❌ 43 pts to go |
| P06M | 32303 | 21.6% | 21.6% | -6.5 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 80.3% | 80.3% | -11.3 | 100% | ❌ 20 pts to go |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 4.1% | 4.1% | +0.1 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 82.3% | 82.3% | -2.0 | n/a | no target |
| P01T | 201 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 629 | 55.6% | 55.6% | +3.3 | 85% | ❌ 29 pts to go |
| P02 | 474 | 62.7% | 62.7% | +3.5 | 90% | ❌ 27 pts to go |
| P03 | 275 | 46.5% | 46.5% | +2.5 | 85% | ❌ 38 pts to go |
| P04 | 4816 | 37.8% | 37.8% | +8.7 | 90% | ❌ 52 pts to go |
| P05 | 443 | 32.5% | 32.5% | -0.4 | 75% | ❌ 42 pts to go |
| P06M | 32303 | 83.1% | 83.1% | -1.2 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 64.8% | 64.8% | -17.0 | 95% | ❌ 30 pts to go |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 3.8% | 3.8% | +0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 52.6% | 52.6% | -13.3 | n/a | no target |
| P01T | 201 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 629 | 55.0% | 55.0% | +3.0 | 85% | ❌ 30 pts to go |
| P02 | 474 | 56.1% | 56.1% | +2.7 | 90% | ❌ 34 pts to go |
| P03 | 275 | 46.5% | 46.5% | +2.1 | 85% | ❌ 38 pts to go |
| P04 | 4816 | 33.5% | 33.5% | +8.9 | 90% | ❌ 56 pts to go |
| P05 | 443 | 40.9% | 40.9% | -1.8 | 75% | ❌ 34 pts to go |
| P06M | 32303 | 58.9% | 58.9% | -10.3 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | +1.0 | 95% | ❌ 94 pts to go |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 3.0% | 3.0% | +0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 97.2% | 97.2% | +2.0 | n/a | no target |
| P01T | 201 | 94.5% | 94.5% | -1.6 | n/a | no target |
| P01_GOLD | 629 | 86.5% | 86.6% | +1.0 | 100% | ❌ 14 pts to go |
| P02 | 474 | 79.1% | 79.1% | +1.5 | 100% | ❌ 21 pts to go |
| P03 | 275 | 90.5% | 90.5% | -2.0 | n/a | no target |
| P04 | 4816 | 53.3% | 53.3% | +2.7 | 95% | ❌ 42 pts to go |
| P05 | 443 | 78.1% | 78.1% | +0.8 | 95% | ❌ 17 pts to go |
| P06M | 32303 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 53176 | 97.8% | 97.8% | +3.3 | n/a | no target |
| P06 | 242 | 20.2% | 20.2% | -0.2 | n/a | no target |
| P07 | 759 | 10.4% | 10.4% | +0.2 | n/a | no target |
| P08 | 28712 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 71 | 93.0% | 93.0% | -5.2 | 100% | 🟡 7 pts to go |
| P10 | 2004 | 71.1% | 71.1% | +0.5 | n/a | no target |
| P11 | 1809 | 70.4% | 70.4% | +0.6 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 98.4% | 98.4% | -1.2 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 97.2% | 97.2% | +2.0 | n/a | no target |
| P01T | 201 | 94.5% | 94.5% | -1.6 | n/a | no target |
| P01_GOLD | 629 | 89.7% | 89.8% | +1.0 | 100% | ❌ 10 pts to go |
| P02 | 474 | 80.4% | 80.4% | +1.6 | 100% | ❌ 20 pts to go |
| P03 | 275 | 91.3% | 91.3% | -1.9 | n/a | no target |
| P04 | 4816 | 55.8% | 55.8% | +1.8 | 95% | ❌ 39 pts to go |
| P05 | 443 | 89.8% | 89.8% | +0.5 | 70% | ✅ met |
| P06M | 32303 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 53176 | 97.8% | 97.8% | +3.3 | n/a | no target |
| P06 | 242 | 20.2% | 20.2% | -0.2 | n/a | no target |
| P07 | 759 | 10.4% | 10.4% | +0.2 | n/a | no target |
| P08 | 28712 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 71 | 93.0% | 93.0% | -5.2 | 100% | 🟡 7 pts to go |
| P10 | 2004 | 71.1% | 71.1% | +0.5 | n/a | no target |
| P11 | 1809 | 70.5% | 70.5% | +0.6 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 629 | 15.4% | 15.4% | -1.5 | 60% | ❌ 45 pts to go · rows from a source that publishes bids: 353 rows, 27.5% filled |
| P02 | 474 | 9.5% | 9.5% | -1.2 | n/a | no target · rows from a source that publishes bids: 289 rows, 15.6% filled |
| P03 | 275 | 11.6% | 11.6% | -2.3 | n/a | no target · rows from a source that publishes bids: 136 rows, 23.5% filled |
| P04 | 4816 | 1.2% | 1.2% | -0.5 | n/a | no target · rows from a source that publishes bids: 886 rows, 6.4% filled |
| P05 | 443 | 3.4% | 3.4% | +0.8 | n/a | no target · rows from a source that publishes bids: 67 rows, 22.4% filled |
| P06M | 32303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53176 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 5.6% | 5.6% | +1.2 | n/a | no target · rows from a source that publishes bids: 63 rows, 6.3% filled |
| P10 | 2004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1809 | 0.4% | 0.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 68 rows, 11.8% filled |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 11 rows, 0.0% filled |
| P13 | 229919 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 201 | 0.0% | 97.0% | +0.0 | n/a | no target |
| P01_GOLD | 629 | 51.8% | 83.6% | -1.6 | 90% | ❌ 38 pts to go |
| P02 | 474 | 51.7% | 87.8% | -1.7 | 90% | ❌ 38 pts to go |
| P03 | 275 | 43.6% | 82.5% | -2.3 | 90% | ❌ 46 pts to go |
| P04 | 4816 | 14.8% | 94.8% | -4.8 | 90% | ❌ 75 pts to go |
| P05 | 443 | 0.7% | 79.9% | +0.7 | 90% | ❌ 89 pts to go |
| P06M | 32303 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 53176 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 11.3% | 18.3% | +8.4 | 90% | ❌ 79 pts to go |
| P10 | 2004 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1809 | 2.2% | 97.6% | +0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 201 | 1.0% | 98.0% | +0.1 | n/a | no target |
| P01_GOLD | 629 | 26.4% | 58.2% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 474 | 51.7% | 87.8% | -0.7 | n/a | no target |
| P03 | 275 | 24.4% | 63.3% | -0.8 | n/a | no target |
| P04 | 4816 | 16.1% | 96.1% | -5.3 | n/a | no target |
| P05 | 443 | 0.5% | 79.7% | +0.0 | n/a | no target |
| P06M | 32303 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 53176 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 2.8% | 9.9% | -37.6 | n/a | no target |
| P10 | 2004 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1809 | 2.3% | 97.7% | +0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 201 | 3.0% | 100.0% | +0.8 | n/a | no target |
| P01_GOLD | 629 | 51.4% | 83.1% | -0.6 | 95% | ❌ 44 pts to go |
| P02 | 474 | 57.2% | 93.2% | -0.9 | n/a | no target |
| P03 | 275 | 46.2% | 85.1% | -4.2 | n/a | no target |
| P04 | 4816 | 16.6% | 96.6% | -5.6 | n/a | no target |
| P05 | 443 | 6.3% | 85.6% | +1.3 | n/a | no target |
| P06M | 32303 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 53176 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 242 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 759 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28712 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 16.9% | 23.9% | -43.5 | n/a | no target |
| P10 | 2004 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1809 | 2.3% | 97.8% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 229919 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 201 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 629 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 474 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4816 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 443 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 32303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 53176 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 242 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 759 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 28712 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2004 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1809 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 229919 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 201 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 629 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 474 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4816 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 443 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 32303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 53176 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 242 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 759 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 28712 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2004 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1809 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 229919 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 435 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 201 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 629 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 474 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4816 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 443 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 32303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 53176 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 242 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 759 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 28712 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2004 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1809 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 229919 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

