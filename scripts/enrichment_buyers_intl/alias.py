"""Stage 1b: alias rules for buyers not matched by bulk directories (CanadaBuys entity names, Quebec agencies, US agencies, etc.).
Websites here are the organisations' well-known official domains; each one is then fetched by the crawler, and only sites that
respond are kept as official_website (crawl status recorded). Updates WORK/bulk.json in place (adds records with source 'alias')."""
import json, re, sys, os, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

GC_ALIAS = [
    (r'public works and government services|\bpspc\b|services publics et approvisionnement|receiver general|translation bureau', 'pwgsc-tpsgc'),
    (r'correction+al services? (of )?can|corrections service|\bcsc\b|corcan|correctional service canda|regional headquarters prairie', 'csc-scc'),
    (r'fisheries and oceans|\bdfo\b', 'dfo-mpo'), (r'coast guard|\bccg\b', 'dfo-mpo'),
    (r'department of justice|\bjus\b', 'jus'), (r'parc?ks canada', 'pc'), (r'natural resources|\bnrcan\b', 'nrcan-rncan'),
    (r'superintendent of financial in', 'osfi-bsif'), (r'department of transport|\btc\b', 'tc'), (r'agriculture and agri food|\baafc\b', 'aafc-aac'),
    (r'department of the environment|\beccc\b', 'ec'), (r'auditor general', 'oag-bvg'), (r'national research council|nrc cnrc', 'nrc-cnrc'),
    (r'department of health|\bhc\b', 'hc-sc'), (r'department of industry|\bised\b|measurement canada', 'ic'),
    (r'employment and social development|\besdc\b|service canada|labour program', 'esdc-edsc'), (r'indigenous services', 'isc-sac'),
    (r'farm credit', 'fcc-fac'), (r'housing infrastructure and communities|office of infrastructure', 'infc'), (r'department of finance', 'fin'),
    (r'natural sciences and engineering', 'nserc-crsng'), (r'foreign affairs trade and development|\bgac\b', 'dfatd-maecd'),
    (r'federal judicial affairs', 'fja-cmf'), (r'export development canada', 'edc'), (r'secretary to the governor general', 'osgg-bsgg'),
    (r'citizenship (and )?immigration|\bircc\b', 'cic'), (r'invest in canada', 'iic-iac'), (r'privacy commissioner', 'opc-cpvp'), (r'marine atlantic', 'mai'),
    (r'commissioner of official languages', 'ocol-clo'), (r'public sector integrity', 'psic-ispc'), (r'information commissioner', 'oic-ci'),
    (r'canada post', 'cpc-scp'), (r'national defence|\bdnd\b|canadian army|royal canadian navy|cansofcom|special operations forces|defence investment agency|canadian armed forces|military personnel generation|director services contracting|directorate land procurement|royal military college', 'dnd-mdn'),
    (r'commissioner of lobbying', 'ocl-cal'), (r'chief electoral officer', 'elections'), (r'correctional investigator', 'oci-bec'),
    (r'economic development agency of canada for the regions of quebec', 'ced-dec'), (r'veterans affairs', 'vac-acc'), (r'library and archives', 'lac-bac'),
    (r'public safety and emergency', 'ps-sp'), (r'canada lands company|parc downsview', 'clcl-sicl'), (r'national battlefields', 'nbc-ccbn'),
    (r'immigration and refugee board', 'irb-cisr'), (r'women and gender equality', 'wage'), (r'public service commission', 'psc-cfp'),
    (r'rcmp|royal canadian mounted police|canadian police college', 'rcmp-grc'), (r'transportation accident investigation', 'tsb-bst'),
    (r'canada school of public service', 'csps-efpc'), (r'director of public prosecutions', 'ppsc-sppc'), (r'communications security establishment', 'csec-cstc'),
    (r'public health agency', 'phac-aspc'), (r'defence research and development', 'drdc-rddc'), (r'national capital commission|^ncc$', 'ncc-ccn'),
    (r'national film board', 'nfb-onf'), (r'western economic diversification', 'wd-deo'), (r'canada border services', 'cbsa-asfc'),
    (r'shared services canada', 'ssc-spc'), (r'statistics canada', 'statcan'), (r'canadian heritage', 'pch'), (r'treasury board', 'tbs-sct'),
    (r'canadian food inspection', 'cfia-acia'), (r'canada revenue agency', 'cra-arc'), (r'canadian space agency', 'csa-asc'),
    (r'via rail|via hfr', 'viarail'), (r'canadian commercial corporation', 'ccc'), (r'canadian nuclear safety', 'cnsc-ccsn'),
]
GC_SITE = {  # official sites not resolved from canada.ca/en/government/dept.html
    'pwgsc-tpsgc': 'https://www.canada.ca/en/public-services-procurement.html', 'csc-scc': 'https://www.canada.ca/en/correctional-service.html',
    'jus': 'https://www.justice.gc.ca/eng/', 'osfi-bsif': 'https://www.osfi-bsif.gc.ca/en', 'oag-bvg': 'https://www.oag-bvg.gc.ca/internet/English/admin_e_41.html',
    'fcc-fac': 'https://www.fcc-fac.ca/en', 'infc': 'https://housing-infrastructure.canada.ca/index-eng.html', 'fin': 'https://www.canada.ca/en/department-finance.html',
    'nserc-crsng': 'https://www.nserc-crsng.gc.ca/index_eng.asp', 'fja-cmf': 'https://www.fja-cmf.gc.ca/home-accueil/index-eng.html', 'osgg-bsgg': 'https://www.gg.ca/en',
    'iic-iac': 'https://www.investcanada.ca/', 'opc-cpvp': 'https://www.priv.gc.ca/en/', 'ocol-clo': 'https://www.clo-ocol.gc.ca/en', 'psic-ispc': 'https://psic-ispc.gc.ca/en',
    'oic-ci': 'https://www.oic-ci.gc.ca/en', 'ocl-cal': 'https://lobbycanada.gc.ca/en/', 'oci-bec': 'https://oci-bec.gc.ca/en', 'clcl-sicl': 'https://www.clc-sic.ca/',
    'wd-deo': 'https://www.canada.ca/en/prairies-economic-development.html', 'dfo-mpo': 'https://www.dfo-mpo.gc.ca/index-eng.html', 'pc': 'https://parks.canada.ca/index',
    'nrcan-rncan': 'https://natural-resources.canada.ca/', 'tc': 'https://tc.canada.ca/en', 'aafc-aac': 'https://agriculture.canada.ca/en',
    'ec': 'https://www.canada.ca/en/environment-climate-change.html', 'nrc-cnrc': 'https://nrc.canada.ca/en', 'hc-sc': 'https://www.canada.ca/en/health-canada.html',
    'ic': 'https://ised-isde.canada.ca/site/ised/en', 'esdc-edsc': 'https://www.canada.ca/en/employment-social-development.html',
    'isc-sac': 'https://www.canada.ca/en/indigenous-services-canada.html', 'dfatd-maecd': 'https://www.international.gc.ca/global-affairs-affaires-mondiales/home-accueil.aspx?lang=eng',
    'edc': 'https://www.edc.ca/', 'cic': 'https://www.canada.ca/en/immigration-refugees-citizenship.html', 'mai': 'https://www.marineatlantic.ca/',
    'cpc-scp': 'https://www.canadapost-postescanada.ca/cpc/en/home.page', 'dnd-mdn': 'https://www.canada.ca/en/department-national-defence.html',
    'rcmp-grc': 'https://rcmp.ca/en', 'viarail': 'https://www.viarail.ca/en', 'ccc': 'https://www.ccc.ca/en/',
}
GC_CCG_SITE = 'https://www.ccg-gcc.gc.ca/index-eng.html'

