from typing import Dict, List

from tinydb import TinyDB

from model.webcase import WebCase


def handle(db: Dict[str, TinyDB], length: int) -> List[WebCase]:
    web_cases: List[WebCase] = db["web"].all()
    
    if length == -1:
        return web_cases

    else:
        return web_cases[:length]