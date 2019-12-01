from typing import List, Dict

from tinydb import TinyDB

from model.webvalidcase import WebValidCase


def handle(db: Dict[str, TinyDB], length: int) -> List[WebValidCase]:
    web_valid_cases: List[WebValidCase] = db["webvalid"].all()
    
    if length == -1:
        return web_valid_cases

    else:
        return web_valid_cases[:length]