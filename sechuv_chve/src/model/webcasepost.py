from typing import List

from .vulnerability import Vulnerability
from .webspec import WebSpec

class WebCasePost:
    def __init__(self, 
                 vulns: List[Vulnerability], 
                 spec: WebSpec) -> None:
        self.vulns: List[Vulnerability] = vulns
        self.spec: WebSpec = spec
