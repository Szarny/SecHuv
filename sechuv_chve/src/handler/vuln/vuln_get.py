from typing import Dict, List

from tinydb import TinyDB

from model.vulnerability import Vulnerability


def handle(db: Dict[str, TinyDB]) -> List[Vulnerability]:
    vulnerabilities: List[Vulnerability] = db["vulnerability"].all()

    return vulnerabilities