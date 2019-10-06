from typing import List

from vulnerability import Vulnerability
from otherspec import OtherSpec

class OtherCasePost:
    def __init__(self, 
                 vulns: List[Vulnerability], 
                 spec: OtherSpec) -> None:
        self.vulns: List[Vulnerability] = vulns
        self.spec: OtherSpec = spec
