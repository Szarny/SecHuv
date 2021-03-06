from typing import Dict, List, Tuple, Union, Any

from tinydb import TinyDB, Query

from model.webcase import WebCase
from model.mailcase import MailCase
from model.othercase import OtherCase
from model.vulnerability import Vulnerability


def validation(db: TinyDB, vulntype: str) -> Tuple[bool, str]:
    query: Query = Query()

    vulnerability: List[Vulnerability] = db["vulnerability"].search(query.vulntype == vulntype)

    if len(vulnerability) == 1:
        return (True, "")
    else:
        return (False, "Not found.")


def handle(db: Dict[str, TinyDB], length: int, vulntype: str) -> Dict[str, Union[List[WebCase], List[MailCase], List[OtherCase]]]:
    query: Query = Query()
    
    web_cases: List[WebCase] = db["web"].search(query.vulntypes.any([vulntype]))
    mail_cases: List[MailCase] = db["mail"].search(query.vulntypes.any([vulntype]))
    other_cases: List[OtherCase] = db["other"].search(query.vulntypes.any([vulntype]))

    if length == -1:
        return {
            "web": web_cases,
            "mail": mail_cases,
            "other": other_cases
        }
    else:
        return {
            "web": web_cases[:length],
            "mail": mail_cases[:length],
            "other": other_cases[:length]
        }