QC = [  # (regex on normalized name, canonical name, website, type)
    (r'^hydro quebec', 'Hydro-Québec', 'https://www.hydroquebec.com/', 'Quebec crown corporation'),
    (r'centre d acquisitions gouvernementales|direction des acquisitions strategiques et des unites specialisees', "Centre d'acquisitions gouvernementales (CAG)", 'https://www.quebec.ca/gouvernement/ministeres-organismes/centre-acquisitions-gouvernementales', 'Quebec public body'),
    (r'ministere des transports|^mtq\b|dgcger|^mtmd', 'Ministère des Transports et de la Mobilité durable', 'https://www.transports.gouv.qc.ca/', 'Quebec ministry'),
    (r'^sqi\b|societe quebecoise des infrastructures', 'Société québécoise des infrastructures', 'https://www.sqi.gouv.qc.ca/', 'Quebec crown corporation'),
    (r'ressources naturelles et des forets', 'Ministère des Ressources naturelles et des Forêts', 'https://mrnf.gouv.qc.ca/', 'Quebec ministry'),
    (r'^revenu quebec|agence du revenu du quebec', 'Revenu Québec', 'https://www.revenuquebec.ca/', 'Quebec agency'),
    (r'^societe de transport de montreal|^stm$', 'Société de transport de Montréal', 'https://www.stm.info/', 'Quebec public transit authority'),
    (r'assurance automobile du quebec', "Société de l'assurance automobile du Québec", 'https://saaq.gouv.qc.ca/', 'Quebec crown corporation'),
    (r'cybersecurite et du numerique', 'Ministère de la Cybersécurité et du Numérique', 'https://www.quebec.ca/gouvernement/ministere/cybersecurite-numerique', 'Quebec ministry'),
    (r'reseau de transport de la capitale', 'Réseau de transport de la Capitale', 'https://www.rtcquebec.ca/', 'Quebec public transit authority'),
    (r'ministere de l environnement', "Ministère de l'Environnement, de la Lutte contre les changements climatiques, de la Faune et des Parcs", 'https://www.environnement.gouv.qc.ca/', 'Quebec ministry'),
    (r'^loto quebec', 'Loto-Québec', 'https://societe.lotoquebec.com/', 'Quebec crown corporation'),
    (r'curateur public', 'Curateur public du Québec', 'https://www.curateur.gouv.qc.ca/', 'Quebec agency'),
    (r'universite mcgill|mcgill university', 'McGill University', 'https://www.mcgill.ca/', 'university'),
    (r'^universite laval', 'Université Laval', 'https://www.ulaval.ca/', 'university'),
    (r'surete du quebec', 'Sûreté du Québec', 'https://www.sq.gouv.qc.ca/', 'Quebec police'),
    (r'^retraite quebec', 'Retraite Québec', 'https://www.retraitequebec.gouv.qc.ca/', 'Quebec agency'),
    (r'commission des normes de l equite|^cnesst', 'CNESST', 'https://www.cnesst.gouv.qc.ca/', 'Quebec agency'),
    (r'^omh de montreal|office municipal d habitation de montreal', "Office municipal d'habitation de Montréal", 'https://www.omhm.qc.ca/', 'municipal housing office'),
    (r'reseau de transport de longueuil', 'Réseau de transport de Longueuil', 'https://www.rtl-longueuil.qc.ca/', 'Quebec public transit authority'),
    (r'regie de l assurance maladie', "Régie de l'assurance maladie du Québec", 'https://www.ramq.gouv.qc.ca/', 'Quebec agency'),
    (r'etablissements de plein air|sepaq', 'Sépaq', 'https://www.sepaq.com/', 'Quebec crown corporation'),
    (r'^sante quebec$', 'Santé Québec', 'https://www.santequebec.ca/', 'Quebec health agency'),
    (r'^universite de montreal', 'Université de Montréal', 'https://www.umontreal.ca/', 'university'),
    (r'universite du quebec a montreal|^uqam', 'Université du Québec à Montréal', 'https://uqam.ca/', 'university'),
    (r'transport metropolitain|^exo\b', 'exo (Réseau de transport métropolitain)', 'https://exo.quebec/', 'Quebec public transit authority'),
    (r'societe des alcools du quebec', 'Société des alcools du Québec', 'https://www.saq.com/', 'Quebec crown corporation'),
    (r'^ministere de l education', "Ministère de l'Éducation", 'https://www.quebec.ca/gouvernement/ministere/education', 'Quebec ministry'),
    (r'^ministere de la justice', 'Ministère de la Justice du Québec', 'https://www.justice.gouv.qc.ca/', 'Quebec ministry'),
    (r'urgences sante', "Corporation d'urgences-santé", 'https://www.urgences-sante.qc.ca/', 'Quebec agency'),
    (r'^hema quebec', 'Héma-Québec', 'https://www.hema-quebec.qc.ca/', 'Quebec public body'),
    (r'securite interieure|securite publique', 'Ministère de la Sécurité publique / Sécurité intérieure', 'https://www.quebec.ca/gouvernement/ministere/securite-publique', 'Quebec ministry'),
    (r'societe de transport de sherbrooke', 'Société de transport de Sherbrooke', 'https://www.sts.qc.ca/', 'Quebec public transit authority'),
    (r'assemblee nationale', 'Assemblée nationale du Québec', 'https://www.assnat.qc.ca/', 'Quebec legislature'),
    (r'emploi et de la solidarite sociale', "Ministère de l'Emploi et de la Solidarité sociale", 'https://www.quebec.ca/gouvernement/ministere/emploi-solidarite-sociale', 'Quebec ministry'),
    (r'economie de l innovation', "Ministère de l'Économie, de l'Innovation et de l'Énergie", 'https://www.economie.gouv.qc.ca/', 'Quebec ministry'),
    (r'societe des traversiers', 'Société des traversiers du Québec', 'https://www.traversiers.com/', 'Quebec crown corporation'),
    (r'financiere agricole', 'La Financière agricole du Québec', 'https://www.fadq.qc.ca/', 'Quebec crown corporation'),
    (r'college de maisonneuve', 'Collège de Maisonneuve', 'https://www.cmaisonneuve.qc.ca/', 'CEGEP'),
    (r'parc auto du quebec', 'Société parc-auto du Québec', 'https://www.spaq.com/', 'Quebec crown corporation'),
    (r'habitation et de developpement de montreal', "Société d'habitation et de développement de Montréal", 'https://www.shdm.org/', 'Montreal paramunicipal corporation'),
    (r'^parc olympique', 'Parc olympique', 'https://parcolympique.qc.ca/', 'Quebec crown corporation'),
    (r'regie du batiment', 'Régie du bâtiment du Québec', 'https://www.rbq.gouv.qc.ca/', 'Quebec agency'),
    (r'societe de transport de l outaouais', "Société de transport de l'Outaouais", 'https://www.sto.ca/', 'Quebec public transit authority'),
    (r'universite du quebec a trois rivieres', 'Université du Québec à Trois-Rivières', 'https://www.uqtr.ca/', 'university'),
    (r'agriculture des pecheries', "Ministère de l'Agriculture, des Pêcheries et de l'Alimentation", 'https://www.mapaq.gouv.qc.ca/', 'Quebec ministry'),
    (r'verificateur general du quebec', 'Vérificateur général du Québec', 'https://www.vgq.qc.ca/', 'Quebec legislative body'),
    (r'autorite des marches financiers', 'Autorité des marchés financiers', 'https://lautorite.qc.ca/', 'Quebec regulator'),
    (r'concordia', 'Concordia University', 'https://www.concordia.ca/', 'university'),
    (r'soquij|information juridique', "Société québécoise d'information juridique", 'https://soquij.qc.ca/', 'Quebec crown corporation'),
    (r'autorite regionale de transport metropolitain|^artm', 'Autorité régionale de transport métropolitain', 'https://www.artm.quebec/', 'Quebec transit authority'),
    (r'commission de la construction du quebec', 'Commission de la construction du Québec', 'https://www.ccq.org/', 'Quebec agency'),
    (r'^hec montreal', 'HEC Montréal', 'https://www.hec.ca/', 'university'),
    (r'societe d habitation du quebec', "Société d'habitation du Québec", 'https://www.habitation.gouv.qc.ca/', 'Quebec crown corporation'),
    (r'societe de transport de laval', 'Société de transport de Laval', 'https://stlaval.ca/', 'Quebec public transit authority'),
    (r'union des municipalites du quebec', 'Union des municipalités du Québec', 'https://umq.qc.ca/', 'municipal association'),
    (r'ecole de technologie superieure', 'École de technologie supérieure', 'https://www.etsmtl.ca/', 'university'),
    (r'agence de mobilite durable', 'Agence de mobilité durable', 'https://agencemobilitedurable.ca/', 'Montreal paramunicipal agency'),
    (r'directeur general des elections du quebec', 'Élections Québec', 'https://www.electionsquebec.qc.ca/', 'Quebec legislative body'),
    (r'institut de technologie agroalimentaire', 'Institut de technologie agroalimentaire du Québec', 'https://www.itaq.ca/', 'college'),
    (r'bibliotheque et archives nationales', 'Bibliothèque et Archives nationales du Québec', 'https://www.banq.qc.ca/', 'Quebec agency'),
    (r'universite de sherbrooke', 'Université de Sherbrooke', 'https://www.usherbrooke.ca/', 'university'),
    (r'ecole polytechnique|polytechnique montreal', 'Polytechnique Montréal', 'https://www.polymtl.ca/', 'university'),
    (r'cegep de jonquiere', 'Cégep de Jonquière', 'https://www.cegepjonquiere.ca/', 'CEGEP'),
    (r'universite du quebec en abitibi|universite du quebec de l abitibi|uqat', "Université du Québec en Abitibi-Témiscamingue", 'https://www.uqat.ca/', 'university'),
    (r'universite du quebec a chicoutimi|uqac', 'Université du Québec à Chicoutimi', 'https://www.uqac.ca/', 'university'),
    (r'universite du quebec a rimouski|uqar', 'Université du Québec à Rimouski', 'https://www.uqar.ca/', 'university'),
    (r'universite du quebec en outaouais|uqo\b', 'Université du Québec en Outaouais', 'https://uqo.ca/', 'university'),
    (r'institut national de la recherche scientifique|^inrs', 'Institut national de la recherche scientifique', 'https://inrs.ca/', 'university'),
    (r'universite bishop|bishop s university', "Bishop's University", 'https://www.ubishops.ca/', 'university'),
    (r'tourisme quebec|ministere du tourisme', 'Ministère du Tourisme', 'https://www.quebec.ca/gouvernement/ministere/tourisme', 'Quebec ministry'),
    (r'ministere de la culture', 'Ministère de la Culture et des Communications', 'https://www.quebec.ca/gouvernement/ministere/culture-communications', 'Quebec ministry'),
    (r'ministere des finances', 'Ministère des Finances du Québec', 'https://www.finances.gouv.qc.ca/', 'Quebec ministry'),
    (r'investissement quebec', 'Investissement Québec', 'https://www.investquebec.com/', 'Quebec crown corporation'),
    (r'caisse de depot', 'CDPQ', 'https://www.cdpq.com/', 'Quebec crown corporation'),
    (r'telé quebec|tele quebec', 'Télé-Québec', 'https://www.telequebec.tv/', 'Quebec crown corporation'),
    (r'societe du parc jean drapeau', 'Société du parc Jean-Drapeau', 'https://www.parcjeandrapeau.com/', 'Montreal paramunicipal corporation'),
    (r'commission des services electriques de montreal', 'Commission des services électriques de Montréal', 'https://cse.montreal.ca/', 'Montreal municipal body'),
    (r'^energir', 'Énergir', 'https://www.energir.com/', 'utility'),
    (r'palais des congres de montreal', 'Société du Palais des congrès de Montréal', 'https://congresmtl.com/', 'Quebec crown corporation'),
    (r'societe de developpement de la baie james', 'Société de développement de la Baie-James', 'https://www.sdbj.gouv.qc.ca/', 'Quebec crown corporation'),
    (r'institut national de sante publique', 'Institut national de santé publique du Québec', 'https://www.inspq.qc.ca/', 'Quebec public body'),
    (r'sainte justine|ste justine', 'CHU Sainte-Justine', 'https://www.chusj.org/', 'Quebec health establishment'),
    (r'societe quebecoise du cannabis', 'Société québécoise du cannabis', 'https://www.sqdc.ca/', 'Quebec crown corporation'),
    (r'institut de tourisme et d hotellerie', "Institut de tourisme et d'hôtellerie du Québec", 'https://www.ithq.qc.ca/', 'Quebec public body'),
    (r'place des arts', 'Société de la Place des Arts de Montréal', 'https://placedesarts.com/', 'Quebec crown corporation'),
    (r'autorite des marches publics', 'Autorité des marchés publics', 'https://amp.quebec/', 'Quebec regulator'),
    (r'^rexforet', 'Rexforêt', 'https://www.rexforet.com/', 'Quebec crown corporation'),
    (r'commission de la capitale nationale du quebec', 'Commission de la capitale nationale du Québec', 'https://www.capitale.gouv.qc.ca/', 'Quebec public body'),
    (r'^college ahuntsic', 'Collège Ahuntsic', 'https://www.collegeahuntsic.qc.ca/', 'CEGEP'),
    (r'universite du quebec siege social|^universite du quebec$', 'Université du Québec (siège social)', 'https://www.uquebec.ca/', 'university network'),
    (r'^ministere de la famille', 'Ministère de la Famille', 'https://www.quebec.ca/gouvernement/ministere/famille', 'Quebec ministry'),
    (r'^ministere de la sante et des services sociaux', 'Ministère de la Santé et des Services sociaux', 'https://www.msss.gouv.qc.ca/', 'Quebec ministry'),
    (r'immigration de la francisation', "Ministère de l'Immigration, de la Francisation et de l'Intégration", 'https://www.quebec.ca/gouvernement/ministere/immigration', 'Quebec ministry'),
    (r'^cegep de saint laurent', 'Cégep de Saint-Laurent', 'https://www.cegepsl.qc.ca/', 'CEGEP'),
    (r'^college dawson|^dawson college', 'Dawson College', 'https://www.dawsoncollege.qc.ca/', 'CEGEP'),
    (r'ecole nationale de police', 'École nationale de police du Québec', 'https://www.enpq.qc.ca/', 'Quebec public body'),
    (r'societe de telediffusion du quebec', 'Télé-Québec', 'https://www.telequebec.tv/', 'Quebec crown corporation'),
    (r'^cegep limoilou', 'Cégep Limoilou', 'https://www.cegeplimoilou.ca/', 'CEGEP'),
    (r'^cegep de saint jerome', 'Cégep de Saint-Jérôme', 'https://www.cstj.qc.ca/', 'CEGEP'),
    (r'western quebec school board', 'Western Québec School Board', 'https://www.wqsb.qc.ca/', 'school board'),
    (r'^collecto', 'Collecto Services regroupés en éducation', 'https://www.collecto.ca/', 'Quebec education purchasing group'),
    (r'ministere des affaires municipales', "Ministère des Affaires municipales et de l'Habitation", 'https://www.quebec.ca/gouvernement/ministere/affaires-municipales', 'Quebec ministry'),
    (r'parc industriel et portuaire de becancour', 'Société du parc industriel et portuaire de Bécancour', 'https://www.spipb.com/', 'Quebec crown corporation'),
    (r'^cegep de|^college de |^college lionel groulx|^college montmorency|^college edouard montpetit', None, None, None),
]
US_AG = {  # awarding_agency_code -> (name, website)
    '3300': ('Smithsonian Institution', 'https://www.si.edu/'), '524': ('Millennium Challenge Corporation', 'https://www.mcc.gov/'),
    '027': ('Federal Communications Commission', 'https://www.fcc.gov/'), '1601': ('Department of Labor', 'https://www.dol.gov/'),
    '1602': ('Pension Benefit Guaranty Corporation', 'https://www.pbgc.gov/'), '3302': ('National Gallery of Art', 'https://www.nga.gov/'),
    '060': ('Railroad Retirement Board', 'https://www.rrb.gov/'), '424': ('National Transportation Safety Board', 'https://www.ntsb.gov/'),
    '003': ('Library of Congress', 'https://www.loc.gov/'), '349': ('District of Columbia Courts', 'https://www.dccourts.gov/'),
    '097': ('Department of Defense', 'https://www.defense.gov/'), '014': ('Department of the Interior', 'https://www.doi.gov/'),
    '047': ('General Services Administration', 'https://www.gsa.gov/'), '075': ('Department of Health and Human Services', 'https://www.hhs.gov/'),
    '036': ('Department of Veterans Affairs', 'https://www.va.gov/'), '019': ('Department of State', 'https://www.state.gov/'),
    '013': ('Department of Commerce', 'https://www.commerce.gov/'), '012': ('Department of Agriculture', 'https://www.usda.gov/'),
    '015': ('Department of Justice', 'https://www.justice.gov/'), '080': ('National Aeronautics and Space Administration', 'https://www.nasa.gov/'),
    '070': ('Department of Homeland Security', 'https://www.dhs.gov/'), '089': ('Department of Energy', 'https://www.energy.gov/'),
    '069': ('Department of Transportation', 'https://www.transportation.gov/'), '020': ('Department of the Treasury', 'https://home.treasury.gov/'),
    '068': ('Environmental Protection Agency', 'https://www.epa.gov/'), '072': ('Agency for International Development', 'https://www.usaid.gov/'),
    '049': ('National Science Foundation', 'https://www.nsf.gov/'), '091': ('Department of Education', 'https://www.ed.gov/'),
    '016': ('Department of Labor', 'https://www.dol.gov/'), '086': ('Department of Housing and Urban Development', 'https://www.hud.gov/'),
    '028': ('Social Security Administration', 'https://www.ssa.gov/'), '031': ('Nuclear Regulatory Commission', 'https://www.nrc.gov/'),
    '024': ('Office of Personnel Management', 'https://www.opm.gov/'), '073': ('Small Business Administration', 'https://www.sba.gov/'),
    '033': ('Smithsonian Institution', 'https://www.si.edu/'), '059': ('National Endowment for the Arts', 'https://www.arts.gov/'),
    '095': ('Independent agencies', ''), '011': ('Executive Office of the President', 'https://www.whitehouse.gov/'),
    '064': ('Tennessee Valley Authority', 'https://www.tva.com/'), '061': ('Consumer Product Safety Commission', 'https://www.cpsc.gov/'),
    '088': ('National Archives and Records Administration', 'https://www.archives.gov/'), '090': ('Department of Justice? (code 090)', ''),
    '514': ('U.S. Agency for Global Media', 'https://www.usagm.gov/'), '029': ('Federal Trade Commission', 'https://www.ftc.gov/'),
    '045': ('Equal Employment Opportunity Commission', 'https://www.eeoc.gov/'), '050': ('Securities and Exchange Commission', 'https://www.sec.gov/'),
}

