from typing import Any, List, Tuple, Dict, Union
from tinydb import TinyDB, Query

from model.webcasepost import WebCasePost
from model.webcase import WebCase
from model.vulnerability import Vulnerability

import util


def validation(post_data: Any) -> bool:
    # TODO: POSTされたデータのバリデーションを行う
    return True


def handle(db: Dict[str, TinyDB], web_case_post: WebCasePost) -> Tuple[bool, Dict[str, str]]:
    uuid: str = util.uuid.get_uuid()
    post_date: str = util.datetime.get_current()

    ok: bool
    ok = util.vulnchecker.check_corresponding_vuln(db=db, vulntypes=web_case_post["vulntypes"])

    if not ok:
        return (False, {})

    web_case: WebCase = {
        "uuid": uuid,
        "post_date": post_date,
        "vulntypes": web_case_post["vulntypes"],
        "spec": web_case_post["spec"]
    }

    # TODO: DB登録時のエラーハンドリングを実装する
    _: int = db["web"].insert(web_case)

    return (True, {
        "uuid": uuid,
        "post_date": post_date
    })

