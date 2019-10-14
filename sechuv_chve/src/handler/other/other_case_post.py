from typing import Any, List, Tuple, Dict, Union
from tinydb import TinyDB, Query

from model.othercasepost import OtherCasePost
from model.othercase import OtherCase
from model.vulnerability import Vulnerability

import util


def validation(post_data: Any) -> bool:
    # TODO: POSTされたデータのバリデーションを行う
    return True


def handle(db: Dict[str, TinyDB], other_case_post: OtherCasePost) -> Tuple[bool, Dict[str, str]]:
    uuid: str = util.uuid.get_uuid()
    post_date: str = util.datetime.get_current()

    ok: bool
    vulns: List[Vulnerability]
    ok, vulns = util.vulnmapper.map_vulntype_to_vuln(db=db, vulntypes=other_case_post["vulntypes"])

    if not ok:
        return (False, {})

    otehr_case: OtherCase = {
        "uuid": uuid,
        "post_date": post_date,
        "vulns": vulns,
        "spec": other_case_post["spec"]
    }

    # TODO: DB登録時のエラーハンドリングを実装する
    _: int = db["other"].insert(otehr_case)

    return (True, {
        "uuid": uuid,
        "post_date": post_date
    })

