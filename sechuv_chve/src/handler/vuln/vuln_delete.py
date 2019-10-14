from typing import Dict, List, Tuple, Union

from tinydb import TinyDB, Query

from model.webcase import WebCase
from model.mailcase import MailCase
from model.othercase import OtherCase
from model.vulnerability import Vulnerability


def validation(vulntype: str) -> Tuple[bool, str]:
    if vulntype is None:
        return (False, "Parameter vulntype is missing.")

    return (True, "")


def handle(db: Dict[str, TinyDB], vulntype: str) -> Tuple[bool, str]:
    query: Query = Query()

    vulnerability: List[Vulnerability] = db["vulnerability"].search(query.vulntype == vulntype)

    if len(vulnerability) == 1:
        db["vulnerability"].remove(query.vulntype == vulntype)

        for kind in ["web", "mail", "other"]:
            cases: List[Union[WebCase, MailCase, OtherCase]] = db[kind].search(query.vulns.vulntype.any(vulntype))
            
            for case in cases:
                for vi in range(len(case["vulns"])):
                    if case["vulns"][vi]["vulntype"] == vulntype:
                        case["vulns"].pop(vi)
                        break

            db[kind].write_back(cases)

        return (True, "")
        
    else:
        return (False, "Not found.")