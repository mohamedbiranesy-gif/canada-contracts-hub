#!/usr/bin/env python3
"""Normalize TED notices with Canadian winners into the shared record shape.

Inputs (all under downloads/ted_eu):
  api_eforms/*.json   full-field Search API JSON for eForms-era notices (winner-country=CAN etc.)
  api_legacy/*.json   full-field Search API JSON for legacy notices found via CSV (2016+ only)
  xml_eforms/*.xml, xml_legacy/*.xml   notice XML from the daily OJS packages
  csv_extract/*.canada.csv            open-data CSV award rows (WIN_COUNTRY_CODE contains CA)
  csv_extract/cn_rows_for_canada_cans.csv  matching contract-notice rows (DURATION, CONTRACT_START/COMPLETION)

Output: one JSON line per (notice, Canadian contractor award) to <out_jsonl>.
Usage: python3 -I normalize_ted.py <downloads_dir> <out_jsonl> <stats_json>
"""
import csv, datetime as dt, glob, json, os, re, sys
from collections import defaultdict
from lxml import etree

TODAY = dt.date(2026, 10, 25)
csv.field_size_limit(1 << 30)

NS = {
    'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
    'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
    'efac': 'http://data.europa.eu/p27/eforms-ubl-extension-aggregate-components/1',
    'efbc': 'http://data.europa.eu/p27/eforms-ubl-extension-basic-components/1',
    'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
    'efext': 'http://data.europa.eu/p27/eforms-ubl-extensions/1',
}

ISO3_TO_2 = {'CAN': 'CA'}
LEGAL_TYPE = {'cga': 'central government authority', 'ra': 'regional authority', 'la': 'local authority',
              'body-pl': 'body governed by public law', 'pub-undert': 'public undertaking', 'eu-ins-bod-ag': 'EU institution/body/agency',
              'int-org': 'international organisation', 'org-sub': 'organisation awarding a contract subsidised by a contracting authority',
              'def-cont': 'defence contractor', 'body-pl-cga': 'body governed by public law, controlled by a central government authority',
              'body-pl-ra': 'body governed by public law, controlled by a regional authority', 'body-pl-la': 'body governed by public law, controlled by a local authority',
              'grp-p-aut': 'group of public authorities', 'spec-rights-entity': 'entity with special or exclusive rights', 'rl-aut': 'regional or local authority'}
LEGACY_AA = {'1': 'ministry or any other national or federal authority', '3': 'regional or local authority', '4': 'utilities entity', '5': 'European institution/agency or international organisation',
             '6': 'body governed by public law', '8': 'other', 'N': 'national or federal agency/office', 'R': 'regional or local agency/office', 'Z': 'not specified'}


# ----------------------------------------------------------------------------- helpers
def iso_date(s):
    """'2024-01-15+01:00' / '2024-01-15Z' / '20240115' / '15-JAN-24' / '15/01/24' -> 'YYYY-MM-DD'"""
    if not s:
        return None
    s = str(s).strip()
    m = re.match(r'^(\d{4}-\d{2}-\d{2})', s)
    if m:
        return m.group(1)
    m = re.match(r'^(\d{4})(\d{2})(\d{2})$', s)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.match(r'^(\d{1,2})-([A-Z]{3})-(\d{2})$', s.upper())
    if m:
        try:
            return dt.datetime.strptime(s.upper(), '%d-%b-%y').date().isoformat()
        except ValueError:
            return None
    m = re.match(r'^(\d{2})/(\d{2})/(\d{2})$', s)
    if m:
        d, mo, y = m.groups()
        return f"20{y}-{mo}-{d}"
    return None


def to_date(s):
    s = iso_date(s)
    return dt.date.fromisoformat(s) if s else None


