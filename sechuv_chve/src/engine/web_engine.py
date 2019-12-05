from typing import List, Dict

from model.webspec import WebSpec

from . import core

def check_fake_url(web_spec: WebSpec) -> Dict[str, str]:
    is_detect, message = core.fake_url.check(web_spec["url"])

    if is_detect:
        return {
            "vulntype": "fake_url",
            "message": message
        }
    else:
        return {}


def run(web_spec: WebSpec) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    # fake_url
    fake_url_result: Dict[str, str] = check_fake_url(web_spec)
    if fake_url_result:
        result.append(fake_url_result)

    return result