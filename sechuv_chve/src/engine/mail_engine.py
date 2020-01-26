from typing import List, Dict

from model.mailpostspec import MailPostSpec

import util

from . import core

def check_fake_url(mail_post_spec: MailPostSpec) -> Dict[str, str]:
    urls: List[str] = util.url.extract(mail_post_spec["body"]) + [mail_post_spec["from_addr"].split("@")[1]]
    is_detect, message = core.fake_url.check(url)

    if is_detect:
        return {
            "vulntype": "fake_url",
            "message": message
        }
    else:
        return {}


def run(mail_post_spec: MailPostSpec) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    # fake_url
    check_fake_url_result: Dict[str, str] = check_fake_url(mail_post_spec)
    if check_fake_url:
        result.append(check_fake_url_result)

    

    return result