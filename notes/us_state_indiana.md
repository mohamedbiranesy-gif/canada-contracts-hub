# us_state_indiana — Indiana IDOA Public Contract Search (secure.in.gov/apps/idoa/contractsearch): checked, rejected

The search is a Vue single-page app ("doesn't work properly without JavaScript"); its bundle references `/agencies` and `/contracts/search` routes on a relative API root, but the obvious paths (`/apps/idoa/contractsearch/api/...`) return 404 or the SPA shell, and no documented API exists. in.gov/idoa contract-information page 404s. Not pulled (JS-only, undocumented backend).
