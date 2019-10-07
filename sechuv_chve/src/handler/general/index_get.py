from typing import Dict, List

from tinydb import TinyDB

from model.case import Case
from model.webcase import WebCase
from model.mailcase import MailCase
from model.othercase import OtherCase


def handle(db: Dict[str, TinyDB], length: int) -> Dict[str, List[Case]]:
    webcases: List[WebCase] = db["web"].all()
    mailcases: List[MailCase] = db["mail"].all()
    othercases: List[OtherCase] = db["other"].all()
    
    if length == -1:
        cases: Dict[str, List[Case]] = {
            "web": webcases,
            "mail": mailcases,
            "other": othercases
        }

    else:
        cases: Dict[str, List[Case]] = {
            "web": webcases[:length],
            "mail": mailcases[:length],
            "other": othercases[:length]
        }
    
    return cases