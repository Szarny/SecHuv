import re
import MeCab
import numpy as np
from gensim.models import Word2Vec

from typing import List, Dict

from model.otherpostspec import OtherPostSpec

import util
from . import core


def check_fake_url(other_post_spec: OtherPostSpec) -> Dict[str, str]:
    urls: List[str] = util.url.extract(other_post_spec["payload"]) 

    for url in urls:
        is_detect, message = core.fake_url.check(url)

        if is_detect:
            return {
                "vulntype": "fake_url",
                "message": message
            }

    return {}


def check_sextortion(summary: str) -> Dict[str, str]:
    is_detect, message = core.sextortion.check(summary)
    
    if is_detect:
        return {
            "vulntype": "sextortion",
            "message": message
        }
    else:
        return {}



def run(other_post_spec: OtherPostSpec) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    # fake_url
    check_fake_url_result: Dict[str, str] = check_fake_url(other_post_spec)
    if check_fake_url_result != {}:
        result.append(check_fake_url_result)


    summary: str = util.semantic_volume.summarize(other_post_spec["payload"])

    # sextortion
    check_sextortion_result: Dict[str, str] = check_sextortion(summary)
    if check_sextortion_result != {}:
        result.append(check_sextortion_result)

    return result


if __name__ == '__main__':
    run({
        "media": "SMS",
        "metadata": "hoge",
        "payload": "あなたを撮影しました。"
    })