AU_AG = [  # (regex on normalized name, website)
    (r'^department of defence$|royal australian air force', 'https://www.defence.gov.au/'), (r'^austrade', 'https://www.austrade.gov.au/'),
    (r'^department of foreign affairs and trade', 'https://www.dfat.gov.au/'), (r'^geoscience australia', 'https://www.ga.gov.au/'),
    (r'^bureau of meteorology', 'https://www.bom.gov.au/'), (r'^department of climate change energy', 'https://www.dcceew.gov.au/'),
    (r'^department of industry science and resources', 'https://www.industry.gov.au/'), (r'^australian signals directorate', 'https://www.asd.gov.au/'),
    (r'^australian centre for international agricultural research', 'https://www.aciar.gov.au/'), (r'^australian transaction reports', 'https://www.austrac.gov.au/'),
    (r'^department of health', 'https://www.health.gov.au/'), (r'^department of infrastructure transport', 'https://www.infrastructure.gov.au/'),
    (r'^attorney general s department', 'https://www.ag.gov.au/'), (r'^australian bureau of statistics', 'https://www.abs.gov.au/'),
    (r'^australian centre for disease control', 'https://www.cdc.gov.au/'), (r'^australian criminal intelligence commission', 'https://www.acic.gov.au/'),
    (r'^australian financial security authority', 'https://www.afsa.gov.au/'), (r'^australian office of financial management', 'https://www.aofm.gov.au/'),
    (r'^australian prudential regulation authority', 'https://www.apra.gov.au/'), (r'^australian research council', 'https://www.arc.gov.au/'),
    (r'^csiro', 'https://www.csiro.au/'), (r'^clean energy regulator', 'https://cer.gov.au/'), (r'^department of finance$', 'https://www.finance.gov.au/'),
    (r'^department of home affairs', 'https://www.homeaffairs.gov.au/'), (r'^department of the treasury$', 'https://treasury.gov.au/'),
    (r'^federal court of australia', 'https://www.fedcourt.gov.au/'), (r'^ndis quality and safeguards', 'https://www.ndiscommission.gov.au/'),
    (r'^office of the australian accounting standards board', 'https://aasb.gov.au/'), (r'^royal australian mint', 'https://www.ramint.gov.au/'),
    (r'^services australia', 'https://www.servicesaustralia.gov.au/'), (r'^tourism australia', 'https://www.tourism.australia.com/'),
]

