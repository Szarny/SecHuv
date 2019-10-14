from typing import Any, List, Tuple, Dict, Union
from tinydb import TinyDB, Query

from model.mailspec import MailSpec
from model.mailvalidcase import MailValidCase

import util


def validation(post_data: Any) -> bool:
    # TODO: POSTされたデータのバリデーションを行う
    return True


def handle(db: Dict[str, TinyDB], mail_spec: MailSpec) -> Tuple[bool, Dict[str, str]]:
    uuid: str = util.uuid.get_uuid()
    post_date: str = util.datetime.get_current()

    mail_valid_case: MailValidCase = {
        "uuid": uuid,
        "post_date": post_date,
        "spec": mail_spec
    }

    # TODO: DB登録時のエラーハンドリングを実装する
    _: int = db["mailvalid"].insert(mail_valid_case)

    return (True, {
        "uuid": uuid,
        "post_date": post_date
    })

