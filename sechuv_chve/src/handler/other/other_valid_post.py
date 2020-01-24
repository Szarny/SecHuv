from typing import Any, List, Tuple, Dict, Union
from tinydb import TinyDB, Query

from model.otherspec import OtherSpec
from model.othervalidcase import OtherValidCase

import util


def validation(post_data: Any) -> bool:
    # TODO: POSTされたデータのバリデーションを行う
    return True


def handle(db: Dict[str, TinyDB], other_spec: OtherSpec) -> Tuple[bool, Dict[str, str]]:
    uuid: str = util.uuid.get_uuid()
    post_date: str = util.dt.get_current()

    other_valid_case: OtherValidCase = {
        "uuid": uuid,
        "post_date": post_date,
        "spec": other_spec
    }

    # TODO: DB登録時のエラーハンドリングを実装する
    _: int = db["othervalid"].insert(other_valid_case)

    return (True, {
        "uuid": uuid,
        "post_date": post_date
    })

