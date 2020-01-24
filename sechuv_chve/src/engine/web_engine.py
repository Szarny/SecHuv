from typing import List, Dict

from model.web_check import WebCheck

from . import core

def check_fake_url(web_check: WebCheck) -> Dict[str, str]:
    is_detect, message = core.fake_url.check(web_check["url"])

    if is_detect:
        return {
            "vulntype": "fake_url",
            "message": message
        }
    else:
        return {}


def run(web_check: WebCheck) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    fake_url_result: Dict[str, str] = check_fake_url(web_check)
    if fake_url_result:
        result.append(fake_url_result)

    return result