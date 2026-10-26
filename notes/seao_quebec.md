# seao_quebec — coverage note

Source key: `seao_quebec` · Reference date ("today"): **2026-10-25** · Output: `/home/claude/contracts/normalized/seao_quebec.jsonl` (331,410 records, one JSON object per line, 2.6 GB).

Dataset: *Système électronique d'appel d'offres (SEAO)* open data, published by the **Secrétariat du Conseil du trésor (Québec)** on Données Québec
(`https://www.donneesquebec.ca/recherche/dataset/systeme-electronique-dappel-doffres-seao`, CKAN package id `d23b2e02-085d-43e5-9e6e-e1d558ebfdd5`,
metadata_modified 2026-10-19). It contains every contract disclosure made in SEAO by Québec public bodies (ministries and agencies, health and
social-services network, education network, and — mandatory since April 2011 — municipalities), from 2009 onwards.

## 1. What was downloaded (exact URLs, timestamps, sizes)

Discovery: `https://www.donneesquebec.ca/recherche/api/3/action/package_show?id=systeme-electronique-dappel-doffres-seao`
(retrieved 2026-10-25T12:05Z, 438 resources: 381 JSON, 53 XML-zips (one mis-tagged ZIP = JSON re-export), 3 PDF; saved as
`/home/claude/contracts/downloads/seao_quebec/meta/package_show.json`, flattened to `meta/resources.tsv`).

Documentation (retrieved 2026-10-25T12:06Z, read in full with `pdftotext -layout`):
- `seao-specificationsxml-donneesouvertes-20210305.pdf` (375,599 B, "Format XML pour les données ouvertes du SEAO", 13 p.) — `https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/af41596c-b07f-4664-82c8-577e1ef9a6f3/download/seao-specificationsxml-donneesouvertes-20210305.pdf`
- `seao-specificationsjson-donneesouvertes-20210330.pdf` (278,502 B, "Format JSON pour les données ouvertes du SEAO", 17 p.) — `https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/271331f3-bbdb-42f7-a052-0c75b524287d/download/seao-specificationsjson-donneesouvertes-20210330.pdf`
- `faqseao.pdf` (94,801 B, FAQ) — `https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/e9589860-8f09-42f1-b5b4-fd3870ee4703/download/faqseao.pdf`

### 1a. XML archives — ALL of them (2009-01 → 2024-05, the XML feed stopped after May 2024)
54 zip files, 253.4 MB, downloaded 2026-10-25T12:09:18Z–12:12:16Z with `curl -sS -L -C - --retry 3 -A contracts-research/1.0`
(log `downloads/seao_quebec/logs/download_xml.log`), extracted (nested zips included) to `downloads/seao_quebec/xml_extracted/<zipstem>/` → **489 XML files**:

| kind | files | records | bytes |
|---|---|---|---|
| `Avis_*.xml` (contracts concluded + their notice) | 86 | 569,127 `<avis>` | 1,504 MB |
| `AvisRevisions_*.xml` (corrected versions of earlier avis, 2018-01 → 2024-05 only) | 77 | 51,018 | 138 MB |
| `Contrats_*.xml` (information finale = closure records) | 86 | 272,500 `<contrat>` | 97 MB |
| `ContratsRevisions_*.xml` | 77 | 4,979 | 1.8 MB |
| `Depenses_*.xml` (dépenses supplémentaires) | 86 | 48,521 `<avis>` blocks / 71,213 `<depense>` | 37 MB |
| `DepensesRevisions_*.xml` | 77 | 4,807 blocks / 19,526 depense | 9 MB |

Period coverage is gap-free: yearly files 2009–2017 (`annee2009.zip` … `annee2017.zip`), monthly files 2018-01 … 2024-05 (`annee2018.zip`, `annee2019.zip`,
`annee_2020.zip` [12 nested monthly zips], then one zip per month 2021-01 … 2024-05). Revision files exist only from 2018-01. Note the two CKAN resources
labelled "Decembre 2023"/"Decembre 2024" are actually Dec-2022 / Dec-2023 data (checked from the `<export datedebut>` attribute — the file content, not the label, was used).

| zip | CKAN name | bytes | CKAN last_modified | URL |
|---|---|---|---|---|
| 2021_fevrier.zip | Février 2021 | 1,263,930 | 2021-03-02 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/be2a3f6d-0e23-4fd3-965d-3f37ea520893/download/2021_fevrier.zip |
| 2021_janvier.zip | Janvier 2021 | 1,249,503 | 2021-02-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/d35c74e0-9ac9-4c19-84f7-c8cb0179f550/download/2021_janvier.zip |
| 2021_mars.zip | Mars 2021 | 1,802,471 | 2021-04-07 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/e1e0422c-1dde-4c94-859d-60cc45fc249d/download/2021_mars.zip |
| annee2009.zip | Année 2009 | 4,230,883 | 2018-02-06 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/40ee196b-25d5-4786-a6e4-c4e301676190/download/annee2009.zip |
| annee2010.zip | Année 2010 | 4,948,923 | 2018-02-06 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/256fc1f4-3b21-41f6-8266-f1e4474a10ab/download/annee2010.zip |
| annee2011.zip | Année 2011 | 7,997,147 | 2018-02-06 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/262007bb-742d-4de3-904a-6d4ee4759bbe/download/annee2011.zip |
| annee2012.zip | Année 2012 | 9,287,525 | 2018-02-06 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/ce331443-53c1-4b77-9829-74f12a934bb4/download/annee2012.zip |
| annee2013.zip | Année 2013 | 10,916,681 | 2018-02-06 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/338e1f63-0a8f-4790-851c-928a00c066f4/download/annee2013.zip |
| annee2014.zip | Année 2014 | 11,269,645 | 2018-02-06 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/2cf196da-a7b7-47c7-ae21-bdc21157e4c4/download/annee2014.zip |
| annee2015.zip | Année 2015 | 11,638,934 | 2018-02-06 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/a7a3e3e4-b3c4-4e2e-b732-67aa87458d1d/download/annee2015.zip |
| annee2016.zip | Année 2016 | 11,492,396 | 2018-02-06 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/4d8729ad-2bea-47fc-a097-fb8d41872816/download/annee2016.zip |
| annee2017.zip | Année 2017 | 12,000,331 | 2018-02-06 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/1773998b-0cc0-4402-9b09-51f939633112/download/annee2017.zip |
| annee2018.zip | Année 2018 | 12,740,420 | 2019-02-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/d1747eb5-894d-4907-8d7b-7d6f12714476/download/annee2018.zip |
| annee2019.zip | Année 2019 | 14,166,764 | 2020-10-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/0e57d621-999e-4863-a0fe-2ea161d06911/download/annee2019.zip |
| annee_2020.zip | Année 2020 | 15,426,031 | 2021-03-10 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/9c227faa-8629-4e38-aa10-f47c59c46a48/download/annee_2020.zip |
| aout-2021.zip | Aout 2021 | 1,152,923 | 2021-09-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/b5104190-5fbf-4167-9ebd-888b8dbdbb3b/download/aout-2021.zip |
| aout-2022.zip | Aout 2022 | 1,317,158 | 2022-09-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/d0172dd5-1ba6-4d01-ab48-4eca6b270c71/download/aout-2022.zip |
| aout-2023.zip | Aout 2023 | 1,646,335 | 2023-09-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/6a4d2ae9-534c-49a9-bdfc-d8a1811da22d/download/aout-2023.zip |
| avril-2022.zip | Avril 2022 | 1,658,483 | 2022-10-20 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/dd513d07-b0b1-4c75-862b-5a797de961f6/download/avril-2022.zip |
| avril-2023.zip | Avril 2023 | 1,676,054 | 2023-05-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/29893563-0246-4b6c-b856-0099f686fa3f/download/avril-2023.zip |
| avril-2024.zip | Avril 2024 | 2,084,042 | 2024-05-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/d892843d-f809-4e7e-9304-409aa33365bf/download/avril-2024.zip |
| avril_2021.zip | Avril 2021 | 1,728,769 | 2021-05-26 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/ddae572c-9001-45af-b61f-04da7e66aa4b/download/avril_2021.zip |
| decembre-2022.zip | Decembre 2022 | 1,324,955 | 2022-01-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/15c205d8-ffca-4847-ad12-de4b77bb31c8/download/decembre-2022.zip |
| decembre-2023.zip | Decembre 2023 | 1,530,199 | 2023-01-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/7f258917-228b-4856-98a3-3707e8c11b0e/download/decembre-2023.zip |
| decembre-2024.zip | Decembre 2024 | 1,512,788 | 2024-01-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/19a9e367-b43d-4abb-a64e-6e78c95766a9/download/decembre-2024.zip |
| fevrier-2022.zip | Fevrier 2022 | 1,349,383 | 2022-03-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/0eaae3d4-ab7b-4d71-9f14-7bc9ad2d9a5f/download/fevrier-2022.zip |
| fevrier-2023.zip | Fevrier 2023 | 1,490,615 | 2023-03-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/f60ee7ad-50e8-47d8-9f21-cc5336da53f9/download/fevrier-2023.zip |
| fevrier-2024.zip | Fevrier 2024 | 1,926,676 | 2024-03-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/f068622c-3fe2-4726-ae61-7f79151dd74c/download/fevrier-2024.zip |
| janvier-2022.zip | Janvier 2022 | 1,193,447 | 2022-02-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/7def32b0-1a1f-4e89-b296-3dc0b94bb371/download/janvier-2022.zip |
| janvier-2023.zip | Janvier 2023 | 1,440,860 | 2023-02-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/14478d9f-e2fa-492a-8c38-86cae34921dd/download/janvier-2023.zip |
| janvier-2024.zip | Janvier 2024 | 1,750,813 | 2024-02-07 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/e6ff96f8-de88-4232-938c-6fc01e74c4ed/download/janvier-2024.zip |
| json_mensuel_20230101_20240430.zip | JSON_Mensuel_20230101_20240430.zip | 61,762,904 | 2024-05-02 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/86182c32-812e-4566-8cd1-f289d32ad092/download/json_mensuel_20230101_20240430.zip |
| juillet-2021.zip | Juillet 2021 | 1,272,457 | 2021-08-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/b466d3bc-dddd-404b-a3c4-b838f58c50bf/download/juillet-2021.zip |
| juillet-2022.zip | Juillet 2022 | 1,349,767 | 2022-08-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/b909cbdd-fa16-4bf7-94a8-d7a06088f645/download/juillet-2022.zip |
| juillet-2023.zip | Juillet 2023 | 1,661,632 | 2023-08-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/be79111a-a228-4d5c-ab22-fc91a053f363/download/juillet-2023.zip |
| juin-2021.zip | Juin 2021 | 1,771,151 | 2021-07-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/48ba7af6-1d82-4e16-acb4-796dfc1ab020/download/juin-2021.zip |
| juin-2022.zip | Juin 2022 | 1,741,596 | 2022-07-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/19d499f1-323c-4dd2-b801-7ee1b59e1407/download/juin-2022.zip |
| juin-2023.zip | Juin 2023 | 1,898,422 | 2023-07-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/8807eb12-b64e-4381-9ca5-e447b95f9a79/download/juin-2023.zip |
| mai-2021.zip | Mai 2021 | 1,730,597 | 2021-06-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/ec0829bd-ee8d-41e8-b982-45676dbe635e/download/mai-2021.zip |
| mai-2022.zip | Mai 2022 | 1,844,885 | 2022-06-09 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/81970ecd-5487-4727-8a90-e9ffbe67761d/download/mai-2022.zip |
| mai-2023.zip | Mai 2023 | 1,956,669 | 2023-06-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/a17f3e5a-3660-489d-a633-7b78a024e93d/download/mai-2023.zip |
| mai-2024.zip | Mai 2024 | 2,170,019 | 2024-06-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/bec3732c-7ea8-4247-8ba0-6eda61b7af8f/download/mai-2024.zip |
| mars-2022.zip | Mars 2022 | 1,694,471 | 2022-04-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/80387d53-cb07-479c-acec-bb3eea4abfc0/download/mars-2022.zip |
| mars-2023.zip | Mars 2023 | 2,037,769 | 2023-04-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/7c4b1ec1-e057-42af-8234-5e2dd3eede6b/download/mars-2023.zip |
| mars-2024.zip | Mars 2024 | 1,948,169 | 2024-04-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/adbf7e57-8650-4898-85e1-d507ec81f554/download/mars-2024.zip |
| novembre-2021.zip | Novembre 2021 | 1,448,929 | 2021-12-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/bfdeea3e-a25d-4360-847b-ae6f78498488/download/novembre-2021.zip |
| novembre-2022.zip | Novembre 2022 | 1,515,245 | 2022-12-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/e8459ab0-fa2d-45ec-b630-be2e0d40ccdd/download/novembre-2022.zip |
| novembre-2023.zip | Novembre 2023 | 1,567,357 | 2023-12-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/3ab85685-66d3-42c7-81ae-7903b87a3320/download/novembre-2023.zip |
| octobre-2021.zip | Octobre 2021 | 1,347,823 | 2021-11-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/1b31c723-6699-4d88-8f64-a2d7406dad7a/download/octobre-2021.zip |
| octobre-2022.zip | Octobre 2022 | 1,432,947 | 2022-11-08 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/ebc77c46-bb27-4bad-bd1f-6dd63a54e773/download/octobre-2022.zip |
| octobre-2023.zip | Octobre 2023 | 1,705,657 | 2023-11-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/a477e7e1-5f5c-43c3-b982-5438c9de3ab0/download/octobre-2023.zip |
| septembre-2021.zip | Septembre 2021 | 1,365,418 | 2021-10-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/a45e0aba-72b2-40eb-99e1-e52ff0d57f65/download/septembre-2021.zip |
| septembre-2022.zip | Septembre 2022 | 1,441,959 | 2022-10-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/1a33c267-d606-4307-8396-0995c5a7a344/download/septembre-2022.zip |
| septembre-2023.zip | Septembre 2023 | 1,530,958 | 2023-10-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/24d6cbb0-cf05-4167-a352-f1ad9fa149b3/download/septembre-2023.zip |

