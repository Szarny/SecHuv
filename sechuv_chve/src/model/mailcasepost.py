from typing import List

from model.vulnerability import Vulnerability
from model.mailspec import MailSpec

class MailCasePost:
    def __init__(self, 
                 vulns: List[Vulnerability],
                 spec: MailSpec) -> None:
        self.vulns: List[Vulnerability] = vulns
        self.spec: MailSpec = spec