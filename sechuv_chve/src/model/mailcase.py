from typing import List

from model.case import Case
from model.vulnerability import Vulnerability
from model.mailspec import MailSpec

class MailCase(Case):
    def __init__(self, 
                 uuid: str,
                 post_date: str,
                 vulns: List[Vulnerability],
                 spec: MailSpec) -> None:
        self.uuid: str = uuid
        self.post_date: str = post_date
        self.vulns: List[Vulnerability] = vulns
        self.spec: MailSpec = spec