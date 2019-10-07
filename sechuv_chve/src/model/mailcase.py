from typing import List

from .vulnerability import Vulnerability
from .mailspec import MailSpec

class MailCase:
    def __init__(self, 
                 uuid: str,
                 post_date: str,
                 vulns: List[Vulnerability],
                 spec: MailSpec) -> None:
        self.uuid: str = uuid
        self.post_date: str = post_date
        self.vulns: List[Vulnerability] = vulns
        self.spec: MailSpec = spec