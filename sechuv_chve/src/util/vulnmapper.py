from tinydb import TinyDB, Query
from typing import List, Dict, Tuple

from model.vulnerability import Vulnerability

def map_vulntype_to_vuln(db: Dict[str, TinyDB], vulntypes: List[str]) -> Tuple[bool, List[Vulnerability]]:
    return (True, [])
    # TODO: 脆弱性の対応付けができたら外す
    # query: Query = Query()

    # vulns: List[Vulnerability] = []

    # print(vulntypes)
    # for vulntype in vulntypes:
    #     v: List[Vulnerability] = db["vulnerability"].search(query.vulntype == vulntype)

    #     if len(v) == 1:
    #         vulns.append(v[0])
    #     else:
    #         return (False, [])

    # return (True, vulns)