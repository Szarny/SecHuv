import re

from typing import List, Dict

from model.webpostspec import WebPostSpec

from . import core

def check_fake_url(web_post_spec: WebPostSpec) -> Dict[str, str]:
    urls: List[str] = util.url.extract(web_post_spec["url"]) 
    is_detect, message = core.fake_url.check(url)

    if is_detect:
        return {
            "vulntype": "fake_url",
            "message": message
        }
    else:
        return {}


def summarize(text: str) -> str:
    text = re.sub(r"《[^》]*》", "", text)
    text = text.replace("\u3000", "")
    text = re.sub(r"\n\n［.*\n\n", "。", text)
    text = re.sub(r"[\n]", "。", text)
    text = re.sub("[。]+", "。", text)

    sv = SemanticVolume()
    sv.execute(text, 200)
    return " ".join(sv.summarized_sentence)


def run(web_post_spec: WebPostSpec) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    # fake_url
    check_fake_url_result: Dict[str, str] = check_fake_url(web_post_spec)
    if check_fake_url:
        result.append(check_fake_url_result)


    return result