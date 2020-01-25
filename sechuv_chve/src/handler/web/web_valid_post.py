from typing import Any, List, Tuple, Dict, Union
from tinydb import TinyDB, Query

from model.webspec import WebSpec
from model.webvalidcase import WebValidCase

import util


def validation(post_data: Any) -> bool:
    # TODO: POSTされたデータのバリデーションを行う
    return True


def handle(db: Dict[str, TinyDB], web_spec: WebSpec) -> Tuple[bool, Dict[str, str]]:
    uuid: str = util.uuid.get_uuid()
    post_date: str = util.dt.get_current()

    web_valid_case: WebValidCase = {
        "uuid": uuid,
        "post_date": post_date,
        "spec": web_spec
    }

    # TODO: DB登録時のエラーハンドリングを実装する
    _: int = db["webvalid"].insert(web_valid_case)

    return (True, {
        "uuid": uuid,
        "post_date": post_date
    })

