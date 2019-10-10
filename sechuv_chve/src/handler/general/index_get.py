from typing import Dict, List

from tinydb import TinyDB

from model.case import Case
from model.webcase import WebCase
from model.mailcase import MailCase
from model.othercase import OtherCase


def handle(db: Dict[str, TinyDB], length: int) -> Dict[str, List[Case]]:
    web_cases: List[WebCase] = db["web"].all()
    mail_cases: List[MailCase] = db["mail"].all()
    other_cases: List[OtherCase] = db["other"].all()
    
    if length == -1:
        cases: Dict[str, List[Case]] = {
            "web": web_cases,
            "mail": mail_cases,
            "other": other_cases
        }

    else:
        cases: Dict[str, List[Case]] = {
            "web": web_cases[:length],
            "mail": mail_cases[:length],
            "other": other_cases[:length]
        }
    
    return cases