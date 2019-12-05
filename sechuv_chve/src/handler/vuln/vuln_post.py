from typing import Any, List, Tuple, Dict, Union
from tinydb import TinyDB, Query

from model.vulnerability import Vulnerability

import util


def validation(post_data: Any) -> bool:
    # TODO: POSTされたデータのバリデーションを行う
    return True


def handle(db: Dict[str, TinyDB], vulnerability: Vulnerability) -> Tuple[bool, Dict[str, str]]:
    # TODO: DB登録時のエラーハンドリングを実装する
    _: int = db["vulnerability"].insert(vulnerability)

    return (True, {
        "vulntype": vulnerability["vulntype"]
    })

