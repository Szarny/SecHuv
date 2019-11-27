from typing import Dict, List, Tuple, Union

from tinydb import TinyDB, Query

from model.othercase import OtherCase
from model.vulnerability import Vulnerability


def validation(db: TinyDB, vulntype: str) -> Tuple[bool, str]:
    query: Query = Query()

    vulnerability: List[Vulnerability] = db["vulnerability"].search(query.vulntype == vulntype)

    if len(vulnerability) == 1:
        return (True, "")
    else:
        return (False, "Not found.")


def handle(db: Dict[str, TinyDB], length: int, vulntype: str) -> List[OtherCase]:
    query: Query = Query()
    
    other_cases: List[OtherCase] = db["other"].search(query.vulns.vulntype.any(vulntype))

    if length == -1:
        return other_cases
    else:
        return other_cases[:length]