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


def handle(db: Dict[str, TinyDB], length: int, vulntype: str) -> List[MailCase]:
    query: Query = Query()
    
    mail_cases: List[MailCase] = db["mail"].search(query.vulns.vulntype.any(vulntype))

    if length == -1:
        return mail_cases
    else:
        return mail_cases[:length]