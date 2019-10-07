from typing import List

from .mailspec import MailSpec

class MailValidCase:
    def __init__(self, 
                 uuid: str,
                 post_date: str,
                 spec: MailSpec) -> None:
        self.uuid: str = uuid
        self.post_date: str = post_date
        self.spec: MailSpec = spec