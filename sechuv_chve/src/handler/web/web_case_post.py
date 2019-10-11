from typing import Any, Tuple, Dict, Union
from tinydb import TinyDB

from model.webcasepost import WebCasePost
from model.webcase import WebCase

import util


def validation(post_data: Any) -> bool:
    # TODO: POSTされたデータのバリデーションを行う
    return True


def handle(db: TinyDB, web_case_post: WebCasePost) -> Tuple[bool, Dict[str, str]]:
    uuid: str = util.uuid.get_uuid()
    post_date: str = util.datetime.get_current()

    web_case: WebCase = {
        "uuid": uuid,
        "post_date": post_date,
        "vulns": web_case_post["vulns"],
        "spec": web_case_post["spec"]
    }

    # TODO: DB登録時のエラーハンドリングを追加する
    _: int = db["web"].insert(web_case)

    return (True, {
        "uuid": uuid,
        "post_date": post_date
    })

