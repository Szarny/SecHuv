from typing import Any, List, Tuple, Dict, Union
from tinydb import TinyDB, Query

from model.mailcasepost import MailCasePost
from model.mailcase import MailCase
from model.vulnerability import Vulnerability

import util


def validation(post_data: Any) -> bool:
    # TODO: POSTされたデータのバリデーションを行う
    return True


def handle(db: Dict[str, TinyDB], mail_case_post: MailCasePost) -> Tuple[bool, Dict[str, str]]:
    uuid: str = util.uuid.get_uuid()
    post_date: str = util.dt.get_current()

    ok: bool
    ok = util.vulnchecker.check_corresponding_vuln(db=db, vulntypes=mail_case_post["vulntypes"])

    if not ok:
        return (False, {})

    mail_case: MailCase = {
        "uuid": uuid,
        "post_date": post_date,
        "vulntypes": mail_case_post["vulntypes"],
        "spec": mail_case_post["spec"]
    }

    # TODO: DB登録時のエラーハンドリングを実装する
    _: int = db["mail"].insert(mail_case)

    return (True, {
        "uuid": uuid,
        "post_date": post_date
    })