(`json_mensuel_20230101_20240430.zip` is a JSON re-export of the 16 monthly JSON files 2023-01…2024-04 — 61.8 MB, extracted to `downloads/seao_quebec/json_reexport/reexport_*.json` and loaded as well.)

### 1b. JSON (OCDS-inspired) files — all 69 monthly files 2021-03 → 2026-09 plus the 3 weekly files after the last monthly one
72 files, 3.82 GB, downloaded 2026-10-25T12:20:52Z–12:28:30Z (log `logs/download_json.log`). CKAN's `size` metadata is stale by ~86 bytes on
some files, so the downloader accepts |size−ckan| ≤ 4 KB when curl succeeds and the JSON tail is well-formed; every file parsed completely with `ijson`
(1,039,974 releases in total incl. re-export; 414,002 distinct `ocid`). Two months exist twice on CKAN (Feb-2025 and Aug-2025, different resource ids);
both copies were downloaded (second copy prefixed with the resource id) and loaded. The earlier weekly files (2021-04 → 2026-09-27) are subsumed by
the monthly files (the monthly file is the consolidated view of the month; verified by sampling) and were not downloaded.

| file | bytes | CKAN last_modified | URL |
|---|---|---|---|
| 44d4b475_mensuel_20250201_20250301.json | 83,560,579 | 2025-04-03 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/44d4b475-8654-4447-9e64-ed708cc19642/download/mensuel_20250201_20250301.json |
| 95858f9c_mensuel_20250801_20250831.json | 59,774,031 | 2025-09-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/95858f9c-81c9-4555-a109-167cc6d73946/download/mensuel_20250801_20250831.json |
| hebdo_20260928_20261004.json | 19,279,996 | 2026-10-05 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/048e71e2-e17d-46bc-b5a6-096b00aa9ca0/download/hebdo_20260928_20261004.json |
| hebdo_20261005_20261011.json | 19,423,914 | 2026-10-12 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/868890cd-7846-4ee5-a8ed-933294f8d346/download/hebdo_20261005_20261011.json |
| hebdo_20261012_20261018.json | 16,854,444 | 2026-10-19 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/7c3b4d4b-e548-40d3-87e3-1a71d2c9f9f6/download/hebdo_20261012_20261018.json |
| mensuel_20210301_20210331.json | 33,889,525 | 2021-05-14 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/291d8cc0-5c6b-4ced-a8d0-d7b880a33809/download/mensuel_20210301_20210331.json |
| mensuel_20210401_20210430.json | 35,901,460 | 2021-05-14 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/e8246369-6b50-4e10-bc7f-8e4e2804c892/download/mensuel_20210401_20210430.json |
| mensuel_20210501_20210531.json | 37,016,382 | 2021-06-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/7f900036-6579-4765-bc0c-c73b4ff77a9e/download/mensuel_20210501_20210531.json |
| mensuel_20210601_20210630.json | 36,908,439 | 2021-07-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/48561625-a93c-4029-8e92-25ed9d901f43/download/mensuel_20210601_20210630.json |
| mensuel_20210701_20210731.json | 27,246,088 | 2021-08-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/ef01e892-da47-4e50-90f9-19cb04113048/download/mensuel_20210701_20210731.json |
| mensuel_20210801_20210831.json | 24,480,662 | 2021-09-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/db2a850d-29f3-406a-a871-da5af924d3bf/download/mensuel_20210801_20210831.json |
| mensuel_20210901_20210930.json | 30,537,673 | 2021-10-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/9b67b2dc-4582-4962-8de8-79cae3ea67a3/download/mensuel_20210901_20210930.json |
| mensuel_20211001_20211031.json | 28,993,409 | 2021-11-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/eafdb003-df33-4b28-89d5-0df7e4f24143/download/mensuel_20211001_20211031.json |
| mensuel_20211101_20211130.json | 31,623,157 | 2021-12-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/7bce77da-346c-4c0d-973d-2ee30f2b8de7/download/mensuel_20211101_20211130.json |
| mensuel_20211201_20211231.json | 29,159,826 | 2022-01-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/29680aa9-96a0-4b6b-b8ca-2b824baf717a/download/mensuel_20211201_20211231.json |
| mensuel_20220101_20220131.json | 26,912,761 | 2022-02-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/e068da1e-51be-4db1-981b-ce489cc26af1/download/mensuel_20220101_20220131.json |
| mensuel_20220201_20220228.json | 30,098,923 | 2022-03-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/a053dd62-3baa-448e-be19-00b810cb09f2/download/mensuel_20220201_20220228.json |
| mensuel_20220301_20220331.json | 37,122,181 | 2022-04-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/0b558a7a-a85b-4d36-8ce0-bc1507fd335f/download/mensuel_20220301_20220331.json |
| mensuel_20220401_20220430.json | 34,873,260 | 2022-05-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/5c9a8af2-fe4c-414d-8b57-a3cb0ac79fa4/download/mensuel_20220401_20220430.json |
| mensuel_20220501_20220531.json | 40,709,530 | 2022-06-09 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/4e39ae6c-f32e-49d5-9b2b-5574a30e9e2b/download/mensuel_20220501_20220531.json |
| mensuel_20220601_20220630.json | 35,915,156 | 2022-07-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/c45f5c22-a9b0-436c-95cd-745f1fc297ab/download/mensuel_20220601_20220630.json |
| mensuel_20220701_20220731.json | 29,389,961 | 2022-08-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/9c985fbe-4b82-4bf5-91f4-33cd8124b65b/download/mensuel_20220701_20220731.json |
| mensuel_20220801_20220831.json | 29,104,343 | 2022-09-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/2b8ee577-3414-4378-9c32-c940c6f5716c/download/mensuel_20220801_20220831.json |
| mensuel_20220901_20220930.json | 31,421,092 | 2022-10-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/c3d8869a-61f7-4c0d-8bd2-c18f70351a82/download/mensuel_20220901_20220930.json |
| mensuel_20221001_20221031.json | 32,475,780 | 2022-11-08 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/78f8aff0-1282-4bd7-817d-a5eecce526dc/download/mensuel_20221001_20221031.json |
| mensuel_20221101_20221130.json | 34,875,199 | 2022-12-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/884fdb17-5ec7-4419-bf8b-6f93e84a9ea1/download/mensuel_20221101_20221130.json |
| mensuel_20221201_20221231.json | 32,906,375 | 2023-01-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/1af71c82-fd74-45b1-bf55-90599eb1469f/download/mensuel_20221201_20221231.json |
| mensuel_20230101_20230131.json | 31,610,689 | 2023-02-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/fab8c266-71f6-47ee-a88b-421900d99eda/download/mensuel_20230101_20230131.json |
| mensuel_20230201_20230228.json | 33,688,729 | 2023-03-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/2a738935-88b7-494f-a89a-319a1d121204/download/mensuel_20230201_20230228.json |
| mensuel_20230301_20230331.json | 41,586,909 | 2023-04-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/7c00c0af-a876-4d22-a012-02d0e106f955/download/mensuel_20230301_20230331.json |
| mensuel_20230401_20230430.json | 36,255,287 | 2023-05-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/f28efa2d-9842-40fc-a166-35b618206d7d/download/mensuel_20230401_20230430.json |
| mensuel_20230501_20230531.json | 41,565,887 | 2023-06-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/12e4551d-80bd-4961-88e8-f43cd5394112/download/mensuel_20230501_20230531.json |
| mensuel_20230601_20230630.json | 37,723,769 | 2023-07-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/6cde096a-56fc-49b7-bdf6-4602de4d77bc/download/mensuel_20230601_20230630.json |
| mensuel_20230701_20230731.json | 36,665,079 | 2023-08-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/b194e792-3ffe-4c38-966d-b8ec4b0b0966/download/mensuel_20230701_20230731.json |
| mensuel_20230801_20230831.json | 32,726,606 | 2023-09-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/4b46bc6d-4a43-47ce-b0e2-c36a3aa7e92a/download/mensuel_20230801_20230831.json |
| mensuel_20230901_20230930.json | 29,829,114 | 2023-10-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/3781ad39-1757-4b71-bc46-fa3b383954c5/download/mensuel_20230901_20230930.json |
| mensuel_20231001_20231031.json | 36,160,995 | 2023-11-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/b5fa5b13-f042-4d2d-96da-baad81cf569e/download/mensuel_20231001_20231031.json |
| mensuel_20231101_20231130.json | 32,874,564 | 2023-12-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/7a197967-226f-4735-bc45-6ddfc1347a11/download/mensuel_20231101_20231130.json |
| mensuel_20231201_20231231.json | 31,330,450 | 2024-01-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/31bf01f0-f347-4b69-a5cd-389eaac145f7/download/mensuel_20231201_20231231.json |
| mensuel_20240101_20240131.json | 38,002,113 | 2024-02-07 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/5bbc4b40-1127-4530-bade-02a2fdd3c680/download/mensuel_20240101_20240131.json |
| mensuel_20240201_20240229.json | 40,793,280 | 2024-03-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/c0626500-4cb8-478b-9bdc-d9a574dbdaeb/download/mensuel_20240201_20240229.json |
| mensuel_20240301_20240331.json | 38,527,119 | 2024-04-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/4fa973fc-1f4d-4eff-a7b8-574aa5b0215a/download/mensuel_20240301_20240331.json |
| mensuel_20240401_20240430.json | 46,212,231 | 2024-05-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/1fecfb32-6f8a-4f8a-bb72-1371176a4721/download/mensuel_20240401_20240430.json |
| mensuel_20240501_20240531.json | 48,548,664 | 2024-06-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/9ebbb969-c178-4252-ac1e-8794a261ed70/download/mensuel_20240501_20240531.json |
| mensuel_20240601_20240630.json | 65,291,885 | 2024-07-31 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/f25e1348-4622-409c-9677-7dc1502e7a47/download/mensuel_20240601_20240630.json |
| mensuel_20240701_20240731.json | 65,813,819 | 2024-08-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/f48b3aac-382d-4e41-90d7-235946179235/download/mensuel_20240701_20240731.json |
| mensuel_20240801_20240831.json | 55,430,530 | 2024-09-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/fc2b3c2e-a04a-49c4-88a0-e1d3d8deb4bf/download/mensuel_20240801_20240831.json |
| mensuel_20240901_20240930.json | 57,943,083 | 2024-10-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/2a10a65b-fd6a-495d-9c4d-a1e6d15ddbac/download/mensuel_20240901_20240930.json |
| mensuel_20241001_20241031.json | 64,873,283 | 2024-11-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/d1f7b3e5-0073-4eef-9a0a-043fdccfa693/download/mensuel_20241001_20241031.json |
| mensuel_20241101_20241130.json | 64,407,515 | 2025-02-13 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/e764ec5e-1429-472b-9938-b024910252fa/download/mensuel_20241101_20241130.json |
| mensuel_20241201_20241231.json | 56,704,240 | 2025-01-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/54ea88df-eace-4594-b48b-37fb38072fc7/download/mensuel_20241201_20241231.json |
| mensuel_20250101_20250131.json | 64,259,888 | 2025-02-13 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/674daf95-21bb-4526-834e-f2978c365fe2/download/mensuel_20250101_20250131.json |
| mensuel_20250201_20250301.json | 86,017,645 | 2025-04-09 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/08c3c0f7-6eb7-4245-88bf-93a6f5020491/download/mensuel_20250201_20250301.json |
| mensuel_20250301_20250331.json | 106,858,655 | 2025-04-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/4ea647f4-91ee-4490-9192-b663a5c4f100/download/mensuel_20250301_20250331.json |
| mensuel_20250401_20250430.json | 85,109,998 | 2025-05-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/16f7ef55-dd9a-4611-a2e3-a1c419577ca4/download/mensuel_20250401_20250430.json |
| mensuel_20250501_20250531.json | 84,428,350 | 2025-06-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/ba993578-b900-4b29-8818-534406b4d033/download/mensuel_20250501_20250531.json |
| mensuel_20250601_20250630.json | 77,655,107 | 2025-07-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/62aaeb66-11ce-44c8-adb4-86a4a90d677e/download/mensuel_20250601_20250630.json |
| mensuel_20250701_20250731.json | 75,480,287 | 2025-08-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/12a9b716-bb60-4ed4-b398-ce5b56ead2b4/download/mensuel_20250701_20250731.json |
| mensuel_20250801_20250831.json | 59,774,057 | 2025-09-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/81d7ef09-b950-4013-831f-86edaba11807/download/mensuel_20250801_20250831.json |
| mensuel_20250901_20250930.json | 217,711,279 | 2025-10-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/ec48c72b-f484-41fa-a324-3e0cd17ccc21/download/mensuel_20250901_20250930.json |
| mensuel_20251001_20251031.json | 66,312,761 | 2025-11-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/ad664e0a-d0b9-44e4-8599-44c9fb993190/download/mensuel_20251001_20251031.json |
| mensuel_20251101_20251130.json | 75,950,797 | 2026-08-13 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/f99004d8-d8c7-41c5-ad6b-f91486656675/download/mensuel_20251101_20251130.json |
| mensuel_20251201_20251231.json | 86,758,824 | 2026-08-13 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/0ca534c1-5f62-43f4-8d9b-c14a32e25a19/download/mensuel_20251201_20251231.json |
| mensuel_20260101_20260131.json | 86,149,104 | 2026-08-14 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/80f37f9e-d7b2-4fb8-b8aa-c5c31202e7d9/download/mensuel_20260101_20260131.json |
| mensuel_20260201_20260228.json | 91,151,090 | 2026-08-14 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/80255833-2e06-486f-b877-c1621f42c444/download/mensuel_20260201_20260228.json |
| mensuel_20260301_20260331.json | 109,457,690 | 2026-08-14 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/e023cdae-6ccf-4c21-b085-78011de234b7/download/mensuel_20260301_20260331.json |
| mensuel_20260401_20260430.json | 95,682,672 | 2026-05-30 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/563e23ce-20fc-470e-a147-0ac351b21db9/download/mensuel_20260401_20260430.json |
| mensuel_20260501_20260531.json | 85,810,639 | 2026-06-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/0f79befd-1968-4122-89ee-952626262419/download/mensuel_20260501_20260531.json |
| mensuel_20260601_20260630.json | 85,971,145 | 2026-07-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/eb34be05-2d89-4e75-a321-38642f0f9c53/download/mensuel_20260601_20260630.json |
| mensuel_20260701_20260731.json | 74,581,311 | 2026-08-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/a336dd6c-cf8a-44f4-b3bb-5425c3274428/download/mensuel_20260701_20260731.json |
| mensuel_20260801_20260831.json | 64,216,703 | 2026-09-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/b11b4088-f193-4ae8-83ec-d5e113bb164c/download/mensuel_20260801_20260831.json |
| mensuel_20260901_20260930.json | 68,208,314 | 2026-10-01 | https://www.donneesquebec.ca/recherche/dataset/d23b2e02-085d-43e5-9e6e-e1d558ebfdd5/resource/b7ac3d06-bdc0-492d-8801-c7f650eba2ce/download/mensuel_20260901_20260930.json |

