"""Stage 1 (v2): directory matching for the new buyers -> WORK/bulk.json {buyer_key: partial record} and WORK/sites_main.json (crawl list).
Sources: parent-organisation rules (classify.json) + official domains of parents (alias table, verified by crawl), Ontario school board
contact list (data.ontario.ca), Wikidata label lookup (downloads/enrichment_buyers_v2/dir/wikidata/), website fields published in the
contract notices' buyer contact blocks, extra alias rules (ALIAS below)."""
import sys, os, json, re, csv, glob, collections, urllib.parse, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

PARENT_SITE = {
    'city_of_toronto': 'https://www.toronto.ca/', 'city_of_ottawa': 'https://ottawa.ca/en', 'gov_AB': 'https://www.alberta.ca/',
    'gov_BC': 'https://www2.gov.bc.ca/', 'gov_NS': 'https://novascotia.ca/', 'gov_SK': 'https://www.saskatchewan.ca/', 'gov_NL': 'https://www.gov.nl.ca/',
    'gov_NT': 'https://www.gov.nt.ca/', 'gov_ON': 'https://www.ontario.ca/', 'gov_YT': 'https://yukon.ca/', 'gov_MB': 'https://www.gov.mb.ca/',
    'state_ma': 'https://www.mass.gov/', 'state_vt': 'https://vermont.gov/', 'state_ak': 'https://alaska.gov/', 'state_ok': 'https://oklahoma.gov/',
    'state_de': 'https://delaware.gov/', 'montgomery_md': 'https://www.montgomerycountymd.gov/', 'miami_dade': 'https://www.miamidade.gov/',
    'mesa_az': 'https://www.mesaaz.gov/', 'fulton_ga': 'https://www.fultoncountyga.gov/', 'city_la': 'https://lacity.gov/',
    'mesquite_tx': 'https://www.cityofmesquite.com/', 'baton_rouge': 'https://www.brla.gov/', 'corona_ca': 'https://www.coronaca.gov/',
    'indio_ca': 'https://www.indio.org/', 'richmond_ca': 'https://www.ci.richmond.ca.us/', 'nyc': 'https://www.nyc.gov/', 'san_jose': 'https://www.sanjoseca.gov/',
    'undp': 'https://www.undp.org/', 'who': 'https://www.who.int/', 'eu_commission': 'https://commission.europa.eu/', 'uoft': 'https://www.utoronto.ca/',
    'ttc': 'https://www.ttc.ca/', 'nlhs': 'https://nlhealthservices.ca/', 'nl_mod': 'https://www.defensie.nl/', 'ethz': 'https://ethz.ch/',
    'epfl': 'https://www.epfl.ch/', 'ngu': 'https://www.ngu.no/'}
GOV_PORTALS = {'https://www.alberta.ca/', 'https://www2.gov.bc.ca/', 'https://novascotia.ca/', 'https://www.saskatchewan.ca/', 'https://www.gov.nl.ca/',
               'https://www.gov.nt.ca/', 'https://www.ontario.ca/', 'https://yukon.ca/', 'https://www.gov.mb.ca/', 'https://www.mass.gov/', 'https://vermont.gov/',
               'https://alaska.gov/', 'https://oklahoma.gov/', 'https://delaware.gov/', 'https://www.nyc.gov/', 'https://lacity.gov/', 'https://www.undp.org/',
               'https://www.who.int/', 'https://commission.europa.eu/', 'https://www.defensie.nl/'}
