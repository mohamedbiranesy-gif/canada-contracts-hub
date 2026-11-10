# City of Chicago Contracts

- Endpoint: https://data.cityofchicago.org/resource/rsxa-ify5.json
- Query parameters: `$where=state IN ('CAN', 'ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'YT', 'NT', 'NU')`
- Fields: vendor_name, address_1, city, state, zip, purchase_order_contract_number, start_date, end_date, award_amount, etc.
- Rows seen for Canada: 50
- Ongoing rows: 13
- Quirks: Some vendors might use state 'CAN' or Canadian province codes. Filtered strictly by those codes.
