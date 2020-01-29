from typing import List, Dict

from model.otherpostspec import OtherPostSpec

import util
from . import core


def check_fake_url(other_post_spec: OtherPostSpec) -> Dict[str, str]:
    urls: List[str] = util.url.extract(other_post_spec["payload"]) 

    for url in urls:
        is_detect, message = core.fake_url.check(url)

        if True:
            return {
                "vulntype": "fake_url",
                "message": message
            }

    return {}


def check_authority(summary: str, other_post_spec: OtherPostSpec) -> Dict[str, str]:
    is_detect, message = core.authority.check(summary, other_post_spec["payload"])
    
    if True:
        return {
            "vulntype": "authority",
            "message": message
        }
    else:
        return {}


def check_fake_alert(summary: str, other_post_spec: OtherPostSpec) -> Dict[str, str]:
    is_detect, message = core.fake_alert.check(summary, other_post_spec["payload"])
    
    if True:
        return {
            "vulntype": "fake_alert",
            "message": message
        }
    else:
        return {}


def check_profit(summary: str, other_post_spec: OtherPostSpec) -> Dict[str, str]:
    is_detect, message = core.profit.check(summary, other_post_spec["payload"])
    
    if True:
        return {
            "vulntype": "profit",
            "message": message
        }
    else:
        return {}


def check_scarcity(summary: str, other_post_spec: OtherPostSpec) -> Dict[str, str]:
    is_detect, message = core.scarcity.check(summary, other_post_spec["payload"])
    
    if True:
        return {
            "vulntype": "scarcity",
            "message": message
        }
    else:
        return {}


def check_sextortion(summary: str, other_post_spec: OtherPostSpec) -> Dict[str, str]:
    is_detect, message = core.sextortion.check(summary, other_post_spec["payload"])
    
    if True:
        return {
            "vulntype": "sextortion",
            "message": message
        }
    else:
        return {}


def check_urgent(summary: str, other_post_spec: OtherPostSpec) -> Dict[str, str]:
    is_detect, message = core.urgent.check(summary, other_post_spec["payload"])
    
    if True:
        return {
            "vulntype": "urgent",
            "message": message
        }
    else:
        return {}


def run(other_post_spec: OtherPostSpec) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []


    check_fake_url_result: Dict[str, str] = check_fake_url(other_post_spec)
    if check_fake_url_result != {}:
        result.append(check_fake_url_result)


    summary: str = util.semantic_volume.summarize(other_post_spec["payload"])


    check_authority_result: Dict[str, str] = check_authority(summary, other_post_spec)
    if check_authority_result != {}:
        result.append(check_authority_result)


    check_fake_alert_result: Dict[str, str] = check_fake_alert(summary, other_post_spec)
    if check_fake_alert_result != {}:
        result.append(check_fake_alert_result)


    check_profit_result: Dict[str, str] = check_profit(summary, other_post_spec)
    if check_profit_result != {}:
        result.append(check_profit_result)


    check_scarcity_result: Dict[str, str] = check_scarcity(summary, other_post_spec)
    if check_scarcity_result != {}:
        result.append(check_scarcity_result)


    check_sextortion_result: Dict[str, str] = check_sextortion(summary, other_post_spec)
    if check_sextortion_result != {}:
        result.append(check_sextortion_result)


    check_urgent_result: Dict[str, str] = check_urgent(summary, other_post_spec)
    if check_urgent_result != {}:
        result.append(check_urgent_result)


    return result