from typing import List, Dict

from model.mailpostspec import MailPostSpec

import util
from . import core


def check_fake_url(mail_post_spec: MailPostSpec) -> Dict[str, str]:
    urls: List[str] = util.url.extract(mail_post_spec["body"]) + [mail_post_spec["from_addr"].split("@")[1]]

    for url in urls:
        is_detect, message = core.fake_url.check(url)

        if is_detect:
            return {
                "vulntype": "fake_url",
                "message": message
            }

    return {}


def check_authority(summary:str, mail_post_spec: MailPostSpec) -> Dict[str, str]:
    is_detect, message = core.authority.check(summary, mail_post_spec["body"])
    
    if is_detect:
        return {
            "vulntype": "authority",
            "message": message
        }
    else:
        return {}


def check_fake_alert(summary:str, mail_post_spec: MailPostSpec) -> Dict[str, str]:
    is_detect, message = core.fake_alert.check(summary, mail_post_spec["body"])
    
    if is_detect:
        return {
            "vulntype": "fake_alert",
            "message": message
        }
    else:
        return {}


def check_profit(summary:str, mail_post_spec: MailPostSpec) -> Dict[str, str]:
    is_detect, message = core.profit.check(summary, mail_post_spec["body"])
    
    if is_detect:
        return {
            "vulntype": "profit",
            "message": message
        }
    else:
        return {}


def check_scarcity(summary:str, mail_post_spec: MailPostSpec) -> Dict[str, str]:
    is_detect, message = core.scarcity.check(summary, mail_post_spec["body"])
    
    if is_detect:
        return {
            "vulntype": "scarcity",
            "message": message
        }
    else:
        return {}


def check_sextortion(summary:str, mail_post_spec: MailPostSpec) -> Dict[str, str]:
    is_detect, message = core.sextortion.check(summary, mail_post_spec["body"])
    
    if is_detect:
        return {
            "vulntype": "sextortion",
            "message": message
        }
    else:
        return {}


def check_urgent(summary:str, mail_post_spec: MailPostSpec) -> Dict[str, str]:
    is_detect, message = core.urgent.check(summary, mail_post_spec["body"])
    
    if is_detect:
        return {
            "vulntype": "urgent",
            "message": message
        }
    else:
        return {}



def run(mail_post_spec: MailPostSpec) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    # fake_url
    check_fake_url_result: Dict[str, str] = check_fake_url(mail_post_spec)
    if check_fake_url_result:
        result.append(check_fake_url_result)

    summary: str = util.semantic_volume.summarize(mail_post_spec["body"])

    check_authority_result: Dict[str, str] = check_authority(summary, mail_post_spec)
    if check_authority_result != {}:
        result.append(check_authority_result)


    check_fake_alert_result: Dict[str, str] = check_fake_alert(summary, mail_post_spec)
    if check_fake_alert_result != {}:
        result.append(check_fake_alert_result)


    check_profit_result: Dict[str, str] = check_profit(summary, mail_post_spec)
    if check_profit_result != {}:
        result.append(check_profit_result)


    check_scarcity_result: Dict[str, str] = check_scarcity(summary, mail_post_spec)
    if check_scarcity_result != {}:
        result.append(check_scarcity_result)


    check_sextortion_result: Dict[str, str] = check_sextortion(summary, mail_post_spec)
    if check_sextortion_result != {}:
        result.append(check_sextortion_result)


    check_urgent_result: Dict[str, str] = check_urgent(summary, mail_post_spec)
    if check_urgent_result != {}:
        result.append(check_urgent_result)


    return result