def add_months(d, months):
    y = d.year + (d.month - 1 + months) // 12
    m = (d.month - 1 + months) % 12 + 1
    day = min(d.day, [31, 29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return dt.date(y, m, day)


def add_duration(d, value, unit):
    unit = (unit or '').upper()
    v = float(value)
    if unit in ('MONTH', 'MON', 'MONTHS'):
        whole = int(v)
        res = add_months(d, whole)
        frac = v - whole
        if frac:
            res = res + dt.timedelta(days=round(frac * 30.4))
        return res
    if unit in ('YEAR', 'ANN', 'YEARS'):
        return add_months(d, int(round(v * 12)))
    if unit in ('DAY', 'DAYS'):
        return d + dt.timedelta(days=int(round(v)))
    if unit in ('WEEK', 'WEEKS'):
        return d + dt.timedelta(days=int(round(v * 7)))
    return None


def first_lang(v):
    """eForms i18n field {'eng': ['x']} or {'eng': 'x'} -> list of strings (prefer eng)"""
    if v is None:
        return []
    if isinstance(v, dict):
        langs = ['eng'] + [k for k in v if k != 'eng']
        out = []
        for k in langs:
            x = v.get(k)
            if isinstance(x, list):
                out.extend(x)
            elif x:
                out.append(x)
        return out
    if isinstance(v, list):
        return v
    return [v]


def lang_dict_pos(v, i):
    """return i-th element of a language-mapped list, in the original language."""
    if isinstance(v, dict):
        for k, x in v.items():
            if isinstance(x, list) and i < len(x):
                return x[i]
            if not isinstance(x, list) and i == 0:
                return x
        return None
    if isinstance(v, list):
        return v[i] if i < len(v) else None
    return v if i == 0 else None


def num(s):
    if s is None:
        return None
    try:
        return float(str(s).replace(' ', '').replace(',', ''))
    except ValueError:
        return None


def localname(e):
    return etree.QName(e).localname


def el_to_dict(e):
    """Generic XML -> dict (verbatim: tags, attributes, text). Lists for repeated children."""
    d = {}
    for k, v in e.attrib.items():
        d['@' + etree.QName(k).localname] = v
    text = (e.text or '').strip()
    children = list(e)
    if not children:
        if d:
            if text:
                d['#text'] = text
            return d
        return text
    for c in children:
        key = localname(c)
        val = el_to_dict(c)
        if key in d:
            if not isinstance(d[key], list) or (isinstance(d[key], list) and d.get('__list_' + key) is None):
                d[key] = [d[key]]
                d['__list_' + key] = True
            d[key].append(val)
        else:
            d[key] = val
    for k in [k for k in d if k.startswith('__list_')]:
        del d[k]
    if text:
        d['#text'] = text
    return d


# ----------------------------------------------------------------------------- eForms XML parsing
def parse_eforms_xml(path):
    root = etree.parse(path).getroot()
    ext = root.find('ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/efext:EformsExtension', NS)
    orgs = {}
    touchpoints = {}
    if ext is not None:
        for org in ext.findall('efac:Organizations/efac:Organization', NS):
            comp = org.find('efac:Company', NS)
            if comp is None:
                continue
            oid = comp.findtext('cac:PartyIdentification/cbc:ID', namespaces=NS)
            addr = comp.find('cac:PostalAddress', NS)
            o = {
                'id': oid,
                'name': comp.findtext('cac:PartyName/cbc:Name', namespaces=NS),
                'website': comp.findtext('cbc:WebsiteURI', namespaces=NS),
                'size': comp.findtext('efbc:CompanySizeCode', namespaces=NS),
                'legal_ids': [{'scheme': c.get('schemeName'), 'id': c.text} for c in comp.findall('cac:PartyLegalEntity/cbc:CompanyID', NS)],
                'address': {
                    'street': addr.findtext('cbc:StreetName', namespaces=NS) if addr is not None else None,
                    'additional_street': addr.findtext('cbc:AdditionalStreetName', namespaces=NS) if addr is not None else None,
                    'lines': [l.text for l in addr.findall('cac:AddressLine/cbc:Line', NS)] if addr is not None else [],
                    'city': addr.findtext('cbc:CityName', namespaces=NS) if addr is not None else None,
                    'postal_code': addr.findtext('cbc:PostalZone', namespaces=NS) if addr is not None else None,
                    'country_subentity': addr.findtext('cbc:CountrySubentity', namespaces=NS) if addr is not None else None,
                    'nuts': addr.findtext('cbc:CountrySubentityCode', namespaces=NS) if addr is not None else None,
                    'country': addr.findtext('cac:Country/cbc:IdentificationCode', namespaces=NS) if addr is not None else None,
                    'country_name': addr.findtext('cac:Country/cbc:Name', namespaces=NS) if addr is not None else None,
                },
                'contact': {
                    'name': comp.findtext('cac:Contact/cbc:Name', namespaces=NS),
                    'telephone': comp.findtext('cac:Contact/cbc:Telephone', namespaces=NS),
                    'fax': comp.findtext('cac:Contact/cbc:Telefax', namespaces=NS),
                    'email': comp.findtext('cac:Contact/cbc:ElectronicMail', namespaces=NS),
                },
                'roles': [],
            }
            orgs[oid] = o
            for tp in org.findall('efac:TouchPoint', NS):
                tid = tp.findtext('cac:PartyIdentification/cbc:ID', namespaces=NS)
                touchpoints[tid] = {'org': oid, 'name': tp.findtext('cac:PartyName/cbc:Name', namespaces=NS),
                                    'city': tp.findtext('cac:PostalAddress/cbc:CityName', namespaces=NS),
                                    'country': tp.findtext('cac:PostalAddress/cac:Country/cbc:IdentificationCode', namespaces=NS),
                                    'email': tp.findtext('cac:Contact/cbc:ElectronicMail', namespaces=NS)}
    # buyers
    buyer_ids = []
    for cp in root.findall('cac:ContractingParty', NS):
        bid = cp.findtext('cac:Party/cac:PartyIdentification/cbc:ID', namespaces=NS)
        buyer_ids.append({'org': bid, 'legal_type': cp.findtext('cac:ContractingPartyType/cbc:PartyTypeCode', namespaces=NS),
                          'activity': cp.findtext('cac:ContractingActivity/cbc:ActivityTypeCode', namespaces=NS),
                          'buyer_profile': cp.findtext('cbc:BuyerProfileURI', namespaces=NS)})
        if bid in orgs:
            orgs[bid]['roles'].append('buyer')
    # lots
    lots = {}
    for lot in root.findall('cac:ProcurementProjectLot', NS):
        lid = lot.findtext('cbc:ID', namespaces=NS)
        pp = lot.find('cac:ProcurementProject', NS)
        period = lot.find('cac:ProcurementProject/cac:PlannedPeriod', NS)
        dm = period.find('cbc:DurationMeasure', NS) if period is not None else None
        lots[lid] = {
            'id': lid,
            'scheme': lot.find('cbc:ID', NS).get('schemeName') if lot.find('cbc:ID', NS) is not None else None,
            'internal_id': pp.findtext('cbc:ID', namespaces=NS) if pp is not None else None,
            'title': pp.findtext('cbc:Name', namespaces=NS) if pp is not None else None,
            'description': pp.findtext('cbc:Description', namespaces=NS) if pp is not None else None,
            'contract_nature': pp.findtext('cbc:ProcurementTypeCode', namespaces=NS) if pp is not None else None,
            'cpv_main': pp.findtext('cac:MainCommodityClassification/cbc:ItemClassificationCode', namespaces=NS) if pp is not None else None,
            'cpv_additional': [c.text for c in pp.findall('cac:AdditionalCommodityClassification/cbc:ItemClassificationCode', NS)] if pp is not None else [],
            'place_of_performance_country': [c.text for c in pp.findall('cac:RealizedLocation/cac:Address/cac:Country/cbc:IdentificationCode', NS)] if pp is not None else [],
            'place_of_performance_nuts': [c.text for c in pp.findall('cac:RealizedLocation/cac:Address/cbc:CountrySubentityCode', NS)] if pp is not None else [],
            'period_start': period.findtext('cbc:StartDate', namespaces=NS) if period is not None else None,
            'period_end': period.findtext('cbc:EndDate', namespaces=NS) if period is not None else None,
            'duration_value': dm.text if dm is not None else None,
            'duration_unit': dm.get('unitCode') if dm is not None else None,
            'duration_description': period.findtext('cbc:DescriptionCode', namespaces=NS) if period is not None else None,
            'framework': lot.findtext('cac:TenderingProcess/cac:ContractingSystem/cbc:ContractingSystemTypeCode[@listName="framework-agreement"]', namespaces=NS),
            'estimated_value': lot.findtext('cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount', namespaces=NS),
        }
    res = {'orgs': orgs, 'touchpoints': touchpoints, 'buyers': buyer_ids, 'lots': lots, 'lot_results': [], 'tenders': {}, 'contracts': {}, 'tendering_parties': {}}
    nr = ext.find('efac:NoticeResult', NS) if ext is not None else None
    if nr is not None:
        ta = nr.find('cbc:TotalAmount', NS)
        res['total_amount'] = {'value': ta.text, 'currency': ta.get('currencyID')} if ta is not None else None
        for lr in nr.findall('efac:LotResult', NS):
            hv = lr.find('cbc:HigherTenderAmount', NS)
            lv = lr.find('cbc:LowerTenderAmount', NS)
            fw = lr.find('efac:FrameworkAgreementValues', NS)
            res['lot_results'].append({
                'id': lr.findtext('cbc:ID', namespaces=NS),
                'status': lr.findtext('cbc:TenderResultCode', namespaces=NS),
                'tenders': [t.text for t in lr.findall('efac:LotTender/cbc:ID', NS)],
                'contracts': [c.text for c in lr.findall('efac:SettledContract/cbc:ID', NS)],
                'lot': lr.findtext('efac:TenderLot/cbc:ID', namespaces=NS),
                'higher_tender_amount': {'value': hv.text, 'currency': hv.get('currencyID')} if hv is not None else None,
                'lower_tender_amount': {'value': lv.text, 'currency': lv.get('currencyID')} if lv is not None else None,
                'framework_values': el_to_dict(fw) if fw is not None else None,
                'received_submissions': [{'type': s.findtext('efbc:StatisticsCode', namespaces=NS), 'n': s.findtext('efbc:StatisticsNumeric', namespaces=NS)} for s in lr.findall('efac:ReceivedSubmissionsStatistics', NS)],
                'decision_reason': lr.findtext('efac:DecisionReason/efbc:DecisionReasonCode', namespaces=NS),
            })
        for t in nr.findall('efac:LotTender', NS):
            pa = t.find('cac:LegalMonetaryTotal/cbc:PayableAmount', NS)
            res['tenders'][t.findtext('cbc:ID', namespaces=NS)] = {
                'id': t.findtext('cbc:ID', namespaces=NS),
                'rank': t.findtext('cbc:RankCode', namespaces=NS),
                'ranked': t.findtext('cbc:TenderRankedIndicator', namespaces=NS),
                'variant': t.findtext('efbc:TenderVariantIndicator', namespaces=NS),
                'amount': {'value': pa.text, 'currency': pa.get('currencyID')} if pa is not None else None,
                'origin_country': [o.text for o in t.findall('efac:Origin/efbc:AreaCode', NS)],
                'subcontracting': t.findtext('efac:SubcontractingTerm/efbc:TermCode', namespaces=NS),
                'subcontracting_description': t.findtext('efac:SubcontractingTerm/efbc:TermDescription', namespaces=NS),
                'subcontracting_amount': el_to_dict(t.find('efac:SubcontractingTerm/efbc:TermAmount', NS)) if t.find('efac:SubcontractingTerm/efbc:TermAmount', NS) is not None else None,
                'tendering_party': t.findtext('efac:TenderingParty/cbc:ID', namespaces=NS),
                'lot': t.findtext('efac:TenderLot/cbc:ID', namespaces=NS),
                'reference': t.findtext('efac:TenderReference/cbc:ID', namespaces=NS),
            }
        for c in nr.findall('efac:SettledContract', NS):
            res['contracts'][c.findtext('cbc:ID', namespaces=NS)] = {
                'id': c.findtext('cbc:ID', namespaces=NS),
                'award_date': c.findtext('cbc:AwardDate', namespaces=NS),
                'issue_date': c.findtext('cbc:IssueDate', namespaces=NS),
                'title': c.findtext('cbc:Title', namespaces=NS),
                'framework': c.findtext('efbc:ContractFrameworkIndicator', namespaces=NS),
                'reference': [r.text for r in c.findall('efac:ContractReference/cbc:ID', NS)],
                'url': c.findtext('cbc:URI', namespaces=NS),
                'tenders': [t.text for t in c.findall('efac:LotTender/cbc:ID', NS)],
                'signatories': [s.text for s in c.findall('cac:SignatoryParty/cac:PartyIdentification/cbc:ID', NS)],
                'duration_justification': c.findtext('efbc:DurationJustificationReason', namespaces=NS),
            }
        for tp in nr.findall('efac:TenderingParty', NS):
            res['tendering_parties'][tp.findtext('cbc:ID', namespaces=NS)] = {
                'id': tp.findtext('cbc:ID', namespaces=NS),
                'name': tp.findtext('cbc:Name', namespaces=NS),
                'tenderers': [{'org': t.findtext('cbc:ID', namespaces=NS), 'group_lead': t.findtext('efbc:GroupLeadIndicator', namespaces=NS)} for t in tp.findall('efac:Tenderer', NS)],
                'subcontractors': [s.findtext('cbc:ID', namespaces=NS) for s in tp.findall('efac:SubContractor', NS)],
            }
    # modification notice information (can-modif)
    mods = []
    if ext is not None:
        for cm in ext.findall('efac:ContractModification', NS):
            mods.append(el_to_dict(cm))
    res['contract_modifications'] = mods
    # procedure-level
    pp = root.find('cac:ProcurementProject', NS)
    res['procedure'] = {
        'notice_id': root.findtext('cbc:ID', namespaces=NS),
        'contract_folder_id': root.findtext('cbc:ContractFolderID', namespaces=NS),
        'issue_date': root.findtext('cbc:IssueDate', namespaces=NS),
        'version': root.findtext('cbc:VersionID', namespaces=NS),
        'regulatory_domain': root.findtext('cbc:RegulatoryDomain', namespaces=NS),
        'notice_type': root.findtext('cbc:NoticeTypeCode', namespaces=NS),
        'language': root.findtext('cbc:NoticeLanguageCode', namespaces=NS),
        'procedure_type': root.findtext('cac:TenderingProcess/cbc:ProcedureCode', namespaces=NS),
        'previous_notices': [n.text for n in root.findall('cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID', NS)],
        'internal_id': pp.findtext('cbc:ID', namespaces=NS) if pp is not None else None,
        'title': pp.findtext('cbc:Name', namespaces=NS) if pp is not None else None,
        'description': pp.findtext('cbc:Description', namespaces=NS) if pp is not None else None,
        'contract_nature': pp.findtext('cbc:ProcurementTypeCode', namespaces=NS) if pp is not None else None,
        'cpv_main': pp.findtext('cac:MainCommodityClassification/cbc:ItemClassificationCode', namespaces=NS) if pp is not None else None,
    }
    return res


# ----------------------------------------------------------------------------- legacy XML parsing
def ptext(e):
    """join <P> paragraphs"""
    if e is None:
        return None
    ps = [''.join(p.itertext()).strip() for p in e.findall('{*}P')]
    if ps:
        return '\n'.join(ps)
    return ''.join(e.itertext()).strip() or None


def parse_legacy_xml(path):
    root = etree.parse(path).getroot()
    out = {'coded': {}, 'form': None, 'awards': [], 'contracting_body': None, 'object': None, 'procedure': None}
    cds = root.find('{*}CODED_DATA_SECTION')
    if cds is not None:
        out['coded'] = el_to_dict(cds)
    fs = root.find('{*}FORM_SECTION')
    if fs is None:
        return out
    orig = None
    for ch in fs:
        if ch.get('CATEGORY') == 'ORIGINAL':
            orig = ch
            break
    if orig is None:
        for ch in fs:
            if localname(ch) != 'NOTICE_UUID':
                orig = ch
                break
    if orig is None:
        return out
    out['form_name'] = localname(orig)
    out['form_attrs'] = dict(orig.attrib)
    out['form'] = el_to_dict(orig)
    fn = out['form_name']
    if fn.startswith('F0') or fn.startswith('F2') or fn.startswith('F1'):
        # R2.0.9 2014 forms (F03_2014, F06_2014, F21_2014, F15_2014...)
        cb = orig.find('{*}CONTRACTING_BODY/{*}ADDRESS_CONTRACTING_BODY')
        if cb is not None:
            out['contracting_body'] = {
                'name': cb.findtext('{*}OFFICIALNAME'), 'national_id': cb.findtext('{*}NATIONALID'), 'address': cb.findtext('{*}ADDRESS'),
                'town': cb.findtext('{*}TOWN'), 'postal_code': cb.findtext('{*}POSTAL_CODE'),
                'country': cb.find('{*}COUNTRY').get('VALUE') if cb.find('{*}COUNTRY') is not None else None,
                'contact_point': cb.findtext('{*}CONTACT_POINT'), 'phone': cb.findtext('{*}PHONE'), 'email': cb.findtext('{*}E_MAIL'), 'fax': cb.findtext('{*}FAX'),
                'nuts': cb.find('{*}NUTS').get('CODE') if cb.find('{*}NUTS') is not None else None,
                'url_general': cb.findtext('{*}URL_GENERAL'), 'url_buyer': cb.findtext('{*}URL_BUYER'),
            }
            cbp = orig.find('{*}CONTRACTING_BODY')
            ca_type = cbp.find('{*}CA_TYPE')
            out['contracting_body']['ca_type'] = ca_type.get('VALUE') if ca_type is not None else cbp.findtext('{*}CA_TYPE_OTHER')
            ca_act = cbp.find('{*}CA_ACTIVITY')
            out['contracting_body']['ca_activity'] = ca_act.get('VALUE') if ca_act is not None else cbp.findtext('{*}CA_ACTIVITY_OTHER')
            ce_act = cbp.find('{*}CE_ACTIVITY')
            if ce_act is not None:
                out['contracting_body']['ce_activity'] = ce_act.get('VALUE')
        oc = orig.find('{*}OBJECT_CONTRACT')
        lots = {}
        if oc is not None:
            vt = oc.find('{*}VAL_TOTAL')
            out['object'] = {
                'title': ptext(oc.find('{*}TITLE')), 'reference_number': oc.findtext('{*}REFERENCE_NUMBER'),
                'cpv_main': oc.find('{*}CPV_MAIN/{*}CPV_CODE').get('CODE') if oc.find('{*}CPV_MAIN/{*}CPV_CODE') is not None else None,
                'type_contract': oc.find('{*}TYPE_CONTRACT').get('CTYPE') if oc.find('{*}TYPE_CONTRACT') is not None else None,
                'short_descr': ptext(oc.find('{*}SHORT_DESCR')),
                'val_total': {'value': vt.text, 'currency': vt.get('CURRENCY')} if vt is not None else None,
            }
            for od in oc.findall('{*}OBJECT_DESCR'):
                lot_no = od.findtext('{*}LOT_NO')
                dur = od.find('{*}DURATION')
                lots[lot_no or '_'] = {
                    'item': od.get('ITEM'), 'lot_no': lot_no, 'title': ptext(od.find('{*}TITLE')), 'short_descr': ptext(od.find('{*}SHORT_DESCR')),
                    'cpv_additional': [c.get('CODE') for c in od.findall('{*}CPV_ADDITIONAL/{*}CPV_CODE')],
                    'nuts': [n.get('CODE') for n in od.findall('{*}NUTS')], 'main_site': ptext(od.find('{*}MAIN_SITE')),
                    'duration_value': dur.text if dur is not None else None, 'duration_unit': dur.get('TYPE') if dur is not None else None,
                    'date_start': od.findtext('{*}DATE_START'), 'date_end': od.findtext('{*}DATE_END'),
                    'options': od.find('{*}NO_OPTIONS') is None and od.find('{*}OPTIONS') is not None,
                    'options_descr': ptext(od.find('{*}OPTIONS_DESCR')),
                    'renewal': od.find('{*}RENEWAL') is not None, 'renewal_descr': ptext(od.find('{*}RENEWAL_DESCR')),
                    'eu_progr_related': ptext(od.find('{*}EU_PROGR_RELATED')), 'info_add': ptext(od.find('{*}INFO_ADD')),
                }
        out['lots'] = lots
        pr = orig.find('{*}PROCEDURE')
        if pr is not None:
            out['procedure'] = {'children': [localname(c) for c in pr], 'notice_number_oj': pr.findtext('{*}NOTICE_NUMBER_OJ'),
                                'framework': pr.find('{*}FRAMEWORK') is not None, 'dps': pr.find('{*}DPS') is not None}
        for ac in orig.findall('{*}AWARD_CONTRACT'):
            awd = ac.find('{*}AWARDED_CONTRACT')
            a = {'item': ac.get('ITEM'), 'contract_no': ac.findtext('{*}CONTRACT_NO'), 'lot_no': ac.findtext('{*}LOT_NO'), 'title': ptext(ac.find('{*}TITLE')),
                 'awarded': awd is not None, 'no_award_reason': None, 'contractors': []}
            if awd is None:
                na = ac.find('{*}NO_AWARDED_CONTRACT')
                a['no_award_reason'] = [localname(c) for c in na] if na is not None else None
                out['awards'].append(a)
                continue
            a['date_conclusion_contract'] = awd.findtext('{*}DATE_CONCLUSION_CONTRACT')
            t = awd.find('{*}TENDERS')
            if t is not None:
                a['tenders'] = {localname(c): c.text for c in t}
            else:  # R2.0.9.S01 layout (2016-2017): NB_TENDERS_* directly under AWARDED_CONTRACT
                a['tenders'] = {localname(c): c.text for c in awd if localname(c).startswith('NB_TENDERS')}
            a['awarded_to_group'] = awd.find('{*}CONTRACTORS/{*}AWARDED_TO_GROUP') is not None or awd.find('{*}AWARDED_TO_GROUP') is not None
            contractor_els = awd.findall('{*}CONTRACTORS/{*}CONTRACTOR') or awd.findall('{*}CONTRACTOR')
            for con in contractor_els:
                ad = con.find('{*}ADDRESS_CONTRACTOR')
                a['contractors'].append({
                    'name': ad.findtext('{*}OFFICIALNAME') if ad is not None else None,
                    'national_id': ad.findtext('{*}NATIONALID') if ad is not None else None,
                    'address': ad.findtext('{*}ADDRESS') if ad is not None else None, 'town': ad.findtext('{*}TOWN') if ad is not None else None,
                    'postal_code': ad.findtext('{*}POSTAL_CODE') if ad is not None else None,
                    'country': ad.find('{*}COUNTRY').get('VALUE') if ad is not None and ad.find('{*}COUNTRY') is not None else None,
                    'nuts': ad.find('{*}NUTS').get('CODE') if ad is not None and ad.find('{*}NUTS') is not None else None,
                    'phone': ad.findtext('{*}PHONE') if ad is not None else None, 'email': ad.findtext('{*}E_MAIL') if ad is not None else None,
                    'url': ad.findtext('{*}URL') if ad is not None else None,
                    'sme': con.find('{*}SME') is not None, 'no_sme': con.find('{*}NO_SME') is not None,
                })
            vals = awd.find('{*}VALUES')
            if vals is None and (awd.find('{*}VAL_TOTAL') is not None or awd.find('{*}VAL_ESTIMATED_TOTAL') is not None or awd.find('{*}VAL_RANGE_TOTAL') is not None):
                vals = awd  # R2.0.9.S01 layout: values directly under AWARDED_CONTRACT
            if vals is not None:
                vt = vals.find('{*}VAL_TOTAL')
                ve = vals.find('{*}VAL_ESTIMATED_TOTAL')
                a['values'] = {'val_total': {'value': vt.text, 'currency': vt.get('CURRENCY')} if vt is not None else None,
                               'val_estimated_total': {'value': ve.text, 'currency': ve.get('CURRENCY')} if ve is not None else None,
                               'val_range_total': el_to_dict(vals.find('{*}VAL_RANGE_TOTAL')) if vals.find('{*}VAL_RANGE_TOTAL') is not None else None}
            a['likely_subcontracted'] = awd.find('{*}LIKELY_SUBCONTRACTED') is not None
            vs = awd.find('{*}VAL_SUBCONTRACTING')
            a['val_subcontracting'] = {'value': vs.text, 'currency': vs.get('CURRENCY')} if vs is not None else None
            a['pct_subcontracting'] = awd.findtext('{*}PCT_SUBCONTRACTING')
            a['info_add_subcontracting'] = ptext(awd.find('{*}INFO_ADD_SUBCONTRACTING'))
            out['awards'].append(a)
        ci = orig.find('{*}COMPLEMENTARY_INFO')
        if ci is not None:
            out['complementary_info'] = {'date_dispatch_notice': ci.findtext('{*}DATE_DISPATCH_NOTICE'), 'info_add': ptext(ci.find('{*}INFO_ADD')),
                                         'recurrent_procurement': ci.find('{*}RECURRENT_PROCUREMENT') is not None}
    elif fn.startswith('CONTRACT_AWARD'):
        # R2.0.8 pre-2016 forms
        fd = orig[0] if len(orig) else None
        if fd is None:
            return out
        cb = fd.find('.//{*}NAME_ADDRESSES_CONTACT_CONTRACT_AWARD/{*}CA_CE_CONCESSIONAIRE_PROFILE')
        if cb is None:
            cb = fd.find('.//{*}CA_CE_CONCESSIONAIRE_PROFILE')
        if cb is not None:
            out['contracting_body'] = {
                'name': cb.findtext('{*}ORGANISATION/{*}OFFICIALNAME'), 'national_id': cb.findtext('{*}ORGANISATION/{*}NATIONALID'), 'address': cb.findtext('{*}ADDRESS'),
                'town': cb.findtext('{*}TOWN'), 'postal_code': cb.findtext('{*}POSTAL_CODE'),
                'country': cb.find('{*}COUNTRY').get('VALUE') if cb.find('{*}COUNTRY') is not None else None,
                'contact_point': cb.findtext('{*}CONTACT_POINT'), 'attention': cb.findtext('{*}ATTENTION'), 'phone': cb.findtext('{*}PHONE'),
                'email': cb.findtext('{*}E_MAILS/{*}E_MAIL') or cb.findtext('{*}E_MAIL'), 'fax': cb.findtext('{*}FAX'),
                'url_general': fd.findtext('.//{*}INTERNET_ADDRESSES_CONTRACT_AWARD/{*}URL_GENERAL'), 'url_buyer': fd.findtext('.//{*}INTERNET_ADDRESSES_CONTRACT_AWARD/{*}URL_BUYER'),
            }
            ta = fd.find('.//{*}TYPE_AND_ACTIVITIES')
            if ta is not None:
                tca = ta.find('{*}TYPE_OF_CONTRACTING_AUTHORITY')
                tcao = ta.find('{*}TYPE_OF_CONTRACTING_AUTHORITY_OTHER')
                out['contracting_body']['ca_type'] = tca.get('VALUE') if tca is not None else (tcao.get('VALUE') + ': ' + (tcao.text or '') if tcao is not None else None)
                out['contracting_body']['ca_activity'] = [a.get('VALUE') for a in ta.findall('{*}TYPE_OF_ACTIVITY')] or [a.text for a in ta.findall('{*}TYPE_OF_ACTIVITY_OTHER')]
        desc = fd.find('.//{*}DESCRIPTION_AWARD_NOTICE_INFORMATION')
        if desc is None:
            desc = fd.find('.//{*}DESCRIPTION_CONTRACT_AWARD_UTILITIES')
        if desc is None:
            desc = fd.find('.//{*}DESCRIPTION_AWARD_NOTICE_INFORMATION_DEFENCE')
        if desc is None:
            # fall back to any element whose name starts with DESCRIPTION_ under the object section
            for c in fd.iter():
                if localname(c).startswith('DESCRIPTION_') and c.find('{*}TITLE_CONTRACT') is not None:
                    desc = c
                    break
        tfv = fd.find('.//{*}TOTAL_FINAL_VALUE//{*}VALUE_COST')
        tfvc = fd.find('.//{*}TOTAL_FINAL_VALUE/{*}COSTS_RANGE_AND_CURRENCY_WITH_VAT_RATE')
        out['object'] = {
            'title': ptext(desc.find('{*}TITLE_CONTRACT')) if desc is not None else None,
            'type_contract': desc.find('.//{*}TYPE_CONTRACT').get('VALUE') if desc is not None and desc.find('.//{*}TYPE_CONTRACT') is not None else None,
            'short_descr': ptext(desc.find('{*}SHORT_CONTRACT_DESCRIPTION')) if desc is not None else None,
            'cpv_main': desc.find('.//{*}CPV_MAIN/{*}CPV_CODE').get('CODE') if desc is not None and desc.find('.//{*}CPV_MAIN/{*}CPV_CODE') is not None else None,
            'cpv_additional': [c.get('CODE') for c in desc.findall('.//{*}CPV_ADDITIONAL/{*}CPV_CODE')] if desc is not None else [],
            'location': ptext(desc.find('.//{*}LOCATION_NUTS/{*}LOCATION')) if desc is not None else None,
            'nuts': [n.get('CODE') for n in desc.findall('.//{*}LOCATION_NUTS/{*}NUTS')] if desc is not None else [],
            'framework': desc.find('.//{*}CONCLUSION_FRAMEWORK_AGREEMENT') is not None if desc is not None else None,
            'val_total': {'value': tfv.get('FMTVAL') or tfv.text, 'currency': tfvc.get('CURRENCY') if tfvc is not None else None} if tfv is not None else None,
            'reference_number': ptext(fd.find('.//{*}FILE_REFERENCE_NUMBER')),
        }
        out['lots'] = {}
        award_els = fd.findall('{*}AWARD_OF_CONTRACT') + fd.findall('{*}AWARD_OF_CONTRACT_DEFENCE') + fd.findall('{*}AWARD_AND_CONTRACT_VALUE')
        if not award_els:
            # utilities form (F06 R2.0.8): AWARD_CONTRACT_CONTRACT_AWARD_UTILITIES/AWARD_AND_CONTRACT_VALUE
            for e in fd.iter():
                if localname(e) in ('AWARD_AND_CONTRACT_VALUE', 'AWARD_OF_CONTRACT', 'AWARD_OF_CONTRACT_DEFENCE'):
                    award_els.append(e)
        for ac in award_els:
            d = ac.find('{*}CONTRACT_AWARD_DATE')
            if d is None:
                d = ac.find('{*}DATE_OF_CONTRACT_AWARD')
            date = None
            if d is not None and d.findtext('{*}YEAR'):
                date = f"{d.findtext('{*}YEAR')}-{d.findtext('{*}MONTH').zfill(2)}-{d.findtext('{*}DAY').zfill(2)}"
            eo = ac.find('{*}ECONOMIC_OPERATOR_NAME_ADDRESS')
            cd = eo.find('{*}CONTACT_DATA_WITHOUT_RESPONSIBLE_NAME') if eo is not None else None
            if cd is None and eo is not None:
                cd = eo[0] if len(eo) else None
            if cd is None:
                for tag in ('CONTACT_DATA_WITHOUT_RESPONSIBLE_NAME_CHP', 'CONTACT_DATA_WITHOUT_RESPONSIBLE_NAME', 'ECONOMIC_OPERATOR_NAME_ADDRESS'):
                    cd = ac.find('{*}' + tag)
                    if cd is not None:
                        break
            cv = ac.find('{*}CONTRACT_VALUE_INFORMATION')
            def costs(tag):
                c = cv.find('{*}' + tag) if cv is not None else None
                if c is None:
                    return None
                vc = c.find('{*}VALUE_COST')
                rng = c.find('{*}RANGE_VALUE_COST')
                return {'currency': c.get('CURRENCY'), 'value': (vc.get('FMTVAL') or vc.text) if vc is not None else None,
                        'low': rng.find('{*}LOW_VALUE').get('FMTVAL') if rng is not None and rng.find('{*}LOW_VALUE') is not None else None,
                        'high': rng.find('{*}HIGH_VALUE').get('FMTVAL') if rng is not None and rng.find('{*}HIGH_VALUE') is not None else None}
            a = {'item': ac.get('ITEM'), 'contract_no': ptext(ac.find('{*}CONTRACT_NUMBER')) or ac.findtext('{*}CONTRACT_NUMBER'), 'lot_no': ptext(ac.find('{*}LOT_NUMBER')) or ac.findtext('{*}LOT_NUMBER'),
                 'title': ptext(ac.find('{*}CONTRACT_TITLE')) or ptext(ac.find('{*}TITLE_CONTRACT')), 'awarded': True, 'date_conclusion_contract': date,
                 'tenders': {'NB_TENDERS_RECEIVED': ac.findtext('{*}OFFERS_RECEIVED_NUMBER'), 'NB_TENDERS_RECEIVED_EMEANS': ac.findtext('{*}OFFERS_RECEIVED_NUMBER_MEANING')},
                 'contractors': [], 'values': {'initial_estimated': costs('INITIAL_ESTIMATED_TOTAL_VALUE_CONTRACT'), 'val_total': costs('COSTS_RANGE_AND_CURRENCY_WITH_VAT_RATE')},
                 'likely_subcontracted': ac.find('{*}MORE_INFORMATION_TO_SUB_CONTRACTED/{*}CONTRACT_LIKELY_SUB_CONTRACTED') is not None}
            if cd is not None:
                a['contractors'].append({
                    'name': cd.findtext('{*}ORGANISATION/{*}OFFICIALNAME'), 'national_id': cd.findtext('{*}ORGANISATION/{*}NATIONALID'),
                    'address': cd.findtext('{*}ADDRESS'), 'town': cd.findtext('{*}TOWN'), 'postal_code': cd.findtext('{*}POSTAL_CODE'),
                    'country': cd.find('{*}COUNTRY').get('VALUE') if cd.find('{*}COUNTRY') is not None else None,
                    'phone': cd.findtext('{*}PHONE'), 'email': cd.findtext('{*}E_MAILS/{*}E_MAIL') or cd.findtext('{*}E_MAIL'), 'url': cd.findtext('{*}URL'), 'fax': cd.findtext('{*}FAX'),
                })
            out['awards'].append(a)
        nd = fd.find('.//{*}NOTICE_DISPATCH_DATE')
        if nd is not None and nd.findtext('{*}YEAR'):
            out['complementary_info'] = {'date_dispatch_notice': f"{nd.findtext('{*}YEAR')}-{nd.findtext('{*}MONTH').zfill(2)}-{nd.findtext('{*}DAY').zfill(2)}",
                                         'info_add': ptext(fd.find('.//{*}COMPLEMENTARY_INFORMATION_CONTRACT_AWARD/{*}ADDITIONAL_INFORMATION'))}
    return out


# ----------------------------------------------------------------------------- status
def compute_status(start, signed, end, dur_value, dur_unit, basis_prefix):
    """returns (status, status_basis, computed_end)"""
    base = start or signed
    if end:
        if end >= TODAY and (base is None or base <= TODAY):
            return 'ongoing', f"{basis_prefix}: explicit end date {end.isoformat()} >= 2026-10-25 and start/award {base.isoformat() if base else 'n/a'} <= today.", end
        if end < TODAY:
            return 'ended', f"{basis_prefix}: explicit end date {end.isoformat()} < 2026-10-25.", end
        return 'not_started', f"{basis_prefix}: start {base.isoformat()} is after today.", end
    if dur_value and base:
        ce = add_duration(base, dur_value, dur_unit)
        if ce:
            if ce >= TODAY and base <= TODAY:
                return 'ongoing_inferred', f"{basis_prefix}: no explicit end date; computed end = {'start' if start else 'award/conclusion'} date {base.isoformat()} + duration {dur_value} {dur_unit} = {ce.isoformat()} >= 2026-10-25.", ce
            if ce < TODAY:
                return 'ended_inferred', f"{basis_prefix}: computed end = {base.isoformat()} + {dur_value} {dur_unit} = {ce.isoformat()} < 2026-10-25.", ce
            return 'not_started', f"{basis_prefix}: start {base.isoformat()} after today.", ce
    return 'end_date_unknown', f"{basis_prefix}: no end date and no usable duration in the notice.", None


# ----------------------------------------------------------------------------- main build
def load_csv_rows(dl):
    by_pub = defaultdict(list)
    for f in sorted(glob.glob(os.path.join(dl, 'csv_extract', '*.canada.csv'))):
        with open(f, encoding='utf-8', newline='') as fh:
            for row in csv.DictReader(fh):
                m = re.search(r'NOTICE:(\d+-\d{4})', row.get('TED_NOTICE_URL', ''))
                if m:
                    row['_source_csv'] = os.path.basename(f)
                    by_pub[m.group(1)].append(row)
    cn_by_can = defaultdict(list)
    p = os.path.join(dl, 'csv_extract', 'cn_rows_for_canada_cans.csv')
    if os.path.exists(p):
        with open(p, encoding='utf-8', newline='') as fh:
            for row in csv.DictReader(fh):
                cn_by_can[row['FUTURE_CAN_ID'].strip()].append(row)
    return by_pub, cn_by_can


def main():
    dl, out_path, stats_path = sys.argv[1:4]
    retrieved_default = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    csv_by_pub, cn_by_can = load_csv_rows(dl)
    api = {}
    for d in ('api_eforms', 'api_legacy'):
        for f in glob.glob(os.path.join(dl, d, '*.json')):
            if os.path.basename(f).startswith('_'):
                continue
            n = json.load(open(f, encoding='utf-8'))
            n['_api_dir'] = d
            api[n['publication-number']] = n
    xml_paths = {}
    for d in ('xml_eforms', 'xml_legacy'):
        for f in glob.glob(os.path.join(dl, d, '*.xml')):
            xml_paths[os.path.basename(f)[:-4]] = f
    pubnos = sorted(set(api) | set(csv_by_pub) | set(xml_paths), key=lambda s: (int(s.split('-')[1]), int(s.split('-')[0])))
    stats = defaultdict(int)
    excluded = []
    n_out = 0
    with open(out_path, 'w', encoding='utf-8') as out:
        for pn in pubnos:
            try:
                recs, excl = build_records(pn, api.get(pn), xml_paths.get(pn), csv_by_pub.get(pn, []), cn_by_can, retrieved_default)
            except Exception as e:  # keep going
                stats['errors'] += 1
                excluded.append({'publication_number': pn, 'reason': f'error: {e!r}'})
                print('ERROR', pn, repr(e), file=sys.stderr)
                continue
            excluded += excl
            for r in recs:
                out.write(json.dumps(r, ensure_ascii=False) + '\n')
                stats[r['status']] += 1
                n_out += 1
            stats['notices_seen'] += 1
    stats['records_written'] = n_out
    stats['excluded'] = len(excluded)
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump({'stats': dict(stats), 'excluded': excluded}, f, ensure_ascii=False, indent=1)
    print(json.dumps(dict(stats), indent=1))


def build_records(pn, api_n, xml_path, csv_rows, cn_by_can, retrieved_default):
    """Return (records, excluded) for one notice."""
    recs, excl = [], []
    retrieved_at = (api_n or {}).get('_retrieved_at') or retrieved_default
    record_url = f"https://ted.europa.eu/en/notice/-/detail/{pn}"
    is_eforms = bool(api_n and api_n.get('customization-id')) or (xml_path and 'xml_eforms' in xml_path)
    xml = None
    xml_kind = None
    if xml_path:
        try:
            root_tag = localname(etree.parse(xml_path).getroot())
        except Exception as e:
            root_tag = None
            print('xml parse error', pn, e, file=sys.stderr)
        if root_tag == 'TED_EXPORT':
            xml = parse_legacy_xml(xml_path)
            xml_kind = 'legacy'
        elif root_tag:
            xml = parse_eforms_xml(xml_path)
            xml_kind = 'eforms'
    notice_type = (api_n or {}).get('notice-type') or (csv_rows[0]['ID_TYPE'] if csv_rows else None)
    cn_rows = []
    for r in csv_rows:
        cn_rows += cn_by_can.get(r['ID_NOTICE_CAN'].strip(), [])
    # de-dup cn rows
    seen = set()
    cn_rows_u = []
    for r in cn_rows:
        k = json.dumps(r, sort_keys=True)
        if k not in seen:
            seen.add(k)
            cn_rows_u.append(r)
    cn_rows = cn_rows_u

    base_raw = {
        'publication_number': pn,
        'search_api_notice': api_n,
        'notice_xml': xml,
        'notice_xml_schema': xml_kind,
        'opendata_csv_award_rows': csv_rows,
        'opendata_csv_contract_notice_rows': cn_rows,
    }

    if xml_kind == 'eforms' or (is_eforms and api_n):
        recs, excl = build_eforms(pn, api_n, xml, base_raw, record_url, retrieved_at, notice_type)
    else:
        recs, excl = build_legacy(pn, api_n, xml, csv_rows, cn_rows, base_raw, record_url, retrieved_at, notice_type)
    return recs, excl


def src(record_url, retrieved_at):
    return {
        'key': 'ted_eu',
        'name': 'TED - Tenders Electronic Daily (Supplement to the Official Journal of the EU)',
        'publisher': 'Publications Office of the European Union',
        'dataset_url': 'https://ted.europa.eu/en/ (Search API https://api.ted.europa.eu/v3/notices/search; XML packages https://ted.europa.eu/packages/daily/<yyyy><nnnnn>; CSV https://data.europa.eu/data/datasets/ted-csv)',
        'record_url': record_url,
        'retrieved_at': retrieved_at,
    }


def build_eforms(pn, api_n, xml, base_raw, record_url, retrieved_at, notice_type):
    recs, excl = [], []
    if xml is None:
        # fall back to API arrays (winner-* arrays are aligned)
        return build_eforms_from_api(pn, api_n, base_raw, record_url, retrieved_at, notice_type)
    orgs = xml['orgs']
    buyer_org = orgs.get(xml['buyers'][0]['org']) if xml['buyers'] else None
    buyer_meta = xml['buyers'][0] if xml['buyers'] else {}
    pub_date = iso_date((api_n or {}).get('publication-date'))
    proc = xml['procedure']
    # Collect contracts with Canadian tenderer
    lot_by_tender = {}
    lotres_by_tender = {}
    for lr in xml['lot_results']:
        for t in lr['tenders']:
            lotres_by_tender[t] = lr
    contracts_by_tender = defaultdict(list)
    for c in xml['contracts'].values():
        for t in c['tenders']:
            contracts_by_tender[t].append(c)
    for tid, tender in xml['tenders'].items():
        tp = xml['tendering_parties'].get(tender['tendering_party']) or {}
        ca_orgs = [orgs[t['org']] for t in tp.get('tenderers', []) if t['org'] in orgs and (orgs[t['org']]['address']['country'] or '').upper() == 'CAN']
        if not ca_orgs:
            # subcontractor-only matches are not awards to a Canadian supplier
            continue
        lr = lotres_by_tender.get(tid) or {}
        lot = xml['lots'].get(lr.get('lot') or tender.get('lot')) or {}
        contracts = contracts_by_tender.get(tid, [])
        con = contracts[0] if contracts else {}
        if lr.get('status') and lr['status'] not in ('selec-w', 'open-nw'):
            excl.append({'publication_number': pn, 'tender': tid, 'reason': f"lot result status {lr['status']} (not a winner)"})
            continue
        award_date = to_date(con.get('award_date')) or to_date(con.get('issue_date')) or to_date(proc.get('issue_date'))
        start = to_date(lot.get('period_start'))
        end = to_date(lot.get('period_end'))
        status, basis, computed_end = compute_status(start, award_date, end, lot.get('duration_value'), lot.get('duration_unit'),
                                                     'eForms XML: lot PlannedPeriod (BT-536 start / BT-537 end / BT-36 duration), SettledContract AwardDate (BT-145)')
        if notice_type == 'can-modif':
            basis += ' Notice is a contract modification notice (can-modif); dates refer to the modified contract as republished.'
        if status in ('ended', 'ended_inferred', 'not_started'):
            excl.append({'publication_number': pn, 'tender': tid, 'reason': basis})
            continue
        v = tender.get('amount') or {}
        ca_org = ca_orgs[0]
        group = len(tp.get('tenderers', [])) > 1
        rec = {
            'record_id': f"ted_eu:{pn}:{tid}",
            'source': src(record_url, retrieved_at),
            'status': status,
            'status_basis': basis,
            'contract': {
                'identifiers': {
                    'publication_number': pn,
                    'ojs_issue': (api_n or {}).get('ojs-number'),
                    'notice_id_uuid': proc.get('notice_id'),
                    'procedure_id': proc.get('contract_folder_id') or (api_n or {}).get('procedure-identifier'),
                    'procedure_internal_id': proc.get('internal_id'),
                    'lot_id': lot.get('id'),
                    'lot_internal_id': lot.get('internal_id'),
                    'lot_result_id': lr.get('id'),
                    'tender_id': tid,
                    'tender_reference': tender.get('reference'),
                    'contract_id': con.get('id'),
                    'contract_reference': con.get('reference'),
                    'previous_notice_ids': proc.get('previous_notices'),
                    'buyer_contract_reference_api': (api_n or {}).get('contract-identifier'),
                },
                'title': con.get('title') or lot.get('title') or proc.get('title'),
                'description': lot.get('description') or proc.get('description'),
                'instrument_type': 'framework agreement' if (str(con.get('framework')).lower() == 'true' or (lot.get('framework') and lot.get('framework') != 'none')) else 'contract',
                'procurement_method': proc.get('procedure_type'),
                'solicitation_procedure': (api_n or {}).get('procedure-type'),
                'commodity': {'cpv': lot.get('cpv_main') or proc.get('cpv_main'), 'cpv_additional': lot.get('cpv_additional'), 'contract_nature': lot.get('contract_nature') or proc.get('contract_nature')},
                'value': num(v.get('value')),
                'currency': v.get('currency'),
                'value_detail': {
                    'tender_payable_amount': num(v.get('value')),
                    'notice_total_amount': num((xml.get('total_amount') or {}).get('value')),
                    'notice_total_currency': (xml.get('total_amount') or {}).get('currency'),
                    'lot_estimated_value': num(lot.get('estimated_value')),
                    'lot_result_framework_values': lr.get('framework_values'),
                },
                'dates': {
                    'published': pub_date,
                    'signed': iso_date(con.get('award_date')),
                    'start': iso_date(lot.get('period_start')),
                    'end': iso_date(lot.get('period_end')),
                    'end_computed': computed_end.isoformat() if computed_end and not end else None,
                    'duration': {'value': lot.get('duration_value'), 'unit': lot.get('duration_unit')} if lot.get('duration_value') else None,
                    'notice_issue_date': iso_date(proc.get('issue_date')),
                    'winner_decision_date': None,
                    'amended_last': None,
                },
                'related': {
                    'award_notice_url': record_url,
                    'notice_xml_url': f"https://ted.europa.eu/en/notice/{pn}/xml",
                    'notice_pdf_url': f"https://ted.europa.eu/en/notice/{pn}/pdf",
                    'previous_notices': [f"https://ted.europa.eu/en/notice/-/detail/{x}" for x in (proc.get('previous_notices') or []) if re.match(r'^\d+-\d{4}$', x)],
                    'contract_url': con.get('url'),
                    'buyer_profile_url': buyer_meta.get('buyer_profile'),
                },
            },
            'buyer': {
                'name': (buyer_org or {}).get('name'),
                'country': country2((buyer_org or {}).get('address', {}).get('country')),
                'type': LEGAL_TYPE.get(buyer_meta.get('legal_type'), buyer_meta.get('legal_type')),
                'identifiers': {'organization_id_in_notice': (buyer_org or {}).get('id'), 'legal_ids': (buyer_org or {}).get('legal_ids'), 'buyer_identifier_api': (api_n or {}).get('buyer-identifier')},
                'address': (buyer_org or {}).get('address'),
                'contact': {**((buyer_org or {}).get('contact') or {}), 'website': (buyer_org or {}).get('website')},
                'main_activity': buyer_meta.get('activity'),
                'all_buyers': [orgs.get(b['org'], {}).get('name') for b in xml['buyers']],
            },
            'vendor': {
                'name': ca_org['name'],
                'country': 'CA',
                'country_basis': 'eForms XML efac:Organizations/efac:Organization/efac:Company/cac:PostalAddress/cac:Country/cbc:IdentificationCode = CAN for the tenderer organization referenced by the winning tender (BT-514-Organization-Company); API field winner-country / organisation-country-tenderer',
                'identifiers': {'organization_id_in_notice': ca_org['id'], 'legal_ids': ca_org['legal_ids']},
                'address': {'line1': (ca_org['address']['street'] or '; '.join(ca_org['address']['lines'] or [])) or None, 'line2': ca_org['address']['additional_street'],
                            'city': ca_org['address']['city'], 'region': ca_org['address']['country_subentity'], 'postal_code': ca_org['address']['postal_code'], 'country': ca_org['address']['country']},
                'contact': {**ca_org['contact'], 'website': ca_org['website']},
                'company_size': ca_org['size'],
                'awarded_to_group': group,
                'group_members': [{'name': orgs[t['org']]['name'], 'country': orgs[t['org']]['address']['country'], 'group_lead': t.get('group_lead')} for t in tp.get('tenderers', []) if t['org'] in orgs] if group else None,
                'tendering_party_id': tender.get('tendering_party'),
            },
            'raw': {**base_raw, 'matched_tender': tender, 'matched_lot_result': lr, 'matched_lot': lot, 'matched_contracts': contracts, 'matched_tendering_party': tp},
        }
        recs.append(rec)
    if not recs and not excl:
        # eForms XML without a Canadian tenderer in a winning tender (e.g. subcontractor only, or veat/pre-award)
        reason = 'no winning tender with a Canadian tenderer organization in the XML'
        if notice_type == 'veat':
            reason = 'voluntary ex-ante transparency notice (veat): intended award, not a concluded contract; ' + reason
        excl.append({'publication_number': pn, 'reason': reason})
    return recs, excl


def build_eforms_from_api(pn, api_n, base_raw, record_url, retrieved_at, notice_type):
    """eForms notice without XML: use aligned winner-* arrays from the API."""
    recs, excl = [], []
    countries = api_n.get('winner-country') or api_n.get('organisation-country-tenderer') or []
    names = api_n.get('winner-name') or api_n.get('organisation-name-tenderer')
    starts = api_n.get('contract-duration-start-date-lot') or []
    ends = api_n.get('contract-duration-end-date-lot') or []
    periods = api_n.get('contract-duration-period-lot') or []
    concl = api_n.get('contract-conclusion-date') or []
    pub_date = iso_date(api_n.get('publication-date'))
    for i, c in enumerate(countries):
        if c != 'CAN':
            continue
        start = to_date(starts[0]) if len(starts) == 1 else None
        end = to_date(ends[0]) if len(ends) == 1 else None
        per = periods[0] if len(periods) == 1 else {}
        signed = to_date(concl[i]) if i < len(concl) else (to_date(concl[0]) if len(concl) == 1 else None)
        status, basis, computed_end = compute_status(start, signed, end, per.get('value'), per.get('unit'), 'Search API fields contract-duration-start-date-lot / contract-duration-end-date-lot / contract-duration-period-lot / contract-conclusion-date (single-lot notice)')
        if status in ('ended', 'ended_inferred', 'not_started'):
            excl.append({'publication_number': pn, 'winner_index': i, 'reason': basis})
            continue
        recs.append({
            'record_id': f"ted_eu:{pn}:winner{i}",
            'source': src(record_url, retrieved_at),
            'status': status, 'status_basis': basis,
            'contract': {
                'identifiers': {'publication_number': pn, 'ojs_issue': api_n.get('ojs-number'), 'notice_id_uuid': api_n.get('notice-identifier'), 'procedure_id': api_n.get('procedure-identifier'),
                                'contract_identifier': api_n.get('contract-identifier'), 'lot_ids': api_n.get('identifier-lot')},
                'title': (first_lang(api_n.get('contract-title')) or first_lang(api_n.get('title-proc')) or [None])[0],
                'description': (first_lang(api_n.get('description-proc')) or [None])[0],
                'instrument_type': 'framework agreement' if any(api_n.get('contract-framework-agreement') or []) else 'contract',
                'procurement_method': api_n.get('procedure-type'), 'solicitation_procedure': api_n.get('procedure-type'),
                'commodity': {'cpv': (api_n.get('main-classification-proc') or [None])[0], 'cpv_all': api_n.get('classification-cpv'), 'contract_nature': api_n.get('contract-nature-main-proc')},
                'value': num((api_n.get('tender-value') or [None]*(i+1))[i] if i < len(api_n.get('tender-value') or []) else None),
                'currency': (api_n.get('tender-value-cur') or [None]*(i+1))[i] if i < len(api_n.get('tender-value-cur') or []) else None,
                'value_detail': {'notice_total_value': api_n.get('total-value'), 'notice_total_currency': api_n.get('total-value-cur')},
                'dates': {'published': pub_date, 'signed': signed.isoformat() if signed else None, 'start': start.isoformat() if start else None, 'end': end.isoformat() if end else None,
                          'end_computed': computed_end.isoformat() if computed_end and not end else None, 'duration': per or None, 'amended_last': None},
                'related': {'award_notice_url': record_url, 'notice_xml_url': f"https://ted.europa.eu/en/notice/{pn}/xml"},
            },
            'buyer': {'name': (first_lang(api_n.get('buyer-name')) or [None])[0], 'country': country2((api_n.get('buyer-country') or [None])[0]),
                      'type': LEGAL_TYPE.get((api_n.get('buyer-legal-type') or [None])[0], (api_n.get('buyer-legal-type') or [None])[0]),
                      'identifiers': {'buyer_identifier': api_n.get('buyer-identifier')},
                      'address': {'city': (first_lang(api_n.get('buyer-city')) or [None])[0], 'postal_code': (api_n.get('buyer-post-code') or [None])[0], 'street': (api_n.get('organisation-street-buyer') or [None])[0], 'country': (api_n.get('buyer-country') or [None])[0]},
                      'contact': {'email': (api_n.get('buyer-email') or [None])[0], 'phone': (api_n.get('organisation-tel-buyer') or [None])[0], 'website': (api_n.get('buyer-internet-address') or [None])[0]}},
            'vendor': {'name': lang_dict_pos(names, i), 'country': 'CA', 'country_basis': 'Search API winner-country[i] = CAN (aligned winner-* arrays; no XML available)',
                       'identifiers': {'winner_identifier': (api_n.get('winner-identifier') or [None]*(i+1))[i] if i < len(api_n.get('winner-identifier') or []) else None},
                       'address': {'city': (api_n.get('winner-city') or [None]*(i+1))[i] if i < len(api_n.get('winner-city') or []) else None, 'postal_code': (api_n.get('winner-post-code') or [None]*(i+1))[i] if i < len(api_n.get('winner-post-code') or []) else None, 'country': 'CAN'},
                       'contact': {'email': (api_n.get('winner-email') or [None]*(i+1))[i] if i < len(api_n.get('winner-email') or []) else None}},
            'raw': base_raw,
        })
    return recs, excl


def country2(c):
    if not c:
        return None
    c = c.upper()
    if len(c) == 2:
        return 'GB' if c == 'UK' else c
    m = {'AUT': 'AT', 'BEL': 'BE', 'BGR': 'BG', 'HRV': 'HR', 'CYP': 'CY', 'CZE': 'CZ', 'DNK': 'DK', 'EST': 'EE', 'FIN': 'FI', 'FRA': 'FR', 'DEU': 'DE', 'GRC': 'GR', 'HUN': 'HU', 'IRL': 'IE', 'ITA': 'IT', 'LVA': 'LV', 'LTU': 'LT', 'LUX': 'LU', 'MLT': 'MT', 'NLD': 'NL', 'POL': 'PL', 'PRT': 'PT', 'ROU': 'RO', 'SVK': 'SK', 'SVN': 'SI', 'ESP': 'ES', 'SWE': 'SE', 'GBR': 'GB', 'NOR': 'NO', 'ISL': 'IS', 'LIE': 'LI', 'CHE': 'CH', 'CAN': 'CA', 'USA': 'US', 'MKD': 'MK', 'SRB': 'RS', 'TUR': 'TR', 'UKR': 'UA', 'MDA': 'MD', 'GEO': 'GE', 'ALB': 'AL', 'BIH': 'BA', 'MNE': 'ME', 'XKX': 'XK', 'ARM': 'AM', 'AUS': 'AU', 'JPN': 'JP', 'KOR': 'KR', 'CHN': 'CN', 'IND': 'IN', 'BRA': 'BR', 'MEX': 'MX', 'ISR': 'IL', 'ZAF': 'ZA', 'NZL': 'NZ', 'SGP': 'SG', 'ARE': 'AE', 'SAU': 'SA', 'EGY': 'EG', 'MAR': 'MA', 'TUN': 'TN', 'NGA': 'NG', 'KEN': 'KE', 'ETH': 'ET', 'GHA': 'GH', 'SEN': 'SN', 'CIV': 'CI', 'CMR': 'CM', 'TZA': 'TZ', 'UGA': 'UG', 'MOZ': 'MZ', 'ZMB': 'ZM', 'ZWE': 'ZW', 'AGO': 'AO', 'COD': 'CD', 'MDG': 'MG', 'RWA': 'RW', 'BFA': 'BF', 'MLI': 'ML', 'NER': 'NE', 'TCD': 'TD', 'SDN': 'SD', 'SOM': 'SO', 'DJI': 'DJ', 'ERI': 'ER', 'LBY': 'LY', 'DZA': 'DZ', 'JOR': 'JO', 'LBN': 'LB', 'IRQ': 'IQ', 'IRN': 'IR', 'AFG': 'AF', 'PAK': 'PK', 'BGD': 'BD', 'LKA': 'LK', 'NPL': 'NP', 'MMR': 'MM', 'THA': 'TH', 'VNM': 'VN', 'KHM': 'KH', 'LAO': 'LA', 'MYS': 'MY', 'IDN': 'ID', 'PHL': 'PH', 'TWN': 'TW', 'HKG': 'HK', 'MNG': 'MN', 'KAZ': 'KZ', 'UZB': 'UZ', 'KGZ': 'KG', 'TJK': 'TJ', 'TKM': 'TM', 'AZE': 'AZ', 'BLR': 'BY', 'RUS': 'RU', 'ARG': 'AR', 'CHL': 'CL', 'COL': 'CO', 'PER': 'PE', 'VEN': 'VE', 'ECU': 'EC', 'BOL': 'BO', 'PRY': 'PY', 'URY': 'UY', 'GUY': 'GY', 'SUR': 'SR', 'PAN': 'PA', 'CRI': 'CR', 'NIC': 'NI', 'HND': 'HN', 'SLV': 'SV', 'GTM': 'GT', 'BLZ': 'BZ', 'CUB': 'CU', 'DOM': 'DO', 'HTI': 'HT', 'JAM': 'JM', 'TTO': 'TT', 'BRB': 'BB', 'BHS': 'BS', 'GRL': 'GL', 'FRO': 'FO', 'GIB': 'GI', 'AND': 'AD', 'MCO': 'MC', 'SMR': 'SM', 'VAT': 'VA', 'QAT': 'QA', 'KWT': 'KW', 'BHR': 'BH', 'OMN': 'OM', 'YEM': 'YE', 'SYR': 'SY', 'PSE': 'PS', 'CPV': 'CV', 'MUS': 'MU', 'SYC': 'SC', 'NAM': 'NA', 'BWA': 'BW', 'LSO': 'LS', 'SWZ': 'SZ', 'MWI': 'MW', 'BDI': 'BI', 'GAB': 'GA', 'COG': 'CG', 'GNQ': 'GQ', 'CAF': 'CF', 'SSD': 'SS', 'TGO': 'TG', 'BEN': 'BJ', 'LBR': 'LR', 'SLE': 'SL', 'GIN': 'GN', 'GNB': 'GW', 'GMB': 'GM', 'MRT': 'MR', 'FJI': 'FJ', 'PNG': 'PG', 'WSM': 'WS', 'TON': 'TO', 'VUT': 'VU', 'SLB': 'SB', 'TLS': 'TL', 'BRN': 'BN', 'MDV': 'MV', 'BTN': 'BT', 'PRK': 'KP', '1A': 'EU'}
    return m.get(c, c)


def build_legacy(pn, api_n, xml, csv_rows, cn_rows, base_raw, record_url, retrieved_at, notice_type):
    recs, excl = [], []
    pub_date = iso_date((api_n or {}).get('publication-date')) or (iso_date(((xml or {}).get('coded') or {}).get('REF_OJS', {}).get('DATE_PUB')) if xml else None)
    # awards with Canadian contractor from XML
    cb = (xml or {}).get('contracting_body') or {}
    obj = (xml or {}).get('object') or {}
    lots = (xml or {}).get('lots') or {}
    coded = (xml or {}).get('coded') or {}
    codif = coded.get('CODIF_DATA', {}) if isinstance(coded, dict) else {}
    aa = codif.get('AA_AUTHORITY_TYPE', {}) if isinstance(codif, dict) else {}
    aa_code = aa.get('@CODE') if isinstance(aa, dict) else None
    # CN duration info (from CSV contract notices), keyed by lot
    cn_dur_by_lot = defaultdict(list)
    for r in cn_rows:
        cn_dur_by_lot[(r.get('ID_LOT') or '').strip()].append(r)
    # If no XML (shouldn't normally happen), build from CSV rows
    awards = (xml or {}).get('awards') or []
    matched_any = False
    if awards:
        for ai, a in enumerate(awards):
            if not a.get('awarded'):
                continue
            ca_cons = [c for c in a.get('contractors', []) if (c.get('country') or '').upper() in ('CA', 'CAN')]
            if not ca_cons:
                continue
            matched_any = True
            lot = lots.get(a.get('lot_no') or '_') or (list(lots.values())[0] if len(lots) == 1 else {})
            signed = to_date(a.get('date_conclusion_contract'))
            start = to_date(lot.get('date_start'))
            end = to_date(lot.get('date_end'))
            dur_v, dur_u = lot.get('duration_value'), lot.get('duration_unit')
            basis_prefix = 'legacy TED XML: AWARD_CONTRACT/AWARDED_CONTRACT/DATE_CONCLUSION_CONTRACT and OBJECT_DESCR DURATION/DATE_START/DATE_END of the awarded lot'
            cn_used = None
            if not end and not dur_v:
                # fall back to contract-notice CSV row(s) (same lot, else single row)
                cands = cn_dur_by_lot.get((a.get('lot_no') or '').strip()) or (cn_rows if len({(r.get('DURATION'), r.get('CONTRACT_START'), r.get('CONTRACT_COMPLETION')) for r in cn_rows}) == 1 else [])
                cands = [r for r in cands if r.get('DURATION') or r.get('CONTRACT_COMPLETION')]
                if cands:
                    cn_used = cands[0]
                    start = start or to_date(cn_used.get('CONTRACT_START'))
                    end = to_date(cn_used.get('CONTRACT_COMPLETION'))
                    dur_v = cn_used.get('DURATION') or None
                    dur_u = 'MONTH' if dur_v else None
                    basis_prefix = f"legacy TED: award DATE_CONCLUSION_CONTRACT from the CAN XML; duration/start/end from the linked contract notice {cn_used.get('ID_NOTICE_CN')} (open-data CSV columns DURATION (months) / CONTRACT_START / CONTRACT_COMPLETION)"
            status, basis, computed_end = compute_status(start, signed, end, dur_v, dur_u, basis_prefix)
            if a.get('contract_no') is None and (xml or {}).get('form_name', '').startswith('CONTRACT_AWARD') and notice_type:
                pass
            if status in ('ended', 'ended_inferred', 'not_started'):
                excl.append({'publication_number': pn, 'award_item': a.get('item'), 'reason': basis})
                continue
            con = ca_cons[0]
            vals = a.get('values') or {}
            vt = vals.get('val_total') or {}
            csv_match = [r for r in csv_rows if (r.get('ID_LOT_AWARDED') or '').strip() == (a.get('lot_no') or '').strip() or (r.get('CONTRACT_NUMBER') or '').strip() == (a.get('contract_no') or '').strip()] or csv_rows
            recs.append({
                'record_id': f"ted_eu:{pn}:award{a.get('item') or ai+1}",
                'source': src(record_url, retrieved_at),
                'status': status, 'status_basis': basis,
                'contract': {
                    'identifiers': {
                        'publication_number': pn, 'ojs_issue': (api_n or {}).get('ojs-number') or (coded.get('NOTICE_DATA', {}) or {}).get('NO_DOC_OJS') if isinstance(coded, dict) else None,
                        'notice_ndoc_ojs': (coded.get('NOTICE_DATA', {}) or {}).get('NO_DOC_OJS') if isinstance(coded, dict) else None,
                        'award_item': a.get('item'), 'lot_no': a.get('lot_no'), 'contract_no': a.get('contract_no'),
                        'buyer_reference_number': obj.get('reference_number'),
                        'opendata_id_notice_can': csv_rows[0]['ID_NOTICE_CAN'] if csv_rows else None,
                        'opendata_id_award': [r.get('ID_AWARD') for r in csv_match],
                        'previous_notice_oj': ((xml or {}).get('procedure') or {}).get('notice_number_oj'),
                        'contract_notice_ids_opendata': sorted({r['ID_NOTICE_CN'] for r in cn_rows}),
                    },
                    'title': a.get('title') or obj.get('title'),
                    'description': lot.get('short_descr') or obj.get('short_descr'),
                    'instrument_type': 'framework agreement' if (((xml or {}).get('procedure') or {}).get('framework') or obj.get('framework') or any(r.get('B_FRA_AGREEMENT') == 'Y' for r in csv_rows)) else 'contract',
                    'procurement_method': (codif.get('PR_PROC') or {}).get('#text') if isinstance(codif.get('PR_PROC'), dict) else None,
                    'solicitation_procedure': (api_n or {}).get('procedure-type') or (csv_rows[0].get('TOP_TYPE') if csv_rows else None),
                    'commodity': {'cpv': obj.get('cpv_main'), 'cpv_additional': lot.get('cpv_additional') or obj.get('cpv_additional'), 'contract_nature': obj.get('type_contract')},
                    'value': num(vt.get('value')),
                    'currency': vt.get('currency'),
                    'value_detail': {'award_val_total': num(vt.get('value')), 'award_val_estimated_total': num((vals.get('val_estimated_total') or {}).get('value')),
                                     'award_val_range_total': vals.get('val_range_total'), 'award_initial_estimated': vals.get('initial_estimated'),
                                     'notice_val_total': num((obj.get('val_total') or {}).get('value')), 'notice_val_total_currency': (obj.get('val_total') or {}).get('currency'),
                                     'opendata_award_value_euro': num(csv_match[0].get('AWARD_VALUE_EURO')) if csv_match else None,
                                     'opendata_notice_value_euro': num(csv_match[0].get('VALUE_EURO')) if csv_match else None},
                    'dates': {'published': pub_date, 'signed': signed.isoformat() if signed else None, 'start': start.isoformat() if start else None, 'end': end.isoformat() if end else None,
                              'end_computed': computed_end.isoformat() if computed_end and not end else None,
                              'duration': {'value': dur_v, 'unit': dur_u} if dur_v else None,
                              'dispatch': iso_date(((xml or {}).get('complementary_info') or {}).get('date_dispatch_notice')) or iso_date(codif.get('DS_DATE_DISPATCH')),
                              'amended_last': None},
                    'related': {'award_notice_url': record_url, 'notice_xml_url': f"https://ted.europa.eu/en/notice/{pn}/xml", 'notice_pdf_url': f"https://ted.europa.eu/en/notice/{pn}/pdf",
                                'legacy_notice_url': csv_rows[0]['TED_NOTICE_URL'] if csv_rows else None,
                                'contract_notice_urls': sorted({r['TED_NOTICE_URL'] for r in cn_rows}) if cn_rows else [],
                                'buyer_profile_url': cb.get('url_buyer'), 'buyer_website': cb.get('url_general')},
                },
                'buyer': {
                    'name': cb.get('name') or (csv_rows[0].get('CAE_NAME') if csv_rows else None),
                    'country': country2(cb.get('country') or (csv_rows[0].get('ISO_COUNTRY_CODE') if csv_rows else None)),
                    'type': LEGACY_AA.get(aa_code, cb.get('ca_type')),
                    'identifiers': {'national_id': cb.get('national_id'), 'opendata_cae_nationalid': csv_rows[0].get('CAE_NATIONALID') if csv_rows else None, 'ca_type_code': cb.get('ca_type'), 'aa_authority_type_code': aa_code},
                    'address': {'line1': cb.get('address'), 'city': cb.get('town'), 'postal_code': cb.get('postal_code'), 'country': cb.get('country'), 'nuts': cb.get('nuts')},
                    'contact': {'contact_point': cb.get('contact_point'), 'attention': cb.get('attention'), 'phone': cb.get('phone'), 'fax': cb.get('fax'), 'email': cb.get('email'), 'website': cb.get('url_general')},
                    'main_activity': cb.get('ca_activity'),
                },
                'vendor': {
                    'name': con.get('name'), 'country': 'CA',
                    'country_basis': 'legacy TED XML AWARD_CONTRACT/AWARDED_CONTRACT/CONTRACTORS/CONTRACTOR/ADDRESS_CONTRACTOR/COUNTRY@VALUE = CA (R2.0.9) or ECONOMIC_OPERATOR_NAME_ADDRESS/.../COUNTRY@VALUE = CA (R2.0.8); open-data CSV WIN_COUNTRY_CODE contains CA',
                    'identifiers': {'national_id': con.get('national_id'), 'opendata_win_nationalid': csv_match[0].get('WIN_NATIONALID') if csv_match else None},
                    'address': {'line1': con.get('address'), 'city': con.get('town'), 'region': None, 'postal_code': con.get('postal_code'), 'country': con.get('country'), 'nuts': con.get('nuts')},
                    'contact': {'phone': con.get('phone'), 'fax': con.get('fax'), 'email': con.get('email'), 'website': con.get('url')},
                    'sme': con.get('sme'),
                    'awarded_to_group': a.get('awarded_to_group') or len(a.get('contractors', [])) > 1,
                    'group_members': [{'name': c.get('name'), 'country': c.get('country')} for c in a.get('contractors', [])] if len(a.get('contractors', [])) > 1 else None,
                },
                'raw': {**base_raw, 'matched_award': a, 'matched_lot': lot, 'matched_contract_notice_row': cn_used},
            })
    if not matched_any:
        if not awards and csv_rows:
            # XML missing: build from CSV rows only
            for r in csv_rows:
                parts = [p.strip().upper() for p in (r.get('WIN_COUNTRY_CODE') or '').split('---')]
                names = [p.strip() for p in (r.get('WIN_NAME') or '').split('---')]
                towns = [p.strip() for p in (r.get('WIN_TOWN') or '').split('---')]
                addrs = [p.strip() for p in (r.get('WIN_ADDRESS') or '').split('---')]
                pcs = [p.strip() for p in (r.get('WIN_POSTAL_CODE') or '').split('---')]
                nids = [p.strip() for p in (r.get('WIN_NATIONALID') or '').split('---')]
                for i, p in enumerate(parts):
                    if p != 'CA':
                        continue
                    signed = to_date(r.get('DT_AWARD')) or to_date(r.get('DT_DISPATCH'))
                    cands = [c for c in cn_rows if c.get('DURATION') or c.get('CONTRACT_COMPLETION')]
                    cn_used = cands[0] if len({(c.get('DURATION'), c.get('CONTRACT_START'), c.get('CONTRACT_COMPLETION')) for c in cands}) == 1 else None
                    start = to_date(cn_used.get('CONTRACT_START')) if cn_used else None
                    end = to_date(cn_used.get('CONTRACT_COMPLETION')) if cn_used else None
                    dur_v = (cn_used.get('DURATION') or None) if cn_used else None
                    status, basis, computed_end = compute_status(start, signed, end, dur_v, 'MONTH' if dur_v else None, 'open-data CSV only (notice XML not retrievable): DT_AWARD and linked contract-notice DURATION/CONTRACT_START/CONTRACT_COMPLETION')
                    if status in ('ended', 'ended_inferred', 'not_started'):
                        excl.append({'publication_number': pn, 'id_award': r.get('ID_AWARD'), 'reason': basis})
                        continue
                    recs.append({
                        'record_id': f"ted_eu:{pn}:csvaward{r.get('ID_AWARD')}:{i}",
                        'source': src(record_url, retrieved_at),
                        'status': status, 'status_basis': basis,
                        'contract': {'identifiers': {'publication_number': pn, 'opendata_id_notice_can': r.get('ID_NOTICE_CAN'), 'opendata_id_award': r.get('ID_AWARD'), 'lot_no': r.get('ID_LOT_AWARDED'), 'contract_no': r.get('CONTRACT_NUMBER')},
                                     'title': r.get('TITLE') or None, 'description': None, 'instrument_type': 'framework agreement' if r.get('B_FRA_AGREEMENT') == 'Y' else 'contract',
                                     'procurement_method': r.get('TOP_TYPE'), 'solicitation_procedure': r.get('TOP_TYPE'),
                                     'commodity': {'cpv': r.get('CPV'), 'cpv_additional': r.get('ADDITIONAL_CPVS'), 'contract_nature': r.get('TYPE_OF_CONTRACT')},
                                     'value': num(r.get('AWARD_VALUE_EURO')), 'currency': 'EUR' if r.get('AWARD_VALUE_EURO') else None,
                                     'value_detail': {'opendata_award_value_euro': num(r.get('AWARD_VALUE_EURO')), 'opendata_award_est_value_euro': num(r.get('AWARD_EST_VALUE_EURO')), 'opendata_notice_value_euro': num(r.get('VALUE_EURO'))},
                                     'dates': {'published': pub_date, 'signed': signed.isoformat() if signed else None, 'start': start.isoformat() if start else None, 'end': end.isoformat() if end else None, 'end_computed': computed_end.isoformat() if computed_end and not end else None, 'duration': {'value': dur_v, 'unit': 'MONTH'} if dur_v else None, 'dispatch': iso_date(r.get('DT_DISPATCH')), 'amended_last': None},
                                     'related': {'award_notice_url': record_url, 'legacy_notice_url': r.get('TED_NOTICE_URL')}},
                        'buyer': {'name': r.get('CAE_NAME'), 'country': country2(r.get('ISO_COUNTRY_CODE')), 'type': r.get('CAE_TYPE'), 'identifiers': {'opendata_cae_nationalid': r.get('CAE_NATIONALID')},
                                  'address': {'line1': r.get('CAE_ADDRESS'), 'city': r.get('CAE_TOWN'), 'postal_code': r.get('CAE_POSTAL_CODE'), 'country': r.get('ISO_COUNTRY_CODE')}, 'contact': {}, 'main_activity': r.get('MAIN_ACTIVITY')},
                        'vendor': {'name': names[i] if i < len(names) else None, 'country': 'CA', 'country_basis': 'open-data CSV WIN_COUNTRY_CODE[i] = CA',
                                   'identifiers': {'opendata_win_nationalid': nids[i] if i < len(nids) else None},
                                   'address': {'line1': addrs[i] if i < len(addrs) else None, 'city': towns[i] if i < len(towns) else None, 'postal_code': pcs[i] if i < len(pcs) else None, 'country': 'CA'}, 'contact': {}},
                        'raw': {**base_raw, 'matched_csv_row': r},
                    })
        elif awards:
            excl.append({'publication_number': pn, 'reason': 'legacy XML has no awarded contract with a Canadian contractor (CSV match may come from a non-CA winner in a group or from a corrected notice)'})
        else:
            excl.append({'publication_number': pn, 'reason': 'no XML awards and no CSV rows'})
    return recs, excl


if __name__ == '__main__':
    main()
