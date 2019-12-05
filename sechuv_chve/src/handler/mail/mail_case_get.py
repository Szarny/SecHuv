from typing import Dict, List

from tinydb import TinyDB

from model.mailcase import MailCase


def handle(db: Dict[str, TinyDB], length: int) -> List[MailCase]:
    mail_cases: List[MailCase] = db["mail"].all()
    
    if length == -1:
        return mail_cases

    else:
        return mail_cases[:length]