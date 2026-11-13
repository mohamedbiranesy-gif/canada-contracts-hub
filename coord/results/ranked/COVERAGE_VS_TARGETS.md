# Coverage vs the downstream team's targets — 2026-11-13

Benchmarks (field × package with a numeric target): **90 of 438 met** (20.5%); 63 within 10 points; 285 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 391, P01T 206, P01_GOLD 654, P02 490, P03 277, P04 4832, P05 427, P06M 29627, P06T 55379, P06 251, P07 782, P08 29395, P09 276, P10R 0, P10 2055, P11 1812, P12 11, P13 200003

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 10.2% | 7 | vendor GST/HST number (370 rows) |
| P01T | 206 | 1.0% | 32.5% | 8 | payment terms (162 rows) |
| P01_GOLD | 654 | 22.8% | 69.0% | 9 | payment terms (249 rows) |
| P02 | 490 | 7.1% | 52.9% | 9 | PO rule (381 rows) |
| P03 | 277 | 14.8% | 54.5% | 9 | PO rule (143 rows) |
| P04 | 4832 | 1.0% | 12.7% | 7 | PO rule (4632 rows) |
| P05 | 427 | 0.9% | 16.9% | 7 | payment terms (356 rows) |
| P06M | 29627 | 0.0% | 2.4% | 7 | PO rule (29243 rows) |
| P06T | 55379 | 0.1% | 13.3% | 7 | PO rule (55059 rows) |
| P06 | 251 | 0.0% | 9.2% | 6 | reference to quote (PO / contract / vendor id) (234 rows) |
| P07 | 782 | 0.0% | 2.6% | 6 | PO rule (747 rows) |
| P08 | 29395 | 0.0% | 1.3% | 6 | PO rule (29145 rows) |
| P09 | 276 | 1.4% | 42.0% | 8 | payment terms (257 rows) |
| P10 | 2055 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2055 rows) |
| P11 | 1812 | 0.1% | 7.7% | 6 | PO rule (1749 rows) |
| P12 | 11 | 0.0% | 36.4% | 8 | PO rule (11 rows) |
| P13 | 200003 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (200003 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 391 | 11 | 71 | 309 | 0 | 0 | 66 |
| P01T | 206 | 26 | 33 | 147 | 0 | 0 | 66 |
| P01_GOLD | 654 | 253 | 172 | 229 | 0 | 0 | 81 |
| P02 | 490 | 0 | 191 | 299 | 0 | 0 | 66 |
| P03 | 277 | 0 | 0 | 265 | 12 | 0 | 57 |
| P04 | 4832 | 0 | 0 | 4164 | 668 | 0 | 46 |
| P05 | 427 | 16 | 28 | 370 | 13 | 0 | 51 |
| P06M | 29627 | 0 | 19 | 29558 | 50 | 0 | 46 |
| P06T | 55379 | 0 | 26 | 37970 | 17383 | 0 | 38 |
| P06 | 251 | 15 | 32 | 204 | 0 | 0 | 67 |
| P07 | 782 | 0 | 17 | 747 | 18 | 0 | 55 |
| P08 | 29395 | 0 | 0 | 26615 | 2780 | 0 | 46 |
| P09 | 276 | 4 | 10 | 261 | 1 | 0 | 53 |
| P10 | 2055 | 2 | 10 | 1390 | 653 | 0 | 41 |
| P11 | 1812 | 7 | 12 | 39 | 0 | 1754 | 23 |
| P12 | 11 | 0 | 0 | 11 | 0 | 0 | 51 |
| P13 | 200003 | 12 | 66 | 199912 | 13 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 391 | 288 | 73.7% | tax treatment (74) |
| P01T | 206 | 123 | 59.7% | bill-to legal name and address (68) |
| P01_GOLD | 654 | 491 | 75.1% | bill-to legal name and address (96) |
| P02 | 490 | 332 | 67.8% | the buyer's PO / reference rule (85) |
| P03 | 277 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (277) |
| P04 | 4832 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4832) |
| P05 | 427 | 45 | 10.5% | a confirmed invoicing / AP or finance channel (339) |
| P06M | 29627 | 321 | 1.1% | a confirmed invoicing / AP or finance channel (29221) |
| P06T | 55379 | 322 | 0.6% | a confirmed invoicing / AP or finance channel (54625) |
| P06 | 251 | 44 | 17.5% | the buyer's PO / reference rule (109) |
| P07 | 782 | 47 | 6.0% | the buyer's PO / reference rule (324) |
| P08 | 29395 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (29395) |
| P09 | 276 | 38 | 13.8% | a confirmed invoicing / AP or finance channel (227) |
| P10 | 2055 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (1981) |
| P11 | 1812 | 19 | 1.0% | a confirmed invoicing / AP or finance channel (1754) |
| P12 | 11 | 2 | 18.2% | a confirmed invoicing / AP or finance channel (9) |
| P13 | 200003 | 43 | 0.0% | a confirmed invoicing / AP or finance channel (197514) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 391 | 9 | 2.3% | 7 | 0 | the vendor's GST/HST number (BN9) (370) |
| P01T | 206 | 81 | 39.3% | 2 | 0 | the vendor's GST/HST number (BN9) (76) |
| P01_GOLD | 654 | 407 | 62.2% | 11 | 0 | the vendor's GST/HST number (BN9) (171) |
| P02 | 490 | 215 | 43.9% | 22 | 0 | the vendor's GST/HST number (BN9) (224) |
| P03 | 277 | 17 | 6.1% | 0 | 134 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (106) |
| P04 | 4832 | 43 | 0.9% | 7 | 906 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3819) |
| P05 | 427 | 20 | 4.7% | 8 | 128 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (203) |
| P06M | 29627 | 8 | 0.0% | 14 | 704 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (28412) |
| P06T | 55379 | 352 | 0.6% | 15 | 18055 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (36489) |
| P06 | 251 | 19 | 7.6% | 47 | 0 | the vendor's GST/HST number (BN9) (116) |
| P07 | 782 | 14 | 1.8% | 135 | 36 | the vendor's GST/HST number (BN9) (387) |
| P08 | 29395 | 4 | 0.0% | 13 | 7019 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22318) |
| P09 | 276 | 36 | 13.0% | 0 | 107 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (108) |
| P10 | 2055 | 5 | 0.2% | 13 | 285 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1675) |
| P11 | 1812 | 7 | 0.4% | 2 | 0 | a confirmed invoicing / AP or finance channel (1738) |
| P12 | 11 | 1 | 9.1% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 200003 | 22 | 0.0% | 1184 | 78929 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (118403) |
| **all** | 326868 | 1260 | 0.4% | 1480 | 106308 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 380 | 0 | 0 | 0 | 279 | 10 | 0 | 325 | 347 | 1 |
| P01T | 180 | 0 | 0 | 0 | 116 | 61 | 29 | 149 | 163 | 2 |
| P01_GOLD | 401 | 0 | 0 | 0 | 39 | 78 | 30 | 222 | 264 | 3 |
| P02 | 490 | 0 | 490 | 0 | 59 | 57 | 14 | 381 | 305 | 2 |
| P03 | 277 | 0 | 277 | 0 | 28 | 45 | 26 | 143 | 152 | 2 |
| P04 | 4832 | 0 | 4832 | 0 | 2685 | 1501 | 1013 | 4632 | 4387 | 32 |
| P05 | 411 | 0 | 359 | 0 | 87 | 99 | 40 | 343 | 358 | 7 |
| P06M | 29627 | 0 | 29627 | 0 | 23305 | 1743 | 128 | 29243 | 28982 | 19 |
| P06T | 55379 | 0 | 55379 | 0 | 49823 | 34531 | 22493 | 55059 | 54590 | 391 |
| P06 | 236 | 0 | 0 | 0 | 128 | 69 | 42 | 184 | 208 | 5 |
| P07 | 782 | 0 | 782 | 0 | 532 | 304 | 98 | 747 | 744 | 5 |
| P08 | 29395 | 0 | 29395 | 0 | 23254 | 12699 | 4273 | 29145 | 28789 | 187 |
| P09 | 272 | 0 | 253 | 0 | 12 | 67 | 1 | 246 | 259 | 7 |
| P10 | 2053 | 0 | 2023 | 0 | 1061 | 1111 | 948 | 1992 | 1955 | 16 |
| P11 | 1805 | 1754 | 1709 | 0 | 932 | 1224 | 546 | 1749 | 1742 | 21 |
| P12 | 11 | 0 | 10 | 0 | 0 | 3 | 0 | 11 | 11 | 2 |
| P13 | 199991 | 0 | 199532 | 0 | 169525 | 120977 | 19 | 199643 | 198747 | 70 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 57.2% | 95% | 75596 |
| buyer_logo_url | P13 | 72.8% | 95% | 44468 |
| buyer_legal_name_as_published | P13 | 39.5% | 60% | 40976 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 39944 |
| ap_system_hint | P13 | 0.3% | 20% | 39372 |
| buyer_bn_as_published | P13 | 10.5% | 30% | 39020 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 29835 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 29794 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 28854 |
| vendor_registered_address | P08 | 31.8% | 70% | 11229 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11061 |
| ap_system_hint | P06T | 0.6% | 20% | 10746 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8214 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8203 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 7939 |
| buyer_phone | P08 | 70.9% | 95% | 7087 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 5912 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5867 |
| ap_system_hint | P08 | 0.7% | 20% | 5659 |
| ap_system_hint | P06M | 0.9% | 20% | 5651 |
| vendor_emails | P08 | 55.8% | 75% | 5634 |
| vendor_bn9 | P08 | 31.4% | 50% | 5480 |
| buyer_legal_name_as_published | P08 | 56.8% | 75% | 5351 |
| vendor_phone | P08 | 67.2% | 85% | 5246 |
| vendor_trading_name | P08 | 33.9% | 50% | 4720 |
| buyer_esignature_preference | P06M | 0.3% | 15% | 4347 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 4314 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 4309 |
| buyer_tax_exempt_status | P06M | 0.5% | 15% | 4284 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 4233 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 4219 |
| invoice_reference_hint | P08 | 12.1% | 25% | 3783 |
| buyer_bn_as_published | P08 | 22.5% | 35% | 3662 |
| average_contract_duration_days | P04 | 14.6% | 90% | 3644 |
| currency | P04 | 21.0% | 95% | 3577 |
| ap_phone | P04 | 14.9% | 85% | 3389 |
| commodity_codes | P04 | 16.5% | 85% | 3311 |
| award_or_notice_id | P04 | 18.5% | 85% | 3215 |
| contract_value | P04 | 20.6% | 85% | 3111 |
| invoice_mailing_address | P04 | 14.9% | 75% | 2904 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 94.6% | 94.6% | +1.4 | 50% | ✅ met |
| P01T | 206 | 95.1% | 95.1% | -0.5 | 50% | ✅ met |
| P01_GOLD | 654 | 92.4% | 94.6% | +0.2 | 95% | 🟡 3 pts to go |
| P02 | 490 | 75.7% | 77.1% | +0.7 | 95% | ❌ 19 pts to go |
| P03 | 277 | 82.7% | 85.9% | +1.1 | 95% | ❌ 12 pts to go |
| P04 | 4832 | 43.5% | 44.9% | +11.7 | 90% | ❌ 46 pts to go |
| P05 | 427 | 40.3% | 43.3% | +0.7 | 70% | ❌ 30 pts to go |
| P06M | 29627 | 93.8% | 93.8% | +0.6 | n/a | no target |
| P06T | 55379 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06 | 251 | 33.1% | 33.1% | -2.3 | 30% | ✅ met |
| P07 | 782 | 13.4% | 13.4% | -0.8 | 30% | ❌ 17 pts to go |
| P08 | 29395 | 12.1% | 12.1% | -0.1 | 25% | ❌ 13 pts to go |
| P09 | 276 | 98.9% | 99.6% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2055 | 3.1% | 3.1% | -0.2 | 25% | ❌ 22 pts to go |
| P11 | 1812 | 54.9% | 55.6% | +0.6 | 60% | 🟡 5 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 200003 | 99.6% | 99.6% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 654 | 5.5% | 5.5% | -0.2 | 50% | ❌ 44 pts to go |
| P02 | 490 | 5.9% | 5.9% | -0.3 | 50% | ❌ 44 pts to go |
| P03 | 277 | 1.8% | 1.8% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4832 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 29627 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 92.3% | 92.3% | +2.7 | n/a | no target |
| P01T | 206 | 77.7% | 77.7% | -2.2 | 50% | ✅ met |
| P01_GOLD | 654 | 68.5% | 68.5% | +1.2 | 85% | ❌ 16 pts to go |
| P02 | 490 | 67.6% | 67.6% | +1.4 | 90% | ❌ 22 pts to go |
| P03 | 277 | 62.5% | 62.5% | +2.0 | 85% | ❌ 22 pts to go |
| P04 | 4832 | 41.5% | 41.5% | +12.4 | 85% | ❌ 44 pts to go |
| P05 | 427 | 30.9% | 30.9% | +1.0 | 60% | ❌ 29 pts to go |
| P06M | 29627 | 93.6% | 93.6% | +0.6 | n/a | no target |
| P06T | 55379 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06 | 251 | 6.8% | 6.8% | +0.4 | n/a | no target |
| P07 | 782 | 9.0% | 9.0% | -0.1 | n/a | no target |
| P08 | 29395 | 11.3% | 11.3% | +0.0 | n/a | no target |
| P09 | 276 | 95.7% | 95.7% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 52.2% | 52.2% | +0.7 | 60% | 🟡 8 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 654 | 49.5% | 49.5% | -2.2 | 80% | ❌ 30 pts to go |
| P02 | 490 | 55.3% | 55.3% | -2.8 | 60% | 🟡 5 pts to go |
| P03 | 277 | 48.4% | 48.4% | -2.0 | 80% | ❌ 32 pts to go |
| P04 | 4832 | 17.8% | 17.8% | -6.2 | 50% | ❌ 32 pts to go |
| P05 | 427 | 13.6% | 13.6% | +1.0 | 40% | ❌ 26 pts to go |
| P06M | 29627 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 81.2% | 81.2% | +0.1 | 50% | ✅ met |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 3.3% | 3.3% | +0.0 | 40% | ❌ 37 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 654 | 58.4% | 58.4% | -2.5 | 85% | ❌ 27 pts to go |
| P02 | 490 | 55.3% | 55.3% | -2.8 | 90% | ❌ 35 pts to go |
| P03 | 277 | 57.0% | 57.0% | -2.4 | 85% | ❌ 28 pts to go |
| P04 | 4832 | 18.5% | 18.5% | -6.4 | 85% | ❌ 66 pts to go |
| P05 | 427 | 21.3% | 21.3% | +0.9 | 50% | ❌ 29 pts to go |
| P06M | 29627 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 3.6% | 3.6% | +0.0 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 654 | 12.1% | 12.1% | -0.5 | 60% | ❌ 48 pts to go |
| P02 | 490 | 6.9% | 6.9% | -0.4 | 50% | ❌ 43 pts to go |
| P03 | 277 | 8.3% | 8.3% | -0.3 | 50% | ❌ 42 pts to go |
| P04 | 4832 | 1.4% | 1.4% | -0.5 | 40% | ❌ 39 pts to go |
| P05 | 427 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 29627 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 3.6% | 3.6% | +0.0 | 50% | ❌ 46 pts to go |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 654 | 34.4% | 34.4% | -1.5 | 80% | ❌ 46 pts to go |
| P02 | 490 | 50.6% | 50.6% | -2.4 | 90% | ❌ 39 pts to go |
| P03 | 277 | 32.5% | 32.5% | -1.3 | 80% | ❌ 48 pts to go |
| P04 | 4832 | 16.5% | 16.5% | -5.7 | 85% | ❌ 68 pts to go |
| P05 | 427 | 7.5% | 7.5% | +1.1 | 50% | ❌ 42 pts to go |
| P06M | 29627 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 73.2% | 73.2% | +0.1 | 95% | ❌ 22 pts to go |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 2.6% | 2.6% | +0.0 | 50% | ❌ 47 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 654 | 7.8% | 7.8% | -0.3 | 50% | ❌ 42 pts to go |
| P02 | 490 | 5.9% | 5.9% | -0.3 | 50% | ❌ 44 pts to go |
| P03 | 277 | 2.5% | 2.5% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 4832 | 0.4% | 0.4% | -0.2 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 29627 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 206 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 654 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 490 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4832 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 29627 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55379 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 251 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 782 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29395 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2055 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1812 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 5.4% | 5.4% | -1.0 | 70% | ❌ 65 pts to go |
| P01T | 206 | 54.9% | 54.9% | -5.4 | 60% | 🟡 5 pts to go |
| P01_GOLD | 654 | 71.6% | 71.6% | -3.2 | 90% | ❌ 18 pts to go |
| P02 | 490 | 51.8% | 51.8% | -2.5 | 85% | ❌ 33 pts to go |
| P03 | 277 | 63.9% | 63.9% | -3.0 | 90% | ❌ 26 pts to go |
| P04 | 4832 | 28.2% | 28.2% | -10.0 | 75% | ❌ 47 pts to go |
| P05 | 427 | 54.6% | 54.6% | -0.1 | 50% | ✅ met |
| P06M | 29627 | 2.9% | 2.9% | +0.0 | n/a | no target |
| P06T | 55379 | 65.0% | 65.0% | +0.5 | n/a | no target |
| P06 | 251 | 41.8% | 41.8% | -0.3 | 40% | ✅ met |
| P07 | 782 | 32.1% | 32.1% | +0.0 | 50% | ❌ 18 pts to go |
| P08 | 29395 | 31.4% | 31.4% | +0.8 | 50% | ❌ 19 pts to go |
| P09 | 276 | 56.2% | 56.2% | -0.5 | 80% | ❌ 24 pts to go |
| P10 | 2055 | 38.7% | 38.7% | -0.1 | 40% | 🟡 1 pts to go |
| P11 | 1812 | 53.5% | 53.5% | -1.1 | 60% | 🟡 6 pts to go |
| P12 | 11 | 54.5% | 54.5% | +9.0 | 85% | ❌ 30 pts to go |
| P13 | 200003 | 44.8% | 44.8% | +0.0 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 42.2% | 42.2% | -4.4 | n/a | no target |
| P01T | 206 | 55.3% | 55.3% | -4.5 | n/a | no target |
| P01_GOLD | 654 | 74.0% | 74.0% | +1.1 | 95% | ❌ 21 pts to go |
| P02 | 490 | 75.1% | 75.1% | +0.5 | 95% | ❌ 20 pts to go |
| P03 | 277 | 70.8% | 70.8% | +1.3 | 95% | ❌ 24 pts to go |
| P04 | 4832 | 54.0% | 54.0% | +0.9 | 95% | ❌ 41 pts to go |
| P05 | 427 | 58.8% | 58.8% | +0.7 | 70% | ❌ 11 pts to go |
| P06M | 29627 | 39.0% | 39.0% | -2.3 | n/a | no target |
| P06T | 55379 | 68.5% | 68.5% | +1.0 | n/a | no target |
| P06 | 251 | 38.2% | 38.2% | +0.0 | 80% | ❌ 42 pts to go |
| P07 | 782 | 31.5% | 31.5% | +0.5 | 70% | ❌ 38 pts to go |
| P08 | 29395 | 31.8% | 31.8% | +2.1 | 70% | ❌ 38 pts to go |
| P09 | 276 | 86.2% | 86.2% | +0.0 | 100% | ❌ 14 pts to go |
| P10 | 2055 | 38.9% | 38.9% | -0.3 | 70% | ❌ 31 pts to go |
| P11 | 1812 | 58.5% | 58.5% | -0.1 | 75% | ❌ 16 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 40.5% | 40.5% | +0.3 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 22.0% | 22.0% | -0.1 | n/a | no target |
| P01T | 206 | 58.7% | 58.7% | -6.8 | n/a | no target |
| P01_GOLD | 654 | 50.6% | 50.6% | +1.8 | 60% | 🟡 9 pts to go |
| P02 | 490 | 58.0% | 58.0% | +2.2 | 60% | 🟡 2 pts to go |
| P03 | 277 | 54.9% | 54.9% | +2.6 | 60% | 🟡 5 pts to go |
| P04 | 4832 | 54.2% | 54.2% | +11.6 | 55% | 🟡 1 pts to go |
| P05 | 427 | 23.4% | 23.4% | +0.7 | 50% | ❌ 27 pts to go |
| P06M | 29627 | 10.9% | 10.9% | +1.4 | n/a | no target |
| P06T | 55379 | 70.1% | 70.1% | +2.2 | n/a | no target |
| P06 | 251 | 50.6% | 50.6% | +2.0 | n/a | no target |
| P07 | 782 | 39.3% | 39.3% | -0.3 | 55% | ❌ 16 pts to go |
| P08 | 29395 | 33.9% | 33.9% | +0.9 | 50% | ❌ 16 pts to go |
| P09 | 276 | 72.1% | 72.1% | +0.1 | 70% | ✅ met |
| P10 | 2055 | 47.6% | 47.6% | -0.5 | 55% | 🟡 7 pts to go |
| P11 | 1812 | 59.4% | 59.4% | +0.2 | 50% | ✅ met |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 200003 | 2.9% | 2.9% | -0.3 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 24.8% | 24.8% | -8.5 | n/a | no target |
| P01T | 206 | 76.7% | 76.7% | -2.8 | n/a | no target |
| P01_GOLD | 654 | 48.0% | 48.0% | -2.4 | 70% | ❌ 22 pts to go |
| P02 | 490 | 53.9% | 53.9% | -2.9 | 70% | ❌ 16 pts to go |
| P03 | 277 | 48.4% | 48.4% | -2.0 | 70% | ❌ 22 pts to go |
| P04 | 4832 | 49.3% | 49.3% | -5.6 | 65% | ❌ 16 pts to go |
| P05 | 427 | 28.8% | 28.8% | -0.3 | 60% | ❌ 31 pts to go |
| P06M | 29627 | 23.8% | 23.8% | -3.6 | n/a | no target |
| P06T | 55379 | 86.9% | 86.9% | +4.2 | n/a | no target |
| P06 | 251 | 70.5% | 70.5% | +1.2 | 40% | ✅ met |
| P07 | 782 | 66.4% | 66.4% | +1.4 | 85% | ❌ 19 pts to go |
| P08 | 29395 | 67.2% | 67.2% | +3.2 | 85% | ❌ 18 pts to go |
| P09 | 276 | 56.2% | 56.2% | -0.2 | 85% | ❌ 29 pts to go |
| P10 | 2055 | 65.1% | 65.1% | -1.0 | 85% | ❌ 20 pts to go |
| P11 | 1812 | 68.3% | 68.3% | +0.2 | 75% | 🟡 7 pts to go |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 200003 | 90.8% | 90.8% | -1.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 28.9% | 28.9% | -8.9 | n/a | no target |
| P01T | 206 | 98.1% | 98.1% | -0.2 | n/a | no target |
| P01_GOLD | 654 | 75.4% | 75.4% | -3.2 | 90% | ❌ 15 pts to go |
| P02 | 490 | 78.4% | 78.4% | -3.4 | 90% | ❌ 12 pts to go |
| P03 | 277 | 81.6% | 81.6% | -3.7 | 90% | 🟡 8 pts to go |
| P04 | 4832 | 70.9% | 70.9% | -11.9 | 85% | ❌ 14 pts to go |
| P05 | 427 | 44.5% | 44.5% | +0.0 | 70% | ❌ 26 pts to go |
| P06M | 29627 | 29.2% | 29.2% | -3.8 | n/a | no target |
| P06T | 55379 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 251 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 782 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 29395 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 276 | 77.5% | 77.5% | -0.3 | 100% | ❌ 22 pts to go |
| P10 | 2055 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1812 | 97.5% | 97.5% | -0.5 | 100% | 🟡 2 pts to go |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 200003 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 13.6% | 13.6% | -2.5 | n/a | no target |
| P01T | 206 | 53.9% | 53.9% | -5.9 | n/a | no target |
| P01_GOLD | 654 | 41.4% | 41.4% | -2.0 | 70% | ❌ 29 pts to go |
| P02 | 490 | 45.5% | 45.5% | -1.7 | 75% | ❌ 30 pts to go |
| P03 | 277 | 43.7% | 43.7% | -1.0 | 75% | ❌ 31 pts to go |
| P04 | 4832 | 35.1% | 35.1% | -3.6 | 70% | ❌ 35 pts to go |
| P05 | 427 | 21.5% | 21.5% | +0.2 | 55% | ❌ 34 pts to go |
| P06M | 29627 | 6.4% | 6.4% | +0.5 | n/a | no target |
| P06T | 55379 | 42.1% | 42.1% | -5.3 | n/a | no target |
| P06 | 251 | 51.4% | 51.4% | +0.3 | n/a | no target |
| P07 | 782 | 53.6% | 53.6% | +0.9 | 70% | ❌ 16 pts to go |
| P08 | 29395 | 55.8% | 55.8% | +1.0 | 75% | ❌ 19 pts to go |
| P09 | 276 | 46.7% | 46.7% | -0.2 | 85% | ❌ 38 pts to go |
| P10 | 2055 | 44.4% | 44.4% | +0.0 | 80% | ❌ 36 pts to go |
| P11 | 1812 | 51.7% | 51.7% | -1.6 | 70% | ❌ 18 pts to go |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 200003 | 5.9% | 5.9% | +0.4 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 28.4% | 28.4% | -9.4 | n/a | no target |
| P01T | 206 | 96.1% | 96.1% | -0.4 | n/a | no target |
| P01_GOLD | 654 | 69.9% | 69.9% | -3.0 | 90% | ❌ 20 pts to go |
| P02 | 490 | 73.3% | 73.3% | -3.4 | 90% | ❌ 17 pts to go |
| P03 | 277 | 78.3% | 78.3% | -3.7 | 90% | ❌ 12 pts to go |
| P04 | 4832 | 66.7% | 66.7% | -11.0 | 85% | ❌ 18 pts to go |
| P05 | 427 | 43.1% | 43.1% | +0.2 | 75% | ❌ 32 pts to go |
| P06M | 29627 | 28.8% | 28.8% | -4.1 | n/a | no target |
| P06T | 55379 | 97.8% | 97.8% | -0.5 | n/a | no target |
| P06 | 251 | 92.0% | 92.0% | +2.0 | n/a | no target |
| P07 | 782 | 94.2% | 94.2% | +2.5 | 100% | 🟡 6 pts to go |
| P08 | 29395 | 92.8% | 92.8% | +5.5 | 100% | 🟡 7 pts to go |
| P09 | 276 | 66.3% | 66.3% | -0.2 | n/a | no target |
| P10 | 2055 | 90.0% | 90.0% | -0.3 | 100% | 🟡 10 pts to go |
| P11 | 1812 | 90.2% | 90.2% | +0.0 | n/a | no target |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 200003 | 69.3% | 69.3% | -0.5 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 32.5% | 32.5% | -4.4 | n/a | no target · QC vendors: 55 rows, 100.0% filled |
| P01T | 206 | 22.3% | 22.3% | +2.6 | n/a | no target · QC vendors: 34 rows, 88.2% filled |
| P01_GOLD | 654 | 45.6% | 45.6% | +2.1 | 95% | ❌ 49 pts to go · QC vendors: 49 rows, 98.0% filled |
| P02 | 490 | 57.6% | 57.6% | +1.6 | 95% | ❌ 37 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 277 | 45.1% | 45.1% | +2.2 | 95% | ❌ 50 pts to go · QC vendors: 19 rows, 100.0% filled |
| P04 | 4832 | 39.0% | 39.0% | +6.6 | 95% | ❌ 56 pts to go · QC vendors: 595 rows, 97.8% filled |
| P05 | 427 | 14.5% | 14.5% | +0.5 | n/a | no target · QC vendors: 37 rows, 100.0% filled |
| P06M | 29627 | 34.8% | 34.8% | -2.7 | n/a | no target · QC vendors: 7558 rows, 99.9% filled |
| P06T | 55379 | 38.0% | 38.0% | +7.4 | n/a | no target · QC vendors: 21426 rows, 96.1% filled |
| P06 | 251 | 6.8% | 6.8% | -0.3 | n/a | no target · QC vendors: 10 rows, 60.0% filled |
| P07 | 782 | 6.8% | 6.8% | -0.1 | n/a | no target · QC vendors: 44 rows, 79.5% filled |
| P08 | 29395 | 7.1% | 7.1% | +0.1 | n/a | no target · QC vendors: 1787 rows, 92.8% filled |
| P09 | 276 | 73.6% | 73.6% | +0.1 | 95% | ❌ 21 pts to go · QC vendors: 101 rows, 100.0% filled |
| P10 | 2055 | 15.9% | 15.9% | +0.2 | n/a | no target · QC vendors: 194 rows, 95.4% filled |
| P11 | 1812 | 20.8% | 20.8% | +1.2 | n/a | no target · QC vendors: 324 rows, 94.1% filled |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 200003 | 22.0% | 22.0% | -0.2 | n/a | no target · QC vendors: 44089 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 41.9% | 41.9% | -4.3 | n/a | no target · vendors with a registry record: 164 rows, 100.0% filled |
| P01T | 206 | 55.3% | 55.3% | -4.5 | n/a | no target · vendors with a registry record: 114 rows, 100.0% filled |
| P01_GOLD | 654 | 81.7% | 81.7% | +0.8 | 100% | ❌ 18 pts to go · vendors with a registry record: 534 rows, 100.0% filled |
| P02 | 490 | 78.8% | 78.8% | +0.4 | 100% | ❌ 21 pts to go · vendors with a registry record: 386 rows, 100.0% filled |
| P03 | 277 | 79.1% | 79.1% | +0.9 | 100% | ❌ 21 pts to go · vendors with a registry record: 219 rows, 100.0% filled |
| P04 | 4832 | 54.7% | 54.7% | +0.7 | 100% | ❌ 45 pts to go · vendors with a registry record: 2642 rows, 100.0% filled |
| P05 | 427 | 63.0% | 63.0% | +0.2 | n/a | no target · vendors with a registry record: 269 rows, 100.0% filled |
| P06M | 29627 | 39.0% | 39.0% | -2.2 | n/a | no target · vendors with a registry record: 11549 rows, 100.0% filled |
| P06T | 55379 | 68.6% | 68.6% | +1.0 | n/a | no target · vendors with a registry record: 37970 rows, 100.0% filled |
| P06 | 251 | 39.0% | 39.0% | -0.3 | n/a | no target · vendors with a registry record: 98 rows, 100.0% filled |
| P07 | 782 | 32.2% | 32.2% | +0.4 | n/a | no target · vendors with a registry record: 252 rows, 100.0% filled |
| P08 | 29395 | 31.9% | 31.9% | +1.9 | n/a | no target · vendors with a registry record: 9370 rows, 100.0% filled |
| P09 | 276 | 89.5% | 89.5% | +0.0 | n/a | no target · vendors with a registry record: 247 rows, 100.0% filled |
| P10 | 2055 | 40.0% | 40.0% | -0.1 | n/a | no target · vendors with a registry record: 823 rows, 100.0% filled |
| P11 | 1812 | 59.3% | 59.3% | +0.0 | n/a | no target · vendors with a registry record: 1075 rows, 100.0% filled |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P13 | 200003 | 40.5% | 40.5% | +0.3 | n/a | no target · vendors with a registry record: 80997 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 97.4% | 97.4% | +1.0 | 90% | ✅ met |
| P01T | 206 | 70.4% | 70.4% | -0.3 | 90% | ❌ 20 pts to go |
| P01_GOLD | 654 | 88.1% | 88.1% | +0.7 | 95% | 🟡 7 pts to go |
| P02 | 490 | 88.4% | 88.4% | +0.2 | 95% | 🟡 7 pts to go |
| P03 | 277 | 83.8% | 83.8% | +0.7 | 85% | 🟡 1 pts to go |
| P04 | 4832 | 68.9% | 69.0% | +4.4 | 90% | ❌ 21 pts to go |
| P05 | 427 | 76.8% | 76.8% | -1.2 | 75% | ✅ met |
| P06M | 29627 | 94.1% | 94.1% | +0.3 | n/a | no target |
| P06T | 55379 | 37.6% | 37.7% | +0.7 | n/a | no target |
| P06 | 251 | 72.5% | 72.5% | +1.4 | 80% | 🟡 8 pts to go |
| P07 | 782 | 61.1% | 61.3% | +2.9 | 80% | ❌ 19 pts to go |
| P08 | 29395 | 56.8% | 56.8% | +4.9 | 75% | ❌ 18 pts to go |
| P09 | 276 | 75.7% | 75.7% | +0.1 | 95% | ❌ 19 pts to go |
| P10 | 2055 | 45.9% | 46.0% | -0.9 | 70% | ❌ 24 pts to go |
| P11 | 1812 | 32.5% | 32.5% | +0.7 | 65% | ❌ 32 pts to go |
| P12 | 11 | 72.7% | 72.7% | +0.0 | 80% | 🟡 7 pts to go |
| P13 | 200003 | 39.5% | 39.5% | -6.1 | 60% | ❌ 20 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 14.6% | 14.6% | -3.9 | 50% | ❌ 35 pts to go |
| P01T | 206 | 16.5% | 16.5% | +0.3 | n/a | no target |
| P01_GOLD | 654 | 19.3% | 19.3% | -0.5 | 40% | ❌ 21 pts to go |
| P02 | 490 | 19.0% | 19.0% | -0.9 | 40% | ❌ 21 pts to go |
| P03 | 277 | 19.5% | 19.5% | -0.8 | 40% | ❌ 20 pts to go |
| P04 | 4832 | 14.0% | 14.0% | -2.3 | 40% | ❌ 26 pts to go |
| P05 | 427 | 21.1% | 21.1% | +0.2 | 25% | 🟡 4 pts to go |
| P06M | 29627 | 19.6% | 19.6% | -0.8 | n/a | no target |
| P06T | 55379 | 10.0% | 10.0% | +2.5 | n/a | no target |
| P06 | 251 | 20.3% | 20.3% | +2.8 | 35% | ❌ 15 pts to go |
| P07 | 782 | 22.9% | 22.9% | +3.8 | 35% | ❌ 12 pts to go |
| P08 | 29395 | 22.5% | 22.5% | +4.8 | 35% | ❌ 12 pts to go |
| P09 | 276 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P10 | 2055 | 9.2% | 9.2% | +2.1 | 30% | ❌ 21 pts to go |
| P11 | 1812 | 9.5% | 9.5% | +3.0 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 200003 | 10.5% | 10.5% | -2.0 | 30% | ❌ 20 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 206 | 85.0% | 85.0% | -0.2 | 100% | ❌ 15 pts to go |
| P01_GOLD | 654 | 91.7% | 91.7% | +0.6 | 100% | 🟡 8 pts to go |
| P02 | 490 | 96.7% | 96.7% | +0.1 | 100% | 🟡 3 pts to go |
| P03 | 277 | 89.9% | 89.9% | +0.4 | 100% | ❌ 10 pts to go |
| P04 | 4832 | 78.6% | 78.6% | +6.1 | 100% | ❌ 21 pts to go |
| P05 | 427 | 89.9% | 89.9% | -0.1 | 100% | ❌ 10 pts to go |
| P06M | 29627 | 99.6% | 99.6% | +0.2 | n/a | no target |
| P06T | 55379 | 59.4% | 59.4% | +0.7 | n/a | no target |
| P06 | 251 | 81.7% | 81.7% | -0.4 | 95% | ❌ 13 pts to go |
| P07 | 782 | 87.2% | 87.2% | +1.8 | 95% | 🟡 8 pts to go |
| P08 | 29395 | 85.4% | 85.4% | +0.9 | 95% | 🟡 10 pts to go |
| P09 | 276 | 96.4% | 96.4% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2055 | 53.8% | 53.8% | -0.8 | 95% | ❌ 41 pts to go |
| P11 | 1812 | 61.8% | 61.8% | +0.9 | 80% | ❌ 18 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 200003 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 69.8% | 69.8% | -1.3 | n/a | no target |
| P01T | 206 | 71.8% | 71.8% | -2.4 | n/a | no target |
| P01_GOLD | 654 | 73.2% | 73.2% | +0.0 | 90% | ❌ 17 pts to go |
| P02 | 490 | 76.7% | 76.7% | -1.7 | 95% | ❌ 18 pts to go |
| P03 | 277 | 74.4% | 74.4% | +0.3 | 95% | ❌ 21 pts to go |
| P04 | 4832 | 69.5% | 69.5% | +0.0 | 95% | ❌ 26 pts to go |
| P05 | 427 | 71.4% | 71.4% | -1.1 | 90% | ❌ 19 pts to go |
| P06M | 29627 | 72.2% | 72.2% | -4.5 | n/a | no target |
| P06T | 55379 | 58.4% | 58.4% | -0.2 | n/a | no target |
| P06 | 251 | 70.5% | 70.5% | +5.1 | 95% | ❌ 24 pts to go |
| P07 | 782 | 67.8% | 67.8% | +8.1 | 90% | ❌ 22 pts to go |
| P08 | 29395 | 70.9% | 70.9% | +12.3 | 95% | ❌ 24 pts to go |
| P09 | 276 | 85.9% | 85.9% | +0.1 | 100% | ❌ 14 pts to go |
| P10 | 2055 | 53.1% | 53.1% | -0.7 | 95% | ❌ 42 pts to go |
| P11 | 1812 | 33.0% | 33.0% | +2.3 | 75% | ❌ 42 pts to go |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target |
| P13 | 200003 | 57.2% | 57.2% | -10.7 | 95% | ❌ 38 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 82.6% | 82.6% | -0.9 | n/a | no target |
| P01T | 206 | 90.8% | 90.8% | -0.9 | 95% | 🟡 4 pts to go |
| P01_GOLD | 654 | 85.3% | 85.3% | +0.3 | 90% | 🟡 5 pts to go |
| P02 | 490 | 90.4% | 90.4% | -0.6 | 95% | 🟡 5 pts to go |
| P03 | 277 | 84.5% | 84.5% | +0.7 | 95% | ❌ 10 pts to go |
| P04 | 4832 | 90.3% | 90.3% | -1.3 | 90% | ✅ met |
| P05 | 427 | 92.5% | 92.5% | +0.1 | 95% | 🟡 2 pts to go |
| P06M | 29627 | 83.9% | 83.9% | -1.4 | n/a | no target |
| P06T | 55379 | 87.3% | 87.3% | +2.7 | n/a | no target |
| P06 | 251 | 92.8% | 92.8% | +7.4 | 100% | 🟡 7 pts to go |
| P07 | 782 | 94.6% | 94.6% | +11.0 | 100% | 🟡 5 pts to go |
| P08 | 29395 | 95.0% | 95.0% | +17.2 | 100% | 🟡 5 pts to go |
| P09 | 276 | 74.3% | 74.3% | +0.1 | n/a | no target |
| P10 | 2055 | 94.3% | 94.3% | -0.1 | 100% | 🟡 6 pts to go |
| P11 | 1812 | 55.5% | 55.5% | +4.4 | 80% | ❌ 24 pts to go |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 200003 | 72.8% | 72.8% | -8.0 | 95% | ❌ 22 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 2.6% | 2.6% | -0.6 | n/a | no target |
| P01T | 206 | 9.2% | 9.2% | +0.5 | n/a | no target |
| P01_GOLD | 654 | 13.5% | 13.5% | -0.5 | 25% | ❌ 12 pts to go |
| P02 | 490 | 23.7% | 23.7% | -1.1 | 40% | ❌ 16 pts to go |
| P03 | 277 | 8.7% | 8.7% | -0.3 | 20% | ❌ 11 pts to go |
| P04 | 4832 | 2.4% | 2.4% | -0.9 | 20% | ❌ 18 pts to go |
| P05 | 427 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 29627 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 55379 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 251 | 5.6% | 5.6% | +0.2 | n/a | no target |
| P07 | 782 | 8.1% | 8.1% | +0.2 | n/a | no target |
| P08 | 29395 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 276 | 7.2% | 7.2% | -0.4 | n/a | no target |
| P10 | 2055 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1812 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 12.0% | 12.0% | -4.1 | n/a | no target |
| P01T | 206 | 18.0% | 18.0% | -1.2 | 70% | ❌ 52 pts to go |
| P01_GOLD | 654 | 40.4% | 40.4% | -1.7 | 80% | ❌ 40 pts to go |
| P02 | 490 | 54.7% | 54.7% | -2.6 | 90% | ❌ 35 pts to go |
| P03 | 277 | 18.4% | 18.4% | -0.8 | 60% | ❌ 42 pts to go |
| P04 | 4832 | 14.9% | 14.9% | -5.3 | 85% | ❌ 70 pts to go |
| P05 | 427 | 11.2% | 11.2% | +0.1 | 50% | ❌ 39 pts to go |
| P06M | 29627 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06T | 55379 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 251 | 13.1% | 13.1% | -0.1 | n/a | no target |
| P07 | 782 | 9.6% | 9.6% | +0.5 | n/a | no target |
| P08 | 29395 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P09 | 276 | 71.7% | 71.7% | -0.3 | 95% | ❌ 23 pts to go |
| P10 | 2055 | 1.5% | 1.5% | -0.1 | n/a | no target |
| P11 | 1812 | 12.6% | 12.6% | -0.4 | n/a | no target |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 200003 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 4.3% | 4.3% | -1.3 | n/a | no target |
| P01T | 206 | 10.7% | 10.7% | +1.5 | n/a | no target |
| P01_GOLD | 654 | 32.4% | 32.4% | -1.4 | 70% | ❌ 38 pts to go |
| P02 | 490 | 36.9% | 36.9% | -1.8 | 75% | ❌ 38 pts to go |
| P03 | 277 | 18.4% | 18.4% | -0.8 | 55% | ❌ 37 pts to go |
| P04 | 4832 | 14.9% | 14.9% | -5.3 | 75% | ❌ 60 pts to go |
| P05 | 427 | 10.3% | 10.3% | +0.1 | 50% | ❌ 40 pts to go |
| P06M | 29627 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 55379 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 251 | 5.6% | 5.6% | -0.1 | n/a | no target |
| P07 | 782 | 4.9% | 4.9% | +0.3 | n/a | no target |
| P08 | 29395 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P09 | 276 | 68.5% | 68.5% | -0.2 | 95% | ❌ 26 pts to go |
| P10 | 2055 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P11 | 1812 | 12.5% | 12.5% | -0.3 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 200003 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 5.6% | 5.6% | -2.0 | n/a | no target |
| P01T | 206 | 8.7% | 8.7% | +0.0 | n/a | no target |
| P01_GOLD | 654 | 54.9% | 55.0% | -2.2 | 80% | ❌ 25 pts to go |
| P02 | 490 | 43.3% | 43.5% | -2.0 | 75% | ❌ 32 pts to go |
| P03 | 277 | 34.7% | 34.7% | -1.4 | 70% | ❌ 35 pts to go |
| P04 | 4832 | 14.7% | 15.0% | -5.2 | 70% | ❌ 55 pts to go |
| P05 | 427 | 13.8% | 13.8% | -0.2 | 50% | ❌ 36 pts to go |
| P06M | 29627 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 55379 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 251 | 13.1% | 13.1% | -0.1 | n/a | no target |
| P07 | 782 | 1.0% | 1.0% | -0.1 | n/a | no target |
| P08 | 29395 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 276 | 46.4% | 46.7% | -0.5 | 80% | ❌ 34 pts to go |
| P10 | 2055 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P11 | 1812 | 4.3% | 4.4% | -0.2 | n/a | no target |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 200003 | 0.1% | 0.1% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 11.3% | 11.3% | -3.6 | n/a | no target |
| P01T | 206 | 20.9% | 20.9% | +1.7 | 60% | ❌ 39 pts to go |
| P01_GOLD | 654 | 59.6% | 59.6% | -2.6 | 70% | ❌ 10 pts to go |
| P02 | 490 | 37.8% | 37.8% | -1.7 | 50% | ❌ 12 pts to go |
| P03 | 277 | 45.1% | 45.1% | -2.6 | 55% | 🟡 10 pts to go |
| P04 | 4832 | 9.2% | 9.2% | -3.3 | 40% | ❌ 31 pts to go |
| P05 | 427 | 16.2% | 16.2% | -0.4 | 40% | ❌ 24 pts to go |
| P06M | 29627 | 2.2% | 2.2% | -0.6 | n/a | no target |
| P06T | 55379 | 1.4% | 1.4% | -0.1 | n/a | no target |
| P06 | 251 | 17.1% | 17.1% | -1.1 | n/a | no target |
| P07 | 782 | 4.9% | 4.9% | +0.0 | n/a | no target |
| P08 | 29395 | 2.1% | 2.1% | +0.0 | n/a | no target |
| P09 | 276 | 6.2% | 6.2% | +0.4 | n/a | no target |
| P10 | 2055 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P11 | 1812 | 3.9% | 3.9% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.6% | 0.6% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 16.9% | 16.9% | -4.8 | n/a | no target |
| P01T | 206 | 27.7% | 27.7% | -0.2 | 65% | ❌ 37 pts to go |
| P01_GOLD | 654 | 66.1% | 66.1% | -2.5 | 70% | 🟡 4 pts to go |
| P02 | 490 | 22.2% | 22.2% | -1.5 | 50% | ❌ 28 pts to go |
| P03 | 277 | 48.4% | 48.4% | -2.0 | 60% | ❌ 12 pts to go |
| P04 | 4832 | 4.1% | 4.1% | -1.5 | 40% | ❌ 36 pts to go |
| P05 | 427 | 19.7% | 19.7% | -0.2 | 45% | ❌ 25 pts to go |
| P06M | 29627 | 1.3% | 1.3% | -0.4 | n/a | no target |
| P06T | 55379 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 251 | 26.7% | 26.7% | -2.6 | n/a | no target |
| P07 | 782 | 4.5% | 4.5% | -0.6 | n/a | no target |
| P08 | 29395 | 0.9% | 0.9% | +0.0 | n/a | no target |
| P09 | 276 | 10.9% | 10.9% | +0.0 | n/a | no target |
| P10 | 2055 | 3.1% | 3.1% | -0.2 | n/a | no target |
| P11 | 1812 | 3.5% | 3.5% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 10.5% | 10.5% | -1.5 | n/a | no target |
| P01T | 206 | 14.1% | 14.1% | +1.4 | n/a | no target |
| P01_GOLD | 654 | 48.3% | 48.3% | -1.9 | 50% | 🟡 2 pts to go |
| P02 | 490 | 35.7% | 35.7% | -1.9 | n/a | no target |
| P03 | 277 | 48.7% | 48.7% | -2.1 | 60% | ❌ 11 pts to go |
| P04 | 4832 | 9.3% | 9.3% | -3.5 | n/a | no target |
| P05 | 427 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 29627 | 0.6% | 0.6% | -0.2 | n/a | no target |
| P06T | 55379 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 251 | 17.9% | 17.9% | -2.5 | n/a | no target |
| P07 | 782 | 4.9% | 4.9% | -0.8 | n/a | no target |
| P08 | 29395 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 276 | 20.7% | 20.7% | +0.0 | n/a | no target |
| P10 | 2055 | 2.2% | 2.2% | -0.3 | n/a | no target |
| P11 | 1812 | 2.5% | 2.5% | -0.2 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 200003 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 6.4% | 6.4% | -2.4 | 15% | 🟡 9 pts to go |
| P01T | 206 | 13.6% | 13.6% | +0.9 | 15% | 🟡 1 pts to go |
| P01_GOLD | 654 | 33.6% | 33.6% | -1.5 | 40% | 🟡 6 pts to go |
| P02 | 490 | 11.6% | 11.8% | -0.6 | 25% | ❌ 13 pts to go |
| P03 | 277 | 15.9% | 15.9% | -0.6 | 25% | 🟡 9 pts to go |
| P04 | 4832 | 2.1% | 2.1% | -0.6 | 15% | ❌ 13 pts to go |
| P05 | 427 | 6.3% | 6.3% | -0.3 | 15% | 🟡 9 pts to go |
| P06M | 29627 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 55379 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 251 | 9.2% | 9.2% | -0.1 | 15% | 🟡 6 pts to go |
| P07 | 782 | 3.5% | 3.5% | +0.1 | 15% | ❌ 12 pts to go |
| P08 | 29395 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 276 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2055 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1812 | 1.2% | 1.2% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 200003 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 4.3% | 4.3% | -1.3 | 15% | ❌ 11 pts to go |
| P01T | 206 | 11.7% | 11.7% | +0.8 | 25% | ❌ 13 pts to go |
| P01_GOLD | 654 | 27.5% | 27.5% | -1.4 | 25% | ✅ met |
| P02 | 490 | 24.3% | 24.3% | -1.1 | 15% | ✅ met |
| P03 | 277 | 20.9% | 20.9% | -0.9 | 15% | ✅ met |
| P04 | 4832 | 3.0% | 3.0% | -1.0 | 15% | ❌ 12 pts to go |
| P05 | 427 | 11.5% | 11.5% | +0.1 | 15% | 🟡 4 pts to go |
| P06M | 29627 | 0.5% | 0.5% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 55379 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 251 | 6.4% | 6.4% | -0.7 | 15% | 🟡 9 pts to go |
| P07 | 782 | 1.7% | 1.7% | -0.1 | 15% | ❌ 13 pts to go |
| P08 | 29395 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 276 | 1.4% | 1.4% | -0.1 | 15% | ❌ 14 pts to go |
| P10 | 2055 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1812 | 1.8% | 1.8% | +0.0 | 15% | ❌ 13 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 200003 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 1.3% | 1.3% | -0.3 | 20% | ❌ 19 pts to go |
| P01T | 206 | 3.4% | 3.4% | +0.3 | 20% | ❌ 17 pts to go |
| P01_GOLD | 654 | 4.1% | 4.1% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 490 | 1.2% | 1.2% | -0.3 | 20% | ❌ 19 pts to go |
| P03 | 277 | 1.8% | 1.8% | -0.1 | 20% | ❌ 18 pts to go |
| P04 | 4832 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P05 | 427 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 29627 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 251 | 1.6% | 1.6% | +0.2 | 20% | ❌ 18 pts to go |
| P07 | 782 | 0.3% | 0.3% | +0.1 | 20% | ❌ 20 pts to go |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 276 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2055 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1812 | 0.1% | 0.1% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 1.0% | 1.0% | -0.6 | 15% | ❌ 14 pts to go |
| P01T | 206 | 2.4% | 2.4% | -0.7 | 15% | ❌ 13 pts to go |
| P01_GOLD | 654 | 10.2% | 10.2% | -0.3 | 15% | 🟡 5 pts to go |
| P02 | 490 | 11.0% | 11.0% | -0.5 | 15% | 🟡 4 pts to go |
| P03 | 277 | 19.9% | 19.9% | -0.8 | 15% | ✅ met |
| P04 | 4832 | 1.8% | 1.8% | -0.6 | 15% | ❌ 13 pts to go |
| P05 | 427 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 29627 | 0.3% | 0.3% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 55379 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 251 | 4.0% | 4.0% | +0.1 | 15% | ❌ 11 pts to go |
| P07 | 782 | 1.3% | 1.3% | +0.1 | 15% | ❌ 14 pts to go |
| P08 | 29395 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 276 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2055 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1812 | 0.7% | 0.7% | -0.1 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 200003 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 11.8% | 11.8% | -0.6 | 20% | 🟡 8 pts to go |
| P01T | 206 | 15.0% | 15.0% | +1.5 | 40% | ❌ 25 pts to go |
| P01_GOLD | 654 | 44.8% | 44.8% | -1.8 | 40% | ✅ met |
| P02 | 490 | 41.2% | 41.2% | -2.0 | 20% | ✅ met |
| P03 | 277 | 47.3% | 47.3% | -1.2 | 35% | ✅ met |
| P04 | 4832 | 11.0% | 11.0% | -3.9 | 20% | 🟡 9 pts to go |
| P05 | 427 | 15.7% | 15.7% | +0.1 | 20% | 🟡 4 pts to go |
| P06M | 29627 | 0.9% | 0.9% | -0.1 | 20% | ❌ 19 pts to go |
| P06T | 55379 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 251 | 18.7% | 18.7% | -2.4 | 20% | 🟡 1 pts to go |
| P07 | 782 | 5.4% | 5.4% | -0.7 | 20% | ❌ 15 pts to go |
| P08 | 29395 | 0.7% | 0.7% | -0.1 | 20% | ❌ 19 pts to go |
| P09 | 276 | 21.4% | 21.4% | +0.3 | 20% | ✅ met |
| P10 | 2055 | 3.6% | 3.6% | -0.2 | 20% | ❌ 16 pts to go |
| P11 | 1812 | 3.1% | 3.1% | -0.1 | 20% | ❌ 17 pts to go |
| P12 | 11 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P13 | 200003 | 0.3% | 0.3% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 12.0% | 12.0% | -6.1 | n/a | no target |
| P01T | 206 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 654 | 68.7% | 68.7% | -2.9 | 95% | ❌ 26 pts to go |
| P02 | 490 | 63.3% | 63.3% | -2.9 | 95% | ❌ 32 pts to go |
| P03 | 277 | 55.6% | 55.6% | -2.3 | 90% | ❌ 34 pts to go |
| P04 | 4832 | 20.6% | 20.6% | -5.9 | 85% | ❌ 64 pts to go |
| P05 | 427 | 39.3% | 39.3% | +0.4 | 75% | ❌ 36 pts to go |
| P06M | 29627 | 23.5% | 23.5% | -4.6 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 3.9% | 3.9% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 12.0% | 12.0% | -6.1 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 654 | 70.5% | 70.5% | -3.0 | 100% | ❌ 30 pts to go |
| P02 | 490 | 64.9% | 64.9% | -3.3 | 100% | ❌ 35 pts to go |
| P03 | 277 | 58.1% | 58.1% | -2.4 | n/a | no target |
| P04 | 4832 | 21.0% | 21.0% | -6.0 | 95% | ❌ 74 pts to go |
| P05 | 427 | 35.1% | 35.1% | +0.5 | 80% | ❌ 45 pts to go |
| P06M | 29627 | 23.5% | 23.5% | -4.6 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 91.7% | 91.7% | +0.1 | 100% | 🟡 8 pts to go |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 4.0% | 4.0% | +0.0 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 82.1% | 82.1% | -2.2 | n/a | no target |
| P01T | 206 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 654 | 54.3% | 54.3% | +2.0 | 85% | ❌ 31 pts to go |
| P02 | 490 | 60.8% | 60.8% | +1.6 | 90% | ❌ 29 pts to go |
| P03 | 277 | 46.6% | 46.6% | +2.6 | 85% | ❌ 38 pts to go |
| P04 | 4832 | 37.6% | 37.6% | +8.5 | 90% | ❌ 52 pts to go |
| P05 | 427 | 33.0% | 33.0% | +0.1 | 75% | ❌ 42 pts to go |
| P06M | 29627 | 82.0% | 82.0% | -2.3 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 81.9% | 81.9% | +0.1 | 95% | ❌ 13 pts to go |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 3.8% | 3.8% | +0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 54.0% | 54.0% | -11.9 | n/a | no target |
| P01T | 206 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 654 | 53.8% | 53.8% | +1.8 | 85% | ❌ 31 pts to go |
| P02 | 490 | 55.1% | 55.1% | +1.7 | 90% | ❌ 35 pts to go |
| P03 | 277 | 46.9% | 46.9% | +2.5 | 85% | ❌ 38 pts to go |
| P04 | 4832 | 33.3% | 33.3% | +8.7 | 90% | ❌ 57 pts to go |
| P05 | 427 | 42.2% | 42.2% | -0.5 | 75% | ❌ 33 pts to go |
| P06M | 29627 | 63.4% | 63.4% | -5.8 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.4% | 0.4% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 2.9% | 2.9% | +0.4 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 96.9% | 96.9% | +1.7 | n/a | no target |
| P01T | 206 | 95.6% | 95.6% | -0.5 | n/a | no target |
| P01_GOLD | 654 | 85.9% | 86.1% | +0.4 | 100% | ❌ 14 pts to go |
| P02 | 490 | 78.2% | 78.2% | +0.6 | 100% | ❌ 22 pts to go |
| P03 | 277 | 92.8% | 92.8% | +0.3 | n/a | no target |
| P04 | 4832 | 53.5% | 53.5% | +2.9 | 95% | ❌ 42 pts to go |
| P05 | 427 | 77.5% | 77.5% | +0.2 | 95% | ❌ 18 pts to go |
| P06M | 29627 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 55379 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 251 | 20.3% | 20.3% | -0.1 | n/a | no target |
| P07 | 782 | 10.2% | 10.2% | +0.0 | n/a | no target |
| P08 | 29395 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P09 | 276 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2055 | 71.1% | 71.1% | +0.5 | n/a | no target |
| P11 | 1812 | 70.1% | 70.1% | +0.3 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 99.6% | 99.6% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 96.9% | 96.9% | +1.7 | n/a | no target |
| P01T | 206 | 95.6% | 95.6% | -0.5 | n/a | no target |
| P01_GOLD | 654 | 89.0% | 89.1% | +0.3 | 100% | ❌ 11 pts to go |
| P02 | 490 | 79.4% | 79.4% | +0.6 | 100% | ❌ 21 pts to go |
| P03 | 277 | 93.5% | 93.5% | +0.3 | n/a | no target |
| P04 | 4832 | 56.0% | 56.0% | +2.0 | 95% | ❌ 39 pts to go |
| P05 | 427 | 89.7% | 89.7% | +0.4 | 70% | ✅ met |
| P06M | 29627 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 55379 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 251 | 20.3% | 20.3% | -0.1 | n/a | no target |
| P07 | 782 | 10.2% | 10.2% | +0.0 | n/a | no target |
| P08 | 29395 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P09 | 276 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2055 | 71.1% | 71.1% | +0.5 | n/a | no target |
| P11 | 1812 | 70.1% | 70.1% | +0.2 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 654 | 16.2% | 16.2% | -0.7 | 60% | ❌ 44 pts to go · rows from a source that publishes bids: 367 rows, 28.9% filled |
| P02 | 490 | 10.2% | 10.2% | -0.5 | n/a | no target · rows from a source that publishes bids: 297 rows, 16.8% filled |
| P03 | 277 | 13.4% | 13.4% | -0.5 | n/a | no target · rows from a source that publishes bids: 143 rows, 25.9% filled |
| P04 | 4832 | 1.3% | 1.3% | -0.4 | n/a | no target · rows from a source that publishes bids: 883 rows, 6.9% filled |
| P05 | 427 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 59 rows, 18.6% filled |
| P06M | 29627 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55379 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 4.3% | 4.3% | -0.1 | n/a | no target · rows from a source that publishes bids: 263 rows, 4.6% filled |
| P10 | 2055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 0.4% | 0.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 67 rows, 10.4% filled |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 11 rows, 0.0% filled |
| P13 | 200003 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 97.6% | +0.0 | n/a | no target |
| P01_GOLD | 654 | 51.2% | 83.0% | -2.2 | 90% | ❌ 39 pts to go |
| P02 | 490 | 50.8% | 87.6% | -2.6 | 90% | ❌ 39 pts to go |
| P03 | 277 | 44.0% | 80.5% | -1.9 | 90% | ❌ 46 pts to go |
| P04 | 4832 | 14.6% | 94.7% | -5.0 | 90% | ❌ 75 pts to go |
| P05 | 427 | 0.0% | 81.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 29627 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55379 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 2.9% | 4.7% | +0.0 | 90% | ❌ 87 pts to go |
| P10 | 2055 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1812 | 2.1% | 97.6% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 206 | 1.0% | 98.5% | +0.1 | n/a | no target |
| P01_GOLD | 654 | 25.4% | 57.2% | -1.1 | 90% | ❌ 65 pts to go |
| P02 | 490 | 50.0% | 86.7% | -2.4 | n/a | no target |
| P03 | 277 | 24.2% | 60.6% | -1.0 | n/a | no target |
| P04 | 4832 | 15.8% | 95.9% | -5.6 | n/a | no target |
| P05 | 427 | 0.5% | 81.7% | +0.0 | n/a | no target |
| P06M | 29627 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55379 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 40.9% | 42.8% | +0.5 | n/a | no target |
| P10 | 2055 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1812 | 2.2% | 97.7% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 206 | 2.4% | 100.0% | +0.2 | n/a | no target |
| P01_GOLD | 654 | 49.8% | 81.7% | -2.2 | 95% | ❌ 45 pts to go |
| P02 | 490 | 55.5% | 92.2% | -2.6 | n/a | no target |
| P03 | 277 | 48.4% | 84.8% | -2.0 | n/a | no target |
| P04 | 4832 | 16.4% | 96.5% | -5.8 | n/a | no target |
| P05 | 427 | 5.2% | 86.4% | +0.2 | n/a | no target |
| P06M | 29627 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55379 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 251 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 782 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29395 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 59.8% | 61.6% | -0.6 | n/a | no target |
| P10 | 2055 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1812 | 2.4% | 97.9% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 200003 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 206 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 654 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 490 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4832 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 29627 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55379 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 251 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 782 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29395 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2055 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1812 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 200003 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 206 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 654 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 490 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4832 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 29627 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55379 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 251 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 782 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29395 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2055 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1812 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 200003 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 391 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 206 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 654 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 490 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4832 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 29627 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55379 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 251 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 782 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29395 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2055 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1812 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 200003 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

