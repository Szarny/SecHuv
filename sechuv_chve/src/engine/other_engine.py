from typing import List, Dict

from model.othercheck import OtherCheck

import util

from . import core


def check_fake_url(url: str) -> Dict[str, str]:
    is_detect, message = core.fake_url.check(url)

    if is_detect:
        return {
            "vulntype": "fake_url",
            "message": message
        }
    else:
        return {}


def run(other_check: OtherSpec) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    # fake_url
    urls: List[str] = util.url.extract(other_check["payload"])
    for url in urls:
        fake_url_result: Dict[str, str] = check_fake_url(url)
        if fake_url_result:
            result.append(fake_url_result)
            break

    return result