# extra alias rules: regex on normalized name -> (canonical name, official domain, type). Official domains of well-known organisations; each is
# fetched by the crawler and its status recorded in extras.website_check.
ALIAS = [
    (r'^3shealth$', '3sHealth (Health Shared Services Saskatchewan)', 'https://www.3shealth.ca/', 'Saskatchewan health shared services organisation'),
    (r'^workplace ?nl$', 'WorkplaceNL', 'https://workplacenl.ca/', 'NL workers compensation board'),
    (r'^cape breton university$', 'Cape Breton University', 'https://www.cbu.ca/', 'university'),
    (r'^provincial health services authority', 'Provincial Health Services Authority (PHSA)', 'http://www.phsa.ca/', 'BC health authority'),
    (r'^bc transit$', 'BC Transit', 'https://www.bctransit.com/', 'BC crown corporation'),
    (r'^worksafebc$', 'WorkSafeBC', 'https://www.worksafebc.com/', 'BC workers compensation board'),
    (r'^royal roads university$', 'Royal Roads University', 'https://www.royalroads.ca/', 'university'),
    (r'^british columbia assessment authority$', 'BC Assessment', 'https://info.bcassessment.ca/', 'BC crown corporation'),
    (r'^bc housing management commission$', 'BC Housing', 'https://www.bchousing.org/', 'BC crown agency'),
    (r'^royal british columbia museum$', 'Royal BC Museum', 'https://royalbcmuseum.bc.ca/', 'BC crown corporation'),
    (r'^innovacorp$', 'Innovacorp', 'https://innovacorp.ca/', 'NS crown corporation'),
    (r'^art gallery of nova scotia$', 'Art Gallery of Nova Scotia', 'https://agns.ca/', 'NS crown agency'),
    (r'^islands trust$', 'Islands Trust', 'https://islandstrust.bc.ca/', 'BC local government federation'),
    (r'^red deer catholic separate school division$', 'Red Deer Catholic Regional Schools', 'https://www.rdcrs.ca/', 'Alberta school division'),
    (r'^palliser school division$', 'Palliser School Division', 'https://www.pallisersd.ab.ca/', 'Alberta school division'),
    (r'^prairie rose school division$', 'Prairie Rose School Division', 'https://www.prrd.ab.ca/', 'Alberta school division'),
    (r'^grande yellowhead public school division$', 'Grande Yellowhead Public School Division', 'https://www.gypsd.ca/', 'Alberta school division'),
    (r'^golden hills school division$', 'Golden Hills School Division', 'https://www.goldenhills.ca/', 'Alberta school division'),
    (r'^wolf creek school division$', 'Wolf Creek Public Schools', 'https://www.wolfcreek.ab.ca/', 'Alberta school division'),
    (r'^grande prairie roman catholic separate school division$', 'Grande Prairie Catholic Schools', 'https://www.gpcsd.ca/', 'Alberta school division'),
    (r'^pembina hills school division$', 'Pembina Hills School Division', 'https://www.pembinahills.ca/', 'Alberta school division'),
    (r'^the board of trustees of st albert public schools$', 'St. Albert Public Schools', 'https://www.spschools.org/', 'Alberta school division'),
    (r'^lethbridge school division$', 'Lethbridge School Division', 'https://www.lethsd.ab.ca/', 'Alberta school division'),
    (r'^aspen view school division$', 'Aspen View Public Schools', 'https://www.aspenview.org/', 'Alberta school division'),
    (r'^medicine hat public board of education$', 'Medicine Hat Public School Division', 'https://www.mhpsd.ca/', 'Alberta school division'),
    (r'^conseil scolaire francosud$', 'Conseil scolaire FrancoSud', 'https://www.francosud.ca/', 'Alberta francophone school authority'),
    (r'^living waters catholic separate school division$', 'Living Waters Catholic Schools', 'https://www.lwcrd.ab.ca/', 'Alberta school division'),
    (r'^fort mcmurray roman catholic separate school division$', 'Fort McMurray Catholic Schools', 'https://www.fmcschools.ca/', 'Alberta school division'),
    (r'^elk island catholic separate school division$', 'Elk Island Catholic Schools', 'https://www.eics.ab.ca/', 'Alberta school division'),
    (r'^battle river school division$', 'Battle River School Division', 'https://www.brsd.ab.ca/', 'Alberta school division'),
    (r'^grasslands school division$', 'Grasslands Public Schools', 'https://www.grasslands.ab.ca/', 'Alberta school division'),
    (r'^holy spirit roman catholic separate school division$', 'Holy Spirit Catholic Schools', 'https://www.holyspirit.ab.ca/', 'Alberta school division'),
    (r'^northland school division$', 'Northland School Division', 'https://www.nsd61.ca/', 'Alberta school division'),
    (r'^chinook s edge school division$', "Chinook's Edge School Division", 'https://www.cesd73.ca/', 'Alberta school division'),
    (r'^calgary economic development', 'Calgary Economic Development', 'https://calgaryeconomicdevelopment.com/', 'municipal economic development corporation'),
    (r'^transalta tri leisure centre$', 'TransAlta Tri Leisure Centre', 'https://www.trileisure.com/', 'recreation facility (Spruce Grove / Stony Plain / Parkland)'),
    (r'^explore edmonton corporation$', 'Explore Edmonton', 'https://exploreedmonton.com/', 'municipal corporation'),
    (r'^wood buffalo housing$', 'Wood Buffalo Housing', 'https://www.wbhadc.ca/', 'municipal housing corporation'),
    (r'^gef seniors housing$', 'GEF Seniors Housing', 'https://www.gefseniors.ca/', 'Alberta housing management body'),
    (r'^newfoundland labrador liquor corporation$|^newfoundland liquor corporation$|^nlc$', 'Newfoundland and Labrador Liquor Corporation', 'https://www.nlliquor.com/', 'NL crown corporation'),
    (r'^school district 72 campbell river', 'School District No. 72 (Campbell River)', 'https://www.sd72.bc.ca/', 'BC school district'),
    (r'^rm of de salaberry$', 'Rural Municipality of De Salaberry', 'https://www.rmdesalaberry.mb.ca/', 'Manitoba rural municipality'),
    (r'^nasittuq corporation$', 'Nasittuq Corporation', 'https://www.nasittuq.com/', 'company (North Warning System operator)'),
    (r'^nalcor energy$', 'Nalcor Energy', 'https://nlhydro.com/', 'NL crown energy corporation (now part of NL Hydro)'),
    (r'^halifax regional municipality', 'Halifax Regional Municipality', 'https://www.halifax.ca/', 'Nova Scotia regional municipality'),
    (r'^city of orillia$', 'City of Orillia', 'https://www.orillia.ca/', 'Ontario municipality'),
    (r'^city of port colborne$', 'City of Port Colborne', 'https://www.portcolborne.ca/', 'Ontario municipality'),
    (r'^regional municipality of wood buffalo$', 'Regional Municipality of Wood Buffalo', 'https://www.rmwb.ca/', 'Alberta specialized municipality'),
    (r'^manitoba hydro$', 'Manitoba Hydro', 'https://www.hydro.mb.ca/', 'Manitoba crown corporation'),
    (r'^epcor', 'EPCOR', 'https://www.epcor.com/', 'municipally owned utility (City of Edmonton)'),
    (r'^enmax$', 'ENMAX Corporation', 'https://www.enmax.com/', 'municipally owned utility (City of Calgary)'),
    (r'^metropolitan transportation authority$', 'Metropolitan Transportation Authority (New York)', 'https://new.mta.info/', 'NY public authority'),
    (r'^power authority of the state of new york$', 'New York Power Authority', 'https://www.nypa.gov/', 'NY public authority'),
    (r'^york university$', 'York University', 'https://www.yorku.ca/', 'university'),
    (r'^toronto metropolitan university$', 'Toronto Metropolitan University', 'https://www.torontomu.ca/', 'university'),
    (r'^canoe procurement group', 'Canoe Procurement Group of Canada', 'https://canoeprocurement.ca/', 'group purchasing organisation'),
    (r'^cbc radio canada$', 'CBC/Radio-Canada', 'https://cbc.radio-canada.ca/en', 'federal crown corporation'),
    (r'^canadian air transport security authority$', 'Canadian Air Transport Security Authority (CATSA)', 'https://www.catsa-acsta.gc.ca/en', 'federal crown corporation'),
    (r'^nlschools$', 'NLSchools (Newfoundland and Labrador English School District)', 'https://www.nlschools.ca/', 'school district'),
    (r'^nl provincial health shared services supply chain$', 'Provincial Health Shared Services Supply Chain (NL Health Services)', 'https://nlhealthservices.ca/', 'health supply chain'),
    (r'^civida$', 'Civida (Capital Region Housing)', 'https://civida.ca/', 'housing management body'),
    (r'^nwt health and social services authority$', 'Northwest Territories Health and Social Services Authority', 'https://www.nthssa.ca/', 'territorial health authority'),
    (r'^university of calgary$', 'University of Calgary', 'https://www.ucalgary.ca/', 'university'),
    (r'^university of alberta$', 'University of Alberta', 'https://www.ualberta.ca/', 'university'),
    (r'^rural municipalities of alberta', 'Rural Municipalities of Alberta', 'https://rmalberta.com/', 'municipal association'),
    (r'^public service delivery$', 'Manitoba Public Service Delivery', 'https://www.gov.mb.ca/', 'Manitoba government department'),
    (r'^edmonton catholic separate school division$', 'Edmonton Catholic Schools', 'https://www.ecsd.net/', 'school division'),
    (r'^calgary housing company$', 'Calgary Housing Company', 'https://www.calgaryhousingcompany.org/', 'municipal housing company'),
    (r'^alberta innovates$', 'Alberta Innovates', 'https://albertainnovates.ca/', 'Alberta provincial corporation'),
    (r'^mcmaster university$', 'McMaster University', 'https://www.mcmaster.ca/', 'university'),
    (r'^efficiency manitoba$', 'Efficiency Manitoba', 'https://efficiencymb.ca/', 'Manitoba crown corporation'),
    (r'^nl hydro$|^newfoundland labrador hydro$', 'Newfoundland and Labrador Hydro', 'https://nlhydro.com/', 'NL crown corporation'),
    (r'^housing nwt$|^nwt housing corporation$', 'Housing NWT', 'https://www.nwthc.gov.nt.ca/', 'GNWT territorial agency'),
    (r'^liquor control board of ontario', 'Liquor Control Board of Ontario (LCBO)', 'https://www.lcbo.com/', 'Ontario crown agency'),
    (r'^workplace safety and insurance board', 'Workplace Safety and Insurance Board (WSIB)', 'https://www.wsib.ca/', 'Ontario agency'),
    (r'^alberta electric system operator$', 'Alberta Electric System Operator (AESO)', 'https://www.aeso.ca/', 'Alberta independent system operator'),
    (r'^alberta energy regulator$', 'Alberta Energy Regulator', 'https://www.aer.ca/', 'Alberta regulator'),
    (r'^alberta gaming liquor and cannabis commission$', 'Alberta Gaming, Liquor and Cannabis Commission (AGLC)', 'https://aglc.ca/', 'Alberta agency'),
    (r'^red deer polytechnic$', 'Red Deer Polytechnic', 'https://rdpolytech.ca/', 'post-secondary'),
    (r'^keyano college$', 'Keyano College', 'https://www.keyano.ca/', 'post-secondary'),
    (r'^macewan university$', 'MacEwan University', 'https://www.macewan.ca/', 'university'),
    (r'^toronto police service$', 'Toronto Police Service', 'https://www.tps.ca/', 'municipal police service'),
    (r'^york regional police$', 'York Regional Police', 'https://www.yrp.ca/', 'regional police service'),
    (r'^workers compensation board of alberta$', 'Workers\' Compensation Board – Alberta', 'https://www.wcb.ab.ca/', 'Alberta agency'),
    (r'^ornge$', 'Ornge', 'https://www.ornge.ca/', 'Ontario air ambulance'),
    (r'^technical standards and safety authority$', 'Technical Standards and Safety Authority (TSSA)', 'https://www.tssa.org/', 'Ontario safety regulator'),
    (r'^northern alberta institute of technology', 'NAIT', 'https://www.nait.ca/', 'post-secondary'),
    (r'^southern alberta institute of technology$', 'SAIT', 'https://www.sait.ca/', 'post-secondary'),
    (r'^atb financial$', 'ATB Financial', 'https://www.atb.com/', 'Alberta crown financial institution'),
    (r'^aimco alberta investment management corporation$|^alberta investment management corporation$', 'Alberta Investment Management Corporation (AIMCo)', 'https://www.aimco.ca/', 'Alberta crown corporation'),
    (r'^manitoba liquor and lotteries corporation$', 'Manitoba Liquor & Lotteries', 'https://www.mbll.ca/', 'Manitoba crown corporation'),
    (r'^manitoba housing renewal corporation$', 'Manitoba Housing', 'https://www.gov.mb.ca/housing/', 'Manitoba housing corporation'),
    (r'^municipal property assessment corporation$', 'MPAC', 'https://www.mpac.ca/', 'Ontario assessment corporation'),
    (r'^ontario tech university$', 'Ontario Tech University', 'https://ontariotechu.ca/', 'university'),
    (r'^humber polytechnic$', 'Humber Polytechnic', 'https://humber.ca/', 'post-secondary'),
    (r'^halifax water$', 'Halifax Water', 'https://www.halifaxwater.ca/', 'municipal water utility'),
    (r'^interior health$', 'Interior Health Authority', 'https://www.interiorhealth.ca/', 'BC health authority'),
    (r'^london hydro$', 'London Hydro', 'https://www.londonhydro.com/', 'municipal utility'),
    (r'^vancouver island health authority$', 'Island Health', 'https://www.islandhealth.ca/', 'BC health authority'),
    (r'^sourcewell$', 'Sourcewell', 'https://www.sourcewell-mn.gov/', 'US cooperative purchasing agency'),
    (r'^saskatchewan power corporation', 'SaskPower', 'https://www.saskpower.com/', 'Saskatchewan crown corporation'),
    (r'^greater toronto airports authority$', 'Greater Toronto Airports Authority', 'https://www.torontopearson.com/', 'airport authority'),
    (r'^createto', 'CreateTO', 'https://createto.ca/', 'City of Toronto agency'),
    (r'^manitoba public insurance$', 'Manitoba Public Insurance', 'https://www.mpi.mb.ca/', 'Manitoba crown corporation'),
    (r'^bruce power$', 'Bruce Power', 'https://www.brucepower.com/', 'nuclear operator'),
    (r'^university of guelph$', 'University of Guelph', 'https://www.uoguelph.ca/', 'university'),
    (r'^university of manitoba$', 'University of Manitoba', 'https://umanitoba.ca/', 'university'),
    (r'^university of winnipeg$', 'University of Winnipeg', 'https://www.uwinnipeg.ca/', 'university'),
    (r'^carleton university$', 'Carleton University', 'https://carleton.ca/', 'university'),
    (r'^brock university$', 'Brock University', 'https://brocku.ca/', 'university'),
    (r'^centennial college$', 'Centennial College', 'https://www.centennialcollege.ca/', 'college'),
    (r'^dalhousie university$', 'Dalhousie University', 'https://www.dal.ca/', 'university'),
    (r'^university of saskatchewan$', 'University of Saskatchewan', 'https://www.usask.ca/', 'university'),
    (r'^university of regina$', 'University of Regina', 'https://www.uregina.ca/', 'university'),
    (r'^saskenergy', 'SaskEnergy', 'https://www.saskenergy.com/', 'Saskatchewan crown corporation'),
    (r'^saskatchewan government insurance$', 'SGI', 'https://www.sgi.sk.ca/', 'Saskatchewan crown corporation'),
    (r'^saskatchewan health authority$', 'Saskatchewan Health Authority', 'https://www.saskhealthauthority.ca/', 'health authority'),
    (r'^saskatchewan telecommunications$', 'SaskTel', 'https://www.sasktel.com/', 'Saskatchewan crown corporation'),
    (r'^nova scotia health authority$', 'Nova Scotia Health', 'https://www.nshealth.ca/', 'health authority'),
    (r'^nova scotia liquor corporation$', 'Nova Scotia Liquor Corporation (NSLC)', 'https://www.mynslc.com/', 'NS crown corporation'),
    (r'^nova scotia community college', 'Nova Scotia Community College', 'https://www.nscc.ca/', 'college'),
    (r'^cape breton university$', 'Cape Breton University', 'https://www.cbu.ca/', 'university'),
    (r'^atlantic lottery corporation$', 'Atlantic Lottery Corporation', 'https://www.alc.ca/', 'crown lottery corporation'),
    (r'^george mason university$', 'George Mason University', 'https://www.gmu.edu/', 'Virginia public university'),
    (r'^virginia commonwealth university$', 'Virginia Commonwealth University', 'https://www.vcu.edu/', 'Virginia public university'),
    (r'^james madison university$', 'James Madison University', 'https://www.jmu.edu/', 'Virginia public university'),
    (r'^old dominion university$', 'Old Dominion University', 'https://www.odu.edu/', 'Virginia public university'),
    (r'^university of virginia$', 'University of Virginia', 'https://www.virginia.edu/', 'Virginia public university'),
    (r'^virginia polytechnic institute and state university$', 'Virginia Tech', 'https://www.vt.edu/', 'Virginia public university'),
    (r'^the university of texas m d anderson cancer center$', 'The University of Texas MD Anderson Cancer Center', 'https://www.mdanderson.org/', 'Texas state institution'),
    (r'^the university of texas at austin$', 'The University of Texas at Austin', 'https://www.utexas.edu/', 'Texas state university'),
    (r'^the university of texas medical branch at galveston$', 'UTMB Health', 'https://www.utmb.edu/', 'Texas state institution'),
    (r'^department of public safety$', 'Texas Department of Public Safety', 'https://www.dps.texas.gov/', 'Texas state agency'),
    (r'^transportation department of$', 'Oregon Department of Transportation', 'https://www.oregon.gov/odot/', 'Oregon state agency'),
    (r'^health authority oregon$', 'Oregon Health Authority', 'https://www.oregon.gov/oha/', 'Oregon state agency'),
    (r'^roswell park cancer institute corporation$', 'Roswell Park Comprehensive Cancer Center', 'https://www.roswellpark.org/', 'NY public benefit corporation'),
    (r'^city of providence$', 'City of Providence', 'https://www.providenceri.gov/', 'US city'),
    (r'^city of austin texas$', 'City of Austin', 'https://www.austintexas.gov/', 'US city'),
    (r'^caribbean development bank$', 'Caribbean Development Bank', 'https://www.caribank.org/', 'IGO'),
    (r'^food and agriculture organization', 'FAO', 'https://www.fao.org/', 'IGO'),
    (r'^europol$', 'Europol', 'https://www.europol.europa.eu/', 'EU agency'),
    (r'^european food safety authority', 'EFSA', 'https://www.efsa.europa.eu/', 'EU agency'),
    (r'^european maritime safety agency$', 'EMSA', 'https://www.emsa.europa.eu/', 'EU agency'),
    (r'^rocky view school division$', 'Rocky View Schools', 'https://www.rockyview.ab.ca/', 'Alberta school division'),
    (r'^manitoba water services board$', 'Manitoba Water Services Board', 'https://www.mwsb.mb.ca/', 'Manitoba government agency'),
    (r'^town of collingwood$', 'Town of Collingwood', 'https://www.collingwood.ca/', 'Ontario municipality'),
    (r'^calgary roman catholic separate school division$', 'Calgary Catholic School District', 'https://www.cssd.ab.ca/', 'Alberta school division'),
    (r'^town of the blue mountains$', 'Town of The Blue Mountains', 'https://www.thebluemountains.ca/', 'Ontario municipality'),
    (r'^black gold school division$', 'Black Gold School Division', 'https://www.blackgold.ca/', 'Alberta school division'),
    (r'^waterloo regional police service$', 'Waterloo Regional Police Service', 'https://www.wrps.on.ca/', 'regional police service'),
    (r'^greater st albert roman catholic separate school division$', 'Greater St. Albert Catholic Schools', 'https://www.gsacrd.ab.ca/', 'Alberta school division'),
    (r'^school district no 43 coquitlam', 'School District No. 43 (Coquitlam)', 'https://www.sd43.bc.ca/', 'BC school district'),
    (r'^municipality of the county of kings$', 'Municipality of the County of Kings', 'https://www.countyofkings.ca/', 'Nova Scotia municipality'),
    (r'^innservices', 'InnServices Utilities Inc.', 'https://innservices.ca/', 'municipal utility'),
    (r'^red deer school division$', 'Red Deer Public Schools', 'https://www.rdpsd.ab.ca/', 'Alberta school division'),
    (r'^agriculture financial services corporation$', 'Agriculture Financial Services Corporation (AFSC)', 'https://afsc.ca/', 'Alberta crown corporation'),
    (r'^the city of edmonton non profit housing corporation', 'HomeEd (City of Edmonton Non-Profit Housing Corporation)', 'https://www.homeed.ca/', 'municipal housing corporation'),
    (r'^aquatera utilities', 'Aquatera Utilities Inc.', 'https://www.aquatera.ca/', 'municipal utility'),
    (r'^sturgeon school division$', 'Sturgeon Public Schools', 'https://www.sturgeon.ab.ca/', 'Alberta school division'),
    (r'^northern lights school division$', 'Northern Lights Public Schools', 'https://www.nlpsab.ca/', 'Alberta school division'),
    (r'^parkland school division$', 'Parkland School Division', 'https://www.psd.ca/', 'Alberta school division'),
    (r'^utilities kingston$', 'Utilities Kingston', 'https://utilitieskingston.com/', 'municipal utility'),
    (r'^middlesex centre$', 'Municipality of Middlesex Centre', 'https://www.middlesexcentre.ca/', 'Ontario municipality'),
    (r'^christ the redeemer catholic separate school division$', 'Christ the Redeemer Catholic Schools', 'https://www.redeemer.ab.ca/', 'Alberta school division'),
    (r'^st clair college', 'St. Clair College', 'https://www.stclaircollege.ca/', 'college'),
    (r'^elk island public schools$', 'Elk Island Public Schools', 'https://www.eips.ca/', 'Alberta school division'),
    (r'^newfoundland and labrador housing corporation', 'Newfoundland and Labrador Housing Corporation', 'https://www.nlhc.nl.ca/', 'NL crown corporation'),
    (r'^city of moncton', 'City of Moncton', 'https://www.moncton.ca/', 'New Brunswick municipality'),
    (r'^conservation halton$', 'Conservation Halton', 'https://www.conservationhalton.ca/', 'conservation authority'),
    (r'^northwestern polytechnic$', 'Northwestern Polytechnic', 'https://www.nwpolytech.ca/', 'post-secondary'),
    (r'^town of la salle$', 'Town of LaSalle', 'https://www.lasalle.ca/', 'Ontario municipality'),
    (r'^divert ns$', 'Divert NS', 'https://divertns.ca/', 'Nova Scotia not-for-profit (stewardship)'),
    (r'^ontario securities commission$', 'Ontario Securities Commission', 'https://www.osc.ca/', 'Ontario regulator'),
    (r'^travel alberta$', 'Travel Alberta', 'https://www.travelalberta.com/', 'Alberta crown corporation'),
    (r'^alberta utilities commission$', 'Alberta Utilities Commission', 'https://www.auc.ab.ca/', 'Alberta regulator'),
    (r'^ottawa community housing$', 'Ottawa Community Housing', 'https://www.och.ca/', 'municipal housing corporation'),
    (r'^town of niagara on the lake$', 'Town of Niagara-on-the-Lake', 'https://www.notl.com/', 'Ontario municipality'),
    (r'^town of penetanguishene$', 'Town of Penetanguishene', 'https://www.penetanguishene.ca/', 'Ontario municipality'),
    (r'^lapp corporation$', 'LAPP Corporation', 'https://www.lapp.ca/', 'Alberta pension plan corporation'),
    (r'^infrastructure ontario$', 'Infrastructure Ontario', 'https://www.infrastructureontario.ca/', 'Ontario crown agency'),
    (r'^district municipality of muskoka$', 'District Municipality of Muskoka', 'https://www.muskoka.on.ca/', 'Ontario upper-tier municipality'),
    (r'^workplacenl$', 'WorkplaceNL', 'https://workplacenl.ca/', 'NL workers compensation board'),
    (r'^city of welland$', 'City of Welland', 'https://www.welland.ca/', 'Ontario municipality'),
    (r'^city of brockville$', 'City of Brockville', 'https://brockville.com/', 'Ontario municipality'),
    (r'^london police service$', 'London Police Service', 'https://www.londonpolice.ca/', 'municipal police service'),
    (r'^alberta securities commission$', 'Alberta Securities Commission', 'https://www.asc.ca/', 'Alberta regulator'),
    (r'^university of houston$', 'University of Houston', 'https://www.uh.edu/', 'Texas state university'),
    (r'^texas education agency$', 'Texas Education Agency', 'https://tea.texas.gov/', 'Texas state agency'),
    (r'^texas division of emergency management$', 'Texas Division of Emergency Management', 'https://tdem.texas.gov/', 'Texas state agency'),
    (r'^teacher retirement system$', 'Teacher Retirement System of Texas', 'https://www.trs.texas.gov/', 'Texas state agency'),
    (r'^employees retirement system$', 'Employees Retirement System of Texas', 'https://ers.texas.gov/', 'Texas state agency'),
    (r'^the university of texas health science center at san antonio$', 'UT Health San Antonio', 'https://www.uthscsa.edu/', 'Texas state institution'),
    (r'^the university of texas southwestern medical center$', 'UT Southwestern Medical Center', 'https://www.utsouthwestern.edu/', 'Texas state institution'),
    (r'^los angeles superior court$', 'Superior Court of California, County of Los Angeles', 'https://www.lacourt.org/', 'US state court'),
    (r'^waterloo regional health network$', 'Waterloo Regional Health Network', 'https://www.wrhn.ca/', 'hospital'),
    (r'^thunder bay regional health sci', 'Thunder Bay Regional Health Sciences Centre', 'https://tbrhsc.net/', 'hospital'),
    (r'^the ottawa hospital$', 'The Ottawa Hospital', 'https://www.ottawahospital.on.ca/', 'hospital'),
    (r'^st joseph s healthcare hamilton$', "St. Joseph's Healthcare Hamilton", 'https://www.stjoes.ca/', 'hospital'),
    (r'^toronto zoo$', 'Toronto Zoo', 'https://www.torontozoo.com/', 'City of Toronto agency'),
    (r'^lakehead university$', 'Lakehead University', 'https://www.lakeheadu.ca/', 'university'),
    (r'^athabasca university$', 'Athabasca University', 'https://www.athabascau.ca/', 'university'),
    (r'^university of lethbridge$', 'University of Lethbridge', 'https://www.ulethbridge.ca/', 'university'),
    (r'^mount royal university$', 'Mount Royal University', 'https://www.mtroyal.ca/', 'university'),
    (r'^bow valley college$', 'Bow Valley College', 'https://bowvalleycollege.ca/', 'college'),
    (r'^olds college$', 'Olds College', 'https://www.oldscollege.ca/', 'college'),
    (r'^lakeland college$', 'Lakeland College', 'https://www.lakelandcollege.ca/', 'college'),
    (r'^norquest college$', 'NorQuest College', 'https://www.norquest.ca/', 'college'),
    (r'^medicine hat college$', 'Medicine Hat College', 'https://www.mhc.ab.ca/', 'college'),
    (r'^lethbridge polytechnic$', 'Lethbridge Polytechnic', 'https://lethpolytech.ca/', 'post-secondary'),
    (r'^calgary public library$', 'Calgary Public Library', 'https://calgarylibrary.ca/', 'public library'),
    (r'^edmonton public library$', 'Edmonton Public Library', 'https://www.epl.ca/', 'public library'),
    (r'^edmonton police service$', 'Edmonton Police Service', 'https://www.edmontonpolice.ca/', 'municipal police service'),
    (r'^calgary board of education$', 'Calgary Board of Education', 'https://cbe.ab.ca/', 'Alberta school division'),
    (r'^edmonton school division$', 'Edmonton Public Schools', 'https://www.epsb.ca/', 'Alberta school division'),
    (r'^yukon university$', 'Yukon University', 'https://www.yukonu.ca/', 'university'),
    (r'^college of the north atlantic$', 'College of the North Atlantic', 'https://www.cna.nl.ca/', 'college'),
    (r'^n s community colleges$', 'Nova Scotia Community College', 'https://www.nscc.ca/', 'college'),
    (r'^chignecto central reg', 'Chignecto-Central Regional Centre for Education', 'https://www.ccrce.ca/', 'Nova Scotia regional centre for education'),
    (r'^municipality of the district of lunenburg$', 'Municipality of the District of Lunenburg', 'https://www.modl.ca/', 'Nova Scotia municipality'),
    (r'^halifax dartmouth bridge commission$', 'Halifax Harbour Bridges', 'https://www.hdbc.ca/', 'NS crown commission'),
    (r'^healthpro procurement services', 'HealthPRO Procurement Services Inc.', 'https://www.healthprocanada.com/', 'health group purchasing organisation'),
    (r'^municipality of the county of cumberland$', 'Municipality of the County of Cumberland', 'https://www.cumberlandcounty.ns.ca/', 'Nova Scotia municipality'),
    (r'^municipality of kings county$', 'Municipality of the County of Kings', 'https://www.countyofkings.ca/', 'Nova Scotia municipality'),
    (r'^municipality of the county of colchester$', 'Municipality of the County of Colchester', 'https://www.colchester.ca/', 'Nova Scotia municipality'),
    (r'^workers compensation board of n s', 'Workers Compensation Board of Nova Scotia', 'https://www.wcb.ns.ca/', 'NS workers compensation board'),
    (r'^saint marys university$|^saint mary s university$', "Saint Mary's University", 'https://www.smu.ca/', 'university'),
    (r'^city of cambridge$', 'City of Cambridge', 'https://www.cambridge.ca/', 'Ontario municipality'),
    (r'^ehealth saskatchewan$', 'eHealth Saskatchewan', 'https://www.ehealthsask.ca/', 'Saskatchewan treasury board agency'),
    (r'^texas a m university$', 'Texas A&M University', 'https://www.tamu.edu/', 'Texas state university'),
    (r'^texas tech university health sciences center$', 'Texas Tech University Health Sciences Center', 'https://www.ttuhsc.edu/', 'Texas state institution'),
    (r'^texas tech university health sciences center at el paso$', 'Texas Tech University Health Sciences Center El Paso', 'https://elpaso.ttuhsc.edu/', 'Texas state institution'),
    (r'^texas tech university$', 'Texas Tech University', 'https://www.ttu.edu/', 'Texas state university'),
    (r'^lamar university$', 'Lamar University', 'https://www.lamar.edu/', 'Texas state university'),
    (r'^stephen f austin state university$', 'Stephen F. Austin State University', 'https://www.sfasu.edu/', 'Texas state university'),
    (r'^tarleton state university$', 'Tarleton State University', 'https://www.tarleton.edu/', 'Texas state university'),
    (r'^texas a m university at galveston$', 'Texas A&M University at Galveston', 'https://www.tamug.edu/', 'Texas state university'),
    (r'^texas a m university central texas$', 'Texas A&M University–Central Texas', 'https://www.tamuct.edu/', 'Texas state university'),
    (r'^texas lottery commission$', 'Texas Lottery Commission', 'https://www.texaslottery.com/', 'Texas state agency'),
    (r'^the university of texas at san antonio$', 'The University of Texas at San Antonio', 'https://www.utsa.edu/', 'Texas state university'),
    (r'^the university of texas rio grande valley$', 'The University of Texas Rio Grande Valley', 'https://www.utrgv.edu/', 'Texas state university'),
    (r'^the university of texas at arlington$', 'The University of Texas at Arlington', 'https://www.uta.edu/', 'Texas state university'),
    (r'^the university of texas at dallas$', 'The University of Texas at Dallas', 'https://www.utdallas.edu/', 'Texas state university'),
    (r'^the university of texas permian basin$', 'The University of Texas Permian Basin', 'https://www.utpb.edu/', 'Texas state university'),
    (r'^texas a m engineering extension service$', 'Texas A&M Engineering Extension Service (TEEX)', 'https://teex.org/', 'Texas state agency'),
    (r'^department of criminal justice$', 'Texas Department of Criminal Justice', 'https://www.tdcj.texas.gov/', 'Texas state agency'),
    (r'^department of insurance$', 'Texas Department of Insurance', 'https://www.tdi.texas.gov/', 'Texas state agency'),
    (r'^parks and wildlife department$', 'Texas Parks and Wildlife Department', 'https://tpwd.texas.gov/', 'Texas state agency'),
    (r'^library archives commission$', 'Texas State Library and Archives Commission', 'https://www.tsl.texas.gov/', 'Texas state agency'),
    (r'^texas department of information resources', 'Texas Department of Information Resources (DIR)', 'https://dir.texas.gov/', 'Texas state agency'),
    (r'^george mason university$', 'George Mason University', 'https://www.gmu.edu/', 'Virginia public university'),
    (r'^radford university$', 'Radford University', 'https://www.radford.edu/', 'Virginia public university'),
    (r'^college of william mary$', 'William & Mary', 'https://www.wm.edu/', 'Virginia public university'),
    (r'^university of mary washington$', 'University of Mary Washington', 'https://www.umw.edu/', 'Virginia public university'),
    (r'^virginia state university$', 'Virginia State University', 'https://www.vsu.edu/', 'Virginia public university'),
    (r'^virginia military institute$', 'Virginia Military Institute', 'https://www.vmi.edu/', 'Virginia public college'),
    (r'^christopher newport university$', 'Christopher Newport University', 'https://cnu.edu/', 'Virginia public university'),
    (r'^virginia department of transportation$', 'Virginia Department of Transportation', 'https://www.vdot.virginia.gov/', 'Virginia state agency'),
    (r'^virginia department of health$', 'Virginia Department of Health', 'https://www.vdh.virginia.gov/', 'Virginia state agency'),
    (r'^virginia museum of fine arts$', 'Virginia Museum of Fine Arts', 'https://vmfa.museum/', 'Virginia state agency'),
    (r'^science museum of virginia$', 'Science Museum of Virginia', 'https://smv.org/', 'Virginia state agency'),
    (r'^library of virginia$', 'Library of Virginia', 'https://www.lva.virginia.gov/', 'Virginia state agency'),
    (r'^oregon state lottery$', 'Oregon Lottery', 'https://www.oregonlottery.org/', 'Oregon state agency'),
]
PROV_CODE = {'Ontario': 'ON', 'Alberta': 'AB', 'British Columbia': 'BC', 'Nova Scotia': 'NS', 'Saskatchewan': 'SK', 'Newfoundland and Labrador': 'NL',
             'Manitoba': 'MB', 'New Brunswick': 'NB', 'Prince Edward Island': 'PE', 'Quebec': 'QC', 'Yukon': 'YT', 'Northwest Territories': 'NT',
             'Nunavut': 'NU', 'Virginia': 'VA', 'Texas': 'TX', 'Massachusetts': 'MA', 'New York': 'NY', 'Vermont': 'VT', 'Alaska': 'AK', 'Oregon': 'OR',
             'Maryland': 'MD', 'Florida': 'FL', 'Arizona': 'AZ', 'Georgia': 'GA', 'California': 'CA', 'Louisiana': 'LA', 'Rhode Island': 'RI',
             'Oklahoma': 'OK', 'Delaware': 'DE', 'Minnesota': 'MN'}
