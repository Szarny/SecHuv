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


def handle(db: Dict[str, TinyDB], length: int, vulntype: str) -> List[WebCase]:
    query: Query = Query()
    
    web_cases: List[WebCase] = db["web"].search(query.vulns.vulntype.any(vulntype))

    if length == -1:
        return web_cases
    else:
        return web_cases[:length]