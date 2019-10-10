from typing import Dict, List

from tinydb import TinyDB

from model.othercase import OtherCase


def handle(db: Dict[str, TinyDB], length: int) -> List[OtherCase]:
    other_cases: List[OtherCase] = db["other"].all()
    
    if length == -1:
        return other_cases

    else:
        return other_cases[:length]