COMPANIES = [  # US/other company buyers (subcontract primes): regex on normalized name -> official domain
    (r'^boeing company|^bell boeing', 'https://www.boeing.com/'), (r'^lockheed martin|^sikorsky', 'https://www.lockheedmartin.com/'),
    (r'^alstom', 'https://www.alstom.com/'), (r'^general dynamics land systems', 'https://www.gdls.com/'),
    (r'^general dynamics mission systems', 'https://gdmissionsystems.com/'), (r'^general dynamics information technology', 'https://www.gdit.com/'),
    (r'^general dynamics ordnance|^general dynamics ots', 'https://www.gd-ots.com/'), (r'^northrop grumman', 'https://www.northropgrumman.com/'),
    (r'^honeywell', 'https://www.honeywell.com/'), (r'^bell textron', 'https://www.bellflight.com/'), (r'^ge renewables|^ge vernova', 'https://www.gevernova.com/'),
    (r'^general electric company|^ge aviation', 'https://www.geaerospace.com/'), (r'^huntington ingalls', 'https://www.hii.com/'),
    (r'^bae systems', 'https://www.baesystems.com/en-us/'), (r'^cgi federal', 'https://www.cgifederal.com/'), (r'^raytheon|^rtx', 'https://www.rtx.com/'),
    (r'^amentum', 'https://www.amentum.com/'), (r'^sierra nevada', 'https://www.sncorp.com/'), (r'^l3harris|^l3 technologies|^l 3 communications', 'https://www.l3harris.com/'),
    (r'^battelle memorial', 'https://www.battelle.org/'), (r'^vertex aerospace', 'https://www.vtxaero.com/'), (r'^triad national security', 'https://www.lanl.gov/'),
    (r'^oshkosh defense', 'https://oshkoshdefense.com/'), (r'^aar government', 'https://www.aarcorp.com/'), (r'^textron aviation', 'https://txtav.com/'),
    (r'^textron systems', 'https://www.textronsystems.com/'), (r'^dewberry', 'https://www.dewberry.com/'), (r'^m c dean', 'https://www.mcdean.com/'),
    (r'^leidos', 'https://www.leidos.com/'), (r'^cdm federal', 'https://www.cdmsmith.com/'), (r'^viasat', 'https://www.viasat.com/'),
    (r'^peraton', 'https://www.peraton.com/'), (r'^rockwell collins', 'https://www.collinsaerospace.com/'), (r'^rolls royce', 'https://www.rolls-royce.com/'),
    (r'^charles stark draper', 'https://www.draper.com/'), (r'^drs network', 'https://www.leonardodrs.com/'), (r'^massachusetts institute of technology', 'https://www.mit.edu/'),
    (r'^johns hopkins university applied physics', 'https://www.jhuapl.edu/'), (r'^booz allen', 'https://www.boozallen.com/'), (r'^caci', 'https://www.caci.com/'),
    (r'^parsons government', 'https://www.parsons.com/'), (r'^general atomics aeronautical', 'https://www.ga-asi.com/'), (r'^icf incorporated', 'https://www.icf.com/'),
    (r'^aecom', 'https://aecom.com/'), (r'^deloitte', 'https://www2.deloitte.com/us/'), (r'^northwestern university', 'https://www.northwestern.edu/'),
    (r'^general motors', 'https://www.gm.com/'), (r'^texas instruments', 'https://www.ti.com/'), (r'^teck metals', 'https://www.teck.com/'), (r'^sobeys', 'https://www.sobeys.com/'),
    (r'^glencore', 'https://www.glencore.com/'), (r'^siemens mobility', 'https://www.mobility.siemens.com/'),
]


