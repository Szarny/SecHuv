from tinydb import TinyDB, Query
from typing import List, Dict, Tuple

from model.vulnerability import Vulnerability

def check_corresponding_vuln(db: Dict[str, TinyDB], vulntypes: List[str]) -> bool:
    query: Query = Query()

    vulns: List[Vulnerability] = []

    # テストデータ用
    if len(vulntypes) == 0:
        return True

    for vulntype in vulntypes:
        v: List[Vulnerability] = db["vulnerability"].search(query.vulntype == vulntype)

        if len(v) == 1:
            return True
        else:
            return False