MUNI_CLS = re.compile(r'(municipal|city|town|township|village|county|district|region|hamlet|borough|summer village|local government|census subdivision|urban|rural)', re.I)


def mtime(p):
    return datetime.datetime.fromtimestamp(os.path.getmtime(p), datetime.timezone.utc).replace(tzinfo=None).replace(microsecond=0).isoformat() + 'Z'


def main():
    buyers = load_buyers()
    C = json.load(open(WORK + '/classify.json'))
    out = {}

    def rec(k):
        if k not in out:
            out[k] = {'identifiers': {}, 'address': {}, 'general_contact': {'emails': [], 'phone': ''}, 'official_website': '', 'canonical_name': '',
                      'organisation_type': '', 'sources': [], 'notes': []}
        return out[k]
    st = collections.Counter()
    # ---- Wikidata index
    wd_dir = DL2 + '/dir/wikidata'
    qlab = json.load(open(wd_dir + '/qid_labels.json'))['labels'] if os.path.exists(wd_dir + '/qid_labels.json') else {}
    items = {}
    for f in sorted(glob.glob(wd_dir + '/batch_*.json')):
        d = json.load(open(f))
        for b in d['results']['bindings']:
            q = b['item']['value'].rsplit('/', 1)[1]
            it = items.setdefault(q, {'qid': q, 'labels': set(), 'webs': [], 'countries': set(), 'classes': set(), 'provs': set(), 'retrieved_at': d['_retrieved_at'], 'batch': os.path.basename(f)})
            it['labels'].add(b['lab']['value'])
            w = b['web']['value']
            if w not in it['webs']:
                it['webs'].append(w)
            for v, s in (('country', 'countries'), ('cls', 'classes'), ('prov', 'provs')):
                if v in b:
                    it[s].add(qlab.get(b[v]['value'].rsplit('/', 1)[1], b[v]['value'].rsplit('/', 1)[1]))
    by_label = collections.defaultdict(set)
    for q, it in items.items():
        for l in it['labels']:
            by_label[norm(l)].add(q)
    # ---- Ontario school boards
    sb_p = DL2 + '/dir/on_school_board_contact_list_september2026_en.csv'
    SB = {}
    if os.path.exists(sb_p):
        for r in csv.DictReader(open(sb_p, encoding='utf-8-sig', errors='replace')):
            SB[norm(r['Board Name'].replace('&', ' and '))] = r
    for b in buyers:
        k = b['buyer_key']; c = C[k]; nn = norm(b['name'])
        par = c.get('parent')
        if par:
            r = rec(k)
            r['parent'] = par
            r['canonical_name'] = b['name'] if norm(b['name']) != norm(par['name']) else par['name']
            r['organisation_type'] = ('unit of ' + par['name']) if norm(b['name']) != norm(par['name']) else (b['types'][0]['value'] if b['types'] else '')
            site = PARENT_SITE.get(par['key'], '')
            if site:
                r['official_website'] = site
                r['website_is_parent'] = True
            r['sources'].append({'source': 'parent-organisation rule (scripts/enrichment_buyers_v2/classify.py)', 'url': site, 'retrieved_at': now(),
                                 'match_basis': par['basis'], 'match_confidence': 'strong'})
            st['parent'] += 1
            continue
        if c.get('ambiguous_jurisdictions'):
            r = rec(k)
            r['ambiguous_jurisdictions'] = c['ambiguous_jurisdictions']
            r['notes'].append('buyer name "%s" is used by departments of several governments in the data (%s); not resolved to one organisation' %
                              (b['name'], ', '.join('%s: %d records' % kv for kv in sorted(c['ambiguous_jurisdictions'].items(), key=lambda t: -t[1]))))
            st['ambiguous'] += 1
            continue
        # alias rules
        hit = None
        for rx, cn, site, typ in ALIAS:
            if re.search(rx, nn):
                hit = (rx, cn, site, typ); break
        if hit:
            r = rec(k)
            r['canonical_name'] = hit[1]; r['official_website'] = hit[2]; r['organisation_type'] = hit[3]
            r['sources'].append({'source': 'alias rule (scripts/enrichment_buyers_v2/bulk_v2.py); website = official domain, verified by crawler fetch',
                                 'url': hit[2], 'retrieved_at': now(), 'match_basis': 'alias rule /%s/' % hit[0], 'match_confidence': 'strong'})
            st['alias'] += 1
            continue
        # Ontario school boards
        if 'ON' in (c['province'], *c['tz_provinces']) or b['country'] == 'CA':
            first = norm(re.split(r'\s+&\s+(?=[A-Z])|\s+/\s+', b['name'])[0])
            sb = SB.get(first) or SB.get(nn) or SB.get(norm(b['name'].replace('&', ' and ')))
            if sb:
                r = rec(k)
                r['canonical_name'] = sb['Board Name']; r['organisation_type'] = 'Ontario school board (%s)' % sb['Board Type']
                r['identifiers']['ontario_board_number'] = sb['Board Number']
                r['official_website'] = sb['Website'].strip()
                r['address'] = {'line1': ' '.join(x for x in (sb['Suite'], sb['Street'], ('PO Box ' + sb['PO Box']) if sb['PO Box'] else '') if x).strip(), 'city': sb['City'],
                                'region': 'ON', 'postal_code': sb['Postal Code'], 'country': 'CA'}
                r['general_contact']['phone'] = sb['Phone Number']
                r['extras_dir'] = {'fax': sb['Fax']}
                r['sources'].append({'source': 'Ontario Ministry of Education, School board and school authority contact information (data.ontario.ca, September 2026 CSV)',
                                     'url': 'https://data.ontario.ca/dataset/9831236f-6e01-447a-9e28-b9c6b3348631/resource/74aa6226-7798-4130-ba44-8546e3198186/download/school_board_contact_list_september2026_en_csv.csv',
                                     'retrieved_at': mtime(sb_p), 'match_basis': 'normalized board name == "%s"%s' % (sb['Board Name'], ' (first of a joint name)' if first != nn else ''),
                                     'match_confidence': 'exact'})
                st['on_school_board'] += 1
                continue
        # Wikidata labels
        if c['labels']:
            cand = set()
            for l in c['labels']:
                cand |= by_label.get(norm(l), set())
            cc = [items[q] for q in cand]
            want_country = {'CA': 'Canada', 'US': 'United States of America'}.get(b['country'])
            if want_country:
                cc = [it for it in cc if want_country in it['countries']]
            allowed = set([c['province']] if c['province'] else []) | set(c['tz_provinces'])
            prov_ok = []
            if allowed:
                prov_ok = [it for it in cc if {PROV_CODE.get(p) for p in it['provs']} & allowed]
            if c['designation']:
                m2 = [it for it in (prov_ok or cc) if any(MUNI_CLS.search(x) for x in it['classes'])]
                if prov_ok:
                    prov_ok = m2 or prov_ok
                else:
                    cc = m2
            pick = prov_ok if allowed else cc
            conf = 'strong' if (allowed and prov_ok) else 'weak'
            if not pick and allowed and not prov_ok:
                pick = []  # province known but no candidate located there
            if len(pick) > 1:
                full = {norm(x) for x in c['labels'] if norm(x) != norm(c['core'])} | {nn}
                dw = (c['designation'] or '').replace('county of', 'county').split()[-1:] if c['designation'] else []
                def score(it):
                    sc = 0
                    if {norm(l) for l in it['labels']} & full:
                        sc += 3
                    if dw and any(dw[0] in x.lower() for x in it['classes']):
                        sc += 2
                    return sc
                best = max(score(it) for it in pick)
                top = [it for it in pick if score(it) == best]
                if best > 0 and len({urllib.parse.urlsplit(it['webs'][0]).netloc.lower().replace('www.', '') for it in top}) == 1:
                    pick = top
            doms = {urllib.parse.urlsplit(w).netloc.lower().replace('www.', '') for it in pick for w in it['webs'][:1]}
            if pick and len(doms) == 1 and (conf == 'strong' or len(c['core'].split()) >= 2 or not c['designation']):
                it = sorted(pick, key=lambda x: (len(x['webs'][0]), x['qid']))[0]
                web = sorted(it['webs'], key=lambda w: (not w.startswith('https'), len(w)))[0]
                r = rec(k)
                r['canonical_name'] = r['canonical_name'] or b['name']
                r['organisation_type'] = r['organisation_type'] or ', '.join(sorted(it['classes']))[:120]
                r['official_website'] = web
                r['identifiers']['wikidata_qid'] = it['qid']
                r['sources'].append({'source': 'Wikidata (SPARQL label/alias lookup, official website P856)', 'url': 'https://www.wikidata.org/wiki/' + it['qid'],
                                     'retrieved_at': it['retrieved_at'], 'match_basis': 'label/alias %s == buyer name variant; country %s; located in %s; class %s' %
                                     (sorted(it['labels'])[:3], ','.join(sorted(it['countries'])), ','.join(sorted(it['provs'])) or '?', ','.join(sorted(it['classes']))[:100]),
                                     'match_confidence': conf})
                st['wikidata_' + conf] += 1
                continue
            elif len(doms) > 1:
                r = rec(k)
                r['notes'].append('Wikidata: %d candidate items with different websites (%s); not resolved' % (len(pick), ', '.join(sorted(doms))[:200]))
                st['wikidata_ambiguous'] += 1
        # website published in the contract notice's buyer contact block
        for cc_ in b.get('contacts', []):
            v = cc_['value'] or {}
            w = (v.get('url') or v.get('website') or '') if isinstance(v, dict) else ''
            if w and w.lower() not in ('none', 'null') and not re.search(r'merx|bidsandtenders|biddingo|seao|mercell|ungm|ted\.europa', w, re.I):
                if not w.startswith('http'):
                    w = 'http://' + w
                r = rec(k)
                r['official_website'] = r['official_website'] or w.strip().lower().rstrip('/')
                r['sources'].append({'source': 'website field of the buyer contact block in the contract notice', 'url': w, 'retrieved_at': '',
                                     'match_basis': 'published by the buyer in the notice', 'match_confidence': 'strong'})
                st['notice_website'] += 1
                break
    # ---- sites list for crawling (priority = sum of high/medium records)
    hm = {b['buyer_key']: b['record_count_high_or_medium'] for b in buyers}
    sites = collections.OrderedDict()
    for b in buyers:
        r = out.get(b['buyer_key'])
        if not r or not r.get('official_website'):
            continue
        s = r['official_website'].rstrip('/')
        if r['official_website'] in GOV_PORTALS:
            continue
        d = sites.setdefault(s, {'site': s, 'buyer_keys': [], 'prio': 0})
        d['buyer_keys'].append(b['buyer_key']); d['prio'] += hm[b['buyer_key']]
    sl = sorted(sites.values(), key=lambda x: -x['prio'])
    json.dump(sl, open(WORK + '/sites_main.json', 'w'), ensure_ascii=False, indent=0)
    json.dump(out, open(WORK + '/bulk.json', 'w'), ensure_ascii=False, indent=0)
    print(dict(st), 'records', len(out), 'sites', len(sl))


main()
