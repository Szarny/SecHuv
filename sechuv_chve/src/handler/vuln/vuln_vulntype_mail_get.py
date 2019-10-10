from typing import Dict, List, Tuple, Union

from tinydb import TinyDB, Query

from model.mailcase import MailCase
from model.vulnerability import Vulnerability


def validation(db: TinyDB, vulntype: str) -> Tuple[bool, str]:
    query: Query = Query()

    vulnerability: List[Vulnerability] = db["vulnerability"].search(query.vulntype == vulntype)

    if len(vulnerability) == 1:
        return (True, "")
    else:
        return (False, "Not found.")


def handle(db: Dict[str, TinyDB], length: int, vulntype: str) -> Dict[str, Union[Vulnerability, List[MailCase]]]:
    query: Query = Query()
    
    vulnerability: Vulnerability = db["vulnerability"].search(query.vulntype == vulntype)[0]
    mail_cases: List[MailCase] = db["mail"].search(query.vulns.vulntype.any(vulntype))

    result: Dict[str, Union[Vulnerability, List[MailCase]]]

    if length == -1:
        result = {
            "vulnerability": vulnerability,
            "cases": mail_cases
        }
    else:
        result = {
            "vulnerability": vulnerability,
            "cases": mail_cases[:length]
        }

    return result