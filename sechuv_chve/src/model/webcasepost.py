from typing import List

from model.vulnerability import Vulnerability
from model.webspec import WebSpec

class WebCasePost:
    def __init__(self, 
                 vulns: List[Vulnerability], 
                 spec: WebSpec) -> None:
        self.vulns: List[Vulnerability] = vulns
        self.spec: WebSpec = spec
