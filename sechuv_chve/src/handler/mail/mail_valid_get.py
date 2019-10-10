from typing import List, Dict

from tinydb import TinyDB

from model.mailvalidcase import MailValidCase


def handle(db: Dict[str, TinyDB], length: int) -> List[MailValidCase]:
    mail_valid_cases: List[MailValidCase] = db["mailvalid"].all()
    
    if length == -1:
        return mail_valid_cases

    else:
        return mail_valid_cases[:length]