Scripts: `/home/claude/contracts/scripts/seao_quebec/` — `list_resources.py`, `download.py`, `extract_zips.py`, `profile_xml.py`, `load_xml.py` (lxml
`iterparse` + `clear()`, into SQLite `downloads/seao_quebec/staging/seao_xml.sqlite`), `load_json.py` (ijson streaming, into `staging/seao_json.sqlite`),
`emit.py` (merge + status logic → JSONL, progressive writes/flush every 1,000 records), `qa.py`, `samples.py`. Everything was run as `python3 -I script.py <paths>`.

## 2. Element dictionary (from the two specification PDFs, confirmed against the files)

**XML `Avis_*.xml` → `<export datedebut datefin>` / `<avis>`** (one per contract-conclusion publication; contains ALL bidders):
`numeroseao` (SEAO numeric notice id — the join key for everything), `numero` (organisation's own reference, ≤25 chars), `organisme` (buyer name),
`municipal` (0/1), buyer `adresse1/adresse2/ville/province/pays/codepostal`, `titre`, `type` (3 = contract after public tender, 9 = gré à gré,
10 = after tender by invitation, 11 = achat mandaté / regroupement [not in the 2021 spec, label taken from the JSON feed], 14 = tender by invitation
published in SEAO, 16 = transport-infrastructure contract, 17 = public tender not published in SEAO), `nature` (1 goods, 2 services, 3 construction,
5 other, 6 concession, 7/8 sale of immovable/movable property), `precision` (for services: 1 professional, 2 technical; for "other": free text),
`categorieseao` (not in spec; SEAO category code+label e.g. "C03 - Autres travaux de construction"), `datepublication`, `datefermeture`,
`datesaisieouverture`, `datesaisieadjudication` (date the award/conclusion was entered), `dateadjudication` (**contract conclusion date**),
`regionlivraison` (delivery region codes 1–19), `unspscprincipale`, `disposition` (legal provision for non-competitive award, Annexe C),
`hyperlienseao` (not in spec; present in 100 % of avis: `https://www.seao.ca/OpportunityPublication/avisconsultes.aspx?ItemId=<uuid>`),
`fournisseurs/fournisseur[]`: `nomorganisation`, `adresse1/2`, `ville`, `province`, `pays` (country code, Annexe A: `CAN`, `USA`, ISO-2 for others),
`codepostal`, `neq` (Numéro d'entreprise du Québec, 10 digits), `admissible`, `conforme`, `adjudicataire` (1 = awarded), `montantsoumis`,
`montantssoumisunite` (1 = $, 2 = $/year, 3 = $/km … 11 = points), `montantcontrat` (**contract amount, CAD**), `montanttotalcontrat` (not in spec).
**There is no planned end date, duration or contract period anywhere in the XML format.**

**XML `Depenses_*.xml`** → `<avis>` {`numeroseao`, `numero`, `depenses/depense[]` {`datedepense`, `datepublicationdepense`, `montantdepense`, `description`, `nomcontractant`, `neqcontractant`}}.
`DepensesRevisions` gives the complete replacement list for a notice ("an avis appearing without depenses means all expenses were withdrawn").

**XML `Contrats_*.xml` = information finale (closure)** → `<contrat>` {`numeroseao`, `numero`, `datefinale` (actual end date), `datepublicationfinale`,
`montantfinal` (final total paid), `nomcontractant`, `neqcontractant`}. Published once the contract is finished; one row per awarded supplier of the notice.
`ContratsRevisions` = corrected closure rows.

**JSON (`hebdo_/mensuel_*.json`)** — OCDS 1.1-inspired release packages: `releases[]` {`ocid` = `ocds-ec9k95-<numeroseao>`, `id` (release id =
publication timestamp YYYYMMDDhhmmss in the new system), `date`, `tag[]` (tender/tenderUpdate/tenderCancellation/award/awardUpdate/awardCancellation/
contract/contractUpdate/contractTermination), `parties[]` {name, id (`OP-<n>` buyer / `FO-<NEQ>` supplier), address{streetAddress, locality, region,
postalCode, countryName}, roles[], details{municipal | neq}}, `buyer`, `tender` {id (= `numero`), title, status, procuringEntity, items[]
{UNSPSC classification + additionalClassifications}, procurementMethod (open/limited/direct/selective), procurementMethodDetails,
procurementMethodRationale (= disposition), mainProcurementCategory, additionalProcurementCategories, tenderPeriod, numberOfTenderers, tenderers[],
documents[].url (= notice URL), lots[] {contractPeriod.startDate/endDate}, value/minValue}, `bids[]`, `awards[]` {id, status (active/cancelled/pending),
date (= dateadjudication), value{amount, currency, totalAmount}, suppliers[]}, `contracts[]` {id, awardID, status (**active/terminated/cancelled/pending**),
**`period.endDate`**, value{amount}, `dateSigned` (= conclusion date), amendments[] {id, rationale, date}}, `relatedProcesses[]`. The spec documents
`contracts.implementation.transactions` for supplementary expenses, but **no release in any file carries `implementation`** — supplementary expenses
exist only in the XML `Depenses` files (until 2024-05) and, since June 2024, as `contracts[].amendments[]` (rationale text, no amount).

Key empirical finding on `contracts[].period.endDate`: the spec calls it "date de fin réelle". In the data it is populated for 100 % of `terminated`
contracts (= actual end, equals XML `datefinale` where both exist, checked on numeroseao 304462) **and for ~45 % of `active` contracts, where it is a
future/planned end date** (e.g. a 2026-06 contract with endDate 2027-06-12 and `dureePrevueSansOptions` = 12 months in the live SEAO API). So an
open contract with `endDate ≥ today` is a genuinely published planned end date, and an open contract with `endDate < today` is a contract whose
planned term has already expired without a closure record.

## 3. How "Canadian vendor" was determined

Field: XML `fournisseur/pays` of the awarded supplier (`adjudicataire = 1`); for notices only in the JSON feed, `parties[role=supplier].address.countryName`.
Distinct values and counts over all awarded-supplier lines evaluated (XML lines vs. JSON lines, ≥ 50 occurrences shown; the full list is in
`downloads/seao_quebec/logs/emit_stats.json` → `pays_values`):

| feed | value | awarded lines |
|---|---|---|
| XML | `'CAN'` | 565,810 |
| JSON | `'CAN'` | 150,834 |
| XML | `'USA'` | 13,031 |
| JSON | `'None'` | 12,747 |
| XML | `''` | 6,973 |
| JSON | `'USA'` | 2,975 |
| XML | `'FR'` | 1,394 |
| XML | `'CA'` | 1,217 |
| XML | `'GB'` | 491 |
| JSON | `'FR'` | 373 |
| XML | `'DE'` | 359 |
| XML | `'UM'` | 184 |
| JSON | `'GB'` | 167 |
| XML | `'CH'` | 136 |
| XML | `'IE'` | 132 |
| XML | `'NL'` | 126 |
| XML | `'CN'` | 114 |
| XML | `'BE'` | 107 |
| JSON | `'DE'` | 98 |
| XML | `'IT'` | 68 |
| XML | `'MX'` | 67 |
| XML | `'AU'` | 59 |
| JSON | `'NL'` | 55 |
| XML | `'FI'` | 53 |
| XML | `'DK'` | 53 |
| JSON | `'BE'` | 52 |
| XML | `'US'` | 50 |
| JSON | `'CH'` | 50 |

Rule: `CAN` → Canada (official Annexe A code). `CA` (1,217 XML lines) → Canada: every such line carries a Canadian province code (QC/ON) and/or a
Canadian postal code, so it is a data-entry variant, not the US state "CA". Blank (`''` 6,973 XML lines, `None` 12,747 JSON lines) → Canada **only if**
the supplier's `province` is a Canadian province code or the postal code matches `A9A 9A9` (7 lines in total qualified); the other blank-country lines
(mostly 2011–2012 municipal records with no address at all, and recent individuals/sole traders without address) were **excluded** as "country unknown".
`USA`, `US`, `usa`, `UM`, `GBR`, `FRA`, `ALL`, `EUR`, `UNK` etc. → not Canada → excluded (40,857 supplier lines in total excluded for country).
`vendor.country_basis` on every record states which field/rule applied.

## 4. How "ongoing" was determined

SEAO publishes no planned end date in the XML; the only closure signal is the *information finale* (`Contrats_*.xml`, or `contracts[].status =
terminated` + `period.endDate` in the JSON). The JSON feed additionally gives a planned `period.endDate` on many open contracts. Logic, per
(numeroseao × awarded supplier):

1. Build the supplier universe from the latest XML version of the notice (Avis then AvisRevisions, latest export period wins) plus the latest OCDS
   release of the same `ocid` (latest = highest file order, then highest release id; if that snapshot lists no contracts at all, the latest
   contract-bearing release is used and a CAVEAT is written into `status_basis`). Suppliers are matched XML↔JSON by NEQ, else by normalised name,
   else (rename/NEQ correction between systems) by identical amount or as the single leftover pair (1,118 pairings, flagged with NOTE in `status_basis`).
2. **Exclude** if: vendor not Canadian; an XML closure row (`Contrats`/`ContratsRevisions`) matches the supplier (by NEQ, else name, else single-supplier
   fallback: 256,451 lines); the OCDS contract line(s) of the supplier are `terminated`/`cancelled` or the award is `cancelled` (97,101); the OCDS
   planned `period.endDate` of the still-open contract is `< 2026-10-25` (30,758 — term expired, no closure published); the tender is `cancelled` and the
   supplier never appeared in the XML (618); the supplier was dropped from the awards in the latest OCDS release (1,538, "superseded"); or the conclusion
   date is after 2026-10-25 (1).
3. **`ongoing`** (26,261): the supplier's open OCDS contract has `period.endDate ≥ 2026-10-25` and `dateSigned ≤ 2026-10-25`. `contract.dates.end` = that
   date. `status_basis` quotes it.
4. **`ongoing_inferred`** (305,149): concluded ≤ 2026-10-25 and no closure anywhere — status_basis = "contract concluded on <date>; no final-information
   (closure) record published as of retrieval (…)" and spells out whether the notice is JSON-backed (OCDS status active, no endDate) or XML-only
   (notice absent from the OCDS feed, so no post-May-2024 closure could have been detected). `contract.dates.signed` (= `dateadjudication` /
   `dateSigned`) is always set so the orchestrator can judge age — **see the year table below: ~113 k of these were concluded before 2014 and are
   almost certainly finished contracts whose organisation never published the information finale** (closure publication is far from universal:
   272,500 closures vs 646,562 awarded lines over 2009–2024-05).
5. No `end_date_unknown` records are emitted: every kept record has either a planned end date or the documented "no closure record" convention.

## 5. Resulting counts

Notices processed: 740,570 distinct `numeroseao` (569,463 in XML, 414,002 in JSON, 243,211 in both); awarded supplier lines: 758,734.

| status | records |
|---|---|
| `ongoing` (planned end date ≥ today, from OCDS `period.endDate`) | 26,261 |
| `ongoing_inferred` (no closure record) — of which JSON-backed / XML-only | 305,149 — 125,766 / 179,383 |
| **total written** | **331,410** |
| excluded: closure (information finale) in XML | 256,451 |
| excluded: OCDS terminated/cancelled | 97,101 |
| excluded: planned end date already past | 30,758 |
| excluded: vendor not Canada / country unknown | 40,857 |
| excluded: superseded in later OCDS award list | 1,538 |
| excluded: tender cancelled / future conclusion | 618 / 1 |
| notices with no awarded supplier (tender-only / cancelled / "Divers fournisseurs" without lines) | 26,133 |

Records by year of contract conclusion (`contract.dates.signed`):

| year | ongoing | ongoing_inferred | total |
|---|---|---|---|
| 0001 | 0 | 1 | 1 |
| 1992 | 0 | 1 | 1 |
| 2000 | 0 | 26 | 26 |
| 2001 | 0 | 12 | 12 |
| 2002 | 0 | 4 | 4 |
| 2003 | 0 | 12 | 12 |
| 2004 | 0 | 10 | 10 |
| 2005 | 0 | 55 | 55 |
| 2006 | 0 | 45 | 45 |
| 2007 | 0 | 122 | 122 |
| 2008 | 0 | 2,040 | 2,040 |
| 2009 | 0 | 16,943 | 16,943 |
| 2010 | 0 | 17,135 | 17,135 |
| 2011 | 0 | 19,817 | 19,817 |
| 2012 | 0 | 19,409 | 19,409 |
| 2013 | 0 | 15,888 | 15,888 |
| 2014 | 0 | 12,721 | 12,721 |
| 2015 | 0 | 12,609 | 12,609 |
| 2016 | 0 | 11,737 | 11,737 |
| 2017 | 0 | 12,487 | 12,487 |
| 2018 | 0 | 13,442 | 13,442 |
| 2019 | 11 | 13,532 | 13,543 |
| 2020 | 30 | 15,497 | 15,527 |
| 2021 | 74 | 18,850 | 18,924 |
| 2022 | 178 | 22,295 | 22,473 |
| 2023 | 1,165 | 21,768 | 22,933 |
| 2024 | 5,266 | 14,778 | 20,044 |
| 2025 | 8,749 | 21,363 | 30,112 |
| 2026 | 10,788 | 22,463 | 33,251 |
| unknown | 0 | 87 | 87 |

Exclusions by conclusion year (closure_xml / closure_json / planned_end_past / superseded / tender_cancelled):

| year | closure XML | closure JSON | planned end past | superseded | tender cancelled |
|---|---|---|---|---|---|
| 0001 | 0 | 0 | 0 | 0 | 1 |
| 1988 | 0 | 0 | 0 | 0 | 1 |
| 1998 | 0 | 1 | 0 | 0 | 0 |
| 2000 | 1 | 0 | 0 | 0 | 0 |
| 2001 | 1 | 0 | 0 | 0 | 0 |
| 2002 | 6 | 1 | 0 | 0 | 1 |
| 2003 | 1 | 0 | 0 | 0 | 0 |
| 2004 | 22 | 1 | 0 | 0 | 0 |
| 2005 | 45 | 3 | 3 | 0 | 0 |
| 2006 | 64 | 7 | 2 | 0 | 0 |
| 2007 | 104 | 9 | 0 | 0 | 0 |
| 2008 | 292 | 20 | 0 | 1 | 0 |
| 2009 | 1,042 | 31 | 0 | 0 | 2 |
| 2010 | 1,811 | 28 | 2 | 1 | 0 |
| 2011 | 9,117 | 85 | 2 | 9 | 0 |
| 2012 | 12,826 | 163 | 7 | 22 | 2 |
| 2013 | 18,468 | 321 | 2 | 20 | 2 |
| 2014 | 21,108 | 500 | 3 | 52 | 1 |
| 2015 | 20,407 | 680 | 3 | 72 | 3 |
| 2016 | 20,589 | 722 | 4 | 95 | 5 |
| 2017 | 22,088 | 1,106 | 8 | 74 | 3 |
| 2018 | 23,399 | 1,680 | 20 | 150 | 4 |
| 2019 | 25,036 | 3,360 | 848 | 145 | 3 |
| 2020 | 25,125 | 4,882 | 1,585 | 370 | 0 |
| 2021 | 23,242 | 8,471 | 1,915 | 237 | 8 |
| 2022 | 19,097 | 12,708 | 1,840 | 182 | 15 |
| 2023 | 11,692 | 19,689 | 5,244 | 103 | 71 |
| 2024 | 826 | 21,415 | 8,855 | 4 | 158 |
| 2025 | 0 | 17,332 | 7,433 | 0 | 242 |
| 2026 | 0 | 3,883 | 2,982 | 0 | 90 |
| unknown | 42 | 3 | 0 | 1 | 6 |

Buyer types (heuristic from name + `municipal` flag; stored in `buyer.type`): city 191,473 · hospital/health & social services 105,513 · school board/college
99,255 · provincial ministry 87,540 · university 58,739 · municipality 44,047 · crown corporation/state enterprise 38,561 · provincial agency 33,460 ·
other Québec public body 27,526 · municipal agency 20,554 · MRC 7,769 (counted over all supplier lines before exclusion).

QA (`qa.py`): 331,410 lines, 0 invalid JSON, 331,410 unique `record_id`, 100 % have `record_url`, 1,603 records with `value = null` (OCDS lines whose
`value` object has only `currency` — amount withheld at source; the raw object is kept), 87 without a conclusion date, 69,116 without NEQ (individuals,
out-of-Québec suppliers, or NEQ not entered). Median record size 6.4 KB (p99 30 KB, max 376 KB for notices with many bidders).

## 6. `record_url`

Every XML avis carries `hyperlienseao` = `https://www.seao.ca/OpportunityPublication/avisconsultes.aspx?ItemId=<uuid>`. The host `www.seao.ca`
no longer resolves (DNS failure / proxy 502 on 2026-10-25); SEAO moved to `https://seao.gouv.qc.ca/` in June 2024 and the OCDS feed's
`tender.documents[].url` uses `https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=<uuid>` with the **same ItemId uuids** for old notices
(checked: 2009 notice 182219, uuid 607dff21-…, and 2009 notice 304462, uuid 8524186d-…). `record_url` is therefore
`https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=<uuid>` where uuid comes from `hyperlienseao` (XML) or `tender.documents[0].url` (JSON);
the original `hyperlienseao` is kept in `contract.related.hyperlienseao_original` and the uuid in `contract.identifiers.seao_item_id`.
Verification (curl, 2026-10-25): `https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=49ae86a1-c09e-4353-b914-cd491d3b6c90` → HTTP 200
(React single-page app shell, 2,337 B — the notice content is loaded client-side), and the backend it calls,
`https://api.seao.gouv.qc.ca/prod/api/avis/49ae86a1-c09e-4353-b914-cd491d3b6c90/consulter` → HTTP 200 JSON with `avisResumeInformation.id = 20150013`
and `titre = "Contrat à exécution sur demande d'un entrepreneur en climatisation pour les postes de contrôle routier Québec"`, matching record
`seao_quebec:20150013:av-tech-inc`. The same check succeeded for 2009 uuids (8524186d-… → id 304462 "Caserne de pompier (route 329)").
The live API also exposes `dureePrevueSansOptions` (expected duration in months) and `/consulter-conclusion-contrat`, `/consulter-information-finale-publie-by-avis`
per notice — not harvested (would be ~330 k requests) but documented here as a possible enrichment for the inferred records.

## 7. Record layout specifics

- `record_id` = `seao_quebec:<numeroseao>:<slug of supplier name>` (slug ≤ 60 chars; when two awarded suppliers of the same notice collide on the slug,
  `-<NEQ>` or `-<sha1[:8] of full name>` is appended). One record per notice × awarded supplier; a supplier awarded several lines/lots in the same notice
  gets one record with amounts summed (`status_basis` says so) and all lines in `raw.fournisseur_lines` / `raw.ocds_supplier_contracts`.
- `contract.identifiers`: `numeroseao`, `numero` (organisation's number = OCDS `tender.id`), `ocid`, `ocds_contract_ids`, `ocds_award_ids`, `seao_item_id`.
- `contract.value` = XML `montantcontrat` (sum over the supplier's lines), else OCDS `contracts[].value.amount` (else `awards[].value.amount`);
  `value_detail` also carries `montantsoumis`, `montanttotalcontrat` (when non-zero), the OCDS amount, `ocds_award_totalAmount`, and the summed
  `supplementary_expenses_total`/`count`. `related.montantssoumisunite_code` flags non-dollar units (2 = $/year, 8 = %, 10 = $/h, 11 = points …) — for
  those the "amount" is a rate, not a total.
- `contract.dates`: `published` = `datesaisieadjudication` (XML) or the first contract-bearing OCDS release timestamp; `signed` = `start` = `dateadjudication`
  / `dateSigned`; `end` = OCDS planned `period.endDate` (only on `ongoing`); `amended_last` = latest supplementary-expense or amendment date;
  plus `tender_published` / `tender_closing`.
- `buyer`: `organisme` name, address, `municipal_flag`, `identifiers.seao_organisation_id` (OCDS `OP-…` id when available), heuristic `type`.
- `vendor`: name, `identifiers.neq` (+ `seao_supplier_id` = OCDS `FO-…`), full address, `country_basis`.
- `raw`: `avis` (full XML notice incl. ALL bidders and their bids, verbatim strings), `avis_appearances` (which files/revisions carried it),
  `fournisseur_lines` (this supplier's awarded lines), `depenses_supplementaires` (list; `_unmatched` for lines naming another contractor),
  `information_finale` (always null for emitted records; `information_finale_unmatched` lists closure rows naming a contractor that matches none of the
  awarded suppliers — 106 notices, flagged with CAVEAT), `ocds_release` (full latest release incl. parties, tender, bids, awards, contracts, relatedProcesses),
  `ocds_release_history` (all release ids/dates/tags/files seen for the ocid), `ocds_supplier_contracts/awards/party`, `code_labels`.

## 8. Known gaps and limits

- **Closure publication is incomplete and late.** Only 272,500 information-finale rows exist for 646,562 XML awarded lines; closures were published up to
  15 years after conclusion (e.g. 2009 contract 304462 closed 2010-08-10, published 2024-05-16). Hence `ongoing_inferred` records concluded before ~2020
  (≈ 180 k) are mostly finished contracts whose organisation never filed the closure — the by-year table should be used to cut. Organisations that never
  publish closures cannot be identified from the feed itself; the pattern is visible per buyer by comparing `raw.information_finale` presence across its notices.
- **Dual systems.** The XML feed ends 2024-05-31 (old SEAO); the JSON feed (new SEAO since June 2024, migrated notices with `numeroseao < 19,000,000`,
  new ones `≥ 20,000,000`) is the only source for closures after May 2024. 326,252 XML notices never appear in the JSON feed, so any closure filed for them
  after May 2024 is invisible → they can only be `ongoing_inferred`. 170,791 notices exist only in JSON.
- **OCDS snapshots are not strictly cumulative**: ~2 % of later releases drop the `contracts[]` (or whole `awards[]`) of an earlier release (e.g. a `tenderUpdate`
  snapshot re-exported without awards), which is why the latest *contract-bearing* release is used with a CAVEAT; and in the 2021–2024-05 old-system
  JSON, ~2,800 `contract`-tagged releases have `awards[]` but no `contracts[]` (treated as award-only, `ongoing_inferred`).
- `period.endDate` on open contracts is missing for ~55 % of new-system contracts and for nearly all pre-2019 ones, so most records are inferred.
- Amounts: 1,603 OCDS contracts have no amount; `montantcontrat` can be 0 or a unit rate (see `montantssoumisunite_code`); "Divers fournisseurs"/placeholder
  suppliers (26,133 notices without an awarded line) are not emitted.
- Blank-country suppliers without province/postal code (≈ 19 k lines, mostly 2011–2012 municipal entries and individuals) were excluded, so a few Canadian
  suppliers may be missing; they cannot be identified by the source's own fields.
- Only the 3 weekly files after 2026-09-30 were loaded (data up to 2026-10-18); anything published 2026-10-19 → 2026-10-25 is not yet in the open data.
- Buyer `type` is a name heuristic (not a source field); buyer identifiers are only available for JSON-backed notices.

## 9. Five sample records (normalized layer; `raw` omitted for brevity)

### Sample `ongoing_json_only` — `seao_quebec:1247955:transport-scolaire-champlain`
```json
{
 "record_id": "seao_quebec:1247955:transport-scolaire-champlain",
 "source": {
  "key": "seao_quebec",
  "name": "Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes",
  "publisher": "Secrétariat du Conseil du trésor (Québec) via Données Québec",
  "dataset_url": "https://www.donneesquebec.ca/recherche/dataset/systeme-electronique-dappel-doffres-seao",
  "record_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c6e2390e-b78f-423d-9191-1f7f130e569d",
  "retrieved_at": "2026-10-25T12:28:30Z"
 },
 "status": "ongoing",
 "status_basis": "OCDS contracts[].period.endDate = 2027-05-21 (planned end date; contract status 'active') is on/after 2026-10-25; contract concluded (dateSigned) 2019-05-21 on/before 2026-10-25; no final-information (closure) record in XML Contrats files nor 'terminated' status in OCDS as of retrieval",
 "contract": {
  "identifiers": {
   "numeroseao": "1247955",
   "numero": "19-107",
   "ocid": "ocds-ec9k95-1247955",
   "ocds_contract_ids": [
    "393950",
    "393951"
   ],
   "ocds_award_ids": [
    "393950",
    "393951"
   ],
   "seao_item_id": "c6e2390e-b78f-423d-9191-1f7f130e569d"
  },
  "title": "Service de transport scolaire-autobus électrique",
  "description": "services; Services de nature technique",
  "instrument_type": "contract",
  "procurement_method": "open",
  "solicitation_procedure": "Avis d’appel d’offres",
  "commodity": {
   "unspsc": "78111802",
   "unspsc_description": "Autobus à horaire fixe",
   "seao_category": "S17 - Services de transport, de voyage et de déménagement"
  },
  "value": 2399952.0,
  "currency": "CAD",
  "value_detail": {
   "ocds_contract_value_amount": 2399952.0
  },
  "dates": {
   "published": "2025-09-20",
   "signed": "2019-05-21",
   "start": "2019-05-21",
   "end": "2027-05-21",
   "amended_last": null,
   "tender_published": "2019-03-29",
   "tender_closing": "2019-04-17"
  },
  "related": {
   "notice_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c6e2390e-b78f-423d-9191-1f7f130e569d",
   "ocds_tender_document_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c6e2390e-b78f-423d-9191-1f7f130e569d"
  }
 },
 "buyer": {
  "name": "Centre de services scolaire  Marguerite-Bourgeoys",
  "country": "CA",
  "type": "school board / college",
  "identifiers": {
   "seao_organisation_id": "OP-47576"
  },
  "address": {
   "line1": "1100, bd de la Côte-Vertu,",
   "line2": null,
   "city": "Montréal",
   "region": "QC",
   "postal_code": "H4L4V1",
   "country": "CAN"
  },
  "contact": {},
  "municipal_flag": "0"
 },
 "vendor": {
  "name": "Transport scolaire Champlain",
  "country": "CA",
  "country_basis": "OCDS parties[role=supplier].address.countryName: supplier country field = \"CAN\" (CAN = Canada per SEAO Annexe A; \"CA\" accepted as Canada: all such rows carry a Canadian province code and/or postal code)",
  "identifiers": {
   "neq": "1174379082",
   "seao_supplier_id": "FO-1174379082"
  },
  "address": {
   "line1": "324 arlington cres,",
   "line2": null,
   "city": "Beaconsfield",
   "region": "QC",
   "postal_code": "H9W2K3",
   "country": "CAN"
  },
  "contact": {}
 },
 "raw_keys_present": {
  "avis": null,
  "avis_appearances": null,
  "fournisseur_lines": null,
  "depenses_supplementaires": "list",
  "depenses_supplementaires_unmatched": null,
  "information_finale": null,
  "information_finale_unmatched": null,
  "ocds_release": "dict",
  "ocds_release_history": "list",
  "ocds_supplier_contracts": "list",
  "ocds_supplier_awards": "list",
  "ocds_supplier_party": "dict",
  "code_labels": null
 }
}
```
(raw omitted here; the full record in the JSONL carries raw.avis / raw.fournisseur_lines / raw.depenses_supplementaires / raw.ocds_release etc. — keys present: depenses_supplementaires:list, ocds_release:dict, ocds_release_history:list, ocds_supplier_contracts:list, ocds_supplier_awards:list, ocds_supplier_party:dict)

### Sample `ongoing_with_xml` — `seao_quebec:1239285:dominion-biologicals-ltee`
```json
{
 "record_id": "seao_quebec:1239285:dominion-biologicals-ltee",
 "source": {
  "key": "seao_quebec",
  "name": "Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes",
  "publisher": "Secrétariat du Conseil du trésor (Québec) via Données Québec",
  "dataset_url": "https://www.donneesquebec.ca/recherche/dataset/systeme-electronique-dappel-doffres-seao",
  "record_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7a74f54e-2e00-4761-b275-de0513268d17",
  "retrieved_at": "2026-10-25T12:28:30Z"
 },
 "status": "ongoing",
 "status_basis": "OCDS contracts[].period.endDate = 2029-06-26 (planned end date; contract status 'active') is on/after 2026-10-25; contract concluded (dateSigned) 2019-06-26 on/before 2026-10-25; no final-information (closure) record in XML Contrats files nor 'terminated' status in OCDS as of retrieval",
 "contract": {
  "identifiers": {
   "numeroseao": "1239285",
   "numero": "2019APP080",
   "ocid": "ocds-ec9k95-1239285",
   "ocds_contract_ids": [
    "396213"
   ],
   "ocds_award_ids": [
    "396213"
   ],
   "seao_item_id": "7a74f54e-2e00-4761-b275-de0513268d17"
  },
  "title": "Analyseurs de banque de sang automatisés",
  "description": "Approvisionnement (biens)",
  "instrument_type": "contract",
  "procurement_method": "open",
  "solicitation_procedure": "Contrat adjugé suite à un appel d'offres public",
  "commodity": {
   "unspsc": "41115803",
   "seao_category": "G21 - Fourniture et équipement médicaux et produits pharmaceutiques",
   "unspsc_description": "Analyseurs pour banques de sang"
  },
  "value": 1920546.68,
  "currency": "CAD",
  "value_detail": {
   "montantcontrat": 1920546.68,
   "montantsoumis": 1920546.68,
   "ocds_contract_value_amount": 2364546.68
  },
  "dates": {
   "published": "2019-06-26",
   "signed": "2019-06-26",
   "start": "2019-06-26",
   "end": "2029-06-26",
   "amended_last": null,
   "tender_published": "2019-04-16",
   "tender_closing": "2019-05-24"
  },
  "related": {
   "hyperlienseao_original": "https://www.seao.ca/OpportunityPublication/avisconsultes.aspx?ItemId=7a74f54e-2e00-4761-b275-de0513268d17",
   "notice_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7a74f54e-2e00-4761-b275-de0513268d17",
   "ocds_tender_document_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7a74f54e-2e00-4761-b275-de0513268d17",
   "delivery_regions": [
    "Chaudière-Appalaches"
   ]
  }
 },
 "buyer": {
  "name": "CISSS de Chaudière-Appalaches",
  "country": "CA",
  "type": "hospital / health and social services institution",
  "identifiers": {
   "seao_organisation_id": "OP-81496"
  },
  "address": {
   "line1": "960 rue de la Concorde",
   "line2": null,
   "city": "Lévis",
   "region": "QC",
   "postal_code": "G6W8A8",
   "country": "CAN"
  },
  "contact": {},
  "municipal_flag": "0"
 },
 "vendor": {
  "name": "Dominion Biologicals ltée.",
  "country": "CA",
  "country_basis": "XML fournisseur/pays: supplier country field = \"CAN\" (CAN = Canada per SEAO Annexe A; \"CA\" accepted as Canada: all such rows carry a Canadian province code and/or postal code)",
  "identifiers": {
   "seao_supplier_id": "FO-88527"
  },
  "address": {
   "line1": "5 Isnor drive",
   "line2": null,
   "city": "Darmouth",
   "region": "NS",
   "postal_code": "B3B 1M1",
   "country": "CAN"
  },
  "contact": {}
 },
 "raw_keys_present": {
  "avis": "dict",
  "avis_appearances": "list",
  "fournisseur_lines": "list",
  "depenses_supplementaires": "list",
  "depenses_supplementaires_unmatched": null,
  "information_finale": null,
  "information_finale_unmatched": null,
  "ocds_release": "dict",
  "ocds_release_history": "list",
  "ocds_supplier_contracts": "list",
  "ocds_supplier_awards": "list",
  "ocds_supplier_party": "dict",
  
```
(raw omitted here; the full record in the JSONL carries raw.avis / raw.fournisseur_lines / raw.depenses_supplementaires / raw.ocds_release etc. — keys present: avis:dict, avis_appearances:list, fournisseur_lines:list, depenses_supplementaires:list, ocds_release:dict, ocds_release_history:list, ocds_supplier_contracts:list, ocds_supplier_awards:list, ocds_supplier_party:dict, code_labels:dict)

### Sample `inferred_xml_only_old` — `seao_quebec:100661:ipl-inc`
```json
{
 "record_id": "seao_quebec:100661:ipl-inc",
 "source": {
  "key": "seao_quebec",
  "name": "Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes",
  "publisher": "Secrétariat du Conseil du trésor (Québec) via Données Québec",
  "dataset_url": "https://www.donneesquebec.ca/recherche/dataset/systeme-electronique-dappel-doffres-seao",
  "record_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f428e438-6452-403d-89b2-095ee4b3608d",
  "retrieved_at": "2026-10-25T12:28:30Z"
 },
 "status": "ongoing_inferred",
 "status_basis": "contract concluded on 2006-06-26; no final-information (closure) record published as of retrieval (no matching record in XML Contrats/ContratsRevisions files 2009-01..2024-05; notice absent from the OCDS JSON feed 2021-03..2026-10-18, so no post-May-2024 closure could be detected)",
 "contract": {
  "identifiers": {
   "numeroseao": "100661",
   "numero": "06-338",
   "seao_item_id": "f428e438-6452-403d-89b2-095ee4b3608d"
  },
  "title": "Fourniture de bacs roulants de récupération",
  "description": "Approvisionnement (biens)",
  "instrument_type": "contract",
  "procurement_method": "open",
  "solicitation_procedure": "Contrat adjugé suite à un appel d'offres public",
  "commodity": {
   "seao_category": "G22 - Produits divers"
  },
  "value": 263835.72,
  "currency": "CAD",
  "value_detail": {
   "montantcontrat": 263835.72,
   "montantsoumis": 263835.72
  },
  "dates": {
   "published": "2014-12-12",
   "signed": "2006-06-26",
   "start": "2006-06-26",
   "end": null,
   "amended_last": null,
   "tender_published": "2006-06-06",
   "tender_closing": "2006-06-22"
  },
  "related": {
   "hyperlienseao_original": "https://www.seao.ca/OpportunityPublication/avisconsultes.aspx?ItemId=f428e438-6452-403d-89b2-095ee4b3608d",
   "notice_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f428e438-6452-403d-89b2-095ee4b3608d",
   "delivery_regions": [
    "Lanaudière"
   ]
  }
 },
 "buyer": {
  "name": "Ville Saint-Rémi",
  "country": "CA",
  "type": "city",
  "identifiers": {},
  "address": {
   "line1": "105, rue Perras",
   "line2": null,
   "city": "Saint-Rémi",
   "region": "QC",
   "postal_code": "J0L 2L0",
   "country": "CAN"
  },
  "contact": {},
  "municipal_flag": "1"
 },
 "vendor": {
  "name": "IPL INC",
  "country": "CA",
  "country_basis": "XML fournisseur/pays: supplier country field = \"CAN\" (CAN = Canada per SEAO Annexe A; \"CA\" accepted as Canada: all such rows carry a Canadian province code and/or postal code)",
  "identifiers": {
   "neq": "1166753963"
  },
  "address": {
   "line1": "140, Commercial",
   "line2": null,
   "city": "Saint-Damien",
   "region": "QC",
   "postal_code": "G0R 2Y0",
   "country": "CAN"
  },
  "contact": {}
 },
 "raw_keys_present": {
  "avis": "dict",
  "avis_appearances": "list",
  "fournisseur_lines": "list",
  "depenses_supplementaires": "list",
  "depenses_supplementaires_unmatched": null,
  "information_finale": null,
  "information_finale_unmatched": null,
  "ocds_release": null,
  "ocds_release_history": null,
  "ocds_supplier_contracts": null,
  "ocds_supplier_awards": null,
  "ocds_supplier_party": null,
  "code_labels": "dict"
 }
}
```
(raw omitted here; the full record in the JSONL carries raw.avis / raw.fournisseur_lines / raw.depenses_supplementaires / raw.ocds_release etc. — keys present: avis:dict, avis_appearances:list, fournisseur_lines:list, depenses_supplementaires:list, code_labels:dict)

### Sample `inferred_json_backed` — `seao_quebec:1002604:energie-valero-inc`
```json
{
 "record_id": "seao_quebec:1002604:energie-valero-inc",
 "source": {
  "key": "seao_quebec",
  "name": "Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes",
  "publisher": "Secrétariat du Conseil du trésor (Québec) via Données Québec",
  "dataset_url": "https://www.donneesquebec.ca/recherche/dataset/systeme-electronique-dappel-doffres-seao",
  "record_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2da8c22e-1760-42b3-bd6d-32e23c047d2b",
  "retrieved_at": "2026-10-25T12:28:30Z"
 },
 "status": "ongoing_inferred",
 "status_basis": "contract concluded on 2016-03-01; no final-information (closure) record published as of retrieval (no matching record in XML Contrats/ContratsRevisions files 2009-01..2024-05; OCDS contract status 'active' with no period.endDate in latest release 20160726183719 from mensuel_20240701_20240731.json)",
 "contract": {
  "identifiers": {
   "numeroseao": "1002604",
   "numero": "CAR-2016",
   "ocid": "ocds-ec9k95-1002604",
   "ocds_contract_ids": [
    "272147"
   ],
   "ocds_award_ids": [
    "272147"
   ],
   "seao_item_id": "2da8c22e-1760-42b3-bd6d-32e23c047d2b"
  },
  "title": "Fourniture et livraison de différents carburants en vrac (essence, diesel et mazout) dans diverses municipalités",
  "description": "goods; Approvisionnement (biens)",
  "instrument_type": "contract",
  "procurement_method": "open",
  "solicitation_procedure": "Contrat à la suite d'un achat mandaté ou d'un regroupement d’organismes",
  "commodity": {
   "unspsc": "15100000",
   "unspsc_description": "Carburants",
   "seao_category": "G11 - Énergie"
  },
  "value": null,
  "currency": "CAD",
  "value_detail": {
   "ocds_contract_value_amount": null
  },
  "dates": {
   "published": "2016-07-26",
   "signed": "2016-03-01",
   "start": "2016-03-01",
   "end": null,
   "amended_last": null,
   "tender_published": "2015-12-11",
   "tender_closing": "2016-01-27"
  },
  "related": {
   "notice_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2da8c22e-1760-42b3-bd6d-32e23c047d2b",
   "ocds_tender_document_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2da8c22e-1760-42b3-bd6d-32e23c047d2b"
  }
 },
 "buyer": {
  "name": "Ville de Gatineau.",
  "country": "CA",
  "type": "city",
  "identifiers": {
   "seao_organisation_id": "OP-14120"
  },
  "address": {
   "line1": "476, boulevard Saint-René Est, 2e étage,",
   "line2": null,
   "city": "Gatineau",
   "region": "QC",
   "postal_code": "J8P8A9",
   "country": "CAN"
  },
  "contact": {},
  "municipal_flag": "1"
 },
 "vendor": {
  "name": "Énergie Valéro inc.",
  "country": "CA",
  "country_basis": "OCDS parties[role=supplier].address.countryName: supplier country field = \"CAN\" (CAN = Canada per SEAO Annexe A; \"CA\" accepted as Canada: all such rows carry a Canadian province code and/or postal code)",
  "identifiers": {
   "neq": "1144999787",
   "seao_supplier_id": "FO-1144999787"
  },
  "address": {
   "line1": "1801, avenue McGill College,13e étage",
   "line2": null,
   "city": "Montréal",
   "region": "QC",
   "postal_code": "H3A2N4",
   "country": "CAN"
  },
  "contact": {}
 },
 "raw_keys_present": {
  "avis": null,
  "avis_appearances": null,
  "fournisseur_lines": null,
  "depenses_supplementaires": "list",
  "depenses_supplementaires_unmatched": null,
  "information_finale": null,
  "information_finale_unmatched": null,
  "ocds_release": "dict",
  "ocds_release_history": "list",
  "ocds_supplier_contracts": "list",
  "ocds_supplier_awards": "list",
  "ocds_supplier_party": "dict",
  "code_labels": null
 }
}
```
(raw omitted here; the full record in the JSONL carries raw.avis / raw.fournisseur_lines / raw.depenses_supplementaires / raw.ocds_release etc. — keys present: depenses_supplementaires:list, ocds_release:dict, ocds_release_history:list, ocds_supplier_contracts:list, ocds_supplier_awards:list, ocds_supplier_party:dict)

### Sample `inferred_with_depenses` — `seao_quebec:1001636:beaudoin-hurens`
```json
{
 "record_id": "seao_quebec:1001636:beaudoin-hurens",
 "source": {
  "key": "seao_quebec",
  "name": "Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes",
  "publisher": "Secrétariat du Conseil du trésor (Québec) via Données Québec",
  "dataset_url": "https://www.donneesquebec.ca/recherche/dataset/systeme-electronique-dappel-doffres-seao",
  "record_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b1990e95-0ac6-48c0-9377-0f65d9c60c41",
  "retrieved_at": "2026-10-25T12:28:30Z"
 },
 "status": "ongoing_inferred",
 "status_basis": "contract concluded on 2016-03-07; no final-information (closure) record published as of retrieval (no matching record in XML Contrats/ContratsRevisions files 2009-01..2024-05; notice absent from the OCDS JSON feed 2021-03..2026-10-18, so no post-May-2024 closure could be detected)",
 "contract": {
  "identifiers": {
   "numeroseao": "1001636",
   "numero": "HON-012-020-42160",
   "seao_item_id": "b1990e95-0ac6-48c0-9377-0f65d9c60c41"
  },
  "title": "HON-012-020-42160 - Ingénieurs - Infiltrations d'eau par les murs extérieurs",
  "description": "Services - Services professionnels",
  "instrument_type": "contract",
  "procurement_method": "direct",
  "solicitation_procedure": "Contrat octroyé de gré à gré",
  "commodity": {
   "unspsc": "81100000",
   "seao_category": "S3 - Services d'architecture et d'ingénierie"
  },
  "value": 29650.0,
  "currency": "CAD",
  "value_detail": {
   "montantcontrat": 29650.0,
   "montantsoumis": 0.0,
   "supplementary_expenses_total": 1330.0,
   "supplementary_expenses_count": 2
  },
  "dates": {
   "published": "2016-07-21",
   "signed": "2016-03-07",
   "start": "2016-03-07",
   "end": null,
   "amended_last": "2016-11-24",
   "tender_published": "2016-07-21",
   "tender_closing": null
  },
  "related": {
   "hyperlienseao_original": "https://www.seao.ca/OpportunityPublication/avisconsultes.aspx?ItemId=b1990e95-0ac6-48c0-9377-0f65d9c60c41",
   "notice_url": "https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b1990e95-0ac6-48c0-9377-0f65d9c60c41",
   "delivery_regions": [
    "Lanaudière"
   ],
   "disposition_or_rationale": "14",
   "montantssoumisunite_code": "0"
  }
 },
 "buyer": {
  "name": "Commission  scolaire Marie-Victorin",
  "country": "CA",
  "type": "provincial agency",
  "identifiers": {},
  "address": {
   "line1": "13, rue Saint-Laurent Est",
   "line2": "2e étage",
   "city": "Longueuil",
   "region": "QC",
   "postal_code": "J4H 4B7",
   "country": "CAN"
  },
  "contact": {},
  "municipal_flag": "0"
 },
 "vendor": {
  "name": "Beaudoin Hurens",
  "country": "CA",
  "country_basis": "XML fournisseur/pays: supplier country field = \"CAN\" (CAN = Canada per SEAO Annexe A; \"CA\" accepted as Canada: all such rows carry a Canadian province code and/or postal code)",
  "identifiers": {
   "neq": "1148115281"
  },
  "address": {
   "line1": "255 boul Crémazie Est 9e Etage",
   "line2": null,
   "city": "Montréal",
   "region": "QC",
   "postal_code": "H2M 1M2",
   "country": "CAN"
  },
  "contact": {}
 },
 "raw_keys_present": {
  "avis": "dict",
  "avis_appearances": "list",
  "fournisseur_lines": "list",
  "depenses_supplementaires": "list",
  "depenses_supplementaires_unmatched": null,
  "information_finale": null,
  "information_finale_unmatched": null,
  "ocds_release": null,
  "ocds_release_history": null,
  "ocds_supplier_contracts": null,
  "ocds_supplier_awards": null,
  "ocds_supplier_party": null,
  "code_labels": "dict"
 }
}
```
(raw omitted here; the full record in the JSONL carries raw.avis / raw.fournisseur_lines / raw.depenses_supplementaires / raw.ocds_release etc. — keys present: avis:dict, avis_appearances:list, fournisseur_lines:list, depenses_supplementaires:list, code_labels:dict)

