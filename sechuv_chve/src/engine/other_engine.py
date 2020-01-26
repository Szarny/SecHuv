from typing import List, Dict

from model.otherpostspec import OtherPostSpec

import util

from . import core


def check_fake_url(other_post_spec: OtherPostSpec) -> Dict[str, str]:
    urls: List[str] = util.url.extract(other_post_spec["payload"]) 
    is_detect, message = core.fake_url.check(url)

    if is_detect:
        return {
            "vulntype": "fake_url",
            "message": message
        }
    else:
        return {}


def run(other_post_spec: OtherPostSpec) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    # fake_url
    check_fake_url_result: Dict[str, str] = check_fake_url(other_post_spec)
    if check_fake_url:
        result.append(check_fake_url_result)


    return result