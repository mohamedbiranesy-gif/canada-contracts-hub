# US Socrata Sweep Continue

This pipeline queries Socrata Discovery API and executes SoQL queries on datasets found by the discovery sweep. The list of matching datasets and columns with Canadian locations are stored in the hardcoded lists below.

## Run

```
python3 contrib/jules/us_socrata_sweep_continue/scraper.py
```
