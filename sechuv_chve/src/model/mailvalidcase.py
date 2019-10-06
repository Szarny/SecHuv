from typing import List

from mailspec import MailSpec

class MailValidCase:
    def __init__(self, 
                 id: str,
                 post_date: str,
                 spec: MailSpec) -> None:
        self.id: str = id
        self.post_date: str = post_date
        self.spec: MailSpec = spec