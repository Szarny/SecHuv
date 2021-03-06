from typing import List, Dict

from model.webpostspec import WebPostSpec

import util
from . import core


def check_fake_url(web_post_spec: WebPostSpec) -> Dict[str, str]:
    url: List[str] = web_post_spec["url"]
    is_detect, message = core.fake_url.check(url)

    if is_detect:
        return {
            "vulntype": "fake_url",
            "message": message
        }
    else:
        return {}

        
def check_authority(summary: str, web_post_spec: WebPostSpec) -> Dict[str, str]:
    is_detect, message = core.authority.check(summary, web_post_spec["raw_body"])
    
    if is_detect:
        return {
            "vulntype": "authority",
            "message": message
        }
    else:
        return {}


def check_fake_alert(summary: str, web_post_spec: WebPostSpec) -> Dict[str, str]:
    is_detect, message = core.fake_alert.check(summary, web_post_spec["raw_body"])
    
    if is_detect:
        return {
            "vulntype": "fake_alert",
            "message": message
        }
    else:
        return {}


def check_profit(summary: str, web_post_spec: WebPostSpec) -> Dict[str, str]:
    is_detect, message = core.profit.check(summary, web_post_spec["raw_body"])
    
    if is_detect:
        return {
            "vulntype": "profit",
            "message": message
        }
    else:
        return {}


def check_scarcity(summary: str, web_post_spec: WebPostSpec) -> Dict[str, str]:
    is_detect, message = core.scarcity.check(summary, web_post_spec["raw_body"])
    
    if is_detect:
        return {
            "vulntype": "scarcity",
            "message": message
        }
    else:
        return {}


def check_sextortion(summary: str, web_post_spec: WebPostSpec) -> Dict[str, str]:
    is_detect, message = core.sextortion.check(summary, web_post_spec["raw_body"])
    
    if is_detect:
        return {
            "vulntype": "sextortion",
            "message": message
        }
    else:
        return {}


def check_urgent(summary: str, web_post_spec: WebPostSpec) -> Dict[str, str]:
    is_detect, message = core.urgent.check(summary, web_post_spec["raw_body"])
    
    if is_detect:
        return {
            "vulntype": "urgent",
            "message": message
        }
    else:
        return {}


def run(web_post_spec: WebPostSpec) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    # fake_url
    check_fake_url_result: Dict[str, str] = check_fake_url(web_post_spec)
    if check_fake_url:
        result.append(check_fake_url_result)


    ok, body, raw_body = util.html.get_html(web_post_spec["url"])
    if not ok:
        return result

    summary: str = util.semantic_volume.summarize(raw_body)

    check_authority_result: Dict[str, str] = check_authority(summary, web_post_spec)
    if check_authority_result != {}:
        result.append(check_authority_result)


    check_fake_alert_result: Dict[str, str] = check_fake_alert(summary, web_post_spec)
    if check_fake_alert_result != {}:
        result.append(check_fake_alert_result)


    check_profit_result: Dict[str, str] = check_profit(summary, web_post_spec)
    if check_profit_result != {}:
        result.append(check_profit_result)


    check_scarcity_result: Dict[str, str] = check_scarcity(summary, web_post_spec)
    if check_scarcity_result != {}:
        result.append(check_scarcity_result)


    check_sextortion_result: Dict[str, str] = check_sextortion(summary, web_post_spec)
    if check_sextortion_result != {}:
        result.append(check_sextortion_result)


    check_urgent_result: Dict[str, str] = check_urgent(summary, web_post_spec)
    if check_urgent_result != {}:
        result.append(check_urgent_result)


    return result