from typing import List, Dict

from model.mailcheck import MailCheck

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


def run(mail_check: mail_check) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    # fake_url
    urls: List[str] = util.url.extract(mail_check["body"]) + [mail_check["from_addr"].split("@")[1]]
    for url in urls:
        fake_url_result: Dict[str, str] = check_fake_url(url)
        if fake_url_result:
            result.append(fake_url_result)
            break

    return result