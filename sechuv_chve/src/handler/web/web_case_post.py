from typing import Any, List, Tuple, Dict, Union
from tinydb import TinyDB, Query

from model.webcasepost import WebCasePost
from model.webcase import WebCase
from model.webspec import WebSpec
from model.vulnerability import Vulnerability

import util


def validation(post_data: Any) -> bool:
    # TODO: POSTされたデータのバリデーションを行う
    return True


def handle(db: Dict[str, TinyDB], web_case_post: WebCasePost) -> Tuple[bool, Dict[str, str]]:
    uuid: str = util.uuid.get_uuid()
    post_date: str = util.dt.get_current()

    ok: bool
    ok = util.vulnchecker.check_corresponding_vuln(db=db, vulntypes=web_case_post["vulntypes"])
    if not ok:
        return (False, {})

    
    ok, body, raw_body = util.html.get_html(web_case_post["spec"]["url"])
    if not ok:
        return (False, {})


    ok, screenshot = util.screenshot.take_screenshot(web_case_post["spec"]["url"])
    if not ok:
        return (False, {})
    
    web_case_post["spec"]["screenshot"] = screenshot

    summary: str = util.semantic_volume.summarize(raw_body)

    web_spec: WebSpec = {
        "url": web_case_post["spec"]["url"],
        "body": body,
        "raw_body": raw_body,
        "screenshot": screenshot,
        "summary": summary if len(summary) <= len(raw_body) else raw_body
    }

    web_case: WebCase = {
        "uuid": uuid,
        "post_date": post_date,
        "vulntypes": web_case_post["vulntypes"],
        "spec": web_spec
    }

    # TODO: DB登録時のエラーハンドリングを実装する
    _: int = db["web"].insert(web_case)

    return (True, {
        "uuid": uuid,
        "post_date": post_date
    })

