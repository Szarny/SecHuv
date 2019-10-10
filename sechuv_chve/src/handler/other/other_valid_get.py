from typing import List, Dict

from tinydb import TinyDB

from model.othervalidcase import OtherValidCase


def handle(db: Dict[str, TinyDB], length: int) -> List[OtherValidCase]:
    other_valid_cases: List[OtherValidCase] = db["othervalid"].all()
    
    if length == -1:
        return other_valid_cases

    else:
        return other_valid_cases[:length]