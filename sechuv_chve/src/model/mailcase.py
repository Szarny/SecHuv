from typing import List

from .vulnerability import Vulnerability
from .mailspec import MailSpec

class MailCase:
    def __init__(self, 
                 id: str,
                 post_date: str,
                 vulns: List[Vulnerability],
                 spec: MailSpec) -> None:
        self.id: str = id
        self.post_date: str = post_date
        self.vulns: List[Vulnerability] = vulns
        self.spec: MailSpec = spec