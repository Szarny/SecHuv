from typing import List

from .vulnerability import Vulnerability
from .mailspec import MailSpec

class MailCasePost:
    def __init__(self, 
                 vulns: List[Vulnerability],
                 spec: MailSpec) -> None:
        self.vulns: List[Vulnerability] = vulns
        self.spec: MailSpec = spec