def main():
    buyers = load_buyers()
    bulk = json.load(open(WORK + '/bulk.json'))
    gc = {o['name']: o for o in json.load(open(DL + '/gc/organization_list.json'))['result']}
    links = {norm(t): u for t, u in json.load(open(DL + '/gc/dept_links.json'))}
    MUN = list(csv.DictReader(open(DL + '/mamh/MUN.csv', encoding='utf-8-sig')))
    mun_by = collections.defaultdict(list)
    for m in MUN:
        mun_by[norm(m['munnom'])].append(m)
    st = collections.Counter()
    for b in buyers:
        k = b['buyer_key']
        r = bulk.get(k)
        if r and r.get('official_website'):
            continue
        name = b['name']
        segs = [s.strip() for s in re.split(r'\s+/\s+|\s+\\\s+', name) if s.strip()]
        first = segs[0]
        nn = norm(first)
        new = None
        if b['country'] == 'CA':
            if 'canada_federal' in {s['value'] for s in b['sources']} or b['types'] and 'federal' in b['types'][0]['value']:
                for rx, code in GC_ALIAS:
                    if re.search(rx, nn):
                        o = gc.get(code)
                        site = GC_SITE.get(code) or (links.get(norm(o['title_translated']['en'])) if o else '')
                        if re.search(r'coast guard|\bccg\b', nn):
                            site = GC_CCG_SITE
                        new = {'canonical_name': o['title_translated']['en'].strip() if o else code, 'official_website': site,
                               'organisation_type': 'Government of Canada organization', 'identifiers': {'owner_org': code},
                               'match_confidence': 'weak' if len(segs) > 1 else 'strong',
                               'match_basis': 'alias rule /%s/ on first entity "%s"%s' % (rx, first, ' (multi-entity name: %s)' % ' | '.join(segs) if len(segs) > 1 else '')}
                        if re.search(r'coast guard|\bccg\b', nn):
                            new['canonical_name'] = 'Canadian Coast Guard (Fisheries and Oceans Canada)'
                        break
            if not new:
                for rx, cn, site, typ in QC:
                    if site and re.search(rx, nn):
                        new = {'canonical_name': cn, 'official_website': site, 'organisation_type': typ, 'identifiers': {},
                               'match_confidence': 'strong', 'match_basis': 'alias rule /%s/' % rx}
                        break
            if not new:
                # municipal names with article kept (e.g. Ville de L'Assomption, La Tuque) or "Ville de X / Service"
                m = re.match(r'^(ville|municipalite|city|town|paroisse|canton)\s+(?:de |d )?(.*)$', nn)
                if m:
                    c = mun_by.get(m.group(2).strip(), [])
                    if len(c) == 1:
                        mm = c[0]
                        new = {'canonical_name': '%s de %s' % (mm['mdes'], mm['munnom']), 'official_website': ('https://' + mm['mweb']) if mm['mweb'] else '',
                               'organisation_type': 'Quebec local municipality (%s)' % mm['mdes'],
                               'identifiers': {'mamh_municipal_code': mm['mcode'], 'quebec_admin_region': mm['regadm']},
                               'address': {'line1': mm['madr1'], 'city': mm['madr2'], 'region': 'QC', 'postal_code': mm['mcodpos'], 'country': 'CA'},
                               'general_contact': {'emails': [mm['mcourriel']] if mm['mcourriel'] else [], 'phone': mm['mtel']},
                               'match_confidence': 'exact', 'match_basis': 'MAMH MUN.csv munnom == "%s" (first segment of "%s")' % (m.group(2), name),
                               'mamh': True}
        elif b['country'] == 'US':
            ac = b['identifiers'].get('awarding_agency_code', [])
            if ac and ac[0]['value'] in US_AG and US_AG[ac[0]['value']][1]:
                n2, site = US_AG[ac[0]['value']]
                new = {'canonical_name': n2, 'official_website': site, 'organisation_type': 'US federal department/agency',
                       'identifiers': {'awarding_agency_code': ac[0]['value'],
                                       'awarding_sub_agency_codes': [x['value'] for x in b['identifiers'].get('awarding_sub_agency_code', [])]},
                       'match_confidence': 'exact', 'match_basis': 'USAspending awarding_agency_code %s' % ac[0]['value']}
        if not new and b['types'] and 'company' in b['types'][0]['value']:
            for rx, site in COMPANIES:
                if re.search(rx, nn):
                    new = {'canonical_name': '', 'official_website': site, 'organisation_type': b['types'][0]['value'], 'identifiers': {},
                           'match_confidence': 'strong', 'match_basis': 'alias rule /%s/ (company name -> official domain)' % rx}
                    break
        if new:
            pass
        elif b['country'] == 'AU':
            for rx, site in AU_AG:
                if re.search(rx, nn):
                    new = {'canonical_name': name, 'official_website': site, 'organisation_type': 'Australian Government entity',
                           'identifiers': {}, 'match_confidence': 'strong', 'match_basis': 'alias rule /%s/ (AusTender agency name)' % rx}
                    break
        if not new:
            # official website published in the contract notice's own contact block (EU/UK/other notices)
            for c in b.get('contacts', []):
                v = c['value'] or {}
                w = (v.get('website') or v.get('url') or '') if isinstance(v, dict) else ''
                if w and not re.search(r'simap|publiccontractsscotland|marches-publics|eu-supply|ted\.europa|contractsfinder|find-tender|achatpublic|e-tenders|etenders|mercell|tenderned|bund\.de/|delta-esourcing|in-tendhost|bravosolution|jaggaer|proactis', w, re.I):
                    if not w.startswith('http'):
                        w = 'http://' + w
                    new = {'canonical_name': '', 'official_website': w.rstrip('/'), 'organisation_type': b['types'][0]['value'] if b['types'] else '',
                           'identifiers': {}, 'match_confidence': 'strong', 'match_basis': 'website field of the buyer contact block in the contract notice'}
                    break
        if not new:
            continue
        if r is None:
            r = bulk[k] = {'identifiers': {}, 'address': {}, 'general_contact': {'emails': [], 'phone': ''}, 'official_website': '',
                           'canonical_name': '', 'organisation_type': '', 'sources': [], 'notes': []}
        r['canonical_name'] = r['canonical_name'] or new['canonical_name']
        r['organisation_type'] = r['organisation_type'] or new['organisation_type']
        r['official_website'] = new['official_website']
        r['identifiers'].update(new['identifiers'])
        if new.get('address'):
            r['address'] = new['address']
        if new.get('general_contact'):
            r['general_contact'] = new['general_contact']
        r['sources'].append({'source': 'MAMH Répertoire des municipalités MUN.csv' if new.get('mamh') else 'alias rule (scripts/enrichment_buyers/alias.py); website = official domain, verified by crawler fetch',
                             'url': 'https://donneesouvertes.affmunqc.net/repertoire/MUN.csv' if new.get('mamh') else new['official_website'],
                             'retrieved_at': now(), 'match_basis': new['match_basis'], 'match_confidence': new['match_confidence']})
        st[b['country']] += 1
    json.dump(bulk, open(WORK + '/bulk.json', 'w'), ensure_ascii=False, indent=0)
    print(st)


main()
