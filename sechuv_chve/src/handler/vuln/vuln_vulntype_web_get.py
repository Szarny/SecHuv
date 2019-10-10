from typing import Dict, List, Tuple, Union

from tinydb import TinyDB, Query

from model.webcase import WebCase
from model.vulnerability import Vulnerability


def validation(db: TinyDB, vulntype: str) -> Tuple[bool, str]:
    query: Query = Query()

    vulnerability: List[Vulnerability] = db["vulnerability"].search(query.vulntype == vulntype)

    if len(vulnerability) == 1:
        return (True, "")
    else:
        return (False, "Not found.")


def handle(db: Dict[str, TinyDB], length: int, vulntype: str) -> Dict[str, Union[Vulnerability, List[WebCase]]]:
    query: Query = Query()
    
    vulnerability: Vulnerability = db["vulnerability"].search(query.vulntype == vulntype)[0]
    web_cases: List[WebCase] = db["web"].search(query.vulns.vulntype.any(vulntype))

    result: Dict[str, Union[Vulnerability, List[WebCase]]]

    if length == -1:
        result = {
            "vulnerability": vulnerability,
            "cases": web_cases
        }
    else:
        result = {
            "vulnerability": vulnerability,
            "cases": web_cases[:length]
        }

    return result