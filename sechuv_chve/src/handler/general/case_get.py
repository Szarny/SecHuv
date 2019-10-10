from typing import Dict, List, Tuple, Union

from tinydb import TinyDB, Query

from model.case import Case
from model.webcase import WebCase
from model.mailcase import MailCase
from model.othercase import OtherCase


def validation(uuid: str, kind: str, is_valid: str) -> Tuple[bool, str]:
    if uuid is None:
        return (False, "Parameter uuid is missing.")

    if kind is None:
        return (False, "Parameter kind is missing.")

    if kind not in ["web", "mail", "other"]:
        return (False, "Parameter kind is invalid.")

    if is_valid is None:
        return (False, "Parameter is_valid is missing.")
    
    if is_valid != "true" and is_valid != "false":
        return (False, "Parameter is_valid is invalid.")

    return (True, "")


def handle(db: Dict[str, TinyDB], uuid: str, kind: str, is_valid: bool) -> Tuple[bool, Union[Case, str]]:
    query: Query = Query()
    _db: TinyDB

    if kind == "web":
        if is_valid:
            _db = db["webvalid"]
        else:
            _db = db["web"]

    if kind == "mail":
        if is_valid:
            _db = db["mailvalid"]
        else:
            _db = db["mail"]

    if kind == "other":
        if is_valid:
            _db = db["othervalid"]
        else:
            _db = db["other"]

    case: List[Case] = _db.search(query.uuid == uuid)

    if len(case) == 1:
        return True, case
    else:
        return False, "Not found."